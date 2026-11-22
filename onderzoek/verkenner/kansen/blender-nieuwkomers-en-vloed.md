# Productkans Blender: waar verkopen nieuwkomers nog, en hoe hard loopt Superhive vol?

Vera, 9 nov 2026 run 01:31 (Amsterdam). **Uitkomst: geen nieuwe niche om te bouwen. Cijfer 3. Advies: nee voor nu.** Wel een belangrijk nieuw feit voor Blender als geheel: het aanbod van nieuwe add-ons op Superhive is in de laatste 30 dagen ongeveer vier keer zo groot als een jaar geleden.

## Het idee
Vorige kansen zochten naar zwakke of verlaten nummers één (`blender-zwakke-nummer-een.md`, `blender-verlaten-bestsellers.md`). Deze keer andersom: in welke soorten add-ons halen **nieuwkomers** (gestart in de laatste 13 maanden) aantoonbaar verkopen, terwijl er weinig aanbod is? Dat is het sterkste bewijs dat een nieuwe add-on van ons daar ook kan verkopen.

## Hoe gemeten (GEZIEN, 9 nov)
- Alle add-ons uit de lijst `superhivemarket.com/categories/addons/browse?sort_date=desc`, pagina 1 tot 125 (nieuwste eerst): **2.955 add-ons**, gepubliceerd van ±13 maanden geleden tot vandaag. Per product de verkoopteller (Superhive toont die pas vanaf 10 verkopen), publicatie, prijs, subcategorie, maker, titel en korte tekst.
- Data: `data/superhive-nieuwe-addons-2026-11-09.jsonl`, script `data/superhive-nieuwe-addons-script.py`. **Let op:** in dit databestand staat `prijs` in centen (de pagina heeft eerst `"price":1499` en later `"price":"14.99"`); het script is daarna verbeterd en leest nu dollars.
- Indeling in 31 thema's op trefwoorden in naam en tekst (grof: een add-on kan in meer thema's vallen, en "step" vangt ook "step-by-step"). Leeftijd uit "x months ago", dus op een maand nauwkeurig.
- Controleur (agent) heeft met curl nagekeken: de datums per lijstpagina, de maker met de meeste add-ons, alle verkooptellers in de print-niche, oude bestsellers en gratis concurrenten. Alles klopt grofweg, prijzen soms in de aanbieding (zie onder).

## Feit 1: het aanbod explodeert (GEZIEN)
| Leeftijd | Nieuwe add-ons | Verschillende makers | Betaald met 10+ verkopen | met 100+ |
|---|---|---|---|---|
| laatste 30 dagen | 729 | 252 | 7% | 1% |
| 1 maand | 238 | 144 | 16% | 2% |
| 2 maanden (twee labels samen) | 351 | 212 | 23% | 3% |
| 3 maanden | 272 | 190 | 28% | 4% |
| 6 maanden | 161 | 133 | 43% | 5% |
| 9 maanden | 109 | 88 | 55% | 9% |
| 11 maanden | 64 | 56 | 55% | 10% |

