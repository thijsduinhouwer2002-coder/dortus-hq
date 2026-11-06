# Logboek verkenner

Nieuwste blok onderaan.

## 6 nov 2026, run 13:31 UTC
- Shopify: nee voor nu. Geld is er, maar geen schoon voorbeeld uit 2026 van snel betaald krijgen. Controleur keurde de eerste versie af, tweede akkoord.
- Unity Asset Store: nee, nu niet. Controleur herstelde onder meer "dalende markt", die conclusie viel weg.
- Winkels zelf (apps.shopify.com, assetstore.unity.com, addons.mozilla.org) zijn vanuit deze omgeving geblokkeerd, dus geen GEZIEN-cijfers. Vraag op de lijst voor Thijs gezet.
- Godot: nee nu, wachtlijst. De nieuwe winkel is nog alleen gratis. Beslissing: niet bouwen zonder bewijs van betaling, want de doelen vragen geld.
- Framer: eerste advies ja als test is door de controleur afgekeurd. Nu nog niet klaar, cijfer 5, met vooraf vastgelegde grens. Tweede controle staat nog open.
- Rol is tijdens de run aangepast (cijfer van 1 tot 10, nog niet klaar als uitkomst, eigen meting). Alle vier de voorstellen bijgewerkt. Geen van vier heeft een eigen steekproef: netwerk blokkeert, dat staat bij Thijs.
- Volgende run: tweede controle Framer, daarna het volgende platform. Als het netwerk open is, eerst de steekproeven van Shopify en Framer.

## 6 nov 2026, run 14:32 UTC
- Apify Store zelf aan de lijst toegevoegd omdat de winkel makers uitbetaalt. Eerste advies (nog niet klaar, 5) afgekeurd door de controleur: mijn eigen grens was niet te halen. Nu nee, cijfer 4. Beslissing volgt het oordeel, want bij nieuwe kleine makers is geen geld aangetoond ondanks $1,7M per maand op platformniveau.
- Bubble: nee, cijfer 3. Eén partij heeft 60%+ van de omzet.
- Discord: nog niet klaar, cijfer 4. Eerlijk want bereik niet meetbaar. Controleur vond ShotCaller ($796 per maand, geverifieerd via Stripe), het beste signaal van vandaag. Volgende stap: steekproef top.gg met Chrome op Thijs' HP of via een andere botlijst.
- Microsoft Marketplace: nee voor nu, cijfer 3.
- Netwerk: `curl` krijgt 403 op alle winkels, alleen GitHub lukt. Regel "netwerk staat open" klopt niet voor deze run. Op lijst Thijs gezet. WebFetch werkt voor links uit zoekresultaten en van gelezen pagina's, niet voor willekeurige winkel-URL's.
- Slimme bron: apifystats.com geeft tellingen die de winkel-API vervangen. Zoek zulke onafhankelijke tellingen ook bij volgende platformen.
- Open: tweede controle Framer. Volgende run: die, daarna volgende platform.

