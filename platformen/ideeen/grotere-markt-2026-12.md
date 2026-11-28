# Grotere markt voor Dortus: één ranglijst en één advies (issue #323)

Vaste Afkijker, za 28 nov 2026 ±05:45 tot 06:45 NL. Derde, onafhankelijke controle op `grotere-markt-2026-12/route-b.md` (Afkijker B) en `route-c.md` (Afkijker C), na hun kruiskeuring (`keuring-route-b-door-c.md`, `keuring-route-c-door-b.md`). Alleen onderzoek, niets gebouwd, niets geplaatst, geen account. Alles hieronder met GEZIEN heb ik zelf met curl gelezen op 28 nov tussen 06:00 en 06:30 NL. Let op: de Cyber Sale van Superhive loopt tot wo 2 dec, dus winkelpagina's tonen ook een saleprijs; ik noem de gewone prijs uit `productData`.

## Kort
- **Advies: niet naar een nieuwe markt. Blijf tot half december in de printhoek en verdien meer per verkoop.** Geen van de zes kansen geeft een nieuwkomer in 3 maanden meer dan een nieuwkomer in onze eigen hoek al haalt (Cleave ±$2.200 en CatPin ±$3.300 per maand netto voor de maker, GOK op GEZIEN), en elke kans kost 2 tot 8 weken nieuw bouwen.
- **Nieuw uit deze controle:** CatPin vraagt $30 en verkoopt even snel als Cleave à $23 (allebei ±150 tot 170 per maand, GOK op GEZIEN). In onze hoek kost een hogere prijs dus geen zichtbare verkopen. Daarom hieronder een concreet prijsvoorstel voor Click Cuts en Pro.
- **Mag Thijs toch iets nieuws willen:** alleen quad fill (route C kans 3) als proef van 2 tot 3 weken, na 14 dec, met een stopregel. De Orca-plugin (route B kans 1) pas als iemand met een Orca Cloud-account in de hub zocht (account is aan Thijs).

## 1. Controle: per kans twee cijfers zelf nagekeken
| Kans | Cijfer in het stuk | Wat ik zag (28 nov, curl) | Klopt? |
|---|---|---|---|
| B1 Orca-plugin | OrcaSlicer 2.5.0 op 7 nov 2026 | newreleases.io: `2026-11-07T07:13:09` | ja |
| B1 | TrestleFDM 268 verkopen, $12, 8 ratings 5,0 | Gumroad-data: `sales_count` 271, `price_cents` 1200, 8 ratings, gemiddeld 5.0 | ja (3 verkopen erbij sinds gisteren) |
| B1 | Split3r 2.501 backers, 114.405 | Kickstarter `stats.json`: `backers_count` 2501, `pledged` 114405.0, `successful` | ja |
| B2 Website gewrichten | JointLab 1.537 accounts | `jointlab3d.com/api/stats`: `registeredUsers` 1542 | ja (5 erbij in ±9 uur) |
| B2 | JointLab Pro $9,99 per maand, $89,99 per jaar, $159,99 levenslang | plannenpagina: precies zo, plus eerste maand $3,99 | ja |
| B3 Modellen verkopen | Flexi Factory 7.377 betalend van 45.738 | Patreon-API: 7376 van 45739 | ja |
| B3 | Cinderwing3D 6.306 van 48.145; NunnBreakable 7 van 311 | 6302 van 48139; 7 van 311 | ja |
| C1 Hand-retopologie | TopoPen 500+, 3 maanden, $24,99 | 500+, "3 months ago", `price` 2499, nu 15 ratings (was 14) | ja |
| C1 | RetopoFlow 11.800+, 62 ratings, $59,99 | 11800+, 62 ratings, `price` 5999 | ja |
| C2 Skinnen | Adaptive Auto Skinning 1.000+, 5 maanden, $35 | **1100+**, "5 months ago", 23 ratings, `price` 3500 | ja, teller loopt op |
| C2 | Voxel Heat Diffuse 13.200+, ±9 jaar, $30 | 13200+, "about 9 years ago", 77 ratings, `price` 3000 | ja |
| C3 Quad fill | Quad Filler 1.900+, ±1 jaar, $15 of $24 met donatie | 1900+, "about 1 year ago", 9 ratings, varianten $15 en $24 (`productData.price` zegt 9900, maar de zichtbare varianten en `max_price` 2400 zeggen $15 tot $24; ik ga uit van de varianten) | ja |
| C3 | Quad Maker $18, 1.200+ | Sales 1200+, $18 (sale $11,70) | ja |
| Prijs | Cleave $23, CatPin $30, Dovetail Key $18, Physical Atmosphere $84 | `price` 2300, 3000, 1800, 8400; tellers 300+ (2 mnd), 500+ (3 mnd), 800+ (5 mnd), 1000+ (4 mnd) | ja |

Niets geschrapt: geen enkel cijfer bleek fout. Twee tellers liepen sinds gisteren op (TrestleFDM, Adaptive); dat verandert geen oordeel.

