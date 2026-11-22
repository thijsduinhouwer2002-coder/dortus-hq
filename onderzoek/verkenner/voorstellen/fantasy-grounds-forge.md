# Voorstel: Fantasy Grounds Forge (extensies)

**Advies: nee voor nu.** Cijfer 4 (eerst 5, verlaagd na de controle). Onderzocht 7 nov 2026 run 11:31 (tweede platform van de run), eigen meting van alle 3.189 items in de winkel. Controleur akkoord, 6 correcties verwerkt.

Kort: een kleine winkel waar betaalde extensies wel verkopen. Maar de hele markt is klein (44 makers met betaalde extensies ooit), de bedragen per extensie zijn laag, en van de twee snelle stijgers van 2026 is er maar één aantoonbaar nieuw.

## Wat is het
Fantasy Grounds (SmiteWorks) is tafelsoftware voor online rollenspellen, net als Foundry. Sinds nov 2025 is de software gratis (DERDEN, SmiteWorks op ENWorld 9 nov 2025: "Our cut is normally 30-40% range", https://www.enworld.org/goto/post?id=9796479). De Forge (forge.fantasygrounds.com) is de winkel voor makers ("crafters"): extensies (Lua-code), kaarten, tokens, skins. Wie koopt, "abonneert" zich en krijgt updates.

## Cijfers

### Bereik en geld (GEZIEN, eigen meting 7 nov)
- Prijzen staan in "gold": 1 gold is 1 dollarcent; kopers betalen met gold uit hun Treasury (DERDEN, https://fantasygroundsunity.atlassian.net/wiki/spaces/FGCP/pages/1915486209/FG+Forge+-+Manage+Craft en .../pages/1901035521/FG+Forge+-+Shop).
- De winkeltabel is openbaar (met een token uit de pagina) en geeft per item prijs, datum en aantal abonnees. Script: `data/fgforge-haal-script.sh`, analyse `data/fgforge-analyse-script.py`, data `data/fgforge-items-2026-11-07.json`.
- **Gratis extensies van mei tot aug 2026 (n=51):** mediaan 69 abonnees, p90 240, 35% haalt 100+.
- **Betaalde extensies van mei tot aug 2026 (n=98):** mediaan 15,5 kopers, p75 39, p90 73, 73% haalt 10+, 7% 100+. Mediaanprijs $3.
- Dus de mediaan betaalde extensie levert ±$49 bruto in 3 tot 6 maanden op (GOK op GEZIEN, aanname: abonnees = kopers tegen de huidige prijs). Abonnees zijn grotendeels kopers, maar ook cadeaus tellen mee (transacties "Purchase, Gift, Donation", DERDEN, Manage Craft). Bruto is dus een bovengrens.
- **Makers die sinds 2025 begonnen (20 met betaalde extensies)**, bruto = abonnees maal huidige prijs (GOK op GEZIEN):
  - Melborne: ±$9.000 bruto sinds 26 mei 2026, ±$1.660 per maand, 25 betaalde extensies ($4 tot $15, Table Tools en AoE Targeting). **Waarschijnlijk geen nieuwe maker:** het makersnummer (410) ligt tussen makers die in sep en okt 2022 begonnen, dus het account bestaat al sinds ±2022 (GOK op GEZIEN, controleur).
  - Henix: ±$6.300 bruto sinds 24 feb 2026, ±$750 per maand, 19 betaalde extensies (automatisering voor D&D 5e 2024). Makersnummer past bij een nieuw account uit 2025 of 2026.
  - Ineffable_DM: ±$2.200 sinds jan 2026, ±$220 per maand, 4 extensies
  - De andere 17: onder $60 per maand, mediaan ±$50 bruto in totaal.
- **Afdracht:** niet openbaar. De maker ziet zijn percentage bij "Royalty Recipients" en het staat in de Crafter Agreement, alleen na aanmelding te zien; uitbetaling in USD via PayPal (DERDEN, wiki Manage Craft en Manage Item). De 30 tot 40% van SmiteWorks gaat over gelicentieerde inhoud, niet over de Forge. Met 30 tot 40% eraf als GOK: Henix ±$450 tot 520 netto per maand.
- **Hele markt (GEZIEN):** 44 makers hebben ooit een betaalde extensie verkocht. De twee grootsten (Mad Nomad, Grimlore, sinds 2021) halen ±$110.000 en ±$74.000 bruto in totaal.

### Drukte (GEZIEN)
- 3.189 items in totaal. Extensies van mei tot aug 2026: 149 (±37 per maand, waarvan ±25 betaald). Pieken in nov 2025 (304 items) en jun 2026 (283), vooral kaartpakketten.

### Vindbaarheid (GOK)
- De Forge-winkel zelf (sorteren op abonnees), de FG-forums en Discord. Gratis software sinds nov 2025 brengt nieuwe gebruikers (DERDEN, SmiteWorks).

### Past het bij ons
- Extensies zijn Lua en XML binnen Fantasy Grounds. Testen in de echte app moet op GitHub Actions; of FG daar draait (Windows, gratis versie, inloggen) is niet onderzocht.
- AI-regels: voor ontwikkelaars die officiële producten omzetten geldt "Do not include AI-generated content unless it's approved by the products publisher", met melding van de gebruikte tools (DERDEN, https://fantasygroundsunity.atlassian.net/wiki/spaces/FGCP/pages/3693707267). Voor eigen Forge-extensies vond de controleur geen regel. Navragen kan via developer_relations@smiteworks.com of in de Crafter Agreement. In de forums vragen gebruikers om AI-inhoud uit te kunnen zetten (DERDEN, https://www.fantasygrounds.com/forums/archive/index.php/t-86447.html).
- Grote nieuwe makers maken veel kleine betaalde extensies voor één spelsysteem (vooral D&D 5e). Dat past bij hoe wij snel bouwen.

## Voor- en nadelen
Voor:
- Betaalde extensies verkopen echt: mediaan 15 kopers, bijna driekwart 10+.
- Eén aantoonbaar nieuwe maker (Henix) kwam in 9 maanden tot ±$450 tot 520 netto per maand (GOK); Melborne verdient meer maar heeft waarschijnlijk een account sinds 2022.
- Weinig concurrentie: ±25 nieuwe betaalde extensies per maand.
- Open, eerlijke telling per item.

Tegen:
- Kleine markt: 44 makers ooit, mediaanprijs $3, mediaan ±$47 per extensie.
- Afdracht niet openbaar, abonnees tellen ook cadeaus mee.
- Lua en een Windows-programma: lastiger te testen dan Obsidian of Foundry.
- Systeemgebonden extensies (D&D 5e) hangen af van licenties van uitgevers.

## Eerste idee (GOK)
Net als Melborne: een reeks kleine betaalde hulpmiddelen voor de spelleider ($4 tot $8), systeemloos waar het kan, met één gratis extensie voor bereik.

## Wat het oordeel zou veranderen
1. Een tweede aantoonbaar nieuwe maker boven $300 netto per maand (herhaalmeting over 4 weken met `data/fgforge-haal-script.sh`).
2. Afdracht 30% of minder (Crafter Agreement, alleen na aanmelding; dat vraagt een account van Thijs, nu niet gevraagd omdat de kans op een ja klein is).
3. AI-code toegestaan voor eigen extensies.
4. Fantasy Grounds te starten op GitHub Actions voor tests.
Pas als 1 en 2 kloppen, wordt het een 5 of 6.
