# YouTube-miniatuur zoekvideo Click Cuts (issue #382 voor #332, Beeldmaker, 28 nov 2026)

Voor de video "How to split a model for 3D printing in Blender (with pins that fit)" van de Regisseur (#332).

**Beeld:** `beelden/yt-zoek-r1a-1280x720.jpg` (kop "TOO BIG / TO PRINT? / SPLIT IT IN / BLENDER") en `beelden/yt-zoek-r1b-1280x720.jpg` (kop "SPLIT ANY / MODEL / FOR 3D PRINTING IN / BLENDER").
- Bron: de Blender-render van het hoofdbeeld (`ontwerp/cuts-hoofdbeeld/beelden/paard-render.jpg`, Blender 5.3.0, Cycles). Links het paard heel in het gouden bouwvolume van 256 mm (Bambu Lab A1), rechts de 12 stukken met pennen uit de echte knop Split to fit van Click Cuts (alle 12 groen, 48 pennen; GEZIEN, `ontwerp/cuts-hoofdbeeld/beelden/paard.json`). Twee uitsneden uit die ene render, dichter bij elkaar gezet, lichter gemaakt, met een pijl.
- Model: Horse Statue 01 van Poly Haven, CC0 ([polyhaven.com/a/horse_statue_01](https://polyhaven.com/a/horse_statue_01), [licentie](https://polyhaven.com/license)). Letters: Poppins ExtraBold (OFL 1.1). Geen AI-beeld, geen foto van een print, geen Blender-logo.
- Leesbaar op 168x94 (zelf bekeken).

```
python3 ontwerp/cuts-yt-zoek/bron/miniatuur.py ontwerp/cuts-hoofdbeeld/beelden/paard-render.jpg ontwerp/cuts-yt-zoek/beelden/yt-zoek-r1a-1280x720.jpg a
python3 ontwerp/cuts-yt-zoek/bron/miniatuur.py ontwerp/cuts-hoofdbeeld/beelden/paard-render.jpg ontwerp/cuts-yt-zoek/beelden/yt-zoek-r1b-1280x720.jpg b
```

**Blinde test:** set `organisatie/blindtest/sets/click-cuts-yt-zoek.json`, tegen de echte top 3 van YouTube op "split model for 3d printing blender" (curl op de zoekpagina, 28 nov ±12:40 NL, GEZIEN): Filaments Folly (566.273 views), 3DRedBox "Split Models for 3D Printing the Easy Way" en iPaintSmallThings (484.294 views). thumb-a van de Regisseur staat ernaast ter vergelijking.
