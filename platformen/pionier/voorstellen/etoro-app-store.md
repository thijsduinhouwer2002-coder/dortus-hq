# eToro App Store (trading- en analyse-apps binnen eToro)

Noor, 9 nov 2026, run 00:40 UTC. Labels: GEZIEN (zelf gelezen), DERDEN (met link), GOK.

**Advies: nog niet klaar. Cijfer 5.** Jonge winkel in een groot, gezond groeiend platform, maar betalen werkt nog niet aantoonbaar, de winkel is niet openbaar te tellen en toelating gaat per aanvraag. Opnieuw kijken na de Q3-cijfers (10 nov 2026) en zodra er een betaalde app of een regeling voor afrekenen verschijnt.

## Wat het is
eToro (beursgenoteerde broker, 40 mln geregistreerde gebruikers) opende op 14 april 2026 de eToro App Store: apps van derden die binnen eToro draaien, met één klik te installeren, gebouwd op de openbare eToro-API (handelen, koersen, portefeuille, watchlists, sociale data, AI-agentportefeuilles), plus een MCP-server, agent skills, een CLI en een no-code omgeving waarin Pro Investors zelf tools maken (GEZIEN, https://www.etoro.com/news-and-analysis/press-releases/etoro-launches-etoro-app-store-its-ai-enabled-application-ecosystem-for-trading-and-investing/ en https://builders.etoro.com/).

## De vijf vragen

**1. Groeit het platform hard en zichtbaar?** Gezond, niet hard. Funded accounts 3,63 mln (Q2 2025) naar 4,28 mln (Q2 2026), +18% (GEZIEN, https://www.etoro.com/news-and-analysis/press-releases/etoro-reports-second-quarter-2026-results/); juli 4,32 mln, augustus 4,36 mln waarvan ±110k door overnames (DERDEN, https://investingnews.com/etoro-reports-selected-august-business-metrics/). Aantal trades in juli vlak, bedrag per trade -23% (GEZIEN, zelfde persbericht). Motor: eToro zet zwaar in op AI en agents (Tori, Agent Portfolios, MCP), maar het is een volwassen bedrijf, geen jong platform dat ontploft.

**2. Is de app-winkel jong?** Ja. Open sinds 14 april 2026, voorwaarden (Builders' Economy Terms) van 17 feb 2026 noemen het een beta (DERDEN, https://tradeinformer.com/broker-news/etoro-launches-ai-trading-app-store). In Q2 "meer dan 75 apps, gebouwd door developers, partners en Pro Investors" (GEZIEN, Q2-persbericht). Er is geen openbare catalogus: builders.etoro.com/appstore zegt letterlijk "it is not a catalog of listings"; de winkel zit alleen in de ingelogde eToro-app (GEZIEN, https://builders.etoro.com/appstore). Ik vond geen API die de app-lijst teruggeeft. Aantal per categorie en per maand: niet te meten zonder in te loggen. Alleen in "eligible markets", lijst van landen niet gevonden.

**3. Kan er betaald worden?** Nog niet aantoonbaar. De voorwaarden zeggen dat eToro "from time to time, at its sole discretion" makers kan toestaan geld te vragen, alleen met voorafgaande toestemming van eToro, en dat eToro zelf kosten mag rekenen aan gebruikers en makers (art. 2.2 en 10.9, GEZIEN, https://www.etoro.com/wp-content/uploads/2026/03/Master_eToro_Builders_Economy_Terms_17-Feb-2026-clean_R.pdf). Art. 11.5.2 noemt abonnementen voor toegang tot je tool als toegestaan. Maar: geen betaalde app gevonden, geen kassa, geen afdracht, geen uitbetaling beschreven; de API-changelog tot 12 okt 2026 zegt niets over betalen (GEZIEN, https://api-portal.etoro.com/core/changelog.md); eToro "hasn't outlined exact revenue-sharing models" (DERDEN, https://thecurrencyanalytics.com/finance/etoro-opens-app-store-for-third-party-trading-tools-252528/amp). Dus: een plan voor geld bestaat op papier, per geval, zonder datum. Volgens de regel van Thijs (8 nov 19:16) hooguit een 6.

**4. Is er al vraag te zien?** Niet te meten. Reddit en X zijn met curl dicht, de helpartikelen (Salesforce) gaven geen inhoud. Wel: bij de start hadden 800+ Pro Investors al 1.000+ tools gebouwd (DERDEN, https://linas.substack.com/p/weeklyfintechpulse396), en op de Pro Investor Summit (3 tot 5 nov 2026) werden twee door Pro Investors gebouwde apps getoond (GEZIEN, https://builders.etoro.com/summit). eToro noemt zelf als soorten: trading bots, dashboards, sociale tools, multi-product apps (GEZIEN).

**5. Is de eerste plek in een categorie te pakken?** Onbekend. Zonder catalogus weet ik niet wie er in welke categorie staat. Mijn GOK: de no-code tools van Pro Investors vullen de hoek "mijn eigen strategie als app"; een kleine maker van buiten zou het eerder moeten zoeken in hulpmiddelen die eToro zelf mist (belastingoverzicht per land, dividendkalender, risico per portefeuille, kopieerhandel-analyse). Eerst moeten we de winkel kunnen zien.

## Risico
- eToro houdt de deur dicht: toelating per aanvraag, "approve, reject, or condition at its sole discretion" (art. 10.2, GEZIEN), en betalen alleen met toestemming. Dan wordt het een partnerprogramma, geen open winkel.
- Financiële regels: apps die orders geven, vallen onder strenge eisen (handmatige noodstop, risicowaarschuwingen, geen beleggingsadvies). Dat kost bouwtijd en geeft aansprakelijkheid.
- De homepage van de builders portal zegt nog steeds "An app store is launching inside the eToro platform" (GEZIEN, https://builders.etoro.com/): de winkel staat zelf nog niet vol in de etalage.
- Teken dat het stokt: geen nieuw app-aantal in de Q3-cijfers van 10 nov, of nog steeds geen betaalregeling begin 2027.

## Productidee (als betalen opengaat)
Een portefeuille-risicomonitor voor eToro: blootstelling per sector, land en munt over eigen posities én gekopieerde Pro Investors heen, met waarschuwing als één aandeel te zwaar weegt. Alleen lezen (geen orders), dus minder regels; abonnement per maand.

## Wat ik niet kon meten en hoe later wel
- App-lijst, installs, makers: alleen ingelogd. Thijs heeft geen eToro-account nodig voor ons werk; niet aanvragen. Wachten op openbare cijfers.
- Herhaalmeting: Q3-cijfers op 10 nov 2026 lezen (aantal apps, funded accounts sep), en rond 8 jan 2027 de voorwaarden en de API-changelog op "fee", "subscription", "payout" doorzoeken (`curl -sL https://api-portal.etoro.com/core/changelog.md | grep -i -E "fee|subscri|payout|monet"`).
