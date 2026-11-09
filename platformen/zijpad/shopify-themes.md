# Shopify Theme Store (betaalde winkelthema's)

Lotte, 9 nov 2026 run 13:49 UTC. Eigen meting van alle 356 thema's uit de sitemap (https://themes.shopify.com/sitemap_theme_en.xml), per thema de pagina plus de eerste en laatste reviewpagina. Data: `data/shopify-themes-2026-11-09.jsonl`, script: `data/shopify-themes.py`. Controleur akkoord met de getallen (12 thema's zelf nageteld, alles gelijk; één veldfout bij thema's zonder reviews, verbeterd).

Waarom dit een zijpad is: Vera mat Shopify-apps (cijfer 5 tot 6), niet de themawinkel. Dat is een aparte, kleine winkel voor digitale producten met hoge prijzen.

## Cijfers
- 356 thema's van 125 makers, 24 gratis (van Shopify zelf), mediaanprijs betaald **$300** (GEZIEN). Klein schap: ter vergelijking 8.000+ Shopify-apps.
- Afdracht 15% van de bruto-omzet plus 2,9% verwerking (DERDEN, https://shopify.dev/docs/storefronts/themes/store/revenue-share.md). Eén verkoop van $300 is dus ±$245 netto.
- Indienen is gratis en staat open (DERDEN, https://shopify.dev/docs/storefronts/themes/store/review-process/submit-theme.md). Er komen nog nieuwe makers bij in 2026 (GEZIEN). Lijst "nieuwe thema's": 8 thema's nu (GEZIEN door controleur).
- **Jonge lichting** (betaald, eerste review tussen 1 nov 2025 en 30 jun 2026): 36 thema's, mediaan **6 reviews**, 21 met 5+, 10 met 10+ (GEZIEN). Snelste: pebble (FoxEcom, $400) 75 reviews sinds maart, maximize (Omni Themes, $220) 56, vetro en athora (The4, $290) 35 en 27.
- Daarnaast 22 betaalde thema's op versie 1.0 of 1.1 zonder reviews (GEZIEN). Tel je die mee als jonge lichting (n=58), dan is de mediaan ±3 reviews, 36% heeft 5+ en 17% 10+.
- **Verhouding reviews en verkopen:** één aanknopingspunt. Een Griekse studio (opgericht 2022, 3 thema's) meldt bij verkoop 2.300+ licenties en $321,5k omzet in 12 maanden (DERDEN, https://app.acquire.com/public/1duv5ijj0r-shopify-theme-solution-for-ecommerce-sellers-to-enhance-store-design). Waarschijnlijk is dat Truly Fine Pixels met 117 reviews samen, dus **±1 review per 20 verkopen** (GOK, koppeling niet bevestigd).
- Met die verhouding: een jong thema met 3 tot 6 reviews heeft ±60 tot 120 verkopen gehad, ±$15.000 tot $30.000 netto in 5 tot 12 maanden (GOK). Ook bij 1 op 50 blijft het ±$6.000 tot $12.000. Geen enkel ander platform dat we bekeken gaf zo'n bedrag voor een gewone nieuwkomer.

## Wat schuurt
- **De markt krimpt in 2026.** Sinds 27 aug 2026 is de knop "Explore more themes" in de Shopify-admin vervangen door een gratis Shopify-thema. Makers melden dalende verkoop, één ontsloeg een team van 15, een ander had 3 dagen $0 op pagina 1 (DERDEN, https://community.shopify.dev/t/x/37670 en https://community.shopify.dev/t/x/38262). Op 1 okt 2026 kwam Shopify Canvas: winkelontwerp met AI (DERDEN, zelfde draden). Mijn reviewdatums lopen grotendeels van vóór die knop.
- **Bouwen is zwaar (punt 3).** Een volledig thema met alle templates, Lighthouse-eisen, toegankelijkheid, demowinkel, handleiding en support. Thema's op basis van Dawn of Horizon worden afgekeurd, het moet "fundamenteel anders" zijn; een studio werd twee keer afgewezen op ontwerp (DERDEN, https://community.shopify.dev/t/x/37514). Binnen 2 weken af is niet realistisch: eerder 4 tot 8 weken (GOK). Testen kan wel in de cloud: gratis ontwikkelwinkel, Shopify CLI en Lighthouse draaien op Linux.
- **Verkopen binnen een week (punt 4).** Partner-account is gratis (Thijs), maar de keuring heeft geen vaste termijn en duurt waarschijnlijk weken (DERDEN, geen antwoord in https://community.shopify.dev/t/theme-store-review-expected-feedback-timeline/35809). Uitbetaling via PayPal of bank met belastinggegevens; of dat zonder KvK gaat, is niet nagekeken.
- Exclusief: een thema in de winkel mag niet ergens anders verkocht worden.
- Startdatum via de oudste review mist thema's zonder reviews. Beter: de themapagina toont "Version X • datum", bij 1.0.x is dat de lanceerdatum (controleur).

## De vier punten
1. Nieuwe kleine makers verdienen: **sterk** als de verhouding ook maar ongeveer klopt (een kwart heeft 5+ reviews, dus vermoedelijk 100+ verkopen à $245). Maar het is afgeleid, niet gezien.
2. Bereik voor nieuwkomers: **redelijk**, klein schap met een lijst "nieuw" en filters per branche, maar het verkeer daalt sinds aug 2026.
3. Bouwen en testen: **testen ja, binnen 2 weken nee**, en de ontwerplat is heel hoog.
4. Verkopen binnen een week: **nee**, keuring van weken, KvK-vraag open.

## Eerste productidee
Een thema voor één branche waar weinig keus is en die past bij een strak, eigen ontwerp, bijvoorbeeld digitale producten en software (er is maar één thema "digital" van Segment) of één product met veel varianten. Eerst tellen welke branche-filters de minste thema's hebben.

## Cijfer: 6
Het sterkste geldsignaal dat ik zag ($300 per verkoop, jonge thema's met tientallen tot honderden verkopen volgens de enige bekende verhouding), maar punt 3 en 4 schuren echt en de markt krimpt sinds augustus. Advies: **doorgeven aan de herweger (Kees)**. De meting die de doorslag geeft: (a) per thema de "Version • datum" ophalen en een echte lichting maken, inclusief thema's zonder reviews, en de reviews per maand vóór en na 27 aug 2026 vergelijken; (b) een tweede bron voor de verhouding reviews en verkopen. Blijft de lichting na augustus verkopen en is de verhouding ±1 op 20: dan een 7, ondanks de bouwtijd.
