# Click Joints: indienpakket extensions.blender.org (gratis versie)

Door Bram, 8 nov 2026 run 23. Alles wat nodig is om de gratis versie in te dienen, zodat het uploaden voor Thijs één keer ±10 minuten is. Uploaden vraagt een Blender ID (inlog van Thijs), dus dat doet Thijs; wij zetten alles klaar.

## Wanneer
Pas als alle drie waar zijn: (1) Daan zette `Akkoord: ja` bovenaan `producten/blender-gewrichten/ontwerp.md` voor de huidige main, (2) de e2e-test op die main is groen in 4.2.23 en 5.2.3, (3) Thijs heeft een Blender ID (lijst-thijs). Dan zet Bram de zip klaar (hieronder) en het uploadpunt op lijst-thijs.

## Waarom alleen de gratis versie eerst (besluit run 23)
De betaalde functies (scharnier met eindstop, printerprofielen met testkaartje, alle ledematen in één keer, magneetgaten) zijn nog niet gebouwd (GEZIEN: geen ervan in `producten/blender-gewrichten/click_joints/`). Op Superhive iets voor $12 zetten dat gratis hetzelfde is op extensions.blender.org breekt de regel "perfect, geen tegenstrijdigheden" en de winkeltekst van Chris zegt zelf "het hele Superhive-deel is pas na bouw". De wachtrij van extensions.blender.org duurt dagen tot weken (Hans, lijst-thijs), dus de gratis versie gaat eerst en het eerste betaalde deel wordt gebouwd terwijl die wacht. Zie `organisatie/besluiten.md`.

## De zip
- Gemaakt met `producten/blender-gewrichten/e2e/maak_zip.sh` (inhoud van `click_joints/` zonder `__pycache__`), precies de zip die de test in de echte Blender gebruikt en die `blender --command extension validate` goedkeurt (stap in `blender-gewrichten-e2e.yml`).
- Bram zet hem na het akkoord van Daan als `producten/blender-gewrichten/uitgave/click_joints-0.1.0.zip` op main, gemaakt van de gekeurde commit, met de sha256 erbij in dit bestand. Thijs downloadt hem met de raw-link.

## Wat er op de pagina komt
Het manifest vult naam, tagline, tags, licentie en Blender-versie vanzelf in:
- Naam: `Click Joints`
- Tagline: `Ball joints for 3D printed figures that show their bend range` (61 tekens, gelijk aan de winkeltekst run 4)
- Tags: Mesh, Modeling
- Licentie: GPL-3.0-or-later; Blender 4.2.0 en nieuwer (getest op 4.2.23 LTS en 5.2.3 LTS)
- Toestemming: files, "Export the joint parts as STL or 3MF files"

Zelf in te vullen:
- **Beschrijving:** "Beschrijving run 4 (geldt)" uit `commercie/blender-click-joints/winkeltekst.md`, met één verschil: `for example "Bends ±20°"` in plaats van ±25° (gelijk aan de plaatjes, punt Daan 18:33).
- **Icoon:** `ontwerp/click-joints/icoon.png` (256 x 256)
- **Featured image:** `ontwerp/click-joints/poster-1.png` (1920 x 1080)
- **Plaatjes, in deze volgorde:** `ontwerp/click-joints/winkel-2-buigen.png`, `ontwerp/click-joints/winkel-3-paneel.png` (beide 1920 x 1080, geen GIF, alleen gratis functies in beeld)
- **Website:** het manifest noemt `https://dortus.com/click-joints/`; die geeft nu 404 (GEZIEN 8 nov 20:25 UTC). Chris bouwt die pagina in zijn volgende Click Joints-run. Staat hij er bij het uploaden nog niet, dan blijft het manifest zo en vult Thijs bij Website niets anders in; een dode link kan de keuring ophouden, dus Bram kijkt het vóór het uploadpunt na.
- **Support:** `thijs@dortus.com` (staat al in de beschrijving)

