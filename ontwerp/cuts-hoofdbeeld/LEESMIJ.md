# Hoofdbeeld Click Cuts: het paard voor en na (issue #13, Beeldmaker, 25 nov 2026)

Waarom: de rechters vroegen "visual proof" van de ene klik: het voor en na in één beeld (`producten/blender-splitser/galerij.md`). Lat: Cleave, Split 3D Print en SnapSplit (`organisatie/lat/click-cuts.md`).

**Model:** Horse Statue 01 van Poly Haven, [polyhaven.com/a/horse_statue_01](https://polyhaven.com/a/horse_statue_01), licentie CC0 ([polyhaven.com/license](https://polyhaven.com/license)). Gekozen boven Gothic Statue (de 1k-mesh viel na het dichtmaken uiteen in losse snippers) en Marble Bust 01 (de snede liep dwars door het gezicht, en juist dat vrezen de rechters). Geen AI-beeld.

**Snijden:** door de echte knop Split to fit van Click Cuts (zip van main, printer Bambu Lab A1, bed 256 mm). Uitkomst (GEZIEN, `beelden/paard.json`): paard 520 mm hoog, 12 stukken, alle 12 groen, grootste stuk 127 x 173 x 193 mm, 48 pennen van 5 mm. De kleuren per stuk zijn die van de add-on. Alleen voor het beeld: de stukken staan verder uit elkaar dan in de viewport (0,42 in plaats van 0,25 van de afstand tot het midden), en elke pen staat op de plek van zijn gatenpaar, halverwege de twee stukken.

**Links** staat hetzelfde paard heel, in één neutrale kleur, met het gouden bouwvolume van 256 mm aan zijn voet. Het beeld is een render, geen foto van een print.

Maken (Blender 5.3.0, Cycles 48 samples, lokaal in de sessie):
```
HB_UIT=0.42 HB_UIT_Z=0.8 HB_DRAAI=0.35 HB_AFSTAND=400 \
  blender -b --factory-startup --python bron/hoofdbeeld.py -- <click_cuts.zip> <modelmap horse_statue_01> render.png paard.json 48 100
python3 bron/tekst.py render.png paard.json beelden <fontmap met Bricolage.ttf en Inter.ttf> producten/blender-splitser/merk/icoon.svg paard [kort]
```
Kandidaten in `beelden/`: `paard` (met drie regels) en `paard-kort` (alleen de haak), elk 2400x1200 (Superhive) en 1920x1080 (Gumroad). Kale render: `beelden/paard-render.jpg`.
Blinde test: set `organisatie/blindtest/sets/click-cuts-hoofdbeeld.json`.
