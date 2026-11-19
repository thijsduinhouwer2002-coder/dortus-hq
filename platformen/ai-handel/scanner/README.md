# Koersverschil-scanner

Onderzoek voor Thijs zelf, geen Dortus-product en geen advies. Vraag: bestaan er tussen crypto-beurzen bij
kleinere munten prijsverschillen die **na alle kosten** overblijven, **lang genoeg** blijven staan om te pakken,
en waar je **echt** je munt kunt opnemen en storten? Zoeker D mat alleen BTC-EUR op 4 beurzen (verschil 0,007%,
zie `../D-arbitrage.md` hoofdstuk 1). Deze scanner meet een week lang alle munten op 15 tot 17 beurzen.

## Wat hij doet
- Elke ±20 seconden haalt hij van elke beurs in één verzoek het beste bod en de beste laat van alle paren.
- Hij vergelijkt alleen dezelfde munt in **dezelfde quote** (USDT met USDT, EUR met EUR, USDC, USD). Hij rekent
  nooit om tussen quotes; euro's in het rapport zijn alleen omgerekend om bedragen te kunnen optellen (koers
  USDT-EUR van Kraken of Bitvavo, USD via EUR-USD van Kraken).
- Is kopen op beurs A en verkopen op beurs B duurder dan de takerkosten samen, dan haalt hij de orderboeken op
  en loopt ze af: hoeveel euro kun je kopen en verkopen met winst na takerkosten aan beide kanten en de
  opnamekosten van de munt (één opname per kans). Hij rekent de winst uit bij €100, €500, €1.000 en €2.500 per
  kans, en hoeveel euro er in totaal winstgevend op het boek ligt (tot €20.000).
- Hij houdt bij hoe lang elk verschil blijft staan (begin en eind, in stappen van ±20 seconden).
- Hij noteert per kans of **opnemen op de koopbeurs** en **storten op de verkoopbeurs** open staan, volgens de
  openbare API van de beurs (elk half uur ververst). Geven beide beurzen hun netwerken per munt (KuCoin, Gate,
  Bitget, HTX, XT, Bitstamp, Bitvavo, Poloniex), dan kijkt hij of er een netwerk is dat aan beide kanten open is
  (namen als "ERC20", "ETH" en "Ethereum" tellen als hetzelfde) en neemt hij de opnamekosten van dat netwerk.
- Rooster: per ronde hooguit 120 boekcontroles. Eerst open kansen waar alles open is, dan kandidaten die nog nooit
  bekeken zijn, dan open kansen waar opnemen, storten of netwerk dicht of onbekend is (hooguit eens per ±3 rondes),
  dan de rest. Het rapport meldt hoeveel kandidaten nooit bekeken zijn.
- Hij gooit weg: verschillen boven 15%, op de ticker en op het boek (bijna altijd een andere munt met dezelfde naam of een dode markt),
  hefboomtokens (ETH3S, BTC5L: bestaan maar op één beurs) en markten die niet handelen.
- Hij markeert munten waarvan de contractadressen op beide beurzen bekend zijn maar niet gelijk: dan is het
  waarschijnlijk een andere munt met dezelfde naam (bijv. twee verschillende "AI"-tokens). Die tellen niet.

## Wat hij niet doet
- Geen account, geen sleutel, geen handel, geen geld. Alleen openbare API's lezen.
- Het **netwerk** vergelijkt hij alleen als beide beurzen hun netwerken geven en de namen te koppelen zijn. Anders
  staat het netwerk als "niet te koppelen"; zulke kansen tellen mee en staan apart in de trechter.
- Hij meet niet hoe snel een opname echt aankomt. Het rapport toont daarom per overmaaktijd (5, 10, 30, 60
  minuten) welk deel van de kansen dan nog stond.
