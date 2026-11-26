# Broncode: Bool Tool (Blender-add-on, gratis op extensions.blender.org)

Uitgeplozen door de Afkijker op do 26 nov 2026 (±03:30 NL), voor issue #20. Code gelezen uit `git clone --depth 1` van https://github.com/nickberckley/bool_tool (laatste commit a5635e5, 15 jul 2026; niets uitgevoerd). Winkelpagina en alle 5 pagina's reviews met curl gelezen.

## Waarom dit project
- **Downloads 1.265.829, 65 reviews, gemiddeld 5.0 (61 keer 5 sterren), versie 2.1.0 van 14 jul 2026** (GEZIEN, https://extensions.blender.org/add-ons/bool-tool/ en `/reviews/`, 26 nov ±03:15 NL). Een van de meest gedownloade add-ons in de winkel van Blender zelf.
- Het snijdt modellen met een vorm die je zelf tekent (Carver). Dat is precies gat 3 van Click Cuts: "snedes langs de vorm of zelf leggen" (`organisatie/lat/click-cuts.md`).
- Licentie: GPL-3.0 of later (GEZIEN, `LICENSE` en `source/blender_manifest.toml`). Zelfde licentie als onze add-ons; code overnemen mag met hun copyrightregels, het idee nabouwen is het schoonst.

## Wat ze slim doen (bestand en regels)
1. **Snijden door te tekenen in het scherm, niet door een vlak te verschuiven.** Carver heeft drie gereedschappen: rechthoek, cirkel en lijn met punten (`source/tools/carver_box.py`, `carver_circle.py`, `carver_polyline.py`). Je klikt en sleept over het model; het werkvlak komt van het scherm (VIEW), van het oppervlak onder de muis (SURFACE) of van de 3D-cursor. Onder de motorkap één regel: `region_2d_to_ray_3d` plus `scene.ray_cast` (`source/functions/scene.py` regels 54 tot 68). Raakt de straal niets, dan valt het stil terug op het scherm (`source/tools/common/base.py` regels 431 tot 434), dus er komt nooit een foutmelding bij het tekenen.
2. **De toetsen staan in de statusbalk zolang je bezig bent, met muis- en toetsplaatjes.** `context.workspace.status_text_set(modal_keys_draw)` (`carver_box.py` regels 210 tot 300): "LMB Confirm, MMB Rotate View, RMB Cancel, Space Move, R Rotate, Shift Aspect, B Bevel", elk met het echte icoon (`MOUSE_LMB`, `EVENT_SPACEKEY`). Na afloop zet `status_text_set(None)` de gewone balk terug (`base.py` regel 701). Een nieuwe gebruiker hoeft niets te onthouden.
3. **Rechtsklik op elke knop opent het goede stuk van de handleiding.** Eén klein bestand: `source/manual.py` koppelt elke operator aan een pagina (`bpy.utils.register_manual_map`). Blender zet dan "Online Manual" in het rechtsklikmenu van die knop. Geen extra knoppen in het paneel, wel hulp op het moment van twijfel. In 2.1.0 in de "What's New" genoemd als nieuw.
4. **Elke knop heeft een omkeer-knopje ernaast.** In het paneel staat per bewerking een tweede knop met alleen een icoon (`flip=True`, `source/ui/panels.py` regels 36 tot 47). Ook in het venster na de bewerking (redo) kun je omdraaien. Kies je verkeerd om, dan los je het op zonder opnieuw te beginnen.
5. **Wat niet kan, stoppen ze vóór het misgaat, met de naam van het object.** "Modifiers cannot be applied to {naam} because it has shape keys", "{naam} is linked and can not be carved" (`base.py` regels 81 tot 90). Objecten met shape keys worden in 2.1.0 niet meer gesneden zonder vragen (What's New).
6. **Handleiding als eigen site, per gereedschap een pagina** (`documentation/pages/`, gebouwd met Sphinx, https://nickberckley.github.io/bool_tool/). De winkelpagina zegt het zelf: "You can read (way too) detailed documentation".

## Wat gebruikers vragen of klagen (reviews, GEZIEN 26 nov)
- **Rommel in de scène:** "It automatically adds cutters to collection with really ugly name (snake case) and it can not be turned off. Nightmare for scene organization." (Rawalanche, v1.1.1).
- **Werkt alleen met de standaard toetsen:** "the tool is useless because it's hardcoded to only work with default keymap, and will not work with alt-based navigation keymaps" (zelfde review). En: na aanzetten werkt de eigen sneltoets Q niet meer (R1c0, v0.4.1).
- **Niet snappen wat er met het snij-object gebeurt:** "I do not understand how to keep the object cutter present after I use it" (Eric-hoffman, v2.0.0).
- **Kapot op een nieuwere Blender:** een volle Python-fout in een review over 4.5.5 (Anton-Vashkevich, v2.0.0).
- **Wensen:** een mes-modus in Carver (antwoord maker: "on the to-do list"), hoeken laten klikken in plaats van het raster (Hodgson3d), een eigen tabblad "Bool Tool" in plaats van "Edit" (Exec-Sol).
- **Wat ze prijzen:** tijd ("saves an insane amount of time"), "should be core functionality", en dat het werkt als een gewoon Blender-gereedschap.

## Welk product wordt er beter van
**Click Cuts** (eigenaar Productbouwer):
- **Gat 3, zelf een snede leggen.** Nu: "Add free cut" zet een vlak plat midden in het stuk en de koper moet het met G, R en S in 3D goed zetten (`producten/blender-splitser/split_joints/vrije_snede.py` regels 126 tot 145 en 330). Dat vraagt 3D-handigheid die een printer-koper vaak niet heeft. Split 3D Print heeft al "Draw Cut Line" (lat, Paneel). Les uit Carver: laat de koper **een lijn over het model trekken** in het scherm; het snijvlak is die lijn, recht naar achteren in de kijkrichting (VIEW), met `region_2d_to_ray_3d`. Zelfde Cut piece daarna, met pennen en nummers. Kandidaat voor 1.1, na de magneten (#117).
- **Statusbalk met toetsen** (punt 2) zolang een Free cut gekozen is of zolang de lijn getekend wordt: "G Move, R Turn, S Scale, Cut piece". Kost weinig, haalt het "wat moet ik nu"-moment weg.
- **Rechtsklik "Online Manual"** (punt 3) zodra er een hulppagina op dortus.com is; dan is ook de "?"-knop uit de lat bijna gratis. Hetzelfde voor Click Joints Pro.
- **Wat wij al goed doen (geen werk):** onze collecties heten leesbaar ("Click Cuts pieces", "Click Cuts cut planes", `splitsen.py` regel 18, `snedes.py` regel 13) en de hulpcollecties met `sj_` gaan na het splitsen weg (`splitsen.py` regel 384). Click Cuts zet geen eigen sneltoetsen (grep op `keymap`: niets), dus de klacht over botsende toetsen raakt ons niet. Zo houden.
