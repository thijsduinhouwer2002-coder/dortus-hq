# Stripe App Marketplace (marketplace.stripe.com)

Onderzocht door Vera, 15 nov 2026 run 15:31 (Amsterdam). Eigen meting: alle 1.023 app-pagina's uit de sitemap (naam en omschrijving uit de og-gegevens), gekoppeld aan 12.304 TrustMRR-profielen van 8 nov; voorwaarden gelezen in docs.stripe.com. Geen controleur: het oordeel hangt vooral aan wat niet te meten is. Data: `data/stripe-apps-2026-11-15.json`, script ernaast.

## Wat het is
Apps die in het dashboard van Stripe draaien (React-onderdelen plus eventueel een eigen server), te installeren door elk bedrijf met een Stripe-account. Stripe keurt elke app (±4 werkdagen), alleen Engelse vermeldingen, **één openbare app per Stripe-account** (GEZIEN, docs.stripe.com/stripe-apps/publish-app.md, 15 nov).

## Cijfers
- **Aanbod:** 1.023 apps in de sitemap (GEZIEN). Veel zijn koppelingen van bestaande bedrijven (in 188 omschrijvingen staan woorden als sync, integratie, export; GOK dat het werkelijke aandeel hoger is). Drukke hoeken: facturen (118 omschrijvingen), belasting 29, boekhouding 31, opzeggingen 28, mislukte betalingen 26, geschillen 23 (GEZIEN, telling op woorden).
- **Bereik:** **niet te meten.** De winkel toont geen installs en geen reviews; de pagina's worden pas in de browser opgebouwd. De gegevens komen uit een interne endpoint van Stripe; die heb ik bewust niet gebruikt. Ook bij derden geen installcijfers gevonden.
- **Drukte per maand:** niet te zien, de sitemap heeft geen datums.
- **Geld, hoe het kan (GEZIEN):** de maker laat zelf betalen, via zijn eigen Stripe en een eigen prijspagina; de vermelding moet zeggen "Free" of "Paid subscription required" en de prijs moet gelijk zijn aan die buiten de winkel (publish-app.md en review-requirements.md). Een afdracht aan de winkel staat er niet; GOK dat er geen is, behalve de gewone Stripe-kosten.
- **Geld, bewijs:** van de 1.023 apps vond ik er 23 met dezelfde naam in TrustMRR. De meeste zijn gewone SaaS-bedrijven met een koppeling (Cometly ±$211k per 30 dagen, Refgrow $2.310). Kleine tools die echt om Stripe draaien: MassInvoices $343 per 30 dagen (sinds dec 2024, totaal $3.311), Rebounce $90, Signed Reviews $29, Inflowdash $3 (DERDEN, TrustMRR, geverifieerde omzet, 8 nov). Of die omzet uit de winkel komt of van buiten is niet te zien. Geen maker gevonden die zegt dat de winkel hem klanten brengt.

## Voor en tegen
- Voor: kopers zijn bedrijven die al omzet draaien, geen afdracht aan de winkel, goede documentatie, wij kennen Stripe al.
- Tegen: bereik niet te meten en geen bewijs dat de winkel klanten levert, de bekende hoeken zijn al vol (26 apps voor mislukte betalingen, 23 voor geschillen), één app per account, een eigen server en een eigen betaalpagina nodig, en een Stripe-account op naam van Dortus (dus Thijs, met KvK en ID, wat we vóór de verhuizing niet doen).

## Idee (als het ooit verandert)
Een klein hulpmiddel dat iets doet wat het dashboard niet kan, bijvoorbeeld alle facturen in één keer als pdf voor de boekhouder (zoals MassInvoices, dat ±$340 per maand haalt). Klein, maar het voorbeeld laat zien hoe de orde van grootte ligt.

## Advies
**Cijfer 3. Nee voor nu.** Geld kan zonder afdracht en kleine Stripe-tools verdienen een paar honderd dollar per maand, maar of de winkel daar iets aan bijdraagt is niet aan te tonen, en het bereik is niet te meten. Te meten met een browser die de winkel laadt (dan nog zonder installcijfers) of met een eigen Stripe-account; beide doen we nu niet.
