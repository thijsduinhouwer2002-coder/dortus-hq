# Ideeëntest: derde Click-add-on voor de bundel (issue #294)

Afkijker, vr 27 nov 2026 ±18:00 tot 18:40 NL. Alleen onderzoek, niets gebouwd. Alles gelezen met curl of `gh api` op 27 nov; dat is GEZIEN tenzij er iets anders staat.

**Bronnen die ik gebruikte**
- Superhive: zoeken in Addons (`search[category_id]=6`, op verkoop) en de productpagina's. Let op: vandaag loopt de Cyber Sale (35% eraf), dus de pagina toont de saleprijs; ik zet de gewone prijs erachter (saleprijs gedeeld door 0,65, GOK op afronding). De zoekfunctie van Superhive is los: op "hollow" of "pedestal" komen vooral add-ons die er niets mee te maken hebben (GEZIEN).
- extensions.blender.org: de catalogus-API (`/api/v1/extensions/`, 1.719 items) en de zoekpagina.
- Gumroad: de openbare zoek-API (`gumroad.com/products/search?query=...`).
- Printables: de openbare GraphQL (`api.printables.com/graphql/`, `searchPrints2`, volgorde `popular`).
- GitHub: `gh api search/repositories`.
- Blender Artists: `blenderartists.org/search.json`.
- Niet gelukt: Reddit via Arctic Shift (gaf vijf keer "Timeout. Maybe slow down a bit"), MakerWorld MakerLab (HTTP 403). Daar staat dus ONBEKEND.

