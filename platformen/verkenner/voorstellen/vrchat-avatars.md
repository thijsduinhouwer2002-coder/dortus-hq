# VRChat Avatar Marketplace en Jinxxy (avatars, kleding en spullen voor VRChat)

Vera, 8 nov 2026, run 05:32 (UTC). Advies: **nee voor nu, cijfer 3.**

## In het kort
VRChat verkoopt sinds mei 2025 zelf avatars voor VRC Credits. Die markt is nog dicht: verkopen kan alleen na aanvraag en keuring, en toelating voor avatars gaat "slowly". Zonder login is er niets te zien, dus niet zelf te meten. Daarom heb ik de grootste open winkel ernaast gemeten, Jinxxy (Westers, voor dezelfde kopers). Daar is geld voor kleine makers echt: de maker houdt 92%, en een gewone nieuwe betaalde avatar haalt mediaan 27 likes (GOK ±8 tot 14 verkopen van ±$30). Maar het product is 3D-kunst (avatars en kleding op bekende basisavatars), dat kunnen wij niet goed maken in 1 tot 2 weken, en de gemeenschap is sterk tegen AI-gemaakte 3D. Code-producten (scripts, shaders) zijn op Jinxxy een heel klein hoekje. Voor tools blijft BOOTH de betere plek (zie `voorstellen/booth.md`, cijfer 6).

## Hoe gemeten
- VRChat zelf (onderzoeker, met curl): vrchat.com/home/marketplace is een lege app-pagina, api.vrchat.cloud geeft 401 "Missing Credentials" voor avatars en store. Listings, verkoop en likes zijn zonder login niet te zien. GEZIEN 8 nov.
- Jinxxy (eigen meting): robots.txt verbiedt alleen /api/, /my/, /cart/ en dergelijke. Uit de 70 sitemaps 33.695 product-URL's gehaald, daaruit een willekeurige steekproef van 2.000 productpagina's gelezen (1.990 bruikbaar). Per product: created_at, like_count, sales_count (alleen als de maker dat aanzet), categorie, prijs (base_price en versieprijzen in centen), AI-melding.
- Scripts en data: `data/jinxxy-haal-script.py`, `data/jinxxy-analyse-script.py`, `data/jinxxy-urls-2026-11-08.txt`, `data/jinxxy-steekproef-2026-11-08.jsonl`.
- Controleur: 20 producten live nagelezen, alle velden gelijk; het hoofdproduct wordt goed gepakt (aanbevelingen hebben geen versies). Correcties verwerkt: product met gratis demo naast betaalde versies telt nu als betaald, URL's met spaties of &amp; worden goed gelezen, afdracht stond omgedraaid.

## Cijfers

### Regels en geld VRChat Marketplace
- GEZIEN (hello.vrchat.com/legal/economy): verkopen alleen na aanvraag, 18+, account 30+ dagen, identiteitscontrole en belastingformulieren bij Tilia. Voor avatars een aparte toelating: "We will slowly authorize more avatar sellers over time" (creators.vrchat.com/economy/store/avatar-marketplace, bijgewerkt 9 mei 2025).
- GEZIEN (ask.vrchat.com/t/48905, 3 sep 2026): winnaars van een jam krijgen een "fast-track" naar het Avatar Marketplace Seller Program. De markt is dus nog steeds niet open.
- GEZIEN (creators.vrchat.com/economy/faq en /payout, jan 2026): maker krijgt $1 per 200 verdiende credits, koper betaalt ±120 credits per dollar. De maker houdt dus **±50%**. Uitbetaling via Tilia (PayPal of IBAN), minimum ±$100. Of Nederland werkt staat er niet letterlijk, waarschijnlijk wel (GOK).
- Te verkopen: avatars, Udon-producten in werelden (spullen, toegang), groepsrollen als abonnement. Losse kleding als producttype niet gevonden.
- DERDEN: geen totalen van VRChat over uitbetalingen of aantallen makers. Wel: "top creators earn 4x more than on Patreon" (forum, mei 2025). Maker kg13 (note.com, apr 2026) verkocht een avatar 85 keer in een maand in de VRChat-markt (bedrag GOK ±$200 als de prijs het minimum van 600 credits was).
- DERDEN: pixiv (eigenaar van BOOTH) investeerde in sep/okt 2026 in VRChat (gamebusiness.jp 9 sep 2026, newswire 6 okt 2026). BOOTH 3D-categorie 2025 ±¥10,4 miljard omzet.

### Bereik en geld op Jinxxy (eigen meting)
- GEZIEN, lichting mei t/m aug 2026 (2 tot 6 maanden oud), n=339 in de steekproef:
  - Betaald (n=300): mediaan **15 likes**, 66% 10+, 15% 50+, **6% 100+**, 0,3% 500+. Mediaanprijs $10.
  - Avatars betaald (n=53): mediaan **27 likes**, 32% 50+, **21% 100+**, top 10% 174+. Mediaanprijs **$30**.
  - Kleding betaald (n=86): mediaan 19 likes, 2% 100+, prijs $9.
  - Materialen (n=77): mediaan 9, 0% 100+. Avatar-spullen (n=55): mediaan 21, 9% 100+. Wereldspullen (n=16): mediaan 4,5.
