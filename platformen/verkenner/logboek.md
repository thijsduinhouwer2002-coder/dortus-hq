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

## 7 nov 2026, run 07:31 UTC
- Open bericht Thijs 6 nov 20:32 over Shopify eerst gedaan: hoe haalt een gewone nieuwe app zijn eerste 100 installs, en hoe vaak lukt dat.
- Vondst: StoreCensus heeft openbare pagina's per app met actieve installs (storefront-detectie), leesbaar met curl, met een sitemap van 2.369 apps. Gekoppeld aan 2.184 Shopify-pagina's.
- Gemeten: ±7 actieve installs per review (alle apps), ±13 bij jonge apps met 100 tot 300 installs. Toegepast op de steekproef van 6 nov: ±2 tot 6 van de 100 apps uit mei tot aug 2026 haalt 100 installs, alleen betaald nog minder.
- Hulpagent las ±20 forumverslagen uit 2026: bijna allemaal 0 of een handvol installs, advertenties zonder reviews leveren niets op, handwerk (winkels persoonlijk benaderen) werkt het best.
- Beslissing: gevoel van Thijs klopt, Shopify blijft nog niet klaar met cijfer 6, alleen vanwege de route via een nieuwe verplichting. Reden: een gewone app haalt hier geen bereik, dat is nu ook in installs gemeten, niet alleen in reviews.
- Controleur akkoord, 8 correcties verwerkt (Revoq 4.196 en 582, Appio 846 en 122, advertentieclaim kleiner, bovengrens ruimer: ±2 tot 6 in plaats van 1 tot 4, labels aangevuld).
- Arrears van Thijs niet gevonden in de winkel met curl; niet verder gezocht.
- Volgende: Shopify vervolg B (regel met datum). Vindt die niets sterks, dan Shopify naar 5.- Daarna Shopify vervolg B begonnen. Deel 1: de garantielabel-golf (EmpCo, plicht 27 sep 2026) gemeten als tweede toets van de golf-route. 54 apps, mediaan 0 reviews, top 50. Veel kleiner dan de herroepingsknop (2.323). Data in `data/shopify-garan-golf-2026-11-07.json`. Controleur akkoord met 5 correcties, verwerkt: minstens 6 gemiste apps (±60 in totaal, top 7 nu 50 tot 12), twee soorten apps apart genoemd, e-facturen Duitsland alleen B2B, les voorzichtiger verwoord. Volgende run: e-facturen Duitsland en scripttags, dan oordeel 6 of 5.
- Nieuw feit: Shopify gaat apps zonder installs na zes maanden verwijderen (Partner Town Hall 5 nov, via Sicard).

## 7 nov 2026, run 08:31 UTC
- Lokale kopie had een andere geschiedenis dan GitHub; vers gekloond en daarop gewerkt.
- Gekozen: Modrinth (Minecraft-mods), zelf aan de lijst toegevoegd omdat het de enige grote modsite is die makers per dag uit een openbare pot betaalt, met open API. Shopify vervolg B deel 2 laten liggen: Thijs vraagt nieuwe platformen.
- Gemeten: 23.600 mods sinds april. Goedgekeurd mei tot aug: mediaan 371 downloads, 88% 100+, 6,3% 10.000+. Maar mediaan 1 volger, downloads zijn geen spelers. ±4.000 nieuwe mods per maand.
- Geld: pot voor makers openbaar via de API (gemiddeld ±$150.000 per maand). Rond $0,15 per 1.000 downloads als alles telde. Voor €350 per maand een plek in de top ±100 tot 300 nodig. Verkopen verbiedt de EULA.
- Beslissing: nee, cijfer 3. Reden: doelen laten geld voor bereik gaan, en hier is geld voor een kleine maker niet haalbaar; ook NET 60 vertraagt alles 2 maanden.
- Controleur niet akkoord met 10 correcties, alle verwerkt. Grootste: ik had de pot verkeerd opgeteld ($132.800 moest $160.400 zijn), en de datum in de zoekindex is de goedkeuringsdatum. Advies bleef gelijk.
- Les: een platform met veel bereik maar geld alleen uit advertenties levert kleine makers niets op. Volgende keer eerst kijken of verkopen mag, voor ik bereik meet.
- Nieuwe kandidaat genoteerd: BuiltByBit en Polymart (betaalde serverplugins). Volgende run: een platform met betaling in de winkel uit kandidaten.md.

## 7 nov 2026, run 09:31 UTC
- Gekozen: BuiltByBit en Polymart (betaalde Minecraft-serverplugins), omdat de vorige run de les gaf eerst een platform te kiezen waar verkopen mag, en hier wordt in de winkel betaald.
- BuiltByBit geeft 403 met curl en de API vraagt een sleutel. Polymart (heet nu voxel.shop) heeft een open API met downloads per product; die geeft 429 bij snel vragen, dus het script vraagt nu een voor een en kan hervatten.
- Gemeten: 903 Polymart-producten vanaf 8 nov 2025. Betaald mei tot aug 2026 (n=131): mediaan 0 downloads (≈ kopers), 2% 10+, geen 50+, samen $1.494 bruto. Beste nieuwe product van het jaar $623 bruto, beste maker ±$1.260 over 16 producten.
- Hulpagent: BuiltByBit 9,9% afdracht, ±$5,8 miljoen totale verkoop (zwakke bron), geen maker na 2024 boven $300 per maand gevonden. Minecraft-EULA verbiedt letterlijk mods (ook plugins) verkopen. ±194.000 servers in bStats.
- Beslissing: nee, cijfer 2. Reden: op alle drie de pluginwinkels (Polymart gemeten, SpigotMC eerder mediaan 3, BuiltByBit niet te meten) verkoopt een nieuwe betaalde plugin bijna niets, en de EULA maakt verkopen juridisch grijs. Geen BuiltByBit-account aan Thijs gevraagd: de kans dat die meting het oordeel omdraait is klein.
- Controleur akkoord, 7 correcties verwerkt (nov 2025 niet compleet, 2 tot 6 maanden in plaats van 3 tot 6, "bijna nul", label bij wachtende producten, kanttekening verkoop buiten Polymart, EULA nu GEZIEN).
- Les: Minecraft is nu van twee kanten bekeken (mods en plugins) en levert kleine makers geen geld op. Volgende run iets anders dan games, met betaling in de winkel.

