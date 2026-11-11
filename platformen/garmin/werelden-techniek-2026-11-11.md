# Ebb: techniek voor een wereld per dier (voorstel Gijs, 11 nov 2026 22:40 UTC)

Besluit Thijs 11 nov 23:13 NL: elk dier krijgt een eigen stukje zee. Dit is het plan voor het mechanisme, geschreven vóór het blad van Mila, zodat haar werelden meteen in een vorm komen die het horloge aankan. Eerste bouw van het mechanisme staat sinds 23:00 UTC op de tak (`Wereld.mc`, edc0ad7), met drie proefwerelden van Gijs in testscènes; nog niet in beeld gezien. Wat hier GOK is wordt bewezen met de eerste drie werelden (schildpad, krab, clownvis) op FR255 en fenix 7.

## Wat het horloge aankan (GEZIEN in eerdere runs)
- Een scherm dat te veel tekent in één beurt wordt afgebroken (watchdog). Daarom bouwen we een dier nu één keer op in een eigen plaatje, één laag per beurt, en plakken daarna alleen (`EbbDierPlaatje`, plaatjesrun 42963243152).
- Een plaatje van ±377 x 262 px lukt op fenix 8 (sea complete, run 42996562232). Groter is niet geprobeerd.
- Geheugen: FR255 gebruikte 79 van 508 kB met krab en sea log. Op MIP kost een plaatje zonder palet het meest; met palet gaf het witte blokken (run 42973269112), dus we rekenen zonder palet.
- Het maken van een plaatje kan mislukken als de voorraad van het horloge vol is (codelezing hoofdchat 22:10). De app moet dan gewoon doorgaan zonder wereld.

## Mechanisme
1. **Eén bestand `Wereld.mc`** met `EbbWereld`: bouwt de wereld van het gekozen dier één keer als plaatje, één laag per beurt, en plakt hem daarna. Zelfde opzet als `EbbDierPlaatje` en `EbbDierVoorraad`. Schermen roepen alleen `EbbWereld.teken(dc, dier, d)` aan. Regel erbij in `REGELS.md`: werelden alleen via `EbbWereld`.
2. **De wereld is een strook onderin**, de volle breedte en hoogstens 0,40 D hoog (op 454: 454 x 182, kleiner dan het plaatje van sea complete; op 260: 260 x 104). Boven de strook tekent `EbbZee` het water zoals nu. Zo blijft het achter timer, cijfers en tekst rustig (besluit punt 2) en blijft het plaatje klein.
3. **Er is er hoogstens één tegelijk** in het geheugen: de wereld van het dier dat meezwemt. Wisselt het dier, dan gaat de oude weg.
4. **Lukt het plaatje niet** (voorraad vol) of is het nog niet af: het scherm toont de zee zonder wereld. Nooit wachten, nooit crashen.
5. **Hertekenen blijft zoals nu** (inhouden eens per seconde): een wereld beweegt niet. Alleen het dier en de belletjes bewegen. Zo kost het geen extra batterij.
6. **Sea log:** zes kleine werelden per blad is zes plaatjes en dat is te zwaar (GOK, meten). Voorstel: in de sea log per vakje alleen de bodemkleur en één kenmerk van de wereld (bijvoorbeeld één koraaltak), getekend in het bladplaatje dat er al is.
7. **Ademschermen vol water:** dat is `EbbZee.ademZee` met een hogere stand, geen plaatje. De wereldstrook ligt eronder en schuift niet mee.

## Vorm waarin Mila de werelden levert
Zelfde vorm als de dieren (`ontwerp/garmin/bron/ebb_dieren_v83.py`, omgezet door `bron/maak_dieren_json.py`):
- Gevulde vlakken (veelhoeken) en cirkels, geen verlopen, geen doorzichtigheid.
- Punten in 1/100 van de strook: x van 0 tot 100 over de volle breedte, y van 0 (bovenkant strook) tot 40.
- Hoogstens 8 lagen per wereld en hoogstens 40 punten per vlak; één laag is één kleur. Meer lagen betekent langer opbouwen (één laag per beurt).
- Alleen de 64 MIP-kleuren (elke kleurwaarde 00, 55, AA of FF), want FR255 en fenix 7 kunnen niets anders. Op AMOLED mogen we later een verloop in het water erboven leggen.
- De ronde rand snijdt de hoeken af: belangrijke dingen binnen x 15 tot 85, en het midden (x 35 tot 65) laag houden, daar zwemt het dier en staat soms tekst.
- Onder tekst die in het water staat ("1 more session", namen, weekstippen) moet het rustig blijven: contrast meten we na in de beelden.

## Bewijs dat ik lever vóór de overige werelden
- FR255 en fenix 7: geen watchdog in de plaatjesrun op inhouden, eindscherm, menu en sea log met de drie werelden.
- Geheugen: regel "GEHEUGEN" in het log met wereld plus dier, naast de 79 kB van nu.
- Aantal tekenbeurten per minuut gelijk aan nu (log), dus geen extra batterij.
- Contrast van timer en tekst gemeten in de beelden.
- Nieuwe scènes in de plaatjesrun voor elk van de drie werelden.

## Wat ik niet weet
- Hoe groot de plaatjesvoorraad op FR165 en Venu 3S is (NIET GEZIEN; in de simulator ging sea complete goed).
- Of de strook op 454 x 182 zonder palet op elk AMOLED-horloge past naast het dierplaatje (GOK ja, omdat sea complete groter is).
