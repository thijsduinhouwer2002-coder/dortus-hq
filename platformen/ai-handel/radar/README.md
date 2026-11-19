# Kansenradar

Onderzoek voor Thijs zelf, geen Dortus-product en geen advies. De scanner (`../scanner/`) meet gewone
prijsverschillen tussen beurzen. Deze radar kijkt een week lang naar drie **zeldzame momenten** waarvan op forums
wordt gezegd dat daar het geld ligt, en meet of dat klopt na alle kosten:

- **A. Nieuwe noteringen.** Een munt komt nieuw op een beurs. Is hij daar de eerste uren duurder of goedkoper dan
  op beurzen waar hij al stond, en kun je dat pakken (opnemen en storten open, genoeg op het boek)?
- **B. Funding-pieken.** Een perpetual heeft een uitzonderlijk hoge funding (boven 0,1% per 8 uur). Wat had een
  gedekte positie (spot kopen en de perp shorten) na kosten opgeleverd, en hoe lang duurde de piek?
- **C. Stablecoins die afwijken.** USDC, USDT, EURC, EURe en de rest tegen EUR, USD, USDT en USDC op alle beurzen.
  Wanneer zitten ze meer dan 0,3% naast hun gewone prijs, of is dezelfde munt op de ene beurs goedkoper dan op de andere?

Zoeker D mat funding al als gemiddelde: 3 tot 11% per jaar (`../D-arbitrage.md` hoofdstuk 2). Hier gaat het om de
uitschieters.

