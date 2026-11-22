# Voorstel: Ring Appstore (Amazon Ring)

Noor, pionier, 17 nov 2026. Cijfer **6 (krap 7)**. Advies: **ja met kleine inzet, na één vraag aan Ring** (mag een ontwikkelaar uit Nederland certificeren zonder apparaat in de VS?).

**Controle 17 nov ±08:50 UTC (controleur-agent, alles met curl nagelezen): cijfer van 6 (krap 7) naar 5.** Correcties:
- Pakketwacht is niet leeg: de launch-app **Package Protect** ("package delivery tracking", DERDEN, https://techcrunch.com/2026/03/31/ring-app-store-bets-on-ai-to-go-beyond-home-security/) staat er sinds dag één, Home Analytics noemt "package delivery notices" (Ring-blog), en webhooks hebben sinds 5 okt een subtype `package_delivery` (release notes, GEZIEN door controleur). Het productidee moet anders of weg.
- 100 mln camera's is een cijfer van TechCrunch, niet van Ring (Ring zelf: "millions of Ring customers", https://blog.ring.com/?p=7763).
- Aantal apps bij de start: rond 15 (TechCrunch), niet "tientallen".
- De studentengolf is een uiterste datum (live "by March 1, 2027", indienen liefst vóór 15 feb), geen gezamenlijke lancering, en 1.000 finalisten zijn niet 1.000 apps; alleen Amerikaanse studenten (https://ring.com/appchallenge).
- Vergeten: Private Apps werken voor Ring-accounts uit elk land, zonder keuring, voor 5 of 10 accounts (de docs spreken elkaar tegen). Bouwen en testen vanuit Nederland kan dus wel; verkopen alleen in de VS, en de winkel is buiten de VS niet eens te zien (developer-faq Q21).
- Winkel live 31 mrt 2026 en 10% afdracht en Playground 28 mei: kloppen.


Ring (van Amazon) heeft 100 mln+ camera's en deurbellen in gebruik en opende in 2026 een winkel voor apps van derden die met die camera's werken (beelden, bewegingen, pakketten, deurbel). Klanten zien de winkel in de Ring-app onder Apps. Het past bij wat Thijs zoekt: een groot bestaand publiek dat net een winkel met een betaalknop krijgt, en de winkel is nog lang niet vol.

## De vijf vragen

**1. Groeit het platform hard? Groot publiek, sterke motor.**
- "more than 100 million cameras in the field" (DERDEN, https://techcrunch.com/2026/03/31/ring-app-store-bets-on-ai-to-go-beyond-home-security/, GEZIEN gelezen).
- Amazon duwt de winkel hard: Ring Appstore Challenge met $500.000 prijzengeld, inschrijven 22 okt tot 20 nov 2026, tot 1.000 finalisten die op 1 mrt 2027 tegelijk live gaan (GEZIEN, https://ring.com/appchallenge en ring.com/support/articles/4t7h8 via hulpagent). Grootste prijs ($250.000) gaat naar de hoogste maandomzet: Ring wil dat apps geld verdienen.
- Ontwikkelaarsportaal wordt elke paar weken bijgewerkt: Playground (28 mei), Private Apps (21 jul), voorbeeldapp Watchtower (11 nov) (GEZIEN, https://developer.amazon.com/docs/ring/release-notes.html).

**2. Is de winkel jong? Ja, en voor klanten nog niet helemaal open.**
- Aangekondigd op CES jan 2026, live met partners op 31 mrt 2026 (DERDEN, TechCrunch). API "generally available" volgens de release notes op 21 april (er staat 2025, vrijwel zeker een tikfout want de winkel bestond toen nog niet; GEZIEN).
- ring.com/appstore toont nog "Coming Soon ... Ring Appstore is currently available for limited users" (GEZIEN, 17 nov). Dus ouder dan 3 maanden, maar het brede publiek ziet hem nog niet allemaal.
- Aantal apps: niet te tellen, de catalogus laadt pas na inloggen (GOK: tientallen). Categorieën op de pagina: Business intelligence and operations, Home analytics, Elderly care monitoring, Pet wellness assessment (GEZIEN). Prijslabels in de code: Free, Free Trial, Contact developer for pricing (GEZIEN door hulpagent).
- **Het venster:** nu tot 1 mrt 2027. Dan komen er in één keer tot 1.000 studentenapps bij (GEZIEN, challenge-regels). Wie vóór maart staat met beoordelingen en installs, staat bovenaan.

**3. Kan er betaald worden? Ja, nu al, en goedkoop.**
- Abonnementen per maand of jaar via Ring, Ring houdt 10% (GEZIEN, https://developer.amazon.com/docs/ring/get-started.html FAQ en https://developer.amazon.com/docs/ring/program-requirements.html art. 5.2 "a fee of 10% of the Ring Product Price"). Publiceren is gratis.
- Alleen klanten in de VS: "you may not distribute, sell, license, or market Ring In-App Products outside the following territories: United States" (GEZIEN, program-requirements art. 6).

**4. Is er vraag?** Wat Ring-klanten vragen en Ring niet doet (GEZIEN door hulpagent, Ring Community):
- pakketmeldingen ook op camera's, niet alleen op deurbellen (https://community.ring.com/t/enable-package-alerts-for-ring-cameras/170515);
- aparte meldingsgeluiden per soort (beweging, persoon, pakket) (https://community.ring.com/t/separate-app-alert-tones-for-motion-person-package/157894);
- dieren herkennen, slimmere AI-herkenning, eigen modi en schema's (DERDEN, titels op het Feature Request Board).
- r/Ring kon niet gelezen worden (403).

**5. Is de eerste plek te pakken? Ja, in de thuis-hoek.** De launchpartners zijn bedrijven met een eigen dienst (Density voor ouderenzorg, QueueFlow voor wachtrijen, Minut voor verhuur). Een app voor gewone thuisgebruikers die één klacht oplost (pakketten op elke camera) heeft nog geen bekende nummer één (GOK, catalogus niet te zien).

## Kunnen wij binnen een week een eerste versie hebben?
- **Bouwen: ja.** Ring API's en een MCP-server, webhooks, live beeld via WebRTC. Playground: sandbox met nagebootste apparaten, nep-gebeurtenissen (Package, Vehicle, Motion), zonder app en zonder Ring-abonnement (GEZIEN, release notes 28 mei). Open-source voorbeeldapp Watchtower die 98% scoort op de keuringslijst (GEZIEN, release notes 11 nov).
- **Certificeren: hier zit de drempel.** Testen voor de keuring moet met echte Ring-apparaten, en "Currently we only support devices located in the US", met een Ring Protection-abonnement (GEZIEN, https://developer.amazon.com/docs/ring/develop.html). Daarnaast identiteitsverificatie van de accounteigenaar en een vragenlijst over bedrijf en gegevens (GEZIEN, get-started en certify).
- Ons product is een clouddienst (webhooks ontvangen, beelden bekijken): dat vraagt hosting met een vaste plek (kosten, GOK $5 tot $20 per maand bij weinig gebruikers).

## Categorie en eerste idee
**Pakketwacht voor elke Ring-camera:** melding als er een pakket wordt bezorgd en als het wordt weggepakt (door jou of door iemand anders), ook op camera's zonder pakketmelding, plus een avondoverzicht "2 pakketten bezorgd, 1 nog buiten". Gratis proef, daarna ±$2,99 per maand (GOK). Waarom wij: Ring doet het alleen op deurbellen, en de winkel heeft nog geen thuis-app die dit doet (niet te controleren zonder inlog). Concurrentiecheck volgens de regel van 16 nov nog doen, ook op de studentenideeën die in maart live gaan. Risico: Ring bouwt pakketmelding op camera's zelf.

## Risico en waaraan je ziet dat het stokt
- Ring kan zelf de populaire functies bouwen (pakketten, dieren).
- Privacy-ophef rond Ring; de winkel verbiedt gezichtsherkenning en kentekens (DERDEN, TechCrunch).
- Teken dat het stokt: ring.com/appstore staat in februari nog op "limited users", of de challenge gaat niet door. Teken dat het opengaat: winkel voor alle abonnees open, en 1 mrt 2027 de studentengolf.

## Cijfer en advies
**6, krap 7.** Groot publiek, betalen werkt nu met maar 10% afdracht, winkel jong en voor klanten nog niet eens helemaal open, eerste versie in een week te bouwen met de sandbox. Geen 7 omdat de keuring een Ring-apparaat in de VS vraagt en alleen Amerikaanse klanten mogen kopen; voor een ploeg in Nederland kan dat een harde muur zijn.

**Wat het een 7 maakt:** Ring bevestigt dat een ontwikkelaar buiten de VS mag certificeren (bijvoorbeeld via hun reviewers of een testaccount van Ring), of er is een eerlijke manier om een apparaat in de VS te laten testen. Dat is één vraag aan de ontwikkelaarssupport van Ring; die kan pas na aanmelden (login van Thijs). Niets doen dat de regel "devices located in the US" omzeilt.

**Kosten als de hoofdchat ja zegt:** aanmelden gratis, één Ring-camera (GOK ±$60 tot $100) en Ring Protection (GOK ±$5 per maand) voor de keuring, hosting (GOK $5 tot $20 per maand). Bedragen nakijken voor het besluit.

## Hoe gemeten
Zelf gelezen met curl: portaal developer.amazon.com/ring, docs get-started, develop, publish, certify, release-notes, program-requirements, ring.com/appstore en ring.com/appchallenge. Hulpagent: datums, challenge-regels, Ring Community, Playground; de kern daarvan zelf nagelezen (GA-datum, Private Apps, Playground, Watchtower, art. 5.2 en 6, prijzengeld). Geen aparte controleur meer deze run (tijd); de volgende run laat een controleur dit voorstel nalezen vóór het in de top 3 komt.
Niet gemeten: aantal apps en prijzen (catalogus achter inlog), hoeveel klanten de winkel nu zien, of NL-ontwikkelaars mogen certificeren.
