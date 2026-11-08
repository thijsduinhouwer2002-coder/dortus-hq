Akkoord: nee 8 nov 2026 09:36, voor main na ronde h en de bouwproef, omdat het gewricht nog niet buigt (snijvlakken op elkaar, bouwproef Bram). Kleur, paneel en 3MF zijn goed. Wat er moet: vorm v0.3 met kegel, gemeten bereik, beweegproef, dan mijn lijstplaatjes. Zie "Reactie van Daan op ronde h en de bouwproef".

Oud: Akkoord: nee 8 nov 2026 07:35, voor main c26267b4 en tak `claude/blender-2026-11-08-g`, omdat Tight nog mosterd is (wordt `#FFEA00`), 3MF ontbreekt en het eigen gezicht (beweegproef, icoon, lijstplaatjes) er nog niet is. Paneel, ring, opengewerkt beeld, Engels en Auto met Good fit zijn goed. Zie beoordeling 2.

Oud: Akkoord: nee 8 nov 2026 04:35, voor v0.1 op main 5928b98, omdat het nog niet opvalt en niet af oogt: Nederlandse teksten in het paneel, het hele figuur wordt mosterdbruin in plaats van een gloed op het gewricht, een rood veld bij Map, en het gewricht zelf is op het hoofdplaatje niet te zien. Zie beoordeling 1 onderaan. Voor een v0.1 is het een goede basis.

**Waarom wij (regel Thijs 8 nov, Bram, bijgesteld 09:35 na de bouwproef):** Click Joints is de enige Blender-add-on die je meteen na één klik laat zien of het gewricht in je printbare figuur klikt (groen, geel of rood op de snede, met de wand in mm) en hoe ver het buigt voor het ergens tegenaan komt (bijvoorbeeld "Bends ±25°"); kogel en pen met die controle zijn gratis, scharnieren, printerprofielen en alle ledematen in één keer kosten $12.
Winkelzin (Engels, overal gelijk): "See if it clicks, and how far it bends, before you print. Ball and pin joints free; hinges, printer profiles and full-figure setup for $12."
- Waarom beter dan de beste concurrent: Cut Flex ($34,99) en Cleave ($23) snijden ook gewrichten, maar meten geen bereik in graden; Cut Flex kijkt één houding per keer na (onderzoek ronde h hieronder, GEZIEN). Of zij de wand per gewricht in mm tonen is nog niet nagekeken: die claim gebruiken we pas na controle. Wij zijn ook goedkoper en hebben een volledig werkende gratis versie.
- Gratis en betaald: de beweegproef (bereik in graden) hoort bij de gratis versie, want het hoofdplaatje en de poster moeten op extensions.blender.org ook mogen (daar alleen gratis functies tonen, ToS 6.2). Betaald blijft: scharnier met eindstop (daar horen de grote hoeken als 0 tot 115° bij), printerprofielen met testkaartje, alle ledematen in één keer, magneetgaten.
- Let op: het bereik in graden is nog niet gebouwd, en het gewricht van nu buigt nog helemaal niet (zie "Bouwproef beweegproef" onderaan). Tot beide opgelost zijn, mag deze zin niet op een winkelpagina.

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
Eerste versie op tak `claude/blender-2026-11-08`, paneel volgens Daan (drie stappen, passing met icoon). Schermen uit de echte Blender: https://raw.githubusercontent.com/thijsduinhouwer2002-coder/dortus-hq/schermen/blender-gewrichten/claude-blender-2026-11-08/5.2.3/1-paneel-x.png en `.../5.2.3/2-gewricht-x.png` (ook 4.2.23). Daan, kijk gerust mee, maar je oordeel is pas nodig na de correcties van de controleur (klikopening in de kom, passing ook op de bodem). Bekende zwaktes (bijgewerkt 8 nov 05:15, ronde b): kleur is nu zichtbaar in de gewone Solid-weergave, maar kleurt nog het hele deel in plaats van een ring rond de snede (punt 2 van Daan staat open); de kogel staat op plaatje 2 alleen in beeld omdat de test deel B 8 mm opschuift, de add-on doet dat zelf nog niet (dat plaatje mag niet in de winkel); nog geen gloed of beweegproef. Besluit: delen worden los geprint en klikken in elkaar (opening ±0,85 keer de kogeldiameter), geen print-in-place.

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

### Na de controleur (8 nov 04:40): nieuwe volgorde en aanvullingen
De controleur (agent) was het grotendeels eens, maar vond de volgorde fout: Engels is snel klaar en maakt niets mooier; de kleur en het zichtbare gewricht bepalen of het opvalt. Eens. **Nieuwe volgorde: 2, 4, 1, 3, 5, 6**, plus:
7. **Zeg waarom.** "Krap" zonder reden helpt niet; speling 0,20 is normaal, dus het is de wand (0,89 mm). Toon de oorzaak: "Tight: wall 0.9 mm (aim for 1.2 mm or more)". En het woord "oranje" hoort niet in de tekst.
8. **Controleknop op de goede plek.** "Controleer figuur" staat bij stap 1 terwijl stap 3 "Controleer" heet. Noem de knop in stap 1 "Check mesh" en stap 3 "Fit and export".
9. **Standaardmaat schaalt mee.** Een kogel van 3 mm in een arm van speelgoedformaat oogt te klein; begin met een diameter van ±60% van de dikte van het onderdeel op de snede.
10. **Kan:** plaatje 3 is nu een bol in een bol, zonder naad of kleur. Met punt 2 en 4 wordt dit vanzelf beter.

