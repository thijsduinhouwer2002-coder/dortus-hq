# Een wereld toevoegen aan Ebb

Gijs, 12 nov 2026 (run 58), op verzoek van de hoofdchat (besluit Thijs 08:15: tweede bouwer voor de 22 werelden zodra de krab een 8 haalt). Voor iemand die de code niet kent. Lees ook `REGELS.md` (regel 4 en 7 tot 10).

**Eerlijk vooraf.** Dit beschrijft de code zoals hij op 12 nov op de bouwtak staat (16bd5fd). Er staan twee werelden in als proef: de krab (wereld 0, verspreid over `KrabV2.mc`, `KrabV2Band.mc`, `KrabV2Lagen.mc`, `KrabV2Boven.mc`) en de schildpad (wereld 1, bijna helemaal in `KrabV2Schild.mc`). **De schildpad is het voorbeeld om na te doen.** De werelden zitten nog alleen in de testscènes, niet in de echte sessie. En een wereld inpluggen kan nu nog niet zonder de bestanden van Gijs aan te raken: zie "Wat Gijs nog moet doen" onderaan. Tot dat klaar is levert de tweede bouwer alleen zijn eigen bestand en plugt Gijs het in.

## 1. Wat een wereld is

Eén dier (de held) op zes schermen, elk bij dag en bij nacht, dus twaalf beelden:

| Nummer | Scherm | Waar |
|---|---|---|
| 0 | inademen | boven water |
| 1 | uitademen | boven water |
| 2 | Calm | boven water |
| 3 | inhouden | onder water |
| 4 | menu | onder water |
| 5 | eindscherm ("new friend") | onder water |

Boven water zijn lucht, zon of maan, wolk, de kam en de golven voor elke wereld gelijk (`KrabV2Boven.boven`). Onder water zijn het verloop van het water, de lichtbundel en de belletjes gelijk (`KrabV2Lagen.onder`). Een wereld voegt daar zijn eigen dingen aan toe: de bodem en planten onder water, één drijvend ding boven water, en de grap bij de held (zwemband, meeuw op het schild).

Alle maten zijn in 1/260 van de schermbreedte, zoals op Mila's blad van 260 pixels. `v.q(maat)` rekent om naar het echte scherm. Schrijf nooit een maat in echte pixels.

## 2. Hoe het tekenen gaat

`KrabV2View` (in `KrabV2.mc`) tekent een scherm in stukjes, omdat een horloge anders te lang over één beurt doet en de app dan gestopt wordt (watchdog):

1. **Vijf lagen, één per beurt**, in een plaatje dat blijft staan: laag 0 de achtergrond (lucht of water), laag 1 tot 3 de wereld van ver naar dichtbij, laag 4 wat direct onder of achter de held staat.
2. **Daarna elke beurt:** het plaatje, de held (het dier, gekanteld), dan wat vóór de held hoort, dan de tekst.

Houd elke laag klein. Maatstaf: een beurt blijft op AMOLED onder de 100 ms in de simulator (de plukken van de schildpad zaten op 108 tot 183 ms en moeten goedkoper). Dikke lijnen zijn goedkoper dan veelhoeken.

## 3. Wat jouw bestand levert

Eén bestand `source/KrabV2<Naam>.mc` met één module `KrabV2<Naam>`, hoogstens 300 regels (anders splitsen). Neem `KrabV2Schild.mc` als voorbeeld. Deze functies, met precies deze vorm:

| Functie | Wat |
|---|---|
| `held(s as Number) as Array<Number>` | per scherm 0 tot 5: midden van het dier x, y en zijn maat, in 1/260 |
| `kantel(s as Number) as Float` | per scherm de hoek in graden (min is neus omhoog, het dier kijkt naar links) |
| `onder(v, dc, stap, am, nacht, scherm)` | onder water, laag 1 tot 3: ver (ruggen, zand), midden (planten aan de randen), dichtbij (klein spul) |
| `onderHeld(v, dc, scherm, am, h)` | onder water, laag 4: schaduw of voorwerp direct onder de held (`h` is de uitkomst van `held`) |
| `boven(v, dc, top)` | boven water, laag 3: één drijvend ding onder het oppervlak, alleen als een frisse kijker het herkent (krab en schildpad hebben er nu geen: de verre slipper en het drijvende blad lazen niet) |
| `voor(v, dc, scherm, am, nacht, h, graden)` | elke beurt na de held: de grap en wat voor het dier langs loopt (golfje voor de buik, voorhelft van de zwemband) |