**Moets uit de kruiskeuring, opgelost?**
- Route B, moet 1 (rekenfout kans 1): ja, nu 2.000 x 3% = 60 kopers, ±€240 per maand, plus een tweede scenario met ons eigen cijfer (0,3%, ±€24). Nagerekend: 20 x $13,00 = $260, klopt.
- Route B, moet 2 (API leest alleen, delen op de plaat via omweg): ja, deel 4 en kans 1, bouwtijd naar 4 tot 6 weken.
- Route B, moet 3 (openbare code, geen kassa): ja, drie eerlijke opties genoemd.
- Route B, moet 4 (geen splitser in de hub = ONBEKEND, Embedder als concurrent): ja.
- Route C, moet 1 (geld per maand, waarom producten wegvallen): ja, geldkolom met de makersformule (prijs min 5,5% min $0,49) x 70%. Nagerekend: TopoPen 167 x $16,19 = ±$2.700, Cleave 150 x $14,87 = ±$2.230, klopt.
- Route C, moet 2 (eerlijk vergelijken, nieuwkomer tegen nieuwkomer): ja, staat in "Ranglijst" en "Advies".
- Klein, niet blokkerend: route B noemt de maker van Embedder "minstens 7" plugins, keuring C "minstens 8". Maakt niets uit voor het oordeel.

## 2. Eén ranglijst over beide routes
Euro per maand na 3 maanden is de middenschatting uit de route-bestanden (GOK, rekensom daar). "Euro per bouwweek" deelt dat door het midden van de bouwweken (GOK), om snel geld eerlijk te wegen.

| Plek | Kans | €/maand na 3 mnd (GOK) | Bouwen (GOK) | € per bouwweek | Grootste twijfel |
|---|---|---|---|---|---|
| 1 | C3 Quad fill (gaten dichten met vierhoeken) | ±€349 (€174 tot €1.380) | 2 tot 3 weken | ±€140 | markt kleiner en goedkoper ($15) dan onze eigen hoek |
| 2 | C1 Hand-retopologie | ±€565 (€283 tot €2.360) | 5 tot 8 weken | ±€87 | TopoPen zit er al, gevoel met een pen kunnen wij niet testen |
| 3 | C2 Automatisch skinnen | ±€444 (€177 tot €710) | 6 tot 10 weken | ±€55 | Adaptive Auto Skinning (5 sterren, net uit) is al beter |
| 4 | B1 Click Cuts als OrcaSlicer-plugin | ±€75 (€4 tot €240) | 4 tot 6 weken | ±€15 | geen kassa, openbare code, delen op de plaat niet te testen op Windows en Mac |
| 5 | B2 Website STL naar gewrichten | ±€60 (€0 tot €300) | 5 tot 8 weken | ±€9 | drie gratis alternatieven, ons voordeel (rig lezen) valt weg bij een STL |
| 6 | B3 Zelf beweegbare modellen verkopen | €0 tot €50 | 1 tot 2 weken plus prints | n.v.t. | geen printer, dus nu dood |

Ter vergelijking, zonder bouwtijd: een nieuwkomer in onze eigen hoek haalt ±150 tot 170 stuks per maand (Cleave, CatPin, Dovetail Key; GOK op GEZIEN, teller gedeeld door leeftijd). Dat is ±€2.000 tot €3.000 netto per maand voor de maker (GOK). Wij staan daar nog niet: Click Joints Pro 1 verkoop, Click Cuts sinds vr 27 nov live op Gumroad (`organisatie/lat/click-joints-pro.md`, `producten/blender-splitser/KAART.md`). Het gat tussen ons en hen zit in etalage, reviews en bereik, en dat kost geen nieuwe weken bouwen.

Mijn eigen kijk naast B en C: beide routes zijn eerlijk en de cijfers kloppen. De ranglijst van C (retopologie boven quad fill) en mijn ranglijst verschillen alleen omdat ik snel geld per bouwweek weeg; C weegt het plafond. Bij "snel veel geld" wint de korte proef.

## 3. Prijsvoorstel voor Click Cuts en Click Joints Pro
**Wat we weten (GEZIEN 28 nov, gewone prijs):** Cleave $23 en $28 (±150 per maand), CatPin $30, $45 en Studio $100 (±167 per maand), Dovetail Key $18 (±160 per maand), SnapSplit $20 (Sales 30+, lat Click Cuts), NB Figure Joints $25, SlicerJoint Pro $20, JointLab $65 (20+ in 4 maanden). CatPin heeft net als Cleave en wij geen grote naam (route C: "Maker had al een hit? nee"). Bij de duurdere producten in route C verkopen teams en studio's een eigen variant (MatPlus $300 en $600, CatPin $100).

**Wat al besloten is:** Click Cuts $19 intro tot en met zo 14 dec, vaste prijs daarna op basis van verkoop (Thijs 25 nov 22:03); Supporter $29. Pro Gumroad $19, $24, $59; Superhive van $12 en $45 naar $19 en $59 op do 3 dec (besluiten r. 27 en 90).

