# Voorstel: Omi app store (Based Hardware)

Noor, pionier, 9 nov 2026. Cijfer **3**, advies **nee**.

## Wat is het
Omi is een open-source AI-ketting (en app op telefoon en Mac) die gesprekken opneemt en samenvat. In de Omi-app zit een app store waar makers apps zetten: samenvattingen, chat-assistenten, meldingen tijdens een gesprek en koppelingen (Notion, Google Drive, Zapier). Makers kunnen een maandprijs vragen.

## De vijf vragen

**1. Groeit het platform hard en zichtbaar? Nee, er is geen bewijs, wel tekenen van stilstand.**
- iPhone-app "Omi - Smart Meeting Notes": 145 beoordelingen in de VS, 4 in het VK, 5 in Duitsland, 10 in India, na 2,5 jaar (sinds 27 mei 2024) (GEZIEN, https://itunes.apple.com/lookup?id=6502156163&country=us).
- Android-app (com.friend.ios): 10K+ downloads (GEZIEN, https://play.google.com/store/apps/details?id=com.friend.ios).
- Een claim van $10 mln omzet per jaar op arr.club kon ik niet lezen (pagina leeg via curl) (DERDEN, niet bevestigd, https://www.arr.club/omi/omi-crossed-10m-annualized-run-rate).
- Het nieuwsblog van Omi bestaat uit herhaalde SEO-stukken, geen cijfers (GEZIEN, https://www.omi.me/blogs/news.atom).
- Motor: open source, actieve ontwikkeling (betaalcode met Stripe Connect en PayPal in de backend), Product Hunt-moment in sept 2026 (DERDEN, https://aitoolly.com/ai-news/article/2026-09-04-omi-the-emergence-of-an-open-source-ai-necklace-and-personal-companion-on-product-hunt). Maar geen enkel gemeten groeicijfer.

**2. Is de app-winkel jong? Ja, maar de instroom is ingestort.**
Zelf geteld via de open API (GEZIEN, https://api.omi.me/v1/approved-apps, bestand `data/omi-apps-2026-11-09.json`): 593 goedgekeurde apps, 91 zonder datum. Nieuw per maand:
2024-11 61, 2024-12 28, 2025-01 10, 2025-02 14, 2025-03 10, 2025-04 44, 2025-05 18, 2025-06 17, 2025-07 17, 2025-08 24, 2025-09 7, 2025-10 23, 2025-11 10, **2025-12 78, 2026-01 99**, 2026-02 16, 2026-03 7, 2026-04 15, **2026-05 1, 2026-06 1, 2026-07 2**, aug tot nov 0.
Sinds mei 2026 komen er bijna geen apps meer bij. Of makers afhaken of Omi niet meer goedkeurt, is van buitenaf niet te zien; beide zijn slecht nieuws voor een pionier.

**3. Kan er betaald worden? Ja, nu al, en Omi houdt niets.**
- Makers zetten een maandprijs; Omi maakt een Stripe-betaallink met `transfer_data.destination` naar het Stripe Connect-account van de maker, zonder application fee (GEZIEN, broncode https://raw.githubusercontent.com/BasedHardware/omi/main/backend/utils/stripe.py, functie create_app_payment_link). Een betaalde app werkt pas na betaling (GEZIEN, backend/routers/apps.py, "This app requires a paid subscription").
- 43 betaalde apps, prijzen $0,10 tot $50 per maand (GEZIEN, API).
- Maar ze verkopen niet: alleen 4 betaalde apps hebben 10 of meer installs (550, 150, 147, 90), alle vier uit nov 2024 of zonder datum. De 39 andere hebben 0 tot 8 installs (GEZIEN). Installs is niet hetzelfde als betalende klanten; het echte aantal kopers is dus nog lager.

**4. Is er vraag te zien? Zwak.**
Installs totaal 143.733 over alle apps samen, waarvan 45.955 voor de officiële Google Drive-koppeling (GEZIEN). Mediaan installs per app: jaargang 2024 84, 2025 25, 2026 6 (GEZIEN). Een nieuwe app haalt dus vrijwel niemand. Forums en Discord niet gelezen (geen tijd nodig: de cijfers hierboven beslissen al).

**5. Is de eerste plek in een categorie te pakken? Ja, maar die is weinig waard.**
De grootste categorieën (gespreksanalyse 157 apps, productiviteit 103) hebben zwakke leiders van een paar duizend installs over twee jaar, en de koppelingen doet Omi zelf (Google Drive, Notion, General Summary). Eerste worden kan, maar in een winkel waar een nieuwe app mediaan 6 installs haalt, levert dat bijna niets op.

## Risico
Het grootste risico is al zichtbaar: de winkel staat sinds mei 2026 bijna stil en de telefoon-apps zijn klein. Teken dat het toch gaat lopen: de instroom komt terug boven 30 per maand, of Omi meldt verkoopcijfers van de ketting (100.000+).

## Categorie en eerste productidee (alleen als het keert)
Vergaderverslag met actiepunten naar een takenlijst (Todoist, Linear), want productiviteit is de grootste betaalde hoek en de enige betaalde app met omzet-achtige installs is een takenapp (Task Flow, $10 per maand, 147 installs).

## Cijfer en advies
**3, nee.** Betalen werkt nu al en Omi houdt 0%, precies wat Thijs vraagt, maar vraag 1 en 2 (die het zwaarst wegen) zijn negatief: geen bewijs van groei, kleine apps in de winkels van Apple en Google, en een app-instroom die van 99 in januari naar 0 tot 2 per maand zakte. Een lege winkel die stilstaat is geen pionierskans.

Herhaalmeting rond 9 feb 2027: `python3 -I data/omi-apps-meet.py data/omi-apps-2027-02-09.json`.
