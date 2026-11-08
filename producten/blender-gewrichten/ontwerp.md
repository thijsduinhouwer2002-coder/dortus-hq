Akkoord: nee 8 nov 2026, nog niet beoordeeld door Daan

# Blender-gewrichten (werktitel "Click Joints"): ontwerp v1

Bouwbesluit: `organisatie/besluiten.md` (8 nov, Bram) en `platformen/blender/kandidaten-2026-11-07.md` sectie 19. Bewijsproduct: het moet de hele weg leren, niet het meeste geld opleveren. Status: v1.1. Controleur 8 nov: akkoord met correcties, alle tien verwerkt (zie onderaan). Nog niet beoordeeld door Daan.

## Wat het doet
Je hebt een figuur in Blender (gesculpt, gekocht of uit een AI-generator) en je wilt hem printen met bewegende armen, benen en nek. Je kiest het figuur, klikt in de viewport op de plek waar het gewricht moet komen, en de add-on snijdt daar het figuur in twee gesloten, waterdichte delen met een passende kogel en kom (of pen en gat). De speling tussen de delen stel je in millimeters in, zodat het op jouw printer klikt maar niet los valt. Een kleurweergave in de viewport laat vooraf zien of het gewricht past: groen is goed, oranje is krap, rood is te dun of steekt uit het figuur. Daarna exporteer je de delen als STL of 3MF, altijd in millimeters. Is het figuur kleiner dan 5 mm of groter dan 500 mm, dan waarschuwt de add-on en biedt een knop "zet om naar mm".

- **Gratis versie (extensions.blender.org):** kogel- en pengewricht, speling in mm, één gewricht tegelijk, de passingkleur, waterdichte uitvoer. Volledig werkend, geen verwijzing naar de betaalde versie (regels 3.3, 3.10, 6.1 van extensions.blender.org).
- **Betaalde versie (Superhive, $12, lanceerprijs $9, GOK):** scharnier met eindstop voor knie en elleboog, printerprofielen met een testkaartje (print vijf spelingen, kies welke klikt, de add-on onthoudt het per printer), alle ledematen in één keer volgens een poseerbaar sjabloon, magneetgaten en wrijvingsribbels.

## Wat het bewust niet doet
Geen splitsen op printbedmaat en geen zwaluwstaarten (dat doen Dovetail Key, CatPin en de gratis splitsers), geen supports, geen slicen, geen echte meshreparatie: is het figuur niet gesloten, dan een duidelijke melding en een knop "Maak gesloten" die op een kopie een voxel-remesh doet met een voxelgrootte in mm; het origineel blijft onaangetast, geen eigen server of account.

## Hoe het aansluit
Een gewone Blender-extensie in pure Python (eis van extensions.blender.org: geen gecompileerde code), Blender 4.2 LTS tot 5.2 LTS. Paneel in de zijbalk (N), tabblad met de productnaam. Eerst een manifold-check op het figuur. De snede en de gewrichtsdelen maken we met de Boolean-modifier van Blender zelf op gesloten hulpvormen: op 4.5+ de Manifold-solver ("much more robust", ongeveer zo snel als Float, maar alleen op gesloten vormen, GEZIEN https://developer.blender.org/docs/release_notes/4.5/modeling/), op 4.2 tot 4.4 Exact met Self Intersection aan en Hole Tolerant uit. Kogel en kom met minstens 64 segmenten. De passing per gewricht wordt opgeslagen als eigenschap en kleurattribuut, zodat de test hem kan lezen; de passingcontrole met BVH-tree (mathutils) voor wanddikte en uitsteken. De test in de echte Blender bouwt voort op `producten/blender-proef/` en `.github/workflows/blender-proef-e2e.yml` (installeren als extensie, aanzetten, schermafbeeldingen via Xvfb op tak `schermen`). Twee builds uit één bron: de gratis zip bevat de betaalde modules niet. Beide GPL-3.0-or-later (eis van extensions.blender.org 1.1 en Superhive). Geen sleutel: Superhive levert een zip zonder sleutelsysteem en een koper mag een GPL-kopie doorgeven (GEZIEN, support.superhivemarket.com artikel 41, 54, 247). De betaalde code staat niet in de openbare product-repo (afwijking van de gewone regel, want die code verkopen we; voorleggen aan Hans voor het uitbrengen). Beschrijving en plaatjes op extensions.blender.org tonen alleen de gratis functies (ToS 6.2), en de add-on hangt niet af van andere extensies (ToS 5.3). Export: STL met de exporter van Blender, 3MF met een eigen kleine schrijver in pure Python (een zip met XML), want Blender heeft geen eigen 3MF-export (GOK) en we mogen niet afhangen van threemf-io.

## Wanneer is het af (toetsbaar, in de echte Blender op GitHub Actions)
1. Op drie testfiguren (een eenvoudige pop, een gesculpte figuur met veel polygonen, een AI-mesh van ±200K driehoeken, allemaal zelf gemaakt of CC0) levert elk gewricht twee gesloten delen, in 4.2 en 5.2. Gesloten betekent: elke rand heeft precies 2 vlakken, geen randen aan de buitenkant, volume groter dan 0. Plus een vierde figuur die met opzet open en zelfdoorsnijdend is: eerst een nette melding, na "Maak gesloten" twee gesloten delen.
2. Speling: gemeten met BVH `find_nearest` over minstens 500 punten van de kogel naar de kom, bij ingestelde waarden 0,1, 0,2 en 0,3 mm; de gemiddelde afwijking is kleiner dan 0,02 mm (64 segmenten geeft ±0,004 mm facetfout, berekening controleur).
3. Een gewricht op een plek die te dun is, krijgt passing "rood" in de eigenschap van het gewricht (de test leest die) en een melding, geen kapot model. De kleur in de viewport is alleen te zien op de schermafbeelding.
4. Eén gewricht op het figuur van 200K driehoeken duurt onder de 5 seconden met de Manifold-solver (4.5+) op de runner van GitHub. Op 4.2 eerst meten en vastleggen; de eis voor 4.2 volgt na die meting.
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

## Nakijken
- 8 nov 2026, controleur (agent, niet de maker): akkoord met correcties. Verwerkt: kapotte meshes ("Maak gesloten" op een kopie), Manifold-solver op 4.5+ en Exact op 4.2 tot 4.4, twee builds en GPL zonder sleutel, 3MF met eigen schrijver en schaalcheck in mm, eisen toetsbaar gemaakt (gesloten gedefinieerd, meetmethode speling, passing als eigenschap, snelheid per solver, undo in Xvfb), fysieke print als handmatige proef, eerlijk onderscheid in de vraag voor Daan.
