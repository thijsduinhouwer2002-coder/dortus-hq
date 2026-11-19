# Inventaris: wat leunt op de Pro-code (Bram, 19 nov 2026)

Doel: de Pro-code (`producten/blender-gewrichten/click_joints/betaald/`) uit de openbare repo halen, want nu kan iedereen Pro gratis pakken. **Niets verplaatst**, alleen geteld (grep op main, commit dfb59bf).

## De Pro-code zelf
- `producten/blender-gewrichten/click_joints/betaald/`: 15 .py-bestanden plus `iconen/` (figuur, rig, scharnier en zes scharnier-hulpen, afstand, snippers, een_lid_diep, figuur_ring, figuur_teken).
- `producten/blender-gewrichten/e2e/betaald/init_betaald.py`: registratie die `maak_zip.sh betaald` achter `__init__.py` plakt. Hoort mee.
- `producten/blender-gewrichten/e2e/maak_zip.sh`: tak `betaald` kopieert `click_joints/` inclusief `betaald/`.

## Workflows die de betaalde zip bouwen (`bash e2e/maak_zip.sh betaald`)
| Workflow | Wat | Gevolg als `betaald/` weg is |
|---|---|---|
| `blender-gewrichten-e2e.yml` | hoofdtest in 4.2.23, 5.2.3, 5.3.0; bouwt de Pro-zip (PRO_VERSIE 1.1.0), ±10 Pro-stappen, schermen 13 tot 19 | breekt, de grootste klus |
| `click-joints-pro-uitgave.yml` | haalt de Pro-zip uit een e2e-run en zet hem als artefact | breekt mee met e2e |
| `click-joints-pro-film.yml` | demofilm (film_pro.py) | breekt |
| `click-joints-pro-film-release.yml` | zet de film in een release | hangt aan de film |
| `youtube-pro-1.yml` | YouTube-opname Pro | breekt |
| `click-joints-render.yml`, `blender-chris-figuur.yml` | figuur voor Chris (maak_chris_figuur.py) | breekt |
| `click-joints-uitgave.yml` | gratis uitgave; controleert juist dat `betaald/` NIET in de zip zit | blijft werken |

## Tests en scripts in `producten/blender-gewrichten/e2e/` die Pro-modules laden
37 bestanden noemen `betaald`. De belangrijkste: `test_betaald.py`, `toets_zips.py` (gratis zonder Pro, betaald met Pro), alle `toetsen_scharnier*`, `toetsen_rig*`, `toetsen_figuur`, `toetsen_mens`, `toetsen_meshy_*`, `toetsen_neus*`, `toetsen_zwaai`, `toetsen_flip`, `toetsen_kijk`, `toetsen_vrije_stop`, `toetsen_print`, `toetsen_melden`, de schermen `scherm_pro`, `scherm_scharnier`, `scherm_figuur`, `scherm_rig`, `scherm_rig_armen`, `scherm_mens`, en de proeven `proef_*` en `film_pro.py`, `maak_chris_figuur.py`. Volledige lijst: `grep -l betaald producten/blender-gewrichten/e2e/*`.

## Wat er nog meer openbaar is
- **De hele git-geschiedenis.** Ook als `betaald/` van main gaat, staat elke oude versie in de geschiedenis van deze openbare repo. Verwijderen daaruit is geschiedenis herschrijven en geforceerd pushen, en dat is verboden (CLAUDE.md regel 6). Eerlijk: wat al openbaar was, blijft te vinden. Weghalen helpt wel voor de toekomst (1.2 en verder) en tegen toevallige vinders.
- **Releases:** geen enkele release heeft een Pro-zip (GEZIEN via de API 19 nov: `click-joints-pro-v1.0.1`, `-v1.0.2`, `-film-v1`, `youtube-pro-1` hebben geen zip). Goed.
- **Actions-artefacten** `click-joints-pro-zip-*`: in een openbare repo kan elke ingelogde GitHub-gebruiker ze downloaden (GOK op hoe GitHub werkt, niet nagekeken). Ze bewaren 3 dagen.
- **De GPL:** Pro is GPL-3.0-or-later. Een koper mag hem verder delen. Weghalen uit de repo is dus tegen gemak, niet tegen een recht.

## Voorstel voor de verhuizing (beslissing hoofdchat; geld kost het niet)
1. Nieuwe **private** repo `dortus-pro` (aanmaken kan alleen Thijs of een sessie met die rechten: op de lijst).
2. `betaald/`, `e2e/betaald/` en de Pro-tests daarheen; de Pro-workflows ook, met een checkout van de openbare repo voor het gratis deel.
3. In de openbare repo: `maak_zip.sh betaald` laten stoppen met een duidelijke melding, de Pro-stappen uit `blender-gewrichten-e2e.yml` halen (gratis blijft getest), `toets_zips.py` alleen nog de gratis kant.
4. Daarna pas `betaald/` van main weghalen. Volgorde andersom breekt de hoofdtest.
Schatting: één tot twee runs werk voor mij (GOK). Private repo's tellen Actions-minuten mee; op het gratis plan van GitHub zit daar een grens op (GOK, nagaan voor het gaat kosten).
