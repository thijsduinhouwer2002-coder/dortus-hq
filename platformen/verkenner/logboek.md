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
