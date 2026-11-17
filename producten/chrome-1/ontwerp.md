Akkoord: nee (concept, wacht op de productkeuze van ±10:45 NL en op de controleur)

# Chrome-extensie 1: ontwerp (CONCEPT voor kandidaat 1, Google Agenda in bulk)

Kai, 17 nov 2026, run 2. Geschreven vóór de keuze, zodat het bouwen direct na 10:45 kan beginnen. Kiest de hoofdchat iets anders, dan blijft alleen het deel "Sleutel en betalen" staan.

**Waarom wij (één zin):** Ruim je Google Agenda op in één keer: onbeperkt gratis verwijderen, dubbele afspraken vinden over al je agenda's heen (ook na een Outlook-koppeling), en titels zoeken en vervangen, met een voorbeeld van elke wijziging vóór je klikt en alles ongedaan te maken.

Werknaam: **Agenda Opruimer** (Engels in de winkel, GOK: "Calendar Sweep"). Naam en uiterlijk met Daan.

## Wat het doet
Een venster van de extensie (eigen tabblad, geen pop-up: lijsten van honderden afspraken passen niet in een pop-up) praat rechtstreeks vanuit de browser met de officiële Google Calendar-API. De gebruiker logt zelf in bij Google; wij zien nooit een wachtwoord en hebben geen server.
1. **Kiezen:** agenda's (meerdere tegelijk), periode, filter op tekst in titel, beschrijving of locatie, kleur, "door mij gemaakt" of "uitgenodigd". Lijst met vinkjes, shift-klik voor een reeks, "alles selecteren".
2. **Doen met de selectie:** verwijderen, verplaatsen naar een andere agenda, verzetten (minuten tot weken, klok blijft gelijk over zomertijd heen), kleur geven, zoeken en vervangen in titel, beschrijving of locatie.
3. **Dubbelen:** zoekt over alle gekozen agenda's naar afspraken met dezelfde titel (hoofdletters, spaties en leestekens tellen niet) en hetzelfde begin en eind (hele dagen: zelfde datum). Toont groepen, stelt per groep voor welke blijft (die in de agenda die de gebruiker bezit, bij gelijkspel de oudste), de rest staat aangevinkt.
4. **Voorbeeld en terug:** vóór elke actie een lijst "dit gaat er veranderen" met aantallen; na de actie "Ongedaan maken" voor de laatste 10 acties (oude versie van elke afspraak lokaal bewaard; verwijderde afspraken komen terug via `events.insert` met dezelfde velden).
5. **Netjes voor anderen:** gasten krijgen standaard geen mail (`sendUpdates=none`), keuze om ze wel te mailen. Bij een afspraak waar je alleen gast bent, verdwijnt hij alleen uit jouw agenda (Google doet dat zelf bij `events.delete` door een gast, GOK, na te lezen in stap 2).

## Wat het bewust niet doet
Geen eigen server, geen gegevens naar ons of derden, geen bediening van de agendapagina (breekbaar), geen automatische acties zonder klik van de gebruiker in versie 1 (een wekelijkse regel komt pas na de lancering, als er vraag is), geen afspraken maken uit tekst of AI, geen Outlook of Apple. Geen scopes breder dan nodig.

## Hoe het aansluit (techniek)
- **MV3.** Rechten: `identity`, `storage`; `host_permissions` alleen `https://www.googleapis.com/*` en `https://api.gumroad.com/*`. Geen content script.
- **Inloggen:** `chrome.identity.launchWebAuthFlow` met een OAuth-client van Thijs (scopes `calendar.events` en `calendar.calendarlist.readonly`, GEZIEN in run 1). Waarom niet `getAuthToken`: dat werkt alleen in Chrome met een aangemeld profiel; `launchWebAuthFlow` werkt ook in Edge en Brave (Calendar Bulk belooft die drie, GEZIEN). Token verloopt na een uur; dan stil opnieuw met `prompt=none`, lukt dat niet, een knop "Opnieuw verbinden". Precieze vorm (implicit token of PKCE, type client) lees ik na in stap 2; GOK tot dan.
- **API-gebruik:** `events.list` met `singleEvents=true`, pagina's via `nextPageToken`, hooguit 2.500 per pagina; acties één voor één met een kleine pauze en opnieuw proberen bij 403 `rateLimitExceeded` en 429 (wachten 1, 2, 4, 8 s). Terugkerende afspraken: een actie raakt standaard alleen de gekozen keren; "hele reeks" is een aparte keuze.
- **Bestanden (elk onder 400 regels):** `manifest.json`, `app.html`/`app.css`/`app.js` (scherm), `lib/google.js` (inloggen en API, één plek om na te bootsen), `lib/dubbelen.js` (zuivere functie, los te testen), `lib/acties.js` (uitvoeren, voorbeeld, ongedaan maken), `lib/sleutel.js` (Gumroad), `lib/grens.js` (teller gratis gebruik). `architectuur.md` erbij.

