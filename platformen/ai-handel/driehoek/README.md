# Driehoek-meter

Onderzoek voor Thijs zelf, geen Dortus-product en geen advies. Vraag: bestaan er **binnen één beurs** driehoeken
(bijvoorbeeld euro naar bitcoin, bitcoin naar ether, ether terug naar euro) die **na alle kosten** winst geven,
**lang genoeg** blijven staan om te pakken en **genoeg diepte** hebben? En kan dat ook met **weinig geld**
(€100 tot €200)? Zoeker D schatte het al als "valt af" (drie keer kosten, zie `../D-arbitrage.md` hoofdstuk 1);
deze meter meet het een week lang op 8 beurzen.

Alleen openbare API's: geen account, geen sleutel, geen handel, geen geld.

## Wat hij doet
- Per beurs een eigen draad met een eigen ritme (elke 3 tot 5 seconden). Elke ronde haalt hij in één verzoek het
  beste bod en de beste laat van alle paren op die beurs.
- Hij zoekt alle driehoeken van 3 munten waarvan alle drie de paren op die beurs bestaan (op Kraken en OKX
  ±2.300, op Bitvavo 22, want daar zijn alleen euro- en USDC-paren) en rekent ze in beide richtingen door tegen de
  beste prijzen, met de takerkosten van elke stap.
- Geeft een driehoek dan winst, dan haalt hij de drie orderboeken op en loopt ze af: hoeveel euro kan erdoor met
  winst, en hoeveel blijft er over bij €100, €150, €200, €500, €1.000, €2.000, €5.000 en €10.000. Een bedrag telt
  alleen als alle drie orders boven de **minimale ordergrootte** van de beurs blijven (uit de API, per paar). Het
  aantal munten rondt hij per order naar beneden af op de **stapgrootte** van de beurs (ook uit de API), en bij
  Bitvavo rekent hij per euro-order €0,01 extra (Bitvavo rondt de kosten naar boven af op de cent).
- Hij volgt elke driehoek met winst tot hij weg is en schrijft dan één regel: winst, diepte in euro, hoe lang
  hij bleef staan, en waarom hij stopte.
- Elke 5 minuten noteert hij per beurs hoe de meting ervoor staat, ook als er niets te halen viel: hoeveel rondes,
  hoeveel kandidaten, en **hoe dicht de beste driehoek bij winst kwam** (zo zie je ook hoe ver het ernaast zit).
- Per beurs telt hij hoeveel driehoeken je met €100, €150 en €200 überhaupt kunt rondmaken (minimale
  ordergrootte op alle drie stappen).

## Wat hij niet doet
- Geen handel, geen account. Hij weet dus niet wat jouw tarief is; hij rekent met het standaardtarief van de
  laagste trede (tabel hieronder).
- Hij is niet snel. Wij meten elke paar seconden; snelle partijen (bots naast de server van de beurs) pakken een
  driehoek meestal binnen milliseconden. **Wat wij zien, is wat er overbleef.** Een driehoek die korter dan een
  ronde stond, zien we meestal niet.
- De EU-versie van een beurs (die minder paren kan hebben dan de wereldwijde API die we meten) rekent hij niet
  mee.

## Hoe het draait
- Workflow `.github/workflows/driehoek.yml`, naar het voorbeeld van de scanner: één job van ±5 uur 25 minuten,
  daarna de volgende. Hij start 4 keer per dag op een vast tijdstip en bij elke push naar main; de klok
  (`organisatie/controle/klok.py`, interval 6 uur) beslist of hij aan de beurt is. Een push die de code raakt
  (`*.py` in deze map, `opslaan.sh` of de workflow) start de vaste run opnieuw met de nieuwe code; een push met
  alleen tekst (README, KEURING.md) niet. Bij afbreken schrijft de meter binnen 5 seconden alles weg en zet de
  opslaan-stap de data alsnog op de tak.
- Meetweek: tot en met **27 nov 2026**. Daarna slaat de vaste run het meten over. Verlengen: `EINDE` in de
  workflow aanpassen.