`v` is de `KrabV2View`, `dc` het tekenvlak, `am` waar op een AMOLED-scherm, `nacht` waar bij nacht. Welk dier de held is (het nummer uit `DierenData.mc`) geef je door aan Gijs; het dier zelf teken je nooit (regel 4).

## 4. Wat je gebruikt in plaats van zelf te schrijven

- **Kleur:** altijd `v.kleur(dc, 0xRRGGBB)` voor een vlak en `v.pen(dc, 0xRRGGBB)` voor een lijn, nooit `dc.setColor`. Die twee doen de nachtregel (`Nacht.mc`, Mila v1.2) en de 64 kleuren van MIP vanzelf. Je geeft dus alleen de dagkleur op.
- **Vormen:** `v.rondje` (ovaal met rand en glans), `v.blob` (ronde veelhoek), `v.golf`, `v.gloed` en `v.glas` (doorschijnend, alleen AMOLED), `KrabV2Lagen.verloop`, `KrabV2Lagen.vierhoek`.
- **Een los voorwerp plaatsen:** `KrabV2Lagen.inRond(x, y, r)` schuift het naar binnen tot het 10/260 van de ronde rand blijft (regel 10); meld het daarna met `KrabV2Rand.meet(v, scherm, naam, x, y, r)`, dan staat de meting in het log. Alleen bodem, rotsen en water mogen door de rand lopen.
- **Voorwerp bij tekst:** `KrabV2Tekst.raakt(v, x, y, r)` zegt of het binnen 6/260 van tekst staat; dan niet tekenen of korter maken (zie de sprieten in `KrabV2Schild.onder`).
- **Achter de held** staat nooit iets in zijn eigen kleurfamilie: laat een open plek (`KrabV2Schild.openPlek`).
- **Versiering (belletje, ster, vonk):** vraag eerst `KrabV2Tekst.vrij(v, x, y, r)`. Geeft die onwaar, dan teken je het niet (regel 9).
- **Tekst teken je niet.** Alle tekst van de zes schermen staat in `KrabV2Tekst.mc`.

## 5. Waar je werk op getoetst wordt

De plaatjesrun (`.github/workflows/garmin-adem-iq.yml`) start op dertien horloges elke scène in de echte simulator, maakt een schermafbeelding en leest het log. De run wordt rood bij een crash, bij "watchdog", bij "out of memory" en bij elke regel met `VEILIG ... NEE`.

1. **Veilige zone (regel 8):** minstens 6/260 lucht tussen elk tekstvak en de held met zijn grap, ook als hij kantelt. De app meet het zelf en schrijft `VEILIG wereld N scherm S ... ja` of `NEE`. Staat je held te hoog, dan zet je hem lager in `held`; de tekst schuift niet.
2. **Versiering:** het log zegt `VERSIERING wereld N scherm S getekend X, geweken voor tekst Y`. Wijkt bijna alles, dan staat je versiering op de verkeerde plek.
3. **Rand:** een los voorwerp staat 10/260 binnen de ronde rand. Het log zegt `VEILIG wereld N scherm S rand <naam> lucht X van 260, norm 10 ja` of `NEE`.
4. **Contrast:** elke tekstregel haalt 4,5 op 1 tegen wat jij erachter tekent. Geen licht voorwerp achter witte tekst.
5. **Grap herkenbaar (besluit 12 nov 06:00):** een frisse kijker ziet alleen het beeld van 260 pixels en zegt wat het is. Herkent die de grap niet, dan gaat de grap eruit. Dat doet de hoofdchat, niet de bouwer.
6. **Regels van de code:** hoogstens 300 regels per bestand, bouwt zonder waarschuwingen (`-l 2`); de toetsworkflow `garmin-adem-e2e.yml` controleert dat.

## 6. Hoe je wereld in de plaatjesrun komt

