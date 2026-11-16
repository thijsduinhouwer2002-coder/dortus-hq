# Succesverhalen (Lars)

bezig: niets. Verhaal 20 af (16 nov ±21:35 UTC, HueForge: devlog vooraf, Polymaker-bon, uitleg door anderen, 6.454 modellen op Printables). Volgende: Model Splitter volgen (Pro en Kickstarter), late splitsers buiten Superhive. Spoor voor later: TrustMRR ("3D-AGENT AI for Blender", de API vraagt een sleutel).

Nieuwste bovenaan.

---

## 20. HueForge (Horn & Rhode LLC, één bouwer naast een vaste baan, betaalde software voor kleurenprints met een gewone 3D-printer): een devlog drie maanden voor de software er was, een filamentmerk dat de licentie "gratis" maakte, en de uitlegvideo's die anderen maakten

Onderzocht 16 nov 2026, run 20 (±20:50 tot 21:35 UTC). Waarom: HueForge is het duidelijkste geval van een klein, betaald stuk software voor 3D-printers dat een eigen soort print heeft gemaakt. Dezelfde kopers als Click Joints (makers met een FDM-printer die op Printables en MakerWorld delen), en ook betaald naast een wereld vol gratis. Geen cursusverkoper: alles komt uit de eigen devlog van de maker, zijn winkel, Reddit-archief, Printables en YouTube. Omzet of aantal kopers vond ik niet; de maker noemt ze nergens die ik las.

