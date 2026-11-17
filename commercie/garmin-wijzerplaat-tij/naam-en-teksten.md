# Wijzerplaat Tij: naam, werkteksten van de instellingen, eerlijke punten voor de winkeltekst

Chris, 17 nov 2026, run 77 (±07:45 tot 08:30 UTC). Antwoord op de vraag van Gijs (berichten/chris.md, 17 nov ±07:25 UTC) en op zijn vraag van 16 nov 23:05 UTC (naam van de plaat zonder "Tide").

Labels: GEZIEN (zelf gemeten of gelezen), DERDEN (bron), GOK (schatting). Winkel gemeten op 17 nov ±08:00 UTC met curl op de open zoek-API van de winkel (`.../api/asw/apps/keywords?keywords=<woord>&pageSize=30&sortType=mostRelevant&appType=watchface`, en zonder `appType` voor alle soorten). Scripts: `meet-naam.py` (hoeveel namen dragen het woord) en `zoek-woord.py` (de eerste treffers op een woord).

## 1. Werkteksten van de instellingen

Bron voor hoe Garmin het zelf noemt: de lijst met glances in de handleiding van de Forerunner 255, in het Engels, Duits en Nederlands (DERDEN, GEZIEN 17 nov):
- EN: https://www8.garmin.com/manuals-apac/webhelp/forerunner255series/EN-SG/GUID-8CE5FED3-1CB4-41FF-9EE4-52C10E3BF8D3-7298.html en de pdf https://www8.garmin.com/manuals/webhelp/GUID-676967A0-1B23-4384-9BC9-76F3D643F1C8/EN-US/Forerunner_255_OM_EN-US.pdf
- DE: zelfde map, `DE-DE/Forerunner_255_OM_DE-DE.pdf`
- NL: zelfde map, `NL-NL/Forerunner_255_OM_NL-NL.pdf`

Garmin schrijft de namen van glances met alleen een hoofdletter aan het begin ("Heart rate", "Floors climbed", "Intensity minutes"). Onze werkteksten doen dat ook. Goed zo.

| id | Werktekst | Garmin zelf (EN) | Mijn advies EN | DE | NL |
|---|---|---|---|---|---|
| ThemaTitel | Theme | (Garmin: "Styles", "Accent Color"; Theme is gewoon en duidelijk) | **Theme** | Thema | Thema |
| ThemaDusk / Tide / Kelp / Night | Dusk, Tide, Kelp, Night | n.v.t. | **zo laten** (namen, niet vertalen) | Dusk, Tide, Kelp, Night | Dusk, Tide, Kelp, Night |
| Veld1Titel | Left field | (Garmin: "data field") | **Left field** | Feld links | Veld links |
| Veld2Titel | Middle field | | **Middle field** | Feld Mitte | Veld midden |
| Veld3Titel | Right field | | **Right field** | Feld rechts | Veld rechts |
| VeldHart | Heart rate | Heart rate | **zo laten** | Herzfrequenz | Hartslag |
| VeldStress | Stress | Stress | **zo laten** | Stress | Stress |
| VeldStappen | Steps | Steps | **zo laten** | Schritte | Stappen |
| VeldCalorie | Calories | Calories | **zo laten** | Kalorien | Calorieën |
| VeldTrappen | Floors climbed | Floors climbed | **zo laten** | Stockwerke | Geklommen etages |
| VeldMinuten | Intensity minutes (week) | Intensity minutes (de glance toont het weektotaal en het weekdoel) | **zo laten** | Intensitätsminuten (Woche) | Intensieve minuten (week) |
| VeldAfstand | Distance | (Garmin: "Distance", in de dagoverzichten) | **zo laten** | Distanz | Afstand |
| VeldAccu | Battery | "Battery" voor het horloge, maar ook "Body Battery level" | **anders: Watch battery** | Uhr-Akku (Garmin: Akkuladestand) | Horlogebatterij (Garmin: Batterijstatus) |
| VeldTemp | Temperature (weather) | De glance heet "Weather" en "displays the current temperature" | **zo laten** | Temperatur (Wetter) | Temperatuur (weer) |

**Waarom de meeste blijven:** ze zijn letterlijk de namen van Garmin, dus de drager herkent ze van zijn eigen horloge. Korter maken is niet nodig: de langste is 26 tekens (DE "Intensitätsminuten (Woche)"; Engels hooguit 24) en Garmin Connect zet elke keuze op een eigen regel.

**Eén wijziging, Battery wordt Watch battery.** Op deze plaat staat Body Battery groot in beeld, en Garmin noemt dat getal zelf "Body Battery level" (GEZIEN in de handleiding). Een veld dat alleen "Battery" heet kan dan gelezen worden als Body Battery. "Watch battery" zegt dat het de accu van het horloge is.

**Waarom "(week)" en "(weather)" blijven:** het zijn eerlijke woorden. Intensiteitsminuten tellen bij Garmin per week, maar stappen en calorieën per dag; zonder "(week)" denkt iemand misschien aan vandaag. "(weather)" zegt dat de temperatuur van het weer via de telefoon komt en niet van de voeler in het horloge (die meet de pols).

