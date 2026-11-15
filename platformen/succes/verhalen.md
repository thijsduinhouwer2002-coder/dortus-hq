# Succesverhalen (Lars)

bezig: niets (laatste: CatPin, klaar 16 nov 2026 01:10 NL-tijd). Volgende: een Obsidian-plugin met betaalde extra's die echt verkoopt (opdracht hoofdchat 16 nov 00:05).

Nieuwste bovenaan.

---

## 3. CatPin (Alex Sokol, solo, één product, splitsen voor 3D-printen, Superhive en Gumroad)

Onderzocht 16 nov 2026, run 2, opdracht van de hoofdchat. Waarom dit verhaal: de sterkste nummer één in onze hoek (figuren printen), van een maker zonder eerder product, en hij verkoopt in drie prijsklassen, waaronder een Business-licentie.

### Bronnen
- Superhive, met curl gelezen 16 nov 2026 (00:50 NL-tijd): productpagina, FAQ, documentatie, reviews en versiepagina: https://superhivemarket.com/products/catpin, https://superhivemarket.com/products/catpin/faq, https://superhivemarket.com/products/catpin/docs, https://superhivemarket.com/products/catpin/ratings
- Gumroad, productpagina (schema.org-gegevens in de pagina) en de openbare zoek-API, 16 nov: https://alexsokol.gumroad.com/l/catpin en https://gumroad.com/products/search?query=catpin
- 80 Level, Emma Collins, 5 okt 2026: https://80.lv/articles/prepare-your-3d-models-for-printing-with-this-blender-add-on
- Digital Production, Bela Beier, 9 okt 2026, met prijzen gecontroleerd op 7 okt: https://digitalproduction.com/2026/10/09/catpin-blender-cuts-3d-printing/
- Zijn tutorial (titel via de oEmbed van YouTube; kijkcijfers en datum niet te lezen, YouTube blokkeert curl): https://youtu.be/KVPY63W0ovg, kanaal https://youtube.com/@alex_sokol_art
- Eerdere metingen van onze ploeg: Olaf (blender-2), 8 nov 2026, `platformen/blender-2/status.md` en `platformen/blender-2/data/superhive-print-2026-11-08.jsonl`.
- Niet gelukt: Reddit (blokkeert curl), Instagram, Telegram, ArtStation. Geen interview of devlog van de maker gevonden (zoektocht 16 nov). Hoe hij zijn eerste kopers kreeg, zegt hij nergens.