- Opname- en stortstatus: Kraken, Bitvavo, Bitstamp, KuCoin, Gate, Bitget, HTX, Poloniex en XT geven die openbaar.
  OKX, MEXC, Crypto.com, BingX, Bitfinex, Bybit, Binance en Coinbase niet (Coinbase alleen "online").
  Kansen met zo'n beurs staan als **status onbekend** en tellen niet mee als echte kans; het rapport toont ze apart.
- Opnamekosten: openbaar bij Bitvavo, KuCoin, Bitget, HTX, Poloniex en XT. Bij de andere nemen we de mediaan van
  wat de beurzen die het wel noemen voor die munt vragen (GOK, staat als "geschat" in de data). Noemt geen enkele
  beurs ze, dan is de kans geen echte kans (niet als 0 gerekend).

## Hoe het draait
- Workflow `.github/workflows/scanner.yml`: één job van ±5 uur 25 minuten, daarna de volgende. Hij start bij een
  gepland tijdstip (4 keer per dag) en bij elke push naar main; de klok (`organisatie/controle/klok.py`, interval
  6 uur) beslist of hij aan de beurt is, omdat GitHub geplande runs in deze repo vaak laat vallen.
- Elk half uur en aan het eind zet hij de data op de tak **`ai-handel-data`**, map `scanner/<datum>/run-<nummer>/`:
  `kansen.jsonl` (één regel per kans), `stand.jsonl` (elke ±5 minuten hoe de meting ervoor staat),
  `beurzen.json` (welke beurzen antwoorden, hoeveel paren) en `samenvatting.json`. Ook `scanner/rapport.md`
  wordt bij elke keer opslaan opnieuw gemaakt.
- Een proefrun (met de hand, via een opdrachtbestand met invoer `minuten`) krijgt `-proef` achter de mapnaam en
  raakt de klok en de vaste run niet. Het rapport telt proefruns niet mee (ze lopen gelijk met de vaste run en
  zouden dubbel tellen); `python3 rapport.py <map> --met-proef` neemt ze wel mee.
- Zelf draaien: `python3 scanner.py --minuten 10 --uit /tmp/scan` en dan `python3 rapport.py /tmp --met-proef`.
- Tests: `python3 -m unittest test_scanner` (in deze map).

## Het rapport lezen
Het staat op `https://raw.githubusercontent.com/thijsduinhouwer2002-coder/dortus-hq/ai-handel-data/scanner/rapport.md`.

Een **echte kans** moet aan alles voldoen: (1) winst na takerkosten en opnamekosten (die bekend of geschat zijn),
(2) opnemen en storten open (bekend), en geen netwerk-mismatch als beide beurzen hun netwerken geven, (3) minstens
€100 winstgevend op het boek, (4) minstens 2 minuten blijven staan, (5) niet zichtbaar een andere munt.

Alles staat in drie kolommen: **alle beurzen**, **alleen MiCA-beurzen** (beide beurzen vergund) en **met minstens
één grijze beurs**. Zo zie je wat de route met alleen vergunde beurzen oplevert en wat de grijze route erbij doet. Kansen van dezelfde munt die in de tijd overlappen (bijv. goedkoop op MEXC, duur op vijf
andere beurzen) tellen als **één** kans, met het beste beurspaar.

- **Hoeveel wordt er gecontroleerd**: kandidaten per ronde, hoeveel met het boek bekeken en hoeveel nog nooit.
  Zolang dat laatste meer dan 5% is, zijn alle aantallen en sommen een **ondergrens**.
- **Trechter**: hoeveel verschillen er waren en bij welke stap ze afvallen. Hier zie je hoe vaak het gat er alleen
  is omdat opnemen of storten dicht staat, en hoeveel kansen een onbekend contractadres of netwerk hebben.
- **Per dag**: aantal echte kansen, mediane winst per kans bij €500 en bij de volle ruimte op het boek, mediane duur.
- **Beste munten en beursparen**.
- **Overmaaktijd**: welk deel van de echte kansen er na 5, 10, 30 en 60 minuten nog stond. Zonder voorraad op
  beide beurzen moet je de munt overmaken; dan telt alleen de regel die past bij de snelheid van dat netwerk.
