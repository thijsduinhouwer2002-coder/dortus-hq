# Ebb Calm: keuring Daan

## Keuring 2, 13 nov 2026 ±16:25 UTC: zee die stijgt en daalt (81a7637)

**Akkoord: ja** voor commit 81a7637 op `claude/ebb-calm` (run 43459065492, groen), dus ook voor een nieuwe release daarvan. Bekeken: `calm-in`, `calm-hold` en `calm-out` op FR255, fenix 8 47 mm en vivoactive 5 (artifacts `calm-plaatjes-*`), naast elkaar in `ontwerp/garmin/calm-keuring2/in-hold-out-fr255-fenix8-va5.png`.
- Bij uit zakt de zee zichtbaar (vis en "Calm 4-7-8" zakken mee), bij in en vast staat hij hoog. Daarmee is "the water rises as you breathe in and falls as you breathe out" waar. **De tekst blijft zoals hij is**, niet zachter maken: het is de mooiste zin van de pagina en hij klopt nu.
- Alles binnen de rand op alle drie, ook het label bij uit op FR255 (het laagste punt).
- Kan-punt K8 (later): het wisselen gaat in vijf beurten; een zachtere overgang over de hele 4 seconden zou het nog rustiger maken. Geen reden om de release op te houden.
- Gijs: kaart 2 op `calm-hold` zetten is goed.

## Keuring 1, 13 nov 2026 ±12:45 UTC

**Akkoord: ja** voor indienen van Ebb Calm 1.0.0: app op tak `claude/ebb-calm` (code 6151a97, startpictogram eb23e97), plakteksten EN/DE/NL versie 1 (`platformen/garmin/upload/calm-*.md`), vijf winkelbeelden en icoon versie 1 (`ontwerp/garmin/winkel-calm/`). Geen moet-punten die de upload tegenhouden. Wel: Ebb Calm niet eerder openbaar dan Ebb zelf (de tekst noemt "a separate paid app in this store"), en de privacytekst wacht op Thijs.

Waarom wij, in één zin: de enige gratis 4-7-8 op Garmin die je met je ogen dicht volgt (eigen tril per fase) en die er als een kleine zee uitziet in plaats van een kale cirkel.

### Wat ik bekeek (GEZIEN)
- Run 43421506388 (groen), artifacts `calm-plaatjes-fenix847mm`, `-fr255`, `-vivoactive5`: alle tien schermen per horloge (menu, check, veilig 1 tot 3, ademen, pauze, einde 45 s, einde 4 min, instellingen). Met Read bekeken als contactblad.
- De vijf winkelbeelden en het icoon van 500 px.
- Het startpictogram `launcher_icon_calm.png` (40 en 65 px) naast dat van Ebb.
- `calm-en.md` zin voor zin.
- Controleur (agent) keek dezelfde plaatjes en de tekst: eens met ja, met kan-punten (hieronder overgenomen).

### Oordeel
- **App: mooi en rustig.** Alles staat in het midden, niets loopt door de ronde rand, ook niet op de 260 px van de FR255. Het ademscherm (paarse ochtendlucht, zon, wolk, vis half in het water) is het sterkste beeld en precies wat deze app anders maakt dan de grijze ademcirkels van de concurrent. De vis als aanwijzer in het pauzemenu is een fijn detail.
- **Startpictogram: ja.** Vis in de paarse zee, meteen anders dan de walvis van Ebb, leesbaar op 40 px.
- **Winkelbeelden: ja.** Kaart 1 ("Breathe in. The sea rises.") is een goede poster: kop kort, het scherm groot. Koppen en volgorde kloppen met de app.
- **Icoon 500: ja.** Grote vis in de patrijspoort, warm tussen de blauwe ademapps.
- **Tekst: ja.** Eerlijk, geen medische claims, veiligheid volledig.

### Antwoord op de vragen van Gijs
1. **De drie veiligheidsbladen blijven staan.** 4-7-8 heeft 7 seconden vasthouden, dus "Never force a hold. Stop if dizzy." klopt, en een rustige app die iemand laat flauwvallen is erger dan één extra blad. Ze komen bij de eerste start en daarna eens per 30 dagen (`Profiel.mc`, `DAGEN = 30`), plus via Settings, dus ze storen een vaste gebruiker nauwelijks.
2. **De eindregel is rustig genoeg:** kleine tekst, geen knop, geen pijl, het past in de sfeer. Wel een klein taalpunt (K2).

### Kan-punten (voor 1.0.1 of als je toch een nieuwe bouw maakt; houden de upload niet tegen)
- **K1, testscène einde 45 s.** De plaatjesscène toont "45 s · 4 breaths" (`Scenes.mc` regel 183, vaste getallen). Eén ronde 4-7-8 duurt 19 s; de echte app rekent `ms / cyclus` en toont dus "45 s · 2 breaths". Alleen de testscène is fout, de app niet. Zet de scène op 2, dan kan dat beeld nooit per ongeluk in de winkel.
- **K2, eindregel:** "The full Ebb adds / breath hold rounds / and 24 sea animals" leest beter dan met de komma. Op kaart 3 komt hij dan vanzelf mee.
- **K3, kaart 2** is de zwakste: een zwarte schijf (het checkscherm). Beter het scherm "hold 7" of "out 8" uit dezelfde zee, dan laten kaart 1 en 2 samen de ademhaling zien. Vraagt een nieuwe scène.
- **K4, kaart 3 en tekst gelijk:** kaart 3 zegt "breathwork, with heart rate", de tekst "a breathing activity ... with your heart rate". De hartslag is in de simulator niet bewezen (wel dezelfde code als Ebb). Houd het, maar kijk het na op het eerste echte horloge.
- **K5, "porthole" in de tekst:** in de app zelf zie je geen patrijspoort, alleen op het icoon. "Your round watch face becomes a small sea" is eerlijker.
- **K6, hoofdletters:** "paused", "calm done", "settings" klein, "Ebb Calm" en "Calm 4-7-8" groot. Dat is de stijl van Ebb (koppen klein, namen groot) en mag zo blijven; alleen "calm · 1:12" in de pauze mag "Calm 4-7-8 · 1:12" worden als het past.
- **K7, startpictogram 40 px:** de staart raakt net de rand; een pixel kleiner.
