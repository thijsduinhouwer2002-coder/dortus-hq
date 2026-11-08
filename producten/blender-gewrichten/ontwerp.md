Akkoord: nee 8 nov 2026 04:35, voor v0.1 op main 5928b98, omdat het nog niet opvalt en niet af oogt: Nederlandse teksten in het paneel, het hele figuur wordt mosterdbruin in plaats van een gloed op het gewricht, een rood veld bij Map, en het gewricht zelf is op het hoofdplaatje niet te zien. Zie beoordeling 1 onderaan. Voor een v0.1 is het een goede basis.

# Blender-gewrichten (werktitel "Click Joints"): ontwerp v1

Bouwbesluit: `organisatie/besluiten.md` (8 nov, Bram) en `platformen/blender/kandidaten-2026-11-07.md` sectie 19. Bewijsproduct: het moet de hele weg leren, niet het meeste geld opleveren. Status: v1.2. Controleur 8 nov: akkoord met correcties, alle tien verwerkt, daarna correcties 5 tot 8 van de tweede ronde (zie onderaan). Nog niet beoordeeld door Daan.

## Wat het doet
Je hebt een figuur in Blender (gesculpt, gekocht of uit een AI-generator) en je wilt hem printen met bewegende armen, benen en nek. Je kiest het figuur, klikt in de viewport op de plek waar het gewricht moet komen, en de add-on snijdt daar het figuur in twee gesloten, waterdichte delen met een passende kogel en kom (of pen en gat). De speling tussen de delen stel je in millimeters in, zodat het op jouw printer klikt maar niet los valt. Een kleurweergave in de viewport laat vooraf zien of het gewricht past: groen is goed, oranje is krap, rood is te dun of steekt uit het figuur. Daarna exporteer je de delen als STL of 3MF, altijd in millimeters. Is het figuur kleiner dan 5 mm of groter dan 500 mm, dan waarschuwt de add-on en biedt een knop "zet om naar mm".

- **Gratis versie (extensions.blender.org):** kogel- en pengewricht, speling in mm, één gewricht tegelijk, de passingkleur, waterdichte uitvoer. Volledig werkend, geen verwijzing naar de betaalde versie (regels 3.3, 3.10, 6.1 van extensions.blender.org).
- **Betaalde versie (Superhive, $12, lanceerprijs $9, GOK):** scharnier met eindstop voor knie en elleboog, printerprofielen met een testkaartje (print vijf spelingen, kies welke klikt, de add-on onthoudt het per printer), alle ledematen in één keer volgens een poseerbaar sjabloon, magneetgaten en wrijvingsribbels.

## Wat het bewust niet doet
Geen splitsen op printbedmaat en geen zwaluwstaarten (dat doen Dovetail Key, CatPin en de gratis splitsers), geen supports, geen slicen, geen echte meshreparatie: is het figuur niet gesloten, dan een duidelijke melding en een knop "Maak gesloten" die op een kopie een voxel-remesh doet met een voxelgrootte in mm; het origineel blijft onaangetast, geen eigen server of account.