- **3 maanden bij €2.000 en €5.000**: twee sommen, allebei GOK. De bovengrens neemt aan dat je elke kans pakt met
  de helft van je inleg aan elke kant (geld overal tegelijk, kan in het echt niet). De tweede neemt alleen het
  beste beurspaar (al je geld op twee beurzen); dat paar is achteraf gekozen en het model neemt aan dat je van elke
munt al voorraad op de verkoopbeurs hebt. Beide sommen staan apart voor alleen MiCA en voor alle beurzen. Waarom
ze te rooskleurig of te somber kunnen zijn, staat eronder.

Het eerste rapport zegt iets na een paar runs (een dag); na 7 dagen is het een week aan metingen.

## Wat houd je echt over? (voorraad-simulatie)
De sommen hierboven nemen aan dat je geld overal tegelijk staat. In het echt heb je geld en munten op twee beurzen
staan, en na een paar kansen is de ene kant leeg. `simulatie.py` rekent dat na op de opgeslagen echte kansen. Het
rapport toont het in het blok **"Wat houd je echt over?"**, per beurspaar (alle MiCA-paren en de 5 beste grijze
paren), per dag, voor een inleg van €100, €150, €200, €2.000 en €5.000. Bovenaan staat in één regel wat het met
€150 per dag oplevert.

Hoe het rekent, met een voorbeeld van €2.000 op Bitvavo en Kraken:
- Je begint met €1.000 in euro en €1.000 in munten (verdeeld over de munten die op dat paar echte kansen hadden),
  en alles half op elke beurs: €500 euro en €500 aan munten op Bitvavo, net zo op Kraken.
- Bij elke echte kans koop je op de goedkope beurs en verkoop je tegelijk op de dure beurs uit je voorraad, 2 minuten
  na het begin (dan pas weet je dat hij meetelt). Je zet niet meer in dan er winstgevend op het boek lag (gemeten),
  niet meer dan het geld op de koopbeurs en niet meer dan de munten op de verkoopbeurs. Er gaat bij een kans niets
  over de keten. Gaat dezelfde kans binnen 5 minuten weer open, dan is het deel van het boek dat je al gebruikte op.
- Elke beurs heeft een minimale order (in euro en in munten) en een minimale opname. Die haalt het rapport uit de
  openbare API van Bitvavo, Kraken, KuCoin en Gate. Een kans onder het minimum telt als gemist. Met weinig geld is
  dat vaak zo: bij €100 over 5 munten heb je €5 per munt per beurs, en Bitvavo wil minstens €5 per order.
- Zakt een kant onder 25% van wat er aan het begin stond, dan schuif je terug: de helft van het verschil gaat naar
  de lege kant, maar alleen als de kosten hooguit 1% van het bedrag zijn (een kans levert maar ±0,3 tot 1% op).
  Die 1% is achteraf gekozen (eerst 5%, daar aten de kosten met €150 de winst op); de tabel "Andere keuzes"
  laat ook 2% en 5% zien.
  Met weinig geld schuif je daardoor bijna nooit: je handelt tot een kant leeg is en dan stopt het. Dat kost opnamekosten (munt: wat de beurs zelf noemt; euro: Bitvavo €0, Kraken €1 met Instant SEPA)
  en tijd (munt 30 minuten, euro 1 uur vanaf Kraken en 1 werkdag vanaf Bitvavo, USDT 30 minuten; tijden zijn een
  GOK). Wat onderweg is, kun je niet gebruiken. Kansen die daardoor niet konden, staan als **gemist**; kansen die
  kleiner moesten, als **kleiner door voorraad**.
- De munten die je aanhoudt, worden meer of minder waard. Dat is het **koerseffect**, apart gemeld (koersen uit de
  openbare candles van Bitvavo, KuCoin, Gate of Kraken). Lukt het ophalen niet, dan staat er "onbekend".
