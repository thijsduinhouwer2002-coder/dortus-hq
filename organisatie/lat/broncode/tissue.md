# Tissue (gratis Blender-add-on voor computational design, veel gebruikt voor 3D-print: roosters, patronen, dikte)

Afkijker, za 28 nov 2026 ±18:50 NL, issue #20. Waarom deze: een van de best gedownloade gratis add-ons op extensions.blender.org, populair bij mensen die printen (roosters, lattices), en hij laat zien wat er gebeurt als de versie op Extensions achterloopt. MACHIN3tools wilde ik eerst nemen (gratis add-on als etalage voor betaalde), maar die staat niet meer op GitHub (zoeken via de GitHub-API geeft alleen kopieën, GEZIEN).

## Feiten (curl en `git clone --depth 1`, GEZIEN 28 nov ±18:40)
- Code: https://github.com/alessandro-zomparelli/tissue , maker Alessandro Zomparelli (Co-de-iT), sinds 2017. Versie 0.3.76 (`blender_manifest.toml`), Blender 4.5 en nieuwer.
- Licentie **GPL-3.0-or-later** (SPDX-kop in elk bestand, manifest). Niets uitgevoerd, alleen gelezen. ±17.300 regels Python.
- **1,1k sterren, 14 open en 140 gesloten issues** (img.shields.io, GEZIEN). De issues zelf niet te lezen: de repo valt buiten de GitHub-toegang van deze taak en de webpagina geeft 403.
- **extensions.blender.org: 110.130 downloads, 21 reviews**, gepubliceerd 14 mei 2024, 0.3.76 sinds 31 okt 2026 (https://extensions.blender.org/add-ons/tissue/, GEZIEN).
- Geld: alleen Patreon. De README noemt 8 "Tissue Supporters" bij naam. Een Gumroad-pagina bestaat, met 0 ratings (`"ratings":{"count":0` in de pagina, GEZIEN). Geen betaalde versie.

## Wat ze slim doen (bestand en regels)
1. **De instellingen wonen op het resultaat, dus je kunt later terug.** Elk getesselleerd object krijgt een eigen PropertyGroup (`tissue_properties.py` r. 156 tot 175: `bool_lock`, `bool_dependencies`, `bool_run`). In het paneel `TISSUE_PT_tessellate_object` (`tessellate_numpy.py` r. 2435 tot 2502) staat bovenaan een rij: Refresh, een schakel "Update Dependencies", een slotje "Lock" (geen automatische update meer) en een kruisje "Remove". Daaronder alle instellingen opnieuw, en een foutregel als `error_message` gevuld is. Je verandert een getal en het resultaat rekent opnieuw; geen Ctrl+Z nodig.
2. **Testen in elke Blender plus de bèta, één keer per week vanzelf.** `.github/workflows/tests.yml`: matrix 4.5, 5.0, 5.1 en 5.2, plus 5.3 als bèta met `continue-on-error` (een rode bèta meldt, maar breekt de run niet), en `cron: "0 6 * * 1"`. `tests/run_tests.py` bouwt per gereedschap een kleine scène en controleert de uitkomst. Een aparte job bouwt en valideert de extensie-zip.
3. **De maker antwoordt op elke review**, ook op de boze, met wat hij deed ("I finally took ownership of this page and updated the Tissue version", reviewpagina, GEZIEN).

## Wat gebruikers klagen (reviews op Extensions, GEZIEN 28 nov)
- Zeven maanden lang stond op Extensions 0.3.71, die niet werkte in Blender 5. De nieuwere versie stond wel op GitHub. Reviews van 2 tot 7 maanden oud gaan bijna allemaal daarover: "Please update the addon for blender 5.1", en gebruikers die elkaar uitleggen hoe ze `utils.py` zelf moeten repareren. Die reviews blijven staan, ook nu het al 4 weken opgelost is.
- Les: wat op Extensions staat, is wat bijna iedereen krijgt. Loopt die versie achter, dan worden de reviews een bugloket en zien nieuwe kijkers alleen klachten.

## Wat dit betekent voor ons
- **Gratis Click Joints op Extensions staat nog op 0.1.1** (437 downloads, 0 reviews, "Updated 1 w", GEZIEN 28 nov 18:45), terwijl 0.1.3 met de tenenfix klaarstaat (kaart, plakkaart `winkel/plak-gratis-0.1.3.md`, plakken ma 30 nov). 0.1.1 werkt, dus geen ramp zoals bij Tissue; maar houd de regel aan: een fix die een gebruiker raakt, staat binnen een dag op Extensions. En antwoord op elke review daar, zoals Tissue en Cleave (V4SS3UR antwoordt op Superhive op elke review, GEZIEN 28 nov).
- **Bijstellen na het plaatsen (Pro, na de sale).** Tissue bewaart de instellingen op het resultaat; Cleave 1.8 (28 nov) zegt nu "any earlier cut can be cancelled, so you can go back and edit it" (https://superhivemarket.com/products/cleave, GEZIEN). Bij ons staat de speling al per deel opgeslagen (`cj_speling_mm`, `click_joints/beweeg.py` r. 141 tot 147), maar een geplaatst gewricht veranderen kan alleen met Ctrl+Z en opnieuw klikken (geen operator om opnieuw te passen, grep op de code, GEZIEN). Gezet als #420 bij Bram, label later.
- **Week-test met de bèta hebben wij al** (`blender-gewrichten-e2e.yml` haalt een daily van builder.blender.org voor de week-test). Zo houden.
- **Gratis zonder betaalde versie levert weinig op:** 110k downloads en 1,1k sterren, en de inkomsten zijn 8 supporters op Patreon (GOK op het bedrag, niet zichtbaar). Bevestigt de keus voor gratis plus Pro.

Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.
