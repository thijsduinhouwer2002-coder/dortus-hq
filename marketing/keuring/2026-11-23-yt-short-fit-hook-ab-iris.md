# Keuring YouTube Shorts Fit test hook A en hook B (regisseur-2), 23 nov 2026 ±17:45 UTC, Iris (opdracht hoofdchat 12:05, punt 1)
Wat ik keurde: `marketing/wachtrij/2026-11-26-yt-short-fit-hook-a.md` en `2026-11-28-yt-short-fit-hook-b.md`, video's `fit-groot-a.mp4` en `fit-groot-b.mp4` uit release `regisseur-2`. Lat: zelfde als de Hats-schermen en `marketing/keuring/2026-11-23-yt-short-knee-hook-ab-daan.md`.
Akkoord: **ja op beeld en plezier, maar nog niet inplannen: één moet (M1, Pro 1.2 staat nog niet op Gumroad).** Status van beide: `wacht` tot M1 weg is; daarna mag de hoofdchat of de Keurder van Roep ze groen zetten zonder nieuwe beeldkeuring.

## Wat ik deed
- Gedownload met `curl -L`; sha256 gelijk aan `SHA256SUMS.txt` van regisseur-2 (A 7532c1b5..., B 7af81aad..., GEZIEN).
- ffprobe (GEZIEN): beide 1080x1920, 30 fps, h264 plus aac; 44,97 s (A) en 44,67 s (B).
- 15 beelden per video (0,05 tot 44 s) op 360 breed, plus beeld 14 s en 34 s op volle maat, zelf geopend met Read. Helderheid van de laatste 2,5 s gemeten: geen zwart einde.
- URL: GET met range geeft 206 (bestand openbaar). Let op: `curl -I` geeft 401 bij de S3-doorverwijzing van GitHub, omdat de ondertekende link alleen GET toestaat; geen fout in het bestand, wel iets voor de Maker als hij met `-I` toetst.
- `curl -IL https://dortus.com/yt`: 200 op /yt/ (GEZIEN). `marketing/STOP` bestaat niet.

## Keurformulier (REGELS, 10 vragen)
| # | A | B | Toelichting |
|---|---|---|---|
| 1 beweringen met bron | ja | ja | knoppen "Fit test: ball" en "Fit test: hinge" in beeld en aangeklikt, vijf stukken 0.10 tot 0.30 met nummer, veld Clearance; bron `platformen/blender/pro-1.2.0.md` regel 8 |
| 2 geen AI-zinnen, AI-stem gemeld | ja | ja | "Voice: AI text to speech (Kokoro, Apache 2.0)" |
| 3 geen medische claim | ja | ja | |
| 4 niets over Hats | ja | ja | |
| 5 echt beeld, geluid GOED | ja | ja | viewport-render en schermopname Blender 5.3; geen figuur meer in beeld (MakeHuman weg, wens Thijs) |
| 6 geen persoonsgegevens, geen Gumroad-link | ja | ja | |
| 7 past bij het kanaal | ja | ja | 45 s, één idee, haak in de eerste seconde |
| 8 niet bijna gelijk aan post van 14 dagen | ja | ja | geen Fit test-Short in `commercie/geplaatst.md` |
| 9 geen AI-beeld, echte hook in 1,5 s | ja | ja | A: "Which gap fits?" plus stem vanaf beeld 1; B: "Guessing the gap?"; strips bewegen (zoom) vanaf beeld 1 |
| 10 schrijft als Dortus | ja | ja | |

Techniek-check: titels 63 en 60 tekens, één emoji, 5 hashtags, dortus.com/yt over te typen, geen klikbare link, geen prijs: goed.

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| A1 | De Short zegt "In Click Joints Pro 1.2, press Fit test". Op Gumroad staat nog 1.1; 1.2.1 en 1.2.2 wachten op Thijs (bord 23 nov 17:45). Wie vandaag koopt, vindt de knop niet. | feit | hoog | versie op de Gumroad-pagina zodra Thijs plaatst |
| A2 | Beelden tonen echt wat de stem zegt: klik op beide knoppen, vijf stukken met nummer, het veld Clearance oplichtend. | feit (GEZIEN) | hoog | |
| A3 | Bij "default 0.2 mm" valt de waarde van het veld Clearance rechts buiten de uitsnede: je ziet het veld, niet het getal 0.2. Niet fout, wel een gemiste kans. | feit (beeld 34 s volle maat) | hoog | |

## Deel B: regels
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| B1 | AI-stem gemeld; YouTube Studio bij AI-gebruik op "Yes" zetten bij plaatsen. | feit | hoog | REGELS regel 33 |
| B2 | "Measured in Blender, not print tested by us yet" onder elk Blender-beeld en in de tekst. | feit | hoog | eerlijk |

## Deel C: zou een kijker het leuk vinden?
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| C1 | Het eerste beeld is sterk: oranje en blauwe strips schermvullend, grote vraag, beweging. Veel beter dan de regisseur-1-versie. | zo houden | |
| C2 | Na 2,5 s val je van kleur naar grijze stukken op donker scherm, en dat blijft zo tot het eind (op de UI na). Daar haakt een kijker af (GOK). | ook de middenscènes met de oranje/blauwe render, of de strip kleuren in de viewport | midden |
| C3 | De stukken zien eruit als dichte cilinders: je ziet nergens de kogel of het scharnier binnenin, dus "joint" blijft abstract. | één doorsnede of exploded view van één stuk | midden |
| C4 | Waarde 0.2 in het veld Clearance niet in beeld (A3). | uitsnede iets naar rechts | klein |
| C5 | Op 14 s zijn de nummers op de stukken nog vaag; op 22 s pas leesbaar. | de scène "Every joint numbered" meteen op de dichtbij-opname | klein |
| C6 | Ondertitels staan bij scène 3 en 6 over panelregels; leesbaar door de rand, wel druk. | ondertitel iets lager of donkere band | klein |

## Moet (blokkeert inplannen)
- **M1:** pas inplannen als Pro 1.2.x op Gumroad staat (of de zin "In Click Joints Pro 1.2" klopt voor een koper van vandaag). Geen nieuwe beeldkeuring nodig.

## Kan (mag later, voor de volgende versie)
- C2 tot C6. Voor deze twee niet nodig.
