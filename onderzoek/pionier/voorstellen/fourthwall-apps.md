# Fourthwall Apps (Developer Platform)

Onderzocht door Noor op 9 nov 2026, run 06:40 UTC. Cijfer **5**, advies **nog niet klaar**.

Fourthwall is een winkelbouwer voor creators (YouTubers, streamers, podcasters): merch, digitale producten, memberships. Sinds kort kan elke creator een app bouwen (OAuth, een instellingenpagina in het dashboard, installeerbare secties in de site-editor) en die laten opnemen in de Apps-directory.

## De vijf vragen

**1. Groeit het platform? Ja, stevig maar niet explosief.**
- Live winkels volgens Storeleads: 4.502 (Q4 2023), 11.767 (Q4 2024), 17.421 (Q4 2025), 23.613 (Q3 2026), nu 25.732 (GEZIEN, https://storeleads.app/reports/fourthwall; de 25.732 zelf gelezen, de reeks via de hulpagent). Dat is ±+45% per jaar, Q3 2026 +9% op Q2.
- Geld: $17M in nov 2021 (Lightspeed, Initialized, Seven Seven Six), totaal "over $25 million" na een ronde met Jellysmack in mei 2023 (DERDEN, https://tubefilter.com/2023/05/10/jellysmack-investment-fourthwall/). Geen nieuwere ronde gevonden. De homepage noemt "over 500,000 creators" en elders "over 200,000"; marketing, niet te gebruiken.
- Motor: de creator-economie en de koppelingen met YouTube Shopping en TikTok Shop (GEZIEN, sitemap fourthwall.com).

**2. Is de winkel jong? Ja, bijna leeg.**
- Publiceren gaat nog met de hand: "We're still developing an app publishing process. For now, you can submit your app for review by contacting us on Discord" (GEZIEN, https://docs.fourthwall.com/apps/publishing.md).
- Echobrain (productreviews) heet in de help-center "the first third-party app available on Fourthwall" (GEZIEN via de hulpagent, https://help.fourthwall.com/manage-my-shop/apps-features-and-integrations/echobrain-product-reviews-app.md, bijgewerkt 26 okt 2026). Verder ±25 integraties, allemaal van Fourthwall zelf of grote merken (Klaviyo, beehiiv, StreamElements, TikTok Shop, YouTube) (GEZIEN, https://help.fourthwall.com/llms.txt en sitemap).
- De directory zit achter de inlog; geen openbare lijst of API, dus aantallen apps en installs zijn niet te tellen (GEZIEN: fourthwall.com/apps geeft 404).

**3. Kan er betaald worden? Ja, met een eigen kassa.**
- "Monetization for third-party apps is not managed through Fourthwall. If you want to charge for your app, you handle billing and access control independently" (GEZIEN, https://help.fourthwall.com/manage-my-shop/apps-features-and-integrations/developer-platform-building-apps-and-webhooks.md, bijgewerkt 30 okt 2026). Echobrain heeft eigen prijzen. Geen plan gevonden voor afrekenen via Fourthwall.
- Kosten: geen afdracht aan Fourthwall; wel een eigen kassa (bijvoorbeeld Lemon Squeezy of Paddle) en de drempel dat de creator buiten Fourthwall moet betalen.

**4. Is er vraag?** Niet te meten. Geen openbaar feedbackbord (wensen gaan via mail, Discord en een chatbot), Discord niet zonder inlog te lezen, geen bruikbare Reddit-draden gevonden. Eén aanwijzing: ingebouwde reviews werken alleen voor catalogusproducten, daarvoor verwijst Fourthwall naar Echobrain (GEZIEN, llms.txt). Typische Shopify-apps (upsell, loyaliteit, pop-ups, wishlist) zijn nergens te zien (GOK dat er vraag is).

**5. Is de eerste plek te pakken?** Ja, in bijna elke categorie: er is maar één zelfstandige app (reviews). Maar Fourthwall bouwt zelf hard (Channel API, streaming alerts en gifting, bundels, MCP-server en een ChatGPT- en Claude-app in 2026; GEZIEN, https://docs.fourthwall.com/guides/changelog.md) en is een alles-in-één-platform, dus een goede app-categorie kan zomaar een ingebouwde functie worden. Via de eigen MCP kunnen creators ook zelf kleine dingen laten bouwen.

## Risico en waaraan je het ziet
Fourthwall zelf lijkt gezond, maar klein: 25.732 live winkels, veel daarvan kleine creators met weinig omzet en een kleine portemonnee voor apps. Het grootste risico is dat de directory een bijzaak blijft (handwerk via Discord, achter de inlog, betalen buiten het platform) en dat Fourthwall de goede ideeën zelf inbouwt. Teken van stokken: over drie maanden nog steeds publiceren via Discord en geen tweede zelfstandige app. Teken van doorbraak: een echt publicatieproces, een openbare directory of afrekenen via Fourthwall.

## Categorie en eerste idee (GOK, niet getoetst)
Een app voor supporters die meer kopen: beloningen en loyaliteit voor fans (punten per aankoop, kortingen voor leden), gekoppeld aan memberships. Past bij creators, staat niet in de lijst van Fourthwall. Eerst nagaan of Fourthwall dit zelf al half heeft (memberships hebben eigen voordelen).

## Cijfer en advies
**5, nog niet klaar.** Jong, bijna leeg en betalen kan nu al met een eigen kassa, maar het bereik is klein, de vraag is niet te meten, en de directory is nog handwerk zonder installcijfers. Geen voorstel voor een manager nu. Opnieuw wegen (dan 6 of hoger) als Fourthwall een echt publicatieproces of een openbare directory opent, of als winkels boven 35.000 live komen. Geen controleur ingezet: geen ja, en de drie beslissende feiten (publiceren via Discord, eigen kassa, aantal winkels) heb ik zelf gelezen.

Herhaalmeting rond 9 feb 2027: Storeleads-teller (https://storeleads.app/reports/fourthwall), https://docs.fourthwall.com/apps/publishing.md (nog Discord?), en `grep -i third-party` in https://help.fourthwall.com/llms.txt.
