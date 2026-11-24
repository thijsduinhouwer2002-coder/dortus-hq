# Open broncode van add-ons die op Click Joints Pro en Click Cuts lijken (25 nov 2026)

## De 5 dingen die kopers het meest opleveren, op volgorde van geld
1. **Click Cuts: klikpennen die vasthouden zonder lijm** (ring op de pen, groef in het gat). Zelfs de gratis slicers van Bambu en Prusa hebben "Snap" (`concurrentie.md`); wij alleen gladde losse pennen. Voorbeeld: printsplit `joints/cylinder.py` r34 tot 77, SnapSplit `ops_connectors.py` r1553 tot 1597. Ons bestand: `split_joints/vormen.py` (`pen_bmesh`, `gat_bmesh`). Issue #21.
2. **Click Joints Pro: twee nieuwe gewrichten, swivel (draaien in bovenarm, dij, middel) en dubbele kogel** (los haltertje met twee kogels). De enige klacht in de ARTICULATOR-reviews is "more types of joints" en Cut Flex verkoopt op 15 presets (`click-joints-plan-2026-11-19.md`). Voorbeeld: printsplit `joints/swivel.py` en `joints/double_ball.py`. Ons bestand: `click_joints/betaald/` (nieuw), `vormen.py`, `maat.py`. Issue #22.
3. **Click Cuts: één veld "Print size (mm)"** voor de langste kant, dan schaalt het model en snijdt het op maat. BedSplit Lite verkoopt dit als stap 2 ("no unit setup, no scale maths"). Ons bestand: `split_joints/schaal.py`, `paneel.py`. Issue #23.
4. **Click Joints (beide): klikcontrole per materiaal** met de rekenregel van printsplit (`joints/snapfit.py` r15 tot 58): genoeg overlap om te houden, niet zoveel dat hars of PETG barst, met een zin in de lijst. Ons bestand: `click_joints/maat.py` (OPENING staat vast op 0,85).
5. **Beide: vertaling van het paneel** via `bpy.app.translations`. SnapSplit heeft 19 talen (`localization.py`, 3.069 regels), de ingebouwde 3D Print Toolbox kreeg 7 vertalingen van gebruikers. Opbrengst is een GOK (Japanse en Chinese figuurprinters).

Licentie: Click Joints (ook Pro, zelfde map) en Click Cuts zijn **GPL-3.0-or-later** (GEZIEN: `producten/blender-gewrichten/click_joints/blender_manifest.toml` en `producten/blender-splitser/split_joints/blender_manifest.toml`). GPL-code van printsplit, SnapSplit, JointCraft of de Toolbox mogen we dus overnemen, met hun copyrightregel en een vermelding in de code en de changelog. MIT-code mag ook (vermelding houden).

---

Werkwijze: gezocht met `gh api search/repositories` (16 zoekopdrachten: joint, ball joint, print in place, articulated, connector, dowel, split mesh, 3d print toolbox, boolean cutter, keyed cut, rig print, bed split en meer), repo's gekloond met `git clone --depth 1` in /tmp en alleen gelezen, niets uitgevoerd. Issues gelezen via de zoek-API van GitHub en de API van projects.blender.org. Sterren en licenties GEZIEN op 25 nov 2026. Betaalde concurrenten (Cleave, CatPin, Split 3D Print, NB Figure Joints, JointLab) hebben geen open code; die staan in `producten/blender-splitser/concurrentie.md` en `click-joints-plan-2026-11-19.md`.

