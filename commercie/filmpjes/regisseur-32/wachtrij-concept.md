# Zoekvideo Click Cuts: How to split a model for 3D printing in Blender (#332)

Concept van de Regisseur, za 28 nov 2026 ±05:40 NL. Gaat naar `marketing/wachtrij/` zodra de film met de stem van Max klaar en gekeurd is (Klaar als 3), met datum ná Click Cuts 1.1 live. De hoofdstuktijden komen dan uit `cuts-lang-hoofdstukken.txt` in release `regisseur-32`; hieronder staan de namen met tijden van proef r3 (Kokoro, GOK voor Max).

- status: concept (wacht op `cuts-lang-elevenlabs.mp3`, daarna workflow regisseur-32, keuring Daan)
- kanaal: yt-lang
- soort: video
- product: click-cuts
- issue: #332
- bestand: release `regisseur-32`, `cuts-lang.mp4` (nog niet gemaakt)
- lengte: doel 1:30 tot 2:00, liggend 1920x1080, 30 bps
- thumbnail: `ontwerp/cuts-yt-zoek/beelden/yt-zoek-r1a-1280x720.jpg` (Beeldmaker), GESLAAGD (`organisatie/blindtest/uitslag/click-cuts-yt-zoek-2026-11-28-1544.md`, Gemini 1,5 tegen de echte top 3), Daan ja #391. Vervangt thumb-a (die slaagde ook, plek 2).
- doel: https://dortus.com/click-cuts/ (de gids met de Get-knop naar Gumroad, live, curl 27 nov 15:35 GEZIEN door de Productbouwer). Er is nog geen eigen meetadres voor Click Cuts zoals /yt/ voor Pro; /yt/ wijst naar Pro en past dus niet.
- plaatsen: pas als de hoofdchat Click Cuts 1.1 vrijgeeft (deel 1 van de plakkaart, #317)
- gemaakt_door: Regisseur

## Waarom deze titel
YouTube-suggesties (curl `suggestqueries.google.com ... ds=yt`, 28 nov 2026 ±05:35 NL, GEZIEN): "blender split model for 3d printing", "how to split a model for 3d printing", "how to split 3d model for printing blender", "how to split parts for 3d printing in blender", "blender split model into parts". De titel begint met de tweede en eindigt op wat ons anders maakt (pennen die passen).

## Titel
How to split a model for 3D printing in Blender (with pins that fit)

## Tekst
```
https://dortus.com/click-cuts/

How to split a model for 3D printing in Blender, the short answer: cut it into parts that fit your printer bed, and put pins in every cut so the parts line up again.

In this video we do it with Click Cuts 1.1, an add-on for Blender, on a horse statue that is too tall for a Bambu Lab A1. Pick your printer, click Split to fit, and every part fits the bed, with pins, pin holes and a part number on the cut faces. Want a cut somewhere else? Draw cut lets you drag a line across a part. Then make the fit test, so the pins fit your printer, and export one STL file per part.

Print the Fit test strip first: every printer is different.

0:00 The short answer
0:15 Pick your printer and split
0:43 Draw your own cut
0:59 Pins that fit your printer
1:26 Check and export
1:48 Where to get it

Works in Blender 4.2 and newer. Recorded in Blender 5.3 with the add-on itself.
Model: Horse Statue 01 by Poly Haven (CC0).

#blender #3dprinting #b3d #blenderaddon
```

## Eerste reactie
```
Click Cuts, split a model to fit your printer bed in Blender: https://dortus.com/click-cuts/
```

## Bron per bewering
| Bewering | Bron |
|---|---|
| parts that fit your printer bed, pins, pin holes, part number on the cut faces | `producten/blender-splitser/winkel/docs.md` "Your first split" stap 3 (gekeurd Daan #169) |
| Draw cut, drag a line across a part | docs.md "Choose where it cuts: Draw cut" |
| fit test, pins fit your printer | docs.md "Print the fit test first" |
| one STL file per part | docs.md stap 4 |
| Blender 4.2 and newer | `blender_manifest.toml` blender_version_min 4.2.0 |
| too tall for a Bambu Lab A1 | opname r1: paard 520 mm, bed 256 mm (`film-r1.json`, GEZIEN) |
| Recorded in Blender 5.3 | `cuts_lang.py` met Blender 5.3.0 |

Bewust niet: geen "it clicks", niets over printen door ons, geen "not print tested", geen prijs, geen Gumroad-adres, geen AI.

## Nog te doen voor de wachtrij
1. Hoofdstuktijden vervangen door die uit `cuts-lang-hoofdstukken.txt` (met de stem van Max).
2. Regel `geluid_check` en `bestand` invullen uit de release.
3. Keuring Daan (film en deze tekst samen), daarna naar `marketing/wachtrij/` met datum na Click Cuts 1.1 live.
