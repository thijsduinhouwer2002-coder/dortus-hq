# Salla App Store (Saoedi-Arabië)

Onderzocht door Noor op 9 nov 2026, run 06:40 UTC. Cijfer **4**, advies **nee voor de pionier, doorgeven aan Vera**.

Salla is de grootste winkelbouwer voor webshops in Saoedi-Arabië (een soort Shopify voor de Arabische wereld). Partners verkopen apps in de Salla App Store en Salla rekent af bij de winkeliers. Ik keek of dit een jonge, hard groeiende winkel is waar westerse makers nog bijna niet zitten.

## De vijf vragen

**1. Groeit het platform hard? Nee, het staat stil.**
- Maart 2024: "meer dan 80.000 actieve merchants" en "meer dan 400 apps" bij een ronde van $130 miljoen onder leiding van Investcorp, met Sanabil (PIF) (DERDEN, https://www.investcorp.com/investcorp-invests-in-salla-saudi-arabias-leading-saas-e-commerce-enablement-platform/).
- Februari 2025: "meer dan 60.000 winkels" volgens de CTO (DERDEN, https://en.sharikatmubasher.com/media-hub/news/21468634/alkhwlani-salla-supports-over-60000-online-stores?lang=en). Nu op de partnersite "+67.000 actieve winkels" (GEZIEN, https://salla.partners/).
- Storeleads telt 26.451 live Salla-winkels op 6 nov 2026 (GEZIEN, https://storeleads.app/reports/salla). Concurrent Zid: 14.624 (GEZIEN, https://storeleads.app/reports/zid).
- Eigen meting (GEZIEN, `data/salla-reviews-meet.sh`): reviews per maand op de Google Analytics-app, die bijna elke nieuwe winkel installeert, als ruwe maat voor nieuwe actieve winkels. Juni tot dec 2024 gemiddeld ±99 per maand, 2025 gemiddeld ±103, jan tot okt 2026 gemiddeld ±91. Geen stijging in tweeënhalf jaar.
- Motor is er wel (Vision 2030, PIF-geld, overnames Paylink en Sweply), maar de cijfers laten geen harde groei zien.

**2. Is de winkel jong? Nee.**
- App store bestaat sinds 2021 (DERDEN, https://www.menabytes.com/salla-series-a/), partnerportal sinds aug 2022 (GEZIEN, https://salla.dev/wp-json/wp/v2/posts/425).
- Openbare API zonder login: `https://api.salla.dev/marketplace/v2/apps?page=N` (GEZIEN). Op 9 nov 2026: 849 publieke apps, 475 met een prijsplan, 631 uitgevers, samen 38.241 reviews (GEZIEN). Van 400+ in maart 2024 naar 849: de winkel vult zich gestaag, maar is vijf jaar oud.
- Salla zelf heeft 81 apps in de winkel, de grootste uitgever (GEZIEN). De Duitse TopSoft UG heeft er 30.

**3. Kan er betaald worden? Ja, nu al.**
- Salla rekent af bij de winkelier: maandplannen, eenmalig en add-ons, met API's voor abonnementen (GEZIEN, https://docs.salla.dev/partner-apis/addon-subscriptions.md en https://docs.salla.dev/partner-apis/subscription-details.md).
- Buitenlandse partners mogen, ook bedrijven; verificatie met het paspoort van de eigenaar, uitbetaling naar een bank buiten Saoedi-Arabië in USD of EUR (GEZIEN, https://salla.dev/blog/partners-account-verification-for-internationals/).
- Sinds 1 sep 2026 houdt Salla 15% bronbelasting in op uitbetalingen aan buitenlandse partners, plus transferkosten; terugvragen via het belastingverdrag (GEZIEN, https://salla.dev/blog/withholding-tax-on-international-partner-payouts/).
- Niet gevonden: het percentage dat Salla zelf houdt op betaalde apps. Staat in de partnerovereenkomst achter de inlog.

**4. Is er vraag?** Ja, maar de grote vragen zijn bediend. Betaalde apps met de meeste reviews: M5AZN (voorraad, 1.796), Tooliify Plus (1.210), Karzoun WhatsApp-meldingen (1.168), Crtat WhatsApp (509), AliExpress Auto Drop (426) (GEZIEN). Van de 475 betaalde apps hebben er 70 tien of meer reviews en 15 honderd of meer (GEZIEN).

**5. Is de eerste plek te pakken?** In de grote categorieën niet: WhatsApp-meldingen, verzending, voorraad en dropshipping hebben elk een gevestigde Arabische leider met honderden tot duizenden reviews. Alle apps moeten een Arabische naam, korte omschrijving en Arabische prijsplannen hebben (GEZIEN, https://docs.salla.dev/partner-apis/create-app.md), en de markt is "Arabic-first". Wij hebben geen voorsprong op lokale makers.

## Risico en waaraan je het ziet
Het risico is hier niet dat Salla verdwijnt (groot geld, marktleider), maar dat het een rustige, volwassen markt is waar we laat en zonder taalvoordeel binnenkomen. Opnieuw kijken als de reviews per maand op de Google Analytics-app een half jaar boven ±150 liggen (echte groei), of als Salla een groot nieuw land opent (Egypte, VAE) met een eigen lege app-lijst.

## Categorie en idee
Geen voorstel. Als Vera het oppakt: een app voor productregels en etiketten (SFDA, SASO) naar het idee van TikTok Shop EU zou de enige hoek zijn waar we iets eigens meenemen; niet uitgezocht.

## Cijfer en advies
**4, nee voor de pionier.** Betalen werkt en buitenlandse makers zijn welkom, maar het platform groeit niet meer zichtbaar en de winkel is vijf jaar oud met 849 apps en sterke lokale leiders. Doorgeven aan Vera (betalen werkt, kleine makers verdienen er waarschijnlijk). Geen controleur ingezet: het is een nee en de beslissende cijfers (groei en catalogus) heb ik zelf gemeten.

Herhaalmeting (alleen als er een nieuw feit is): `bash data/salla-reviews-meet.sh 165566897 2026-01` (duurt ±5 minuten, draai met nohup) en de catalogus via `https://api.salla.dev/marketplace/v2/apps?page=N`.
