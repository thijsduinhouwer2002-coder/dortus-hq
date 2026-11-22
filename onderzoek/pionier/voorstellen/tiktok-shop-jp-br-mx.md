# Voorstel: TikTok Shop App Store in Japan, Brazilië en Mexico (Noor, 8 nov 2026, run 20:40 UTC)

Vervolg op het EU-voorstel (`tiktok-shop-app-store.md`, cijfer 7, ja; manager Tess). Vraag van deze run: zijn de jongste TikTok Shop-landen buiten de EU een tweede pionierskans, met dezelfde opzet (eigen app-winkel per land, eigen kassa, TikTok houdt niets in)?

Gemeten met dezelfde open portal-API als voor de EU. Nieuw gevonden: elk land heeft een eigen host (`seller-jp.tiktok.com`, `seller-br.tiktok.com`, `seller-mx.tiktok.com`); de API geeft per `shop_region` dezelfde lijst, op welke host je ook vraagt (GEZIEN). Script bijgewerkt: `python3 -I data/tiktokshop-apps-meet.py JP` (of BR, MX), analyse met `data/tiktokshop-apps-analyse.py`. Tellingen in `data/tiktokshop-apps-{JP,BR,MX}-2026-11-08.json`.

## Kort
| Land | Apps | Makers | Nieuw in 2026 (jan t/m okt) | Ook in EU/UK actief | Oordeel |
|---|---|---|---|---|---|
| Japan (live 30 juni 2025) | 184 | 156 | 72 (2, 4, 7, 12, 10, 12, 10, 8, 5, 2) | 62 makers | 5, nog niet klaar |
| Brazilië (live mei 2025) | 385 | 354 | 259 (9, 6, 17, 28, 22, 31, 41, 44, 33, 28) | 46 makers | 4, nee: loopt vol |
| Mexico | 198 | 173 | 85 (5, 4, 10, 14, 8, 10, 15, 12, 5, 2) | 52 makers | 4, nee voor nu |
| ter vergelijking NL | 82 | | 31 | | (EU-voorstel, 7) |
| ter vergelijking VS | 721 (714 uniek) | | 278 | | vol |

Alle cijfers in de tabel GEZIEN (open portal-API, 8 nov 2026 ±20:45 UTC). De aanmaakmaand komt uit het service_id. Bij het nakijken bleek de standaardsortering van de API te verschuiven tijdens het bladeren (dubbele en gemiste apps); het script vult nu aan met een stabiele sortering en de tabel is daarmee opnieuw geteld (JP, BR, MX volledig; de EU- en VS-telling van eerder vandaag kan een paar dubbele bevatten, VS 714 uniek van 721). Let op: september en oktober zijn overal laag (ook VS 13 in okt, NL 2), waarschijnlijk door de keuring van 4 tot 8 weken; de laatste twee maanden zijn dus te laag (GOK).

## De vijf vragen (Japan, het enige land dat in de buurt komt)

