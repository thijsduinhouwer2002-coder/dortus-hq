# Rapport koersverschil-scanner

Gemaakt 2026-11-19 10:13 UTC uit 5 runs, samen ±1.3 uur gemeten (GEZIEN).
Echte kans = winst na alle kosten (opnamekosten bekend), opnemen en storten open (en een netwerk dat aan beide kanten open is, als de beurzen dat geven), minstens €100,00 op het boek, minstens 2 minuten blijven staan, geen andere munt met dezelfde naam.
**Vergund** = beide beurzen hebben een MiCA-vergunning (ESMA-register), vaak via een EU-dochter die minder munten kan hebben dan de wereldwijde API die we meten (GOK). **Grijs** = minstens één beurs zonder vergunning (MEXC, Bitget, HTX, Poloniex, XT, Bitfinex, Binance). Zie README.md.

## Hoeveel wordt er gecontroleerd? (GEZIEN, stand.jsonl)

Per ronde (mediaan over 15 metingen): 991 kandidaten (verschil op de ticker groter dan de takerkosten), 120 met het orderboek gecontroleerd, 650 nog nooit gecontroleerd (66%).
**Daarom zijn de aantallen en sommen hieronder een ondergrens:** een deel van de kandidaten is nooit met het boek bekeken.

## Trechter (GEZIEN, eigen metingen)

| Stap | Alle beurzen | Alleen MiCA-beurzen | Met minstens één grijze beurs |
|---|---|---|---|
| Verschillen met winst op het boek na alle kosten | 964 | 94 | 870 |
| ...waarvan opnemen of storten dicht | 226 | 19 | 207 |
| ...waarvan status onbekend (beurs geeft het niet openbaar) | 503 | 44 | 459 |
| Opnemen en storten open | 235 | 31 | 204 |
| ...en geen netwerk dat aan beide kanten open is: valt af | 3 | 0 | 3 |
| ...en opnamekosten onbekend: valt af | 0 | 0 | 0 |
| ...en minstens €100,00 op het boek | 66 | 21 | 45 |
| ...en minstens 2 minuten blijven staan | 16 | 2 | 14 |
| ...en geen andere munt met dezelfde naam | 14 | 1 | 13 |
|    ...waarvan contractadres bekend en gelijk | 1 | 0 | 1 |
|    ...waarvan contractadres onbekend (telt mee, kan een andere munt zijn) | 13 | 1 | 12 |
|    ...waarvan netwerk gekoppeld en open | 8 | 0 | 8 |
|    ...waarvan netwerk niet te koppelen (telt mee) | 6 | 1 | 5 |
| **Echte kansen** (zelfde munt overlappend in de tijd samengevoegd, beste beurspaar telt) | 10 | 1 | 9 |
| Ter vergelijking: zelfde eisen, maar opnamestatus onbekend (niet meegeteld) | 34 | 6 | 29 |

## Echte kansen per dag (GEZIEN)

| Dag | Echt, alleen MiCA | Echt, met grijs | Mediane winst per kans bij €500 (MiCA / grijs) | Mediane duur |
|---|---|---|---|---|
| 2026-11-19 | 1 | 9 | €5,15 / €0,52 | 7.2 min |
| Totaal | 1 | 9 | €5,15 / €0,52 | 7.2 min |

## Beste munten (GEZIEN)

| | Soort | Kansen | Som winst bij €500 per kans |
|---|---|---|---|
| LUNC-USDT | grijs | 2 | €5,31 |
| MERL-EUR | vergund | 1 | €5,15 |
| CBK-USDT | grijs | 3 | €4,13 |
| CORE-USDT | grijs | 2 | €1,11 |
| VERONA-USDT | grijs | 1 | €0,52 |
| USDT-EUR | grijs | 1 | €0,03 |

## Beste beursparen (kopen op > verkopen op) (GEZIEN)

| | Soort | Kansen | Som winst bij €500 per kans |
|---|---|---|---|
| bitvavo > kraken | vergund | 1 | €5,15 |
| xt > htx | grijs | 1 | €3,52 |
| htx > xt | grijs | 1 | €3,27 |
| bitget > xt | grijs | 1 | €2,04 |
| bitget > htx | grijs | 3 | €1,45 |
| bitget > kucoin | grijs | 1 | €0,52 |
| gate > htx | grijs | 1 | €0,27 |
| kucoin > bitget | grijs | 1 | €0,03 |

Beurzen die het vaakst meedoen (koop of verkoop): htx (grijs) 6, bitget (grijs) 6, xt (grijs) 3, kucoin 2, gate 1, bitvavo 1, kraken 1 (GEZIEN).

