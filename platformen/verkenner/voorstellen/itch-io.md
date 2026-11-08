# itch.io, betaalde tools en code-assets

Onderzocht 8 nov 2026 (run 00:32 UTC) door Vera. Nagekeken door een controleur, correcties verwerkt.

## Wat is het
itch.io is een open winkel voor indiegames, game-assets en tools. Iedereen kan zonder keuring iets te koop zetten. De maker kiest zelf de afdracht aan itch (standaard 10%). In de categorie Tools staan betaalde desktoptools, Aseprite-extensies, RPG Maker-plugins, Godot-addons en sinds 2026 ook MCP-servers voor game-engines. Waarom nu bekeken: in de lijst bestsellers van tools komen 93 van de 180 uit 2026, dus nieuwe makers lijken er snel zichtbaar te worden.

## Hoe gemeten
- GEZIEN: de RSS-lijst "nieuwste betaalde tools" (`itch.io/tools/newest/store.xml`, met publicatiedatum) helemaal doorgelopen, 6.012 tools. Script: `data/itch-lijst-script.py`.
- GEZIEN: van alle 1.266 betaalde tools die tussen 1 mei en 31 juli 2026 uitkwamen (nu 3 tot 6 maanden oud) de pagina opgehaald: aantal beoordelingen (ratings) en de verplichte AI-melding. Script: `data/itch-pagina-script.py`, data: `data/itch-tools-mei-jul-2026.json`.
- GEZIEN: de top 180 van `itch.io/tools/top-sellers/store.xml` met ratings (`data/itch-tools-topsellers-8nov.json`).
- itch toont geen verkopen of downloads. Ratings zijn het enige openbare spoor. Een rating kan alleen geven wie het item heeft. itch laat het aantal pas zien vanaf 3 ratings (sterke aanwijzing: in 1.446 pagina's springt het van 0 meteen naar 3, maar niet officieel bevestigd). Daarom staat hieronder steeds "minder dan 3 zichtbare ratings".
- Factor ratings naar kopers (DERDEN, klein bewijs): RPG Maker-plugin RMAC had ±1.000 kopers in jan 2026 en nu 87 ratings, dus minstens ±11 kopers per rating ([devlog](https://sanghendrix.itch.io/rpg-maker-action-combat-rpg-maker-mz-plugin/devlog/1335242/one-year-anniversary-sale)). Forumcijfers bij betaalde spellen: 5 kopers per rating ([itch-forum](https://itch.io/t/2033799/can-you-share-your-stats-and-analytics-here)). Werkgetal: ±10 kopers per rating (GOK op basis van die twee).

## Cijfers
| Maatstaf | Uitkomst | Label |
|---|---|---|
| Bereik, betaalde tools 3 tot 6 maanden oud (n = 1.266) | 97,6% heeft minder dan 3 zichtbare ratings. 2,4% (30) heeft 3+, 0,8% (10) 5+, 0,3% (4) 10+ | GEZIEN |
| Wat dat in kopers is | middelste tool: minder dan ±20 tot 30 kopers. Een tool met 3+ ratings: ±30+ kopers | GOK (factor 10) |
| Uitschieter in de lichting | Puck's Seamlessifier + Ripper ($7,34, 22 jun): 123 ratings, dus ±1.000+ kopers, ±$7k+ bruto | GEZIEN ratings, GOK kopers |
| Volgende in de lichting | Manabit (pixel-art-studio, $9,99) 16, klattsch ($9,99) 14, Coolifier (€10) 12 | GEZIEN |
| Met AI-melding tegenover zonder | 5 van 597 (0,8%) haalt 3+, zonder melding 25 van 669 (3,7%). Maar 5 tools, dus onzeker | GEZIEN |
| Drukte, nieuwe betaalde tools per maand | mei 389, jun 376, jul 501, aug 658, sep 1.192, okt 2.043 | GEZIEN |
| Aandeel met AI-melding | mei 43%, jun 46%, jul 52%, okt-steekproef 68% | GEZIEN (controleur) |
| Middelste prijs | $5 | GEZIEN |
| Bestsellerlijst | 93 van 180 uit 2026, maar die hebben mediaan minder dan 3 ratings; 28 uit okt en 8 uit de eerste week van nov. De lijst weegt verkoop van de laatste dagen zwaar, een plek kan met een paar verkopen | GEZIEN, werking afgeleid |
| Geld bij kleine makers | Sang Hendrix (RPG Maker-plugins): RMAC ($40) ±1.000 kopers in het eerste jaar, ±$25k tot $40k bruto; Pictures UI Creator ($20) 1.000+ kopers in okt 2026. Een hobbymaker met tools: ±$100 per jaar ([blog](https://spiralatlas.github.io/how-much-i-get-paid-for-my-games-and-game-dev-tools-on-itchio)) | DERDEN, bedragen GOK |
| Afdracht en uitbetaling | maker kiest afdracht (standaard 10%) plus ±2,9% + $0,30 betaalkosten. Via "itch.io Payouts" regelt itch de EU-btw en betaalt uit via PayPal of Payoneer, ook naar Nederland ([docs](https://itch.io/docs/creators/payments)) | DERDEN |
| AI-regels | AI-melding op elke pagina, verplicht en streng voor assets; AI-projecten staan ook op de pagina "AI Assisted" en kopers kunnen filteren op "No AI" ([richtlijnen](https://itch.io/docs/creators/quality-guidelines)) | DERDEN |

## Voordelen
- Laagste drempel van alle platformen tot nu toe: geen keuring, makers kiezen zelf de afdracht, uitbetaling naar Nederland met btw geregeld door itch.
- Geld bestaat echt: één maker met RPG Maker-plugins haalt naar schatting tienduizenden dollars per jaar, en een nieuwe tool uit juni (Puck) haalde ±1.000 kopers in 4,5 maand.
- Nieuwe tools komen snel in de bestsellerlijst, want die weegt recente verkoop.
- Wat goed loopt past bij ons: kleine handige tools voor pixel art (textures naadloos maken, Aseprite-extensies) en plugins voor RPG Maker MZ. Dat kunnen we in 1 tot 2 weken bouwen.

## Nadelen
- Bereik van een gewone nieuwe betaalde tool is bijna nul: 97,6% heeft na 3 tot 6 maanden minder dan 3 zichtbare ratings.
- Het wordt snel drukker: het aantal nieuwe betaalde tools per maand is van mei tot oktober meer dan vervijfvoudigd, en steeds meer met AI gemaakt (okt ±68%). Dat is precies de vloed waar wij in zouden zitten.
- Wij moeten eerlijk AI melden, en tools met AI-melding scoren in deze lichting slechter (0,8% tegen 3,7%, kleine aantallen). De gemeenschap van indiemakers is AI-kritisch en kan op "No AI" filteren.
- Geen verkoopcijfers zichtbaar, dus we kunnen nooit precies zien hoe het concurrenten gaat.
- De succesvolle makers (Sang Hendrix, Puck) bouwden een naam op met video's, Discord en een reeks producten; het succes komt niet uit de winkel alleen.

## Eerste idee (als we het ooit doen)
Een reeks kleine, mooie RPG Maker MZ-plugins of Aseprite-extensies van $5 tot $15, met een gratis instapversie, korte video's en een bundel. Eerst één gratis plugin om te meten hoeveel downloads itch zelf geeft.

## Oordeel
Cijfer 4. Advies: nee voor nu.
Reden: geld is aangetoond bij een handvol makers, maar een gewone nieuwe betaalde tool haalt bijna niets en de lijst groeit explosief door AI-tools, waar wij er een van zouden zijn. Beter dan BOOTH (6) of Blender (7) is het niet.
Wat het oordeel zou veranderen: een herhaalmeting over 3 maanden (scripts in `data/`) waaruit blijkt dat de lichting aug t/m okt vaker 3+ ratings haalt, of een gratis proefplugin die in een maand 500+ downloads haalt.
