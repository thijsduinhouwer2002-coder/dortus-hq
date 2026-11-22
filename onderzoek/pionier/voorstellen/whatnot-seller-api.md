# Voorstel pionier: Whatnot Seller API (apps voor live-verkopers)

Noor, 9 nov 2026 (run 09:39 UTC). Cijfer **5, nog niet klaar**. Eén stap van Whatnot (apps van derden toelaten) kan het een 7 maken; daarom elke week meten.

## In het kort
Whatnot is de snelst groeiende winkelplek die ik tot nu toe zag: live shopping, $20 miljard waard, verkoop verdubbelt dit jaar. Op 29 oktober 2026 (tien dagen geleden) ging de Seller API open voor elke verkoper die live mag verkopen, na twee jaar beta. Maar die opening is **alleen voor eigen gebruik**: een verkoper maakt een eigen sleutel en koppelt zijn eigen systemen. Apps die wij aan veel verkopers verkopen, kunnen alleen met een OAuth-app die Whatnot zelf toekent; daarvoor is geen openbaar loket, geen app-lijst en geen winkel. De techniek ervoor staat al klaar in de docs ("different sellers using your app"). Zodra Whatnot dat loket opent, is dit een lege markt op een platform dat hard groeit. Tot die tijd kunnen we er niet echt verkopen.