### Cijfers
- **Superhive:** 400+ verkopen, 4 reviews (alle vier 5 sterren), "Published 3 months ago", dus ±half augustus 2026 (GEZIEN 16 nov). Al 400+ op 8 nov (GEZIEN Olaf), dus in de laatste week geen nieuw blok; het volgende blok is waarschijnlijk 500+ (GOK over hoe Superhive telt).
- **Gumroad:** 84 reviews, gemiddeld 4,8 (GEZIEN 16 nov). Op 8 nov waren het er 81 (GEZIEN Olaf). Dus ±3 nieuwe reviews per week op Gumroad, tegen 4 in 3 maanden op Superhive. Hij heeft maar 1 product op Gumroad.
- Wat 84 reviews op Gumroad betekent in verkopen weet ik niet. Gumroad toont geen verkoopteller. Gumroad vraagt kopers in hun bibliotheek om sterren, dus daar schrijven waarschijnlijk veel meer kopers een review dan op Superhive (GOK). Bij Kambari zagen we op Superhive 1 review op 50 tot 140 verkopen; dezelfde verhouding op Gumroad toepassen kan niet.
- **Drie prijsklassen op Superhive** (GEZIEN 16 nov, nu 20% korting): Basic $27 ($21,60), Supporter Edition $40 ($32), Business / Studio $90 ($72) voor tot vijf mensen. Op Gumroad $30, nu $21.
- **De prijs veranderde, met bijna altijd korting:** 7 okt: Basic $30 met korting $24, Supporter $45 naar $36, Business $100 naar $80, extra jaar support 25% (DERDEN, Digital Production). 8 nov: $24 (GEZIEN Olaf). 16 nov: lijstprijs omlaag naar $27, $40 en $90, korting naar $21,60, en een extra jaar support nu 50% van de prijs (GEZIEN). Op alle drie de meetmomenten stond er een korting. Zoekresultaten tonen de pagina met `src=on_sale` en `src=popular`, dus hij stond in de lijsten "on sale" en "popular" van Superhive (GEZIEN in de links van de zoekmachine; hoe vaak en hoe lang weet ik niet).
- **Business-licentie:** 3,3 keer Basic voor vijf plaatsen. Ter vergelijking Click Joints Pro: Studio $45 is 3,75 keer Personal $12 (besluiten 15 nov 19:36).
- **Supporter Edition:** $13 meer dan Basic voor dezelfde add-on plus "an exclusive, personal thank-you letter from the add-on's creator" en "your name featured in the creator's Instagram Highlights". Hoeveel kopers die kiezen toont Superhive niet.
- Omzet, GOK: alleen Superhive, 400 tot 500 verkopen x ±$22 (meestal met korting) is $8.800 tot $11.000 bruto in 3 maanden, voor afdracht. Gumroad komt daar bovenop, maar hoeveel is niet te zeggen.
- Versies: 1.0.7 vóór 5 okt (80 Level), 1.0.8 in de oktober-update (Digital Production). De versiepagina op Superhive is leeg ("No versions found"), dus anders dan Cleave toont hij zijn versies daar niet.

### Wat hij deed, in volgorde (uit de pagina's afgeleid)
1. **Half augustus: één add-on, één klus.** Splitsen met pin en gat, rechte en gebogen snede, origineel blijft heel, alles in één keer exporteren naar STL. Op twee winkels tegelijk: Superhive en zijn eigen Gumroad. Of Gumroad eerder kwam weet ik niet.
2. **Antwoord op elke review, met een belofte met datum.** Een koper vraagt een losse deuvel (twee gaten en een los pinnetje). Zijn antwoord: "Yes, I can! It'll be available in the next Update on September 9". Alle vier de reviews op Superhive kregen een antwoord.
3. **Snel nieuwe functies:** handmatige snede, veelhoek-snede (ogen, monden, autoruiten los printen), tot vijf verbinders per snede, dubbelzijdige verbinder, controle op open randen (80 Level, 5 okt). Versie 1.0.8 in oktober.
4. **Begin oktober: twee vakbladen schrijven erover**, 80 Level (5 okt) en Digital Production (9 okt). Of hij die zelf tipte of dat ze het zelf vonden, weet ik niet (GOK). 80 Level heeft een betaalde rubriek "Promote", maar dit stuk staat onder Nieuws en Marketplace; of het betaald was, is niet te zien.
5. **Prijs en korting:** duurdere lijstprijs met een vaste korting, drie klassen, en in november een lagere lijstprijs met weer korting.
6. **De pagina vangt slechte reviews af:** "If something does not behave as expected, please contact support before leaving a review", met een lijstje van de vijf meest voorkomende oorzaken (schaal, eenheden, dicht model). Ook een eerlijk blok "Know what CatPin can handle" met wat niet werkt.

### Drie lessen
1. **Verkoop zakelijke kopers apart.** Een Business-licentie voor vijf plaatsen ($90) naast Basic ($27), met als doelgroep "3D-printing studios" en "STL model creators" op de pagina. Wie modellen verkoopt (en dat zijn er in de printwereld veel, zie McGybeer bij Joris), betaalt graag meer voor een licentie die bij zijn bedrijf past. Wij hebben die klasse al (Studio $45), dus dit bevestigt de keuze.
2. **Twee winkels, en de kleinere kan de grotere zijn.** Op Gumroad 84 reviews, op Superhive 4. Ook als Gumroad veel meer reviews per koper oplevert, is Gumroad bij hem geen bijzaak (GOK op GEZIEN). Wij staan voor Click Joints Pro alleen op Superhive.
3. **Vakbladen schrijven over kleine add-ons, juist als ze iets laten zien.** Na Kambari (CG Channel na 6 dagen) de tweede maker zonder publiek die binnen een paar weken in een vakblad stond, nu twee keer. Beide stukken zijn feitelijk en volgen de productpagina bijna letterlijk: een goede pagina met filmpjes is wat een redacteur nodig heeft.