## 1. printsplit (wenyen-hsu)
- Link: https://github.com/wenyen-hsu/printsplit · Licentie: GPL-3.0-or-later (GEZIEN, LICENSE en SPDX-kop per bestand) · Sterren: 2 (GEZIEN) · ±4.600 regels Python, laatste push 15 jul 2026.
- Wat: lijn tekenen, snijden met bmesh (geen boolean), daarna een vast of beweegbaar verbindstuk. Noemt zichzelf een "clean-room" namaak van betaalde splits-add-ons.
- **Slim:**
  - `joints/snapfit.py` r1 tot 58: klikregel zonder bpy. Overlap i = (1 − opening) × D − 2 × speling; rek = i / opening. Houdt als i ≥ 0,4 mm en rek ≥ 1,5%; barst boven rek 25%; wand minimaal 1,2 mm. Te klein: opening kleiner maken en anders een waarschuwing "Ball too small for a snap fit ... scale the joint up". (DERDEN: hun eigen PLA-richtlijn, niet door ons geprint.)
  - `joints/ball_socket.py` r110 tot 124: kogel plus wand moet in het materiaal passen; zo niet, de kogel tot drie keer verkleinen; te klein dan geen gewricht (geeft `None`).
  - `joints/ball_socket.py` r56 tot 74: rond de kom een schotel onder de bewegingshoek, zodat de platte vlakken niet meteen botsen.
  - `joints/_solids.py` r106 tot 112: gat met N hoeken straal delen door cos(π/N), zodat een veelhoekige pen in elke stand vrij draait.
  - `joints/swivel.py` r1 tot 27: paddenstoelpen in een kamer met ondersnijding, alleen draaien; ondersnijding gerekend bóvenop speling en hoekfout, met kruissleuven zodat de kop indrukt bij het klikken.
  - `joints/double_ball.py` r1 tot 45: beide delen een kom, plus een los haltertje (kogel, staaf, kogel) als derde object naast de naad.
  - `joints/hinge.py` r1 tot 20: scharnier dat van opzij inschuift, zonder losse pen; V-sleuf en wiggen onder de bewegingshoek geven een vlakke eindstop.
  - `joints/cylinder.py` r1 tot 77: taps toelopende pen met klikring op 0,6 van de diepte (bolling = speling + max(snap_mm, 0,08 × r)), groef in het gat; "parts hold without glue".
  - `core/history.py` r1 tot 107: oude mesh bewaard met fake user, zodat "Undo Last" ook werkt na opslaan en opnieuw openen.
  - `tests/test_movable_joints.py`: toetsen op houden, draaien, eindstop en klikrekenwerk (r112 tot 307), headless in Blender.
- **Klachten (issues):** #1 "The hinge cut": "the hinge is always generated in wrong places", vraagt hoe je de scharniersnede maakt. Kans: wij zetten de scharnieras uit het rig (Pro), en leggen in het paneel uit waar de as komt.
- **Toepassen:** swivel en dubbele kogel in Click Joints Pro (`click_joints/betaald/`, `vormen.py`, `maat.py`); klikring in Click Cuts (`split_joints/vormen.py`); klikregel in `click_joints/maat.py`. Click Cuts doet de cos(π/N)-correctie al (`split_joints/vormen.py` `gat_bmesh`); Click Joints niet, maar met 64 hoeken is de fout 0,12% van de straal (GOK: verwaarloosbaar).

## 2. SnapSplit (Betakontext)
- Link: https://github.com/Betakontext/snapsplit · Licentie: GPL-3.0-or-later (GEZIEN, `snapsplit/LICENCE.txt` en manifest) · Sterren: 34 (GEZIEN, de meeste van alle gevonden repo's) · ±16.200 regels in de add-on, versie 0.2.1, push 19 nov 2026.
- Wordt ook verkocht: $20 op Superhive, $14 op Gumroad, 30+ verkopen in 8 maanden (DERDEN: `producten/blender-splitser/concurrentie.md`). Open code en toch verkopen.
- **Slim:**
  - `profiles.py` r42 tot 46 en r522: speling per kant per materiaal (PLA 0,20, PETG 0,30, ABS en ASA 0,25, TPU 0,35, SLA 0,10 mm), met een eigen getal dat voorgaat; "0 betekent het profiel, niet nul speling".
  - `ops_connectors.py` r1553 tot 1597: klikbolletjes in een ring om de pen (aantal, diameter 2 mm, uitsteek 1 mm), het gat met dezelfde bolletjes plus speling. Varianten Snap Pin, Snap Tenon, Snap Dovetail (`profiles.py` r264 tot 266).
  - `contact_geometry.py` r151 tot 230: zoekt zelf het gedeelde snijvlak tussen twee delen (driehoeken tegen elkaar in, overlap van de projectie), niet op naam of bounding box.
  - `ops_split.py` r654 tot 856: holle modellen (Solidify, 3D Print Toolbox Hollow, losse binnenschil) eerst herkennen en samenvoegen; r1389: dichtmaken als ring tussen buiten- en binnenrand, zodat de holte blijft.
  - Live Preview van verbinders als draadmodel, max 200 objecten, zonder boolean (README).
  - `localization.py`: 19 talen via Blenders eigen vertaalsysteem.