## 1. Groeit het platform hard en zichtbaar? Ja, het hardst van alles wat ik zag.
- Live-verkoop $3 miljard in 2024, meer dan $8 miljard in 2025; in de eerste helft van 2026 meer verkocht dan in heel 2025; de CEO verwacht dat het volume in 2026 verdubbelt (DERDEN, https://valueaddedresource.net/whatnot-20-billion-valuation/).
- Waardering $5 miljard (jan 2025), $11,5 miljard (okt 2025), $20 miljard (aug 2026, Series G van $545 miljoen) (DERDEN, zelfde bron).
- Meer dan 650.000 nieuwe mensen per week, 5 miljoen nieuwe listings per dag, 1 miljard orders totaal in juni 2026, ±60% van de live shopping in Noord-Amerika en Europa (DERDEN, zelfde bron).
- Uitbreiding: VS, Canada, VK, Frankrijk, Duitsland, Australië op de blog; Ierland in 2027; eerste landelijke reclamecampagne in de VS in okt 2026 (GEZIEN, menu van blog.teamwhatnot.com; DERDEN, kop op valueaddedresource.net van 24 okt 2026).
- Motor: veel geld (a16z, CapitalG, ICONIQ), categorieën groeien buiten kaarten (mode is nu de grootste op orders), concurrenten (eBay Live, TikTok Shop, StockX Live) trekken de hele soort mee.

## 2. Is de app-winkel jong of gaat hij net open? Er is geen winkel. De API is tien dagen algemeen open, alleen voor eigen gebruik.
- "Starting today, every seller approved to sell live on Whatnot can now access the Whatnot Seller API", gepubliceerd 29 okt 2026 (GEZIEN, https://blog.teamwhatnot.com/unitedstates/whatnot-seller-api, datePublished 2026-10-29).
- Zelfde blog: "This release supports integrations you build for your own business today, with more updates and functionality to come in the future" en "Don't send [your personal access token] to a vendor or developer" (GEZIEN).
- De docs kennen wel apps voor meerdere verkopers: rate limit "per seller, per connected app ... different sellers using your app don't share", tokens met voorvoegsel `wn_access_tk_` "issued to an app through OAuth", en klantgegevens "only if Whatnot has approved your app" (GEZIEN, https://developers.whatnot.com/llms-full.txt en /getting-started/authentication/index.md).
- Zo'n OAuth-app krijg je niet zelf: "Your Client App will need a secret, which the Whatnot team will generate and provide to you via secure link" (GEZIEN, https://developers.old.whatnot.com/docs/getting-started/authentication). Geen aanmeldformulier of partnerprogramma gevonden (GEZIEN door hulpagent: docs, help-center-zoek-API, blog).
- Geen app-lijst of directory: verkopers vinden tools via lijstjes van de makers zelf, de Chrome Web Store en Reddit (GEZIEN door hulpagent).
- Wie al OAuth heeft: Mascot ("Authorize Mascot to access your Whatnot account", GEZIEN, https://intercom.help/withmascot/en/articles/10427727). Verder vond de hulpagent geen enkele tool die via de officiële API werkt.
- Ook nieuw sinds de GA: MCP-koppeling voor Claude en Cursor, verzendlabels maken via de API, snellere webhooks (GEZIEN, blog en docs).

## 3. Kan er betaald worden? Ja, met een eigen kassa; geen verbod gevonden. Maar we kunnen pas verkopen met een OAuth-app van Whatnot.
- Mascot vraagt $4, $99 of $399 per maand plus 1 tot 1,25% van de omzet en koppelt via OAuth (DERDEN via hulpagent, withmascot.com/pricing; koppeling GEZIEN).
- De oude docs gaan uit van betaalde apps: "you may request less than your maximum if needed (e.g. if certain features are an upsell within your platform)" (GEZIEN, developers.old.whatnot.com).
- Losse tools voor Whatnot-verkopers vragen $9 tot $49 per maand (NotBot $30 GEZIEN https://mellowstate.com/notbot; Aftershows $19, Viewnot $49 tot $199, SellDeck tot $24,99, via hulpagent GEZIEN).
- Niet gelezen: de API-voorwaarden. De docs zeggen alleen "License: Proprietary"; whatnot.com geeft 403 op curl. Volgens derden verbieden de gewone voorwaarden scrapen (DERDEN, alleen titel, conductatlas.com). Dat raakt de vele scrapende Chrome-extensies, niet een officiële OAuth-app.
- Whatnot houdt niets af van een eigen abonnement; kosten vooraf: geen bekend. Wel nodig: een Whatnot-verkopersaccount om te testen (alleen Thijs kan dat aanmaken) en een OAuth-app van het Whatnot-team.

## 4. Is er vraag te zien? Ja.
- Whatnot zelf: koppelen aan eigen systemen was "one of your top requests" (GEZIEN, blog 29 okt).
- 33 tools van derden gevonden, bijna allemaal kleine Chrome-extensies onder 200 gebruikers die whatnot.com uitlezen: labels en bakjes (Scan2Tray, NotBot, SwiftSale, BundleLive 6, Last Label Printer 27), analytics (Whatnot Seller Analytics 69, LiveStreamPro 54, SellDeck 26), breaks (Break → CSV 44), videobonnen (177, 2,3 sterren) (GEZIEN door hulpagent, Chrome Web Store en sites).
- Terugkerende wensen: inpakken en sorteren na de show; analytics tijdens de show ("Whatnot doesn't tell you in real time"); weten of Boost (betaalde promotie) iets oplevert; 13 van 38 in een poll op r/whatnotapp werken met spreadsheets (DERDEN, https://aftershows.co/whatnot-apps; snapshots r/whatnotapp mei en juni 2026 via hulpagent).
- Nieuwe pijn: Whatnot stopt per 4 nov 2026 met het betalen van USPS-gewichtscorrecties; verkopers dragen die kosten nu zelf (DERDEN, https://valueaddedresource.net, kop van 3 nov 2026). Gewicht en afmetingen goed zetten wordt dus geld waard.

## 5. Is de eerste plek in een categorie nog te pakken? Ja, in elke categorie die de officiële API nodig heeft; maar pas als Whatnot apps toelaat.
- **Inpakken en labels:** al bezet door Scan2Tray (desktop, Whatnot plus TikTok Shop plus eBay Live, "pack 1,000s of orders in under an hour", GEZIEN https://scan2tray.com) en NotBot ($30). Niet onze hoek.
- **Winst per show en Boost-rendement (onze kans):** de API geeft per show `estimated_earnings`, `in_show_estimated_sales`, `giveaway_orders_count` en meer (GEZIEN, llms-full.txt). Huidige beste: Aftershows ($19, werkt met CSV-upload), SellDeck (26 gebruikers), spreadsheets. Niemand gebruikt de officiële gegevens. Wij kunnen beter: automatisch na elke show een rapport met echte winst na kosten, giveaways, verzendcorrecties en Boost, vergelijk per categorie en tijdstip, zonder CSV en zonder scrapen.
- **Gewicht en verzendcorrecties (tweede kans):** sinds 4 nov betaalt de verkoper de USPS-correcties. Een app die per product het gewicht controleert en correcties per show telt, bestaat nog niet (GOK, niets gevonden).

## Eerste productidee
"Showcijfers voor Whatnot": koppelt via OAuth, stuurt na elke show een overzicht (omzet, echte winst, giveaways, Boost, verzendcorrecties) en laat per week zien welke tijden en categorieën het meeste opleveren. Gratis: laatste show. Betaald ($15 tot $25 per maand): alle shows, vergelijken, meerdere accounts, export naar boekhouding. Past ook bij Tess: dezelfde soort verkopers zitten op TikTok Shop (Scan2Tray doet beide al).

## Risico's en waaraan je ze ziet
- **Whatnot opent apps van derden nooit, of alleen voor grote partners.** Teken: over drie maanden staat er nog steeds "integrations you build for your own business" en geen partnerformulier. Dan blijft het een 4.
- **Whatnot bouwt de analytics zelf.** Ze kochten in juli 2026 een AI-bedrijf (Shaped) voor zoeken en aanbevelingen (DERDEN, valueaddedresource.net), en de show-analytics zitten al in de Seller Hub. Teken: nieuwe analytics-schermen in de Seller Hub.
- **Groei stokt.** Teken: geen verdubbeling in 2026, of eBay Live en TikTok Shop pakken het marktaandeel.
- **Wij zijn geen verkoper.** Testen kan alleen met een verkopersaccount dat live mag verkopen (stap voor Thijs), en zonder eigen shows hebben we geen echte gegevens.

## Wat ik niet kon meten
- Aantal verkopers met API-toegang of aantal OAuth-apps: niet openbaar.
- De API-voorwaarden: whatnot.com geeft 403; alleen met een browser of via Thijs te lezen.
- Hoe je als maker een OAuth-app aanvraagt: geen openbaar loket. Een mail van Thijs aan het Whatnot-team zou het antwoord geven, maar dat is posten onder zijn naam; alleen als Hans dat wil.

## Cijfer en advies
**5, nog niet klaar.** Vraag 1 is een 10, vraag 5 is goed (lege hoeken met de officiële API), betalen met eigen kassa mag. Maar er is geen winkel en geen open weg voor apps van derden, dus we kunnen nu niets aan andere verkopers leveren. Dit is wel de beste "vlak voor het opengaat"-plek die ik zag: wie er staat op de dag dat Whatnot OAuth-apps opent, is vroeg.

**Herhaalmeting elke week (eerste keer 16 nov):** `python3 -I data/whatnot-api-meet.py` en vergelijk met 9 nov (docs ±69.450 tekens met 'connected app' 2, 'client secret' 1, 'marketplace' 4 alleen als veldnaam; blog: 'vendor' 7, 'more updates' 1). Een nieuw woord als 'partner', 'apply' of 'app directory' is een reden om meteen opnieuw te wegen; dan mogelijk een 7.
