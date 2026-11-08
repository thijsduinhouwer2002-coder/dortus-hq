# Voorstel: Slack Marketplace (Vera, 8 nov 2026, run 18:33)

**Cijfer: 5. Advies: nog niet klaar.** Slack past goed bij de koers van 8 nov: teams betalen een maandabonnement, Slack neemt geen deel van de omzet, en een solo-maker haalt aantoonbaar $4.091 per maand. Maar bereik is niet te meten (geen installs, geen datum, geen makernaam op de pagina's), de toegang is traag (eerst 10 actieve werkruimtes of 20 maandgebruikers, dan tot 10 weken keuring), en van de nieuwkomers sinds 2025 die ik vond haalde er maar één meer dan $200. Voor het tussendoel van 20 december komt Slack te laat.

## Wat ik mat en hoe
- **Eigen meting (GEZIEN):** sitemap van de Marketplace (slack.com/sitemaps/sitemap_marketplace_en-us.xml, robots.txt staat het toe): 2.810 app-pagina's. Alle 343 pagina's met de nieuwste soort app-ID (A0A tot A0Z, GOK: vooral 2025 en 2026) gelezen en het prijslabel geteld. App-pagina's tonen geen installs, geen datum en geen maker.
- **Eigen meting (GEZIEN):** TrustMRR (omzet uit Stripe, robots.txt staat het toe), 67 profielen met Slack-achtige woorden in de naam, 10 echte Slack-apps.
- **Onderzoeker (agent):** regels, betalen, verhalen van makers. De belangrijkste regels heb ik zelf nagelezen op docs.slack.dev.
- **Niet te meten:** installs per app en hoeveel apps er per maand bijkomen (sitemap zonder datums, app-ID's niet strikt op volgorde).

## Cijfers
**Prijslabels van de 343 nieuwste apps (GEZIEN, 294 met label):** Included with service subscription 82 (apps van bestaande SaaS-bedrijven), Paid with free trial 81, Free and paid plans 75, Free 42, Paid 14. Dus ±58% vraagt zelf geld.

**Makers met geverifieerde omzet (GEZIEN, TrustMRR 8 nov):**

| App | Start | Totaal | Laatste 30 dagen |
|---|---|---:|---:|
| Meet for Slack (solo) | jun 2023 | $150.544 | $2.133 (MRR $4.091, 382 abonnementen, ook op TrustMRR) |
| Anonymous bot for Slack | mrt 2020 | $51.083 | $551 |
| SlackNotify (Google Forms naar Slack) | apr 2022 | $14.822 | $194 |
| Roster for Slack | jun 2025 | $5.605 | $272 |
| Slack Catch-up | nov 2024 | $220 | $0 |
| Stay Green on Slack | mei 2026 | $170 | $62 |
| Botferry, Google Form to Slack, Jev for Slack | 2026 | $0 | $0 |

Nieuwkomers sinds 2025: 1 van 5 boven $200 (Roster, ±$330 per maand gemiddeld). Kleine steekproef, en TrustMRR is een zelfgekozen groep.

**Andere bedragen (DERDEN):**
- Karma bot: $420.000 per jaar, maar team tot 20 mensen (starterstory.com/ideas/slack-bot-business/success-stories, mei 2026).
- Slack/Teams-app van 6 jaar te koop: $4.800 tot $6.165 MRR, ruim 100 betalende klanten op ±$29 per maand (flippa.com/12878926).
- Reactie-bot uit okt 2024: honderden actieve organisaties maar $5 MRR (flippa.com/12167755). Veel installs is hier geen geld.

**Regels (GEZIEN, docs.slack.dev):**
- Keuring: voorcheck tot 10 werkdagen, daarna tot 10 weken voor een nieuwe app (slack-marketplace-review-guide).
- Sinds 2 nov 2026: geen keuring als een app op minder dan 10 actieve werkruimtes staat en minder dan 20 maandgebruikers heeft (letterlijk gelezen is één van de twee halen genoeg); afgewezen is 30 dagen wachten (changelog 2026/11/02).
- Sinds 29 mei 2025: commerciële apps buiten de Marketplace mogen berichten nog maar 1 keer per minuut lezen, 15 per keer. Dat geldt alleen voor conversations.history en conversations.replies. Voor apps die berichten lezen is de Marketplace dus bijna verplicht; een app die geen berichten leest kan al via een eigen site en installatielink verkocht worden (changelog 2025/05/29).
- AI: Slack-data niet gebruiken om modellen te trainen, model en bewaartermijn opgeven, een losse MCP-server zonder echte Slack-functie wordt geweigerd (app-guidelines).
- Betalen: Slack rekent niet af en vraagt niets; de maker regelt zelf Stripe (app-guidelines, FAQ).

## De maatstaf
- **Bereik:** niet te meten. Geen installs openbaar. Makers noemen de Marketplace en Google als bron (DERDEN, zwak).
- **Geld:** ja voor wie al jaren draait (Meet for Slack $4.091 MRR solo). Nieuwkomers mager.
- **Wie betaalt, hoeveel, hoe vaak:** teams en bedrijven, $5 tot $29 per maand per werkruimte, maandelijks of jaarlijks. Dat is precies het soort klant dat de koers zoekt.
- **Drukte:** 2.810 apps in totaal, rustig vergeleken met andere winkels. Hoeveel nieuw per maand: onbekend.
- **Vindbaarheid:** Marketplace-zoek en Google. Geen ranglijst met nieuwe apps.
- **Past het bij ons:** bouwen in 1 tot 2 weken kan. Daarna eerst zelf 10 werkruimtes of 20 gebruikers vinden, dan tot ±3 maanden wachten. Een app die geen berichten leest mag in de tussentijd al via een eigen site verkopen, maar zonder Marketplace is bereik krijgen moeilijk. Een server draaien (Slack-apps zijn webdiensten) is nieuw voor Dortus en kost iets per maand.

## Voor en tegen
Voor:
- Terugkerend geld van teams, geen afdracht.
- Solo-makers met een simpel, duidelijk nut (videogesprek starten, rooster, anoniem bericht) verdienen jaren door.
- Minder dan 3.000 apps; drempels houden de massa buiten.

Tegen:
- Bereik niet te meten, dus een gok.
- Lange weg naar de Marketplace, buiten de Marketplace afgeknepen.
- Een eigen server met Slack-data: privacy, beveiliging en kosten.
- Nieuwkomers op TrustMRR halen bijna niets.

## Eerste idee
Een kleine, duidelijke teamtool met abonnement van $5 tot $15 per werkruimte per maand, in een hoek waar Roster en Meet laten zien dat het werkt: bijvoorbeeld een rooster of beurtrol (wie heeft dienst, wie doet de standup) met herinneringen, gekoppeld aan Google Agenda. Geen AI op berichten, dan blijft de keuring eenvoudig.

## Wat er nog gemeten moet worden (daarom nog niet klaar)
- Hoe vaak nieuwe Slack-apps aan betalende klanten komen. Kan door over 4 weken de sitemap opnieuw te halen (nieuwe ID's zijn dan echt nieuw) en die apps op TrustMRR, Product Hunt en hun eigen site te volgen. Script: haal de sitemap en vergelijk met `data/slack-marketplace-urls-2026-11-08.txt`.
- Of een Marketplace-pagina verkeer geeft: alleen te meten met een eigen app, of via verhalen van makers (Indie Hackers was niet leesbaar, Cloudflare).
- Herhaalmeting: 6 december 2026.

## Nagekeken
Controleur (agent, 8 nov): prijslabels en TrustMRR-tabel kloppen, 2 profielen opnieuw opgehaald. Correcties verwerkt: drempel is 10 werkruimtes of 20 maandgebruikers; de rate limit geldt alleen voor apps die berichten lezen. Oordeel controleur: 5 redelijk; het tussendoel van 20 dec haalt Slack niet. Advies daarom: later, na het tussendoel, met de herhaalmeting van 6 dec als eerste stap.

## Cijfer
Beste koers-pasvorm van de laatste runs (abonnement, teams, geen afdracht), maar bereik onbekend en de weg erin is lang. **5, nog niet klaar.**
