# TikTok Shop: productkeuze

Tess, 8 nov 2026, run 23:05 UTC. Onderzoek: `onderzoek/2026-11-08-betaalbewijs-gpsr-apps.md` en `onderzoek/2026-11-08-vraag-tiktok-verkopers.md`.

## Uitkomst: nog geen keuze

Het bewijs dat verkopers voor "EU-proof" (idee A) betalen is te dun, en de tweede kans (winstanalyse, idee B) is al vol. Volgens de taak kies ik dan niet. Er wordt niets gebouwd en Hans krijgt geen bouwvoorstel.

## Idee A: EU-proof (Europese verplichte velden): nee in deze vorm

Wat ervoor pleit:
- Het gat in de winkel is echt: in de 260 apps van de 13 EU-landen in onze data en de 253 Britse apps staat geen enkele app voor GPSR, Responsible Person, CLP of EPR (GEZIEN, `platformen/pionier/data/tiktokshop-apps-*-2026-11-08.json`, twee keer los van elkaar gezocht).
- De regels worden steeds strenger: Responsible Person verplicht vanaf 28 feb 2026 met deactivering na 28 maart 2026, Dangerous Goods voor UK en EU vanaf 22 sep 2026 (GEZIEN, https://partner.tiktokshop.com/docv2/changelog).
- Op Shopify betalen winkels voor zoiets: GCM GPSR gratis plan, $15 en $29 per maand, 29 reviews, cijfer 4,9 (GEZIEN, https://apps.shopify.com/gpsr).

Wat ertegen pleit (zwaarder):
- **TikTok doet de kern zelf, gratis.** In Seller Center beheer je fabrikant en Responsible Person per winkel op één plek ("Qualifizierungszentrum") en vul je verplichte velden in bulk via Excel-sjablonen, één sjabloon per categorie (GEZIEN, https://seller-de.tiktok.com/university/essay?knowledge_id=2495034554238752&default_language=de-DE). Het artikel zegt niet of die gegevens vanzelf aan alle producten hangen of in het Excel-sjabloon zitten, maar onze kernbelofte "in bulk invullen vanuit één profiel" bestaat dus grotendeels al.
- **De koppelsoftware doet de rest:** M2E (vanaf $49 per maand op Shopify, GEZIEN), Lengow, Channable, ChannelEngine nemen de GPSR-velden voor TikTok al mee (DERDEN, hulppagina's met links in het onderzoek).
- **De pijn is nauwelijks zichtbaar:** één klacht van een TikTok-verkoper gevonden (Shopify Community, 19 maart 2026, 2 berichten, 159 keer bekeken, GEZIEN, https://community.shopify.com/t/official-tiktok-shop-shopify-integration-is-extremely-limited-for-real-eu-catalog-management/592651). Geen golf op fora (Reddit niet te lezen; telt als niet gevonden).
- **De betaalgolf op Shopify is voorbij:** GCM kreeg 26 van zijn 29 reviews tussen oktober 2024 en juni 2025, daarna 3 in anderhalf jaar (GEZIEN). In 2026 kwamen er minstens 60 nieuwe GPSR-apps bij op Shopify, bijna allemaal met 0 reviews (GEZIEN). GPSR wordt steeds vaker gratis meegeleverd (Complimus, Germanized met 70.000 installs, GEZIEN). Gangbare prijs voor alleen GPSR: gratis tot $15 per maand (GEZIEN), dus onder onze ondergrens van €15.

## Idee B: winstanalyse: nee

- 11 EU-apps doen winst per bestelling, waarvan 8 nieuw in 2026 (GEZIEN, zelfde data). Prijzen op hun eigen sites meestal €29 tot €99 per maand, Kixmon tot $249 (GEZIEN: Nexium Hub €49/€99, SellerGoo €29/€39/€59 bij jaarbetaling en €39/€49/€69 per maand los, Kixmon $16 tot $249, ZonWizard €70).
- Dat is wel betaalbewijs (prijzen, geen klantenaantallen), maar een nieuwkomer valt daar niet meer op en we hebben geen "waarom wij" die beter is dan Nexium Hub of SellerGoo. Besluit van Noor (8 nov 19:50) blijft staan.

## Wat er nog kan (niet gekozen, alleen een richting)

Een smallere versie van A: "zie welke listings TikTok binnenkort deactiveert en los het in één keer op", gedreven door elke nieuwe regel (Dangerous Goods, CLP). Dat is nu een GOK: er is geen gemeten vraag en de prijs zou rond gratis tot $10 liggen. Ik neem het pas op als er nieuw bewijs komt (veel deactiveringen of klachten na een nieuwe regel).

## Volgende stap

Breder zoeken in plaats van één idee forceren: welke categorieën in de VS-winkel hebben veel apps met een vaste maandprijs, en zijn in de EU leeg of bijna leeg? Uit de data van Noor (GEZIEN): creator-samenwerking NL 6 tegen VS 82 (VS-mediaan $149), video shopping NL 3 tegen 36, reviews NL 1 tegen 14 (mediaan $49), klantenservice (mediaan $89). Per categorie meten: EU-aantal per land, aanmaakdatum (groei), prijzen, en of TikTok het zelf al gratis doet. Zie `taken.md`.

## Tussenstand bredere zoektocht (8 nov 23:30 UTC, nog geen keuze)

Onderzoek: `onderzoek/2026-11-08-categorieen-vs-eu.md` (nagekeken, correcties onderaan verwerkt). Per categorie betaalde VS-apps tegen EU-apps (GEZIEN, data 8 nov):
- **Reviews** (VS 10 betaald, EU 2): valt af. Alle apps zetten reviews van een bestaand reviewplatform over (Judge.me, Yotpo); de klant betaalt voor dat platform. Wij hebben geen reviews om over te zetten.
- **LIVE Shopping** (VS 5 betaald, EU en GB 0): echt leeg, maar in de VS een kleine nis (geen LIVE-app in de top 60) en vraag in de EU niet gemeten.
- **Boekhoudkoppeling per land** (VS 18 betaald, mediaan $27; EU 10, vooral Duitse DATEV-exporten): geen enkele listing noemt Moneybird, Exact, e-Boekhouden, SnelStart, Pennylane of Holded (GEZIEN). Betaalbewijs redelijk voor de VS, dun voor NL: op Shopify halen de Moneybird-koppelingen 30 en 7 reviews ($18 tot $36, en $15,95) (GEZIEN). Prijs dicht bij onze ondergrens. Open voorwaarde: geeft TikTok in de EU een API voor uitbetalingen en kosten?
- **Creator-samenwerking** is in de EU niet leeg: 17 apps, 13 nieuw in 2026 (GEZIEN).

Meting 1 en 2 gedaan (23:30, `onderzoek/2026-11-08-finance-api.md`): de Finance-API bestaat (statements, transacties per bestelling met commissie en kosten), de scope "Finance Information" staat op Public en er is een eigen app-categorie Finance > Accounting met een gids voor precies deze koppeling (GEZIEN, zelf nagekeken). Seller Center geeft zelf PDF-facturen voor de TikTok-kosten met een Excel per bestelling en een export van uitbetalingen (GEZIEN, Seller University), maar geen koppeling met een boekhoudpakket (niet gevonden). Moneybird en Exact Online hebben een open API (GEZIEN). Open: btw op de verkoop zit niet als veld in de API voor lokale EU-winkels, NL staat niet in de regiotabel van de docs (taalcodes, GOK dat NL gewoon werkt).
Meting NL-vraag (23:35, `onderzoek/2026-11-08-nl-boekhoudkoppelingen.md`, zelf steekproef nagekeken): NL-verkopers betalen voor marktplaats naar boekhouding. Webwinkelfacturen (Bol naar Moneybird, Exact, e-Boekhouden, €80 tot €180 per jaar, claimt duizenden klanten), iWebDevelopment (Bol en Amazon naar Exact, €12 tot €29 per maand) en xCore (€29 per maand plus €250 installatie) staan in de officiële overzichten van Moneybird en Exact (GEZIEN). Klantaantallen niet zichtbaar. Twee remmen: de gangbare prijs voor Moneybird en e-Boekhouden is €7 tot €15 per maand, onder onze ondergrens; en Schakel (schakel.app, €0 tot €30 per maand) heeft al een pagina "TikTok Shop naar Moneybird" (GEZIEN, waarschijnlijk nog een aanvraagpagina, GOK). Link My Books en A2X doen TikTok Shop al, maar alleen naar Xero, QuickBooks en NetSuite (GEZIEN).
Stand boekhoudkoppeling: betaalbewijs in NL redelijk, prijs laag, markt TikTok Shop NL nog klein en jong. Nog geen keuze; als het deze kant op gaat, dan alle negen landen tegelijk (DATEV is in DE al bezet, FR Pennylane en ES Holded zijn leeg) of samen met een hogere waarde (btw per land uitrekenen, wat de API niet geeft).
Volgende metingen voor een keuze: (3) LIVE-verkoop in de EU: veilingen, aantallen sessies, wat er na de uitzending misgaat; (4) verkopers per land voor NL en FR. Kiezen pas met gemeten betaalbewijs en een "waarom wij".

## Nagekeken
Controleur (agent, 8 nov 23:15 UTC): akkoord na verbeteringen. Seller University-artikel, GCM (prijzen, 29 reviews, 26 van 29 tussen okt 2024 en juni 2025), nul compliance-apps in 13 EU-landen en GB, en prijzen Nexium Hub en SellerGoo zelf tegen de bron nagekeken. Verbeteringen (woordkeus Qualifizierungszentrum, SellerGoo jaar/maand, prijsrange, 13 landen, gratis plan GCM) zijn verwerkt. Changelog-data niet apart nagekeken.

## Uitkomst bredere zoektocht (9 nov 2026, run 02:03 UTC): voorstel boekhoudkoppeling aan Hans

Twee nieuwe metingen, allebei nagekeken door een controleur (correcties onderaan de stukken verwerkt):
- **LIVE-hulpmiddelen valt af** (`onderzoek/2026-11-09-live-verkoop-eu.md`). LIVE is 17,2% van de omzet in DE, FR, ES en IT (DERDEN, Kalodata via Lengow) en TikTok doet het werk na de veiling niet helemaal zelf, maar veilingen zijn alleen bevestigd in VS en VK, en in de EU is er één betaalde app voor het werk na de veiling (DARITAI in ES, €119 per maand, geen klanten zichtbaar) (GEZIEN). Betaalbewijs bijna nul. Opnieuw bekijken als TikTok veilingen in DE, FR of NL aanzet.
- **Boekhoudkoppeling: FR en IT leeg én betaald** (`onderzoek/2026-11-09-boekhouding-fr-es-it.md`). Geen TikTok-koppeling naar Pennylane, Holded of Fatture in Cloud; Link My Books ondersteunt TikTok EU nog niet; in FR verkoopt Order Invoicer zulke koppelingen voor andere marktplaatsen (€12 tot €299 per maand, 450+ klanten volgens eigen zeggen), in IT hebben Shopify-koppelingen naar Fatture in Cloud 24 en 25 reviews (GEZIEN). ES valt af (Holded doet Amazon zelf gratis, weinig bewijs).

**Keuze:** boekhoudkoppeling voor NL (Moneybird, Exact), FR (Pennylane) en IT (Fatture in Cloud) als eerste product. Waarom: in drie landen gemeten betaalbewijs voor marktplaats naar lokaal pakket, het gat in de TikTok-winkel is GEZIEN, de API bestaat, en de "waarom wij" is helder (lokaal pakket, in de App Store). Zwakke punten: prijs dicht bij €15, de gratis Excel-export van TikTok, Schakel (NL) en mogelijk Order Invoicer en Link My Books. Voorstel voor Hans: `voorstel-boekhoudkoppeling.md` (nagekeken, 14 verbeteringen verwerkt). Er wordt niets gebouwd voor zijn ja en een ontwerp dat Daan keurde.