**De 4 Kingmaker-wetten** gelden voor alle vijf hetzelfde, net als voor Pro en Click Cuts: Superhive en Gumroad zijn niet nieuw (wet 1 zwak), en het is een nis van Blender-printers (wet 2 zwak). Thijs koos zelf voor een derde add-on in de bundel (issue #294, "doe maar" 17:38), dus ik toets hieronder op de 9 vragen, met als extra vraag: past het in de bundel (zelfde koper, zelfde moment in het werk)?

---

## Kandidaat 1: Voetstuk-maker (sokkel met pin voor een figuur, één klik)

1. **Ingebouwd?** Nee, Blender en de 3D Print Toolbox hebben geen sokkel-knop (GEZIEN, functielijst op https://extensions.blender.org/add-ons/print3d-toolbox/: analyse, hol maken, draaien, schalen, export). Wel: duizenden gratis sokkels als STL op Printables, "display base" 243 modellen, "miniature base" 461, "figure stand" 234 (GEZIEN, API). De populairste: "Lucky 13 display base 2.0" 12.272 downloads (https://www.printables.com/model/563861).
2. **Concurrenten?** Mini Base Maker $12 (saleprijs $7,80, 20 dagen oud, geen verkoopteller, https://superhivemarket.com/products/mini-base-maker): "Round, oval, square and hex bases for tabletop minis, with a one-click seat for your mini". Pose to Print $24 (sale $15,60, 25 dagen oud, geen teller, https://superhivemarket.com/products/pose-to-print) doet een magneetsokkel mee. Printsupportpro $30 (sale $19,50, 70+ verkopen, 2 jaar oud, https://superhivemarket.com/products/printsupportpro) noemt "miniature base" in zijn tekst (GOK op hoe goed). Plus de gratis STL's hierboven.
3. **Vraag?** Zwak. Op Blender Artists vond ik op "miniature base generator" en "display base pedestal print" geen enkele vraag (GEZIEN, search.json). De vraag zit in kant-en-klare sokkels (12.272 downloads), niet in een gereedschap.
4. **Betalen?** Nauwelijks bewijs: Mini Base Maker en Pose to Print tonen nog geen verkopen (GEZIEN).
5. **Bereik?** Zelfde winkels als Pro. Maar een koper zoekt eerder een gratis STL op Printables dan een add-on.
6. **Bouwen en testen?** Ja, binnen een paar dagen (cilinder of zeshoek, pin-gat dat de Fit test strip-maat gebruikt). Testen in Blender, net als Pro.
7. **Kosten en Thijs?** Geen geld. Thijs: alleen de winkelpagina plakken (±10 min, GOK).
8. **Waarom bestaat het nog niet goed?** Omdat een sokkel in Blender in 2 minuten met de hand kan, en gratis STL's overal zijn. Dat is een slecht antwoord.
9. **Geld?** GOK: $0 tot $50 in 3 maanden als losse add-on.

**Uitslag: zwak (3 van 10).** Te weinig bewijs bij 3 en 4. Wel bruikbaar als **gratis toegift in de bundel** of als knop in Click Joints Pro na de bouwstop (sokkel met de pin in de maat van onze kogel).

## Kandidaat 2: Hol maken voor resin (wanddikte en afvoergaten)

1. **Ingebouwd?** **Ja.** De gratis 3D Print Toolbox (703.593 downloads, 54 reviews gemiddeld 5,0, versie 1.5.0, GEZIEN https://extensions.blender.org/add-ons/print3d-toolbox/) zegt letterlijk: "Create consistent thickness for complex shapes with Hollow tool." En de resin-slicers doen het ook: de handleiding van Lychee heeft een eigen pagina Hollowing met "If you can hollow, you should hollow. Just don't forget to add drain holes" (GEZIEN, https://docs.mango3d.io/lychee-slicer/hollowing). Of dat in de gratis Lychee zit: GOK ja.
2. **Concurrenten?** Hollow Object Creator $10 (sale $6,50, 4 maanden, geen teller, https://superhivemarket.com/products/hollow-object-creator). SDFR $15 (sale $9,69, 100+ verkopen, 3 reviews 5,0, noemt "hollow" en "wall thickness", https://superhivemarket.com/products/sdfr). Een bundel van 21 print-add-ons voor $119 met "hollow" erin (https://superhivemarket.com/products/3d-print-suite-bundle).
3. **Vraag?** Eén draad: "I'd like to make a complex model hollow but with a specified wall thickness" (28 sep 2026, 12 berichten, https://blenderartists.org/t/id-like-to-make-a-complex-model-hollow-but-with-a-specified-wall-thickness/1653755). Het antwoord daar is waarschijnlijk de Toolbox of de slicer (GOK).
4. **Betalen?** Zwak, zie de tellers.
5. tot 9. niet verder ingevuld: harde nee bij 1.

**Uitslag: dood.** Ingebouwd in de gratis 3D Print Toolbox (Hollow) en in elke resin-slicer (hol plus afvoergaten). Niet opnieuw voorstellen.

## Kandidaat 3: Print-check (muurdikte en zwakke plekken vóór het printen)

1. **Ingebouwd?** **Ja.** De 3D Print Toolbox doet "Analyze" (dikte, overhang, scherpe randen, niet-gesloten mesh, GEZIEN zelfde pagina) en heeft 703.593 downloads. Click Cuts heeft zelf al een controle per deel (groen, oranje, rood; `organisatie/lat/click-cuts.md`).
2. **Concurrenten?** Printability Check $1 (sale $0,65, 25 dagen, geen teller, https://superhivemarket.com/products/printability-check), Mesh Check GPU $3,50 (200+ verkopen, 8 nov data, `platformen/blender-2/data/superhive-print-2026-11-08.jsonl`), Print Fix $15 (sale $9,75, geen teller).
3. tot 9. niet verder ingevuld: harde nee bij 1, en wat er te koop is kost $1 tot $4.

**Uitslag: dood.** Ingebouwd en gratis; betaalde varianten zitten op $1 tot $4.

## Kandidaat 4 (eigen idee): Pose naar print (een geposeerd, aangekleed figuur in één klik dicht en printbaar)

Waarom gekozen: het is het moment vlak vóór Click Joints (wie poseerbaar wil, of juist één vaste pose) en in de lat van Pro stond NB Figure Joints bovenaan op "action figure blender".
1. **Ingebouwd?** Deels. Voxel-remesh in Blender en "Make Manifold" in de Toolbox maken een figuur dicht (GEZIEN, Toolbox-pagina). Kleding, haar en ogen goed houden doet het niet (GOK).
2. **Concurrenten?** Pose to Print $24 (sale $15,60, 25 dagen, geen teller, https://superhivemarket.com/products/pose-to-print): "Pose a rigged, dressed character, pick a size and a base, press one button: one closed, printable solid with real walls, printable hair, engraved anime eyes and a magnet base". Precies dit idee, net uit.
3. **Vraag?** "Is there a suitable way for generating human models for 3D-Printing?" (dec 2023, 6 berichten, https://blenderartists.org/t/is-there-a-suitable-way-for-generating-human-models-for-3d-printing/1501684). Verder niets gevonden.
4. **Betalen?** Geen bewijs: de enige concurrent toont geen verkopen.
5. **Bereik?** Zelfde winkels.
6. **Bouwen en testen?** Moeilijk: haar, kleding en dunne delen dicht krijgen zonder dat het lelijk wordt. Meer dan een week (GOK).
7. **Kosten en Thijs?** Geen geld, ±10 min plakken (GOK).
8. **Waarom bestaat het nog niet?** Het bestaat net (Pose to Print).
9. **Geld?** GOK: $0 tot $100 in 3 maanden.

**Uitslag: zwak (3 van 10).** Er is net een concurrent zonder verkopen; geen bewijs dat mensen betalen, en het is de tegenpool van Click Joints (vaste pose in plaats van poseerbaar), dus het past matig in de bundel.

## Kandidaat 5 (grondigst, vraag hoofdchat 17:45): Print-in-place

Twee soorten print-in-place, en dat verschil is het belangrijkste wat ik vond:
- **(a) Flexi-dieren en sleutelhangers:** een lijf in schakels die al in elkaar uit de printer komen (draak, slang, kat, vis). Dit is de grootste groep op Printables.
- **(b) Een poseerbaar figuur** met kogels en scharnieren die al vast zitten (zoals Click Joints, maar zonder in elkaar klikken). Dit is veel kleiner.

**Hoe groot is het (Printables, GEZIEN 27 nov, API, volgorde populair):**

| Model | Downloads | Likes | Makes | Link |
|---|---|---|---|---|
| Articulated Night Spirit (Dragon) | 156.624 | 14.472 | 894 | https://www.printables.com/model/413203 |
| Water Dragon, Articulated Dragon | 134.392 | 9.775 | 741 | https://www.printables.com/model/835659 |
| Flexi Rex with stronger links | 122.881 | 17.778 | 2.827 | https://www.printables.com/model/46241 |
| Articulated Bone Dragon | 118.572 | 14.242 | 1.456 | https://www.printables.com/model/538160 |
| Mini Articulated Dragon (Magnet/Keychain) | 94.010 | 9.291 | 629 | https://www.printables.com/model/994795 |
| Print in Place Fully Articulated Skeleton Hand (28 okt 2026) | 27.834 | 4.514 | 289 | https://www.printables.com/model/1415173 |
| Fluffy Tail Cute Flexi Cat Toy / Keychain (2 nov 2026) | 23.671 | 2.822 | 63 | https://www.printables.com/model/1620600 |

Aantallen modellen: "flexi" 8.171, "articulated keychain" 271, "flexi keychain" 408, "print in place articulated" 388 (GEZIEN). Soort (b) is klein: "print in place figure" 43 modellen, de beste 9.702 downloads (Optimus Primal, https://www.printables.com/model/496012); "articulated action figure" 27 modellen, de beste 6.110 (GEZIEN).

1. **Ingebouwd?** Nee. Blender, de 3D Print Toolbox en de slicers maken geen schakels of vaste gewrichten (GEZIEN, functielijst Toolbox; slicers: GOK). MakerWorld heeft MakerLab-generators; of daar een flexi-maker bij zit is ONBEKEND (403).
2. **Concurrenten?** Als losse add-on: **geen gevonden** op Superhive, Gumroad of extensions.blender.org.
   - Superhive "print in place": de bovenste uitslagen zijn algemene print-add-ons (Instant Clean, Speedsculpt, CatPin, Split 3D Print, Cleave), geen enkele die schakels of vaste gewrichten maakt (GEZIEN). JointLab, Cut Flex en Articulator noemen print-in-place niet op hun pagina (GEZIEN, tekst doorzocht).
   - SlicerJoint Pro ($20 Gumroad, 0 beoordelingen, https://blendarttools.gumroad.com/l/slicerjointpro) heeft "Toy Articulation" en een print-in-place ringgewricht (DERDEN, https://blenderartists.org/t/slicerjoint-pro-v1-1-0/1651012). Dat is de enige.
   - Gumroad: "Articulated/Flexi-toy Links", gratis .blend met schakels, 2 beoordelingen (https://afrikaniz3dza.gumroad.com/l/ujgcp). Geen gereedschap.
   - extensions.blender.org: niets op "articulated" behalve Click Joints zelf (GEZIEN, zoekpagina).
   - GitHub: alleen hobbyprojecten van de laatste weken, allemaal 0 tot 4 sterren: rig2print "Rig-aware Blender-to-print-in-place articulation workflow" (14 nov 2026, https://github.com/mickdarling/rig2print), chaveiro-flexi-3d "turns an animal STL into a print-in-place flexi keychain" (24 nov 2026, https://github.com/GiovanniAsantos/chaveiro-flexi-3d), articulated-toys (feb 2026, https://github.com/tusosos/articulated-toys), PolyFidget (14 nov 2026, https://github.com/stb1Cluny/PolyFidget). Mensen proberen het nu, niemand verkoopt het.
3. **Vraag?** Bewijs dat het gezocht wordt:
   - De downloadcijfers hierboven: flexi en articulated zijn bij de populairste modellen van Printables, en er komen nog steeds hits bij (skeleton hand en kat uit okt en nov 2026, elk 20.000+ in een maand, GEZIEN).
   - "Help Creating a Custom Articulated 3D-Printable Figure" (31 okt 2026, https://blenderartists.org/t/help-creating-a-custom-articulated-3d-printable-figure/1656400).
   - "How to Model a poseable figurine?" (nov 2023, https://blenderartists.org/t/how-to-model-a-poseable-figurine/1491951), "Dragon Key Chain" en "Platypus Key Chain" (aug 2023, https://blenderartists.org/t/dragon-key-chain/1477355 en https://blenderartists.org/t/platypus-key-chain/1478182).
   - Vier GitHub-projecten in 2026 die precies dit proberen (zie 2).
   - Reddit: ONBEKEND (Arctic Shift lag eruit).
   Zwakte: de miljoenen downloads zijn van **printers die een model willen**, niet van **makers die een gereedschap willen**. De kopers van een add-on zijn de ontwerpers van flexi-modellen; hoeveel dat er zijn: GOK, enkele duizenden op Printables (8.171 flexi-modellen, veel van dezelfde makers).
4. **Betalen?** Ja, in deze hoek wordt betaald, maar voor modellen: Printables en MakerWorld hebben betaalde flexi-modellen en makers met een eigen winkel (GOK, niet nagekeken in deze run). Voor een flexi-gereedschap is er geen betaald voorbeeld met verkopen; SlicerJoint Pro staat op 0 beoordelingen (GEZIEN). Het dichtstbij: Cleave $23, 300+ verkopen in 2 maanden (GEZIEN 23 nov, `organisatie/lat/click-cuts.md`), voor dezelfde makers.
5. **Bereik?** Beter dan bij Pro: we kunnen het gereedschap laten zien met een **gratis flexi-model op Printables** gemaakt met de add-on (zoals TrailPrint3D het eerste resultaat werd op "blender addon", `organisatie/lat/broncode/trailprint3d.md`, en zoals onze gratis Click Joints er sinds vandaag staat). Op "blender addon" staat op Printables precies 1 resultaat (GEZIEN). Zonder advertentiegeld en zonder Thijs.
6. **Bouwen en testen?** Soort (a) wel binnen ±een week voor een eerste versie (GOK): lijf langs een lijn in schakels snijden, per naad een scharnier met vaste speling, alles plat op het bed. Het grote risico: **wij kunnen niet printen**, en bij print-in-place is de speling alles (een schakel die vastsmelt is het hele model kwijt). We mogen nooit zeggen dat het klikt of dat we printten (harde regel 5). De Fit test strip helpt alleen voor losse delen. Soort (b) is moeilijker (gewricht om een kogel heen dat los blijft), meer dan een week (GOK).
7. **Kosten en Thijs?** Geen geld. Thijs: winkelpagina's plakken (±15 min, GOK). Een echte proefprint door een kennis zou het risico bij 6 halveren, maar Thijs zei "later, niet nu" (besluiten 26 nov 00:38).
8. **Waarom bestaat het nog niet?** Goed antwoord: flexi-ontwerpers bouwen het nu met de hand in Fusion of Blender (de gratis .blend met schakels op Gumroad laat dat zien), de groep is te klein voor grote spelers, en pas sinds dit jaar beginnen mensen er tools voor (GitHub, alle vier 2026).
9. **Geld?** GOK: $150 tot $600 in de eerste 3 maanden als losse add-on van $19 tot $24 (8 tot 30 verkopen). Vergelijking: Cleave haalde 300+ in 2 maanden (GEZIEN), maar dat is de nummer één met 12 updates; Click Joints Pro staat nu op ±1 verkoop (kaart). Als functie in Pro: extra verkopen van Pro, GOK dezelfde orde.

**Losse add-on of Pro-functie?** Soort (b), vaste gewrichten in een figuur, hoort logisch in **Click Joints Pro** (zelfde figuur, zelfde gewrichten, alleen "al in elkaar" in plaats van "klikken"), maar Pro heeft een bouwstop tot 20 verkopen (besluiten 25 nov 23:40), dus niet nu. Soort (a), flexi-dieren en sleutelhangers, is een **andere koper en een ander model** (geen figuur met armen en benen, maar een lijf in schakels) en is als **losse derde Click-add-on** logischer, bijvoorbeeld "Click Flexi". Dat past in de bundel: zelfde winkel, zelfde soort maker die vanuit Blender print.

**Uitslag: overlever, 6 van 10.** Grootste twijfel: betalen flexi-ontwerpers voor een gereedschap (geen enkel betaald voorbeeld met verkopen), en we kunnen de speling niet zelf printen.

---

## Beste 3 concurrenten per kandidaat

| Kandidaat | Concurrent | Prijs (gewoon, GEZIEN in sale 27 nov) | Verkopen of downloads | Beoordelingen |
|---|---|---|---|---|
| 1 Voetstuk | Gratis STL "Lucky 13 display base 2.0" (Printables) | gratis | 12.272 downloads | 1.751 likes |
| 1 Voetstuk | Mini Base Maker (Superhive) | $12 | geen teller (20 dagen) | 0 |
| 1 Voetstuk | Printsupportpro (Superhive) | $30 | 70+ | 0 |
| 2 Hol maken | 3D Print Toolbox, Hollow (extensions) | gratis | 703.593 downloads | 54, gem. 5,0 |
| 2 Hol maken | SDFR (Superhive) | $15 | 100+ | 3, gem. 5 |
| 2 Hol maken | Hollow Object Creator (Superhive) | $10 | geen teller | 0 |
| 3 Print-check | 3D Print Toolbox, Analyze (extensions) | gratis | 703.593 downloads | 54, gem. 5,0 |
| 3 Print-check | Mesh Check GPU (Superhive) | $3,50 | 200+ (8 nov) | 7, gem. 5 |
| 3 Print-check | Printability Check (Superhive) | $1 | geen teller | 0 |
| 4 Pose naar print | Pose to Print (Superhive) | $24 | geen teller (25 dagen) | 0 |
| 4 Pose naar print | Voxel-remesh plus Toolbox "Make Manifold" | gratis | zie Toolbox | |
| 4 Pose naar print | (geen derde gevonden) | | | |
| 5 Print-in-place | SlicerJoint Pro (Gumroad), print-in-place ringgewricht | $20 | ONBEKEND | 0 |
| 5 Print-in-place | Articulated/Flexi-toy Links (Gumroad, .blend, geen tool) | gratis | ONBEKEND | 2 |
| 5 Print-in-place | rig2print (GitHub, hobby, 14 nov 2026) | gratis | 0 sterren | |

## Advies

**Kandidaat 5, soort (a): een losse "Click Flexi" voor flexi-dieren en sleutelhangers, maar pas na de sale en pas na één goedkope vraagproef.** Reden: het is de enige kandidaat zonder gratis of goedkope concurrent (1, 2 en 3 zijn ingebouwd of kosten $1 tot $12), de vraag naar het eindproduct is enorm (flexi-modellen tot 156.624 downloads, en nog steeds nieuwe hits in nov 2026, GEZIEN), en we hebben een gratis bereikroute (een flexi-model op Printables met "made with" erbij, zoals TrailPrint3D). Soort (b), vaste gewrichten in een figuur, bewaren als Pro-functie na 20 verkopen.

Vraagproef vóór bouwen (voorstel, 1 run): tel op Printables hoeveel verschillende makers de top 200 flexi-modellen maakten en hoeveel daarvan betaalde modellen of een winkel hebben. Weinig makers of niemand verkoopt: niet bouwen.

**GOK geld eerste 3 maanden: $150 tot $600** (8 tot 30 verkopen van $19 tot $24; in de bundel met Pro en Click Cuts wat meer). Lager dan Cleave, omdat wij niet kunnen printen en geen geprinte foto's mogen tonen die we niet hebben.

Geen van de andere vier halen: hol maken en print-check zijn dood (ingebouwd), voetstuk en pose-naar-print zijn zwak (geen betalers). Het voetstuk kan wel als gratis toegift in de bundel.
