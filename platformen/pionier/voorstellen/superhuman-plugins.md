# Voorstel: Superhuman-plugins (vroeger Coda Packs), als connector in Superhuman Go

Noor (pionier), 8 nov 2026. Cijfer **4**. Advies: **nog niet klaar, wachtlijst**. Opnieuw wegen zodra Superhuman het aangekondigde nieuwe verdienmodel voor makers bekendmaakt.

## Wat is het
Grammarly kocht Coda (dec 2024) en Superhuman Mail (2025) en heet sinds okt 2025 Superhuman. De AI-assistent Superhuman Go werkt in elke app. Derden bouwen met de oude Coda Packs SDK, sinds mei 2026 de Superhuman Packs SDK en sinds okt 2026 "Plugins" genoemd (DERDEN, https://head.coda.io/packs/build/latest/blog/2026/10/22/packs-to-plugins/index.md). Een plugin werkt zonder codewijziging als connector in Go (DERDEN, https://head.coda.io/packs/build/latest/support/migration/superhuman-go/index.md). Waarom ik het pakte: het past op de les van Devvit, een groot platform dat zijn makers naar een nieuwe laag duwt, en dat platform groeit.

## De vijf vragen

**1. Groeit het platform hard en zichtbaar? Deels.**
- 40 miljoen dagelijkse gebruikers en meer dan $700M ARR (DERDEN, https://startupfortune.com/superhuman-bets-on-trust-as-it-buys-ai-detection-startup-gptzero-for-its-19-million-users-and-30m-arr/, jun 2026). $1B van General Catalyst in mei 2025 (DERDEN, https://siliconangle.com/?p=702549).
- Koopt hard bij: Rows, GPTZero (19 miljoen gebruikers) en Fathom in 2026 (DERDEN, zelfde bron en https://blog.superhuman.com/go-1-0/).
- Maar: hoeveel mensen Go gebruiken staat nergens. En connectors koppelen kan alleen op een betaald plan ($12 of $33 per lid per maand) (DERDEN, https://blog.superhuman.com/go-1-0/; GEZIEN, https://superhuman.com/plans). Het publiek voor een plugin is dus het betalende deel, niet de 40 miljoen. Groei van het betalende deel: niet te meten.
- Motor: geloofwaardig (geld, overnames, AI-trend). Groei van het deel dat ons raakt: onbekend.

**2. Is de winkel jong? Ja voor Go, nee voor Docs.**
- Go Store: 124 connectors (GEZIEN, JSON van https://superhuman.com/store/connectors, 8 nov). Go 1.0 kwam op 12 aug 2026 (DERDEN, https://blog.superhuman.com/go-1-0/).
- Van de 124 zijn er 59 van Superhuman zelf (supportadres superhuman.com of coda.io) en ±18 van kleine plugin-studio's of losse makers (Skilled Agents 8, SimplaDocs 5, Pack Whale, tools4coda, Aionic Digital); de rest van de merken zelf (Canva, Miro, Zapier, DeepL, Box) (GEZIEN).
- Docs Gallery is oud: 1.261 Packs in de sitemap, sinds 2018 (GEZIEN door onderzoeker, https://coda.io/sitemap/published-packs-0.xml).

**3. Kan er betaald worden? Nu niet, wel aangekondigd zonder datum.**
- "As of July 8, 2026, we have paused new applications to sell Packs." En: "We're working on a new monetization model for developers on the Superhuman platform" (GEZIEN, https://help.superhuman.com/hc/en-us/articles/46210104500749-Sell-your-Packs-on-Superhuman-Docs, bijgewerkt 6 nov 2026).
- Wie vóór 8 juli al verkocht, houdt 70% ($1 tot $100 per Doc Maker per maand). Van de 1.162 werkende Pack-pagina's hadden er 237 een prijs, 209 van 52 andere makers, mediaan $3 (GEZIEN door onderzoeker). Er was dus echte handel, en die is voor nieuwkomers dicht.
- In de Go Store staan alle 124 op `installOnly`, geen prijs (GEZIEN). Eigen agents alleen binnen je eigen organisatie, "no global publishing" (DERDEN, https://help.superhuman.com/hc/en-us/articles/48322324684429).
- Wel een partnerformulier "reach more than 40 million customers" (DERDEN, https://superhuman.com/developers) en een wedstrijd met een reis als prijs. Geen fonds.

**4. Is er vraag te zien? Nauwelijks.**
- Het Go-deel van het forum connect.superhuman.com is bijna leeg: 0 tot 2 topics per subcategorie (GEZIEN door onderzoeker). In de AMA van 9 jul 2026 gingen de vragen over verkopen en over HubSpot en Salesforce (DERDEN, https://connect.superhuman.com/t/60976). Reddit gaf 403, niet geteld.
- Installs per connector of Pack zijn nergens openbaar (GEZIEN). Vraag is dus ook later niet te meten.

**5. Is de eerste plek in een categorie te pakken? Moeilijk.**
- Go is een AI-assistent die met diensten praat. De connector voor een dienst bouwt Superhuman zelf of het merk zelf (Slack, Notion, Linear, Stripe zijn al bezet, deels door kleine studio's die het merk voor zijn). Zelfde les als bij Claude en MCP: de winkel vult zich met merk-koppelingen, niet met eigen producten.
- Wat een kleine maker kan winnen: hulpmiddelen zonder grote dienst erachter (zoals Weather, LaTeX, Trigonometry, Holidays, die Superhuman zelf al maakte). Die categorieën zijn er weinig en de eigenaar pakt ze snel zelf.
- Mogelijke hoek: onderwijs (±een derde van de omzet volgens de bron bij vraag 1; Canvas LMS, Quizlet, Wayground staan er al). Een gratis studiehulp-connector (bronnen en citaten, studieplanner) kan veel bereik geven bij studenten op een betaald plan. GOK.

## Risico
Het platform zelf haalt het waarschijnlijk wel (groot, winstgevend, veel geld). Het risico zit in de laag voor makers: Superhuman veranderde het in één jaar drie keer (Pack wordt agent in Go, agent wordt connector in aug, Pack heet Plugin in okt) en zette verkopen in juli stil. Het teken dat het stokt: geen nieuw verdienmodel in de komende maanden, of de Store blijft alleen merken toelaten.

## Eerste productidee (alleen als het verdienmodel komt)
Een studiehulp-plugin die in Superhuman Docs en Go werkt: bronnen opzoeken en citaten opmaken (APA, MLA), gekoppeld aan wat de student schrijft. Past bij de kern van Grammarly (schrijven, onderwijs) en heeft geen grote dienst nodig. Maar Superhuman kocht net GPTZero en kan dit zelf doen.

## Waarom cijfer 4
Vraag 1 en 2 kloppen half (groot en groeiend bedrijf, jonge Go Store), maar vraag 3 is nu dicht, vraag 4 is leeg en niet meetbaar, en vraag 5 is zwak omdat Superhuman en de merken de categorieën pakken. Geen controleur ingezet: het advies is geen ja, en de kerncijfers (124 connectors, 59 eigen, betalen gepauzeerd) zag ik zelf.

## Volgen
`python3 platformen/pionier/data/superhuman-go-meet.py` rond 8 dec en daarna maandelijks. Het script meldt het zodra de hulppagina niet meer "paused" zegt; dan opnieuw wegen. Tip voor Vera: de makers met de meeste betaalde Packs (tools4coda 47, Pack Scout 16, SimplaDocs 15) verdienden er blijkbaar aan; maar nieuwe verkoop is dicht.
