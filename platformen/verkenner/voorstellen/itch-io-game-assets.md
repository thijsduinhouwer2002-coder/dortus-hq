# itch.io, betaalde game-assets (3D, pixel, geluid, Godot)

Onderzocht 17 nov 2026 (run 01:31 UTC) door Vera, voor de nachtscan (nacht-2026-11-17.md). Nagekeken door een controleur (eigen steekproef, akkoord). De tools op itch zijn op 8 nov al gemeten (voorstellen/itch-io.md, cijfer 4); assets nog nooit.

## Wat is het
In de categorie Game assets verkopen makers pakketten aan spelmakers: 3D-modellen (low poly, PSX-stijl), pixel art, tilesets, geluidseffecten, muziek, lettertypes, en effecten en shaders voor Godot en Unity. Geen keuring, live binnen minuten, maker kiest de afdracht (standaard 10%), itch regelt btw en betaalt uit via PayPal of Payoneer.

## Hoe gemeten
- GEZIEN: de RSS-lijsten "nieuwste betaalde assets" (`itch.io/game-assets/newest/store.xml`, en per tag `.../store/tag-<tag>.xml`), voor de tags low-poly, 3d, pixel-art, 2d, sound-effects, music, fonts en godot. Elke lijst stopt na 200 pagina's (7.200 items). Script: `data/itch-assets-lijst-script.py`, tellingen per maand: `data/itch-assets-per-maand-2026-11-17.json`.
- GEZIEN: productpagina's (ratings, prijs, tags, AI-melding) van een willekeurige steekproef: 400 betaalde 3D- en low-poly-assets uit mei t/m jul 2026, 300 geluid en muziek uit mei t/m jul, 240 Godot-getagde uit mei t/m jul, en 200 pixel/2D uit 10 t/m 30 sep (de lijst reikt bij pixel niet verder terug). Plus de 59 assets uit 2026 in de top 180 bestsellers. Data: `data/itch-assets-steekproef-2026-11-17.json`. Pagina-script: `data/itch-pagina-script.py`.
- Controleur: eigen 40 low-poly-items uit mei t/m jul: 2 met 3+ ratings (5%), mediaan 0, max 13. Past bij mijn 2,5%.
- itch toont geen verkopen. Ratings zijn het enige spoor, zichtbaar pas vanaf 3. Werkgetal uit de meting van 8 nov: ±10 kopers per rating (GOK).

## Cijfers
| Maatstaf | Uitkomst | Label |
|---|---|---|
| Bereik 3D en low poly, 3,5 tot 6,5 maanden oud (n=400) | 97,5% minder dan 3 ratings, 2,5% 3+, 0,5% 10+, max 19 | GEZIEN |
| Geluid en muziek, zelfde leeftijd (n=300) | 94% minder dan 3, 6% 3+, geen 10+ | GEZIEN |
| Godot-getagd, zelfde leeftijd (n=240) | 88,8% minder dan 3, 11,2% 3+, geen 10+, max 8 | GEZIEN |
| Pixel en 2D, 1,5 tot 2 maanden oud (n=200) | 98% minder dan 3, 2% 3+ | GEZIEN |
| Middelste prijs | $4,99 (3D), $5 (geluid), $3,99 (pixel) | GEZIEN |
| Wat een gewone nieuwe asset verkoopt | minder dan ±20 tot 30 kopers in een half jaar, dus minder dan ±$100 | GOK (factor 10) |
| Drukte, nieuwe betaalde assets | alle soorten samen ±340 tot 470 per dag midden nov (controleur bevestigt). 3D-tag: mei 205, jul 373, sep 899, okt 3.229 | GEZIEN (oudere maanden mogelijk te laag door verwijderde items, GOK) |
| AI-melding in de steekproef | 3D ±26%, geluid ±44%, pixel sep ±61% met AI | GEZIEN |
| Bestsellers | 59 van de top 180 uit 2026, daarvan 32 met 3+ ratings en 6 met 10+. Beste nieuwe maker: Case Portman, geluidspakketten "Cute & Cozy UI SFX" (£4,99, aug 2026) 29 ratings, dus GOK ±300 kopers | GEZIEN, kopers GOK |
| Godot-effecten als soort | Binbun: Godot Effects Collection Vol. 1 ($26,25, feb 2026) 11 ratings, Vol. 2 en Fire VFX ook in de top 180; Godot Compositor Effect pack ($12) 4. Maar MOBA VFX voor Godot en hun0fx combat-VFX ($29,99, okt) nog 0 | GEZIEN |
| Godot Asset Store | nog alleen gratis, roadmap: "we only allow to publish free assets", geen datum (controleur, 17 nov) | GEZIEN |
| AI-regels | "strictly enforcing disclosure for all game asset, soundtrack ... pages", en "do not use automated systems to mass produce product pages" | GEZIEN (controleur, quality-guidelines) |

## Voordelen
- Snelste route naar de winkel van alle kandidaten: geen keuring, live in minuten. Thijs: itch-account, uitbetaling (PayPal of Payoneer) en belastingformulier.
- Alles in de cloud te bouwen: Blender headless voor 3D, Godot voor effecten, Python voor geluid.
- Wie een reeks bouwt met een vaste stijl verkoopt (Case Portman, KayKit, Puck, Binbun), en de bestsellerlijst weegt recente verkoop, dus een nieuw pakket kan even zichtbaar worden.
- Betaalde Godot-assets hebben geen eigen winkel: itch is de plek. Wij bouwen al in Godot (Hats).

## Nadelen
- Bereik van een gewone nieuwe betaalde asset is bijna nul, net als bij de tools: 94 tot 98% onder 3 ratings na een half jaar.
- De vloed groeit hard: de 3D-tag van ±200 per maand in mei naar ±3.200 in okt, grotendeels met AI. Wij moeten AI eerlijk melden, en kopers kunnen op "No AI" filteren.
- De winnaars zijn makers met een naam en een reeks van jaren (Kenney, KayKit, LimeZu). Eén pakket doet weinig.
- Bedragen zijn klein: middelste prijs $5.

## Eerste idee (als het ooit ja wordt)
Een Godot 4-effectenpakket dat werkt in de Compatibility-renderer (dus ook in webexport en op zwakke laptops), want de bestaande pakketten zijn vooral Forward+. Bouwen en testen in de cloud met Godot en een software-renderer, voor-en-na gif per effect. GOK: hooguit ±30 tot 100 kopers in een half jaar, $10 tot $15.

## Cijfer en advies
**Cijfer 3, nee voor nu** (Godot-effecten apart: 4). Snel en makkelijk, maar het bewijs van kopers voor nieuwe makers is net zo dun als bij de tools, en het wordt elke maand drukker met AI-werk. Niet in de top 5 van de nachtscan; eventueel als reserve naast plek 3 (Poki) voor wie al een Godot-effect heeft liggen.
