# Route C: een add-on voor iets wat heel veel Blender-gebruikers doen (issue #323)

Afkijker C, vr 27 nov 2026 ±21:00 tot 22:40 NL. Alleen onderzoek, niets gebouwd. Alles gelezen met curl op 27 nov 2026; dat heet hieronder GEZIEN. Let op: vandaag loopt de Cyber Sale van Superhive (35% eraf, tot 2 dec), dus winkelpagina's tonen de saleprijs. Ik noem de gewone prijs uit de pagina (doorgestreepte prijs of `productData`).

## Kort
- **Advies: route C nu niet als hoofdroute.** Een nieuwkomer in een "grote" categorie verkoopt in dezelfde orde als Cleave in onze hoek. De grote totalen (RetopoFlow 11.800+, FLIP Fluids 19.000+) zijn jaren plus bundels opgeteld; ze zeggen weinig over wat een nieuwe add-on per maand haalt.
- **Top 3 als we het toch doen:** (1) hand-retopologie, tegen RetopoFlow ($59,99) en TopoPen ($24,99); (2) automatisch skinnen of gewichten zetten voor figuren met een rig; (3) een gereedschap dat gaten met vierhoeken dicht ("quad fill"), tegen Quad Filler.
- **Belangrijkste feit:** Cleave staat deze week op plek 7 van "Top Selling Items this Week" op heel Superhive, tussen Auto-Rig Pro, HumGen3D en RetopoFlow (GEZIEN, voorpagina). Onze hoek is dus niet klein naar maatstaven van Superhive. Superhive zelf is klein.

## Hoe gemeten (controleerbaar)
Scripts en ruwe data staan in `route-c-data/` naast dit bestand.
1. **Bestsellers Superhive:** `https://superhivemarket.com/categories/addons/browse?sort_sales=desc&page=1..20` gaf 477 add-ons (laagste teller 500+). Per product de productpagina gelezen: Sales-teller, aantal ratings, sterren in beeld, "Published", "Blender Version", maker (`browse.py`, `prod.py`; uitslag `superhive-top477-2026-11-27.jsonl`, met `plek` = plek in de verkooplijst). Bij 88 pagina's gaf Superhive eerst geen tabel (te snel achter elkaar); die heb ik langzaam opnieuw gelezen, daarna miste er geen enkele.
2. **Per subcategorie** (modeling, rigging, rendering enz.) de eerste 6 pagina's op verkoop (`subcat.py`). Een product staat vaak in meerdere categorieën, dus optellen per categorie geeft dubbeltellingen. Ik gebruik het alleen om te zien wie waar bovenaan staat.
3. **Snelheid:** teller gedeeld door leeftijd in maanden ("3 months ago" = 3). Dat is een ondergrens (de teller rondt af naar beneden) en een GOK op GEZIEN, want de teller telt ook bundelverkopen mee.
4. **Zoeken:** `https://superhivemarket.com/search?search[q]=<woord>&search[category_id]=6&sort_sales=desc` (`search.py`). De zoekfunctie van Superhive is los: er komen veel add-ons die er niets mee te maken hebben.
5. **Voorpagina Superhive:** de blokken "Top Selling Items this Week" en "New and Rising".
6. **Superhive market stats:** https://superhivemarket.com/market-stats.
7. **Blender Extensions:** `https://extensions.blender.org/add-ons/?sort_by=-download_count&page=1..10` (downloads en aantal reviews per add-on).
8. **Gumroad:** `https://gumroad.com/products/search?taxonomy=3d%2F3d-assets%2Fblender&sort=most_reviewed` (108 producten met de meeste ratings).
9. **Blender Artists:** `https://blenderartists.org/search.json?q=...` en `/t/<id>.json`.
10. **Niet gelukt:** Reddit (`www.reddit.com/.../search.json` gaf HTTP 403). BlenderKit niet bekeken in deze run (zie `organisatie/lat/broncode/blenderkit.md` voor wat we al weten). Daar staat dus ONBEKEND.

## Wat de markt laat zien

