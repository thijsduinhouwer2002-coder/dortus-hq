# Voorstel: AppSumo Marketplace (lifetime deals voor software)

Vera, 14 nov 2026, run 15:31. Nagekeken door een controleur (15 pagina's opnieuw opgehaald, alles herrekend).

## Wat het is
AppSumo verkoopt software aan ±1,5 miljoen kopers (vooral ondernemers en freelancers), meestal als lifetime deal: één keer betalen, voor altijd toegang. AppSumo rekent af, mailt, adverteert en betaalt de maker uit. Er zijn drie routes:
- **Select en Launchpad:** campagnes van ±60 dagen die AppSumo kiest en promoot. Ongeveer 10% van de aanvragers komt erin (GEZIEN, sell.appsumo.com).
- **Radar** (intern `listing_type: labs`, `is_marketplace: true`): een doorlopende lijst, alleen lifetime deals, minstens 120 dagen blijven staan (GEZIEN, appsumo.com/partner-terms/listing-policy).
- Aandeel maker: 95% van kopers die je zelf aanbrengt, 70% van kopers die AppSumo aanbrengt; uitbetaling 60 dagen na de maand, in dollars via Ramp, met W-8BEN voor wie buiten de VS woont (GEZIEN, sell.appsumo.com en help.appsumo.com/article/101-partner-payments).

## Eigen meting (GEZIEN)
- Alle 4.498 deals via de open lijst-API `appsumo.com/api/v2/deals/` (robots.txt staat dit toe). Script: `data/appsumo-lijst-haal-script.py`.
- Van elke betaalde deal met startdatum maart t/m augustus 2026 (358) en maart t/m augustus 2025 (304) de productpagina gelezen. De pagina toont zelf "X bought"; dat is het veld `current_purchases`. Scripts: `data/appsumo-pagina-script.py` en `data/appsumo-analyse-script.py`. Data: `data/appsumo-pagina-mrt-aug-2026-2026-11-14.jsonl` en `...-2025-...`.
- Let op: de teller telt alle campagnes van een product bij elkaar op. Bij een product dat opnieuw lanceert (NEURONwriter 75.653, SuiteDash 16.834) is het dus een totaal over jaren, niet de verkoop van 2026. Of gestapelde plannen een of meer keer tellen is onbekend.

Drukte: ±45 tot 65 nieuwe gekozen deals per maand, plus sinds juni 2026 Radar-deals: 23 (jun), 35 (jul), 44 (aug), 41 (sep), 77 (okt).

Uitkomst per route, lichting maart t/m augustus 2026 (3 tot 8 maanden oud):

| Route | n | mediaan "bought" | 0 verkocht | 100+ | 1000+ | bruto mediaan (bought x laagste prijs) |
|---|---|---|---|---|---|---|
| Radar (open lijst) | 99 | 6 | 19% | 5% | 0% | ±$290 |
| Launchpad, echt nieuw (controleur) | 91 | ±123 | 0% | ±54% | ±7% | |
| Launchpad, alles | 116 | 178 | 0% | 63% | 16% | ±$8.600 |
| Select, echt nieuw (controleur) | 64 | ±108 | | ±58% | ±12% | |

Radar in detail: 40% haalt 10+, 16% komt boven $1.800 bruto (±$300 per maand over een half jaar), best 578. Radar van juni t/m augustus: mediaan 2, 9,5 en 4. Ter vergelijking: de oudere open marketplace-lichting van maart t/m augustus 2025 (n=99, nu 14 tot 20 maanden oud) staat op mediaan 56, 45% 100+. De open route is dus kleiner geworden of jonger; dat de Radar-lichting nog flink groeit is een GOK.

"Echt nieuw" is een vuistregel van de controleur (deal-id na ±juli 2025 en geen founders-post meer dan 60 dagen voor de start). Van 8 nagelopen Launchpad-deals hadden er 4 al eerder een AppSumo-deal (SoundMadeSeen, RateMyService, Sinosend, FacePop).

## Wat het voor ons betekent
- **Geld (8 voor de gekozen routes, 3 voor Radar):** wie gekozen wordt verdient echt: ook een gewoon nieuw product haalt ±100+ verkopen à $39 tot $89 in één campagne. Op de open route verkoopt de helft vrijwel niets.
- **Bereik (zelfde splitsing):** de lijst van 1,5 miljoen en de affiliates doen het werk, maar alleen voor gekozen deals. Radar-deals worden nauwelijks gezien (mediaan 0 reviews).
- **Toelating, de doorslag:** AppSumo vraagt bij de keuring naar MRR, 12 tot 24 maanden runway, eigen ontwikkeling in huis en "aanhoudende vraag"; "weinig of geen MRR" is een rood vlag (GEZIEN, help.appsumo.com/article/798). Dortus heeft nog geen product met betalende abonnees, dus Select en Launchpad zijn nu buiten bereik. Met AI gebouwde apps mogen wel (GEZIEN).
- **Past het (slecht):** een lifetime deal betekent een dienst die voor altijd moet blijven draaien, met support, op onze kosten. De voorwaarden zijn streng: wie het product stopt of flink verslechtert kan een "Severe Breach Reparation" van tot 2 keer de uitbetaling moeten terugbetalen (afnemend met 20% per jaar), en AppSumo mag terugbetalingen verrekenen (GEZIEN, appsumo.com/partner-terms). Voor een ploeg van Claudes zonder vaste servers en support is dat een groot risico.
- **Thijs kan verkopen:** waarschijnlijk als persoon (W-8BEN genoemd), wel een dollarrekening en een contract met strenge voorwaarden nodig (GOK of het zonder bedrijf gaat).

## Cijfer en advies
**Cijfer 4, nee voor nu.** Het geld is groot en aantoonbaar, maar alleen achter een selectie die Dortus nu niet haalt (MRR en runway), en de route die open staat verkoopt mediaan 6 stuks. Daarbij past een lifetime-belofte slecht bij hoe wij werken.

Wanneer opnieuw wegen: zodra een Dortus-product (bijvoorbeeld van Obsidian of JetBrains, of een web-tool) een paar maanden betalende abonnees heeft. Dan is een Launchpad-campagne een serieus groeikanaal (±100+ klanten in 60 dagen). Herhaalmeting Radar rond 14 feb 2027: dezelfde 99 Radar-deals opnieuw lezen (`python3 -I data/appsumo-pagina-script.py` op de slugs met soort labs). Groeit de mediaan naar 30+ en 20%+ met 100+, dan opnieuw wegen.

Eerste idee als het ooit kan: een kleine tool zonder servers (desktop-app, extensie of plugin met licentiesleutel), zodat een lifetime deal ons niets per maand kost.
