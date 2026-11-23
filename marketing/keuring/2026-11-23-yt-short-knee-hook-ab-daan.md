# Keuring YouTube Shorts knie hook A en hook B (recept v3), 23 nov 2026 ±14:45 NL, Daan (opdracht hoofdchat 12:05, punt 2)
Wat ik keurde: `marketing/wachtrij/2026-11-25-yt-short-knee-hook-a.md` en `2026-11-27-yt-short-knee-hook-b.md`, video's `knee-hook-a-staand.mp4` en `knee-hook-b-staand.mp4` uit release `stem-proef-1`. Lat: `marketing/keuring/2026-11-22-yt-shorts-4.md` (eerste beeld mooi, tekst klopt met beeld). Vorige keuring van dezelfde film zonder hook: `marketing/keuring/2026-11-23-yt-short-stem.md` (groen).
Akkoord: **ja, voor allebei (groen).** Geen moet-punten; kan-punten onderaan.

## Wat ik deed
- Gedownload met `curl -L`, ffprobe (GEZIEN): beide 1080x1920 staand, 30 fps, met geluidsspoor; 56,9 s (A) en 57,1 s (B), gelijk aan `lengtes.txt`.
- `geluid_check.txt` van de release (GEZIEN): A GOED -16,4 dB, piek -1,3; B GOED -16,4 dB, piek -1,4.
- Eerste beeld van elk op 540 px, plus 13 beelden per video (0,05 / 0,9 / 1,6 / 3 / 8 / 14 / 20 / 26 / 32 / 38 / 44 / 50 / 55 s) en een uitvergroting van de export (42 / 44 / 46 s). Zelf geopend.
- Transcripten (`transcript-hook-a.srt`, `-b.srt`) gelezen tegen het beeld.
- `curl -IL https://dortus.com/yt`: 301 naar /yt/, dan 200 (GEZIEN).

## Keurformulier (REGELS, 10 vragen)
| # | A | B | Toelichting |
|---|---|---|---|
| 1 beweringen met bron | ja | ja | lijst "Left knee · Hinge · 0–120° · from rig" en "Right knee ... mirror" in beeld; schuif 120 eindstop, 132.00 met "+12° past limit" (0,9 s), 128 met "+8°", 126 met "+6°"; "Export 3MF" knop na klik op 3MF (44 s) |
| 2 geen AI-zinnen, AI-stem gemeld | ja | ja | "Voice: AI text to speech (Kokoro, Apache 2.0)" in de tekst |
| 3 geen medische claim | ja | ja | |
| 4 niets over Hats | ja | ja | |
| 5 echt beeld, geluid GOED | ja | ja | echte Blender 5.3-opname en viewport-renders uit youtube-shorts-4; bestand eindigt niet op `-geluid.mp4` (zelfde naamkwestie als bij de stem-Short, geen inhoud) |
| 6 geen persoonsgegevens, geen Gumroad-link | ja | ja | |
| 7 past bij het kanaal | ja | ja | 57 s, haak in de eerste seconde; de titel begint met de hook en niet met "Blender", dat is recept v3 en wint het van de oude voorbeeldregel |
| 8 niet bijna gelijk aan een post van 14 dagen | ja, op het randje | ja, op het randje | zie B1 |
| 9 geen AI-beeld of AI-persoon; echte hook in 1,5 s | ja | ja | A: kop "Knees bending too far?" + gesproken vraag 0,15 tot 1,84 s; B: "Still guessing?" 0,15 tot 2,05 s; beeld vanaf het eerste beeld de knie op 132° met rode boog |
| 10 schrijft als Dortus | ja | ja | "our left knee", "our add-on" |

Techniek-check YouTube Short: titels 68 en 74 tekens, geen < of >, één emoji, 5 hashtags, dortus.com/yt over te typen, geen klikbare link, geen prijs of korting: goed. `marketing/STOP` bestaat niet.

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid |
|---|---|---|---|
| A1 | Eerste beeld: groot rood label, vette vraag van twee regels, daaronder het Blender-venster met de knie en de rode boog. Binnen 0,9 s zoomt het in op de knie: boog en "+12° past limit" dan goed leesbaar op een telefoon. Op het allereerste beeld (heel venster) is de boog klein. | feit | hoog |
| A2 | Ondertitels kloppen met het beeld op alle bekeken momenten (lijst, schuif, export 3MF, eindkaart met dortus.com/yt). | feit | hoog |
| A3 | Tekst noemt "Click Joints Pro 1.1": klopt met de opname (youtube-shorts-4). Op 25 en 27 nov is 1.2.0 of 1.2.1 de versie; Figure from rig, lijst en boog zijn daarin gelijk, dus niet misleidend. | feit | hoog |
| A4 | Hook A: whisper schreef "Your figure's knees bend too far." met een punt; de stem klinkt dus mogelijk niet als vraag. De kop erboven heeft wel het vraagteken. | vermoeden | midden |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid |
|---|---|---|---|
| B1 | Vraag 8: dit worden knie-Short nummer 3 en 4 in een week (Ij-jc6t4WNo 22 nov, lcUBuWMaJ_A 23 nov). Montage, stem en hook zijn anders, en A en B zijn met opzet een A/B-proef op opdracht van de hoofdchat (recept v3 punt 4). Daarom geen moet. Als losse Shorts zouden ze rood zijn. | feit | hoog |
| B2 | Kop volgens LEESMIJ, bestand en geluid_check met datum, `vorige:` ingevuld. | feit | hoog |

## Deel C: zou een kijker blijven hangen?
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| C1 | A is de sterkere: "Knees bending too far?" noemt het probleem dat iemand die figuren print kent; "Still guessing?" zegt pas in de tweede regel waarover. Label OLD WAY past slecht bij het beeld, want het beeld toont al onze oplossing (de rode boog), niet de oude manier. (GOK) | bij B een beeld van de oude manier (print die te ver buigt of gokken in een dialoog) | midden |
| C2 | In A staat de vraag twee keer (kop en zin eronder), net als bij de stem-Short (C1 daar). | kop alleen, of zin korter | klein |

## Moet / Kan
**Moet:** geen.

**Kan**
1. Plaats A op 25 nov als eerste; B pas na de Fit test-Shorts van 26 nov, zodat er tussen twee knie-Shorts iets anders zit (B1).
2. Volgende hook-proef op een nieuw onderwerp, niet weer de knie (B1).
3. Bij een "oude manier"-hook ook echt de oude manier laten zien (C1).
4. Bestandsnaam met `-geluid.mp4`, zodat vraag 5 letterlijk klopt.
