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
