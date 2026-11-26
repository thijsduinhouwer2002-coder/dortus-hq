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

**25 nov ±16:40, opnieuw gemaakt (Daan #82, M1):** zelfde opdracht en instellingen, nu met de zip van main op 4801bc8. Het paneel toont "Horse (closed): 505,742 faces" in plaats van "Horse_watertight"; verder gelijk (12 stukken groen, 48 pennen, 0,20 mm; GEZIEN, `beelden/paneel.json`). Geen nieuwe blinde test: alleen de modelnaam veranderde (hoofdmanager 15:45 in #39).

## Beeld "Numbered for assembly" met het hele paard (`beelden/nummer-paard-*`, 26 nov ±02:10, issue #105)
Waarom: Thijs zag `nummer-*` en vroeg "wat moet het voorstellen?" (los oranje stuk). Dit beeld vervangt het: zelfde boodschap, maar je ziet eerst het hele paard.

**Midden:** het paard (Poly Haven, CC0) gesneden door de echte knop Split to fit (zip van main op 29d0af9, A1): 12 stukken, alle groen, 48 pennen, uit elkaar zoals het hoofdbeeld (0,42), gouden pen op elk gatenpaar (GEZIEN, `beelden/nummer-paard.json`). **Rechts:** kaart met de close-up van de naad 5-9: het hoofd (stuk 9) boven de borst (stuk 5), pennen in de gaten van stuk 5 en het gegraveerde 5-9 van de add-on (pen 5 mm, speling 0,2 mm; GEZIEN, `beelden/nummer-naad.json`). Een gouden lijn wijst van die naad in het paard naar de kaart. Renders, geen foto van een print.
```
HB_UIT=0.42 HB_UIT_Z=0.8 NP_STUK=5 NP_BUUR=9 NP_X0=0.38 NP_X1=0.66 \
  blender -b --factory-startup --python bron/nummer_paard.py -- ../cuts-hoofdbeeld/bron/hoofdbeeld.py <click_cuts.zip> <modelmap> render-paard.png nummer-paard.json 48 100
SV_STUK=5 SV_BUUR=9 SV_N_GAT=2 SV_RAND=55 SV_F=16 SV_LEEG=0 SV_BUUR_IN_BEELD=1 SV_GAT=55 SV_BUUR_KADER=1.8 SV_X0=0.66 SV_Y0=0.05 SV_HOOG=0.75 SV_DRAAI=0.6 SV_LENS=70 \
  blender -b --factory-startup --python bron/snijvlak.py -- ../cuts-hoofdbeeld/bron/hoofdbeeld.py <click_cuts.zip> <modelmap> render-naad.png nummer-naad.json 48 100
python3 bron/tekst_nummer_paard.py render-paard.png nummer-paard.json render-naad.png nummer-naad.json beelden <fonts> ../../producten/blender-splitser/merk/icoon.svg
```
Blinde test: set `organisatie/blindtest/sets/click-cuts-galerij-nummer-paard.json`, GESLAAGD: Gemini 2,0, ChatGPT 1,5 (`organisatie/blindtest/uitslag/click-cuts-galerij-nummer-paard-2026-11-26-0200.md`). Het oude `nummer-*` haalde 2,0 en 2,0.

**M1 van Daan (#129), 26 nov ±03:41:** de zin links is nu "Cut faces get pin holes where a pin fits, and an engraved part number, like 5-9 where part 5 meets part 9." (de add-on zet geen pen waar er geen past en meldt dan "Glue this joint"). De renders waren niet bewaard, dus `bron/tekst_nummer_paard_m1.py` haalde de oude zin uit beide jpg's (inpainten op het donkere verloop) en zette de nieuwe erin met dezelfde letters (Inter, 44 Medium, 740 breed), plek en schaduw; paard en kaart zijn ongewijzigd. `bron/tekst_nummer_paard.py` heeft de nieuwe zin voor een volgende render. Geen nieuwe blinde test nodig (Daan).

## Beeld "Magnet holes in every cut" (`beelden/magneet-*`, 26 nov ±05:40, issue #137)
Waarom: Click Cuts 1.0.0 heeft magneetgaten (#117, Daan ja #131); Cleave zet Magnets in titel en galerij, onze galerij toonde alleen pennen. Zelfde opzet als "Numbered for assembly" met het hele paard (GESLAAGD).

**Midden:** het paard (Poly Haven, CC0) gesneden door de echte knop Split to fit met Joint: Magnets, maat 6x2 (de standaard van de add-on; zip van main op 69f3cf2, A1): 12 stukken, alle groen, uit elkaar zoals het hoofdbeeld, met een zilveren schijfmagneet in elk magneetgat (GEZIEN, `beelden/magneet-paard.json`). **Rechts:** kaart met de naad 5-9 van dichtbij: een magneet in het gat van stuk 5 en het gegraveerde 5-9 (gat 6,2 mm, magneet 6 mm; GEZIEN, `beelden/magneet-macro.json`). Alleen voor het beeld: de magneten zelf (de add-on maakt de gaten; de koper koopt de magneten, dat staat ook op het beeld). Renders, geen foto van een print.

`hoofdbeeld.py` kreeg HB_VERBINDER en HB_MAGNEET (zonder: pennen zoals altijd) en zilveren magneten in `pennen()` (HB_MAG_UIT: hoeveel mm de magneet uit het vlak steekt); `snijvlak.py` zet bij magneetgaten een magneet in het gat (SV_MAG_UIT), kent SV_X1 en schrijft `pennen_beeld` in de json.
```
HB_VERBINDER=MAGNET HB_MAGNEET=6x2 HB_MAG_UIT=0.8 HB_UIT=0.42 HB_UIT_Z=0.8 NP_STUK=5 NP_BUUR=9 NP_X0=0.38 NP_X1=0.66 \
  blender -b --factory-startup --python bron/nummer_paard.py -- ../cuts-hoofdbeeld/bron/hoofdbeeld.py <click_cuts.zip> <modelmap> render-paard.png magneet-paard.json 48 100
HB_VERBINDER=MAGNET HB_MAGNEET=6x2 SV_STUK=5 SV_BUUR=9 SV_LEEG=0 SV_MAG_UIT=0.8 SV_N_GAT=1 SV_RAND=9 SV_F=8 SV_BUUR_IN_BEELD=0 SV_X0=0.05 SV_Y0=0.05 SV_HOOG=1.0 SV_DRAAI=0.4 SV_LENS=100 \
  blender -b --factory-startup --python bron/snijvlak.py -- ../cuts-hoofdbeeld/bron/hoofdbeeld.py <click_cuts.zip> <modelmap> render-macro.png magneet-macro.json 64 100
KT_X=1600 KT_B=700 MG_CX=0.39 python3 bron/tekst_magneet.py render-paard.png magneet-paard.json render-macro.png magneet-macro.json beelden <fonts> ../../producten/blender-splitser/merk/icoon.svg
```
Blinde test: set `organisatie/blindtest/sets/click-cuts-galerij-magneet.json`, zelfde concurrenten als "Numbered for assembly".
