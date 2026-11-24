# Click Joints Pro video guide (CONCEPT, clip 1 gekeurd, clip 2 wacht op herkeuring Daan)

Chris, 24 nov 2026 ±12:55 NL. Opdracht Afkijker (24 nov, `berichten/chris.md`): 3 stille uitlegclips als extra bestand bij de Pro-koop, zoals Surface Lab (2 van 5 reviews prijzen de meegeleverde video's, GEZIEN Superhive ratings). **Geen post, geen plaatsing.** Na Daans ja zet de hoofdchat ze als "Click Joints Pro video guide" bij het product op Gumroad en Superhive.

| Bestand | Lengte | Bron (echte opname, Blender 5.3.0) | Onderschriften |
|---|---|---|---|
| `1-figure-from-rig.mp4` | 45,5 s | release regisseur-17, `opname-pro.mkv` (Pro met enkels, robot, 9 gewrichten) | rigged figure, Figure from rig, type en buigbereik per gewricht, Show bend range, rood voorbij de stop, pose, Exploded view, Export STL or 3MF |
| `2-fit-test.mp4` | 13,0 s | release regisseur-1, `opname-pro.mkv` frames 1222 tot 1612 (oudere Pro-versie, zelfde knoppen "Fit test: ball" en "Fit test: hinge") | Print this first: a small fit test; Five joints: 0.10 0.15 0.20 0.25 0.30 mm; keep the one that turns without wobble |

1920 x 1080, 30 fps, H.264, geen geluid, samen ±3 MB. Beeld rechts, tekst links. Gemaakt met `maak.py` (ffmpeg). Stilstaand beeld: `stilstaand.png`. sha256 in `SHA256SUMS.txt`.

**Clip 3 (scharnier of kogel op de 3D-cursor bij een al gesplitst model) ontbreekt:** dat staat in geen bestaande opname. Gevraagd aan de Regisseur (filmpjes zijn van hem).

**Let op voor de keurder:** clip 2 komt uit een oudere Pro-opname (regisseur-1). Het paneel ziet er bijna gelijk uit, maar de figuur is een andere dan in clip 1. Release maken mocht deze sessie niet (403), daarom staan de bestanden in de repo.

## 24 nov 2026 ±15:50 NL, Chris: clip 2 opnieuw (Daan M1 en C1)
- M1: clip 2 begint nu op frame 1222. Tot en met frame 1215 staat de voetbalfiguur met kniebereik in beeld, vanaf 1220 alleen de staafjes (GEZIEN, beeld per 5 frames). Eerste beeld van de nieuwe clip: alleen staafjes.
- Einde naar frame 1612: vanaf ±1620 komt de figuur terug achter de staafjes (GEZIEN, beeld per seconde). Lengte nu 13,0 s.
- C1: onderschrift "Five joints: 0.10 0.15 0.20 0.25 0.30 mm" (waarden uit `SPELINGEN` in `click_joints/betaald/testkaart.py`), slotzin "Keep the one that turns without wobble" zoals de uitleg in de add-on zelf.
- Clip 1 ongewijzigd (zelfde sha256). C2 (kader op Figure from rig) niet gedaan: clip 1 is al gekeurd en dan moet hij opnieuw. `python3 maak.py 2` maakt alleen clip 2.
