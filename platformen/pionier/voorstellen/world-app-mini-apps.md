# Voorstel: World App mini apps (Noor, 8 nov 2026)

**Advies: nee. Cijfer 2.** Het platform krimpt hard: het aantal actieve gebruikers per maand is in elf maanden met ruim 70% gedaald en er komen bijna geen nieuwe geverifieerde mensen meer bij. Een krimpend platform is volgens de rol geen pionierskans, hoe leeg de categorieën ook zijn.

## Wat het is
World (Tools for Humanity, van Sam Altman) heeft een app met een wallet en World ID (bewijs dat je een mens bent, via de Orb). Sinds eind 2024 kunnen makers "mini apps" bouwen: webapps die in de app draaien, met World ID, betalen in WLD of stablecoins (Pay-commando) en meldingen. Er is een Mini App Store met keuring. In april 2025 begon een Developer Rewards-programma ($300K per maand in WLD op basis van echte gebruikers). Sinds 21 sep 2026 is de app gesplitst: mini apps zitten in "World Money", World ID in een aparte "World ID app".

## Bronnen en meting
- Eigen meting: de openbare JSON van World zelf, `https://metrics.worldcoin.org` (de teller op world.org), nu en via het Wayback-archief. Plus de openbare lijst `https://www.miniapps.world/` (World linkt ernaar vanuit de docs), met per mini app de unieke gebruikers van 7 dagen. Script: `data/worldapp-meet.py`, uitkomst `data/worldapp-2026-11-08.json`.
- Onderzoeker (agent) voor oudere standen, geld, regels en risico's. De kerncijfers van dec 2025, jun 2026 en vandaag heb ik zelf nagekeken.

## De vijf vragen

### 1. Groeit het platform hard en zichtbaar? Nee, het krimpt.
| Datum | Orb-geverifieerd | Actief per 30 dagen | Actief per 7 dagen | Goedgekeurde mini apps | Bron |
|---|---|---|---|---|---|
| dec 2024 | 8,30M | 7,28M | 4,90M | 57 | onderzoeker via archief |
| sep 2025 | 15,63M | 9,54M | 5,09M | 361 | onderzoeker via archief |
| 8 dec 2025 | 17,62M | 7,84M | 3,74M | 463 | GEZIEN (archief) |
| 24 jun 2026 | 18,12M | 3,63M | 1,59M | 684 | GEZIEN (archief) |
| 8 nov 2026 | 18,17M | 2,21M | 0,81M | 586 | GEZIEN |

- Actief per maand: 9,5M (sep 2025) naar 2,2M nu. Per dag nog 168.000 (GEZIEN).
- Nieuwe Orb-verificaties: in 2025 0,5 tot 1M per maand, nu bijna nul (18,12M in juni, 18,17M nu; GEZIEN).
- Transacties per dag (gemiddelde 7 dagen): 1,67M in dec 2025, 0,62M in juni, 0,20M nu (GEZIEN).
- WLD-koers $0,33, een jaar geleden ±$0,82 (onderzoeker, CoinGecko-API). De grootste reden om de app te openen (gratis WLD) is dus veel minder waard.
- Voorbehoud: door de splitsing kan de teller sinds september een kleinere app meten (GOK). Maar de daling begon al in dec 2025, ruim voor de splitsing.
- Motor: World richt zich in 2026 op World ID voor bedrijven (Tinder, Zoom, Okta, Vercel; DERDEN, https://world.org/blog) en op World Money (DERDEN, https://thepaypers.com/crypto-web3-and-cbdc/news/world-launches-world-money-super-app-across-150-countries). Geen motor die het gebruik van mini apps omhoog trekt.

### 2. Is de winkel jong? Ja, maar hij loopt leeg.
- Open sinds eind 2024. Goedgekeurde mini apps: 57 (dec 2024), 684 (jun 2026), nu 586 (GEZIEN). Het aantal daalt netto sinds juni.
- In de lijst van miniapps.world staan 631 apps, samen ±945.000 unieke gebruikers per 7 dagen (met dubbeltellingen). Mediaan per app 77 per week; 116 apps halen 1.000+, 13 halen 10.000+ (GEZIEN).
- Grootste: de WLD-uitdeling zelf (225.000 per week, in okt 2025 nog ±4M volgens de onderzoeker), daarna "verdien WLD"-apps, wallets en tikspelletjes (GEZIEN).

### 3. Kan er betaald worden? Technisch ja, maar het makersgeld lijkt weg.
- Betalen in de mini app met WLD of stablecoins kan (Pay-commando). Niet in elke regio ("Payments are not available in the user's region"). Afdracht niet gevonden (onderzoeker, https://docs.world.org/mini-apps/commands/pay.md).
- Regels: geen abonnementen voor rendement, geen token-voorverkoop, kansspellen bijna nooit (onderzoeker, https://docs.world.org/mini-apps/guidelines/app-guidelines.md).
- Developer Rewards: de bedragen op miniapps.world staan sinds aug 2025 stil en de voorwaardenpagina is weg. Waarschijnlijk gestopt (GOK, sterk).
- Voor Dortus: geld komt binnen als crypto op een wallet; Thijs zou een wallet en een ontwikkelaarsaccount moeten maken en de belasting en MiCA laten nakijken. Extra drempel.

### 4. Is er al vraag te zien? Weinig.
- GitHub minikit-js: 28 issues in totaal, de recente zijn fouten die open blijven zonder reactie (onderzoeker, GitHub-zoek-API). Weinig makers, weinig steun.
- Gebruikers komen voor WLD verdienen; gewone hulpapps en spelletjes hebben bijna geen gebruikers (GEZIEN in de lijst). Reddit, Discord en X niet te lezen.

### 5. Is de eerste plek in een categorie te pakken? Ja, maar het levert niets op.
- Buiten "verdien WLD" en wallets zijn de categorieën leeg (spelletjes, hulpmiddelen). Maar een nummer één in een krimpende app met mediaan 77 gebruikers per week groeit niet mee; hij krimpt mee.

## Risico
- Het platform haalt het al niet in zijn huidige vorm: gebruik daalt 10 tot 15% per maand.
- Verboden of stopbevelen in meerdere landen (Spanje, Portugal, Kenia, Indonesië, Colombia, Filipijnen, Thailand, AVG-besluit Beieren; onderzoeker, bv. https://www.biometricupdate.com/202510/philippines-privacy-authority-orders-halt-to-world-biometrics-processing). De mini app is zelf verantwoordelijk voor de regels in elk land (onderzoeker, https://docs.world.org/mini-apps/guidelines/policy.md).
- Crypto-betalingen en naam van Thijs aan een omstreden project.

## Categorie en productidee
Geen. Als het toch ooit wordt: een eenvoudig, mooi spel of hulpmiddel zonder WLD-belofte, als goedkope proef. Niet nu.

## Wat het advies zou veranderen
Twee metingen op rij met stijgend `actief_30d` en weer +100.000 Orb-verificaties per maand, plus een nieuw makersfonds met datum (dan opnieuw wegen). Herhaalmeting: `python3 data/worldapp-meet.py`, niet vaker dan eens per kwartaal (volgende rond 8 feb 2027).

## Nagekeken
Geen aparte controleur: het advies is een nee en de kerncijfers (gebruikers, verificaties, apps, mediaan) heb ik zelf in de bron gezien.
