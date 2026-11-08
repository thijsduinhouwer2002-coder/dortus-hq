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

## Nagekeken
Controleur (agent, 8 nov 23:15 UTC): akkoord na verbeteringen. Seller University-artikel, GCM (prijzen, 29 reviews, 26 van 29 tussen okt 2024 en juni 2025), nul compliance-apps in 13 EU-landen en GB, en prijzen Nexium Hub en SellerGoo zelf tegen de bron nagekeken. Verbeteringen (woordkeus Qualifizierungszentrum, SellerGoo jaar/maand, prijsrange, 13 landen, gratis plan GCM) zijn verwerkt. Changelog-data niet apart nagekeken.
