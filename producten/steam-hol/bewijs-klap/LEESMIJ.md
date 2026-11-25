# Klap-ster en kader (Mila, 25 nov 2026, issue #43)

Waarom: Iris (keuring 52aa730 en f6aa9b6) gaf de klap aandacht 7 en mooi 6/7: de ster was beige-grijs of wit, ±12 à 14 px, één beeld, leest als stofwolk (GEZIEN door Iris); het kader rechts is het grootste vlak in beeld en saai bruin.

## Wat er is (beelden uit code in Blender, geen AI, geen gekocht pakket)
- `godot/kunst/klapster.png`: 4 beelden van 16 x 16 spelpixels (blad 512 x 128, 8 bladpixels per spelpixel, scherp tot schaal 8). Model `modellen/klapster.py`. Wit hart, geel lijf, oranje punten, donkere rand eromheen (leest op aarde, gang en gras).
  - 0 inslag (klein, wit), 1 ster (±11 spelpixels breed = ±33 px op 120, GEZIEN in `strook-120-klap-en-bord.png`), 2 op zijn grootst met 4 vonkjes, 3 zes vonkjes.
  - Bedoeld voor 8 per seconde, één keer: 0,5 s in beeld (oude ster 0,25 s). Midden van de cel = plek van de klap (nu `HOL.GANG_BOVEN + 6` in `kern/klap.gd`). Filter lineair, net als de andere 3D-bladen.
- **Witte flits op de held die valt** (code, voor Olaf): op het moment van raken 1 beeld (±0,12 s) de held helemaal wit, dan ±0,06 s half wit (kan Daan #45: het tweede beeld korter, anders leest het als een wit spookje), samen ±0,18 s. In Godot: een `ShaderMaterial` op de held met `COLOR.rgb = mix(COLOR.rgb, vec3(1.0), flits);` en `flits` 1,0 (0,12 s), dan 0,5 (0,06 s), dan 0. In het bewijs nagebootst op de echte film.
- `godot/kunst/paneel_hol.png`: het kader rechts als krijtbord (donkergroene lei met vage krijtvegen) in een lijst van honingkleurig hout met koperen hoekbeslag. Model `modellen/krijtbord.py`. Zelfde 9-slice als `paneel_3d.png` (384 x 384, `BRON_RAND` 128), dus in `kern/tekst.gd` alleen `PANEEL_3D` naar dit bestand. De crème en gouden tekst blijft leesbaar, en het groen staat los van de rode aarde (meer kleurverschil, doel uit de opdracht). Let op: de houten lijst is ±6 px op 120 (de oude gouden rand ±3 px), dus de tekst rechts heeft 2 à 3 px meer binnenruimte nodig.

## Bewijs (nagebootst op de echte film van main, run op tak `schermen`, `steam-hol/main/film.gif`, beelden 39 tot 47)
- `val-klap-120-ware-maat.gif` en `val-klap-2x.gif`: een val van begin tot eind, held loopt, valt (witte flits), klap-ster in 4 beelden, "+6", muntjes; het bord rechts.
- `klap-reeks-2x.png`: de klap beeld voor beeld op 2x. `voor-boven-na-onder-120.png`: oud boven, nieuw onder, ware maat.
- `klapster-blad-op-aarde.png`: het blad op een aardekleur.
- Maker: `maak_bewijs.py` (de oude ster is weggepoetst met hetzelfde stuk gang uit beeld 30; de tekst op het bord is uit de oude film losgemaakt, dus een fractie zachter dan in het spel).

## Nakeuring kader: binnenruimte (25 nov ±07:40 NL, moet Daan #45)
- `kern/tekst.gd`: `PANEEL_3D` is nu `kunst/paneel_hol.png` (het krijtbord); de tekst blijft rechts `marge_r()` = 3 x schaal + 1 px binnen het vak (was 6 px, op 120 nu 10) en het paneel begint links op `paneel_links(x)` (op 120 1 px breder, op 96 2 px breder). Kroniekregels, doel, uitleg en goud op het kaartje rekenen met dezelfde marge.
- Gemeten op ware maat, 1920 breed, 120 hoog (GEZIEN, pixels geteld in `bord-marge-120-een-regel.png`): tussen de laatste letter van "Big Gloop ready: click Gloop" en het hout rechts 6 px lei, tussen het hout links en het muntje 4 px. Was rechts ±0,5 px.
- Beelden uit het echte spel (Godot 4.3, `--write-movie`, doel en regels ingezet voor de foto): `strook-1920-120-bord-marge.png` (hele strook ware maat), `bord-marge-120-een-regel.png` en `-drie-regels.png` (ware maat), `bord-marge-2x-een-regel.png`, `-drie-regels.png` (2x), `bord-marge-2x-96.png` en `-160.png` (de andere hoogtes, 2x).
- Toetsen: toets_systemen, toets_namen, toets_held, toets_vleermuis, toets_berg_wand, toets_klap allemaal 0 FOUT (GEZIEN, Godot 4.3 Linux).