- Elk half uur en aan het eind zet hij de data op de tak **`ai-handel-data`**, map `driehoek/<datum>/run-<nummer>/`:
  `driehoeken.jsonl` (één regel per driehoek met winst), `stand.jsonl` (elke 5 minuten per beurs),
  `beurs-<naam>.json` (paren, driehoeken, kosten, minimale inleg) en aan het eind `beurzen.json` en
  `samenvatting.json`. `driehoek/rapport.md` wordt bij elke keer opslaan opnieuw gemaakt.
- Een proefrun (met de hand, opdrachtbestand met invoer `minuten`) krijgt `-proef` achter de mapnaam en raakt de
  klok en de vaste run niet. Het rapport telt proefruns niet mee; `python3 rapport.py <map> --met-proef` wel.
- Zelf draaien: `python3 driehoek.py --minuten 10 --uit /tmp/dh/2026-11-19/run-1-proef` en dan
  `python3 rapport.py /tmp/dh --met-proef`.
- Tests: `python3 -m unittest test_driehoek` (in deze map, zonder netwerk).

## Het rapport lezen
Het staat op `https://raw.githubusercontent.com/thijsduinhouwer2002-coder/dortus-hq/ai-handel-data/driehoek/rapport.md`.

Bovenaan staat een **kort antwoord** in gewone woorden: hoeveel echte kansen er met €100 tot €200 waren en wat
dat per dag opleverde (GOK), apart voor de beurzen met en zonder vergunning. Daarna pas de tabellen.

Een **echte driehoek** moet aan alles voldoen: (1) winst na drie keer takerkosten op het orderboek, niet alleen
tegen de beste prijs, (2) op twee metingen die minstens 3 seconden uit elkaar liggen (en alle metingen daartussen)
elk minstens €100 diepte met winst, (3) bij die latere meting minstens €0,05 winst, (4) niet meer dan 5% winst per
rondje (dat is bijna altijd een dode markt of een foute koers). Alle bedragen zijn die van de latere meting: wat
er na 3 seconden nog stond, niet het beste moment. Wij meten op zijn best elke 3 seconden, dus dat is wat wij
hadden kunnen pakken.

**Eén kans, niet vier.** Eén scheve prijs op bijvoorbeeld een altcoin/BTC-paar zit op Kraken in meerdere
driehoeken tegelijk (via EUR, USD, USDT en USDC). Die willen allemaal hetzelfde stukje orderboek, en dat kun je
maar één keer leeghalen. Daarom voegt het rapport driehoeken op dezelfde beurs die tegelijk openstonden en
minstens één paar delen samen tot **één kans**, en telt het alleen de beste. Aantallen per dag en de opschaling
gaan over kansen, niet over driehoeken.

Alles staat apart voor **MiCA** (de beurs of een EU-dochter heeft een vergunning in het ESMA-register) en
**grijs** (geen vergunning). In het rapport:
- **Per beurs**: hoe vaak gemeten, fouten, en de beste marge per ronde (mediaan en hoogste). Is die negatief, dan
  verloor zelfs de beste driehoek geld. Een positieve marge is nog geen winst: de bulk-koers kan achterlopen of er
  ligt maar een paar cent op die prijs; het orderboek beslist.
- **Trechter**: hoeveel driehoeken bij welke stap afvallen.
- **Per dag**: aantal echte driehoeken en kansen, mediane winst per kans in euro, mediane diepte en hoe lang er
  minstens €100 diepte bleef staan.
- **Beste driehoeken per beurs**, en de grootste die net niet echt waren.
- **Kleine inleg**: per beurs hoeveel driehoeken met €100, €150 en €200 kunnen (minimale ordergrootte).
- **Opschaling** naar €100, €150, €200, €2.000 en €5.000 (GOK): som over de kansen van de winst die je bij die
  inleg na 3 seconden nog had kunnen pakken, per dag en maal 30 per maand, voor alle beurzen samen en voor alleen
  de beste beurs. Dit is een bovengrens: je pakt elke kans als eerste, met het geld al op de beurs. Waarom het in het echt minder is,
  staat eronder.