### Eerlijk: wat niet zomaar voor ons geldt
- Zijn add-on doet precies wat Click Joints bewust niet doet (splitsen). Hij zegt zelf: "Articulated, rotating and movable joints are not currently supported." Dat is onze hoek. Maar Cleave heeft sinds 28 okt kogelgewrichten, dus "beweegbaar" is niet meer van ons alleen.
- Of de vaste korting werkt of alleen goedkoop oogt, kan ik niet meten. Ik zie wel dat hij hem steeds aan heeft en dat hij in de lijst "on sale" van Superhive staat.
- Waar zijn eerste kopers vandaan kwamen weet ik niet. Hij heeft YouTube, Instagram en Telegram, maar die kon ik niet lezen.

### Voorstel voor Dortus deze week
**Wie:** Chris (schrijft de tip), Thijs (verstuurt hem, want het gaat onder zijn naam), na de goedkeuring van Click Joints Pro (verwacht 18 tot 20 nov).
**Wat:** zodra Click Joints Pro live staat, een korte nieuwstip naar drie vakbladen die aantoonbaar over kleine Blender-add-ons voor printen schrijven: CG Channel (schreef over Smart Remesh), 80 Level en Digital Production (allebei over CatPin). Chris zet in `commercie/` per blad een mail van 5 zinnen klaar: wat het doet (gewrichten die bewegen, iets wat CatPin niet doet), voor wie, prijs, link naar de pagina en het demofilmpje, en één GIF. Daarna een regel op `organisatie/lijst-thijs.md` met de drie contactadressen van de redacties en wat hij moet doen. Kost niets en is in een uur klaar. Of het werkt is een GOK, maar het is twee keer gezien bij makers zonder publiek.
**Erbij, voor later (niet deze week):** Click Joints Pro ook op Gumroad, zoals CatPin. Dat vraagt een Gumroad-account van Thijs en Gumroad houdt 10% in (besluiten 6 nov). Pas zinvol als Pro op Superhive verkoopt.

---

## 2. Cleave (V4SS3UR, solo, één product, 3D-printen op Superhive)

Onderzocht 15 nov 2026, run 1, opdracht van de hoofdchat. Waarom dit verhaal: een nieuwkomer zonder publiek, in precies onze hoek (figuren printen, gewrichten), in een drukke categorie. Onze ploeg kent Cleave al als concurrent van Click Joints (`producten/blender-gewrichten/ontwerp.md`); hier gaat het om hoe hij het aanpakte.

### Bronnen
- Productpagina, versiegeschiedenis en reviews, met curl gelezen 15 nov 2026: https://superhivemarket.com/products/cleave, https://superhivemarket.com/products/cleave/versions, https://superhivemarket.com/products/cleave/ratings
- Zijn YouTube-filmpjes (titels via de openbare oEmbed van YouTube; kijkcijfers niet te lezen, YouTube gaf 429): kanaal https://www.youtube.com/@V4SS3UR
- Concurrenten in dezelfde categorie, productpagina's Superhive 15 nov: catpin, split-3dprint, printsplitter, easy-print, split-it, cutandkey, print-forge, dovetail-key.
- Geen interview, devlog of Reddit-post van de maker gevonden (zoektocht 15 nov).