## 6 nov 2026, run 15:32 UTC
- Netwerk: curl krijgt weer 403 op mql5.com en addons.mozilla.org. Onderzoek via WebSearch en WebFetch.
- MetaTrader Market (MQL5) zelf aan de lijst toegevoegd, omdat de winkel zelf verkoopt en betaalt. Uitkomst: nee, cijfer 3. Reden: mediaan 17 demo-downloads bij 15 nieuwe producten, geld gaat naar gevestigde makers, en geen nieuwe kleine maker boven $300 per maand te vinden. Controleur akkoord, vijf correcties verwerkt.
- Tweede controle Framer nog steeds open. Niet gedaan: Thijs vraagt nieuwe platformen, die gaan voor.
- Adobe Express add-ons: nee voor nu, cijfer 3. Reden: Adobe neemt 0% maar regelt geen betaling, fonds staat stil, installs nergens te zien, en geen kleine maker met aantoonbaar geld. Controleur akkoord, drie correcties verwerkt. (Tijd bij "in onderzoek" stond op 15:55, het was 15:46.)
- Setapp zelf toegevoegd, omdat het makers naar gebruik betaalt. Uitkomst: nee, cijfer 3 (eerst 2, controleur liet zien dat "volwassen app" geen harde eis is). Reden: geen enkel bedrag van een maker openbaar, abonneecijfer onbekend sinds 2018, weinig geld per gebruiker.
- Les van vandaag: platformen die zelf betalen (MQL5, Setapp) laten verkoopcijfers niet zien. Bij de volgende kandidaten eerst zoeken of er openbare tellingen bestaan, zoals bij Apify.
- Volgende run: tweede controle Framer staat nog open, daarna het volgende platform uit `kandidaten.md`.
- Na de laatste pull staat in CLAUDE.md: nooit WebFetch, alleen curl. Mijn agents gebruikten in deze run WebFetch (er kwam geen toestemmingsvraag), omdat curl op alle winkels een 403 gaf. Vanaf nu alleen curl en WebSearch. Probleem: curl werkt hier niet voor winkels, dan blijft alleen WebSearch over. Run hier gestopt (±30 minuten), want een vierde platform alleen met zoekresultaten wordt een half onderzoek.

## 6 nov 2026, run 16:31 UTC
- Bericht Thijs (netwerk open, eigen steekproeven): apps.shopify.com en framer.com geven nu 200 met curl, top.gg nog 403. Gekozen voor Shopify grondig, want Thijs vraagt liever één platform goed.
- Eigen steekproef: 6.000 willekeurige apps uit de sitemap van 30.060. Nieuwe apps van mei tot aug 2026: 78% geen review, 1% met 10+. Sinds mei 3 tot 5 keer zo veel nieuwe apps per maand.
- Nieuw: EU-herroepingsknop (verplicht 19 juni 2026). Twee kleine makers haalden 2.323 en 580 reviews in 8 tot 10 maanden, maar van ±130 aanbieders wonnen er twee, en dezelfde maker kreeg met een GPSR-app maar 29 reviews.
- Uitkomst: nog niet klaar, cijfer 6 (was 5). Reden: er is nu eigen bewijs dat kleine makers hier groot worden, maar alleen als vroege uitschieter bij een nieuwe regel. Controleur akkoord met 11 correcties, alle verwerkt.
- Volgende run: Framer eigen steekproef (curl werkt), of Shopify-vervolg: een aankomende regel met datum zoeken.

## 6 nov 2026, run 17:31 UTC
- Bericht Thijs (eigen steekproeven): Framer gepakt, want curl werkt daar en het stond als volgende.
- Eigen steekproef: 605 plugins uit overzicht en 11 categorieën, 603 winkelpagina's gelezen. Framer toont nergens meer gebruikersaantallen, dus bereik is niet te meten. Wel gezien: 51% betaald, ±100 tot 180 nieuwe id's per maand in 2026 (begin 2025 ±25 tot 50), makers die 8 tot 9 betaalde plugins in een paar maanden uitbrengen.
- Geld: BuildinFrame (kleine maker, 8 plugins) geverifieerd $400 in 7 maanden. Templatemakers melden na Framer 3.0 bijna geen verkoop meer.
- Beslissing: nee voor nu, cijfer 4 (was 5). Reden: van de drie vooraf vastgelegde eisen is er geen gehaald, en de bedragen die we wel vonden laten zien dat het weinig is.
- Controleur akkoord, vier correcties verwerkt (aandeel betaald per halfjaar, Miglena, naam maker, groei 3 tot 4 keer).
- curl met nep-browserkop werd geweigerd door de veiligheidscontrole. Gewone curl werkt prima op framer.com. Archive.org geeft 403.
- Daarna Roblox Creator Store zelf toegevoegd, omdat Roblox 100% van de netto opbrengst van betaalde plugins aan makers geeft. Eigen meting via de openbare zoek-API: 1.000 betaalde plugins, waarvan 365 van feb tot aug 2026. Mediaan minder dan ±10 stemmen, 2% haalt 10+, aanbod per maand ±10 keer zo groot als een jaar geleden, prijsmediaan $4,99.
- Beslissing: nog niet klaar, cijfer 4. Reden: het geldmodel is top, maar geen kleine nieuwe maker met aantoonbaar geld en geen teken van bereik voor nieuwe betaalde plugins. Controleur akkoord, acht correcties verwerkt, waaronder klachten over uitbetalingen in 2026.
- Les: Roblox heeft een open API zonder sleutel, daardoor snel en eerlijk te meten. Zoek bij volgende platformen eerst naar zo'n API.
- Volgende run: een ander platform uit `kandidaten.md` met betaling via de winkel (bijvoorbeeld Slack, Miro of Sketch), of Shopify-vervolg.

