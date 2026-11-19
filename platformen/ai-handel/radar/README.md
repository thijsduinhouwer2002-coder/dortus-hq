# Kansenradar

Onderzoek voor Thijs zelf, geen Dortus-product en geen advies. De scanner (`../scanner/`) meet gewone
prijsverschillen tussen beurzen. Deze radar kijkt een week lang naar drie **zeldzame momenten** waarvan op forums
wordt gezegd dat daar het geld ligt, en meet of dat klopt na alle kosten:

- **A. Nieuwe noteringen.** Een munt komt nieuw op een beurs. Is hij daar de eerste uren duurder of goedkoper dan
  op beurzen waar hij al stond, en kun je dat pakken (opnemen en storten open, genoeg op het boek)?
- **B. Funding-pieken.** Een perpetual heeft een uitzonderlijk hoge funding (boven 0,1% per 8 uur). Wat had een
  gedekte positie (spot kopen en de perp shorten) na kosten opgeleverd, en hoe lang duurde de piek?
- **C. Stablecoins die afwijken.** USDC, USDT, EURC, EURe en de rest tegen EUR, USD, USDT en USDC op alle beurzen.
  Wanneer zitten ze meer dan 0,3% naast hun koppeling, of is dezelfde munt op de ene beurs goedkoper dan op de andere?

Zoeker D mat funding al als gemiddelde: 3 tot 11% per jaar (`../D-arbitrage.md` hoofdstuk 2). Hier gaat het om de
uitschieters.