### Cijfers (GEZIEN 15 nov 2026, tenzij anders vermeld)
- 100+ verkopen, 3 reviews (alle drie 5 sterren), "about 2 months ago" gepubliceerd. Versie 1.0.0 op 23 sep 2026, dus ±7,5 weken.
- Prijs $23, plus een tweede keuze "Support the developer" van $28: dezelfde download, $5 extra "to help fund future updates". Nu een coupon van 10% voor een week.
- De maker heeft maar 1 product in de winkel: geen eerder publiek op Superhive.
- **12 versies in 6 weken:** 1.0.0 (23 sep), 1.1.0 (24 sep), 1.2.0 (4 okt), 1.2.1 (6 okt), 1.3.0 (10 okt), 1.4.0 (11 okt), 1.5.0 (20 okt), 1.5.1 (21 okt), 1.6.0 (28 okt, kogelgewrichten), 1.6.1 (2 nov).
- Omzet, GOK: 100 tot 200 verkopen x $23 is $2.300 tot $4.600 bruto in 7,5 weken, voor afdracht en coupons.
- De categorie "model splitsen voor printen" is druk: Dovetail Key (Kambari, met publiek) 800+, CatPin 400+, Split 3D Print 400+ (teller telt ook gratis downloads), Cleave 100+, Split It 10+, Easy Print 10, Printsplitter, Cut and Key en PrintForge geen blok (onder 10). Cleave is de enige nieuwkomer van de laatste 2 maanden boven de 10+.

### Wat hij deed, in volgorde
1. **Versie 1.0 met één heldere belofte:** "Too big to print? Split it." Splitsen waar het model buigt (nek, schouders, knieën), verbinders in echte millimeters, controle tegen je printer.
2. **Daarna bijna elke week een versie**, steeds iets wat kopers vragen of nodig hebben: Make Manifold, printerlijst (120+ modellen) en 3MF-export, dowels en staafkanalen, een "Simple mode" omdat het paneel te vol werd, en op 28 okt kogelgewrichten voor beweegbare figuren. Elke versie staat met datum op de pagina, dus een koper ziet dat het product leeft.
3. **Hij beantwoordt elke review zelf, binnen een paar dagen**, bedankt, en vraagt om Blender-versie, besturingssysteem en een voorbeeldbestand bij een crash. Op de klacht "te veel menu's" antwoordt hij dat hij eraan werkt; in 1.5.0 kwam de "Simple mode".
4. **Uitleg op de plek waar mensen zoeken:** vier YouTube-filmpjes met titels die mensen intypen ("Cleave 01 (Beginner): Split a Model for 3D Printing in Blender", "Ball Joints for 3D Printed Figures (Blender)"). Op de pagina: "Your first split, step by step, in under four minutes."
5. **De pagina beantwoordt de gratis vervanger:** een blok "Why not just bisect it by hand?" ("You can. ... find out the fit was wrong after a six hour print"), en een eerlijk blok wat het niet doet ("Slicing, hollowing and supports stay in your slicer").
6. **Een eigen blok voor AI-modellen:** "Made for Meshy, Tripo and the like. Generators fuse arms, armour and props into one shell." Met een controle vooraf of het model dicht is en Make Manifold.

### Drie lessen
1. **Zichtbaar en snel bijwerken verkoopt, juist zonder publiek.** 12 versies in 6 weken, elk met datum op de pagina, en reviews die zeggen "in its early stages ... it can only get better" en "Didn't expect it to be so good yet". Een koper vergeeft ruwe randjes als hij ziet dat er elke week iets bijkomt. Dit is de tweede keer na Kambari (versie 2 na 6 dagen).
2. **AI-modellen zijn een eigen doelgroep, en ook hier staat het op de pagina.** Na Kambari ("Tame the mess AI leaves behind") de tweede maker die er een apart blok aan wijdt. Mensen die met Meshy of Tripo een figuur maken en het willen printen, hebben precies het probleem dat splitsen en gewrichten oplost.
3. **Elke review beantwoorden en een duurdere steunkeuze met dezelfde download.** Kost niets, maakt de pagina warmer, en de $28-keuze vangt kopers die meer willen geven. Hoeveel mensen die kiezen weet ik niet (geen cijfer, Superhive toont het niet).

