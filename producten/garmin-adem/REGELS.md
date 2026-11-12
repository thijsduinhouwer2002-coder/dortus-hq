# Regels voor de code van Ebb

Besluit Thijs, 11 nov 2026 07:41 NL. Elke run die aan Ebb werkt leest dit eerst. Waarom: reparaties bleven op één plek hangen (de watchdog-fix kwam terug op drie andere schermen), omdat hetzelfde werk op meer plekken stond.

1. **Eén taak per bestand.** Een scherm, een stuk logica of een tekenhulp heeft een eigen bestand in `source/`. Zie de kaart hieronder.
2. **Hoogstens 300 regels per codebestand.** Toetsen (`*Test.mc`) tellen niet. Wordt een bestand groter, splits het eerst. De workflow `garmin-adem-e2e.yml` controleert dit (stap "Regels: bestanden hoogstens 300 regels").
3. **Eerst zoeken of iets al bestaat** (grep in `source/`) voordat je een nieuwe functie schrijft.
4. **Dieren alleen via de gedeelde functies.** `EbbDierPlaatje.laag` is de enige plek die een dier tekent (rand, lijf, ogen, silhouet). Een scherm tekent een dier met `EbbDierVoorraad.teken` of `EbbDierMaat.inBand` (één laag per beurt, tegen de watchdog). Alleen de sea log bouwt zijn blad zelf op, maar ook met `EbbDierPlaatje.laag`.
5. **Zee alleen via `EbbZee`** (`Zee.mc`): `zee` (inhouden in standen), `ademZee` (ademen en rustig), `zeeBanden` (elke andere zee), `strook` (dunne zee onder today, 8 weeks, settings), `stil` (platte zee van het pauzemenu). Geen eigen golven of banden in een scherm.
7. **Werelden alleen via `EbbWereld`** (`Wereld.mc`). De werelden zijn gegevens, geen code: `bron/maak_werelden.py` maakt uit Mila's json per wereld één `jsonData` in `resources/werelden/werelden.xml` (en de lijst in `WereldData.mc`), nooit met de hand, en alleen de wereld van het gekozen dier wordt geladen. `EbbWereld.bouw(dier, d)` bouwt tijdens het ademen, `EbbWereld.teken(dc, dier, d, f)` bouwt verder, plakt de strook (bovenkant per wereld) en tekent de planten, `EbbWereld.voor` tekent na het dier wat eroverheen hoort, `EbbWereld.thuis` zegt waar het dier woont, `EbbWereld.los` ruimt op aan het einde van de sessie. In het plaatje staat alleen wat stil staat (lagen ver en midden, details per gehaald weekdoel). Planten in twee standen en de voorlaag worden direct getekend met `EbbWereld.buig`: dezelfde punten in beide standen, de tussenstand volgt de adem (f in duizendsten, 0 bij uitademen en inhouden, 1000 bij ingeademd), nooit een tweede of derde plaatje. Grenzen: hoogstens 200 punten per beurt in het plaatje, hoogstens één wereldplaatje tegelijk, en wat direct getekend wordt blijft onder 40 punten per beurt (het omzetscript weigert meer). Valt het plaatje uit de voorraad, dan bouwt hij opnieuw, hoogstens 3 keer; daarna blijft de zee zonder wereld staan. De wereld krijgt nooit de inhoudtijd mee: hij ziet er op 0:30 en 2:30 gelijk uit. Maan en dagdeel reken je alleen via `EbbLucht` (`Lucht.mc`). Geen scherm tekent zelf een bodem, planten of rotsen.
6. **Opruimen verandert niets aan wat de app doet.** Bewijs met de testbeelden: vóór en na pixel voor pixel gelijk (`bron/vergelijk_plaatjes.py`).

## Kaart van `source/`

| Bestand | Taak |
|---|---|
| `EbbApp.mc` | app, eerste scherm |
| `Scenes.mc` | alleen de plaatjesbouw: één stilgezette scène per start |
| `Bouw.mc` | vlaggen voor test- en plaatjesbouw |
| `Veilig.mc` | drie veiligheidsbladen |
| `Start.mc` | startmenu |
| `StartCheck.mc` | "how it works" en "Sit or lie down" voor Rounds en Calm |
| `EbbView.mc` | de sessie met rondes: klok, opslaan, pauze, trillen |
| `SessieScherm.mc` | tekenen van ademen, inhouden en herstel |
| `EindScherm.mc` | eindscherm na de rondes (6b, 6c, alles gevonden; de eerste keer sea complete) |
| `SeaComplete.mc` | feestscherm sea complete: groepsfoto van alle 24, dier voor dier geplakt |
| `Pauze.mc` | pauzemenu in Ebb-stijl voor Rounds en Calm (Resume, Save, Discard; knoppen en tik) |
| `Overzicht.mc` | today en 8 weeks |
| `OverzichtView.mc` | today en 8 weeks als eigen scherm vanuit het menu; `EbbNaarMenu.ga` (na een sessie terug naar het menu dat er al ligt, niet stapelen) |
| `EbbDelegate.mc` | knoppen tijdens de sessie; opent het pauzemenu |
| `RustigView.mc` | Calm (rustig ademen), opent het pauzemenu, en het Calm-eindscherm |
| `InstellingenView.mc`, `Instellingen.mc` | settings: scherm en opgeslagen waarden |
| `SeaLog.mc` | sea log |
| `DierPlaatje.mc` | de dier-tekenfunctie, het dierplaatje en de voorraad |
| `DierMaat.mc` | maat en plaats van een dier in een vak |
| `DierenData.mc` | de punten en kleuren van Mila's dieren (gemaakt door `bron/maak_dieren_json.py`) |
| `Zee.mc` | de zee |
| `Wereld.mc` | de wereld per dier (gegevens in `resources/werelden/werelden.xml`, lijst in `WereldData.mc`, beide gemaakt uit Mila's json; maan en dagdeel in `Lucht.mc`): het wereldplaatje en `EbbWereld.teken` |
| `Teken.mc` | kleuren, letters, pil, hart, weekstippen en kleine tekenhulpen: `px` (maat in 1/260 D), `tekst260` (tekst met bovenkant op y/260), `tekstInRonde` (tekst die in de cirkel past) |
| `Sessie.mc` | rekenwerk van rondes en rustig ademen (geen tekenen) |
| `Trouw.mc`, `TrouwDieren.mc` | tellers en reeks in weken; welke dieren je hebt |
| `Profiel.mc` | 8 weeks rekenwerk, zeestand, veiligheid elke 30 dagen |
| `Vandaag.mc`, `Opslag.mc` | today en de 56 dagen op het horloge |
| `Opname.mc` | de activiteit en de FIT-velden |
| `Trillen.mc` | trilpatronen |
