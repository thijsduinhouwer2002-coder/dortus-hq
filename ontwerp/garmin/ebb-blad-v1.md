# Ebb blad v1: alle schermen (Mila, 10 nov run 15 en 16)

Blad: **`ontwerp/garmin/ebb-blad-v1.png`** (per scherm links 454 px, rechts 260 px, ware grootte). Losse beelden en meting in `ontwerp/garmin/blad/`, bron `ontwerp/garmin/bron/ebb_blad.py`. Gaat eerst naar Thijs via de hoofdchat; Gijs bouwt pas na zijn ja.

## Beeldtaal van Ebb in 10 regels (eerst het gevoel, dan de schermen)
1. **Gevoel: één duik, van kust tot diep en terug.** Menu is de kust (laag tij onderin), ademen is golven, inhouden is zakken, boven komen is zon, het resultaat is je duikprofiel. Elk scherm is een plek in dat ene verhaal.
2. **Rust boven alles.** Eén groot ding per scherm (het getal), hooguit twee kleine regels. Wat beweegt, beweegt traag: golf 2 golven per scherm, peil op het tempo van je adem.
3. **Vorm: de patrijspoort.** Ring met acht bouten langs de rand van elk scherm; alles staat in het midden en gespiegeld. Dat is ons gezicht, van icoon tot instellingen.
4. **Water in vlakken, nooit in verloop.** Drie of vier vaste MIP-tinten met golfranden: hoe dieper, hoe donkerder. Schuim (0x55FFFF) alleen op de bovenste golf.
5. **Kleur: koud met één warme stem.** Turkoois en nachtblauw op zwart; koraal alleen voor wat leeft of wat je bereikt (dieren, record, waarschuwing); geel alleen voor de zon.
6. **Letter: Barlow Condensed Medium**, overal dezelfde, kleine letters voor woorden ("in", "hold", "today"), getallen groot en smal.
7. **Tekst en water spelen samen.** Wat onder water staat, kleurt mee (nachtblauw); het getal wordt door de golf gesneden. Tekst staat nooit op een golfrand.
8. **Dieren: rond, vrolijk, gevuld.** Gevulde vlakken in koraal met een lichte buik en een oog met glans, geen lijntjes die klein wegvallen. Ze kijken naar links, zwemmen naar het midden en dobberen daar. Een dier is een beloning, nooit versiering.
9. **Grafieken zijn zee, geen statistiek.** Today is een duikprofiel in dezelfde diepte-banden, 8 weeks is een getij. Kader binnen 15 tot 85% van D, gespiegeld.
10. **Overgangen voelen als water.** Van scherm naar scherm stijgt of zakt het peil (geen harde wissel); bij een record één korte trilling en een koraal stip, geen vuurwerk.

**De lat, drie voorbeelden:**
- **ABZÛ** (Giant Squid): een duik als verhaal, kleur wordt donkerder met de diepte en dieren zijn de beloning. Wij nemen over: diepte vertellen met kleur, dieren als ontmoeting.
- **Alto's Odyssey** (Snowman): vlakke kleurlagen zonder drukte, rust door één horizon. Wij nemen over: lagen in vaste tinten, één lijn (de golf) die het hele scherm draagt.
- **Headspace**: rustige ademoefening met figuren die je laten glimlachen. Wij nemen over: rust met een knipoog (de walvis die lacht), nooit klinisch zoals de huidige ademapps op Garmin (kale ring of tekst, GEZIEN in run 12).


Opdracht: besluit hoofdchat met Thijs 10 nov 19:45 (de hele app mooi) en de harde regel van 20:20 (alles in het midden). Dit blad gaat **eerst naar Thijs** via de hoofdchat. Gijs bouwt pas na zijn ja. Daan keurt daarna blad en bouw.

