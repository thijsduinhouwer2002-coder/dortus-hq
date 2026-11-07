# Blender: wat bouwen we? Kandidaten (7 nov 2026, Bram)

Status: nagekeken door de controleur (akkoord met correcties, verwerkt). Nog geen bouwbesluit: A valt af, B en C worden eerst verder uitgezocht.

## 1. Eigen meting per categorie (GEZIEN, data van Vera)
Bron: `platformen/verkenner/data/superhive-steekproef-2026-11-07.jsonl`, alleen betaalde add-ons van 2 tot 6 maanden oud (n=316). Netto per maand = teller (ondergrens) x (65% van de prijs min $0,49) / leeftijd, dus GOK op GEZIEN.

| Categorie | n | 10+ verkopen | 100+ | samen netto per maand | mediaanprijs |
|---|---|---|---|---|---|
| modeling | 104 | 37% | 9 | ±$22.000 | $12 |
| interface | 28 | 29% | 2 | ±$6.100 | $9 |
| rendering | 62 | 34% | 4 | ±$4.900 | $15 |
| rigging | 23 | 52% | 2 | ±$1.500 | $20 |
| import-export | 28 | 25% | 2 | ±$730 | $15 |
| materials | 31 | 23% | 2 | ±$560 | $12 |
| animation | 12 | 17% | 0 | ±$210 | $20 |
| asset-management | 23 | 13% | 0 | ±$90 | $12 |
| vse | 5 | 20% | 0 | ±$230 | $14 |

Modelleren levert het meeste geld. Binnen modelleren vallen drie groepen op: opschonen van AI- en scanmeshes (Smart Remesh $17 2.500+, Nitro Retopo $25 300+, Smart Segmentation $12 300+, BWrap $30 200+), voorbereiden voor 3D-printen (Dovetail Key $18 800+ in 4 maanden) en precisie/CAD (Forge CAD $49 300+, JointLab $65 20+). Allemaal GEZIEN teller.

