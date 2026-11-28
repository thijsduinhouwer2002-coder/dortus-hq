# Cover gratis testblok Click Cuts (issue #423 voor #395, Beeldmaker, 28 nov 2026)

Voor het gratis model op Printables, Thingiverse en Cults3D (#395, Productbouwer).

**Beeld r1:** `beelden/testblok-cover-r1-1600x1200.jpg` (4:3; tekst en blok binnen y 66..1134, zodat de uitsnede 3:2 van Printables niets afsnijdt).
- Precies wat in de download zit: het blok en de vier pennen uit de echte knop Make fit test van Click Cuts (zip van main, Bambu Lab A1, PLA, speling 0,20 mm): pen 5 mm, lengte 12 mm, gaten 0.15, 0.20, 0.25 en 0.30 mm gegraveerd, blok 68 x 17,1 x 8,3 mm, waterdicht (GEZIEN, `beelden/render-r1.json`). De pennen zijn de pennen van de add-on zelf, los gemaakt; één staat boven het gat 0.20, drie voor het blok.
- Render in Blender 5.3.0 (Cycles, 128 samples), geen foto van een print, geen AI-beeld. Letters Poppins (OFL 1.1). Kop "Pin Fit Test Block", regel "Find the clearance for pins in split prints", badge "FREE STL + 3MF" (het model is gratis; de add-on niet, daarom staat er alleen "Click Cuts for Blender").

```
TB_HOOG=0.95 TB_DRAAI=0.18 TB_VOOR=1.9 TB_LENS=110 TB_XB=0.05,0.95 TB_YB=0.09,0.64 TB_ZWEEF=7 \
  blender -b --factory-startup --python bron/cover.py -- ../cuts-hoofdbeeld/bron/hoofdbeeld.py <click_cuts.zip> render-r1.png beelden/render-r1.json 128 100
python3 bron/tekst.py render-r1.png beelden/render-r1.json beelden/testblok-cover-r1-1600x1200.jpg <fontmap met Poppins-ExtraBold> ../../producten/blender-splitser/merk/icoon.svg
```
(`<click_cuts.zip>` = de map `producten/blender-splitser/split_joints` gezipt.)

**Blinde test:** set `organisatie/blindtest/sets/click-cuts-testblok-cover.json`, tegen drie echte covers van gratis tolerantietests op Printables (gezocht met curl op de api van Printables, 28 nov ±19:00 NL, GEZIEN): Clearance Tolerance Test (7250 likes), Press/Tight/Loose-Fit Offset Gauge en FDM Tolerance Test 5 mm Pin.