- Losse schermen: `ontwerp/garmin/blad/ebb-blad-<n>-<D>.png`; walvis groot: `ebb-walvis-v3-patrijspoort.png`
- Bron met alle maten als deel van D: `ontwerp/garmin/bron/ebb_blad.py` (letter Barlow Condensed Medium, OFL, dezelfde als Gijs' cijfers)
- Meting: `ontwerp/garmin/blad/meting.txt`

## Het idee in één zin
Elk scherm is dezelfde patrijspoort: een donkere ring met acht bouten langs de rand, daarbinnen zee of nacht, en alles staat recht in het midden. Zo herken je Ebb op elk scherm, ook in het menu, en belooft de winkel niets wat de app niet laat zien.

## De haken
1. **Het getal zakt mee in het water.** Bij ademen en rustig ademen snijdt de golf door het grote getal: boven het water wit, onder water nachtblauw. Het fasewoord botst nooit meer met de golfrand (punt 4 van de hoofdchat), en het water voelt echt. In Monkey C: het getal twee keer tekenen met `setClip` boven en onder de golf (stroken van 4 px).
2. **Boven komen is een zonsopkomst.** Na de duik zakt het water en komt er een gele zon boven de golf: "breathe in", 15 tellen.
3. **De duik wordt donkerder in banden** (geen verloop, drie MIP-tinten met golfranden), het dier zwemt naar het midden onder de tijd en blijft daar dobberen.
4. **Sea log als verzameling:** drie dieren bovenaan en de walvis groot eronder; een dier dat je nog niet zag is een donker silhouet met een vraagteken met de tijd die je moet halen ("3 of 4 met"). Dat is de reden om morgen terug te komen.

## Per scherm, met in één zin wat Gijs bouwt
Haalbaarheid voor alle schermen: alleen `fillPolygon`, `fillCircle`, `fillRoundedRectangle`, `drawLine` en `drawText` met 64 MIP-kleuren; de golf is één veelhoek van ±60 punten (zoals nu al in `Teken.mc`); Barlow Condensed als eigen letter (FNT met PNG, zoals Gijs' cijfers nu, geheugen nu 4 tot 6%, GEZIEN in `metingen.txt`). Geen bitmaps nodig behalve de letter.
1. **Menu** (punt 1): "Ebb" in licht turkoois, gekozen regel in een pil precies in het midden (62% D breed), vorige en volgende klein en gedimd, geen schuifbalk, en in het lage tij komt de walvis met zijn spuitje boven (de grap op het eerste scherm). *Gijs:* eigen `View` met `onUpdate` in plaats van `Menu2` (Menu2 laat de pil en het water niet toe), omhoog en omlaag schuiven de lijst, walvis eerst tekenen en dan het water eroverheen.
2. **Ademen:** water tot 54% (peil volgt de adem), fasewoord bovenaan, getal 34% D gesneden door de golf: wit boven, nachtblauw onder water; "of 30 · round 2" in het water. *Gijs:* het getal twee keer tekenen, met `dc.setClip` op stroken van 4 px boven en onder de golf (±12 stroken over de breedte van het getal; `setClip` bestaat sinds Connect IQ 2.3, GOK, alle negen horloges zitten ver daarboven).
3. **Duiken:** drie diepte-banden met golfranden, diepte in schuim, tijd 30% D, dier op 70% D, belletjes in gespiegelde paren. *Gijs:* drie `fillPolygon` per frame; het dier zwemt van rechts naar het midden en dobbert daar (±2 px op en neer per 2 s) in plaats van door te zwemmen.
3b. **Walvis op 3:03** (punt 5, W1, W7): walvis v3 = Daans richting v2 (lichte buik, schuine borstvin, oog met glans, gevulde glimlach in 0xAA0000, tekenfilmstaart), niets in de waterkleur, plus een glansboog op de kop als hij groot is. *Gijs:* de punten uit `dieren_richting_daan.py` (al rond het midden van het kader) en de boog uit `walvis3()`.
3c. **Schildpad op 2:03** (W5): Daans schildpad (van opzij, lichte platen en buikschild, peddelpoten), op 1,45 eenheid, midden onder de tijd. *Gijs:* punten uit `dieren_richting_daan.py`, `schildpad()`.
4. **Boven komen:** gele zon achter de golf, "breathe in" in geel, tel 24% D, "held 1:34" in het water. *Gijs:* één `fillCircle` vóór de golf, verder als ademen.
5. **Rustig ademen 4-7-8** (punt 4, W10): zelfde gesneden getal als ademen, naam "4-7-8" in het water in nachtblauw, op alle horloges onder de golf (laagste peil 44% in de fase "uit"). *Gijs:* `getal_gesplitst` van scherm 2 hergebruiken; naam vast op 75% D.
6. **Today** (punt 2, W9): doorlopend duikprofiel zoals een duikcomputer, kommen met een ronde bodem, gevuld in dezelfde banden als de duik, koraal stip op de diepste en het label gecentreerd onder de stip ("2:08 new best", alleen bij een record; anders lichtgeel zonder "new best"). Grafiek 15% tot 85% D. *Gijs:* per ronde 25 punten (`profiel_lijn()`), de banden als drie `setClip`-stroken over dezelfde veelhoek.
7. **8 weeks** (punt 3): getij-vlak (gemiddelde van 7 dagen) in diep blauw, beste per dag als schuimlijn met gaten, weekstreepjes op beide uiteinden, grafiek 16% tot 84% D. *Gijs:* het bestaande vlak houden (M2), alleen de marges en het randje uit `s_weken()`.
8. **Sea log** (W8): bovenaan vis, kwal en schildpad op één hoogte (±0,085 D), onderaan in het midden de walvis, het breedst; een dier dat je nog niet zag is een donkerblauw silhouet met een vraagteken ("3 of 4 met"). *Gijs:* `walvis_silhouet()` is alleen lijf, staart en vin in 0x0055AA.
9. **Settings:** zelfde opbouw als het menu, waarde met pijltjes in de pil. *Gijs:* dezelfde `View` als het menu, links en rechts veranderen de waarde.
10. **Veiligheid:** koraal waarschuwingsdriehoek, drie korte regels, knop OK in de pil, laag tij onderin. *Gijs:* tekst op vaste hoogtes, langste regel past binnen de koorde (GEZIEN: 69% van de straal).

## Vergelijking met de mooiste Connect IQ-apps (winkel-API met curl, run 16)
Bekeken: Pokémon Sleep: Snorlax & Friends (4,9 sterren, 1.969 reviews, 100.000+), Butterflies (4,8, 3.428), Minimal Lines (4,9, 501) en Surfline (4,0, 833), DERDEN (apps.garmin.com, winkel-API).
- **Snorlax:** een figuur groot in het midden van een kleine wereld, ronde vlakjes onderaan, alles gespiegeld. Dat werkt omdat het scherm een plek is. Overgenomen: de walvis in het menu, elk scherm een plek in de zee.
- **Minimal Lines:** een eigen cijferstijl maakt de hele app herkenbaar. Bij ons doet het gesneden getal dat (wit boven, blauw onder water).
- **Butterflies:** rijk door één volle kleurlaag achter de tijd. Bij ons de diepte-banden.
- **Surfline** is een app over de zee en toont kale tekst. Daar zit precies ons gat: niemand op Garmin laat de zee zien.

## Kleuren (alleen MIP, kanalen 00, 55, AA, FF)
Ring 0x005555 met bouten 0x55AAAA; water 0x00AAFF (ademen, boven), 0x00AAAA (rustig), banden 0x0055AA, 0x0000AA, 0x000055 (duik, today, 8 weeks); schuim 0x55FFFF; zachte tekst 0x55AAAA; gedimd 0x555555; pil 0x0055AA; koraal 0xFF5555 en 0xFFAAAA alleen voor dieren, record en waarschuwing; zon 0xFFFFAA.

## Gemeten (GEZIEN, `meting.txt`)
- Midden van het kader van alles wat getekend is: op alle 24 beelden binnen 0,5 px van het schermmidden (eis 2 px).
- Zwaartepunt horizontaal: binnen 0,4 px op alle schermen behalve today (6,6 px), 8 weeks (22,7 px op 454) en sea log (1,8 px). Dat komt door de gegevens zelf (de diepste duik en de stijgende lijn wegen zwaarder); het kader van de grafiek staat wel exact in het midden. Een grafiek met echte gegevens kan nooit gespiegeld zijn, daarom toetst Daan bij grafieken op het kader.
- Verste tekst of figuur vanaf het midden: hooguit 72% van de straal (eis: binnen 80%). Alleen de ring met bouten ligt buiten de veilige cirkel, met opzet.

## Voor Gijs (pas na het ja van Thijs)
Alles staat in `ebb_blad.py` als deel van D; de functies heten naar de schermen (`s_menu`, `s_ademen`, ...). Walvis: punten uit `dieren_richting_daan.py` (al gecentreerd), plus de glansboog uit `walvis3()`. Zet in de test een meting zoals `meet()` (kader binnen 2 px van het midden) op elk scherm van elk horloge.
