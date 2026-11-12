# Een wereld toevoegen aan Ebb

Gijs, 12 nov 2026 (run 58), op verzoek van de hoofdchat (besluit Thijs 08:15: tweede bouwer voor de 22 werelden zodra de krab een 8 haalt). Voor iemand die de code niet kent. Lees ook `REGELS.md` (regel 4 en 7 tot 10).

**Eerlijk vooraf.** Sinds run 60 (12 nov) is er een inplugpunt: `source/KrabV2Werelden.mc`. Een wereld toevoegen is je eigen bestand plus één regel in de lijst daar (hoofdstuk 7). Er staan twee werelden in: de krab (wereld 0, `KrabV2Krab.mc` met de zwemband in `KrabV2Band.mc`) en de schildpad (wereld 1, `KrabV2Schild.mc`). **De schildpad is het voorbeeld om na te doen.** De werelden zitten nog alleen in de testscènes, niet in de echte sessie; dat bouwt Gijs en het verandert jouw bestand niet.

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

Eén bestand `source/KrabV2<Naam>.mc`, hoogstens 300 regels (anders splitsen), met twee dingen: een module `KrabV2<Naam>` met de functies hieronder, en onderaan het aanmeldblok `class KrabV2W<Naam> extends KrabV2Wereld` dat die functies doorgeeft en zegt welk dier de held is (`dier`) en wie de nieuwe vriend is (`vriend`, `vriendNaam`). Neem `KrabV2Schild.mc` als voorbeeld, ook voor het blok. Wat je in het blok weglaat doet niets. Deze functies, met precies deze vorm:

| Functie | Wat |
|---|---|
| `held(s as Number) as Array<Number>` | per scherm 0 tot 5: midden van het dier x, y en zijn maat, in 1/260 |
| `kantel(s as Number) as Float` | per scherm de hoek in graden (min is neus omhoog, het dier kijkt naar links) |
| `onder(v, dc, stap, am, nacht, scherm)` | onder water, laag 1 tot 3: ver (ruggen, zand), midden (planten aan de randen), dichtbij (klein spul) |
| `onderHeld(v, dc, scherm, am, h)` | onder water, laag 4: schaduw of voorwerp direct onder de held (`h` is de uitkomst van `held`) |
| `boven(v, dc, top)` | boven water, laag 3: één drijvend ding onder het oppervlak, alleen als een frisse kijker het herkent (krab en schildpad hebben er nu geen: de verre slipper en het drijvende blad lazen niet) |
| `voor(v, dc, scherm, am, nacht, h, graden)` | elke beurt na de held: de grap en wat voor het dier langs loopt (golfje voor de buik, voorhelft van de zwemband) |

`v` is de `KrabV2View`, `dc` het tekenvlak, `am` waar op een AMOLED-scherm, `nacht` waar bij nacht. Welk dier de held is (het nummer uit `DierenData.mc`) zet je in je aanmeldblok; het dier zelf teken je nooit (regel 4). In `KrabV2Wereld` (bovenaan `KrabV2Werelden.mc`) staan nog een paar zelden nodige knoppen (plek van de lichtbundel, belletjes, hoogte van de kam, eigen meting van de grap); gebruik die alleen met een reden uit een keuring.

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
- **Scènenummer en naam:** volgen vanzelf uit de lijst: `53 + 12 x wereld + 6 x nacht + scherm` (krab 53 tot 64, schildpad 65 tot 76; 51 en 52 zijn het thuiswater). De beelden heten `<naam>-<in|uit|calm|hold|menu|eind>-<dag|nacht>-<horloge>.png`, met de naam uit jouw regel in de lijst. Je hoeft `Bouw.mc`, `Scenes.mc` en de workflow niet aan te raken.
- **Beelden:** de run zet ze openbaar op tak `schermen`, map `garmin-adem/plaatjes-proef/namen/` (proeftak) of `garmin-adem/plaatjes/namen/` (bouwtak), als `<naam>-<horloge>.png`. Kijk altijd zelf naar FR255 (MIP, 260) en fenix 8 47 mm (AMOLED, 454), dag en nacht, naast Mila's blad.
- **Uitslag lezen:** `curl -s "https://api.github.com/repos/thijsduinhouwer2002-coder/dortus-hq/actions/runs?branch=<tak>&per_page=4"`.
- **Bundelen:** alle punten van een keuring in één run, en één keer beelden maken.

## 7. Inpluggen: één regel

In `source/KrabV2Werelden.mc` staat de lijst, in de functie `maak`:

```
if (w == 0) { return new KrabV2WKrab(); } // naam: krab2
if (w == 1) { return new KrabV2WSchild(); } // naam: schild2
```

Jouw wereld is de volgende regel: het volgende nummer (zonder gaten), jouw blok, en achter `// naam:` een kort woord in kleine letters en cijfers zonder spaties. Dat woord wordt de naam van je beelden en de workflow telt deze regels om te weten hoeveel scènes er zijn. Meer hoeft niet.

- **Tweede bouwer:** op je eigen tak mag je die ene regel zelf toevoegen om beelden te krijgen. Raak verder alleen je eigen bestanden aan. Gijs voegt samen; bij twee bouwers die dezelfde regel toevoegen kiest Gijs de nummers.
- Nergens anders in de code staat nog een vertakking per wereld. Mis je iets wat je wereld nodig heeft (een knop in `KrabV2Wereld`), schrijf het in `berichten/gijs.md`; bouw het niet zelf in de bestanden van Gijs.
- Bewijs dat het inplugpunt niets veranderde: de beelden van krab en schildpad voor en na zijn vergeleken, zie `platformen/garmin/status.md` (run 60).

## 8. Wat nog niet vastligt

- Hoe een wereld eruit moet zien ligt pas vast als de krab op echte schermen een 8 haalt. Tot dan kan de vorm van de zes functies nog veranderen.
- De werelden hangen nog niet aan de klok van de sessie (de zee stijgt en zakt niet mee, het zijn stilstaande beelden). Dat is werk van Gijs en verandert jouw bestand niet, zolang je alleen de zes functies levert.
- Geheugen: elke wereld is nu code en zit dus altijd in het bestand. Bij 24 werelden van ±200 regels moet gemeten worden of dat op de FR255 past. Gijs meet dit na de eerste vijf werelden; past het niet, dan worden de werelden gegevens (zoals de oude opzet in `Wereld.mc`, regel 7).
