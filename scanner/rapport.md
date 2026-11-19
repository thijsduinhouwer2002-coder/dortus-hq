# Rapport koersverschil-scanner

Gemaakt 2026-11-19 15:34 UTC uit 8 runs, samen ±6.5 uur gemeten (GEZIEN).
Echte kans = winst na alle kosten (opnamekosten bekend), opnemen en storten open (en een netwerk dat aan beide kanten open is, als de beurzen dat geven), minstens €100,00 op het boek, minstens 2 minuten blijven staan, geen andere munt met dezelfde naam.
**Vergund** = beide beurzen hebben een MiCA-vergunning (ESMA-register), vaak via een EU-dochter die minder munten kan hebben dan de wereldwijde API die we meten (GOK). **Grijs** = minstens één beurs zonder vergunning (MEXC, Bitget, HTX, Poloniex, XT, Bitfinex, Binance). Zie README.md.

## Hoeveel wordt er gecontroleerd? (GEZIEN, stand.jsonl)

Per ronde (mediaan over 78 metingen): 1042 kandidaten (verschil op de ticker groter dan de takerkosten), 120 met het orderboek gecontroleerd, 2 nog nooit gecontroleerd (0%).
Bijna alle kandidaten komen aan de beurt; de aantallen hieronder missen weinig.

## Trechter (GEZIEN, eigen metingen)

| Stap | Alle beurzen | Alleen MiCA-beurzen | Met minstens één grijze beurs |
|---|---|---|---|
| Verschillen met winst op het boek na alle kosten | 5643 | 800 | 4843 |
| ...waarvan opnemen of storten dicht | 1141 | 96 | 1045 |
| ...waarvan status onbekend (beurs geeft het niet openbaar) | 3200 | 472 | 2728 |
| Opnemen en storten open | 1302 | 232 | 1070 |
| ...en geen netwerk dat aan beide kanten open is: valt af | 19 | 0 | 19 |
| ...en opnamekosten onbekend: valt af | 0 | 0 | 0 |
| ...en minstens €100,00 op het boek | 447 | 175 | 272 |
| ...en minstens 2 minuten blijven staan | 136 | 62 | 74 |
| ...en geen andere munt met dezelfde naam | 124 | 57 | 67 |
|    ...waarvan contractadres bekend en gelijk | 7 | 1 | 6 |
|    ...waarvan contractadres onbekend (telt mee, kan een andere munt zijn) | 117 | 56 | 61 |
|    ...waarvan netwerk gekoppeld en open | 55 | 10 | 45 |
|    ...waarvan netwerk niet te koppelen (telt mee) | 69 | 47 | 22 |
| **Echte kansen** (zelfde munt overlappend in de tijd samengevoegd, beste beurspaar telt) | 86 | 57 | 39 |
| Ter vergelijking: zelfde eisen, maar opnamestatus onbekend (niet meegeteld) | 192 | 53 | 158 |

## Echte kansen per dag (GEZIEN)

| Dag | Echt, alleen MiCA | Echt, met grijs | Mediane winst per kans bij €500 (MiCA / grijs) | Mediane duur |
|---|---|---|---|---|
| 2026-11-19 | 47 | 39 | €1,99 / €1,02 | 4.8 min |
| Totaal | 47 | 39 | €1,99 / €1,02 | 4.8 min |

## Beste munten (GEZIEN)

| | Soort | Kansen | Som winst bij €500 per kans |
|---|---|---|---|
| MERL-EUR | vergund | 9 | €91,52 |
| LUNC-USDT | grijs | 5 | €26,38 |
| DYM-EUR | vergund | 20 | €22,57 |
| LUNA-EUR | vergund | 6 | €20,65 |
| GMT-EUR | vergund | 7 | €18,44 |
| YB-USDT | grijs | 1 | €16,34 |
| USTC-USDT | grijs | 4 | €15,61 |
| WAN-USDT | grijs | 3 | €12,65 |
| VERONA-USDT | grijs | 7 | €11,93 |
| AVA-EUR | vergund | 3 | €7,30 |

## Beste beursparen (kopen op > verkopen op) (GEZIEN)

