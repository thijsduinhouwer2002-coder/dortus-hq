# Galerijbeelden Click Cuts (issue #39, Beeldmaker, 25 nov 2026)

Waarom: Click Cuts gaat in de week van 30 nov live; het hoofdbeeld is GESLAAGD (#13), de galerij was leeg. Momenten en onderschriften: `producten/blender-splitser/galerij.md`. Lat: `organisatie/lat/click-cuts.md`.

## Beeld "Numbered for assembly" (`beelden/nummer-*`)
Moment 2 uit `galerij.md`: het snijvlak van dichtbij. Geen concurrent graveert nummers (lat).

**Model:** Horse Statue 01 van Poly Haven, [polyhaven.com/a/horse_statue_01](https://polyhaven.com/a/horse_statue_01), licentie CC0 ([polyhaven.com/license](https://polyhaven.com/license)). Zelfde paard als het hoofdbeeld. Geen AI-beeld.

**Snijden:** door de echte knop Split to fit van Click Cuts (zip van main, printer Bambu Lab A1, bed 256 mm). In beeld stuk 7 (borst en voorbeen) met zijn bovenste snijvlak, waar het stuk 11 raakt; op het voorvlak lees je 7-5. De pengaten, het gegraveerde nummer 7-11 en de nummers op de zijvlakken maakte de add-on zelf (GEZIEN, `beelden/nummer.json`: pen 5 mm, speling 0,2 mm, gravure 0,6 mm diep, beide stukken groen). Alleen voor het beeld: gouden pennen half in de gaten van het bovenvlak (één gat leeg, zodat je het gat ziet). Het beeld is een render, geen foto van een print.

**Tekst:** titel uit onderschrift 4 van `galerij.md`, met de nummers in beeld (7-11) in plaats van het voorbeeld 3-5.

Maken (Blender 5.3.0, Cycles 64 samples, lokaal in de sessie; bron `bron/snijvlak.py` gebruikt `ontwerp/cuts-hoofdbeeld/bron/hoofdbeeld.py`):
```
SV_STUK=7 SV_BUUR=11 SV_N_GAT=4 SV_RAND=25 SV_F=4 \
  blender -b --factory-startup --python bron/snijvlak.py -- ../cuts-hoofdbeeld/bron/hoofdbeeld.py <click_cuts.zip> <modelmap horse_statue_01> render.png nummer.json 64 100
TK_DX=-60 TK_DY=-280 TK_STOP=85 python3 bron/tekst.py render.png nummer.json beelden <fontmap met Bricolage.ttf en Inter.ttf> ../../producten/blender-splitser/merk/icoon.svg nummer
```
Uit: `nummer-2400x1200.jpg` (Superhive) en `nummer-1920x1080.jpg` (Gumroad). Blinde test: set `organisatie/blindtest/sets/click-cuts-galerij-nummer.json` tegen de sterkste verbindersbeelden uit de galerij van Cleave, Split 3D Print en SnapSplit.

## Beeld "Pins that fit your printer" (`beelden/passend-*`, 25 nov ±13:15)
Moment 4 uit `galerij.md`: het proefblokje, ons voordeel tegen alle drie (lat). Onderschrift 6, ingekort.

**Blok:** uit de echte knop Make fit test van Click Cuts (zip van main, A1, PLA, speling 0,20 mm). Spelingen 0.15, 0.20, 0.25 en 0.30 mm gegraveerd, pen 5 mm, lengte 12 mm, blok 68 x 17,1 x 8,3 mm, waterdicht (GEZIEN, `beelden/passend.json`). Alleen voor het beeld: gouden pennen van die maat half in drie gaten en één voor het blok (de pennen van de add-on zelf staan uit). **Kaartje:** stuk 11 van het paard (Poly Haven, CC0) zweeft boven stuk 7 met de pennen, uit `bron/snijvlak.py` (`beelden/passend-zak.json`). Wens van beide rechters bij "Numbered for assembly". Renders, geen foto van een print.
```
PB_X0=0.44 blender -b --factory-startup --python bron/passend.py -- ../cuts-hoofdbeeld/bron/hoofdbeeld.py <click_cuts.zip> <modelmap> render-passend.png passend.json 48 100
SV_STUK=7 SV_BUUR=11 SV_N_GAT=4 SV_RAND=40 SV_F=11 SV_LEEG=0 SV_BUUR_IN_BEELD=1 SV_GAT=40 SV_BUUR_KADER=1.3 SV_X0=0.25 SV_HOOG=2.4 SV_DRAAI=0.7 SV_LENS=70 \
  blender -b --factory-startup --python bron/snijvlak.py -- ../cuts-hoofdbeeld/bron/hoofdbeeld.py <click_cuts.zip> <modelmap> render-zak.png zak.json 48 70
ZK_KADER=0.56,0.10,0.855,0.80 ZK_Y=870 ZK_H=380 python3 bron/tekst_passend.py render-passend.png passend.json render-zak.png beelden <fonts> ../../producten/blender-splitser/merk/icoon.svg
```
Blinde test: set `organisatie/blindtest/sets/click-cuts-galerij-passend.json`, zelfde concurrenten als "Numbered for assembly".

## Beeld "Three steps in one tab" (`beelden/paneel-*`, 25 nov ±15:00)
Moment 5 en onderschrift 7 uit `galerij.md`: het echte paneel. Wens van beide rechters bij "Numbered for assembly" (een stukje echt Blender-paneel).

**Schermafbeelding:** echte Blender 5.3.0 met interface (Xvfb, schaal 1.5), add-on uit de zip van main, het paard (Poly Haven, CC0) 520 mm hoog, echte knop Split to fit met Bambu Lab A1: 12 stukken, alle 12 groen, 48 pennen, speling 0,20 mm (GEZIEN, `beelden/paneel.json` en kale schermafbeelding `beelden/paneel-scherm.jpg`). Het 3D-venster staat schermvullend; de pennenbak naast het model staat uit. Het vergrote paneel rechts is pixel voor pixel uit dezelfde schermafbeelding, niets nagetekend. Stappen links: printers uit `printers.py` (Bambu, Prusa, Creality, eigen maat), formaten uit `eigenschappen.py` (STL, 3MF, in mm).
```
xvfb-run -s "-screen 0 2880x1620x24" env PN_AFSTAND=1.18 PN_DX=40 PN_DRAAI=-28 PN_KANTEL=74 \
  blender --gpu-backend opengl <start.blend zonder splash> --python bron/paneel.py -- <click_cuts.zip> <modelmap> <uitmap>
python3 bron/tekst_paneel.py <uitmap>/paneel-scherm.png <uitmap>/paneel.json beelden <fonts> ../../producten/blender-splitser/merk/icoon.svg
```
Blinde test: set `organisatie/blindtest/sets/click-cuts-galerij-paneel.json`, tegen de paneelbeelden van Cleave, Split 3D Print en SnapSplit (lat, deel Paneel).
