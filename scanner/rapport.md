# Rapport koersverschil-scanner

Gemaakt 2026-11-19 15:27 UTC uit 7 runs, samen ±6.3 uur gemeten (GEZIEN).
Echte kans = winst na alle kosten (opnamekosten bekend), opnemen en storten open (en een netwerk dat aan beide kanten open is, als de beurzen dat geven), minstens €100,00 op het boek, minstens 2 minuten blijven staan, geen andere munt met dezelfde naam.
**Vergund** = beide beurzen hebben een MiCA-vergunning (ESMA-register), vaak via een EU-dochter die minder munten kan hebben dan de wereldwijde API die we meten (GOK). **Grijs** = minstens één beurs zonder vergunning (MEXC, Bitget, HTX, Poloniex, XT, Bitfinex, Binance). Zie README.md.

## Hoeveel wordt er gecontroleerd? (GEZIEN, stand.jsonl)

Per ronde (mediaan over 76 metingen): 1042 kandidaten (verschil op de ticker groter dan de takerkosten), 120 met het orderboek gecontroleerd, 2 nog nooit gecontroleerd (0%).
Bijna alle kandidaten komen aan de beurt; de aantallen hieronder missen weinig.

## Trechter (GEZIEN, eigen metingen)

| Stap | Alle beurzen | Alleen MiCA-beurzen | Met minstens één grijze beurs |
|---|---|---|---|
| Verschillen met winst op het boek na alle kosten | 5321 | 753 | 4568 |
| ...waarvan opnemen of storten dicht | 1041 | 88 | 953 |
| ...waarvan status onbekend (beurs geeft het niet openbaar) | 3036 | 443 | 2593 |
| Opnemen en storten open | 1244 | 222 | 1022 |
| ...en geen netwerk dat aan beide kanten open is: valt af | 18 | 0 | 18 |
| ...en opnamekosten onbekend: valt af | 0 | 0 | 0 |
| ...en minstens €100,00 op het boek | 427 | 169 | 258 |
| ...en minstens 2 minuten blijven staan | 122 | 56 | 66 |
| ...en geen andere munt met dezelfde naam | 112 | 52 | 60 |
|    ...waarvan contractadres bekend en gelijk | 7 | 1 | 6 |
|    ...waarvan contractadres onbekend (telt mee, kan een andere munt zijn) | 105 | 51 | 54 |
|    ...waarvan netwerk gekoppeld en open | 50 | 9 | 41 |
|    ...waarvan netwerk niet te koppelen (telt mee) | 62 | 43 | 19 |
| **Echte kansen** (zelfde munt overlappend in de tijd samengevoegd, beste beurspaar telt) | 79 | 52 | 36 |
| Ter vergelijking: zelfde eisen, maar opnamestatus onbekend (niet meegeteld) | 192 | 53 | 158 |

## Echte kansen per dag (GEZIEN)

| Dag | Echt, alleen MiCA | Echt, met grijs | Mediane winst per kans bij €500 (MiCA / grijs) | Mediane duur |
|---|---|---|---|---|
| 2026-11-19 | 43 | 36 | €1,77 / €0,95 | 4.3 min |
| Totaal | 43 | 36 | €1,77 / €0,95 | 4.3 min |

## Beste munten (GEZIEN)

| | Soort | Kansen | Som winst bij €500 per kans |
|---|---|---|---|
| MERL-EUR | vergund | 8 | €76,32 |
| LUNC-USDT | grijs | 4 | €22,00 |
| LUNA-EUR | vergund | 6 | €20,65 |
| DYM-EUR | vergund | 19 | €19,99 |
| YB-USDT | grijs | 1 | €16,34 |
| GMT-EUR | vergund | 6 | €14,87 |
| WAN-USDT | grijs | 3 | €12,65 |
| USTC-USDT | grijs | 3 | €11,83 |
| VERONA-USDT | grijs | 6 | €11,42 |
| CBK-USDT | grijs | 3 | €4,13 |