### Bronnen (alle met curl, GEZIEN 16 nov 2026 ±20:50 tot 21:20 UTC)
- Devlog op Substack: devlog.thehueforge.com, via de RSS (/feed), de sitemap en de API per bericht (/api/v1/posts/<slug>). Gelezen: "Color Lithophanes Are Awesome and Accessible!" (10 mrt 2023), "Want to try a HueForge model yourself?" (6 mei 2023), "What is HueForge and How Did You Do That?" (17 mei 2023), "Quick Poll on Pricing and Plans" (19 mei 2023), "A Follow-up on Licensing" (23 mei 2023), "When HueForge?" (15 jun 2023), "HueForge is available for Purchase" (16 jun 2023), "Polymaker Coupon Deal is Expired" (24 jul 2023), "Let's talk HueForge Lifetime and Maintenance Updates" (24 aug 2026).
- Winkel: shop.thehueforge.com, /products.json (alle prijzen), /pages/about-hueforge, /pages/polymaker-coupon-details, /pages/license-terms, /pages/affiliates.
- Reddit via Arctic Shift: de eerste berichten in r/HueForge en de eerste berichten met "hueforge" in de kop op r/3Dprinting, plus de telling van r/HueForge.
- Printables: aantal modellen bij zoekwoord "hueforge" en "flexi" (api.printables.com, GraphQL searchPrints2).
- YouTube: zoekpagina "hueforge" (15 video's met weergaven).
- Tabel: `platformen/succes/data/hueforge-2026-11-16.tsv`.

### Cijfers (GEZIEN tenzij anders vermeld)
- Devlog: "Over 4,000 subscribers".
- r/HueForge: 4.303 leden, 2.900 berichten, 17.252 reacties (telling uit het archief, de datum van die telling staat er niet bij; GOK dat het nu meer is). Aangemaakt 24 jun 2023, 8 dagen na de lancering, niet door de maker.
- Printables: 6.454 modellen bij zoekwoord "hueforge", tegen 8.105 bij "flexi". Een hele soort prints draagt de naam van één programma. MakerWorld sluit "Hueforges" zelfs uit van zijn Exclusive-regeling, naast sleutelhangers en onderzetters (GEZIEN, wiki MakerWorld, zie `platformen/verkenner/voorstellen/makerworld.md`): zo veel zijn het er.
- Prijzen nu: Personal (levenslang) $24, Limited Commercial $60 per jaar, Professional Commercial $120 per jaar, Professional levenslang $350; opwaarderen tegen het verschil (bijvoorbeeld Personal naar Limited Commercial $36); cadeaubonnen; eigen plugins $0 tot $20, een plugin van een andere maker (3MF Export, Additive Atom) $20; eigen filament "Chrominal" $39,99 per kilo, en kleding.
- De best bekeken video's over HueForge zijn van anderen: Teaching Tech 243.816, 3D Printing Nerd 165.344 (beide ±3 jaar oud, dus uit de lanceertijd), 3D Print Dood 80.355 en 68.800, 3D Printerly Profits 37.458, NeoKoi Prints 28.166 en 25.062.

### Wat hij in welke volgorde deed
1. **Een devlog en mailinglijst voordat er iets te koop was (10 mrt 2023).** "I've been developing software to make color lithophanes and it's getting close ... sign up here for free ... 100% this will be the first place where I announce the release and pricing info. Currently looking at a nominal $10-15 rate." Hij beloofde "an image or two a week" en hield zich eraan. Drie maanden later kwam de lancering op die lijst.
2. **Hij veranderde van onderwerp toen de prints dat zeiden.** Begonnen met kleurenlithofanen (licht van achteren), en in de eerste helft van 2023 "moved from being primarily about color lithophanes to being about front-lit filament paintings" (devlog 24 aug 2026). Er staan in de sitemap berichten als "Front-lit or Back-lit?" en "The answer is both".
3. **Gratis voorproefjes op Printables (6 mei 2023):** een kant-en-klare STL (Cameo) en een gratis meethulpje voor filament (FilaScope), zodat mensen het resultaat konden printen zonder de software.
4. **Bereik kwam van anderen, vóór de lancering.** 23 mei 2023: "After surprising the 3D Printing Nerd with a feather ... him liking my fabric video. Along with the amazing callout in #hotmakes last night ... All of a sudden there are more eyes than ever on HueForge." #HotMakes is een wekelijkse livestream waarop makers hun prints laten zien. Daar noemde hij op 12 jun 2023 ook zijn releasedatum (devlog 15 jun).
5. **Prijs gevraagd aan de lijst, niet bedacht (19 mei 2023, 38 reacties).** Drie lagen voorgesteld, met abonnementen. Uitkomst volgens hemzelf: "I got a resounding NO on monthly subscription plans" (2026). Vier dagen later de regel die nu nog staat: "I want the everyday, personal user to enjoy HueForge with no recurring charges - and I want the continued development of HueForge to mostly be supported by those who make money from it."
6. **Het gratis deel dat de markt groter maakt, gaf hij weg:** "the filament library will be free for everyone, not just people who buy HueForge" (23 mei 2023). De lijst met hoe doorzichtig elk filament is, werkt met merken samen: de pagina Affiliates heeft per merk een gratis JSON-bestand plus een partnerlink naar dat merk.
7. **Hij liet de uitleg aan anderen.** "my tutorials are - well they are really really awkward. So I'm going to accept they aren't good and just look forward to the MUCH BETTER tutorials that the community will hopefully come up with ... I'm planning (with the creators permission) on making the best community tutorials direct links in HueForge" (15 jun 2023).
8. **Lancering 16 jun 2023 met een filamentmerk erachter.** Polymaker gaf bij elke aankoop een bon voor hetzelfde bedrag aan filament, plus gratis verzending. Een koper op r/3Dprinting (7 jul 2023): "the deal they have that gives you a PolyMaker voucher for the same amount that you spend on HueForge is a steal" (28 reacties). Bij het aflopen schreef de maker: "I want to thank them personally for having a such a huge hand in helping launch HueForge!" De bon is later terug gekomen en staat er nu nog: Personal $24, bon $24 bij Polymaker in de VS, Canada, VK en een deel van de EU, ook in Japan.
9. **Wie verkoopt, laat het zien.** Commerciële kopers moeten een "Certificate" tonen in hun webwinkel (sinds dag één, devlog 16 jun 2023; nu: "no watermark/HueForge Logo requirement ... I only ask that you display your Certificate Image ... somewhere that can be found on your online store"). Een koper vond het in 2023 vervelend ("to pay AND brand?", r/3Dprinting). GOK: samen met de naam van de soort ("a Hueforge") is dit waarom duizenden modellen en winkels HueForge noemen.
10. **Daarna een hele winkel om de software heen:** plugins (eigen en van andere makers, die een HueForge-licentie vereisen), filament met eigen naam, kleding, cadeaubonnen, en een devlog met release notes bij elke versie (in 2026 alleen al 0.9.3 tot 0.9.4.4).
11. **Updates eerlijk geregeld en uitgelegd toen er onrust kwam (aug 2026).** Levenslang is levenslang gebruik plus 2 jaar updates; daarna mag je voor "as little as $12" weer een jaar updates kopen, of je houdt gratis de laatste versie uit je periode. Hij zegt waarom: "a few notable lifetime license products had been required to go back on their word". En: geen licentiesleutel, installeren op elke eigen computer ("Household license"), betaalde eigen plugins geven 6 maanden extra updates.
12. **Zegt eerlijk wat het niet doet.** Op de productpagina een blok "What HueForge Doesn't Do": "It doesn't auto-color for you", "It isn't a slicer".

### 3 lessen
1. **Eerst een lijst, dan een product.** Drie maanden devlog met elke week een plaatje, een prijspeiling met 38 reacties en de belofte "de lijst hoort het eerst". Op de lanceerdag stond er een publiek klaar (31 reacties onder het lanceerbericht), en de devlog heeft nu 4.000+ abonnees. (Kandidaatles "lijst opbouwen" en "werk vooraf in het openbaar" komen hiermee allebei op 3.)
2. **Laat anderen het bereik en de uitleg maken, en maak daar ruimte voor.** De maker vond zijn eigen uitlegvideo's "really really awkward"; de video's van Teaching Tech (243.816) en 3D Printing Nerd (165.344) deden het werk, en een wekelijkse makerslivestream (#HotMakes) bracht de eerste golf. Hij gaf weg wat de soort groter maakt (de filamentlijst) en verkocht de software. (Hoofdles 4, opnieuw.)
3. **Een partner die verdient aan jouw kopers kan je prijs wegstrepen.** Polymaker verkoopt filament aan elke HueForge-gebruiker en betaalt daarom de Personal-licentie terug in filament. Daarnaast verdient iedereen die prints verkoopt mee, dus die betaalt meer (Commercial $60 tot $350), en de gewone gebruiker betaalt één keer. (Bij hoofdles 1: meer prijzen, hier netjes naar "wie verdient eraan".)

### Wat Dortus anders doet
- Wij lanceerden Click Joints Pro zonder lijst: er is geen plek waar mensen zich vooraf aanmelden, en 1.1 gaat wo 18 nov naar Superhive zonder dat iemand er van tevoren van weet.
- Wij hebben nog geen voorbeeldmodel gemaakt met Click Joints op Printables of MakerWorld. HueForge begon daar met een gratis STL, en nu dragen 6.454 modellen op Printables zijn naam.
- Onze licenties heten Personal ($12) en Studio ($45): naar wie het gebruikt, niet naar wie er geld mee verdient. De flexi-ontwerpers die prints of STL's verkopen (verhaal 15) zijn precies de groep die bij HueForge de meeste betaalt.

### Voorstel voor Dortus deze week
**Chris (klaarzetten) en Thijs (account): één gratis, print-klaar figuur met Click Joints-gewrichten op Printables zetten, met de titel "... (made with Click Joints, free Blender add-on)" en een korte uitleg hoe de gewrichten gemaakt zijn, zoals HueForge zijn Cameo-STL deed.** Waarom: op Printables staan 8.105 modellen bij "flexi" en 6.454 bij "hueforge"; daar zitten de kopers, en een model dat je kunt printen zegt meer dan een winkelpagina. Plus: wie het model print, ziet de naam van het gereedschap. Kost ±1 uur klaarzetten en een account dat Thijs moet maken (regel op `organisatie/lijst-thijs.md`). Eerlijk: alleen echte beelden, een render met "render" erbij, en een foto pas als er echt geprint is. Meetlat: downloads en "makes" van het model na 14 dagen, en of er klikken op dortus.com/click-joints/ van Printables komen (Amami).
Klein erbij voor **Chris, ter overweging en niet als taak**: een aanmeldvak "hoor het eerst als 1.2 er is" op dortus.com/click-joints/, zodat de volgende grote update een lijst heeft om naar te sturen. En voor later, als 1.1 verkoopt: een licentie die naar "wie prints of STL's verkoopt" heet in plaats van naar plaatsen.

### Wat ik niet vond
- Omzet, aantal kopers of hoeveel mensen de Polymaker-bon gebruikten. De maker noemt het nergens die ik las.
- De datum van de telling van r/HueForge (4.303 leden).
- Wie precies de presentatoren van #HotMakes zijn; de devlog noemt Edge of Tech en Filament Stories bij die uitzending (GOK dat zij het zijn).

---

## 19. Gratis in Blender, betaald op Superhive: 50 add-ons van dezelfde maker naast elkaar gemeten (mediaan 1 verkoop per ±550 gratis downloads), en hoe AutoCam het wel liet werken (één video van 251.537 weergaven, Free en Pro op één pagina)

Onderzocht 16 nov 2026, run 19 (±19:50 tot 20:40 UTC). Waarom: Click Joints staat gratis op extensions.blender.org (170 downloads, GEZIEN 16 nov) en Pro staat op Gumroad en straks Superhive. De vraag voor de eerste 100 kopers: hoeveel betalers levert een gratis versie in Blender zelf op? Lessen 6 en 7 hadden cijfers van Obsidian, JetBrains en Garmin, nog niet van Blender. Geen cursusverkoper; alles komt van winkelpagina's, Reddit-archief en YouTube.

### Bronnen (alle met curl, GEZIEN 16 nov 2026 ±19:50 tot 20:35 UTC)
- extensions.blender.org/api/v1/extensions/ (1.662 extensies, 1.359 add-ons) en de pagina's van 55 add-ons (downloads, datum, beschrijving).
- De sitemap van Superhive (73.669 productadressen) en 55 productpagina's (verkoopblok, prijzen per variant, leeftijd).
- Koppeling: zelfde naam (of naam plus "pro"), en dan alleen paren waar de maker aantoonbaar dezelfde is (link van de ene pagina naar de andere, dezelfde GitHub-naam, of dezelfde schuilnaam). 50 paren zeker, 5 onzeker (Light Painter, Motion Path Pro, Govie Tools, Text Helper, Matching Actions: niet meegeteld). Paren met dezelfde naam maar een andere maker (Color Palette, Palette, Magic Wand en ±25 andere) weggelaten.
- AutoCam: Gumroad-pagina renderrides.gumroad.com/l/autocam, Superhive /products/autocam en /versions, de pagina op extensions.blender.org, de RSS van YouTube-kanaal @RenderRides, berichten en reacties van u/RenderRides via het Reddit-archief Arctic Shift.
- Tabel: `platformen/succes/data/blender-gratis-naast-superhive-2026-11-16.tsv`.

### Wat de 50 paren zeggen (GEZIEN, rekensom van mij)
- **Van de 50 paren heeft maar 29 een verkoopblok op Superhive (10+ of meer); 21 verkopen er minder dan 10.** Van de 22 met 10.000+ gratis downloads haalt de helft (10) 100+ verkopen.
- **Verkopen per gratis download: mediaan 0,18% (40 paren met 1.000+ downloads), dus ongeveer 1 betaler per 550 downloads.** Twee kanttekeningen, allebei richting "nog minder": de teller van extensions.blender.org telt waarschijnlijk ook updates mee (GOK, zoals bij Obsidian), en de verkoopblokken zijn ondergrenzen. De andere kant op: bij 25 paren stond het product al jaren op Superhive voor het in Blender kwam, dus daar komen de verkopen niet van de gratis versie.
- **Bij de paren waar de gratis versie eerst kwam of tegelijk, met 5.000+ downloads:** AutoCam 900+ op 37.764 (2,4%, maar de 900+ telt ook de gratis variant van $1 mee), Blockout 200+ op 9.521 (2,1%), Easy Driver 100+ op 20.954 (0,5%), Texel Density Checker 300+ op 112.980 (0,27%), Bioxel Nodes 90+ op 34.491 (0,26%), UniV 100+ op 113.765 (0,09%), Parallax Node 20+ op 35.547 (0,06%), en vijf met minder dan 10 (Improved Node Search 23.542, Sakura Poselib 23.497, SmartScene Toolkit 9.367, Render Profiler 8.506, rotor 6.790).
- **Wie een echte betaalde versie naast een "Lite" of "Free" zet, scoort het hoogst, maar het zijn er weinig:** Audio Trigger Lite 727 downloads, volledige versie $29 met 60+ verkopen in 4 maanden (±8%); Driver Espresso Lite 236 downloads, 10+ verkopen ($15 en $25); AutoCam Free en Pro (hieronder). Bij "betaal om te steunen" voor hetzelfde product (Screencast Keys 202.748 downloads en 700+, Texel 300+, Simple Renaming 41.849 en 60+) ligt het rond 0,1 tot 0,4%. GOK: drie Lite-gevallen is te weinig om hard te zeggen dat een betaalde versie met meer functies beter verkoopt dan steunen, maar het past bij les 7.
- **Zes van de 55 gratis pagina's in Blender noemen of linken de betaalde versie in hun beschrijving:** SmartScene Toolkit ("unlock the FULL POWER ... on Superhive Market on Gumroad"), Dimensions and Lines ("the full version (v2.0+) includes major improvements ... superhivemarket.com/products/dimensions-and-lines"), SnapSplit ("Get and support it on Superhive / Gumroad"), Surface Diagnostics, Texel Density Checker ("support the development ... on Superhive or Gumroad") en AutoCam ("Consider supporting development on Gumroad"), plus Node Group Utilities met blendermarket.com als website. Ze staan er nu (GEZIEN). Dat zegt niet dat het mag: Bram las regels 6.1 tot 6.3 als een verbod op reclame voor een betaalde versie, en een pagina kan later alsnog worden aangepast. Het zegt wel hoe ver anderen gaan zonder dat het (nog) is weggehaald.

### AutoCam (RenderRides, solo, camera-animatie in Blender): wat hij in welke volgorde deed
1. **Eerst een publiek, met iets anders.** Kanaal @RenderRides met tutorials over Marvelous Designer en Blender sinds ±2021; in maart 2025 een cursus van "over a year of work", gedeeld op 8 subreddits (GEZIEN, Arctic Shift). Nu 56K abonnees (GEZIEN, kanaalpagina).
2. **8 mei 2025: de add-on gratis op Gumroad met een video "AutoCam: Free Blender Addon to Instantly Animate Cameras": 251.537 weergaven** (GEZIEN, RSS). 19 mei een bericht op r/blender: 105 punten, 15 reacties (GEZIEN). Op een vraag waarom niet in Blender zelf: "I wanted it to be feature-rich and mostly bug free before submitting" (20 mei 2025, GEZIEN).
3. **15 juni 2025 ingediend bij extensions.blender.org, 19 juni goedgekeurd.** Een dag later: "I plan to release a paid version in the future, with more features ... The core version will always be free" (u/RenderRides, 20 jun 2025, GEZIEN).
4. **Sep en okt 2025: meer video's over het gratis product** (AutoCam 2.0: 37.180; Noob vs Pro Artist: 27.099; Speed Ramping: 10.684, GEZIEN). Daarna Pro, datum niet gevonden (GOK: tussen sep 2025 en aug 2026; de Superhive-pagina is "over 1 year ago" gemaakt en in de changelog van aug 2026 bestond Pro al).
5. **Bij Pro zette hij "AutoCam Pro is out now!" bovenaan de beschrijving van zijn oude gratis video's,** ook de video van 251.537 (GEZIEN, RSS-beschrijving). In okt 2026 een video over Pro zelf: 2.023 weergaven (GEZIEN). De gratis video's bleven dus de motor; de Pro-video zelf deed weinig.
6. **Free en Pro op één pagina, met vijf prijzen:** Free $0 (op Superhive $1, "because Superhive requires a minimum"), Pro Personal $29, Studio 5 plaatsen $129, Studio+ 15 plaatsen $349, Unlimited $899, alle met "Lifetime updates" (GEZIEN, Gumroad en Superhive). Gumroad telt 24.960 "sales", vooral gratis downloads, en 180 beoordelingen met 4,9; Superhive 900+ (GEZIEN). Hoeveel daarvan Pro is, zegt geen bron.
7. **Eerlijk over de grens tussen gratis en betaald.** De gratis versie: "No trial period, no watermark, no buttons that ask you to upgrade." Pro begint met waarom: "Pro is what you reach for when the take was nearly right". Plus een blok "Is AutoCam right for your shot? ... Better you know now than after you buy" met wat Pro nog niet kan (GEZIEN, Gumroad).
8. **Naam in Blender:** in aug 2026 hernoemd naar "AutoCam Free" in de lijst van add-ons, "matching how the Pro edition already read" (GEZIEN, changelog 2.1.1). Wie de gratis naam ziet, weet dat er meer is, zonder knop of reclame in Blender.

### 3 lessen
1. **De gratis versie in Blender is geen verkoopmotor: mediaan ±1 betaler per 550 downloads, en de helft van de paren met 10.000+ downloads haalt geen 100 verkopen.** Click Joints heeft 170 downloads; volgens deze maat levert dat 0 tot 3 kopers van Pro (GOK). Voor 100 kopers zou je bij 0,2% ±50.000 gratis downloads nodig hebben, bij de beste gevallen (2%) ±5.000. De motor moet dus ergens anders zitten. (Bij les 6 en 4.)
2. **Wat wel werkte bij AutoCam: één sterke video van het gratis product, op een kanaal dat er al was, en daarna de betaalde versie bovenaan die oude video zetten.** De Pro-video zelf haalde 2.023 weergaven, de gratis video 251.537. (Bij les 3 en 4.)
3. **Een betaalde versie met echte extra's naast een gratis versie onder de naam "Lite" of "Free" doet het beter dan "betaal om te steunen"** (Audio Trigger Lite ±8%, Driver Espresso Lite, AutoCam; steunen 0,1 tot 0,4%). Zeg in de gratis versie niets over upgraden, maar laat de naam het werk doen, en zeg op de betaalde pagina eerlijk wat Pro nog niet kan. (Bij les 7 en les 1: AutoCam heeft vijf prijzen, van $0 tot $899.)

### Wat Dortus anders doet
- Wij hebben Free en Pro op twee plekken met twee namen (Click Joints, Click Joints Pro). AutoCam heeft één productpagina met Free als eerste keuze, zodat ook wie gratis neemt in de winkel als koper telt (en kan reviewen; zie verhaal 8 bij Split 3D Print).
- Wij hebben nog geen video van het gratis product met veel weergaven; Chris begint di 17 nov met korte filmpjes. Bij AutoCam deed één video van 4 minuten met een duidelijke belofte ("Instantly Animate Cameras") het werk, niet de korte filmpjes.
- Wij hebben alleen Personal $12 en Studio $45; AutoCam gaat tot 15 plaatsen en onbeperkt.

### Voorstel voor Dortus deze week
**Chris (met de hoofdchat): maak één uitlegvideo van 2 tot 4 minuten over het gratis Click Joints op @Dortusapps, met een belofte in de titel zoals AutoCam ("Print-ready joints in Blender in one click", echte beelden), en zet de link naar Pro bovenaan de beschrijving, zoals RenderRides deed.** Waarom: de gratis versie in Blender levert volgens 50 paren maar ±1 betaler per 550 downloads; bij AutoCam kwam het bereik van één video, en Pro kreeg zijn plek in de beschrijving van die video. Meetlat: weergaven en Gumroad-verkopen 14 dagen na plaatsing. Plaatsen pas na ja van Thijs (via `organisatie/goedkeuren.md`).
Klein erbij voor **Bram**, ter overweging en niet als taak: zes gratis pagina's op extensions.blender.org linken nu naar hun betaalde versie, en AutoCam heet in Blender "AutoCam Free". Of een naam als "Click Joints Free" of één regel "support development" binnen regel 6 valt, is aan Bram; ik stel niet voor de regel op te rekken.

---

## 18. Hoe leren mensen poseerbare en flexi-prints maken? 89 uitlegvideo's op YouTube naar programma geteld: het nieuwe jaar is van webtools zonder 3D-modelleren, en sinds gisteren zet een gratis webtool (Model Splitter) kogelgewrichten in elk model

Onderzocht 16 nov 2026, run 18 (na de top 3). Waarom: in verhaal 15 bleef open welke software de flexi-ontwerpers gebruiken (koopt die groep wel een Blender-add-on?). Interviews met Flexi Factory, MatMire en Cinderwing3D vond ik niet (drie zoekopdrachten, niets bruikbaars), en hun YouTube-beschrijvingen noemen geen programma, alleen Patreon, MyMiniFactory Tribes, Thangs en Cults3D (GEZIEN, RSS van beide kanalen, 15 video's elk). Dus de vraag andersom gesteld: met welk programma leren nieuwe makers het, volgens wat ze op YouTube zoeken en bekijken? Daarbij vond ik een nieuwe concurrent van gisteren.

Ook geprobeerd en niet gedaan: YouTube-reacties lezen voor pro-lijp. Dat kan alleen via de interne API van YouTube of de officiële API met een sleutel; de eerste mag niet (mijn poging werd tegengehouden en ik heb hem niet omzeild), een sleutel is werk voor Thijs en dit gat is hem dat niet waard. Het gat in pro-lijp blijft dus open; Reddit, BlenderArtists en Printables dekken het grootste deel.

### Bronnen (alle met curl, GEZIEN 16 nov 2026 ±18:52 tot 19:00 UTC)
- YouTube-zoekpagina's (gewone HTML, de lijst in de pagina) voor 8 zoektermen: "how to design flexi 3d print", "how to make articulated 3d print", "how to design print in place articulated figure", "flexi model tutorial", "how to make your own flexi stl", "articulated dragon 3d print tutorial", "ball joint action figure 3d print design tutorial", "how to make poseable figure 3d print". Samen 89 verschillende video's. Tabel: `platformen/succes/data/youtube-figuren-uitleg-2026-11-16.tsv` (id, kanaal, titel, weergaven, leeftijd, programma in de titel).
- Openbare RSS van Flexi Factory (https://www.youtube.com/feeds/videos.xml?channel_id=UCpV00uonUYokxB5w8sQeaLw), MatMire Makes (channel_id=UCxsWnsAdUGRnpOH3BkrHAFg) en Model Splitter (channel_id=UCo1dZdm6EqBGFFhQ9eJdEzg).
- Model Splitter zelf: https://modelsplitter.com en de video https://www.youtube.com/watch?v=itFpGRqcFrU ("Why Every 3D Printer Needs Model Splitter") en de video van 16 nov "Ball and socket joints: make any 3D print posable in Model Splitter" (16 nov 2026, 127 weergaven bij het lezen).

### Cijfers
Ik telde alleen uitlegvideo's (hoe maak je het), 62 van de 89, en keek welk programma in de titel staat. Leeftijd zoals YouTube die toont ("1 year ago" kan 12 tot 23 maanden zijn).

| Programma in de titel | Ouder dan 1 jaar | Laatste 12 maanden | Weergaven laatste 12 maanden |
|---|---|---|---|
| Webtool of AI, zonder 3D-modelleren (Bambu PrintU, Text to Flexi, STL Buddy, Layerling, Audja, Model Splitter, AI-figuur) | 0 | **10** | 128 tot 31.046, samen ±92K |
| Blender | 4 (waaronder 700K en 143K) | 4 | 560 tot 38.222 |
| Tinkercad | 9 | 4 | 459 tot 10.326 |
| Nomad Sculpt | 7 | 0 | |
| Fusion of Onshape | 1 | 1 | |
| Geen programma in de titel | 28 | (meestal oud) | |

(GEZIEN, eigen telling uit de zoekpagina's. De zoekvolgorde van YouTube kiest mee, dus dit is een beeld, geen meting van de hele markt.)

Model Splitter (GEZIEN op de site en in de RSS):
- Gratis openbare beta in de browser ("all current tools unlocked for testing"), het model blijft op je eigen computer. Op de site staat ook "Pro and the launch draw" en "Follow on Kickstarter": er komt dus een betaalde versie.
- Sinds 16 nov: **"Ball joint cut"**. Je tekent een naad, drukt op de knop, en krijgt een kogel met een kruissleuf (veert in de kom) en een ronde kom. "There are no settings to get right: the ball is sized from the seam, and the fit was worked out on test prints." In de video krijgt een alien kogels in polsen, elleboog en schouder, geprint in PLA op een Bambu A1, zonder lijm.
- Verder: Push-fit en Inlay, een Pose-gereedschap (30 okt), mallen, en een video "AI Model to Printed Figure: Tripo + ModelSplitter" (1 nov). Ongeveer 15 video's sinds half oktober, 66 tot 1.292 weergaven, kanaal 806 abonnees.
- Wat ik niet zag: een scharnier met eindstop, bereik in graden, of iets wat een rig leest. Alleen kogel, push-fit en inlay als verbinding.

### Wat ze in welke volgorde deden (Model Splitter)
1. Een gratis splitter in de browser voor wie een te groot model wil printen (oktober).
2. Elke paar dagen een korte uitlegvideo per gereedschap, met de functie in de titel ("Paint to cut", "Band and Rope cuts", "Cut, Push-fit or Inlay?").
3. De AI-weg erbij (Tripo, foto of prompt naar model) met een affiliate-link.
4. Pose-gereedschap, daarna gewrichten. Betalen pas later, via Pro en Kickstarter.

### 3 lessen
1. **Het nieuwe publiek leert figuren maken zonder 3D-programma.** In de laatste 12 maanden is de grootste groep uitlegvideo's over een webtool of AI (10), meer dan Blender en Tinkercad samen (8); een jaar eerder was het Tinkercad en Nomad, en geen enkele webtool. Dat past bij verhaal 13 (Nikko: "zonder Blender") en verhaal 14 (PrintPal). Voor wie een AI-figuur wil laten bewegen is een knop in de browser de makkelijkste weg.
2. **De gratis weg wordt beter, dus het verschil moet in wat gratis niet kan.** Model Splitter doet nu gratis wat de gratis Click Joints ook doet (kogel met speling), zonder Blender. Wat wij hebben en zij niet (zover ik kon zien): scharnier met eindstop, bereik in graden zichtbaar vóór het printen, waarschuwing als iets botst, en in 1.1 gewrichten uit de rig. Dat is hoofdles 7 opnieuw.
3. **Blender houdt de grote, oude uitlegvideo's (700K, 143K), en Blender-makers zijn de makers die al figuren ontwerpen.** Onze koper is dus de Blender-gebruiker die zelf figuren maakt, niet de printer die een AI-model wil laten bewegen. Die tweede groep gaat naar de browser.

### Wat doen wij anders
Onze filmpjes en teksten beginnen nu bij "ball joints". Dat is precies wat sinds gisteren gratis in de browser kan. Het scharnier dat stopt, en het bereik dat je ziet, staat nog niet vooraan.

### Voorstel voor Dortus deze week
**Ruben zet Model Splitter in de concurrentiecheck van 1.1 (naast NB Figure Joints en Action Joint Generator), en Chris zet in de eerste Pro-teksten en de eerste Short het scharnier met eindstop vooraan, niet de kogel.** Concreet: de Short uit de top 3 van vandaag ("How to make a hinge that stops at 90° #3dprinting") gaat vóór elke kogel-Short. En de waarom-zin op Gumroad en Superhive wordt iets als "Hinges that stop where you want and range you can see before you print, inside Blender. Free tools give you a ball; Pro gives you a figure that holds its pose." (Ruben zegt "klopt" of past aan.) Kost een half uur, geen geld. Ik volg Model Splitter: als hun Pro of Kickstarter verschijnt, schrijf ik prijs en functies erbij.

### Eerlijk: wat ik niet weet
- Welke software Flexi Factory, MatMire en Cinderwing3D echt gebruiken, blijft open. Alleen McGybeer zegt Blender (verhaal 15).
- Of Model Splitter veel gebruikers heeft. Hun video's halen honderden weergaven, en ze sturen "anonymous counts" maar maken die niet openbaar.
- De telling hangt aan titels; een Blender-video zonder "Blender" in de titel telt als "geen programma".

---

## 17. Drie kleine bouwers van gewrichtengereedschap uit 2026 (BOSSposes, NunnBreakable, Granite Studio): elf goedkope add-ons of één tool op Patreon levert weinig op, en NB Figure Joints doet bijna wat Rig to Figure belooft

Onderzocht 16 nov 2026, run 17. Waarom dit verhaal: in pro-lijp (C) stond een mogelijke concurrent die ik niet had bekeken ("Blender Auto Joints", kanaal Nunn Breakable). Bij het uitzoeken vond ik drie kleine makers die dit jaar een gewrichtengereedschap voor figuren uitbrachten. Het zijn geen winnaars, en juist daarom nuttig: wat doen ze anders dan CatPin en Cleave, en wat betekent het voor Click Joints Pro en 1.1 Rig to Figure? Geen cursusverkopers; alles hieronder komt van winkelpagina's, YouTube-feeds en Graphtreon.

### Bronnen (alle met curl, GEZIEN 16 nov 2026 ±17:50 tot 18:20 UTC)
- Superhive: https://superhivemarket.com/products/articulator---easy-figure-joint-generator , de ratings-pagina daarvan, en de winkel https://superhivemarket.com/creators/bossposes3d plus de 11 productpagina's.
- YouTube-feed (openbare RSS, met volledige beschrijving, weergaven en duimpjes) van Nunn Breakable: https://www.youtube.com/feeds/videos.xml?channel_id=UCe2sVvbraJFvQcc6I4g0_Dw en van Granite Studio: https://www.youtube.com/feeds/videos.xml?channel_id=UCQSAX6dfPQkgy63_G4kkK-w . Video's: https://www.youtube.com/watch?v=IBObASfadOo , https://www.youtube.com/watch?v=_mPwesbueMM , https://www.youtube.com/watch?v=wXbZm7Q_NcQ , https://www.youtube.com/watch?v=-VsZXeIVsGg
- Thangs: https://thangs.com/designer/Granite%20Studio en de productpagina van de "Flexi articulated knee and leg joint tool".
- Graphtreon (openbare lijst van Patreon-makers in 3D Printing): https://graphtreon.com/api/creators/3d-printing
- Niet gelukt: YouTube-kijkpagina's (doorgestuurd naar een Google-controle) en Patreon-pagina's (403). Prijs van NB Figure Joints en wat er precies in zit heb ik dus niet gezien.

### De drie, naast elkaar (GEZIEN)
| Maker | Gereedschap | Sinds | Waar en prijs | Wat ik zag aan vraag |
|---|---|---|---|---|
| BOSSposes (add-onmaker, animator, VFX) | Articulator, add-on: kogel met kom, scharnier met pen, pen | ±aug 2026 ("3 months ago") | Superhive, **$1** | 30+ verkopen, 2 ratings (5 en 3 sterren) |
| Nunn Breakable (David, kanaal met grappen en tekentijdlapses sinds ±2020, sinds juni 2026 printbare figuren) | NB Figure Joints, add-on: gewrichten plaatsen en kogels, kommen, scharnieren en pennen maken, figuur in delen | aangekondigd 28 sep, uitleg 16 okt 2026 | alleen via zijn Patreon (prijs niet gezien) | Patreon 8 leden (Graphtreon); uitlegvideo 596 weergaven, 12 duimpjes; snelle video 102; aankondiging 37 en Short 97 |
| Granite Studio (STL-ontwerper, vazen en flexi-diertjes) | Flexi Articulator Tool: een .blend met een kniptool voor kogelgewrichten, werkt met een Boolean, geen add-on | 23 feb 2026; knie- en beentool 30 mrt | Thangs $5 (knie- en beentool), en via Patreon | knie-tool 3 ratings op Thangs; video 560 en 33 weergaven; Patreon 0 leden (Graphtreon) |

### BOSSposes: elf add-ons in vier jaar (GEZIEN, Superhive-winkel 16 nov)
| Add-on | Prijs | Verkopen | Online |
|---|---|---|---|
| Fixamo | $15 | 100+ | bijna 4 jaar |
| Fixamo 2 | $10 | 100+ | ruim 3 jaar |
| 3D Print Checker (Toolbox 4) | $9 | 70+ | bijna 2 jaar |
| Articulator | $1 | 30+ | 3 maanden |
| Pose Warehouse | $10 | 30+ | ruim 1 jaar |
| Model Kit Maker | $8 | 20+ | bijna 2 jaar |
| PRINTcipal | $6 | 20+ | bijna 4 jaar |
| ALCHEMY360 | $30 | 10+ | 4 maanden |
| Test Pilot | $15 | 10+ | ruim 2 jaar |
| Afterblend | $30 | geen getal | ruim 1 jaar |
| Happy Tab | $3 | geen getal | bijna 4 jaar |

Samen minstens 390 verkopen in vier jaar. Bruto omzet als ondergrens, GOK want Superhive rondt naar beneden af en kortingen weet ik niet: ±$4.200 in vier jaar. Ter vergelijking: CatPin haalde met één product 400+ in een paar maanden (verhaal 3), Split 3D Print 400+ in ±4 maanden voor $22 (verhaal 8). Vier van zijn add-ons gaan over printen (Checker, Model Kit Maker, PRINTcipal, Articulator), en geen daarvan kwam boven 70+.

### Wat de kopers van Articulator zeggen (GEZIEN, de 2 ratings, al kort in verhaal 9)
- "I just love it ... would like to see more joints but it works ok" (23 dagen geleden).
- "saves you some time but it should have more types of joints, not just ball, hinge and peg joints" (±2 maanden geleden, 3 sterren).
Zelfs voor $1 vragen beide kopers om meer soorten gewrichten. De pagina belooft "guaranteed to fit", zonder te zeggen voor welke printer of speling.

### NB Figure Joints: wat het belooft (DERDEN, zijn eigen videobeschrijvingen)
- "transform static 3D characters into articulated, 3D-printable action figures", "position and customize joints", "generate ball joints, sockets, hinges, and pins", "separate body parts", "measure limbs and adjust joint sizes", "fine-tune joint clearances".
- Het werkt per plek: "Shoulders, elbows, wrists, neck, waist, hips, knees, and ankles". De snelle video toont "Custom joint placement" en "Automatic articulation generation", en noemt het "1 hour of work".
- Wat ik NIET zag: of het een rig (skelet) leest, of het bereik in graden of een eindstop heeft, en of het een test op botsen doet. "Auto" lijkt te gaan over het maken van de vormen na het plaatsen, niet over plaatsen uit een rig. GOK, want ik kon de video zelf niet kijken.
- In de beschrijving van de snelle video staat nog letterlijk "Patreon: [Your Patreon Link]", een sjabloon dat niet is ingevuld.

### Wat ze in welke volgorde deden
1. **BOSSposes:** sinds ±2022 steeds een nieuwe kleine add-on op Superhive, prijs $1 tot $30, elk in een andere hoek (rigging, VFX, printen, CAD). Geen tweede versie van een loper, behalve Fixamo 2.
2. **Nunn Breakable:** een bestaand kanaal (oude video's 10.000 tot 17.000 weergaven, grappen en "life hacks"), in 2026 omgezet naar printbare figuren met Shorts (1.065 en 1.233 weergaven voor een print van een horrorclown), juni 2026 een Patreon voor modellen ($3 per stuk of lidmaatschap, eigen tekst), toen zelf een gewrichtentool gebouwd, eerst een "sneak peek", daarna een uitleg van 47 minuten. Verkoop via dezelfde Patreon.
3. **Granite Studio:** STL-ontwerper op Thangs en Patreon, maakte voor zijn eigen flexi-dieren een kniptool en verkoopt die als bestand voor een paar dollar, met dezelfde YouTube-film als voor een vaas.

### 3 lessen
1. **Eén product dat steeds beter wordt verslaat elf losse.** BOSSposes is een harde werker met elf add-ons, maar geen enkele haalt de 400+ van CatPin of Split 3D Print, en de printadd-ons blijven onder 70+. CatPin en Split hebben één product, meerdere prijzen en elke week een update. Dit is een tegenvoorbeeld voor de kandidaat-les "veel schoten" (Kambari, PrintPal): veel schoten helpt alleen als je daarna doorgaat met de soort die raak is, en die stap zette BOSSposes niet.
2. **Een gereedschap op je eigen Patreon of in een bestand verkoopt niet als het publiek er niet zit.** NunnBreakable heeft 8 Patreon-leden, Granite 0; hun gereedschapsvideo's halen 33 tot 596 weergaven. De kopers zoeken op Superhive en Gumroad (verhaal 16: daar staan CatPin met 84 ratings en Cleave). Zijn oude publiek (grappen, tekenen) koopt geen gewrichtentool. Past bij hoofdles 4 (anderen maken het bereik, niet je eigen kanaal) en bij verhaal 16.
3. **De hoek loopt vol, maar alleen met gewrichten maken, niet met nakijken.** In 2026 kwamen er bij ons onderzoek al bij: Articulator (aug), Action Joint Generator (verhaal 16), NB Figure Joints (okt), Granite (feb, mrt), naast Cleave, CatPin en Cut Flex. Geen van de drie hier noemt bereik in graden, een eindstop of een botstest. Wat kopers zelf missen is "more types of joints".

### Voorstel voor Dortus deze week
**Ruben (Pro 1.1 Rig to Figure): zet NB Figure Joints in de concurrentiecheck van 1.1 en maak het verschil zichtbaar in één zin op de pagina.** NB Figure Joints plaatst ook gewrichten op schouders, ellebogen, polsen, nek, middel, heupen, knieën en enkels; dat is dichtbij wat Rig to Figure belooft. Het verschil dat ik kon zien: Rig to Figure leest de rig die je al hebt (geen gewricht met de hand plaatsen) en geeft per gewricht bereik en eindstop. Als dat klopt, zet Chris op Superhive en Gumroad de zin "Reads your rig: joints with end stops and range in degrees, placed where your bones are", en noemt Ruben in de changelog welke gewrichtsoorten er zijn, omdat dat het enige is waar kopers van Articulator om vragen. Kosten: een half uur, geen geld. Ruben kijkt eerst zelf naar de uitlegvideo (47 minuten, https://www.youtube.com/watch?v=IBObASfadOo), want ik kon die niet openen.

---

## 16. Gumroad, de winkel waar Click Joints Pro sinds 16 nov staat: wat CatPin daar deed, wat Discover vraagt, en twee nieuwe concurrenten met 0 reviews

Waarom dit verhaal: Click Joints Pro staat sinds vandaag live op Gumroad ($12, besluit 16 nov 15:02) en de Superhive-keuring loopt nog. CatPin heeft op Gumroad 84 reviews tegen 4 op Superhive (verhaal 3). Vraag: waar kwamen die kopers vandaan, en wat moet Pro doen om daar gevonden te worden?

### Bronnen (alle met curl, GEZIEN 16 nov 2026 ±15:00 tot 15:30 UTC)
- Gumroad Help, "Gumroad Discover": https://gumroad.com/help/article/79-gumroad-discover
- Gumroad Help, "Gumroad's fees": https://gumroad.com/help/article/66-gumroads-fees
- Gumroad Help, "Product ratings and reviews": https://gumroad.com/help/article/222-product-ratings-on-gumroad en "Rate and review your purchase": https://gumroad.com/help/article/344-rate-and-review-your-purchase
- Gumroad Help, "Affiliates on Gumroad": https://gumroad.com/help/article/333-affiliates-on-gumroad
- De openbare zoek-API van Discover: `https://gumroad.com/products/search?query=...` (9 zoektermen, 1.553 producten; uittreksel van de 66 Blender-producten over printen, gewrichten en splitsen: `platformen/succes/data/gumroad-discover-print-joints-2026-11-16.tsv`)
- De openbare reviews per product, met datum: `https://gumroad.com/product_reviews?product_id=...` (8 producten, 137 geschreven reviews zonder namen: `platformen/succes/data/gumroad-reviews-print-addons-2026-11-16.tsv`)
- Productpagina's: https://alexsokol.gumroad.com/l/catpin , https://teenturtlecustoms.gumroad.com/l/ajgenerator , https://ayhancelik.gumroad.com/l/slicerjointpro
- Gumroad toont geen verkoopteller (`sales_count` is leeg op elke pagina die ik las). Aantallen kopers zijn dus GOK.

### Wat Gumroad zelf zegt (DERDEN, hun helppagina's)
- **Discover is niet meteen open.** Een account komt pas op Discover na "a balance of at least $100 USD from enough genuine sales", plus een keuring door hun risicoteam die "on average 3 weeks after you pass the $100 threshold" duurt. Daarna staat een product er pas als het minstens 1 verkoop heeft, een categorie heeft en ratings aan staan. Tags helpen bij het zoeken.
- **Discover kost 30%.** Verkopen via de eigen link: 10% + $0,50 plus kaartkosten (2,9% + $0,30). Verkopen via Discover: vast 30%. Producten op Discover doen automatisch mee met Gumroad Affiliates (10% voor wie een link deelt, cookie 7 dagen).
- **Gumroad vraagt elke koper om een review.** "We automatically send a reminder email to customers who have yet to leave a review 5 days after their purchase." Een ster zonder tekst telt al als review. Dat verklaart waarom Gumroad veel meer reviews per koper geeft dan Superhive.

Rekensom voor Pro, GOK: $12 min ±$2,35 kosten is ±$9,65 per verkoop, dus ±11 verkopen tot $100 (als Gumroad netto telt; bruto zijn het er 9). Daarna ±3 weken keuring. Komen die 11 voor eind november, dan staat Pro op zijn vroegst half december op Discover.

### CatPin op Gumroad, per maand (GEZIEN, 51 geschreven reviews van 84 ratings)
| Maand 2026 | Geschreven reviews |
|---|---|
| juli (vanaf 29 jul) | 2 |
| augustus | 13 |
| september | 24 |
| oktober | 10 |
| november (tot 16) | 2 |

- De eerste Gumroad-review (29 jul) is ouder dan zijn Superhive-pagina (±half augustus, verhaal 3). Gumroad kwam dus eerst.
- De piek ligt in september, **vóór** de vakbladen (80 Level 5 okt, Digital Production 9 okt). Na de pers zakte het juist. Wat september bracht zegt hij nergens. Mijn GOK: de toelating tot Discover, want $100 haalde hij in juli of augustus en de keuring duurt ±3 weken; daarnaast zijn YouTube-tutorial. Bewijs heb ik niet.
- 44 van de 51 geschreven reviews zijn 5 sterren, 6 zijn 4 sterren, 1 is 1 ster ("I don't apply the discount!!!", een kortingscode die niet werkte).
- **Hij antwoordt op 41 van de 51.** Kopers noemen de hulp vaak zelf: "excellent support via Telegram", "Aftercare is A+++", "Dev is super helpful".
- **Wat de 4-sterren vragen is uitleg, geen functies:** "the YouTube instruction video is too fast to see what's going on", "seria de utilidad que emitieras un tutorial indicando para que sirve cada una de las opciones", "it would benefit from proper documentation". Drie van de zes.
- **De koper kent Blender vaak nauwelijks:** "I almost gave up on Blender until this Add-On", "even though I'm not all that familiar with Blender", en in het Russisch: blender eergisteren voor het eerst gezien, vandaag al een figuur gesneden. Kopers verdienen er ook mee: "make my life and business so much easier".
- **Eén op vijf schrijft niet in het Engels** (10 van 51: Spaans 4, Portugees 2, Italiaans, Russisch, Turks, Frans; eigen telling).

Ter vergelijking (GEZIEN): Split 3D Print 22 ratings op Gumroad (gratis trede) tegen 400+ verkopen op Superhive; Cleave 2 ratings, eerste op 1 nov 2026.

### De lege plank: wat een koper vindt als hij zoekt (GEZIEN, Discover-zoekresultaten)
| Zoekterm | Resultaten | Bovenaan |
|---|---|---|
| ball joints blender | 4 | Cleave (2), Action Joint Generator (0), twee kitbash-pakketten |
| ball joint | 78 | vooral VRChat-avatars; Cleave staat eerste |
| articulated figure | 83 | CatPin (84), actiefiguren als STL |
| 3d print joints | 34 | CatPin, Cleave, SlicerJoint Pro (0) |
| blender addon 3d printing | 47 | Split 3D Print (22), Cleave, Resin2FDM Lite |
| flexi blender | 3 | geen enkel gewrichtengereedschap |

Twee concurrenten die wij nog niet kenden of nog niet goed kenden, allebei met **0 ratings**, terwijl Gumroad elke koper na 5 dagen om een review vraagt:
- **Action Joint Generator** (teenturtle.customs, $12, nieuw voor ons): "This Generator let's you create printready joints for figures of any kind", kogel, dumbbell en ballpeg met socket, maat in mm, "FDM / Resin Fits with different strength (tight, standard, loose)", hoekgewrichten "(Mafex Style)" en presets voor de schalen van Legends, Legions en Mafex (actiefiguren). Updates op 25 aug, 6 sep en 1 nov 2026. Hij maakt losse gewrichten om een gebroken gewricht te vervangen, niet in je eigen model met eindstop. Zelfde prijs als Pro.
- **SlicerJoint Pro** ($20): snijden, pennen, magneten, "Toy Articulation", een "Lock V4"-gewrichtsjabloon. Staat al in `platformen/blender-2/rig-to-figure.md` (8 nov ook 0).
Beide staan op Discover (ze komen in de zoekresultaten), en toch geen enkele rating. Op Discover staan is dus geen motor; het zet je alleen op een plank waar weinig mensen langs lopen (GOK op basis van 0 ratings bij herinneringsmails, verkopen zijn niet te zien).

### 3 lessen
1. **Gumroad geeft geen startduw, het beloont wie al verkoopt.** Discover gaat pas open na $100 echte verkopen en ±3 weken keuring, en kost dan 30%. De eerste ±11 kopers van Pro moeten van buiten komen: makersmails, dortus.com, filmpjes, de Website-link van de gratis versie. Twee concurrenten die er wel op staan zonder motor van buiten hebben 0 ratings.
2. **Op Gumroad stapelen reviews vanzelf, als je antwoordt.** Gumroad mailt elke koper na 5 dagen; CatPin kreeg zo 84 ratings tegen 4 op Superhive, en antwoordde op 41 van 51. Die reviews zijn daarna zijn bewijs op de zoekpagina (hij staat eerste bij "articulated figure" en "3d print joints"). Herinneringen aan laten en elke review beantwoorden is gratis.
3. **De koper wil uitleg, en is vaak geen Blender-gebruiker.** De enige kritiek bij CatPin gaat over een te snelle video en geen uitleg per knop; veel kopers zagen Blender net voor het eerst, een op vijf schrijft in een andere taal. Een rustige uitlegvideo en een korte uitleg per knop zijn het werk dat reviews oplevert. Past bij hoofdles 2 en 3 en de kandidaat over installeren.

### Eerlijk: wat ik niet weet
- Hoeveel kopers bij 84 ratings horen (geen teller). Waarom september piekte (GOK Discover, niet bewezen).
- Hoe Discover zoekresultaten ordent. CatPin staat bovenaan bij veel termen, maar of dat door ratings, verkopen of de tekst komt zegt Gumroad niet.
- Of Click Joints Pro al een categorie en tags heeft. De pagina toont `tags_data: []`, maar dat veld is ook leeg bij producten die wel op Discover staan, dus dat zegt niets.

### Wat doen wij anders
We rekenen stil op Gumroad als tweede winkel, maar Gumroad brengt ons de eerste weken niemand. En voor Pro 1.1 (figuurpresets) is er een concurrent die precies dat al doet voor actiefiguren, voor dezelfde $12, met 0 reviews: de vraag naar losse gewrichten met presets is daar dus niet bewezen.

### Voorstel voor Dortus deze week
**Hoofdchat (beheert de Gumroad-pagina): controleer in het Share-tabblad van Click Joints Pro dat er een categorie staat, dat ratings en reviewherinneringen aan staan, en zet zes tags zoals kopers zoeken: "blender addon", "3d printing", "ball joints", "articulated", "action figure", "print in place".** Zet in je telling een meetlat: verkoop 11 op Gumroad is het begin van de Discover-keuring (±3 weken); tot dan komt elke koper via onze eigen links. Tweede, voor **Ruben**: neem Action Joint Generator op in de concurrentiecheck van Pro 1.1. Zij hebben al presets voor Legends, Legions en Mafex en pasvormen tight, standard en loose; ons verschil moet het lezen van de rig en de eindstop zijn, niet de presets. Derde, klein, voor **Chris**: de eerste uitlegvideo van Pro langzaam, met elke knop één keer in beeld, want dat is precies wat CatPin-kopers missen.

---

## 15. De kopers van Click Joints Pro: flexi-ontwerpers op Patreon (Flexi Factory, MatMire Makes, Cinderwing3D, McGybeer, Valeria & Mattia), hoeveel het er zijn en hoe ze werken

Waarom dit verhaal: tot nu keek ik naar makers van gereedschap (de concurrent). Dit keer naar de koper: wie ontwerpt beweegbare printfiguren voor geld, hoeveel zijn het er, en hoe maken ze hun gewrichten.

### Bronnen (alle met curl, GEZIEN 16 nov 2026 ±14:00 UTC)
- Graphtreon, de openbare lijst van alle Patreon-makers in de soort 3D Printing, via de eigen databron van de pagina: https://graphtreon.com/api/creators/3d-printing (3155 makers). Mijn uittreksel: `platformen/succes/data/patreon-3dprint-flexi-2026-11-16.tsv` (de 72 makers met flexi, articulated, print-in-place of jointed in naam of beschrijving).
- Graphtreon per maker: https://graphtreon.com/creator/FlexiFactory , https://graphtreon.com/creator/matmire_makes , https://graphtreon.com/creator/cinderwing3d , https://graphtreon.com/creator/SEREV3d , en de top 50: https://graphtreon.com/top-patreon-creators/3d-printing
- Interview met Javier Rodríguez (McGybeer, de beweegbare draak), Snapmaker-blog, 24 feb 2022: https://www.snapmaker.com/blog/3d-printed-articulated-dragon-model-designer-javier-rodriguez/
- Thangs-blog over Valeria en Mattia (Cute Flexi Maker), 2 jul 2026: https://thangs.com/resources/blog/behind-the-designs-valeria-momo-of-cute-flexi-maker , en hun productpagina op Thangs: https://thangs.com/m/1546372
- Niet te lezen vanuit de cloud: Patreon zelf, Cults3D, MakerWorld en Printables (403). De ledenaantallen komen dus van Graphtreon (DERDEN, zij lezen Patreon dagelijks), de omzet is hun schatting (DERDEN, ruwe band).

### Cijfers
| Maker | Betaalde leden Patreon | Schatting omzet per maand (Graphtreon) | Op Patreon sinds | Plaats in 3D Printing |
|---|---|---|---|---|
| Flexi Factory ("Creating Flexi models") | 7.306 | $21K tot $63K | mrt 2022 | 2 |
| Cinderwing3D (beweegbare draken) | 6.345 | $19K tot $55K | jan 2022 | 5 |
| MatMire Makes ("Flexi Articulated STL Models") | 5.053 | $15K tot $44K | jun 2022 | 7 |
| Valeria Momo & Mattia 3D (Cute Flexi) | 1.408 | niet gelezen | | 25 |
| SEREV3d ("flexi designs, fidgets") | 1.085 | $3K tot $9K | sep 2024 | 35 |

(GEZIEN op de pagina's per maker; de top 50 en de databron verschillen een paar procent, die worden niet op hetzelfde moment bijgewerkt.)

De hele soort, uit de databron (GEZIEN, eigen telling):
- 2306 makers met minstens 1 betaald lid, samen ±240.000 betaalde leden.
- **72 makers noemen flexi of articulated zelf in naam of beschrijving, samen 18.854 betaalde leden** (±8% van de soort). Dat is een ondergrens: Cinderwing3D en Valeria & Mattia zeggen het niet in hun regel en tellen niet mee.
- Van de 40 makers met 1000+ betaalde leden doen er minstens 5 vooral beweegbare figuren (Flexi Factory, Cinderwing3D, MatMire, Valeria & Mattia, SEREV3d).
- Nieuwkomers per jaar in de flexi-groep: 2022: 4 (mediaan 2.639 leden), 2023: 4 (mediaan 195), 2024: 23 (mediaan 34), 2025: 25 (mediaan 8), 2026 tot nu: 15 (mediaan 11). **Er komen er dus elk jaar ±20 tot 25 bij, en de meesten blijven klein.** Wel haalt 17% van de flexi-nieuwkomers sinds 2024 de 100 betaalde leden (11 van 63), tegen ±8% van alle 3D-printmakers die toen begonnen (138 van 1723). Flexi verkoopt dus beter dan gemiddeld, maar de vroege drie houden het grootste deel.

### Hoe ze werken (wat de bronnen zelf zeggen)
- **McGybeer (Javier Rodríguez, elektronica-ingenieur, Valencia):** "Usually, I do the articulations first, as they are the key and the rest of the model depends on them. I model in Blender, but sometimes I use other CAD software for quick tests and concepts" (GEZIEN, interview). Voor de draak: "I designed a bunch of prototypes, tested them, modified them, and went back to the test." Hij stopte met zijn baan door de draak, want hij was 2 tot 3 uur per dag kwijt aan berichten beantwoorden (EIGEN OPGAVE).
- **Valeria en Mattia:** kopers vroegen steeds om varianten (andere dieren, kerstmutsen, namen); ze waren "spending more time creating variations of existing designs than creating entirely new ones" en bouwden daarom in ±6 maanden een eigen webgereedschap, Cute Flexi Maker (live 25 feb 2026). Elk model daaruit is "designed to print without supports" (GEZIEN, Thangs-blog). Ze verkopen het niet los: een model plus 5 downloads uit de webtool kost $5,87 eenmalig, lidmaatschap vanaf $9,99, en een commerciële licentie (prints mogen verkopen) loopt via Patreon, Thangs en MyMiniFactory (GEZIEN, productpagina; welke trede $39 is: GOK, waarschijnlijk die licentie).
- Een pijnpunt dat ik in de zoekresultaten zag maar niet kon openen: een gratis "Flow Calibration Tool ... Fix Fused Joints On Flexi Prints" op Printables en Thangs. Dat gewrichten vastsmelten is dus een bekend probleem bij printers van flexi (titel GEZIEN, aantallen niet).

### 3 lessen
1. **De koper bestaat en groeit: ±70 tot 80 flexi-ontwerpers op Patreon alleen, ±20 tot 25 nieuwe per jaar.** Dat zijn mensen die van hun gewrichten leven. Click Joints Pro hoeft geen hobbyist te overtuigen die één keer een figuur maakt; de kleine nieuwkomers (mediaan 8 tot 34 leden) zijn precies wie tijd wil winnen en $20 tot $45 kan uitgeven (GOK, geen koper gesproken).
2. **De beste ontwerper begint bij het gewricht, niet bij het figuur.** McGybeer maakt eerst de gewrichten, test ze in prints, en bouwt het dier eromheen, in Blender. Click Joints Pro doet het omgekeerde: een af figuur krijgt gewrichten. Voor AI-figuren en hobbyisten klopt onze volgorde; voor de professionele ontwerper is de waarde vooral dat hij snel een gewricht kan proefprinten met verschillende spelingen. Dat zeggen wij nu nergens.
3. **Ontwerpers met succes bouwen zelf gereedschap om varianten sneller te maken, en verdienen aan licenties.** Valeria en Mattia hadden geen tijd meer voor nieuwe ontwerpen door variantwerk; hun antwoord was een eigen tool. Wat zij verkopen naast het model is de commerciële licentie (ook bij McGybeer, verhaal 1 van Joris). Onze koper verdient dus aan snelheid: elke variant die hij sneller maakt is geld. Dat is de zin die bij hem werkt, niet "makkelijk".

### Eerlijk: wat niet zomaar voor ons geldt
- Ik heb niet gezien welke software Flexi Factory, MatMire en Cinderwing3D gebruiken. Alleen McGybeer zegt Blender. Een deel van deze groep werkt in ZBrush, Fusion of Nomad (GOK); die kopen geen Blender-add-on.
- Patreon-leden zijn printers die modellen downloaden, niet ontwerpers. De koper van Pro is de maker zelf, één per Patreon-pagina. Het getal dat telt is dus ±70 tot 80 (plus wie op Cults3D, MakerWorld en Thangs zit), niet 18.854.
- De omzetbanden van Graphtreon zijn schattingen met een factor 3 ertussen.

### Wat doen wij anders
Onze pagina, filmpjes en makersmails spreken de hobbyist en de AI-figuurmaker aan ("ball joints for your figure"). De professionele flexi-ontwerper, die al geld verdient en snel wil testen, spreken we nergens aan. En we hebben geen knop voor een proefprint van alleen het gewricht, terwijl vastgesmolten gewrichten een bekend probleem zijn.

### Voorstel voor Dortus deze week
**Ruben (eigenaar Pro 1.1) kijkt of een knop "Clearance test" in 1.1 past: hetzelfde gewricht drie keer naast elkaar exporteren bij 0,1, 0,2 en 0,3 mm speling, als één klein printbestand.** Bram heeft die drie spelingen al gemeten (0,0998, 0,1996 en 0,2995 mm, GEZIEN in `platformen/blender/status.md`, 8 nov), dus het is weinig nieuw werk (GOK). Chris kan er daarna één Short mee maken in de "connect"-vorm van verhaal 14: "Flexi joints fusing? Print this test first", met de drie printjes in beeld. Meetlat: haalt die Short meer dan de mediaan van onze eerste vijf, dan houden we de vorm. Tweede, kleiner: Chris voegt bij de makersmails twee of drie kleine flexi-ontwerpers op Patreon toe (100 tot 1.200 leden, uit het data-bestand), met een gratis Studio-licentie, want zij leven van gewrichten en hebben een publiek dat zelf print. Thijs verstuurt, net als de andere mails.

---

## 14. PrintPal (Atlas Rodin LLC, klein bedrijf uit Chicago, van OctoPrint-plugin naar een site met 50+ gratis printgereedschappen en een abonnement van $10): flexi is daar een gratis lokkertje, en hun filmpjes over flexi zijn hun slechtste

Onderzocht 16 nov 2026, run 14. Waarom dit verhaal: in verhaal 13 bleek de flexi-hoek te kiezen voor "zonder Blender". PrintPal is de grootste van die webdiensten die ik vond, en het heeft een volgorde die we kunnen nalopen: eerst een plugin voor OctoPrint, dan een AI-generator, dan tientallen kleine gratis gereedschappen, elk met een eigen pagina en een eigen Short. Omzet staat nergens openbaar; het enige grote getal ("400,000+ makers") is hun EIGEN OPGAVE. Wat ik zelf telde staat als GEZIEN.

### Bronnen (alle met curl of yt-dlp, GEZIEN 16 nov 2026)
- Flexi-gereedschap: https://printpal.io/tools/flexi-model-creator en de uitleg op hun blog, 27 feb 2026: https://blog.printpal.io/how-to-turn-any-3d-model-into-a-flexi-print-with-the-articulated-model-creator/
- Prijzen: https://printpal.io/pricing. Wie erachter zit: https://printpal.io/terms ("provided by Atlas Rodin LLC", Chicago).
- Hoeveel gereedschappen: https://printpal.io/sitemap-pages.xml (154 pagina's, waarvan 54 onder /tools/) en https://blog.printpal.io/sitemap-posts.xml (139 blogberichten met datum).
- De oude producten: https://plugins.octoprint.org/plugins.json (PrintWatch en BedCheckAI, auteur "printpal.io", met gebruikscijfers van OctoPrint zelf).
- YouTube: https://www.youtube.com/@printpal-io (17,5K abonnees; 8 gewone video's en 192 Shorts met weergaven via yt-dlp). Lijst: `platformen/succes/data/printpal-shorts-2026-11-16.csv`. Let op: YouTube rondt weergaven af (134.000 is "134K").
- Naast PrintPal gekeken: 3D AI Studio (https://www.3daistudio.com/pricing, "Join 1,000,000+ creators", EIGEN OPGAVE) en de Flexi Articulator Tool van Granite Studio op Thangs (een snij-STL voor $4,50; de hele maker heeft 299 downloads over 58 modellen, GEZIEN).
- Niet gelukt: Reddit (de zoek-API gaf een HTML-blokkade), het webarchief (geen verbinding), GitHub-gegevens van printpal-io (deze omgeving mag alleen bij onze eigen repo's).

### Wat ze in welke volgorde deden
1. **Jan 2022: PrintWatch**, een OctoPrint-plugin die mislukte prints stopt met AI. Nu 50 sterren op GitHub en 0 gebruikers per maand volgens OctoPrint (GEZIEN).
2. **Sep 2023: BedCheckAI**, tweede OctoPrint-plugin (kijkt of het bed leeg is). Nu 124 installaties per maand (GEZIEN). Klein, maar het bedrijf leefde door.
3. **Maart tot juli 2025: de AI-generator** (tekst of plaatje naar 3D-model) met een golf blogberichten: 56 berichten in vier maanden, bijna allemaal zoekvragen ("How to generate 3D models using ChatGPT", "What is a 3D print farm") (GEZIEN, sitemap).
4. **2026: gereedschap na gereedschap.** 54 pagina's onder /tools/, van rekenhulpjes (filament, kosten, e-steps) tot makers (naambord, vaas, puzzel, scharnierloze flexi, bureaumaatje met ESP32). Elk heeft een eigen pagina met uitleg onderaan en vaak een eigen Short ("3D Printing tools you should know part 7"). In januari 2026 alleen al 30 blogberichten (GEZIEN).
5. **Geld:** gratis met 10 AI-generaties per maand, Pro $10 per maand (200 generaties, "Flexi Model Creator", commerciële rechten), Studio $25, scholen $4 per plaats per maand, plus een aparte "AI CAD Agent" voor $20 per maand (GEZIEN). De flexi-pagina zelf zegt "100% free to use in your browser", de prijslijst zet de Flexi Model Creator bij Pro: dat spreekt elkaar tegen (GEZIEN). Mijn lezing (GOK): knippen is gratis, het AI-model maken waar je de gewrichten in zet kost generaties.

### Cijfers die iets zeggen
- **192 Shorts, samen ±4,4 miljoen weergaven, mediaan 14.000** (GEZIEN). 20 Shorts boven de 50.000, 21 onder de 5.000.
- **Per onderwerp (GEZIEN, mijn indeling op woorden in de titel; een Short kan in twee groepen vallen):**

| onderwerp | aantal | mediaan | hoogste |
|---|---|---|---|
| printdelen verbinden (snap fit, inserts, draad, "connect 3d prints") | 7 | 40.000 | 134.000 |
| een printfout oplossen (overhang, naad, eerste laag) | 28 | 27.000 | 120.000 |
| slicer-les "Day N" | 13 | 28.000 | 41.000 |
| een gereedschap van de eigen site laten zien | 31 | 14.000 | 96.000 |
| **flexi** | 3 | **3.200** | 6.200 |

- De flexi-Shorts ("How to make a flexi 3d print without designing" 6.200, "custom flexi animals" 3.200, "flexi animal ... perfect gift" 2.100) zitten alle drie in de onderste 15% van hun eigen kanaal (GEZIEN). "How to easily connect 3d prints with a snap fit" haalde 134.000.
- Eén gewone video brak uit: "Build an Interactive Desk Buddy for Under $20!" met 561.000 weergaven; de andere zeven gewone video's 1.000 tot 9.700 (GEZIEN). Daar hoort een gereedschap bij (Desk Pal Maker) en een bouwpakket van onderdelen van $20: iets wat je ook echt maakt.

### 3 lessen
1. **Flexi zonder Blender is nu een gratis lokkertje op grote sites, geen product.** PrintPal, STL Buddy (verhaal 13) en 3D AI Studio stoppen flexi als één van tientallen gereedschappen in een abonnement van ±$10 per maand, en de losse snij-STL van Granite Studio kost $4,50 en verkoopt bijna niets. Wie alleen "maak van een STL een flexi" wil, betaalt Click Joints Pro niet. Wat geen van deze sites doet: gewrichten met een eindstop en een bereik, kogel en scharnier die je los print en klikt, of een rig lezen (Ruben, `platformen/blender-2/rig-to-figure.md`). Daar zit ons verschil, en dat moet in de eerste zin staan.
2. **Het woord "flexi" trekt niet, het probleem "twee printdelen aan elkaar" wel.** Op hetzelfde kanaal, met dezelfde vorm en dezelfde hashtags, haalt "verbinden" mediaan 40.000 en "flexi" 3.200 (GEZIEN). Dat past bij hoofdles 3 (filmpjes rond de vraag van de gebruiker): een koper zoekt hoe hij delen verbindt, niet naar de naam van een soort speelgoed. Click Joints is precies een verbinder.
3. **Veel kleine gratis gereedschappen, elk met een eigen pagina en een eigen Short, en een betaald plan erboven.** PrintPal overleefde twee kleine plugins door te blijven schieten: 54 gereedschappen, en het gereedschap met een echt bouwproject (bureaumaatje) brak uit. Dit is de tweede keer na Kambari (verhaal 1) dat "veel schoten, door met wat raak is" terugkomt. Let op de schaal: dit is een bedrijf met een site en AI-servers, geen solo-add-on; de les is de vorm (één vraag, één gereedschap, één pagina, één Short), niet het aantal.

### Wat doen wij anders
- Onze reeks "Printable joints in Blender, day N" (Chris, `commercie/filmpjes/reeks.md`) is al tips, geen reclame. Goed. Maar de koppen gaan over speling en wanddikte: vragen die je pas hebt als je al gewrichten maakt. De grootste groep die PrintPal bereikt, heeft de vraag ervóór: "hoe krijg ik twee geprinte delen aan elkaar zodat ze bewegen".
- Op de winkelpagina en dortus.com/click-joints staat nog niet waarom iemand ons kiest boven een gratis flexi-site.

### Voorstel voor Dortus deze week
**Chris:** zet in de reeks vóór dag 5 één tip met een "connect"-kop, bijvoorbeeld "How to connect two 3D printed parts so they still move" (bal en kom, in Blender, los geprint en geklikt), met de Engelse woorden die werken: "connect 3d prints", "snap fit", plus #3dprinting. Gebruik het woord "flexi" niet in koppen. Meetlat (GOK): haalt die tip na 7 dagen minder dan de mediaan van de eerste vier tips, dan klopt deze les voor ons niet en schrappen we hem. Bram zegt "klopt" op de tekst zoals bij de andere tips. Kost geen geld en geen nieuwe opname als de bestaande beelden van kogel en kom (staande opname 5) gebruikt worden.
**Klein erbij voor Bram en Chris (geen taak, wel een zin):** "Flexi sites cut a joint into an STL. Click Joints builds joints that stop where you want, in Blender." of iets met dezelfde inhoud, als waarom-wij-zin op dortus.com/click-joints zodra Pro live staat.

---

## 13. Nikko Industries en STL Buddy (Nikko Industries, klein bedrijf uit Californië, YouTube sinds 2017, STL-winkel, abonnement en sinds 2025 een webgereedschapskist voor 3D-printen): de flexi-hoek kiest voor "zonder Blender", en elk gereedschap krijgt een eigen "How to make X"-filmpje

Onderzocht 16 nov 2026, run 13. Waarom dit verhaal: de opdracht was een "Sascha" voor geprinte figuren (verhaal 12): iemand met een publiek van mensen die beweegbare prints maken. Bij het zoeken naar uitlegvideo's over flexi in Blender (Joris noemde er een in `verhalen-groei.md`, 38.163 views) bleek de maker van die video niet alleen uitlegger maar ook een **concurrent**: hij verkoopt een webgereedschap dat flexi-gewrichten in een STL zet. Dat is precies wat Click Joints in Blender doet, maar dan in de browser en als abonnement. Let op: hij verkoopt ook een cursus ("School", "masterclass"). Ik neem daar niets van over; alles hieronder komt uit winkelpagina's, prijzen en tellers die ik zelf zag. Omzet en ledenaantallen staan nergens openbaar.

### Bronnen (alle met curl of yt-dlp, GEZIEN 16 nov 2026)
- YouTube-kanaal, video's en Shorts: https://www.youtube.com/@NikkoIndustries (kanaalpagina, lijst van 60 recente video's en 96 Shorts met weergaven).
- De flexi-video: https://www.youtube.com/watch?v=Sml8ecHkhPg (datum, weergaven, likes en beschrijving via yt-dlp). Daarna blokkeerde YouTube verdere vragen ("Sign in to confirm you're not a bot"); reacties onder de video heb ik dus NIET gelezen.
- STL Buddy, prijzen en voorwaarden: https://stlbuddy.com/pricing, https://stlbuddy.com/terms ("STL Buddy is operated by Nikko Industries"), https://stlbuddy.com/affiliates, de gereedschapspagina's https://stlbuddy.com/flexi-cutter en https://stlbuddy.com/flexi.
- Domeinregistratie stlbuddy.com via RDAP (openbaar register van Verisign).
- STL-winkel https://www.nikkoindustries.com en abonnement https://nikkoindustriesmembership.com.
- Niet te lezen: Patreon (403), de "School" (niet gevonden op Skool onder zijn naam).

### Cijfers
- **Kanaal: 23,1K abonnees, 1.174 video's, 13.923.302 weergaven, sinds 2 sep 2017** (GEZIEN). Onderwerpen eerst cosplay-helmen en harnassen, nu vooral "how to make X for 3D printing".
- **Flexi in Blender, 5 dec 2025: 38.202 weergaven, 675 likes, 13,5 minuten** ("How to Make Your Own Flexi STL Files (Free FlexiMaker Tutorial Using Blender + STL Buddy)"). Werkwijze volgens de beschrijving: plaatje maken met ChatGPT, plaatje naar STL met STL Buddy, in Blender de "FlexiMaker cutter" erover. Onderaan een betaalde vervolgcursus met o.a. "How to sell your Flexi files & prints online".
- **Flexi zonder Blender, 15 mei 2026: 771 weergaven** ("How to Make Your Own Flexi STLs Without 3D Modeling", 6,7 min). Zelfde onderwerp, nu in zijn eigen webgereedschap: 50 keer minder.
- Ter vergelijking, zijn andere lange video's in de lijst: meestal 300 tot 5.000; de uitschieters zijn uitleg over een slicer ("How to Cut Large Files in Bambu Studio" 21.000, "How to Paint in BambuLab Studio Slicer" 19.000) en de flexi-video.
- **Shorts: allemaal "How to make X #3dprinting", één gereedschap per filmpje.** Hoogste: "How to make a hinged box" 255.574 weergaven en 7.050 likes, geplaatst 9 nov 2026, dus in één week (GEZIEN). Daarna "how to make life size figures" 37.000, "how to make modular storage" 13.000, "How to split your models" 12.000. De scharnierdoos hoort bij het gratis gereedschap "Hinged Box Maker" van STL Buddy.
- **STL Buddy, domein geregistreerd 6 aug 2025** (RDAP). 94 betaalde plus 24 gratis gereedschappen, elk voor één ding (scharnierdoos, sleutelhanger, opbergla, onderzetter, splitsen, flexi). Prijzen (GEZIEN):
  - Free $0 (24 gereedschappen), Tinkerer $10 per maand (43, met **Flexi Cutter: "Add adjustable flexi joints to your STL model"**), Maker $20 per maand (87, "articulated models", met **Flexi Maker: "Build cute articulated flexi critters"**), Inventor $32 per maand (94, met Model Splitter).
  - Zonder abonnement losse credits: 40 voor $10 of 100 voor $20; een download uit Tinkerer kost 5 credits, dus een Flexi Cutter-bestand kost $1 tot $1,25 (eigen rekensom).
  - "Free to design": ontwerpen en voorbeeld zien is gratis, pas het downloaden kost geld.
  - Daarnaast "Image to STL" met eigen creditplannen van $10 tot $99 per maand, en een Etsy-tekstmaker en een foto-opknapper voor verkopers.
  - Partnerprogramma: 20% van elke abonnementsbetaling zolang de klant blijft, "There's no 12-month limit"; het staat nog in de testfase ("Automatic payouts are not enabled yet").
- **Abonnement op zijn eigen modellen: $20 per maand**, onbeperkt downloaden; op de voorpagina 19 keer "Flexi" (flexi-draken in thema's van Kerst en Halloween). Veel van zijn modellen zijn fan-art van bekende merken (Halo, Star Wars, Marvel, Pokémon); dat nemen we niet over.
- Niet gezien: hoeveel leden, abonnees op STL Buddy of kopers. Of het geld oplevert weet ik dus NIET.

### Wat hij in welke volgorde deed (uit de tellers en datums, geen eigen verhaal van hem gelezen)
1. Vanaf 2017 video's over cosplay printen, een STL-winkel met helmen ($20 tot $125) en later een abonnement van $20 per maand op zijn modellen.
2. Video's over geld verdienen met een printer ("5 Ways to Make Money with 3d Printing", "5 Places to Sell Your 3d Prints", "Is the New Thangs Print on Demand Worth It?"). Zijn publiek wordt zo: mensen die prints verkopen op Etsy en markten.
3. Aug 2025 STL Buddy: een website met kleine generatoren, elk voor één product dat je kunt verkopen.
4. Dec 2025 de flexi-video met Blender plus zijn eigen AI-stap, met een gratis cutter en een betaalde cursus. Zijn grootste lange video in die periode.
5. Daarna zette hij flexi als gereedschap in de site (Flexi Cutter in de $10-laag, Flexi Maker in de $20-laag) en maakte in mei 2026 een video zonder Blender, die bijna niet bekeken werd.
6. Sinds 2026 vooral Shorts in één vaste vorm, "How to make X", elk met één gereedschap van de site. Nov 2026 de scharnierdoos met 255.000 in een week.

### Drie lessen
1. **Onze directe concurrent in de flexi-hoek is geen Blender-add-on maar een website voor $10 per maand, gemaakt door iemand met 23K abonnees die verkopers bedient.** Wie flexi wil zonder te modelleren, gaat naar STL Buddy, PrintPal Flexi of Riggable (Ruben noemde die laatste twee al in `platformen/blender-2/rig-to-figure.md`). Click Joints moet dus niet vechten om "flexi in drie klikken", maar om wat een website niet doet: gewrichten met speling in mm, een scharnier met eindstop, nakijken waar het botst, in je eigen Blender-model. Dat zegt de mail aan de makers al ("for jointed figures rather than chain-link flexi"); deze les bevestigt dat die keuze klopt. Past bij hoofdles 7 (zeg waarom je beter bent dan de andere weg).
2. **"In Blender" in de titel kostte hem geen kijkers, eerder het omgekeerde.** Dezelfde maker, hetzelfde onderwerp: met Blender 38.202, zonder Blender 771. Waarom precies weet ik niet (GOK: het woord "Free", de lengte, of dat YouTube de eerste beter testte). Maar het laat zien dat er een groep is die flexi in Blender wil leren, en dat is onze koper. Dezelfde groep zag Joris (lange Blender-uitleg over beweegbare prints 38.000 tot 143.000).
3. **Eén gereedschap, één concreet ding, één "How to make X"-filmpje.** Zijn grootste Short is een scharnierdoos (255.574 in een week), niet het merk en niet de site. Elke generator is een filmpje over iets wat de kijker wil printen. Bevestigt hoofdles 3 (filmpjes rond de vraag van de gebruiker) en Joris' meting van de vaste kopvorm. Voor ons ligt het voor de hand: een scharnier dat stopt op 90 graden is precies wat Click Joints Pro doet.

### Eerlijk: wat niet zomaar voor ons geldt
- Hij had acht jaar kanaal en een publiek van verkopers vóór STL Buddy. Zijn Shorts komen bij een kanaal met 23K abonnees; onze eerste Shorts beginnen bij nul (Joris: 300 tot 900 views is normaal).
- Ik weet niet of STL Buddy loont; er staat nergens een omzet of ledental. Het partnerprogramma zit nog in de test. Het kan een groot aanbod zijn met weinig kopers.
- De 255.000 voor de scharnierdoos kan ook komen doordat het een ding voor iedereen is (een doosje), niet een gewricht voor figuurmakers. Een filmpje over ons scharnier haalt dat niet vanzelf (GOK).
- Nikko is een concurrent met een eigen flexi-gereedschap. Hem een gratis Pro aanbieden als bespreker heeft weinig kans, en het hoort niet op de makerslijst.
- YouTube blokkeerde na een paar vragen; reacties en de video's van zijn cursus heb ik niet gezien.

### Voorstel voor Dortus deze week
**Wie:** Chris (filmpjes), Ruben levert een schermopname uit Blender en, als het kan, een foto of filmpje van een print.
**Wat:** één van de eerste Shorts precies in Nikko's vorm: kop **"How to make a hinge that stops at 90° #3dprinting"** (of "How to make a print-in-place ball joint #3dprinting" met de gratis versie zolang Pro nog in de keuring zit). In de eerste seconde het onderdeel dat buigt en stopt, dan in 20 tot 30 seconden de stappen in Blender, aan het eind de print in de hand. Geen merk in de kop, Click Joints alleen in beeld en in de beschrijving. Het past in Joris' advies (vaste kopvorm, 15 filmpjes) en geeft die vorm een begin: "How to make <iets wat beweegt> #3dprinting". Meten zoals afgesproken: views na 48 uur en downloads die dag; bij 3 keer de mediaan de volgende vijf in dezelfde vorm (deur van een doosje, kaak van een figuur, vleugel, knie).

---

## 12. Craftsman Cabinet Creator (Sascha Feider en Ahmad, twee mensen, kasten op maat in Blender met zaaglijst, Superhive): een vakman met een cursus plus een bouwer die zijn leerling was

Onderzocht 16 nov 2026, run 12. Waarom dit verhaal: Click Joints Pro is net als deze add-on een Blender-hulpmiddel voor iets wat je echt gaat maken (printen tegenover zagen), komt laat in een hoek, en heeft geen eigen publiek. Craftsman Cabinet Creator (CCC) is ±9 maanden oud, kwam niet vroeg, en werd door Superhive zelf geïnterviewd. Geen cursusverkoper met beloftes: de cursus bestaat, maar alles hieronder komt van de winkelpagina's en het interview zelf.

### Bronnen
- Interview door Superhive (Wes Burke), 5 mei 2026: https://superhivemarket.com/posts/craftsman-cabinet-creator-interview-how-ccc-brings-parametric-cabinet-design-to-blender (GEZIEN met curl, EIGEN OPGAVE van de makers).
- Productpagina, versies en reviews: https://superhivemarket.com/products/craftsman-cabinet-creator (GEZIEN 16 nov 2026).
- De cursus van Sascha bij CG Cookie op Superhive: https://superhivemarket.com/products/craftsman--precision-modeling-with-blender-for-real-world-application (GEZIEN).
- YouTube-kanaal van Sascha: https://www.youtube.com/@SFE-Viz/videos (GEZIEN 16 nov, kanaalpagina met curl; de losse videopagina's gaven een lege pagina, dus de beschrijvingen zijn NIET GEZIEN).
- Bijlezen, ander Superhive-stuk met makersadvies (TrueVFX, Lens Sim, Mark Kingsnorth, SMOUSE), 22 jan 2025: https://superhivemarket.com/posts/the-business-of-blender-how-to-succeed-in-an-increasingly-competitive-market (GEZIEN, EIGEN OPGAVE van de makers).

### Cijfers (GEZIEN 16 nov, verkoopblokken zijn ondergrenzen)
- **CCC: 90+ verkopen voor $39, gepubliceerd "9 months ago"** (±feb 2026), 1 review (5 sterren). Ruwe omzet dus minstens ±$3.500 voor de winkel zijn deel neemt (GOK op GEZIEN blok en prijs).
- **De cursus van Sascha (CG Cookie, $39,99): 300+ verkopen**, "over 1 year ago". De cursus kwam eerst, de add-on daarna.
- **Kanaal SFE-Viz: 3,77K abonnees.** De laatste video's (weergaven, leeftijd):
  - "Blender 5.3: Dimensions in Edit Mode Are Finally Here!" 23K, 1 maand
  - "Blender 5.1 Face Snapping Is HERE But There's a CATCH!" 2,6K, 8 maanden
  - "I tested Texture Caching in Blender 5.2" 2,1K, 4 maanden
  - "Parametric Cabinets in Minutes - CCC Tutorial" 2,1K, 8 maanden
  - "This Cutlist Feature is a Game-Changer for Professionals - CCC Update" 1,7K, 7 maanden
  - "Built Right - Construction Logic For Interior ArchViz - BCON Austin 2026" 1,2K, 6 maanden
  - "New Front-Style Controls ... Cabinet Workflow" 868, 1 maand
  - "Craftsman Cabinet Creator - Blender Add-on Announcement" 797, 8 maanden
- Versiegeschiedenis op Superhive: leeg ("No versions found"), terwijl kanaal en interview twee updates noemen (zaaglijst, voorkanten). De updates staan dus niet als versies op de pagina.

### Wat ze in welke volgorde deden (uit het interview, EIGEN OPGAVE)
1. Sascha is timmerman met "nearly 20 years in the trade" en gebruikt Blender in zijn eigen bedrijf. Hij maakte een cursus bij CG Cookie over kasten op maat modelleren.
2. Ahmad, ontwikkelaar zonder timmerervaring, volgde die cursus: "watching how much manual effort goes into building cabinets traditionally was the spark". Hij bouwde een opzet in Geometry Nodes en benaderde Sascha. Sascha: "when Ahmad approached me with his Geometry Nodes setup, I jumped on it."
3. Ze bouwden samen tot het op de millimeter klopte. Sascha toetste het door een oud klantproject na te bouwen: "basically a perfect copy".
4. Aankondiging en uitlegvideo op Sascha's kanaal (±feb/mrt 2026), daarna een update met een video (zaaglijst), daarna het interview op de blog van Superhive (mei), een praatje op BCON Austin 2026, en een tweede update met video (voorkanten, okt).
5. Hun eigen uitleg waarom het een productietool is en geen plaatjesmaker: de zaaglijst. Ahmad: "That's the bridge between a 3D model and something a workshop can actually build."

### Drie lessen
1. **Een vakman met een cursus plus een bouwer is een goede ploeg; de vakman brengt het vertrouwen en de kopers, de bouwer het product.** CCC heeft geen vroege plek en maar 1 review, en toch 90+ verkopen voor $39 in 9 maanden, wat boven elke late nieuwkomer in onze hoek ligt (verhaal 9: de beste nieuwkomer sinds september 30+). De bouwer vond de vakman via diens cursus. Dit is een nieuwe vorm van hoofdles 4 (anderen maken het bereik): niet iemand die je product bespreekt, maar iemand die je product mee maakt.
2. **Op hetzelfde kanaal haalt een video over iets nieuws in Blender 10 keer zoveel als een productvideo.** 23K voor "Dimensions in Edit Mode" tegen 797 tot 2,1K voor de CCC-video's (GEZIEN). De nieuwsvideo's passen bij de vraag van zijn kijkers (precies modelleren), niet bij het product. Bevestigt hoofdles 3 (filmpjes rond de vraag van de gebruiker), nu bij een maker in de echte-wereld-hoek.
3. **Elke update kreeg een eigen video met de nuttige functie in de titel ("Cutlist Feature"), en de winkel interviewde ze kort na die update.** Bevestigt hoofdles 2 en 10. Maar: de versies staan niet op de Superhive-pagina, dus wie daar kijkt ziet geen leven. En uit het bijgelezen stuk: SMOUSE deed diepe kortingen vlak voor een sitebrede sale om op de voorpagina te komen; "even if it works once ... It's always a race to the bottom" (EIGEN OPGAVE). Dat past bij de kandidaat over korting: meedoen ja, onderbieden nee.

### Eerlijk: wat niet zomaar voor ons geldt
- Hoeveel van de 90+ uit Sascha's kanaal of cursus komt, zegt niemand. Het kan ook de interviewpagina of BCON zijn. Samenhang, geen bewijs.
- CG Cookie en Superhive zijn van hetzelfde bedrijf (Autotroph). Een docent van CG Cookie krijgt dus makkelijker een interview dan wij. Dat het interview er kwam, zegt niet dat wij er een krijgen.
- 90+ is een ondergrens; het kunnen er ook 99 zijn. En $39 is drie keer onze prijs.
- Voor 3D-geprinte figuren heb ik deze run geen "Sascha" gezocht. Chris heeft al 10 makers op een lijst (`commercie/blender-click-joints/makers.md`), maar dat zijn bespreekkanalen, geen mede-makers.

### Voorstel voor Dortus deze week
**Wie:** Chris schrijft een korte vraag aan de blog van Superhive (klaarzetten, niet versturen), de hoofdchat zet het versturen op `organisatie/lijst-thijs.md` zodra Pro live is, Bram levert twee feiten en één schermopname.
**Wat:** Superhive interviewt zelf makers (CCC mei 2026, "Inside the Hive", de lanceerreeks van 2020 uit verhaal 11). Dat is een bereik dat geen geld kost en dat de winkel zelf naar kopers stuurt. Vraag: "Interview or Creator Spotlight: how two-part ball joints and hinges with an end stop make 3D printed figures move, built in Blender." Vijf zinnen, drie beelden (het buigen met de schuif, rood waar het botst, een print), en het aanbod om de vragen schriftelijk te beantwoorden. Net als CCC: noem de brug naar de echte wereld (meten vóór het printen) als de reden dat het een werktool is. Versturen via het makerscontact van Superhive (de Creator Slack of het adres dat Superhive daarvoor noemt) door Thijs, na de goedkeuring en liefst na Pro 1.1, zodat er een update is om over te praten. Meten: of er binnen 4 weken een stuk komt, en het verkoopblok in de week erna.

---

## 11. Drie lanceringen uitgelegd door de makers zelf (Superhive-blog 2020: Serpens, InstaMat, KIT OPS), en wat er zes jaar later van over is

Onderzocht 16 nov 2026, run 11. Waarom dit verhaal: Click Joints Pro komt deze week uit de keuring. Superhive liet in okt en nov 2020 drie makers in eigen woorden uitleggen hoe zij een product lanceren. Dat zijn geen cursusverkopers: alle drie verkopen nog steeds op Superhive, en ik heb hun cijfers van nu ernaast gelegd. Eén van hen, Oliver J. Post, deed daarna precies wat hij beschreef, en dat is na te lopen op BlenderNation.

### Bronnen
- Serpens, Joshua Knauber (student, Duitsland, solo), 23 okt 2020: https://superhivemarket.com/posts/serpens-creator-joshua-knauber-the-anatomy-of-a-successful-product-launch (GEZIEN met curl, EIGEN OPGAVE van de maker).
- InstaMat, Oliver J. Post (architectuurstudent, Nederland, solo), 28 okt 2020: https://superhivemarket.com/posts/instamat-creator-oliver-post-the-anatomy-of-a-successful-product-launch (GEZIEN, EIGEN OPGAVE).
- KIT OPS, Chipp Walters (industrieel ontwerper, VS, klein team), 9 nov 2020: https://superhivemarket.com/posts/kit-ops-creator-chipp-walters-the-anatomy-of-a-successful-product-launch (GEZIEN, EIGEN OPGAVE).
- Winkels nu (GEZIEN 16 nov 2026 met curl): https://superhivemarket.com/creators/joshua-knauber , https://superhivemarket.com/creators/oliver-j-post , productpagina's https://superhivemarket.com/products/serpens , .../layerpainter , .../humgen3d , .../kit-ops .
- Alle berichten van Oliver Post op BlenderNation, 2020 tot 2023: https://www.blendernation.com/author/oliverjpost/ en de berichten zelf (teaser 28 jan 2021, lancering 15 mrt 2021, V2 15 jul 2021, V3 27 nov 2021; GEZIEN).
- Superhive, totaalcijfers van de winkel: https://superhivemarket.com/market-stats (DERDEN, de winkel zelf, GEZIEN 16 nov).
- Regels BlenderNation nu: https://www.blendernation.com/submit-news/ (GEZIEN 16 nov: een commercieel bericht kost EUR 25 of een Patreon-lidmaatschap).

### Cijfers (GEZIEN 16 nov 2026 tenzij anders vermeld)
| Maker | Product | Verkopen | Reviews | Prijs | Online |
|---|---|---|---|---|---|
| Joshua Knauber | Serpens 3 (visueel programmeren) | 2900+ | 59 | $20 | ±6 jaar |
| Joshua Knauber | Layer Painter | 2400+ | 29 | $1 nu | ±8 jaar |
| Oliver J. Post (met Alexander Lashko) | Human Generator Ultimate | 17200+ | 138 | $68, met plaatsen $128 | ±5,5 jaar (15 mrt 2021) |
| Oliver J. Post | Nature Clicker (gratis) | 400+ | 0 | $0 | ±6,5 jaar |
| Oliver J. Post | Water Shader, Flower Pack | 100+ elk | 0 tot 1 | $7 en $9 | ±6,5 jaar |
| Chipp Walters | KIT OPS 4 | geen blok getoond | | $35 | |

- Smudgr Pro en InstaMat, de twee add-ons waar Post in 2020 over vertelde, staan niet meer in zijn winkel (GEZIEN). Waarom niet, weet ik niet.
- Human Generator: 17200+ x ±$60 (na kortingen, GOK) is ruwweg $1 miljoen bruto in 5,5 jaar, voor twee mensen. Ter vergelijking: Superhive betaalde in 12 jaar $53,5 miljoen uit aan 6.885 makers (DERDEN), gemiddeld ±$7.800 per maker, met een heel scheve verdeling (GOK).
- Reviews tegen verkopen: Human Generator 138 op 17200 (0,8%), Serpens 59 op 2900 (2%). Weer dezelfde orde als bij Kambari en TrueDepth (hoofdles 5).
- Eigen opgave Post (2020): zijn promovideo van Smudgr Pro kreeg toen nog 22 weergaven per dag zonder promotie, "with an average of more than 1 sale per 10 views". Niet na te meten, EIGEN OPGAVE.
- Eigen opgave Post: 20 tot 40 minuten per week support, zonder bugs repareren; "More than half of the reviews on my product are from people I helped with customer support."
- Eigen opgave Walters: "well over 40,000 folks who have downloaded my products on Gumroad" (zijn mailinglijst, vooral van gratis producten) en "over 400 patrons".

### Wat Oliver Post deed, in volgorde (BlenderNation, GEZIEN)
1. **mei 2020:** Smudgr & Scratchr op BlenderNation; een week later een gratis add-on (Nature Clicker) ook op BlenderNation.
2. **30 jul 2020:** Smudgr Pro, "25% Launch Sale", weer een bericht.
3. **24 sep 2020:** InstaMat, bericht op de dag van uitbrengen. De promovideo maakte hij terwijl Superhive de add-on keurde (interview).
4. **23 nov 2020:** "Smudgr and InstaMat, Updates & Sale": een update samen met de Black Friday-actie als nieuw moment.
5. **28 jan 2021:** teaser van een veel groter product, Human Generator, met Alexander Lashko: "subscribe to the developer diary ... get a 10% launch discount". Zes weken voor de lancering een lijst met wachtende kopers.
6. **15 mrt 2021:** lancering Human Generator ("Half a year in the making"), 13 reacties onder het bericht.
7. **15 jul 2021:** V2, "25% Sale and Huge Update", "much requested features like a face rig"; gratis voor wie V1 had.
8. **27 nov 2021:** V3, "start the Black Friday sale early with 25% off", video van 56 seconden, Discord voor vragen.
9. **27 aug 2023:** "Human Generator Ultimate, 25% off and huge new update".
Zo is elke grote update een nieuwe lancering: video, bericht, 25% korting, en vaak vlak voor of in de grote sale van de winkel.

### Wat ze in 2020 zelf zeiden (de kern, letterlijk waar het telt)
- **Post: de lancering begint pas als jij promoot.** "for me, the real launch of the product happens days after it's been released on BlenderMarket. You might get some sales from the 'new' or 'staff picks' section, but the launch really begins when you start promoting." En: "most people don't look on Blender Market that often."
- **Post: de video beslist.** Rond één minuut, "show something cool and attention-grabbing in the first 10 seconds", en beelden op de winkelpagina die naar de video wijzen. Eerst BlenderNation, "the YouTube views of the promotional video go through the roof after this news post". Daarna YouTubers als partner met een gratis exemplaar, een royaal percentage en de tutorial erbij, zodat ze niets verkeerd laten zien.
- **Post: na de lancering is snel helpen het belangrijkste.** "Bad reviews just after launch are devastating"; meldingen aan op zijn telefoon, vaak binnen een uur antwoord; "never promise any features ... that I can't deliver within 1-2 weeks"; een formulier voor wensen, die hij één voor één uitbrengt en pas later samen promoot met een prijsverhoging ("people can now still buy it for the old price, before the price goes up forever").
- **Knauber: documentatie en uitlegvideo's.** Bij zijn eerste add-on niet gedaan, "it was the biggest issue with that launch". Voor Serpens bouwde hij vóór het uitbrengen een Discord op, dat werd "the main place of communication". Stukjes laten zien terwijl je bouwt, om te horen wat mensen verwachten.
- **Walters: 50% bouwen, 50% verkopen en marketing.** Per product een korte omschrijving WAT, voor WIE (en voor wie niet), WAAROM, WANNEER; daaruit komt de winkeltekst. Bètatesters in een Discord-kanaal, vooraf beelden op Twitter, een geschreven script voor de eerste minuten van de promovideo, en "Your existing customers are your best customers to sell new offerings to."

### Drie lessen
1. **Goedkeuring is niet de lancering. De lancering is het moment dat je overal tegelijk laat zien dat het er is, met een korte video die in 10 seconden pakt.** "New Arrivals" geeft een paar verkopen; het nieuwsbericht en de video van anderen geven de golf. Dat zegt Post, en Lens Sim (verhaal 10) en TrueDepth (verhaal 6) laten hetzelfde zien.
2. **Elke grote update is een tweede lancering: video, bericht, 25% korting, liefst op het moment van de grote sale, en daarna de prijs omhoog.** Human Generator deed dat drie keer in 2,5 jaar (V2, V3 op Black Friday, Ultimate), en V1-kopers kregen alles gratis. Past bij hoofdles 2 en de kandidaat "grote gratis update rechtvaardigt hogere prijs" (nu 3 keer: TrueDepth, BashSupport Pro, Human Generator).
3. **Support binnen het uur maakt de reviews.** Meer dan de helft van Posts reviews kwam van mensen die hij hielp (EIGEN OPGAVE), voor 20 tot 40 minuten per week. Past bij hoofdles 2.

### Wat ook opvalt
- Alle drie bouwden een eigen lijst of plek: Post een ontwikkeldagboek met korting, Knauber een Discord vóór de lancering, Walters 40.000 adressen via gratis producten op Gumroad. De kandidaat "lijst van gratis gebruikers" komt hiermee op 2 (Copilot, en nu deze drie samen als één verhaal).
- De grote treffer kwam pas bij product vier van Post, en was veel groter van opzet ("something BIG", zegt hij zelf). Zijn kleine producten blijven op 100+. Zelfde beeld als Kambari (veel schoten, door met wat raakt).

### Eerlijk: wat niet zomaar voor ons geldt
- Dit is 2020. BlenderNation plaatste toen commerciële berichten gratis (Post steunde ze wel op Patreon); nu kost het EUR 25 per bericht of een lidmaatschap (GEZIEN). YouTube en Twitter werken nu anders.
- Het zijn interviews op de blog van de winkel zelf, gekozen omdat het goed ging. Wat mislukte zien we niet, behalve dat twee van Posts add-ons uit zijn winkel verdwenen zijn.
- "1 verkoop per 10 weergaven" en "meer dan de helft van de reviews" zijn eigen opgaven en niet na te meten.
- Post en Walters zijn zelf 3D-gebruikers met een eigen publiek. Wij hebben 154 gebruikers van de gratis Click Joints (Bram, 16 nov 08:20) en mogen in die add-on niet naar Pro wijzen.

### Wat doen wij anders
- Chris heeft de lancering van Pro klaar (`commercie/blender-click-joints/lancering.md`), met als advies keuze A: een BlenderNation-bericht met Pro voor EUR 25, wat Thijs moet beslissen. Dit verhaal steunt dat advies: bij Post was BlenderNation telkens de eerste stap en de aanjager van de video.
- Er is geen plan voor een tweede lancering. Pro gaat uit als 1.0.x en daarna niets gepland als moment.
- Supportmail komt binnen bij thijs@dortus.com; geen agent kan die lezen. Snel antwoord hangt dus helemaal aan Thijs.

### Voorstel voor Dortus deze week
**Plan Pro 1.1 als tweede lancering op de eerste dag van de Cyber Sale (±27 nov, GOK op het vaste patroon), zoals Human Generator V3.**
- **Bram:** Pro 1.1 klaar op 26 nov, met de eerste wensen en meldingen van kopers en gebruikers van de gratis versie (bijvoorbeeld de kniefout die nu op een tak staat), en een changelog met per punt wie erom vroeg. Niets beloven wat niet binnen 1 tot 2 weken kan.
- **Chris:** één aankondiging "update plus Cyber Sale" klaarzetten voor dezelfde plekken als de lancering (Superhive-pagina, dortus.com, BlenderNation als Thijs ja zei op keuze A), met een video van ±1 minuut waarvan de eerste 10 seconden een figuur laten zien dat klikt en buigt (Daan keurt). Na de sale gaat de lanceerprijs weg (dat staat al in `prijs.md`).
- **Klein erbij, Chris:** een lijst van 10 kant-en-klare antwoorden op de vragen die kopers waarschijnlijk stellen (installeren, welke Blender-versie, past het scharnier op mijn printer, verschil gratis en Pro), zodat Thijs een vraag op Superhive of per mail binnen een uur kan beantwoorden door te plakken. Bij Post kwam meer dan de helft van de reviews uit zulke antwoorden.
- **Waarom dit beter is dan niets plannen:** een nieuw product zonder publiek heeft na "New Arrivals" geen tweede moment. De Cyber Sale is het grootste moment van het jaar op Superhive (verhaal 10), en een update geeft een eerlijke reden om er opnieuw over te berichten.

---

## 10. Lens Sim (Håvard Dalen, "Heinzelnisse", solo, echte cameralenzen in Cycles, Superhive): lanceren vlak voor de Cyber Sale, plus wat de Cyber Sale echt doet

Onderzocht 16 nov 2026, run 10. Waarom dit verhaal: Click Joints Pro zit in de keuring (ingediend 15 nov, 3 tot 5 dagen) en de Cyber Sale van Superhive begint rond Black Friday, vr 27 nov 2026 (GOK op het vaste patroon; de pagina `superhivemarket.com/page/2026-cyber-sale` bestaat sinds kort, op 8 nov nog niet, maar de inhoud laadt alleen met JavaScript, GEZIEN 16 nov). Superhive noemt zelf één kleine maker als uitschieter van de Cyber Sale 2024: Lens Sim, "published just prior to Cyber". Dat is precies de stand van Pro. Chris heeft de Cyber Sale al in `commercie/blender-click-joints/prijs.md` (punt 2, korting 25%); dit verhaal voegt de maker toe die het zo deed, en nieuwe cijfers van Superhive zelf. Geen cursusverkoper: bronnen zijn de forumdraden van de maker en de blog en hulppagina's van Superhive.

### Bronnen
- Werkdraad van de maker op Blender Artists, "Lens simulation", vanaf 8 mei 2024: https://blenderartists.org/t/lens-simulation/1528999 (GEZIEN met curl, pagina 1 en 2).
- Lanceerdraad "Lens Sim" in Released Add-ons, vanaf 8 nov 2024: https://blenderartists.org/t/lens-sim/1557203 (GEZIEN).
- Productpagina en versies: https://superhivemarket.com/products/lens-sim (GEZIEN 16 nov).
- Superhive, Cyber Sale 2024: https://superhivemarket.com/posts/blender-market-2024-cyber-sale-recap en 2023: https://superhivemarket.com/posts/2023-cyber-sale-recap (DERDEN, cijfers van de winkel zelf).
- Superhive, "Do People Only Buy During Sales?" (Kyle Maurer, 5 mrt 2026): https://superhivemarket.com/posts/do-people-only-buy-during-sales-here-s-what-the-data-says (DERDEN).
- Hulppagina's: meedoen met sitebrede sales https://support.superhivemarket.com/article/300-participating-in-site-wide-sales, eigen campagnes .../article/315-creator-sale-campaigns, uitgelicht worden .../article/242-how-to-get-your-product-featured, partners (affiliates) .../article/238-how-to-select-an-affiliate-percentage en .../article/385-using-the-affiliate-directory (DERDEN).
- Eigen meting splitshoek, korting en coupons: `platformen/succes/data/splitsers-korting-2026-11-16.tsv` (GEZIEN).

### Wat hij deed, in volgorde
1. **8 mei 2024: werk laten zien, nog geen product.** Na een tutorial over de nieuwe "Ray Portal BSDF"-shader van Blender opent hij een draad met renders door echte lenzen uit patenten (Canon 85mm, Kodak Petzval, Minolta Fisheye). 47 likes op de eerste post; de derde reactie: "I could definitely see this as an addon" (GEZIEN). Zijn antwoord: "Haven't yet decided what to do with it". Hij rijdt op een nieuwe techniek waar mensen net naar zoeken (hoofdles 9).
2. **17 juni 2024: plan hardop.** "I'm planning to make it into a add-on on BlenderMarket ... I think I will add a free version ... I'll might also add a light version" (GEZIEN). En een dag later: "if I'm going to sell it I need to be transparent of what I sell" (GEZIEN). De prijstrap gratis, lite, volledig staat dus al een half jaar voor de lancering vast.
3. **Zomer en najaar 2024: bètatesters.** In de lanceerdraad: "feedback from beta testers has also helped a lot with discovering missing features" (GEZIEN). Superhive schrijft erover: "thorough beta testing with some of the best in the business" (DERDEN).
4. **8 nov 2024: de lanceerdraad staat er drie weken vóór het product.** Op 26 nov: "Lens Sim will be out this week on time for the Black Friday sale" (GEZIEN).
5. **Rond 28 nov 2024: uitbrengen, één dag voor de Cyber Sale, en meteen in de sale.** 29 nov: "my addon is marked for the sale ... a 30% off marking" (GEZIEN). Dezelfde ochtend zet Bart Veldhuizen (BlenderNation) zijn YouTube-video bovenaan de draad: "I'll post it on BlenderNation too" (GEZIEN). Op dag één kopers met renders in de draad, en de maker antwoordt binnen een uur op elke vraag (GEZIEN, posts 6 tot 18).
6. **Daarna: Superhive noemt hem in het jaaroverzicht.** "The most impressive showing during Cyber 2024 was Lens Sim ... published just prior to Cyber and really took off ... utilized some genuine Affiliate marketing" (DERDEN).
7. **Twee jaar later:** 7500+ verkopen, volledige versie $40, Lite $15, demo $0 (upgrade: de Lite-prijs gaat eraf), 72 beoordelingen, versie 4.0.1 van 22 okt 2026, "I have opted in for all future Blender Market sales", een Discord met 452 leden, en een bundel met CinePack van een andere maker (GEZIEN). Omzet GOK: 7500 keer gemiddeld ±$30 (mix van korting en Lite) is grofweg $200.000 bruto; niet na te gaan.

### Cijfers van Superhive over de Cyber Sale (alle DERDEN, de winkel zelf)
| | Cyber 2023 (4 dagen, 30%) | Cyber 2024 (5 dagen) |
|---|---|---|
| Omzet (bruto) | $789.720 | $713.400 |
| Verkochte producten (betaald) | 35.918 | 33.691 |
| Verschillende producten met minstens één verkoop | 3.592 | 4.952 |
| Makers uitbetaald | (niet genoemd) | 1.442, gemiddeld $375 |
- Een gewone maand zonder sale was in 2024 gemiddeld $881k; de 5 Cyber-dagen waren dus ±80% van een maand.
- Per dag: Cyber 2023 was 8 keer de 60 dagen ervoor, het hoogste ooit; de October Blend Fest 2025 maar 1,2 keer. De klap van sitebrede sales wordt langzaam kleiner (Maurer).
- Meer dan 75% van alle aankopen is tegen de volle prijs; maar 0,4% van de vaste kopers koopt alleen in de sale. Kopers wachten de week vóór Cyber niet af: in 6 van de 7 jaar lag de omzet die week boven het jaargemiddelde (Maurer).
- Hoe meedoen: in het makersdashboard, Sale Campaigns, Sitewide Sale Settings, vinkje "Opt-in to all sitewide sales", of het product apart aan één campagne toevoegen. Alleen gepubliceerde producten. Meestal 25% korting. Een eigen campagne werkt niet zolang een sitebrede sale loopt (hulppagina's 300 en 315).
- "Popular Creations this week" zijn de 8 producten met de meeste verkopen van de afgelopen 7 dagen; "New Arrivals" toont de 8 nieuwste goedgekeurde producten (hulppagina 242).
- Hele winkel: ±14 reviews per dag, meestal binnen een dag na de aankoop (Superhive, Blend Fest-overzicht 29 okt 2025).

### Eigen meting: korting in de splitshoek nu (GEZIEN 16 nov ±10:45)
Alle vier winnaars van verhaal 9 doen mee aan korting: CatPin 20% via een eigen campagne ($21,60 in plaats van $27), Split 3D Print ($22 in plaats van $28), Kambari met publieke coupon "lunch25" (25%) op Dovetail Key en Smart Segmention. Cleave (100+) heeft een coupon van 10% "voor één week". Van de 17 achterblijvers doen er 3 mee (Split-it 30%, Easy Print 45%, RegoSplit met twee coupons). Korting maakt dus geen winnaar (achterblijvers geven zelfs meer), maar geen enkele winnaar staat erbuiten. Oorzaak en gevolg zijn niet te scheiden; GOK: winnaars gebruiken korting als moment, achterblijvers als noodgreep.

### Drie lessen
1. **Breng uit vlak vóór de grootste week van de winkel, en doe mee aan de sale.** Lens Sim kwam een dag voor Cyber 2024 uit, met 30% korting, en werd de uitschieter van de week. Het werkt omdat een sale volgens Superhive "attention" samenbalt: kopers lopen bladwijzers en nieuwe dingen af. Een nieuw product staat dan ook nog in New Arrivals. Wel nuchter: 4.952 verschillende producten verkochten iets in Cyber 2024; erin staan is geen garantie, en de sales slaan minder hard aan dan vroeger.
2. **Laat het werk maanden vooraf in het openbaar zien, met echte uitkomsten, en laat de vraag "maak er een add-on van" van anderen komen.** De werkdraad van mei gaf hem publiek, bètatesters en de lanceerdraad die er drie weken voor de lancering al stond. BlenderNation pakte het op uit die draad, niet uit een persbericht. Past bij hoofdles 4 (anderen maken het bereik).
3. **Een trap van gratis demo, Lite en volledig, met de upgrade verrekend.** De demo laat je eerst zien of het op jouw computer werkt ("Try the demo to verify compatibility before purchasing"), de Lite is de goedkope instap. Past bij hoofdles 1 en de kandidaat gratis variant.

### Wat doen wij anders
- Pro komt waarschijnlijk 18 tot 20 nov uit de keuring, dus net als Lens Sim een week vóór Cyber. Maar meedoen is een vinkje in het dashboard, achter de inlog van Thijs, en het staat niet op zijn lijst. Zonder dat vinkje heeft Pro in de drukste week de volle prijs naast concurrenten met 25% korting.
- Wij hebben geen draad met werk in uitvoering gehad; Pro komt uit zonder dat iemand erom vroeg. De gratis Click Joints (154 downloads) is ons publiek, maar we mogen in de add-on niet naar Pro wijzen (besluit Bram 15 nov 23:20).
- Wij hebben gratis (extensions.blender.org) en Pro $12 en Studio $45; dat lijkt op de trap van Lens Sim, alleen in twee winkels.

### Voorstel voor Dortus deze week
**Click Joints Pro meteen na goedkeuring in de Cyber Sale zetten, en een lanceerdraad op Blender Artists klaarzetten.** (a) Thijs (of de hoofdchat in zijn browser, zoals bij de upload) zet in het Superhive-dashboard onder Sale Campaigns, Sitewide Sale Settings het vinkje "Opt-in to all sitewide sales", of voegt Pro apart toe aan de Cyber-campagne, zodra Pro gepubliceerd is en vóór vr 27 nov. ±2 min. Prijsgevolg staat al bij Chris: $12 min 25% is $9, Dortus houdt ±$5,81 (`commercie/blender-click-joints/prijs.md`). (b) Chris schrijft een draad voor "Released Add-ons and Extensions" op Blender Artists (demofilm van Pro bovenaan, wat gratis en wat betaald is, link naar Superhive), Thijs plaatst hem op de dag dat Pro live staat. Wie: hoofdchat zet (a) op de lijst van Thijs (ik heb er een regel voor gezet), Chris (b). Waarom nu: de Cyber Sale is ±80% van een maand omzet in 5 dagen, en het enige kleine voorbeeld dat Superhive zelf noemt deed precies dit.

---

## 9. De hele hoek naast elkaar: 23 add-ons voor splitsen, verbinders en gewrichten op Superhive, en waarom er maar 4 verkopen

Onderzocht 16 nov 2026, run 9. Waarom dit verhaal: in verhaal 2, 3 en 8 keek ik naar de winnaars (Cleave, CatPin, Split 3D Print). Dat geeft een vertekend beeld, want de makers die niets verkopen schrijven geen blog. Daarom deze keer de hele hoek waar Click Joints Pro in komt te staan, de achterblijvers erbij, gemeten met curl. Geen cursusverkoper; alles komt van de winkelpagina's zelf.

### Bronnen
- 23 productpagina's op superhivemarket.com, met /ratings en /versions, GEZIEN 16 nov ±08:55 NL-tijd met curl. Lijst en meting: `platformen/succes/data/splitsers-superhive-2026-11-16.tsv`.
- Stand 8 nov uit `platformen/blender-2/data/superhive-print-2026-11-08.jsonl` (Olaf).
- Zoekvolgorde van Superhive (standaard, zonder sortering), GEZIEN 16 nov: `superhivemarket.com/search?search[q]=` met split, 3d print, connector, split 3d print, joint, joints, ball joint, articulated, hinge, figure, action figure.
- Eerdere metingen van YouTube en Gumroad: verhaal 2 (Cleave), 3 (CatPin), 8 (Split 3D Print), 1 (Kambari).

### Cijfers (alle GEZIEN 16 nov, verkoopblok van Superhive, ondergrenzen)
| Groep | Add-ons | Verkopen |
|---|---|---|
| Winnaars | Dovetail Key (Kambari, $18) 800+, Split 3D Print ($22) 400+, CatPin ($27) 400+, Smart Segmention (Kambari, $12) 300+ | samen 1.900+ |
| Midden | Cleave ($23) 100+, PuzzleUrPrint ($15, 5 jaar oud) 100+ | 200+ |
| Achterblijvers | One Click Splitting ($1) 40+, Articulator ($1) 30+, CutLink ($2) 30+, SnapSplit ($20) 30+, JointLab ($65) 20+, Meshsmith ($15) 20+, Split It ($8,40) 20+, 3D Slicer Suite ($17) 10+, Cut Flex ($34,99) 10+, One Click Split ($2) 10+, en 7 zonder verkoopblok (minder dan 10): FigureCut, PrintSplitter, Print-Ready Modelling Kit, RegoSplit, Split Helper, SplitPinPro, Easy Print v2 | samen 230+ |

- **De top 4 heeft ±82% van alle verkopen in deze hoek** (1.900 van ±2.330, ondergrenzen van de blokken; GOK op GEZIEN tellers, want 400+ kan ook 499 zijn).
- **Sinds september haalde geen nieuwkomer meer dan 100+.** Na Cleave (±half september, 100+) kwamen er 8 bij: CutLink 30+, Split It 20+, Cut Flex 10+, en RegoSplit, Easy Print v2, Print-Ready Modelling Kit, SplitPinPro en FigureCut onder de 10. De vier winnaars kwamen allemaal tussen juni en augustus (Dovetail Key ±juni, Split 3D Print ±juli, CatPin en Smart Segmention ±augustus).
- **In 8 dagen (8 tot 16 nov) ging alleen Split It een blok omhoog (10+ naar 20+).** De rest bleef in hetzelfde blok. Dat zegt weinig over de winnaars (een blok van 400+ loopt tot 499), maar wel dat de achterblijvers stil liggen.
- **Reviews:** alle 4 winnaars hebben er 2 tot 13. Van de 17 achterblijvers hebben er maar 2 reviews: Articulator (2) en JointLab (3, waarvan 2 met "Product was received for free").
- **Prijs verklaart het niet:** de goedkoopste ($1 en $2: One Click Splitting, Articulator, CutLink, One Click Split) blijven op 10+ tot 40+. De duurste (JointLab $65, Cut Flex $34,99) ook. Alle winnaars zitten tussen $12 en $27.
- **De pagina verklaart het ook niet:** Split It heeft 46 plaatjes en 20+ verkopen; RegoSplit 2.379 woorden en minder dan 10; Cleave 41 plaatjes en 4 video's en 100+; CatPin 0 losse plaatjes in de tekst (alles in de galerij) en 400+.
- **Zoekplek verklaart het maar half:** Split 3D Print staat eerste op "split" en "split 3d print", en verkoopt. Maar Cleave staat eerste op "connector", "ball joint" en "joints" (zijn titel somt "Pegs, Dowel, Rod channel, Magnets, Ball Joints" op) en blijft op 100+. Split It staat derde op "split 3d print" en blijft op 20+. Dovetail Key staat pas tiende op "split 3d print" en verkoopt het meest. De zoekvolgorde lijkt op woorden in titel en tags te gaan, niet op verkopen.
- **Een eigen winkel helpt niet als het de verkeerde kopers zijn:** Split It komt van Blender Procedural, met ruim 20 andere producten (generatoren voor kastelen, rotsen, steden). Toch 20+.

### Wat de winnaars wel hadden: elk één motor buiten de pagina
- **Dovetail Key en Smart Segmention:** Milad Kambari had al kopers en een reeks AI-add-ons (Smart Remesh, Image to 3D; verhaal 1). Twee producten in de top 4 van dezelfde maker.
- **CatPin:** een uitlegvideo van 22.704 weergaven en een Gumroad-pagina met 84 reviews (verhaal 3), dus een tweede winkel en een video die mensen echt zagen.
- **Split 3D Print:** geen publiek (10 abonnees), maar de eerste plek op het woord waar printers op zoeken ("split"), een gratis variant op dezelfde pagina, een tweede winkel (Gumroad, 22 reviews) en vroeg in de hoek (verhaal 8).
- **Cleave (middengroep):** goede pagina, eerste zoekplek op drie woorden, video van 2.890 weergaven, maar later (september) en geen gratis variant of tweede winkel. 100+.

### De gewrichten zelf, onze eigen kleine hoek
De twee add-ons die echt over gewrichten voor printfiguren gaan, staan allebei bij de achterblijvers:
- **Articulator ($1, 30+, 2 reviews, gemiddeld 4):** kogel, scharnier met pen en pengat. Beide reviews vragen hetzelfde: "would like to see more joints" en "it should have more types of joints, not just ball, hinge and peg joints" (GEZIEN). Op "ball joint" en "action figure" staat hij vierde.
- **JointLab ($65, 20+, 3 reviews):** de twee goede reviews kregen het gratis; de enige betaalde review geeft 1 ster: "Not what it seems. MCP forces you to use Jointlabs server ... Hard to use" (GEZIEN). Ook een online versie "USE ONLINE, FREE" op de pagina.
- Click Joints Pro (Personal $12, Studio $45) komt hier tussen. Zijn eigen dingen (scharnier met eindstop, de rode botsproef, kleur op de passing) heeft geen van beide volgens hun pagina (`commercie/blender-click-joints/winkeltekst.md`, GEZIEN 8 nov door Chris).

### Drie lessen
1. **In een kleine winkelhoek pakken een paar vroege makers bijna alles, en de rest blijft onder de 40.** Vier van de 23 hebben ±82% van de verkopen, en sinds september kwam er geen nieuwe meer boven de 100+. Wie later komt, moet een motor meebrengen; de pagina en de prijs zijn dat niet. Dit is een tegenwicht voor verhaal 8, waar het leek alsof de winkel je vanzelf vindt: dat lukte daar omdat Split 3D Print vroeg was en op het hoofdwoord bovenaan staat.
2. **Elke winnaar had één motor buiten de pagina: een bestaande kopersgroep, een video die echt bekeken werd, of de eerste plek op het hoofdwoord met een gratis variant en een tweede winkel.** Alleen een goede pagina (Cleave, Split It, RegoSplit) of alleen een lage prijs (vier add-ons van $1 en $2) gaf 10+ tot 100+. Dit bevestigt hoofdles 4 (anderen of iets buiten de winkel maken het bereik) en hoofdles 9 (op een moment komen).
3. **De paar reviews in onze hoek vragen om meer soorten gewrichten en om iets dat gewoon werkt.** Articulator: twee keer "meer soorten gewrichten". JointLab: 1 ster omdat het lastig is en een eigen server vraagt. Een koper die een figuur wil laten bewegen, wil kiezen uit genoeg soorten en geen gedoe. Dat is een wens die Click Joints Pro kan vullen (kogel en scharnier met stop nu; meer soorten is een update die het melden waard is, hoofdles 2).

### Eerlijk: wat niet zomaar voor ons geldt
- De blokken zijn ondergrenzen en Superhive zegt nergens precies wat "Sales" telt (verhaal 8: waarschijnlijk alleen betaald). De 82% kan dus wat anders uitvallen, maar het beeld (vier ver vooruit, de rest klein) blijft.
- Ik zie alleen Superhive. Achterblijvers kunnen elders verkopen (Gumroad, eigen site); dat heb ik deze run niet gemeten.
- "Sinds september geen nieuwkomer boven 100+" kan ook komen doordat 2 maanden te kort is. Cleave haalde 100+ in ±2 maanden, en de anderen van september en oktober staan op 10+ tot 30+ of lager; dus ook naast Cleave lopen ze achter.
- Of meer soorten gewrichten echt meer verkoopt, weet ik niet; het zijn 2 reviews.

### Voorstel voor Dortus deze week
**Wie:** Chris (titel, tags en eerste zin op de Superhive-pagina, klaar te zetten nu, aan te passen zodra de keuring klaar is), Bram (één regel in de releasenotes van 1.0.2), de hoofdchat (de keuze welke motor).
**Wat:** Click Joints Pro komt laat in een hoek waar de pagina alleen 10+ tot 30+ oplevert. Kies daarom nu bewust de motor, en geef die de eerste twee weken na de goedkeuring voorrang boven nieuwe functies:
1. **Gratis variant op de Superhive-pagina** (voorstel verhaal 8, nu sterker): dat is wat de enige winnaar zonder publiek deed.
2. **De woorden van de koper in titel en tags**, want de zoekvolgorde gaat op woorden. Nu: titel "Click Joints Pro" en 9 tags (welke staat niet in de repo, `platformen/blender/superhive-pagina.md`). Voorstel titel: **"Click Joints Pro: Ball Joints and Hinges with End Stop for 3D Printed Figures"**, tags (als ze er nog niet staan): ball joint, hinge, articulated, action figure, figurine, 3d printing, cosplay, resin, fdm. Op "ball joint" en "action figure" staat nu alleen Articulator ($1, 30+) tussen de splitsers; daar kan Click Joints Pro in de top 3 komen (GOK).
3. **De video als tweede motor:** de YouTube-uitleg die Chris klaarzet (`commercie/filmpjes/youtube-1.md`) wordt "how to make a figure with ball joints and knee hinges in Blender for 3D printing", een zoekvraag (hoofdles 3), niet een productfilmpje. CatPin is het bewijs dat één bekeken uitlegvideo de hoek openbreekt.
Meten: verkoopblok en zoekplek op "ball joint", "joint" en "action figure" elke week in `platformen/blender/status.md`. Verwachting eerlijk: zonder motor 10+ tot 30+ in de eerste maanden, zoals de rest van de late groep (GOK op GEZIEN).

---

## 8. Split 3D Print (AUER, solo, splitsen met verbinders voor 3D-printen, Superhive en Gumroad, zonder eigen publiek)

Onderzocht 16 nov 2026, run 8. Waarom dit verhaal: de hoofdchat vroeg verhalen die helpen bij de eerste 100 kopers van Click Joints Pro. Split 3D Print is een add-on voor precies onze kopers (figuren, cosplay, resin en FDM), van een maker die buiten Superhive bijna niet bestaat, en toch staat hij na ±4 maanden op 400+ verkopen voor $22. Hij doet twee dingen die wij niet doen: een gratis variant op dezelfde winkelpagina en een gratis instap op Gumroad. Geen cursusverkoper; alles hieronder komt van de winkelpagina's, YouTube en een eigen meting.

### Bronnen
- Superhive-pagina's (GEZIEN 16 nov met curl): https://superhivemarket.com/products/split-3dprint , /versions, /ratings, /faq
- Tweede product van dezelfde maker: https://superhivemarket.com/products/bizen3d ; makerpagina https://superhivemarket.com/creators/auer
- Gumroad: https://auerblender.gumroad.com/l/kxxyq (opties en reviewtelling uit de JSON op de pagina, GEZIEN 16 nov); stand 8 nov uit `platformen/blender-2/data/gumroad-print-2026-11-08.jsonl` (Olaf)
- YouTube: kanaal https://www.youtube.com/@AUER_Blender en de video https://www.youtube.com/watch?v=l3I08ctCQkk ; zoekresultaten "split3d print blender addon" (GEZIEN 16 nov)
- Controle van de verkoopteller: drie andere Superhive-pagina's (https://superhivemarket.com/products/3dt-stylized-oak-geometry-node , /animals-free , /chlorophytum-comosum), GEZIEN 16 nov
- Zoeken naar ander bereik: BlenderArtists-zoek-API (split3d, auer.blender: 0 draden), BlenderNation en 80.lv (geen artikel over Split 3D Print gevonden; het 80.lv-stuk over "drawing lines" gaat over Dovetail Key). Reddit gaf 403 vanuit de cloud, niet gemeten.
- Meetbestand: `platformen/succes/data/split3dprint-2026-11-16.tsv`

### Cijfers
- **Verkopen (GEZIEN):** blok "Sales 400+" en "Downloads 400+", 3 ratings gemiddeld 5, "Published 4 months ago" (dat stond er op 8 nov ook al, dus uitgebracht ±juli 2026). Prijs $22 met doorgestreepte $28 ("On Sale!"; ook op 8 nov al $22, dus de korting staat er vast op).
- **Wat de teller telt (GEZIEN, nieuw):** een pagina met alleen gratis spullen toont alleen "Downloads" (animals-free 4700+, chlorophytum 80+) en geen "Sales". Een pagina met een gratis proefje naast betaalde licenties (3dt-stylized-oak, $0 / $7,99 / $18,99) toont "Sales 30+" en "Downloads 400+". "Sales" telt dus vrijwel zeker alleen betaalde aankopen, "Downloads" de gratis. Bij Split 3D Print zijn dat er allebei 400+. Dat maakt het waarschijnlijk dat hij echt 400+ betaalde verkopen heeft, ±$8.800 bruto voor kortingen (GOK op GEZIEN teller, één vergelijking). Dit verbetert een eerdere lezing in ons huis ("teller telt ook gratis downloads", verhaal 2 en `platformen/blender-2/`): die was waarschijnlijk te voorzichtig.
- **Prijstrap (GEZIEN, Superhive):** Free $0 ("Limited Cuts Line with its adjustable peg and socket connector, and STL export"), Full $22 (van $28), Support $28 (van $34, "A big thank you for your support!"), 5 seats $59 (van $65). Alles met "Lifetime updates."
- **Gumroad (GEZIEN):** zelfde vier opties, maar de pagina opent op $0 (Free), Full $28 zonder korting, Support $34, 5 seats $65. Reviews: 20 op 8 nov, 22 op 16 nov, gemiddeld 4,9. Verkoopteller verborgen.
- **Eigen bereik (GEZIEN):** YouTube-kanaal 10 abonnees, 3 video's; de productvideo 1.288 weergaven in 2 maanden. Ter vergelijking: de video van CatPin 22.704, Cleave 2.890, Split It (concurrent) 1.320. Geen draad op BlenderArtists, geen vakblad gevonden.
- **Versies (GEZIEN):** V3 op 26 aug (gratis variant op 28 aug), V4 op 11 nov (automatisch opdelen met een AI-model, 865 MB eenmalig te downloaden), daarna 4.0.1 op 12 nov (toetsen voor wie de Industry Compatible keymap gebruikt) en 4.0.2 op 13 nov (Windows-fout "DLL load failed" opgelost). Oudere versies staan niet meer in de lijst.
- **Reviews en antwoorden (GEZIEN):** op alle 3 reviews antwoordt hij, ook op de lange kritische van iemand die de gratis versie gebruikte ("Product was received for free"); die koper schreef dat hij eerst wilde vergelijken "before buying". De maker legt uit, wijst naar de video en naar de nieuwe Repair-functie, en nodigt uit om contact op te nemen. Een andere koper bedankt hem voor een wens die in V3 zat (verbinders plaatsen zonder te snijden).
- **Tweede product (GEZIEN):** Bizen3D (AI-modellen in Blender), 9 dagen oud, zelfde trap ($20 van $24, Support $26, 5 seats $60), nog geen verkoopblok. De pagina van Split 3D Print verwijst onderaan naar Bizen3D ("ALSO FROM ME"), andersom niet.
- **Vindbaar in de winkel (GEZIEN):** op de tagpagina "figurine" staat hij als zesde, na FigureCut, Cleave en CatPin. Zijn tags: cut, split, print, magnets, connector, 3d print, resin, fdm, cosplay, figurine.

### Wat hij deed, in volgorde (zover de bronnen het tonen)
1. ±Juli 2026: op Superhive, $22 met doorgestreepte $28, met steunklasse en 5 plaatsen. Zelfde product op Gumroad.
2. Eind augustus: grote V3 (snelle en expertmodus, bewerkbare sneden, reparatie, verbinders zonder snijden) en meteen een gratis variant met één soort snede en STL-export, op Superhive én Gumroad.
3. September: één productvideo op een leeg kanaal. Verder geen bereik buiten de winkels dat ik kon vinden.
4. November: V4 met automatisch opdelen (AI), twee herstelversies in twee dagen, en een tweede product dat op de eerste pagina wordt aangeprezen.

### Drie lessen
1. **Een gratis variant op dezelfde winkelpagina laat de winkel zelf je proefversie uitdelen, en de verkoopteller blijft eerlijk.** Bezoekers van Superhive zien naast $22 ook $0. Gratis gebruikers mogen reviewen (1 van zijn 3 reviews), krijgen de updates in hun Superhive-bibliotheek, en tellen niet mee in "Sales", dus de teller die nieuwe kopers zien blijft over betaalde verkopen gaan. Op Gumroad opent de pagina zelfs op $0, wat in zoeklijsten "gratis" laat zien. Click Joints heeft de gratis versie alleen op extensions.blender.org (152 downloads), waar we niet naar Pro mogen verwijzen (besluit Bram 15 nov 23:20). Een gratis variant op de Superhive-pagina is de omgekeerde route: de koper die al op Superhive zoekt, kan eerst proberen en ziet Pro ernaast.
2. **Zonder eigen publiek kan het, maar dan moet de winkel je vinden.** 10 abonnees, één video van 1.288 weergaven, geen forum en geen pers, en toch 400+ (waarschijnlijk betaald). Wat hij wel had: de woorden waar printers op zoeken als tags (figurine, cosplay, resin, fdm, magnets), een pagina die per functie zegt "Where to find it", printers bij naam (18 voorinstellingen: Bambu Lab, Prusa, Creality en meer), en een vaste korting met doorgestreepte prijs. Dit is een tegenvoorbeeld voor hoofdles 4 (anderen maken het bereik): in de printhoek van Superhive is er genoeg verkeer van binnen, zolang je in die hoek vindbaar bent. Waarom precies hij en niet Split It (10+) kan ik niet zien; GOK: eerder in de winkel, meer functies en de gratis variant.
3. **Grote gratis updates en snelle herstelversies, met elke review beantwoord.** Twee grote versies in ±4 maanden en twee fixes binnen twee dagen na V4, plus "I listen to every request from the community". Dat is hoofdles 2 nog een keer. Hij belooft wel "Lifetime updates" terwijl Superhive dat afraadt (verhaal 7); net als TrueDepth gebruikt hij het als verkoopargument.

### Eerlijk: wat niet zomaar voor ons geldt
- Dat "Sales" alleen betaalde aankopen telt, rust op één pagina met beide soorten en twee gratis pagina's. Superhive schrijft het nergens op. Het blijft dus een sterke aanwijzing, geen zekerheid.
- Splitsen is een grotere klus met meer kopers dan gewrichten met een eindstop (verhaal 2 en `platformen/verkenner/superhive-2026-11.md`: gewrichten 20+ tot 30+). 400+ is geen verwachting voor Click Joints Pro.
- Of de gratis variant de verkoop deed stijgen weet ik niet: de teller toonde op 8 nov al 400+ en ik heb geen oudere standen (archief gaf geen antwoord).
- Of een nieuwe variant op een goedgekeurde pagina een nieuwe keuring vraagt, weet ik niet (GOK: kleine wijzigingen niet, maar de keuring van 1.0.1 loopt nu nog).

### Voorstel voor Dortus deze week
**Wie:** Bram maakt de gratis zip klaar als variant (de bestaande gratis build 0.1.1, al getest), de hoofdchat zet hem op de Superhive-pagina zodra Click Joints Pro is goedgekeurd, Chris schrijft de ene regel.
**Wat:** op de Superhive-pagina van Click Joints Pro een derde variant naast Personal $12 en Studio $45: **"Click Joints Free, $0: the ball joint with print clearance, same as on extensions.blender.org. Pro adds the click hinge with the 115° end stop and the red collision check."** Waarom: zo deelt Superhive zelf onze proefversie uit aan mensen die al naar print-add-ons zoeken, gratis gebruikers kunnen reviewen, en de verkoopteller van Pro blijft alleen over betaalde aankopen gaan. Het raakt de regels van extensions.blender.org niet (de verwijzing staat op Superhive, niet in de gratis listing). Meten: Downloads- en Sales-blok van de pagina wekelijks noteren in `platformen/blender/status.md`; na 4 weken kijken of Sales sneller groeit dan in de weken zonder gratis variant.

---

## 7. Superhive zelf: de markt waar Click Joints Pro staat, en wat kopers vinden van "12 maanden updates" (Support Periods, 2026)

Onderzocht 16 nov 2026, run 7. Waarom dit verhaal: de hoofdchat vroeg verhalen die helpen bij de eerste 100 kopers van Click Joints Pro. Pro staat op Superhive in keuring met een Support Period aan (12 maanden updates, verlengen voor 25% van de prijs, `platformen/blender/superhive-pagina.md`). Ik vond dat Superhive dit jaar zelf zijn cijfers en zijn grootste ruzie met kopers openbaar maakte, precies over die keuze. Geen enkele maker, maar het "verhaal" van de winkel, met eigen telling van 110 productpagina's. Geen cursusverkoper.

### Bronnen
- Jonathan Williamson (baas van Superhive, bedrijf Autotroph), "The Blender Creator Economy is Breaking. Let's Start Talking About It.", 18 feb 2026: https://autotroph.com/the-blender-creator-economy-is-breaking-lets-start-talking-about-it
- Williamson, "We built this together, now we need to fix it" (uitwerking van zijn praatje op BCON Austin, voorjaar 2026): https://autotroph.com/we-built-this-together-now-we-need-to-fix-it
- Williamson, "Support Periods: A Sustainable Path Forward for Blender Creators", 22 apr 2026: https://superhivemarket.com/posts/support-periods-a-sustainable-path-forward-for-blender-creators
- Hulpartikelen voor makers: FAQ https://support.superhivemarket.com/article/331-support-period-faqs-creators , verlengkorting https://support.superhivemarket.com/article/328-discounting-support-period-renewals , levenslang verkopen https://support.superhivemarket.com/article/327-selling-lifetime-support-and-updates , oude kopers https://support.superhivemarket.com/article/345-managing-legacy-customers
- BlenderNation (Greg Zaal, Poly Haven), "Incoming Policy Changes on Superhive", 1 apr 2026, met reacties: https://www.blendernation.com/2026/04/01/incoming-policy-changes-on-superhive/
- BlenderArtists, draad "Superhive Changes", 20 mrt tot 25 jun 2026, 812 berichten, 46.025 keer bekeken (GEZIEN via de JSON van het forum): https://blenderartists.org/t/1634680 . Ik las de laatste 40 berichten.
- Spencer Magnusson (kleine maker op Superhive), nieuwsbrief 7 mrt 2026: https://spencer-magnusson.beehiiv.com/p/blender-creator-economy-is-breaking-whats-next
- Marktcijfers: https://superhivemarket.com/market-stats (16 nov 2026) en de terugblik 2022: https://superhivemarket.com/posts/2022-wrap-up-and-cyber-results
- Eigen telling, 16 nov 2026 met curl: de 71 best verkochte producten (`/products?sort_sales=desc`, pagina 1 tot 3) en de 39 nieuwste add-ons van de laatste ±6 maanden (`/categories/addons?sort_date=desc`). Per pagina gekeken wat er over updates staat. Bestand: `platformen/succes/data/superhive-updatebelofte-2026-11-16.tsv`.
- Niet gelukt: het Medium-stuk "Who Is Superhive's Support Policy Actually Benefiting?" (leeg vanuit de cloud), de grafieken in de blogs (plaatjes, geen getallen), de Reddit-draden. Verkoopcijfers per maand van Superhive staan nergens openbaar na 2022.

### Cijfers
- **De markt nu (GEZIEN 16 nov, market-stats):** 6.877 makers, 73.662 producten, waarvan 6.770 add-ons, 5.795.934 verkochte items aan 1.138.576 klanten, $53.532.733 betaald aan makers sinds 2014. Gemiddeld $9,24 per verkocht item voor de maker en ±$7.800 per maker in 12 jaar (rekensom; gratis items tellen misschien mee in de items, dus GOK hoe precies).
- **Groei is voorbij de top (DERDEN, Williamson):** acht jaar op rij verdubbeling, piek in 2022. Recordmaand nov 2022: $1.246.632 omzet (DERDEN, blog 2022). In zijn praatje (voorjaar 2026): "7,500 creators", "over 60,000 products", "nearly $50 million" uitbetaald. Sindsdien ±$3,5 miljoen erbij in ±7 maanden, dus ±$0,5 miljoen per maand (GOK, zijn getallen zijn afgerond).
- **Het patroon bij "virtually all top sellers" (DERDEN, Williamson):** het aantal kopers dat steun verwacht groeit, de verkopen per jaar blijven gelijk of dalen. "The pattern is consistent across categories, product types, and audience sizes." Zijn verklaring: de onuitgesproken verwachting van levenslang gratis updates.
- **Wat er gebeurde (DERDEN, BlenderNation en Superhive):** 18 mrt mail aan makers: verplicht voor iedereen, ook voor oude aankopen, verlengen voor 50%. Felle reacties ("feels similar to a subscription"). 22 apr de nieuwe versie: vrijwillig per product, oude kopers houden alles, de maker kiest 25, 50, 75 of 100% van de prijs voor verlengen. Live op 22 jun 2026. Superhive zegt zelf dat de communicatie fout ging.
- **Wie doet mee (GEZIEN, eigen telling 16 nov):**
  - Top 71 best verkocht: 17 met Support Period (24%), waarvan 9 op 25%, 7 op 50% en 1 op 75%. De grootste van de hele winkel, Auto-Rig Pro (71.200+ verkopen), doet mee op 25%. 45 pagina's zeggen niets over updates, 6 noemen "free updates" zonder termijn, 2 noemen levenslang (onder meer TrueDepth: "Lifetime support. All future updates, free"), 1 heeft een eigen jaarregeling (MACHIN3tools: "1 year of free Updates", verlengen als aparte variant, al van vóór Support Periods).
  - 39 nieuwe add-ons (±6 maanden): 9 met Support Period (23%), 4 op 25% en 5 op 50%. 23 zeggen niets, 5 "free updates", 2 levenslang.
  - Onze drie vergelijkers in 3D-printen doen het alle drie anders: TrueDepth levenslang, CatPin 12 maanden en verlengen 50%, Cleave "Free updates for the 1.x line".
- **Wat kopers zeggen (GEZIEN, BlenderArtists mei tot jun 2026):** "What used to be 'buying a fun product to try ... when I have time' is now 'entering into a potential future contract with unknown time and financial expenses'." Twee vaste kopers kochten in de voorjaarsuitverkoop niets. Een ander: "I still think the entire idea of support periods will only help the top 10 most popular addons." Tegengeluid: "Communication could be better but im quite satisfied with the changes."
- **Hoe een kleine maker het bracht (GEZIEN, mail van Cablerator, doorgeplaatst 25 jun):** "I have enabled yearly Support Periods for Cablerator at 25% (the lowest available setting), however this will apply only to new customers ... nothing changes for you ... you can optionally join." De koper die het plaatste vond dat goed: "most creators still want their add-ons to be affordable".

### Wat er gebeurde, in volgorde
1. 2014 tot 2022: de winkel groeit elk jaar met de helft of meer; kopers wennen aan "eens kopen, altijd updates". Superhive eiste dat nooit, maar vroeg alleen om op de pagina te zeggen of updates gratis zijn (oude hulptekst, aangehaald door een lezer van BlenderNation).
2. 2022 tot 2025: meer kopers, niet meer verkopen. Williamson ziet het bij bijna alle grote verkopers.
3. Feb 2026: hij maakt het probleem openbaar, met geanonimiseerde grafieken.
4. Mrt 2026: verplichte regel per mail, ook voor oude aankopen. Woede op elk forum.
5. Apr 2026: alles vrijwillig, oude kopers ongemoeid, verlengprijs door de maker gekozen.
6. Jun 2026: live. Weinig makers doen mee in het begin; in november een kwart van de toppers en een kwart van de nieuwe add-ons.

### Drie lessen
1. **Op Superhive is "12 maanden updates" normaal geworden, maar kopers voelen het nog als een abonnement. Zeg dus in gewone woorden wat de koper houdt.** Superhive zelf zegt "This is not a subscription. You own what you buy", maar de kopers op het forum lezen "contract". Auto-Rig Pro en de kleine maker van Cablerator kozen allebei de laagste stand (25%), en de maker legde het uit in zijn eigen woorden. Onze keuze (25%) is dus dezelfde als die van de grootste verkoper; wat ontbreekt is de uitleg op onze pagina.
2. **"Levenslang gratis updates" is een verkoopargument dat de winkel zelf afraadt, en dat maakt het juist een onderscheid.** TrueDepth, de best verkochte printadd-on, zet "Lifetime support. All future updates, free" in zijn rijtje. Superhive: "we genuinely believe that lifetime support and updates is an unsustainable promise". Voor een product van $12 met weinig onderhoud is het vooral een kwestie van wat je durft te beloven. Ik raad het niet aan (een belofte zonder einde past niet bij een ploeg die nog niet weet hoeveel kopers er komen), maar we moeten weten dat het er naast ons staat.
3. **De markt groeit niet meer vanzelf.** Na acht jaar verdubbelen is Superhive sinds 2022 niet meer gegroeid, en de baas zegt dat bijna elke grote verkoper minder verkoopt per jaar. Wie nu nieuw binnenkomt, krijgt geen golf mee; de kopers moeten van buiten komen (video's van anderen, hoofdles 4) of uit een echt nieuwe vraag (hoofdles 9). Gemiddeld verdient een maker op Superhive ±$7.800 in 12 jaar (rekensom).

### Eerlijk: wat niet zomaar voor ons geldt
- Of een Support Period de verkoop van een nieuw product remt, kan ik niet meten: nieuwe producten tonen nog geen verkoopblok, en de toppers met Support Period verkochten al jaren vóór juni. De mediaan van de 17 toppers met Support Period (11.500) is hoger dan die van de rest (7.600), maar dat zegt niets over oorzaak.
- De forumdraad is een luide groep; 812 berichten zijn niet de 1,1 miljoen klanten. Hoeveel kopers echt minder kopen weet niemand buiten Superhive.
- De grafieken van Williamson zijn geanonimiseerd en zonder getallen. Hij heeft er belang bij dat makers meedoen (Superhive verdient aan verlengingen).
- Voor ons gaat het om $3 per jaar (25% van $12). Het bedrag is het probleem niet; het woord "contract" in het hoofd van de koper wel.

### Voorstel voor Dortus deze week
**Wie:** Chris schrijft de zin (`commercie/blender-click-joints/`), de hoofdchat zet hem op de pagina zodra Pro live is (de pagina nu niet aanraken tijdens de keuring, GOK dat aanpassen de keuring stoort), Bram houdt het aan bij 1.0.2.
**Wat:** één regel onder "Good to know" op de Superhive-pagina van Click Joints Pro, in de lijn van Cablerator: "Includes 12 months of updates. Every version you download is yours to keep. After a year you can extend updates for 25% of the price ($3 today); it is never required." En dezelfde zin in het antwoord-sjabloon van Chris voor vragen van kopers. Waarom: het neemt de angst voor een abonnement weg zonder iets te veranderen aan de prijs of de regeling, en het kost niets. Daarnaast voor later (geen taak): bij elke nieuwe add-on bewust kiezen tussen 25% en "updates voor de hele 1.x-reeks" zoals Cleave, niet automatisch.

---

## 6. TrueDepth (Lewis Martin, solo, mogelijk met een helper, AI-dieptekaart naar 3D in Blender, Superhive)

Onderzocht 16 nov 2026, run 6. Waarom dit verhaal: TrueDepth is in de lijst van Olaf (8 nov) het best verkochte product met "3d print" op Superhive: 6900+ verkopen in bijna twee jaar. Het is een kleine maker die een gratis AI-model (Depth Anything) in één klik in Blender zet, terwijl er gratis wegen bestaan. Dat lijkt op Click Joints Pro: iets wat je met de hand of gratis ook kunt, maar sneller en binnen Blender. Geen cursusverkoper: hij verkoopt add-ons, geen cursus.

### Bronnen
- Superhive, met curl gelezen 16 nov 2026: productpagina https://superhivemarket.com/products/truedepth , alle 57 reviews (https://superhivemarket.com/products/truedepth/ratings?page=1 tot 6), zijn winkel https://superhivemarket.com/creators/lewis-martin en de pagina's van al zijn 15 producten en bundels (verkoopblokken en "published").
- Eerdere meting Olaf, 8 nov: `platformen/blender-2/data/superhive-print-2026-11-08.jsonl` (TrueDepth toen al 6900+, prijs $25, 57 reviews).
- YouTube, kanaalpagina's met curl (aantallen afgerond zoals YouTube ze toont), 16 nov: zijn eigen kanaal https://www.youtube.com/@TheBlenderAcademy69 , Defonten https://www.youtube.com/@defonten , Gleb Alexandrov https://www.youtube.com/@GlebAlexandrov , 247 Creative Secrets https://www.youtube.com/@247creativesecrets . Titels via de oEmbed van YouTube.
- Creative Shrimp (Gleb Alexandrov), "True Depth Blender Add-on: A Complete Guide (V3)", 13 aug 2026: https://www.creativeshrimp.com/true-depth-blender-add-on-the-complete-guide-v3.html (links naar Superhive met `?ref=88`, een partnerlink).
- BlenderArtists, aankondiging V3 door Defonten, 25 jul 2026: https://blenderartists.org/t/1648658 (206 keer bekeken, 0 reacties, GEZIEN via de JSON van het forum).
- Een open kloon op GitHub die zegt de werkwijze van TrueDepth na te volgen: https://github.com/saranunt-0/2D-to-3D-TrueDepth
- Niet gelukt: archive.org (verbinding geweigerd vanuit de cloud), YouTube-videopagina's (geen beschrijving of datum te lezen), X. Geen interview, devlog of omzetcijfer van de maker gevonden (zoektocht 16 nov). Hoe hij de eerste kopers kreeg zegt hij nergens; wat hieronder staat over kanalen komt uit de reviews en de videocijfers.

### Cijfers
- **TrueDepth: 6900+ verkopen, 57 reviews (81% vijf sterren), "published almost 2 years ago"**, dus rond eind 2024 (GEZIEN 16 nov). Op 8 nov ook al 6900+ (GEZIEN Olaf), dus ±290 per maand gemiddeld over de hele looptijd (rekensom, Superhive telt in blokken).
- **Eén review per ±121 verkopen** (57 op 6900+, GEZIEN). Bij Kambari zagen we 1 op 50 tot 140; het past dus.
- **Prijs (GEZIEN 16 nov):** 1 persoon $25, 3 plaatsen $35, 10 plaatsen $85. Vóór V3 was het $15: twee reviews van 10 en 6 maanden geleden noemen "$15" (GEZIEN). Bij de grote gratis update V3 (zomer 2026) ging de prijs dus 67% omhoog, terwijl bestaande kopers alles gratis kregen.
- **Omzet (GOK):** 6900 verkopen grotendeels tegen $15, met korting en bundels, is ruwweg $90.000 tot $110.000 bruto in twee jaar; wat de maker daarvan houdt na het deel van Superhive weet ik niet. Hij noemt zelf alleen "Total donated: $1,571" aan de Blender Foundation (GEZIEN).
- **Zijn andere producten (GEZIEN 16 nov):** CinePack (camerabewegingen, ±6 jaar) 4000+, The Particle Library (±4 jaar) 1100+, True Fire (±5 jaar) 300+, PocketCam (27 dagen, $0 tot $69) 100+, OpacityFlow (3 maanden) 70+. Plus negen bundels, waarvan twee **met add-ons van andere makers**: Light Wrangler 3 + CinePack 100+ en Lens Sim + CinePack 100+. Bundels met alleen zijn eigen spullen: 20+ tot 200+.
- **Zijn eigen YouTube-kanaal: ±1.000 abonnees, 27 video's** (GEZIEN). TrueDepth-video's daar: 31.000 (installatie en demo, ±1 jaar), 27.000, 8.800 (V3), 2.800 en 1.200 weergaven.
- **Video's van anderen over TrueDepth (GEZIEN 16 nov):** Defonten (10.900 abonnees) maakte er 8, samen ±72.000 weergaven, waarvan "How to Install and Use TrueDepth V3" 36.000 en een eerdere installatievideo 20.000. Gleb Alexandrov (242.000 abonnees) "True Depth 3.0 for Blender - Complete Guide" 25.000, plus eerder een bas-reliëfvideo met TrueDepth en een geschreven gids met partnerlink. 247 Creative Secrets 1.600. Samen dus meer weergaven dan op zijn eigen kanaal.

### Wat hij deed, in volgorde (voor zover te zien)
1. **Eerst een andere niche, jaren eerder.** CinePack (2020) verkocht 4000+ aan mensen die filmische camerabewegingen willen. Zijn kanaal bleef klein; de best bekeken video is die van CinePack (33.000).
2. **Eind 2024: TrueDepth voor $15**, op het moment dat open dieptemodellen (Depth Anything V2) goed genoeg werden. De belofte in één regel: "Turn any image ... into 3D, with AI, right inside Blender", lokaal, zonder abonnement. Kopers vergelijken het in hun reviews zelf met de duurdere of omslachtige weg: VistaSculpt (abonnement, alleen Windows), Nomad Sculpt, ComfyUI, de Displace-modifier van Blender (GEZIEN in reviews).
3. **Andere makers maakten de uitleg.** Defonten maakte vanaf ±jan 2026 installatie- en gebruiksvideo's en kondigde V3 aan op BlenderArtists alsof het zijn eigen product is ("the latest update ... is officially here"). Of hij betaald wordt of meewerkt weet ik niet (GOK; een review noemt "the creator and maintainer", en Martin schrijft "we"). Gleb Alexandrov schreef een gids met een partnerlink van Superhive (`?ref=88`, GEZIEN): hij verdient dus aan elke verkoop via zijn link. Twee kopers schrijven hoe ze het vonden: "after seeing a random YouTube video about it" en "by chance, I came across a random blog that mentioned this Blender add-on" (GEZIEN).
4. **Installeren was het grootste probleem.** Van de 13 kritische reviews die ik las gaan er 5 over installeren of afhankelijkheden (de sterren per review staan niet in de tekst), en ook veel vijfsterrenreviews noemen "had an issue with installation ... solved quickly" (GEZIEN). In V3 bouwde hij het opnieuw: het AI-model downloaden in Blender met een voortgangsbalk, modellen apart bewaard zodat een update ze niet wist, en "self-healing settings". De twee best bekeken video's over het product (31.000 en 36.000) zijn installatievideo's.
5. **Zomer 2026: V3 gratis voor alle kopers, prijs naar $25**, met drie nieuwe modi, waaronder een paneel voor 3D-printen (waterdicht model, maat in mm, STL voor Bambu Studio, PrusaSlicer en Cura). Zo kwam hij ook in de printhoek, waar wij zitten. Kopers zeiden het zelf: "BOOM new features all over the place ... With Superhive and some authors trying to reduce support this was an amazing bonus" (GEZIEN). Wachten kostte wel: "seriously where is update in this 5 months?" (GEZIEN).
6. **Antwoorden op bijna elke review, ook de slechte**, meestal met uitleg en een vraag om de afbeelding op te sturen. Op "can be easily done for free using ComfyUI" antwoordt hij: "The value here is the Integration Directly within Blender, no need to leave the program." Soms kortaf: "Thousands of others have had no issue installing this" (GEZIEN).
7. **Nu: steeds nieuwe kleine add-ons en bundels.** PocketCam (okt 2026) met een gratis klasse ($0) naast betaalde, 100+ in 27 dagen; bundels met zijn eigen producten en met die van andere makers.

### Drie lessen
1. **De grootste verkoper in onze hoek kreeg zijn bereik via de video's van anderen, niet via zijn eigen kanaal.** Zijn kanaal heeft ±1.000 abonnees; video's van Defonten en Gleb Alexandrov over TrueDepth haalden samen ±97.000 weergaven, en een grote maker linkte met een partnerlink van Superhive. Dit is de derde keer dat we dit zien, na McGybeer (filmpjes van printerbezitters en Snapmaker, Joris) en de taakbalkspellen (verzamelvideo's van anderen, Fenna).
2. **"Hoe installeer en gebruik je X" is de video die bekeken wordt, en installeren is waar de slechte reviews vandaan komen.** De twee best bekeken TrueDepth-video's zijn installatievideo's; ruim een derde van de kritische reviews gaat over installeren. Hij loste het op in het product (download in Blender, zelfherstel) en niet alleen met uitleg.
3. **Een grote gratis update maakt van bestaande kopers aanbevelers en rechtvaardigt een hogere prijs.** Van $15 naar $25 bij V3, met plaatsen voor 3 en 10 mensen, en bestaande kopers kregen alles gratis. Bij elke vraag "kan dit niet gratis?" noemt hij één ding: het zit in Blender, in één klik. Hetzelfde verhaal als Click Joints Pro tegenover voegen met de hand.

### Eerlijk: wat niet zomaar voor ons geldt
- Zijn product heeft een "wauw"-beeld (een foto wordt 3D) dat zich vanzelf laat filmen; een kogelgewricht is minder spectaculair, tot je de figuur ziet bewegen.
- Hij had al zes jaar een winkel met 4000+ kopers van CinePack en dus een naam op Superhive toen TrueDepth uitkwam. Hoeveel van de eerste kopers daarvandaan kwamen weet ik niet.
- Of Defonten betaald werd of meebouwt, weet ik niet. Als hij meebouwt, is "anderen maakten de video's" minder sterk dan het lijkt.
- De verkoopblokken op Superhive geven geen tijdlijn; ik weet niet hoe snel de eerste 100 kwamen.

### Voorstel voor Dortus deze week
**Wie:** Chris maakt het klaar (`commercie/blender-click-joints/`), Hans beslist, Thijs verstuurt; Bram levert één installatie- en gebruiksvideo.
**Wat:** (1) Zodra Click Joints Pro live staat: een korte mail aan twee of drie middelgrote Blender-YouTubers die al uitlegvideo's maken over betaalde add-ons of 3D-printen (zoals Defonten, 10.900 abonnees, 36.000 weergaven op één installatievideo), met een gratis Studio-licentie en de vraag of ze er een eerlijke video over willen maken, met hun eigen partnerlink van Superhive als ze die hebben. Dat staat nu als plek 9 in `verspreiding.md` met "na dag 14, besluit Hans nodig"; dit verhaal is het bewijs om dat naar de lanceerweek te halen. (2) Bram maakt een video "How to install and use Click Joints Pro" van 2 tot 4 minuten (installeren, een figuur, kogel en scharnier, printen), naast de demofilm. Kost geen geld; de licenties zijn gratis voor ons.

---

## 5. BashSupport Pro (Joachim Ansorg, solo, Duitsland, betaalde taalplugin voor Bash en Zsh in JetBrains-IDE's)

Onderzocht 16 nov 2026, run 4. Waarom dit verhaal: JetBrains is ons eerste betaalde doel (6 dec), en Bison & Flex is net als dit een betaalde taalplugin naast een gratis alternatief. BashSupport Pro is de bekendste betaalde taalplugin van een solomaker, en de maker schrijft zelf openlijk over elke stap. Geen cursusverkoper: hij verkoopt de plugin en plugin-werk voor klanten, geen cursus.

### Bronnen
- Marketplace-API, met curl gelezen 16 nov 2026: https://plugins.jetbrains.com/api/plugins/13841 (Pro), `/api/plugins/4230` (oude gratis BashSupport), `/updates`, `/comments` en `/rating` van beide.
- Zijn eigen nieuwsberichten, met curl gelezen 16 nov: https://www.bashsupport.com/news/ , vooral "BashSupport's future" (18 jul 2019), "Current status of BashSupport Pro" (20 nov 2019), "BashSupport Pro released" (26 feb 2020), "1.3 and future of open-source BashSupport" (2 jun 2020), "1.4, now standalone" (18 jul 2020), "Pricing Update" (8 apr 2024), "Celebrating six years" (24 mrt 2026).
- Prijspagina en vergelijkingspagina, 16 nov: https://www.bashsupport.com/pricing/ en https://www.bashsupport.com/features/
- Interview uit 2018 (vóór Pro, over hoe hij begon): https://tomassetti.me/jetbrains-plugins/
- Zijn bedrijfssite: https://www.j-a.dev/
- Niet gevonden: omzet of aantal kopers. Hij noemt ze nergens, ook niet in interviews (zoektocht 16 nov). Alles over geld hieronder is dus GOK of afgeleid.

### Cijfers
- **Pro: 624.199 downloads, 63 reviews, cijfer 5 (59 keer 5 sterren, 1 keer 4)** (GEZIEN, API 16 nov). Downloads tellen updates mee.
- **Oude gratis BashSupport: 14.499.371 downloads, 118 beoordelingen** (GEZIEN). Pro staat dus op 4,3% van de downloads van de gratis voorganger (rekensom). In onze eigen marktmeting (`platformen/jetbrains/marktmeting-2026-11-06.md`) staat Nginx op dezelfde orde: betaald ±10% van gratis.
- **Eén review per ±10.000 downloads**, en 22 van de 63 reviews kwamen in 2020, het jaar van de overstap (GEZIEN, telling per jaar: 2020 22, 2021 15, 2022 3, 2023 11, 2024 5, 2025 3, 2026 4).
- **Werk: "close to 4,500 hours" in zes jaar**, dus ±750 uur per jaar (EIGEN OPGAVE, bericht 24 mrt 2026). **94 builds op de Marketplace tussen 19 nov 2024 en 6 nov 2026** (GEZIEN), vaak in paren voor twee IDE-lijnen, dus ±47 echte versies in twee jaar: ongeveer elke twee weken een update. 236 meldingen in zijn openbare issue-tracker op GitHub (GEZIEN via zoek-API).
- **Gebruikers nu (GOK):** de laatste versie (5.0.13, 6 nov) haalde in 10 dagen ±3.000 downloads over twee builds (GEZIEN); alle builds van 2025 samen 90.854. Dat wijst op enkele duizenden actieve installaties, inclusief proefgebruikers. Hoeveel er betalen weet niemand buiten JetBrains.
- **Prijs (GEZIEN 16 nov):** persoonlijk $39 per jaar of $3,90 per maand, zakelijk $99 per jaar of $9,90 per maand. Tweede jaar ±20% goedkoper, derde jaar ±40%. Na 12 maanden een blijvende licentie (fallback). Proef 30 dagen zonder registratie. Gratis voor open bron en onderwijs via JetBrains. Volumekorting voor bedrijven vanaf 10 licenties.
- **Prijs bij de start (feb 2020 tot jun 2024): $23 persoonlijk, $68 zakelijk per jaar** (GEZIEN, bericht 8 apr 2024). In nov 2019 noemde hij nog "$10 to $20 per year" voor persoonlijk. Na ruim vier jaar ging de prijs 70% omhoog.

### Wat hij deed, in volgorde
1. **2009: een gratis plugin voor een wedstrijd.** BashSupport won de eerste prijs van een plugin-wedstrijd van JetBrains (±$8.000, zegt hij in het interview). Daarna tien jaar gratis en open source, in zijn vrije tijd. Hij werd "the most widely used community plugin": de laatste versie alleen al meer dan 1 miljoen downloads (EIGEN OPGAVE, jul 2019).
2. **Jul 2019: JetBrains stopt een gratis Shell-plugin in elke IDE.** Dat botste met zijn plugin. Hij schreef meteen en eerlijk wat hij ging doen: "I'm not planning to compete with JetBrains's offering", de gratis plugin gaat in onderhoud, en een betaalde Pro komt bovenop die van JetBrains. Hij gaf ook toe dat een miljoen gebruikers als hobby niet meer ging.
3. **Nov 2019: vooraf vertellen wat Pro doet en ongeveer kost.** De eerste versie draait om één ding dat JetBrains niet had: een debugger. Prijs "most likely in the range of $10 to $20 per year", zakelijk duurder. Testers konden zich melden. Een nieuwsbrief op elke pagina.
4. **26 feb 2020: Pro 1.0 op de Marketplace**, acht maanden na de start van betaalde plugins daar (JetBrains begon op 26 jun 2019 met 10 betaalde plugins, in jul 2020 waren het er 46: DERDEN, JetBrains-blog). Hij zat er dus vroeg bij.
5. **De gratis plugin als wegwijzer.** In de beschrijving van de oude BashSupport (14,5 miljoen downloads) staat nog steeds: gestopt, gebruik BashSupport Pro, "attractively priced starting at 2.30 USD per month", met drie zoete redenen: 30 dagen proef, **25% korting tot 1 okt 2020 met de code BASHSUPPORT_THANKS**, en je oude instellingen werken gewoon (GEZIEN). Wie vroeger iets bijdroeg kreeg een gratis licentie. JetBrains staat zo'n verwijzing in een beschrijving dus toe (anders dan extensions.blender.org, zie besluit Bram 15 nov).
6. **Jun 2020: de gratis plugin stopt echt** (geen versie meer voor 2020.2). Tegelijk maakte hij Pro beter dan de oude ("superior to the old BashSupport plugin"), zodat overstappen geen stap terug was. In 2020 kwamen 22 van zijn 63 reviews.
7. **Jul 2020: los van JetBrains' plugin.** Bovenop de gratis Shell-plugin bouwen werkte niet: elke reparatie moest via JetBrains en duurde tot 4 maanden. Pro werd een eigen, complete plugin, met de oude instellingen van beide plugins nog bruikbaar.
8. **2021 tot 2025: steeds verder van wat gratis is.** Testrunner (bats-core), scripts op een andere machine draaien en debuggen, hernoemen, Zsh (versie 5.0, aug 2025), eigen opmaker. Een vergelijkingspagina met vinkjes tegen de gratis Shell van JetBrains én tegen VS Code (GEZIEN). Bijna alles waar je voor betaalt is iets wat de gratis plugin bewust niet doet.
9. **Apr 2024: prijs omhoog, netjes.** Twee maanden vooraf aangekondigd, wie wilde kon tot drie jaar vooruit betalen tegen de oude prijs, de korting voor trouwe klanten bleef, en "I don't like this" had een eigen kopje met een mailadres. Nieuw: volumekorting voor bedrijven.
10. **Mrt 2026: zes jaar, actie met de prijs van 2020** voor een maand. Hij verkoopt ook plugin-werk voor klanten (j-a.dev), en zegt daar dat AI-agents nu een deel van het werk aan zijn plugins doen.

### Drie lessen
1. **De betaalde plugin verkoopt precies wat de gratis plugin van de grote speler niet doet, en laat dat zien in een tabel.** Een debugger, een testrunner, op afstand draaien: werk dat JetBrains voor een gratis plugin niet gaat doen. Gewoon kleuren en aanvullen gaf hij bewust op ("I'm not planning to compete"). Dit is de tweede keer na Copilot dat het betaalde deel iets is wat de gebruiker niet zelf of gratis heeft.
2. **Het publiek kwam eerst, gratis, en jaren lang.** Tien jaar en 14,5 miljoen downloads gratis, daarna een betaalde opvolger die nu op 4,3% van die downloads staat. Bij de overstap gebruikte hij zijn gratis plugin als bord naar Pro, met korting en proef. Wij hebben bij Bison & Flex geen eigen gratis publiek; het gratis alternatief (Bison Language Support, 13.020 downloads, GEZIEN 8 nov in `commercie/jetbrains-bison-flex/indienen.md`) is van iemand anders. Met dezelfde verhouding is dat ±560 downloads voor een betaalde Bison-plugin in totaal, over jaren (GOK, en downloads zijn geen kopers).
3. **Rustig en lang volhouden, met eerlijke prijsstappen.** Laag begonnen ($23), na ruim vier jaar omhoog naar $39, met vooruitbetalen tegen de oude prijs, korting in jaar 2 en 3, en een blijvende licentie na een jaar. Elke twee weken een update, zes jaar lang, 4.500 uur. Zakelijk kost 2,5 keer persoonlijk (past in hoofdles 1).

### Eerlijk: wat niet zomaar voor ons geldt
- Hij had tien jaar naam en een miljoen gebruikers vóór hij iets vroeg. Dat valt niet te kopiëren; wij starten bij 0.
- Bash wordt door bijna elke ontwikkelaar gebruikt. Bison en Flex door een klein deel (compilervakken, oudere C-projecten). De markt is vele malen kleiner (GOK, niet gemeten).
- Of hij ervan kan leven weten we niet. Dat hij ook klantwerk verkoopt en in 2024 de prijs verhoogde "to let us keep working on BashSupport Pro" wijst erop dat de plugin alleen misschien niet genoeg is (GOK).
- Hij beantwoordt maar 9 van de 63 reviews op de Marketplace (GEZIEN). Hulp loopt via zijn forum en issue-tracker. Dat gaat tegen hoofdles 2 in; zijn cijfer is toch 5.

### Voorstel voor Dortus deze week
**Wie:** Chris (winkeltekst, `commercie/jetbrains-bison-flex/`), met Jet voor de feiten; zodra Bison & Flex zichtbaar is.
**Wat:** een vergelijkingstabel zoals die van BashSupport Pro, met vinkjes in drie kolommen: Bison & Flex Pro, Bison & Flex gratis, en Bison Language Support (het gratis alternatief, 13.020 downloads). Alleen rijen die waar zijn en die een koper merkt (bijvoorbeeld het werk tussen scanner en grammatica en de meldingen, als Jet bevestigt dat de ander dat niet heeft). Zet hem op dortus.com bij Bison & Flex en een korte versie in de Marketplace-beschrijving, met de link. Zet onder de prijs dezelfde zin als Ansorg: wie een gratis licentie voor onderwijs of open bron gebruikt, wordt gevraagd om een review. Reviews zijn schaars (bij hem 1 op de 10.000 downloads), en studenten zijn bij Bison en Flex waarschijnlijk een grote groep (GOK, staat ook al in `indienen.md`). Kost een uur, geen geld, geen nieuwe code.
**Voor Jet, ter info:** reken op dag 30 niet met de 2 tot 5% uit `doelen.md`. Een betaalde taalplugin naast een gratis plugin haalt in de twee gevallen die we kennen 4 tot 10% van de downloads van de gratis plugin (BashSupport, Nginx), en dat over jaren.

---

## 4. Copilot for Obsidian (Logan Yang, Brevilabs, twee vaste bouwers, AI-plugin met abonnement en levenslange licentie)

Onderzocht 16 nov 2026, run 3, opdracht van de hoofdchat ("een Obsidian-plugin met betaalde extra's die echt verkoopt, zodat we zien wat Rollwright mist"). Waarom dit verhaal: de enige betaalde Obsidian-plugin waarvan de omzet openbaar en gecontroleerd is, maand voor maand. Geen cursusverkoper: de cijfers komen rechtstreeks uit Stripe.

### Bronnen
- TrustMRR, profiel Brevilabs, met curl gelezen 16 nov 2026 (03:20 NL-tijd), ook de machineleesbare versie: https://trustmrr.com/startup/brevilabs en https://trustmrr.com/startup/brevilabs.md. TrustMRR haalt de omzet zelf op met een Stripe-sleutel van de maker ("Revenue is verified with Stripe API key", laatst bijgewerkt 15 nov 2026 20:51 UTC). De tekst over het bedrijf op die pagina is wel door de maker of TrustMRR zelf geschreven en niet gecontroleerd.
- Prijspagina, 16 nov: https://www.obsidiancopilot.com/en/pricing
- Bedrijfssite, 16 nov: https://brevilabs.com/
- De openbare code en de hele geschiedenis (git clone zonder bestanden, 16 nov): https://github.com/logancyang/obsidian-copilot. Daaruit de data van commits, tags en wie wat schreef.
- Downloads: `community-plugin-stats.json`, eerder gemeten door Olaf in `platformen/obsidian/volgend-product.md` (Copilot 3.340.702 in totaal).
- Tegenvoorbeeld: een maker met een eenmalige, offline Pro-licentie zoals Rollwright, DEV 19 jun 2026 (0 reacties): https://dev.to/ibrh96prog/im-not-a-software-engineer-but-i-shipped-an-obsidian-plugin-with-zero-servers-and-offline-4i14. Op Indie Hackers staat een bericht met de titel "Shipped my 7th one-time-purchase Obsidian plugin. Real numbers: ~7 views/day, 2 sales total" (https://www.indiehackers.com/post/shipped-my-7th-one-time-purchase-obsidian-plugin-real-numbers-7-views-day-2-sales-total-distribution-is-the-whole-problem-9a46ab4295). Alleen de titel gezien (Cloudflare blokkeert curl), dus wie het schreef en wat erin staat weet ik niet.
- Niet gevonden: een interview of blog van Logan Yang over hoe hij de eerste betalers kreeg (zoektocht 16 nov). FirstMRR heeft een stuk over Brevilabs, maar die site lag eruit (503).

### Cijfers
**Omzet, GEZIEN via TrustMRR (Stripe), alle bedragen bruto in dollars:**

| Periode | Omzet |
|---|---|
| Alles sinds de start | $926.038 |
| Laatste 12 maanden | $468.348 |
| Laatste 6 maanden | $177.538 |
| Laatste 3 maanden | $78.331 |
| Laatste 30 dagen | $19.286 (-17,3%) |

Per maand: dec 2025 $53.160, jan 2026 $55.789, **feb 2026 $66.646 (top)**, mrt $35.096, apr $34.309, mei $38.223, jun $36.054, jul $29.259, aug $33.873, sep $32.590, **okt $18.994**, nov tot en met de 15e $10.084.
- MRR (vaste maandomzet uit abonnementen) $17.600, **1.336 actieve abonnementen**, winstmarge 95% (GEZIEN, TrustMRR).
- Vóór december 2025 (jan tot nov 2025): $926.038 min $468.348 is **±$458.000 in ±11 maanden**, gemiddeld ±$42.000 per maand (rekensom op GEZIEN).
- **Let op:** het is de hele Stripe van Brevilabs, niet alleen Copilot. Brevilabs verkoopt ook advieswerk ("a four-week, $45k AI product sprint", GEZIEN op brevilabs.com) en twee nieuwere producten (Miyo en OpenArtifacts). Hoeveel daarvan in de omzet zit, is niet te zien. Copilot is wel het oudste en grootste product (GOK dat het meeste van Copilot komt).

**Prijzen nu (GEZIEN 16 nov):** Free $0 (eigen API-sleutel, lokale modellen, je eigen Claude- of ChatGPT-abonnement, zonder account). Plus $14,99 per maand of $139,99 per jaar (gehoste modellen, betere webzoeker, meerdere agents tegelijk). **Supporter $349,99 eenmalig**, doorgestreept van $499,96: twee jaar Plus, levenslang Miyo en OpenArtifacts, levenslang zelf hosten, vroege toegang, 15% extra tegoed. Terugbetalen binnen 14 dagen.

**Downloads:** 3.340.702 in totaal (Olaf, community-plugin-stats). De prijspagina zegt zelf "2.5M". Downloads tellen ook updates mee, dus het aantal echte gebruikers is veel lager (GOK, hoeveel weet niemand buiten Obsidian).

**Rekensom die ertoe doet (GOK op GEZIEN):** 1.336 abonnementen op 3,34 miljoen downloads is **0,04% per download**. ±$20.000 per maand op 3,34 miljoen downloads is ±$0,006 per download per maand. Neem je aan dat 1 op de 10 downloads een echte, actieve gebruiker is (GOK), dan betaalt 0,4% van de gebruikers een abonnement. Dat is 5 tot 12 keer minder dan de 2 tot 5% in het rekenvoorbeeld van `organisatie/doelen.md`. En dit is de meest gedownloade AI-plugin van Obsidian, met een betaalde laag die echt iets levert.

### Wat ze deden, in volgorde (uit de code en de pagina's)
1. **Maart 2023: gratis en open source, met je eigen OpenAI-sleutel.** Eerste commit 30 maart 2023, vier maanden na ChatGPT. 119 commits in april 2023. Hij zat vanaf dag één op de golf.
2. **Twintig maanden alleen gratis.** Van maart 2023 tot november 2024 geen betaalde laag. In die tijd werd het de grootste AI-plugin van Obsidian.
3. **Oktober 2024: een tweede vaste bouwer** (Zero Liu, eerste commit 26 okt 2024). Sinds half april 2026 schrijft die het meeste: 568 commits tegen 93 van Logan Yang (GEZIEN in de git-geschiedenis). Dit is dus geen solomaker meer.
4. **21 nov 2024: Copilot Plus als alfa voor testers. 15 jan 2025: bèta voor iedereen.** Brevilabs is opgericht in januari 2025 (TrustMRR). De betaalde laag verkoopt wat de gebruiker niet zelf heeft: gehoste modellen en eigen zoek- en embeddingmodellen ("copilot-plus-small", "copilot-plus-large", "copilot-plus-flash"), webzoeken, plaatjes in de chat. Gratis blijft alles wat met je eigen sleutel kan.
5. **5 feb 2025: een "believer"-klasse** met een eigen model alleen voor hen (commit "Add believer exclusive model"). Dat is de voorloper van de huidige Supporter van $349,99 eenmalig. De ±$42.000 per maand in 2025 met nu maar $17.600 MRR wijst erop dat een groot deel van het geld uit eenmalige levenslange licenties kwam (GOK, de verdeling toont TrustMRR alleen na inloggen).
6. **Aug 2025: Plus uit de bèta, met een agent.** Daarna versie 3 (aug 2025) en elke maand tientallen commits.
7. **Feb 2026: de top, daarna gehalveerd.** Van $66.646 in februari naar $35.096 in maart. Waarom zegt niemand. Mijn GOK: jaarabonnementen van de bèta-kopers van jan en feb 2025 verlengden in jan en feb 2026, en een deel stopte daarna.
8. **2026: de golf keert.** Gratis plugins die Claude Code en Codex in de kluis zetten groeien het hardst (Claudian 300.668 downloads in 30 dagen, Agent Client 34.048, gemeten door Olaf, `volgend-product.md`). Copilot volgt: **versie 4.0 op 11 aug 2026 met OpenCode, Claude Code en Codex**, en op de prijspagina staat nu bij Free "Use your Claude or ChatGPT subscription". Dat haalt een reden weg om Plus te kopen. Twee maanden later, in oktober, zakt de omzet van $32.590 naar $18.994. Of dat oorzaak en gevolg is, weet ik niet (GOK).
9. **Nu: breder dan één plugin.** Brevilabs zet Miyo (lokale contextdienst) en OpenArtifacts naast Copilot, stopt die in de Supporter-licentie, en verkoopt advieswerk. In de README vraagt Copilot alle gratis gebruikers om een gratis account en de Discord ("Sign up free and join our Discord"): een lijst van gebruikers die ze later iets kunnen aanbieden.

### Drie lessen
1. **Eerst groot gratis, pas daarna betalen, en dan alleen voor wat de gebruiker zelf niet heeft.** Twintig maanden gratis tot het de grootste AI-plugin was, daarna een betaalde laag met gehoste modellen. Zelfs dan betaalt maar 0,04% per download een abonnement. Bij Rollwright (40 downloads, skins van $6) is de verwachte verkoop met die verhouding nul. Dat ligt dus niet aan de skins of de betaalweg, maar aan het bereik.
2. **Eén dure eenmalige klasse brengt veel geld.** Supporter $349,99 (eerst "believer") naast $14,99 per maand. Dit past in hoofdles 1 (meer dan één prijs). Het verschil met Cleave en CatPin: hier is de duurste klasse 23 keer de maandprijs, niet $5 tot $13 extra. De top van $66.646 in één maand haal je niet met abonnementen van $14,99 alleen (GOK: dat zijn ±4.400 maandabonnementen, terwijl er nu 1.336 zijn).
3. **Een betaalde laag die AI doorverkoopt kan snel leeglopen.** Toen gebruikers hun eigen Claude- of ChatGPT-abonnement konden gebruiken (gratis plugins, en daarna Copilot zelf), viel de omzet van ±$42.000 per maand in 2025 naar ±$20.000 nu. Ook de grootste maker moest volgen en zijn gratis deel ruimer maken. Wat je verkoopt moet iets zijn wat een abonnement elders niet ook al geeft.

### Eerlijk: wat niet zomaar voor ons geldt
- Copilot is een AI-product in de drukste hoek. Mensen betalen voor AI meer en vaker dan voor dobbelstenen (GOK). De verhouding 0,04% is voor Rollwright eerder te gunstig dan te streng.
- De omzet is van heel Brevilabs, inclusief advieswerk dat $45.000 per opdracht vraagt. Eén opdracht zou al een maand vertekenen. Ik zie geen pieken van die grootte per dag (hoogste dag in de laatste 30: $1.562), maar voor eerdere maanden kan ik het niet uitsluiten.
- Downloads zijn geen gebruikers. De 0,4% per gebruiker is een GOK op een GOK.
- Twee vaste bouwers sinds eind 2024, ex-Google en ex-Uber (zegt de eigen site). Dat is meer menskracht dan een solomaker.

### Wat Rollwright mist (de vraag van de hoofdchat)
Niet de betaalweg en niet de skins zelf: die zijn er en werken (Polar, $6, offline na de controle). Wat mist, in volgorde:
1. **Bereik.** Copilot had miljoenen downloads voor het iets vroeg. Rollwright heeft er 40 (Olaf, 15 nov). Met de verhouding van Copilot zijn voor €350 per maand ±60.000 tot 70.000 downloads nodig (GOK: $400 / $0,006). Met eenmalige skins van $6 eerder meer.
2. **Een betaalde kant die iets doet wat gratis niet kan.** Copilot verkoopt rekenkracht en modellen. Skins zijn uiterlijk; dat werkt in spellen (Rusty's Supporter Pack, 11% bij Fenna), maar daar is het spel zelf al gekocht of gespeeld door tienduizenden.
3. **Een lijst van gratis gebruikers.** Copilot vraagt elke gebruiker om een gratis account en Discord. Rollwright heeft niets waarmee we gebruikers later kunnen bereiken, behalve de forumdraad (19 keer bekeken).
4. **Een dure eenmalige klasse.** Kan erbij, maar heeft pas zin met bereik.

### Voorstel voor Dortus deze week
**Wie:** Olaf (Obsidian-manager), in `platformen/obsidian/volgend-product.md`; Hans kijkt het na bij de volgende weekkeuze.
**Wat:** een vaste verdientoets voor elk kandidaat-product op Obsidian, vóór er gebouwd wordt, met de enige gecontroleerde verhouding die we hebben: **±$0,006 omzet per download per maand, 0,04% abonnees per download** (Copilot, Stripe via TrustMRR, 16 nov 2026). Per kandidaat drie regels: (a) hoeveel downloads haalt de beste plugin in die hoek per maand (GEZIEN in de stats), (b) wat levert dat op met die verhouding, (c) wat zit in de betaalde laag dat de gebruiker niet al gratis of via een eigen abonnement heeft. Komt (b) voor de hele hoek onder €350 per maand, dan geen betaald product in die hoek. Kost Olaf een halfuur, en voorkomt een tweede Rollwright. Voor Rollwright zelf: geen werk meer aan betaalde skins tot er minstens een paar duizend downloads zijn; die tijd naar bereik of naar een ander product.
**Voor de hoofdchat, ter info:** het rekenvoorbeeld in `organisatie/doelen.md` gaat uit van 2 tot 5% betalende gebruikers. De grootste betaalde Obsidian-plugin zit op ±0,4% (GOK op GEZIEN). Dat is een vraag voor Thijs, niet voor mij, want doelen.md is van hem.

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
- De categorie "model splitsen voor printen" is druk: Dovetail Key (Kambari, met publiek) 800+, CatPin 400+, Split 3D Print 400+ (teller telt ook gratis downloads; bijgesteld in verhaal 8: "Sales" telt waarschijnlijk alleen betaald), Cleave 100+, Split It 10+, Easy Print 10, Printsplitter, Cut and Key en PrintForge geen blok (onder 10). Cleave is de enige nieuwkomer van de laatste 2 maanden boven de 10+.

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