## Gratis en betaald (prijs GOK, Chris beslist)
- **Gratis, zonder grens:** alles zien en selecteren, onbeperkt verwijderen (SUPER en Calendar Bulk geven dat ook, dus anders verliezen we), dubbelen **vinden en zien**.
- **Gratis met grens, zichtbaar vóór de eerste klik:** 25 afspraken per dag verplaatsen, verzetten, kleuren, zoeken en vervangen, of als dubbel opruimen. Teller staat altijd in beeld.
- **Pro:** geen grens. Voorstel naast Calendar Bulk ($9 eenmalig) en SUPER ($29 per maand): $19 levenslang of $4 per maand (GOK).

## Sleutel en betalen (geldt voor elke kandidaat)
- Gumroad: `POST https://api.gumroad.com/v2/licenses/verify` met `product_id`, `license_key`, `increment_uses_count=false` (GEZIEN, run 1). Goed als `success` en niet `refunded`, `disputed`, `chargebacked`, en bij een abonnement geen `subscription_ended_at`, `subscription_cancelled_at` of `subscription_failed_at` in het verleden.
- Controle bij invoeren, daarna hooguit één keer per dag. **Les Lars (verhaal 29):** een sleutel die ooit goed was, blijft 30 dagen Pro als Gumroad niet antwoordt (time-out, geen netwerk, 5xx, 429). Alleen een duidelijk "nee" van Gumroad (404, of terugbetaald) haalt Pro weg, en dan met een melding waarom.
- Elke fout van Google of Gumroad geeft een melding in gewone woorden met wat de gebruiker kan doen ("Google antwoordt even niet. Je afspraken zijn niet veranderd. Probeer het over een minuut opnieuw.").

## Wanneer is het af (toetsbaar)
1. e2e in Chromium met Playwright (nagebootste Google en Gumroad, antwoorden in de vorm van de documentatie) slaagt voor: inloggen, 3 agenda's laden met meer dan één pagina, filteren, 30 afspraken verwijderen en ongedaan maken, 10 verzetten over een zomertijdwissel (klok blijft gelijk), zoeken en vervangen met voorbeeld, dubbelen over 2 agenda's (met verschil in hoofdletters) vinden en opruimen.
2. Grens: de 26e betaalde actie op een dag wordt geweigerd met uitleg; met geldige sleutel niet; teller staat vóór de eerste klik in beeld.
3. Storingen: Google 403, 429, 500 en time-out midden in een reeks: niets dubbel uitgevoerd, melding in gewone woorden, doorgaan kan. Gumroad time-out, 500 en geen netwerk na een eerdere goede controle: Pro blijft Pro (ook na 29 dagen nagebootste tijd), na 31 dagen terug naar gratis met melding. Gumroad 404 en "refunded": gratis met melding.
4. Unit-tests voor `dubbelen.js` en `sleutel.js` groen; workflow bouwt de zip als Actions-artefact en zet schermafbeeldingen op de tak `schermen`.
5. Daan zet `Akkoord: ja` bovenaan (uiterlijk, icoon, winkelbeelden), en alles op de winkelpagina is door de test gedekt.

## Wat Thijs moet doen (komt op de lijst na de keuze)
Google Cloud-project met OAuth-toestemmingsscherm en client (±15 min), Gumroad-product met licentiesleutel en `product_id` doorgeven, Chrome-ontwikkelaarsaccount ($5, geld), daarna de keuring bij Google aanvragen (tot 10 dagen; tot dan hooguit 100 gebruikers en een waarschuwing).
