# Productkans Overwolf: populaire pc-games zonder of met een zwakke Overwolf-app

Vera, 9 nov 2026 run 09:31 (Amsterdam). Nagekeken door een controleur: akkoord, 4 correcties verwerkt. Overwolf heeft geen manager; Hans weegt dit mee bij het platformvoorstel `voorstellen/overwolf.md` (cijfer 6, nog niet klaar).

## Wat ik zocht
Games waar Overwolf game-data voor levert (Game Events), met veel spelers, maar zonder of met een zwakke eigen app. Bij een nieuwe game is de lijst kort en sta je meteen bovenaan (zie voorstel). Plus: opnieuw zoeken naar wat een app per gebruiker opbrengt.

## Wat ik mat
- GEZIEN: de openbare statuslijst van Overwolf Game Events (`game-events-status.overwolf.com/gamestatus_prod.json`): 77 regels, ±68 echte games (een paar zijn PBE- of launcher-varianten). Data: `data/overwolf-gep-games-2026-11-09.json`.
- GEZIEN: alle 35 game-pagina's van de web-appstore (`/browse-by-game/<game>`), 239 unieke apps. Apps die op meer dan 3 game-pagina's staan (Outplayed, Insights Capture, Hone, overlays) tellen als algemeen, de rest als game-specifiek. Downloads uit de meting van 8 nov plus 31 nieuwe pagina's (29 gaven geen data, verborgen of verwijderd). Data: `data/overwolf-per-game-2026-11-09.json`, `data/overwolf-apps-extra-2026-11-09.jsonl`, script `data/overwolf-gamepaginas-script.py`.
- GEZIEN: spelers nu op Steam via de open Steam-API, 9 nov ±08:55 UTC (maandagochtend Europa, dus laag; vergelijk onderling, niet als piek). Data: `data/overwolf-steam-spelers-2026-11-09.json`, script `data/steam-spelers-script.py`.
- GEZIEN, losse zoekacties: apps die niet op een game-pagina staan maar wel in de winkel (via zoekmachine gevonden, pagina zelf gelezen).

## Belangrijkste les eerst: de game-pagina's zijn niet compleet
De web-appstore toont maar 35 game-pagina's, terwijl Game Events ±68 games dekt. Apps voor de andere games bestaan wel, maar staan op geen enkele game-pagina. GEZIEN voorbeelden: AlecaFrame (Warframe) 1.140.024 downloads, Once Human Map 98.423, Wuthering Waves Map 90.449, Overframe (Warframe) 59.260, Spire Codex (Slay the Spire 2) 23.907, Baldur's Gate 3 Character Builder 5.664. Gevolg: de 234 apps van de meting van 8 nov zijn niet de hele winkel. "Geen app gevonden" betekent hier dus alleen "niet gevonden op de website en niet via de zoekmachine". De zoek-API van de winkel (`store-website-internal-api.overwolf.com`) was vanaf hier niet bereikbaar; niet omzeild.

