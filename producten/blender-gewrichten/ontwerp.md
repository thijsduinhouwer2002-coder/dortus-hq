Akkoord: nee 8 nov 2026, nog niet beoordeeld door Daan

# Blender-gewrichten (werktitel "Click Joints"): ontwerp v1

Bouwbesluit: `organisatie/besluiten.md` (8 nov, Bram) en `platformen/blender/kandidaten-2026-11-07.md` sectie 19. Bewijsproduct: het moet de hele weg leren, niet het meeste geld opleveren. Status: eerste opzet van Bram, nog niet goedgekeurd door de controleur (regel 0) en nog niet door Daan.

## Wat het doet
Je hebt een figuur in Blender (gesculpt, gekocht of uit een AI-generator) en je wilt hem printen met bewegende armen, benen en nek. Je kiest het figuur, klikt in de viewport op de plek waar het gewricht moet komen, en de add-on snijdt daar het figuur in twee gesloten, waterdichte delen met een passende kogel en kom (of pen en gat). De speling tussen de delen stel je in millimeters in, zodat het op jouw printer klikt maar niet los valt. Een kleurweergave in de viewport laat vooraf zien of het gewricht past: groen is goed, oranje is krap, rood is te dun of steekt uit het figuur. Daarna exporteer je de delen als STL of 3MF.

- **Gratis versie (extensions.blender.org):** kogel- en pengewricht, speling in mm, één gewricht tegelijk, de passingkleur, waterdichte uitvoer. Volledig werkend, geen verwijzing naar de betaalde versie (regels 3.3, 3.10, 6.1 van extensions.blender.org).
- **Betaalde versie (Superhive, $12, lanceerprijs $9, GOK):** scharnier met eindstop voor knie en elleboog, printerprofielen met een testkaartje (print vijf spelingen, kies welke klikt, de add-on onthoudt het per printer), alle ledematen in één keer volgens een poseerbaar sjabloon, magneetgaten en wrijvingsribbels.

## Wat het bewust niet doet
Geen splitsen op printbedmaat en geen zwaluwstaarten (dat doen Dovetail Key, CatPin en de gratis splitsers), geen supports, geen slicen, geen reparatie van kapotte meshes buiten wat nodig is voor een gesloten snede (dan een duidelijke melding met de knop van de gratis 3D Print Toolbox van Blender), geen eigen server of account.

## Hoe het aansluit
Een gewone Blender-extensie in pure Python (eis van extensions.blender.org: geen gecompileerde code), Blender 4.2 LTS tot 5.2 LTS. Paneel in de zijbalk (N), tabblad met de productnaam. De snede en de gewrichtsdelen maken we met de Boolean-modifier van Blender zelf (Exact solver) op gesloten hulpvormen; de passingcontrole met BVH-tree (mathutils) voor wanddikte en uitsteken. De test in de echte Blender bouwt voort op `producten/blender-proef/` en `.github/workflows/blender-proef-e2e.yml` (installeren als extensie, aanzetten, schermafbeeldingen via Xvfb op tak `schermen`). De betaalde versie is dezelfde code met de extra functies aan; hoe de licentie werkt zoeken we uit voor de bouw (Superhive levert een zip, GOK: geen sleutel nodig).

## Wanneer is het af (toetsbaar, in de echte Blender op GitHub Actions)
1. Op drie testfiguren (een eenvoudige pop, een gesculpte figuur met veel polygonen, een AI-mesh van ±200K driehoeken, allemaal zelf gemaakt of CC0) levert elk gewricht twee delen die volgens `bmesh` gesloten (manifold) zijn, in 4.2 en 5.2.
2. De gemeten speling tussen kogel en kom wijkt minder dan 0,02 mm af van de ingestelde waarde.
3. Een gewricht op een plek die te dun is, geeft rood in de passingkleur en een melding, geen kapot model.
4. Eén gewricht op het figuur van 200K driehoeken duurt onder de 5 seconden op de runner van GitHub (GOK op wat redelijk is).
5. Ongedaan maken (Ctrl+Z) zet het figuur terug zoals het was.
6. Schermafbeeldingen van het paneel, de passingkleur en het resultaat staan op tak `schermen` voor Daan.
7. Fysieke print: minstens één echte print van een kogel- en pengewricht door een mens, anders is eis "klikt het" niet bewezen. Dat zetten we op de lijst voor Thijs zodra er een eerste versie is (alleen als hij of iemand die hij kent een printer heeft).

## Vraag voor Daan
Dit is een product voor mensen die figuren printen (actiefiguren, tabletop, cosplay-props): ze delen foto's van hun prints en houden van speelgoedachtige, tastbare dingen. Concurrenten om naar te kijken: Cleave (https://superhivemarket.com/products/cleave), Cut Flex (https://superhivemarket.com/products/cut-flex), ARTICULATOR, FigureCut. Mijn idee voor het eigen gezicht: de passingkleur in de viewport (groen, oranje, rood, als een soort warmtebeeld van de speling) en een gewricht dat even "inklikt" in een korte animatie als je het plaatst. Wat vind jij: klopt dat als onderscheid, en welke naam, kleuren en paneelopbouw horen erbij? Graag je eerste reactie hieronder, ook als het kort is, zodat ik niet bouw wat je straks afkeurt.

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
