# Digital Production: nieuws-tip Click Joints, vóór de sale (Verspreider, run 5, 24 nov 2026)

**Kort:** een korte mail aan de redactie van Digital Production (digitalproduction.com) met een nieuws-tip over de gratis Click Joints en Click Joints Pro. Haak: hun artikel over CatPin (9 okt) zegt letterlijk dat CatPin geen beweegbare gewrichten doet; dat is precies wat wij doen. Versturen op **wo 25 nov** (di 24 nov is al 80.lv, max één ding per dag voor Thijs), zodat een eventueel bericht in de saleweek valt. Kost 0 euro. Gaat van thijs@dortus.com onder de naam van Thijs, dus **alleen na zijn ja op de tekst** (CLAUDE.md regel 4).

## Waarom deze plek (meeste kopers per minuut werk)
- Digital Production schrijft ±2 keer per week over een Blender-add-on, ook kleine makers op Superhive: Alpaca3D (5 okt), CatPin (9 okt), Nitro Retopo (13 okt), NKZ Retopia (20 okt), Animatica Marionette (21 okt), Poster Print en Poster Pin (28 okt), Omniscient (6 nov), Metawrap (10 nov), Dolly Zoom (13 nov), CL Sculpt Assistant (16 nov) (GEZIEN 24 nov ±00:00 UTC, curl https://digitalproduction.com/?s=blender+add-on). Elke week dus een plek voor een add-on als de onze.
- Hun CatPin-artikel (Bela Beier, 9 okt 2026) gaat over het in delen snijden van sculpts voor 3D-print, met pin en socket, en zegt: "The documentation excludes articulated, rotating and movable joints. A keyed assembly and an action figure's elbow are different engineering conversations." En over speling: "Treat tolerance as a physical parameter" (GEZIEN, curl https://digitalproduction.com/2026/10/09/catpin-blender-cuts-3d-printing/). Onze add-on doet beweegbare gewrichten met een eindstop en een paskleur, en Pro 1.2 heeft een teststrip voor de speling. Een betere haak krijgen we niet: de redacteur stelde zelf de vraag die wij beantwoorden.
- Ze schrijven uit de documentatie, FAQ en tutorial van de maker (het CatPin-stuk citeert FAQ en tutorial). Daarom geven we in de mail de videolinks en de pagina met alle uitleg mee.
- Contact: info@digitalproduction.com, het enige adres op hun contactpagina (GEZIEN, curl https://digitalproduction.com/contact/). Geen apart tip-formulier gevonden.
- Bereik: niet bekend; geen eigen cijfer gevonden (geen GOK op bezoekers). Vergelijking: BlenderNation zette ons gratis op 18 nov, die dag +43 downloads tegen 11 tot 28 op gewone dagen (GEZIEN, LOG.md run 1). Kans dat ze het oppakken: GOK 1 op 4, hoger dan 80.lv omdat de haak uit hun eigen stuk komt en ze juist zulke kleine add-ons brengen. Verwacht als ze het brengen: 0 tot 5 verkopen Pro en 20 tot 50 downloads gratis (GOK). Werk voor Thijs: ±3 minuten (GOK).

## Regels nagelezen
- Digital Production heeft betaalde "Sponsored & Partners"-pagina's en een Media Kit (GEZIEN, menu op de site). Wij vragen niets betaalds; alleen een tip. Komt er een aanbod voor een betaalde post terug: niet op ingaan zonder ja van Thijs (geld). Geen tweede mail als ze niet reageren.
- Onze eigen regels: geen printbelofte (besluit 17 nov 13:40): "not print tested by us yet". Geen AI-zin (besluit 16 nov 20:09). De grens "works best on figures about 200 mm tall or more with separate arms and legs, Blender 4.5 or newer" staat erin (moet-punt van de keuring van 80.lv). Elke bijlage krijgt een Engelse naam en één regel uitleg, en de mail zegt welk beeld bij welke versie hoort (kan-punten C4 en A11 van die keuring).
- Wat Pro doet komt uit de gekeurde tekst 5 en 7 van `commercie/blender-click-joints/plekken-boost-2026-11-20.md` en de Gumroad-pagina (GEZIEN 24 nov, "Works best on figures with separate arms and legs, at about 200 mm tall or more"). De Fit test strip komt uit de releasenotes van 1.2 (`platformen/blender/pro-1.2.0.md`, Daan ja); 1.2.2 staat sinds 23 nov 20:45 NL op Gumroad en Superhive (`commercie/geplaatst.md`). De gratis versie: de beschrijving op extensions.blender.org (GEZIEN 24 nov, curl: "a ball and socket or a pin, sized with the clearance your printer needs", bend range in 8 richtingen, ring groen/geel/rood, STL of 3MF per deel).
- Let op: de Gumroad-beschrijving zegt nog "1.1 is a free update" en noemt de Fit test strip nog niet (GEZIEN 24 nov; staat op lijst Thijs punt 3). De mail noemt Fit test toch, want die zit in de zip die een koper nu krijgt. Is punt 3 op 25 nov nog niet gedaan, dan klopt de mail nog steeds, maar ziet de redacteur het niet op Gumroad terug; de link gaat daarom naar dortus.com/click-joints/.

## De mail (Engels, letterlijk plakken)
**Aan:** info@digitalproduction.com
**Van:** thijs@dortus.com
**Onderwerp:**
```
News tip: articulated joints for 3D printable figures in Blender (the elbow from your CatPin piece)
```
**Tekst:**
```
Hi Digital Production team,

A news tip for your Blender coverage. Your CatPin article (October 9) noted that its documentation excludes articulated, rotating and movable joints, and that an action figure's elbow is a different engineering conversation. That conversation is what our add-on is about.

Click Joints (free, GPL, on Blender Extensions) cuts a model into two parts with a ball and socket or a pin, sized with the clearance you set in millimetres. For a ball joint it measures how far it bends before the parts collide, in degrees, before you print, and a ring on the cut shows the fit: green is good, yellow is tight, red is too thin. Export to STL or 3MF, one file per part.
https://extensions.blender.org/add-ons/click-joints/

Click Joints Pro does the same for a whole rigged figure. Pick the figure and press one button: elbows and knees get a hinge with an end stop, shoulders, hips and neck get a ball joint. If a bone has a Limit Rotation constraint, the hinge stops at that angle, and red shows where parts would hit past the stop. It reads Rigify, Mixamo, Auto-Rig Pro, Unreal, Character Creator, VRoid, 3ds Max Biped and Daz bone names. It works best on figures about 200 mm tall or more with separate arms and legs, in Blender 4.5 or newer.

To be clear: it is not print tested by us yet, so we tell users to print a test joint first.

Pro is $19 on Gumroad (25% off from November 27 to December 1) and $12 on Superhive. Overview and links:
https://dortus.com/click-joints/?van=digitalproduction

Videos:
Full walkthrough, rig to printable figure: https://www.youtube.com/watch?v=4-3l3MZZWPc
One click, rig to 10 printable parts: https://www.youtube.com/watch?v=I78weVdhwdw

Attached:
- click-joints-pro-hinge-bend.gif: a Pro hinge bending through its range, 0 to 115 degrees.
- click-joints-pro-figure-from-rig.png: a rigged figure after one click in Pro, nine joints with their ranges.
- click-joints-free-ball-joints.jpg: a figure made with the free version, ball joints with the green fit band.

Happy to answer questions or send more images.

Thijs
Dortus
```

**Bijlagen (3), met de naam die ze in de mail krijgen:**
| Naam in de mail | Bestand in de repo | Wat het is |
|---|---|---|
| click-joints-pro-hinge-bend.gif | `commercie/verspreiden/beeld/pro-buig-400.gif` | 400 x 711, 1,7 MB, Pro-scharnier buigt tot 115° (gekeurd bij 80.lv) |
| click-joints-pro-figure-from-rig.png | `commercie/blender-click-joints/gumroad-1.1/1-figuur-uit-rig.png` | 1920 x 1080, figuur met 9 gewrichten en hun bereik (gekeurd bij 80.lv) |
| click-joints-free-ball-joints.jpg | `commercie/blender-click-joints/blendernation-1456x672.jpg` | gratis versie, houten pop met groene pasbanden |

Links nagekeken (GEZIEN 24 nov ±00:00 UTC, curl): dortus.com/click-joints/?van=digitalproduction geeft 200 en noemt "$19" en "25% off from November 27 to December 1"; superhivemarket.com/products/click-joints-pro geeft 200 en $12 en $45; beide YouTube-video's bestaan (oEmbed 200); extensions.blender.org/add-ons/click-joints/ geeft de listing (356 downloads).

## Wie, wat, wanneer
| Stap | Wie | Wanneer | Account |
|---|---|---|---|
| Tekst keuren | aparte keurder | nu | geen |
| Ja op de tekst | Thijs | wo 25 nov | geen |
| Check: staat CYBER25 (25%, automatisch toepassen) klaar op Gumroad? Zo niet, "(25% off from November 27 to December 1)" weglaten | hoofdchat | vlak voor versturen | Gumroad |
| Versturen met de drie bijlagen, hernoemd zoals hierboven | Thijs (of de hoofdchat zet het klaar als Gmail-concept, nooit zelf versturen) | wo 25 nov | thijs@dortus.com |
| Regel in `commercie/geplaatst.md` | hoofdchat | na versturen | geen |
| Meten | Verspreider | 26 nov tot 9 dec | geen |

## Meten
- `curl -s -A "Mozilla/5.0" "https://digitalproduction.com/?s=click+joints"` elke run van 26 nov tot 9 dec.
- Bezoeken met `?van=digitalproduction` en verwijzer digitalproduction.com op dortus.com (Umami), downloads gratis versie per dag (scorebord), verkopen Gumroad en de verkoopklasse op Superhive.
- Geen bericht op 9 dec: plek valt af, geen tweede mail.

## Ook gezien deze run (geen actie nodig)
- **Addon Radar** heeft beide al: https://addonradar.com/addon/click-joints/ (gratis, 338 downloads, gecontroleerd 23 nov) en https://addonradar.com/addon/click-joints-pro/ ($12, sinds 20 nov gevolgd) (GEZIEN). Hun Black Friday-pagina toont elke add-on die op Superhive in de aanbieding staat, plus kortingscodes van makers op Superhive ("527 add-ons on sale right now", "249 coupon codes", GEZIEN https://addonradar.com/black-friday/). Pro komt daar vanzelf op zodra de Cyber Sale van Superhive start (vr 27 nov, Sitewide Sales staat aan, besluit 19 nov 13:45). Meten op 27 nov.
- **Concurrenten in dezelfde hoek** (allemaal op Superhive, DERDEN via zoekmachine): Jointlab (https://superhivemarket.com/products/jointlab-), Pose to Print (https://superhivemarket.com/products/pose-to-print), FigureCut, LayerMechanic, en de gratis 299 Tools (BlenderNation 10 sep, https://www.blendernation.com/2026/09/10/299-tools-free-blender-tools-for-figure-3d-printing/). Jointlab en Pose to Print lijken het dichtst bij Pro; een vergelijking van titel, prijs en verkoopklasse is een goede volgende stap voor de vindbaarheid op Superhive.
- **All3DP** schrijft lijstjes met gratis Blender-add-ons voor 3D-print ("5 free Blender add-ons to fix and 3D print your messy AI models", DERDEN https://all3dp.com/1/5-free-blender-add-ons-to-fix-3d-print-your-messy-ai-models/), maar de site geeft 403 met curl en er is geen tipadres gevonden. Later, met een echte print.

Keuring: zie onder.

## Verwerkt na de keuring (Verspreider, 24 nov)
- Moet 1: de zin over 1.2 en de Fit test strip is uit de mail, en de "To be clear"-zin is weer "print a test joint first"; de render van de strip is geen bijlage meer. Reden: geen openbare pagina noemt 1.2 nog (GEZIEN door de keurder). De alinea "Let op" hierboven geldt daarmee niet meer. Staat lijst Thijs punt 3 (Gumroad-tekst 1.2) vóór versturen live, dan mag de hoofdchat deze zin na "past the stop." terugzetten: "Version 1.2 adds a fit test strip: five joints from 0.10 to 0.30 mm clearance, so you know which gap fits your printer."
- Kan: onderwerp "the elbow from your CatPin piece" en "3D printable". Prijsregel laten we staan (beide winkels eerlijk genoemd); keuze voor de hoofdchat.

## Keuring (aparte keurder, 24 nov 2026)
# Keuring Digital Production-tip Click Joints, 24 nov 2026, aparte keurder (Claude, niet de Verspreider)
Wat ik keurde: dit bestand (mail, onderwerp, vier bijlagen en de onderbouwing), tegen de live pagina's (curl -A "Mozilla/5.0", 24 nov), tekst 5 en 7 van `commercie/blender-click-joints/plekken-boost-2026-11-20.md`, `platformen/blender/pro-1.2.0.md`, `commercie/geplaatst.md` en de keuring van `2026-11-23-80lv.md`.
Akkoord: ja mits (één moet-punt: 1.2 en de Fit test strip moeten op een openbare pagina staan vóór versturen, of uit de mail)

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| A1 | CatPin-artikel klopt: Bela Beier, 9 okt 2026, letterlijk "The documentation excludes articulated, rotating and movable joints. A keyed assembly and an action figure's elbow are different engineering conversations." en "Treat tolerance as a physical parameter". De parafrase in de mail ("noted that its documentation excludes ... and that an action figure's elbow is a different engineering conversation") is eerlijk. Het stuk citeert inderdaad FAQ en tutorial. | Feit | hoog | curl catpin-artikel |
| A2 | Contact: info@digitalproduction.com is het enige adres op /contact/ (4 keer, geen ander). | Feit | hoog | curl /contact/ |
| A3 | De tien artikelen in regel 6 bestaan precies met die data (5 okt tot 16 nov). Tien in zes weken is ±1,7 per week, dus "±2 keer per week" klopt ongeveer. | Feit | hoog | curl ?s=blender+add-on |
| A4 | Gratis versie klopt met extensions.blender.org: twee waterdichte delen, ball and socket of pin, speling in mm, bend gemeten in graden voor de botsing, ring groen/geel/rood, STL of 3MF per deel, GPL 3.0 of later, 356 downloads, Blender 4.2 en nieuwer. | Feit | hoog | curl listing |
| A5 | Pro klopt met Gumroad (JSON in de html) en Superhive: één knop, hinge met eindstop bij elleboog en knie, ball joint bij schouder, heup, nek; stop uit Limit Rotation; rood voorbij de stop; de acht rignamen letterlijk; "Works best on figures with separate arms and legs, at about 200 mm tall or more"; "Best in Blender 4.5 and newer". Prijs Gumroad 1900 cent USD, Superhive $12 Personal en $45 Studio. Het moet-punt A3 van de 80.lv-keuring (de grens) staat er nu in. | Feit | hoog | curl Gumroad en Superhive |
| A6 | **"Version 1.2 adds a fit test strip" staat op geen enkele openbare pagina.** Gumroad: geen "Fit test" of "test strip", nog "1.1 is a free update". dortus.com/click-joints/: ook geen "Fit test" of "1.2" (de hele tekst gelezen). Superhive: in de html staat alleen "1.1.0 (20 Nov 2026)" als versie, geen 1.2 (ondanks de regel in `geplaatst.md` dat 1.2.2 daar met releasenotes is ingezet; mogelijk nog in keuring bij Superhive). De bewering zelf is waar (releasenotes 1.2.0, zip 1.2.2 op Gumroad), maar regel 16 in dit plan ("de link gaat daarom naar dortus.com/click-joints/") klopt niet: ook daar ziet de redacteur het niet. DP schrijft uit de documentatie van de maker (A1); vindt de redacteur het nieuwste punt van de mail nergens terug, dan laat hij het weg of twijfelt hij aan de rest. | Feit (pagina's), gevolg vermoeden | hoog / midden | grep "Fit test", "1.2" op de drie pagina's vlak voor versturen |
| A7 | Fit test strip "five joints from 0.10 to 0.30 mm clearance, each with its number" komt letterlijk uit de releasenotes 1.2.0 (Daan ja). | Feit | hoog | `platformen/blender/pro-1.2.0.md` |
| A8 | YouTube: 4-3l3MZZWPc "Blender rig to 3D printable figure: one button, hinges and ball joints \| Click Joints Pro" en I78weVdhwdw "One click: rig to 10 printable parts in Blender", beide van @Dortusapps. Omschrijvingen in de mail passen. | Feit | hoog | oEmbed |
| A9 | dortus.com/click-joints/?van=digitalproduction geeft 200 en noemt "$19 once on Gumroad (25% off from November 27 to December 1)". | Feit | hoog | curl |
| A10 | Bijlage 1 (gif 400 x 711, 1,7 MB, frame op 8 s bekeken): ledemaat met scharnier, boog 0° tot 115°, titel "Bends 0° to 115°". Past bij "a Pro hinge bending through its range, 0 to 115 degrees". | Feit | hoog | Read-tool, ffmpeg-frame |
| A11 | Bijlage 2 (png 1920 x 1080, bekeken): figuur uit rig in Blender 5.3.0, 9 gewrichten (±20°, 140°, 120°), lijst "9 joints · 2 rig · 2 mirror · 5 preset". Past bij "nine joints with their ranges". | Feit | hoog | Read-tool |
| A12 | Bijlage 3 (png 1600 x 900, bekeken): vijf oranje paren bal en kom op een rij. Dat is de strip, maar **de nummers zijn in de render niet te zien**, terwijl de mail "each with its number" zegt. Geen fout in de mail (de zin gaat over de functie), wel een klein verschil tussen tekst en beeld. | Feit | hoog | Read-tool |
| A13 | Bijlage 4 (jpg 1456 x 672, bekeken): houten tekenpop op één been met groene ringen bij elleboog en knie, uit het gekeurde filmpje van de gratis versie (`lancering.md`). Correct als gratis versie benoemd; de kogels zelf zie je niet, alleen de groene ring. | Feit | hoog | Read-tool, `lancering.md` |
| A14 | Prijs: de mail zet "$19 on Gumroad (25% off ...)" naast "$12 on Superhive". Met korting is Gumroad $14,25, nog steeds duurder dan Superhive zonder korting. Een redacteur ziet twee prijzen voor hetzelfde zonder uitleg (updates: Gumroad "all Pro 1.x updates", Superhive "12 months"), en de korting oogt dan vreemd. Geen fout, wel verwarrend. | Feit (prijzen), gevolg vermoeden | hoog / midden | Gumroad- en Superhive-pagina |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| B1 | Geen printbelofte: "it is not print tested by us yet, which is why the fit test strip comes first". "Printable" staat ook in de gekeurde teksten. Het onderwerp zegt "for 3D printed figures": dat is de categorie en staat zo ook in de titel van de listing op extensions.blender.org ("ball joints for 3D printed figures"), geen bewering dat er geprint is. Bij 80.lv werd "a poseable 3D printed action figure" wel afgekeurd; hier is het zwakker, dus kan (zie Kan 3). | Feit | hoog | besluit 17 nov 13:40 |
| B2 | Geen AI-zin in de mail (grep op "AI" vindt alleen de regelverwijzing en de All3DP-titel in de onderbouwing). | Feit | hoog | besluit 16 nov 20:09 |
| B3 | Geen persoonsgegevens: alleen thijs@dortus.com en de voornaam. De Gumroad-link met gebruikersnaam staat niet in de mail. `organisatie/controle/check.py`: "Controle openbare repo: OK". | Feit | hoog | CLAUDE.md regel 2 |
| B4 | Gaat onder de naam van Thijs: plan zegt alleen na zijn ja, hoofdchat zet hooguit een concept klaar, nooit zelf versturen; geen ingaan op een betaald aanbod. Goed. | Feit | hoog | regel 1 en 4 |
| B5 | Cijfers gelabeld: downloads, artikelen, contact GEZIEN; kans 1 op 4, verkopen, downloads en ±3 minuten GOK; concurrenten DERDEN met link. "Bereik niet bekend" in plaats van een verzonnen cijfer: goed. | Feit | hoog | regel 5 |
| B6 | Nederlands zonder gedachtestreepjes (grep op lange en korte streepjes leeg); de mail is Engels. Schrijft als Dortus ("our add-on", "Thijs, Dortus"). | Feit | hoog | regel 8 |
| B7 | Fouten van 80.lv komen niet terug: grens 200 mm staat erin, bijlagen hebben Engelse namen met uitleg en zeggen welke bij gratis en welke bij Pro hoort, "a Pro hinge" (niet "knee"), CYBER25-check in de tabel, regel over betaald aanbod. | Feit | hoog | keuring 2026-11-23-80lv.md |

## Deel C: zou een redacteur van Digital Production het oppakken?
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| C1 | De haak is sterk en eerlijk: hun eigen zin over de elleboog, en een maker die daar antwoord op geeft. DP brengt precies dit soort kleine add-ons, met een droge, grappige toon. Kans dat ze het lezen en serieus nemen is goed; de GOK 1 op 4 vind ik redelijk. | Zo laten. | klein |
| C2 | "the gap from your CatPin piece" in het onderwerp kan lezen alsof we een andere maker afkraken. De openingszin in de tekst doet het netjes; het onderwerp is scherper. | Bijv. "News tip: articulated joints for 3D printable figures in Blender (the elbow from your CatPin piece)". | klein |
| C3 | DP schrijft over één ding per stuk. De mail brengt twee producten; dat is goed, maar het nieuws (Pro 1.2, rig naar figuur met eindstop uit de rig) zit in alinea 3. | Overweeg Pro eerst en de gratis versie als "the free base version" erna; of laten zoals het is, de volgorde is ook logisch. | klein |
| C4 | Ze citeren graag de maker over grenzen ("Honest limits", "not print tested"). Dat staat erin, goed. Wat ze nog missen om zonder vragen te schrijven: een plek met de Fit test strip (zie A6) en een korte uitleg wat er gebeurt bij een figuur die niet past ("the list says which joint is skipped and why", staat op Gumroad). | Eén halve zin: "Joints that do not fit are skipped, and the list says why." | klein |
| C5 | Bijlage 3 toont geen nummers (A12). | Of "each with its number" bij de bijlage weglaten, of een render met zichtbare nummers. | klein |
| C6 | Er bestaat een Pro-render van de houten tekenpop met messing gewrichten, gemaakt met de echte knop Figure from rig van Pro 1.2.0 (release `tekenpop-1`). Als kopbeeld bij Pro is dat sterker dan de Blender-schermafbeelding, en het voorkomt dat de redacteur de gratis pop (bijlage 4) als Pro-kopbeeld gebruikt. | Als er een gekeurd beeld uit `tekenpop-1` is: als vijfde bijlage, of in plaats van bijlage 2. | klein tot midden |
| C7 | Twee prijzen naast elkaar (A14). | Bijv. "Pro is $19 on Gumroad, 25% off from November 27 to December 1, with all 1.x updates; it is also on Superhive for $12 with 12 months of updates." Of alleen de dortus.com-link met "from $12". Keuze voor de hoofdchat (geld per verkoop verschilt per winkel). | klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet**
1. Vóór versturen moet "1.2" en de Fit test strip te zien zijn op minstens de pagina waar de mail naar linkt. Makkelijkst: één regel op dortus.com/click-joints/ bij Pro (onze eigen site), bijv. "New in 1.2: Fit test strip, five joints from 0.10 to 0.30 mm clearance to print first." Of Gumroad bijgewerkt (lijst Thijs punt 3), of Superhive toont 1.2.2. Lukt dat niet vóór 25 nov: schrap in de mail de zin "Version 1.2 adds a fit test strip ..." en maak van de "To be clear"-zin "it is not print tested by us yet, so we tell users to print a test joint first". Pas ook regel 16 van dit plan aan, want dortus.com noemt de strip nu niet. (A6)

**Kan**
1. Prijsregel duidelijker maken (A14, C7).
2. Onderwerp minder scherp: "the elbow from your CatPin piece" in plaats van "the gap" (C2).
3. "for 3D printed figures" in het onderwerp wordt "for 3D printable figures", in lijn met de nakeuring van 80.lv (B1).
4. Bij bijlage 3 "each with its number" niet beloven of een render met nummers (A12, C5).
5. Halve zin over overgeslagen gewrichten (C4).
6. Pro-beeld uit `tekenpop-1` als die gekeurd is (C6).
7. CYBER25-check blijft nodig; staat er al in de tabel.

Na moet 1: akkoord ja, zonder nieuwe volledige keuring (de hoofdchat of Verspreider kan met één curl op "Fit test" laten zien dat het staat).