- **Tak:** werk op een eigen tak met "proef" in de naam, bijvoorbeeld `claude/garmin-werelden-proef-<naam>`. Op zo'n tak draait de plaatjesrun alleen de wereldscènes (vanaf 51) en is de uitslag er in ongeveer tien minuten in plaats van veertig.
- **Scènenummer:** `51 + 12 x wereld + 6 x nacht + scherm`. Krab is 51 tot 62, schildpad 63 tot 74. Let op: 75 en 76 zijn nu het thuiswater van het startscherm; dat krijgt een eigen plek voordat wereld 2 erbij komt (zie onderaan).
- **Beelden:** de run zet ze openbaar op tak `schermen`, map `garmin-adem/plaatjes-proef/namen/` (proeftak) of `garmin-adem/plaatjes/namen/` (bouwtak), als `<naam>-<horloge>.png`. Kijk altijd zelf naar FR255 (MIP, 260) en fenix 8 47 mm (AMOLED, 454), dag en nacht, naast Mila's blad.
- **Uitslag lezen:** `curl -s "https://api.github.com/repos/thijsduinhouwer2002-coder/dortus-hq/actions/runs?branch=<tak>&per_page=4"`.
- **Bundelen:** alle punten van een keuring in één run, en één keer beelden maken.

## 7. Wat Gijs nog moet doen voordat de tweede bouwer begint

Nu staat op ongeveer twintig plekken in de bestanden van Gijs een vertakking per wereld (`if (wereld == 1)`): in `KrabV2.mc` (held en kantel bij de start, laag 4, `voor`, de nieuwe vriend op het eindscherm), `KrabV2Lagen.mc` (laag 1 tot 3, plek van de lichtbundel, belletjes), `KrabV2Boven.mc` (laag 3, meeuw) en `KrabV2Tekst.mc` (ruimte boven de held, naam van de nieuwe vriend, veilige zone). Verder staan het aantal scènes in `Bouw.mc` en de lijst `NAMEN` en de teller `seq $EERSTE 76` in de workflow vast. Daarmee kan een tweede bouwer nu geen wereld toevoegen zonder die bestanden te wijzigen.

Wat Gijs daarvoor bouwt, in één run, vóór de start van de tweede bouwer:

1. Eén bestand `KrabV2Werelden.mc`: de enige plek waar een wereldnummer naar een module wijst (held, kantel, onder, onderHeld, boven, voor, het dier, de nieuwe vriend, de plek van de lichtbundel). Alle vertakkingen hierboven vragen het daar. Een wereld toevoegen is dan één blok in dat bestand, en dat blok voegt Gijs toe bij het samenvoegen.
2. De krab in dezelfde vorm als de schildpad (`KrabV2Krab.mc` met dezelfde zes functies), zodat er geen uitzondering voor wereld 0 meer is.
3. Het thuiswater een eigen scènenummer buiten de reeks van de werelden, en de scènes en namen van de werelden uit het aantal werelden laten volgen, zodat `Bouw.mc` en de workflow niet per wereld gewijzigd hoeven.
4. Bewijs dat er niets verandert: de beelden van krab en schildpad voor en na pixel voor pixel gelijk (`bron/vergelijk_plaatjes.py`, regel 6).

Daarna geldt: de tweede bouwer raakt alleen `source/KrabV2<Naam>.mc` aan, op zijn eigen tak; Gijs voegt samen en zet het ene blok in `KrabV2Werelden.mc`.

## 8. Wat nog niet vastligt

- Hoe een wereld eruit moet zien ligt pas vast als de krab op echte schermen een 8 haalt. Tot dan kan de vorm van de zes functies nog veranderen.
- De werelden hangen nog niet aan de klok van de sessie (de zee stijgt en zakt niet mee, het zijn stilstaande beelden). Dat is werk van Gijs en verandert jouw bestand niet, zolang je alleen de zes functies levert.
- Geheugen: elke wereld is nu code en zit dus altijd in het bestand. Bij 24 werelden van ±200 regels moet gemeten worden of dat op de FR255 past. Gijs meet dit na de eerste vijf werelden; past het niet, dan worden de werelden gegevens (zoals de oude opzet in `Wereld.mc`, regel 7).
