# Voorstel: Notion Marketplace (betaalde templates)

Vera, verkenner, 7 nov 2026 run 20:33 (tweede platform). Advies: **nee voor nu, niet te meten. Cijfer 3.**

Eerder stond "Notion" in `onderzocht.md` als zwak; dat ging over integraties. De templatewinkel, waar Notion zelf afrekent, was nog niet bekeken.

## Wat is het
In de Notion Marketplace (notion.com/templates) zetten makers templates: kant-en-klare Notion-pagina's en databases. Gratis of betaald. Bij betaald is Notion de verkoper (merchant of record) en rekent af via Stripe.

## Zo gemeten (GEZIEN)
- robots.txt staat de templatepagina's toe (alleen zoeken is verboden). De sitemap `sitemaps.notion.com/sitemap-templates.xml` heeft **99.667** adressen, waarvan **65.007** zonder taalcode (Engels).
- Steekproef van 240 willekeurige Engelse templates (seed 7), prijs uit de structured data: **91 betaald (38%)**, mediaanprijs **$9,99**. Data: `data/notion-prijs-steekproef-2026-11-07.txt`, script `data/notion-steekproef-script.sh`.
- **Verkoop is niet te zien.** De pagina's hebben een veld `number_of_duplicates`, maar dat staat altijd op -1 (verborgen). Er is geen publicatiedatum van de template: de pagina toont "Last updated 56 years ago" (een lege datum). Wel staan er andere datums in de pagina (`datePublished` en `created_time` van reviews, `source_block_last_edited_time` als wijzigdatum); dat zijn geen startdatums. Ik ben niet verder gaan zoeken naar verborgen cijfers (les van Elgato).
- Zwakke aanwijzing voor bereik (GEZIEN door de controleur, eerste 60 van de steekproef): 13 van de 60 (22%) hebben reviews, tussen 1 en 24 (1 1 1 2 4 4 5 7 9 9 13 22 24); de rest 0. Reviews zijn geen verkopen, en niet bij elke treffer is gecontroleerd dat hij bij de template zelf hoort.
- De `lastmod` in de sitemap loopt van 2.500 tot 7.300 per maand (sep 2025 t/m okt 2026, oplopend). Dat is een wijzigdatum, geen startdatum, dus alleen een ruwe aanwijzing voor drukte (GOK).

## Geld (DERDEN)
- Notion rekent 8% plus $0,40 per verkoop, en 1% extra wisselkoers buiten de VS. Uitbetaling elke twee weken vanaf $20. Om zelf te verkopen moet je op een wachtlijst; "it may take a few months to get reviewed", en Notion kan weigeren (DERDEN: [help/selling-on-marketplace](https://www.notion.com/help/selling-on-marketplace)). Je mag ook een link naar Gumroad of een eigen winkel zetten.
- Grote makers verdienen veel: Thomas Frank noemt $1 miljoen aan templateverkoop (DERDEN: [typefully, Thomas Frank](https://typefully.com/TomFrankly/dollar1-million-in-notion-template-sales-kuFT0iD)). Dat is een maker met een groot YouTube-kanaal, geen kleine maker.
- Kleine makers: alleen losse blogverhalen van $250 tot $500 per maand, niet na te gaan (DERDEN, zwak: [substack](https://themindfulplanner.substack.com/p/how-i-made-250-selling-notion-templates), [dev.to](https://dev.to/ioneldigital/how-to-create-and-sell-notion-templates-my-500mo-strategy-5cch)). Geen meting van wat een gewone nieuwe template verkoopt.

## Drukte
Heel druk: 65.007 Engelse templates (GEZIEN), duizenden wijzigingen per maand (GOK). Templates zijn makkelijk te maken, ook met AI, dus de winkel loopt vol.

## Vindbaarheid
Categorieën, collecties van Notion en zoeken (DERDEN, eigen bezoek). Verkoop komt volgens de verhalen vooral via eigen publiek: YouTube, TikTok, X, Reddit. Zonder publiek is een nieuwe template één van 65.000.

## Past het bij ons
Bouwen wel: een goede template is in dagen klaar en Thijs hoeft niet te programmeren. Maar Dortus heeft geen publiek, en dat lijkt hier de sleutel. Thijs moet zich ook aanmelden voor de wachtlijst (stap voor Thijs).

## Vervolg 7 nov: Gumroad als meetpunt (GEZIEN)
Veel Notion-templates worden via Gumroad verkocht. Gumroad zet per maand een openbare sitemap met nieuwe producten (robots.txt staat dat toe) en de productpagina bevat aantal ratings (alleen kopers kunnen raten) en soms een verkoopteller (alleen als de maker die aanzet).
- Sitemap juni 2026: 20.856 producten. Willekeurige steekproef van 3.000 (seed 7) gelezen met gewone curl: 1.710 nog online (43% gaf geen pagina; meest 404, ook een paar time-outs, dus een bovengrens).
- Van de 1.710: 1.568 betaald, mediaanprijs $10. **44 (2,6%) hebben minstens één rating.** 97 betaalde tonen een verkoopteller: mediaan **0**, 3 met 10+ (de top: 414, 18, 10); 11 van de 97 boven 0. Makers die de teller tonen zijn eerder de betere verkopers, dus dit is eerder te mooi dan te somber (GOK).
- Notion-templates in de steekproef (naam bevat "notion"): **27**: 26 betaald ($5 tot $599) en 1 gratis. Eén heeft 1 rating, twee tonen een teller en die staat op 0.
- Data: `data/gumroad-juni2026-steekproef-2026-11-07.json`, script `data/gumroad-haal-script.py` (sitemap: public-files.gumroad.com/sitemap/products/monthly/2026/6/sitemap.xml.gz).
- Betekenis: een nieuw Gumroad-product (alle soorten) verkoopt na 5 maanden mediaan 0. Bij Notion zijn maar 2 tellers zichtbaar (beide 0) en 1 rating op 27. Dat past bij het nee, maar het is geen harde meting voor Notion, en of de maker een eigen publiek heeft is niet gemeten.
- Nagekeken door een controleur: getallen opnieuw uitgerekend, 6 pagina's zelf gelezen (alle gelijk), sitemap 20.856 klopt. 3 correcties verwerkt (top 3, Notion-prijzen, voorzichtiger conclusie).

## Nagekeken
Controleur 7 nov: akkoord. Sitemap (99.667, 65.007 Engels), steekproef (91 van 240 betaald, mediaan $9,99) en fee opnieuw gemeten: klopt. Correcties verwerkt: veldnaam `number_of_duplicates`, uitleg over andere datums op de pagina, reviews als zwakke aanwijzing toegevoegd. Nederland staat in de lijst van landen die direct mogen verkopen.

## Cijfer en advies
**Cijfer 3. Nee voor nu: bereik en verkoop van nieuwe templates niet te meten**, de winkel is heel vol, en het geld dat aantoonbaar is zit bij makers met een groot eigen publiek.

Hoe het wel te meten is: Gumroad-pagina's van Notion-templates die een verkoopteller tonen, of een andere winkel met tellers (Etsy toont "sales" per winkel). Wat dit verandert: een meting waaruit blijkt dat nieuwe templates zonder eigen publiek mediaan 10+ verkopen halen in 3 maanden.