**1. Superhive is als geheel klein.** Sinds juni 2014: $53.533.027 uitbetaald aan makers, 7.454 makers, 7.170 add-ons, 5.821.336 verkochte items (GEZIEN, market-stats). Dat is gemiddeld ±$4,3 miljoen per jaar voor alle makers samen (GOK, gerekend over 12,5 jaar; recente jaren liggen waarschijnlijk hoger).

**2. De top wordt goed onderhouden.** Van de 477 best verkochte add-ons heeft 392 een versietag van 5.0 of hoger, 85 niet (GEZIEN, dataset). Bijna alle grote namen hebben 4 of 5 sterren in beeld en tientallen tot honderden ratings: Auto-Rig Pro 71.600+ (449 ratings), Hard Ops/Boxcutter 48.500+, MACHIN3tools 36.600+, MESHmachine 24.100+, UVPackmaster 20.100+, FLIP Fluids 19.000+ (GEZIEN). Vera vond op 8 nov al dat bijna elke verlaten bestseller binnen een jaar een opvolger had (`onderzoek/verkenner/kansen/blender-verlaten-bestsellers.md`).

**3. Wat nieuwkomers echt halen.** 31 van de 477 zijn jonger dan 12 maanden (GEZIEN). De snelste (teller per maand, GOK op GEZIEN):

