# Opdracht voor een familie-agent (Mila, run 50, 12 nov 2026)

Webpagina's lees je met `curl` in Bash, nooit met WebFetch.

Je tekent voor Ebb (ademapp voor Garmin-horloges) de werelden van jouw familie dieren, in precies dezelfde opzet als de drie voorbeelden krab, schildpad en clownvis.

## Lees eerst
- `ontwerp/garmin/ebb-werelden-v3.md`: hele bestand; vooral "Lijst versie 2" (jouw dieren: plek en grap) en "Veilige zone".
- Scripts in `ontwerp/garmin/bron/`: `werelden_v21.py` (Doek, water, lucht, tekst, `D` = lijst van de 25 dieren in volgorde van `ebb-dieren-v83-data.json`, nr 1 is `D[0]`, bonus is `D[24]`), `werelden_v3.py` (adem, hold, menu, eind per wereld), `werelden_v32.py` (huidige stand, bundel en eindscherm), `meet_contrast_v32.py`, `toets_veilige_zone_v32.py`.
- Voorbeeldbeelden: `ontwerp/garmin/werelden32/overzicht-<krab|schild|clown>-260-2x.png` en `-454-1x.png` (bekijk ze met Read).

## Maak
- Eén script `ontwerp/garmin/bron/werelden_v4_<familie>.py` dat de v32-functies hergebruikt (importeer, kopieer niet de hele lucht en zee) en per dier een eigen grapvoorwerp en eigen plek tekent. Uitvoer: `ontwerp/garmin/werelden4/<dier>-<in|uit|calm|hold|menu|eind>-<dag|nacht>-<454|260>.png` en per dier `overzicht-<dier>-260-2x.png` en `overzicht-<dier>-454-1x.png` (zelfde opbouw als de v32-overzichten).
- Pas de contrastmeting en de veilige-zone-toets aan voor jouw dieren (eigen kopie `meet_v4_<familie>.py`) en draai ze. Eis: elke tekstregel 4,5:1 of hoger, en 0 regels te dicht (6/260) bij dier of grapvoorwerp.

## Regels (hard)
- Boven water = ademen (lucht per dagdeel, zee stijgt en zakt, dier dobbert in de kam, kantelt 8/3/0 graden bij in/Calm/uit). Onder water = inhouden, menu, eind (alleen water, bundel bovenin, plek onderin, held vooraan en groot, minstens een kwart van de breedte in menu en hold).
- Het dier zelf verandert niet (vaste sticker via `d.dier` of `v3.dier_kantel`). De grap is een los voorwerp, groot genoeg om op 260 ware grootte als vorm te lezen. Geen grap die op beweging leunt of op iets wat de sticker zelf moet doen.
- Eigen plek per dier: nooit de rots met anemoon van de clownvis, de slipper van de krab of de zeegrasweide van de schildpad. Ronde zachte vormen met witte of lichte rand, drie tot vijf dingen per plek, alles binnen de ronde rand.
- Tekst vrij (veilige zone 6/260). "press START to breathe" blijft altijd staan op hold. Niets beloont langer inhouden; geen duikwoorden, dieptemeters, stopwatches of medailles.
- MIP (260): alleen de 64 kleuren (elke kanaal 0, 55, AA of FF hex); geen doorschijnend vullen, wit altijd als gewone kleur; gloed in drie vaste tinten. Op AMOLED (454) mag meer.
- Bekijk elk overzicht zelf met Read (260 2x en 454 1x) en verbeter tot de grap zonder uitleg leest. Vergelijk met de drie voorbeelden.
- Schrijf alleen in de bestanden hierboven (je eigen script, je eigen meetscript, `werelden4/` met je eigen dieren). Geen git commit of push, niets anders aanpassen; Mila slaat op.
- Werk maximaal 20 minuten. Schrijf in het Nederlands, gewone woorden, geen gedachtestreepjes.

## Antwoord (maximaal 300 woorden)
Per dier: wat je tekende (plek, grap), uitkomst contrast en veilige zone, wat je zelf zag en wat nog zwak is, en welk overzicht het sterkst is.