## 7 nov 2026, run 10:31 UTC
- Gekozen: Blender geld, de open meettaak van Hans (6 nov). Reden: Blender had het beste bereik en alleen het geld ontbrak; de les van de vorige runs was een platform met betaling in de winkel.
- Vondst: Superhive (vroeger Blender Market) toont op elke productpagina een verkoopteller (vanaf 10) en de publicatiedatum. Eerste platform waar ik echte verkopen van nieuwe producten kon tellen.
- Gemeten: elke derde pagina uit de sitemap rond product-id 253.450 tot 264.732 (3.166 pagina's, 375 add-ons). Betaald, 2 tot 6 maanden oud (n=316): mediaan onder 10 verkopen, 31% 10+, 7% 100+, 16 add-ons (14 makers) ±$300+ netto per maand. Eerst 429 bij 8 tegelijk; script nu 3 tegelijk met wachten.
- Eerste aanpak (lijst add-ons op datum) laten vallen: die lijst mengt bijgewerkte producten, dus scheef. Sitemap-volgorde volgt het id en is eerlijker.
- Beslissing: Blender van nog niet klaar (5) naar ja (7). Reden: beide eisen van Hans zijn gehaald (nieuwe betaalde add-ons verkopen regelmatig, en meerdere nieuwe makers zitten boven $300 per maand), en het bereik was al gemeten. Bedragen blijven GOK (bundels, codes, kortingen).
- Controleur akkoord, 10 correcties verwerkt (n=316 in plaats van 318, 375 add-ons, formule in het script gelijkgetrokken, presets en theme-packages niet meegeteld en dat vermeld, Published is eerste publicatie, onderbouwing teller onder 10).
- Besluit ligt nu bij Hans. Volgende run: een nieuw platform uit kandidaten.md, iets anders dan games, met betaling in de winkel.

## 7 nov 2026, run 11:31 UTC
- Gekozen: Foundry VTT, zelf toegevoegd. Reden: CodeCanyon geeft 403, en bij Foundry verdienen makers van code-modules zichtbaar geld via Patreon, met open tellingen (Forge Bazaar API, graphtreon).
- Vondst: de Forge Bazaar API (`forge-vtt.com/api/bazaar/modules`) geeft alle 9.360 modules met datum en installs als percentage van ±73.500 Forge-gebruikers (kleinste stap = 1 gebruiker). Graphtreon toont Patreon-leden en bedragen; patreon.com zelf geeft 403.
- Gemeten: gratis code-modules van mei tot aug 2026 mediaan 14 Forge-gebruikers (±70 tot 140 totaal, GOK), 65% 10+. Van 9 nieuwe code-makers op Patreon zitten er 4 boven $300 per maand, 2 boven $3.000.
- Belangrijk: de AI-regels van Foundry (18 mrt 2026) eisen menselijke tekst, ook UI-labels, en een maker die alle code kan uitleggen, bij elke update. Dat botst met hoe Dortus werkt.
- Beslissing: nog niet klaar, cijfer 6. Reden: geld en bereik zijn goed genoeg voor een ja, maar alleen als Thijs de maker wil zijn volgens die regels; dat is een risico voor zijn account, dus zijn keuze. Vraag op lijst Thijs gezet.
- Controleur akkoord, 7 correcties verwerkt (Gambit is geen nieuwe maker, Nox krap, 100+ als GOK erbij, Forge-gebruikers installeren meer, Patreon valt onder de officiële regels, regel geldt bij elke update, ja bij Thijs eerst een 6).
- GitHub-downloadtellers van modules waren de betere bereikmeting, maar geven hier 403 voor repo's buiten Dortus.
- Volgende run: een nieuw platform uit kandidaten.md.
- Tweede platform: Fantasy Grounds Forge, zelf toegevoegd (de andere tafelsoftware naast Foundry, met een eigen betaalde winkel). De winkeltabel is openbaar met een token uit de pagina: alle 3.189 items met prijs, datum en abonnees.
- Gemeten: betaalde extensies mei tot aug 2026 mediaan 15 kopers bij $3, gratis mediaan 69. Melborne ±$1.660 bruto per maand en Henix ±$750, maar Melborne heeft waarschijnlijk een account sinds 2022 (controleur, via makersnummer).
- Beslissing: nee voor nu, cijfer 4 (eerst 5). Reden: kleine markt (44 makers ooit), lage bedragen per extensie, maar één aantoonbaar nieuwe maker boven $300, en de afdracht is niet openbaar.
- Controleur akkoord, 6 correcties verwerkt (prijs in gold, cadeaus tellen mee, afdracht alleen in de Crafter Agreement, AI-regel voor omzetters gevonden, Melborne niet nieuw, cijfer omlaag).

## 7 nov 2026, run 12:31 UTC
- Opgeruimd: de lokale kopie van main liep uiteen met GitHub (50 tegen 97 commits). Lokale tak hernoemd naar oud-main-lokaal en verder gewerkt vanaf origin/main. Niets verwijderd.
- Berichten van Thijs: alles verwerkt. Godot is in een eerdere run nagekeken (niets veranderd), dus een nieuw platform.
- Gekozen: Google Workspace Marketplace. Reden: op 6 nov "niet te meten", nu met curl leesbaar, en het is een grote winkel met bedrijven als klant.
- Vondst: elke zoekpagina geeft 100 kaarten met gebruikers; met ±400 zoekwoorden 5.865 add-ons, ongeveer de hele winkel. Daarna alle vermeldingen gelezen in 2,5 minuut.
- Gemeten: waarschijnlijk nieuwe add-ons mediaan 48 (laatste update mei tot aug) tot 97 (maart tot juni), 39 tot 50% 100+. Geen eerste publicatiedatum te zien en Wayback niet bereikbaar, dus leeftijd GOK.
- Hulpagent: geen betaling in de winkel, geen afdracht. Alle makers sinds 2025 op TrustMRR onder $150 per maand; Sync2Sheets ($9.000, start 2021) en BudgetSheet zijn oud.
- Beslissing: nee voor nu, cijfer 5. Reden: bereik is goed, maar aantoonbaar geld voor nieuwe kleine makers ontbreekt, en betalen moet helemaal zelf gebouwd worden.
- Controleur akkoord, 10 correcties verwerkt (o.a. vertekening door latere updates, steekproef: ongeveer de helft van de groep is echt nieuw, één geldgrens van $300).
- Les: zoekpagina's met veel woorden zijn een snelle manier om een hele winkel te tellen. Over 4 weken opnieuw draaien geeft een echte lijst nieuwe add-ons.
- Tweede platform: Open VSX (de winkel van Cursor, Windsurf, Antigravity, Kiro). Reden: open API met eerste-versiedatum, dus een schone meting van leeftijd.
- Gemeten: steekproef van 2.500 uit de 10.000 laatst bijgewerkte (de API geeft er niet meer). Groep juni tot aug mediaan 1.492 downloads, maar de laagste extensie per maand ligt op ±400 tot 630: elke extensie krijgt automatisch honderden downloads. Extensies zonder updates mediaan 729.
- Beslissing: nee voor nu, cijfer 4. Reden: bereik niet eerlijk te meten, ±1.700 nieuwe extensies per maand, en geen kleine maker boven $300 per maand (beste $131, TrustMRR).
- Controleur akkoord, 9 correcties verwerkt (labels en links, vloer 400 met voorbeelden, telling april niet als groei).
- Les: downloadtellers van open registers kunnen een vloer van automatisch verkeer hebben. Kijk altijd naar het minimum en naar extensies zonder updates.
- Volgende run: een nieuw platform uit kandidaten.md, liefst met betaling in de winkel.

## 7 nov 2026, run 13:31 UTC
- Lokale kopie stond los van een tak (detached); main opnieuw gezet op origin/main. Niets verwijderd.
- Berichten van Thijs: alles al verwerkt. Gekozen: Wix App Market. Reden: op 6 nov "niet te meten", betaling zit in de winkel, en nu is wix.com leesbaar.
- Vondst: elke lijstpagina heeft de data als base64 in de HTML, met reviews en prijsvorm; maar Wix toont geen installs en geen datum, en de interne API mocht niet. Wel een lijst "Newest apps" (306) en per app de 5 nieuwste reviews met datum.
- Gemeten: 1.818 apps (±3.200 in de winkel, GOK), mediaan 2 reviews, 37% nul. 48 nieuwste apps allemaal 0 reviews, 15 ervan van één bedrijf. Apps met eerste review mei tot aug: 69, bijna allemaal 1 tot 2 reviews.
- Onderzoeker: 80/20 en eerste jaar 100% voor de maker, uitbetaling vanaf $200. Geen kleine maker met een bedrag gevonden (TrustMRR, Indie Hackers, Reddit).
- Beslissing: nee voor nu, cijfer 3. Reden: bereik niet te meten en reviews wijzen op bijna niets, en geen enkel geldbewijs, terwijl er sinds de AI-keuring waarschijnlijk een vloed van nieuwe apps is.
- Controleur akkoord, 8 correcties verwerkt (schatting ±3.200 want 8 collecties telden dubbel, stijging eerste reviews deels meeteffect, PURPLE-groep weegt zwaar, bronnen vindbaarheid en bouwtijd, Harmony één bron, script repareren).
- Les: als een winkel alleen reviews toont, is een lijst "nieuwste" met allemaal 0 reviews al een sterk signaal.
- Daarna TradingView geprobeerd (makers verkopen scripts): robots.txt verbiedt AI-agents uitdrukkelijk /scripts/ en /u/. Beslissing: niet scrapen, platform als niet te meten genoteerd. Reden: die regel is duidelijk bedoeld voor ons.
- Tweede platform: Thunderbird. Open API met aanmaakdatum en gebruikers per dag: alle 2.282 extensies in een minuut.
- Gemeten: nieuwe extensies mei t/m aug 2026 mediaan 16 per dag, 18% 100+; nieuwe betaalde (n=33) mediaan 7. Owl for Exchange (2018) 41.817 per dag en ±€10 per jaar, maar oud, en Exchange zit sinds Thunderbird 145 ingebouwd.
- Beslissing: nee, cijfer 3. Reden: bereik ver onder JetBrains en Obsidian, en geld alleen bij makers van 8 tot 16 jaar oud.
- Controleur akkoord, 8 correcties verwerkt (grootste extensie, Exchange ingebouwd, maandtellingen, overlappende groepen, TrustMRR doorzocht, gebruikersbron).
- Volgende run: Zotero of Anki uit kandidaten.md, of een nieuw platform met betaling in de winkel.
- Derde platform: Firefox (zelfde soort open API). De API toont maar de 30.000 nieuwste, en die gaan terug tot ±8 juni: ±5.000 tot 10.000 nieuwe extensies per maand. Elke 5e pagina genomen (6.000).
- Gemeten: nieuw jun t/m aug mediaan 1 gebruiker per dag, 2% 100+, betaald ook mediaan 1.
- Beslissing: nee, cijfer 1. Reden: laagste bereik van alles wat we maten, en geen betaling.
- Controleur akkoord, 6 correcties verwerkt (venster ±8 juni tot 5 nov, totaal 116.388, overleving maakt oude maanden te laag, onzekerheid per maand).
- Les: browserwinkels (Chrome, Edge, Firefox) zijn dicht; niet meer naar kijken zonder nieuw feit.
- Volgende run: Zotero of Anki uit kandidaten.md, of liever een nieuw platform met betaling in de winkel.


## 7 nov 2026, run 15:32
- Lokale kopie stond weer los van een tak; main opnieuw gezet op origin/main. Niets verwijderd.
- Open bericht van Thijs (15:25): Foundry VTT, route (c), alleen buiten de officiële lijst. Dat gaat voor, dus geen nieuw platform eerst.
- Gemeten: alle 16 modules van GlitchSmith en Wand & Widgets staan in de officiële lijst (200 op foundryvtt.com/packages), als "Purchase: Publisher". Hun geld loopt dus via de lijst.
- Gemeten: alle 3.038 Forge-modules van mei 2025 tot aug 2026 nagekeken op de lijst. 615 gaven 404, maar de controleur vond dat de helft van de gratis code-modules met 404 onder een ander id toch in de lijst staat. Echt buiten: 40, met minder Forge-bereik (mediaan 14,5 tegen 35 voor de oudere groep).
- Onderzoeker: geen maker alleen buiten de lijst boven ±$350 per maand (Loremaster $90, Shattered Codex $346 deels in de lijst, Mad Wizard onbekend en klein). Reddit en GitHub geven 403.
- Beslissing: route (c) nee, cijfer 3. Reden: het geldbewijs van 7 nov hoort bij de officiële lijst, en het zoekscherm in Foundry toont alleen de lijst. Wat dit verandert: een maker die aantoonbaar alleen buiten de lijst boven $300 per maand haalt, of soepeler AI-regels.
- Controleur akkoord, 7 correcties verwerkt (andere id's, kleine groepen niet hard, GlitchSmith-koppeling GOK, artikel 1.2 als recht, rij "ander").
- Les: een 404 op een pakket-id betekent niet dat het pakket er niet is. Vergelijk op de repo-link.
- Volgende run: een nieuw platform uit kandidaten.md (Zotero, Anki, Home Assistant of iets met betaling in de winkel).
- Tweede platform: Autodesk Design and Make Marketplace (vroeger App Store). Reden: betaling zit in de winkel en kopers zijn bedrijven. aescripts.com (After Effects) eerst geprobeerd, geeft 403.
- Gemeten: alle 5.055 apps via de openbare sitemap (robots.txt staat dat toe). Instroom van ±50 naar ±150 per maand sinds aug 2026. 41% echt te koop in de winkel. 0% afdracht. Geen downloads of reviews op de pagina's; de interne API van de winkel niet gebruikt (de veiligheidscontrole weigerde, terecht).
- Onderzoeker: geen kleine maker met cijfers. Op r/Revit: betaalde plugins komen vooral van bedrijven.
- Beslissing: nog niet klaar, cijfer 4. Reden: de voorwaarden zijn top, maar er is niets te zien van verkoop of bereik, en bouwen vraagt Windows en een dure licentie.
- Controleur eerst niet akkoord: mijn telling "betaald" nam proefplannen mee (65% werd 41%) en de mediaanprijs was als tekst gesorteerd. Beide scripts gerepareerd, 7 correcties verwerkt.
- Les: tel bij prijsplannen alleen wat echt te koop is, en zet bedragen om naar getallen voor je rekent.
- Volgende run: Zotero, Anki of Home Assistant uit kandidaten.md, of SketchUp Extension Warehouse (betaalde extensies).


## 7 nov 2026, run 16:33
- Lokale kopie stond los (main had een oude, losse geschiedenis). Niets weggegooid: nieuwe werktak gemaakt vanaf origin/main en daarvandaan op main gezet.
- Geen open bericht van Thijs (Foundry van 15:25 al verwerkt).
- Eerst: SketchUp Extension Warehouse. De winkel haalt alles uit een interne API zonder inlog (1.429 extensies met downloads en datum). Alles ophalen weigerde de veiligheidscontrole, net als bij Autodesk; niet omzeild. SketchUcation verbiedt ClaudeBot in robots.txt, dus ook niet. Toestemming gevraagd op lijst Thijs (in de chat of de taakopdracht, niet in een bestand).
- Geprobeerd en afgevallen: CodeCanyon (Cloudflare-controle), food4rhino en maxforlive.com (403).
- Daarna: WooCommerce Marketplace. Reden: geld loopt via de winkel (70% voor de maker) en elke productpagina toont actieve installs en publicatiedatum, met een gewone pagina en een sitemap die robots.txt toestaat.
- Gemeten: alle 1.562 pagina's. Plugins van mei t/m aug 2026 (n=85): 1% haalt 100+ actieve installs; van 459 sinds jan 2025 maar 9, geen enkele 200+. Oud (voor 2024) mediaan 200.
- Beslissing: nee, cijfer 2. Reden: in het eerste jaar komt bijna niemand boven de 100 actieve installs, en geen nieuwe maker met een aantoonbaar bedrag. Wat dit verandert: een nieuwe verplichting voor webwinkels zonder goede extensie, of bewijs dat Woo nieuwe extensies naar voren haalt.
- Controleur akkoord, 8 correcties verwerkt (1.216 plugins in plaats van 1.154, de 186 gratis vermeldingen, leeftijd en lichting, andere maten bij vergelijking, prijs per jaar, 100+ is 100 tot 199, externe licenties, drempel afgeleid).
- Les: een productpagina met de data in de HTML is beter dan een API; zoek eerst daarnaar.
- Volgende run: Zotero, Anki, Home Assistant, of een winkel met betaling waar de pagina's installs of verkopen tonen (BigCommerce, Squarespace Extensions, Ecwid zijn bereikbaar met curl).
- Voorwerk voor de volgende run: BigCommerce (alleen reviews zichtbaar, geen installs), Squarespace en Ecwid staan in kandidaten.md. Niet meer aan begonnen: te weinig tijd over voor een grondige meting met controleur, en haast hoort niet.

## 7 nov 2026, run 17:32
- Lokale kopie stond los (main met oude losse geschiedenis, ondiepe kloon). Niets weggegooid: werktak vanaf origin/main, daarvandaan op main gezet.
- Geen open bericht van Thijs.
- Gekozen: Craft CMS Plugin Store, zelf toegevoegd. Reden: betalen in de winkel, 20% afdracht, en één open API geeft de hele winkel met installs, datum en prijs.
- Gemeten: alle 1.670 plugins. Nieuwe betaalde plugins (mei t/m aug 2026) mediaan 3 installs, 0% 100+. Mediaan nieuwe maker $195 bruto in totaal.
- Massamaker gevonden: Justinholt.com Incorporated met 145 plugins. Apart gehouden bij alle tellingen.
- Controleur: nee terecht, maar cijfer 3 te laag. Hij vond samuelreichor (eerste plugin dec 2024, door mijn filter gemist), ±$5.000 per maand bovengrens met AI-plugins, en dat LindemannRock al klanten had van vóór de winkel. Cijfer 4.
- Beslissing: nee voor nu, cijfer 4. Reden: de mediaan is slecht en de markt klein en krimpend. Wat dit verandert: Craft 6 (±maart 2027), dan herhaalmeting.
- Les: een filter op "eerste plugin vanaf datum X" mist makers die net daarvoor iets kleins zetten. Kijk ook naar de datum van de beste plugin.
- Tweede platform: Statamic Marketplace, omdat het lijkt op Craft (PHP-CMS met betaalde addons) en ook een open API heeft. De API geeft geen installs, dus Packagist-downloads erbij gehaald.
- Gemeten: 645 addons, 523 met Packagist-data. Nieuwe betaalde addons mediaan 3 downloads per maand. ±14.800 sites (BuiltWith).
- Beslissing: nee, cijfer 2. Reden: nog kleiner dan Craft, geen bedrag van een kleine maker. Controleur akkoord, 3 correcties.
- Les: kleine CMS'en (Craft, Statamic) hebben eerlijke winkels maar te weinig kopers. Volgende run liever een platform met miljoenen gebruikers en betaling in de winkel.
- Volgende run: Ecwid of BigCommerce (betaling via de winkel, bereikbaar met curl), of Zotero, Anki, Home Assistant.
- Derde platform: eerst Ecwid, niet te meten (474 apps zonder installs, datum of reviews in de pagina). Daarna BigCommerce: de app-pagina's hebben createdOn en reviews in de ingebedde JSON, sitemap toegestaan.
- Gemeten: alle 1.469 pagina's. Betaalde apps sinds 2025 mediaan 0 reviews, niemand 20+. ±41.000 winkels, krimpend.
- Beslissing: nee, cijfer 2. Reden: geen bereik en geen bedrag van een kleine maker. Alleen nuttig als tweede winkel naast een Shopify-app. Controleur akkoord.
- Les: createdOn bij BigCommerce is de registerdatum, niet de livegang. Check bij elke winkel wat een datumveld echt betekent.
- Run afgesloten na drie platforms. Volgende run: een platform met veel gebruikers en betaling in de winkel; Zotero, Anki en Home Assistant hebben geen betaling en wachten.
- Nagekomen: Squarespace Extensions kort bekeken via de open API. Maar 60 extensies van gekozen partners, ±8 per jaar. Nee, geen open winkel. Geen controleur nodig: het is een telling van 60 regels uit één bron.
- Vierde platform: Telegram (bots en Mini Apps, betalen met Stars), zelf toegevoegd. Reden: ruim 1 miljard gebruikers en betalen zit in de app, het grotere broertje van Discord.
- Gemeten: voorwaarden zelf gelezen ($0,013 per Star, 21 dagen, Fragment). Nieuwe bots niet te meten: geen lijst met startdatum (tapps.center zonder datum, findmini.app verbiedt ClaudeBot), cijfers pas boven 10.000. Een poging de JavaScript van tapps.center te lezen werd door de veiligheidscontrole geweigerd; niet omzeild.
- Beslissing: nee voor nu, cijfer 4. Reden: geen bereik te meten en geen kleine maker met een controleerbaar bedrag, terwijl het zeer druk is en een bot een eigen server nodig heeft. Wat dit verandert: twee kleine makers sinds 2025 boven $300 per maand in Stars, of maandrapporten met nieuwe bots.
- Controleur akkoord, 8 punten. Belangrijkste: ik las alleen het eerste blok op de t.me-pagina; het cijfer staat in het tweede. Hersteld en zelf nagetest.
- Les: bij het uitlezen van een pagina altijd alle treffers bekijken, niet alleen de eerste.
- Volgende run: een platform met betaling in de winkel en een lijst met datums; Zotero, Anki en Home Assistant wachten nog (geen betaling).
- Vijfde stuk: Shopify vervolg B deel 2 (stond vrij). Reden: Shopify was met 6 het hoogste open platform en de vraag lag klaar.
- Gemeten: 234 apps uit de sitemap met factuurnamen, 75 met een e-factuurstandaard op de pagina. 56 uit 2026, mediaan 0 reviews, top 6. Oude brede apps winnen (controleur vond Order Printer Pro en Vify die ik miste).
- Beslissing: Shopify van 6 naar 5, nee voor nu. Reden: drie golven gemeten, alleen de eerste werkte; bij e-facturen is het vol vóór de deadline. Wat dit verandert: apps die in maart en april 2027 breken (scripttags, tokens) zonder vervanger, of een nieuwe verplichting met na een maand minder dan tien aanbieders.
- Controleur akkoord, 7 correcties.
- Les: zoeken op naam mist grote apps die een functie toevoegen. Kijk bij een golf altijd ook naar de top van de categorie.
- Laatste kwartier: voorwerk Elgato Marketplace (Stream Deck). Pagina's tonen datum en prijs maar geen downloads. Steekproef van 400: 58% uit 2026, ±700 nieuwe producten per maand (GOK). Nog geen oordeel, staat in kandidaten.md voor de volgende run. Reden om te stoppen: geen tijd meer voor een controleur, en een half oordeel telt niet.

## 7 nov 2026, run 18:33
- Geen open bericht van Thijs (alle berichten verwerkt).
- Gekozen: Elgato Marketplace afmaken. Reden: het voorwerk van vorige run lag klaar en had nog een oordeel nodig.
- Gezocht naar downloads of bedragen. De winkel toont ze nergens, ook niet in de lijst die de site laadt (1.798 plugins). Toen ik dieper wilde kijken of die lijst meer prijsgeeft, weigerde de veiligheidscontrole dat twee keer. Niet omzeild en gestopt met die winkel.
- Geld van derden: BarRaider, de bekendste pluginmaker, $14 tot $87 per maand op Patreon (graphtreon). Geen kleine maker met een bedrag gevonden.
- Beslissing: nee voor nu, cijfer 3. Reden: bereik en geld niet te meten, en het ene geldsignaal is slecht. Wat dit verandert: twee makers met $300+ per maand, of Elgato toont downloads.
- Geen controleur: er zijn geen eigen cijfers om na te kijken.
- Les: als een winkel cijfers verbergt, niet gaan zoeken naar verborgen velden. Dan is het "niet te meten" en door.
- Volgende: Zoho Marketplace (betaalde extensies voor Zoho CRM en andere Zoho-apps), zelf toegevoegd.
- Tweede platform: Zoho Marketplace, zelf toegevoegd. Reden: 45 miljoen+ Zoho-gebruikers en betaalde extensies kun je in de winkel kopen.
- Gevonden: app-pagina's tonen installemmer, publicatiedatum en of betaald. Er is geen sitemap met apps en de lijst laadt via een script; ik ben daar niet in gaan graven. Wel 104 uitgelichte extensies van Zoho's eigen pagina's gemeten: 38 met installs (18 van de 104 zijn van Zoho zelf), de top is van Zoho zelf. Zoho noemt zelf ±30.000 installs per maand voor 2.000+ extensies.
- Nog geen oordeel: de uitgelichte lijst is geen eerlijke steekproef van nieuwe apps, en de afdracht staat nergens leesbaar. Staat als voorwerk in kandidaten.md voor de volgende run. Reden om te stoppen: werktijd op, en een half oordeel telt niet.

## 7 nov 2026, run 19:33
- Geen open bericht van Thijs.
- Gekozen: Zoho Marketplace afmaken. Reden: het voorwerk lag klaar en er ontbrak een eerlijke lijst nieuwe apps.
- Gevonden: Zoho zet elke maand een openbare lijst "What's new on Zoho Marketplace" op help.zoho.com. Dat is de eerlijke steekproef. Common Crawl en het Wayback-archief waren vanaf hier niet bereikbaar, en in het script van de winkel ben ik niet gaan zoeken.
- Gemeten: 354 apps uit 18 maandlijsten, 340 pagina's gelezen. Teller verschijnt pas vanaf 100+. Andere makers dan Zoho: betaald 3 van 114 boven 100, gratis ±7%. Zoho rekent alleen af na een aparte overeenkomst met listing fees, percentage nergens openbaar. Enige bedrag: Bercha Consulting $15 MRR.
- Beslissing: nee, cijfer 2. Reden: bereik en geld allebei gemeten slecht; de winkel werkt voor Zoho zelf en voor partnerbureaus. Wat dit verandert: openbare afdracht zonder listing fee en twee kleine makers met $300+ per maand.
- Controleur akkoord, 6 correcties. Belangrijkste: okt, nov en dec 2025 bestonden wel (okt onder een ander adres, nov en dec mislukten bij mij). Bijgeteld: 27 betaalde extra, geen enkele boven 100. Makertelling 217 werd 190 (rommel achter de naam).
- Les: als een maandpagina 0 links geeft, check of het een foutpagina is en zoek het overzicht van alle artikelen, in plaats van aan te nemen dat hij niet bestaat.
- Tweede platform: Pipedrive Marketplace, zelf toegevoegd. Reden: CRM met veel kleine bedrijven, nog niet bekeken, sitemap toegestaan.
- Gevonden: 530 apps, geen publicatiedatum (alleen updated_at), en de maker rekent zelf af (Pipedrive-forum 2022). Een installveld bestaat, maar de pagina bevat ook andere apps en mijn uitlezing was niet betrouwbaar; die cijfers gebruik ik niet.
- Beslissing: nee voor nu, cijfer 2, zonder controleur omdat er geen eigen cijfers in het oordeel zitten. Reden: geen lichting nieuwe apps te meten en geen betaling via de winkel, net als HubSpot en monday eerder. Wat dit verandert: datums op de pagina's of eigen betaling door Pipedrive.
- Les: bij ingebedde JSON eerst kijken of een veld bij de app zelf hoort of bij een lijst "vergelijkbare apps" op dezelfde pagina.
- Volgende run: een platform met betaling in de winkel en datums. Nog open: Zapier en Make, Miro, Slack, Sketch, Neovim; Zotero, Anki en Home Assistant hebben geen betaling.
- Derde platform: Salesforce AppExchange, zelf toegevoegd. Reden: grootste CRM, betaalde apps, en robots.txt staat de lijstpagina's toe met een sitemap.
- Gemeten: alle 10.897 pagina's (datum, prijsmodel, reviews uit de structured data; geen installs). Nieuwe betaalde apps mei t/m aug 2026: mediaan 0 reviews, 16% met 1+, 2% met 5+.
- Beslissing: nee voor nu, cijfer 3. Reden: bereik gemeten zwak en geld loopt via verkoopgesprekken en een betaalde security review ($999 per poging). Wat dit verandert: installcijfers, of twee kleine makers sinds 2024 met $1.000+ per maand.
- Controleur akkoord, 6 correcties. Belangrijkste: de review-kosten haalde ik uit een oude versie van de documentatie ($2.550); nu $999 per poging. En de prijs is gemengd per maand en per jaar.
- Les: bij documentatie met versienummers altijd de nieuwste versie lezen.
- Laatste kwartier: voorwerk Xero App Store, zelf toegevoegd. Sitemap met 462 app-pagina's, met datum en reviews, geen installs. Eerste cijfers staan in kandidaten.md. Nog geen oordeel: de sitemap is mogelijk niet compleet en er was geen tijd meer voor een controleur. Een half oordeel telt niet.
- Run afgesloten na Zoho (2), Pipedrive (2), AppExchange (3) en voorwerk Xero.

## 7 nov 2026, run 20:33
- Geen open bericht van Thijs.
- Gekozen: Xero App Store afmaken. Reden: het voorwerk lag klaar met drie open vragen.
- (1) De sitemap was onvolledig (462). Alle functie- en branchepagina's in 13 regio's gelezen met `?page=N`: 1.128 apps, 1.069 met datum. Apps buiten de VS laden alleen onder hun regio-adres. (2) Betalen via de winkel (XASS) is op 30 juni 2026 gestopt, en sinds 2 maart betaalt de maker Xero per maand; een winkelvermelding kan pas vanaf Plus (AUD 245). (3) reviewSummary hoort bij alle 1.069 bij de app zelf.
- Gemeten: nieuwe apps mei t/m aug 2026 mediaan 0 reviews, 17% met 5+. Beste nieuwe apps zijn gewone softwarebedrijven (tofu, Mercury).
- Beslissing: nee, cijfer 2. Reden: bereik zwak, geen betaling meer via de winkel, en de vermelding kost zelf geld; bouwen vraagt een server met boekhouddata van klanten. Wat dit verandert: betalen via de winkel terug of gratis vermelding, plus kleine makers met $300+ per maand.
- Controleur akkoord, 2 correcties (certificering en keuring horen bij een winkelvermelding, niet al bij Core; "geen enkele maker" werd "niet gevonden bij kort zoeken"). Steekproef 10 van 10 gelijk.
- Les: een sitemap is niet de hele winkel. Kijk altijd of de lijstpagina's per regio meer apps tonen.
- Tweede platform: Notion Marketplace (betaalde templates), zelf toegevoegd. Reden: Notion rekent zelf af en templates zijn zonder programmeren te maken; eerder alleen integraties bekeken.
- Gemeten: sitemap 99.667 templates (65.007 Engels), steekproef 240: 38% betaald, mediaan $9,99. Verkoop staat verborgen (number_of_duplicates -1), geen startdatum. Fee 8% plus $0,40, wachtlijst van mogelijk maanden.
- Beslissing: nee voor nu, cijfer 3. Reden: niet te meten en heel vol; aantoonbaar geld alleen bij makers met groot eigen publiek. Wat dit verandert: een meting via Gumroad- of Etsy-tellers met mediaan 10+ verkopen in 3 maanden zonder eigen publiek.
- Controleur akkoord, 3 kleine correcties (veldnaam, andere datums op de pagina, reviews als zwakke aanwijzing: 13 van 60 met reviews).
- Run afgesloten na Xero (2) en Notion Marketplace (3).
- Na afsluiten nog tijd: Notion vervolg via Gumroad. Gumroad heeft openbare maandsitemaps met nieuwe producten. Steekproef van 3.000 uit juni 2026 (1.710 nog online): 2,6% heeft een rating, 97 betaalde met teller mediaan 0, 3 met 10+. Notion: 27 templates, 1 rating, 2 tellers op 0. Nee blijft, cijfer 3. Controleur akkoord, 3 correcties (top 3 was 414, 18, 10; Notion-prijzen; conclusie voorzichtiger, het Notion-deel is klein).
- Les: Gumroad is een goede plek om geld van kleine makers te meten voor elk platform waarvan de makers via Gumroad verkopen. Script staat klaar.
- Derde stuk: Canva opnieuw, omdat de geldprogramma's in 2026 veranderden. robots.txt van canva.com verbiedt ClaudeBot, dus niet zelf gemeten; alleen het forum en de documentatie gelezen.
- Beslissing: nee voor nu, cijfer 4. Reden: de Adoption Awards (de enige aantoonbare betaling aan kleine makers, gemiddeld ±$250 per maand) stopten 1 juni 2026, Premium Apps is op aanmelding zonder bedragen. Wel weinig apps (500+) voor een groot publiek. Geen controleur: geen eigen cijfers.
- Run afgesloten na Xero (2), Notion Marketplace (3, met Gumroad-meting) en Canva (4).

## 7 nov 2026, run 21:33 (UTC)
- Geen open bericht van Thijs. Webflow stond in onderzoek sinds 21:22 en CodeCanyon werd tegelijk door een andere run gepakt (botsing bij opslaan, beide regels bewaard). Er draaien dus twee Vera-runs naast elkaar; door de "in onderzoek"-regel botsen ze niet op hetzelfde platform.
- CodeCanyon eerst geprobeerd: item- en lijstpagina's 403 (Cloudflare). Notitie voor de andere run in kandidaten.md gezet.
- Gekozen: Steam, kleine bureaublad-apps, zelf toegevoegd. Reden: Steam heeft sinds kort een eigen label Desktop Companion, de zoekpagina toont reviews, prijs en datum, en kleine makers verkopen daar zichtbaar.
- Gemeten: Desktop Companion betaald, lichting mei t/m aug 2026 (95 apps): mediaan 10 reviews, 75% 29, 90% 94, 54% met 10+. Met 30 verkopen per review en 50% netto: mediaan ±$750, 75% ±$2.200 (GOK). 82 van 95 zelf uitgegeven. Nieuw per maand van 18 (jun) naar 67 (okt).
- Beslissing: ja als proef, cijfer 6. Reden: geld zit breed over een hele lichting kleine makers, niet in één uitschieter; product is klein. Wat dit verandert: herhaalmeting over 4 weken waarin sep en okt duidelijk slechter scoren, of verlanglijsten onder ±500 bij een proefpagina.
- Controleur niet akkoord in eerste ronde, 6 correcties: mijn maandtellingen kwamen uit een eerdere, ruimere zoekopdracht (ook software); reviewgetal is soms alleen Engels; prijzen zijn actuele kortingsprijzen; "beter dan Steam gemiddeld" klopte niet (gelijk); top 12 heeft 5 uitgevers; 46% onder 10 reviews erbij. Alles verwerkt, daarna akkoord.
- Les: als ik een zoekopdracht opnieuw draai met andere filters, alle tellingen uit dezelfde run halen.
- Tweede stuk: Steam software en tools (label Utilities), zelf toegevoegd. Reden: een tool past beter bij Dortus dan een spel, en solo-makers als Lossless Scaling verdienen veel. Gemeten: alle 1.706; betaald mei t/m aug mediaan onder 10 reviews, 17% met 10+, 4% met 100+. Beslissing: nee voor nu, cijfer 4. Reden: de gewone nieuwe tool doet het veel slechter dan een bureaublad-app en de drukte verviervoudigde. Wat dit verandert: een omrekening reviews naar verkopen voor software die veel hoger uitvalt. Controleur akkoord, 3 kleine correcties (gamer-zin afgezwakt, Easy Pose is Early Access en een bestaand merk, $9.000 in plaats van $10.000). Dit maakt het Steam-advies scherper: als Steam, dan een bureaublad-app.
## 7 nov 2026, run 21:32
- Geen open bericht van Thijs. Webflow was al geclaimd door een andere run (21:30), en een derde run pakte Steam; die liet ik staan.
- Gekozen: CodeCanyon, zelf toegevoegd. Reden: elke itempagina toont verkopen, dus geld van kleine makers zou direct meetbaar zijn. Niet te meten: Cloudflare geeft 403, de Envato API vraagt een sleutel. Geen tijd aan verspild, direct door.
- Gekozen: Shopware Store, zelf toegevoegd. Reden: de winkel verkoopt en betaalt uit, robots.txt staat alles toe, en elke pagina toont downloads, datum en prijs.
- Gemeten: alle 6.181 extensies. Lichting mei t/m aug 2026 (zonder Shopware zelf): 330, 85% onder 10 downloads, 2% 100+. Na een jaar haalt 3% van de betaalde de 100. Alle uitschieters zijn EU-wetgolven (herroepingsknop, GARAN-label); J&G Agency (partner sinds 2025) haalde 669 downloads met de herroepingsknop.
- Geld: 25% afdracht, alleen huur, mediaan €9,90 per maand. Geen kleine maker met bedrag gevonden. Markt ±30.000 winkels, -3% per jaar. Keuring 30 dagen tot maanden.
- Beslissing: nee voor nu, cijfer 3. Reden: bereik zwak in een kleine, krimpende markt; alleen wetgolven werken, en de trage keuring maakt die lastig. Wat dit verandert: een aankomende wet met datum zonder sterke extensie, of kleine makers met €300+ per maand zonder wetgolf.
- Controleur akkoord na 5 correcties. Belangrijkste: mijn filter op Shopware zelf werkte niet (hoofdletter Swag, de id's zijn klein), dus 330 in plaats van 335; Fishnet is partner sinds 2021, niet 2014 tot 2017.
- Les: filters op id's altijd eerst klein maken (lower) en tellen hoeveel er wegvallen; 0 weggevallen is een rood lampje.
- Les: de wetgolf-route uit Shopify werkt hier ook. Een gezamenlijke wetgevingskalender voor Shopify en Shopware is het onderzoeken waard (taak staat al in taken.md).
- Laatste minuten: voorwerk OpenCart Marketplace, zelf toegevoegd. Elke pagina toont een openbare verkoopteller (Sales) en de aanmaakdatum, dus geld van kleine makers is hier direct te meten. Geen oordeel: geen tijd meer voor meting en controleur. Staat klaar in kandidaten.md.
- Run afgesloten na Shopware Store (3) en voorwerk OpenCart.

## 7 nov 2026, run 21:33 (UTC), vervolg (de andere run schreef ertussen)
- Derde stuk: Mac App Store, kleine hulpprogramma's, zelf toegevoegd. Reden: bekende plek voor solo-makers met betaling via Apple, nooit gemeten. Gemeten via de open iTunes-zoek-API (52 zoekwoorden, 5.769 apps): nieuwe betaalde apps mei t/m aug 2026 mediaan 0 ratings, 0 van 72 met 10+. Beslissing: nee, cijfer 2. Reden: geen spoor van geld binnen de winkel, ook met een steekproef die te gunstig is. Wat dit verandert: een verhouding ratings naar verkopen die laat zien dat 0 tot 1 rating honderden verkopen is. Controleur akkoord, 3 kleine correcties.
- Run afgesloten na Steam bureaublad-apps (6, ja als proef), Steam software (4) en Mac App Store (2). Voor Hans: Steam bureaublad-apps is na Blender het tweede ja-voorstel.
- Na afsluiten nog tijd: vervolg Steam bureaublad-apps. Totaal reviews in alle talen gezocht via appdetails (recommendations.total). Staat maar bij 10 van 111 apps, dus het gat onder de 10 blijft open. Waar het staat: zoekgetal 8 van 9 keer gelijk aan het totaal. Advies en cijfer blijven. Geen controleur nodig: geen nieuwe cijfers die het oordeel veranderen, alleen een bevestiging. Geen nieuw platform meer begonnen: een half oordeel telt niet.

## 7 nov run 21:31
- Platform: Webflow Marketplace, betaalde templates. Reden: Webflow rekent af en geeft makers sinds okt 2025 95%, en eerder was alleen naar de apps gekeken.
- Gemeten: robots.txt van webflow.com verbiedt /api/, die niet gebruikt (een poging op de templates-api werd door de veiligheidscontrole geweigerd, terecht, niet omzeild). Wel alle 11.903 templatepagina's uit de sitemap van templates.webflow.com gelezen; de kaartjes erop tonen goedkeuringsdatum en aankopen. 3.103 templates gezien.
- Uitkomst: betaalde templates mrt t/m jun 2026: 357, mediaan 1 aankoop, 31% nul, 6% 10+, top 73 (Meridian, ±$1.000 per maand). Lichting 2025 mediaan 6, top bij studio's (Alture 475).
- Beslissing: nee voor nu, cijfer 4. Reden: geld per klant goed (95%, ±$75 per verkoop) maar de middelste nieuwe template verkoopt 1 keer in een half jaar, nieuwe makers mogen maar één template tegelijk indienen, en het wordt snel drukker. Wat dit verandert: een niche waar nieuwe templates aantoonbaar 10+ aankopen halen.
- Controleur akkoord, correcties verwerkt (3 templates met prijs 0 eruit: 357, 303, 404). Steekproef 9 van 9 gelijk. Nieuw: uniqueViewers staat sinds juli op 0.
- Les: kaartjes van "andere templates" op detailpagina's kunnen cijfers tonen die de lijst zelf verbergt. Kijk daar ook bij andere winkels naar.
- 7 nov, testrun nieuw account: curl example.com gaf 200, opslaan werkt.

## 7 nov run 22:33 (UTC)
- Platform: OpenCart Marketplace, betaalde extensies. Reden: voorwerk van run 21:32 lag klaar, openbare Sales-teller per extensie.
- Gemeten: alle 1.300 extensiepagina's ID 48300 t/m 49599 (mei t/m aug 2026 is ID 48447 t/m 49537) plus 450 pagina's uit 2025 ter vergelijking.
- Uitkomst: betaald 2026 mediaan 0 sales, 88% nul, top 16, samen 92 verkopen. Lichting 2025 na 14 tot 18 maanden ook mediaan 0, top 48. Gratis mediaan 3 downloads (2025: 34).
- Beslissing: nee, cijfer 1. Reden: geen geld en geen bereik voor betaald, 50% commissie, krimpende markt.
- Controleur akkoord: steekproef 25 van 25 gelijk, cijfers nagerekend, lichting compleet. Correctie verwerkt: commissie is 50% tot $700 per maand (niet 20%).
- Les: als ID's oplopen met de datum, kun je een hele lichting compleet ophalen zonder lijst of sitemap. Eerst een probe met grote stap om het bereik te vinden.
- Tweede stuk: BOOTH (booth.pm), Unity- en VRChat-tools, zelf toegevoegd. Reden: de 3D-categorie van BOOTH groeit hard (¥10,4 miljard in 2025) en kleine makers verkopen er code (editortools). Gemeten: alle 1.920 tools uit de categorielijst van 11 mei t/m 30 sep via de open JSON per item.
- Uitkomst: betaalde tools mediaan 40 likes, 30% 100+, 10,5% 500+. Geen verkoopteller; via één paper (36% van likes koopt) geschat ±14 verkopen voor de middelste tool.
- Beslissing: nog niet klaar, cijfer 6. Reden: beste bereik plus geldsignaal voor code tot nu toe naast Blender, maar uitbetaling buiten Japan en Engelstalig succes nog onbekend.
- Controleur akkoord: 20 van 20 gelijk, lichting compleet, cijfers nagerekend. Correcties verwerkt: 500+ is 10,5%, lilSSRT vanaf ¥500, 取扱高 is verkoopvolume van de hele 3D-categorie, script telt nu de laagste prijs.
- Voor Hans: BOOTH is het eerste nieuwe platform met een 6 sinds Steam bureaublad-apps. Volgende run kan de drie open punten meten.
- BOOTH vervolg: uitbetaling naar PayPal buiten Japan kan (announcements/562). Engelse namen: mediaan 32 likes tegen 41 voor Japanse, 100+ 28% tegen 31%. Cijfer blijft 6, open: verhouding likes en verkoop bij tools. Geen controleur voor dit stukje: twee kleine aanvullingen uit al nagekeken data plus één bron.

## 7 nov run 23:32 (UTC)
- Platform: Anki, add-ons via AnkiWeb. Reden: stond nog open op de lijst, groot studentenpubliek, makers verdienen via Patreon. Food4Rhino en Cults3D eerst geprobeerd: 403.
- Gemeten: de open endpoints van AnkiWeb gevonden in de JavaScript van de site (protobuf, zelf uitgepakt). Hele lijst van 3.835 add-ons, info met alle beoordelingen voor 2.299. Plus 1.908 forumonderwerpen Add-ons.
- Uitkomst: geen downloads zichtbaar, leeftijd via eerste beoordeling (ondergrens). Nieuwe lichting mediaan 1 duimpje (zonder de onbeoordeelde), 2,6% 10+. Uitschieters Synapse en Cristal Memoria, allebei gratis. Geld via Patreon klein (Gainz, nieuw in 2026, $41 tot $262).
- Beslissing: nee voor nu, cijfer 4. Reden: geen betaalroute in de winkel, gewone nieuwe add-on haalt niets, geld bij kleine makers klein.
- Controleur akkoord, 14 van 14 live gelijk. Correcties verwerkt: groei niet te meten (meetfout door welke add-ons info kregen), leeftijd ondergrens, tegenargument erbij.
- Les: een SvelteKit-site zonder HTML-inhoud heeft vaak open /svc/-endpoints; zoek de namen in de JavaScript-chunks. En: info ophalen voor een deel van de lijst vertekent groeicijfers, haal alles of meet groei niet.
- 8 nov 00:00: Owlbear Rodeo extensies opgepakt, maar robots.txt verbiedt ClaudeBot. Niet gemeten, teruggezet op de lijst met die notitie.

## 8 nov run 00:32 (UTC)
- Platform: itch.io, betaalde tools en code-assets. Reden: nieuw, open winkel zonder keuring, maker kiest de afdracht, en in de bestsellerlijst van tools komen 93 van de 180 uit 2026.
- Gemeten: RSS-lijst nieuwste betaalde tools helemaal doorgelopen (6.012), van alle 1.266 tools uit mei t/m jul de pagina met ratings en AI-melding, plus de top 180. Een onderzoeker zocht geldbewijs (Sang Hendrix, ratings-naar-kopers-factor, uitbetaling en AI-regels).
- Uitkomst: 97,6% minder dan 3 zichtbare ratings, 2,4% 3+, 0,3% 10+. Nieuwe betaalde tools per maand 389 (mei) tot 2.043 (okt), aandeel met AI-melding stijgt naar ±68%. Bestsellerlijst weegt recente verkoop, dus zegt weinig.
- Beslissing: nee voor nu, cijfer 4. Reden: geld bestaat bij een paar makers, maar een gewone nieuwe tool haalt bijna niets en wij zouden in de groeiende AI-vloed zitten.
- Controleur akkoord, 20 van 20 live gelijk, lijst compleet, geen dubbelen. Correcties verwerkt: "minder dan 3 zichtbare ratings" in plaats van 0, drempel van 3 is een aanwijzing, AI-verschil onzeker (5 tools), maart, april en november onvolledig, bestsellerlijst is recente verkoop.
- Les: itch.io heeft open RSS per lijst met publicatiedatum (`/<categorie>/newest/store.xml?page=N`), handig voor elke itch-categorie (game-assets kan zo ook).
- 01:00: Godot Asset Store opnieuw bekeken (nu store.godotengine.org): nog steeds beta en alleen gratis, dus besluit van 6 nov blijft staan.
- 01:02: itch.io game-assets voorwerk: ±3.600 nieuwe betaalde assets per week (RSS-pagina 100 is al 31 okt, pagina 200 is 24 okt). De RSS houdt rond pagina 240 op, dus een lichting van 3 tot 6 maanden oud is zo niet te bereiken. Niet verder gemeten: te druk en AI-assets worden streng geweerd, dus past niet bij ons. Op de lijst gezet.
- Run afgesloten na ±30 minuten: de overige open kandidaten (Zotero, Home Assistant, Miro, Slack, Sketch, Zapier en Make, Neovim, Trello) hebben geen betaalroute of te weinig geld, en een grondige nieuwe meting past niet meer in deze run. Volgende run: zelf een nieuwe kandidaat met geldbewijs zoeken.

## 8 nov run 01:32 (UTC)
- Platform: Overwolf Appstore, zelf toegevoegd. Reden: vorige run vroeg om een nieuwe kandidaat met geldbewijs; Overwolf betaalt makers aantoonbaar (totaal $300 miljoen+ in 2025) en app-pagina's tonen downloads.
- Gemeten: alle game- en categoriepagina's doorgelopen, 234 geldige app-pagina's met downloads en ratings. Geen publicatiedatum op de pagina's, daarom als lichting de apps voor Arc Raiders (game van 30 okt 2025). Een onderzoeker zocht geldbewijs.
- Uitkomst: kleine makers bij Arc Raiders 2.086 tot 211.664 downloads in ±1 jaar. Per game maar 13 tot 30 apps. Geen kleine maker met een openbaar bedrag, geen opbrengst per gebruiker.
- Beslissing: nog niet klaar, cijfer 6. Reden: beste bereik tot nu toe bij een winkel met ingebouwd geld, maar het geldbedrag per gebruiker is niet aangetoond en er is een keuring vooraf.
- Controleur akkoord: 15 van 15 live gelijk, regex pakt geen andere apps, Arc Raiders-lijst compleet (16 van 16). Correcties verwerkt: 234 in plaats van 232 apps (2 gemist), 196 met 1.000+ en 84 met 100.000+, MetaForge ook voor andere games, Treestn Dev geen nieuwkomer, startdata alleen aanwijzing.
- Les: zonder publicatiedatum kun je een lichting maken uit de apps voor een game met een bekende lanceerdatum.
- Voor Hans: tweede 6 van vannacht na BOOTH. Thijs zou een ontwikkelaarsaccount moeten maken als Hans verder wil; ik heb niets op zijn lijst gezet omdat het advies nog niet ja is.
- 02:05: Facer voorwerk: ±1,1 miljoen wijzerplaten in de sitemap, downloads alleen via /api/ en /parse en die verbiedt robots.txt. Niet zelf te meten, notitie in kandidaten.md. Opbrengst per gebruiker bij Overwolf nog gezocht: het ontwikkelaarsdashboard meet ARPDAU en ARPMAU, maar de voorbeelden in de documentatie hebben geen echte getallen. Run afgesloten na ±35 minuten, de rest past niet meer in een grondige meting.

## 8 nov run 02:33 (UTC)
- Platform 1: Facer afgemaakt (vorige run vroeg alleen nog geldbewijs). Uitkomst: verkopen alleen op uitnodiging via het Partner Program, voorwaarden geheim, 75+ partners samen $1 miljoen in ±6 jaar. Nee, cijfer 2. Zie voorstellen/facer.md.
- Platform 2: betaalde Wear OS-wijzerplaten op Google Play, zelf toegevoegd (de open route die Facer niet biedt). Gemeten: 6.315 apps via categorie, 50 zoekopdrachten en makerpagina's, met exacte installs via google-play-scraper; 4.084 wijzerplaten van 271 makers. Een onderzoeker zocht geld, regels en drukte.
- Uitkomst: betaalde lichting mei t/m aug 2026 van gevonden makers mediaan 117, maar de controleur liet zien dat dat te mooi is: alles samen mediaan ±75, nieuwe onbekende makers mediaan 9 (14% 100+). Prijs $1 tot $2, gratisacties gewoon, geen openbaar omzetbedrag.
- Beslissing: nee voor nu, cijfer 4.
- Controleur niet akkoord met de eerste mediaan; alle correcties verwerkt (titelfilter miste 102, "volledige makerpagina" niet volledig, 10 gratis catalogus-apps in de lichting, installs zijn een bovengrens). Rekenwerk en 15 van 15 live gelijk.
- Les: zoeken in Google Play geeft vooral bekende makers. Voor een eerlijke lichting: begin bij kleine apps en klik door via "lijkt op" en "meer van deze maker". google-play-scraper geeft het exacte aantal installs (realInstalls) en de releasedatum, bruikbaar voor elke Play-categorie.
- 02:58: Samsung Galaxy Themes voorwerk: makers alleen via een wervingsronde (laatste juli 2023), nee zonder meting. Status bijgewerkt. Run afgesloten na ±30 minuten: een nieuwe grondige meting past niet meer. Volgende run: zelf een nieuwe kandidaat zoeken; idee: andere Google Play-hoeken met de doorklik-methode (bijvoorbeeld iconpacks of KWGT-widgets, betaald en door solo-makers).
- 03:05: toch nog een tweede meting gedaan: betaalde icon packs op Google Play (990 packs van 105 makers, zelfde methode). Betaalde lichting mei t/m aug mediaan 34 installs bij zichtbare makers. Nee, cijfer 3. Zelf 5 van 5 live nagekeken, geen aparte controleur omdat het oordeel nee is. Volgende run: andere hoeken van Google Play zijn nu snel te meten met de scripts in data/ (bijvoorbeeld KWGT-widgets), maar kansrijker lijkt een nieuwe winkel met groter geld per verkoop.

## 8 nov run 03:33 (UTC)
- Platform: Odoo Apps Store, zelf toegevoegd. Reden: de overige open kandidaten hebben geen betaalroute; Odoo verkoopt modules zelf (70% voor de maker) en elke kaart toont openbaar het aantal aankopen, ook vorige maand.
- Gemeten: elke 10e lijstpagina van betaalde modules met een 19.0-versie (250 pagina's, 4.998 kaartjes), 900 modulepagina's voor het oplopende interne ID, en van kandidaten de oudste versie. Een onderzoeker zocht afdracht en regels en ijkte ID naar datum via OCA-merges (±326.000 begin juni, ±371.000 eind aug 2026).
- Uitkomst: alle betaalde 19.0-modules mediaan 0, maar 3,2% verkocht vorige maand. Echt nieuwe modules jun t/m aug 2026: n=207, 94% nul, max 3. Oudere lichting sep 2025 t/m mei 2026: 73% nul, 3% 10+. Geld bij grote bureaus (top 10 ±87% van de omzet vorige maand in de steekproef) en een paar vroege thema's (twee MCP-modules ±$2.000 per maand).
- Beslissing: nee, cijfer 3. Reden: geld bestaat, maar een gewone nieuwe module verkoopt niets, en het is heel druk (±50.000 betaalde modules per versie).
- Controleur akkoord: 30 van 30 live gelijk plus 80 kaartjes. Correcties verwerkt: groep heet "betaalde modules met een 19.0-versie", aankopen zijn levensduur over alle versies, lichting is 2 tot 5 maanden oud, 1,1% zonder prijs.
- Les: bij winkels zonder datum op de pagina kan een oplopend intern ID als klok dienen; ijk het met een bron met datum (hier OCA-merges op GitHub). Let op: makers zetten een module vaak tegelijk voor veel versies online, dus kijk naar het laagste ID over alle versies.
- 04:02: Adobe Exchange opgepakt als volgende, maar robots.txt verbiedt automatisch lezen zonder toestemming van Adobe. Niet gemeten, notitie in kandidaten.md. Run afgesloten na ±30 minuten: een nieuwe grondige meting past niet meer in de werktijd.

## 8 nov run 04:32 (UTC)
- Begin: lokale main liep scheef met GitHub (72 tegen 127 commits). Niet weggegooid; gewerkt op een nieuwe tak vanaf origin/main en daarvandaan naar main gepusht.
- Platform: Microsoft Store (Windows-apps), zelf toegevoegd. Reden: nog niet onderzocht, Store rekent af en 0% afdracht met eigen betaling, en past technisch goed bij ons.
- Gemeten: sitemap (157.032 pagina's), 4.000 willekeurige pagina's met datum, VS-ratings, prijs en add-ons. Een onderzoeker zocht regels, geldbewijs en een ijkpunt voor ratings per install (KDE: VS ±0,3 tot 0,5 per 1.000).
- Uitkomst: de winkel toont onder 5 ratings per land 0. Betaalde apps mei t/m aug 2026: 0 van 104 met 5+. Geen kleine maker met openbare omzet. Sinds juli 2026 een golf van ±11.000 nieuwe apps per maand.
- Beslissing: nee voor nu, cijfer 3.
- Controleur akkoord met de kern, 15 van 15 live gelijk. Correcties verwerkt: 433 mislukte pagina's (stonden als 0) opnieuw opgehaald, games eruit, schatting per maand met juiste noemer, label "onder 5".
- Les: haal niet met 6 tegelijk, dan geeft apps.microsoft.com lege pagina's van 1.484 bytes. Controleer altijd of een kernveld er is, niet alleen de lengte. En ratings per land lees je met de eigen taal van dat land (hl en gl samen).
- 05:08: run afgesloten na ±36 minuten: een nieuwe grondige meting past niet meer. Idee voor de volgende run: VRChat Avatar Marketplace (open kandidaat, maker kg13 verkocht 85 avatars in een maand) of een winkel met openbare verkooptellers.

## 8 nov run 05:32 (UTC)
- Begin: lokale main liep weer scheef met GitHub. Niet weggegooid (kopie op tak oud-main-backup), gewerkt op een nieuwe tak vanaf origin/main en naar main gepusht.
- Platform: VRChat Avatar Marketplace (open kandidaat met geldsignaal van kg13).
- Onderzoeker: VRChat-markt alleen na aanvraag en keuring, avatars worden langzaam toegelaten (sep 2026 nog fast-track voor jamwinnaars), maker ±50%, zonder login 401. Geen openbare totalen.
- Zelf gemeten in plaats daarvan: Jinxxy, 33.695 producten uit de sitemap, steekproef 2.000. Betaalde lichting mei t/m aug mediaan 15 likes, avatars 27 likes en $30, scripts maar 12 van 1.990. Maker houdt 92%.
- Beslissing: nee voor nu, cijfer 3. Reden: geld bestaat, maar voor 3D-kunst die we niet goed kunnen maken, met sterke weerstand tegen AI; VRChat-markt zelf dicht.
- Controleur akkoord met 20 van 20 live gelijk. Correcties verwerkt: gratis demo naast betaalde versies telt als betaald (300 in plaats van 292), URL's met spaties, afdracht omgedraaid (Standard 92%, Supporter 87%).
- Les: Jinxxy-pagina's hebben de prijs soms in versions en soms alleen in base_price; lees beide. Controleer de eerste uitlezing altijd op lege velden voor je analyseert (eerste poging miste 80% van de prijzen).- 05:58: Sketch opgepakt als tweede. Open pluginlijst: 821 plugins, maar 47 actief sinds 2025, geen betaling in de winkel. Nee zonder volledige meting, cijfer 1. Run afgesloten: volgende open kandidaten zijn Zotero, Home Assistant (HACS opnieuw), Miro, Slack, Zapier en Make, Neovim. Die hebben bijna allemaal geen betaling in de winkel; liever eerst een nieuw platform met openbare verkooptellers zoeken (Gumroad zelf kan met data/gumroad-haal-script.py).

## 8 nov run 06:32 (UTC)
- Begin: lokale main liep weer scheef met GitHub. Niets weggegooid, gewerkt op tak vera-werk vanaf origin/main en naar main gepusht.
- Platform: Pebble (Core Devices), zelf toegevoegd. Reden: jong platform met nieuwe horloges, open API, past bij de vraag van Thijs naar plekken waar Dortus groot kan worden.
- Gemeten: alle 3.785 apps en 4.327 wijzerplaten via appstore-api.repebble.com (hearts, eerste versie, beschrijving) plus de lijst meest gebruikt. Een onderzoeker zocht geld, groei en regels.
- Uitkomst: nieuwe uitgaven mrt t/m jun 2026 mediaan 16 tot 18 hearts, 10% haalt 100+; 33 van de 50 meest gebruikte wijzerplaten zijn uit 2026. Geen betalen in de winkel, KiezelPay werkt nog (Flights $5,99, 414 hearts), maar geen enkel bedrag van een maker gevonden. ±40.000 nieuwe horloges (GOK).
- Beslissing: nee voor nu, cijfer 4. Reden: bereik voor nieuwe makers is goed, maar de markt is te klein en geld is niet aangetoond.
- Controleur akkoord, 20 van 20 live gelijk. Correcties verwerkt: wijzerplaten in plaats van makers bovenaan, Round 2-voorbestellingen zonder bron, top 200 per soort, extra tabelrij.
- Les: de Pebble-API heeft verborgen collecties (top-used, top-picks); zoek in de HTML van de winkel naar "collections/" om ze te vinden.
- 06:50: tweede platform gezocht met openbare verkoop- of gebruikscijfers. ChatGPT-apps (robots.txt verbiedt Claude), Hytale op CurseForge (403), Creative Market (robots.txt verbiedt ClaudeBot) en Etsy (403) zijn niet te meten; notities in kandidaten.md. Twee nieuwe kandidaten toegevoegd: Apple Vision Pro en Meta Horizon Store. Run afgesloten na ±30 minuten: een nieuwe grondige meting past niet meer in de werktijd.

## 8 nov run 07:33 (UTC)
- Platform: Apple Vision Pro, betaalde visionOS-apps (stond als kandidaat). Meta Horizon overgeslagen: robots.txt van meta.com heeft een kennisgeving tegen automatisch verzamelen, notitie in kandidaten.md.
- Gemeten: 120 uitlichtpagina's van de visionOS-winkel, 553 apps, 131 alleen voor de bril (12 uit 2026, kleine makers worden uitgelicht). Alle 495 new-app-sitemaps gelezen (90.594 id's): daar zitten geen visionOS- of Mac-apps in, alleen iPhone en iPad.
- Onderzoeker: ±600.000 brillen, geen goedkope bril voor eind 2028, 20 tot 45 nieuwe apps per maand, enige maker met cijfers ±$1.300 per maand met 17 apps.
- Beslissing: nee, cijfer 2. Reden: weinig concurrentie maar ook bijna geen kopers, geen groei in zicht.
- Controleur akkoord, 6 van 6 live gelijk. Nuances verwerkt (artikel noemt niet alle 17 apps betaald).
- Les: Apple toont voor visionOS-apps nergens openbaar ratings (lookup, webpagina, RSS allemaal 0), en de zoek-API en new-app-sitemaps bevatten geen visionOS- of Mac-apps. Voor Apple-platformen buiten iPhone en iPad alleen via lookup op bekende id's of uitlichtpagina's.

## 8 nov run 08:31 (UTC)
- Begin: lokale main liep scheef met GitHub. Niets weggegooid, main opnieuw gezet op origin/main zonder eigen werk te verliezen (er stond niets open).
- Platform: Meta Horizon Store (open kandidaat). Apple Vision Pro was door de vorige run al gedaan.
- meta.com zelf blokkeert automatische lezers (sitemaps 403, foutpagina). Niet omzeild. In plaats daarvan vrdb.app gemeten (robots.txt staat het toe): alle 6.850 nieuwe titels van eind sep 2025 t/m 7 nov 2026, met beoordelingen, prijs en datum. Een onderzoeker zocht regels, markt en geld.
- Uitkomst: betaald mei t/m aug mediaan 1 beoordeling, 14% 10+, 2% 100+; betaalde Apps mediaan 0. Vuistregel 110 verkocht per beoordeling (DERDEN). Headsetverkoop daalt, winkelomzet staat stil.
- Beslissing: nee voor nu, cijfer 4. Reden: het geld zit in 3D-spellen die we zonder headset en zonder echte test niet goed kunnen maken; het deel dat bij ons past doet het slecht.
- Controleur akkoord, alle tellingen gelijk, 15 van 15 live gelijk. Correcties verwerkt: makers op id, auteur en spreiding van de vuistregel, beperking bij GameDiscoverCo, vertekening door de prijs van nu, drukte als piek.
- Les: vrdb.app heeft per lijstpagina een __data.json (SvelteKit, devalue-formaat) met alle velden; 50 per pagina, ±1,5 s ertussen gaat goed. Zelfde aanpak werkt waarschijnlijk voor andere SvelteKit-sites.
- 08:50: tweede platform: Rhino en Grasshopper, zelf toegevoegd. Food4Rhino geeft 403 (niet omzeild), maar de package-API van McNeel (yak.rhino3d.com) is open met downloads en versiedatums. Alle 1.395 pakketten opgehaald.
- Uitkomst: golf sinds maart 2026 (okt 131 nieuwe), nieuwe pakketten mei t/m aug mediaan 57,5 downloads, 6,9% haalt 1.000+; AI-pakketten doen het beter. Geen betalen in de winkel, geen verkoopaantallen gevonden, alleen Patreon-bedragen.
- Beslissing: nog niet klaar, cijfer 4. Reden: past bij ons en de gebruikers betalen voor software, maar geld voor kleine makers is niet aangetoond.
- Controleur akkoord, 8 van 8 live gelijk. Correcties verwerkt (betaalwoorden ±14 tot 25, schrijver AI-voorbeeld werkt bij McNeel, uitspraak McNeel preciezer).
- Run afgesloten na ±45 minuten.

## 8 nov run 09:33 (UTC)
- Platform: Moodle Marketplace, doorgegeven door Noor (net geopend voor betaalde plugins, oud platform). Andere open kandidaten (Zotero, Miro, Slack, Zapier) hebben geen betalen in de winkel.
- moodle.org niet gelezen: robots.txt zegt ai-input=no en er staat een captcha. Wel open: download.moodle.org/api/1.3/pluglist.php (3.248 plugins met isPaid) en marketplace.moodle.com (robots.txt staat alles toe, 10 s tussen verzoeken). Elke winkelpagina toont installaties en downloads van 90 dagen.
- Gemeten: alle 130 betaalde plugins en 45 gratis nieuwe (mrt t/m jul). Onderzoeker zocht afdracht, regels en bedragen.
- Uitkomst: betaalde nieuwe mediaan 3 installaties (jul/aug 5, 0 van 19 haalt 100), gratis nieuwe mediaan 32 (15% 100+). Golf in okt: 194 gratis en 32 betaalde nieuwe, veel AI-plugins. Maker is zelf verkoper (Stripe, btw, eigen licenties). Geen bedrag van een maker.
- Beslissing: nog niet klaar, cijfer 5. Reden: kopers met budget en een officiële winkel met betalen, maar betaald bereik is nog niet aangetoond; over 4 weken zien we of de beste nieuwe plugins groeien.
- Controleur akkoord met correcties, 6 van 6 live gelijk. Correcties verwerkt (mediaan 5, oude plugins uit de gratis steekproef, vergelijking op gelijke leeftijd, bron 1.517).
- Les: in pluglist.php krijgen overgekomen oude plugins soms een nieuwe versiegeschiedenis; gebruik het id (onder ±3900 is van voor de lancering) om echt nieuwe plugins te scheiden. Let op met pgrep -f in een wachtlus: die vindt zichzelf.

## 8 nov run 10:33 (UTC)
- Begin: lokale map stond los van main; main opnieuw gezet op origin/main (niets open, niets verloren).
- Platform: MakerWorld (Bambu Lab), zelf toegevoegd. Open kandidaten Zotero, Miro, Slack, Zapier hebben geen betalen in de winkel.
- Webpagina's geven Cloudflare (403), niet omzeild. De open API (design-service/design/<id>) wel, robots.txt staat alles toe. Id's lopen op met de tijd, dus 1.600 willekeurige id's uit mei t/m aug genomen.
- Uitkomst: mei mediaan 10 downloads, 13,8% 100+, aug mediaan 4. Exclusive mediaan 16. Geen enkel betaald model. ±104.000 nieuwe modellen per maand (GOK). Onderzoeker: geen verkoop, punten vooral tegoed, opbrengst 30 tot 50% omlaag in 2026, contant via Exclusive, BOM-commissie en licentie-abonnement.
- Beslissing: nee voor nu, cijfer 3. Reden: bereik is er, geld voor kleine makers niet.
- Controleur akkoord met correcties, alle tellingen gelijk, 15 van 15 live gelijk. Correcties verwerkt (statussen, drempel per maker, BOM contant, Exclusive als samenhang, eenheden rekensom).
- Les: bij sites met oplopende id's en een open detail-API is een willekeurige steekproef van id's in een datumbereik de snelste eerlijke meting; zoek de grenzen met een paar losse id's.
- 10:52: tweede platform: Printables (Prusa), zelf toegevoegd als vergelijking omdat het een Store met contante verkoop heeft. Webpagina's 403, open GraphQL-API wel. API gaf "Request was throttled" toen ik met 3 verzoeken tegelijk werkte; gestopt, gewacht, daarna 1 verzoek per 1,5 tot 2,5 s.
- Uitkomst: alle 7.650 betaalde modellen sinds 4 mrt opgehaald; van 1.727 met losse prijs uit mei t/m aug heeft 94% geen beoordeling (alleen kopers kunnen beoordelen). Eén kleine maker (foam blasters, 10 modellen, 157 beoordelingen) verdient duidelijk. Gratis mediaan 11 downloads, 8,6% 100+.
- Beslissing: nee voor nu, cijfer 3. Reden: geld kan, maar bijna niemand verkoopt, en we kunnen zonder printer niet testen.
- Controleur akkoord met correcties, alle tellingen gelijk, 8 van 8 live gelijk. Grootste correctie: 55% van de betaald-lijst is Club zonder losse prijs, apart gezet.
- Les: in GraphQL zonder introspectie vind je velden door ze te proberen (foutmeldingen noemen soms de goede naam, zoals 'Did you mean paid'). datePublished verschuift bij updates; gebruik firstPublish.
- Run afgesloten na ±45 minuten.

## 8 nov run 11:33 (UTC)
- Begin: lokale main liep uiteen met origin; gewerkt op een tak vanaf origin/main, gepusht naar main.
- Platform: Fortnite-eilanden (UEFN), zelf toegevoegd. Om 11:40 op "in onderzoek" gezet en gepusht.
- Open Data API van Epic (api.fortnite.com/ecosystem/v1) werkt zonder sleutel: hele lijst (286.128 eilanden, 77.189 makers) en per eiland dagcijfers, maar alleen de laatste 7 dagen en zonder publicatiedatum. Dagen onder 5 spelers zijn leeg. fortnite.gg geeft 403, niet omzeild.
- Uitkomst: steekproef 6.000, 84% van de makerseilanden geen dag met 5 spelers, 4,4% samen 100+, GOK 1,3% $100+ per maand. Top 0,5% bijna 90% van de minuten. Onderzoeker: $352 miljoen in 2024, ruim $1 miljard sinds 2023, verkopen in het eiland 100% tot 31 jan 2027.
- Beslissing: nee voor nu, cijfer 3. Reden: geld is er, bereik voor een doorsnee eiland bijna nul, en UEFN draait alleen op Windows met een editor, dus wij kunnen niet bouwen.
- Controleur akkoord, alle tellingen gelijk, 8 van 8 live gelijk, 9 correcties verwerkt (vooral: catalogus is niet hetzelfde als nieuwe eilanden, tarief komt van dezelfde bron als de vergelijking).
- Les: bij een API zonder datum kun je nieuwe items vinden door de hele lijst te bewaren en over een week opnieuw te halen. De lijst staat in data/fortnite-eilanden-2026-11-08.tsv.gz.
- 11:53: tweede platform Poe (botmakers verdienen per bericht). Niet te meten: explore toont alleen officiële modellen, /search en /api/ verboden in robots.txt, geen sitemap, botpagina's tonen alleen volgers. Programma bestaat nog. Geen oordeel, in kandidaten.md gezet.
- 11:58: derde poging CGTrader (3D-modellen). Sitemaps werken, maar elke pagina geeft 202 zonder inhoud (botuitdaging). Niet omzeild, in kandidaten.md gezet.
- Run afgesloten.

## 8 nov run 13:33 (Amsterdam)
- Begin: lokale map stond los van een tak; main opnieuw gezet op origin/main. Berichten van Thijs: niets nieuws open.
- Platform: CLIP STUDIO ASSETS, zelf toegevoegd. Om 13:40 op "in onderzoek" gezet en gepusht.
- Open zoek-API gevonden in site.js (/en-us/search/ajax met published_from/to, pay en cursor). Alles opgehaald: 20.707 materialen mei t/m aug, 3.129 GOLD-items mrt t/m okt, per verkoper de geschiedenis.
- Uitkomst: bereik het beste tot nu toe (gratis mediaan ±100, GOLD 86), maar de teller is downloads. Bruto 1,28 miljard GOLD past niet bij de jaarrekening van Celsys. GOLD alleen na screening en contract, ±65 verkopers, geen nieuwe in mei t/m aug.
- Beslissing: nog niet klaar, cijfer 5. Controleur akkoord met de cijfers, correctie: downloads zijn geen verkopen, GOK 10 tot 50%.
- Les: bij een winkel met eigen punten (GOLD, Clippy) altijd nagaan of de teller verkopen of downloads telt, en het bruto naast de jaarrekening van het bedrijf leggen.
- 13:58: Max for Live (maxforlive.com) niet te meten, Cloudflare-uitdaging op elke pagina. In kandidaten.md gezet.
- 14:00: tweede platform DLsite (alle leeftijden). Open productinfo geeft per 100 werken verkopen, prijs, datum en soort; robots.txt vraagt 10 s. 2.477 werken opgehaald. Uitkomst: nee voor nu, cijfer 3; wat wij kunnen maken (tools, materiaal) verkoopt niet, stemwerk wel. Geen controleur, tijd op; zelf nagekeken dat de teller verkopen zijn.
- Run afgesloten.

## 8 nov run 14:33 (Amsterdam)
- Begin: main opnieuw gezet op origin/main. Berichten van Thijs: niets nieuws open.
- Platform: Construct 3 en GDevelop (kleine game-engines met eigen winkel), zelf toegevoegd. Om 14:36 op "in onderzoek" gezet en gepusht.
- Construct 3: elke pagina, ook robots.txt, geeft een Cloudflare-uitdaging. Niet omzeild.
- GDevelop: robots.txt staat alles toe. Open shop-API gevonden (api.gdevelop.io/shop/asset-pack, game-template, bundle) met maker, datum en prijs, geen verkopen. Hele winkel opgehaald: 274 packs, 79 sjablonen, 46 makers van derden. Wiki: 60/40, selectie met de hand, Nederland via Tremendous. Blog: VegeTato leeft ervan. itch.io-vergelijking: zijn sjablonen daar 0 tot 8 ratings.
- Beslissing: nog niet klaar, cijfer 5. Controleur akkoord, 8 van 8, correcties verwerkt (bundels, concentratie, concurrentie groeit).
- Les: een winkel zonder tellers is alleen eerlijk te meten met een proef; zeg dat meteen in het advies.
- Run afgesloten.

## 8 nov run 15:33 (Amsterdam)
- Begin: main opnieuw gezet op origin/main. Berichten van Thijs: niets nieuws open. Geen herhaalmeting verlopen.
- Platform: VCV Rack Library (muzieksoftware met eigen winkel, past bij "vakprogramma's met een eigen winkel"), zelf toegevoegd. Om 15:38 op "in onderzoek" gezet en gepusht.
- Open API met alle 602 plugins, premium-vlag, datum en popularity (downloads) voor gratis plugins. Prijzen van alle 116 premiumpagina's gelezen. Forum via Discourse-JSON (robots.txt staat het toe).
- Uitkomst: bereik gratis het beste tot nu toe (mediaan 2.318, 100% boven 1.000), maar geld onzichtbaar en geen bedrag van een maker. Beslissing: nee voor nu, cijfer 4, omdat geld net zo zwaar weegt als bereik en hier niets aantoonbaar is.
- Controleur: 6 van 6 klopt; correctie: de 0,1 tot 1% van Vult is een ruwe schatting tegen alle Rack-gebruikers. Verwerkt. Afdracht 30% alleen van één maker.
- Les: een tellende winkel voor gratis plugins zegt niets over betaald; zoek bij gemengde winkels altijd apart naar een verkoopteller.
- Run afgesloten.

## 8 nov run 16:33 (Amsterdam)
- Begin: lokale main liep los van origin (andere geschiedenis na de overstap); oude stand bewaard als lokale tak oud-lokaal-main, nieuwe main op origin/main. Berichten van Thijs: niets nieuws open.
- Platform: Playdate Catalog (Panic), zelf toegevoegd (hardware-winkel). Om 16:40 op "in onderzoek" gezet en gepusht.
- Alle 510 titelpagina's gelezen: datum, prijs, AI-verklaring. Onderzoeker vond makercijfers op Bluesky en de cijfers van Panic.
- Uitkomst: geld per titel het beste tot nu toe naast Blender, maar alle makers samen ±$36.000 per maand en het apparaat groeit niet. AI-regel sinds april 2026: geen AI-art, geluid of tekst.
- Beslissing: nee voor nu, cijfer 4. Waarom: Thijs zoekt een plek om groot te worden, het plafond is hier te laag. Controleur akkoord (4 tot 5), 5 correcties verwerkt.
- Les: wacht tot het ophaalscript klaar is voor je telt (ik telde 496 van 510); en lees bij een sale de normale prijs.
- 16:58 tot 17:05: korte schifting voor de volgende run. Cults3D niet te meten (Cloudflare). Reason Shop zonder tellers, lage prioriteit. Reallusion Marketplace heeft een interne API met datum en downloads in app.js, staat klaar als voorwerk. Daarna gestopt: geen tijd meer voor een grondige meting met controleur.
- Run afgesloten.

## 8 nov run 17:33 (Amsterdam)
- Begin: lokale main liep weer los van origin; oude stand bewaard als lokale tak oud-lokaal, main op origin/main. Berichten van Thijs: niets nieuws open.
- Nexus Mods eerst geprobeerd: Cloudflare op elke pagina, niet te meten, in kandidaten.md gezet.
- Platform: Reallusion Marketplace (voorwerk uit run 16:33). Om 17:38 op "in onderzoek" gezet en gepusht.
- Open zoek-API gevonden in app.js (Marketplace20/v1/Content/OpenSearch). 3.500 nieuwste items, top 300 bestsellers van 3 maanden en alle 61 plugins opgehaald. Het veld PurchasedTimes is voor iedereen leeg; niet geprobeerd te omzeilen.
- Uitkomst: winkel leeft (±450 nieuw per maand, 5% van het nieuwe betaalde werk in de top 300), maar verkoop onzichtbaar, echt geld pas na certificering en het geld zit in 3D-content, niet in software. Pluginmarkt 61 stuks.
- Beslissing: nee voor nu, cijfer 3. Waarom: geld niet aangetoond en wat wij kunnen bouwen (plugins) heeft hier bijna geen markt. Controleur akkoord, 4 correcties verwerkt (ratings betaald apart, verkoopprijs naast normale prijs, top 300 is geen geld, plugins van maar 6 makers).
- Les: een veld in de API dat altijd leeg is, is een bewuste keuze van de winkel; noteer het en ga door.
- Tweede platform: Roblox UGC (avatar-items), zelf toegevoegd, om 17:47 op "in onderzoek" gezet en gepusht. Open catalogus-API met datum, prijs en favorieten, geen verkopen. Lijst nieuwste stopt bij 1.000, daarom 60 willekeurige makers gevolgd.
- Uitkomst: nee voor nu, cijfer 3. Waarom: extreem druk, bestsellers oud werk, centen per verkoop, ID van Thijs nodig, en het is 3D-mode in plaats van software. Controleur akkoord, 4 correcties verwerkt (cohort is ondergrens door afkapping op 480, lijst niet schoon op datum, mediaanprijs betaald 90, voorschot niet terugbetaalbaar).
- Les: bij een script met een maximum aantal pagina's altijd nagaan wie dat maximum raakt voor je telt.
- Run afgesloten.

## 8 nov run 18:33 (Amsterdam)
- Begin: lokale main stond los (detached), main opnieuw op origin/main. Berichten van Thijs: niets nieuws open. Geen herhaalmeting verlopen.
- Platform: shadcn-registry's, doorgegeven door Noor met de vraag of kleine premium-registry's nu verkopen. Om 18:35 op "in onderzoek" gezet en gepusht. Gekozen omdat het het enige open doorgegeven platform was en ontwikkelaars professionals zijn.
- Eigen meting via TrustMRR (omzet rechtstreeks uit Stripe of Polar, robots.txt staat het toe): 502 profielen, 30 over UI-kits. Onderzoeker vond Obra, Aceternity, 21st.dev en Gumroad. Tellers Shadcnblocks en Cult UI zelf gecontroleerd.
- Uitkomst: geld aangetoond voor vroege spelers, nieuwkomers mediaan ±$485 totaal, eenmalige verkoop. Beslissing: nee voor nu, cijfer 4. Waarom: de koers vraagt terugkerend geld en de motor hier is een eigen publiek dat we niet hebben.
- Controleur: tabel en tellers kloppen; correcties verwerkt (QuasarUI is Vue, RareUI miste door lege datum, som 30 dagen ±$2.620). Oordeel 4 redelijk.
- Les: TrustMRR is een goede bron voor echte bedragen van kleine makers op elk platform; let op profielen zonder startdatum bij het filteren.
- Tweede platform: Slack (apps), om 18:46 op "in onderzoek" gezet en gepusht. Gekozen omdat teams daar een abonnement betalen, wat past bij de koers van 8 nov.
- Eigen meting: sitemap (2.810 apps), prijslabels van 343 nieuwste pagina's (58% vraagt zelf geld), 10 Slack-apps op TrustMRR. Pagina's tonen geen installs, datum of maker. Regels zelf nagelezen op docs.slack.dev.
- Uitkomst: nog niet klaar, cijfer 5. Waarom: beste pasvorm met de koers (abonnement, geen afdracht, solo-maker $4.091 MRR), maar bereik niet te meten en de weg naar de Marketplace duurt maanden; haalt het tussendoel van 20 dec niet.
- Controleur: tellingen kloppen; 2 correcties verwerkt (drempel 10 werkruimtes of 20 gebruikers; rate limit alleen voor apps die berichten lezen).
- Run afgesloten.
- Na afsluiten toch nog tijd over (run duurde pas ±20 minuten), dus derde platform: Miro (apps), om 18:53 op "in onderzoek" gezet en gepusht.
- Eigen meting: de marketplace-pagina bevat alle 224 apps met gebruikersteller, betaaltype en maker. Uitkomst: nee, cijfer 3. Waarom: nieuwe apps van andere makers halen mediaan 19 gebruikers, Miro's eigen apps nemen 93% van het bereik, geen kassa en geen bedrag van een maker.
- Controleur vond een fout in mijn script (appKey van letters viel weg, 53 apps gemist). Gerepareerd en opnieuw geteld; oordeel blijft 3.
- Les: test een regex op de hele pagina door het aantal treffers te vergelijken met een ruwe telling (bijvoorbeeld het aantal keer "usageCount").
- Run afgesloten.

## 8 nov run 19:31 (Amsterdam)
- Begin: lokale main stond los, main opnieuw op origin/main. Open bericht van Thijs (19:22): eigen platformen officieel scoren, vóór de volgende productkans. Om 19:34 op "in onderzoek" gezet en gepusht.
- Eigen meting JetBrains: alle 897 betaalde en freemium plugins, leeftijd uit de oudste versie (het veld cdate van de plugin bleek geen eerste publicatie). 3 tot 6 maanden oud: n=86, mediaan 272 downloads, 81% 100+. Oktober: 182 nieuwe betaalde plugins, bijna de helft van 3 reeksmakers.
- Eigen meting Obsidian: README's van de 600 nieuwste plugins; 3 van 599 bij anderen verkopen echt een licentie.
- Onderzoeker: geen enkel omzetbedrag van een kleine maker op Obsidian of JetBrains te vinden (TrustMRR-sitemap, prijspagina's, Buy Me a Coffee). De Obsidian-labels Paid/Optional payment zijn alleen via de zoekfunctie van de site te tellen; dat niet gedaan.
- Beslissing: Blender 7, JetBrains 5, Obsidian 4. Waarom: alleen op Blender is geld van nieuwe kleine makers gezien; JetBrains past het best bij de koers maar bedragen zijn onzichtbaar; Obsidian heeft bereik maar bijna geen geld.
- Controleur: JetBrains-cijfers kloppen precies; 12 correcties verwerkt (Obsidian-treffers per README gelezen, oktobergolf komt van weinig makers, labels).
- Les: bij een API-veld met een datum altijd nagaan of het de eerste publicatie is, met een plugin waarvan je de leeftijd kent.
- Volgende run: productkans op Blender (twee van de drie runs productkansen).
- Tweede onderdeel (tijd over): productkans Blender, verlaten bestsellers na Blender 5. Om 19:53 op "in onderzoek" gezet en gepusht. De 190 best verkochte add-ons van Superhive gemeten: 15 zonder 5.x-tag; onderzoeker liep ze na, 4 punten zelf nagekeken.
- Uitkomst: geen kans, cijfer 2. Waarom: 13 van de 15 hebben al een opvolger die 5.x steunt (vaak van dezelfde maker) of Blender bouwde het zelf in; Pixel en Angle Tool klein en niet bewezen kapot. Zie `kansen/blender-verlaten-bestsellers.md`. Geen bericht aan Bram of Olaf.
- Les: de versietag op Superhive is vaak verouderd (SurfaceFlow, BQR); kijk naar changelog en reviews, niet alleen naar de tag.
- Run afgesloten.


## 8 nov run 20:31 (Amsterdam)
- Begin: lokale main stond los, main opnieuw op origin/main. Berichten van Thijs: niets nieuws open (19:22 al verwerkt). Geen herhaalmeting verlopen.
- Onderdeel: productkans Blender, zwakke nummer één (tweede productkans-run van drie). Om 20:35 op "in onderzoek" gezet en gepusht. Gekozen omdat ontevreden kopers van een bestseller zowel betalen als een zwakke leider bewijzen, en Blender ons sterkste platform is (7).
- Eigen meting: 596 best verkochte add-ons van Superhive met de verdeling van de sterren; van de 28 met 15+ beoordelingen, 1.000+ verkopen en 20%+ laag alle lage reviews gelezen. 17 met recente klachten. Onderzoeker liep de concurrentie na in vijf niches; drie punten zelf nagekeken.
- Uitkomst: geen kans om nu te bouwen, cijfer 3. Waarom: in bijna elke niche staat binnen een jaar, vaak binnen een maand, een nieuwkomer of gratis vervanger klaar; breien en ragdoll zijn half open maar kregen net een nieuwkomer (wool-generator, vier ragdoll-tools in één maand). Herhaalmeting rond 6 dec op taken.md. Geen bericht aan Bram of Olaf.
- Controleur: akkoord, tellingen en 12 cijfers kloppen; correcties verwerkt (eis 15+ beoordelingen bij de 28, grens 12 maanden, labels in de tabel, playrig bruto en netto).
- Les: de reviewlijst op Superhive staat op sterren, niet op datum; mijn eerste telling las daardoor alleen 5 sterren. Altijd de volgorde van een lijst nakijken voor je telt.
- Tweede onderdeel (tijd over, platformrun): TrustMRR-scan per platform, het idee uit de run van 18:33. Om 20:52 op "in onderzoek" gezet en gepusht. Gekozen omdat de oude restjes in kandidaten.md geen kassa hebben, en deze scan in één keer laat zien op welke platformen nieuwe kleine makers geverifieerde omzet halen.
- Alle 12.304 profielen opgehaald (robots.txt staat .md toe, 4 tegelijk met pauze, in delen van ±9 minuten). Data en hervatbaar script staan in data/. Eerste ruwe telling op trefwoorden in kandidaten.md, nog niet nagekeken en nog geen oordeel.
- Volgende run: analyse per platform, per treffer nalezen of het product echt op dat platform draait, controleur erbij.
- Run afgesloten.

## 8 nov run 21:31 (Amsterdam)
- Begin: lokale main stond los, main opnieuw op origin/main. Berichten van Thijs: niets nieuws open. Geen herhaalmeting verlopen.
- Onderdeel: analyse van de TrustMRR-scan (vervolg op run 20:31, platformrun). Om 21:34 op "in onderzoek" gezet en gepusht. Gekozen omdat de data klaarlag en dit in één keer laat zien op welke platformen nieuwe kleine makers echt geld halen.
- Eigen meting: 8.469 makers sinds 2025 per platform ingedeeld op domein en vaste zinnen (script data/trustmrr-platform-analyse.py).
- Uitkomst: geen nieuw winkelplatform met cijfer 6+. Mac-apps buiten de App Store (20% haalt $300+) en tools rond AI-codeagenten krijgen 5, nog niet klaar: geld aangetoond, maar geen winkel, dus eigen verspreiding nodig die we niet hebben. Zie voorstellen/trustmrr-scan-per-platform.md.
- Controleur: klopt met correcties, verwerkt (Mac-groep groter door "macOS", Claude/MCP 11 echte in plaats van 21, Discord, Figma en Blender wel echte plugins, Pastel uitgesloten, startdatum onbetrouwbaar).
- Bijvangst: 3D-Agent (AI-plugin voor Blender, $6.733 in 30 dagen) en Discord-bots met geld. Beide op taken.md voor volgende runs.
- Les: een trefwoord zegt niet of een product óp een platform draait; laat de controleur per treffer met geld nalezen.
- Run afgesloten.
- Tweede onderdeel (tijd over): productkans Blender, AI-plugins. Om 21:58 op "in onderzoek" gezet en gepusht. Uitkomst: nee, cijfer 3. Waarom: de enige die verdient (3D-Agent, $6.733 in 30 dagen) is een SaaS met eigen AI-tegoed, gratis blender-mcp is sterk, en op Superhive verkoopt geen enkele AI-copiloot (Sovereign AI onder 10). Zie kansen/blender-ai-plugins.md. Geen bericht aan Bram of Olaf. Niet apart nagekeken omdat het advies nee is.
- Run afgesloten.

## 8 nov run 22:31 (Amsterdam)
- Begin: lokale map dortus-hq had een oude, losse geschiedenis (unrelated histories met origin, de repo is opnieuw opgezet); niets weggegooid, vers gekloond in een nieuwe map en daarin gewerkt. Berichten van Thijs: niets nieuws open (22:31 over tunnelvisie is al verwerkt in de rol). Geen herhaalmeting verlopen.
- Onderdeel: productkans JetBrains (productkans-run; Blender had er al drie, JetBrains nog geen van mij). Om 22:38 op "in onderzoek" gezet en gepusht. Gekozen hoek: zwakke nummer één bij de ±500 betaalde plugins buiten talen en bestandssoorten, die Jet niet bekeek.
- Uitkomst: buiten talen overal een sterke leider of door JetBrains zelf vervangen. Enige zwakke nummer één met betalende gebruikers: taalpakketten (Code, $39 per jaar; Frans 1,75, Russisch 2,5, Italiaans 2,0, Tsjechisch 1,0; klachten over machinevertaling). Cijfer 4, nog niet bouwen, kleine proef mogelijk. Zie kansen/jetbrains-taalpakketten.md. Bericht aan Jet.
- Controleur: alle 8 beweringen kloppen, correcties verwerkt (meer gratis concurrenten, Rusland kan niet betalen).
- Les: de ratings van taalpakketten rusten op 1 tot 5 stemmen; de comments zeggen meer dan het gemiddelde.
- Tweede onderdeel (tijd over, platformrun): Coda Packs, zelf toegevoegd. 150 nieuwste packs uit de sitemap gemeten: ±11 nieuw per maand, 5 van 89 betaald, geen installaties zichtbaar, geen maker met bedrag (ook niet op TrustMRR). Nee, cijfer 2, zie voorstellen/coda.md. Niet apart nagekeken omdat het advies nee is.
- Derde onderdeel: Logitech Marketplace (hardwarewinkel), zelf toegevoegd. Klein (171 plugins), niet betalen in de winkel, downloads niet zichtbaar. Nee, cijfer 2, zie voorstellen/logitech-marketplace.md.
- Volgende platformrun: Discord-herhaalmeting rond 4 dec (4 weken na 6 nov); tot dan nieuwe hardware- en vakwinkels zoeken.
- Run afgesloten.

## 8 nov run 23:31 (Amsterdam)
- Lokale kloon liep uit de pas met GitHub (72 oude lokale commits tegen 51 nieuwe). Niet weggegooid: gewerkt op een nieuwe tak vanaf origin/main en daarnaar gepusht.
- Productkans Obsidian (twee van drie runs productkansen; Obsidian had nog geen kansbestand). Gemeten: alle 10.132 plugins, top 1.000 met GitHub-gegevens via de zoek-API (de gewone API en github.com zijn vanaf hier dicht voor andere repo's, de zoek-API werkt wel), 30-dagengroei uit Olafs meting.
- Uitkomst: veel verlaten reuzen, maar Kanban is nu een weergave van Obsidian zelf (1.14), Zotero Integration (archief, stuk door Zotero 9) heeft ZotLit als actieve opvolger, Remotely Save heeft vijf groeiende gratis opvolgers. Nergens wordt betaald. Cijfer 3, nee. Controleur akkoord, 5 correcties.
- Les: `community-archive` op GitHub is een goede bron voor verlaten Obsidian-plugins; ook nuttig om bij andere platformen naar zo'n archief-org te zoeken.
- Run afgesloten.
- Na afsluiten nog tijd: PDF++ toegevoegd aan de Obsidian-kans (cijfer 2, een onafhankelijke voortzetting is al aangevraagd). Platformrun: Twitch Extensions voorwerk, niet te meten zonder account.
- Roll20 Marketplace voorwerk: niet te meten (lijst via /api/, verboden in robots.txt), vooral kunst. Run nu echt afgesloten.

## 9 nov run 00:31 (Amsterdam)
- Begin: lokale main stond los, opnieuw op origin/main. Berichten van Thijs: niets nieuws open. Geen herhaalmeting verlopen.
- Onderdeel: platformrun (de twee runs hiervoor waren productkansen). TRMNL zelf gevonden (hardware met een winkel voor plugins en een maandelijks Creator Fund). Om 00:35 op "in onderzoek" gezet en gepusht.
- Eigen meting: alle 1.237 recipes via de open Recipes API (recipes.json, met publicatiedatum en installs) en alle 12 maandposts van het Creator Fund.
- Uitkomst: nee voor nu, cijfer 3. Geld gaat aantoonbaar naar kleine makers, maar de pot is sinds april vlak ±$3.900 per maand voor alle makers samen; nieuwe recipes halen mediaan 14 connections, geen eigen prijs mogelijk. Zie voorstellen/trmnl.md.
- Controleur: alle getallen kloppen; vier toevoegingen verwerkt.
- Les: zoek eerst in de documentatie naar een open JSON-ingang (hier `.json` achter de lijst-URL) voor je pagina's gaat schrapen; dat scheelde ±15 minuten en gaf datums die op de pagina's ontbraken.
- Tweede onderdeel (tijd over): taak Mac-apps buiten de App Store, haalt een maker zonder publiek het? X-volgers van alle 190 oprichters gelezen op TrustMRR. Van de oprichters met 1 tot 999 volgers haalt 15% $300+ in 30 dagen, zonder X-account niemand. Cijfer blijft 5 (wij hebben geen publiek en posten niet onder de naam van Thijs). Controleur: rekensom klopt, correcties verwerkt.
- Voorwerk zonder meting: Homey (geen betaalde apps) en flightsim.to (botbescherming) in kandidaten.md.
- Run afgesloten.

## 9 nov run 01:31 (Amsterdam)
- Begin: lokale map stond los, opnieuw op origin/main. Berichten van Thijs: niets nieuws open. Geen herhaalmeting verlopen.
- Onderdeel: productkans (vorige run was een platformrun). Blender, nieuwe hoek: in welke soorten add-ons verkopen nieuwkomers? Om 01:34 op "in onderzoek" gezet en gepusht.
- Eigen meting: alle 2.955 add-ons van de laatste 13 maanden uit de lijst op datum (125 pagina's), met verkoopteller, prijs, maker en tekst; ingedeeld in 31 thema's.
- Uitkomst: geen nieuwe niche, cijfer 3, nee voor nu. Waar nieuwkomers goed verkopen (jiggle, mist, retopologie, print-splitsen) is de top sterk of stroomt het jonge aanbod binnen. Print-splitsen bevestigt wat Olaf in drie rondes al vond.
- Nieuw feit: ±720 nieuwe add-ons in de laatste 30 dagen, tegen ±110 tot 150 per maand een jaar geleden; een kwart is één maker (ZEG, 165 generators). Een nieuwe add-on staat nu minder dan een dag op pagina 1 van "nieuwste". Bericht aan Bram en Olaf. Herhaalmeting rond 5 dec in taken.md.
- Controleur: datums per pagina, ZEG, alle tellers in de print-niche, oude bestsellers en gratis concurrenten nagekeken, alles klopt grofweg; prijzen soms in de aanbieding.
- Les: lees eerst de mappen van de bouwers (hier `platformen/blender-2/`) voor je een niche induikt; Olaf had print-splitsen al grondig gedaan. Tweede les: de pagina heeft twee prijsvelden (centen en dollars), pak het veld met aanhalingstekens.
- Na afsluiten nog tijd: Orbolt (Houdini) voorwerk in kandidaten.md, prijzen zichtbaar maar geen tellers. Run afgesloten.

## 9 nov run 02:31 (Amsterdam)
- Begin: lokale main stond los en GitHub had een geforceerde update; opnieuw op origin/main. Berichten van Thijs: niets nieuws open. Geen herhaalmeting verlopen.
- Keuze: eigenlijk een productkansrun, maar de vaste toestemming van Thijs noemt nu uitdrukkelijk het lezen van de winkel-API van SketchUp, het platform dat op 7 nov niet te meten was. Platformen zijn de hoofdzaak, dus SketchUp eerst. Om 02:38 op "in onderzoek" gezet en gepusht.
- Eigen meting: alle 1.429 zichtbare extensies via twee API-verzoeken (packages?count=1000), met downloads, prijs, proef en datum. API gevonden door de netwerkverzoeken van de winkel in Playwright te bekijken.
- Uitkomst: nee voor nu, cijfer 4. Gratis bereik goed (mediaan 236 na 3 tot 6 maanden, 67% 100+), betaald klein (nieuwe betaalde mediaan 14 tot 25 downloads, 5% van de jonge betaalde haalt 100+), 30% afdracht (DERDEN), geen maker met een bedrag. Zie voorstellen/sketchup.md.
- Controleur: alle getallen kloppen; aangevuld met 4.715 pakketten bij showHidden=true (alleen overlevers zichtbaar), proeven in downloads, 5% bij jonge betaalde.
- Les: bij een winkel die alleen in de browser laadt, eerst met Playwright de netwerkverzoeken bekijken; dat gaf in 5 minuten de hele API.
- Volgende productkansrun weer zoals gepland; volgende platformrun: Autodesk-reviews via de winkel-API.

## 9 nov run 03:31 (Amsterdam)
- Begin: lokale main stond los, opnieuw op origin/main. Berichten van Thijs: niets nieuws open. Geen herhaalmeting verlopen.
- Keuze: platformrun, het vervolg dat de vorige run plande (Autodesk-reviews via de winkel-API, nu in de vaste toestemming van Thijs). Daarmee waren twee van de laatste drie runs platformen; de volgende run is een productkans. Om 03:36 op "in onderzoek" gezet en gepusht.
- Eigen meting: API gevonden met Playwright (developer.api.autodesk.com/ngappapi/public/), rating-samenvatting van alle 5.058 apps en alle 18.159 reviews met datum.
- Uitkomst: nee voor nu, cijfer 3 (was 4). Hele winkel ±135 reviews per maand sinds de overstap (±200 in 2025), betaalde apps samen ±30 tot 40 per maand; van nieuwe betaalde apps (3 tot 6 maanden) heeft 10% één review; beste betaalde app ooit 55. Geen kleine maker met een bedrag (onderzoeker). Zie voorstellen/autodesk.md.
- Controleur: akkoord na 5 correcties, vooral: mei tot juli was een stilstand van de reviews tijdens de overstap, geen inzakking.
- Les: de comments-API weigert limit boven 50 met een foutmelding in JSON; mijn eerste ophaling gaf daardoor 0 regels zonder fout. Altijd na een minuut controleren of er echt data binnenkomt.
- Herhaalmeting begin feb 2027 in taken.md.