- **Netto handel** = bruto winst min kosten terugschuiven: dat is wat de methode oplevert. **Netto met koerseffect**
  telt de waardeverandering van je munten erbij. Het koerseffect is het risico van de voorraad, geen opbrengst: bij
  één munt over een paar uur is het vooral toeval (een munt die op een dag 50% stijgt, geeft een mooi getal dat niets
  met de methode te maken heeft). Rendement = netto gedeeld door de inleg, beide apart.
- Onder de tabel staat voor het beste MiCA-paar wat een andere schuifdrempel (10%, 25%, 40%) of minder munten met
  meer voorraad per munt doet.

Wat je moet weten: de munten in de voorraad zijn achteraf gekozen (vooraf weet je niet welke munten kansen geven);
het koerseffect kan veel groter zijn dan de winst (een munt die op één dag 50% stijgt of daalt); en andere bots die
dezelfde kans pakken tellen niet mee. Alle aannames staan onder de tabel in het rapport.
Zonder koersen en minima draaien (sneller, geen netwerk): `python3 rapport.py <map> --zonder-koers`.

## Takerkosten per beurs (standaardtarief, laagste trede)
Waar de API het tarief per paar geeft, gebruikt de scanner dat (GEZIEN, uit de API, per paar). Anders deze tabel.

