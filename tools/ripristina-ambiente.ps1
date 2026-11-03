# Ripristina su una macchina Windows tutto cio' che serve agli strumenti del progetto, e lo verifica.
#
# Perche' esiste. Il 2026-11-03 il proprietario ha chiesto che ogni strumento del progetto sia ripristinabile su
# questa macchina e su qualunque macchina Windows su cui il progetto si sposti. Fino a quel giorno non lo era: i
# venti strumenti tools\pkhex-* puntano a una libreria compilata dentro _notes\, che Git esclude, le dipendenze
# Python non erano scritte da nessuna parte, e l'hook di apertura porta il percorso assoluto della radice.
#
# Che cosa fa, in ordine. Controlla i programmi di sistema (git, Python 3.11 o piu', SDK .NET della versione
# fissata, e come facoltativi gh e ffmpeg). Installa le dipendenze Python di tools\requirements.txt. Ricrea il clone
# di PKHeX alla versione di tools\pkhex-versione.txt, se manca o e' a un'altra versione, e ne compila PKHeX.Core.
# Compila tutti gli strumenti tools\pkhex-*. Riporta il percorso dell'hook di .claude\settings.json alla radice
# corrente. Esegue le prove interne degli strumenti che ne hanno. Alla fine stampa un esito per passo ed esce con
# 1 se uno e' fallito.
#
# Che cosa non fa. Non ripristina i dati privati di _notes\, cioe' salvataggi, lotti, copie per HOME e fonti
# scaricate: quelli non sono in Git per decisione (ADR-005) e tornano dal backup. Non installa i programmi di
# sistema: dice quale manca e con quale comando lo si installa.
#
# Uso:  powershell -NoProfile -ExecutionPolicy Bypass -File tools\ripristina-ambiente.ps1 [-SoloVerifica]
#       -SoloVerifica controlla e prova senza installare, clonare o compilare nulla.

param([switch]$SoloVerifica)

$ErrorActionPreference = "Continue"
$radice = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
Set-Location $radice
$esiti = New-Object System.Collections.Generic.List[string]
$falliti = 0

function Esito([string]$passo, [bool]$ok, [string]$nota) {
    $marca = if ($ok) { "ok" } else { "KO" }
    if (-not $ok) { $script:falliti++ }
    $script:esiti.Add(("   {0}  {1}{2}" -f $marca, $passo, $(if ($nota) { ": " + $nota } else { "" })))
}

function Comando([string]$nome) { return [bool](Get-Command $nome -ErrorAction SilentlyContinue) }

Write-Output "== Ripristino dell'ambiente in $radice"
if ($SoloVerifica) { Write-Output "   modo: sola verifica, niente viene installato o compilato" }

# 1. Programmi di sistema.
$okGit = Comando "git"
Esito "git" $okGit $(if ($okGit) { "" } else { "manca: winget install Git.Git" })
$py = $null
if (Comando "python") {
    $v = (& python -c "import sys;print('%d.%d' % sys.version_info[:2])") 2>$null
    if ($v -and [version]$v -ge [version]"3.11") { $py = "python" }
    Esito "Python 3.11 o piu'" ([bool]$py) ("trovato " + $v)
} else { Esito "Python 3.11 o piu'" $false "manca: winget install Python.Python.3.13" }

$pkhex = @{}
Get-Content "tools\pkhex-versione.txt" | Where-Object { $_ -match "^[a-z]+=" } | ForEach-Object {
    $k, $val = $_ -split "=", 2; $pkhex[$k] = $val.Trim()
}
$sdkOk = $false
if (Comando "dotnet") {
    $sdk = & dotnet --list-sdks 2>$null
    $sdkOk = [bool]($sdk | Where-Object { $_ -match ("^" + $pkhex["dotnet"] + "\.") })
}
Esito (".NET SDK " + $pkhex["dotnet"]) $sdkOk $(if ($sdkOk) { "" } else { "manca: winget install Microsoft.DotNet.SDK." + $pkhex["dotnet"] })
if (-not (Comando "gh")) { Write-Output "   avviso: gh assente; serve agli strumenti che leggono GitHub con autenticazione (winget install GitHub.cli)" }
if (-not (Comando "ffmpeg")) { Write-Output "   avviso: ffmpeg assente; serve a tools\trascrivi-video-cpu.py (winget install Gyan.FFmpeg)" }

