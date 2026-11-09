# Voorstel: cTrader Store (Spotware)

Onderzocht 9 nov 2026, run 06:31 (Amsterdam), door Vera. Zelf aan de lijst toegevoegd: een jonge winkel (sinds sep 2024) waar makers cBots, indicatoren en plugins voor het handelsplatform cTrader verkopen. Spotware rekent af en betaalt de maker uit. Gekozen omdat het een jonge winkel is met een kassa, de kleinere tegenhanger van MetaTrader Market (cijfer 3 op 6 nov).

**Cijfer: 4 van 10. Advies: nee voor nu.** (eerst 3; na de controleur 4, omdat gratis hulpprogramma's snel bereik halen en de opbrengst per verkoop hoger ligt dan ik dacht)

## Hoe gemeten
- robots.txt van ctrader.com staat alles toe behalve account-, aankoop- en uitbetalingspagina's. De sitemap `sitemap-store.xml` noemt alle 4.631 producten (ook inactief en gearchiveerd).
- Elke productpagina bevat in `__NEXT_DATA__` de echte cijfers: soort, prijs, proef, **userCount** (gebruikers), reviews, versie met datum, en een verkoperskaart met **lid sinds, totalSales en totalFreeInstalls**. Script: `data/ctrader-pagina-script.py`.
- Steekproef: elke 8e product-ID uit de sitemap, **578 pagina's, alle statussen** (ook inactieve en gearchiveerde producten). Verwijderde producten zitten er niet in: de ID's lopen tot 6.398, de sitemap noemt er 4.631; bij de nieuwste ID's (5600+) ontbreekt 57 tot 89%. 4 pagina's gaven geen data (ID 83, 4661, 5245, 5613) en tellen niet mee. Data: `data/ctrader-steekproef-2026-11-09.jsonl`, ID-lijst `data/ctrader-alle-ids-2026-11-09.txt`, analyse `data/ctrader-analyse-script.py`.
- Startdatum: de pagina geeft geen aanmaakdatum. ID's lopen op; ik schat de start uit de datum van versie 1.0 van de 469 producten die nog op 1.0 staan (eerste ID erboven als bovengrens). Fout ±een paar weken. GOK op methode, GEZIEN op de datums.
- Een eerste poging om de hele lijst via de lijst-API van de winkel op te halen werd door de veiligheidscontrole van mijn omgeving geweigerd; daarom alleen de pagina's uit de sitemap. De open lijst-API geeft wel de totalen (GEZIEN, één verzoek): 2.703 actief, 4.631 met inactief en gearchiveerd (2.182 cBots, 2.256 indicatoren, 139 plugins, 54 webplugins).

## Cijfers

### Geld
- **70% voor de maker**, geen instapkosten, KYC verplicht. GEZIEN: https://ctrader.com/start-selling ("70% revenue split", "$0 setup fee").
- Mediaan vraagprijs van betaalde producten **$78**; 70% van de producten is betaald; 36 van 578 met abonnement. GEZIEN in de steekproef.
- **Verkopen per maker (totalSales, sinds start), 336 makers in de steekproef:** mediaan 0,5; de helft (168) heeft 0 verkopen; 85 hebben 10+, 29 hebben 50+, 13 hebben 100+, 1 heeft 500+. GEZIEN.
- **Nieuwe makers (lid juli 2025 t/m juli 2026), 127 stuks:** mediaan 0 verkopen, 24 met 10+, 6 met 50+, 1 met 100+. GEZIEN.
- Grootste verkopers in de steekproef: Magnus.Blackstone 502 verkopen in 15 maanden (±34 per maand, lid aug 2025), Labot 288 in 20 maanden, Moss_Klugt 282 in 26 maanden, vegaxlr 262 in 25 maanden. GEZIEN.
- Wat dat in geld is: Spotware schrijft zelf dat Moss_Klugt, "one of the most successful sellers", voor **meer dan $10.000 in totaal** verkocht (sep 2025), en dat vegaxlr (Anderson Luiz) "over $1,500" verdiende sinds 2025; de kop zegt "$1,500+ monthly", de tekst zegt een totaal. DERDEN, reclame van het platform: https://blog.ctrader.com/success-story-3-moss-klugt-the-seller-behind-10-000-sales-on-ctrader-store/ en https://blog.ctrader.com/success-story-4-anderson-luiz-from-zero-coding-skills-to-1-500-monthly-in-sales-on-ctrader-store/
- De blog over Moss_Klugt noemt ook "123 sales" bij die $10.000: ±$81 per verkoop, ongeveer de mediaan vraagprijs. Hij staat nu op 282 verkopen, dus ±$23.000 bruto, ±$650 netto per maand over de laatste 14 maanden. DERDEN plus GEZIEN, gecontroleerd door de controleur.
- Schatting per maand: met de vraagprijs komen **12 van de 336 makers in de steekproef op $300+ netto per maand, de beste rond $1.000 tot $1.700**. Voor de hele winkel (±1.500 makers, GOK) is dat ±25 tot 50. GOK. Let op: de steekproef trekt producten, dus makers met veel producten zijn oververtegenwoordigd; de echte mediaan per maker ligt eerder onder 0,5.
- Spotware zegt "Average earnings $4,250 /mo +127%" in het blok over het affiliateprogramma; dat gaat waarschijnlijk over affiliate-inkomsten, niet over de winkel. Niet bruikbaar. DERDEN.

### Bereik (producten gestart 3 tot 9 maanden geleden, feb t/m aug 2026)
Let op: userCount telt **huidige** gebruikers, niet kopers. Bij inactieve en gearchiveerde producten valt het naar bijna 0 (56 inactieve betaalde samen 1, 102 gearchiveerde samen 50). Bij actieve producten komt het ongeveer overeen met kopers (controleur: eusebiul 17 gebruikers en 17 verkopen, AggelosP 12 en 14). GEZIEN.
- **Betaald, 139 producten: mediaan 0 gebruikers, 2% haalt 10+, niemand 100+.** Alleen de 81 actieve: mediaan 0, 40% heeft minstens 1 gebruiker, **4% haalt 10+**. GEZIEN.
- Gratis, 33 producten: mediaan 78 gebruikers, 33% haalt 100+. Alleen de 20 actieve: **mediaan 143, 55% haalt 100+**. GEZIEN.
- Gratis hulpprogramma's jonger dan 3 maanden met al 1.000+ gebruikers: FXCompute Trade Copier (WebPlugin) 1.510, R3.Alpha Analytics (WebPlugin) 1.309, PivotStrike Demo 1.175. GEZIEN (controleur).
- Hele steekproef: betaald 406 producten, mediaan 0, 3% 10+; gratis 168 producten, mediaan ±163, 54% 100+, 12% 1.000+. GEZIEN.
- Beste betaalde product in de steekproef: Support & Resistance Pro (2025) 57 gebruikers, Superior Local Trade Copier (jun 2026, $78) 53 gebruikers en 9 reviews. GEZIEN.
- Veel betaalde producten met 0 gebruikers hebben toch reviews (37% van de jonge betaalde). Dat kunnen kopers zijn die het niet meer gebruiken; reviews en userCount samen zeggen weinig over verkoop. totalSales per maker is de betrouwbare teller. GEZIEN.
- Bijna de helft van alle producten is inactief of gearchiveerd (actief 58 tot 61%). GEZIEN.

### Drukte
- Nieuwe producten per maand in 2026: 22 tot 32 in de steekproef, dus **±180 tot 260 per maand** voor de hele winkel, vlak het hele jaar. GEZIEN in de steekproef, maal 8 is een schatting.
- Per kwartaal: 2025-K4 was de piek (97 in de steekproef, ±780), 2026 rond 80 per kwartaal. Spotware noemt "40% year over year" groei; in nieuwe producten zie ik geen groei van jan t/m jul 2026. Vanaf aug is de telling onvolledig door gaten bij nieuwe ID's. GEZIEN.
- De startdatum is een bovengrens (datum van versie 1.0, eerste ijkpunt erboven), dus het cohort ligt eerder een paar weken ouder. De ijkpunten lopen netjes op (controleur).

### Vindbaarheid
- In cTrader zelf (Windows, Mac, web, mobiel) en op ctrader.com, met lijsten als "best free trading bots" en tags. Gratis producten krijgen echte installs; betaald verkoopt via vertrouwen, vaak een gratis versie eerst (Moss_Klugt: "free test versions" en daarna de volle versie). DERDEN.
- Spotware heeft een affiliateprogramma: makers verdienen ook aan brokeractiviteit van hun gebruikers. Met veel gratis gebruikers is dat mogelijk een tweede bron. Niet uitgezocht; dat is het eerste vervolg.

### Past het bij ons
- Indicatoren en cBots zijn C# of Python (cTrader Algo). Een goede indicator of hulpprogramma (trade manager, risicocalculator, trade copier) is in 1 tot 2 weken te bouwen. GOK.
- KYC van Thijs nodig om te verkopen.
- Het gros van de verkopers verkoopt winstbeloftes (goudscalpers, "AI scalping", bots van $200 tot $950). Daar doen wij niet aan mee. Wat overblijft voor ons zijn hulpprogramma's: gratis halen die snel 1.000+ gebruikers (trade copiers, WebPlugins), betaald is het beste in de steekproef 53 gebruikers in 5 maanden.

## Voor- en nadelen
Voor:
- Echte kassa met 70% voor de maker en snelle uitbetaling (Wise).
- Openbare tellers per maker: geld is hier beter te zien dan op bijna elk ander platform.
- Gratis producten krijgen bereik (actief mediaan 143 na 3 tot 9 maanden), gratis hulpprogramma's soms 1.000+ in minder dan 3 maanden.

Nadelen:
- Betaalde nieuwe producten verkopen bijna niets: actief mediaan 0 gebruikers, 4% haalt 10+.
- Van nieuwe makers heeft de helft 0 verkopen; 1 op 127 kwam boven de 100.
- De showcase-verkoper van Spotware zelf haalt ±$650 netto per maand na 2 jaar: het plafond is laag.
- Groei in nieuwe producten stopte in 2026; de markt is een kleine kopie van MetaTrader Market.
- De winkel wordt gedomineerd door winstbeloftes aan particuliere handelaren; past slecht bij hoe Dortus wil werken.

## Eerste idee (alleen als het ooit verandert)
Een gratis hulpprogramma (bijvoorbeeld een trade manager met risico per trade en een dashboard) voor bereik, met een betaalde Pro-versie van ±$29. Verwachting volgens de steekproef: 100 tot 1.000+ gratis gebruikers in een half jaar, en een handvol tot enkele tientallen kopers.

## Advies
**Nee voor nu, cijfer 4.** Geld is aangetoond maar dun en geconcentreerd (6 van 127 nieuwe makers boven 50 verkopen), betaald bereik bijna nul; gratis hulpprogramma's halen wel echt bereik. Vervolg dat het cijfer kan verhogen: uitzoeken wat het affiliateprogramma per gratis gebruiker oplevert (dan kan een gratis trade copier met 1.000+ gebruikers geld geven zonder verkoop). Herhaalmeting rond feb 2027 met dezelfde ID's (`data/ctrader-pagina-script.py` op `ctrader-alle-ids-2026-11-09.txt`, elke 8e), volg makers via totalSales: opnieuw wegen als nieuwe makers (lid na nov 2026) vaker dan 1 op 10 boven de 50 verkopen komen.
