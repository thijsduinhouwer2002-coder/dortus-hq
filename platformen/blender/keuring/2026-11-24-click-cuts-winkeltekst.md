# Keuring winkeltekst Click Cuts, 24 nov 2026, keurder (agent van de hoofdchat)
Wat ik keurde: `platformen/blender/superhive/click-cuts-winkeltekst.md` (commit f63f4ba, Chris). Opdracht: `berichten/chris.md`, hoofdchat kwartier 24 nov ±04:25 en ±06:25.
Akkoord: nee (één moet-punt, klein: de bundel botst met de Cyber-korting op Pro; de tekst voor de koper zelf is goed)

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | Elke regel in "Wat het doet" klopt met de code van 1.0.0: knop "Split to fit" (`in_een_klik.py`: dichtmaken alleen als nodig, sneden plannen, splitsen, controle), 9 printers plus "Custom size" (`printers.py`), passingproef met 4 spelingen die per printer en materiaal bewaard wordt (`passing.py` `spelingen()`, `passingproef.py`), controle groen/oranje/rood met reden en wand rond de gaten (`controle.py`), vrije snede (`vrije_snede.py`), Make watertight op een kopie met grens 3000 voxels (`gesloten.py`), export STL of 3MF in mm (`exporteer.py`), Convert to mm (`schaal.py`), Blender 4.2 en nieuwer (`blender_manifest.toml`). Niets beloofd wat er niet is; alleen pennen. | feit | hoog | |
| 2 | "a number on every cut face" klopt: "Engrave numbers" staat standaard aan (`eigenschappen.py`, default=True). | feit | hoog | |
| 3 | De waarschuwing in de tekst ("orange" is nog geel in `controle.py`) is verouderd: de bouwer heeft het al opgelost, KLEUREN["oranje"] = (1.0, 0.26, 0.0) (commit 36912d5, Productbouwer run 8). "orange" mag dus in de tekst blijven. | feit | hoog | |
| 4 | Zoekonderbouwing titel klopt in de kern (curl zelf, 24 nov, eerste 12): "split model" #1 Cleave, #2 Bed Fit Splitter, #4 PrintSplitter, #5 CatPin, #7 FigureCut; "split 3d printing" #1 Cleave, #2 SnapSplit, #4 Oryx CAD, #8 FigureCut, #9 PrintSplitter; "printer bed" #1 Bed Fit Splitter, #2 CatPin, daarna geen splitters; "3d print connectors" #1 Cleave, #2 Split It, #3 CatPin. Bed Fit Splitter $19, nu $14.25 (GEZIEN). Kleine onjuistheid: "Wie bovenaan staat heeft 'Split Models' in de titel" klopt niet voor #1: Cleave heeft "Model Split", niet "Split Models". | feit | hoog | |
| 5 | Titel is 85 tekens, niet 84 (`wc -c`). Geen gevolg, wel een verkeerd cijfer. | feit | hoog | |
| 6 | Prijzen kloppen met `concurrentie.md` punt 5 en tabel 2a: Cleave $23 en $28, CatPin $24 en $36, Split $22 en $28, startprijs $19 tot 14 dec, daarna $24. Maar de CatPin-prijzen staan in `concurrentie.md` als DERDEN (keuring 23 nov), niet GEZIEN. En "Supporter met dezelfde functies doen Cleave en CatPin ook" staat nergens onderbouwd. | feit | midden | De pagina's van Cleave en CatPin met curl: wat krijgt een Supporter extra? |
| 7 | Bundelbron Gumroad klopt (curl, help-artikel 339): type "Bundle", eigen producten, eigen prijs, losse waarde doorgestreept, één variant per product, geen bundel in een bundel. Extra uit dezelfde pagina wat de tekst mist: de doorgestreepte waarde is "fixed by the product variants you picked when you built the bundle". | feit | hoog | |
| 8 | Bundelbron Superhive klopt: pagina bestaat, "Products: 7", "Sales: 20+" (curl 24 nov). Wel was die bundel een actie van 4 dagen ("Available from May 20 to May 23"). | feit | hoog | |
| 9 | Click Joints Pro kost op Superhive $12 Personal en $45 Studio (GEZIEN curl 24 nov) en op Gumroad $19 (price_cents 1900, GEZIEN json). Klopt met de tekst. | feit | hoog | |
| 10 | **Bundel botst met de Cyber-korting.** `commercie/blender-click-joints/black-friday.md` punt 1: code CYBER25, 25% op Click Joints Pro op Gumroad tot di 1 dec 23:59, automatisch toegepast. Click Cuts gaat live in de week van ma 30 nov. Op 30 nov en 1 dec is los dan $14,25 + $19 = $33,25, goedkoper dan de bundel van $34. De doorgestreepte waarde ($38 bij de startprijs) wekt dan een verkeerde indruk. De tekst noemt alleen het verschil met $19 tot 14 dec, niet deze botsing. | feit | hoog | Datum van uitgave van Click Cuts, en of CYBER25 ook op de bundel komt. |
| 11 | Rekenfout in een interne zin: "bundel op $29 zetten (21% onder $36)". $29 is 19% onder $36 (21% zou $28,44 zijn). Staat niet in de tekst voor de koper. | feit | hoog | |
| 12 | Engels is goed en vrij van AI-zinnen (geen "unleash", "seamless", "elevate", geen opsomming van bijvoeglijke naamwoorden). Kort, concreet, werkwoorden vooraan. Klein: "Click Cuts cuts" leest iets stroef; Britse spelling ("millimetres", changelog "Colour") terwijl de add-on zelf "millimeters" en "color" zegt (`exporteer.py`, `controle.py`), dus kies één. | feit | midden | |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Geen persoonsgegevens van Thijs (geen account- of partnernummer, geen adres). | feit | hoog | harde regel 2 |
| 2 | Geen concurrentnaam in de titel; titel neemt de titel van Bed Fit Splitter niet letterlijk over. | feit | hoog | opdracht |
| 3 | Geen gedachtestreepjes in de Nederlandse tekst (grep op lange en halve streepjes en op een los streepje tussen spaties: niets). | feit | hoog | harde regel 8 |
| 4 | Bijna alle cijfers hebben GEZIEN/DERDEN. Uitzonderingen: CatPin-prijzen GEZIEN genoemd waar de bron DERDEN zegt (A6); "Sales 20+", "$14,25", "$12/$45" goed gelabeld. Bundelprijs en $9/21% zijn eigen rekensom, mag zonder label. | feit | hoog | harde regel 5 |
| 5 | Status CONCEPT en "plakken doet Thijs", geen prijsbesluit genomen (prijs bij Thijs). Geen geld uitgegeven. | feit | hoog | harde regel 1 en 4 |

