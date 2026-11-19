# Rapport koersverschil-scanner

Gemaakt 2026-11-19 15:22 UTC uit 6 runs, samen ±6.3 uur gemeten (GEZIEN).
Echte kans = winst na alle kosten (opnamekosten bekend), opnemen en storten open (en een netwerk dat aan beide kanten open is, als de beurzen dat geven), minstens €100,00 op het boek, minstens 2 minuten blijven staan, geen andere munt met dezelfde naam.
**Vergund** = beide beurzen hebben een MiCA-vergunning (ESMA-register), vaak via een EU-dochter die minder munten kan hebben dan de wereldwijde API die we meten (GOK). **Grijs** = minstens één beurs zonder vergunning (MEXC, Bitget, HTX, Poloniex, XT, Bitfinex, Binance). Zie README.md.

## Hoeveel wordt er gecontroleerd? (GEZIEN, stand.jsonl)

Per ronde (mediaan over 75 metingen): 1039 kandidaten (verschil op de ticker groter dan de takerkosten), 120 met het orderboek gecontroleerd, 2 nog nooit gecontroleerd (0%).
Bijna alle kandidaten komen aan de beurt; de aantallen hieronder missen weinig.

## Trechter (GEZIEN, eigen metingen)

| Stap | Alle beurzen | Alleen MiCA-beurzen | Met minstens één grijze beurs |
|---|---|---|---|
| Verschillen met winst op het boek na alle kosten | 5071 | 714 | 4357 |
| ...waarvan opnemen of storten dicht | 954 | 80 | 874 |
| ...waarvan status onbekend (beurs geeft het niet openbaar) | 2915 | 420 | 2495 |
| Opnemen en storten open | 1202 | 214 | 988 |
| ...en geen netwerk dat aan beide kanten open is: valt af | 17 | 0 | 17 |
| ...en opnamekosten onbekend: valt af | 0 | 0 | 0 |
| ...en minstens €100,00 op het boek | 410 | 163 | 247 |
| ...en minstens 2 minuten blijven staan | 108 | 50 | 58 |
| ...en geen andere munt met dezelfde naam | 100 | 47 | 53 |
|    ...waarvan contractadres bekend en gelijk | 7 | 1 | 6 |
|    ...waarvan contractadres onbekend (telt mee, kan een andere munt zijn) | 93 | 46 | 47 |
|    ...waarvan netwerk gekoppeld en open | 45 | 8 | 37 |
|    ...waarvan netwerk niet te koppelen (telt mee) | 55 | 39 | 16 |
| **Echte kansen** (zelfde munt overlappend in de tijd samengevoegd, beste beurspaar telt) | 72 | 47 | 33 |
| Ter vergelijking: zelfde eisen, maar opnamestatus onbekend (niet meegeteld) | 192 | 53 | 158 |

## Echte kansen per dag (GEZIEN)

| Dag | Echt, alleen MiCA | Echt, met grijs | Mediane winst per kans bij €500 (MiCA / grijs) | Mediane duur |
|---|---|---|---|---|
| 2026-11-19 | 39 | 33 | €1,62 / €0,88 | 4.8 min |
| Totaal | 39 | 33 | €1,62 / €0,88 | 4.8 min |

## Beste munten (GEZIEN)

| | Soort | Kansen | Som winst bij €500 per kans |
|---|---|---|---|
| MERL-EUR | vergund | 7 | €61,12 |
| LUNA-EUR | vergund | 6 | €20,65 |
| DYM-EUR | vergund | 18 | €17,62 |
| YB-USDT | grijs | 1 | €16,34 |
| LUNC-USDT | grijs | 3 | €15,44 |
| WAN-USDT | grijs | 3 | €12,65 |
| GMT-EUR | vergund | 5 | €11,95 |
| VERONA-USDT | grijs | 5 | €10,92 |
| USTC-USDT | grijs | 2 | €7,82 |
| CBK-USDT | grijs | 3 | €4,13 |

## Beste beursparen (kopen op > verkopen op) (GEZIEN)

| | Soort | Kansen | Som winst bij €500 per kans |
|---|---|---|---|
| bitvavo > kraken | vergund | 38 | €113,49 |
| bitget > gate | grijs | 5 | €18,41 |
| gate > xt | grijs | 1 | €16,34 |
| kucoin > htx | grijs | 5 | €13,65 |
| kucoin > bitget | grijs | 4 | €8,36 |
| htx > xt | grijs | 1 | €5,83 |
| bitget > htx | grijs | 5 | €3,98 |
| bitget > xt | grijs | 2 | €3,96 |
| xt > htx | grijs | 1 | €3,52 |
| bitget > kucoin | grijs | 4 | €2,67 |