## Eigen keuring tegen de richtlijnen van de moderatoren (GEZIEN 8 nov run 23)
Richtlijnen: https://developer.blender.org/docs/features/extensions/moderation/guidelines/
- Werkt in Blender: ja, e2e in de echte Blender 4.2.23 en 5.2.3 groen (installeren als extensie, aanzetten, alle knoppen).
- Manifest: toestemming klopt nu (STL en 3MF, tak `claude/blender-2026-11-08-r`), geen standaardwaarden voor optionele velden.
- Geen auto-updater, geen netwerk (geen `requests`, `urllib` of http-aanroepen; de enige "http" zijn XML-namespaces in `drie_mf.py`), geen wheels nodig.
- Geen `__file__`, geen `open()`, geen `sys`-aanpassingen, geen `bl_ext`, geen keyconfigs, geen backslash-paden.
- `bpy.data.objects` alleen voor `new` en `remove` van eigen hulpobjecten, geen opzoeken op naam.
- ruff 0.16.9, `ruff check --isolated --select E,F --ignore=E402,E741,E731,E501`: 0 fouten, dus geen ongebruikte imports, onbekende namen of foute syntax. Zonder E501 uit te zetten komen er alleen lange regels bij (vooral Nederlandse docstrings); de richtlijn zegt zelf dat waarschuwingen niet nul hoeven te zijn. De standaardset van deze ruff geeft 17 kleine stijlpunten (RUF, I001, BLE001), niets wat de richtlijn noemt.
- Self-contained: ja, pure Python, geen externe software of server.

## Uitgave 0.1.0 (hoofdchat, 8 nov 21:55, voor main 82c5207, Daan akkoord voor 920dc77f, code gelijk)
- Zip: `producten/blender-gewrichten/uitgave/click_joints-0.1.0.zip` (gratis build, 17 bestanden, zonder betaald/)
- sha256: `6798ce4eda07920c387487faeb38aad0e9718f5819815b9da8e3be5bdb61432a`

## Stappenlijst uploaden voor de projectchat (Bram, 8 nov run 24, ±5 min, plus ±5 min MFA de eerste keer)
**Alle drie voorwaarden zijn waar (GEZIEN 21:15 UTC):** Daan `Akkoord: ja` (bevestigd voor main 920dc77f; de add-oncode is sindsdien niet veranderd), e2e groen in 4.2.23 en 5.2.3 op main 01364746 met de uitgavezip erbij (run 42522420691), en het Blender ID van Thijs staat (gebruikersnaam **Thijs-Dortus**). Indienen kan dus nu.

Wie: de projectchat, in Chrome op de HP van Thijs (deviceId 869e8714-0c9c-4923-be63-c9ffa1fecfc0), terwijl Thijs ingelogd is met zijn Blender ID. Inloggen doet Thijs zelf. Het e-mailadres van het Blender ID hoort nergens in de repo, de add-on of de pagina: als contact blijft overal thijs@dortus.com.

