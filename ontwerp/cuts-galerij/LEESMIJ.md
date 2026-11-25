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