## Beste beursparen (kopen op > verkopen op) (GEZIEN)

| | Soort | Kansen | Som winst bij €500 per kans |
|---|---|---|---|
| bitvavo > kraken | vergund | 42 | €134,71 |
| bitget > gate | grijs | 5 | €18,41 |
| gate > xt | grijs | 1 | €16,34 |
| kucoin > htx | grijs | 5 | €13,65 |
| kucoin > bitget | grijs | 5 | €12,37 |
| kucoin > xt | grijs | 1 | €6,56 |
| htx > xt | grijs | 1 | €5,83 |
| bitget > htx | grijs | 5 | €3,98 |
| bitget > xt | grijs | 2 | €3,96 |
| xt > htx | grijs | 1 | €3,52 |

Beurzen die het vaakst meedoen (koop of verkoop): bitvavo 42, kraken 42, bitget (grijs) 22, kucoin 18, htx (grijs) 16, gate 9, xt (grijs) 7, poloniex (grijs) 2 (GEZIEN).

## Hoeveel kansen blijven staan terwijl je geld schuift? (GEZIEN, duur uit eigen metingen)

Wie geen voorraad op beide beurzen heeft, moet kopen, de munt opnemen, wachten tot hij binnen is en dan verkopen. Hoe lang dat duurt verschilt per munt en netwerk: een paar minuten (snelle ketens) tot een uur of meer (Bitcoin, beurzen die opnames met de hand keuren) (GOK, niet per munt gemeten).

| Overmaaktijd | Alle beurzen | Alleen MiCA-beurzen | Met minstens één grijze beurs |
|---|---|---|---|
| 5 min | 36 van 79 (46%) | 19 van 52 (37%) | 20 van 36 (56%) |
| 10 min | 19 van 79 (24%) | 13 van 52 (25%) | 8 van 36 (22%) |
| 30 min | 14 van 79 (18%) | 10 van 52 (19%) | 5 van 36 (14%) |
| 60 min | 5 van 79 (6%) | 4 van 52 (8%) | 2 van 36 (6%) |

## Wat zou het opleveren over 3 maanden? (GOK, doorgetrokken uit de metingen)

Gemeten over ±6.3 uur (GEZIEN), doorgetrokken naar 90 dagen (GOK: aanname dat de week die we maten gewoon is).

| Beurzen | Inleg | Model | Kansen per uur | Per kans (mediaan) | 3 maanden |
|---|---|---|---|---|---|
| Alleen MiCA | €2.000,00 | bovengrens: elke kans, geld overal tegelijk | 8.21 | €2,95 | €52.240,70 |
| Alleen MiCA | €2.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 6.63 | €2,99 | €76.130,11 |
| Alleen MiCA | €5.000,00 | bovengrens: elke kans, geld overal tegelijk | 8.21 | €4,00 | €70.867,56 |
| Alleen MiCA | €5.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 6.63 | €4,87 | €114.044,02 |
| Alle (met grijs) | €2.000,00 | bovengrens: elke kans, geld overal tegelijk | 12.47 | €2,10 | €56.443,44 |
| Alle (met grijs) | €2.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 6.63 | €2,99 | €76.130,11 |
| Alle (met grijs) | €5.000,00 | bovengrens: elke kans, geld overal tegelijk | 12.47 | €2,48 | €66.692,17 |
| Alle (met grijs) | €5.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 6.63 | €4,87 | €114.044,02 |

Bovengrens: elke kans met de helft van de inleg aan elke kant, alsof het geld op alle beurzen tegelijk staat (kan in het echt niet). Beste beurspaar: het paar is **achteraf** gekozen uit de metingen (vooraf kiezen levert minder op), en het model neemt aan dat je van elke munt al voorraad op de verkoopbeurs hebt.