## 2. Wat kopers en gebruikers zeggen (onderzoeker, nagekeken: zie onder)
- AI-meshes (Meshy en dergelijke) opschonen en printklaar maken is de rode draad in de reviews van Smart Remesh, Smart Segment en CatPin (GEZIEN, https://superhivemarket.com/products/smart-remesh/ratings).
- Kopers van Dovetail Key vragen om scharnieren voor actiefiguren: kogelgewricht ("ball and cup"), pen, draaipen, en om de snijlijn te kunnen aanpassen (GEZIEN, https://superhivemarket.com/products/dovetail-key/ratings). Klacht: haperende voorbeeldweergave, "vibe coded".
- Forge CAD (gemiddeld 3 uit 4): crashes, zwakke documentatie, geen antwoord van de maker (GEZIEN, https://superhivemarket.com/products/forge-cad-precision-modelling-in-blender/ratings).
- SketchUp-overstappers zoeken precies modelleren: https://blenderartists.org/t/1643140, https://blenderartists.org/t/1630927 (DERDEN).
- Reddit was niet te lezen vanaf ons netwerk; devtalk nog niet bekeken.

## 3. Kandidaten met scores (1 tot 5, hoger is beter)
Vraag = bewijs dat mensen het willen. Betaalbewijs = vergelijkbare betaalde add-ons verkopen. Concurrentie = 5 bij weinig goede concurrenten. Bouwtijd = 5 bij klein. Opvallen = kan het er speciaal en mooi uitzien (lat van Thijs, 7 nov).

| | Vraag | Betaal | Concurrentie | Bouwtijd | Opvallen | Totaal |
|---|---|---|---|---|---|---|
| A. Gewrichten voor printbare figuren (kogel, pen, draaipen, met speling per printer) | 3 | 4 | 1 | 3 | 5 | 16 (was 18) |
| **B. AI-model naar printklaar in één paneel** (samenvoegen, waterdicht, mm, wanddikte, splitsen) | 4 | 4 | 2 | 3 | 3 | **16** |
| **C. Precies modelleren voor SketchUp-overstappers** (push/pull, maten intypen) | 4 | 5 | 2 | 1 | 4 | **16** |
| D. 3D naar vlakke onderdelen voor laser/CNC | 3 | 1 | 2 | 5 | 2 | 13 |
| E. Export naar spelmotoren | 2 | 3 | 1 | 4 | 1 | 11 |

Onderbouwing per kandidaat (cijfers GEZIEN door de onderzoeker op superhivemarket.com en extensions.blender.org, 7 nov):
- **A:** JointLab $65 20+ (1 ster: dwingt een eigen server af), Cleave $23 90+ (belooft ook kogelgewrichten). Splitsers verkopen goed maar dat hoekje is vol: Dovetail Key 800+, CatPin $24 400+, Split-3DPrint $22 400+. Gratis: Easy-Print 7K, EasySlice 6K downloads. **Correctie controleur: het gat is er niet.** Cleave ($23 tot $28, 90+ in ±2 maanden, ±45 per maand GOK op GEZIEN) heeft sinds v1.6 kogelgewrichten voor poseerbare figuren, aanpasbare snijlijnen en controle per printer: precies de wensen van de Dovetail-kopers (https://superhivemarket.com/products/cleave). Verder Cut Flex ($34,99, 10+ in 17 dagen, 15 gewrichtsoorten, https://superhivemarket.com/products/cut-flex), ARTICULATOR ($1, 30+ in 3 maanden, https://superhivemarket.com/products/articulator---easy-figure-joint-generator), LayerMechanic ($25, 26 dagen, nog geen teller) en Fit & Tolerance Test Generator ($7, 13 dagen). Alles GEZIEN 7 nov. Op extensions.blender.org geen gratis gewrichten-add-on gevonden, wel gratis splitsers met verbinders. Visueel sterk blijft waar (GOK), maar vier betaalde makers, twee in de laatste maand erbij.
- **B:** sterke vraag, maar de gratis 3D Print Toolbox (680K downloads) doet de controles al en Smart Remesh (2.500+) en OkTopo ($24, 700+) zitten op het opschonen. Verschil maken is lastig (GOK).
- **C:** grootste geld (Construction Lines $11 7.400+, Design Magic $29 2.600+, Seamless CAD $14,90 300+ in 3 maanden), maar groot en moeilijk stabiel te krijgen. Te groot als eerste product.
- **D:** betaald verkoopt weinig (Cross Section Maker $2,50 200+ in 5 jaar), veel gratis. Hooguit gratis lokmiddel.
- **E:** vol, niets duidelijks dat ontbreekt.

## 4. Keus
Eerste voorlopige keus was A. Na de controle valt A af: de wensen die we zagen zijn al vervuld door Cleave, en er komen elke maand nieuwe gewrichtenmakers bij. Daarmee staan B en C gelijk (16) en is er geen duidelijke winnaar. Ik neem nu geen bouwbesluit (geen haast, besluit Thijs 6 nov). Volgende stap: B en C verder uitzoeken (wat doet het gratis 3D Print Toolbox niet, waar klagen kopers van Construction Lines en Seamless CAD over, kan een kleiner deel van C als eerste product), en kijken of er in modelleren nog een kandidaat is die we missen.

## Nakijken
- 7 nov 22:20, controleur (agent, niet de maker): akkoord met correcties. Tabel klopt (n=316, elke rij nagerekend; vse ontbrak, toegevoegd). Zes+ cijfers tegen de bron gecontroleerd, alles klopt. Gat voor A bestaat niet (zie A). Labels per cijfer beter maken bij de volgende versie.

## 5. Ronde 2: B en C verder uitgezocht (7 nov 22:25, onderzoeker; nagekeken 22:35, akkoord met correcties, zie onder)
Alle tellers GEZIEN 7 nov op superhivemarket.com en extensions.blender.org.
- **B:** de gratis 3D Print Toolbox (679.674 downloads, v1.5.0 van 19 okt 2026, https://extensions.blender.org/add-ons/print3d-toolbox/) doet al controleren, Make Manifold, uithollen, schalen en exporteren. Niet op de pagina: polycount naar een doel, losse delen samenvoegen, splitsen op printbedmaat, 3MF, afvoergaten (GOK dat het echt ontbreekt). Betaalde add-ons die op AI-mesh naar print mikken verkopen zwak: Mesh Prep Studio $22 30+ in 7 maanden (niet teruggevonden door de controleur, dus niet nagekeken), PrintPrep $20 10+ in ruim 1 jaar, 3DQuads Print Ready 10+ in 8 maanden, Quadify Bridge $19 10 in 6 maanden, QuadMend $15 geen teller. Oudere printhulpen: Clean Mesh $5 300+, Ultimate STL Export $10 100+, Print Support Pro $30 70+ en 3D Print Toolbox 4 $9 70+ (die twee niet teruggevonden door de controleur), allemaal ±2 jaar. Wel betaalbewijs voor AI-mesh opschonen: Quadify $25 tot $150, 400+, ruim 1 jaar, vooral retopologie (https://superhivemarket.com/products/quadify). Het geld in AI-meshes opschonen zit bij games (Smart Remesh 2.500+, OkTopo $24 700+), niet bij printen.
- **C:** Construction Lines ($11, 7.400+, gemiddeld 4 uit 56) doet maten intypen en push/pull al goedkoop en wordt bijgehouden. Maatvoering is bezet door Snap Measure ($25, 200+, 5 sterren) en Dimensions and Lines ($18, 200+, 5 sterren). Seamless CAD ($14,90, nu $9,90 voor de komende ±100, 300+ in 3 maanden) levert voor Windows, Linux en macOS, maar is alleen op Windows goed getest (correctie controleur, https://superhivemarket.com/products/seamless-cad). Geen klein deel van C met zwakke concurrentie gevonden.
- **Derde kandidaat:** AI-mesh in onderdelen splitsen (Smart Segmention van Milad Kambari, $12, 300+ in 3 maanden, https://superhivemarket.com/products/smart-segmention-), maar die maker zit er al sterk.

**Mijn oordeel (Bram):** nog steeds geen kandidaat die alle vier tegelijk haalt (vraag, betaalbewijs, zwakke concurrentie, haalbaar). B smal heeft zwakke concurrentie maar ook zwak betaalbewijs: printhulpen verkopen slecht. Ik besluit nog niet. Volgende run: niet verder op deze drie ideeën, maar systematisch zoeken naar gaten. Aanpak: per tag in modelleren en rigging de best verkochte add-ons van het afgelopen jaar, en per stuk de klachten in ratings waar nog niemand iets voor maakte. Daarnaast de geldhoek AI-mesh opschonen voor games bekijken (sterk betaalbewijs, maar sterke spelers).

## 6. Ronde 3: systematisch gaten zoeken (7 nov 22:40, onderzoeker; nagekeken 22:50, akkoord met correcties, zie sectie 7)
Aanpak: per categorie (modeling, rigging, interface, rendering, animation) de eerste pagina gesorteerd op verkoop (/categories/<cat>/browse?sort_sales=desc), 78 producten, van 18 de ratings gelezen. Let op: de ratingspagina toont eerst de beste sterren, klachten staan op de laatste pagina. Alles GEZIEN 7 nov.

- **Gat 1 (sterkst): opvolger van Pie Menu Editor voor Blender 5.** Pie Menu Editor ($16, 2.400+, ruim 4 jaar, ondersteunt tot Blender 4.3, https://superhivemarket.com/products/pie-menu-editor). De tien nieuwste reviews gaan over Blender 5: "please make it work on 5.2!", "Can't upgrade to Blender 5 without this", "happy to pay for the update"; 1 ster: "Stopped development for 5.0+. Messaged him, no response" (https://superhivemarket.com/products/pie-menu-editor/ratings). Volgens een review bestaat er een goedgekeurde fork alleen voor kopers (niet gevonden). Concurrentie: PieMaster $20, 100+, 5 maanden, 9 beoordelingen; Quick Pie & Favorites $2, 10+; Flick Pie $4,99, 10, 1 maand. Op extensions.blender.org alleen kleine losse pies. Bouwtijd middel tot groot (GOK). Past bij een verlaten bestseller met kopers die zeggen te willen betalen.
- **Gat 2: bone-jiggle die goed bakt.** BoneDynamics Pro ($15, 6.000+, ruim 5 jaar): "baking doesn't work", "not compatible at all with Auto Rig Pro" (https://superhivemarket.com/products/bonedynamics/ratings). Swingy Bone Physics ($14,79, 1.700+): kapot na hernoemen of dupliceren, geen linken, tot 3 GB geheugen (https://superhivemarket.com/products/swingy-bone-physics/ratings). Maar veel gratis en betaalde concurrenten (wiggle-2, jiggle-physics, easy-jiggle, goo-physics). Het gat is kwaliteit, niet afwezigheid. Bouwtijd middel (GOK).
- **Gat 3 (zwakker): pivot-tool.** Pivot Transform ($15, 2.600+, 7 jaar) verloor functies in de versie voor Blender 5, drie keer 1 ster (https://superhivemarket.com/products/pivot-transform/ratings). Maar veel gratis pivot-tools en MACHIN3tools ($20, 36.400+) doet het ook.
- Verworpen: Layer Painter (verlaten, maar gratis Paint System bestaat), DynRemesh (remeshen al bezet), Human Generator (te groot).

**Oordeel Bram:** Gat 1 is de eerste kandidaat die vraag, betaalbewijs (2.400+ kopers van een product dat stopt) en een zichtbaar gat combineert. Het is ook een product waar uiterlijk telt: een pie menu ís interface, dus Daan kan er echt het verschil maken (GOK). Nog geen besluit: eerst nakijken, en uitzoeken of PieMaster het gat al vult (functies, ratings, verkopen per maand) en of de fork van PME bestaat en voor iedereen te koop is.

## 7. Controle ronde 3 en doorlichting gat 1 (7 nov 22:50)
**Gat 1 valt af.** Twee agents (controleur en onderzoeker, los van elkaar) vonden hetzelfde:
- Er is al een opvolger van PME voor Blender 5: Pie Menu Editor Fork van Pluglug, $36, 30 reviews gemiddeld 5,0, "Blender 5.0 and later" (GEZIEN, https://pluglug.gumroad.com/l/pie-menu-editor-fork). Versie 2.1.0 van 3 okt 2026 als Blender Extension, leest PME-menu's in via JSON (GEZIEN, https://blenderartists.org/t/pie-menu-editor-v2/662456/6100). Pluglug houdt het officiële PME-draadje bij (6.000+ posts, actief tot 6 nov 2026). PME is GPL, dus de fork is legaal. De link stond gewoon in een review op ratings ?page=6.
- PieMaster van Pitiwazou ($20, Pro $80, 100+, 5 maanden, 9 ratings gemiddeld 5,0, Blender 4.2 tot 5.2) dekt de moderne kant: pies, dropdowns, zwevende panelen, knoppen per modus, GPU-getekend (GEZIEN, https://superhivemarket.com/products/piemaster/faq). Enige klacht: groot en lastig te leren.
- Correcties op de citaten: "happy to pay for the update" en "Can't upgrade to Blender 5 without this" zijn 11 en 12 maanden oud, "Stopped development" 7 maanden. Niet "de tien nieuwste".
- Gat 2 klopt in grote lijnen (BoneDynamics $15 6.000+, Blender 4.2 tot 5.2; "baking doesn't work" gaat over de gratis versie; Swingy "geen linken" is twijfelachtig, een andere review zegt dat linken werkt). Gat 3: Pivot Transform $14,99, 2.600+, klacht bestaat.

**Les voor de volgende rondes:** een "verlaten bestseller" telt pas als gat nadat we zoeken naar forks en opvolgers (Gumroad, GitHub, het BlenderArtists-draadje van het product, alle pagina's van de ratings). Bij GPL-add-ons is een fork waarschijnlijk.

**Stand na deze run:** vijf ideeën en één gat bekeken, allemaal afgevallen of niet overtuigend. Over: gat 2 (bone-jiggle die goed bakt, kwaliteitsgat bij twee bestsellers met 6.000+ en 1.700+ kopers, maar veel concurrentie) en een eenvoudige pie-editor als gratis lokker (zwak). Geen bouwbesluit.