- GEZIEN, code-hoekje (alle leeftijden): scripts 12 van 1.990 (mediaan 14 likes, max 253), shaders 28 (mediaan 29). Heel klein.
- GEZIEN: maar 46 van 1.990 producten tonen het aantal verkopen. Bij de 37 betaalde daarvan zijn verkopen per like mediaan 0,45, met grote spreiding (0 tot 9,5). Scheef: wie zijn verkopen toont heeft vaker succes (mediaan 34,5 likes tegen 14). Gebruik als grove maat 0,3 tot 0,5 verkopen per like (GOK).
- GOK met die maat: middelste betaalde product ±5 tot 8 verkopen in 2 tot 6 maanden (±$45 tot $70 netto). Middelste avatar ±8 tot 14 verkopen (±$250 tot $380 netto). Avatar in de top 10% ±50 tot 90 verkopen (±$1.400 tot $2.400 netto).
- GEZIEN (jinxxy.com/about/selling): Standard 5% platform + 3% betaling, maker houdt **92%**. Supporter 10% + 3% met meer zichtbaarheid, maker houdt 87%. $1,50 per uitbetaling, wekelijks via PayPal of Stripe, minimum $10. Jinxxy is merchant of record (btw geregeld). Nederland kan via PayPal en Stripe.

### Drukte
- GOK uit de steekproef (× 33.695 / 1.990): ±1.400 nieuwe producten per maand in mei t/m aug 2026, ±2.700 in oktober. Hard groeiend. Sitemap loopt een paar dagen achter (controleur).
- GEZIEN: 49 van 623 producten sinds mei hebben een ingevulde AI-melding (veld generative_ai_disclosure bestaat op Jinxxy).

### Vindbaarheid
- Jinxxy: marktpagina met categorieën, nieuwste, likes en uitgelicht; Supporter-optie geeft meer zichtbaarheid. Kopers komen veel uit Discord en X van de maker (GOK, niet gemeten).
- VRChat-markt: categorieën, A-Z en passen voor kopen (DERDEN, moguravr.com 28 mei 2025).

### AI
- DERDEN (gamebusiness.jp 7 okt 2026, automaton-media.com 2 nov 2026): VRChat discussieert nog over AI-gemaakte assets, 95% van de spelers wil een label, en na een AI-ophef op 29 okt zakte de recente Steam-score naar "Mostly Negative". BOOTH haalt sinds 2023 winkels met massaal gelijke (vaak AI-)producten uit de zoekresultaten.

## Voordelen
- Kleine makers verdienen aantoonbaar, vooral met avatars ($30 en meer).
- Jinxxy: 92% voor de maker, btw geregeld, uitbetaling naar Nederland.
- Hard groeiende markt (BOOTH 3D +79% in 2025, Jinxxy aanbod verdubbeld in een paar maanden).

## Nadelen
- VRChat-markt zelf is dicht voor nieuwe verkopers en niet te meten.
- Het product is 3D-kunst: avatars, kleding passend op Manuka, Shinano en andere basisavatars. Dat vraagt een 3D-artiest, geen code. Niet te maken in 1 tot 2 weken door ons.
- Gemeenschap staat vijandig tegenover AI-gemaakte 3D; we zouden het moeten melden en dat kost verkoop.
- Code-producten zijn op Jinxxy bijna afwezig; dat publiek koopt kunst.
- Verkoop alleen te schatten via likes.

## Eerste idee als we het toch doen
Geen avatar of kleding. Hooguit een Unity-editortool voor avatarmakers (bijvoorbeeld kleding automatisch passend maken op meerdere basisavatars) die we op BOOTH uitbrengen en daarnaast op Jinxxy zetten voor de Westerse kopers. Dat hoort bij het BOOTH-voorstel, niet bij een eigen platform.

## Cijfer en advies
**3 van 10. Nee voor nu.** Geld is er, maar voor 3D-kunst die wij niet goed kunnen maken, en de VRChat-markt zelf is dicht. Opnieuw kijken als VRChat de Avatar Marketplace openzet voor iedereen, of als VRChat Udon-producten in werelden een openbare lijst met cijfers krijgen. Voor het BOOTH-voorstel: Jinxxy is een goede tweede winkel voor dezelfde tool (92% voor de maker).

Herhaalmeting: `python3 data/jinxxy-haal-script.py urls urls.txt` en daarna `haal urls.txt uit.jsonl 2000 <seed>`, analyse met `data/jinxxy-analyse-script.py`.