Beurzen die het vaakst meedoen (koop of verkoop): bitvavo 38, kraken 38, bitget (grijs) 20, htx (grijs) 16, kucoin 15, gate 9, xt (grijs) 6, poloniex (grijs) 2 (GEZIEN).

## Hoeveel kansen blijven staan terwijl je geld schuift? (GEZIEN, duur uit eigen metingen)

Wie geen voorraad op beide beurzen heeft, moet kopen, de munt opnemen, wachten tot hij binnen is en dan verkopen. Hoe lang dat duurt verschilt per munt en netwerk: een paar minuten (snelle ketens) tot een uur of meer (Bitcoin, beurzen die opnames met de hand keuren) (GOK, niet per munt gemeten).

| Overmaaktijd | Alle beurzen | Alleen MiCA-beurzen | Met minstens één grijze beurs |
|---|---|---|---|
| 5 min | 36 van 72 (50%) | 19 van 47 (40%) | 20 van 33 (61%) |
| 10 min | 19 van 72 (26%) | 13 van 47 (28%) | 8 van 33 (24%) |
| 30 min | 14 van 72 (19%) | 10 van 47 (21%) | 5 van 33 (15%) |
| 60 min | 5 van 72 (7%) | 4 van 47 (9%) | 2 van 33 (6%) |

## Wat zou het opleveren over 3 maanden? (GOK, doorgetrokken uit de metingen)

Gemeten over ±6.3 uur (GEZIEN), doorgetrokken naar 90 dagen (GOK: aanname dat de week die we maten gewoon is).

| Beurzen | Inleg | Model | Kansen per uur | Per kans (mediaan) | 3 maanden |
|---|---|---|---|---|---|
| Alleen MiCA | €2.000,00 | bovengrens: elke kans, geld overal tegelijk | 7.52 | €2,48 | €40.206,63 |
| Alleen MiCA | €2.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 6.08 | €2,95 | €64.099,28 |
| Alleen MiCA | €5.000,00 | bovengrens: elke kans, geld overal tegelijk | 7.52 | €2,48 | €40.206,63 |
| Alleen MiCA | €5.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 6.08 | €4,00 | €93.587,67 |
| Alle (met grijs) | €2.000,00 | bovengrens: elke kans, geld overal tegelijk | 11.52 | €1,74 | €43.253,79 |
| Alle (met grijs) | €2.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 6.08 | €2,95 | €64.099,28 |
| Alle (met grijs) | €5.000,00 | bovengrens: elke kans, geld overal tegelijk | 11.52 | €2,09 | €52.054,59 |
| Alle (met grijs) | €5.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 6.08 | €4,00 | €93.587,67 |

Bovengrens: elke kans met de helft van de inleg aan elke kant, alsof het geld op alle beurzen tegelijk staat (kan in het echt niet). Beste beurspaar: het paar is **achteraf** gekozen uit de metingen (vooraf kiezen levert minder op), en het model neemt aan dat je van elke munt al voorraad op de verkoopbeurs hebt.

Waarom dit te rooskleurig is (GOK): elke kans wordt maar één keer geteld met het mediane boek, maar andere bots pakken hem ook; de munt die je als voorraad aanhoudt kan dalen; na een paar kansen moet de voorraad terug (opnamekosten en tijd); minimale opname- en ordergroottes tellen niet mee; en een kans die we 2 minuten zagen staan, staat er niet per se nog als jouw order binnenkomt. Waarom het te somber kan zijn: niet alle kandidaten zijn gecontroleerd, en met voorraad op beide beurzen kun je dezelfde kans vaker pakken als het boek zich aanvult; dat telt hier niet mee.

## Over de meting

- Opnamekosten bij de echte kansen: 18 van een netwerk dat aan beide kanten open is, 49 van de beurs zelf (laagste open netwerk), 5 geschat uit wat andere beurzen voor die munt vragen (GOK). Onbekende opnamekosten tellen niet als echte kans.
- Netwerk: KuCoin, Gate, Bitget, HTX, XT, Bitstamp, Bitvavo en Poloniex geven hun netwerken per munt. Als beide beurzen dat doen en de namen te koppelen zijn, moet er een netwerk zijn dat aan beide kanten open is. Anders is het netwerk "niet te koppelen" en telt de kans mee (staat apart in de trechter).
- De duur is gemeten in stappen van ±20 seconden; een kans kan een paar rondes eerder begonnen zijn dan we zagen.
- Takerkosten: uit de API waar die ze per paar geeft, anders het standaardtarief uit de README (deels GOK).
- Laatste run: 15 beurzen antwoordden, 2286 munt-quote-paren op minstens twee beurzen (GEZIEN).
