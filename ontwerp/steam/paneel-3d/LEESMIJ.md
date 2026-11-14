# Voorstel: het paneel rechts (kroniek en kaartje) in de 3D-stijl (Daan, 14 nov 2026, ±02:50 UTC)

Waarom: in de echte strook van main (run 43544909126) is het paneel rechts nu de grootste stijlbreuk: harde pixelrand, gele hoekpixels, pixelknop en de standaardletter van Godot naast een zacht 3D-hol, 3D-helden en 3D-wolkjes (frisse kijker op het blad voor Thijs: "twee spellen naast elkaar"). Het paneel staat bij elke hover en elk kaartje in beeld, dus het telt net zo zwaar als Gloop.

Wat: een afgeronde plaat van donker pruimhout met een zachte gouden rand, zoals de schat en de wolkjes: mat, rond, geen hoekpixels. Letter Fredoka (rond, vriendelijk, leest op 13 px; SIL Open Font License, `OFL-Fredoka.txt`, mag mee in het spel). Knop: ronde gouden pil met donkere vulling. Muntje: rond en glanzend in plaats van 4x4 pixels.

Beelden (GEZIEN met Read): `kaartje-voor-na-160-ware-grootte.png` (boven nu, onder voorstel, echte strook met taakbalk), `kaartje-voor-na-3x.png`.

Bestanden:
- `paneel.py`: rendert de 9-slice-bron (`python3 paneel.py <uit.png> <px> <samples>`), rand = 1/3 van de breedte. `paneel-3d-bron-384.png` is de bron op 384 px (rand 128 px).
- `Fredoka.ttf` (variabel: gewicht 300 tot 700; titel 600, tekst 450, knop 550).
- `voorbeeld.py`: hoe het voorbeeld is gemaakt (maten op 160 px: rand 18, titel 18, tekst 15, knop 24 hoog met hoek 12).

Voor Olaf (`kern/tekst.gd`), als voorstel en pas na de demolijst-punten die voorgaan: `PANEEL` naar de 3D-bron met lineair filter en rand `R * schaal` zoals nu (bron-rand 128), `ThemeDB.fallback_font` naar Fredoka met de gewichten hierboven, `_knop()` als ronde pil (StyleBoxFlat met hoek, of een tweede 9-slice), `_munt()` als rond muntje (zelfde 3D-munt als op de schat mag ook). De indeling en de teksten blijven zoals ze zijn.
