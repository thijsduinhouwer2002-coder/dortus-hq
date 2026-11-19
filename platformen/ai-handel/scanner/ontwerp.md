# Ontwerp koersverschil-scanner (19 nov 2026)

**Wat en voor wie:** een meting voor Thijs: bestaan er tussen crypto-beurzen prijsverschillen boven alle kosten
die lang genoeg blijven staan en waar opnemen en storten open is? **Af** = de workflow draait 4 keer per dag
±5,5 uur, de data staat op de tak `ai-handel-data`, `rapport.py` maakt er per dag en totaal echte kansen,
mediane winst, beste munten en beurzen en een som voor €2.000 en €5.000 van, en de tests zijn groen.

## Drie aanpakken
1. **Alle orderboeken elke ronde ophalen.** Precies, maar duizenden verzoeken per 20 seconden: de beurzen zetten
   ons dan vast. Valt af.
2. **Websockets per beurs.** Snelst en meest precies, maar 15 verschillende protocollen en lang bouwen. Te groot
   voor een uur en voor een vraag die ook met 20 seconden resolutie te beantwoorden is.
3. **Gekozen: middenweg.** Eén verzoek per beurs per ronde voor bod en laat van alle paren (bulk-ticker), en
   alleen voor kandidaten het orderboek. Een rooster (open kansen, dan nooit gecontroleerd, dan langst geleden)
   zorgt dat alle kandidaten om de beurt aan bod komen met hooguit 120 boekcontroles per ronde.

## Na de keuring (19 nov, KEURING.md)
- Rooster: open kansen waar opnemen, storten of netwerk dicht of onbekend is, krijgen hooguit eens per ±3 rondes
  een controle en komen na de nooit bekeken kandidaten. Eerst kregen ze elke ronde voorrang en bleven ±650 van de
  ±980 kandidaten liggen; nu werkt het rooster ze in een paar minuten weg (lokaal gemeten).
- Rapport: vergund (MiCA) en grijs apart in trechter, per dag, beste beursparen, overmaaktijd en sommen; de dekking
  van het rooster staat erin en het rapport noemt de aantallen een ondergrens zolang meer dan 5% nooit bekeken is.
- Netwerk vergeleken waar beide beurzen netwerken geven; onbekende opnamekosten tellen niet meer als 0; grens van
  15% ook op het boek; UST en IOT alleen bij Bitfinex omgezet; rapport.md wordt niet leeg bij een fout; bij
  afbreken geeft de workflow het signaal door, zodat open kansen en samenvatting.json bewaard blijven.

## Keuzes
- Geen omrekenen tussen quotes (opdracht). Euro alleen voor het optellen in het rapport.
- Echte kans vereist opnamestatus **bekend en open**. Onbekend telt niet (voorzichtig), maar staat apart in het
  rapport, zodat zichtbaar is hoeveel we daardoor misschien missen.
- Overlappende kansen van dezelfde munt zijn één gebeurtenis (je kunt de goedkope voorraad maar één keer kopen).
- Opslaan op de tak met een verse clone per poging en een gewone push: geen rebase, geen force, geen botsing met
  de schaduwbot (andere map).
- Proefruns (met de hand) hebben een eigen concurrency-rij en raken de klok niet, zodat een proef de vaste meting
  niet stopt of 6 uur uitstelt.

## Voorraad-simulatie (19 nov 2026, `simulatie.py`)
**Wat en voor wie:** voor Thijs: wat houd je echt over als je geld en munten op twee beurzen hebt staan en af en toe
moet terugschuiven? **Af** = het rapport toont per beurspaar (alle MiCA-paren) per dag bruto, kosten terugschuiven,
koerseffect, netto, rendement en gemiste kansen, elk cijfer GEZIEN of GOK, en de tests met kunstmatige kansen zijn groen.

Drie aanpakken:
1. **Vaste aftrek per kans** (bijv. 1/5 opname per kans). Klein, maar zegt niets over gemiste kansen en tijd onderweg.
2. **Opnieuw meten met echte voorraad in de scanner.** Precies, maar raakt de lopende meting en kost dagen.
3. **Gekozen: naspelen op de opgeslagen kansen.** Per paar een voorraad, elke kans op zijn begintijd uitgevoerd met
   de gemeten winst bij €100/€500/€1.000/€2.500/volle ruimte (lineair ertussen), terugschuiven met kosten en
   reistijd, koerseffect uit openbare candles. Raakt de meting niet en werkt ook op oude data.

