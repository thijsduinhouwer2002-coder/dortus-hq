# Marktbewijs: TikTok Shop naar boekhouding in NL (Moneybird, Exact)

Chris, 9 nov 2026, run 21 (±02:45 tot 03:30 UTC). Voor Hans, bij het voorstel van Tess (`platformen/tiktok-shop/voorstel-boekhoudkoppeling.md`). Ik kies het product niet; dit zijn de metingen op de zwakke plekken van het voorstel, met NL eerst omdat dat de eerste markt is. Onderzoek door een agent, kernpunten door mij nagemeten (Moneybird-eisen en de knoppen van Schakel, GEZIEN 02:52 UTC), en daarna nagekeken door een controleur (akkoord mits, alle moet-punten verwerkt, Schakel-lijst door mij nagemeten 03:00 UTC).

## Kort
1. **Het gat in NL is echt, maar smal.** Geen enkel officieel overzicht van Moneybird, Exact, e-Boekhouden, SnelStart of Jortt noemt TikTok. Alleen Schakel heeft een pagina TikTok Shop naar Moneybird, met een knop "Koppeling aanvragen"; volgens hun eigen lijst op schakel.app/koppelingen/ is die nog niet live (GEZIEN). Dit stuurt het voorstel van Tess bij, waar staat "Of Schakel echt live is: niet te zien zonder account".
2. **Vraag in NL is nog niet te zien.** Geen verkopersaantal voor NL, geen forumdraad of klacht van een NL-verkoper, één NL-blog die handwerk met de Excel-export aanraadt. De markt is pas 5 maanden oud (live 15 juni 2026). Vraag blijft GOK.
3. **De overzichten van Moneybird en Exact zijn bij de start geen kanaal.** Moneybird vermeldt een koppeling pas na minstens 25 actieve administraties en 2 maanden in bedrijf; Exact pas na een review. Geen van beide toont reviews of klantaantallen. Vinden moet dus via de TikTok App Store zelf en eigen verspreiding.

## 1. Bestaat er al een koppeling? (GEZIEN 9 nov 2026, tenzij anders vermeld)
| Plek | TikTok? | Bron |
|---|---|---|
| Moneybird koppelingen en webshops | 0 keer; bij marktplaatsen alleen Bol | https://www.moneybird.nl/product/koppelingen/ |
| Exact App Center | 0 van 603 vermeldingen (ongeveer 284 verschillende apps) noemt TikTok; wel Bol, Amazon, ChannelEngine | https://apps.exactonline.com/nl/nl-NL/ |
| e-Boekhouden, SnelStart, Jortt | 0 (Jortt alleen een link naar hun eigen TikTok-account); pagina's laden deels via script | hun pagina's /koppelingen |
| Webwinkelfacturen, Combidesk | 0 | home en /koppelingen |
| **Schakel** | pagina TikTok Shop naar Moneybird, alleen Moneybird, niet bij "Populaire koppelingen"; knoppen "Start gratis" en "Koppeling aanvragen" | https://schakel.app/koppelingen/tiktokshop-moneybird/ (sitemap 20 okt 2026) |

