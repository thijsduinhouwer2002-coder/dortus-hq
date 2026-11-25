# Lat: Click Joints Pro (bijgewerkt 24 nov 2026 ±21:40 NL, door de Afkijker)

De 3 sterkste concurrenten in onze winkel (Superhive, waar kopers van Blender-add-ons voor 3D-print zoeken), en waar wij staan. Elk feit met GEZIEN (link) of GOK. Alles gelezen met curl op 24 nov 2026 tenzij anders vermeld. Elke agent leest dit vóór hij iets bouwt, verzint, schrijft of maakt (CLAUDE.md regel 10).

Waarom deze drie: Cleave is de best verkopende add-on voor figuren in 3D-print (plek 3 "Top Selling this Week" op heel Superhive, 22 nov) en wint elke blinde test; Split 3D Print verkoopt het meest (400+); JointLab is de enige die precies ons ding verkoopt (beweegbare gewrichten) en staat op plek 1 bij "articulated". Ook gezien, kleiner: Cut Flex ($34,99, Sales 10+, https://superhivemarket.com/products/cut-flex), CatPin (pinnen, Sales 400+, `platformen/ideeen/afkijken-2-2026-11-21/doorlopend/2026-11-24-catpin-alex-sokol.md`).

## Wie
| | Cleave | Split 3D Print | JointLab | Wij |
|---|---|---|---|---|
| Naam en link | [Cleave](https://superhivemarket.com/products/cleave) (V4SS3UR, solo) | [Split 3D Print](https://superhivemarket.com/products/split-3dprint) (AUER, solo) | [JointLab](https://superhivemarket.com/products/jointlab-) (2 makers, Brazilië) | [Click Joints Pro](https://superhivemarket.com/products/click-joints-pro), [Gumroad](https://dortus.gumroad.com) |
| Prijs (en varianten) | $23, steun $28 (GEZIEN) | $22 (doorgestreept $28), gratis $0, $34, 5 plekken $59 (GEZIEN) | $65 (GEZIEN); daarnaast web-Pro $9,99/maand, $89,99/jaar, $159,99 levenslang ([plannen](https://jointlab3d.com/planos/?lang=EN)) | Superhive $12 Personal, $45 Studio, $3 Lite (GEZIEN); Gumroad $19 / $24 / $59 (besluit 19 nov); Superhive naar $19/$59 op 2 dec (besluit 24 nov) |
| Verkopen, reviews, downloads | Sales 300+ in 2 maanden, 3 ratings (GEZIEN) | Sales 400+, Downloads 400+, 3 ratings, 4 maanden (GEZIEN) | Sales 20+, 3 ratings (gem. 4; 2 van 3 "received for free"), 4 maanden (GEZIEN); web 1.483 accounts ([api/stats](https://jointlab3d.com/api/stats)) | Superhive: geen teller, 0 ratings, 5 dagen (GEZIEN); totaal 1 verkoop $19 (GEZIEN, bord 24 nov); gratis versie 375 downloads (GEZIEN, `producten/blender-gewrichten/taken.md`) |

## Product: wat het kan en hoe het voelt
| Functie of eigenschap | Cleave | Split 3D | JointLab | Wij | Gat? |
|---|---|---|---|---|---|
| Model automatisch in delen knippen | ja, waar het buigt (nek, schouders, knieën) | ja, "Automatic Detection" per deel | ja, met de hand | ja, uit de rig | nee |
| Delen passen op het printbed (controle per deel, resin/FDM) | ja | ja | GOK deels | nee (zit in Click Cuts, apart product) | **ja**, bundel met Click Cuts |
| Verbinders (pinnen, deuvels, magneten, staafkanaal) | ja, 5 soorten | ja, plus socket | ja ("fittings") | nee, alleen gewrichten | klein: wij zijn de gewrichtenmaker, niet de knipper |
| Kogelgewricht | ja | GOK nee | ja | ja, met kleur voor passing en graden | nee |
| Scharnier met eindstop (knie buigt niet achteruit) | nee | nee | GOK nee (presets) | **ja, uit de rig** | ons voordeel |
| Rig lezen, één knop voor heel figuur | nee | nee | nee | **ja**, 8 rigsoorten | ons voordeel |
| Bewegingsbereik in graden zien vóór print | nee | nee | nee | ja | ons voordeel |
| Proefstrip voor speling | nee | nee | nee | ja (Fit test strip) | ons voordeel |
| Gratis proberen | nee | ja, $0-variant op Superhive | ja, gratis in de browser | ja, maar alleen op extensions.blender.org, niet zichtbaar bovenaan de Pro-pagina | **ja**, zie gat 2 |
| Flexi-patronen, lithofanen | nee | nee | ja (1.2.0) | nee | nee, ander publiek |
| Gebruiksgemak: eerste 2 minuten | knip met aantal delen, naden aanpasbaar | knop, plus "Where to find it" bij elke functie | 4 stappen in de tekst; één ster: "Hard to use" | één knop als je een rig hebt; zonder rig 6 presets | let op: zonder rig zijn wij niet makkelijker |
| Updates: hoe vaak, laatste | 11 versies in 8 weken, 1.7.0 op 17 nov ([versies](https://superhivemarket.com/products/cleave/versions)) | V4 11 nov, 4.0.2 13 nov | 1.2.0 op 30 okt, één versie in de lijst | 4 versies in 5 dagen, 1.2.3 op 24 nov | nee |
| Uitleg, handleiding, support | 3 video's op de pagina | "Where to find it" bij elke functie, maker antwoordt op elke review | gidsen op eigen site in 7 talen | update-log, issues, mail; 1 video | klein |

## Paneel (de add-on zelf in Blender, Bram 25 nov 2026, issue #70)
Ons paneel: schermbeelden uit de e2e op main (run 45583103324, commit 2945513, `referentie/blender-gewrichten/main/5.3.0/` en `4.2.23/` op de tak `schermen`): `1-paneel-x.png` (gratis), `16-figuur-rig-paneel.png` en `19-mens-paneel.png` (Pro). Concurrenten: galerijbeelden en tekst van hun Superhive-pagina, gelezen met curl op 25 nov: [Cleave](https://superhivemarket.com/products/cleave) (beeld 6 en 8, kop "One sidebar tab, six steps"), [Split 3D Print](https://superhivemarket.com/products/split-3dprint) (beeld 1 tot 3 en 9 tot 14), [CatPin](https://superhivemarket.com/products/catpin) (beeld 6 tot 9), [MACHIN3tools](https://superhivemarket.com/products/machin3tools) (tekst; de docs op machin3.io weigeren curl, 403). Alles GEZIEN tenzij GOK erbij staat.

| | Cleave | Split 3D Print | CatPin | MACHIN3tools | Wij (Pro 1.2.8) |
|---|---|---|---|---|---|
| Eerste knop die je ziet | "Scan Model" bovenaan, dan een schuif Parts | schakelaar Fast / Expert met één regel uitleg, dan Cut tools en "Automatic Detection" | modus en knippen bovenaan | geen zijbalk: taartmenu's per sneltoets | stap 1 Place met "Check mesh"; **Figure from rig staat in een tweede paneel onder ±880 px andere knoppen** (16-figuur-rig-paneel: niet in beeld; alleen te zien als je het hoofdpaneel inklapt, 19-mens-paneel) |
| Volgorde | zes genummerde stappen, elke stap een eigen in te klappen kop ("3 - Explode & Preview", "4 - Export") | koppen per soort (Cut tools, Automatic tools, Connectors, Inspect, Repair), dicht wat je niet nodig hebt | één lijst | per menu | drie genummerde stappen, daarna los onder Export: "Print this first", "Place hinge, bends up to", "Hinge" (bereik). **Proefstrip en scharnier staan na Export** |
| Standaardwaarden | verbinders in mm | Clearance 0,5 mm, in echte mm | GOK | n.v.t. | Clearance 0,20 mm, kogel "Auto", Ball; scharnier drie standen 90/115/135° |
| Uitleg | video's en "Your first split" | "Where to find it" bij elke functie op de pagina | handleidingen in 11 talen, YouTube | docs per gereedschap | knoptips, één INFO-regel bij Export, "Shift + right click sets the 3D cursor" |
| Foutmeldingen | "the panel warns when one does not fit"; mesh niet dicht: Make Manifold | Mesh Check in beeld, Fix Mesh | Repair Mesh, één klik | n.v.t. | rood vak bij verkeerde maat met knop "Convert to mm"; niet dicht: knop "Make watertight"; Tight/Good fit met reden; "No end stop found" |
| Beoordelingen | 3 | 3 | GOK | 131 ratings | 0; geen regel om te beoordelen |

**De drie grootste verschillen en wat 1.2.9 doet (geen nieuwe functies):**
1. **Eerste klik tot resultaat.** Bij Cleave en Split 3D Print is de automatische knop het eerste wat je ziet; bij ons zat onze sterkste knop (Figure from rig) uit beeld. 1.2.9: heeft je mesh een rig, dan staat bovenaan het paneel "Rig found: <naam>" met de grote knop Figure from rig en "More bones (ankles too)". Zonder rig verandert er niets.
2. **Volgorde.** Cleave en Split 3D Print zetten elke knop in de stap waar hij hoort; bij ons stonden proefstrip en scharnier ná Export. 1.2.9: de proefstrip ("Not sure? Print a fit test first") staat in stap 2 direct onder Clearance, het scharnier ("Or a hinge that bends up to: 90° 115° 135°", Flip bend) in stap 2 onder Place joint, en het bereik van het scharnier in stap 3 bij de passing.
3. **Beoordelingen (gat 3).** Na een Good fit één rustige regel onder het paneel: "Happy with it? Leave a rating:" met knoppen Superhive en Gumroad (gratis: Blender Extensions). Geen popup, niets in ruil.

Voor en na (5.3.0, uit de e2e): `producten/blender-gewrichten/keuring/2026-11-25-1.2.8-paneel-voor.png`, `2026-11-25-1.2.9-paneel-rig-boven.png` (Rig found bovenaan) en `2026-11-25-1.2.9-paneel-na-figuur.png` (nieuwe volgorde, beoordelingsregel).

Niet gedaan, wel gezien: in te klappen koppen per stap (Cleave) en een Fast/Expert-schakelaar (Split 3D Print). Pas doen als een koper of de blinde test zegt dat het paneel te lang is.

## Etalage
| | Cleave | Split 3D | JointLab | Wij |
|---|---|---|---|---|
| Hoofdbeeld (blinde test, plek) | plek 1 bij bijna elke ronde ([uitslag](../blindtest/uitslag/click-joints-pro-superhive-r3-2026-11-24-2123.md)) | concurrent in de test | niet getest | huidige cover plek 2; held-1, 2, 3 met tekst plek 1 tot 2, GESLAAGD; held-4 plek 4 |
| Wat de rechters missen bij ons | | | | een echte print (foto), een gedetailleerd personage in plaats van de houten tekenpop, meer soorten gewrichten in beeld (GEZIEN in de uitslagen) |
| Video op de pagina | 3 | 0 | 1 (197 weergaven) | 1 |
| Titel en eerste zin | "Cleave - Smart Model Split & Cut for 3D Printing with Connectors (Pegs, Dowel, Rod channel, Magnets, Ball Joints)"; "Too big to print? Split it." | "Split-3DPrint"; blok "NEW UPDATE · V4" bovenaan | "JointLab: Articulated Joints & Multi-Part Tools for 3D Printing"; "Create articulated and multi-part 3D prints directly inside Blender", twee knoppen: koop en "USE ONLINE, FREE" | "Click Joints Pro" (kaal); "Rig to printable figure: elbows and knees stop where your rig stops." |

## Marketing: waar en hoe vinden kopers hen
| Kanaal | Cleave | Split 3D | JointLab | Wij |
|---|---|---|---|---|
| YouTube | 4 Shorts per dag, ander figuur per Short, mediaan 1.000, 162 abonnees (GEZIEN 22 nov, `2026-11-22-cleave-shorts-motor.md`) | geen | geen (197 weergaven) | Shorts via hoofdchat, best ±1.300 (GEZIEN 22 nov) |
| Reddit, forums, Discord | GOK weinig | geen | 0 posts in 9 subreddits (GEZIEN) | Reddit-pakket ligt bij Thijs |
| Pers en makers | GOK geen | geen | persblad, `llms.txt` | BlenderNation is onze grootste verwijzer (GEZIEN, bord); persblad in de maak (Bram) |
| Zoeken in de winkel | plek 1 op "ball joint" en "joints" (GEZIEN 21 nov); plek 7 op "3d print" (GEZIEN 24 nov) | plek 10 op "3d print" (GEZIEN 24 nov) | plek 1 op "articulated" (GEZIEN 21 nov) | niet in de top 24 op "articulated" of "3d print", plek 3 op "ball joint" (GEZIEN 21 en 24 nov) |
| Sale, bundels, nieuwsbrief | doet mee aan sales GOK | doorgestreepte prijs nu | eerste maand $3,99 (web) | CYBER25 vanaf 27 nov; mail aan gratis Gumroad-lijst in de maak |

## Gaten, op volgorde van geld
1. **Echte print in beeld.** Beide rechters vragen het bij elk beeld; geen concurrent heeft het wel, dus wie het eerst heeft, wint. Wij: testprint (besluit bij Thijs, kost geld) of een foto van een koper met toestemming. Wie: hoofdchat legt de keus bij Thijs. Wanneer: vóór het einde van de sale.
2. **Gratis proberen bovenaan de Pro-pagina** (JointLab, Split 3D Print). Wij: een regel "Try it free first" met link naar de gratis versie direct onder de eerste zin, op Superhive en Gumroad. Wie: Bram, keuring Daan, hoofdchat plakt mee met de prijsstap van 2 dec.
3. **Beoordelingen.** Alle drie hebben er 3; wij 0. JointLab en Split 3D Print kregen hun eerste via gratis exemplaren. Wie: hoofdchat (ja van Thijs voor benaderen). Wanneer: deze week.
4. **Titel met zoekwoorden** (alle drie). Staat al bij de hoofdchat (melding 21 nov); nog niet gedaan op Superhive (titel nog kaal, GEZIEN).
5. **Gedetailleerd personage in plaats van de tekenpop** in het hoofdbeeld (rechters, Cleave toont orks en ridders). Wie: Bram met de heldenbeelden, blinde test.
6. **Knippen voor het printbed ontbreekt in Pro.** Niet in Pro bouwen; bundel met Click Cuts na 2 dec (keuring Daan 24 nov: geen bundel zolang Pro $12 kost).

## Ons voordeel (waarom kopen ze ons en niet hen?)
Alleen Click Joints leest je rig: één knop geeft elke elleboog en knie een scharnier dat stopt waar je rig stopt, met het bereik in graden, en de Fit test strip zegt welke speling op jouw printer past; de anderen knippen en zetten pinnen of kogels, maar niets stopt een knie die achteruit buigt.
