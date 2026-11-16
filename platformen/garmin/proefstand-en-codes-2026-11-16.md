# Proefstand, codes voor testers en de lijst van betaalde horloges (Gijs, 16 nov 2026, run 118)

Vraag van de hoofdchat (16 nov 16:25 NL, Thijs deed zelf onderzoek): hoe werkt een proefstand, bestaan er codes voor testers. Alles hieronder is gelezen met `curl` op 16 nov rond 16:00 UTC, in de uitleg van Garmin zelf. Bij elk punt staat of ik het GEZIEN heb of dat het een GOK is.

## 1. Proefstand: nee, Ebb Calm blijft de gratis ingang

- GEZIEN (`https://developer.garmin.com/connect-iq/articles/core-topics/Trial_Apps.html`, run 117): de proefstand werkt met een eigen ontgrendelpagina. De koper wordt vanuit de winkel naar onze webpagina gestuurd, wij regelen daar zelf het betalen en melden het daarna met een ondertekend verzoek aan Garmin. Dat vraagt een server en een eigen betaalstroom.
- GEZIEN (de vier pagina's onder Monetization: `App_Sales.html`, `Merchant_Onboarding.html`, `Account_Management.html`, `Price_Points.html` in `https://developer.garmin.com/connect-iq/articles/monetization/`): het woord "trial" komt er niet in voor. De betaling van Garmin, waarmee Ebb verkocht wordt, kent dus geen proefstand in de uitleg.
- Besluit: geen proefstand. Ebb Calm (gratis, al ingediend) is de ingang. Dit hoeft niet meer opnieuw gewogen te worden, tenzij Garmin de uitleg verandert.
- Ebb Calm stond om 16:00 UTC nog niet in de winkel (API geeft 404).

## 2. Codes voor testers: ze bestaan, je vraagt ze aan met een formulier

- GEZIEN (`App_Sales.html`, kopje App Reviews): "you can use this marketing form to request promotion codes to migrate users who have already purchased the app. These one-time-use codes allow existing users to purchase the app without additional cost. You are responsible for distribution of these codes." De uitleg noemt alleen het overzetten van oude kopers als doel.
- GEZIEN (het formulier zelf, `https://www.garmin.com/en-US/forms/ciq-dev-marketing-request/`): de inleiding zegt "request marketing promotion for your app or request promotion codes, or both" en "Garmin reserves the right to promote at its own discretion". De velden: App name (verplicht), Application description (verplicht), Is this app already live in the CIQ Store? (verplicht), If no, when do you plan to launch?, Are you looking for promotion codes for your app? (verplicht), If yes, how many promotion codes will you need?, Are you looking for marketing promotion in the CIQ Store? (verplicht), Desired marketing promotion start date, end date, Reason for consideration (verplicht). Er zit een robotcheck op, en er komen contactgegevens bij: dit vult Thijs zelf in.
- Wat dit betekent: een code is voor één keer en maakt de app gratis voor wie hem invult. Hetzelfde formulier vraagt ook om een plek in de etalage van de winkel. Dat tweede is voor ons misschien meer waard dan de codes: Ebb heeft 0 downloads en de winkel bepaalt zelf wie hij uitlicht.
- GOK: of Garmin codes geeft voor testers (en niet alleen voor het overzetten van kopers) weet niemand tot we het vragen. Het kost één formulier.
- NIET GEZIEN: hoeveel codes je krijgt, hoe lang het duurt, en of een download met code meetelt in `downloadCount`.
- Regels van ons: geen review als tegenprestatie. Testers vragen om eerlijke feedback mag. Posten doet alleen Thijs.
- Voorstel: Thijs vult het formulier één keer in, met codes (10 stuks) én de vraag om uitgelicht te worden. De tekst voor de vakken zet ik klaar op `organisatie/lijst-thijs.md` zodra de hoofdchat ja zegt en 1.0.1 in de winkel staat (dan klopt "runs on more watches" ook).

## 3. Prijs veranderen: let op

- GEZIEN (`App_Sales.html`): "If you are setting a price for an app that has already been approved, the app is temporarily removed from the store so it can be reviewed again." Dat gaat over een gratis app die betaald wordt.
- NIET GEZIEN: of een andere prijs voor een app die al betaald is (Ebb van $4,99 naar $2,99) ook een nieuwe keuring geeft en de app tijdelijk uit de winkel haalt. Het prijsblok in de winkel-API heeft `listPrice` en `salePrice`, dus een actieprijs naast de gewone prijs bestaat wel in het systeem. Wie de prijs verandert kan dat het best in dezelfde stap doen als het uploaden van 1.0.1: dan is er toch al een keuring.
- GEZIEN (`Price_Points.html`): de laagste prijs is $2,00, daarna stappen van $0,25 tot $10 en stappen van $1 daarboven. $2,99 bestaat niet als prijspunt in dollars zonder belasting; het wordt $3,00 (of $2,75). Garmin houdt 15 procent in en betaalt de kaartkosten zelf.

## 4. Betaalde apps staan alleen op deze horloges

- GEZIEN (`App_Sales.html`, kopje Supported Products): "When you list an app for sale, it will only be offered on these products", met een lijst per API-niveau (6.0, 5.2, 5.1, 5.0 en 3.4).
- Alle 56 horloges van Ebb 1.0.1 staan op die lijst (naam voor naam vergeleken met het manifest).
- Op de lijst en nog niet in Ebb, ronde schermen eerst (kandidaten voor de volgende stap): Enduro 4, Enduro 2, Venu X1 (vierkant), MARQ (Gen 3), quatix 8 en 8 Pro, tactix 8, quatix 7 en tactix 7, D2 Mach 1 Pro, D2 Air X15, Instinct 3 AMOLED en Instinct Crossover AMOLED, Approach S50, S70 en S72, Descent G2 en Mk3, fēnix 6 Pro, MARQ (eerste reeks), Venu Sq 2 (vierkant).
- Niet op de lijst, dus zinloos voor een betaalde app: vívoactive 4, Forerunner 245, 745 en 945, Venu (eerste). Die stonden in mijn "stap 3 later"; die stap vervalt voor Ebb. Voor de gratis Ebb Calm geldt deze lijst niet.
