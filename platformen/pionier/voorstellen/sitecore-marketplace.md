# Sitecore Marketplace (apps voor SitecoreAI)

Noor, 9 nov 2026, run 10:40 UTC. Nagekeken door een controleur (agent, 9 nov ±11:00 UTC): punten 1 tot 6 kloppen, zie onder.

**Cijfer: 4. Advies: nee voor de pionier.** Ook niet voor Vera: er is geen enkel bewijs dat er iemand verdient.

## Wat het is
Sitecore is een oude, dure CMS voor grote bedrijven (licenties van tienduizenden euro's per jaar). Het nieuwe SaaS-product heet SitecoreAI (eerder XM Cloud). Oude uitbreidingen (modules, config-patches) werken daar niet meer, daarom kwam er een Marketplace: apps in het Next.js/TypeScript-stijl die je zelf host en die via de Marketplace SDK in de Sitecore-schermen verschijnen. Eigen apps per klant sinds 14 aug 2025, publieke apps voor alle klanten sinds 10 nov 2025 (GEZIEN, https://developers.sitecore.com/changelog/marketplace/10112025/share-your-solutions-with-the-sitecore-community-through-public-marketplace-apps). Sinds 5 nov 2026 een openbare lijst met app-ideeën van klanten met stemmen, en analytics voor makers.

## De vijf vragen

**1. Groeit het platform hard? Nee.**
- De grote Next.js-pakketten van Sitecore samen: okt 2025 180.697, okt 2026 187.686 downloads per maand (GEZIEN, npm: @sitecore-jss/sitecore-jss-nextjs plus @sitecore-content-sdk/nextjs). Daartussen een bult in juni en juli 2026 (±324.000 en ±379.000, controleur), maar per oktober gelijk. Het oude pakket zakt, het nieuwe vervangt het: dat is een overstap binnen dezelfde klanten, geen groei.
- Vragen op sitecore.stackexchange.com: 1e helft 2024 424, 1e helft 2025 240, 2e helft 2025 171, 1e helft 2026 88 (GEZIEN, api.stackexchange.com). Stack Exchange zakt overal, maar dit is ruim een halvering per jaar.
- Sitecore zelf noemde in juli 2025 "hundreds of global brands" op XM Cloud (DERDEN, https://www.sitecore.com/company/newsroom/press-releases/2025/07/sitecore-puts-marketers-in-control-with-xm-cloud-sandbox-access). Het aantal kopers is dus honderden tot een paar duizend bedrijven, geen massa.
- Motor: de gedwongen overstap van Sitecore XP naar SitecoreAI. Dat lijkt op Craft 6 (nieuw raamwerk, oude plugins werken niet), maar de markt eromheen krimpt.

**2. Is de winkel jong? Ja.**
- Publieke apps sinds 10 nov 2025, dus precies een jaar.
- SDK-gebruik stijgt: @sitecore-marketplace-sdk/client 2.590 downloads in okt 2025 naar 7.656 in okt 2026, piek 16.067 in juni 2026 (GEZIEN, npm; controleur: klopt).
- Aantal publieke apps: niet te meten. De lijst op https://portal.sitecorecloud.io/marketplace laadt pas na inloggen (GEZIEN). Op GitHub staan 55 repo's met de SDK in package.json, waarvan 8 van Sitecore en 3 van de hackathon; de rest zijn losse makers, vooral Sitecore-MVP's van bureaus, met gratis open-source apps (GEZIEN, gh search/code).
- Sinds 7 okt 2026 bouwt Sitecore eigen "default apps" voor "common product and feature gaps", die het zelf automatisch kan installeren (GEZIEN, changelog en https://doc.sitecore.com/mp/en/developers/marketplace/default-marketplace-apps.md). Juist de lege hoeken pakt Sitecore dus zelf.

**3. Kan er betaald worden? Ja, met eigen kassa.**
- Bij indienen kies je "Financial model": Free, Freemium of Paid (GEZIEN, https://doc.sitecore.com/mp/en/developers/marketplace/finish-configuration-and-submit-a-public-app-for-approval.md). Sitecore rekent niet af en noemt geen percentage; er is een instelling voor pop-ups "for login and payment flows" (controleur). De maker int dus zelf.
- Geen enkele betaalde app met prijs gevonden, ook niet door de controleur (niet te controleren zonder inlog).
- Kosten en drempel: om te bouwen en te testen heb je een Sitecore Cloud Portal-organisatie nodig met SitecoreAI. Er is sinds juli 2025 een gratis proefversie (DERDEN, persbericht hierboven), hoe lang die loopt is niet gevonden (GOK: 30 tot 60 dagen). Daarna is er een klant- of partneraccount nodig. Elke publieke app krijgt een technische, ontwerp-, beveiligings- en zakelijke keuring en moet een beveiligingslijst halen. Verkopen aan grote bedrijven betekent inkoop, beveiligingsvragenlijsten en contracten.

**4. Is er vraag te zien? Een beetje, maar niet te lezen.**
- De ideeënlijst met stemmen bestaat sinds 5 nov 2026, maar staat achter de inlog (GEZIEN, https://doc.sitecore.com/mp/en/developers/marketplace/submit-ideas-for-new-marketplace-apps.html).
- Sitecore noemt zelf als gewenste apps: AI alt-teksten en tags, contentoverdracht tussen omgevingen, vertalen, web-analytics, websitesnelheid, SEO, eigen veldtypes zoals kleurkiezer en iconen (GEZIEN, https://doc.sitecore.com/mp/en/developers/marketplace/introduction-to-the-sitecore-marketplace.md). Voor bijna al die soorten staat al een gratis repo op GitHub (content-transfer, Optima-SEO, pageSpeed, icon-picker van Sitecore zelf, image_crop, Content-Export).
- Op Stack Exchange 9 vragen over de Marketplace sinds okt 2025 (GEZIEN). Weinig.

**5. Is de eerste plek te pakken? Moeilijk te zeggen, en weinig waard.**
De ruimte wordt gevuld door bureaus die gratis apps maken als visitekaartje voor hun diensten, en door Sitecore zelf met default apps. Een kleine maker zonder Sitecore-klanten, zonder testomgeving na de proef en zonder naam in de Sitecore-wereld wint daar geen nummer één. De kopers betalen wel veel, maar verkopen aan hen kost een verkoopgesprek, geen klik.

## Risico
Sitecore verliest terrein aan nieuwe headless-CMS'en (Contentful, Storyblok, Sanity, Payload). Teken dat het erger wordt: SDK-downloads zakken terug onder de 5.000 per maand, of nog minder Stack Exchange-vragen. Teken van een kans: Sitecore gaat zelf afrekenen in de Marketplace, of noemt openbaar het aantal apps en installaties.

## Productidee (als het ooit wel kan)
Een vertaal- en lokalisatie-app voor SitecoreAI (AI-vertaling met goedkeuringsstap per taal), freemium met een jaarlicentie per organisatie. Niet bouwen nu.

## Waarom geen 5 of hoger
Vraag 1 faalt: het platform groeit niet, alleen de nieuwe laag binnen een krimpende of vlakke klantenkring. De rol zegt: een platform dat niet groeit is geen pionierskans, hoe leeg ook. Daarbij geen bewijs van een betaalde app, geen meetbare winkel en een drempel (Sitecore-omgeving, keuring, verkoop aan grote bedrijven) die niet bij Dortus past.

## Herhaalmeting
Niet nodig. Alleen opnieuw kijken als Sitecore zelf gaat afrekenen of aantallen noemt. Snelle meting kan altijd: npm `@sitecore-marketplace-sdk/client` per maand.