### Nog niet te keuren
Het eigen gezicht (gloed, beweegproef, inklikken), het icoon en de lijstplaatjes. Dat oordeel komt als 1 tot 4 zijn gedaan. Valt het nu op? Nee, maar dat hoort bij een v0.1: de basis is goed.

## Ronde b nagekeken (8 nov 05:15, Bram)
Controleur (agent, niet de maker) op tak `claude/blender-2026-11-08-b`: akkoord met correcties. Run 42446806960 groen in 4.2.23 en 5.2.3 op de laatste commit 54e8d2e0, getallen in het log kloppen (GEZIEN). Geen bestaande test zwakker. Marge 1e-9 naar 1e-6 in de eigen nieuwe schaaltoets goedgekeurd (float32 is ±1,2e-7 relatief nauwkeurig). Verwerkt: kleuren nu de heldere kleuren van Daan (#3DDC84, #FFB020, #FF4D4D), `__pycache__` weg met `.gitignore`. Nog open: punt 2 (ring rond de snede in plaats van het hele deel) en punt 4 (uit elkaar schuiven in de add-on zelf, alleen in de weergave). Staan bovenaan `platformen/blender/taken.md`.

## Tussenreactie van Daan (8 nov 05:28, tak `claude/blender-2026-11-08-c`, run 42450482820, commit fc1a657)

Geen oordeel: de tak is nog in de maak. Wel wat ik zag op `5.2.3/1-paneel-x`, `2-gewricht-x` en `3-kijkrichting-x`, zodat Bram er nu iets aan heeft.

1. **Exploded view werkt en is het plaatje.** Op `2-gewricht-x` zie je voor het eerst kogel en kom los van elkaar: dat is wat mensen gaan delen. Twee dingen maken het af: (a) de kom is van deze kant een dicht vlak, je ziet de holte niet; zet de camera voor het plaatje een kwartslag gedraaid (driekwart van voren), zodat je in de kom kijkt; (b) de opening tussen de delen mag ±1,5 keer de kogeldiameter zijn, nu is het krap twee keer de nek.
2. **Oranje botst met de selectierand van Blender.** Blender tekent een geselecteerd object met een oranje rand. Een oranje (Tight) arm die ook geselecteerd is, leest als "dit is geselecteerd", niet als "dit is krap". Daarbij kleurt nog steeds de hele bovenarm (punt 2 uit beoordeling 1 staat open). Voorstel bij het bouwen van de ring: Tight wordt **amber geel `#FFD23F`** in plaats van `#FFB020`, en na "Place joint" wordt de selectie opgeheven of naar het andere deel gezet, zodat de passingkleur nooit naast de oranje rand staat. Groen en rood blijven.
3. **De standaardmaat is te klein.** 3,0 mm in een arm van deze dikte oogt als een speld (`2-gewricht-x`). Punt 9 (±60% van de dikte op de snede) maakt het plaatje meteen beter.
4. **Nog Nederlands** (Plek, Kogel, Speling, Plaats gewricht, Passing: Krap (oranje)), naast een Engelse knop "Exploded view". Gemengd oogt onaf; neem de Engelse woorden uit punt 1 in één keer over.
5. **Goed:** het rode Map-veld is weg en de hint "Leeg: click_joints naast .blend" is rustig (in het Engels: "Empty: saves next to the .blend file"). Kijkrichting/Cursor en Kogel/Pen staan nu als knoppen: goed.

Volgende stap voor mij: een echt oordeel (beoordeling 2) zodra Bram punt 2 (ring) en het Engels op een tak heeft en het vraagt.

## Tussenreactie 2 van Daan (8 nov 06:31, tak `claude/blender-2026-11-08-e`, run 42454838164 groen, commit 456ce02)

Nog geen beoordeling 2: ronde e staat op een tak. Wel wat ik zag op `5.2.3/1-paneel-x` en `5.2.3/2-gewricht-x`, zodat Bram er nu mee verder kan. Staat hier en niet onderaan, zodat het niet botst met wat Bram onderaan op zijn tak schrijft.

**Goed, dit blijft:** de camera kijkt nu in de kom, de holte en de kogel op de nek zijn voor het eerst echt te zien, en de opening tussen de delen is ruim. Geen selectierand meer in beeld. Het paneel is helemaal Engels, de keuzes staan als knoppen, en "Tight: wall 0.89 mm / Aim for 1.5 mm or more" zegt precies wat er mis is en wat je moet doen. Dat is het plaatje dat mensen gaan delen, als de kleur klopt.

**Moet, op volgorde:**
1. **Amber wordt in beeld weer mosterd.** Gemeten op `2-gewricht-x`: de belichte kant is `#A78B2F`, de schaduwkant `#806B24` tot `#8F772C`. Dat is dezelfde vale olijfkleur als in beoordeling 1. Oorzaak (GOK): de Solid-weergave maakt elke kleur ±35 tot 50% donkerder, en donker geel leest als bruin, terwijl donker groen en donker rood groen en rood blijven. Voorstel: een proefstrook in de test, vier cilinders naast elkaar in dezelfde belichting met `#FFD23F`, `#FFE45C`, `#FFF06A` en `#FFC400`, één scherm. Ik kies de kleur waarvan de belichte kant op het scherm boven ±`#E0C040` blijft en die nog naast groen en rood te onderscheiden is. Lukt geen enkele geel, dan kijken we naar een lichtere ring met een donkere rand, maar eerst de proef.
2. **Auto kiest een maat die krap is.** Op `2-gewricht-x` staat Auto aan, Diameter 3.0, en de uitkomst is Tight (wand 0.89 mm). Een automatische maat hoort de goede maat te zijn: kies de grootste kogel waarbij de wand nog minstens 1,5 mm is (of de drempel van Good fit), en pas als dat niet kan de 0,6-regel met de melding waarom. Krijgt een gebruiker met Auto aan een gele ring, dan voelt het alsof de add-on zichzelf tegenspreekt.
3. **Het hoofdplaatje toont Good fit.** De winkel en de README beginnen met een groen gewricht, niet met een waarschuwing. Krap en te dun horen in een tweede plaatje dat laat zien hoe de add-on je helpt. Dat volgt vanzelf uit punt 2.

**Kan:** de regel "Empty: click_joints folder / next to the .blend" staat over twee rijen met een gat ertussen; korter maken tot "Saves next to the .blend" past op één rij.

Volgende stap voor mij: beoordeling 2 zodra punt 1 tot 3 op een tak staan en Bram het vraagt; de proefstrook kijk ik zo snel mogelijk na.

## Beoordeling 2 van Daan (8 nov 07:35, main c26267b4 en tak `claude/blender-2026-11-08-g`)

Bekeken: main run 42455734989 (`5.2.3/1-paneel-x`, `2-gewricht-x`, `3-kijkrichting-x`), tak g run 42458223828 (`2-gewricht-x`, `4-geeltinten-x`) en mijn eigen proefstrook op tak `ontwerp/blender-geel` (run 42458842877, `proef-geel.png` en `proef-geel-standard.png`, Blender 5.2.3, gladde cilinders, Studio-licht Default, kleur volgens Material).

### Wat goed is (afgevinkt uit beoordeling 1)
Punt 1 (Engels), 2 (ring in plaats van hele arm), 3 (geen rood veld), 4 (opengewerkt beeld, kijk in de kom), 6 (keuzes naast elkaar), 7 (zeg waarom), 8 (knopnamen) en 9 (maat schaalt mee) zijn gedaan en in de echte Blender gezien. Op tak g ook mijn tussenreactie 2 punt 2 en 3: Auto kiest 3.0 mm met Good fit, wand 1.55 mm, en het hoofdplaatje is groen. De korte map-hint "Saves next to the .blend" past op één regel. Het paneel is rustig en duidelijk; dit is een goede basis.

### De geelkeuze: `#FFEA00`
Gemeten in mijn proefstrook (GEZIEN, pixels op de belichte kant, midden):

| stof | op het scherm |
|---|---|
| groen nu | `#3B945F` |
| `#FFD23F` (nu) | `#A88D3C` mosterd |
| `#FFE45C` | `#A89848` vaal |
| `#FFF06A` | `#A8A04F` olijf |
| `#FFC400` | `#A78428` oker |
| `#FFEA00` | `#A79C25` geel |
| rood nu | `#A73C3C` |

Wat ik leerde: in Solid met Studio-licht komt **geen enkele kleur boven ±`#AE`** per kanaal; groen en rood ook niet. Mijn eis "belicht boven `#E0C040`" uit tussenreactie 2 kan dus niet, die vervalt. De kleurweergave (AgX of Standard) maakt hier niets uit: beide schermen zijn pixel voor pixel gelijk (GEZIEN). Wat wel uitmaakt is de tint: hoe minder wit erin, hoe meer het geel blijft. `#FFEA00` (verzadigd citroengeel, lineair 1,0 / 0,823 / 0,0) leest als geel en staat duidelijk los van groen en rood; `#FFD23F` en de lichtere tinten worden mosterd of olijf. **Besloten: Tight wordt `#FFEA00`.** Waarom niet oker `#FFC400`: dat leest als amber, maar staat dichter bij de oranje selectierand en bij rood.

Bijvangst: op gladde vlakken (smooth shading) oogt de kleur veel mooier dan op de platte vlakken van de testpop. Dat is aan het figuur van de gebruiker, niet aan ons; voor de lijstplaatjes gebruiken we een glad figuur.

### Wat er nog moet voor akkoord, op volgorde
1. **Tight `#FFEA00`** in `passing.KLEUREN` (één regel), en de proefstrook uit de gewone test laten zodra de keuze erin staat (scheelt tijd per run).
2. **3MF** naast STL (punt 5 uit beoordeling 1, eis 7). Printers van nu (Bambu, Prusa) werken liefst met 3MF.
3. **Het eigen gezicht: de beweegproef.** Nu doet Click Joints wat Cleave en Cut Flex ook doen, alleen netter. Het moment waar iemand een schermafbeelding van maakt, is: het ledemaat rondtrekken en zien waar het botst en hoe ver het buigt ("Bends 0 to 115°"). Bram: zoek eerst uit of Cleave, Cut Flex of FigureCut dit hebben (productpagina en video's), en schrijf dan een kort ontwerp (5 tot 10 regels) hieronder: hoe je het start, wat je ziet, hoe je stopt. Ik reageer de run daarna. Is het te groot voor de eerste versie, zeg dat dan met reden; dan zoeken we samen een kleiner eigen gezicht.
4. **Icoon en lijstplaatjes** maak ik zelf zodra 1 en 2 op main staan: poster "See if it clicks before you print" met een gladde figuur, ring in groen en het opengewerkte gewricht groot.

**Controleur (agent):** eens met `#FFEA00`, de volgorde en de beweegproef eerst onderzoeken. Overgenomen: (a) bij punt 2 hoort ook de knop: "Export STL" wordt een keuze STL of 3MF (of "Export" met een keuze); (b) voor de lijstplaatjes overlays uit (rode as en 3D-cursor lopen nu over de ring op `2-gewricht-x`), kogel duidelijk los, en een figuur waar de ring echt een ring is (nu is het hele zichtbare deel A groen); (c) de kleurweergave maakt alleen in Solid niets uit, in Material Preview kan fel geel bleker worden: Bram, maak bij punt 1 ook één scherm in Material Preview. Kan-punt, houdt akkoord niet tegen: voor mensen zonder groen zien worden ons groen en rood allebei donker olijf (omgerekend door de controleur); een groen met iets meer blauw (richting `#00C389`) helpt. Bram, neem dat mee in dezelfde regel als het geel, dan kijk ik het na in de volgende proefstrook.

Valt het nu op? Nog niet: het is verzorgd, maar nog niet speciaal. Met de beweegproef en een goede poster kan het dat wel worden.

### Beweegproef: wat de anderen hebben en kort ontwerp (Bram, 8 nov, ronde h)
Nagekeken (onderzoeker, productpagina's en docs gelezen met curl, GEZIEN): **Cut Flex** ($34,99, 10+ verkopen) heeft al stap 4 "Pose & check": schuifjes per gewricht, en "Check Pose evaluates rigid overlap at the current sampled pose", één houding per keer, geen hoekbereik, geen rood genoemd, werkt niet met pennen. **Cleave** ($23, 100+) heeft alleen een ghost waar het deel na montage landt, geen draaien. **FigureCut** ($10): alleen pennen, niets. **LayerMechanic** ($25) meet wel "First bind is near 40.5°", maar alleen voor een scharnier dat je zelf modelleert, geen kogel. **Interference Checker** ($6,99) kleurt raakvlakken rood, maar statisch. Dus: "beweging nakijken" is niet nieuw meer, maar een **gemeten bereik in graden, meteen na het maken van de kogel, met de botsplek in rood** heeft niemand.

Ontwerp (v0.2, het eigen gezicht):
1. **Starten:** na Place joint meet de add-on het vanzelf (geen extra knop). Deel B draait om het kogelmidden, in 8 richtingen loodrecht op de as, in stappen van 2,5°, tot het eerste raakpunt met deel A (BVH-overlap, alleen de vlakken binnen ±3 kogeldiameters van het gewricht, zodat het ook op 261K driehoeken onder ±1 s blijft; kogel en kom tellen niet, die hebben speling).
2. **Wat je ziet:** in stap 3 een regel "Bends 0 to 115°" (kleinste en grootste richting, bijvoorbeeld "Bends 40° to 115°"), en in de viewport een dunne waaier (lijnen) met de grens per richting in de passingkleur. Een schuif "Pose" (hoek) plus de 8 richtingen als knoppen draait deel B echt mee, alleen in de weergave (`delta_rotation`, net als Exploded view); voorbij de grens worden de botsende vlakken van deel A rood. Dit is het moment voor de schermafbeelding en de poster.
3. **Stoppen:** schuif terug op 0 of de knop "Reset pose"; de export gebruikt altijd de echte plek (zoals nu bij Exploded view, `echte_plek` krijgt ook de draaiing).
4. **Grens van v0.2:** alleen de kogel (de pen draait vrij om zijn as en meet alleen de draai-aanslag niet), geen ketting van gewrichten, geen draai om de eigen as. Bouwproef eerst: meten in de echte Blender of 8 x 72 stappen op de testarm onder 1 s blijft; zo niet, minder stappen met bisectie naar de grens.
5. **Toetsbaar:** op een staaf met bekende maten klopt de gemeten grens binnen 2,5° met de rekensom (nek tegen de rand van de klikopening), de STL en 3MF blijven gelijk met en zonder pose, en de hoekregel staat in het log.

Niet te groot voor de eerste betaalde versie, wel te groot voor deze ronde: eerst kleur en 3MF op main. **Daan, graag je reactie op dit ontwerp.**

## Ronde c: ring en opengewerkt beeld (8 nov 05:40, Bram) en vraag aan Daan
Op main (run 42451041466 groen in 4.2.23 en 5.2.3, GEZIEN). Controleur (agent, niet de maker): akkoord met correcties; de ene correctie vóór samenvoegen (een tweede gewricht of Maak gesloten op een verschoven deel B bakte de verschuiving in) is verwerkt en getoetst (regel `TWEEDE` in het log: verschil 0,00000 mm).
- **Punt 2 (ring):** het figuur houdt zijn eigen materiaal. Alleen vlakken met een hoekpunt binnen 3 mm van het snijvlak, plus kogel, nek, pen en kom, krijgen de passingkleur (helder: #3DDC84, #FFB020, #FF4D4D). Bij de testarm is ±38% van het oppervlak gekleurd, ring, kogel en kom volledig. Geen zachte overgang. Bij een grof figuur (lange vlakken) kleurt meer mee; een klein deel (een hand) is bijna helemaal ring.
- **Punt 4 (opengewerkt):** instelling "Exploded view" in stap 2, standaard aan: deel B schuift 1,5 keer de kogeldiameter langs de as, alleen in de weergave (`delta_location`). De STL van deel B is met en zonder gelijk tot op 0,000000 mm. Bekend: Ctrl+A Apply Transforms op deel B bakt de verschuiving in; nog op te vangen.
- Tekst in het paneel is nog Nederlands (punt 1 komt hierna).

**Daan, graag je oordeel over punt 2 en 4:** https://raw.githubusercontent.com/thijsduinhouwer2002-coder/dortus-hq/schermen/blender-gewrichten/claude-blender-2026-11-08-c/5.2.3/2-gewricht-x.png (en straks dezelfde op `main/`). Zelf gezien: lijf grijs, smalle oranje band op deel A, kogel los en goed te zien; deel B is klein en daardoor bijna helemaal oranje. Is de band zo goed, of wil je een zachte overgang of een smallere ring?

### Ronde e (bouwer, tak `claude/blender-2026-11-08-e`)
Verwerkt uit de tussenreactie van Daan (8 nov 05:28). Runs 42453798012 en 42454200676 groen in 4.2.23 en 5.2.3 (GEZIEN).
- **Tight is amber geel #FFD23F** (lineair 1,0 / 0,644 / 0,05) in plaats van #FFB020, in materiaal en ring (één bron: `passing.KLEUREN`). Groen en rood blijven.
- **Na Place joint is niets geselecteerd.** Deel A blijft actief zonder selectie (geen rand), zodat het paneel de passing toont. Export en Exploded view vonden de delen al op `cj_deel`, niet op selectie; de export zet de selectie daarna terug zoals hij was. Log: `SELECTIE na plaatsen: geselecteerd=[] actief=arm_A`, export en Exploded view werken, na export nog steeds niets geselecteerd. Elke plaatsing in de test toetst nu "niets geselecteerd".
- **Automatische kogelmaat (punt 9):** knop "Auto" naast Diameter, standaard aan. Bij Place joint: smalste breedte in het snijvlak (stralen in 36 richtingen, voor plus achter), diameter 0,6 keer die breedte, afgerond op 0,5 mm, 2 tot 50 mm. De maat komt in het veld Diameter te staan, zodat de gebruiker hem ziet. Zelf een diameter typen zet Auto uit. Waarom zo: één vinkje dat je ziet en terug kunt zetten is duidelijker dan een verborgen vlag, en het veld laat altijd de echte maat zien. Ligt de cursor buiten het figuur, dan blijft de oude maat. Testarm (10 mm dik): breedte 10,0 mm, diameter 6,0 mm (0,60 keer), passing Good fit, wand 1,56 mm (GEZIEN, beide versies).
- **Plaatje 2:** camera driekwart van voren, langs de as (kijkrichting 0,8 / 0,6 / -0,3), afstand 24. Je kijkt in de opening van de kom van deel B en ziet de holte, met de kogel op de nek van deel A ervoor. Zelf bekeken in 4.2.23 en 5.2.3. Geen oranje selectierand meer in beeld.
- **Paneel stap 3:** de regel "Wall: ..." staat er alleen nog bij Good fit; bij Tight en Too thin staat de wand al in de reden. Veld "Diameter (mm)" is breder gemaakt naast Auto (werd afgekapt).
- Geen bestaande toets zwakker of gewijzigd in verwachting. `hulp.plaats` zet Auto uit, want die toetsen kiezen de diameter zelf. Nog open: de paneeltekst zelf wordt niet automatisch getoetst (alleen op de plaatjes gezien).

## Ronde d en e nagekeken en op main (8 nov 06:40, Bram) en vraag aan Daan: beoordeling 2
Controleur op tak d (Engels): akkoord met correcties; de wand in de passingtekst staat nu op twee decimalen (anders "wall 1.5 mm (aim for 1.5 mm)" bij 1,46), de dubbele regel "Wall:" is weg. Testwijziging "niet gesloten" naar "not watertight" apart goedgekeurd. Controleur op tak e: akkoord met één tekstcorrectie (verwerkt). Run 42454838164 groen in 4.2.23 en 5.2.3 (GEZIEN).
- Tight is nu amber geel #FFD23F, groen en rood bleven.
- Na Place joint is niets geselecteerd (deel A blijft actief), dus geen oranje selectierand naast de passingkleur.
- Knop **Auto** naast Diameter, standaard aan: 0,6 keer de smalste breedte op de snede, afgerond op 0,5 mm (arm van 10 mm: kogel 6,0 mm, Good fit, wand 1,56 mm, GEZIEN). Zelf typen zet Auto uit.
- Plaatje 2 kijkt driekwart in de kom; je ziet de holte en de kogel ervoor.
- Alle zichtbare tekst in het paneel is Engels (materiaalnamen in de Outliner nog niet, volgt).

Bekend en open: de arm van de testpop is maar 5 mm dik, dus Auto geeft daar 3,0 mm en Tight (wand 0,89 mm). De wand is ongeveer 0,2 keer de dikte; onder ±5 mm dikte wordt het rood. Nog geen melding als Auto geen breedte vindt.

**Daan, graag beoordeling 2** van wat nu op main staat: https://raw.githubusercontent.com/thijsduinhouwer2002-coder/dortus-hq/schermen/blender-gewrichten/main/5.2.3/1-paneel-x.png en https://raw.githubusercontent.com/thijsduinhouwer2002-coder/dortus-hq/schermen/blender-gewrichten/main/5.2.3/2-gewricht-x.png (zelfde als https://raw.githubusercontent.com/thijsduinhouwer2002-coder/dortus-hq/schermen/blender-gewrichten/claude-blender-2026-11-08-e/5.2.3/2-gewricht-x.png). Vraag erbij: op het plaatje is de pop dun, dus staat er Tight in amber; wil je voor het hoofdplaatje een dikkere arm zodat het Good fit (groen) toont, of juist Tight met uitleg omdat dat laat zien wat de add-on doet?

## Ronde g: tussenreactie 2 van Daan verwerkt (8 nov 07:30, Bram), tak `claude/blender-2026-11-08-g`
Runs 42458761523 en 42459047164 (laatste commit 6c9ef28) groen in 4.2.23 en 5.2.3 (GEZIEN). Controleur: akkoord met correcties (alleen tekst, verwerkt).
1. **Proefstrook (moet 1):** plaatje `4-geeltinten-x.png`: zes cilinders in dezelfde kijkrichting en Solid-belichting als plaatje 2 (#FFD23F, #FFE45C, #FFF06A, #FFC400, en groen en rood ter vergelijking), kleurcode eronder. De test meet per cilinder de kleur op het scherm (17 punten langs het midden, regels `GEEL` in het log). Uitslag (GEZIEN, 5.2.3 met AgX; in 4.2.23 belicht gelijk op 1 tot 2 eenheden na, schaduw tot 5 eenheden):

   | kleur | belicht | schaduw |
   |---|---|---|
   | #FFD23F | #A78C33 | #443513 |
   | #FFE45C | #A89843 | #423717 |
   | #FFF06A | #A9A14C | #504A20 |
   | #FFC400 | #A98524 | #624A09 |
   | groen #3DDC84 | #37955E | #19643B |
   | rood #FF4D4D | #AA4040 | #822525 |

   Geen enkele geel komt boven #E0C040: elke kleur, ook groen en rood, komt uit op ±0,66 keer de opgegeven waarde. Het ligt niet aan de kleurweergave: met View Transform "Standard" in plaats van AgX (plaatje `5-geeltinten-standard-x.png`) zijn de getallen gelijk. Het ligt dus aan de Solid-weergave zelf (waarschijnlijk de belichting, GOK), en dat is wat een gebruiker in Solid ziet. Dus de grens #E0C040 haalt geen enkele kleur in dit beeld. Wat wel verschilt is hoe geel hij blijft: #FFF06A houdt groen/rood 0,95 (leest als geel), #FFD23F maar 0,84 (leest als mosterd), #FFC400 0,79 (oker). Mijn voorstel: **#FFF06A**, of de lichtere ring met donkere rand die je noemde. Daan kiest.
2. **Auto kiest de grootste Good fit (moet 2):** vanaf 0,6 keer de breedte (bovengrens) in stappen van 0,5 mm omlaag tot de passing groen is; lukt groen nergens, dan de grootste Tight met de melding "Auto: no size gives a good fit here (mesh X mm thick at the cut)"; ook geen Tight, dan rood en niet snijden. Getoetst (GEZIEN): staaf 7 mm: 3,5 mm Good fit (wand 1,55), 4,0 mm zou Tight zijn; staaf 5 mm: 2,5 mm Tight met melding; arm 10 mm: 6,0 mm Good fit zoals eerst.
   Daarbij gevonden en gerepareerd: een kogel onder ±4,5 mm kon nooit Good fit zijn, hoe dik het figuur ook was, want de bodem van deel B naast de klikopening bleef onder 1,5 mm. Het kogelmidden komt bij kleine kogels nu zo hoog dat die bodem 1,55 mm is (de nek wordt iets langer, grote kogels blijven gelijk). De ring kleurt tot de echte bovenkant van de kom.
3. **Hoofdplaatje Good fit (moet 3):** de pop op de plaatjes heeft dikkere en langere armen (8 mm dik, 40 mm lang); regel `HOOFDPLAATJE passing=groen keuze=goed`: Auto koos 4,5 mm, wand 1,54 mm (net boven de grens). Tight en Too thin blijven in de achtergrondtest (dunne pop) voor het tweede plaatje later.
- **Kan:** de map-hint is één regel: "Saves next to the .blend" (of "Saves to a temporary folder" als het bestand nog niet is opgeslagen).
- Testwijziging (apart goedgekeurd door de controleur bij de herkeuring van ronde g, zie logboek): de kijktoets in `schermen.py` staat 2 mm hoger in het been (z = -12), omdat het gewricht van 3 mm nu langer is; drempels gelijk.

## Ronde h: kleur, Material Preview en 3MF (8 nov 08:40, Bram) en vraag aan Daan
Tak `claude/blender-2026-11-08-h`, controleur (agent, niet de maker): akkoord met correcties, de twee moet-punten (3MF-toets weer streng op 0 foute randen, architectuur.md bij) verwerkt.
- **Punt 1:** Tight is `#FFEA00` (lineair 1,0 / 0,823 / 0,0). Groen is `#00D696`: dezelfde tint als `#00C389` (blauw gedeeld door groen 0,70), maar even helder als het oude groen, omdat Solid alles al donkerder maakt. Rood bleef. De proefstrook met vier geeltinten is uit de gewone test. Nieuw plaatje 4: `4-material-preview-x.png`, de drie echte materialen van de add-on als gladde cilinders in Material Preview. Gemeten op het X-scherm (GEZIEN, belicht / schaduw): 5.2.3 Good fit `#67B193` / `#419E80`, Tight `#C1B35C` / `#A89E31`, Too thin `#D1675F` / `#A63D39`; 4.2.23 Good fit `#4FA281`, Tight `#B4A544`, Too thin `#C1534D`. In Material Preview wordt het geel dus iets bleker (witte glans), maar het blijft geel en los van groen en rood.
- **Punt 2:** 3MF naast STL. Boven de exportknop twee knoppen STL | 3MF, de knop heet dan "Export STL" of "Export 3MF". Blender heeft geen eigen 3MF-export, dus een eigen schrijver (`drie_mf.py`), één bestand per deel in mm. De test leest het bestand terug: maat gelijk tot 0,00000 mm, volume gelijk, gesloten met dezelfde draairichting, ook in een scene in meters.
- **Punt 3:** onderzoek en kort ontwerp beweegproef staan hierboven onder beoordeling 2.

**Daan, graag je oordeel** over https://raw.githubusercontent.com/thijsduinhouwer2002-coder/dortus-hq/schermen/blender-gewrichten/main/5.2.3/2-gewricht-x.png en https://raw.githubusercontent.com/thijsduinhouwer2002-coder/dortus-hq/schermen/blender-gewrichten/main/5.2.3/4-material-preview-x.png (na samenvoegen; tot dan dezelfde onder `claude-blender-2026-11-08-h/`), en over het ontwerp van de beweegproef.

## Bouwproef beweegproef (8 nov 09:30, Bram): het gewricht van nu buigt 0°
Bouwproef `proef/proef_beweeg.py` op main (run 42467258159 groen in 4.2.23 en 5.2.3, GEZIEN). Controleur (agent, niet de maker): akkoord met correcties, alle vier verwerkt.
- **Grootste vondst, een fout in het product:** de snijvlakken van deel A en deel B liggen precies op elkaar (0 mm, de 0,0137 mm zit tussen cursor en snijvlak). Bij elke draaiing zakt de rand van B in A: bij 2,5° al 0,215 mm (5·sin 2,5° min 3,486·(1 min cos 2,5°), nagerekend door de controleur). Een geprint gewricht van nu klikt wel, maar buigt niet; alleen de speling geeft ±1,9° rammel. Gemeten: "Bends 0.0 to 0.0 degrees" op arm en staaf, in alle 8 richtingen.
- **Wat de vorm toelaat als de snijvlakken vrij zijn:** de voet van de nek komt tegen de wand van de klikopening. Rekensom staaf (kogel 5 mm, opening 0,85r, nek 0,48r, kogelmidden 3,486 mm boven het snijvlak): 16,20°, gemeten precies 15,0° (laatste vrije stap van 2,5°). Dus ook met een spleet maar ±15°.
- **Tijd:** een bereik met twee grote delen (45K tegen 62K vlakken) kost ±40 tot 50 ms per toets; zonder snijvlak 0,84 s (5.2) en 1,57 s (4.2) op de arm. De 1 s-eis is alleen gehaald met een kleine uitsnede (nek, 0,13 tot 0,19 s). Grove stappen met bisectie missen soms een kort raakmoment (op de staaf gezien). Overlap van oppervlakken ziet ook niet dat een deel in het volume van het andere zakt: in de add-on is een binnen-of-buiten-toets nodig.

**Besluit (Bram):** eerst de vorm repareren, dan pas de beweegproef in de add-on. Een gewricht dat niet buigt is geen product, wat het paneel ook toont.
**Voorstel vorm v0.3 (controleur, nagerekend):** een spleet alleen is lelijk en rammelt (voor 16° is 1,26 mm nodig), een langere nek maakt het slechter. Wel: onder de klikrand een kegelvormige opening (verzinking) in deel B met tophoek ±25°, en het snijvlak als V (kegel van 25° op deel A, top 0,36 mm onder het snijvlak). Dan begrenst alleen de klikrand tegen de nek: **±25,5° per richting** (51° totaal) bij nek 0,48r, **±30°** bij nek 0,40r. Meer kan niet zonder de klikopening ruimer te maken. Risico: de klikring wordt dunner; de passingcontrole moet die ring meten en een echte print moet uitwijzen of hij nog klikt.

**Daan, graag je reactie:** (1) is ±25 tot 30° genoeg als eigen gezicht voor de kogel (nek, schouder, heup), met de grote hoeken (knie 0 tot 115°) bij het betaalde scharnier? (2) Een V-snede is zichtbaar op het figuur: liever V op deel A (naad loopt schuin) of een rechte naad met een smalle afgeschuinde rand op beide delen?

## Reactie van Daan op ronde h en de bouwproef (8 nov 09:36 UTC)
Bekeken: `5.2.3/2-gewricht-x.png` en `5.2.3/4-material-preview-x.png` op `schermen/blender-gewrichten/main` (GEZIEN met de Read-tool).

**Ronde h: goed.** Geel `#FFEA00` leest in Material Preview als geel, los van groen en rood; het groen `#00D696` is frisser en blauwer dan eerst, de drie zijn ook in grijs uit elkaar te houden. De keuze STL | 3MF boven de knop, met "Export STL" of "Export 3MF" op de knop zelf, is precies goed: één klik minder dan een menu en je ziet wat je krijgt. Punt 1 en 2 van beoordeling 2 zijn af.

**De bouwproef is de belangrijkste vondst van vandaag.** Een gewricht dat klikt maar niet buigt, is geen gewricht. Eens met je besluit: eerst de vorm, dan pas de beweegproef. Dit gaat voor alles, ook voor mijn lijstplaatjes.

**Vraag 1, is ±25 tot 30° genoeg?** Ja, kies nek 0,40r voor **±30°** (60° totaal), als de passingcontrole de klikring meet en hem goed keurt; anders 0,48r en ±25°. Waarom: het eigen gezicht is niet de grootte van de hoek, maar dat je het **meet en ziet** voor je print ("Bends ±30°", waaier, rood waar het botst). Niemand anders laat dat zien (jouw onderzoek). ±30° is eerlijk voor een klikkogel en genoeg voor nek, schouder, pols en heup bij een pop of figuur. De grote hoeken (knie, elleboog 0 tot 115°) horen bij het scharnier, dat mag het betaalde deel worden. Schrijf nooit meer graden op het paneel dan gemeten.

**Vraag 2, V of rechte naad?** De V (kegel) op deel A, hol in deel B. Waarom: een smalle afschuining op de rand helpt alleen aan de buitenkant; het hele snijvlak moet vrij zijn om te kunnen draaien, en dat geeft alleen een kegel met de top bij het draaipunt. Op een rond lid (arm, been) is de naad van een kegel aan de buitenkant toch een rechte ring, dus je ziet de V niet. Eisen: (a) in rechte stand sluit de naad tot op de speling (0,2 mm), geen zichtbare spleet; (b) bij een plat of hoekig lid kijken we samen op een plaatje of de naad mooi genoeg is, anders daar een kleinere tophoek; (c) de kegel komt in de STL en 3MF, en de toets "gesloten, zelfde draairichting" blijft gelden.

**Volgorde voor akkoord, nieuw:** (1) vorm v0.3 met kegel en klikring in de passingcontrole, (2) gemeten bereik op het paneel ("Bends ±30°"), (3) waaier en rood in de viewport (de beweegproef uit je ontwerp, dat ontwerp keur ik goed), (4) icoon en lijstplaatjes door mij, met het buigende gewricht als hoofdbeeld. Kan-punt voor (3): de waaier moet op de lijstplaatjes groot en dik genoeg zijn om op 1280 breed te zien.

`Akkoord: nee` blijft, alleen om de vorm. Kleur, paneel en export zijn goed.

## Vorm v0.3 (8 nov 10:15, Bram, run 13): bolnaad in plaats van V, tak `claude/blender-2026-11-08-j`
**Afwijking van het voorstel (V-kegel), met reden.** Bij het bouwen bleek: een kegel (V) waarbij de naad in rechte stand dicht zit (eis (a) van Daan) kan niet draaien. Draai je deel B om het kogelmidden, dan wordt aan de kant die zakt de kegelwand van B steiler dan die van A en zakt B in A, wat de tophoek ook is. De kegel van de controleur (25°, top 0,36 mm onder het snijvlak) werkt alleen als B vlak blijft, en dan staat er buiten op een staaf van 10 mm een spleet van ±2,7 mm: dat botst met eis (a). De enige naad die in rechte stand dicht is en toch vrij draait, is een **bol om het draaipunt** (het kogelmidden). Dat is ook wat Daan bedoelde met "het hele snijvlak moet vrij zijn".
- **Vorm:** deel A eindigt op een holle bol om het kogelmidden (straal: grootste straal van het figuur rond de as plus 0,5 mm plus speling), deel B vult die bol; tussen beide precies de speling. Buiten de bol loopt de vlakke snede nu door het kogelmidden. Nek 0,40r (keus Daan, ±30°). Onder de klikrand een trechter met halve tophoek gelijk aan de berekende grens plus 3°, zodat alleen de klikrand tegen de nek komt.
- **Wat je ziet:** op een rond lid een rechte ring, ±1,2 mm boven de plek waar je klikte (staaf 10 mm, kogel 5 mm). Bij een plat of hoekig lid loopt de ring golvend: plaatje voor Daan (eis (b)).
- **Rekensom grens:** t = acos(n / (r+s)) - atan2(d, a), met d = wortel((r+s)² - a²). Kogel 5 mm, speling 0,2: ±30,2°.
- **Passing:** de schil van B tussen kom en bolnaad, en nieuw de wand tussen trechter en huid (loodrecht op de trechter gemeten). De klikring zelf heeft een hoek van ±95° (was 128°), dus niet scherp.
- **Bekende zwakte:** de rand van deel A aan de buitenkant wordt een dunne rand (hoek ±25° bij marge 0,5 mm). Meer marge maakt die rand dikker maar de trechterwand in B dunner. Eerst meten in de echte Blender, dan kiezen.
- **Stand:** gebouwd, nog niet nagekeken. De e2e-toetsen voor de klikopening (meet onder de klikrand, waar nu de trechter zit), de wand in de meterscene en het snijvlak naast de cursor gaan uit van de oude vorm en moeten mee; die wijziging moet de controleur apart goedkeuren (geen toets zwakker).
