# Garmin ademhalingsapp: naam en stijlrichting (Mila, 9 nov)

Vraag van Gijs (9 nov 22:45): naam en een stijlrichting voor een rond horlogescherm van 260 tot 454 px, een vorm die zelf ademt, en een mooie lijn van je inhoudtijd per ronde en per week. Bouwen pas na het ja van Hans.

## Naam: Ebb (besluit Mila 10 nov ±01:00 NL, na naamcheck Gijs)
**Ebb.** Tide valt af (±30 getijden-apps, een heet letterlijk "Tide"), Deep Tide ook. Waarom Ebb: (1) vrij in de winkel (alleen Ebbcast en Ebbmoon, andere woorden); (2) eb is het water dat zich terugtrekt, precies wat je doet bij uitademen voor je duikt, dus het past bij de patrijspoort en het duikprofiel; (3) drie letters, leest groot op een rond scherm van 260 px en als icoon. Alles hieronder blijft; waar "Tide" staat, lees "Ebb". Wat het zou veranderen: een merkbezwaar of Hans kiest anders.

## De haak: elke keer inhouden is een duik
Iedere concurrent toont een timer (kale tekst) of een cirkel die groter en kleiner wordt. Wij maken van het ronde scherm een **patrijspoort onder water**:
- **Inademen:** het water stijgt in het ronde scherm (een golvende waterlijn die van onder naar boven loopt). **Uitademen:** het water zakt. Dat is de vorm die zelf ademt, en het is het hele scherm, niet een cirkeltje in het midden.
- **Inhouden = duiken.** Na de laatste uitademing zakt de waterlijn niet meer: je gaat onder. Het blauw wordt per 15 seconden een tint dieper (turkoois, blauw, nachtblauw), langzaam stijgen een paar luchtbelletjes. In het midden één groot getal: je inhoudtijd, en klein eronder de "diepte" (1 seconde is 1 meter, alleen voor het gevoel, zo genoemd in de app).
- **De grap: wie je tegenkomt.** Bij 1:00 zwemt er een visje door het scherm, bij 1:30 een kwal, bij 2:00 een schildpad, bij 3:00 een walvis in de verte. Een keer gezien, dan staan ze in je logboek. Iets om over te vertellen ("vanochtend zag ik de schildpad"), en een reden om morgen weer te ademen. Geen beweringen over echte dieren of gezondheid.
- **Herstelademhaling** (15 s inhouden na een ronde): de waterlijn schiet omhoog met een plons van belletjes, je komt boven.

## De lijn van je inhoudtijd: een duikprofiel
- **Per sessie:** een duikprofiel zoals op een duikcomputer: per ronde een V die zo diep gaat als je inhoudtijd. Drie of vier V's naast elkaar, de diepste ronde met een klein lichtpuntje en het getal erbij. Mooier dan een staafje en het past bij de rest.
- **Per week (8 weken):** een getijdentabel: een golvende lijn door je beste inhoudtijd per dag, met daaronder het gemiddelde als lichte schaduw. Groeit je inhoudtijd, dan zie je het tij letterlijk stijgen.

## Werkt het klein
- Het scherm is een paar centimeter. Daarom: **één groot getal, één bewegend vlak (het water), verder niets.** Geen menu's tijdens het ademen, geen kleine tekst. De fase ("in", "uit", "vast") als één woord bovenaan, of alleen trillen.
- MIP-schermen (Forerunner, fenix, Instinct) hebben maar 64 kleuren en geen verloop. Daarom het water in **drie of vier vaste tinten uit het MIP-palet** (bijvoorbeeld 0x00FFFF, 0x00AAFF, 0x0055AA, 0x000055) met een golvende rand, geen verloop. Op AMOLED (Venu, Epix) mag het zachter en met meer belletjes. Zwart blijft de basis (zuinig op AMOLED).
- Golf: een sinuslijn van 2 of 3 golven over de breedte, die per frame een stukje opschuift; bij 1 frame per seconde in de rust blijft hij toch leven.

## Naam
- **Mijn keuze: "Tide"** (Engels voor tij, de werktitel). Kort, rustig, en het verhaal (water stijgt en zakt, je tij stijgt) zit in het woord. Als ondertitel in de winkel: "Tide: breath hold & breathwork".
- Terugval als "Tide" in de Connect IQ-winkel al bestaat of slecht vindbaar is: **"Ebb"**, of **"Deep Tide"**. Gijs: controleer de drie in de winkel-API voor je kiest. Niet: iets met Wim Hof (merk), en geen naam die een medisch effect belooft.

## Kleur en logo
- Turkoois en nachtblauw op zwart, met één warme kleur (koraal, 0xFF5555 uit het MIP-palet) alleen voor je record en de dieren. Daardoor herken je het schermpje naast de grijze en gele concurrenten.
- Icoon: een cirkel half gevuld met golvend turkoois water en één belletje erboven. Werkt op 40 px.

## Wat ik nog maak (zodra Hans ja zegt)
Een klikbare schets van de vier schermen (ademen, duiken, boven komen, duikprofiel) op 260 en 454 px, en de winkelplaatjes. Gijs bouwt, ik keur op het echte scherm in de simulator.

## Schets van de schermen (Mila 10 nov run 10, na het ja van Hans)
Bestanden: `ontwerp/garmin/schets/ebb-schets-260.png` en `-454.png` (alle vijf naast elkaar), losse schermen `ebb-<n>-<naam>-<D>.png`. Bron met alle maten als deel van de diameter D: `ontwerp/garmin/bron/ebb_schets.py`. Alleen MIP-kleuren, geen verloop, geen zachte randen, dus 1 op 1 na te bouwen met `fillPolygon`, `drawLine`, `drawCircle` en `drawText`.
1. **Ademen:** water tot 58% (peil volgt de adem: onderin 20% bij uit, 80% bij in), golf van 2,5 golven, amplitude 2,5% D, schuimrand 0x55FFFF van D/110 dik. Fasewoord klein bovenaan op 13% (0x55AAAA), groot getal = ademhaling (30% D hoog), daaronder "of 30 · round 2".
2. **Duiken:** water tot 93%, kleur per 15 s dieper: 0x00AAAA, 0x0055AA, 0x0000AA, 0x000055. Groot getal = inhoudtijd, "94 m" eronder. Drie of vier belletjes (alleen omtrek, 0x55AAFF) die stijgen. Dier in koraal 0xFF5555 (hier de kwal van 1:30), zwemt in ±6 s van rechts naar links.
3. **Boven (herstel):** water schiet in 0,5 s naar 80% met vijf belletjes boven de lijn, aftellen van 15.
4. **Duikprofiel:** oppervlakte op 32%, per ronde een V tot evenredige diepte (diepste tot 70%), vlakken in oplopende tint, schuimlijn erover. Diepste: stip 2,2% D met de tijd links ervan; koraal en "new best" alleen bij een record over alle tijd, anders lichtgeel 0xFFFFAA en "3 rounds".
5. **Week:** getijdenlijn door de beste tijd per dag over 56 dagen, gaten waar geen sessie was, daaronder het gemiddelde van 7 dagen als vlak 0x0000AA.
Besluit: tekst blijft binnen 75% van de breedte (geen tekst langs de rand van de cirkel), want op 260 px valt anders de rand weg (GEZIEN). Waarom de kwal koraal: één warme kleur in al dat blauw is het enige wat je met een halve blik op je pols ziet.
