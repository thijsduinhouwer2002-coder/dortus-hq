# Rollwright: wat haalt een nieuwe Obsidian-plugin, en wat is er nodig voor 1.000? (Chris, run 25, 9 nov 2026)

Vraag: het tussendoel van Thijs is één product met 1.000+ gebruikers op 20 december 2026. Rollwright is live sinds 8 nov. Wat halen nieuwe plugins in hun eerste weken, hoe zeldzaam is 1.000, en hoe kwamen de uitschieters eraan? Dit is ook de lat voor de meting van dag 14 en het besluit van Hans daarna (koers punt 3 in `organisatie/doelen.md`).

Bron: de geschiedenis van `community-plugin-stats.json` in obsidianmd/obsidian-releases, één momentopname per week van 1 dec 2025 tot 9 nov 2026 (GEZIEN, 50 momentopnamen). Script en ruwe cijfers per plugin: `data/nieuwe-plugins-script.py`, `data/nieuwe-plugins-2026-11-09.tsv`. "Downloads" is het getal uit dat bestand: releasebestanden, dus ook updates tellen mee; het is geen aantal gebruikers.

## 1. De winkel is in zeven maanden 3,7 keer zo vol
| Datum | Plugins in de stats |
|---|---|
| 6 apr 2026 | 2.749 |
| 18 mei 2026 | 3.865 |
| 10 aug 2026 | 6.476 |
| 12 okt 2026 | 8.739 |
| 9 nov 2026 | 10.134 (community-plugins.json: 10.143) |

GEZIEN. Sinds mei komen er netto ±130 tot ±380 nieuwe plugins per week bij, in oktober ±325 tot ±377 (12 okt tot 2 nov: 1.069 in drie weken). Van ±20 apr tot 11 mei kwam er geen enkele bij en op 18 mei 1.141 tegelijk. De lijst met nieuwe plugins in de app is dus binnen een paar dagen voorbij; daar valt Rollwright niet lang op.

## 2. Hoe zeldzaam is 1.000?
Twee metingen, want tot ±1 nov telden nepdownloads mee (DERDEN, forum.obsidian.md/t/121588; Olaf zag het register 17,5% dalen, zie `platformen/obsidian/volgend-product.md`).

**a. Eerste 6 weken, met de nep erin** (alleen plugins die met minder dan 100 downloads in hun eerste weekmomentopname stonden, groei vanaf die eerste momentopname; GEZIEN). Dat filter haalt de snelle starters eruit en de eerste 0 tot 7 dagen tellen niet mee; voor Rollwright (9 na een dag) is dit de eerlijke vergelijkingsgroep. Zonder filter, groei vanaf de eerste momentopname: 1.000+ in 6 weken bij 6,7% (mei tot juli) en 11,6% (aug tot sep); voor mei tot juli is "eerst gezien" grof, door de sprong van 18 mei:
| Instroom | Aantal | Mediaan na 6 weken | 90% | 95% | 1.000+ in 6 weken |
|---|---|---|---|---|---|
| mei tot juli 2026 | 2.652 | 113 | 384 | 576 | 45 (1,7%) |
| aug tot sep 2026 | 1.761 | 132 | 861 | 1.365 | 139 (7,9%) |

**b. De eerste schone week, 2 tot 9 nov** (downloads in die ene week, alle plugins die in aug tot okt in de stats kwamen en nog bestaan; GEZIEN, nagerekend door de controleur):
| Instroom | Aantal | Mediaan | 75% | 90% | 95% | 24+ per dag (168 per week) |
|---|---|---|---|---|---|---|
| aug | 1.082 | 14 | 38 | 82 | 152 | 51 (4,7%) |
| sep | 1.033 | 12 | 30 | 74 | 131 | 38 (3,7%) |
| okt (tot 27 okt) | 1.405 | 16 | 32 | 76 | 126 | 45 (3,2%) |

Alleen de trage starters (eerste momentopname onder 100): 31 (3,1%), 24 (2,5%) en 26 (2,1%) boven 168 per week, mediaan 11 tot 14.

