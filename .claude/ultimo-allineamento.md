# Ultimo allineamento dal template

<!-- generato da allinea-dal-template.py -->

Commit a monte: `2ba5943c0fcb1d4cce94285e209e160974eb6767`. File interessati dalla passata: 38. Commit e push del progetto restano manuali.

| Esito | File |
|---|---|
| NUOVO | `.claude/rules/artefatti-temporanei.md` |
| NUOVO | `.claude/skills/analisi-codice/SKILL.md` |
| VECCHIO | `.claude/skills/gate-pacchetti/SKILL.md` |
| VECCHIO | `.claude/skills/init-project-system/SKILL.md` |
| MERGE | `.claude/templates/PACKAGES.md` |
| VECCHIO | `.claude/templates/agenti-terminale/README.md` |
| VECCHIO | `.claude/templates/agenti-terminale/codex-agents.riferimento.md` |
| NUOVO | `.claude/templates/agenti-terminale/tests/test-temporanei-agenti.ps1` |
| VECCHIO | `.claude/templates/agenti-terminale/tools/Installa-Claude.ps1` |
| VECCHIO | `.claude/templates/agenti-terminale/tools/Pulisci-Codex.ps1` |
| VECCHIO | `.claude/templates/alignment/README.md` |
| VECCHIO | `.claude/templates/alignment/tools/Test-Allineamento.py` |
| NUOVO | `.claude/templates/analisi-codice/README.md` |
| NUOVO | `.claude/templates/analisi-codice/analisi-codice.esempio.json` |
| NUOVO | `.claude/templates/analisi-codice/assets/documento.css` |
| NUOVO | `.claude/templates/analisi-codice/tools/documento-estrai.py` |
| NUOVO | `.claude/templates/analisi-codice/tools/documento-genera.py` |
| NUOVO | `.claude/templates/analisi-codice/tools/dove-usato.py` |
| NUOVO | `.claude/templates/analisi-codice/tools/ricerca.py` |
| NUOVO | `.claude/templates/analisi-codice/tools/sorgenti.py` |
| VECCHIO | `.claude/templates/comandi-ragionamento/skills/artefatto/SKILL.md` |
| VECCHIO | `.claude/templates/fix-typography/tools/fix-dashes.py` |
| VECCHIO | `.claude/templates/fix-typography/tools/test-tipografia.py` |
| VECCHIO | `.claude/templates/fonti-a-monte.json` |
| VECCHIO | `.claude/templates/fonti-a-monte.md` |
| VECCHIO | `.claude/templates/lezioni-recepite.json` |
| VECCHIO | `.claude/templates/riferimento-voci.json` |
| MERGE | `.claude/templates/tools/README.md` |
| VECCHIO | `.claude/templates/tools/allinea-dal-template.py` |
| VECCHIO | `.claude/templates/tools/check-raggiungibilita.py` |
| VECCHIO | `.claude/templates/tools/chiudi-allineamento.ps1` |
| VECCHIO | `.claude/templates/tools/session-end-wipe.ps1` |
| VECCHIO | `.claude/templates/tools/stato-template.py` |
| VECCHIO | `.claude/templates/tools/test-agenti-terminale.py` |
| VECCHIO | `.claude/templates/tools/tests/test_gate_dovuto.py` |
| VECCHIO | `.claude/templates/tools/verifica-pacchetti.py` |
| NUOVO | `.claude/templates/tools/wipe-temporanei-perimetro.ps1` |
| VECCHIO | `tools/fix-dashes.py` |

Conflitti ancora da risolvere: 0.

## Gate dei pacchetti

Gate dovuto: 106 voci del catalogo su 106 non sono mai state viste dal gate né decise (nessuna tornata registrata). La tornata la avvia /riprendi, oppure /gate-pacchetti.

La riga si ricalcola in ogni momento con `python .claude/templates/tools/verifica-pacchetti.py --gate`. Una tornata dovuta si dice al proprietario nella prima risposta della sessione, perché l'agente non può lanciare `/gate-pacchetti` da sé.

Voci mai viste: `academic-researcher`, `academix`, `agent-catalog`, `agenti-terminale`, `alignment`, `anatomy`, `andrej-karpathy-skills`, `anki-mcp`, `anonymization`, `anti-slop`, `arxiv-cli`, `automation-starter`, `blender-skills`, `book-bib-extract`, `book-to-skill`, `caveman`, `ccusage`, `claude-code-handoff`, `claude-code-router`, `claude-mem`, `code-context`, `code-simplifier`, `codebase-learning`, `codebase-memory-mcp`, `comandi-ragionamento`, `community-sources`, `context-mode`, `context7`, `craft-apps`, `cyber-lab`, `deepwiki-mcp`, `deepwiki-skill`, `dev-skills`, `diagram-design`, `diagrams`, `discord-mcp`, `doc-ingest`, `documentazione-didattica`, `docx-to-docs`, `drawio-skill`, `feynman`, `figma-mcp`, `fix-typography`, `gancio-globale`, `github-mcp`, `graphify`, `grc-skills`, `grobid`, `guardia-pubblicazione`, `hallmark`, `headroom`, `hermes-agent`, `hooks-starter`, `humanizer`, `impeccable`, `instradamento-modelli`, `knowledge-mcp`, `knowledge-wiki`, `latex`, `lavoro-a-lotti`, `learning-agent`, `linear-mcp`, `llm-local`, `matt-pocock-skills`, `md-unwrap`, `memoria-di-progetto`, `micro-passi`, `mods-claude-code`, `multiclaude`, `nimbalyst`, `notebooklm-bridge`, `openalex`, `operations-log`, `paperqa2`, `pipeline-app`, `playwright-mcp`, `ponytail`, `psmux`, `rea`, `readme-sync`, `refchecker-mcp`, `repomix`, `roadmap`, `rtk`, `scientific-skills`, `security-audit`, `semantic-scholar-mcp`, `sentry-mcp`, `serena`, `stack-profiles`, `stratega-impresa`, `subagent-template`, `superpowers`, `taste-skill`, `timeline-progetto`, `tmux-claude-hatch`, `vault-di-progetto`, `veeam-linux`, `vercel-mcp`, `verifica-link`, `voicestudio`, `voicestudio-mcp`, `voltagent-subagents`, `vps-baseline`, `wshobson-agents`, `zotero-mcp`.
