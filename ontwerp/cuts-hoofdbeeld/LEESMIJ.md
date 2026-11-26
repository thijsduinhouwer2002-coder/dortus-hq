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

**25 nov ±04:40 NL, moet van Daan (#34):** regel 2 was "Pins, holes and part numbers on every cut"; te sterk, want bij een te kleine snede meldt de add-on "Glue this joint" en komt er geen pen. Nu: "Pins, holes and part numbers added for you". Alleen `bron/tekst.py` opnieuw gedraaid op de bestaande render (`beelden/paard-render.jpg`); de pixelvergelijking met de vorige versie laat alleen verschil zien in het vak van die regel. De render zelf is gelijk, dus geen nieuwe blinde test (zoals Daan schreef).

**26 nov ±07:00 NL, vierkante Gumroad-thumbnail (#147):** `beelden/paard-vierkant-1200x1200.jpg` en `-600x600.jpg`, uit dezelfde render (`beelden/paard-render.jpg`, geen nieuwe render): vierkante uitsnede met het hele paard in het gouden bouwvolume links en de 12 stukken rechts, bovenaan "Click Cuts" groot en "Too big to print? One click.", labels "520 mm tall / gold box: 256 mm bed" en "12 parts, 48 pins / every part fits" (cijfers uit `beelden/paard.json`, GEZIEN). Leesbaar op 200 px (zelf bekeken). Maken: `python3 bron/vierkant.py beelden/paard-render.jpg beelden/paard.json beelden <fontmap> producten/blender-splitser/merk/icoon.svg`. Blinde test: set `organisatie/blindtest/sets/click-cuts-vierkant-gumroad.json` tegen de Gumroad-vierkanten van CatPin, Cleave en Split 3D Print (url's via de zoek-API van Gumroad, GEZIEN 26 nov).
Ronde 1 GESLAAGD: Gemini 1,0, ChatGPT 1,0 (`organisatie/blindtest/uitslag/click-cuts-vierkant-gumroad-2026-11-26-0643.md`). Verbeterd met hun zinnen: pil "Blender add-on" naast de haak (ChatGPT, twee keer) en de labels onderaan groter en vetter (Gemini, twee keer). Ronde 2: set `click-cuts-vierkant-gumroad-r2.json`.