- Schakel belooft precies ons product voor Moneybird: verkoopfacturen per order of per dag, commissie en affiliatekosten op een eigen grootboekrekening, btw per regel met OSS, creditfacturen bij retour. Prijs: €0 (25 items), €10 per maand bij jaarbetaling of €15 maandelijks (250 items), €30 of €50 (onbeperkt) (GEZIEN, schakel.app/prijzen). Volgens de eigen lijst in de broncode van schakel.app/koppelingen/ is TikTok Shop naar Moneybird niet live en ook niet "binnenkort": de lijst met live koppelingen telt er 12 (onder meer bol-moneybird en shopify-moneybird), de lijst "binnenkort" 5 (bol-exact, bol-eboekhouden, amazon-moneybird en meer), en tiktokshop-moneybird staat in geen van beide. Het is een pagina waarop je de koppeling kunt aanvragen (GEZIEN 9 nov 2026). Schakel kan hem wel snel bouwen (GOK).
- Omwegen: TikTok naar ChannelEngine en dan via xCore of OrderChief naar Exact (voor grotere verkopers, xCore €29 per maand plus €250, onderzoek Tess). Shopify-verkopers kunnen orders doorzetten, maar niet de TikTok-kosten en uitbetalingen (GOK).
- Buitenland: Link My Books, A2X, Webgility, ConnectBooks doen TikTok alleen naar QuickBooks, Xero of NetSuite (DERDEN, https://linkmybooks.com/blog/tiktok-shop-bookkeeping , https://www.webgility.com/integrations/tiktok-shop).

## 2. Vraag
- Aantal verkopers NL: **niet gevonden.** tiktokshop.nl: "eigen cijfers zijn er nog nauwelijks" (DERDEN, https://tiktokshop.nl/artikel/tiktok-shop-europa-cijfers-q2-2026-wat-nederlandse-verkopers-leren.html); Puredigital na drie maanden (30 sep 2026) geeft geen getal (DERDEN, https://puredigital.nl/insights/sea/tiktok-shop-nederland-drie-maanden-later/). FR ±33.000 en IT 21.000+ staan al bij Tess (DERDEN).
- Klachten of vragen van NL-verkopers: geen gevonden. Reddit gaf 403 (niet omzeild); Moneybird- en Exact-community via WebSearch: 0 treffers voor TikTok (de sites zelf laden via script, niet doorzocht).
- Velocora (23 apr 2026) raadt aan de CSV of Excel uit Seller Center vast in Moneybird of e-Boekhouden te zetten (DERDEN, https://www.velocora.nl/blog/btw-tiktok-shop-nederland). Dat is het handwerk dat de app wegneemt, maar het is advies van een kennisblog ("Onafhankelijke kennishub" van klyo.nl), geen klacht van een verkoper. Velocora noemt €100 tot €250 per maand voor een boekhouder (DERDEN): bruikbaar als waardeargument.
- Buitenlandse makers (Link My Books, beancount.io met vertaalde NL-gidsen) schrijven veel over TikTok-uitbetalingen afstemmen (DERDEN). Wijst op vraag in VK en VS, niet bewezen voor NL.

## 3. Kanaal: overzichten van de pakketten
- **Moneybird** (GEZIEN, https://www.moneybird.nl/helpcenter/nl/articles/207365-zelf-een-koppeling-maken): API gratis. Voor een vermelding: OAuth, **minstens 25 actieve administraties en minstens 2 maanden actief**, refresh token, 150 aanvragen per 5 minuten, webhooks, boekingen die Moneybird zelf toetst, support. Geen reviews of installs op de pagina.
- **Exact** (GEZIEN, voorwaarden App Center 2018, https://files.exact.com/static/downloads/terms-and-conditions/2018/Exact-Exact-Online-App-Center-Terms-and-Conditions-of-Use-October-2018.pdf): publicatie na review met data- en securitycheck, audits op onze kosten mogelijk, Exact mag later een vergoeding vragen (art. 5.2). Plus het Developer-abonnement van €15 per maand (pakket-apis.md van Tess). Geen reviews of klantaantallen te zien.
- Ter vergelijking, NL-koppelingen in de Shopify App Store blijven klein, ook na jaren (GEZIEN, aantal reviews): Moneybird Bookkeeping (Combidesk) 30, Exact Online Bookkeeping 22, e-Boekhouden.nl 12, Moneybird 7, Combidesk e-Boekhouden 6, Moneybird Boekhouding 2; prijzen $9,99 tot $36 per maand.

## 4. Prijs
- Combidesk voor Moneybird, Exact en e-Boekhouden: elk $18, $24 of $36 per maand (GEZIEN, Shopify App Store). Past bij €15 tot €29.
- Let op het verschil met Tess ("in NL is €7 tot €15 per maand gangbaar"): dat gaat vooral over Bol-koppelingen, mijn $9,99 tot $36 over Shopify-apps. Samen: €7 tot €36, met €15 in het midden.
- De echte prijsconcurrent is Schakel met €10 per maand bij jaarbetaling. Voorstel voor later (GOK, pas na ja van Hans uit te werken in `prijs.md`): €15 per maand of €150 per jaar, met een gratis laag op aantal bestellingen; hoger dan Schakel verdedigen we met "in de TikTok App Store, één klik, per bestelling, en NL plus FR en IT".

## Wat dit betekent voor het besluit (mijn lezing, Hans beslist)
- Voor: het gat is er in NL echt (geen enkel officieel overzicht), de technische weg is open (Moneybird gratis), en betalen voor zulke koppelingen is gewoon in NL ($9,99 tot $36 op Shopify, GEZIEN).
- Tegen: in NL is de vraag niet te meten en waarschijnlijk klein (5 maanden oude markt, geen verkopersaantal), en Schakel staat al klaar voor Moneybird tegen €10. Moneybird-vermelding pas na 25 klanten, dus de eerste 25 moeten uit de TikTok App Store en eigen verspreiding komen.
- Wat het sterker zou maken: FR (±33.000 verkopers, Pennylane zonder TikTok) is de grotere markt; als Pennylane via hun partnerteam bereikbaar is, weegt FR zwaarder dan NL. Een meting van het aantal NL-winkels (bijvoorbeeld via de winkelpagina's in de TikTok-app of een bron na de KvK) zou de NL-vraag uit de GOK halen.
- Verspreiding (schets, uitwerken na ja van Hans in `verspreiding.md`): de listing in de TikTok App Store (zoekwoorden Moneybird, Exact, boekhouding, btw, OSS), een NL-pagina op dortus.com die zoekt op "TikTok Shop boekhouden Moneybird" (er staat bijna niets in het Nederlands, zie punt 2), kennisblogs zoals Velocora en boekhouders die TikTok-verkopers bedienen, en pas na 25 klanten het Moneybird-overzicht.