## Hoeveel kansen blijven staan terwijl je geld schuift? (GEZIEN, duur uit eigen metingen)

Wie geen voorraad op beide beurzen heeft, moet kopen, de munt opnemen, wachten tot hij binnen is en dan verkopen. Hoe lang dat duurt verschilt per munt en netwerk: een paar minuten (snelle ketens) tot een uur of meer (Bitcoin, beurzen die opnames met de hand keuren) (GOK, niet per munt gemeten).

| Overmaaktijd | Alle beurzen | Alleen MiCA-beurzen | Met minstens één grijze beurs |
|---|---|---|---|
| 5 min | 6 van 10 (60%) | 1 van 1 (100%) | 5 van 9 (56%) |
| 10 min | 2 van 10 (20%) | 0 van 1 (0%) | 2 van 9 (22%) |
| 30 min | 0 van 10 (0%) | 0 van 1 (0%) | 0 van 9 (0%) |
| 60 min | 0 van 10 (0%) | 0 van 1 (0%) | 0 van 9 (0%) |

## Wat zou het opleveren over 3 maanden? (GOK, doorgetrokken uit de metingen)

Gemeten over ±1.3 uur (GEZIEN), doorgetrokken naar 90 dagen (GOK: aanname dat de week die we maten gewoon is). Ondergrens: niet alle kandidaten zijn gecontroleerd.

| Beurzen | Inleg | Model | Kansen per uur | Per kans (mediaan) | 3 maanden |
|---|---|---|---|---|---|
| Alleen MiCA | €2.000,00 | bovengrens: elke kans, geld overal tegelijk | 0.80 | €6,23 | €10.762,53 |
| Alleen MiCA | €2.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 0.80 | €6,23 | €10.762,53 |
| Alleen MiCA | €5.000,00 | bovengrens: elke kans, geld overal tegelijk | 0.80 | €7,16 | €12.371,98 |
| Alleen MiCA | €5.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 0.80 | €7,16 | €12.371,98 |
| Alle (met grijs) | €2.000,00 | bovengrens: elke kans, geld overal tegelijk | 8.00 | €0,65 | €11.271,83 |
| Alle (met grijs) | €2.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 0.80 | €6,23 | €10.762,53 |
| Alle (met grijs) | €5.000,00 | bovengrens: elke kans, geld overal tegelijk | 8.00 | €0,65 | €11.271,83 |
| Alle (met grijs) | €5.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 0.80 | €7,16 | €12.371,98 |

Bovengrens: elke kans met de helft van de inleg aan elke kant, alsof het geld op alle beurzen tegelijk staat (kan in het echt niet). Beste beurspaar: het paar is **achteraf** gekozen uit de metingen (vooraf kiezen levert minder op), en het model neemt aan dat je van elke munt al voorraad op de verkoopbeurs hebt.

Waarom dit te rooskleurig is (GOK): elke kans wordt maar één keer geteld met het mediane boek, maar andere bots pakken hem ook; de munt die je als voorraad aanhoudt kan dalen; na een paar kansen moet de voorraad terug (opnamekosten en tijd); minimale opname- en ordergroottes tellen niet mee; en een kans die we 2 minuten zagen staan, staat er niet per se nog als jouw order binnenkomt. Waarom het te somber kan zijn: niet alle kandidaten zijn gecontroleerd, en met voorraad op beide beurzen kun je dezelfde kans vaker pakken als het boek zich aanvult; dat telt hier niet mee.

## Over de meting

- Opnamekosten bij de echte kansen: 3 van een netwerk dat aan beide kanten open is, 5 van de beurs zelf (laagste open netwerk), 2 geschat uit wat andere beurzen voor die munt vragen (GOK). Onbekende opnamekosten tellen niet als echte kans.
- Netwerk: KuCoin, Gate, Bitget, HTX, XT, Bitstamp, Bitvavo en Poloniex geven hun netwerken per munt. Als beide beurzen dat doen en de namen te koppelen zijn, moet er een netwerk zijn dat aan beide kanten open is. Anders is het netwerk "niet te koppelen" en telt de kans mee (staat apart in de trechter).
- De duur is gemeten in stappen van ±20 seconden; een kans kan een paar rondes eerder begonnen zijn dan we zagen.
- Takerkosten: uit de API waar die ze per paar geeft, anders het standaardtarief uit de README (deels GOK).
- Laatste run: 15 beurzen antwoordden, 2293 munt-quote-paren op minstens twee beurzen (GEZIEN).