**Duits en Nederlands:** Garmin Connect toont de instellingen in de taal van de telefoon als de app die taal heeft (GOK, zo werkt het bij andere Connect IQ-apps die ik ken; NIET GEZIEN bij ons). De winkeltekst komt in drie talen, dus de instellingen ook. Gijs kan `resources-deu/strings/strings.xml` en `resources-dut/strings/strings.xml` maken met de kolommen DE en NL. Waar ik afweek van Garmin:
- DE "Stockwerke" in plaats van Garmins "Stockwerke hochgestiegen" (24 tekens, met afbreekstreepje in de handleiding). Een veld toont toch alleen omhoog.
- NL "Intensieve minuten (week)" in plaats van Garmins "Minuten intensieve training" (26 tekens plus "(week)"). Garmin gebruikt in de NL-handleiding ook "minuten intensieve training" in de lopende tekst; "intensieve minuten" is de gewone spreektaal (GOK).
- NL "Geklommen etages" is letterlijk Garmin (glance-lijst NL).

## 2. Naam van de plaat: Skiff

**Besluit (Chris, naam is mijn stuk volgens `platformen/garmin/reeks.md` stap 3):**

| | Engels | Duits | Nederlands |
|---|---|---|---|
| Betaald | `Skiff: Body Battery Sea` | `Skiff: Body Battery Meer` | `Skiff: Body Battery Zee` |
| Gratis | `Skiff Free: Body Battery Sea` | `Skiff Free: Body Battery Meer` | `Skiff Free: Body Battery Zee` |
| Op het horloge (lijst met wijzerplaten) | `Skiff` en `Skiff Free` | zelfde | zelfde |

Geen "als" ertussen (eerst zo bedacht, controleur: stijf, en elk extra woord in de naam kost plek). "Body Battery" niet vertalen: Garmin gebruikt het woord ook in de Duitse en Nederlandse handleiding zo (GEZIEN).

### Waarom niet Tij
1. "Tij" zegt een Engelse of Duitse koper niets en is niet uit te spreken zonder Nederlands.
2. De zoekbalk is ruim: op "tij" staan *Tide Phase - Spring & Neap Fishing Watch Face* en *Tide Phase Lite* op plek 3 en 4 (GEZIEN, wisselt per meting). Wie onze naam typt komt dus tussen de getijdenplaten, precies wat Gijs wilde vermijden ("De naam Tide of Tij kan niet", `reeks.md`).
3. Tij is wel uniek (0 namen met het woord, GEZIEN). Dat geldt ook voor Skiff.

### Waarom Skiff
1. Een skiff is een klein bootje: het is letterlijk het bootje op de waterlijn, en de grap op de poster ("Drained: run aground") gaat over dat bootje.
2. Geen enkele wijzerplaat of app heeft het woord in de naam (0 van de eerste 30, ook alle soorten door elkaar, GEZIEN), en de treffers op "skiff" zijn willekeurig (*Stirra Stalltafel*, analoge platen), dus geen veld vol concurrenten.
3. Kort, één lettergreep, uit te spreken in alle drie de talen.
4. Andere woorden die ik mat (aantal wijzerplaten met het woord in de naam, eerste 30): drift 30, swell 14, harbor 11, fathom 4 (waarvan twee keer letterlijk "Fathom"), buoy 1, shoal 1, brine 1; leeg: skiff, keel, lull, mooring, berth, dinghy, low tide. **Reserve: Keel** (0, kort), voor als Skiff toch ergens botst.
5. Een merk "Skiff" bestond (een mailbedrijf, gestopt in 2024; DERDEN, uit mijn geheugen, niet nagekeken); geen horloge of app in de Connect IQ-winkel (GEZIEN). Met de toevoeging "Body Battery Sea" is er geen verwarring.