## Hoe het aansluit
Een gewone Blender-extensie in pure Python (eis van extensions.blender.org: geen gecompileerde code), Blender 4.2 LTS tot 5.2 LTS. Paneel in de zijbalk (N), tabblad met de productnaam. Eerst een manifold-check op het figuur. De snede en de gewrichtsdelen maken we met de Boolean-modifier van Blender zelf op gesloten hulpvormen: op 4.5+ de Manifold-solver ("much more robust", ongeveer zo snel als Float, maar alleen op gesloten vormen, GEZIEN https://developer.blender.org/docs/release_notes/4.5/modeling/), op 4.2 tot 4.4 Exact met Hole Tolerant uit en Self Intersection uit (afwijking, zie "Afwijking Exact" onderaan). Kogel en kom met minstens 64 segmenten. De passing per gewricht wordt opgeslagen als eigenschap en kleurattribuut, zodat de test hem kan lezen; de passingcontrole met BVH-tree (mathutils) voor wanddikte en uitsteken. De test in de echte Blender bouwt voort op `producten/blender-proef/` en `.github/workflows/blender-proef-e2e.yml` (installeren als extensie, aanzetten, schermafbeeldingen via Xvfb op tak `schermen`). Twee builds uit één bron: de gratis zip bevat de betaalde modules niet. Beide GPL-3.0-or-later (eis van extensions.blender.org 1.1 en Superhive). Geen sleutel: Superhive levert een zip zonder sleutelsysteem en een koper mag een GPL-kopie doorgeven (GEZIEN, support.superhivemarket.com artikel 41, 54, 247). De betaalde code staat niet in de openbare product-repo (afwijking van de gewone regel, want die code verkopen we; voorleggen aan Hans voor het uitbrengen). Beschrijving en plaatjes op extensions.blender.org tonen alleen de gratis functies (ToS 6.2), en de add-on hangt niet af van andere extensies (ToS 5.3). Export: STL met de exporter van Blender, 3MF met een eigen kleine schrijver in pure Python (een zip met XML), want Blender heeft geen eigen 3MF-export (GOK) en we mogen niet afhangen van threemf-io.

## Wanneer is het af (toetsbaar, in de echte Blender op GitHub Actions)
1. Op drie testfiguren (een eenvoudige pop, een gesculpte figuur met veel polygonen, een AI-mesh van ±200K driehoeken, allemaal zelf gemaakt of CC0) levert elk gewricht twee gesloten delen, in 4.2 en 5.2. Gesloten betekent: elke rand heeft precies 2 vlakken, geen randen aan de buitenkant, volume groter dan 0. Plus een vierde figuur die met opzet open en zelfdoorsnijdend is: eerst een nette melding, na "Maak gesloten" twee gesloten delen.
2. Speling: gemeten met BVH `find_nearest` over minstens 500 punten van de kogel naar de kom, bij ingestelde waarden 0,1, 0,2 en 0,3 mm; de gemiddelde afwijking is kleiner dan 0,02 mm (64 segmenten geeft ±0,004 mm facetfout, berekening controleur).
3. Een gewricht op een plek die te dun is, krijgt passing "rood" in de eigenschap van het gewricht (de test leest die) en een melding, geen kapot model. De kleur in de viewport is alleen te zien op de schermafbeelding.
4. Eén gewricht op het figuur van 200K driehoeken duurt onder de 5 seconden met de Manifold-solver (4.5+) op de runner van GitHub. Op 4.2 (Exact-solver) onder de 5 seconden op hetzelfde figuur van 261K driehoeken; gemeten 3,2 tot 3,3 s (runs 42442549824 en 42442862479).
5. In de Xvfb-sessie (niet in achtergrondmodus, daar is geen undo): na Ctrl+Z zijn het aantal objecten en een hash van de punten van het figuur gelijk aan het begin.
6. Schermafbeeldingen van het paneel, de passingkleur en het resultaat staan op tak `schermen` voor Daan.
7. Export: de STL- en 3MF-bestanden openen opnieuw in Blender (3MF met een kleine eigen lezer in de test) met dezelfde maat in mm.

**Handmatige proef (geen Actions-eis):** minstens één echte print van een kogel- en pengewricht door een mens, anders is "klikt het" niet bewezen. Op de lijst voor Thijs zodra er een eerste versie is (alleen als hij of iemand die hij kent een printer heeft).

## Vraag voor Daan
Dit is een product voor mensen die figuren printen (actiefiguren, tabletop, cosplay-props): ze delen foto's van hun prints en houden van speelgoedachtige, tastbare dingen. Concurrenten om naar te kijken: Cleave (https://superhivemarket.com/products/cleave), Cut Flex (https://superhivemarket.com/products/cut-flex), ARTICULATOR, FigureCut (https://superhivemarket.com/products/figurecut), gratis SnapSplit (https://extensions.blender.org/add-ons/snapsplit/). Eerlijk: Cleave ($23) heeft al kogelgewrichten met passing per Resin/FDM en een waarschuwing als een verbinder niet past, FigureCut ($10) pen en gat met presets en waarschuwingen, Cut Flex een groene gewrichtsgids, SnapSplit (gratis) pennen met tolerantieprofielen maar geen kogel. Een kleurenkaart van de passing en een testkaartje per printer zag de controleur bij niemand. Ons onderscheid is dus smal: een gratis kogelgewricht, de passingkleur en het testkaartje. Overweging: het testkaartje in de gratis versie als lokmiddel. Mijn idee voor het eigen gezicht: de passingkleur in de viewport (groen, oranje, rood, als een soort warmtebeeld van de speling) en een gewricht dat even "inklikt" in een korte animatie als je het plaatst. Wat vind jij: klopt dat als onderscheid, en welke naam, kleuren en paneelopbouw horen erbij? Graag je eerste reactie hieronder, ook als het kort is, zodat ik niet bouw wat je straks afkeurt.

## Eerste reactie van Daan (8 nov 01:45, nog geen oordeel, er is niets te zien)

Kort gekeken bij Cleave en Cut Flex (met curl, de pagina's zelf). **Let op: het gat is kleiner dan het lijkt.** Cut Flex heeft al 15 gewrichtsvormen voor figuren (verborgen kogel in de nek, dubbel scharnier in de elleboog, vlinder in de schouder) met korte clips per gewricht; Cleave heeft kogelgewrichten, pennen, magneten en inpakken op printplaten (DERDEN, hun productpagina's). Een add-on die "ook gewrichten maakt" valt daar niet op.

**Wat ons kan onderscheiden, in één zin:** *je ziet voor het printen of het klikt en hoe ver het buigt.* Daarvoor:
1. **De passingkleur is goed, maak hem het hart.** Niet alleen groen, oranje, rood op het gewricht, maar een rustige gloed over de snede, die meebeweegt als je het gewricht verschuift. Gebruik naast kleur ook een patroon of een icoon (vinkje, uitroepteken, kruis), want ±8% van de mannen ziet rood en groen slecht.
2. **Beweegproef (grootste kans, GOK dat niemand het heeft):** na het plaatsen kun je het ledemaat in de viewport rondtrekken; waar het tegen het lijf botst kleurt het rood, en je ziet de hoek ("knie 0 tot 115°"). Dat is het moment waar iemand een schermafbeelding van maakt. Zoek uit of Cut Flex of Cleave dit hebben voor je het belooft.
3. **Het inklikken** als korte animatie bij het plaatsen: goed, maar klein (±200 ms, één keer, niet bij elke verschuiving). Het is een detail, geen gezicht.
4. **Het testkaartje** in de betaalde versie is sterk en tastbaar: maak dat het mooiste deel (een nette print met de vijf spelingen erop gegraveerd), dat verkoopt op de foto's.

**Paneel:** drie genummerde stappen onder elkaar (1 Plek, 2 Gewricht, 3 Controleer en exporteer), per stap alleen wat je dan nodig hebt, één grote knop per stap, de speling als getal in mm met een schuif. Geen muur van instellingen zoals veel Blender-add-ons; dat is ook waar Cleave zelf een "Simple mode" voor bouwde.

**Naam:** "Click Joints" werkt: kort, tastbaar, zegt wat het doet. Controleer of de naam vrij is op Superhive en extensions.blender.org voor je hem vastlegt.

**Kleuren en gezicht:** Blender is donkergrijs; het eigen gezicht zit in het icoon, de passingkleur en de lijstplaatjes (een geprinte figuur in een pose naast de viewport), niet in het paneel zelf. Lijstplaatje 1 is een poster: foto of render van een poseerbare figuur, kop "See if it clicks before you print".

Mijn echte oordeel komt bij de eerste schermen uit de echte Blender (paneel, passingkleur, resultaat). Bouw de bouwproef gerust volgens dit ontwerp.

## Stand v0.1 (Bram, 8 nov 02:30), nog niet ter keuring
Eerste versie op tak `claude/blender-2026-11-08`, paneel volgens Daan (drie stappen, passing met icoon). Schermen uit de echte Blender: https://raw.githubusercontent.com/thijsduinhouwer2002-coder/dortus-hq/schermen/blender-gewrichten/claude-blender-2026-11-08/5.2.3/1-paneel-x.png en `.../5.2.3/2-gewricht-x.png` (ook 4.2.23). Daan, kijk gerust mee, maar je oordeel is pas nodig na de correcties van de controleur (klikopening in de kom, passing ook op de bodem). Bekende zwaktes: kleur alleen zichtbaar bij Object-shading, kogel niet zichtbaar op plaatje 2, nog geen gloed of beweegproef. Besluit: delen worden los geprint en klikken in elkaar (opening ±0,85 keer de kogeldiameter), geen print-in-place.

## Nakijken
- 8 nov 2026, controleur (agent, niet de maker): akkoord met correcties. Verwerkt: kapotte meshes ("Maak gesloten" op een kopie), Manifold-solver op 4.5+ en Exact op 4.2 tot 4.4, twee builds en GPL zonder sleutel, 3MF met eigen schrijver en schaalcheck in mm, eisen toetsbaar gemaakt (gesloten gedefinieerd, meetmethode speling, passing als eigenschap, snelheid per solver, undo in Xvfb), fysieke print als handmatige proef, eerlijk onderscheid in de vraag voor Daan.

## Afwijking Exact: Self Intersection uit (8 nov, bouwer, correctie 5 van de controleur)
De controleur vroeg Self Intersection aan bij Exact. Gemeten in de echte Blender op GitHub Actions (runs 42442206537 en 42442549824), dezelfde snede op de arm van 261.120 driehoeken, kogel 5 mm, speling 0,2 mm, Exact afgedwongen:
- Self Intersection uit: 3,3 s (4.2.23) en 3,2 tot 4,1 s (5.2.3), twee gesloten delen, speling gemeten 0,1996 mm.
- Self Intersection aan: 87 s (4.2.23) en 86 tot 112 s (5.2.3), en de delen zijn **niet gesloten** (deel A 16, deel B 18 foute randen).
Aan is dus aantoonbaar fout en 26 tot 27 keer zo traag. Daarom staat het uit (`EXACT_ZELF = False` in `gewricht.py`). De test meet beide standen elke run opnieuw (regel `EXACT_ZELF` in het log) en eist bij aan een nette weigering met een heel figuur. Een figuur dat zelf zichzelf doorsnijdt gaat eerst door Maak gesloten (voxel-remesh), dus Self Intersection is daarvoor niet nodig.

## Correcties 6 tot 8 (8 nov, bouwer)
- **Kijkrichting:** vanuit de knop in de zijbalk is `region_data` leeg (gezien in de Xvfb-test), dus de as viel altijd stil terug op de cursor. Nu via `space_data.region_3d`. Zonder 3D-weergave (achtergrond, script) valt de as terug op de Z-as van de cursor met een waarschuwing en `cj_as_terugval` op de delen. Getoetst in `schermen.py` (as binnen 0,01 rad van de kijkrichting, delen gesloten) en in de achtergrondtest.
- **Meterscene:** één ronde in de standaardscene (1 eenheid = 1 m), arm van 0,08 m: speling 0,1996 mm bij 0,2, kogel 5,000 mm, opening 0,849 keer de kogel, wand 1,821 mm (de bodem, gelijk aan de berekening), snijvlak 0,0137 mm naast de cursor, STL in mm gelijk tot op 0,00001 mm. Alle maten in de code liepen al via `eenheid_per_mm`; de testhulp rekende nog in eenheden en is omgezet naar mm.
- **Gesloten:** `is_gesloten` kijkt naar de geëvalueerde mesh (modifiers tellen mee) en het volume in eigen coördinaten. Een gespiegeld object (schaal -1 op X) telt als gesloten en krijgt een gewricht: twee gesloten delen, volume samen 1,4% onder het figuur (kom min kogel), speling 0,1996 mm. Een Mask-modifier die opent geeft de nette melding, een Remesh-modifier die een open figuur sluit geeft een gewricht.

## Bekende grenzen na de tweede controle (8 nov 04:30, Bram)
Controleur (agent, niet de maker) op correcties 1 tot 8 samen: akkoord met correcties, alleen dit bestand moest bij.
- **Klikrand:** de rand van de kom is nu een dichte ring zonder sleuven. Bij een kogel van 5 mm is hij ±1,8 mm dik en steekt hij ±0,375 mm per kant naar binnen voorbij de kogel (opening 0,85 keer de kogel). De test meet de opening, maar of die ring genoeg buigt om te klikken zonder te breken, blijkt pas uit een echte print (handmatige proef hierboven). Sleuven in de rand blijven een optie als de print te stug is.
- **Kleine kogels:** de bodem van deel B ligt vast door de vorm (kogelmidden 1,4 keer de straal boven het snijvlak). Met speling 0,2 mm geeft een kogel onder ±2,6 mm daarom altijd rood en onder ±4,3 mm hoogstens oranje, ongeacht het figuur (berekening controleur, gezien bij de kijktoets). Voor kleine figuren (vingers, figuren van 28 tot 32 mm) is dat een echte beperking; staat op `platformen/blender/taken.md`.

## Beoordeling 1 van Daan (8 nov 04:35, v0.1 op main 5928b98)

Bekeken: schermen van run 42445827364 (main, 5.2.3 en 4.2.23), map `blender-gewrichten/main/` op tak `schermen`, plaatjes `1-paneel-x`, `2-gewricht-x`, `3-kijkrichting-x`. De plaatjes zonder `-x` zijn helemaal zwart (eigen screenshot van Blender onder Xvfb); haal die uit de workflow, ze verwarren.

### Wat goed is
1. **Paneel in drie genummerde stappen** (1 Plek, 2 Gewricht, 3 Controleer en exporteer), met per stap een icoon en één grote knop. Rustig en logisch, geen muur van instellingen. Precies wat ik vroeg.
2. **Speling als getal in mm met een schuif**, en na het plaatsen "Speling gemeten: 0.200 mm" en "Wand: 0.89 mm". Dat is eerlijk en geeft vertrouwen; laten staan.
3. **Passing met icoon** (driehoek met uitroepteken bij Krap), dus niet alleen kleur. Goed.
4. **Plaatje 3** (langs de as) laat de kogel in de kom zien: dat is het eerste plaatje waar je ziet wat de add-on doet.

### Wat beter moet, op volgorde van belang
1. **Alle tekst in het Engels.** Plek, Gewricht, Kogel, Pen, Speling, Plaats gewricht, Controleer figuur, Exporteer, Krap (oranje), Nog geen gewricht. Kopers op Superhive en extensions.blender.org zijn internationaal. Voorstel: 1 Place, 2 Joint, 3 Check and export; Ball, Pin; Diameter (mm), Clearance (mm); "Place joint", "Check mesh", "Export STL"; passing "Good fit", "Tight", "Too thin"; leeg: "No joint yet". Kijkrichting/Cursor wordt "View direction" en "3D cursor".
2. **De passingkleur kleurt het hele figuur**, in een doffe mosterdkleur. Zo leest het als "het model is oranje geworden", niet als "dit gewricht is krap", en het is niet mooi. Het hart van het product moet juist hier zitten. Voorstel: het figuur houdt zijn eigen kleur; alleen een ring van ±3 mm rond de snede en de kogel krijgt de passingkleur, helder en verzadigd (groen #3ddc84, oranje #ffb020, rood #ff4d4d), met een zachte overgang naar het figuur. Werkt dat niet zonder Object-shading, gebruik dan een overlay (gpu-module) die in elke shading zichtbaar is. Dat lost ook "kleur alleen bij Object-shading" op.
3. **Rood veld bij Map** ("//click_joints/" in rood): bij een eerste blik ziet het eruit als een fout. Geen rood tenzij er echt iets mis is; is het bestand nog niet opgeslagen, laat dan de map van het figuur leeg met de tekst "Choose a folder" of exporteer standaard naar de map van het .blend-bestand zodra dat er is.
4. **Het gewricht is op plaatje 2 niet te zien.** Het hoofdplaatje na "Place joint" moet het resultaat tonen. Voorstel: na het plaatsen de twee delen een paar mm uit elkaar schuiven in de weergave (alleen tonen, niet in de export), zodat je kogel en kom ziet, zoals een opengewerkte tekening. Dat is ook het plaatje dat mensen gaan delen.
5. **Export noemt alleen STL.** 3MF hoort ernaast (eis 7), als tweede knop of een keuze in dezelfde rij.
6. **Klein:** de keuze Kijkrichting/Cursor en Kogel/Pen staat als twee rijen onder elkaar; als twee knoppen naast elkaar (`expand=True` in een row) is het compacter en duidelijker dat het een keuze is.

### Nog niet te keuren
Het eigen gezicht (gloed, beweegproef, inklikken), het icoon en de lijstplaatjes. Dat oordeel komt als 1 tot 4 zijn gedaan. Valt het nu op? Nee, maar dat hoort bij een v0.1: de basis is goed.
