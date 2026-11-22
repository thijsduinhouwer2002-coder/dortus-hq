# Voorstel: MentraOS, Mentra Miniapp Store (Noor, 8 nov 2026)

**Cijfer: 3. Advies: nee voor nu, volgen.** MentraOS is een open besturingssysteem voor slimme brillen (Mentra Live, Even Realities G1, Vuzix Z100) met een eigen winkel. Met Mentra 3.0 (17 aug 2026) is alles herbouwd: apps draaien nu op de telefoon, met een nieuwe Miniapp SDK. Maar makers kunnen in 3.0 hun miniapp nog **niet** in de winkel zetten, de winkel bevat alleen 10 apps van Mentra zelf, en er is nergens een plan om te kunnen betalen. Dat is volgens de rol een nee tot er nieuws komt.

Bronnen: alles zelf gemeten (winkel-API, docs, npm, Discord, GitHub). Geen agent, geen controleur: het advies is geen ja en de doorslaggevende feiten staan letterlijk in de docs.

## 1. Groeit het platform? Onbekend, eerder klein.
- Geen verkoopcijfers van Mentra Live gevonden. $8M opgehaald in juni 2025, investeerders onder wie Y Combinator, Toyota Ventures, Alexa Fund en Eric Migicovsky (DERDEN, https://gamesbeat.com/mentra-raises-8m-and-launches-mentraos-2-0-open-source-smartglasses-software/).
- Discord "Mentra Community": 6.169 leden, 864 online (GEZIEN, openbare invite-API van discord.gg/5ukNvkEAqT, 8 nov). Ter vergelijking: Even Realities 18.794 (zie even-hub.md).
- GitHub MentraOS 2.407 sterren, dagelijks actief (GEZIEN, GitHub search API).
- npm: de oude cloud-SDK `@mentra/sdk` piekte op 20.113 downloads in juni 2026 en zakte naar 7.639 in oktober; de nieuwe `@mentra/miniapp` stijgt van 502 (juli) naar 83.335 (oktober) (GEZIEN, api.npmjs.org). Dat laat ontwikkelaarsinteresse voor 3.0 zien, maar npm-tellingen worden opgeblazen door CI en agents (GOK).

## 2. Is de winkel jong? Ja, te jong: makers mogen er nog niet in.
- De winkel-API (apps.mentraglass.com/api/store/apps) geeft 10 apps, allemaal van Mentra zelf: Captions, Livestreamer, Mentra AI, Mentra Call, Mentra Maps, Mentra Notes, Merge, Recorder, Teleprompter, Translation (GEZIEN, 8 nov).
- Docs letterlijk: "There is currently no way to distribute a miniapp built with the Miniapp SDK. In a future release, developers will upload miniapps through the Mentra Developer Console" (GEZIEN, https://docs.mentraglass.com/app-devs/getting-started/distribution.md). Geen datum.
- De apps van derden uit de oude cloud-tijd zijn door de herbouw uit de winkel verdwenen (GEZIEN: de winkel toont er geen enkele meer; hoeveel het er waren niet gemeten, Wayback gaf 429).

## 3. Kan er betaald worden? Nee, geen plan gevonden.
- Geen pagina over betalen, prijzen of omzetdeling in de volledige docs-index (GEZIEN, https://docs.mentraglass.com/llms.txt). De docs noemen alleen een Auth-API om je eigen backend aan te roepen; een eigen abonnement buiten de winkel zou technisch kunnen (GOK).

## 4. Is er vraag? Klein en niet gemeten.
- Mentra's eigen apps dekken de bekende wensen (ondertitels, vertalen, notities, navigatie, teleprompter). Discord-verzoeken niet gelezen (inloggen nodig).

## 5. Is de eerste plek te pakken? Pas als de winkel opengaat.
- Dan is alles leeg behalve de eigen apps van Mentra. Kansrijk lijkt een categorie die Mentra zelf niet doet en die een camera nodig heeft, bijvoorbeeld werkinstructies of checklists met foto voor monteurs (Mentra mikt met 3.0 ook op bedrijven) (GOK).

## Risico
- Mentra herbouwde het platform al één keer volledig; makers van de oude cloud-apps begonnen opnieuw. Dat kan weer gebeuren.
- Klein bedrijf, klein publiek, concurrenten met veel meer brillen (Meta, Even Realities, Google Android XR).

## Wat het zou veranderen
- De Mentra Developer Console opent voor publicatie van miniapps: dan meteen opnieuw wegen (winkel-API tellen, wie erin staat).
- Een aankondiging van betaalde miniapps of een omzetdeling.
- Herhaalmeting rond 8 feb 2027 of eerder bij nieuws: `curl -s https://apps.mentraglass.com/api/store/apps` (aantal apps en makers), npm `@mentra/miniapp`, Discord-leden.

## Cijfer
Vraag 1: onbekend tot klein. Vraag 2: winkel nog dicht voor makers. Vraag 3: geen plan. Vraag 4: klein. Vraag 5: straks open. Samen 3.
