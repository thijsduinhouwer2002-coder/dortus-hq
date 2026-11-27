# Broncode: ND (Non-Destructive), Blender-add-on van HugeMenace

Uitgeplozen door de Afkijker, vr 27 nov 2026 ±15:30 NL (issue #20). Code gelezen met `git clone --depth 1` in /tmp, niets uitgevoerd, daarna weggegooid.

## Wie en hoeveel
- Repo: https://github.com/hugemenace/nd, laatste commit 23 jul 2026 ("chore(release): 2.2.1"), ±17.600 regels Python (GEZIEN `git log`, `wc -l`). Twee makers (Tristan S. en Ian J.).
- Licentie: GPL-3.0-or-later (GEZIEN `LICENSE` en `blender_manifest.toml`). Dus alleen ideeën overnemen, geen code.
- **Zelfde add-on op drie plekken, gratis én betaald:**
  - extensions.blender.org gratis: 114.986 downloads, 140 reviews, gemiddeld 5,0, sinds 21 apr 2024 (GEZIEN, https://extensions.blender.org/add-ons/nd/).
  - Gumroad betaal wat je wilt, maar met een **ondergrens van A$20** (±$13,32) en A$20 voorgesteld: 549 beoordelingen, gemiddeld 4,9 (96% vijf sterren, 4% vier, 0 lager) (GEZIEN in de paginadata, https://hugemenace.gumroad.com/l/nd-blender-addon). Aantal verkopen toont Gumroad niet.
  - Superhive $15 vast: "Sales 700+", 4 beoordelingen gemiddeld 5 (GEZIEN, https://superhivemarket.com/products/nd-addon).
  - GitHub: 139 sterren, 49 open issues (GEZIEN via img.shields.io). Het geld zit dus niet in GitHub maar in Extensions als ingang.
- Ruwe omzetting: 700+ op Superhive plus minstens 549 op Gumroad (wie beoordeelt, heeft betaald) tegen 115k gratis downloads is ±1,1% die betaalt (GOK, ondergrens). SnapSplit: 30+ verkopen tegen 2.037 gratis downloads, ±1,5% (GEZIEN, `snapsplit.md`). **Zelfde verhouding: het verschil zit in het bereik op Extensions, niet in de prijs.**

## Wat ze slim doen (bestand en regels)
1. **Betalen heet steunen, en de gratis weg staat er eerlijk bij.** Eerste zin op Gumroad én Superhive: "Gumroad is now an official way to support ND's ongoing development through a one-time donation", direct daarna "Looking to download ND for free? ... grab it from the official Blender Extensions page" (GEZIEN, beide pagina's). Samenvatting naast de koopknop: "You can use ND for both personal & commercial projects and will have access to all future updates." Geen druk in de add-on zelf: geen koopknop of steunlink in het paneel, alleen `doc_url` naar de handleiding (GEZIEN, grep op gumroad, patreon en url_open in `interface/` en `__init__.py`: niets).
2. **Snelmenu dat raadt wat je wilt.** `interface/fast_menu.py` r. 47 tot 61: één toets, en het menu toont alleen wat past bij wat je nu geselecteerd hebt: niets geselecteerd, één object, twee objecten (r. 116 tot 139: Difference, Union, Slice, Mirror, Snap align), meer dan twee, of bewerkmodus. Past niets: "No predictions available". De versie staat in de kop ("Fast Menu, ND v2.2.1").
3. **Waarden naast de muis tijdens een handeling.** `lib/overlay.py` r. 33 tot 120 en r. 135 tot 290: zolang een handeling loopt, tekent ND bij de cursor een kopje met de naam, elke instelling met zijn toets ernaast, en een hint onderaan; vastpinnen op één plek kan (`toggle_pin_overlay`, r. 66 tot 76) en wordt onthouden. Getallen typ je gewoon in (`lib/numeric_input.py`, cijfers, min, punt, backspace), de muis loopt aan de rand door naar de andere kant (`wrap_cursor`).
4. **Changelog die de koper leest.** `CHANGELOG.md` per versie met "Features" en "Bug Fixes", en elke uitgave noemt de Blender-versie die het oplost ("fix ... for Blender 5.2+", 2.2.1). Op Extensions staat dat in de tab "What's New" (GEZIEN).
5. **Handleiding en filmpjes los van de winkel.** `website = "https://docs.nd.hugemenace.co/"` in het manifest; winkelpagina linkt naar docs, YouTube en Discord. Reviews noemen dat zelf: "i love the tutorials as well. they teach you a complete new mindset" en "I also love the deep dive videos" (GEZIEN, Extensions-reviews, 8 mnd geleden).

## Wat gebruikers zeggen of klagen
- Extensions, laatste 15 reviews alle 5 sterren (GEZIEN, https://extensions.blender.org/add-ons/nd/reviews/). Steeds terug: "feels so easy and intuitive" (iemand die van HardOps kwam), "Feels pretty much like it was made as part of Blender", "such an extension for free", "I have no idea what I am doing, nor why it is working... 5/5".
- Gumroad: geen enkele beoordeling onder 4 sterren (GEZIEN, percentages 0, 0, 0, 4, 96). De losse reviewteksten kon ik niet lezen: het opvragen van de reviewlijst werd in deze run geweigerd.
- GitHub-issues: niet leesbaar, de repo hugemenace/nd staat niet in de toegang van deze geplande run.

## Welke van onze producten er beter van wordt
- **Click Joints Pro (geld):** onze gratis Click Joints heeft 412 downloads op Extensions, 0 reviews, versie 0.1.1 (GEZIEN 27 nov 15:30, https://extensions.blender.org/add-ons/click-joints/). Bij ±1% omzetting is dat ±4 betalers (GOK); we hebben er 2 (bord). Wil Pro honderden verkopen, dan moet de gratis versie op Extensions eerst tienduizenden downloads halen: de gratis lijst, beelden en reviews daar zijn dus ook etalage van Pro. Dat versterkt gat 2 en 3 in de lat (gratis proberen bovenaan, beoordelingen) en de klaarstaande 0.1.2 (hoofdchat, nog niet geplakt).
- **Click Joints Pro, later (na de sale):** een snelmenu zoals punt 2: één toets, met twee onderdelen geselecteerd "Add joint between", met een rig geselecteerd "Joints from rig". Pas als de lat er een gat voor geeft; nu geen issue.
- **Click Cuts:** de waarden naast de muis (punt 3) passen bij de Draw cut van 1.1 (#208): tijdens het trekken de speling en het aantal delen bij de cursor, met de toets ernaast. Zelfde les als Bool Tool (statusbalk), nu sterker.
- **Winkeltekst van alle Blender-producten:** "personal & commercial use, all future updates" als één zin naast de koopknop (Gumroad-veld "summary"), zoals ND.

Geen nieuw issue: het geldpunt (bereik op Extensions) valt onder gat 2 en 3 van `organisatie/lat/click-joints-pro.md` en de 0.1.2 die al bij de hoofdchat klaarstaat.