### Eerlijk: wat niet zomaar voor ons geldt
- 100+ in 7,5 weken is een nette start, geen grote treffer. CatPin haalde 400+ in 3 maanden.
- Of hij buiten Superhive iets deed (Reddit, Discord, forums) heb ik niet gevonden. De verkoop kan ook uit de nieuwlijst en zoekfunctie van Superhive komen (GOK).
- Zijn productpagina is lang en heel goed, met filmpjes en voor-en-na-beelden; dat is werk dat wij voor Click Joints Pro deels al deden (demofilm, `platformen/blender/superhive-pagina.md`).

### Voorstel voor Dortus deze week
**Wie:** Bram (bouwer Blender) en Chris (winkeltekst), na de goedkeuring van Click Joints Pro door Superhive.
**Wat, drie kleine dingen die samen de les van Cleave en Kambari overnemen:**
1. **Een vast ritme: de eerste 6 weken elke week een kleine versie** (fout weg, of één wens van een koper), met datum in de versiegeschiedenis van Superhive. Past binnen de regel van hooguit één versie per week via Thijs (besluit Hans, 9 nov 20:44).
2. **Een blok "Made for AI-generated figures (Meshy, Tripo)"** op de Superhive-pagina, maar pas als Bram een AI-model door Click Joints Pro heeft gehaald en het werkt (eerst testen, niets beloven wat we niet zagen).
3. **Een tweede prijskeuze "Support the developer"**, $5 boven de gewone prijs, zelfde download. Chris zet het in `commercie/`; Thijs of de hoofdchat zet het in de winkel.
Plus: elke review binnen 2 dagen beantwoorden. Dat moet Thijs doen (bericht onder zijn naam), dus Chris zet per review een antwoord klaar op de lijst.

---

## 1. Milad Kambari (3DRedBox, Smart Remesh en Image to 3D op Superhive)

Onderzocht 15 nov 2026, run 1, opdracht van de hoofdchat. Een 3D-artiest die een klein bedrijf voor game-uitbesteding leidt (3DRedBox) en sinds 2024 op Superhive verkoopt. Hij is geen cursusverkoper met een trucje: zijn cijfers staan openbaar in de winkel.