**Wanneer zegt het iets?** Na de eerste vaste run (±5,5 uur) zie je per beurs hoe dicht het bij winst komt. Na
een dag (4 runs) is het eerste rapport bruikbaar; na 7 dagen is het een week aan metingen, inclusief weekend en
drukke uren.

## Eerste meting: proef van 10 minuten (19 nov 2026, 15:31 tot 15:41 UTC)
GEZIEN, run 44555682966 op een GitHub-runner, data op `ai-handel-data` in `driehoek/2026-11-19/run-44555682966-proef/`.
- Alle 8 beurzen antwoordden vanaf GitHub, 0 fouten, geen enkele keer "te veel verzoeken".
- 0 echte driehoeken. Wel 3 keer winst op het boek, alle op MEXC (grijs), USDT > BTC > BDX > USDT: €0,02 winst
  op €16 diepte, 3 tot 12 seconden. Te dun om iets mee te doen.
- Beste driehoek per ronde na kosten (mediaan): Kraken -0,59%, Bitvavo -0,76%, Bitstamp -1,02%, Bitget -0,28%,
  OKX -0,10%, Gate -0,12%. KuCoin +0,35% en MEXC +0,37%, maar daar gaf het orderboek geen winst (de bulk-koers
  liep achter of er lag maar een paar cent op die prijs).
- Met €100 kun je op elke beurs bijna alle driehoeken rondmaken (Bitstamp 333 van 346, OKX 2.332 van 2.336, de
  rest allemaal): de kleinste inleg die alle drie orders boven het minimum houdt, is in de mediaan €10 of minder
  (Bitstamp €12,50). Een kleine inleg valt dus niet af door het minimum, maar door de kosten.
- Op MEXC werd 12% van de kandidaten overgeslagen door het budget; daarom is het budget daar naar 15 boeken per
  ronde gegaan.

Na de keuring (19 nov) zijn de kosten van Kraken (USDe 0%, USDG 0,01%, pegged-token paren 0,20%) en Bitstamp
(FX en stablecoin 0,08%) bijgesteld. Lokaal 75 seconden gemeten met de nieuwe kosten (GEZIEN, 19 nov 16:03 UTC):
beste driehoek per ronde Kraken -0,21% (was -0,59%) en Bitstamp -0,24% (was -1,02%), dichter bij nul maar nog
steeds verlies.

Tien minuten zeggen weinig: het rapport wordt zinvol na een dag (4 vaste runs) en echt na de week.

## Takerkosten per stap (standaardtarief, laagste trede)

