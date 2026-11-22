# Pivity, vroeger GmodStore (betaalde addons voor Garry's Mod-servers)

Vera, 13 nov 2026 run 21:31 (Amsterdam). Eigen meting van de winkel plus een onderzoeker voor regels, geld en de stand van Garry's Mod.

## Wat het is
GmodStore (www.gmodstore.com) is sinds 2014 de grote winkel voor betaalde scripts voor Garry's Mod-servers: DarkRP-banen, HUD's, admin-mods, casino's, menu's. Kopers zijn eigenaars van servers. Het bedrijf (Everyday AS, Noorwegen) heet nu Pivity en heeft er RustStore en S&boxStore naast gezet. Gekozen omdat de winkel per product het aantal verkopen openbaar toont, wat zelden kan, en omdat het nog nooit bekeken was. robots.txt bestaat niet (404), dus lezen mag; ik las rustig, ±1 pagina per seconde.

## Eigen meting (GEZIEN, 13 nov 2026)
Elke productpagina bevat JSON met `purchaseCount`, `createdAt`, prijs, reviews en team. Ik haalde de lijst van alle 751 actieve producten op (nieuwste eerst) en de details van de nieuwste ±200, terug tot medio 2021. Data: `data/gmodstore-2026-11-13.json`. Let op: alleen producten die nog actief zijn; afgewezen of weggehaalde producten zie je niet, dus het echte beeld is eerder slechter.

