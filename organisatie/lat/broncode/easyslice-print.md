# EasySlice Print (gratis Blender-add-on: model splitsen met pennen voor 3D-print, directe concurrent van Click Cuts)

Afkijker, za 28 nov 2026 ±21:50 NL, issue #20. Waarom deze: de gratis splitser met de meeste reviews op extensions.blender.org (21), en hij doet al wat in onze lat bij Click Cuts nog open staat: snijden langs een getekende bocht. MACHIN3tools kon niet: GitHub buiten de toegang van deze taak (API-melding, GEZIEN). Code daarom uit de zip van Extensions gehaald.

## Feiten (curl, GEZIEN 28 nov ±21:30)
- Zip 0.3.7-alpha van https://extensions.blender.org/add-ons/easy-slice-print/ (sha256 3bd20b1d..., 93 KB). Maker Rafael Omodei, code ook op github.com/rafaelomodei/easySlicePrint (niet te lezen vanuit deze taak). Niets uitgevoerd, alleen gelezen. ±7.500 regels Python.
- Licentie **GPL-3.0-or-later** (`blender_manifest.toml`, SPDX-kop in elk bestand, `LICENSE`). Click Cuts is ook GPL, dus ideeën en zelfs code mogen we overnemen met naamsvermelding.
- **7.581 downloads, 21 reviews**, gepubliceerd 3 sep 2026, laatste versie 22 sep (pagina, GEZIEN). Dat is ±87 downloads per dag (GOK uit GEZIEN: 7.581 gedeeld door 87 dagen).
- Sterren: **10 keer 5 en 11 keer 1** (`data-count` in de reviewpagina, GEZIEN). Alle 11 enen komen van accounts met de naam CatPin of Alex-Sokol (de maker van het betaalde CatPin op Gumroad), met dezelfde tekst "This add-on is stolen". De echte reviews zijn allemaal 5.
- Functies (winkeltekst): Plane, Curve en Freehand cut, pin en socket automatisch, pen als cilinder, taps, zeskant, blok of eigen mesh, Quick Cut, een niet-destructieve Plan Mode, printer-speling plus Fit-keuze, snijspleet (kerf), Exploded View, export STL, OBJ en FBX, werken in mm.

## Wat ze slim doen (bestand en regels)
1. **Een getekende snede raakt alleen het materiaal onder je lijn, niet wat erachter ligt.** `plan.py` r. 255 tot 311 (`ribbon_surfaces`): per kolom van de lijn meten ze met stralen langs de kijkrichting waar het model begint en eindigt (`column_runs`), en houden alleen de "band" van materiaal waar de lijn op staat (`section.band_around`). Uitleg in de code: "That is what keeps a curve drawn across the near leg from reaching through the far one." Een lijn over het voorste been snijdt dus niet ook het achterste been door.
2. **Snijden langs een bocht.** `core/surfaces.py` r. 1 tot 25: de getekende lijn gaat door een Catmull-Rom-spline (glad snijvlak, geen hoekjes), wordt in de kijkrichting uitgerekt tot een lint, en dat lint wordt met de snijspleet dik gemaakt (`slab_from_patch`) en met een boolean afgetrokken. Freehand: een gesloten lus op het oppervlak met een gladgetrokken vlies erin, zo snij je een kapje (oog, knoop) los.
3. **Mislukte snede op het model rood geverfd.** `core/diagnosis.py` r. 1 tot 30: blijft het deel na de boolean in één stuk, dan zoeken ze vanaf beide kanten van de snede door de mesh waar de helften nog vastzitten, en verven het snijvlak van rood (daar zit het vast) via oranje naar groen. Geen tekst "het lukte niet", maar de plek.
4. **Speling hoort bij de printer, de Fit bij de verbinding.** `prefs.py` r. 41 tot 63: één "Printer Clearance" in de voorkeuren (standaard 0,10 mm per kant), met de regel "Print a test joint once, then leave it alone." Per snede kies je dan `core/connectors.py` r. 41 tot 47: Press 0,5x, Snug 1x ("the usual choice"), Easy 1,5x, Loose 2,5x ("leaves room for glue"). Het getal in het paneel is het echte getal (`plan.py` r. 899 tot 918).
5. **Back to Plan en Approve.** `ops_plan.py` r. 579 tot 650: na Build kun je terug naar het plan (delen weg, origineel terug uit een backup-collectie, sneden weer te bewerken); Approve houdt de delen en laat sneden die niet gebouwd zijn op het juiste deel staan.

## Wat gebruikers zeggen (reviews op Extensions, GEZIEN 28 nov)
- Lof gaat bijna altijd over gemak: "the easiest tool ever", "Super easy to use", "Easy and dynamic", "gets the job done quick" (6 van de 10 echte reviews noemen easy, simple of quick).
- Klacht: "Sometimes it acts a little weird and you have to redo the cut" (Bubbalu, 2 weken).
- Wens: "add a feature that allows us to cut parts such as eyes, buttons etc. without split the entire model" (ahmetrock, 1 maand). **Dat kan Click Cuts al:** Free cut en Draw cut snijden alleen binnen hun rechthoek (`split_joints/vrije_snede.py` r. 1).
- Ruzie: de maker van CatPin plaatste 11 eensterrenreviews onder verschillende namen ("If I have to post this here from 20,000 accounts, I will do it"). Rafael antwoordde elke keer hetzelfde, rustig en zakelijk ("Similarity between competing tools is not evidence of copying"). De echte gebruikers bleven 5 sterren geven; een koper schreef zelfs "unlike Catpin, it's free".

## Wat dit betekent voor ons
- **Draw cut snijdt nu door alles wat achter de lijn ligt.** `split_joints/lijn.py` r. 9 tot 34: de rechthoek loopt in de kijkrichting over "the whole depth of the piece" (GEZIEN in de code). Wie in vooraanzicht een lijn over het voorste been van een figuur trekt, snijdt het achterste been ook door, als dat in hetzelfde stuk zit (GOK op hoe vaak dat voorkomt; voor figuren, onze hoofdgroep, vaak). De band-truc van EasySlice lost dat op zonder dat de koper iets extra moet doen. Gezet als #422 bij de Productbouwer.
- **Snijden langs de vorm** (gat 3 in `organisatie/lat/click-cuts.md`, nog open): EasySlice laat zien dat een getekende bocht (spline, lint, kerf) in ±600 regels kan (`core/surfaces.py` 623 regels). Na de eerste verkopen, niet nu.
- **Rood waar het vastzit:** onze foutmelding zegt nu "The free cut box touches ... at its side (x mm2)" (`vrije_snede.py` r. 207 tot 210). Een rode plek op het model is duidelijker. Klein, later.
- **Fit-keuze per verbinding** (Press, Snug, Glue) bovenop onze bewaarde passingproef maakt ons voordeel groter: één proef, en toch kiezen tussen klemmen en lijmen. Hoort bij #21 (klikpennen zonder lijm).
- **Reviews op Extensions zijn niet veilig voor concurrenten.** Komt er een gratis Lite van Click Cuts op Extensions (route C in `platformen/ideeen/grotere-markt-2026-12.md`), antwoord dan zoals Rafael: één keer, rustig, met feiten. En nooit andersom (regel 5).
- **Winkeltekst:** de wens van ahmetrock is een zin voor ons: "Cut off just an arm, an ear or a button, the rest stays whole." Naar de Productbouwer bij de volgende winkeltekst.

Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.
