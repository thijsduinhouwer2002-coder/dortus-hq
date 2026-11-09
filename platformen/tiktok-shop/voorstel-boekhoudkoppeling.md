# Voorstel eerste product TikTok Shop: boekhoudkoppeling per land

Tess, 9 nov 2026, run 02:03 UTC. Voor Hans: ja of nee om te gaan ontwerpen (met Daan). Bouwen pas na zijn ja en een ontwerp dat Daan keurde; indienen pas na registratie (KvK). Onderzoek: `onderzoek/2026-11-08-finance-api.md`, `onderzoek/2026-11-08-nl-boekhoudkoppelingen.md`, `onderzoek/2026-11-09-boekhouding-fr-es-it.md`, `onderzoek/2026-11-08-categorieen-vs-eu.md`, `onderzoek/2026-11-09-live-verkoop-eu.md` (alle nagekeken). Dit voorstel is nagekeken door een controleur (akkoord na 14 verbeteringen, verwerkt).

## Wat het is
Een app in de TikTok Shop App Store die elke uitbetaling van TikTok Shop, met de commissie, kosten en terugbetalingen per bestelling, vanzelf boekt in het boekhoudpakket van de verkoper: Moneybird en Exact in Nederland, Pennylane in Frankrijk, Fatture in Cloud in Italië. Eén app voor NL, FR en IT, elk land met zijn eigen pakket. Duitsland (bezet door DATEV-exporten) en Spanje (zwakste betaalbewijs) doen we nu niet.

**Waarom wij (één zin):** de eerste app in de TikTok Shop App Store die je TikTok-uitbetalingen per bestelling vanzelf in je eigen lokale pakket boekt (Moneybird, Exact, Pennylane, Fatture in Cloud), waar de bestaande EU-apps alleen DATEV, losse exports of Xero en QuickBooks bieden.

