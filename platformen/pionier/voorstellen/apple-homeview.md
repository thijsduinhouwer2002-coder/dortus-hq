# Voorstel pionier: Apple HomeView (widgets van iPhone-apps)

Noor, run 9 nov 2026 01:40 UTC. Cijfer **4**, advies **nee voor nu, volgen**.

## Wat het is
Apple HomeView is een nieuw thuisscherm van Apple: 7 inch, vierkant, op tafel of aan de muur, herkent tot zes gezinsleden aan hun gezicht (GEZIEN, https://www.apple.com/apple-homeview/specs/). Aangekondigd 13 okt 2026, $299, levering vanaf **13 nov 2026** in de VS, VK, Canada, Australië, Nieuw-Zeeland, India en Singapore, Zuid-Afrika via resellers. **Niet in de EU** (GEZIEN, https://www.apple.com/newsroom/2026/10/meet-apple-homeview-a-new-way-to-enjoy-entertainment-and-manage-the-home/).

HomeView heeft **geen eigen App Store**. Derden komen er op twee manieren op:
- Widgets van iPhone-apps, alleen het kleinste formaat (system small), op het eigen beginscherm van elk gezinslid en op de "Modular face": één per huishouden, maximaal vier widgets, die van de iPhones van verschillende gezinsleden mogen komen (GEZIEN, Apple HIG Widgets, bijgewerkt 13 okt 2026, https://developer.apple.com/design/human-interface-guidelines/widgets).
- Audio- en video-apps van CarPlay, in categorieën die Apple aanwijst (GEZIEN, ontwikkelaarsovereenkomst 6.4, https://developer.apple.com/support/terms/apple-developer-program-license-agreement/; DERDEN, https://9to5mac.com/2026/10/14/homeview-can-display-third-party-widgets-from-your-iphone/).

Belangrijk: elke bestaande iPhone-widget verschijnt **automatisch** op HomeView, tenzij de maker hem uitsluit (overeenkomst 6.4.1, GEZIEN). WidgetKit heeft geen aparte HomeView-plek, dus je kunt HomeView ook niet herkennen of apart bedienen (GEZIEN, https://developer.apple.com/tutorials/data/documentation/widgetkit/widgetlocation.json).

## De vijf vragen

**1. Groeit het platform hard en zichtbaar?** Onbekend, en het bewijs wijst eerder op voorzichtig. Het apparaat is nog niet geleverd. Geen voorbestelcijfers of analistenschattingen gevonden. Enige aanwijzing: levertijden voor sommige kleuren schoven op 16 okt naar 23 nov tot 7 dec (DERDEN, https://macrumors.com/2026/10/16/apple-homeview-preorder-wait-times/). Apple's thuisproducten hebben een zwakke geschiedenis: HomePod ±3 mln in de VS en 6% aandeel in 2018 (DERDEN, https://www.macrumors.com/2018/08/02/homepod-estimated-3-million-sales/), het segment Wearables, Home en Accessoires zakte van $41,2 mld (2022) naar $35,7 mld (2025) (DERDEN, https://www.tikr.com/blog/apples-home-segment-is-down-14-since-2022-and-it-just-got-a-robot-homeview-plan-heres-what-it-means-for-aapl-stock). Motor is wel sterk: Apple, Siri AI, een grotere versie in 2027 of 2028 (DERDEN, gerucht Gurman). Score: onzeker.

**2. Is de winkel jong?** Er is geen winkel. Gevonden worden loopt via de gewone iOS App Store, een oceaan. Zoeken op "homeview" in de App Store (VS) geeft 47 resultaten, vooral oude camera-apps; er is één app die de naam al pakte, "SmartHome Dashboard - HomeView" (juli 2026, 3 beoordelingen) (GEZIEN, https://itunes.apple.com/search?term=homeview&entity=software&country=us). De nieuwe plek is dus het apparaat zelf, niet een winkel.

**3. Kan er betaald worden?** Ja, nu al: de App Store met eenmalige aankopen en abonnementen, 15% afdracht in het Small Business Program (DERDEN, radar 8 nov). Kosten vooraf: Apple Developer Program $99 per jaar op naam van Thijs of de BV, en bouwen vraagt een Mac (kan via macOS-runners in GitHub Actions). Voldoet aan de eis van Thijs.

**4. Is er vraag te zien?** Een beetje. Best gewaardeerde reacties onder MacRumors: gedeelde boodschappenlijst in Notes, recepten (Paprika), YouTube in de keuken (GEZIEN, https://www.macrumors.com/2026/10/14/apple-homeview-apps-carplay/). Een concurrent noemt het gat: geen gedeelde kalender, klusjeslijst, beloningen of zakgeld (DERDEN, partijdig, https://greenlight.com/learning-center/reviews/apple-homeview-review). Reddit en het MacRumors-forum blokkeren curl, dus geen draadjes geteld.

**5. Is de eerste plek te pakken?** Moeilijk. Omdat elke iPhone-widget vanzelf meekomt, staan de grote gezinsapps op dag één al op HomeView: Cozi (402.673 beoordelingen), Skylight (52.624), FamilyWall (24.912), Calendars (122.682) (GEZIEN, iTunes Search API, term "family calendar widget"). Op de Modular face zijn maar vier plekken voor het hele huishouden. Precedent: bij nieuwe widgetplekken wonnen algemene widgetapps (Widgetsmith en andere: 7 mln+ downloads in een week bij iOS 14, DERDEN, https://appfigures.com/resources/insights/20200925/1-widgets-widgets-widgets), terwijl apps speciaal voor StandBy klein bleven: "StandBy 27" ±17.000 installs, "Smart Widget - Standby" ±112.000 (GEZIEN, AppGoblin-schattingen, https://appgoblin.info/apps/6466030489 en https://appgoblin.info/apps/1534517360).

## Risico
HomeView kan net als HomePod klein blijven. Teken dat het stokt: geen verkoopschattingen boven ±2 mln in het eerste jaar, of geen EU-lancering in 2027. Teken dat het wel iets wordt: Apple opent een eigen HomeView-sectie in de App Store, een eigen widgetformaat of een "Conversational Apps"-categorie (code in de 27.3-beta, DERDEN, https://www.macrumors.com/2026/11/05/homeview-code-suggests-support-ai-chatbot-apps/).

## Categorie en productidee (alleen als het later opengaat)
Een gezinswidget voor de Modular face: wie moet wat vandaag (klusjes en afspraken van alle gezinsleden in één kleine widget), gratis met een betaald gezinsabonnement. Nu niet bouwen: de widget komt in dezelfde App Store als Cozi en Skylight, zonder eigen plek om gevonden te worden, en niet in Nederland te verkopen aan HomeView-bezitters.

## Waarom een 4
Betalen werkt (harde eis gehaald), maar de twee zwaarste vragen vallen tegen: geen jonge winkel (vraag 2) en geen lege eerste plek, omdat bestaande widgets automatisch meekomen (vraag 5). Groei (vraag 1) is nog niet te meten.

## Herhaalmeting
Rond **8 jan 2027**: verkoopschattingen na de feestdagen (CIRP, Counterpoint), zoeken op "homeview" in de App Store (zelfde API, tel nieuwe apps met HomeView in naam of tekst), en de HIG en WidgetKit-documentatie op een eigen HomeView-plek of -formaat. Meteen opnieuw wegen als Apple een HomeView-gallery of eigen apps voor HomeView aankondigt.