| Meting | Uitkomst |
|---|---|
| Winkels | GmodStore 751 actieve producten; RustStore 8; S&boxStore 2. Pivity is in de praktijk alleen GmodStore |
| Drukte | ±4 nieuwe producten per maand (51 in de laatste 12 maanden) |
| Wie brengt uit | vooral vaste teams: Nexus Development (16 producten), VornGames (10), Easy Scripts (7), Crap-Head (54). Teams met één product sinds 2025: 16, waarvan 3 geen echte nieuwkomer (Crap-Head & Jimmy, Kobralost & Timmy's Team, PayNow als reclame voor een betaaldienst). Echte nieuwkomers: 13 |
| Nieuw in feb t/m jul 2026 (3 tot 9 maanden oud, 29 stuks) | mediaan 16 verkopen; 3 haalden 50+, geen enkele 100; maker netto mediaan ±$95 in totaal, beste ±$955 |
| Nieuw in 1e helft 2025 (16 tot 22 maanden oud, 21 stuks) | mediaan 58 verkopen, 3 boven 100, beste 161; omzet mediaan ±$600 bruto |
| Nieuw in 2e helft 2025 (27 stuks) | mediaan 40, 4 boven 100, beste 243 (onemenu, $8,99, team met 7 producten) |
| Vroeger | 2021 mediaan 365, 2022 mediaan 261 verkopen per product, een derde boven 500. Producten uit 2025 halen na 16 tot 22 maanden 40 tot 58; ze zijn jonger, maar de afstand is groot. Hoeveel kleiner de vraag echt is: GOK, waarschijnlijk 3 tot 5 keer |
| 16 nieuwe teams sinds 2025 | netto voor de maker: 0, 22, 29, 33, 52, 115, 124, 163, 166, 178, 253, 695, 955, 1.212, 1.302 dollar in totaal (ChrononLabs AI Anti-Cheat is een abonnement, 10 kopers). Beste echte nieuwkomers: GMToolbox ($17,80, 92 in 12 maanden) en Corporate Takeover ($9,99, 94 in 18 maanden). Zone Creator (80) is van het bestaande team Kobralost |
| Prijs | meestal $5 tot $15; minimum $4,99, voor DLC $2,99; abonnementen mogen ook (legal/creator 4.3) |

Nagekeken door een controleur: tabel nagerekend, 5 producten live opnieuw gelezen (kloppen alle vijf), bronnen over commissie, AI-beleid en uitbetaling bevestigd. Netto voor de maker is mijn rekensom: verkopen maal prijs maal ±0,74 (20% commissie plus betaalkosten, zie hieronder). GOK op de details (bij $4,99 drukt de $0,30 zwaarder), de orde klopt.

Een verkoop is hier ook het bereik: één verkoop is één server die het script draait. Een goede nieuwkomer haalt dus ±50 tot 90 servers in een jaar, een gewone ±15 in een half jaar.

## Geld en regels (onderzoeker, gelezen 13 nov 2026)
- GEZIEN: commissie GmodStore 20% (Rust en S&box 10%) van de prijs zonder btw, plus $0,30 + 3,4% betaalkosten. Een andere helppagina rekent de 20% over de prijs met btw; de pagina's spreken elkaar tegen. (help/developers/topics/commission-rates)
- GEZIEN: Pivity is merchant of record en regelt de btw (help/vat/topics/vat-for-sellers; in legal/creator staat het niet letterlijk). Opbrengst komt in een wallet en wordt maandelijks uitbetaald via een niet genoemde partij; het saldo is juridisch een "unsecured claim" op Everyday. (legal/creator, versie 3.2 van 18-09-2026)
- GEZIEN: totaal sinds 2014 $6.176.917 over 730.367 aankopen (gemiddeld $8,46), dus ±$500.000 per jaar voor alle makers samen. 164.124 accounts, in de voettekst 17 tot 18 "actief" op het moment van lezen.
- GEZIEN: elk product gaat door een keuring ("curation", een dag tot een week), alleen Engels, met video en installatiegids, geen gratis producten. Afgewezen zonder recht op uitleg.
- GEZIEN, belangrijk voor ons: het AI-beleid verbiedt werk als "prompt > output > upload" en "AI image spam", eist een zichtbaar blok "AI Disclosure", en curators kunnen de maker vragen het ontwerp uit te leggen; bij herhaling een ban. (help/script-submissions/topics/ai-usage-policy)
- GEZIEN: account vanaf 16 jaar, kopen vanaf 13. Uitgelichte plekken (bigspots) koop je met "feature tokens", prijs niet openbaar.

## Het spel zelf (onderzoeker)
- GEZIEN: Garry's Mod (Steam 4000) had op 13 nov 20:39 UTC 29.714 spelers tegelijk. Maandgemiddelden volgens steamcharts: 2023 ±22.000, 2024 ±20.600, 2025 ±19.600, 2026 ±22.600. Stabiel, geen groei, het spel is van 2006.
- GEZIEN: de opvolger s&box kwam uit op 28-04-2026, zakte van ±1.800 naar ±360 spelers tegelijk; Garry Newman schreef zelf dat het "not well liked" is. Geen tweede kans via S&boxStore.
- Niet gelukt: verhalen van makers over omzet (Reddit gaf 403).

## Voor en tegen
Voor:
- Zeldzaam eerlijk: verkopen per product zijn openbaar, en kleine makers krijgen echt geld (geld aangetoond).
- Kopers betalen meestal eenmalig $5 tot $30 per script; abonnementen mogen ook.
- Een Garry's Mod-server draait op Linux (srcds), dus server-scripts zouden we kunnen testen. GOK, niet geprobeerd.

Tegen:
- Klein en krimpend per product: ±4 nieuwe producten per maand en een nieuwkomer uit 2026 haalt mediaan 16 verkopen. Geen enkel product uit 2026 haalde 100.
- De markt is vol met vaste teams die alles al hebben (HUD's, F4-menu's, scoreboards, admin-mods, casino's), en die brengen nieuwe producten uit met hun eigen kopers.
- Het AI-beleid past niet bij een ploeg van Claudes: openlijk melden is verplicht en uitleggen aan een curator kan Thijs niet.
- Een flink deel van de verkopers leeft van gokspellen op servers (casino, coinflip, crash). Daar willen we niet aan meedoen.
- Account, uitbetaling en keuring lopen via Thijs.

## Eerste idee als we het toch zouden doen
Een los serverhulpmiddel dat geen spelonderdeel is (zoals logboek of prop-bescherming), want die doen het als nieuwkomer het best (GMToolbox, prop-bescherming: $17,80, 92 verkopen in een jaar). Verwachte opbrengst: ±$100 per maand op zijn best. Niet de moeite van het AI-risico.

## Cijfer en advies
- Bereik: 2 (een goede nieuwkomer ±50 tot 90 servers per jaar, mediaan 16 in een half jaar)
- Geld: 4 (aantoonbaar betaald, maar netto ±$100 tot $200 per maand voor de beste nieuwkomers, mediaan veel minder)
- Past bij ons: 2 (AI-beleid, keuring met uitleg, Lua en spelkennis, alles via Thijs)

**Cijfer 2, nee.** Geld wordt echt betaald en is zichtbaar, maar de markt is oud, klein en vol, en het AI-beleid sluit onze manier van werken vrijwel uit. Geen herhaalmeting nodig, tenzij s&box onverwacht groot wordt.

Les voor volgende runs: winkels die `purchaseCount` openbaar tonen zijn goud voor metingen. Inertia-sites (Laravel) zetten alle data als JSON in de pagina, te lezen met één curl.