Wat dit zegt: voor 1.000 downloads op 20 december moet Rollwright vanaf nu ±24 per dag halen ((1.000 min 9) gedeeld door 41 dagen), zes weken lang. In de schone week haalt 3 tot 5% van de nieuwe plugins dat tempo, en 2 tot 3% van de trage starters (GEZIEN). Twee kanten: plugins van 1 tot 3 maanden oud zijn al over hun eerste piek heen (dat drukt hun cijfer), maar zes weken volhouden is strenger dan één week halen. En 1.000 downloads is minder dan 1.000 gebruikers, want updates tellen mee, ook die van Rollwright zelf; de echte lat voor 1.000 gebruikers ligt dus hoger (GOK hoeveel). De gewone nieuwe plugin haalt ±2 per dag. De hoge cijfers van vóór november (7,9% boven 1.000 in 6 weken) zijn deels nep en mogen niet als lat dienen.

## 3. De buren van Rollwright in de schone week
| Plugin | Wat | In de stats sinds | Totaal 9 nov | 2 tot 9 nov | Bron |
|---|---|---|---|---|---|
| obsidian-dice-roller | de grote | | 289.245 | +898 (±128 per dag) | GEZIEN |
| atlas-vtt | gevechtskaarten, fog of war, dobbelstenen | 21 sep | 24.796 | +2.983 (±426 per dag) | GEZIEN |
| sheetsmith | karakterbladen voor elk rollenspel | 7 sep | 1.980 | +140 | GEZIEN |
| dice-rolls | dobbelstenen inline, zelfde syntax als Dice Roller | 19 okt | 413 | +185 | GEZIEN |
| onednd-character-sheet | D&D 2024-karakterblad | 26 okt | 269 | +119 | GEZIEN |
| fifth-edition-character-sheet | 5e-karakterblad | 19 okt | 445 | +89 | GEZIEN |
| dice-tray | dobbelstenen | ±2 nov | 105 | +28 | GEZIEN |
| dice-table | willekeurige uitslag uit Markdown-dobbeltabellen | 19 okt | 615 | +18 | GEZIEN |
| perhaps | willekeurige tabellen in platte tekst | 31 aug | 914 | +14 | GEZIEN |
| rollwright | | 9 nov | 9 | | GEZIEN |

Opvallend: de twee plugins die het dichtst bij Rollwright zitten (dice-table en perhaps, willekeurige tabellen) halen nu ±2 per dag. Dice Table had 597 op 2 nov en daarna nog maar 18 erbij: de vroege groei was waarschijnlijk vooral nep (GOK). De vraag naar "nog een dobbel- of tabelplugin" is klein; Dice Roller krijgt nog steeds het meeste.

