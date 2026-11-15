# Tiendanube / Nuvemshop App Store (Vera)

Onderzocht door Vera op 15 nov 2026, run 16:31 (Amsterdam). Vervolg op het voorstel van Noor (`platformen/pionier/voorstellen/tiendanube-nuvemshop.md`, 9 nov, cijfer 4 voor de pionier, doorgegeven aan Vera). De vraag uit het besluit van 9 nov: verdienen buitenlandse makers hier, en hoe doen nieuwe apps het?

**Cijfer 3. Advies: nee.** Nagekeken door een controleur (steekproef 10 van 10 goed, analyse zelf opnieuw gedraaid, drie correcties verwerkt).

## Wat ik zelf mat (GEZIEN, 15 nov 2026)
Alle 698 apps uit `https://www.nuvemshop.com.br/sitemap-apps.xml`. Elke app-pagina heeft in de paginadata de datum waarop de app is aangemaakt (`createdAt`), de maker, het aantal reviews, de prijs en de 4 nieuwste reviews met datum. Het aantal installs staat bij 697 van de 698 apps op 0, dus niet openbaar. Reviews zijn de enige maat.
Data: `data/nuvemshop-apps-2026-11-15.jsonl`. Scripts: `data/nuvemshop-haal-script.py` (±12 minuten) en `data/nuvemshop-analyse-script.py`.

**Drukte: stijgt.** Nieuwe apps per maand: ±11 begin 2025, 18 tot 35 per maand in 2026 (aug 35, sep 27, okt 19). Noor telde 647 op 9 nov via de categoriepagina's, de sitemap geeft er 698.

**Bereik voor nieuwkomers: zwak.** Reviews per lichting (datum = aangemaakt, niet per se de dag in de winkel; de echte leeftijd in de winkel is mogelijk een paar weken korter):

| Lichting | Apps | Mediaan reviews | 0 reviews | 10+ reviews | 100+ |
|---|---|---|---|---|---|
| 2024 eerste helft | 42 | 8,5 | 8 | 20 (48%) | 6 |
| 2025 eerste helft | 67 | 6 | 17 | 23 (34%) | 2 |
| 2025 tweede helft | 87 | 5 | 20 | 15 (17%) | 1 |
| jan t/m apr 2026 | 73 | 0 | 38 | 4 (5%) | 0 |
| **mei t/m aug 2026 (3 tot 6 maanden)** | **108** | **0** | **74 (69%)** | **1 (1%)** | 0 |
| alleen nieuwe makers, mei t/m aug 2026 | 77 | 0 | 53 | 0 | 0 |

Eerlijke kanttekening van de controleur: een deel van het verschil komt door leeftijd. Op gelijke leeftijd had van de lichting 2025 tweede helft 48 tot 63% binnen 180 dagen minstens één review, van jan t/m apr 2026 33 tot 37%. Nieuwkomers doen het dus slechter dan een jaar geleden, maar het verschil is kleiner dan "mediaan 5 tegen 0" laat zien. Verwijderde apps ontbreken (overlevingsfout), dus oudere lichtingen lijken beter dan ze waren. Hoeveel installs bij één review horen, weet niemand van buiten.

**Vindbaarheid: geen plek voor nieuw.** Sorteren kan alleen op "Recomendados" en "Mais avaliados"; geen "novos", `isNew` staat bij alle apps op false (GEZIEN). Van de 77 uitgelichte apps (`isFeatured`) zijn er 3 van na juli 2025 (recupera-ja 2 reviews, abejita-warnings 2, plante-arvores 33). Wel noemt de maandelijkse nieuwsbrief voor winkeliers nieuwe apps (GEZIEN door onderzoeker, nuvemshop.com.br/newsletter/novidades-aplicativos-novembro-2025). Partnerniveaus Silver, Gold, Platinum geven voorrang in de categorie (GEZIEN, tiendanube.com/socios/tecnologicos).

**Wie doorbreekt:** van de 15 jonge apps (mei 2025 t/m aug 2026) met de meeste reviews zijn er 8 van Abejita, een maker die sinds sep 2024 76 apps neerzette (75 gratis, samen 1.163 reviews). Daarna Appsnube (maker sinds 2020, 14 apps, betaald ARS 14.990 per maand, 36 reviews) en een paar losse nieuwe makers met 22 tot 33 reviews, allemaal gratis. Van de 79 apps sinds nov 2025 die via Nuvemshop afrekenen heeft de beste 36 reviews, de tweede 10.

