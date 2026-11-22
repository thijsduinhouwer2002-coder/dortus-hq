# Voorstel: Railway-templates (Template Kickback)

Vera, 14 nov 2026, run 14:31 (Amsterdam). Tip van Noor (8 nov), nooit eerder gemeten.

## Wat het is
Railway is een cloud waar je met één klik een app met database draait. Iedereen kan een "template" publiceren (bijvoorbeeld n8n, een AI-agent of een Linux-terminal met één klik). Draait een gebruiker die template, dan krijgt de maker een deel van wat die gebruiker aan Railway betaalt voor het gebruik: de kickback.

## Advies: nee voor nu, cijfer 4
Geld is echt maar dun en scheef verdeeld, en sinds juli 2026 loopt de winkel vol (vier keer zoveel nieuwe templates per maand). Bouwen past perfect bij ons, maar bereik voor een gewone nieuwe template is bijna nul. Alleen wie als eerste een nieuw populair open-source project verpakt, scoort.

## Cijfers

### Eigen meting (GEZIEN)
Alle 8.091 templates via de open GraphQL-API (backboard.railway.com/graphql/v2, geen sleutel nodig), 14 nov 2026. Script: `data/railway-templates-haal-script.py`, gegevens: `data/railway-templates-2026-11-14.jsonl`. Per template: aanmaakdatum, `projects` (totaal ooit gedeployed), `recentProjects`, `activeProjects` (nu draaiend), maker. Het veld `totalPayout` bestaat maar geeft voor iedereen 0 (afgeschermd).

**Drukte (nieuwe templates per maand):** 2025: 44 tot 173. Jan t/m jun 2026: 170 tot 290. Daarna een vloed: jul 536, aug 983, sep 1.109, okt 1.260, nov (tot 14e) 746. Railway maakte publiceren in juni en augustus 2026 makkelijker via de CLI en de Railway Agent (DERDEN, changelog 2026-06-19 en 2026-08-14). Vloedmakers: onepush 570 templates sinds juli, A3A 465, SuperSlowSloth 340.

**Bereik per lichting** (projects = deploys ooit, actief = nu draaiend):

| Lichting | aantal | mediaan deploys | 100+ deploys | mediaan actief | 100+ actief |
|---|---|---|---|---|---|
| jan t/m jun 2025 | 384 | 15 | 12,5% | 4 | 6,2% |
| jul t/m dec 2025 | 733 | 11 | 9,0% | 4 | 4,2% |
| jan t/m apr 2026 | 963 | 8 | 7,4% | 3 | 4,8% |
| mei en jun 2026 (5 tot 6 mnd oud) | 521 | 4 | 4,4% | 1 | 3,3% |
| jul en aug 2026 (3 tot 4 mnd oud) | 1.519 | 1 | 1,1% | 0 | 0,5% |
| sep 2026 | 1.109 | 1 | 0,8% | 0 | 0,6% |
| okt 2026 | 1.260 | 0 | 0,2% | 0 | 0,2% |

**Wie heeft het gebruik:** van 894.776 actieve projecten draait 60,5% op templates van Railway zelf ("Railway Templates") en 9,6% op die van "Jack". Templates van de community uit juli tot nu hebben samen 1,6% van alle actieve projecten, maar wel 14% van de recente deploys (`recentProjects`).

**Makers:** 1.661 makers. 191 hebben samen 100+ actieve projecten, 44 hebben er 1.000+. Van de 878 makers die in 2026 begonnen hebben er 34 100+ en 7 1.000+. Van de 407 makers die na 1 juli 2026 begonnen hebben er 7 100+ (1,7%) en 1 1.000+.

**Wat scoort in 2026:** verpakkingen van nieuwe, populaire open-source projecten, snel na hun opkomst: Evolution API (WhatsApp, 5.466 actief), Ubuntu SSH + Claude (4.340), 9Router (AI-router, 4.313), Telegram MTProxy, OpenClaw (meerdere makers, tot 2.676), Hermes Agent (meerdere makers, tot 2.645), Linux-terminals in de browser. Vaak hebben drie of vier makers dezelfde app; de eerste wint.

