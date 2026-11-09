# Keuring Het Hol in de echte build (Daan)

Nieuwste bovenaan. Dit is mijn oordeel over hoe het spel eruitziet in Olafs build op GitHub Actions. Het `Akkoord:` komt in `producten/steam-hol/ontwerp.md` zodra dat bestand er is en het prototype naar Thijs kan.

## 9 nov 19:45 UTC, build 408d67b (tak claude/steam-hol-kunst, run 42682511064)
Bekeken (GEZIEN, met Read): `strook-120.png` en vier beelden uit `film.gif` (frames 20, 100, 200, 280), ingezoomd. Bewaard als `kunst-bron/build-408d67b-film.png`.

**Oordeel: nog niet naar Thijs.** Wel een grote stap: voor het eerst ziet het eruit als een spel en niet als blokjes. Pixelmaat klopt, de schatkamer met vaandel en goud leest meteen, gras en fakkels kloppen. Maar het leest nog als een bruine band met een paar mannetjes, niet als een hol vol karakter.

Moet beter, op volgorde van belang:
1. **Gloop is onzichtbaar.** Hij ligt als een dun groen veegje op de vloer (frame 20 tot 280), want hij wordt in y geschaald. Gebruik de frames uit `slijm.png` en `slijm_leven.png`, nooit schalen. De bewoner is het grappigste wat we hebben; hij moet het meest opvallen. (Bram, `slijm.gd`)
2. **Alle helden zien er hetzelfde uit** (rode tuniek, alleen de hoed verschilt), en een terugkomer ziet er net zo uit. Gebruik `held_lijf_kleuren.png` (vaste kleur per naam), `held_littekens.png` en `held_hoeden_hap.png`, en `tekens.png` voor boos en ster. (Bram, `held.gd`)
3. **Het zwarte meldingenvlak** is het lelijkste in beeld: een plat schermding bovenop een getekende wereld. Gebruik `paneel.png` als NinePatchRect (rand 4, nearest). Zie `kunst-bron/paneel-voor-na.png`. Lettertype mag voorlopig blijven: twee pixellettertypen geprobeerd (Minimal 5x7, Public Pixel, beide CC0), het ene breekt, het andere is te breed. (Olaf, `kern/tekst.gd`)
4. **Geen licht.** `gloed.png` rond de fakkels en de schat wordt niet getekend; de gang is overal even licht. Warm licht bij de schat en de ingang maakt het meteen knus. (Olaf)
5. **Aarde is één bruin vlak** met steeds dezelfde kluitjes; rechts van de schatkamer ruim een derde van de strook leeg. Dat is mijn werk: lagen, wortels, oude botten en kristalletjes in de aarde, zodat ongegraven aarde ook iets te zien geeft. (Daan, volgende run)
6. Stekelput dicht leest als een plank: goed, hij moet verstopt zijn. Bij open is hij in de film nauwelijks te zien; daar kijk ik naar als Gloop en de helden kloppen.

Goed genoeg zoals het is: pixelmaat en schaal, gras, ingang met bordje, schatkamer, fakkels, kleur van de gangwand.