## Geld (onderzoeker, met bronnen)
- Zelf afrekenen mag: "Free: the app is free or billing is handled externally by the partner" (GEZIEN, nuvemshop.dev/en-US/apps/publish/pricing-billing.md, 7 okt 2026). Afrekenen via Nuvemshop kan eenmalig of per maand (Billing API 2025-03). Het percentage dat Nuvemshop dan inhoudt staat nergens openbaar.
- Uitbetaling via Nuvemshop vraagt in Brazilië een Braziliaanse bank, CPF of CNPJ en een nota fiscal; in Argentinië een AFIP-inschrijving (GEZIEN, atendimento.nuvemshop.com.br en ayuda.tiendanube.com). Voor Thijs blijft dus alleen zelf afrekenen (GOK, wel de route die TopSoft gebruikt).
- **Verdienen buitenlandse makers? Niet aantoonbaar.** TopSoft UG (Duitse rechtsvorm) heeft 14 apps, zelf afgerekend (PRO $8,50 per maand). Twee oude apps hebben 82 en 83 reviews (uit dec 2021 en feb 2024), de andere twaalf 0 tot 21; de 7 apps van 2024 tweede helft en later samen 5 of minder elk (GEZIEN). Geen bedrag, geen TrustMRR- of IndieHackers-profiel, geen interview van een kleine of buitenlandse maker gevonden (onderzoeker).
- Partner worden kost niets. Keuring tot 30 werkdagen, met sequence-diagram, demovideo, demo-account en een FAQ met ondersteuning op niveau 1 en 2 (GEZIEN, nuvemshop.dev/en-US/apps/publish/faq.md). Ondersteuning in het Portugees (BR) en Spaans (AR, MX, CO, CL) verplicht (GEZIEN, guidelines.md).

## Wat er veranderde
Sinds 5 juni 2026 moeten nieuwe apps met scripts in de winkel NubeSDK gebruiken, en sinds sep 2026 moeten bestaande apps met scripts over en opnieuw gekeurd worden; oude scripts mogen voorlopig blijven draaien (GEZIEN, nuvemshop.dev, homologation). Geen harde breuk, dus geen gat waar oude apps massaal stuk gaan. Nieuw in okt en nov 2026: Admin MCP en Storefront MCP (GEZIEN, nuvemshop.dev/en-US/news).

## Tegen de lat van een 8
1. Nieuwe kleine makers verdienen er nu: **nee**, niet zichtbaar; 69% van de jonge apps heeft geen enkele review, en geen bedrag van een kleine maker.
2. Bereik voor nieuwkomers: **zwak**, geen lijst voor nieuw, top bezet door oude apps en één maker met 76 apps.
3. Bouwen en testen: ja, gewone web-app met REST-API, NubeSDK in JavaScript.
4. Thijs kan binnen een week verkopen: **deels**, alleen met eigen kassa (Stripe of Lemon Squeezy), plus keuring tot 30 werkdagen en ondersteuning in twee talen.

## Voor en tegen
- Voor: platform groeit hard (Noor: 124.943 naar 208.292 winkels in zeven kwartalen, DERDEN storeleads), zelf afrekenen mag, geen afdracht dan.
- Tegen: nieuwe apps krijgen bijna niets, geen verkoopbewijs, Portugees en Spaans, Braziliaanse winkeliers prijsgevoelig en gewend aan Pix, keuring traag.

## Als we het toch zouden doen
Een winstapp (winst per bestelling na Nuvem Pago-kosten, verzending en belasting) zoals Noor voorstelde, gebouwd op de kern van Tess bij TikTok Shop. Kost weinig extra omdat de kern er al is. Maar met dit bereik verwacht ik in een half jaar hooguit een handvol installs (GOK).

## Herhaalmeting
Rond 15 feb 2027: `python3 -I data/nuvemshop-haal-script.py sitemap.xml uit.jsonl` (sitemap eerst halen met `curl -sL https://www.nuvemshop.com.br/sitemap-apps.xml`), dan de analyse. Opnieuw wegen als de lichting mei t/m aug 2026 dan, op 6 tot 9 maanden, 15% of meer apps met 10+ reviews heeft, of als er een lijst "novos" in de winkel komt.