## Uitkomst per kandidaat (game met Game Events, weinig of zwakke apps)
| Game | Steam nu (9 nov 08:55 UTC) | Beste Overwolf-app die ik vond | Oordeel |
|---|---|---|---|
| Slay the Spire 2 | 39.543 (30 dagen gem. 55.888, piek 103.573, steamcharts) | Spire Codex, 23.907 downloads, 1 rating | Overwolf-top zwak, maar Untapped.gg (bedrijf achter de grote Hearthstone- en MTGA-trackers) heeft een gratis eigen StS2-overlay. Harde regel: sterke speler, overslaan |
| Warframe | 48.531 | AlecaFrame 1.140.024, 83 ratings, 4,4, bijgewerkt okt 2026 | Sterke, actieve nummer één. Overslaan |
| Overwatch 2 | 22.267 (plus Battle.net, niet te zien) | geen eigen app gevonden, alleen algemene (zoek-API niet bereikbaar, zes logische app-namen gaven 404; een app buiten de game-pagina's kan ik niet uitsluiten, GOK) | Gat, maar Overwatch speelt vooral via Battle.net; Blizzard staat apps toe. Open |
| Baldur's Gate 3 | 18.003 | Baldurs Map (AzerPUG) 267.665 op 8 nov (±268.000 op 9 nov), 2,9 sterren, 15 ratings; rest onder 6.000 | Zwakke top, maar singleplayer en de game is uit 2023; veel gratis webkaarten. Klein |
| HELLDIVERS 2 | 15.622 | geen Overwolf-app gevonden (zelfde voorbehoud als Overwatch 2, GOK) | Gat. Gebruikers hebben gratis web- en telefoonapps voor de galactische oorlog (DiversHub, Helldivers Companion). Open |
| ARK: Survival Ascended | 15.190 | Arkbuddy 82.809; wikily.gg noemt een eigen in-game app | Bezet door een maker met een reeks |
| Battlefield 6 | 14.548 | Tracker.gg (algemene app voor veel games) 238.302 | Geen eigen app, maar Tracker Network (groot bedrijf) dekt de stats al. Zwak gat |
| Once Human | 13.679 | Once Human Map (Leon Machens) 98.423, bijgewerkt 8 nov | Sterke seriemaker (th.gl, 6 kaarten gezien). Overslaan |
| R.E.P.O | 13.049 | geen Overwolf-app gevonden | Coöp-feestspel, weinig behoefte aan een tracker (GOK) |
| Street Fighter 6 | 12.747 | geen Overwolf-app gevonden | Vechtspel; frame-data-apps bestaan op het web (GOK) |
| Monster Hunter Wilds | 10.432 | geen Overwolf-app gevonden | HunterPie, gratis en open source buiten Overwolf, is de vaste tool. Overslaan |
| Wuthering Waves | 6.967 | Wuthering Waves Map (Leon Machens) 90.449 | Bezet door dezelfde seriemaker |

Ter vergelijking, waar Overwolf wel werkt (GEZIEN): deckbuilder-trackers voor Hearthstone (HearthArena 4.710.330, Firestone 3.811.979, die laatste van één maker), kaarten voor survival-games (Palworld Interactive Map 516.956), trackers voor shooters (Valorant Tracker 19.748.646).

## Seriemakers: het echte patroon
GEZIEN: Leon Machens (th.gl) heeft 6 kaarten die ik zag (Palworld 516.956, Once Human, Wuthering Waves, New World, Sons of the Forest, Diablo 4), samen ±1,1 miljoen downloads. AzerPUG heeft er 7 (D4 Interactive Map 393.713, WoW Info, Paldeck, Baldurs Map, Starfield Companion, CoD Completionist, Mortal Kombat Kombos). Albérico Dias Barreto Filho doet het voor shooters (Fortmapp, Economy Tool, DeepRivals, DynForge, Roblox Backpack Tracker). Een nieuwe grote game wordt dus snel bezet door deze makers. Het gat zit niet bij bestaande games, maar in de eerste weken na een nieuwe lancering, en dan race je tegen hen.

## Geld (opnieuw gezocht, niets nieuws)
- Geen nieuw openbaar bedrag van een kleine Overwolf-maker gevonden. TrustMRR (12.304 profielen, meting 8 nov): 0 treffers op "overwolf".
- Wel indirect (GEZIEN): de seriemakers bouwen steeds meer apps met advertenties (AzerPUG 7, Leon Machens 6, Albérico 5 die ik zag). Dat doe je niet als het niets oplevert, maar het is geen bewijs met een bedrag.
- De vraag van het voorstel blijft dus open: wat brengt een app met 1.000 tot 10.000 gebruikers per maand op.

## Het gat in één zin
Bij bestaande games is er geen echt gat met geld: waar veel spelers zijn, zit een sterke speler (Untapped, AlecaFrame, HunterPie), een algemene app van een groot bedrijf (Tracker Network bij Battlefield 6) of een seriemaker; open blijven Overwatch 2 en Helldivers 2, waar geen Overwolf-app is maar wel gratis alternatieven buiten Overwolf.

## Eerste productidee (als Hans Overwolf toch wil)
Geen app voor een bestaande game, maar klaarstaan voor de eerstvolgende grote lancering met Game Events: een kaart- en voortgangsapp die we in een week kunnen uitbrengen, met advertenties. Als proef eventueel een Helldivers 2-overlay (galactische oorlog, opdrachten, stratagems) omdat daar niets op Overwolf staat. Wie betaalt: adverteerders via Overwolf (70% voor de maker), hoeveel is onbekend.

## Cijfer en advies
**Cijfer 3, nee voor nu.** De harde regel slaat bij bijna elke grote game toe, het geld per gebruiker is nog steeds niet aangetoond, en de echte kans (vroeg zijn bij een nieuwe game) is een race tegen ervaren seriemakers. Het platformcijfer van Overwolf (6) zakt hierdoor niet, maar de meting van 8 nov telde te weinig apps: de winkel is drukker dan 234.

Herhaalmeting: bij de volgende grote lancering die in de statuslijst van Game Events verschijnt (lijst vandaag opgeslagen, verschil maken met `data/overwolf-gep-games-2026-11-09.json`): na 2 en 6 weken tellen hoeveel apps er zijn en van wie. Blijft een game met 50.000+ spelers 4 weken zonder app van een seriemaker, dan cijfer 5 en melden bij Hans.

Bronnen: https://game-events-status.overwolf.com/gamestatus_prod.json, https://www.overwolf.com/browse-by-game/view-all, https://www.overwolf.com/app/alejandro_cabrerizo-alecaframe, https://overwolf.com/app/ptrlrd-spire_codex, https://sts2.untapped.gg/, https://steamcharts.com/app/2868840, https://www.overwolf.com/app/tracker_network-tracker.gg, https://hunterpie.com/, https://api.steampowered.com (GetNumberOfCurrentPlayers).