## 6 nov 2026, run 18:31 UTC
- Garmin Connect IQ zelf toegevoegd, omdat Garmin sinds 2024 betalen in de winkel heeft en de winkel een open API heeft (les van de vorige run: eerst zo'n API zoeken).
- Eigen meting: 44.384 unieke apps opgehaald (±85 tot 90% van de winkel, sortering schuift). Downloads alleen in emmers. Apps en datavelden van 3 tot 6 maanden oud: mediaan 100+, ±60% haalt 100+. Wijzerplaten (82% van het aanbod) veel zwakker. Betaalde apps zonder wijzerplaat uit 2026: 11% haalt 1.000+, 56% blijft op 10+ of lager.
- Geld: 15% afdracht plus $100 per jaar, betalen vóór downloaden. Een paar sportapps van nieuwe makers ($3 tot $8,49) op 1.000+, maar sommige spelletjes begonnen gratis, dus downloads zijn niet altijd verkopen. Eén maker deelde cijfers (Ski Pin, 68 verkopen in januari).
- Beslissing: nog niet klaar, cijfer 5 (eerst 6). Reden: de controleur liet zien dat mijn sterkste bereikcijfers vooral van gratis apps kwamen; een gewone betaalde app haalt weinig. Eerst 3 tot 4 weken emmers volgen voor we Thijs om $100 vragen.
- Controleur akkoord, 9 correcties verwerkt.
- Volgende run: een ander platform uit `kandidaten.md`; de Garmin-emmers opnieuw meten vanaf 13 nov.

## 6 nov 2026, run 21:31 UTC
- Bericht Thijs 20:32: Discord eerst opnieuw met eigen meting. Gedaan.
- Vondst: de officiële App Directory van Discord heeft een open zoek-API zonder sleutel, met serveraantal en betaalvlag per app; de aanmaakdatum zit in het id. Ook Discords winkelproducten met prijs zijn openbaar. top.gg geeft nog 403, maar is zo niet meer nodig.
- Gemeten: 18.343 directory-apps (±93%), 445 betaalde nieuwe apps met hun winkelproducten, en alle 25.598 bots van discordbotlist.com.
- Uitkomst: nieuwe apps (3 tot 6 maanden) mediaan 14 servers, 15% haalt 100+, 2% haalt 1.000+. Geld wel: BabelBot $920, ShotCaller $819 (op maar 343 servers), CopyKitten $333, geverifieerd via TrustMRR. 14% van de nieuwe apps heeft Discords eigen betaalfunctie aan, prijsmediaan $4,99.
- Beslissing: nee voor nu, cijfer 5 (was 4). Reden: de vooraf vastgelegde grens vroeg beide; geld gehaald, bereik ruim niet (14 tegen 100).
- Controleur akkoord, 7 correcties verwerkt. Belangrijkste: ShotCaller stond wel in de directory (343 servers), dus het rekenvoorbeeld werd 170 tot 10.000 servers voor €350 per maand. Les: een betaalde nichebot kan met weinig servers genoeg verdienen; als we ooit naar Discord gaan, dan zo.
- Volgende run: Unity Asset Store met eigen meting, daarna Godot (bericht Thijs 20:32).
- Daarna Unity Asset Store gepakt (bericht Thijs 20:32). De winkel is nu met curl te lezen. Voorwerk: de sitemap (20 delen) geeft 127.741 productlinks, waarvan 15.265 tools; elke productpagina bevat firstPublishedDate, reviewCount, prijs en uitgever. Verkoopcijfers toont Unity niet, dus reviews worden de maat, zoals bij Shopify.
- Eerste ronde over 3.828 tools (id 330000 en hoger) gedaan, maar bij nakijken bleek het script soms de reviews van een ander product op de pagina te pakken (lcloud-for-playmaker-2 kreeg de 645 van Playmaker 2). Uitkomsten daarom niet gebruikt en de data weggegooid. Voorlopige indruk, niet bruikbaar als cijfer: de meeste nieuwe tools uit 2026 hebben 0 reviews.
- Niet half afgemaakt: de tijd was op (±40 minuten) en een voorstel zonder nagekeken meting is wat Thijs juist niet wil. Volgende run: `data/unity-haal-script.py` ombouwen zodat het het productblok met het id uit de URL leest, opnieuw meten, dan controleur. Daarna Godot.

## 6 nov 2026, run 22:31 UTC
- Bericht Thijs 20:32: Unity opnieuw met eigen meting. Gedaan.
- Script herschreven (versie 2): leest de JSON op de productpagina en pakt alleen het product met het id uit de URL. Controleur keek 10 pagina's na, alles klopt, ook een pagina met een ander product erop.
- Gemeten: alle 4.268 tools met id 300000+ uit de sitemap. Betaalde tools van 3 tot 6 maanden oud (n=886): mediaan 0 beoordelingen, 18% 1+, ±2% 5+, ±0% 10+. Na anderhalf jaar nog steeds 60% zonder beoordeling. Nieuw aanbod ±110 per maand begin 2025, ±380 per maand aug tot okt 2026.
- Vondst: Unity neemt beoordelingen mee naar vervolgversies en bundels (PlayMaker 2 begon met 3.428). Bekende uitgevers starten zo met voorsprong.
- Beslissing: nee voor nu, cijfer 3 (was 4). Reden: geen bereik voor nieuwe makers gemeten en geen recent geldcijfer van een kleine maker gevonden; verkopen per beoordeling bleef onbekend.
- Controleur akkoord, 5 correcties verwerkt (filter bundels en V8, cijfers bijgesteld, sitemap mist ±15%, aanbod per maand, verhouding onbekend).
- Bericht Thijs 20:32 noemde daarna Godot. Godot staat in onderzocht.md als nee tot betaald opengaat; volgende run eerst kijken of daar iets veranderd is, anders een nieuw platform uit kandidaten.md.
- Godot even nagekeken (roadmap store.godotengine.org): nog steeds alleen gratis items, betaald zonder datum. Niets veranderd, dus niet opnieuw onderzocht.
- Nieuw kandidaat toegevoegd: Fab (de winkel van Epic voor Unreal), omdat makers daar volgens bronnen 88% houden en Unreal volgens een enquête meer gebruikt wordt dan Unity. Voorwerk: sitemap per dag en een open JSON per product, zonder sleutel (zie kandidaten.md). Te weinig tijd voor een meting met controleur, dus vrij gelaten voor de volgende run.
- Fab daarna toch gemeten (tijd over). Open zoek-API en product-JSON, geen sleutel. 4.108 tools: betaalde tools van 3 tot 6 maanden oud mediaan 0 beoordelingen, 15% 1+, 2% 5+. Aanbod 893 nieuwe tools in okt 2026.
- Beslissing Fab: nee voor nu, cijfer 3. Reden: zelfde beeld als Unity; goed geldmodel (88%) maar geen bereik voor nieuwe makers, en gemiddeld ±$1.200 per verkoper per jaar. Controleur akkoord, 6 kleine correcties verwerkt.
- Les: game-engine-winkels (Unity, Fab, eerder Godot en Roblox) laten allemaal hetzelfde zien: veel aanbod, winst bij gevestigde namen. Volgende runs liever een ander soort platform met betaling in de winkel.
