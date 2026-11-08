# Voorstel: cTrader Store (Spotware)

Noor, pionier. 8 nov 2026, run 21:38 tot ±22:25 UTC. Meting: `data/ctrader-store-meet.py` (alle producten via sitemap en openbare productdata, ±25 minuten), analyse `data/ctrader-store-analyse.py`, ruwe data `data/ctrader-store-2026-11-08.json`. Achtergrond (groei, regels, vraag) door een hulpagent, bronnen hieronder.

**Uitkomst: cijfer 4, nee voor de pionier.** Betalen werkt goed, maar de winkel is niet meer jong, de instroom van makers zakt, en het geld is klein: alle 1.094 verkopers samen hebben in twee jaar 6.192 verkopen. Doorgeven aan Vera als kleine, eerlijke markt waar een handvol makers verdient.

## Wat het is
cTrader is een handelsplatform (forex, CFD's) van Spotware dat brokers en prop firms aan hun klanten geven. Sinds 16 dec 2024 heeft het een eigen winkel, cTrader Store op ctrader.com, voor cBots (robots), indicatoren en plugins in C#. Spotware rekent af, versleutelt het product per koper en houdt 30%. Sinds aug 2026 kunnen ook abonnementen (week, maand, half jaar, jaar) (DERDEN, https://www.financemagnates.com/forex/products/ctrader-adds-subscriptions-as-trading-platforms-court-paid-tool-creators/).

## De vijf vragen

**1. Groeit het platform hard?** Matig. Spotware meldt 8 miljoen "traders" in dec 2024 en 11 miljoen eind 2025, en +105% handelsvolume in 2025 (DERDEN, https://fxnewsgroup.com/forex-news/platforms/ctrader-reports-105-volume-leap-in-2025-as-total-users-top-11-million/). Dat zijn alle cTrader ID's ooit, ook demo's (GOK). Marktaandeel blijft klein: 2% (Europa) tot 7,5% (Azië) van het platformverkeer, MetaTrader 5 heeft meer dan de helft (DERDEN, https://www.financemagnates.com/forex/analysis/north-america-holds-the-line-for-mt4-as-mt5-sweeps-five-of-six-regions/). De motor van 2024 (prop firms die na het besluit van MetaQuotes overstapten) is gestopt: sinds Q1 2026 weert Spotware nieuwe Amerikaanse prop traders, en sommige prop firms gaan terug naar MT5 (DERDEN, https://www.financemagnates.com/forex/ctrader-restricts-us-prop-firm-access-following-internal-regulatory-assessment/).

**2. Is de winkel jong?** Niet meer. Bijna twee jaar open, 4.610 producten ooit (2.693 actief, 1.337 gearchiveerd, 580 inactief), 1.094 verkopers (GEZIEN). Instroom van nieuwe verkopers per maand (lid sinds, GEZIEN): 99 in jan 2025, 57 in jan 2026, en daarna 39, 14, 15, 10 in jul tot okt 2026. De winkel trekt dus steeds minder nieuwe makers, terwijl Spotware "community +40% per jaar" zegt (DERDEN, https://ctrader.com/start-selling).

**3. Kan er betaald worden?** Ja, goed geregeld. 30% afdracht, minimumprijs $39 (cBot) en $19 (indicator, plugin), uitbetaling vanaf $50 naar een Visa- of Mastercard op eigen naam, 14 dagen bedenktijd voor kopers (DERDEN, https://help.ctrader.com/ctrader-store/faq/ en https://ctrader.com/terms-of-use). Let op: verkopen gaat via KYC van een persoon (ID, selfie, adres via Sumsub); een bedrijfsroute staat nergens, dus Thijs zou als persoon verkopen (GOK, sterk). VS uitgesloten. Kosten vooraf: geen.

**4. Is er vraag?** Ja, naar hulpmiddelen die geen strategie zijn. Op het oude forum (5.368 titels in Suggestions, GEZIEN door de hulpagent): trade manager (breakeven, gedeeltelijk sluiten, trailing) 105 titels, risico en lotgrootte 55, nieuws en kalender 54, alerts naar Telegram 32, journaal 26, kopiëren tussen eigen accounts 17, dagelijks verliesmaximum voor prop 13 (https://community.ctrader.com/forum/suggestions/). Spotware schrijft zelf "many traders buy risk calculators" (DERDEN, https://blog.ctrader.com/what-products-traders-really-want-and-ready-to-pay-for/). Maar het forum is sinds 2025 dicht en cTrader 5.2 kreeg zelf een risk-reward-hulpmiddel met volumeberekening.

**5. Is de eerste plek te pakken?** In de hulpmiddelen-hoeken is het al vol (GEZIEN, op titel, beschrijving en tags):

| Hoek | Producten actief | Betaald | Beste (gebruikers) |
|---|---|---|---|
| risico en lotgrootte | 439 | 382 | Lot Sizer Pro (gratis, 2.205) |
| trade manager | 236 | 201 | SLTPTrailing (gratis, 1.047) |
| prop-regels | 738 | 590 | vooral strategie-bots met "prop" erop |
| journaal en dashboard | 135 | 112 | Iridio Dashboard (gratis, 8.145) |
| alerts en Telegram | 157 | 126 | indicatoren met alert |
| sessies | 163 | 109 | Market Sessions Free (5.691) |
| kopiëren tussen accounts | 10 | 7 | twee gratis copiers (±1.500 elk) |
| nieuws en kalender | 36 | 27 | Live Economic Calendar Pro (abonnement $19, 2.578) |

Daarbij buiten de winkel ClickAlgo (lot size panel, equity protector, break-even manager) en copiers als Duplikium (DERDEN, https://clickalgo.com/). Alleen de copier-hoek is dun, maar die raakt aan de regels voor kopieerdiensten (ESMA) als het verder gaat dan je eigen accounts.

## Het geld (doorslaggevend)
- Alle verkopers samen: 6.192 verkopen in twee jaar (GEZIEN, totalSales per verkoper). 347 verkopers hebben ooit iets verkocht, 108 minstens 10 keer, 13 minstens 100 keer. De beste heeft 502 verkopen.
- Betaalde producten: 1.992 actief, mediaan 0 tot 2 gebruikers. 137 hebben 10 of meer gebruikers, 17 hebben 50 of meer, 3 hebben 100 of meer (GEZIEN; gebruikers telt ook proefversies mee, dus verkopen zijn eerder minder).
- Nieuwe verkopers in 2026: 346, mediaan 0 verkopen, 8 met 10 of meer.
- Spotware zelf: Black Friday 2025 ongeveer 100 transacties in 3 dagen, "3 keer normaal" (DERDEN, https://blog.ctrader.com/black-friday-proved-it-ctrader-store-promos-drive-real-sales-real-visibility-and-real-growth/), dus grofweg 10 verkopen per dag voor de hele winkel (GOK). De beste succesverhalen: $10.000+ in totaal (Moss Klugt), $1.500 per maand (Anderson Luiz) (DERDEN, https://blog.ctrader.com/tag/success_story/).
- Rekensom (GOK): mediaanprijs betaald $59, na 30% ±$41. Voor €300 per maand zijn ±8 verkopen per maand nodig, elke maand. Alleen de top 5 van de hele winkel haalt dat tempo.

## Risico
Het platform blijft waarschijnlijk (Spotware bestaat sinds 2010, 300+ brokers en prop firms), maar het is een kleine speler naast MetaTrader en de winkel lijkt al over zijn top: verkopersinstroom van 57 per maand naar 10. Juridisch: losse hulpmiddelen zijn software; strategie-bots met rendementsbeloftes, signalen en kopiëren van andermans trades niet doen (ESMA, Wft) (DERDEN, https://www.esma.europa.eu/sites/default/files/2023-03/ESMA35-42-1428_Supervisory_Briefing_on_Copy_Trading.pdf).

## Als we het toch zouden doen
Categorie: kopiëren tussen je eigen accounts (prop traders met meerdere challenges), als betaalde plugin met abonnement. Dun bezet (10 producten, twee gratis met ±1.500 gebruikers), en het wordt al jaren gevraagd. Maar zelfs als nummer één in een winkel van ±10 verkopen per dag blijft het klein.

## Cijfer en advies
**4, nee voor de pionier.** Betalen werkt (geen 6-plafond), maar vraag 1 en 2 zijn zwak: geen harde groei, winkel bijna twee jaar oud met 2.693 actieve producten en een dalende instroom van makers. Voor Vera kan het een kleine zakelijke markt zijn waar verkopen zichtbaar zijn (zeldzaam: totalSales per verkoper staat open). Wat het zou veranderen: Spotware opent in-app aankopen op mobiel (aangekondigd, DERDEN, https://www.spotware.com/news/ctrader-store-subscriptions/) en de winkelverkoop stijgt zichtbaar (herhaalmeting rond 8 feb 2027: totaal verkopen boven 9.000 en instroom verkopers weer boven 40 per maand, dan opnieuw wegen).
