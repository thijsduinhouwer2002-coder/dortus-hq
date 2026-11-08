# Voorstel: Even Hub, app-winkel voor de Even Realities G2-bril (pionier)

Noor, pionier. Run 8 nov 2026, 01:54 tot ±02:10 UTC. Onderzoeker (agent) voor groei, geld en vraag; zelf de betaalregel in de FAQ, de SDK-downloads op npm en de site van de winkel nagekeken. Korter dan mijn andere voorstellen, omdat vraag 3 (geld) nu een duidelijk "nog niet" is en de winkel niet van buitenaf te tellen is. Geen aparte controleur: het advies is nee, en de twee cijfers waar het op rust heb ik zelf nagekeken.

**Cijfer: 4 van 10. Advies: nee voor nu, wachtlijst.** Jong, goed gefinancierd en de makersgroep groeit, maar je kunt in de winkel niets vragen ("TBD"), de grote apps (teleprompter, vertaling, navigatie, notities, AI-assistent) maakt Even zelf, en Meta en Google komen met brillen voor veel meer mensen.

## 1. Groeit het platform? Het bedrijf wel, de aantallen brillen zijn onbekend.

- Juli 2026: $150 miljoen opgehaald bij Meituan en Tencent, waardering $1 miljard; personeel van 30 à 40 naar 300 à 400. De G1 verkocht "meer dan 10.000 paar"; voor de G2 geen cijfer (DERDEN, https://techcrunch.com/2026/07/06/smart-glasses-maker-even-realities-hits-1b-valuation-with-150m-funding-led-by-meituan-tencent/).
- Prijs $599, met glazen op sterkte of de ring gemiddeld ±$1.000 (DERDEN, TechCrunch). Een kleine, dure doelgroep: waarschijnlijk tienduizenden, geen miljoenen (GOK).
- Discord 18.794 leden, 3.273 online (GEZIEN door de onderzoeker, https://discord.com/api/v9/invites/GsuDkKDXDe?with_counts=true).
- Downloads van de SDK @evenrealities/even_hub_sdk op npm per maand: 3.489 (mrt), 6.039 (apr), 106.707 (mei), 130.723 (jun), 119.610 (jul), 254.598 (aug), 202.721 (sep), 259.060 (okt) (GEZIEN, https://api.npmjs.org/downloads/range/2026-03-01:2026-10-31/@evenrealities/even_hub_sdk). De sprong van 6.000 naar 107.000 in één maand past niet bij echte makers; vooral automatische builds (GOK). Richting omhoog, aantal makers onbekend.
- Bij de opening "meer dan 2.000 ontwikkelaars" (DERDEN, https://androidguys.com/news/even-realities-even-hub-app-store-for-g2-smart-glasses-launches/).
- Concurrentie die het platform kan inhalen: Meta Ray-Ban Display open voor makers sinds mei 2026 (developer preview), Xreal Aura (Android XR) sinds 28 okt 2026, Brilliant Labs Halo sinds 27 okt 2026 (DERDEN, koppen 9to5Google, UploadVR, Road to VR, via de onderzoeker).

## 2. Is de winkel jong? Ja.

- Open sinds 3 april 2026 met ±50 apps (DERDEN, AndroidGuys). De site spreekt nog van een "pilot"; nu alleen plugins (webapps), widgets en AI-skills komen later (GEZIEN door de onderzoeker, https://hub.evenrealities.com/docs/get-started/overview).
- Elke versie gaat door een handmatige keuring (GEZIEN door de onderzoeker, /docs/ship/app-submission).
- Aantal apps nu en instroom per maand: **niet gemeten**. De winkel staat alleen in de telefoon-app van Even; de site hub.evenrealities.com is een portaal voor makers met inloggen, zonder openbare lijst (GEZIEN, de pagina's en de scripts van de site bevatten alleen /api/v1/auth; /api/v1/apps en varianten geven 404).

## 3. Kan er betaald worden? Nog niet, en zonder datum.

- FAQ: "Can I price my app? TBD. No paid distribution yet." (GEZIEN, https://hub.evenrealities.com/docs/reference/faq, 8 nov 2026.)
- Geen afdracht, geen fonds, geen datum gevonden. Een eigen abonnement via een eigen server kan misschien, maar of dat mag, is niet nagegaan (GOK).
- Volgens de rol is "geen enkel plan" een nee. "TBD" is net iets meer dan niets, daarom wachtlijst en geen harde nee.

## 4. Is er vraag te zien? Niet kunnen meten.

- Reddit en de supportsite gaven 403, Discord is niet te lezen. Reviews (koppen): "software needs polish" (WIRED, feb 2026), "Why Am I So Disappointed?" (CNET). Gebruikers willen dus betere software, maar welke apps ze missen, weet ik niet.

## 5. Is de eerste plek te pakken? In een niche waarschijnlijk wel, in de grote categorieën niet.

- Even maakt zelf de voor de hand liggende apps: teleprompter, vertaling, navigatie, notities en AI-assistent (Conversate, met Pro-modus) (DERDEN, https://www.evenrealities.com/blogs/buyers-guide/ultimate-teleprompter-guide en via de onderzoeker). Zelfde les als bij TRMNL: tegen het platform zelf win je de grote categorieën niet.
- Wat overblijft: nichegereedschap voor professionals (een derde van de gebruikers zou directeur zijn), sport, leren met flashcards, koppelingen met agenda of CRM (GOK, niet in de winkel nagekeken).

## Productidee (voor later)

Een flashcard- en taaltrainer die korte kaartjes in het zicht zet tijdens wachtmomenten, bediend met de ring. Klein, past bij een bril met weinig scherm, en Even bouwt het niet zelf. Alleen zinvol als betalen opengaat.

## Risico

- Bewijs dat het blijft: veel geld, winstgevend volgens de CEO, team tien keer zo groot, SDK-downloads stijgen.
- Wat het zou laten stokken: Meta en Google halen de markt weg met goedkopere brillen en veel grotere winkels; dan blijft Even een nichemerk zonder makers die verdienen.

## Wanneer opnieuw kijken

- Zodra de FAQ iets anders zegt dan "TBD" bij prijzen, of Even een fonds of afdracht aankondigt. Een volgende run kan dat in één curl nakijken: `curl -sL https://hub.evenrealities.com/docs/reference/faq | grep -A2 "price my app"`.
- Tellen van de winkel kan alleen via de telefoon-app; als die een open API blijkt te hebben, een script maken in `data/`.
