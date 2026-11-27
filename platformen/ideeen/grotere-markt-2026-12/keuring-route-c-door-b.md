# Keuring route C (grotere markt, issue #323), 27 nov 2026, Afkijker B
Wat ik keurde: `platformen/ideeen/grotere-markt-2026-12/route-c.md` en `route-c-data/` van Afkijker C, commit 53f4ed8.
Akkoord: nee (het onderzoek is degelijk en de cijfers kloppen; twee kleine tekstpunten in de conclusie moeten eerst beter, daarna volstaat één nakeuring)

Ik bouwde niets en paste route-c.md niet aan. Alles hieronder heb ik zelf met curl gelezen op 27 nov 2026 tussen ±22:00 en 22:25 NL (GEZIEN), tenzij anders vermeld. Tellers en prijzen kunnen veranderen; de Cyber Sale van Superhive loopt tot 2 dec.

## Wat ik zelf nacontroleerde
| Cijfer in route-c.md | Mijn meting | Klopt? |
|---|---|---|
| RetopoFlow 11.800+, 62 ratings, $59,99 tot $85,99 | Sales 11800+, 62 ratings, productData 5999 tot 8599 (https://superhivemarket.com/products/retopoflow) | ja |
| TopoPen 500+, 3 maanden, 14 ratings, $24,99 | 500+, "3 months ago", 14 ratings, 2499 | ja |
| SpeedRetopo $10, 9.000+, bijna 7 jaar, 35 ratings | 9000+, "almost 7 years ago", 35 ratings, 1000 | ja |
| Quad Filler 1.900+, ±1 jaar, 9 ratings, $15 of $24 met donatie | 1900+, "about 1 year ago", 9 ratings; varianten $15 en $24 (saleprijs $9,75 en $15,60) | ja |
| Adaptive Auto Skinning 1.000+, 5 maanden, 22 ratings, $35 | 1000+, "5 months ago", 22 ratings, 3500 | ja |
| Voxel Heat Diffuse 13.200+, ±9 jaar, 77 ratings, $30 | 13200+, "about 9 years ago", 77 ratings, 3000 | ja |
| Cleave 300+, 2 maanden, $23 | 300+, "2 months ago", 2300 tot 2800; nu 4 ratings (de lat zegt 3) | ja |
| CatPin 500+, 3 maanden, **GOK $24** | 500+, "3 months ago", maar **$30** (Basic), $45 Supporter, $100 Studio | teller ja, prijs nee (klein, zie Kan 1) |
| Cleave plek 7 in "Top Selling Items this Week", rij Auto-Rig Pro tot Faceit | voorpagina: 1 auto-rig-pro, 2 humgen3d, 3 botaniq-trees, 4 adaptive-auto-skinning, 5 retopoflow, 6 scatter, **7 cleave**, 8 simply-cloth, 9 faceit (https://superhivemarket.com/) | ja |
| Market stats: $53.533.027, 7.454 makers, 7.170 add-ons, 5.821.336 items, sinds juni 2014 | $53,533,027, 7,454, Addons 7,170, 5,821,370 items (34 meer, de teller loopt), "launched on June 10th, 2014" | ja |
| 392 van 477 met versietag 5.0 of hoger | 392 van 477 (eigen telling op de dataset) | ja |
| 31 nieuwkomers jonger dan 12 maanden | 29 tot 31, hangt af of je "about 1 year" meetelt | ja, binnen afronding |
| PolyQuilt 183K downloads, 97 reviews; LoopTools 2M | 183K en (97); LoopTools 2M (https://extensions.blender.org/add-ons/?sort_by=-download_count, pagina 1 en 3) | ja |
| Blender Artists "two horrors": 33 berichten, 717 keer bekeken | 33 posts, 717 views, 19 okt 2026 (https://blenderartists.org/t/1655403.json) | ja |

Rekensommen nagerekend: kans 1 (40 x $15,11 = $604; 167 per maand = $2.523), kans 2 (25 x $19,01 = $475), kans 3 (40 x $9,26 = $370; 158 per maand = $1.463) en de omrekening met 0,91 kloppen allemaal. Twee kleine afwijkingen staan bij Kan 2 en 3.

## Deel A: doet het wat beloofd is?
Opdracht (issue #323): categorieën met veel verkopen en een zwakke of verouderde concurrent, waar wij binnen ±4 weken iets beters neerzetten; per kans kopers, prijs, 3 concurrenten met zwakke plek, weken, euro per maand na 3 maanden, toets aan de ideeëntest; ranglijst en één advies.

| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| A1 | Alle gevraagde onderdelen staan erin: 3 kansen met kopers, prijs, 3 concurrenten met zwakke plek, weken, euro per maand met rekensom, ideeëntest, ranglijst, advies, plus een lijst afgevallen ideeën. Bronnen zijn controleerbaar; de dataset en scripts staan erbij. | feit | hoog | |
| A2 | **De snelheidstabel "Wat nieuwkomers echt halen" telt stuks, geen geld, en laat zonder uitleg vier van de twaalf snelste nieuwkomers weg**, waaronder de twee die het meeste verdienen. Uit C's eigen dataset en mijn curl: Physical Atmosphere 1.000+ in 4 maanden à $84 (±250 per maand), MatPlus 2.100+ in 11 maanden à $75 (±190 per maand), MotionGen 1.400+ in 5 maanden (vanaf $1), LazyRealismFX 500+ in 2 maanden. In geld (maker krijgt (prijs min 5,5% min $0,49) x 70%, formule uit `platformen/blender/click-joints-plan-2026-11-19.md` r. 149; GOK op GEZIEN, bundels tellen mee): Physical Atmosphere ±$13.800, MatPlus ±$9.400, Adaptive ±$4.600, TopoPen ±$2.700, Cleave ±$2.200 per maand. | feit (tellers en prijzen GEZIEN), bedragen GOK | hoog voor het weglaten, midden voor de bedragen | Het advies blijft staan, want beide dure nieuwkomers komen van makers met al een hit (Physical Atmosphere en Physical Starlight, 17.100+, hebben allebei maker physical-addons, GEZIEN in C's dataset; MatPlus van BEFX, de maker van RBDLab, GEZIEN op https://superhivemarket.com/creators/befxstudios). Maar de les "een nieuwkomer haalt Cleave-niveau" geldt per stuk; in geld bepaalt de prijs het verschil met een factor 3 tot 6. Dat hoort Thijs te zien als hij op cijfers beslist. |
| A3 | **De vergelijking met onze hoek in het advies is niet eerlijk opgeschreven.** "Het gat tussen ons en Cleave is groter dan wat route C binnen 3 maanden kan opleveren" zet het plafond van de nummer 1 (Cleave, ±€2.000) tegenover de verwachting voor een nieuwkomer in route C (±€340 tot €550). Eerlijk is nieuwkomer tegen nieuwkomer, en dat staat elders in het stuk wél goed: TopoPen ±167, CatPin ±167, Cleave ±150 per maand. Ook wij zijn in de printhoek een nieuwkomer (1 verkoop, lat Click Joints Pro). | feit | hoog | De printhoek wordt ook voller: Split 3D Print, SnapSplit, CatPin, NB Figure Joints, SlicerJoint Pro en vier nieuwe splitters op BlenderKit van oktober en november (`organisatie/lat/click-cuts.md`, `click-joints-pro.md`). "Daar de nummer 1 worden" is dus geen gegeven en vraagt dezelfde GOK als route C. |
| A4 | De kernconclusie, **route C niet als hoofdroute**, wordt door de cijfers gedragen: nieuwkomers zonder publiek halen in grote categorieën hetzelfde aantal stuks als in onze hoek, de snelste groeiers hebben een eigen rekenmotor of een bekende maker, en goede tools kosten ons 5 tot 8 weken. | feit (op GEZIEN) plus redenering | hoog | Ik kom in route B langs een andere weg tot hetzelfde: buiten de huidige hoek is er voor ons geen markt die in 3 maanden duidelijk meer oplevert. |
| A5 | Kans 2 (skinnen) heet "bijna een harde nee" en krijgt een 3; kans 3 (quad fill) zegt zelf dat het "de vraag van issue #323 niet oplost". Eerlijk, maar dan zijn er feitelijk minder dan 3 kansen die de vraag beantwoorden. | feit | midden | Geen probleem als het zo blijft staan; het eerlijke antwoord kan "geen grotere markt" zijn. |
| A6 | De weeklijst van Superhive is gemeten tijdens de Cyber Sale (35% eraf). Cleave op plek 7 kan door de sale hoger staan, of juist lager omdat anderen meer korting geven; C noemt de sale wel bij de prijzen, niet bij de weeklijst. Op 22 nov stond Cleave op plek 3 (lat Click Joints Pro), en toen liep de sale nog niet: die begon vr 27 nov (`organisatie/besluiten.md` r. 28). | feit (sale GEZIEN in route-c.md r. 3), effect vermoeden | midden | Na 2 dec de weeklijst opnieuw lezen. |
| A7 | Niet onderzocht en eerlijk gemeld: BlenderKit en Reddit (403). Voor route C weegt BlenderKit mee, omdat daar dezelfde add-ons met 75% voor de maker staan (`organisatie/lat/broncode/blenderkit.md`). | feit | midden | |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| B1 | Elk cijfer heeft GEZIEN, DERDEN of GOK; snelheden heten eerlijk "GOK op GEZIEN". De enige GOK die ik kon weerleggen is de prijs van CatPin ($30, geen $24). | feit | hoog | CLAUDE.md regel 5 |
| B2 | Geen gedachtestreepjes gevonden (gezocht op lange en halve streepjes en " - "). Gewone woorden, Nederlands. | feit | hoog | regel 8 |
| B3 | Geen persoonsgegevens van Thijs. Makersnamen in de dataset zijn openbare winkelnamen van Superhive. `check.py` gaf OK bij mijn push. | feit | hoog | regel 2 |
| B4 | Alleen in de eigen map geschreven (`grotere-markt-2026-12/`). 181 regels, onder de grens van ±400. | feit | hoog | regel 6 |
| B5 | Kans 2 stelt voor om skinnen "als functie binnen Click Joints Pro" te gebruiken. Daar geldt een bouwstop voor nieuwe functies tot 20 verkopen (besluit 25 nov 23:40). Niet gemeld. | feit | hoog | `organisatie/besluiten.md` |
| B6 | AI wordt genoemd bij concurrenten (Image to 3D, Auto Unwrap). In intern onderzoek over anderen is dat feitelijk en C zegt er zelf bij dat wij het niet mogen; geen overtreding. | vermoeden | midden | regel 5 |

## Deel C
Niet van toepassing: dit is intern onderzoek, geen beeld, winkeltekst of iets wat een klant ziet.

## Moet (blokkeert akkoord)
1. **Snelheidstabel ook in geld, en zeggen waarom producten wegvallen** (A2). Voeg een kolom "geld per maand voor de maker (GOK)" toe en zet Physical Atmosphere en MatPlus erin, of schrijf in één zin waarom ze er niet in staan. Zeg erbij dat de grootste verdieners per maand dure tools van $75 tot $84 zijn, allebei van makers met al een hit. Dat steunt het advies, maar Thijs moet zien dat prijs de grootste hefboom is.
2. **De vergelijking in het advies eerlijk maken** (A3). Vervang "het gat tussen ons en Cleave is groter dan wat route C kan opleveren" door de vergelijking nieuwkomer tegen nieuwkomer (TopoPen, CatPin, Cleave: ±150 tot 170 per maand). Noem dat "nummer 1 worden in de printhoek" ook een GOK is in een hoek die voller wordt.

## Kan (mag later)
1. CatPin kost $30 op Superhive (GEZIEN), niet GOK $24 (tabel r. 40).
2. Het makersaandeel: de repo heeft de officiële formule (prijs min 5,5% min $0,49) x 70% (`platformen/blender/click-joints-plan-2026-11-19.md` r. 149). C rekent met 65% min $0,49. Het verschil is kleiner dan 3% ($15,53 tegen $15,11 bij $24), dus niets aan het oordeel; wel liever één formule in de hele repo.
3. Ranglijst kans 1, ondergrens: 20 per maand x $15,11 x 0,91 is ±€275, niet €200.
4. In de vergelijkingsregel r. 165 staat "150 per maand à $23 = ±$2.170". Dat is het bedrag na aftrek (150 x $14,46), niet 150 x $23 (= $3.450). Schrijf "netto voor de maker" erbij.
5. Bouwstop tot 20 verkopen noemen bij "functie binnen Click Joints Pro" (B5).
6. De weeklijst na de Cyber Sale (na 2 dec) nog één keer lezen (A6).
7. BlenderKit meenemen voor de drie kansen als er nog een run is (A7).