Waarom dit te rooskleurig is (GOK): elke kans wordt maar één keer geteld met het mediane boek, maar andere bots pakken hem ook; de munt die je als voorraad aanhoudt kan dalen; na een paar kansen moet de voorraad terug (opnamekosten en tijd); minimale opname- en ordergroottes tellen niet mee; en een kans die we 2 minuten zagen staan, staat er niet per se nog als jouw order binnenkomt. Waarom het te somber kan zijn: niet alle kandidaten zijn gecontroleerd, en met voorraad op beide beurzen kun je dezelfde kans vaker pakken als het boek zich aanvult; dat telt hier niet mee.

## Wat houd je echt over? Voorraad op twee beurzen (simulatie)

Per beurspaar: geld en munten op beide beurzen, elke echte kans uitgevoerd tegen het boek zoals gemeten (niet meer dan de ruimte op het boek en niet meer dan de voorraad op die beurs), terugschuiven als een kant leeg dreigt te raken (met opnamekosten en tijd onderweg), en het koerseffect van de aangehouden munten apart. Netto = bruto min kosten terugschuiven plus koerseffect. **Gemeten** (GEZIEN): de kansen, het boek en de koersen; **de rest is een rekenmodel** (GOK, aannames onder de tabel). Geen advies.

### Alleen MiCA-beurzen (alle paren met echte kansen)

| Beurspaar | Inleg | Dag | Gemeten | Kansen | Gemist (geen voorraad) | Kleiner door voorraad | Bruto winst | Kosten terugschuiven | Koerseffect voorraad | Netto | Rendement op de inleg |
|---|---|---|---|---|---|---|---|---|---|---|---|
| bitvavo - kraken | €2.000,00 | 2026-11-19 | 6.3 u | 42 | 22 | 20 | €15,32 | €13,48 (24x) | €-2,00 | €-0,16 | -0.01% |
| bitvavo - kraken | €5.000,00 | 2026-11-19 | 6.3 u | 42 | 21 | 21 | €37,43 | €13,48 (24x) | €-5,00 | €18,95 | 0.38% |
| gate - kucoin | €2.000,00 | 2026-11-19 | 6.3 u | 10 | 2 | 8 | €6,57 | €2,80 (8x) | €-7,77 | €-4,00 | -0.20% |
| gate - kucoin | €5.000,00 | 2026-11-19 | 6.3 u | 10 | 1 | 5 | €12,88 | €2,19 (6x) | €-19,47 | €-8,78 | -0.18% |

- bitvavo - kraken, €2.000,00: munten AVA, DYM, GMT, LUNA, MERL, SSV; bruto zonder voorraadgrens zou €408,00 zijn, met voorraad €15,32 (GEZIEN boek, GOK model).
- bitvavo - kraken, €5.000,00: munten AVA, DYM, GMT, LUNA, MERL, SSV; bruto zonder voorraadgrens zou €408,00 zijn, met voorraad €37,43 (GEZIEN boek, GOK model).
- gate - kucoin, €2.000,00: munten ERG, IR, LUNC, USTC, VERONA; bruto zonder voorraadgrens zou €36,42 zijn, met voorraad €6,57 (GEZIEN boek, GOK model).
- gate - kucoin, €5.000,00: munten ERG, IR, LUNC, USTC, VERONA; bruto zonder voorraadgrens zou €36,42 zijn, met voorraad €12,88 (GEZIEN boek, GOK model).

### Met minstens één grijze beurs (de 5 paren met de meeste bruto winst)

