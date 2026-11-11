# Garmin: uploadformulier en keuringsregels (hoofdchat, 11 nov 22:05 NL)

GEZIEN in het ontwikkelaarsdashboard van Thijs (alleen gelezen) en op developer.garmin.com/connect-iq/app-review-guidelines/ (laatst bijgewerkt 13 okt 2021).

## Stand account
Dashboard meldt: "Je account is goedgekeurd. Je kunt nu apps in de Connect IQ store publiceren zodat ze aangeschaft kunnen worden." Mail van Garmin: 10 nov 16:24 NL. Adres dashboard: apps.garmin.com/nl-NL/developer/dashboard, upload: apps.garmin.com/nl-NL/developer/upload.

## Uploadformulier
- Stap 1: het .iq-bestand kiezen, app-versie (hoogstens 20 tekens), vinkje "Bèta-app (alleen voor testdoeleinden)". Met "Ga door" ga je akkoord met de licentieovereenkomst: dat doet Thijs zelf.
- Stap 2 (details: beschrijving, plaatjes, prijs) komt pas na een geslaagde upload van het bestand. NIET GEZIEN: velden, maten van plaatjes, talen. Dat zien we pas bij het echte indienen.
- Na de upload keurt Garmin; tot die tijd staat de app niet in de winkel, wel kun je hem zelf bekijken en downloaden om te testen.

## Keuringsregels die Ebb raken
1. **Gevaarlijke activiteiten:** apps bedoeld voor gebruik tijdens o.a. scuba diving en free diving zijn verboden. Ebb zegt al "not a freediving or apnea trainer" en "never in or near water": zo houden. Geen duikwoorden of duikbeelden terug laten komen (het oude duikspel had hier kunnen sneuvelen).
2. **Schadelijke uitdagingen:** een app mag gebruikers niet uitdagen tot iets dat lichamelijk risico geeft. Dieren voor trouw en niet voor langer inhouden past daarbij. Geen "new best", geen record, niets dat langer inhouden beloont. Let op bij 8 weeks "avg hold": neutraal tonen, niet als doel.
3. **Medisch:** geen woorden over diagnose, genezen, behandelen of voorkomen. De tekst zegt al "not a medical device". Geen claims over stress, slaap, bloeddruk of angst toevoegen.
4. **Prestaties:** app moet af en getest zijn, geen crashes, batterij niet leegtrekken (dus het punt "Calm hertekent 10 keer per seconde" echt oplossen).
5. **Eerlijke beschrijving:** alle functies, beperkingen en ondersteunde horloges juist. Lijst van horloges in de tekst gelijk aan het manifest.
6. **Betaald:** je moet het **terugbetaalbeleid** noemen (of dat er geen is). ONTBREEKT nu in winkeltekst.md. Ook je supportbeleid duidelijk maken (adres staat er; zin erbij over reactietijd).
7. **Privacy:** eigen privacyverklaring als de app gegevens verwerkt. Ebb zegt "No data leaves your watch"; zet er één zin privacybeleid bij.
8. **Niet voor kinderen onder 13:** Ebb zegt al niet onder 18.
9. **Geen reviews kopen of om ruil vragen.** In de app geen review-vraag (staat al zo).

## Voor Gijs
- Winkeltekst (drie talen): zin over terugbetalen, zin over support, zin privacy. Wat het terugbetaalbeleid wordt beslist Thijs (vraag van de hoofdchat loopt).
- Punt 4 hierboven meenemen bij de codepunten.
