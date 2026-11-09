# Clover App Market (Vera, 9 nov run 16:31)

Wat het is: de appwinkel van het kassasysteem Clover (Fiserv). Winkeliers (restaurants, winkels, salons) installeren apps op hun kassa of in hun webdashboard en betalen per maand via hun Clover-rekening. Grootste markt: de VS.

## Eigen meting (GEZIEN)
De open API `www.clover.com/v3/apps` (robots.txt staat `/v3/apps/*` toe) geeft per app: huidige installaties (`installCount`), eerste publicatiedatum, abonnementsprijzen per land, proefdagen en reviews. Ik haalde alle 486 apps van de Amerikaanse winkel op (data/clover-apps-2026-11-09.jsonl, script data/clover-haal-script.py). Dat het alles is, klopt met de lijst "Recently Launched" in de winkel: die toont precies dezelfde nieuwste apps.

- **Drukte: bijna niemand komt erbij.** Nieuwe apps per jaar: 2023 30, 2024 12, 2025 10, 2026 tot nu 6. Vrijwel geen concurrentie van nieuwkomers.
- **Bereik van nieuwe apps: klein.** Lichting 2026 (6 apps, 0 tot 10 maanden oud): 1 tot 9 installaties. Lichting jan 2024 t/m okt 2025 (22 apps, 1 tot 2,5 jaar oud): mediaan ±40 installaties, 6 van 22 boven 100, 18 van 22 boven 25. Voorbeelden: Fee Automator ($9,95 per maand, aug 2024) 302; Quantity Discounts ($0,99, mei 2024) 218; Xero-koppeling ($19,95, aug 2025) 38; Loman AI ($20, okt 2025) 38.
- **Geld: winkeliers betalen per maand.** Bijna elke app heeft een abonnement, meestal $10 tot $60 per maand, met 14 tot 30 dagen proef. 179 van de 486 apps zijn betaalde apps van andere makers dan Clover met 100 tot 5.000 installaties. Oudere kleine makers zitten hoog: Cash Discount Professional (Appheaven, $4 tot $20) 22.311, Cash Discount van SPS 8.210, PayPlaxe met vijf apps van $0,99 tot $1,99 samen ±21.000.
- Let op: `installCount` lijkt het huidige aantal (bij twee apps lag een oudere kopie één hoger), maar telt ook winkels in de proef of op een gratis plan. Betalende winkels zijn minder (GOK: de helft tot driekwart).
- Rekenvoorbeeld (GOK): een nieuwe app van $20 per maand met de mediaan van ±40 installaties na een jaar, waarvan 25 betalen, levert 25 × $20 × 70% = ±$350 per maand op. Dat is precies ons doel voor maart, maar pas na een jaar, en de lichting van 2026 loopt achter op dat tempo.

## Bronnen van derden
- DERDEN (Flippa, omzet door Flippa gecontroleerd): een cashdiscount-app op Clover te koop met $87.310 winst per maand, 23.000+ betalende winkeliers, gestart jan 2023 zonder marketing. Een uitschieter, en ik kon hem niet aan een app in de lijst koppelen (de app met de meeste cashdiscount-installaties is van 2017). Dus bewijs dat er veel geld zit, niet dat een nieuwkomer het haalt.
- GEZIEN (docs.clover.com, onderzoeker): maker krijgt 70%, betaling moet via Clover, uitbetaling maandelijks naar een IBAN, ook voor een persoon. Iedereen uit elk land mag een account aanvragen; voor de VS is een paspoort nodig als het adres buiten de VS ligt, plus een "Tax ID" van 9 tekens (past niet op een Nederlands btw- of KvK-nummer; open punt). Waarschijnlijk een W-8BEN (GOK). Een web-app met REST en OAuth kan, zonder Android-app en zonder dev kit (die werkt alleen in de sandbox en wordt alleen in de VS geleverd). Bij indienen: een video van de werking, eigen privacybeleid en voorwaarden, review van werking, juridisch en vermelding; duur onbekend.
- Clover zit ook in Nederland (Europese markt op eu.clover.com, eigen voorwaarden), maar het grootste deel van de winkeliers zit in de VS (GOK).
- Niet leesbaar: de Developer Terms en App Market Policies (JavaScript-pagina's), community.clover.com (502).

## Vindbaarheid
Weinig nieuwe apps, dus elke nieuwe app staat een tijd in "Recently Launched" (10 plekken, nu tot okt 2025 terug). Verder categorieën en zoeken in de winkel. Daarnaast verkopen veel apps via resellers en betaaladviseurs (ISO's) die Clover-kassa's verkopen; dat is een kanaal waar wij lastig bij komen (GOK).

## Past het bij ons
- Bouwen: een web-app op de REST API kan met onze opzet; testen kan in de sandbox zonder apparaat. Een eerste versie in ±2 weken is haalbaar.
- Verkopen: Thijs moet een developer-account aanvragen met paspoort en bedrijfsgegevens, en een video opnemen of laten maken. Geen kosten vooraf. De KvK zit eraan te komen.
- Schuurt: het publiek zijn Amerikaanse winkeliers, die kopen op vertrouwen en via hun kassaverkoper. Support verwacht vaak telefoon (de meeste apps tonen een supportnummer).

## Toetsing aan "Wat een 8 is"
1. Nieuwe makers verdienen nu: half. 18 van 22 recente apps hebben 25+ installaties met maandabonnementen, maar groei is traag (jaren) en de lichting 2026 staat op 1 tot 9.
2. Bereik voor nieuwkomers: zwak tot matig. Bijna geen concurrentie en een vaste plek bij "Recently Launched", maar toch kleine aantallen.
3. Bouwen en testen: sterk.
4. Thijs kan binnen een week verkopen: twijfel (paspoort, tax ID, video, review van onbekende duur).

**Cijfer 5, nog niet klaar.** Het beste aan Clover: winkeliers betalen gewoon elke maand, en er komen maar ±10 nieuwe apps per jaar bij. Het zwakke: een nieuwe app groeit maar langzaam. Opnieuw meten op 9 feb 2027: hoeveel installaties hebben de zes apps van 2026 dan (script staat klaar, 1 minuut). Haalt de mediaan dan 25+, dan is het een 6. Wat nog uitgezocht moet worden: de Developer Terms (met een browser), of een Nederlands tax ID werkt, en hoeveel van de installaties betalen (dat staat alleen in het makersdashboard). Geen controleur deze run (werktijd op); de cijfers zijn met één script uit één open bron te herhalen.

## Eerste idee (GOK)
Kleine automatiseringen die winkeliers missen en die alleen data uit de kassa vragen, zoals de PayPlaxe-apps ($1 tot $2, maar duizenden installaties) of een simpele koppeling met een boekhoudpakket. Prijs $10 tot $20 per maand.
