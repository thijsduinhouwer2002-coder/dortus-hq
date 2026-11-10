# Keuring Het Hol in de echte build (Daan)

Nieuwste bovenaan. Dit is mijn oordeel over hoe het spel eruitziet in Olafs build op GitHub Actions. Het `Akkoord:` komt in `producten/steam-hol/ontwerp.md` zodra dat bestand er is en het prototype naar Thijs kan.

## 9 nov 19:45 UTC, build 408d67b (tak claude/steam-hol-kunst, run 42682511064)
Bekeken (GEZIEN, met Read): `strook-120.png` en vier beelden uit `film.gif` (frames 20, 100, 200, 280), ingezoomd. Bewaard als `kunst-bron/build-408d67b-film.png`.

**Oordeel: nog niet naar Thijs.** Wel een grote stap: voor het eerst ziet het eruit als een spel en niet als blokjes. Pixelmaat klopt, de schatkamer met vaandel en goud leest meteen, gras en fakkels kloppen. Maar het leest nog als een bruine band met een paar mannetjes, niet als een hol vol karakter.

Moet beter, op volgorde van belang:
1. **Gloop is onzichtbaar.** Hij ligt als een dun groen veegje op de vloer (frame 20 tot 280), want hij wordt in y geschaald. Gebruik de frames uit `slijm.png` (rust) en `slijm_leven.png` (plat, opstaan, hap, slapen, spugen), nooit schalen: haal `sy` uit `slijm.gd` en zet `systemen/slijm.gd` in `strook.gd` in plaats van `kern/standin_slijm.gd`. De bewoner is het grappigste wat we hebben; hij moet het meest opvallen. (Bram, `slijm.gd`)
2. **Alle helden zien er hetzelfde uit** (rode tuniek, alleen de hoed verschilt), en een terugkomer ziet er net zo uit. Gebruik `held_lijf_kleuren.png` (vaste kleur per naam), `held_littekens.png` en `held_hoeden_hap.png`, en `tekens.png` voor boos en ster. (Bram, `held.gd`)
3. **Geen licht.** `gloed.png` rond de fakkels en de schat wordt niet getekend; de gang is overal even licht. Warm licht bij de schat en de ingang maakt het meteen knus. (Olaf)
4. **Het zwarte meldingenvlak** is het lelijkste in beeld: een plat schermding bovenop een getekende wereld. Gebruik `paneel.png` als NinePatchRect (rand 4, nearest). Zie `kunst-bron/paneel-voor-na.png`. Lettertype blijft zoals het is (het voorbeeld gebruikt een gelijke letter): twee pixellettertypen geprobeerd (Minimal 5x7, Public Pixel, beide CC0), het ene breekt, het andere is te breed. (Olaf, `kern/tekst.gd`)
5. **Aarde is één bruin vlak** met steeds dezelfde kluitjes; rechts van de schatkamer ruim een derde van de strook leeg. Dat is mijn werk: lagen, wortels, oude botten en kristalletjes in de aarde, zodat ongegraven aarde ook iets te zien geeft. (Daan, volgende run)
6. Stekelput dicht leest als een plank: goed, hij moet verstopt zijn. Bij open is hij in de film nauwelijks te zien; daar kijk ik naar als Gloop en de helden kloppen.

Goed genoeg zoals het is: pixelmaat en schaal, gras, ingang met bordje, schatkamer, fakkels, kleur van de gangwand.

**Controleur (agent) op mijn kunst, 19:40:** nee op versie 1: pleister, verband, boos teken en de hap uit de hoed lazen niet op schaal 3, de puntmuts had geen hap (fout in het script), de slijm-hap was geen eigen beweging, het paneel-voorbeeld liet de tekst slechter zien. **Alles verwerkt in versie 2** en zelf bekeken: pleister wit kruisje, verband om het hoofd met slip, boos als rode ader van vier hoekjes, hap met tandje in elke hoed, kauwen in twee frames, laars lichter, paneel als plank met nerf, voorbeeld met gelijke letter, blauwgrijze tuniek wordt zeegroen, regels in kunst.json (combinaties littekens, bron van de hap, hoogte van de tekens, oude tint-kleuren eruit). Licht op plek 3, voor het paneel (advies controleur: meeste effect voor minste werk).
Nog open (kan): naamkaartje en trofee rijker, Gloop in rust groter of feller, rustige achtergrond achter het maaiveld (de terminal en Notepad steken door het gras: dat hoort bij de testopstelling, maar telt voor winkelplaatjes).

**Aarde versie 1 (later in run 58):** `aarde_lagen.png` en `vondsten.png` staan in `godot/kunst/` (zie LEESMIJ). Zelf bekeken op ware grootte naast build 408d67b: diepte leest (lagen, wortels, vondsten), maar de korrel is fijner en rustiger dan de oude kluitjes; of dat in de echte build mooier is, keur ik pas als Olaf hem inbouwt (`hol.gd`: rij 0 van tegels.png vervangen door aarde_lagen.png op diepte, vondsten erover). Botten lezen nog matig.

## Keuring op leesbaarheid, run 42720126269 (commit b520588), 9 nov 23:45 UTC (Daan)
Bekeken met Read: `strook-160.png` en `strook-96.png` van de tak `schermen`. Strook, paneel en tekst lezen op beide hoogtes; het paneel valt niet over andere vensters. Eén leesfout:
- **Namen die Engelse woorden zijn breken de zin.** In beeld: "Ties read about you in a tavern." Een Engelse speler leest "ties" als stropdassen en de zin als onzin. Zelfde risico met "Wil" ("Wil is back" leest als "Will"). `kern/strook.gd` regel 16 (`NAMEN`, Olaf): vervang Ties en Wil door namen die in het Engels alleen een naam kunnen zijn (bijvoorbeeld Tibbe en Wout), of houd Nederlandse namen maar zonder Engelse betekenis. De Nederlandse namen zelf zijn leuk en eigen; houden. Naam in de toets `toets_held.gd` mag blijven (alleen toets).

## Keuring op leesbaarheid, run 42728431261 (commit 7613976), 10 nov 00:35 UTC (Daan)
Bekeken met Read: `strook-96.png` (uitsnede op 2x) en `strook-160.png`, plus `hol-120.log`. Mijn punt van 23:45 is opgelost: Ties en Wil zijn Tibbe en Wout ("Tibbe brought a torch. And hope." leest goed). Strook, paneel en tekst lezen op 96 en 160 px; het paneel blijft in de strook. Hoogte met rechtsklik in drie standen (96, 120, 160) en klikken door lucht en gras: in de code bevestigd. Geen nieuwe leesfouten. Voor de winkeltekst: zie keuring 2 in `winkelpagina/keuring-daan.md` (drie standen, geen schuif).
