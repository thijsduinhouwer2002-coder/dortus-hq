# Architectuur wijzerplaat "Gloop's Hat Tower" (kale proef)

- `manifest.xml`: type watchface, eigen app-id, nu vier horloges (fenix7, fr255, venu3s, venusq2), geen permissies.
- `monkey.jungle`: plaatjes per schermbreedte (`res-260`, `res-320`, `res-390`), overgenomen uit de kit van het spel op tak `claude/garmin-gloop-2026-11-16` (Gloop rust en blij, tien hoeden, icoon).
- `source/GloopFaceApp.mc`: start de wijzerplaat.
- `source/GloopFaceView.mc`: tekent alles. `tekenVol` (gewone stand), `tekenToren` (hoeden stapelen met buiging; kroon in beeld op het doel, daarna het scherm uit), `tekenSlaap` (AMOLED), `tijdFont` (grootste cijfers waarbij uren boven minuten passen); `onUpdate` houdt bij welke hoed de drager al zag landen (`gezien`, `wek`), `tekst` (letter met zwarte rand).
- `source/Regel.mc`: de regels zonder scherm (hoeden per 1.000 stappen, kroon bij het doel, 12 en 24 uur, afstand tussen de hoeden `stap`, `buiging`, de ronde rand `randLinks` en `randBoven`, en `wachtend`: de hoed valt pas als je kijkt). Tests in `source/RegelTest.mc`.
- `source/Maten.mc`: kopie van het spel (gemaakt door `maak_kit.py` daar). Verandert de kit, dan opnieuw kopiëren.
- `source/Bouw.mc`: `AUTO`. Met `true` toont de wijzerplaat elke 3 seconden een andere stand, voor de schermafbeeldingen. In de winkel altijd `false`.
- Bouwstraat: `.github/workflows/garmin-wijzerplaat-gloop.yml`. Beelden op tak `schermen`, map `garmin-wijzerplaat-gloop/<taknaam>/`. Het log toont `LIMIET` (geheugen per horloge voor een wijzerplaat) en `GEHEUGEN` (wat de proef gebruikt).

## Run 114 (16 nov ±12:05 UTC): de kit van Mila ingebouwd
- `source/Plek.mc` is gemaakt uit `ontwerp/garmin/wijzerplaat-gloop/kit/wijzerplaat.json`: per schermbreedte de plekken in pixels (Gloop, tijd, datum, stappen, regel, veld) en de torentabel van 24 plekken. Niet met de hand aanpassen.
- De tijd is geen font meer maar plaatjes: `Uur0..9` (wit) en `Min0..9` (mint). Alleen de vier cijfers die in beeld staan zijn geladen (`cijfer(vak, nr)`), de rest pas als de tijd verspringt.
- `Achter` (achtergrond per maat), `GloopKijk` (oog omhoog) en voor de slaapstand `GloopAod` en `HoedAod0..9` (alleen AMOLED; in `res-260` wijzen die namen naar een leeg plaatje van 1 px zodat de code overal compileert).
- Slaapstand: zelfde cijferplaatjes, grijs gekleurd met `drawBitmap2` en `tintColor` waar het horloge dat kent, anders gewoon.
- Regels in `Regel.mc`: `aantal` (kroon is de bovenste hoed, telt mee), `regel` ("7/10 HATS", "GOAL!", "GOAL! +4") en `punt` ("7.612"), elk met een toets.