# 2. Dipendenze Python.
if ($py) {
    if (-not $SoloVerifica) {
        & python -m pip install --user --quiet -r tools\requirements.txt
        Esito "dipendenze Python" ($LASTEXITCODE -eq 0) "tools\requirements.txt"
    } else {
        $mancanti = @()
        Get-Content tools\requirements.txt | Where-Object { $_ -match "^[A-Za-z]" } | ForEach-Object {
            $nome, $ver = $_ -split "==", 2
            $installata = (& python -m pip show $nome 2>$null | Select-String "^Version:").ToString() -replace "Version:\s*", ""
            if ($installata -ne $ver) { $mancanti += ("{0} (richiesta {1}, installata {2})" -f $nome, $ver, $(if ($installata) { $installata } else { "nessuna" })) }
        }
        Esito "dipendenze Python" ($mancanti.Count -eq 0) ($mancanti -join "; ")
    }
}

# 3. Clone di PKHeX alla versione fissata, e la libreria compilata.
$clone = Join-Path $radice "_notes\fonti\cloni\pkhex"
$testa = if (Test-Path (Join-Path $clone ".git")) { (& git -C $clone rev-parse HEAD 2>$null) } else { $null }
if ($testa -ne $pkhex["commit"] -and -not $SoloVerifica) {
    if (-not $testa) {
        New-Item -ItemType Directory -Force -Path (Split-Path $clone) | Out-Null
        & git clone --quiet --depth 1 --branch $pkhex["tag"] $pkhex["repository"] $clone
    } else {
        & git -C $clone fetch --quiet --depth 1 origin tag $pkhex["tag"]
        & git -C $clone checkout --quiet $pkhex["tag"]
    }
    $testa = (& git -C $clone rev-parse HEAD 2>$null)
}
Esito ("clone di PKHeX " + $pkhex["tag"]) ($testa -eq $pkhex["commit"]) ("testa " + $(if ($testa) { $testa.Substring(0, 7) } else { "assente" }))
$dll = Join-Path $clone ("PKHeX.Core\bin\Release\net" + $pkhex["dotnet"] + ".0\PKHeX.Core.dll")
if ($sdkOk -and $testa -eq $pkhex["commit"] -and -not $SoloVerifica) {
    & dotnet build (Join-Path $clone "PKHeX.Core") -c Release -v q -nologo | Out-Null
}
Esito "PKHeX.Core compilata" (Test-Path $dll) $dll.Substring($radice.Length + 1)

# 4. Gli strumenti tools\pkhex-*.
$progetti = Get-ChildItem tools -Directory -Filter "pkhex-*" | ForEach-Object { Join-Path $_.FullName ($_.Name + ".csproj") } | Where-Object { Test-Path $_ }
$rotti = @()
foreach ($p in $progetti) {
    if ($SoloVerifica) {
        $nome = [IO.Path]::GetFileNameWithoutExtension($p)
        if (-not (Get-ChildItem (Join-Path (Split-Path $p) "bin\Release") -Recurse -Filter ($nome + ".dll") -ErrorAction SilentlyContinue)) { $rotti += $nome }
    } elseif ($sdkOk) {
        & dotnet build $p -c Release --no-incremental -v q -nologo | Out-Null
        if ($LASTEXITCODE -ne 0) { $rotti += [IO.Path]::GetFileNameWithoutExtension($p) }
    }
}
Esito ("strumenti pkhex-* (" + $progetti.Count + ")") ($rotti.Count -eq 0 -and $sdkOk) ($rotti -join ", ")

# 5. Percorso dell'hook di apertura.
$impostazioni = Join-Path $radice ".claude\settings.json"
$testo = [IO.File]::ReadAllText($impostazioni)
$atteso = ($radice -replace "\\", "/") + "/tools/controlla-eventi-nuovi.py"
$nuovo = [regex]::Replace($testo, 'python \\"[^"\\]*/tools/controlla-eventi-nuovi\.py\\"', ('python \"' + $atteso + '\"'))
if ($nuovo -ne $testo -and -not $SoloVerifica) {
    [IO.File]::WriteAllText($impostazioni, $nuovo, (New-Object System.Text.UTF8Encoding($false)))
    $testo = $nuovo
}
Esito "hook di apertura sulla radice corrente" ($testo.Contains($atteso)) $atteso

# 6. Prove interne.
if ($py) {
    foreach ($prova in @(@("tools\controlla-eventi-nuovi.py", "--autotest"), @("tools\conta-letti.py", "--prova"), @("tools\check-visibilita.py", "--autotest"))) {
        if (Test-Path $prova[0]) {
            & python $prova[0] $prova[1] | Out-Null
            Esito ("prove di " + (Split-Path $prova[0] -Leaf)) ($LASTEXITCODE -eq 0) ""
        }
    }
}

Write-Output ""
$esiti | ForEach-Object { Write-Output $_ }
Write-Output ""
Write-Output "I dati privati di _notes\ (salvataggi, lotti, copie per HOME, fonti scaricate) non sono in Git: tornano dal backup."
if ($falliti -gt 0) { Write-Output ("Passi falliti: " + $falliti + "."); exit 1 }
Write-Output "Ambiente pronto."
exit 0