### Waarom "Body Battery Sea" erachter
1. De winkel zet eerst de namen met het zoekwoord, daarna ongeveer de kortste (gemeten bij Ebb, `commercie/ebb/naam-1.0.1.md`). Op "body battery" (832 wijzerplaten) staan bovenaan namen van 2 tot 5 woorden met beide woorden: plek 1 is *Rest: Body Battery & Stress* (4 woorden, zelfde vorm als de onze), plek 4 *Body Battery* zelf (GEZIEN). Kort voor lang is hier maar een neiging: *VERDICT* (4 woorden) en *Clean Rings* (5) staan boven *Body Battery* (2) (controleur, GEZIEN). Verwachting voor `Skiff: Body Battery Sea` daarom ruim: ergens in de eerste ±30 op "body battery" (GOK, zwak onderbouwd).
2. Op "body battery sea" heeft geen enkele naam alle drie de woorden, maar de eerste 10 zijn precies dezelfde als op "body battery" (GEZIEN): "sea" verandert de volgorde blijkbaar niet. Of wij daar hoger staan is dus onzeker (GOK, pas te zien na de upload).
3. "Sea" zegt in één woord wat je ziet. Geen "sea level": dat moest uit de poster (keuring 17 nov 03:23) en het is de zin van Tide Line.
4. Body Battery is een merknaam van Garmin (™ in de handleiding). Op de pagina met richtlijnen voor Connect IQ (https://developer.garmin.com/brand-guidelines/connect-iq/) las ik met curl alleen dat er geen Garmin-merk in het pictogram mag; over het woord in de naam vond ik niets. Een deel van die pagina laadt misschien pas met een script, dus "er staat niets" is niet zeker (GOK). 20 van de eerste 20 treffers op "body battery" dragen het in de naam, ook betaalde (GEZIEN). Risico klein (GOK). In de lange tekst één keer "Body Battery™".
5. **Gratis met "Free" in de naam:** zo vindt iemand die de betaalde ziet de gratis meteen, en andersom. Voorbeeld uit dezelfde zoekopdracht: *Daybook Free - Body Battery & Weather Face* 1.000+ downloads, de betaalde *Daybook* 1+ (GEZIEN). Het kost één woord en dus misschien een plek of twee op "body battery" voor de gratis (GOK). Dat vind ik het waard.

### De reeks
Geen aparte reeksnaam in de titel: dat kost een woord en daarmee plekken in de zoekbalk, en niemand zoekt erop. De reeks herken je aan de makernaam **Dortus** (staat al zo in de winkel, `developerDisplayName`, GEZIEN), aan dezelfde stijl van pictogram en poster, en aan één regel onderaan elke beschrijving: `Part of the Dortus watch face series.` Plaat 2 en verder krijgen elk een eigen kort woord plus zoekwoord, zoals hier.

### Wat dit vraagt van anderen
- **Gijs:** naam in `manifest.xml` en `manifest-gratis.xml` (als string `AppName`): `Skiff` en `Skiff Free`. Werktekst "Battery" wordt "Watch battery". Strings in het Duits en Nederlands als het kan.
- **Daan:** op `tij-poster-v3.png` staat `Tij` groot in cyaan. Wordt `Skiff`. De rest van de poster blijft (`node shot.js`, één woord). Zeg je nee op de naam vanwege het beeld, dan hoor ik het graag met de reden.
- Mappen en tak mogen de werknaam Tij houden; alleen wat de koper ziet heet Skiff.

## 3. Eerlijke punten voor de winkeltekst (komen in de tekst, nog niet geschreven)

Van Gijs (17 nov ±07:25 UTC) en uit `ontwerp-kern.md` (GEZIEN op tak `claude/garmin-reeks-kern`, d81d18b):
1. **Trappen zonder hoogtemeter:** een horloge zonder barometer toont bij "Floors climbed" een streepje. De keuzelijst is op elk horloge gelijk. Zin: `Floors climbed needs a watch with a barometer; on other watches the field shows a dash.`
2. **Temperatuur komt van het weer via de telefoon:** zonder telefoon of weer een streepje. Zin: `Temperature comes from the weather on your phone, not from the watch sensor.`
3. **De gratis versie blijft gratis:** thema Tide, velden hartslag, stress en stappen, geen proeftijd, geen code. Zin voor de gratis: `Free: the Tide theme with heart rate, stress and steps. No trial, no code, no time limit.` (geen "forever": dat is een belofte voor altijd) En de zin met link naar de betaalde (advies Joris, verhaal 22) in de eerste regels: `Skiff (paid) adds three more themes and lets you pick each of the three fields from nine: <link>`.
4. **Geen Body Battery op het horloge:** een vlakke zee halverwege, geen bootje, een streepje als getal (ontwerp-kern, de zee). In de tekst bij de lijst met horloges: `Needs a watch with Body Battery for the sea and the boat.` (pas na nakijken welke horloges uit het manifest geen Body Battery hebben).
5. **Pictogrammen voor de zes nieuwe velden** komen van Mila (17 nov 07:55 klaar); de winkeltekst wacht tot ze in de betaalde versie zitten en Daan ja zei.
6. Eenheden (km of mijl, °C of °F) volgen de instelling van het horloge: mag erin als één woord, geen belofte meer.

## Open
- Winkeltekst in drie talen zodra 1 tot 5 vaststaan en Daan ja zei op de betaalde versie met pictogrammen.
- Prijs: voorstel in `prijs.md` (nog niet gemaakt); vergelijkbaar volgens `reeks.md`: Astra Vital Pro $4,99, Clean Rings $1,99, Body Battery $2,49 (GEZIEN 17 nov in de zoekopdracht hierboven).
- Op de dag van indienen de zoekbalk opnieuw meten op "skiff" en "body battery" (`meet-naam.py skiff`, `zoek-woord.py "body battery"`).

## Controleur (agent, run 77)
Alles opnieuw gemeten. Moets verwerkt: tekens geteld (24 en 26), plek op "tij" (3 en 4), geen "als" in de Duitse en Nederlandse naam. Kans-punten verwerkt: verwachting op "body battery" ruimer en zwakker gelabeld, "body battery sea" niet meer "bovenaan", NL Horlogebatterij, geen "Free forever", richtlijnen van Garmin als GOK.