| Beurs | Taker | Bron |
|---|---|---|
| Kraken | 0,80% op cryptoparen; 0,20% op FX-, stablecoin- en pegged-token paren (TBTC/BTC, WBTC/BTC); 0,01% op USDG-paren; 0% op alle USDe-paren | GEZIEN, [kraken.com/pro/fees](https://www.kraken.com/pro/fees), 19 nov 2026: Tier 1 spot maker 0,40% taker 0,80%; "FX, stablecoin-base and pegged-token pairs" 0,20%; "USDG ($0+) Taker 0.01%"; "USDe (Any) Taker 0.00%, All USDe pairs". Staking-munten (LSETH/ETH, METH/ETH, CMETH/ETH) noemt de pagina niet: die rekenen we als crypto (0,80%, voorzichtig). De korting van 0,02% op 634 paren rekenen we niet mee (voorzichtig) |
| Bitvavo | 0,25% (categorie A, euro-paren) | GEZIEN, [support.bitvavo.com](https://support.bitvavo.com/hc/en-us/articles/4405175148689): "maximum fee of 0.25%" |
| Bitvavo | USDC- en stablecoinparen (categorie B, C, D in de API): hoog 0,25%, laag 0% | Bitvavo noemt ze lager, maar de tarievenpagina geeft ons geen getal (403). Rapport rekent met 0,25%; met 0% staat apart als bovengrens (GOK) |
| KuCoin | 0,1% x klasse x coëfficiënt uit de API | klasse en coëfficiënt GEZIEN (API), 0,1% per klasse GOK (zoals de scanner) |
| Gate, Bitget, MEXC | per paar uit de API | GEZIEN, zoals de scanner (`../scanner/README.md`) |
| OKX | 0,10% | DERDEN, [okx.com/en-eu/fees](https://www.okx.com/en-eu/fees), 19 nov 2026: tab Spot, Standard, munt EUR, "Regular user" takerFee 0,001. De pagina heeft ook een tab "Zero-fee pairs", maar de lijst staat niet in de pagina zelf; die 0%-paren rekenen we dus niet mee (te somber op die paren) |
| Bitstamp | 0,40%; FX- en stablecoinparen 0,08% | DERDEN, [tradingview.com/broker/Bitstamp](https://www.tradingview.com/broker/Bitstamp/): "0.40% - 0.03% Taker", "FX/Stablecoin pairs receive an 80% reduction", "Fee free if < $1,000" (30 dagen volume; dat laatste rekenen we niet mee, het geldt maar voor een paar driehoeken). De pagina van Bitstamp zelf blokkeert curl |

Coinbase doet niet mee: geen openbare bulk-koers met bod en laat (alleen de laatste prijs), en 1,20% taker (GOK)
maakt drie stappen 3,6%. Bybit en Binance antwoorden niet vanaf onze server.

## Grenzen van de openbare API's
Per beurs een eigen ritme, een maximum aantal orderboeken per ronde en een minimale tijd tussen twee verzoeken.
Bij een 429, 418 of 403 (te veel verzoeken) wacht die beurs 10 tot 120 seconden; de andere meten door.

| Beurs | Ritme | Boeken per ronde | Tussen verzoeken | Grens van de beurs (GOK, uit hun documentatie zoals wij die kennen, niet nagekeken) |
|---|---|---|---|---|
| Bitvavo | 4 s | 6 | 0,2 s | 1.000 gewicht per minuut per IP |
| Kraken | 5 s | 3 | 1,0 s | ±1 openbaar verzoek per seconde |
| OKX | 3 s | 10 | 0,1 s | 20 per 2 s (tickers), 40 per 2 s (boeken) |
| KuCoin | 3 s | 10 | 0,1 s | 2.000 gewicht per 30 s |
| Gate | 4 s | 8 | 0,1 s | 200 per 10 s per eindpunt |
| Bitget | 3 s | 10 | 0,1 s | 20 per seconde per eindpunt |
| MEXC | 3 s | 15 | 0,1 s | ruim boven ons gebruik |
| Bitstamp | 5 s | 6 | 0,2 s | 400 per seconde |

Of we eronder blijven, staat in het rapport (kolom "Fouten (te veel)", GEZIEN).

## Vergunning
Zelfde bron als de scanner: het MiCA-register van ESMA (19 nov 2026, zie `../scanner/README.md`). MiCA zelf:
Bitvavo, Kraken, Bitstamp. Via een EU-dochter: OKX, KuCoin, Gate. Grijs (niet in het register): Bitget, MEXC.

## Bestanden
| Bestand | Wat |
|---|---|
| `driehoek.py` | de meting: per beurs een draad, kandidaten zoeken, boeken ophalen, wegschrijven |
| `kosten.py` | takerkosten per paar met bron, minimale ordergrootte en stapgrootte uit de API, vergunning |
| `reken.py` | driehoeken zoeken, doorrekenen tegen de beste prijs en tegen het boek (met afronding) |
| `volgen.py` | een driehoek volgen en bevestigen (na 3 seconden nog €100 diepte) |
| `rapport.py` | het rapport uit de data |
| `opslaan.sh` | zet de data op de tak `ai-handel-data`, map `driehoek/` (nooit geforceerd) |
| `test_driehoek.py` | tests van de rekensom, de kosten, het volgen, het samenvoegen tot kansen en het rapport |
| `ontwerp.md` | waarom zo gebouwd |
| `../scanner/beurzen.py` | de koppelingen met de beurzen (hergebruikt van de scanner) |