## Wat hij doet
| Hoek | Hoe vaak | Wat |
|---|---|---|
| A | elke 3 minuten | de lijst met handelsparen van 15 beurzen naast de vorige leggen. Een munt die de beurs nog nooit had (ook niet in de vorige run), is een nieuwe notering. |
| A | elke minuut, 6 uur lang | de orderboeken van die munt op de nieuwe beurs en op hooguit 6 beurzen waar hij al stond (zelfde quote), beide richtingen. Rekensom van de scanner: takerkosten aan beide kanten en één opname van de munt. Plus opname- en stortstatus, netwerk en contractadres. |
| B | elke 2 minuten | de funding van alle perpetuals op OKX, Bitget, Gate, MEXC, KuCoin, BingX, Kraken Futures, Hyperliquid en dYdX (±5.000 perps). |
| C | elke 15 seconden | per beurs in één verzoek bod en laat van alle paren; waar een stablecoin afwijkt of tussen beurzen een gat laat zien, ook het orderboek (hooguit 4 boeken per beurs per ronde). |
| C | elke 6 uur | de basislijn per stablecoin: mediaan van de slotkoers per dag over de laatste 45 dagen (OHLC-API van Kraken, Bitvavo, OKX, Gate, MEXC, Bitget of KuCoin). |
| alle | elk half uur | opname- en stortstatus, opnamekosten, minimale order- en opnamebedragen (uit de API's). |

Dat blijft ruim binnen de limieten van de beurzen: hooguit een paar verzoeken per beurs per 15 seconden.

**Een funding-piek** begint als de funding boven 0,1% per 8 uur komt (perps die elk uur of elke 4 uur verrekenen
worden omgerekend naar 8 uur). De radar doet alsof je op dat moment spot koopt en de perp shortt. Hij telt de
funding die **echt verrekend** wordt (hij ziet dat het tijdstip van de volgende verrekening opschuift en neemt de
laatste rate van daarvoor). Hij stapt uit als de funding onder 0,05% zakt, maar pas na minstens één verrekening.
Winst = verrekende funding min 4 keer takerkosten (spot in en uit, perp in en uit), plus of min het verschil tussen
spot- en perpprijs bij in- en uitstappen, min één keer **overmaken** als spot en perp op twee beurzen zitten (een
opname van USDT of USDC voor het onderpand: opnamekosten uit de API van de spotbeurs, anders de mediaan van andere
beurzen als GOK; het minimale opnamebedrag uit `minima.py`). De spot koop je bij dezelfde beurs als die de munt
heeft, anders bij de beurs met de laagste takerkosten.
- **Geen spotkoers** (verzoek mislukt, paar niet in de ticker): de piek wacht en stapt in zodra er een koers is.
  Komt die er niet, dan staat hij als "spotkoers onbekend" apart; hij wordt niet weggegooid.
- **Andere munt:** is de spotprijs meer dan 5% anders dan de perp (en geen factor 1000 zoals bij 1000PEPE), dan is
  het waarschijnlijk een ander ding met dezelfde naam en telt de piek niet.
- **Over runs heen:** open pieken gaan bij het einde van een run (en na elke ronde) naar `pieken-open.json` op de
  datatak; de volgende vaste run maakt ze af. Zo betaalt een piek één keer 4 x takerkosten, ook als hij dagen duurt.
  Verrekeningen in het gat tussen twee runs telt hij met de laatste bekende rate (GOK, staat apart als
  `verrekeningen_geschat`). Stopte de vorige run meer dan 2 uur eerder, dan sluit hij de pieken als "gat te lang"
  (apart, niet in de som). Bij een herstart kan een piek twee keer in de data komen; het rapport telt hem één keer.
- **Negatieve pieken** staan apart: daar moet je spot shorten, dat kan een particulier meestal niet.

**Stablecoins** worden op twee manieren bekeken:
1. **Tussen beurzen (C1):** dezelfde munt in dezelfde quote goedkoper kopen dan hij elders verkocht wordt, na
   takerkosten en opnamekosten. Dat is echte arbitrage.
2. **Naast de gewone prijs (C2):** het boek zit minstens 0,3% naast de **basislijn**: de mediaan van de slotkoers
   per dag over de laatste 45 dagen, gedeeld door de koppeling (1 dollar of 1 euro; EUR tegen USD per dag van
   Kraken). Zo is EURQ, die al weken rond 0,97 euro staat (GEZIEN, Kraken OHLC: mediaan 0,968 over 45 dagen), geen
   kans: 3% onder de euro is daar gewoon de prijs. Pas als hij 0,3% naast die 0,97 komt, telt het. Geen basislijn
   (munt korter dan 20 dagen in de handel, of geen bron): het moment staat apart en telt niet. Dit is **geen**
   arbitrage: je wint alleen als de koers naar zijn gewone prijs terugkomt.

## Wat telt als echt moment
- **A en C1:** winst na alle kosten, opnamekosten bekend of geschat, opnemen op de koopbeurs en storten op de
  verkoopbeurs open (bekend, niet "onbekend"), geen netwerk dat aan beide kanten dicht is, geen ander
  contractadres, minstens 2 metingen en minstens €100 winstgevend op het boek.
- **B:** positieve piek, ingestapt met een spotkoers die bij de perp past, en afgerond. Ook pieken die geld kosten
  tellen mee: een bot weet vooraf niet hoe het afloopt.
- **C2:** basislijn bekend, minstens €100 op het boek met 0,3% afwijking, en na 2 keer takerkosten nog winst.

Winst per moment is die bij de **eerste meting** (meteen instappen), uit het echte orderboek.

## Kleine inleg (€100, €150, €200) en één pot
Thijs wil weten wat het met weinig geld oplevert. Het rapport rekent daarom per hoek bij €100, €150, €200, €500,
€2.000 en €5.000, en bovenaan staat per hoek in één zin wat **€150** tot nu toe opleverde.

**Eén pot:** de sommen tellen niet alle momenten op alsof je ze met €150 allemaal tegelijk pakt. Je pakt een moment
als je geld vrij is (het vorige moment dat je pakte is voorbij); beginnen er twee tegelijk, dan het beste. De pot
zit vast tot het moment voorbij is (bij B tot je uitstapt). Het rapport zet ernaast hoeveel momenten er hoogstens
tegelijk open stonden: zoveel potten had je nodig gehad om alles te pakken. Bij €100 tot €200 telt een moment alleen als de **minimale orderbedragen** op beide beurzen (en
bij A en C1 het **minimale opnamebedrag**) bekend zijn en eronder liggen. Vaste kosten per keer, zoals de
opnamekosten van de munt, zitten in de winst en wegen bij een kleine inleg zwaar. Bij B is de inleg verdeeld als
2/3 spot en 1/3 onderpand voor de short bij 2x hefboom (GOK, een gangbare verdeling): van €100 gaat €67 in de positie.

## Wat hij niet ziet
- **Snelheid.** We kijken elke 15 seconden, elke minuut of elke paar minuten. Handelsfirma's kijken elke
  milliseconde en zitten vaak in hetzelfde datacenter als de beurs. Een gat dat korter bestaat dan onze stap zien we
  niet; een gat dat we wel zien, is vaak al deels weggekocht voor een gewone gebruiker zijn order plaatst. De sommen
  per week nemen aan dat je alles pakt wat wij zagen: dat is een **bovengrens (GOK)**.
- **Noteringen in de eerste seconden.** De eerste minuten na een notering (waar de grootste gaten zitten) zien we
  hooguit met een vertraging van 3 minuten. Tussen twee runs zit een gat: een run duurt 5 uur 25 minuten en de klok
  start om de 6 uur, dus ±35 minuten per 6 uur zonder meting (meer als GitHub een geplande run laat vallen). Een
  notering in dat gat zien we bij de eerste vergelijking na de start; die staat apart in het rapport.
- **Voorraad.** A en C1 rekenen met één opname per keer. In het echt heb je dan voorraad op beide beurzen nodig, of
  je moet overmaken en dan is het gat vaak weg. Hoe snel een opname aankomt, meten we niet.
- **Perp-diepte.** Bij B nemen we de laatste prijs van de perp, niet het boek. Bij een dunne perp kost een order
  meer. Het rapport toont de handel per dag; onder $1 miljoen per dag is de som te mooi (GOK).
- **Vergunning per product.** De MiCA-lijst gaat over spot. Of de EU-dochter van een beurs perps aan Nederlandse
  particulieren geeft, is niet nagekeken (GOK: vaak niet of beperkt). Volgens de keuring biedt Kraken futures aan
  EER-klanten via een MiFID II-vergunning op Cyprus (DERDEN, support.kraken.com, niet zelf gelezen); of dat de
  `PF_`-perps zijn die we meten, is niet nagekeken. Hyperliquid en dYdX zijn DEX'en zonder vergunning.
- **Hefboom.** Bij B rekenen we met 2x op de short. Een sprong van ±50% kan de short liquideren; dat zit niet in de som.
- **dYdX.** `nextFundingRate` lijkt kleiner dan de laatst verrekende rate; misschien een lopend gemiddelde (GOK,
  niet nagekeken). Pieken op dYdX kunnen daardoor gemist worden.
- **Bybit en Binance** weigeren vanaf de server en vanaf GitHub (VS): niet gemeten.

## Hoe het draait
- Workflow `.github/workflows/radar.yml`: één job van ±5 uur 25 minuten, daarna de volgende (klok
  `organisatie/controle/klok.py`, interval 6 uur, net als de scanner). Hij start ook bij elke push naar main; de klok
  beslist of hij aan de beurt is. Alleen een push die de **code** raakt (`radar/*.py`, `radar/*.sh`, de workflow, en
  `scanner/beurzen.py` en `scanner/scanner.py`, die de radar gebruikt) start hem opnieuw; een tekst zoals deze
  README niet.
- Elk half uur en aan het eind gaat de data naar de tak **`ai-handel-data`**, map `radar/<datum>/run-<nummer>/`:
  `noteringen.jsonl` (elke nieuwe notering), `noteringen-kansen.jsonl` (A), `funding.jsonl` (B, één regel per
  piek), `stable-tussen.jsonl` (C1), `stable-afwijking.jsonl` (C2), `stand.jsonl` (elke 5 minuten),
  `samenvatting.json`, `paren-laatst.json`, `pieken-open.json` en `basislijn.json`. Ook `radar/rapport.md`,
  `radar/paren-laatst.json` en `radar/pieken-open.json` (waarmee de volgende run begint) worden bij elke keer
  opslaan opnieuw gemaakt. Nooit geforceerd.
- Een proefrun (met de hand, opdrachtbestand met invoer `minuten`) krijgt `-proef` achter de mapnaam en raakt de klok
  en de vaste run niet. Het rapport telt proefruns niet mee, tenzij `--met-proef`.
- Zelf draaien: `python3 radar.py --minuten 10 --uit /tmp/radar/2026-11-19/run-1` en dan
  `python3 radar_rapport.py /tmp/radar --met-proef`.
- Tests: `python3 -m unittest test_radar` (in deze map, geen internet nodig).

Het rapport: `https://raw.githubusercontent.com/thijsduinhouwer2002-coder/dortus-hq/ai-handel-data/radar/rapport.md`.

## Kosten en minima
- **Spot-takerkosten:** uit de API waar de beurs ze per paar geeft, anders `beurzen.taker_standaard` van de scanner
  (tabel in `../scanner/README.md`). Kraken: 0,80% op gewone munten, 0,20% op stablecoin- en FX-paren (ook EURQ, RLUSD en
  de andere stablecoins van de radar), 0% op alle USDe-paren en 0,01% op USDG-paren (GEZIEN, kraken.com/pro/fees,
  19 nov). Radar, rapport en scanner gebruiken dezelfde functie. Data met een ander Kraken-tarief dan dit (van
  vóór de fixes) zet het rapport apart.
- **Perp-takerkosten:** Gate 0,075%, MEXC 0,02%, Bitget en KuCoin 0,06%, BingX 0,05% (GEZIEN, contract-API, 19 nov);
  Kraken Futures 0,05% (DERDEN, kraken.com/pro/fees volgens de keuring); OKX 0,05%, Hyperliquid 0,045%, dYdX 0,05% (GOK).
- **Minimale bedragen** (GEZIEN, veld in de openbare API, 19 nov 2026):

| Beurs | Minimale spotorder | Minimale opname | Minimale perporder |
|---|---|---|---|
| Kraken | `costmin`, `ordermin` (AssetPairs) | niet in de API (wel op kraken.com/pro/fees) | niet in de lijst |
| Bitvavo | `minOrderInQuoteAsset`, `minOrderInBaseAsset` | `withdrawalMinAmount` | geen perps |
| Coinbase | `quote_min_size`, `base_min_size` | niet openbaar | geen perps |
| Bitstamp | `minimum_order` | niet openbaar | geen perps |
| OKX | `minSz` | niet openbaar | `ctVal` x `minSz` |
| KuCoin | `minFunds`, `baseMinSize` | `withdrawalMinSize` | `multiplier` x `lotSize` |
| Gate | `min_quote_amount`, `min_base_amount` | niet openbaar | `quanto_multiplier` x `order_size_min` |
| MEXC | `quoteAmountPrecision` | niet openbaar | `contractSize` x `minVol` |
| Bitget | `minTradeUSDT`, `minTradeAmount` | `minWithdrawAmount` | `minTradeUSDT`, `minTradeNum` |
| HTX | `minov`, `minoa` | `minWithdrawAmt` | niet gemeten |
| Crypto.com | `qty_tick_size` | niet openbaar | niet gemeten |
| Poloniex | `minAmount`, `minQuantity` | niet openbaar | niet gemeten |
| XT | filter `QUOTE_QTY` | `withdrawMinAmount` | niet gemeten |
| BingX | `minNotional`, `minQty` | niet openbaar | `tradeMinUSDT`, `tradeMinQuantity` |
| Bitfinex | `pub:info:pair` (minimum in munten) | niet openbaar | geen perps gemeten |
| Hyperliquid, dYdX | geen spot gemeten | - | Hyperliquid niet in de lijst; dYdX `stepSize` |

Waar "niet openbaar" staat, is het minimum **onbekend** en telt een moment bij €100 tot €200 niet mee (staat apart).

## Bestanden
| Bestand | Wat |
|---|---|
| `radar.py` | de lus en wat de drie hoeken delen (paren, wallets, minima, takerkosten); hergebruikt `../scanner/beurzen.py` en de rekensom uit `../scanner/scanner.py` |
| `hoek_a.py`, `hoek_b.py`, `hoek_c.py` | A noteringen, B funding-pieken, C stablecoins |
| `rekenen.py` | vaste waarden en losse rekensommen (zonder internet) |
| `basislijn.py` | slotkoersen per dag (OHLC) voor de basislijn van C2 |
| `perps.py` | funding van 9 perp-beurzen uit openbare API's |
| `minima.py` | minimale order- en opnamebedragen per beurs |
| `radar_rapport.py` | het rapport per hoek, per dag en per inleg |
| `opslaan.sh` | zet de data op de tak `ai-handel-data`, map `radar/` (nooit geforceerd) |
| `test_radar.py` | tests van de rekensommen, het herkennen van noteringen, de funding-boekhouding en het rapport |
| `ontwerp.md` | waarom zo gebouwd |