| | Soort | Kansen | Som winst bij €500 per kans |
|---|---|---|---|
| bitvavo > kraken | vergund | 46 | €160,20 |
| bitget > gate | grijs | 5 | €18,41 |
| gate > xt | grijs | 1 | €16,34 |
| kucoin > bitget | grijs | 6 | €16,14 |
| kucoin > htx | grijs | 5 | €13,65 |
| bitget > xt | grijs | 3 | €8,35 |
| kucoin > xt | grijs | 1 | €6,56 |
| htx > xt | grijs | 1 | €5,83 |
| bitget > htx | grijs | 5 | €3,98 |
| bitget > kucoin | grijs | 6 | €3,67 |

Beurzen die het vaakst meedoen (koop of verkoop): bitvavo 46, kraken 46, bitget (grijs) 25, kucoin 20, htx (grijs) 16, gate 9, xt (grijs) 8, poloniex (grijs) 2 (GEZIEN).

## Hoeveel kansen blijven staan terwijl je geld schuift? (GEZIEN, duur uit eigen metingen)

Wie geen voorraad op beide beurzen heeft, moet kopen, de munt opnemen, wachten tot hij binnen is en dan verkopen. Hoe lang dat duurt verschilt per munt en netwerk: een paar minuten (snelle ketens) tot een uur of meer (Bitcoin, beurzen die opnames met de hand keuren) (GOK, niet per munt gemeten).

| Overmaaktijd | Alle beurzen | Alleen MiCA-beurzen | Met minstens één grijze beurs |
|---|---|---|---|
| 5 min | 43 van 86 (50%) | 24 van 57 (42%) | 23 van 39 (59%) |
| 10 min | 19 van 86 (22%) | 13 van 57 (23%) | 8 van 39 (21%) |
| 30 min | 14 van 86 (16%) | 10 van 57 (18%) | 5 van 39 (13%) |
| 60 min | 5 van 86 (6%) | 4 van 57 (7%) | 2 van 39 (5%) |

## Wat zou het opleveren over 3 maanden? (GOK, doorgetrokken uit de metingen)

Gemeten over ±6.5 uur (GEZIEN), doorgetrokken naar 90 dagen (GOK: aanname dat de week die we maten gewoon is).

| Beurzen | Inleg | Model | Kansen per uur | Per kans (mediaan) | 3 maanden |
|---|---|---|---|---|---|
| Alleen MiCA | €2.000,00 | bovengrens: elke kans, geld overal tegelijk | 8.77 | €3,01 | €56.956,67 |
| Alleen MiCA | €2.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 7.08 | €3,76 | €89.378,24 |
| Alleen MiCA | €5.000,00 | bovengrens: elke kans, geld overal tegelijk | 8.77 | €4,84 | €91.705,33 |
| Alleen MiCA | €5.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 7.08 | €5,20 | €138.814,31 |
| Alle (met grijs) | €2.000,00 | bovengrens: elke kans, geld overal tegelijk | 13.23 | €2,44 | €69.637,02 |
| Alle (met grijs) | €2.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 7.08 | €3,76 | €89.378,24 |
| Alle (met grijs) | €5.000,00 | bovengrens: elke kans, geld overal tegelijk | 13.23 | €3,52 | €100.693,34 |
| Alle (met grijs) | €5.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 7.08 | €5,20 | €138.814,31 |

Bovengrens: elke kans met de helft van de inleg aan elke kant, alsof het geld op alle beurzen tegelijk staat (kan in het echt niet). Beste beurspaar: het paar is **achteraf** gekozen uit de metingen (vooraf kiezen levert minder op), en het model neemt aan dat je van elke munt al voorraad op de verkoopbeurs hebt.

Waarom dit te rooskleurig is (GOK): elke kans wordt maar één keer geteld met het mediane boek, maar andere bots pakken hem ook; de munt die je als voorraad aanhoudt kan dalen; na een paar kansen moet de voorraad terug (opnamekosten en tijd); minimale opname- en ordergroottes tellen niet mee; en een kans die we 2 minuten zagen staan, staat er niet per se nog als jouw order binnenkomt. Waarom het te somber kan zijn: niet alle kandidaten zijn gecontroleerd, en met voorraad op beide beurzen kun je dezelfde kans vaker pakken als het boek zich aanvult; dat telt hier niet mee.