**Voorstel Click Cuts vanaf ma 15 dec** (past in "op basis van verkoop"):
- Standard **$25**, Supporter **$35**, nieuw **Studio $79** (5 plekken, voor wie verkoopt of in een team print; CatPin vraagt $100).
- Hoger, Standard $29, pas als Click Cuts op 14 dec minstens 10 verkopen en 3 beoordelingen heeft; minder dan 3 verkopen in totaal: op $22 blijven, want dan is het bereik het probleem en niet de prijs.
- Waarom $25 en niet $30: CatPin bewijst dat $30 in deze hoek verkoopt, maar heeft al 500+ verkopen en 4 ratings als bewijs; wij beginnen met 0. $25 zit tussen Cleave ($23) en CatPin ($30), gelijk aan NB Figure Joints.
- Rekensom (GOK, Superhive-formule): bij 30 verkopen per maand geeft $25 per stuk ±$16,19 netto, samen ±$486; $19 geeft ±$12,23, samen ±$367. Verschil ±$119 per maand bij gelijke stuks (+32%).

**Voorstel Click Joints Pro:**
- **Geen prijsstap boven $19 nu.** Met 1 verkoop is de prijs niet het probleem; bereik en etalage wel (lat Pro, gat 2 en 3). De stap naar $19 op Superhive op 3 dec gaat gewoon door.
- Naar **$29 Personal** (Supporter $35, Studio $59 blijft) zodra Pro 10 verkopen en 3 beoordelingen heeft. Grond: Pro doet meer dan een splitser (rig lezen, gewrichten met eindstop), NB Figure Joints vraagt $25 zonder rig, JointLab $65.
- **Bundel Pro plus Click Cuts voor $39** (los samen $44 bij $19 plus $25), zodra Click Cuts op Superhive is goedgekeurd en Pro daar $19 kost. Past bij het besluit "later een bundel" (besluiten r. 36 en 105) en de keuring van Daan ("geen bundel zolang Pro $12 kost"). Een bundel is ook een kans op de bundellijst van Superhive (lat Pro, RetopoFlow).

Eigenaar van de prijzen: hoofdchat met Bram (Pro) en de Productbouwer (Click Cuts). Dit is een voorstel, geen besluit; een prijsverhoging kost geen geld, dus Thijs hoeft er volgens regel 1 geen ja op te geven, maar de intro-afspraak van Click Cuts loopt tot 14 dec en blijft staan.

## 4. Advies (één)
**Geen nieuwe markt. De komende weken alles op Click Cuts en Pro in de printhoek, met de prijzen uit deel 3.** Reden in één zin: een nieuwkomer haalt in retopologie, skinnen of de printwereld buiten Blender niet meer stuks dan een nieuwkomer in onze hoek, terwijl wij daar al twee producten hebben staan en alleen nog etalage, reviews en bereik missen.

Wil Thijs na 14 dec toch een stap buiten de printhoek:
1. **Quad fill als proef**, 2 tot 3 weken bouwen, prijs $19 (Quad Filler $15 en $24, Quad Maker $18). Ons gat: Quad Filler draait vlakken bij lastige selecties en kent geen gesloten lussen (reviews, route C kans 3). Stopregel: minder dan 20 verkopen in de eerste 4 weken na live, dan niet verder naar hand-retopologie.
2. **De Orca-plugin alleen na twee checks:** iemand met een Orca Cloud-account zoekt in de hub op "split", "cut", "connector", "dowel" en "joint" (een account maken is aan Thijs), en een proef van 2 tot 3 dagen laat zien dat gesneden delen op de plaat komen. Dan alleen als gratis etalage voor Click Cuts, niet als eigen inkomen.

## Open punt voor Thijs (via de hoofdchat)
Orca Cloud-account voor de zoekvraag in de plugin-hub (±2 minuten). Alleen nodig als hij de Orca-route wil openhouden; anders vervalt het.

## Bronnen (zelf gelezen 28 nov)
- Superhive: https://superhivemarket.com/products/ met topopen, retopoflow, adaptive-auto-skinning, voxel-heat-diffuse-skinning, quad-filler, quad-maker, cleave, catpin, dovetail-key, physical-atmosphere.
- https://jointlab3d.com/api/stats en https://jointlab3d.com/planos/?lang=EN
- https://www.kickstarter.com/projects/1492464013/split3r-automatically-split-your-3d-files/stats.json
- https://diogom3d.gumroad.com/l/TrestleFDM
- Patreon-API `https://www.patreon.com/api/campaigns?filter[vanity]=` flexifactory, cinderwing3d, NunnBreakable
- https://newreleases.io/project/github/OrcaSlicer/OrcaSlicer/release/v2.5.0
- Verder alle bronnen in `grotere-markt-2026-12/route-b.md` en `route-c.md`.
