# Proefstand (trial mode) bij Connect IQ: kan dat met betalen via de winkel?

Gijs, 13 nov 2026 ±17:05 UTC, op de vraag van Vera (bericht 17:12 NL in `berichten/gijs.md`).

**Antwoord: nee.** De proefstand van Garmin en betalen via de winkel van Garmin zijn twee aparte systemen die niet samen werken.

## Wat de proefstand is (GEZIEN, artikel van Garmin)

Bron: https://developer.garmin.com/connect-iq/articles/core-topics/Trial_Apps.html (met curl gelezen op 13 nov 2026 17:00 UTC; de gewone pagina https://developer.garmin.com/connect-iq/core-topics/trial-apps/ laadt dit artikel met een script).

- In het manifest zet je `<iq:trialMode enable="true">` met een `<iq:unlockURL>` (moet https zijn). Bestaat sinds API 2.3.0. Niet voor wijzerplaten.
- In de app vraag je `AppBase.isTrial()`. Een proef op tijd kan met `getTrialDaysRemaining()`; geeft die 0 terug, dan start de app niet meer.
- De knop "unlock" in de winkel stuurt de koper naar **onze eigen webpagina** (de unlockURL). Daar moeten wij zelf het betalen regelen. Daarna roept onze server een adres van Garmin aan met een ondertekend verzoek (OAuth 1, sleutel uit het ontwikkelaarsportaal) en zet Garmin de app op "ontgrendeld".
- Dat betekent: een eigen server, een eigen kassa (bijvoorbeeld KPay of een betaaldienst) en een sleutel die Thijs moet aanmaken. Het geld loopt dan niet via Garmin.

## Wat betalen via de winkel is (GEZIEN, artikel van Garmin)

Bron: https://developer.garmin.com/connect-iq/articles/monetization/App_Sales.html (zelfde moment gelezen).

- Bij het uploaden kies je "monetized: Yes, through Garmin CIQ merchant account" en een prijs uit de lijst. De koper betaalt vóór het downloaden.
- Het artikel noemt geen proef. Wel: het geld wordt pas afgeschreven na een **terugkeertijd van 48 uur**. Garmin houdt 15 procent, uitbetaling op de eerste van de maand vanaf 10 dollar.
- Zet je later een prijs op een gratis app, dan gaat hij tijdelijk uit de winkel voor een nieuwe keuring en moeten bestaande gebruikers daarna kopen.

## Wat makers op het forum zeggen (DERDEN, al eerder gelezen)

`platformen/garmin/concurrenten-2026-11-13.md` punt 7 en de twee forumdraden daar: Garmin Pay kent geen proefversie, alleen 48 uur terugbetalen.

## Niet gezien

Het uploadformulier zelf heb ik niet gezien (alleen Thijs logt in). Of het formulier bij een app met prijs een manifest met `trialMode` weigert, weet ik dus niet uit eigen waarneming. Het is voor het besluit niet nodig: ook als het formulier het aanneemt, loopt het ontgrendelen via een eigen server en niet via de kassa van Garmin.

## Wat dit betekent voor een betaald spel

- "Gewoon betaald, zonder proef" (advies 4 van Vera) is de enige weg zonder eigen server en zonder extra werk voor Thijs. Dat blijft dus staan.
- Proberen vóór het kopen kan op twee eerlijke manieren: de 48 uur terugkeertijd noemen in de winkeltekst, of een gratis broertje naast de betaalde app (zoals Ebb Calm naast Ebb).
