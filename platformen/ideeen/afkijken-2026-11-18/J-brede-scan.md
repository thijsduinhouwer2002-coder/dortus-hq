# J. Brede scan: 322 repo's op vaste punten (hoofdchat, 18 nov 2026)

**Wat:** per platform-topic (21 stuks) de populairste repo's met een push na 1 nov 2025 en meer dan 30 sterren (GitHub-zoek-API, sortering op sterren). Elk repo gekloond zonder inhoud en automatisch uitgelezen: workflows (naar welke winkel publiceren ze), README en FUNDING.yml (hoe vragen ze geld), AI-bestanden, beeld bovenaan, Discord, changelog, tests. Script: `scan/kies.py` en `scan/lees.py`, ruwe uitkomst `scan/resultaat.json`.

**Let op:** dit zijn de populairste *open* repo's, vooral gratis projecten. Commerciële winnaars houden hun code vaak dicht. Herkenning gaat met zoekpatronen: een winkel waar met de hand naar geüpload wordt, telt niet mee (daardoor scoren Chrome en Steam laag).

## Uitkomst (322 repo's)
| Punt | Aandeel |
|---|---|
| Heeft workflows (automatisch bouwen of uitbrengen) | 76% |
| Tests in de workflow | 55% |
| Echt beeld bovenaan de README (geen badge of logo) | 62%, bewegend (gif of film) 13% |
| Changelog-bestand | 52% |
| Docs-map los van de README | 44% |
| Discord gelinkt | 22% |
| **AI-bestand** (CLAUDE.md, AGENTS.md, .claude/, .cursor/, Copilot) | **37%** (AGENTS.md 98, CLAUDE.md 62, .claude/ 45) |
| Enige geldroute zichtbaar | 41%, vooral GitHub Sponsors (105) en Buy Me a Coffee (22) |
| Betaalde route (Pro, Gumroad, Polar, Superhive, Stripe) | 10% |
| Licentie | MIT 165, Apache 37, GPL 44, AGPL 13, geen of onduidelijk 50 |

Per platform het hoogst: AI-bestand bij mcp-server (75%), claude-code-plugin (65%), vscode-extension (55%). Betaalde route bij blender-addon (35%), claude-code-plugin (30%), telegram-mini-app (30%), wordpress-plugin (25%). Godot-spellen het laagst op alles (19% workflows, 6% AI).

## Wat dit zegt
- Automatisch uitbrengen met workflows is de norm (3 van de 4).
- Bij populaire open repo's verdient bijna niemand via de repo zelf: fooi is het meest, een betaalde versie zie je bij 1 op 10. Het geld zit elders (winkel, eigen site), zoals G en H al zagen.
- AGENTS.md is vaker dan CLAUDE.md: het werkt voor elke AI-tool, niet alleen Claude.