## Wat hij doet
| Hoek | Hoe vaak | Wat |
|---|---|---|
| A | elke 3 minuten | de lijst met handelsparen van 15 beurzen naast de vorige leggen. Een munt die de beurs nog nooit had (ook niet in de vorige run), is een nieuwe notering. |
| A | elke minuut, 6 uur lang | de orderboeken van die munt op de nieuwe beurs en op hooguit 6 beurzen waar hij al stond (zelfde quote), beide richtingen. Rekensom van de scanner: takerkosten aan beide kanten en één opname van de munt. Plus opname- en stortstatus, netwerk en contractadres. |
| B | elke 2 minuten | de funding van alle perpetuals op OKX, Bitget, Gate, MEXC, KuCoin, BingX, Kraken Futures, Hyperliquid en dYdX (±5.000 perps). |
| C | elke 15 seconden | per beurs in één verzoek bod en laat van alle paren; waar een stablecoin afwijkt of tussen beurzen een gat laat zien, ook het orderboek (hooguit 4 boeken per beurs per ronde). |
| alle | elk half uur | opname- en stortstatus, opnamekosten, minimale order- en opnamebedragen (uit de API's). |

Dat blijft ruim binnen de limieten van de beurzen: hooguit een paar verzoeken per beurs per 15 seconden.

**Een funding-piek** begint als de funding boven 0,1% per 8 uur komt (perps die elk uur of elke 4 uur verrekenen
worden omgerekend naar 8 uur). De radar doet alsof je op dat moment spot koopt en de perp shortt. Hij telt de
funding die **echt verrekend** wordt (hij ziet dat het tijdstip van de volgende verrekening opschuift en neemt de
laatste rate van daarvoor). Hij stapt uit als de funding onder 0,05% zakt, maar pas na minstens één verrekening.
Winst = verrekende funding min 4 keer takerkosten (spot in en uit, perp in en uit) plus of min het verschil tussen
spot- en perpprijs bij in- en uitstappen. De spot koop je bij dezelfde beurs als die de munt heeft, anders bij de
beurs met de laagste takerkosten. Is de spotprijs meer dan 5% anders dan de perp (en geen factor 1000 zoals bij
1000PEPE), dan is het waarschijnlijk een ander ding met dezelfde naam en telt de piek niet. Negatieve pieken staan
apart: daar moet je spot shorten, dat kan een particulier meestal niet.

**Stablecoins** worden op twee manieren bekeken:
1. **Tussen beurzen (C1):** dezelfde munt in dezelfde quote goedkoper kopen dan hij elders verkocht wordt, na
   takerkosten en opnamekosten. Dat is echte arbitrage.
2. **Los van de koppeling (C2):** het boek zit minstens 0,3% van 1 dollar of 1 euro af. USDT en USDC als quote
   tellen als 1 dollar; EUR tegen USD komt uit het EUR/USD-boek van Kraken (of Bitstamp). Dit is **geen**
   arbitrage: je wint alleen als de koers terugkomt. Het rapport zegt hoeveel er na 2 keer takerkosten overblijft.

## Wat telt als echt moment
- **A en C1:** winst na alle kosten, opnamekosten bekend of geschat, opnemen op de koopbeurs en storten op de
  verkoopbeurs open (bekend, niet "onbekend"), geen netwerk dat aan beide kanten dicht is, geen ander
  contractadres, minstens 2 metingen en minstens €100 winstgevend op het boek.
- **B:** positieve piek met een spotmarkt die bij de perp past. Ook pieken die geld kosten tellen mee: dat is
  eerlijk, want een bot weet vooraf niet hoe het afloopt.
- **C2:** minstens €100 op het boek met 0,3% afwijking (anders is het een dode markt).

Winst per moment is die bij de **eerste meting** (meteen instappen), uit het echte orderboek.

## Kleine inleg (€100, €150, €200)
Thijs wil weten wat het met weinig geld oplevert. Het rapport rekent daarom per hoek bij €100, €150, €200, €500,
€2.000 en €5.000. Bij €100 tot €200 telt een moment alleen als de **minimale orderbedragen** op beide beurzen (en
bij A en C1 het **minimale opnamebedrag**) bekend zijn en eronder liggen. Vaste kosten per keer, zoals de
opnamekosten van de munt, zitten in de winst en wegen bij een kleine inleg zwaar. Bij B is de inleg verdeeld als
2/3 spot en 1/3 onderpand voor de short bij 2x hefboom (GOK, een gangbare verdeling): van €100 gaat €67 in de positie.

## Wat hij niet ziet
- **Snelheid.** We kijken elke 15 seconden, elke minuut of elke paar minuten. Handelsfirma's kijken elke
  milliseconde en zitten vaak in hetzelfde datacenter als de beurs. Een gat dat korter bestaat dan onze stap zien we
  niet; een gat dat we wel zien, is vaak al deels weggekocht voor een gewone gebruiker zijn order plaatst. De sommen
  per week nemen aan dat je alles pakt wat wij zagen: dat is een **bovengrens (GOK)**.
- **Noteringen in de eerste seconden.** De eerste minuten na een notering (waar de grootste gaten zitten) zien we
  hooguit met een vertraging van 3 minuten. Een notering tussen twee runs (de runs sluiten op elkaar aan, met een
  paar minuten ertussen) zien we bij de eerste vergelijking na de start; die staat apart in het rapport.
- **Voorraad.** A en C1 rekenen met één opname per keer. In het echt heb je dan voorraad op beide beurzen nodig, of
  je moet overmaken en dan is het gat vaak weg. Hoe snel een opname aankomt, meten we niet.
- **Perp-diepte.** Bij B nemen we de laatste prijs van de perp, niet het boek. Bij een dunne perp kost een order
  meer. Het rapport toont de handel per dag; onder $1 miljoen per dag is de som te mooi (GOK).
- **Vergunning per product.** De MiCA-lijst gaat over spot. Of de EU-dochter van een beurs perps aan Nederlandse
  particulieren geeft, is niet nagekeken (GOK: vaak niet of beperkt). Hyperliquid en dYdX zijn DEX'en zonder vergunning.
- **Bybit en Binance** weigeren vanaf de server en vanaf GitHub (VS): niet gemeten.

## Hoe het draait
- Workflow `.github/workflows/radar.yml`: één job van ±5 uur 25 minuten, daarna de volgende (klok
  `organisatie/controle/klok.py`, interval 6 uur, net als de scanner). Hij start ook bij elke push naar main; de klok
  beslist of hij aan de beurt is. Een push die de radar raakt, start hem opnieuw met de nieuwe code.
- Elk half uur en aan het eind gaat de data naar de tak **`ai-handel-data`**, map `radar/<datum>/run-<nummer>/`:
  `noteringen.jsonl` (elke nieuwe notering), `noteringen-kansen.jsonl` (A), `funding.jsonl` (B, één regel per
  piek), `stable-tussen.jsonl` (C1), `stable-afwijking.jsonl` (C2), `stand.jsonl` (elke 5 minuten),
  `samenvatting.json` en `paren-laatst.json`. Ook `radar/rapport.md` en `radar/paren-laatst.json` (de lijst waarmee
  de volgende run begint) worden bij elke keer opslaan opnieuw gemaakt. Nooit geforceerd.
- Een proefrun (met de hand, opdrachtbestand met invoer `minuten`) krijgt `-proef` achter de mapnaam en raakt de klok
  en de vaste run niet. Het rapport telt proefruns niet mee, tenzij `--met-proef`.
- Zelf draaien: `python3 radar.py --minuten 10 --uit /tmp/radar/2026-11-19/run-1` en dan
  `python3 radar_rapport.py /tmp/radar --met-proef`.
- Tests: `python3 -m unittest test_radar` (in deze map, geen internet nodig).

Het rapport: `https://raw.githubusercontent.com/thijsduinhouwer2002-coder/dortus-hq/ai-handel-data/radar/rapport.md`.

## Kosten en minima
- **Spot-takerkosten:** dezelfde als de scanner (uit de API waar die ze per paar geeft, anders de tabel in
  `../scanner/README.md`).
- **Perp-takerkosten** (standaard, laagste trede, allemaal GOK, niet nagekeken): OKX, Gate, BingX, Kraken, dYdX
  0,05%; Bitget en KuCoin 0,06%; MEXC 0,02%; Hyperliquid 0,045%.
- **Minimale bedragen** (GEZIEN, veld in de openbare API, 19 nov 2026):

| Beurs | Minimale spotorder | Minimale opname | Minimale perporder |
|---|---|---|---|
| Kraken | `costmin`, `ordermin` (AssetPairs) | niet openbaar | niet in de lijst |
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
| `radar.py` | de meting (A, B en C in één lus); hergebruikt `../scanner/beurzen.py` en de rekensom uit `../scanner/scanner.py` |
| `perps.py` | funding van 9 perp-beurzen uit openbare API's |
| `minima.py` | minimale order- en opnamebedragen per beurs |
| `radar_rapport.py` | het rapport per hoek, per dag en per inleg |
| `opslaan.sh` | zet de data op de tak `ai-handel-data`, map `radar/` (nooit geforceerd) |
| `test_radar.py` | tests van de rekensommen, het herkennen van noteringen, de funding-boekhouding en het rapport |
| `ontwerp.md` | waarom zo gebouwd |