## Deel C: zou een koper het leuk en fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | Titel en eerste zin zijn sterk: printer kiezen, één knop, past op het bed, passingproef. Dat laatste heeft geen concurrent; een koper die ooit een te strakke pen printte klikt hierop. | | |
| 2 | Op Superhive staat Cleave er direct naast met "Pegs, Dowel, Rod Channel, Magnets, Ball Joints". Een koper ziet bij ons alleen "pins" en vraagt zich af of dat genoeg is. | Zeg het zelf eerlijk en positief in één regel in de lijst, bijvoorbeeld "Round pins with matching holes, sized from your fit test", zonder toekomstbeloftes. | klein |
| 3 | Er staat geen regel over wat er niet in zit in het Engels; sectie 6 is alleen intern. Kopers van CatPin klagen in reviews over verrassingen. | Een korte FAQ voor de pagina (Does it work on AI or sculpted meshes? Which connectors? Does it lay parts flat? Blender versions?), met de antwoorden uit sectie 6. | klein |
| 4 | Geen plan voor beelden: Cleave verkoopt met een uit elkaar geschoven figuur in felle kleuren plus echte geprinte delen. | Hoofdbeeld: model uit elkaar in kleur per deel (zit in 1.0.0) plus de geprinte passingproef. Hoort bij Daan/Sanne, wel noemen bij de uitgave. | midden |
| 5 | Geen tags of zoekwoorden voor het tagveld van Superhive ("terrain", "cosplay", "bust", "connectors", "printer bed"). | Tags-lijst toevoegen. | klein |
| 6 | De supporter-variant zegt niet wat de koper ervoor terugkrijgt. | Eén regel: "Same features, for people who want to support updates" plus wat updates inhouden (bijv. alle 1.x-updates). | klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet**
- M1 (A10): Bundel en Cyber-korting. Zet in sectie 5 dat de bundel op Gumroad pas na di 1 dec live gaat (of dat CYBER25 ook op de bundel komt), anders is los kopen op 30 nov en 1 dec goedkoper dan de bundel ($33,25 tegen $34).

**Kan**
- K1 (A3): haal de verouderde "Let op: nu geel"-regel weg; oranje is al opgelost (36912d5).
- K2 (A5, A4, A11): titel is 85 tekens; Cleave heeft "Model Split" niet "Split Models"; $29 is 19% onder $36.
- K3 (A6, B4): CatPin-prijzen DERDEN noemen; zin over Supporter van Cleave en CatPin onderbouwen of weghalen.
- K4 (A7): noteer dat de doorgestreepte waarde op Gumroad vastligt op het moment van bouwen; na 14 dec de bundel opnieuw opslaan of nakijken dat $43 getoond wordt.
- K5 (C2, C3, C5, C6): regel over pennen, korte Engelse FAQ, tags, wat Supporter is.
- K6 (A12): één spelling kiezen, Brits of Amerikaans, en die ook in de changelog aanhouden.

## Herkeuring, 24 nov 2026 (commit 478962d)
Akkoord: ja

| # | Bevinding | Feit of vermoeden | Zekerheid |
|---|---|---|---|
| 1 | M1 opgelost: sectie 5 punt 0 zet de bundel op Gumroad pas op wo 2 dec live, na het einde van CYBER25 (di 1 dec), met de rekensom $33,25 tegen $34. Click Cuts zelf mag in de week van 30 nov. | feit | hoog |
| 2 | Pennenregel waar: pennen zijn rond (cilinder met afschuining, `vormen.py`), de speling komt uit de instelling of de passingproef, en de pennen zijn een losse pennenplaat die apart wordt geëxporteerd (`exporteer.py`, "every piece and every pin plate"). | feit | hoog |
| 3 | FAQ waar voor 1.0.0: alleen pennen; Make watertight is een voxelkopie die bij een te groot model weigert (`gesloten.py`, grens 3000 voxels), dus "may need to be cleaned first" is eerlijk; delen worden niet vanzelf plat gelegd; Blender 4.2 en nieuwer, getest in 4.2 en 5.3 (CHANGELOG). | feit | hoog |
| 4 | Supporter-zin klopt met de varianten (zelfde add-on). De GOK over Supporter bij Cleave en CatPin staat nu als GOK. | feit | hoog |
| 5 | K1, K2, K3, K6 verwerkt (oranje, 85 tekens, "Model Split", 19%, CatPin DERDEN, Amerikaanse spelling). | feit | hoog |

**Kan (blokkeert niet):**
- K7: "yet" in de FAQ ("No dovetails, magnets or snap keys yet", "Not automatically yet") en "fund faster updates" klinken als een belofte voor later. Liever zonder "yet" en "Pick Supporter if you want to support updates", tenzij het plan er echt is.