1. **Groeit het hard?** Ja, maar vanaf weinig. TikTok zegt: maandelijkse gebruikers van TikTok Shop Japan in juni 2026 meer dan 30 keer zo hoog als in juli 2025; 70% van de omzet via video en live; 60% van de gebruikers is 35 of ouder (DERDEN, https://www.equalocean.com/news/2026080322074-tiktok-shop-reports-30-fold-user-growth-japan-102-fold-rise-brazil-daily-gmv/amp en https://zaikei.co.jp/article/20260729/863386.html). Tegenbewijs: in een enquête onder 176 Japanse winkeliers (Tete Marche) wilde ±10% TikTok Shop gebruiken en stond bijna een kwart ervoor open, en Japanners ontdekken op TikTok maar kopen vaak bij Rakuten of Amazon vanwege punten (DERDEN, https://influencermarketinghub.com/tiktok-shop-japan-ecommerce-market/; artikel van 17 aug 2025, vlak na de start, bijgewerkt 7 okt 2026, dus het cijfer is oud). Brazilië groeit harder: dagomzet mei 2026 102 keer zo hoog als mei 2025 (DERDEN, zelfde EqualOcean-bericht).
2. **Is de winkel jong?** Ja. 184 apps, waarvan 151 van 2025 en 2026; 2 tot 12 nieuwe per maand (GEZIEN). De 33 oudere zijn wereldwijde Chinese ERP's die in elk land staan (妙手, 店小秘, Lingxing, Mabang).
3. **Kan er betaald worden?** Ja, op dezelfde manier als in de EU: de maker int zelf, TikTok houdt niets in (DERDEN, partner-docs, zie EU-voorstel). In Japan, Brazilië en Mexico laat de API geen prijzen zien (net als in de EU; alleen de VS toont ze) (GEZIEN). Dat buitenlandse bedrijven in Japan mogen listen is aannemelijk: 62 van de 156 makers in Japan staan ook in de EU- of UK-winkel, onder meer uit India, Singapore en China (GEZIEN, partner_id vergeleken). Of een Nederlandse BV in Japan mag listen, is niet nagekeken (GOK: waarschijnlijk ja, zelfde Global Partner Center).
4. **Is er vraag?** Er is een duidelijk signaal: een Tokiose advocatenpraktijk bracht in juni 2026 een gratis checklist uit voor verkopers en creators, omdat de regels voor TikTok Shop in vier lagen liggen (voorwaarden, beleid, community-regels en de Japanse wetten 特商法, 景表法 met het verbod op stealth marketing, 薬機法 voor cosmetica en gezondheid, PSE), vaak veranderen en overtredingen tot schorsing leiden (DERDEN, https://prtimes.jp/main/html/rd/p/000000011.000141906.html). Beauty is een hoofdcategorie in Japan (DERDEN, https://www.personalcareinsights.com/news/tiktok-shop-expands-ecommerce-japan.html, titel). Dat iemand voor een app betaalt is niet bewezen, en een gratis checklist is ook reclame voor het kantoor zelf: het signaal is zwak. Een lege categorie kan ook betekenen dat er geen vraag naar een app is.
5. **Is de eerste plek te pakken?** In Japan staat geen enkele app die listings of creatorteksten toetst aan 薬機法 en 景表法; alleen twee Chinese ERP's noemen "自動コンプライアンス" als bijzaak (YiSync, SuperAplus, april 2026) en één creator-tool noemt compliance (ProBoost.AI) (GEZIEN, zoektocht in alle 184 beschrijvingen). De categorie is dus leeg, zoals Europese productregels in de EU.

## Brazilië en Mexico in het kort
- **Brazilië:** de hardste groei, maar de winkel loopt nu al vol: 259 nieuwe apps in 2026, in juli en augustus 41 en 44 per maand, meer dan de VS (GEZIEN). Bijna allemaal Braziliaanse ERP's en NF-e-koppelingen (elektronische factuur, verplicht): 32 apps noemen NF-e of nota fiscal, waarvan 28 van 2026 (GEZIEN). De voor de hand liggende lokale regelcategorie (NF-e) is dus al bezet. Dit is Vera-terrein, geen pionierskans. Tegenargument (controleur): dat de winkel zo snel volloopt, laat ook zien dat verkopers apps zoeken, en andere Braziliaanse regels zijn niet onderzocht: geen enkele app noemt ANVISA (cosmetica en gezondheid) of INMETRO (GEZIEN, zoektocht in alle beschrijvingen). Nagekeken om 21:00: de partner-changelog heeft voor Brazilië geen verplichte ANVISA- of INMETRO-velden, alleen technische wijzigingen (GEZIEN, https://partner.tiktokshop.com/docv2/changelog), dus geen aanwijzing dat verkopers daar door TikTok op vastlopen. Blijft 4.
- **Mexico:** 198 apps, vooral wereldwijde Chinese ERP's en M2E (10 apps), 2 tot 15 nieuwe per maand (GEZIEN). Geen groeicijfer van TikTok Shop Mexico gevonden. De lokale regelhoek (CFDI-facturen, inhoudingen door platforms) heeft maar twee apps die CFDI noemen (Wizerp, CanalPulse) (GEZIEN), maar zonder bewijs van groei en vraag is het nee voor nu.

## Risico
- Japan: TikTok Shop slaat misschien niet aan bij Japanse winkeliers (10%-cijfer), en de groei van 30 keer gaat uit van een maand met bijna niets. Teken dat het stokt: minder dan 3 nieuwe apps per maand in de JP-winkel na de keuringsachterstand, of berichten dat TikTok Shop Japan krimpt.
- Taal en vertrouwen: Japanse verkopers kopen liever van Japanse bedrijven met Japanse support; een product over wetgeving wekt de verwachting van juridische zekerheid (aansprakelijkheid). Claude schrijft goed Japans, maar niemand in Dortus kan het nakijken.
- Capaciteit: Tess is net begonnen in de EU en heeft nog niets gebouwd. Een tweede land nu zou haar ene taak versnipperen (regel 3).

## Categorie en eerste productidee (alleen Japan, voor later)
Categorie: **Japanse reclameregels voor TikTok Shop** (薬機法, 景表法, stealth marketing, PSE). Product: leest alle listings via de Product API, markeert woorden en claims die bij cosmetica, supplementen en gezondheid niet mogen (bijvoorbeeld 治る, シミが消える, No.1 zonder bron), stelt toegestane formuleringen voor en geeft creators een check van hun script en #PR-vermelding. Gratis: scan van 20 listings. Betaald: alle listings en bewaking, ±¥2.980 tot ¥4.980 per maand per winkel, eigen kassa. Dit is dezelfde bouwsteen als het EU-product van Tess (listings via de API toetsen aan lokale regels), dus het kan later als tweede land op dezelfde code.

## Cijfer en advies
- **Japan: 5, nog niet klaar.** Winkel jong, betalen werkt, categorie leeg en een echt vraagsignaal, maar de groei is onzeker (10% van de winkeliers), taal en aansprakelijkheid zijn lastig, en het hoort na het EU-product, niet ernaast. Advies aan Hans: geen aparte manager; zet het als mogelijke tweede markt in de taak van Tess zodra haar EU-product live is en betalende klanten heeft.
- **Brazilië: 4, nee** (loopt vol met lokale ERP's, 259 nieuw in 2026). Eventueel tip voor Vera.
- **Mexico: 4, nee voor nu** (geen groeibewijs, geen vraag gezien).
- Herhaalmeting rond 8 dec 2026: `for r in JP BR MX; do python3 -I data/tiktokshop-apps-meet.py $r; done`, dan de analyse; kijk naar nieuwe apps per maand in Japan en of er een regel-app bijkomt.

Nagekeken door een controleur-agent (8 nov ±20:55 UTC): alle tellingen opnieuw opgehaald en kloppend; verbeterd: 60% gaat over gebruikers, niet kopers; het 10%-cijfer is oud en klein (176 winkeliers); Mexico heeft twee CFDI-apps, niet één; tegenargumenten bij Japan en Brazilië toegevoegd.

Wat ik niet kon meten: installs (de API toont ze niet), prijzen buiten de VS, of een Nederlandse BV in Japan mag listen, en het aantal verkopers per land.
