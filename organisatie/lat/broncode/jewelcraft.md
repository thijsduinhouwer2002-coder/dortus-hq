# JewelCraft (gratis Blender-add-on voor sieraadontwerp, maat en gewicht voor productie)

Afkijker, za 28 nov 2026 ±12:30 NL, issue #20. Waarom deze: de bekendste Blender-add-on voor iets wat echt gemaakt wordt (gieten, printen), op millimeter, net als Click Joints en Click Cuts. En hij haalt zijn bereik zonder extensions.blender.org.

## Feiten (curl en `git clone --depth 1`, GEZIEN 28 nov 12:30)
- Code: https://github.com/mrachinskiy/jewelcraft , maker Mikhail Rachinskiy, sinds 2015. Laatste commit 10 nov 2026, versie 3.0.1 (`source/blender_manifest.toml`).
- Licentie **GPL-3.0-or-later** (`LICENSE`, manifest). Niets uitgevoerd, alleen gelezen. 78 Python-bestanden, ±13.000 regels.
- **618 sterren, 156k downloads van de GitHub-releases, waarvan 3,8k van de nieuwste** (img.shields.io, GEZIEN). 0 open en 83 gesloten issues (shields, GEZIEN). De issues zelf kon ik niet lezen: de repo valt buiten de GitHub-toegang van deze geplande taak (api 403) en de webpagina geeft 403.
- **Niet op extensions.blender.org** (zoeken op "jewel" daar geeft alleen Tissue, GEZIEN). Hij verspreidt zich via een eigen extensie-bron: een statisch bestand https://mrachinskiy.github.io/api/v1/extensions.json met per Blenderversie een zip op GitHub (2.18.1 voor Blender 4.2 tot 5.2, 3.0.1 voor 4.5 en nieuwer, GEZIEN).
- Gratis, geen betaalde versie in de repo of README. Vertaald in 8 talen via `.po`-bestanden (`source/localization/`), vrijwilligers vullen ze aan.

## Wat ze slim doen (bestand en regels)
1. **Installeren is één link slepen.** De README zegt bovenaan "Drag and Drop this link into Blender" met een link van de vorm `...zip?repository=<bron>&blender_version_min=4.5.0`. Blender installeert de zip én voegt de bron toe, dus elke volgende versie komt vanzelf binnen (README r. 22 tot 27 en de link onderaan). Het Blender-handboek beschrijft precies dit formaat, ook voor extensions.blender.org zelf: `{URL}.zip?repository=...&blender_version_min=...` (DERDEN, https://docs.blender.org/manual/en/latest/advanced/extensions/creating_repository/static_repository.html), en "When updates are available a notification will be visible on the status bar" (DERDEN, https://docs.blender.org/manual/en/latest/editors/preferences/extensions.html).
2. **Een waarschuwingspaneel dat alleen verschijnt als er iets mis is, met één grote knop die het oplost.** `VIEW3D_PT_jewelcraft_warning` in `source/ui.py` r. 328 tot 361: `poll` geeft het paneel alleen bij een fout. Twee gevallen: "Updates check is disabled" met knop "Enable and Save" (zet bij de eigen bron "check for updates on startup" aan en bewaart de voorkeuren, `operators/utils/settings.py` r. 13 tot 26; de controle zelf in `lib/updatelib.py`, 38 regels), en "Scene scale is not optimal" met knop "Set Units" (mm, schaal 0,001 en ook de rasterschaal, `settings.py` r. 29 tot 44; `lib/unit.py` r. 23 tot 30).
3. **Gewicht uit volume.** Volume van de geëvalueerde mesh (modifiers toegepast) in wereldmaat, getrianguleerd, met `bm.calc_volume()` (`lib/mesh.py` r. 15 tot 33), keer de dichtheid uit een eigen lijst metalen (`operators/weighting/weighting_panel.py` r. 82 tot 92). Uitkomst als regels "… mm³ Volume" en gram per metaal.
4. **Ontwerprapport als HTML** met een render, maten, gewicht en waarschuwingen (bijvoorbeeld stenen die elkaar raken, `operators/design_report/report_warn.py`). Dat is wat een sieradenmaker naar zijn klant of gieterij stuurt.
5. **Twee versies naast elkaar in één bron:** een oude reeks voor Blender 4.2 en de nieuwe voor 4.5 en nieuwer, elk met eigen `blender_version_min` en `max`. Wie op een oude LTS blijft, krijgt nooit een zip die niet werkt.

## Wat gebruikers vragen of klagen
Niet te lezen deze run (zie boven). Wat wel zichtbaar is: 0 open issues bij 83 gesloten, dus de maker sluit alles af; de README vraagt bij een fout om Blender- en add-onversie plus een schermafdruk van de melding.

## Wat dit betekent voor ons
- **Gratis Click Joints: de sleeplink.** De Extensions-pagina geeft zelf al zo'n link (GEZIEN, `add-on-click-joints-v0.1.1.zip?repository=%2Fapi%2Fv1%2Fextensions%2F&blender_version_min=4.2.0`). Op de README van de loket-repo `click-joints` en op dortus.com/click-joints staat nu alleen "Free on the Blender Extensions platform" met een link naar de pagina. Een regel "Drag this link into Blender (4.2 or newer)" met die link scheelt een stap en zet de officiële bron aan, zodat 0.1.2 (die naar Pro wijst) vanzelf bij de gebruiker komt. Gezet als issue bij Bram.
- **Pro en Click Cuts (betaald):** de koper moet nu bij elke versie de zip opnieuw halen ("Updating later? Install the new zip the same way", `producten/blender-splitser/winkel/docs.md` r. 14). Blender kent bronnen met een toegangssleutel ("Access Token, may be required by some repositories", handboek, DERDEN), maar dortus.com is statisch en kan geen sleutel controleren; dat vraagt een dienst die geld of nieuwe accounts kost, dus niet nu. Later bekijken als Pro meer dan een handvol kopers heeft.
- **Schaal en eenheden doen wij al goed:** Click Joints (`click_joints/schaal.py`) en Click Cuts (`split_joints/schaal.py`) waarschuwen bij een figuur onder 5 of boven 500 mm en zetten met één knop de eenheid om zonder het figuur te schalen. Zo houden.
- **Gram per deel (idee voor later, geen gat in de lat):** Click Cuts toont per deel maat, dicht en wand (`split_joints/controle.py` r. 153 tot 180). Volume keer 1,24 g/cm³ voor PLA (GOK, gangbare waarde) geeft een bovengrens in gram per deel. Een slicer doet dit beter met vulling, dus pas bouwen als een koper erom vraagt (regel 10).

## Ook gezien
- De loket-README van `click-joints` op GitHub zegt nog "Measured in Blender, not print tested by us yet" (curl raw README, GEZIEN 28 nov 12:30; laatste commit daar 20 nov). De verbeterde README zonder die zin staat sinds 26 nov klaar in `producten/blender-gewrichten/repo-click-joints/README.md` (kaart, #160) maar is niet gepusht. Gemeld bij de hoofdchat.

Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.