- Een jaar geleden kwamen er ±110 tot 150 add-ons per maand bij (controleur: ±5 lijstpagina's per maand rond nov 2025 tot mrt 2026). Nu ±720 in 30 dagen (pagina 1 tot 30 samen 707, nagekeken).
- Een kwart daarvan is één maker: **ZEG (Zahit erdem Guzel)**, 165 add-ons in 30 dagen, bijna allemaal "... Generator for Blender" (nagekeken, makerpagina telt 179). Zonder hem nog steeds ±540 in 30 dagen, ruim drie keer een jaar geleden. Ook het aantal verschillende makers per maand is ruwweg verdubbeld (±100 naar 252).
- Wat dit betekent: een nieuwe add-on staat op de eerste pagina van "nieuwste" (24 stuks) nu nog geen dag. Vindbaarheid via de nieuwlijst is bijna weg; het moet komen uit zoeken, de bestsellerlijst, video's en eigen berichten.
- Wat dit (nog) niet bewijst: dat nieuwkomers nu slechter verkopen. Jonge add-ons hebben minder tijd gehad, dus de lage percentages bovenaan de tabel zijn normaal. Dat moet de herhaalmeting rond 5 dec laten zien: haalt de lichting van okt na 2 maanden minder dan 23% 10+ (de lichting van sep nu), dan loopt de winkel echt vol voor nieuwkomers (GOK tot dan).

## Feit 2: waar nieuwkomers verkopen (betaalde add-ons van 3 tot 12 maanden oud, n=1.613, GEZIEN)
Alle samen: 42% haalt 10+ verkopen, 8% haalt 100+, mediaan 0 (onder 10).

| Thema | n | 10+ | 100+ | jong aanbod (0 tot 2 mnd) | Oordeel |
|---|---|---|---|---|---|
| jiggle en zachte fysica | 7 | 71% | 57% | 6 | goo-physics (Dillon Goo, bekende YouTuber) 2.200+, jigglemaker 1.200+: sterke nummer één |
| mist en volume | 8 | 75% | 50% | 15 | loopt vol, Lazy3D en Physical Addons sterk |
| motion capture uit video | 14 | 86% | 21% | 3 | hangt aan AI-modellen, zwaar, past niet bij ons |
| lucht en atmosfeer | 28 | 43% | 21% | 32 | jong aanbod groter dan oud, vol |
| CAD, STEP, NURBS | 40 | 68% | 18% | 33 | ±8 STEP-importers, Forge CAD; Olaf wees dit al af (sterke oude spelers) |
| breken en destructie | 54 | 56% | 17% | 52 | RBDLab sterk, vol |
| retopologie | 51 | 59% | 16% | 38 | vraag groot (18 van 38 jonge al 10+), maar Quad Remesher en Smart Remesh (2.500+ in 3 mnd) sterk |
| 3D-print splitsen | 31 | 52% | 13% | 44 | zie onder |
| haar | 19 | 84% | 11% | 21 | 10+ makkelijk, 100+ zeldzaam, global-hair (700+) sterk |
| beheer en organiseren | 140 | 27% | 3% | 60 | zwak: kopers betalen hier weinig |
| sneller renderen | 20 | 15% | 0% | 15 | zwak |

### De print-niche (nagekeken door de controleur, bevestigt Olaf)
- Drie nieuwkomers verkochten binnen 4 maanden 400 tot 800+: dovetail-key 800+ ($18, Milad Kambari, 13 reviews met klachten over "vibe coded" en bugs), catpin 400+ ($24 in de aanbieding, ook 81 reviews op Gumroad volgens Olaf), split-3dprint 400+ ($22, plus gratis versie). Cleave 100+ in 2 maanden. Geen oude bestseller: de niche is in 2026 ontstaan.
- Maar de nieuwkomers daarna blijven steken op 10+ tot 30+ (snapsplit 30+ in 8 maanden, cut-flex, split-it, easy-print, 3d-slicer-suite). Gratis: Easy-Print 7.016 downloads, EasySlice Print 5.857, SnapSplit 1.278, Print-Prep 723 op extensions.blender.org. En PrusaSlicer en Bambu Studio knippen gratis met pennen, dowels en zwaluwstaart.
- Openstaande wensen in reviews: snede eerst bewerken, knippen langs een loop, stabiel op dichte sculpts, en **beweegbare gewrichten (bal en kom voor actiefiguren)**. Dat laatste is precies Click Joints van Bram; cut-flex (15 gewricht-presets), cleave (kogelgewricht) en jointlab ($65, 20+) zitten er ook al.
- Dit is dezelfde uitkomst als Olaf in `platformen/blender-2/` (drie rondes, advies "liever niet" voor splitsen). Mijn meting voegt alleen de hele-winkelvergelijking toe: print-splitsen is een van de betere thema's voor nieuwkomers, maar het jonge aanbod (44 in 2 maanden) is groter dan het oude (31).

## Het gat in één zin
Er is geen thema met tegelijk veel verkoop bij nieuwkomers, weinig nieuw aanbod en een zwakke nummer één: waar nieuwkomers goed verkopen (jiggle, mist, print-splitsen, retopologie) is de top al sterk of stroomt het aanbod de laatste twee maanden binnen.

## Wie betaalt, hoeveel, hoe vaak
Hobbyisten en kleine studio's, eenmalig $10 tot $60. Een goede nieuwkomer in een levend thema haalt 100 tot 800 verkopen in 3 tot 12 maanden (8% van alle betaalde nieuwkomers haalt 100+).

## Eerste productidee
Geen nieuw. Voor Click Joints wel een les: de nieuwlijst helpt bijna niet meer (minder dan een dag op pagina 1). Een sterke video en een plek in zoekresultaten voor "joint", "articulated", "ball joint" en "3d print" wegen zwaarder dan bij de start van Superhive.

## Cijfer en advies
Cijfer 3, nee voor nu. Blender blijft als platform staan (het geld is er, 42% van de betaalde nieuwkomers haalt 10+), maar de vloed is een nieuw risico. Herhaalmeting rond 5 dec: dit script opnieuw, en de lichting van okt 2026 (nu 0 tot 1 maand) vergelijken met de lichting van sep nu.