### Geld (DERDEN, met bron, nagezocht door een hulpagent)
- Kickback nu **15% van het gebruik, 25% als je vragen in de Template Queue beantwoordt** (docs.railway.com/templates/kickbacks). Was 25% (2023), tijdelijk 50% (maart tot november 2025), sinds 28 nov 2025 weer 25% in de 15+10-vorm (railway.com/changelog/2025-11-28-buckets-ga). Alleen over het gebruik, niet over het abonnement.
- Uitbetaling: standaard als Railway-tegoed, of in geld via Stripe Connect vanaf $100 per keer, 130+ landen.
- Totaal: bijna $1M uitbetaald tot 5 dec 2025, waarvan ±$730k in geld. **2 makers boven $100k, 6 boven $10k, 30 boven $1k** (blog.railway.com/p/1M-paid-to-developers-who-built-railway-templates). Dat was grotendeels in de periode met 50%. Geen nieuwer cijfer gevonden.
- Kosten per project: RAM $10 per GB per maand, CPU $20 per vCPU; kleine diensten $2 tot $3 per maand, n8n $15 tot $25 (DERDEN). Eén maker met ±900 draaiende LibreChat-instanties verwachtte ±$450 per maand en kreeg minder (station.railway.com, 2024).
- **Schatting (GOK):** ±$0,30 tot $1,50 kickback per actief project per maand. Een template met 100 actieve projecten levert dus ±$30 tot $150 per maand op, een treffer met 1.000 actief ±$300 tot $1.500.

## Voor en tegen
**Voor**
- Past perfect: Docker, Linux, open source, alles met code; publiceren kan met de CLI.
- Meten kan heel goed (open API met actieve projecten per template).
- Geld bestaat echt en wordt in geld uitbetaald. Er is een duidelijke route naar een treffer: als eerste een nieuw populair open-source project goed verpakken.

**Tegen**
- Bereik voor een gewone nieuwe template: mediaan 1 deploy na 3 tot 4 maanden, 0,5% haalt 100 actieve projecten.
- Vloed sinds juli, aangejaagd door makkelijk publiceren met agents. Wij zouden precies hetzelfde doen als de vloedmakers.
- Kickback is gehalveerd ten opzichte van 2025 (50% naar 15 tot 25%).
- Railway zelf heeft 60% van het gebruik, en sinds sep 2025 staan "verified" templates van de makers van de technologie zelf bovenaan bij zoeken.
- Per project kleine bedragen; voor €500 per maand heb je ruwweg 500 tot 1.500 actieve projecten nodig. Dat haalden van de 407 nieuwe makers sinds juli er hooguit 1 tot 7.
- Account en Stripe Connect via Thijs; de template moet bijgehouden worden en vragen beantwoord (anders 15%; zonder vragen krijg je de volle 25%; het voorbeeld in de docs noemt 25% bij open source met support, of het voor andere templates anders is, is nog niet uitgezocht).

## Wat we er zouden bouwen (als het ooit ja wordt)
Een "eerste-erbij"-straat: elk uur GitHub Trending en Hacker News lezen, en binnen een dag een nette, goed gedocumenteerde template met database en veilige standaarden publiceren voor elk nieuw self-host-project dat snel stijgt. De les uit OpenClaw en Hermes: drie makers maakten dezelfde template, de eerste met een goede beschrijving won.

## Nog te meten (herhaalmeting rond 14 dec 2026)
`python3 -I data/railway-templates-haal-script.py uit.jsonl` opnieuw. Kijk naar (1) de lichtingen jul t/m okt 2026 een maand later: groeit het percentage met 100+ actief? (2) wordt de vloed kleiner of groter? (3) hoe snel haalt de eerste template van een nieuw trending project zijn eerste 100 actieve projecten (volg 5 projecten die nu op GitHub Trending staan). Haalt de eerste maker bij trending projecten meestal 300+ actief binnen een maand: opnieuw wegen, cijfer kan naar 5.

## Nagekeken
Controleur (agent) rekende alle cijfers na met een eigen script en 3 templates live via de API: alles klopt, behalve 2025 (was 90 tot 175, moet 44 tot 173, verbeterd). Makers zijn geteld op naam. Conclusie volgt volgens de controleur logisch.

## Cijfer
Geld 4 (echt, in geld, maar dun en scheef), bereik 3 (vloed, mediaan 1), past bij ons 8. **Totaal 4, nee voor nu.**