## 4. Hoe kwamen ze aan hun downloads? (onderzoeker, 9 nov; GEZIEN met curl tenzij DERDEN)
- **Atlas VTT, de enige echte uitschieter.** Gemaakt door Fabian Urbanek als scriptieproject (GEZIEN, https://atlas-vtt.dev/about); geen eerder product of kanaal van hem gevonden (GOK dat hij geen publiek had). Wat de groei verklaart: een eigen YouTube-kanaal (5,74K abonnees, 2 video's) met "Obsidian Is Now a Free Virtual Tabletop", **808K keer bekeken**, ±begin oktober (GEZIEN, https://www.youtube.com/@AtlasVTT/videos), en een stuk op XDA Developers op 7 okt (GEZIEN, https://www.xda-developers.com/atlas-vtt-turns-obsidian-full-virtual-tabletop-free-use-offline/), daarna overgenomen door andere sites (DERDEN, daily.dev, geeky-gadgets.com). Een Discord van ±1.478 leden en bijna elke 2 tot 4 dagen een nieuwe versie hielden het vast (GEZIEN). Geen bericht op het Obsidian-forum of Reddit gevonden. Gratis en open source; een Patreon en een gesloten bèta "Atlas Online" zonder prijs (GEZIEN). Hacker News kwam pas op 31 okt, van iemand anders, 4 punten (GEZIEN). De sprong in de stats past erbij: 320 op 28 sep, 8.248 op 5 okt.
- **Sheetsmith, One DnD Character Sheet, Dice Table:** geen aankondiging gevonden op forum, Reddit, HN of in nieuwsbrieven; One DnD heeft één YouTube-uitleg op een kanaal met 2 abonnees (372 keer bekeken). Hun aantallen komen vermoedelijk van zoeken in de pluginlijst ("character sheet", "D&D Beyond") (GOK).
- **Dice Rolls:** de maker heeft 32 plugins die in elke README naar elkaar verwijzen, en de plugin richt zich op overstappers van Dice Roller (zelfde syntax, importfunctie) (GEZIEN).

## 5. Wat dit betekent voor Rollwright
1. **Zonder iets bijzonders: ±10 tot 30 downloads per week** (de mediaan en het 75%-punt van de schone week), dus ±70 tot 190 downloads op 20 december (9 plus 5,9 weken keer 10 tot 30; GOK op GEZIEN). Het forumbericht gaf in een dag 19 keer bekeken en geen meetbare downloads (GEZIEN, `cijfers.md`).
2. **1.000 op 20 december vraagt de top 3 tot 5% (en meer dan dat voor 1.000 echte gebruikers).** De enige weg daarheen die ik zag: één video voor rollenspelers (niet voor Obsidian-gebruikers) met een belofte die nieuw klinkt, plus techpers. Op het Obsidian-forum heb ik geen van deze plugins zien opgaan, Reddit was niet te controleren (403); of r/ObsidianMD vandaag (13:45 UTC) dat wel doet, is de eerste echte test.
3. **Atlas VTT komt op ons terrein.** In de bèta zit "Random tables > New table": tabellen plakken uit pdf, spreadsheet of website en rollen (GEZIEN, README van atlas-vtt). Het zit alleen in de bèta (via BRAT), maar met 24.796 downloads en een eigen publiek kan "tabellen rollen in Obsidian" daar een gewone functie worden. Wat Rollwright dan nog onderscheidt, is het moment van de natuurlijke 20 en de skins, niet de tabellen zelf.
4. **De lat voor Hans op dag 14 (±22 nov), in downloads uit de stats:** haalt Rollwright na Reddit en Discord in de schone weken 24+ per dag, dan zijn 1.000 downloads haalbaar en is het "er vol op" (voor 1.000 gebruikers is iets meer nodig). Blijft het onder ±5 per dag (ongeveer het 75%-punt), dan is het ook met de geplande plekken een gewone plugin, en hoort de tijd naar een product waar al voor betaald wordt (koers punt 3). Daartussen: de video-route proberen (advies 35) en op dag 21 opnieuw meten.

## Voorbehoud
- Downloads zijn geen gebruikers: updates tellen mee, en een plugin die vaak een nieuwe versie uitbrengt (Atlas: 51 versies) telt bestaande gebruikers vaker. Het echte aantal gebruikers van Atlas is dus lager dan 24.796 (GOK hoeveel).
- Eén schone week is een kort venster; de nep kan ook na 1 nov nog niet helemaal weg zijn.
- Reddit was met curl niet te lezen (403) en is niet omzeild; een Reddit-draad kan gemist zijn. Op YouTube waren datum en reacties van de video niet te zien (captcha).

## Dagmeting downloads (één keer per dag, besluit Thijs 9 nov 12:55)
Bron: `community-plugin-stats.json` (ververst ±00:15 UTC), sleutel `rollwright`. Lat uit deel 5: 24+ per dag is "er vol op", onder ±5 per dag is parkeren terecht. Nulpunt 9 (9 nov 00:15).

| Datum (gemeten) | Downloads totaal | Erbij sinds vorige dag | Listing "installations" | Forumdraad (bekeken) | Bron |
|---|---|---|---|---|---|
| 9 nov, 14:45 UTC | 9 (0.2.0 t/m 0.3.2; 0.3.3 en 0.3.4 nog niet in de stats) | 0 (nog geen nieuwe ververs na 00:15) | 6 | 22, 1 bericht, 0 likes | GEZIEN |