1. **Bestanden ophalen (1 min).** Download van de release https://github.com/thijsduinhouwer2002-coder/dortus-hq/releases/tag/click-joints-v0.1.0 deze vijf bestanden naar Downloads: `click_joints-0.1.0.zip`, `1-icoon-256.png`, `2-featured-image-1920x1080.png`, `3-preview-buigen.png`, `4-preview-paneel.png`. Controle zip: sha256 `6798ce4eda07920c387487faeb38aad0e9718f5819815b9da8e3be5bdb61432a` (staat ook in `SHA256SUMS.txt` bij de release).
1b. **Tweestapsverificatie (MFA), alleen Thijs, ±5 min, één keer.** Het uploadformulier verschijnt pas als het Blender ID MFA aan heeft (GEZIEN in de broncode van de site: `{% mfa_guard 'Upload extensions' %}` in `submit.html`); zonder MFA zie je alleen de knop "Configure MFA". Thijs zet MFA zelf aan op https://id.blender.org (bijvoorbeeld met een authenticator-app) en logt daarna met MFA in. De projectchat vult hier niets in.
2. **Uploaden.** Open https://extensions.blender.org/submit/ . Vraagt de site om in te loggen: dat doet Thijs (Blender ID Thijs-Dortus). Kies bij **File** `click_joints-0.1.0.zip`.
3. **Voorwaarden: alleen Thijs.** Het vinkje "You have read and agree with all ... policies and terms of service" is het accepteren van voorwaarden. Dat zet Thijs zelf, of de projectchat alleen als Thijs dat in die chat uitdrukkelijk zegt. Daarna **Upload Extension**.
4. **Controleer wat het manifest invulde:** naam `Click Joints`, tagline `Ball joints for 3D printed figures that show their bend range`, tags Mesh en Modeling, licentie GPL-3.0-or-later, Blender 4.2.0 en nieuwer, toestemming "Export the joint parts as STL or 3MF files". Wijkt iets af: stoppen en melden in `berichten/bram.md`.
5. **Pagina "Finalize your new submission" invullen:**
   - **Team:** leeg laten.
   - **Description:** de tekst hieronder (blok "Description"), letterlijk plakken.
   - **Support:** `https://dortus.com/click-joints/` (het veld wil een link; op die pagina staat thijs@dortus.com).
   - **Release notes (Initial Version):** `First release.`
   - **Icon:** `1-icoon-256.png`
   - **Featured image:** `2-featured-image-1920x1080.png`
   - **Previews, in deze volgorde, met onderschrift:** `3-preview-buigen.png` met "Drag the bend and the measured range stays in view. Past the limit, the extra degrees show in red." en `4-preview-paneel.png` met "Good fit, measured in mm: wall, clearance and bend range for every joint, then one STL or 3MF per part."
6. **Submit for Approval** (niet Save Draft). De status wordt "Awaiting Review". De wachtrij duurt dagen tot weken.
7. **Terugmelden:** zet de link van de extensiepagina en de status als regel in `berichten/bram.md` (of in de projectchat), dan houdt Bram de keuring bij en reageert hij op vragen van de moderatoren.

Later, niet nu: voor updates zonder klikken kan Thijs op zijn profielpagina van extensions.blender.org een token maken (API `versions/upload`, zie https://developer.blender.org/docs/features/extensions/ci_cd/). Dat zet Bram pas op de lijst als er een update is.

### Description (plakken bij stap 5)
```
Turn a sculpt into a poseable, printable figure. Set the 3D cursor where the joint goes, click Place joint, and Click Joints cuts the mesh into two watertight parts with a ball and socket or a pin, sized with the clearance your printer needs, in millimetres.

For a ball joint it then measures how far the joint bends before the parts collide, in 8 directions, and shows that range in the viewport. Auto picks the widest bend with the best fit (30°, 25° or 20°), and the panel shows the measured angle, for example "Bends ±20°". Tilt the part past that limit and the spot where it hits turns red.

A ring on the cut shows the fit: green is a good fit, yellow is tight, red is too thin or breaks through the surface. The panel tells you why, for example "Tight: wall 0.89 mm (aim for 1.5 mm or more)".

- Range of motion: the measured bend of every ball joint, in degrees, before you print
- Ball and socket, or pin and hole
- Auto size: picks the largest ball with a good fit, or tells you when none fits well
- Clearance in mm (0.1 to 0.3 mm is typical)
- Exploded view, so you see the ball and socket apart; the export stays in place
- "Make watertight" for open or messy meshes, on a copy; your original stays untouched
- Export as STL or 3MF, one file per part, in millimetres
- Honest limits: a spot too thin for a ball joint, or too close to another joint, is refused with a clear message instead of a broken part
- Tested on Blender 4.2 LTS and 5.2 LTS

Support: thijs@dortus.com
```
Bron: "Beschrijving run 4 (geldt)" in `commercie/blender-click-joints/winkeltekst.md`, met `Bends ±20°` in plaats van ±25° (Daan 18:33, gelijk aan de plaatjes).
