# Plan: betaald vanaf het begin (Klopt, TikTok Shop naar je boekhouding)

Tess, 9 nov 2026, run 21:06 UTC. Taak "Betaald vanaf het begin" uit `taken.md`. Prijs en gratis grens zijn werkwaarden tot Chris beslist (€15 per maand per winkel, 30 bestellingen per maand gratis, beide GOK). Jet maakt hiervan een technisch ontwerp met controleur voordat hij bouwt (regel 0).

## Besluit in het kort
1. **Kassa: Polar, het account dat Dortus al heeft.** Geen nieuw account, geen nieuwe stap voor Thijs (advies 6: stappen van Thijs zo klein mogelijk). Polar is merchant of record: het rekent de btw af en betaalt uit naar Thijs (GEZIEN, besluit Olaf 6 nov en commercie). Software en SaaS mogen volgens de Acceptable Use Policy van 1 okt 2026 (GEZIEN, polar.sh/docs/merchant-of-record/acceptable-use).
2. **Eén product in Polar: "Klopt, per TikTok-winkel", €15 per maand, maandelijks opzegbaar.** Eén abonnement per TikTok-winkel, niet per verkoper: één verkoper met twee winkels betaalt twee keer (zo staat het ook in de registratieteksten: "a subscription per shop").
3. **Gratis deel zonder kassa:** de proef (zien hoe je uitbetalingen geboekt worden, zonder iets in Moneybird) en de eerste 30 bestellingen per kalendermaand vragen geen betaalgegevens. Daarom géén proefperiode in Polar zelf: een Polar-trial vraagt bij de afrekening al betaalgegevens (GEZIEN, polar.sh/docs/features/subscriptions/trials), en dat past niet bij "eerst gratis zien".
4. **In de TikTok App Store:** prijslabel **Paid plan**, minimum €15 per maand, met een **pricing details URL** naar `https://dortus.com/klopt/prijs` waar de gratis proef en de gratis grens staan. Niet "Free plan": dat zou niet waar zijn, en de docs eisen dat prijsinformatie "true, accurate, and up to date" is (GEZIEN, docv2/page/app-price-information). Valuta en periode in het formulier gelijk aan Polar (EUR, maand); welke valuta het formulier per markt toelaat, beslist het formulier (zelfde pagina).

## Wat het kost (GEZIEN, polar.sh/docs/merchant-of-record/fees, 9 nov)
De organisatie Dortus is van 6 nov 2026, dus na 27 mei 2026: plan **Starter, 5% + 50 dollarcent per betaling, plus 1,5% voor een kaart van buiten de VS**, over het totaal met btw. Geen aparte abonnementstoeslag op Starter.
- NL-winkel met btw-nummer (verlegd, totaal €15): 0,75 + ±0,43 + 0,23 = **±€1,41 per maand** (±9%).
- NL-winkel zonder verlegging (totaal €18,15 met 21% btw): 0,91 + ±0,43 + 0,27 = **±€1,61 per maand**.
- Dollarcent omgerekend tegen ±0,86 (GOK, koers schommelt). Pro ($20 per maand, 3,8% + 40¢) loont pas vanaf ±$1.379 omzet per maand (GEZIEN, zelfde pagina), dus nu niet.
- **Wanneer heroverwegen:** boven ±100 betalende winkels kost Polar ±€150 per maand; een eigen kassa met iDEAL en SEPA-incasso (bijvoorbeeld Mollie) is dan goedkoper per betaling, maar vraagt een KvK, een nieuw account en zelf de btw doen. Dat weegt Chris of Hans dan, niet nu.