## Voor wie, wie betaalt, hoeveel, hoe vaak
- Kleine en middelgrote TikTok Shop-verkopers in NL, FR en IT die een lokaal pakket gebruiken (of hun boekhouder).
- Maandabonnement per winkel: gratis tot een klein aantal bestellingen per maand (proef), daarna €15 per maand, €29 per maand voor meer bestellingen of meerdere winkels (GOK, Chris maakt de prijs).
- Afrekenen met een eigen kassa (Polar of Stripe): TikTok rekent volgens de partner-docs niet zelf af en noemt geen afdracht (GOK op basis van GEZIEN, https://partner.tiktokshop.com/docv2/page/app-price-information en `platformen/pionier/voorstellen/tiktok-shop-app-store.md`).

## Bewijs dat zulke mensen al betalen
Let op: dit zijn koppelingen voor Bol, Amazon en Shopify. Dat er voor een TikTok-koppeling naar een lokaal pakket betaald wordt, is nog nergens gezien (er bestaat er nog geen).
- NL (GEZIEN): Webwinkelfacturen (Bol naar Moneybird, Exact, e-Boekhouden, €80 tot €180 per jaar), iWebDevelopment (Bol en Amazon naar Exact, €12 tot €29 per maand), xCore (€29 per maand plus €250 installatie), elk in het officiële overzicht van Moneybird of Exact. Moneybird-koppelingen op Shopify: 30 reviews ($18 tot $36) en 7 reviews ($15,95).
- FR (GEZIEN): Order Invoicer (Amazon, eBay, Etsy en meer naar Pennylane, Axonaut, Sellsy): €0, €12, €59, €149, €299 per maand, "450+ marchands" (eigen claim).
- IT (GEZIEN): Fatturify (Shopify naar Fatture in Cloud) 25 reviews, $15 en $30 per maand; GetSync 24 reviews, tot $59,50.
- VS (GEZIEN): 18 boekhoudapps met vaste prijs in de TikTok-winkel, mediaan $27 per maand; maar dat zijn vooral boekhoudplatforms, geen losse koppelingen.
- Oordeel: redelijk voor de VS, dun voor NL (reviews 7 en 30), redelijk voor FR en IT. Klantenaantallen niet zichtbaar.

## Het gat
- Geen enkele listing in de 13 EU-landen en GB noemt Moneybird, Exact, e-Boekhouden, SnelStart, Pennylane, Holded of Fatture in Cloud (GEZIEN, twee keer los gezocht).
- Link My Books: "TikTok EU regions (Germany, France, Spain, Italy, etc.) are not yet supported" (GEZIEN, help-pagina, 22 juli 2026), al staat de app wel in de ES-winkel.
- Pennylane heeft 318 integraties, geen voor TikTok Shop, Cdiscount of Vinted (GEZIEN). Order Invoicer heeft geen TikTok (GEZIEN, sitemap).
- Technisch: Finance-API met statements en transacties per bestelling, scope "Finance Information" staat op Public, en er is een app-categorie Finance > Accounting (GEZIEN, partner-docs). Voorbehoud uit dezelfde gids: Partner Center is leidend en een scope kan per categorie of markt goedkeuring vragen; dat zien we pas na het aanmaken van een app.
- Markt: TikTok Shop DE, FR, ES en IT samen €498,8 mln in 90 dagen tot 9 juli 2026 (DERDEN, Kalodata via Lengow). FR ongeveer 33.000 verkopers in maart 2026 (DERDEN, zie LIVE-onderzoek). Voor NL, onze eerste markt, is geen omzet of verkoperaantal bekend (live sinds 15 juni 2026).

## De 3 sterkste concurrenten en waarom wij beter zijn
1. **TikTok zelf (gratis Excel):** Seller Center geeft PDF-facturen voor de TikTok-kosten, een Excel per bestelling en een export van uitbetalingen voor het afstemmen (GEZIEN, Seller University). Een boekhouder kan daar nu al mee werken. Wij: vanzelf, per bestelling, zonder handwerk, met de juiste rekeningen en btw per land. Risico: TikTok bouwt later zelf een koppeling (GOK).
2. **Schakel** (NL, €0, €10 of €30 per maand bij jaarbetaling, maandelijks €15 of €50): heeft een pagina TikTok Shop naar Moneybird met OSS en creditfacturen; de andere pakketten staan op "Aanvragen". Niet in de TikTok App Store, alleen NL. Wij: in de App Store, waar verkopers zoeken, en meerdere landen. Of Schakel echt live is: niet te zien zonder account. Schakel zit met €10 per maand onder onze €15.
3. **Link My Books en Order Invoicer:** Link My Books zegt "not yet supported" voor TikTok EU, wat erop wijst dat EU-steun gepland is (GOK), en staat al in de ES-winkel, maar boekt alleen naar Xero en QuickBooks. Order Invoicer doet in FR precies dit voor andere marktplaatsen en kan TikTok toevoegen (GOK). Wij moeten dus snel zijn en lokale pakketten goed doen.
(DATEV-exporten in DE zijn geen concurrent zolang wij buiten DE blijven.)

## Risico's en open punten
- Prijs: in NL is €7 tot €15 per maand gangbaar, in FR en IT €12 tot €30, iets hoger. Dicht bij onze ondergrens van €15.
- Btw: een btw-veld per verkoop voor lokale EU-winkels niet gevonden in de API; vat_amount geldt alleen voor cross-border (GEZIEN). Dat de app de btw zelf moet uitrekenen is GOK.
- NL staat niet in de regiotabel van de partner-docs; dat NL-winkels met dezelfde API werken is GOK.
- Pakket-API's (gemeten 9 nov 02:30, `onderzoek/2026-11-09-pakket-apis.md`, steekproef zelf nagekeken): alle vier hebben OAuth voor apps (GEZIEN). Moneybird: gratis, app zelf registreren, gratis sandbox, boekingen en btw-tarieven mogelijk; limiet 150 aanvragen per 5 minuten per IP voor al onze klanten samen, per administratie aan te vragen. Exact: Developer-abonnement €15 per maand ex btw (geld, dus Thijs), standaard tot 100 administraties, App Store-vermelding pas na goedkeuring. Fatture in Cloud: gratis, ook de App Store, maar geen grootboek of journaalposten in de API (documenten en kasboek). **Pennylane is de grootste rem:** OAuth-sleutels en sandbox alleen via hun partnerteam, koppeling moet gecertificeerd worden, voorwaarden en kosten onbekend.
- Daarom bouwvolgorde (advies): eerst Moneybird (gratis, alles zelf te regelen), dan Exact (na €15 per maand van Thijs), Pennylane pas na contact met hun partnerteam (formulier, onder de naam van Thijs, na de KvK), IT daarna.
- Registratie vraagt KvK; testen in een echte winkel pas daarna. Tot dan bouwen tegen de gedocumenteerde API met nagebootste antwoorden.
- LIVE-hulpmiddelen vielen af: in de EU bijna geen betaalbewijs (één app, DARITAI in ES, €119 per maand, zonder zichtbare klanten), veilingen alleen bevestigd in VS en VK.

## Advies
Ja om te gaan ontwerpen: eerst NL (Moneybird, dan Exact), daarna FR (Pennylane, na ja van hun partnerteam) en IT. Hans beslist.
