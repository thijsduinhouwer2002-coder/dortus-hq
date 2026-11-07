# Blender: wat bouwen we? Kandidaten (7 nov 2026, Bram)

Status: concept, wacht op de controleur. Nog geen bouwbesluit.

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
| **A. Gewrichten voor printbare figuren** (kogel, pen, draaipen, met speling per printer) | 3 | 4 | 3 | 3 | 5 | **18** |
| **B. AI-model naar printklaar in één paneel** (samenvoegen, waterdicht, mm, wanddikte, splitsen) | 4 | 4 | 2 | 3 | 3 | **16** |
| **C. Precies modelleren voor SketchUp-overstappers** (push/pull, maten intypen) | 4 | 5 | 2 | 1 | 4 | **16** |
| D. 3D naar vlakke onderdelen voor laser/CNC | 3 | 1 | 2 | 5 | 2 | 13 |
| E. Export naar spelmotoren | 2 | 3 | 1 | 4 | 1 | 11 |

Onderbouwing per kandidaat (cijfers GEZIEN door de onderzoeker op superhivemarket.com en extensions.blender.org, 7 nov):
- **A:** JointLab $65 20+ (1 ster: dwingt een eigen server af), Cleave $23 90+ (belooft ook kogelgewrichten). Splitsers verkopen goed maar dat hoekje is vol: Dovetail Key 800+, CatPin $24 400+, Split-3DPrint $22 400+. Gratis: Easy-Print 7K, EasySlice 6K downloads. Gat: een stabiel, goedkoop hulpmiddel alleen voor gewrichten. Visueel sterk: een poseerbare figuur in de lijstplaatjes, gewricht dat in de voorbeeldweergave meedraait.
- **B:** sterke vraag, maar de gratis 3D Print Toolbox (680K downloads) doet de controles al en Smart Remesh (2.500+) en OkTopo ($24, 700+) zitten op het opschonen. Verschil maken is lastig (GOK).
- **C:** grootste geld (Construction Lines $11 7.400+, Design Magic $29 2.600+, Seamless CAD $14,90 300+ in 3 maanden), maar groot en moeilijk stabiel te krijgen. Te groot als eerste product.
- **D:** betaald verkoopt weinig (Cross Section Maker $2,50 200+ in 5 jaar), veel gratis. Hooguit gratis lokmiddel.
- **E:** vol, niets duidelijks dat ontbreekt.

## 4. Voorlopige keus (na de controleur definitief)
A, met B als reserve. Reden: past bij wensen die kopers zelf opschrijven, ligt in de groeiende hoek (3D-printen van AI- en eigen figuren), middelgroot, en het kan opvallen. Risico: de markt voor alleen gewrichten is kleiner dan die voor splitsen (JointLab 20+, Cleave 90+). Voordat we bouwen nog nagaan: hoeveel verkoopt Cleave per maand, en zijn er gratis gewrichten-add-ons op extensions.blender.org.

## Nakijken
(controleur vult in)