- **Klachten:** #23 "Connectors are too big when Scene Units changed to Millimeters": "generating at 1000x scale, completely enveloping the part" (Blender 5.1.0). Kans: Click Cuts en Click Joints rekenen met `scale_length` (`eigenschappen.py` `eenheid_per_mm`) en hebben een schaalcontrole; noem "works in any unit setup, mm or m" in de winkeltekst en houd een e2e-toets met een mm-scène.
- README zegt zelf: "Freehand Cut ... does not create an arbitrary curved cutting path" en opnieuw snijden van een al gesneden deel kan niet. Kans voor Click Cuts Free cut.
- **Toepassen:** klikvariant in `split_joints/vormen.py` (issue #21); holle modellen als toets in `producten/blender-splitser/e2e` (een beeld met Solidify-binnenwand).

## 3. 3D Print Toolbox (Blender, ingebouwd als extensie)
- Link: https://projects.blender.org/extensions/print3d_toolbox · Licentie: GPL-3.0-or-later (GEZIEN, LICENSE en manifest, versie 1.5.0) · Sterren: niet zichtbaar via de API; ±2.090 regels.
- **Slim:**
  - `source/lib.py` r146 tot 205: wanddikte per vlak: per driehoek 6 vaste willekeurige punten (seed = vlaknummer, dus elke keer hetzelfde), straal achterwaarts langs de normaal tot de gevraagde dikte; raakt hij iets, dan zijn beide vlakken te dun.
  - `source/operators/analyze.py` r14 tot 45: eenheden netjes uit `unit_settings` (systeem, lengte-eenheid, terugval naar cm of inch).
  - `source/operators/analyze.py` r186 tot 250: aantal losse eilanden tellen met een tijdelijke Geometry Nodes-groep (Mesh Island plus Attribute Statistic), snel ook bij grote meshes.
  - `source/operators/edit.py` r309 tot 380: Align XY: gekozen vlakken plat op het bed draaien, gewogen naar oppervlak, schaal en plek blijven gelijk.
- **Klachten (31 issues, GEZIEN):** #14 "Export asks for location, every time", #35 export gebruikt Render- in plaats van Viewport-modifiers, #22 volume hangt af van de plek, #33 en #21 valse "Zero Faces", #30 "Check All crashes", #16 en #34 Hollow geeft fouten. Zeven issues zijn vertalingen die gebruikers zelf aanboden (#17, #18, #19, #26, #27, #29, #32).
- **Toepassen:** Click Cuts `split_joints/exporteer.py`: exportmap onthouden (doen we al met `exportmap`, nakijken dat het per bestand blijft); Align XY als idee voor "Lay parts flat" (tak `claude/click-cuts-1.0.1-plat`); vertalingen (punt 5 bovenaan).

## 4. JointCraft 3D (marykaweb)
- Link: https://github.com/marykaweb/JointCraft-3D · Licentie: GPL-3.0-or-later (GEZIEN, `jointcraft/blender_manifest.toml`; geen LICENSE-bestand) · Sterren: 0 (GEZIEN) · ±1.900 regels, push 9 nov 2026, README in het Russisch.
- **Slim:**
  - `jointcraft/preview.py` r18 tot 138: voorbeeld met GPU-lijnen door het model heen (blauw de pen, oranje het gat met speling), zonder objecten of boolean; te groot dan verdwijnt het voorbeeld en zegt het paneel de grootste maat die past. Eén functie `joint_parameters()` voor voorbeeld en echte snede, zodat ze nooit verschillen.
  - "Fit Dimensions to Parts": maten afleiden van de dikte van de delen.
  - `jointcraft/hinge_geometry.py` r18 en r54: dezelfde cos(π/64)-correctie.
- **Klachten:** geen issues.
- **Toepassen:** Click Cuts heeft geen voorbeeld van de pennen vóór het snijden (geen `draw_handler` in `split_joints/`); een lijnvoorbeeld zoals hier kan later in `split_joints/paneel.py`. Click Joints heeft al GPU-tekenwerk (`waaier.py`, `betaald/labels.py`).

## 5. BedSplit Lite (mendbox)
- Link: https://github.com/mendbox/bedsplit-lite · Licentie: GPL-3.0-or-later (GEZIEN) · Sterren: 0 (GEZIEN) · ±1.380 regels, push 21 nov 2026.
- **Slim (verkoop):** gratis open Lite op GitHub en BlendKit, betaalde Full op Gumroad en Superhive met deuvels, zwaluwstaart, meshreparatie en verschuifbare snedes. Tabel "Lite vs Full" in de README. Ook op BlendKit, dat installeert vanuit Blender zelf.
- **Slim (product):** "Resize for print: type the real size of the longest side in millimetres ... No unit setup, no scale maths." 18 printers; delen plat neergelegd naast het model, elk een eigen kleur.
- **Klachten:** geen issues.
- **Toepassen:** veld "Print size (mm)" in `split_joints/schaal.py` en `paneel.py` (issue #23). BlendKit als extra kanaal voor gratis Click Joints is een vraag voor de hoofdchat (niet onderzocht of het geld kost).

## 6. rig2print (mickdarling)
- Link: https://github.com/mickdarling/rig2print · Licentie: MIT (GEZIEN) · Sterren: 0 (GEZIEN) · Rust plus ±1.300 regels Python, push 14 nov 2026, "experimental".
- **Slim:** leest een gewogen botpaar uit Blender en maakt een print-in-place scharnier (`scripts/prototype_joint.py`). `docs/existing-projects.md` geeft een goede lijst met verwante projecten: articulated-toys (MIT, snijdt langs één as met kogels), mcp-printable (MIT), LayerMechanic (betaald op Superhive, controleert print-in-place beweging) en het SIGGRAPH-artikel "Fabricating Articulated Characters from Skinned Meshes" (2012). Speling is "one-sided surface gap", niet de diameter.
- **Klachten:** geen issues.
- **Toepassen:** bevestigt dat niemand nog rig naar losse klikdelen goed doet; Figure from rig (`click_joints/betaald/rig.py`) is onze voorsprong. Print-in-place is een eigen markt (GOK), niet nu.

## 7. Kleinere vondsten
| Repo | Licentie (GEZIEN) | Sterren (GEZIEN) | Wat het doet | Bruikbaar voor ons |
|---|---|---|---|---|
| [agapas/3d-print-toolbox-modified](https://github.com/agapas/3d-print-toolbox-modified) | GPL-3.0 | 63 | oude Toolbox met meer opruiminstellingen en "Copy to Clipboard" van volume | issue #3 vraagt volume als driver: gebruikers willen getallen kopiëren (gewicht, filament) |
| [aturkoz/CutMode](https://github.com/aturkoz/CutMode) | MIT | 11 | alleen README en beeld, geen code; "automatically add Snap Connectors", "Undo Last Cut" | bevestigt dat "snap" het verkoopwoord is |
| [RemindZ/MateSnap](https://github.com/RemindZ/MateSnap) | MIT | 0 | twee klikken: pen op gat zetten, draait vierkante pennen zelf goed | niet nu |
| [The-Anomaly-be/blender-3d-print-model-cutter](https://github.com/The-Anomaly-be/blender-3d-print-model-cutter) | GPL-3.0 | 1 | altijd 8 delen met pennen, namen als `Model_right_front_top` | niets nieuws |
| [oormicreations/BlendShell](https://github.com/oormicreations/BlendShell) | MIT | 47 | uithollen; issue #1 crasht op nieuwe Blender (`apply_as`) | oude add-ons breken op nieuwe Blender: wij toetsen 4.2 en 5.3 |
| [the13th-undecimber/Blender-ball-joint-generator](https://github.com/the13th-undecimber/Blender-ball-joint-generator) | geen | 0 | lege repo (18 nov 2026) | let op: nieuwe kogelgewricht-makers duiken op |
| blanchsb/Print-Prep, SonneblomDigitaal/bedfit-splitter | geen | 1 en 0 | alleen zip of beelden, geen leesbare code | niet gelezen (zip niet uitgepakt) |

## Wat we níet overnemen
- Geen code van repo's zonder licentie (Print-Prep, bedfit-splitter, ball-joint-generator).
- Snijden zonder boolean (printsplit bmesh-bisect) is sneller, maar onze Manifold-booleans met terugval werken en zijn getoetst; niet ombouwen voor de lancering.