| Add-on | Klus | Prijs (gewoon) | Teller | Leeftijd | Per maand | Maker had al een hit? |
|---|---|---|---|---|---|---|
| [Image to 3D](https://superhivemarket.com/products/imageto3d) | AI: foto naar 3D-model | $18 | 1.700+ | 28 dagen | ±1.700 | ja (Milad Kambari) |
| [Smart Remesh](https://superhivemarket.com/products/smart-remesh) | automatisch remeshen | $17 | 2.800+ | 3 mnd | ±930 | ja (Milad Kambari) |
| [Auto Unwrap](https://superhivemarket.com/products/auto-unwrap) | UV automatisch, getraind model | $18 | 1.300+ | 2 mnd | ±650 | ja (Milad Kambari) |
| [Goo Physics](https://superhivemarket.com/products/goo-physics) | gestileerde simulatie | $20 | 2.300+ | 8 mnd | ±290 | ja (DillonGoo Studios) |
| [Adaptive Auto Skinning](https://superhivemarket.com/products/adaptive-auto-skinning) | skinnen op de GPU | $35 | 1.000+ | 5 mnd | ±200 | nee (Jessy Leite) |
| [Puppet Studio](https://superhivemarket.com/products/puppet-studio) | makkelijk riggen | $30 | 1.400+ | 8 mnd | ±175 | GOK nee |
| [TopoPen](https://superhivemarket.com/products/topopen) | hand-retopologie | $24,99 | 500+ | 3 mnd | ±167 | nee |
| [CatPin](https://superhivemarket.com/products/catpin) | splitsen voor 3D-print (onze hoek) | GOK $24 | 500+ | 3 mnd | ±167 | nee |
| [Cleave](https://superhivemarket.com/products/cleave) | splitsen voor 3D-print (onze hoek) | $23 | 300+ | 2 mnd | ±150 | nee |

Wat eruit volgt:
- Van de 31 nieuwkomers komen er 13 van makers die al een hit hadden: Milad Kambari 4, Lazy3D 4, Casey Sheep 3, HugeMenace 1 (maker van ND), physical-addons 1 (GEZIEN, kolom `creator`).
- De drie snelste hebben een **eigen rekenmotor**: een getraind model (Auto Unwrap, Smart Remesh) of een AI-generator (Image to 3D). Dat kunnen wij niet in 4 weken met Python, en AI mogen we nergens noemen (harde regel 5).
- Een nieuwkomer zonder publiek in een "grote" categorie (TopoPen, retopologie) haalt **dezelfde orde als CatPin en Cleave in onze hoek**: ±150 tot 170 per maand.

**4. Onze hoek in de weeklijst.** "Top Selling Items this Week" op 27 nov: Auto-Rig Pro, HumGen3D, Botaniq Trees, Adaptive Auto Skinning, RetopoFlow, Scatter, **Cleave**, Simply Cloth, Faceit (GEZIEN, voorpagina). Op 22 nov stond Cleave op plek 3 (`organisatie/lat/click-joints-pro.md`). De nummer 1 van de 3D-printhoek verkoopt dus al zoveel als de best lopende add-ons van heel Superhive deze week.

**5. Waar de top zwak is.** Bestsellers met 3 sterren of minder in beeld, of een versietag onder 5.0, zitten vooral in remeshen (BQR 4.800+ 3 sterren tag 4.4; Tesselator 3.700+ 3 sterren tag 3.2; DynRemesh 2 3.100+ 3 sterren tag 2.91; QuadWrap 1.200+ 3 sterren; QRemeshify $7 500+ 2 sterren), in explosies en schade (Khaos 4.000+ 3 sterren; Real Damage, Explode FX, Mix Damage alle 3 sterren) en in losse oude hulpjes (Pro Align Tools 2.000+ 3 sterren, Mixamo to Rigify 1.100+ 3 sterren tag 4.3) (GEZIEN, dataset). Maar in elk van die hoeken staat al een nieuwe sterke speler: Smart Remesh en SoftWrap (5 sterren, 3.800+) bij remeshen, RBDLab ($74, 6.100+, 5 sterren) en het nieuwe Project Damage ("New and Rising") bij schade.

---

## Kans 1: Hand-retopologie (een laag vierhoeken over een sculpt of scan tekenen)

**Wat:** een Python-add-on waarmee je met een pen strips, lussen en vlakken op het oppervlak van een hoog-poly model tekent, zodat er een schone mesh met vierhoeken ontstaat. Iedereen die sculpt of scant moet dit; een beginner noemt het "the two horrors of 3D" (1 van 2, met shading nodes), 33 berichten en 717 keer bekeken (DERDEN, https://blenderartists.org/t/the-two-horrors-of-3d-why-do-shading-nodes-and-retopology-terrify-me/1655403).

**Kopers:**
- RetopoFlow 4: Sales 11.800+, 62 ratings, gemiddeld 4 (GEZIEN, https://superhivemarket.com/products/retopoflow). Let op: de teller loopt al door vanaf eerdere versies en telt 5 bundels mee, waaronder een bundel van Superhive van 24 producten voor $365 (GEZIEN, `organisatie/lat/broncode/retopoflow.md`). Hoeveel per maand nu: GOK ±100 tot 300.
- TopoPen: 500+ in 3 maanden, 14 ratings, gemiddeld 4 (GEZIEN, https://superhivemarket.com/products/topopen). Dus ±167 per maand (GOK op GEZIEN).
- SpeedRetopo: $10, 9.000+ in bijna 7 jaar, 35 ratings, 5 sterren in beeld (GEZIEN, https://superhivemarket.com/products/speedretopo).
- Gratis: PolyQuilt op Blender Extensions, 183K downloads en 97 reviews (GEZIEN, lijst op downloads). Blender heeft zelf Poly Build en een "Retopology"-overlay (GEZIEN, https://docs.blender.org/manual/en/latest/editors/3dview/display/overlays.html). Die zijn er al jaren en toch verkopen de betaalde tools, dus geen harde nee op "ingebouwd".

**Prijs die mensen betalen:** $10 (SpeedRetopo), $24,99 (TopoPen), $59,99 tot $85,99 (RetopoFlow, 12 maanden updates, daarna 50% van de prijs per jaar) (GEZIEN).

**3 sterkste concurrenten en hun zwakke plek:**
| | Prijs | Teller | Zwakke plek (bron) |
|---|---|---|---|
| RetopoFlow 4 | $59,99 | 11.800+ | duur; opnieuw betalen voor V4 ("they require you to purchase a whole new license for V4"); functies jaren "coming soon"; instellingen bleven hangen na afsluiten; werkte niet op dag 1 van Blender 4.5 (GEZIEN, alle 62 reviews, samengevat in `organisatie/lat/broncode/retopoflow.md`). Wel: de maker antwoordt op elke klacht. |
| TopoPen | $24,99 | 500+ in 3 mnd | moeilijk te leren: "Very hard to understand at first", "Quite not intuitive at first ... I wish there was better documentation or a full tutorial", "for the lack of tutorials on the web"; op een ruw oppervlak "my draw line do whatever it wants" (GEZIEN, https://superhivemarket.com/products/topopen/ratings). 15% gaf 1 ster (GEZIEN). |
| PolyQuilt (gratis) | $0 | 183K downloads | gratis en goed beoordeeld; zwakke plek ONBEKEND (reviews niet gelezen in deze run). |

Er komen er nog steeds bij: Nitro Retopo (21 sep 2026), Quadify Base nu gratis (23 sep 2026), Safe UV Retopo (19 okt 2026) (DERDEN, https://blenderartists.org/search.json?q=retopology%20addon%20order:latest).

**Bouwen voor ons:** GOK 5 tot 8 weken tot iets wat naast TopoPen kan staan, niet 4. Het kan in Python (RetopoFlow en TopoPen zijn Python; TopoPen heeft alleen op Windows een eigen bibliotheek voor snelheid, GEZIEN op de pagina). Wat het zwaar maakt: tekenen in de viewport met de `gpu`-module, snappen op het oppervlak (BVH), lussen en strips die netjes aansluiten, en het moet lekker voelen. Testen kan in onze e2e met Blender 4.2 en 5.3, maar "voelt het goed" kunnen wij niet testen zoals een artiest dat doet.

**Geld na 3 maanden (GOK):** lukt het TopoPen-niveau niet helemaal, dan 20 tot 60 verkopen per maand. Rekensom bij 40 per maand à $24: 40 × ($24 × 0,65 − $0,49) = 40 × $15,11 = ±$604, ±€550 per maand (omrekening $1 = €0,91, GOK; aandeel maker 65% min $0,49 uit `platformen/blender/kandidaten-2026-11-07.md`). Op TopoPen-niveau (167 per maand): ±$2.520, ±€2.300 per maand.

**Ideeëntest kort:** wet 1 (vroeg) zwak, Superhive is niet nieuw. Wet 2 (brede basistaak) ja. Wet 3 (kassa) ja. Wet 4 (Blender rolt het binnen 3 maanden uit) ONBEKEND; er is een draad "Thoughts on a dedicated retopology mode?" (DERDEN, https://blenderartists.org/t/1646183) maar ik zag geen besluit van Blender. Vraag 8 (waarom bestaat het nog niet?): het bestaat wel, de dure nummer 1 heeft klachten en de goedkope nieuwkomer is moeilijk te leren.

**Grootste reden om te mislukken:** TopoPen zit al precies op de plek "goedkoper en moderner dan RetopoFlow", 3 maanden voor ons, en de lat ligt bij gevoel en snelheid in de viewport. Wij kunnen dat gevoel niet zelf testen met een pen, en een tekentool die niet lekker voelt krijgt 1 ster.

**Cijfer: 5 van 10.**

## Kans 2: Automatisch skinnen of gewichten zetten voor een figuur met rig

**Wat:** een knop die lijf en kleren aan het skelet hangt met goede gewichten, zonder de bekende fout van Blender "Bone Heat Weighting: failed to find solution for one or more bones". Past bij wat wij al kunnen: Click Joints Pro leest 8 soorten rigs (`organisatie/lat/click-joints-pro.md`).

**Pijn (DERDEN):** "Bone Heat Weighting: failed to find solution" (https://blenderartists.org/t/1144412 en https://blenderartists.org/t/1548984), "Large parts of model not moving with armature" (okt 2025, https://blenderartists.org/t/1614036), "I can't rig this :(((" (apr 2026, https://blenderartists.org/t/1637532), "Rigged model is contorting weirdly" (sep 2026, https://blenderartists.org/t/1652575). In reviews: "Blender's built-in automatic weights have always been somewhat limited" (GEZIEN, https://superhivemarket.com/products/adaptive-auto-skinning/ratings).

**Kopers:**
- Voxel Heat Diffuse Skinning: 13.200+ in ±9 jaar, 77 ratings, gemiddeld 5 (GEZIEN, https://superhivemarket.com/products/voxel-heat-diffuse-skinning).
- Adaptive Auto Skinning: 1.000+ in 5 maanden, 22 ratings, gemiddeld 5, deze week in "Top Selling Items this Week" (GEZIEN).
- Auto-Rig Pro (71.600+) en de Quick Rig (10.200+) doen skinnen mee (GEZIEN, teller; dat ze skinnen: GOK op de naam en de review van Nikolaus "integrated into auto rig pro").

**Prijs:** $30 (Voxel Heat Diffuse, `productData`), $35 (Adaptive), $25 (Voxel Weight Transfer, voor kleren op een lijf met gewichten), bundel $45 (GEZIEN).

**3 sterkste concurrenten en hun zwakke plek:**
| | Prijs | Teller | Zwakke plek |
|---|---|---|---|
| Adaptive Auto Skinning | $35 | 1.000+ in 5 mnd | eigenlijk geen: 96% 5 sterren, "Does exactly what it says on the tin", gemiddeld 0,57 s per figuur op een benchmark van 202 figuren, op de GPU onder macOS, Windows en Linux (GEZIEN). Alleen voor wie geen goede GPU heeft: GOK. |
| Voxel Heat Diffuse Skinning | $30 | 13.200+ | oud (±9 jaar op de markt) maar 90% 5 sterren en nog steeds "a MUST have" (GEZIEN, ratings). Je moet de voxelresolutie zelf zoeken: "Find out the perfect voxel resolution for your mesh (it can be too low or also too high)" (GEZIEN, review Oli Gerber). |
| Auto-Rig Pro | $50 | 71.600+ | groot en duur als je alleen wilt skinnen (GOK). |

**Bouwen voor ons:** GOK 6 tot 10 weken voor een eigen oplosser die tegen deze twee op kan. Een snelle versie kan wel in 2 tot 3 weken met alleen Blender zelf: een dichte voxelkopie maken (Remesh), daarop Automatic Weights, dan met Data Transfer terug naar het echte model. Maar dat is de werkwijze uit gratis tutorials, en Adaptive doet het beter en sneller. Een echte volumetrische oplosser in Python met numpy is mogelijk, maar zonder GPU trager dan Adaptive (GOK).

**Geld na 3 maanden (GOK):** 10 tot 40 per maand. Rekensom bij 25 per maand à $30: 25 × ($30 × 0,65 − $0,49) = 25 × $19,01 = ±$475, ±€430 per maand.

**Ideeëntest kort:** wet 2 ja voor iedereen die figuren rigt, wet 3 ja. Vraag 2 (concurrenten): **bestaat al goed en betaalbaar** (Adaptive, 5 sterren, net uit); een aantoonbaar gat vond ik niet. Dat is bijna een harde nee.

**Grootste reden om te mislukken:** de nieuwkomer van dit jaar (Adaptive) is al beter dan wat wij in weken kunnen bouwen, en de oude nummer 1 heeft nog steeds 5 sterren.

**Cijfer: 3 van 10.** Bruikbaar wel: als functie binnen Click Joints Pro (gewichten voor het figuur dat wij al lezen), niet als losse grote markt.

## Kans 3: Gaten en randen dichten met nette vierhoeken ("quad fill")

**Wat:** selecteer twee open randen of een gat, één klik, en er komt een net stuk vierhoeken tussen. Hoort bij modelleren en bij retopologie ("I purchased this right before working on a small retopology project", GEZIEN, review ZAPcon bij Quad Filler).

**Kopers:**
- Quad Filler: Sales 1.900+, ±1 jaar oud, 9 ratings, gemiddeld 4 (56% 5 sterren, 23% 3 sterren, 12% 2 sterren) (GEZIEN, https://superhivemarket.com/products/quad-filler en /ratings). Dus ±158 per maand (GOK op GEZIEN). Maker Casey Sheep heeft nog 3 nieuwkomers boven de 500 (GEZIEN, dataset).
- Quad Maker: $18, 1.200+ in ±2 jaar, 38 ratings, 5 sterren in beeld (GEZIEN, zoeken "quad fill").
- Easy Patch: $14,90, 900+ in bijna 3 jaar, 8 ratings (GEZIEN).
- Gratis in Blender: Grid Fill en Bridge Edge Loops; gratis add-ons LoopTools (2M downloads) en F2 (440K) (GEZIEN, Extensions). Een koper zegt zelf: "Very similar to loop tools bridge feature though with bridge you do not get quads" (GEZIEN, review Louis Laurents).

**Prijs:** $15, of $24 met donatie (Quad Filler, GEZIEN in de varianten); $18 (Quad Maker); $14,90 (Easy Patch).

**3 sterkste concurrenten en hun zwakke plek:**
| | Prijs | Teller | Zwakke plek (GEZIEN, reviews) |
|---|---|---|---|
| Quad Filler | $15 | 1.900+ | "the result becomes unreliable as soon as the selection is even slightly complex ... faces twist, flip, or fill in an unexpected direction"; "I'd much rather have it stop clearly with a warning"; geen gesloten lussen ("The lack of closed loop support definitely holds back quad filler"); de maker zegt zelf dat het draaien van vlakken "a known minor issue" is: "pressing Ctrl+Z and filling again usually resolves it". |
| Quad Maker | $18 | 1.200+ | niet gelezen in deze run (ONBEKEND). |
| LoopTools Bridge en Grid Fill (gratis) | $0 | 2M | geen nette vierhoeken bij ongelijke randen (review hierboven). |

**Bouwen voor ons:** GOK 2 tot 3 weken. Puur `bmesh` in Python, goed te testen in de e2e (tel vierhoeken, kijk of normalen goed staan, geen gedraaide vlakken), zonder gevoel in de viewport. Onze sterke kant past: duidelijk stoppen met een reden in plaats van stil iets kapot maken, zoals wij nu al doen met "No end stop found" in Pro.

**Geld na 3 maanden (GOK):** 20 tot 60 per maand. Rekensom bij 40 per maand à $15: 40 × ($15 × 0,65 − $0,49) = 40 × $9,26 = ±$370, ±€340 per maand. Zelfs op het niveau van Quad Filler (158 per maand) is het ±$1.460, ±€1.330 per maand: even groot als onze eigen hoek, niet groter.

**Ideeëntest kort:** wet 2 half (veel modelleurs, maar het is één handeling), wet 3 ja. Vraag 1: deels ingebouwd (Grid Fill), maar betaalde tools verkopen ernaast. Vraag 8: de huidige nummer 1 is onbetrouwbaar bij lastige selecties; dat is een eerlijk gat.

**Grootste reden om te mislukken:** de markt is klein en goedkoop ($15); het lost de vraag van issue #323 (een grotere markt) niet op.

**Cijfer: 4 van 10** als losse markt, wel de snelste en veiligste van de drie.

---

## Afgevallen (zodat niemand ze opnieuw loopt)
| Idee | Waarom niet (bron) |
|---|---|
| UV automatisch uitvouwen | Auto Unwrap $18, 1.300+ in 2 mnd, 9 ratings gemiddeld 5, met een getraind model ("retrained on more than 1,200 pieces"); Zen UV $24, 13.400+; UVPackmaster $55, 20.100+; gratis Mio3 UV 327K en UniV 116K downloads (GEZIEN). Geen zwakke plek. |
| Automatisch remeshen naar vierhoeken | vraagt een zware rekenmotor (C++ of getraind model); Smart Remesh 2.800+ in 3 mnd, SoftWrap 3.800+ 5 sterren, gratis QRemeshify 511 ratings op Gumroad (GEZIEN). |
| Foto of tekst naar 3D-model | AI; mag niet genoemd worden (harde regel 5) en vraagt een GPU-model (Image to 3D, "generated entirely on your own graphics card", GEZIEN). |
| Lucht en atmosfeer | Physical Starlight $70 17.100+, Physical Atmosphere $84 1.000+ in 4 mnd, True Sky $39 1.900+ (GEZIEN); natuurkunde en beeldkwaliteit die wij niet kunnen keuren. |
| Explosies en schade | oude 3-sterrenproducten, maar RBDLab $74 6.100+ 5 sterren en het nieuwe Project Damage in "New and Rising" (GEZIEN); simulatie is zwaar. |
| Voorwerpen laten vallen met fysica | Physics Dropper kost $4 en heeft 3.300+ verkopen met 43 ratings (GEZIEN, zoeken "physics drop"). Te goedkoop. |
| Rig naar game-engine (Unreal, Unity, Godot) | Game Rig Tools op Superhive heeft tag 3.0 tot 4.5 en laatste update in de tekst 28 okt 2021 (GEZIEN, https://superhivemarket.com/products/game-rig-tools-blender-addon-game-rigs), dus verouderd. Maar het staat gratis (betaal wat je wilt) op Gumroad met 939 ratings (GEZIEN, Gumroad-zoek), Auto-Rig Pro doet het ook, en op Superhive is het maar 1.100+ in 5 jaar à $15. Weinig betaalbewijs. Wel dichtbij ons (rig lezen): bewaren als idee voor Pro. |
| Licht zetten | druk: Light Painter $40 2.400+ in 12 mnd, Light Master Pro $12 1.300+ in 7 mnd, Gaffer $19 4.700+, gratis QLE 47K en Easy HDRI 621 ratings (GEZIEN). |

## Ranglijst
| Plek | Kans | Cijfer | Weken (GOK) | €/maand na 3 mnd (GOK) | Grootste twijfel |
|---|---|---|---|---|---|
| 1 | Hand-retopologie | 5 | 5 tot 8 | ±€550 (bereik €200 tot €2.300) | TopoPen was ons 3 maanden voor; gevoel in de viewport kunnen wij niet testen |
| 2 | Quad fill | 4 | 2 tot 3 | ±€340 (bereik €170 tot €1.330) | markt even klein als onze eigen |
| 3 | Automatisch skinnen | 3 | 6 tot 10 | ±€430 (bereik €170 tot €700) | Adaptive Auto Skinning is net uit en al beter |

Ter vergelijking, onze eigen hoek: Cleave ±150 per maand à $23 = ±$2.170, ±€2.000 per maand voor de nummer 1 (GOK op GEZIEN, `organisatie/lat/click-cuts.md`). Geen van de drie kansen is voor een nieuwkomer duidelijk groter dan dat.

## Advies
**Niet doen als hoofdroute.** Route C belooft een grotere markt, maar die zie ik niet voor een nieuwkomer zonder publiek: wie nieuw binnenkomt in retopologie of skinnen haalt 150 tot 200 per maand, net als Cleave en CatPin in onze hoek, en de grootste groeiers van dit jaar hebben een rekenmotor (getraind model, GPU) of een maker met een publiek. Daarbij kost een goede retopologie-tool ons 5 tot 8 weken, dus het eerste geld komt pas in februari (GOK). Dat past niet bij "snel veel geld".

Wat het meeste oplevert per week werk, volgens deze cijfers: **in de 3D-printhoek blijven en daar de nummer 1 worden.** Die hoek staat deze week met Cleave in de top 9 van heel Superhive; het plafond van de nummer 1 is ±€2.000 per maand (GOK), en wij staan nu op 1 verkoop. Het gat tussen ons en Cleave is groter dan wat route C binnen 3 maanden kan opleveren.

Wil Thijs toch een stap buiten de printhoek: dan **alleen kans 3 (quad fill) als proef van 2 tot 3 weken**, omdat het snel en testbaar is en dezelfde kopers raakt als kans 1. Stopregel: minder dan 20 verkopen in de eerste 4 weken na live = niet doorbouwen naar hand-retopologie. Komt hij er wel boven, dan is kans 1 de volgende stap en gebruiken we de quad fill-code daarin.

## Bronnen voor de keurder (snelle controle)
- Voorpagina met de weeklijst: https://superhivemarket.com/ (blok "Top Selling Items this Week").
- Bestsellers op verkoop: https://superhivemarket.com/categories/addons/browse?sort_sales=desc (pagina 1 tot 20; dataset `route-c-data/superhive-top477-2026-11-27.jsonl`).
- Market stats: https://superhivemarket.com/market-stats.
- Productpagina's en ratings: `https://superhivemarket.com/products/<slug>` en `/products/<slug>/ratings` voor retopoflow, topopen, speedretopo, adaptive-auto-skinning, voxel-heat-diffuse-skinning, quad-filler, auto-unwrap, smart-remesh, imageto3d, cleave.
- Extensions op downloads: https://extensions.blender.org/add-ons/?sort_by=-download_count.
- Gumroad op meeste ratings: https://gumroad.com/products/search?taxonomy=3d%2F3d-assets%2Fblender&sort=most_reviewed.
- Tellers veranderen elke dag en de sale loopt tot 2 dec; wie later kijkt, ziet andere getallen en saleprijzen.
