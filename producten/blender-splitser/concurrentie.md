# Splitser: concurrentie tot in detail, en hoe we winnen

Concurrentie-analist, ma 23 nov 2026 ±16:30 tot 18:15 NL. Alles met curl gelezen op 23 nov 2026, geen account, niets betaald gedownload. GEZIEN = zelf gelezen vandaag (link erbij). DERDEN = cijfer van een ander. GOK = eigen schatting. Van mensen alleen openbare namen van makers; reviews zonder naam, met link.

## Zo worden we beter dan de rest (op volgorde van verkoopwaarde)
1. **"Past de eerste keer": passingproef met je eigen verbinder, binnen de splitser.** Eén knop maakt een proefblokje met precies de verbinder die je net plaatste, op 4 spelingen; wat past onthouden we per printer en materiaal. Geen van de grote vier heeft dit; losse proeftools wel (PrintForge $8,99, Fit & Tolerance Test Generator $7, zie 2c). Vraag ernaar is een GOK: geen koper klaagt letterlijk, wel makers ("guess clearances", obloid).
2. **Nooit vastlopen op lelijke meshes (AI-modellen, sculpts).** De meeste klachten zijn fouten, crashes en "vibe coded" knoppen; CatPin weigert open meshes. Wij controleren en maken dicht, met een vaste proefset van 10 AI-modellen in echte Blender bij elke versie. Moeilijker na te doen dan één functie.
3. **Wandcheck per verbinder in mm, met de reden.** CatPin: "user remains responsible for wall thickness"; PrintForge kleurt dunne wanden rood voor het hele model (steekproef), niet per verbinder; Cleave kleurt alleen wat buiten steekt. Wij meten al wanddikte in Click Joints.
4. **Delen liggen plat en verbinders printen zonder steun.** Pen omhoog, gat in het deel dat op het bed ligt, of een losse deuvel. Pijn op Reddit en in de Bambu-tip "Some connectors stop a cut piece from lying flat".
5. **In 60 seconden je eerste snede, zonder video.** Drie genummerde stappen, uitleg in het paneel. De helft van de 4-sterren van CatPin gaat over uitleg.
6. **Nummers gegraveerd in de verborgen snijvlakken, in Blender** (A1 past in A2). Geen Blender-add-on doet dit; Split3MF graveert wel (web, Pro) en PrintForge nummert zonder gravure. Klein verschil, wel goed te zien in een Short.
7. **De lat, geen voorsprong:** een verbinder die maar op één manier past (standaard aan) en printerkeuze met rood of groen per deel (Cleave en Split hebben dit, CatPin niet).

**Niet doen:** niet racen op aantal snijmodi of automatische onderdelenherkenning in versie 1 (CatPin verkoopt het meest zonder); geen uithollen, steun of slicen; geen AI-download van 865 MB; geen prijs onder $19; nooit een concurrent afkraken (CatPin scheldt openlijk op een gratis kloon, dat schaadt); de productnaam niet in Shorts-titels.

---