| Beurspaar | Inleg | Dag | Gemeten | Kansen | Gemist (geen voorraad) | Kleiner door voorraad | Bruto winst | Kosten terugschuiven | Koerseffect voorraad | Netto | Rendement op de inleg |
|---|---|---|---|---|---|---|---|---|---|---|---|
| kucoin - xt | €2.000,00 | 2026-11-19 | 6.3 u | 4 | 1 | 3 | €16,00 | €3,76 (6x) | €10,90 | €23,14 | 1.16% |
| kucoin - xt | €5.000,00 | 2026-11-19 | 6.3 u | 4 | 1 | 3 | €38,75 | €3,76 (6x) | €27,22 | €62,21 | 1.24% |
| bitget - xt | €2.000,00 | 2026-11-19 | 6.3 u | 5 | 2 | 2 | €5,04 | €0,91 (2x) | onbekend | €9,57* | 0.48% |
| bitget - xt | €5.000,00 | 2026-11-19 | 6.3 u | 5 | 2 | 2 | €11,31 | €0,92 (3x) | onbekend | €24,00* | 0.48% |
| bitget - gate | €2.000,00 | 2026-11-19 | 6.3 u | 8 | 2 | 5 | €8,03 | €1,46 (7x) | €-12,95 | €-6,37 | -0.32% |
| bitget - gate | €5.000,00 | 2026-11-19 | 6.3 u | 8 | 2 | 4 | €10,03 | €1,24 (4x) | €-32,39 | €-23,61 | -0.47% |
| gate - xt | €2.000,00 | 2026-11-19 | 6.3 u | 1 | 0 | 1 | €17,18 | €0,91 (1x) | €445,50 | €461,77 | 23.09% |
| gate - xt | €5.000,00 | 2026-11-19 | 6.3 u | 1 | 0 | 1 | €33,84 | €0,91 (1x) | €1.113,75 | €1.146,68 | 22.93% |
| htx - xt | €2.000,00 | 2026-11-19 | 6.3 u | 9 | 2 | 6 | €7,47 | €3,83 (7x) | onbekend | €6,38* | 0.32% |
| htx - xt | €5.000,00 | 2026-11-19 | 6.3 u | 9 | 2 | 6 | €14,73 | €3,38 (6x) | onbekend | €18,18* | 0.36% |

- kucoin - xt, €2.000,00: munten LUNC; bruto zonder voorraadgrens zou €260,76 zijn, met voorraad €16,00 (GEZIEN boek, GOK model).
- kucoin - xt, €5.000,00: munten LUNC; bruto zonder voorraadgrens zou €260,76 zijn, met voorraad €38,75 (GEZIEN boek, GOK model).
- bitget - xt, €2.000,00: munten KOR, LUNC; bruto zonder voorraadgrens zou €230,37 zijn, met voorraad €5,04 (GEZIEN boek, GOK model).
- bitget - xt, €5.000,00: munten KOR, LUNC; bruto zonder voorraadgrens zou €230,37 zijn, met voorraad €11,31 (GEZIEN boek, GOK model).
- bitget - gate, €2.000,00: munten BABYSHARK, IR, LUNC, VERONA; bruto zonder voorraadgrens zou €41,87 zijn, met voorraad €8,03 (GEZIEN boek, GOK model).
- bitget - gate, €5.000,00: munten BABYSHARK, IR, LUNC, VERONA; bruto zonder voorraadgrens zou €41,87 zijn, met voorraad €10,03 (GEZIEN boek, GOK model).
- gate - xt, €2.000,00: munten YB; bruto zonder voorraadgrens zou €42,96 zijn, met voorraad €17,18 (GEZIEN boek, GOK model).
- gate - xt, €5.000,00: munten YB; bruto zonder voorraadgrens zou €42,96 zijn, met voorraad €33,84 (GEZIEN boek, GOK model).
- htx - xt, €2.000,00: munten CBK, LUNC, SEI, XDC; bruto zonder voorraadgrens zou €35,31 zijn, met voorraad €7,47 (GEZIEN boek, GOK model).
- htx - xt, €5.000,00: munten CBK, LUNC, SEI, XDC; bruto zonder voorraadgrens zou €35,31 zijn, met voorraad €14,73 (GEZIEN boek, GOK model).

Dag en Gemeten: de kansen komen alleen uit de uren dat de scanner mat (GEZIEN); het koerseffect loopt door over de hele tijd van de eerste tot de laatste meting. Rendement = netto gedeeld door de inleg, voor die dag. * = koers niet op te halen, koerseffect onbekend (niet als 0 bedoeld).