## Wat houd je echt over? Voorraad op twee beurzen (simulatie)

Per beurspaar: geld en munten op beide beurzen, elke echte kans uitgevoerd tegen het boek zoals gemeten (niet meer dan de ruimte op het boek en niet meer dan de voorraad op die beurs), terugschuiven als een kant leeg dreigt te raken (met opnamekosten en tijd onderweg), en het koerseffect van de aangehouden munten apart. Netto = bruto min kosten terugschuiven plus koerseffect. **Gemeten** (GEZIEN): de kansen, het boek en de koersen; **de rest is een rekenmodel** (GOK, aannames onder de tabel). Geen advies.

### Alleen MiCA-beurzen (alle paren met echte kansen)

| Beurspaar | Inleg | Dag | Gemeten | Kansen | Gemist (geen voorraad) | Kleiner door voorraad | Bruto winst | Kosten terugschuiven | Koerseffect voorraad | Netto | Rendement op de inleg |
|---|---|---|---|---|---|---|---|---|---|---|---|
| bitvavo - kraken | €2.000,00 | 2026-11-19 | 6.5 u | 46 | 26 | 20 | €15,32 | €13,48 (24x) | €0,23 | €2,07 | 0.10% |
| bitvavo - kraken | €5.000,00 | 2026-11-19 | 6.5 u | 46 | 25 | 21 | €37,43 | €13,48 (24x) | €0,59 | €24,54 | 0.49% |
| gate - kucoin | €2.000,00 | 2026-11-19 | 6.5 u | 11 | 3 | 8 | €6,60 | €2,81 (8x) | €-4,39 | €-0,60 | -0.03% |
| gate - kucoin | €5.000,00 | 2026-11-19 | 6.5 u | 11 | 2 | 5 | €12,95 | €2,19 (6x) | €-11,00 | €-0,25 | -0.01% |

- bitvavo - kraken, €2.000,00: munten AVA, DYM, GMT, LUNA, MERL, SSV; bruto zonder voorraadgrens zou €540,76 zijn, met voorraad €15,32 (GEZIEN boek, GOK model).
- bitvavo - kraken, €5.000,00: munten AVA, DYM, GMT, LUNA, MERL, SSV; bruto zonder voorraadgrens zou €540,76 zijn, met voorraad €37,43 (GEZIEN boek, GOK model).
- gate - kucoin, €2.000,00: munten ERG, IR, LUNC, USTC, VERONA; bruto zonder voorraadgrens zou €40,69 zijn, met voorraad €6,60 (GEZIEN boek, GOK model).
- gate - kucoin, €5.000,00: munten ERG, IR, LUNC, USTC, VERONA; bruto zonder voorraadgrens zou €40,69 zijn, met voorraad €12,95 (GEZIEN boek, GOK model).

### Met minstens één grijze beurs (de 5 paren met de meeste bruto winst)