## 1. Hoe groot is de pot (dit is nieuw)
- **CatPin op Gumroad: `sales_count` 2.042** (GEZIEN, [catpin.json](https://alexsokol.gumroad.com/l/catpin.json); op 16 nov was die teller nog leeg volgens `platformen/succes/verhalen.md`, dus hij staat net aan). Gumroad-pagina aangemaakt 20 jul 2026. Plus **Superhive 400+** (GEZIEN, [Superhive](https://superhivemarket.com/products/catpin)). Samen ±2.450 verkopen in 4 maanden.
- Bruto, GOK: 2.450 keer $21 tot $30, met coupons (30%) en actieprijzen eraf, is **±$35.000 tot $70.000 in 4 maanden**, dus ±$9.000 tot $17.000 per maand voor één maker. Netto houdt hij daar ±65% (Superhive gratis plan) tot ±84% (Gumroad eigen link) van over; welk plan hij heeft is niet bekend.
- Dovetail Key (Superhive alleen): **800+** in 5 maanden, $18 (GEZIEN, [Superhive](https://superhivemarket.com/products/dovetail-key)). Cleave 300+ in 2 maanden, Split 3D Print "Sales 400+" en "Downloads 400+" in 4 maanden (GOK: de verkopen tellen de gratis variant mee; de pagina zegt het niet).
- Vraag naar uitleg is enorm: YouTube "How to Cut a Model in Blender" 564.132, "How to Split Models in Blender | Bisect Tool" 483.117, "Blender. How to cut and key a model for 3d printing" 258.635, Meshmixer "Separate Large STL Files ... Locator Pins" 118.890, en MeshyAI "How to Split Any 3D Model into Printable Parts in One Click" **3.154.840** in 4 maanden (bedrijfskanaal van Meshy, GOK: deels betaald gepromoot, dus zwak als bewijs; de drie onafhankelijke uitlegvideo's zijn het echte bewijs) (alle GEZIEN, [YouTube-zoeken](https://www.youtube.com/results?search_query=split+model+for+3d+printing+blender) en [tweede zoekopdracht](https://www.youtube.com/results?search_query=blender+addon+split+stl+connectors)).

Twee scenario's, GOK. **Laag: 5 tot 15 verkopen per maand**, zoals bijna alle nieuwkomers in tabel 2c (SPLIT IT 20+ in 1 maand, SnapSplit 30+ in 8 maanden, de rest zonder teller). **Hoog: 30 tot 60 per maand**, alleen met dagelijkse Shorts en ±wekelijkse updates zoals CatPin en Cleave. Netto per verkoop van $24: Superhive ±65% (±$15,60), Gumroad eigen link ±84% (±$20), Gumroad Discover 70% ($16,80); bronnen `commercie/blender-click-joints/prijs.md` en verhaal 16 in `platformen/succes/verhalen.md`. Dus laag ±$80 tot $300 netto per maand, hoog ±$500 tot $1.200.

## 2. Vergelijkingstabel

### 2a. De grote drie plus Dovetail Key

| | **CatPin** (Alex Sokol) | **Cleave** (V4SS3UR) | **Split 3D Print** (AUER) | **Dovetail Key** (Milad Kambari, 3DRedBox) |
|---|---|---|---|---|
| Verkopen | Superhive 400+, Gumroad 2.042 (GEZIEN) | Superhive 300+ (was 200+ op 21 nov), Gumroad teller verborgen | Superhive 400+ (met gratis), Gumroad verborgen | Superhive 800+ |
| Beoordelingen | Gumroad 85, 4,8; Superhive 4, 5,0 | Gumroad 5, 5,0; Superhive 3, 5,0 | Gumroad 23, 4,9 (veel gratis); Superhive 3 | Superhive 13, gemiddeld 4 (62% 5, 24% 4, 16% 3) |
| Prijs nu | Superhive $24 (was $30), Supporter $36, Studio 5 pl. $80, coupon 30%; Gumroad $21 (was $30), "CatPin + Thanks" $31,50, "ProMax" $70 (DERDEN, keuring 23 nov) | $23, Support $28; Gumroad €20 | $22 (was $28), gratis $0, Support $28, 5 pl. $59; Gumroad vol $28 | $18 |
| Op de markt sinds | Gumroad 20 jul 2026 | Gumroad 13 sep; 1.0 op 23 sep volgens de [versiepagina](https://superhivemarket.com/products/cleave/versions) (de eigen winkeltekst zegt 17 sep) | Gumroad 21 jul | ±juni ("5 months ago") |
| Updates | ±maandelijks (1.0.7, 1.0.8, 1.0.9 op 15 nov) | 11 versies op Superhive in 2 maanden (Cleave zegt zelf "12 free updates since launch"), ±wekelijks | V3 26 aug, V4 11 nov plus 2 fixes | 5 grote versies in 5 maanden |
| Snijden | recht, gebogen, vrije polylijn, uitsnijden (ogen, ramen), twee sneden samen | auto onderdelen met schuif, randen kwasten, naad van lus, groef, punten | auto onderdelen (download 865 MB), recht, vrij, 360° lus, langs randlus | lijn, vrij, pen op het oppervlak (V5) |
| Snede bewerken vóór snijden | ja (Draft) | ja (curve) | ja (Expert) | ja sinds V5 |
| Verbinders | cilinder of trapezium, losse deuvel, eigen vaste vorm | pen in 4 profielen (recht, rond, D, zwaluwstaart), deuvel, staafkanaal, magneten 5x2 tot 10x3, kogelgewricht | taps pen, pen met nok, magneten, tap en gat (Socket), tot 6 per snede, losse verbinder zonder snede | zwaluwstaart, kogelsleutel, verzonken naad |
| Past maar op één manier | trapezium (half) | ja (D-profiel) | ja (Keyed Peg) | zwaluwstaart |
| Speling | Connector Clearance, Cut Gap, in mm | in mm, snijvlakspleet (1.7) | in mm, standaard 0,5 | clearance, socket gap |
| Past-op-bed | nee ("user remains responsible ... printer volume") | ja, 120+ printers, platen inpakken, 3MF per plaat | ja, 18 printers, rood kader | nee |
| Mesh repareren | nee, open meshes niet ondersteund | Make Manifold | Mesh Check en Fix Mesh | nee (wel terugval tussen boolean-solvers) |
| Labels op delen | nee | alleen bestandsnamen bij export (DERDEN, keuring 23 nov) | nee | nee |
| Wandcheck | nee | deel van verbinder dat buiten steekt rood (1.7) | nee | nee |
| Passingproef | nee ("A small test print is recommended", [FAQ](https://superhivemarket.com/products/catpin/faq)) | nee (wel Reassemble in Blender) | nee | nee |
| Beweegbare gewrichten | nee ("Articulated, rotating and movable joints are not currently supported") | kogelgewricht sinds 1.6 | nee | nee |
| Export | STL, OBJ, FBX | STL per deel of 3MF per plaat, plat gelegd | STL of 3MF per deel | STL |
| Bron | [SH](https://superhivemarket.com/products/catpin), [Gumroad json](https://alexsokol.gumroad.com/l/catpin.json) | [SH](https://superhivemarket.com/products/cleave), [versies](https://superhivemarket.com/products/cleave/versions), [Gumroad](https://v4ss3ur.gumroad.com/l/cleave) | [SH](https://superhivemarket.com/products/split-3dprint), [Gumroad](https://auerblender.gumroad.com/l/kxxyq) | [SH](https://superhivemarket.com/products/dovetail-key) |

Alles in tabel 2a GEZIEN op die pagina's, 23 nov.

### 2b. Hoe ze zich verkopen
| | Titel en eerste zin | Hoofdbeeld (Superhive) | Video's en Shorts (GEZIEN) |
|---|---|---|---|
| CatPin | "CatPin Blender add-on"; "Split your 3D model with full control over every cut and connector." Gumroad: "Cut. Connect. Print." | Grijs-bruine anime-meisjesbuste uit elkaar, losse armen met pennen zichtbaar; grote knoppen "NOVEMBER UPDATE", "NEW VERSION 1.0.9", "-20% OFF NOW", katlogo | Tutorial 23.990, eerste video ±21K. Shorts ±1 tot 3 per dag, 1.000 tot 2.400 weergaven, steeds dezelfde haak: "The fastest way to split your models...", "AI generated model? Split it fast", zelfde short twee keer geplaatst ([RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCNNM4IUdHp-r_qzH53NvcAQ)) |
| Cleave | Titel vol zoekwoorden "Smart Model Split & Cut for 3D Printing With Connectors (Pegs, Dowel, Rod Channel, Magnets, Ball Joints)"; "Too big to print? Split it." | Engelfiguur met vleugels in 5 felle kleuren uit elkaar, op een snijmat met **echte geprinte grijze delen**; drie punten: auto part detection, editable cuts, locking connectors | Demo 3.884, tutorial 01 2.036. Shorts 4 per dag om 08, 12, 17, 21 UTC, ±1.000 per stuk; haken: "Never Cut Through the Ears Again", "Small Printer? Cut a 250 mm Mecha to Fit It", "Beat the Print Bed Boss", "3 Mistakes When You Split a Model" 1.238 ([RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCykM4q_Aq8r4i1gE9kThNdA)) |
| Split 3D Print | "Split 3D Print"; blok "NEW UPDATE · V4" met 10 functies, elk met "Where to find it" | Grijs anime-figuur links, pijl, rechts hetzelfde figuur in 10 kleuren uit elkaar; rode sticker "NEW UPDATE" | Eén video ±1.288 (verhaal 8); bereik vooral uit Superhive en Gumroad-zoeken (staat 2e op "split 3d print") |
| Dovetail Key | "Dovetail Key"; belofte: een lijn trekken geeft delen met een zelfsluitende zwaluwstaart, in "Two clicks, no manual booleans" | Gespierde grijze torso met losse armen en hoofd, zwaluwstaarten zichtbaar; groene "V5"-badge | 3DRedBox "Dovetail Key, Cut & Join Any Mesh" 30.221, "Split Models for 3D Printing the Easy Way" 5.048 |

Wat trekt (GOK uit wat de winnaars delen): een bekend figuur uit elkaar met zichtbare pennen, felle kleur per deel, en een getal (versie, aantal delen, mm). Alleen Cleave toont echte prints; niemand toont een geprint, in elkaar gezet beeld naast de printer. Dat is ons beeld.

### 2c. De rest van de markt
| Speler | Wat | Prijs | Verkopen of bereik | Bron |
|---|---|---|---|---|
| SPLIT IT | sneden tekenen, pen en gat | $12 (nu $8,40) | 20+, 1 maand | [SH](https://superhivemarket.com/products/split-it) |
| Bed Fit Splitter | geef je bedmaat, hij plant zelf de sneden (vlakke vlakken), deuvelgaten, printplan | $19 | geen teller, 1 maand | [SH](https://superhivemarket.com/products/bed-fit-splitter) |
| Print Ready Modelling Kit | getekende snede, sleutels die "only fit one way" (zwaluwstaart, kogel, rond) | $24 | geen teller, 3 maanden | [SH](https://superhivemarket.com/products/print-ready-modelling-kit-cut-models-into-printable-parts-with-snap-fit-keys) |
| Split & Pin Pro | 9 penvormen tegen draaien (hex, D, kruis) | $20 | geen teller, 2 maanden | [SH](https://superhivemarket.com/products/splitpinpro) |
| North Slice | lijn tekenen, pen, deuvel, magneet, op bed leggen | $29,99 (ook $19,99 en $79,99) | 4 dagen oud | [SH](https://superhivemarket.com/products/north-slice) |
| Smart Segment (Kambari) | alleen auto onderdelen voor AI-modellen | $12 | 300+ | [SH](https://superhivemarket.com/products/smart-segmention-) |
| CutLink Studio, FigureCut, Ninja Cut, PrintSplit Easy, Easy Slice, Mesh Split, Key Cleaver, PrintSplitter, One Click Splitting | kleinere snijders | $1 tot $19,99 | 0 tot 40+ | Superhive-zoeken "3d print connectors", "cut 3d printing", "dovetail" |
| SnapSplit | eigen verbinders | $20 (Gumroad $14) | 30+ in 8 maanden | [SH](https://superhivemarket.com/products/snapsplit) |
| CutFlex, JointLab | gewrichten, ook snijden | $34,99, $65 | 10+, 20+ | [CutFlex](https://superhivemarket.com/products/cut-flex), [JointLab](https://superhivemarket.com/products/jointlab-) |
| Gratis op extensions.blender.org | Easy-Print (7.855 downloads), EasySlice Print (7.136, 21 reviews), SnapSplit | $0 | zie downloads | [Easy-Print](https://extensions.blender.org/add-ons/easy-print/), [EasySlice](https://extensions.blender.org/add-ons/easy-slice-print/) |
| CutMode (gratis, xideaa) | snijden met klikverbinders | $0 | video 11.652 | YouTube-zoeken hierboven |
| Bambu Studio, OrcaSlicer | vlak snijden of zwaluwstaart; verbinders Plug, Dowel, Snap | gratis | iedereen met een Bambu | [Bambu-wiki](https://wiki.bambulab.com/en/software/bambu-studio/cut-tool) |
| PrusaSlicer | zelfde: vlak of zwaluwstaart, Plug, Dowel, Snap, vorm en diepte | gratis | | [Prusa-help](https://help.prusa3d.com/article/cut-tool_1779) |
| Lychee (resin) | "Planar Cut" en "Split" van schillen | gratis basis | | [Lychee-functies](https://account.mango3d.io/lychee-slicer-features) |
| Meshy Auto Split | AI splitst in delen, verbinders kubus of cilinder | betaald abonnement, 10 credits | video 3,15 mln; **alleen modellen die in Meshy zijn gemaakt**, geüploade niet | [Meshy-docs](https://docs.meshy.ai/en/webapp/guides/3d-model/auto-split) |
| PrintForge | sneden of een raster op je bedmaat, ronde pen, pen met nok, losse pennen, magneetgaten; wandcheck als steekproef (rood) voor het hele model; genummerde delen, uitgeklapt beeld, bouwgids als HTML en SVG; "Create Fit Test Coupon" (twee proefdelen); geen gravure ("Version 1.0 does not include ... engraved labels") | $8,99 | geen teller, ±2 maanden | [SH](https://superhivemarket.com/products/print-forge), [docs](https://superhivemarket.com/products/print-forge/docs) |
| Fit & Tolerance Test Generator | los proefplaatje met gaten en pennen op 2 tot 12 spelingen, speling gegraveerd naast elk gat; geen splitser | $7 (nu $5,25) | geen teller, 29 dagen | [SH](https://superhivemarket.com/products/fit-tolerance-test-generator) |
| Split3MF "Fit to printer" | web: splitst vanzelf op je bouwvolume, "Every cut face is numbered", losse verbinders | gratis proberen, downloaden vraagt Pro | | [split3mf.com](https://split3mf.com/fit-to-printer) |
| Webtools en apps | Split3MF (kleuren splitsen gratis web), SideSplitter (gratis beta, 6 verbinders die zonder steun printen), obloid STL cutter (3 gratis exports, dan abonnement), CadSplit (Mac-app), printpal | gratis tot abonnement | Reddit-posts 0 tot 1.423 punten | [SideSplitter](https://reddit.com/r/BambuLab/comments/1vxlw73/), [obloid](https://reddit.com/r/BambuLab/comments/1whrzea/), [CadSplit](https://reddit.com/r/BambuLab/comments/1xxmw4h/), [Split3MF](https://reddit.com/r/BambuLab/comments/1xsdh9i/) |
| Meshmixer | vlak snijden plus pennen (oud, GOK: niet meer ontwikkeld) | gratis | video 118.890 | YouTube-zoeken |

Alle cijfers in 2c GEZIEN tenzij GOK erbij staat.

## 3. Wat kopers missen of klagen (het goud)

| # | Klacht of wens | Waar (GEZIEN) | Wie lost het al op | Kans voor ons |
|---|---|---|---|---|
| 1 | Speling gokken, pas na het printen merken dat het niet past | maker obloid: "guess clearances, or just cut and glue and hope it holds" ([Reddit](https://reddit.com/r/BambuLab/comments/1v1efkw/)); Cleave gebruikt het als reclame ("six hour print", winkeltekst, geen klacht van een koper). Geen letterlijke kopersklacht gevonden: vraag is GOK | grote vier niet; losse proeftools PrintForge en Fit & Tolerance Test Generator (2c); obloid presets per materiaal | **Proef met je eigen verbinder, onthouden per printer** |
| 2 | Fouten, crashes, knoppen die haperen | Cleave-review "minor bugs that made my blender crash"; Dovetail Key 3 sterren "suffers the pitfalls of many vibe coded tools ... preview glitching" ([SH p2](https://superhivemarket.com/products/dovetail-key/ratings?page=2)); CatPin-reviews "can't get the manual cut to work; it always throws an error", "i have an error" ([Gumroad reviews](https://gumroad.com/product_reviews?product_id=WalKAmuY-liJb6dY4KvSkQ%3D%3D)); Split-review: snede "gouged a small surface chunk" op een zwaar model ([SH](https://superhivemarket.com/products/split-3dprint/ratings)) | deels (Fix Mesh, Make Manifold) | **Betrouwbaarheid als belofte, met e2e in echte Blender** |
| 3 | Uitleg ontbreekt, paneel niet te vinden | CatPin 4 sterren: "would benefit from proper documentation", "YouTube instruction video is too fast", Spaans: "tutorial ... para que sirve cada una de las opciones" (3 van 6 vier-sterren); Split Gumroad 3 sterren "would like to see a video explaining how to use"; Split SH "small menu icon ... after hitting the N key (thanks Google!)"; Cleave: "many menu's ... hard to oversee" | Split zet "Where to find it" bij elke functie | **3 stappen, uitleg in het paneel, eerste snede in 60 s** |
| 4 | Pen draait of zit verkeerd om | CatPin: "a cylindrical one with a flat side, so it doesn't misalign"; Split & Pin Pro verkoopt op "loose joints that spin" | Cleave D, Split Keyed Peg | **Standaard aan** (lat) |
| 5 | Losse deuvel om plat te kunnen printen | CatPin-review op SH: "2 holes and a pin I can print separately ... laying flat on FDM printer" | CatPin (maker beloofde het voor 9 sep), Cleave | must have |
| 6 | Pen gedrukt liggend is zwak, delen liggen niet plat | SideSplitter: een liggend geprinte pen is "weak, out-of-round, and needs support", en een snijvlak ligt niet altijd plat ([Reddit](https://reddit.com/r/BambuLab/comments/1vxlw73/)); Bambu-tip "Some connectors stop a cut piece from lying flat" (51 punten, [Reddit](https://reddit.com/r/BambuLab/comments/1xw9yl6/)) | Cleave legt delen plat | **Pen-kant kiezen op printrichting** |
| 7 | Meerdere sneden met verbinders die elkaar raken | CadSplit: drie sneden met verbinders die niet botsen "took me longer than the print" ([Reddit](https://reddit.com/r/BambuLab/comments/1xxmw4h/)); Prusa-help: kan geen lijst van 4 delen bijhouden, "align or place more precisely the connectors" ([Prusa](https://help.prusa3d.com/article/cut-tool_1779)) | Blender-add-ons deels | **Botscheck tussen verbinders** (hebben we al in Click Joints) |
| 8 | Alleen een stukje uitsnijden (ogen, knoppen), niet een oneindig vlak | EasySlice-review "cut parts such as eyes, buttons etc. without split the entire model"; Easy-Print "the cut line generate an infinite plane" ([reviews](https://extensions.blender.org/add-ons/easy-print/reviews/)) | CatPin, Split, Cleave | later |
| 9 | Lijnen recht en onder hoek tekenen | CatPin: "axis and angle constraints for drawing lines" | Cleave Shift+klik recht | klein, v1 |
| 10 | Snede langs een randlus, lijn doortrekken na draaien | Dovetail Key-reviews: "select a loop and cut based on that", camera draaien en lijn houden | Cleave, Split, Dovetail V5 | later |
| 11 | Beweegbare gewrichten | CatPin zegt nee; Dovetail Key-review vraagt kogel en scharnier per lichaamsdeel "think ... Hasbro" | Cleave kogel, Click Joints | **Bundel met Click Joints Pro** |
| 12 | Delen kwijt bij in elkaar zetten | niemand klaagt letterlijk (niet gevonden); wel kits van 13 tot 20 delen in Shorts van Cleave | Split3MF graveert (web, Pro), PrintForge nummert zonder gravure; geen Blender-add-on graveert | **Gegraveerde nummers in Blender** (GOK dat kopers het willen; verschil dat je ziet in een Short) |
| 13 | Kortingscode werkt niet | enige 1 ster van CatPin: "I don't apply the discount!!!" | | coupons testen vóór plaatsen |

Ook gezien: kopers zijn vaak nieuw in Blender ("I almost gave up on Blender until this Add-On", Russisch: Blender eergisteren voor het eerst gezien) en één op vijf schrijft niet in het Engels (verhaal 16). Wie goed helpt krijgt sterren: CatPin antwoordt op bijna elke review en vraagt "contact support before leaving a review".

Niet gelukt: YouTube-reacties (watch-pagina geeft een captcha, de interne API mocht niet), commentaar zoeken op Reddit (Arctic Shift gaf steeds "Timeout"), BlenderArtists niet opnieuw gezocht (eerdere runs vonden niets van CatPin of Cleave).

## 4. Waarom iemand niet de gratis slicer gebruikt
1. **Slicer snijdt alleen een plat vlak door het hele model** (Bambu: "Planar" of "Dovetail"; Prusa idem, GEZIEN). Bij een figuur gaat dat dwars door gezicht en handen. Add-ons snijden langs kraag, mouw, riem.
2. **Meerdere sneden zijn gepruts** in de slicer (Prusa-reactie over 4 delen bijhouden, CadSplit-citaat).
3. **Het model blijft in Blender** en is aan te passen; de slicer kan het deel met verbinder niet terug exporteren om verder te bewerken ([Reddit](https://reddit.com/r/BambuLab/comments/1xpgsvh/)).
4. **Wie STL's verkoopt** moet de delen al gesneden leveren; zijn koper heeft misschien geen Bambu (GOK; CatPin richt zich op "STL model creators", "3D-printing studios", "client request").
5. **AI-modellen** zijn één samengesmolten schil; Meshy splitst alleen eigen modellen en verwijst voor exacte sneden of eigen verbinders zelf naar "a tool such as Blender" (GEZIEN, hun eigen bewering, [Meshy](https://docs.meshy.ai/en/webapp/guides/3d-model/auto-split)).
6. Passing zien vóór het printen (opengewerkt beeld, wandcheck): slicer laat alleen de laag zien.

## 5. Prijs en varianten (voorstel)
- **Standaard $24**, startprijs **$19 tot 14 dec** (zoals LayerMechanic: $25, $19 de eerste 14 dagen, volgens het afkijkrapport van 21 nov). Reden: de verkopers met de meeste verkopen zitten op $18 tot $24 (Dovetail Key $18, Split $22, Cleave $23, CatPin $24 en $21 op Gumroad, GEZIEN). Lager levert niet meer kopers op (zelfde redenering als voor Click Joints Pro in `platformen/ideeen/afkijken-2-2026-11-21/A-blender-kopers.md`).
- **Supporter $34**, zelfde download (Cleave $28, CatPin $36, Split $28: elke snelle maker heeft het).
- **Studio 5 plekken $79** (CatPin $80, Split $59).
- **Bundel met Click Joints Pro $35** (los $24 + $19 = $43): snijden plus beweegbare gewrichten, wat CatPin uitdrukkelijk niet kan.
- **Gratis variant: eerst niet.** De eerste twee weken alleen betaald ($19), dan meten; daarna eventueel een $0-variant (één rechte snede, ronde pen, STL) en verkopen per dag vergelijken. Reden: met een $0-variant toont Gumroad de pagina als "$0" ([Split json](https://auerblender.gumroad.com/l/kxxyq.json)), gratis downloads tellen niet mee voor de $100 die Discover vraagt, en zo'n lite doet hetzelfde als de gratis slicers en Easy-Print. Voordeel later: beoordelingen en een maillijst (Split staat 2e op Gumroad-zoeken met 23 beoordelingen; of dat door de gratis variant komt is GOK). Vrijwillig betalen werkt niet (MACHIN3: <1%).
- Shorts linken naar Gumroad (beoordelingen: CatPin 85 daar tegen 4 op Superhive).

Geld, GOK: laag 5 tot 15 verkopen per maand (±$80 tot $300 netto), hoog 30 tot 60 na een maand dagelijkse Shorts (±$500 tot $1.200 netto, zie sectie 1); met de bundel meer per koper.

## 6. Eerste versie: must have en later

**Must have (zonder dit kiest niemand ons boven CatPin of Cleave):**
1. Snijden: recht vlak met hoekstappen, en een getekende lijn op het oppervlak; snede te zien en te verschuiven vóór snijden; alleen het stuk onder de lijn, geen oneindig vlak; origineel blijft bewaard, snede ongedaan te maken.
2. Verbinders: taps ronde pen, pen die maar op één manier past (standaard aan), losse deuvel (export schrijft de pennen mee), magneetgaten 5x2 tot 10x3 mm; meer dan één per snede; maat vanzelf passend bij het snijvlak; kant omdraaien.
3. Speling in echte mm, ook in een scene in meters (hebben we al).
4. **Passingproef met de eigen verbinder** (één knop, 4 spelingen, onthouden per printer en materiaal).
5. **Wandcheck per verbinder** groen, oranje, rood met de reden in mm, en botscheck tussen verbinders (uit Click Joints).
6. Printerkeuze (de 20 meest verkochte plus eigen maat), elk deel groen of rood.
7. Mesh controleren en dichtmaken; werkt op zware sculpts en AI-modellen; e2e in echte Blender met 10 lastige modellen.
8. **Nummers gegraveerd in de snijvlakken** (A1 bij A2), aan of uit. Klein te bouwen, geen voorsprong op zichzelf.
9. Export: STL per deel en 3MF, in mm, elk deel plat op het snijvlak, pen-kant zo gekozen dat het deel plat ligt.
10. Paneel: 3 genummerde stappen, "Where to find it" in de winkeltekst, een korte tutorial van 4 minuten.

**Later (week 3 en verder, op volgorde):** automatisch sneden plannen voor je bedmaat (vlakken die gezicht en handen ontwijken); platen inpakken en 3MF per plaat; automatisch onderdelen vinden (Cleave en Split hebben dit, CatPin niet en verkoopt toch het meest); snede langs randlus; zwaluwstaart en tap-en-gat; staafkanaal voor grote cosplay; een detail uitsnijden als plug; kogel en scharnier via de bundel; bouwplaatje als PDF of PNG (PrintForge heeft dit al, dus geen voorsprong).

## 7. Bronnenlijst (alle GEZIEN 23 nov 2026)
- Superhive: [CatPin](https://superhivemarket.com/products/catpin) ([ratings](https://superhivemarket.com/products/catpin/ratings)), [Cleave](https://superhivemarket.com/products/cleave) ([ratings](https://superhivemarket.com/products/cleave/ratings), [versies](https://superhivemarket.com/products/cleave/versions)), [Split 3D Print](https://superhivemarket.com/products/split-3dprint) ([ratings](https://superhivemarket.com/products/split-3dprint/ratings)), [Dovetail Key](https://superhivemarket.com/products/dovetail-key) ([ratings p2](https://superhivemarket.com/products/dovetail-key/ratings?page=2)).
- Gumroad: [CatPin json](https://alexsokol.gumroad.com/l/catpin.json), [Cleave json](https://v4ss3ur.gumroad.com/l/cleave.json), [Split json](https://auerblender.gumroad.com/l/kxxyq.json), reviews via `gumroad.com/product_reviews?product_id=...` (CatPin 51 met tekst, Split 10, Cleave 3), zoek-API `gumroad.com/products/search?query=split%203d%20print`.
- YouTube: RSS CatPin en Cleave (links in 2b), zoekpagina's (links in 1).
- Reddit via Arctic Shift: r/BambuLab 1xxmw4h, 1xpgsvh, 1vxlw73, 1v1efkw, 1whrzea, 1xw9yl6, 1xsdh9i; r/blender 1x5jq7s (CatPin-gebruiker krijgt een schoen niet los).
- Slicers: [Bambu-wiki](https://wiki.bambulab.com/en/software/bambu-studio/cut-tool), [Prusa-help](https://help.prusa3d.com/article/cut-tool_1779), [Lychee](https://account.mango3d.io/lychee-slicer-features), [Meshy](https://docs.meshy.ai/en/webapp/guides/3d-model/auto-split).
- Blender Extensions: [Easy-Print reviews](https://extensions.blender.org/add-ons/easy-print/reviews/), [EasySlice Print reviews](https://extensions.blender.org/add-ons/easy-slice-print/reviews/) (daar ook de openlijke beschuldigingen van de CatPin-maker).

Keuring: akkoord nee op 23 nov (`producten/blender-splitser/keuring/2026-11-23-concurrentie.md`). Keuring: moet-punten verwerkt 23 nov 2026, wacht op herkeuring.
