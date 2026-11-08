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

## 8. Ronde 5 en 6 (7 nov 22:40, twee onderzoekers; nagekeken 22:45, akkoord)
**Bone-jiggle (gat 2):** vraag en betaalbewijs zijn er, maar het veld loopt vol. Alles GEZIEN 7 nov op superhivemarket.com/products/<slug> en extensions.blender.org.
- Betaald: BoneDynamics Pro $15 6.000+ (5 jaar), Swingy $14,79 1.700+ (3 jaar), JiggleMaker $29,99 1.200+ (1 jaar, vangkooi in plaats van botten), Wiggly $8 600+, SquishyFX $15 300+ in 3 maanden, SpringFX $15 100+ in 3 maanden, GOE Jiggle Studio 40+ in 5 maanden. In de laatste maand nieuw zonder teller: Jiggle Wibble $19, Wobble $20,30, SwayMend $19, Inertia Pro $4,99.
- Gratis en bijgehouden: jiggle-physics 92.415 downloads (5,0), wiggle-bones 30.605, wiggle-2 30.213 (v2.4.0, bijgewerkt voor Blender 5).
- Klachten bij de groten: bakken werkt niet of geeft elke keer iets anders, niet samen met Auto-Rig Pro, kapot na hernoemen of dupliceren, geheugen en fps, wens om presets per lichaamsdeel (https://superhivemarket.com/products/bonedynamics/ratings?page=5, https://superhivemarket.com/products/swingy-bone-physics/ratings?page=4).
- Oordeel Bram: vier nieuwe betaalde makers in één maand plus sterke gratis add-ons. We zouden met "betrouwbaar" moeten winnen, en dat is moeilijk te laten zien op een winkelpagina. Niet overtuigend genoeg voor een eerste product. Scores: vraag 4, betaal 4, concurrentie 1, bouwtijd 3, opvallen 3 = 15.

**Verlaten bestsellers verbreed (materials, import-export, vse, asset-management, pagina 2 van modeling en interface, 120 producten):** bijna alle bestsellers ondersteunen al Blender 5. De 8 met 500+ verkopen en Blender 4.2 of lager (DynRemesh, Tesselator, Car-Rig Pro, Layer Painter, Mask Tools, Drag & Drop Import, Sculpt-Paint Wheel, Alt Tab Easy Fog) hebben allemaal een opvolger, een gratis vervanger, of klachten van 3+ jaar oud. Deze aanpak is uitgeput.

## 9. Stand na run 1 en plan voor de volgende run
Bekeken en afgevallen of te zwak: gewrichten (A), AI naar printklaar (B), CAD (C), laser (D), export (E), Pie Menu Editor-opvolger, pivot, bone-jiggle, verlaten bestsellers. Patroon: waar vraag en betaalbewijs zijn, staan nu al meerdere nieuwe makers per maand. Gaten zoeken in bestaande klachten werkt dus slecht.

Andere aanpak voor run 2 (nog niet geprobeerd): **wat is nieuw in Blender zelf en heeft nog bijna geen add-ons?** Blender 4.2 tot 5.x brachten nieuwe onderdelen (bijvoorbeeld Grease Pencil v3, nieuwe geometry nodes zoals bundels en closures, het nieuwe compositor- en VSE-werk, extensies). Nieuwe functies van Blender trekken nieuwe gebruikers die hulpmiddelen zoeken, terwijl de bestaande makers nog op het oude werk zitten (GOK). Plan: release notes van 4.2 tot 5.2 lezen (developer.blender.org/docs/release_notes), per nieuwe functie tellen hoeveel add-ons er op Superhive en extensions.blender.org zijn, en de vragen op BlenderArtists en StackExchange daarover. Daarnaast ronde 5 en 6 laten nakijken.

## 10. Ronde 7: nieuwe Blender-functies (7 nov 22:45, onderzoeker; eerste verkenning, nagekeken 22:45, akkoord)
Bron release notes: https://developer.blender.org/docs/release_notes/ (GEZIEN). Grote nieuwe functies: Grease Pencil v3 (4.3), Slotted Actions (4.4), Bundles en Closures in geometry nodes (5.0), vernieuwde compositor en VSE (5.0), Physics en Lists in geometry nodes (5.2).
- Aanbod (GEZIEN, Superhive-tagpagina's van ±24 kaartjes): geometry-nodes ±37 pagina's (vol), compositor 6, grease-pencil 3, vse 2, action-slots leeg (op extensions.blender.org alleen slot-link echt over slots).
- Vraag (GEZIEN): klein. Action Slots 14 vragen op StackExchange, de grootste 851 views (https://blender.stackexchange.com/questions/339852). VSE 5.0: modifiers kopiëren naar andere strips (https://blender.stackexchange.com/questions/344510), keyframes meeschuiven (https://blender.stackexchange.com/questions/342735).
- Productideeën: Action Slot Manager (klein tot middel) en VSE Strip Modifier Kit (middel). Geen verkoopbewijs, vraag klein (GOK dat het genoeg oplevert).

**Oordeel Bram:** deze aanpak vindt lege plekken, maar met kleine vraag. Dat is het omgekeerde van de rondes hiervoor (grote vraag, vol). Volgende run eerst controleren en dieper: hoe verkochten add-ons die vroeg op een nieuwe Blender-functie inspeelden (bijvoorbeeld de eerste geometry-nodes- en EEVEE Next-hulpmiddelen), want dat zegt of zo'n gok loont. Daarnaast de lijst toppers uit de steekproef van Vera opnieuw lezen op het patroon "nieuwkomer wint ondanks gevestigde concurrent" (Smart Remesh 2.500+ in 3 maanden tegen bestaande remeshers): misschien is beter en mooier maken in een volle markt juist onze weg, en dan past het bij de lat van Thijs dat uiterlijk de helft is.

- 7 nov 22:45, controleur: sectie 8 en 10 akkoord, 16 punten tegen de bron gelegd, geen fouten. Niet nagekeken: Wiggly, GOE Jiggle Studio, wiggle-bones, Inertia Pro.

## 11. Ronde 8: wint een nieuwkomer in een volle markt met een mooier product? (7 nov 23:10, onderzoeker; nog na te kijken)
Methode: alle betaalde add-ons van 2 tot 6 maanden oud met 100+ verkopen uit de steekproef van Vera (±21), per stuk productpagina, ratings en makerpagina gelezen. Links: https://superhivemarket.com/products/<naam>.
- In ±8 gevallen stond een nieuwkomer tegenover een oudere, bekende concurrent; in 6 daarvan had de maker geen eigen publiek: BWrap ($30, 200+ in 2 mnd, tegen SoftWrap $40 3.700+), Easeam 2 ($10, 200+ in 5 mnd, tegen Zen UV $39 13.400+ en UVPackmaster $55 20.000+), AnyNode Preview ($22, 100+ in 3 mnd, tegen Node Preview $25 6.700+), Nitro Retopo ($25, 300+ tegen RetopoFlow $60 11.600+), SDF.R ($15, 100+ tegen ConjureSDF $45), Blaze AutoPose ($40, 400+ in 2 mnd, tegen Cascadeur) (GEZIEN).
- Ze wonnen steeds met een combinatie: lagere prijs plus een smallere, prettigere werkwijze of een nieuwe aanpak. Geen enkel duel waarin alleen "mooier" won. Producten die vooral op uiterlijk verkopen (Eye Features Set, Flow Selection Pro, Crayon Box) zitten in hoeken zonder sterke concurrent en blijven op 100+ (GEZIEN).
- De grootste tellers gaan naar makers met een eigen publiek (Smart Remesh, Metalworks, Lazy Cracker).
- Drie richtingen: (1) UV-werk (naden, uitvouwen, controle) met live naadpreview in kleur, rond $15 tot $20; (2) topologie wrappen voor personages (scan, sculpt, AI-mesh naar animeerbaar), RetopoFlow heeft 17% een of twee sterren en crashes (GEZIEN, /products/retopoflow/ratings), maar elke maand nieuwe remesh-tools; (3) node-previews voor geometry nodes, shaders en compositor, tag node-preview heeft maar 7 producten (GEZIEN).
- Bijvangst: SpringFX ($15, 100+, 4 mnd) won bij bone-jiggle op "easiest to use for beginner".

## 12. Ronde 9: loont vroeg zijn op een nieuwe Blender-functie? (7 nov 23:10, onderzoeker; nog na te kijken)
- Ja bij grote, brede functies: Poly Haven Asset Browser 18.800+ (Asset Browser 3.0), Baga Rain 5.800+ (geometry nodes), Cell Fluids $25 4.500+ (simulation nodes 3.6, 4 mnd na de release), Disintegration FXs 800+. Ze staan jaren later nog bovenaan (GEZIEN, verkooptellers; datums via archive.org, DERDEN).
- Nee bij smalle functies: Light Linking (beste van 12 haalt 60+), Action Slots (Slot Link 4.145 gratis downloads, verder niets) (GEZIEN).
- Risico: Blender bouwt het zelf in. 5.3 krijgt bloom in de compositor (Add Bloom Back 400+ verliest zijn reden) en Native Loop Tools (GEZIEN, release notes).
- Nieuwe grote functie nu: het Physics-systeem in geometry nodes (5.2, juli 2026: cloth, hair, colliders, XPBD-solver). Op Superhive heeft de tag xpbd 1 product: Hurricane, $98, 200+ in 4 maanden (GEZIEN). Vraag op StackExchange klein: 42 vragen, 7.720 views sinds juli 2025 (GEZIEN). Goo Physics $20 2.200+ in 7 mnd laat zien dat physics in het algemeen verkoopt (GEZIEN; waarschijnlijk door YouTube-publiek, GOK).
- Grease Pencil v3: meeste vragen (100+ vragen, 25.076 views sinds 2025), maar veel gratis aanbod (Grease Pencil Tools 154.990 downloads) (GEZIEN).
- Zwak punt: alleen de winnaars zijn zichtbaar, mislukte vroege add-ons niet.

## 13. Controle ronde 8 en 9, scores, doorlichting UV (7 nov 23:15 tot 23:30)
Controleur: 14 cijfers tegen de bron gelegd, op één kleine fout na (AnyNode kost $23, niet $22) klopt alles (GEZIEN). Maar twee conclusies vielen om:
- **Hurricane bewijst niets over de nieuwe physics van 5.2.** Het is een eigen solver van BeFX (makers van FluidLab, eigen Discord met 1.000+ leden) en werkt ook in 5.1. Het physics-systeem van 5.2 is officieel "experimental" en Blender levert zelf al kant-en-klare Cloth Dynamics- en Hair Dynamics-assets mee (GEZIEN, https://developer.blender.org/docs/release_notes/5.2/physics/). Elke maand nieuwe jiggle-tools (Wobble, Strap Sim 20+, swaymend, tatters). **Physics-kit valt af.**
- Scores (vraag, betaalbewijs, concurrentie, bouwtijd, opvallen, inbouwrisico): A physics-kit 16, B UV-naadtool 21, C node-previews 18.

Doorlichting B (UV-naadtool): **valt ook af.** UV Flow ($24,99, 3.900+, Blender 4.2 tot 5.2) heeft precies de klikflow die we wilden (klik, dubbelklik voor een loop, Ctrl-klik voor een pad, alleen het geraakte stuk opnieuw uitvouwen), Easeam 2 is met $9,99 goedkoper dan ons plan, Zen UV toont vervorming al, en gratis Mio3 UV heeft 316K downloads. Automatische naden: Auto Unwrap $18 1.200+ in 2 mnd, Unwrap Me 1.300+ (allemaal GEZIEN, https://superhivemarket.com/products/uv-flow, /easeam-2, /auto-unwrap; https://extensions.blender.org). Wat overblijft (live stretchkleur op het model, eigen naadkleur) is een wedje, geen gat.

**Oordeel Bram na run 2:** negen richtingen bekeken, elke keer hetzelfde: waar vraag en geld is, staat al een goed product en komen er elke maand nieuwe bij. De markt op Superhive is efficiënt. Een nieuwkomer wint daar alleen met een combinatie van lagere prijs en een nieuwe aanpak (sectie 11), of met een eigen publiek, dat wij niet hebben. Overgebleven: C node-previews (18, opvallen 5, maar moeilijk te bouwen via de Python-API) en de richting "topologie wrappen voor personages" (sectie 11, punt 2). Volgende run: C doorlichten met een bouwproef (kan een preview per geometry-node echt met de Python-API?), en de wrap-richting doorlichten. Haalt geen van beide het, dan kiezen we de beste van de rest op bouwtijd en opvallen, in plaats van verder te zoeken naar een gat dat er niet is.

## 14. Doorlichting C node-previews (8 nov 00:20, onderzoeker; kern zelf nagekeken)
**Valt af, geen gat.** Previews per geometry-node bestaan al, betaald en gratis:
- AnyNode Preview ($23, nu $17,25, Lite $2, 100+ in 3 mnd, Blender 4.2 tot 5.3): kaartjes per node voor mesh, curves, instances en velden, ook in zones (GEZIEN, https://superhivemarket.com/products/anynode-preview).
- Geo-Nodes Doctor 2.0 ($33, 10+, 7 mnd): previewkaarten plus debuggen (GEZIEN, /products/geo-nodes-doctor).
- Gratis Node Preview Thumbnails (8.603 downloads, Blender 5.2+): "a small 3D render of the geometry at each node", ook shader en compositor (GEZIEN, zelf nagelezen op https://extensions.blender.org/add-ons/node-preview/).
- Node Preview ($25, 6.700+) doet alleen shaders; een review vraagt om geometry nodes (GEZIEN, /products/node-preview/ratings). Vraag lijkt bescheiden: AnyNode 100+ tegenover 6.700+ voor de shaderversie, BlenderArtists-topic 66 keer bekeken (GOK op GEZIEN). Geen plan van Blender zelf gevonden (GOK).
- Een bouwproef is daarmee niet meer nodig: anderen laten al zien dat het kan; de vraag was of er plek is, en die is er niet (gratis plus goedkope betaalde versie).

**Stand:** van de twee overgebleven richtingen is alleen "topologie wrappen voor personages" (sectie 11, punt 2) nog open. Volgende run: die doorlichten (BWrap $30 200+, SoftWrap $40 3.700+, RetopoFlow-klachten, gratis alternatieven). Valt die ook af, dan kiezen we volgens het oordeel na run 2 de beste van de rest op bouwtijd en opvallen.

## 15. Doorlichting wrap-richting (8 nov 00:25, onderzoeker; nog niet nagekeken door een controleur, HeadWrap en BWrap zelf nagekeken)
- **Kop in één klik valt af.** HeadWrap (Meshwright, $19,99, was $29, 10 dagen oud, Blender 4.2 tot 5.2) zoekt zelf gezichtspunten, legt een schone kop met UV, ogen, tanden en tong eroverheen, pure Python (GEZIEN, https://superhivemarket.com/products/headwrap). Dezelfde maker brengt er snel meer achteraan (FaceKeys, SkinKit, TightWear).
- Aanbod wrappen: SoftWrap $40 3.700+ (7 jaar, geen Mac, klachten over uitleg), BWrap $29,99 200+ in 2 mnd (handmatige punten, gratis versie, 7x 5 sterren, lof voor "betaalbaar en makkelijk"), Wrap4Blender $29 40+ in 4 mnd (alleen Windows), RetopoWrap $25 10+ in 9 mnd (GEZIEN onderzoeker, BWrap-teller zelf nagekeken). Geen gratis wrap voor personages op extensions.blender.org gevonden.
- Nieuwe makers: ±36 nieuwe retopo-, remesh- en wrapproducten in een jaar, bijna allemaal 0 tot 50 verkopen; boven 200 alleen BWrap, Nitro Retopo, Smart Remesh (GEZIEN onderzoeker).
- **Enige open hoek:** heel lichaam (scan of AI-mesh van Meshy of Tripo, A- of T-pose) in één klik naar een vaste game-klare basismesh met UV, ook op Mac, $19 tot $24 met gratis proef. Bouwtijd GOK: 2 tot 3 weken met handmatige punten, 5 tot 8 weken met automatische punten; zwaar: geen scipy in Blender, punten automatisch vinden, haar en kleding die aan het lichaam vastzitten, eigen basismesh (CC0 van MakeHuman kan).
- Risico: vraag mager bewezen (wrapnieuwkomers 10 tot 200+), Meshwright kan dit snel ook doen.

**Voorlopig oordeel Bram:** nog geen besluit. Lichaam-wrap past bij sectie 11 (smallere werkwijze plus lagere prijs) en is goed te tonen (voor en na, opvallen), maar het is groot werk met een sterke snelle concurrent in de buurt. Volgende run: controleur op sectie 14 en 15, dan kiezen tussen lichaam-wrap (met een proef van één week: handmatige punten, wrap met numpy, test in de echte Blender) en de beste van de rest op bouwtijd en opvallen.

## 16. Controle sectie 14 en 15 (8 nov 00:35, controleur; akkoord met correcties, verwerkt)
16 cijfers tegen de bron gelegd, op twee na klopt alles (GEZIEN). Correcties:
- AnyNode Preview Lite kost nu $1,50 (niet $2). Blender-versie: tekst zegt 4.2 tot 5.3, gegevensvak 4.5 tot 5.2.
- **BWrap is niet alleen handmatig:** versie 1.2 is "built for full-body wraps" (kop en lijf samen) en maakt punten ook automatisch uit edge loops. Wrap4Blender doet lichamen met weinig punten (alleen Windows, eigen basismesh). Faceform Wrap (los programma, oud R3DS) noemt full-body scans naar vaste topologie als hoofdtoepassing (GEZIEN controleur).
- "Geen gratis wrap voor lichamen" geldt voor extensions.blender.org en GitHub, gezocht op wrap, retopology, base mesh, topology transfer en scan.
- Meshwright heeft 10 producten voor personages en VRChat, nog geen lichaam-wrap, maar het past in hun lijn.

**Gevolg:** node-previews valt af (bevestigd). Lichaam-wrap is geen leeg gat maar een smal wedje (meegeleverde basismesh met UV, Mac, iets goedkoper), tegenover BWrap met een gratis versie. Volgens sectie 11 wint een nieuwkomer met lagere prijs plus nieuwe aanpak; hier is de aanpak niet nieuw genoeg. **Oordeel Bram: wrap valt af als eerste product.** Beide overgebleven richtingen zijn nu doorgelicht en afgevallen. Volgende run, zoals afgesproken na run 2: kiezen uit wat we al bekeken hebben op bouwtijd en opvallen (geen nieuwe zoektocht), met een kort scoreschema over alle richtingen uit sectie 3 tot 15, en dat besluit in `organisatie/besluiten.md`.

## 17. Scoreschema over alle richtingen en keus (8 nov 01:20, Bram, run 4; nog na te kijken)
Geen nieuwe zoektocht, alleen kiezen uit sectie 3 tot 16. Nieuwe kolom **nieuwkomer verkoopt**: haalt een add-on van een maker zonder eigen publiek in dit hoekje binnen een paar maanden 100+? Dat is volgens sectie 11 het beste voorspellende bewijs voor ons. Scores 1 tot 5, hoger is beter (concurrentie 5 = weinig, bouwtijd 5 = klein).

| Richting (sectie) | Vraag | Betaal | Nieuwkomer verkoopt | Concurrentie | Bouwtijd | Opvallen | Totaal |
|---|---|---|---|---|---|---|---|
| **Bone-jiggle (6, 8)** | 4 | 4 | 4 | 1 | 3 | 5 | **21** |
| UV-naadtool (11, 13) | 4 | 5 | 4 | 1 | 3 | 4 | 21 |
| Gewrichten printfiguren (3) | 3 | 4 | 4 | 1 | 3 | 5 | 20 |
| CAD voor SketchUp-overstappers (3, 5) | 4 | 5 | 4 | 2 | 1 | 4 | 20 |
| PME-opvolger (6, 7) | 4 | 4 | 3 | 1 | 2 | 4 | 18 |
| AI-model naar printklaar (3, 5) | 4 | 2 | 1 | 3 | 3 | 3 | 16 |
| Node-previews (14) | 2 | 3 | 3 | 1 | 2 | 5 | 16 |
| Lichaam-wrap (15, 16) | 3 | 3 | 3 | 2 | 1 | 4 | 16 |
| Physics-kit 5.2 (12, 13) | 2 | 2 | 2 | 3 | 2 | 4 | 15 |
| Laser/CNC (3) | 3 | 1 | 1 | 2 | 5 | 2 | 14 |
| Action Slots / VSE-kit (10) | 1 | 1 | 1 | 5 | 4 | 2 | 14 |
| Export spelmotoren (3) | 2 | 3 | 2 | 1 | 4 | 1 | 13 |
| Pivot-tool (6) | 2 | 3 | 1 | 1 | 4 | 2 | 13 |

Bewijs nieuwkomers bone-jiggle, zelf opnieuw gemeten 8 nov 01:15 (GEZIEN, superhivemarket.com/products/<slug>): SquishyFX $15 300+ in 3 maanden (zachte vervorming), SpringFX $15 100+ in 3 maanden (botten, gewonnen op "makkelijk voor beginners"), JiggleMaker $29,99 1.200+ in ±1 jaar. Oudere: BoneDynamics Pro $15 6.000+, Swingy $14,79 1.700+, Wiggly 600+. Geen teller (dus onder 10): Inertia Pro $4,99 na 3 maanden, Wobble $20,30 en SwayMend $19 (23 dagen). Rigging heeft in de steekproef het hoogste aandeel nieuwe add-ons met 10+ verkopen: 52%, mediaanprijs $20 (sectie 1, GOK op GEZIEN).

**Waarom bone-jiggle boven de UV-naadtool (gelijk op 21):** bij UV bestaat al precies onze werkwijze (UV Flow) en is een nieuwkomer al goedkoper dan ons plan (Easeam 2, $9,99); bij jiggle zijn de klachten over de groten nog niet opgelost door één product (bakken onbetrouwbaar of elke keer anders, niet samen met Auto-Rig Pro, kapot na hernoemen of dupliceren, geheugen, wens om presets per lichaamsdeel, sectie 8). En beweging is het sterkst te laten zien: een winkelpagina met bewegende voorbeelden, het past bij de lat van Thijs dat uiterlijk de helft is. Gewrichten en CAD vallen af om redenen uit sectie 3 en 5 (Cleave dekt de wensen, CAD te groot als eerste product).

**Voorlopige keus: bone-jiggle, smal en anders.** Werktitel "Jiggle". Aanpak (GOK, na controle te scherpen): botten kiezen, een preset per lichaamsdeel kiezen (haar, staart, oren, buik, borst, cape, antenne) met bewegende voorbeeldkaartjes, live meekijken bij afspelen, en een **bak die elke keer precies hetzelfde geeft** (vaste stap, frame voor frame vanaf het begin), die werkt op een rig van Auto-Rig Pro en Rigify zonder iets te breken en die hernoemen overleeft (botten bewaren op naam plus vaste sleutel). Viewport-overlay die laat zien hoe slap of stijf elk bot staat. Prijs $12 (onder de $15 van het veld), lanceerprijs $9. Gratis versie op extensions.blender.org: één keten, live, zonder bakken en presets (GOK, de regels daar nog nalezen). Bouwtijd GOK 2 tot 3 weken in pure Python met numpy.

**Wat dit besluit zou veranderen:** een concurrent die al deterministisch bakken plus presets per lichaamsdeel plus Auto-Rig Pro biedt voor $15 of minder; of de bak in Python is te traag voor een gewone rig (proef in de echte Blender).