**Aannames:**

- Winst per kans: de mediaan van wat de scanner op het boek mat bij €100, €500, €1.000, €2.500 en de volle ruimte (GEZIEN), lineair daartussen (GOK). Uitgevoerd op het moment dat de kans begon, één keer per kans (GOK).
- Inleg: de helft geld (de quote van de kansen), de helft munten, verdeeld over de munten die op dat paar echte kansen hadden, en alles half op elke beurs (GOK). Die munten zijn **achteraf** gekozen; vooraf weet je dat niet.
- Terugschuiven zodra een kant onder 25% van zijn beginvoorraad komt: de helft van het verschil gaat terug, alleen als de opnamekosten hooguit 5% van het bedrag zijn (GOK, eigen regel).
- Opnamekosten van de munt: wat de scanner bij die beurs zag (GEZIEN uit de API van de beurs; bij Kraken en Gate geschat uit andere beurzen, GOK). Geld: zie de tabel hieronder.
- Een munt is na 30 minuten op de andere beurs (GOK). Zolang iets onderweg is, telt het niet als voorraad; kansen die daardoor niet of kleiner konden, staan als gemist of beperkt.
- Kleiner dan 10 euro telt als gemist (GOK; minimale order- en opnamebedragen per beurs niet meegeteld). USDT telt tegen de koers van het moment van de kans; de koers USDT-EUR zelf beweegt niet mee (GOK).
- Koerseffect: slotkoers per 15 minuten (of per uur) uit de openbare candles van Bitvavo, Kraken, KuCoin of Gate (GEZIEN), over alle aangehouden munten, ook als de scanner tussen twee runs even niet mat.
- Niet meegeteld: andere bots die dezelfde kans pakken, dat het boek zich na jouw order aanvult (dan kan het vaker), belasting, en dat de EU-versie van een beurs minder munten kan hebben dan de API die we meten.
- Geld terugschuiven per beurs: bitget USDT: 1 USDT, GOK (1 USDT, 30 min; niet nagekeken); bitvavo EUR: 0 EUR, kosten GEZIEN (api.bitvavo.com/v2/assets: EUR withdrawalFee 0), tijd GOK (1 werkdag, SEPA); gate USDT: 1 USDT, GOK (1 USDT, 30 min; niet nagekeken); htx USDT: 1 USDT, GOK (1 USDT, 30 min; niet nagekeken); kraken EUR: 1 EUR, kosten GEZIEN (support.kraken.com/articles/360000381846: Instant SEPA, Banking Circle, 1 EUR, near-instant), tijd GOK (1 uur tot het op de andere beurs staat); kucoin USDT: 1 USDT, kosten GEZIEN (api.kucoin.com/api/v3/currencies/USDT: BEP20 1 USDT), tijd GOK; xt USDT: 1 USDT, GOK (1 USDT, 30 min; niet nagekeken).

## Over de meting

- Opnamekosten bij de echte kansen: 20 van een netwerk dat aan beide kanten open is, 54 van de beurs zelf (laagste open netwerk), 5 geschat uit wat andere beurzen voor die munt vragen (GOK). Onbekende opnamekosten tellen niet als echte kans.
- Netwerk: KuCoin, Gate, Bitget, HTX, XT, Bitstamp, Bitvavo en Poloniex geven hun netwerken per munt. Als beide beurzen dat doen en de namen te koppelen zijn, moet er een netwerk zijn dat aan beide kanten open is. Anders is het netwerk "niet te koppelen" en telt de kans mee (staat apart in de trechter).
- De duur is gemeten in stappen van ±20 seconden; een kans kan een paar rondes eerder begonnen zijn dan we zagen.
- Takerkosten: uit de API waar die ze per paar geeft, anders het standaardtarief uit de README (deels GOK).
- Laatste run: 15 beurzen antwoordden, 2286 munt-quote-paren op minstens twee beurzen (GEZIEN).
