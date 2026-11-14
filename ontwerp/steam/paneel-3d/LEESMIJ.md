# Voorstel: het paneel rechts (kroniek en kaartje) in de 3D-stijl (Daan, 14 nov 2026, ±02:50 UTC)

Waarom: in de echte strook van main (run 43544909126) is het paneel rechts nu de grootste stijlbreuk: harde pixelrand, gele hoekpixels, pixelknop en de standaardletter van Godot naast een zacht 3D-hol, 3D-helden en 3D-wolkjes (frisse kijker op het blad voor Thijs: "twee spellen naast elkaar"). Het paneel staat bij elke hover en elk kaartje in beeld, dus het telt net zo zwaar als Gloop.

Wat: een afgeronde plaat van donker pruimhout met een zachte gouden rand, zoals de schat en de wolkjes: mat, rond, geen hoekpixels. Letter Fredoka (rond, vriendelijk, leest op 13 px; SIL Open Font License, `OFL-Fredoka.txt`, mag mee in het spel). Knop: ronde gouden pil met donkere vulling. Muntje: rond en glanzend in plaats van 4x4 pixels.

Beelden (GEZIEN met Read): `kaartje-voor-na-160-ware-grootte.png` (boven nu, onder voorstel, echte strook met taakbalk), `kaartje-voor-na-3x.png`.

Bestanden:
- `paneel.py`: rendert de 9-slice-bron (`python3 paneel.py <uit.png> <px> <samples>`), rand = 1/3 van de breedte. `paneel-3d-bron-384.png` is de bron op 384 px (rand 128 px).
- `Fredoka.ttf` (variabel: gewicht 300 tot 700; titel 600, tekst 450, knop 550).
- `voorbeeld.py`: hoe het voorbeeld is gemaakt (maten op 160 px: rand 18, titel 18, tekst 15, knop 24 hoog met hoek 12).

Voor Olaf (`kern/tekst.gd`), als voorstel en pas na de demolijst-punten die voorgaan: `PANEEL` naar de 3D-bron met lineair filter en rand `R * schaal` zoals nu (bron-rand 128), `ThemeDB.fallback_font` naar Fredoka met de gewichten hierboven, `_knop()` als ronde pil (StyleBoxFlat met hoek, of een tweede 9-slice), `_munt()` als rond muntje (zelfde 3D-munt als op de schat mag ook). De indeling en de teksten blijven zoals ze zijn.

## Ronde 2 (Daan, 14 nov 2026, ±03:50 UTC), na de frisse kijker
Frisse kijker (agent) gaf ronde 1 een 7,5: beter dan het pixelpaneel en bijna goed genoeg, maar plaat te grijs en koel naast het warme hol, gouden rand op 160 px maar 1 tot 2 px, plat, geen lucht aan de rechterrand (rand leek afgesneden), knop te donker en te vlak.
Verwerkt:
- `paneel.py`: binnenvlak warmer pruim (3e2446, was 2b1b33), rand dikker (binnenplaat 1,70 in plaats van 1,78: op 160 px ±3 px goud), wereldlicht iets warmer. Nieuwe bron: `paneel-3d-bron-384.png` (rand nog steeds 128 px).
- `voorbeeld.py` (maten voor Olaf): 4 px vrij van de rechterrand, boven en onder; schaduw zachter en groter naar het hol (blur 6, 3 px omlaag); titel en getal met een zachte donkere schaduw van 1 px; muntje met kleine schaduw; knop 26 hoog met hoek 13, vulling warm pruimroze (7a426c) met een glansstrook bovenin (925880), letter 16 in plaats van 15, gewicht 600.
- Niet gedaan: oplichten bij hover (kan-punt; de strook moet zuinig blijven, en de knop heeft al een hover in `tekst.gd`).
Beelden (GEZIEN met Read): `kaartje-voor-na-3x-ronde2.png`, `kaartje-voor-na-160-ware-grootte-ronde2.png` (echte strook van main, run 43550750927; het oude paneel is in het voorbeeld weggeplakt met hol-wand van ernaast).
Oordeel: goed genoeg om te bouwen. Het paneel valt niet meer uit de 3D-wereld en de knop leest als knop.

## Ronde 3 (Daan, 14 nov 2026, ±05:45 UTC): gebouwd door Olaf, gekeurd
Bekeken met Read: echte Windows-build, run 43557478427 (c3305a0, tak `claude/steam-hol-paneel3d`), strook 96, 120 en 160 (`ronde3-gebouwd-run43557478427-120.png`, `-160.png`).
Besluit: **ja naar main.** Het paneel hoort nu bij het 3D-hol. Frisse kijker (agent): 7.
Moet als volgende stap: op 160 zijn de letters te klein (inhoud vult de bovenste helft). Proef `ronde3-gebouwd-boven-groter-onder-160-2x.png` (gemaakt met `ronde3_groter.py` op het echte schermbeeld): titel 18, tekst 15, knop 1,3x; kijker gaf dat een 8, met als punt dat de knop minstens 8 px van de binnenrand moet blijven (knop ±28 hoog). Op 96 de knop vrij van de onderrand. Op 120 niets veranderen.