| Beurspaar | Inleg | Dag | Gemeten | Kansen | Gemist (geen voorraad) | Kleiner door voorraad | Bruto winst | Kosten terugschuiven | Koerseffect voorraad | Netto | Rendement op de inleg |
|---|---|---|---|---|---|---|---|---|---|---|---|
| kucoin - xt | €2.000,00 | 2026-11-19 | 6.5 u | 5 | 2 | 3 | €16,00 | €3,76 (6x) | €29,60 | €41,84 | 2.09% |
| kucoin - xt | €5.000,00 | 2026-11-19 | 6.5 u | 5 | 2 | 3 | €38,75 | €3,76 (6x) | €74,01 | €109,00 | 2.18% |
| bitget - xt | €2.000,00 | 2026-11-19 | 6.5 u | 6 | 3 | 2 | €5,04 | €0,91 (2x) | onbekend | €18,93* | 0.95% |
| bitget - xt | €5.000,00 | 2026-11-19 | 6.5 u | 6 | 3 | 2 | €11,31 | €0,92 (3x) | onbekend | €47,40* | 0.95% |
| bitget - gate | €2.000,00 | 2026-11-19 | 6.5 u | 9 | 3 | 5 | €8,06 | €1,45 (7x) | €-10,70 | €-4,09 | -0.20% |
| bitget - gate | €5.000,00 | 2026-11-19 | 6.5 u | 9 | 2 | 5 | €12,29 | €1,25 (5x) | €-26,76 | €-15,72 | -0.31% |
| htx - xt | €2.000,00 | 2026-11-19 | 6.5 u | 10 | 3 | 6 | €7,48 | €3,83 (7x) | onbekend | €11,05* | 0.55% |
| htx - xt | €5.000,00 | 2026-11-19 | 6.5 u | 10 | 3 | 6 | €14,75 | €3,38 (6x) | onbekend | €29,88* | 0.60% |
| gate - xt | €2.000,00 | 2026-11-19 | 6.5 u | 1 | 0 | 1 | €17,18 | €0,91 (1x) | €452,84 | €469,11 | 23.46% |
| gate - xt | €5.000,00 | 2026-11-19 | 6.5 u | 1 | 0 | 1 | €33,84 | €0,91 (1x) | €1.132,10 | €1.165,02 | 23.30% |

- kucoin - xt, €2.000,00: munten LUNC; bruto zonder voorraadgrens zou €306,53 zijn, met voorraad €16,00 (GEZIEN boek, GOK model).
- kucoin - xt, €5.000,00: munten LUNC; bruto zonder voorraadgrens zou €306,53 zijn, met voorraad €38,75 (GEZIEN boek, GOK model).
- bitget - xt, €2.000,00: munten KOR, LUNC; bruto zonder voorraadgrens zou €280,48 zijn, met voorraad €5,04 (GEZIEN boek, GOK model).
- bitget - xt, €5.000,00: munten KOR, LUNC; bruto zonder voorraadgrens zou €280,48 zijn, met voorraad €11,31 (GEZIEN boek, GOK model).
- bitget - gate, €2.000,00: munten BABYSHARK, IR, LUNC, VERONA; bruto zonder voorraadgrens zou €46,36 zijn, met voorraad €8,06 (GEZIEN boek, GOK model).
- bitget - gate, €5.000,00: munten BABYSHARK, IR, LUNC, VERONA; bruto zonder voorraadgrens zou €46,36 zijn, met voorraad €12,29 (GEZIEN boek, GOK model).
- htx - xt, €2.000,00: munten CBK, LUNC, SEI, XDC; bruto zonder voorraadgrens zou €38,12 zijn, met voorraad €7,48 (GEZIEN boek, GOK model).
- htx - xt, €5.000,00: munten CBK, LUNC, SEI, XDC; bruto zonder voorraadgrens zou €38,12 zijn, met voorraad €14,75 (GEZIEN boek, GOK model).
- gate - xt, €2.000,00: munten YB; bruto zonder voorraadgrens zou €42,96 zijn, met voorraad €17,18 (GEZIEN boek, GOK model).
- gate - xt, €5.000,00: munten YB; bruto zonder voorraadgrens zou €42,96 zijn, met voorraad €33,84 (GEZIEN boek, GOK model).

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

- Opnamekosten bij de echte kansen: 21 van een netwerk dat aan beide kanten open is, 60 van de beurs zelf (laagste open netwerk), 5 geschat uit wat andere beurzen voor die munt vragen (GOK). Onbekende opnamekosten tellen niet als echte kans.
- Netwerk: KuCoin, Gate, Bitget, HTX, XT, Bitstamp, Bitvavo en Poloniex geven hun netwerken per munt. Als beide beurzen dat doen en de namen te koppelen zijn, moet er een netwerk zijn dat aan beide kanten open is. Anders is het netwerk "niet te koppelen" en telt de kans mee (staat apart in de trechter).
- De duur is gemeten in stappen van ±20 seconden; een kans kan een paar rondes eerder begonnen zijn dan we zagen.
- Takerkosten: uit de API waar die ze per paar geeft, anders het standaardtarief uit de README (deels GOK).
- Laatste run: 15 beurzen antwoordden, 2286 munt-quote-paren op minstens twee beurzen (GEZIEN).