### Bronnen
- Winkel van de maker, alle 85 producten (5 pagina's) en alle 85 productpagina's met curl gelezen op 15 nov 2026: https://superhivemarket.com/creators/miladkambari
- Smart Remesh, productpagina en reviews: https://superhivemarket.com/products/smart-remesh en https://superhivemarket.com/products/smart-remesh/ratings
- Image to 3D, productpagina en reviews (data van alle 22 reviews): https://superhivemarket.com/products/imageto3d
- CG Channel, Jim Thacker, 25 aug 2026, "Check out promising new Blender retopology tool Smart Remesh": https://www.cgchannel.com/2026/08/check-out-promising-new-blender-retopology-tool-smart-remesh/
- Nieuwkomers met hetzelfde onderwerp, ter vergelijking (productpagina's Superhive, 15 nov): image-to-3d-local, genmesh, depthforge.
- Niet gelukt: zijn ArtStation-cv (blokkeert curl) en het webarchief (geen verbinding vanuit onze omgeving). Geen interview of devlog van hem gevonden; alles hieronder komt uit de winkel, zijn productpagina's en CG Channel.

### Cijfers
Superhive toont verkopen in blokken ("2600+"). Alles GEZIEN op 15 nov 2026 tenzij anders vermeld.

| Product | Verkopen | Reviews | Prijs nu | Online sinds |
|---|---|---|---|---|
| Smart Remesh (retopologie) | 2600+ | 19 (gem. 4) | $17 | ±19 aug 2026 |
| Image to 3D (AI, lokaal op eigen GPU) | 1200+ | 22 (gem. 4) | $18 | ±30 okt 2026 (eerste review 16 dagen geleden) |
| Auto Unwrap (UV) | 1200+ | 9 | $18 | ±2 maanden |
| Dovetail Key | 800+ | 13 | $18 | ±5 maanden |
| Smart Segmentation | 300+ | 2 | $12 | ±3 maanden |
| Blender to Unreal Live Link | 300+ | 6 | $18 | ±9 maanden |
| Blender to Substance Painter Live Link | 200+ | 7 | $18 | ±9 maanden |
| Modeling Toolkit | 200+ | 1 | $18 | 20 dagen |
| 21 andere producten | 10+ tot 100+ | | $0 tot $28 | |
| 56 producten (vooral modellen, base meshes, 13 "lighting studios") | geen blok, dus onder 10 | 0 | $8,90 tot $25 | 1 tot 2+ jaar |

- Startprijs Smart Remesh was $15 (CG Channel, 25 aug, DERDEN); nu $17. Hij verhoogde dus na de eerste goede reviews.
- Versie 2 kwam 6 dagen na de release (CG Channel, DERDEN). Nu staat versie 3 online.
- Reviews tegen verkopen: Smart Remesh 19 op 2600 (0,7%), Image to 3D 22 op 1200 (1,8%), Auto Unwrap 9 op 1200 (0,75%), Dovetail Key 13 op 800 (1,6%). Op Superhive schrijft dus maar 1 op de 50 tot 1 op de 140 kopers een review (rekensom met GEZIEN-cijfers; de blokken zijn ondergrenzen).
- Omzet, GOK: de vier toppers samen ±5.800 verkopen x ±$17 is ±$100.000 bruto in ruim een half jaar, het meeste in de laatste 3 maanden. Kortingen (nu 25% coupon), studiolicenties en de afdracht van Superhive niet meegerekend; het echte bedrag voor hem ligt dus lager.
- Vergelijking: drie andere makers zetten in dezelfde weken een AI-naar-3D-add-on op Superhive (6, 21 en 24 dagen geleden). Geen van drieën heeft een verkoopblok, dus onder 10 verkopen (GEZIEN). Hetzelfde onderwerp, hetzelfde moment, 100 keer minder verkoop.

### Wat hij deed, in volgorde (uit de winkel afgeleid)
1. **2024 tot 2025: modellen.** Base meshes (helmen, zwaarden, kisten), ornamenten en 13 "lighting studios". Bijna niets verkocht (56 producten onder 10).
2. **Begin 2026: koppelingen (live links)** van Blender naar Unreal, Substance Painter en RizomUV. Eerste echte verkoop: 200+ tot 300+.
3. **Voorjaar 2026: kleine hulpjes** ($6 tot $18), een paar gratis ($0 tot $2, "betaal wat je wilt"). Dovetail Key haalt 800+.
4. **Aug 2026: Smart Remesh.** Lost een bekende pijn op (rommelige meshes uit CAD, scans, gekochte modellen en vooral AI-generatoren). De organische stand draait op het open-source Instant Meshes (BSD-licentie, op de pagina genoemd); zijn eigen werk is de harde-oppervlak-stand en alles eromheen: één knop, UV's en materialen blijven, terugzetten kan altijd. CG Channel schrijft er na 6 dagen over. Versie 2 na 6 dagen, daarna Mac en Linux, daarna versie 3.
5. **Sept tot nov 2026: de volgende producten haken in op dezelfde kopers.** Auto Unwrap (UV, 1200+), en eind oktober Image to 3D: open-source AI-modellen (TRELLIS, Hunyuan, FLUX.2 Klein en meer) die lokaal op je eigen NVIDIA-kaart draaien, "No cloud. No credits." De pagina laat voorbeelden zien met "Image to 3D + Smart Remesh, 1.5M to 5K faces": het ene product verkoopt het andere.

### Drie lessen
1. **Veel schoten, en de treffer zit in gereedschap voor een grote pijn, niet in spullen.** Van 85 producten verkochten er 56 onder de 10. Vier add-ons maken bijna alle omzet. Hij bleef uitbrengen tot hij de goede soort vond (werkstroom-hulpmiddelen voor game-artiesten) en ging daarna vol op die soort door. GEZIEN in zijn eigen winkel.
2. **Een bewezen open-source motor plus perfecte bediening in Blender is een product, als je op een golf zit.** Smart Remesh is voor de helft Instant Meshes, Image to 3D is TRELLIS en Hunyuan. Wat hij verkoopt is: één knop, niets kwijt (UV's, materialen, naam), alles terug te draaien, filmpje per onderdeel ín de add-on, en het antwoord op de golf van AI-modellen ("Tame the mess AI leaves behind"). Een review: AI-generatoren "spit out chaotic triangle soup with 2 to 3 million faces", dit lost het "in seconds" op.
3. **Na de lancering is snelheid het product.** Versie 2 na 6 dagen, Linux-versie op verzoek, wensen van kopers in de volgende versie. Drie van de tien nieuwste reviews noemen dat de maker snel reageerde of hun idee inbouwde. En een nieuw product verkoopt aan wie het vorige al had: Image to 3D haalde 1200+ in 16 dagen, terwijl drie nieuwkomers met hetzelfde idee onder 10 bleven.

### Eerlijk: wat niet zomaar voor ons geldt
- Hij is zelf 3D-artiest met een game-bedrijf en kent de pijn van binnen. Wij kennen 3D-printen niet uit eigen werk.
- Hoe hij aan zijn eerste kopers kwam, weet ik niet: geen interview gevonden. Dat CG Channel hem na 6 dagen noemde kan toeval zijn of een persbericht (GOK). Hij heeft een Discord en post voorbeelden op X.
- De verkoopblokken zijn ondergrenzen en kunnen ook gratis "betaal wat je wilt"-downloads tellen bij producten van $0 tot $2. Bij zijn toppers ($17 en $18, geen gratis optie) is dat niet zo.

### Voorstel voor Dortus deze week
**Wie:** Bram (bouwer Blender), met een ja van Hans; Chris voor de lanceertekst.
**Wat:** Click Joints is één schot. Maak er een reeks van voor dezelfde kopers (3D-printers die figuren maken), en kies het tweede product op de golf van AI-modellen: een add-on die een AI-model (uit Meshy, TRELLIS, Hunyuan of Image to 3D) in één klik printbaar maakt (dicht maken, wanddikte, opdelen in delen die met Click Joints scharnieren), gebouwd op een bewezen open-source motor met een vrije licentie. Bram kijkt deze week eerst 1 uur in Superhive en op extensions.blender.org of zoiets al bestaat en hoe het verkoopt (zoeken op "printable", "3D print", "AI mesh"). Of de vraag er is, is nog een GOK; de golf zelf is GEZIEN (Image to 3D 1200+ in 16 dagen, reviews die AI-modellen noemen).
**Klein en meteen, na de goedkeuring van Click Joints Pro:** binnen een week na de lancering een versie 1.1 met de eerste wensen van kopers, en dat in de changelog zeggen. Lanceerprijs laag laten (de $9 van Chris klopt met dit verhaal) en na de eerste goede reviews verhogen, zoals Kambari van $15 naar $17.

**Aanvulling na verhaal 2 (Cleave, zelfde run):** het idee "AI-model in één klik printbaar maken en opdelen" is voor een deel al bezet. Cleave heeft een blok voor Meshy en Tripo, een controle of het model dicht is en Make Manifold, en splitst in delen met verbinders en kogelgewrichten (GEZIEN). Bram zoekt dus niet of het bestaat, maar wat Cleave en de rest niet doen. Het voorstel blijft staan als richting (reeks voor dezelfde kopers), het precieze product is nog open.
