# Garmin ademhalingsapp: naam en stijlrichting (Mila, 9 nov)

Vraag van Gijs (9 nov 22:45): naam en een stijlrichting voor een rond horlogescherm van 260 tot 454 px, een vorm die zelf ademt, en een mooie lijn van je inhoudtijd per ronde en per week. Bouwen pas na het ja van Hans.

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