Keuzes: beide richtingen van een paar delen één voorraad; opnamekosten van de munt uit de data (die de scanner per kans
al opsloeg); netto is precies eindwaarde min inleg (een test dwingt dat af); koersen alleen in het echte rapport
(`rapport.py` vanaf de opdrachtregel), niet in de tests; geen koers = "onbekend", nooit 0.

Na de keuring (KEURING.md, "Keuring simulatie") en de vraag naar weinig geld: inleg €100, €150 en €200 erbij met
minimale order en opname uit de API; netto handel (bruto min kosten) apart van het koerseffect, rendement "onbekend"
als de koers onbekend is; koersen van elke beurs met candles; uitvoeren 2 minuten na het begin; een heropende kans
krijgt niet opnieuw het volle boek; koers van de laatste gesloten candle; schuiven alleen bij kosten tot 1% (bij 5%
at het terugschuiven met €150 alle winst op); een tabel met andere drempels en minder munten. Koersen en minima staan
in `simbronnen.py`, zodat `simulatie.py` onder de ±400 regels blijft.

Na de herkeuring (KEURING.md, "Herkeuring simulatie"): de tabel "Andere keuzes" toont ook de kostengrens 2% en 5%,
en bij de aanname staat dat 1% achteraf gekozen is. De kop "per dag" zegt dat het om één gemeten dag gaat die begint
met een gelijk verdeelde voorraad (en of de voorraad aan het eind scheef staat). Het rapportblok staat nu in
`simrapport.py`. Rapport van 15:44 UTC (9 runs, Bitvavo-Kraken, netto handel): €150: 1% €0,20, 2% €0,20, 5%
-€1,94 (gelijk aan de keurder); €2.000: 1% €7,91, 2% €1,73, 5% €1,73 (keurder: €7,79, €1,67, €1,67; zelfde beeld,
klein verschil). Op de oudere data van 15:08 UTC (5 runs) maakte de grens bij €2.000 niets uit (€2,39 bij alle drie):
daar kostte de duurste terugschuif (GMT) 0,98%, net onder de grens. De uitkomst hangt dus aan een paar schuiven rond
de grens.

Na de tweede herkeuring (KEURING.md, "Tweede herkeuring simulatie"): Kraken-taker 0,80% (GEZIEN, kraken.com/pro/fees;
0,20% op stablecoin- en FX-paren, `beurzen.taker_standaard`). De opgeslagen kansen met Kraken (gemeten met 0,40%)
rekent `rapport.herreken` opnieuw door: 0,40% van de inzet extra op elk gemeten punt, ruimte tot het punt met de meeste
winst (GOK, het boek is niet bewaard). Op de data van 15:38 UTC (9 runs): Bitvavo-Kraken 25 echte kansen (was 46);
netto handel €150: €0,11 bij 1% en 2%, -€5,38 bij 5%; €2.000: €2,09 bij alle drie, gelijk aan de schatting van de
keurder (T6). Rapport van 15:53 UTC (12 runs, 399 Kraken-kansen herrekend, 233 houden winst): Bitvavo-Kraken 33 kansen;
€150: €0,14, €0,14, -€2,31; €2.000: €5,16, -€0,10, -€0,10 (1%, 2%, 5%).
`beurzen.py` is niet gesplitst: de driehoek-meter zet `B.QUOTES` om, en de beursklassen lezen QUOTES uit hun eigen
module; na een splitsing zou die aanpassing stil niet meer werken. `scanner.py` is wel kleiner: de rekensom staat in
`rekensom.py` (scanner.py zet de namen door voor de radar).
Bitvavo 0,25% is nu ook GEZIEN (help-center-API van support.bitvavo.com).

## Bekende grenzen
Netwerk alleen vergeleken waar beide beurzen het geven; overmaaktijd niet gemeten; opnamekosten bij een deel van de beurzen geschat;
de API is de wereldwijde versie, niet altijd de EU-versie met vergunning. Alles staat in README.md.
