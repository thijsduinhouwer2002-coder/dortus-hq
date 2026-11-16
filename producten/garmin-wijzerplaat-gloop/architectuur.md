# Architectuur wijzerplaat "Gloop's Hat Tower" (kale proef)

- `manifest.xml`: type watchface, eigen app-id, nu vier horloges (fenix7, fr255, venu3s, venusq2), geen permissies.
- `monkey.jungle`: plaatjes per schermbreedte (`res-260`, `res-320`, `res-390`), overgenomen uit de kit van het spel op tak `claude/garmin-gloop-2026-11-16` (Gloop rust en blij, tien hoeden, icoon).
- `source/GloopFaceApp.mc`: start de wijzerplaat.
- `source/GloopFaceView.mc`: tekent alles. `tekenVol` (gewone stand), `tekenToren` (hoeden stapelen, schuift in elkaar als de toren te hoog wordt), `tekenSlaap` (AMOLED), `tijdFont` (grootste cijfers die links van de toren passen), `tekst` (letter met zwarte rand).
- `source/Regel.mc`: de regels zonder scherm (hoeden per 1.000 stappen, kroon bij het doel, 12 en 24 uur). Tests in `source/RegelTest.mc`.
- `source/Maten.mc`: kopie van het spel (gemaakt door `maak_kit.py` daar). Verandert de kit, dan opnieuw kopiëren.
- `source/Bouw.mc`: `AUTO`. Met `true` toont de wijzerplaat elke 3 seconden een andere stand, voor de schermafbeeldingen. In de winkel altijd `false`.
- Bouwstraat: `.github/workflows/garmin-wijzerplaat-gloop.yml`. Beelden op tak `schermen`, map `garmin-wijzerplaat-gloop/<taknaam>/`. Het log toont `LIMIET` (geheugen per horloge voor een wijzerplaat) en `GEHEUGEN` (wat de proef gebruikt).