| Beurs | Taker | Bron |
|---|---|---|
| Gate | per paar uit de API, meestal 0,2% | GEZIEN, `api.gateio.ws/api/v4/spot/currency_pairs` veld `fee` (ETH_USDT: 0,2) |
| MEXC | per paar uit de API, meestal 0,05% | GEZIEN, `api.mexc.com/api/v3/exchangeInfo` veld `takerCommission` (ETHUSDT: 0,0005) |
| Bitget | per paar uit de API | GEZIEN, `api.bitget.com/api/v2/spot/public/symbols` veld `takerFeeRate` (ETHUSDT: 0,002 = 0,2%; hun website noemt 0,1%, wij nemen de API) |
| KuCoin | 0,1% x klasse (A/B/C = 1/2/3) x coëfficiënt uit de API | klasse en coëfficiënt GEZIEN (`api.kucoin.com/api/v2/symbols`), 0,1% per klasse GOK |
| Bitfinex | 0% | GEZIEN, [bitfinex.com/fees](https://www.bitfinex.com/fees): "Spot and Margin trades ... Taker Fees Zero" |
| Kraken | 0,80% (munt tegen EUR, USD, USDT of USDC); 0,20% op stablecoin- en FX-paren | GEZIEN, [kraken.com/pro/fees](https://www.kraken.com/pro/fees) (19 nov 2026): "Spot fees, Tier 1: 0.40% maker, 0.80% taker" en "Stablecoin and FX pair fees ... from 0.20% maker and 0.20% taker". De API geeft per paar geen tarief. Tot 19 nov rekende de scanner met 0,40% (GOK); het rapport rekent die oude kansen opnieuw door (zie rapport.py, `herreken`) |
| Bitvavo | 0,25% | GEZIEN, [support.bitvavo.com](https://support.bitvavo.com/hc/en-us/articles/4405175148689) (19 nov 2026, via de help-center-API): "we reserve the maximum fee of 0.25%", "maximum taker fee of 0.25%" (laagste trede; met meer volume lager) |
| Coinbase | 1,20% | GOK, Advanced laagste trede, niet nagekeken; daardoor doet Coinbase zelden mee |
| Bitstamp | 0,40% | GOK, niet nagekeken |
| OKX | 0,10% | GOK, gewone gebruiker, niet nagekeken |
| HTX | 0,20% | GOK, niet nagekeken |
| Crypto.com | 0,50% | GOK, voorzichtig gekozen, niet nagekeken |
| Poloniex | 0,20% | GOK, niet nagekeken |
| XT | 0,20% | GOK, niet nagekeken |
| BingX | 0,10% | GOK, niet nagekeken |
| Bybit, Binance | 0,10% | GOK; antwoorden niet vanaf onze server (403 en 451), mogelijk ook niet vanaf GitHub (VS) |

Opnamekosten van de munt komen uit de API van de beurs (zie boven); geen tabel, want ze verschillen per munt.

## Vergunning: wat mag in Nederland? (ESMA-register)
Bron: het MiCA-register van ESMA voor cryptodienstverleners, zelf gedownload op 19 nov 2026
([CASPS.csv](https://www.esma.europa.eu/sites/default/files/2024-12/CASPS.csv), laatst gewijzigd 18 nov 2026; GEZIEN).
Let op: de vergunning hoort vaak bij een **EU-dochter** met een eigen site. De API die de scanner meet is de
wereldwijde versie. Een Nederlandse klant komt bij de EU-versie terecht, die minder munten kan hebben dan we meten
(GOK, niet per munt nagekeken).

| Beurs | MiCA (ESMA) | Wie heeft de vergunning |
|---|---|---|
| Bitvavo | ja | Bitvavo B.V. (NL) |
| Kraken | ja | Payward Europe / Global Solutions (IE) |
| Coinbase | ja | Coinbase Luxembourg (LU) |
| Bitstamp | ja | Bitstamp Europe (LU) |
| OKX | ja, EU-dochter | OKX Europe (MT) |
| Crypto.com | ja, EU-dochter | Foris DAX MT (MT) |
| Bybit | ja, EU-dochter | Bybit EU, bybit.eu (AT) |
| KuCoin | ja, EU-dochter | KuCoin EU, kucoin.eu (AT, sinds 27 nov 2025) |
| Gate | ja, EU-dochter | Gate Technology, gate.com/en-eu (MT) |
| BingX | ja, EU-dochter | BingX EU, bingx.eu (AT, sinds 13 okt 2026) |
| MEXC | **nee**, grijs | niet in het register |
| Bitget | **nee**, grijs | niet in het register |
| HTX (Huobi) | **nee**, grijs | niet in het register |
| Poloniex | **nee**, grijs | niet in het register |
| XT.com | **nee**, grijs | niet in het register (de "XT"-treffers zijn XTB en anderen) |
| Bitfinex | **nee**, grijs | niet in het register (ook niet als iFinex) |
| Binance | **nee**, grijs | niet in het register |

Grijs betekent hier: een beurs zonder MiCA-vergunning gebruiken als particulier in Nederland. Het risico is vooral
dat je account dicht kan of je geld vast kan komen te zitten, en dat je bij problemen nergens terecht kunt (GOK).
Zie ook `../A-kant-en-klaar.md` hoofdstuk 2. MEXC staat in de eerste metingen bij veel kansen aan de koopkant.

## Bestanden
| Bestand | Wat |
|---|---|
| `beurzen.py` | koppelingen met de openbare API's (paren, koersen, orderboek, opname- en stortstatus) |
| `scanner.py` | de meting: kandidaten zoeken, boeken aflopen, kansen volgen en wegschrijven |
| `rekensom.py` | de rekensom: twee boeken tegelijk aflopen, winst na takerkosten en opnamekosten (ook gebruikt door de radar via `scanner.*`) |
| `rapport.py` | het rapport uit de data |
| `simulatie.py` | wat je overhoudt met voorraad op twee beurzen (terugschuiven, kosten, koerseffect) |
| `simrapport.py` | het blok "Wat houd je echt over?" in het rapport (tabellen, andere keuzes, aannames) |
| `simbronnen.py` | koersen (candles) en minimale order- en opnamebedragen uit de openbare API's, voor de simulatie |
| `opslaan.sh` | zet de data op de tak `ai-handel-data` (nooit geforceerd) |
| `test_scanner.py` | tests van de rekensom, het volgen van kansen, het rapport en de simulatie |
| `ontwerp.md` | waarom zo gebouwd |
