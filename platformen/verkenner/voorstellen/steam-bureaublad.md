# Voorstel: Steam, kleine bureaublad-apps (Desktop Companion en Idler)

Vera, verkenner, 7 nov 2026 run 21:33 UTC. Advies: **ja, als proef met één klein betaald product. Cijfer 6.** Nagekeken door een controleur (6 correcties verwerkt, zie onder).

## Wat is het
Op Steam is sinds 2024 een nieuwe soort klein product ontstaan: apps die onderaan of in een hoek van het scherm blijven staan terwijl je werkt (een boerderijtje, een kat, een focus-timer met een tuin). Voorbeelden: Rusty's Retirement, Spirit City: Lofi Sessions, Bongo Cat. Steam heeft er sinds kort een eigen label voor: **Desktop Companion**. Verwant label: **Idler**. Steam verkoopt, rekent af en betaalt de maker uit (30% afdracht).

Steam is geen nieuw platform, maar deze hoek ervan is wel nieuw en groeit snel. Daarom gemeten.

## Hoe gemeten (GEZIEN)
- Lijst via de openbare zoekpagina van Steam (`store.steampowered.com/search/results/`, robots.txt verbiedt dit niet), per label, nieuwste eerst, met datum, prijs en aantal reviews uit de zoekresultaten. Script: `data/steam-zoek-script.py`, data: `data/steam-companion-2026-11-07.json` (alle 399 Desktop Companion-games) en `data/steam-idler-2026-11-07.json` (de 2.600 nieuwste Idler-games, terug tot juli 2025).
- Lichting: uitgekomen 1 mei t/m 31 aug 2026, dus nu 2 tot 6 maanden oud. Analyse: `data/steam-analyse-script.py`.
- Makers per app via de open appdetails-API: `data/steam-details-script.py`, data `data/steam-companion-makers-2026-11-07.json`.
- **Grens van de meting:** Steam toont in de zoekresultaten geen reviewaantal onder de 10. "0" betekent dus 0 tot 9 reviews. Het getal is alleen Engels als Steam genoeg Engelse reviews heeft (Rusty's Retirement 6.623), en anders het totaal over alle talen (Birdwatching Notebook 1.802). Bij apps met veel Aziatische kopers ligt het totaal veel hoger (The NOexistenceN of Lilith: 767 Engels, 2.842 totaal). De cijfers zijn dus eerder te laag dan te hoog.
- **Prijzen** zijn de actuele prijzen van 7 nov, inclusief lopende kortingen (8 van de 95 betaalde Desktop Companion-apps staan in de korting). De mediaan blijft $4,99.
- De endpoint `appreviews` (exacte aantallen) stuurt vanaf hier door naar de voorpagina; niet bruikbaar.

## Bereik en geld (GEZIEN, reviews)
| Lichting mei t/m aug 2026 | Aantal | Mediaan reviews | 75% | 90% | 10+ reviews | 100+ reviews |
|---|---|---|---|---|---|---|
| Desktop Companion, betaald | 95 | 10 | 29 | 94 | 54% | 9% |
| Desktop Companion, gratis | 16 | 51 | 680 | 759 | 81% | 38% |
| Idler, betaald | 730 | onder 10 | 30 | 133 | 43% | 14% |
| Idler, gratis | 109 | 27 | 58 | 230 | 83% | 19% |

Mediaanprijs betaald: $4,99 (GEZIEN, beide labels).

## Van reviews naar geld
- Gangbare omrekening voor games uit 2023 en later: **±30 verkopen per review, bandbreedte 20 tot 40** (DERDEN: [Steam Page Analyzer, 16 jun 2026](https://www.steampageanalyzer.com/blog/steam-review-to-sales-multiplier), op basis van Birkett 2018, GameDiscoverCo 2020 (mediaan 38 voor 2020) en VG Insights; zij zeggen zelf dat 30 een werkcijfer is, geen onderzoek).
- Netto naar de maker per verkoop: prijs × 0,7 (Steam) en dan nog kortingen, regioprijzen, btw en terugbetalingen. Ik reken met **±50% van de prijs** (GOK).
- Dan voor een betaalde Desktop Companion-app van 2 tot 6 maanden oud (GOK, rekensom):
  - mediaan 10 reviews ≈ 300 verkopen ≈ **$750 netto tot nu toe**
  - 75% (29 reviews) ≈ 870 verkopen ≈ **$2.200**
  - 90% (94 reviews) ≈ 2.800 verkopen ≈ **$7.000**
  - top: Birdwatching Notebook (Biekka Games, zelf uitgegeven, $9,99) 1.802 reviews ≈ 54.000 verkopen ≈ **$270.000**
- Ter vergelijking (DERDEN): de mediaan van álle Steam-games is $1.100 tot $3.500 bruto over de hele levensduur, en bijna de helft van de 2025-games had eind 2025 hooguit 10 reviews (DERDEN: [Steam Page Analyzer, sep 2026](https://www.steampageanalyzer.com/blog/median-steam-game-2026)). Deze hoek doet het dus ongeveer zoals Steam gemiddeld (mediaan ±10 reviews; hier 54% met 10+, van alle 2025-games ±51%), maar dan met een veel kleiner product dat sneller te maken is. De helft blijft onder de 10 reviews.

## Kleine makers (GEZIEN)
- Van de 95 betaalde Desktop Companion-apps uit de lichting zijn er **82 zelf uitgegeven** (maker = uitgever; 83 als je een spatiefout in de data meetelt). Bijna alle makers hebben 1 app in de lichting (Pinch Games 4, PiqFocus 3, tatsumaki 2).
- 7 van de top 12 zijn zelf uitgegeven (onder meer Biekka Games, okfinegames, Little Lantern, Sos Sosowski); 5 hebben een uitgever (Playsaurus, Crow Interactive, Flyhigh Works, Stay2Busy, Level Up Gaming).
- Dit is het sterkste bewijs van geld bij kleine makers dat ik tot nu toe zag: niet één uitschieter, maar de helft van een hele lichting die naar schatting honderden dollars ophaalt.

## Drukte (GEZIEN)
- Desktop Companion, nieuwe per maand 2026: apr 18, mei 17, jun 18, jul 42, aug 34, sep 57, okt 67 (nov tot 7 nov al 38, deels aangekondigde datums). **Ruwweg verdubbeld tot verdriedubbeld sinds juni.** Dat de kans nu ligt en het over een jaar vol is, is een GOK op basis van deze groei.
- Idler: ±150 per maand in het voorjaar, ±260 tot 350 per maand sinds juli. Al druk.
- Steam totaal: ±20.000 games in 2025 (DERDEN, zelfde bron).

## Vindbaarheid
Steam laat nieuwe games zien op basis van verlanglijsten (wishlists) vóór de lancering, labels, "More like this" bij bekende games (Rusty's Retirement) en evenementen als Steam Next Fest (DERDEN, algemeen bekend, niet zelf gemeten). Daarnaast TikTok en YouTube. Een eigen label voor deze hoek helpt: kopers die Rusty's Retirement hebben, krijgen nieuwe Desktop Companion-apps te zien (GOK).

## Kosten, regels en stappen voor Thijs (DERDEN)
- **$100 per app** (Steam Direct Fee), niet terug te krijgen, wel verrekend zodra de app $1.000 omzet haalt ([partner.steamgames.com/doc/gettingstarted/appfee](https://partner.steamgames.com/doc/gettingstarted/appfee)). Dat is geld uitgeven: Thijs beslist.
- Een Steamworks-account met belasting- en bankgegevens en identiteit: alleen Thijs kan dat.
- **AI moet gemeld worden** op de winkelpagina als plaatjes, geluid of tekst met AI gemaakt zijn ([contentsurvey](https://partner.steamgames.com/doc/gettingstarted/contentsurvey)). Mag wel, maar kopers zien het. Niet verstoppen.
- Een winkelpagina moet een tijd "binnenkort" staan om verlanglijsten te verzamelen (GOK op duur, ±2 tot 8 weken is gangbaar).

## Past het bij ons
- **Bouwen:** een klein venster dat onderaan het scherm blijft staan, met een eenvoudige spellus (groeien, verzamelen, tijd bijhouden). In Godot of een vergelijkbare engine goed te doen in 1 tot 3 weken (GOK). Testen kan op GitHub Actions met Windows-runners.
- **Het echte risico is uiterlijk en gevoel.** Deze apps verkopen op hun plaatjes en sfeer (pixelart, schattige dieren). Dat past bij de nieuwe regel van Thijs dat een product moet opvallen en mooi moet zijn, maar het is ook het moeilijkste deel voor ons. Met AI gemaakte plaatjes moet gemeld worden en kunnen reviews kosten (GOK).
- Het is een spelletje, geen tool. Een **focus- en werkhulp in deze vorm** (taken afvinken laat je tuintje groeien, Pomodoro met een dier) past het best bij wat Dortus kent en spreekt ook werkende mensen aan. Focus Grove ($10,99, 196 reviews, GEZIEN) laat zien dat dit verkoopt.

## Eerste idee
"Desk-tuin": een smalle strook onderaan het scherm waar een klein dorp of tuin groeit terwijl je werkt. Pomodoro-timer, taken afvinken geeft groei, rustig geluid, geen menu-gedoe. $4,99. Eerst een winkelpagina met mooie plaatjes en een trailer om verlanglijsten te meten, pas daarna afbouwen. Bij minder dan ±500 verlanglijsten voor de lancering (GOK) heroverwegen.

## Voor en tegen
Voor:
- Geld bij kleine makers aantoonbaar, breed over de lichting, niet alleen een uitschieter.
- Steam rekent af, betaalt uit, en heeft een enorm publiek dat betalen gewend is.
- Een nieuwe, snel groeiende hoek met een eigen label: nu nog vroeg.
- Producten zijn klein, dus meerdere producten per jaar kan.

Tegen:
- $100 per app en een Steamworks-account: Thijs moet betalen en inloggen.
- Uiterlijk bepaalt alles, en dat is ons zwakste punt; AI-melding verplicht.
- Drukte verdubbelt; over een jaar mogelijk vol zoals Idler.
- Onder de 10 reviews zie ik niets, dus het onderste deel van de verdeling is onbekend. Geld is een schatting via een omrekening (GOK met DERDEN-basis), geen gemeten bedrag.

## Cijfer en advies
**Cijfer 6. Ja, als proef, met eerst een winkelpagina om verlanglijsten te meten.** Dit is na Blender de beste geldplek die ik zag: de mediaan betaalde Desktop Companion-app haalt naar schatting $750 in de eerste maanden, een op de vier ±$2.200, en de meeste makers zijn klein en zelf uitgegeven. Eerlijk erbij: 46% (44 van 95) blijft onder de 10 reviews, dus naar schatting onder $750 netto, en daar gaan de $100, de plaatjes en 1 tot 3 weken werk nog af. Het geld zit breed, maar niet vanzelf. Het cijfer is geen 7 omdat uiterlijk het verschil maakt en dat voor ons nog onbewezen is, en omdat het $100 per app kost.

Wat er nog gemeten kan worden: exacte reviewaantallen in alle talen (Steam-API `appreviews` vanaf een andere plek, of SteamDB), en verlanglijst-cijfers van kleine makers (sommigen delen die op Reddit of in postmortems). Wat dit verandert naar nee: als de lichting sep en okt 2026 bij herhaalmeting over 4 weken duidelijk slechter scoort dan mei t/m aug (teken dat het vol raakt). Herhaalmeting: `python3 data/steam-zoek-script.py 1320952 uit.json 3000` en dan `steam-analyse-script.py` met nieuwe datums.

## Nakijken
Controleur 7 nov run 21:33: tabel, mediaanprijs, geldsommen, bronnen en 82 van 95 kloppen; steekproef van 9 app-pagina's gelijk (reviews, datum, prijs). Gecorrigeerd: maandtellingen (eerste versie kwam uit een ruimere zoekopdracht), Engels of totaal per app, kortingsprijzen, de vergelijking met Steam gemiddeld (gelijk, niet beter), top 12 met 5 uitgevers, en de 46% onder de 10 reviews. Controleur gaf 5 tot 6; ik houd 6 omdat het geld breed over een hele lichting kleine makers zit, wat ik op geen ander platform buiten Blender zag. Akkoord na correcties.