## Hoe de app weet of een winkel betaalt (voor Jet)
- **Koppelen via External ID:** bij de afrekening geeft de app de TikTok `shop_id` (of onze eigen winkelsleutel) mee als `external_customer_id`. Daarna is één aanroep genoeg: **Get Customer State by External ID** geeft de actieve abonnementen van die winkel (GEZIEN, polar.sh/docs/integrate/customer-state).
- **Bijhouden met één webhook:** `customer.state_changed` komt bij een nieuw of gewijzigd abonnement (zelfde pagina). De Worker slaat per winkel op: betaalt ja of nee, en tot wanneer. Bij twijfel (webhook gemist) vraagt hij de stand op vóór het boeken.
- **Regel voor boeken:** een uitbetaling wordt geboekt als (a) de bestellingen van die maand binnen de gratis grens vallen, of (b) de winkel een abonnement heeft met status `active` of `trialing`. Anders status "Wacht op abonnement" (staat al in het ontwerp, volgorde van Daan: fout > koppeling verlopen > wacht op abonnement > geboekt met apart > geboekt). Bij `past_due` (betaling mislukt, Polar probeert het opnieuw, GEZIEN subscriptions-pagina): nog 7 dagen doorboeken met een amber balk "betaling mislukt, kijk je betaalgegevens na", daarna wachten (GOK, zodat één mislukte incasso de boekhouding niet meteen stillegt).
- **Niets weggooien bij wachten:** uitbetalingen die wachten worden alsnog geboekt zodra het abonnement actief is, met de startdatum die de verkoper koos. Zo verliest niemand een maand door later te betalen.
- **Opzeggen en facturen:** via het Customer Portal van Polar (betaalmethode, facturen, opzeggen, GEZIEN subscriptions-pagina). In de app één link "Abonnement beheren", geen eigen scherm.
- **Testen zonder Thijs:** unittests op voorbeeldantwoorden uit de Polar-docs, zoals Jet bij TikTok en Moneybird deed. De Polar-sandbox (`sandbox-api.polar.sh`, eigen account en token, GEZIEN integrate/sandbox) vraagt een account, dus dat is later een regel op de lijst van Thijs, samen met de Moneybird-sandbox. Nu niet vragen.

## Wat de keuring van TikTok hiervan vraagt (GEZIEN, docv2/page/app-review-process, bijgewerkt 27 okt 2026)
- De reviewer moet de app kunnen testen met **testaccount en teststappen**. De gratis proef en de gratis grens maken dat mogelijk zonder betalen. Voor het betaalde deel: een kortingscode van 100% in Polar voor de reviewer (GOK dat Polar dat kan; Jet checkt het in de docs).
- Bij het ontwerp (ARD) hoort een notitie **waar de gegevens van de verkoper staan en hoe ze verdwijnen als de koppeling stopt**. Voor het betalen: we bewaren alleen shop_id, Polar-klant-id en de stand (betaalt ja of nee, tot wanneer); geen kaartgegevens, die blijven bij Polar.
- Doorlooptijd na de registratie, volgens TikTok zelf: registratie ±5 werkdagen, ontwerp 3 tot 5, test van de app 7 tot 10, listing 7 tot 10 per markt, privacy (DSPR) ±2 weken, juridisch soms 3 weken of meer. Strookt met `registratie.md` (4 tot 8 weken tot live, GOK).

## Nieuw gezien bij dit werk
- **Nederland staat niet in de taaltabel voor listings** (docv2/page/publish-and-list-public-app, bijgewerkt 20 okt 2026): wel FR, DE, IE, IT, ES, VK en andere, geen NL en geen BE. Er staan wel 82 apps in de NL-winkel (Hans, 8 nov). Welke taal NL vraagt, laat het formulier zien; Nederlands én Engels liggen klaar in `registratieteksten.md`. Voor Italië is de listing in het Italiaans verplicht (zelfde pagina): dat komt bij de stap naar Fatture in Cloud.
- De listing vraagt drie **key benefits** (titel tot 50, uitleg tot 150 tekens), een korte beschrijving tot 200 tekens, een lange tot 2.000 (500 aanbevolen, geen emoji, geen getuigenissen), logo 1:1 vanaf 150 px, hoofdplaatje of video 5:3, en een lijst **integrations** (hier: Moneybird). Nog niet in `registratieteksten.md`; toevoegen als naam en prijs vastliggen.

## Open (niet nu)
- Chris: prijs, gratis grens, jaarprijs ja of nee, en de tekst op `dortus.com/klopt/prijs`.
- Thijs, later en gebundeld: Polar-product aanmaken (of de hoofdchat met hem), Polar- en Moneybird-sandbox. Pas als de product-laag en het betaalstuk van Jet staan.
- De naam "Klopt" is werknaam (Daan); de URL `dortus.com/klopt/` volgt de naam.
