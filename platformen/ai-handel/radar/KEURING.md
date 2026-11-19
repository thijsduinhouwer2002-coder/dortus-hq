# Keuring kansenradar, 19 nov 2026, keurder (losse Claude)
Wat ik keurde: commit 2b36a6c1 op main (radar.py, perps.py, minima.py, radar_rapport.py, opslaan.sh, test_radar.py,
README.md, ontwerp.md), `.github/workflows/radar.yml`, de regel radar.yml in `organisatie/controle/opdracht.py`, en
de data en het rapport op de tak `ai-handel-data`, map `radar/` (stand 15:50 UTC, run 44557336325).
Akkoord: nee

Hoe ik keek: tests gedraaid (22 groen), data van de tak gelezen, drie momenten met de hand nagerekend, kosten en
minima met curl tegen de API en kraken.com/pro/fees, de runs van radar.yml bekeken (skill `actions`), en één fout
nagespeeld met een los script buiten de repo (niets aan de code veranderd).

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| A1 | **Handrekening B klopt.** MEXC EVAA: kosten 2 x (0,02% perp + 0,08% spot) = 0,20%, netto -0,20%, bij €500 is de positie €333, winst -€0,67. Kraken LQTY: 2 x (0,05% + 0,40%) = 0,90%, winst500 -€3,00. Hyperliquid SAGA: 2 x (0,045% + 0,05%) = 0,19%. Alle drie gelijk aan `funding.jsonl`. | Feit | hoog | |
| A2 | **Handrekening C2 klopt.** Bitfinex EURQ-EUR: laat 0,99233, koppeling 1,0, taker 0: afwijking 0,767%, winst100 = 100 x (1/0,99233 - 1) = €0,7729. Gelijk aan de data. | Feit | hoog | |
| A3 | **B telt alleen echt verrekende funding, 4 x taker en het prijsverschil spot/perp.** Code: `ontvangen` groeit alleen als `volgende` opschuift; `kosten = 2 x (taker_perp + taker_spot)`; `basis` met verhoudingen. Klopt met de opdracht. Velden van de API nagekeken: OKX `fundingTime` is het tijdstip van verrekening (`method: current_period`), KuCoin `nextFundingRateDateTime` is een echt tijdstip (geen aftelling), Gate `funding_next_apply` in seconden. | Feit | hoog | curl op de API's, 19 nov 15:55 UTC |
| A4 | **B: opnamekosten tellen niet mee.** De opdracht vraagt ze. In de data staat de spot vaak op een andere beurs dan de perp (Kraken- en Hyperliquid-perps met spot op MEXC, MEXC-perp met spot op BingX). Dan moet je geld op twee beurzen zetten: minstens één opname van een stablecoin (bij Kraken USDC 0,78 USDC, GEZIEN kraken.com/pro/fees). Bij €100 inleg (€67 positie) is dat ±1% extra, meer dan de hele piek meestal oplevert. | Feit | hoog | een kolom "overmaken" per piek als spot en perp niet op dezelfde beurs zitten |
| A5 | **B: een ontbrekende spotkoers gooit de piek weg.** In `funding_stap`: als het koersen-verzoek van de spotbeurs mislukt of het paar niet in de ticker staat, is `bod = laat = 0`, dan zegt `zelfde_ding(0, prijs)` nee en wordt de piek "spot_anders" (ander ding, niet geteld), met spot `None`. Nagespeeld met de nep-beurs uit de tests: lege koersen geeft `spot None, spot_anders True`. Een storing van één verzoek telt dus als "andere munt". | Feit | hoog | los script op de testklassen |
| A6 | **B: pieken worden bij elke nieuwe run doorgeknipt.** Een run duurt ±5,5 uur en een push in de radar-map start hem ook opnieuw. Elke open piek sluit dan (`einde_run`) en opent opnieuw (`al_bij_start`), en elk stuk betaalt opnieuw 4 x taker. In de data: alle 27 positieve pieken `einde_run`, 25 `al_bij_start`. Ze tellen gewoon mee in "Som gemeten" en "Per week". Een piek van een dag betaalt zo 4 keer de kosten: B komt te slecht uit. | Feit | hoog | open pieken bewaren op de datatak (zoals `paren-laatst.json`) of doorgeknipte pieken apart zetten |
| A7 | **C2: duidelijk dat het geen arbitrage is.** README, rapport en code zeggen het ("je wint alleen als de koers terugkomt", met USDC 2023 en UST 2022). | Feit | hoog | |
| A8 | **C2: EURQ staat structureel onder de euro en telt toch als kans.** Kraken EURQ/EUR per dag (OHLC-API, laatste 45 dagen): mediaan van het slot 0,968, laagste 0,951; alleen 11 tot 13 okt rond of boven 1,00 (met 2 tot 3.006 EURQ handel), daarna steeds onder 0,99. Mediane handel 300 EURQ per dag. In het rapport staan alle 4 "C2 met winst na kosten" op naam van EURQ (Bitfinex en Kraken). Het rapport zegt nergens dat EURQ niet terugkomt; de winst per keer veronderstelt verkopen op €1,00. | Feit | hoog | curl `api.kraken.com/0/public/OHLC?pair=EURQEUR&interval=1440` |
| A9 | **Sommen per week: alsof je met €100 alle momenten tegelijk pakt.** `tabel_inleg` telt de winst van elk moment op. Bij B stonden er 27 pieken tegelijk open; met €100 heb je er maar één. "Per week bij €100" wordt dan gelezen als "dit verdien ik met €100", maar het vraagt in het echt 27 x €100. De README noemt de som een bovengrens om de snelheid, niet om het geld dat tegelijk vastzit. | Feit | hoog | per inleg alleen tellen wat met dat geld tegelijk kan (bijv. een moment pas meetellen als het vorige gesloten is), of het benodigde geld ernaast zetten |
| A10 | **Kraken-taker: de lopende meting rekent nog met 0,40%.** De fix in `scanner/beurzen.py` (b335b992: 0,80%, en 0,20% op stablecoin- en FX-paren, GEZIEN kraken.com/pro/fees: "FX, stablecoin-base and pegged-token pairs" tier 1 0,20%/0,20%) zit niet in de lopende run 44558559812 (gestart 15:46 op 2b36a6c1). De klok kijkt alleen naar `platformen/ai-handel/radar/**` en `radar.yml`, niet naar de scannerbestanden die de radar importeert, dus de fix startte de radar niet opnieuw. Gevolg in de data: Kraken-spot bij B te goedkoop (LQTY, GOAT: 0,004 i.p.v. 0,008), Kraken-stablecoins bij C1 en C2 te duur (0,004 i.p.v. 0,002). De velden `taker_spot`, `taker_koop`, `taker` staan wel in elke regel, dus herrekenen kan. Let op: deze keuring staat in de radar-map en start de radar dus opnieuw, vanaf dan met 0,80%. | Feit | hoog | runs van radar.yml (klok bij b335b992 zei nee, meet overgeslagen) |
| A11 | **Minima kloppen met de API.** Kraken EURQ/EUR `ordermin` 4 x laat 0,9885 = €3,954 (data: 3,954); Bitvavo BTC-EUR `minOrderInQuoteAsset` 5,00; MEXC FDUSDUSDT `quoteAmountPrecision` 1 USDT = €0,91 (data: 0,9096) en `takerCommission` 0,002 (data: 0,002); Bitfinex EURQ:EUR minimum 0,001 (data: 0,001). | Feit | hoog | curl 19 nov |
| A12 | **Perp-takers bij de API nagekeken.** MEXC 0,02%, Bitget 0,06%, KuCoin 0,06%, BingX 0,05% gelijk aan `TAKER_PERP` (GEZIEN, veld `takerFeeRate` in hun contract-API). Kraken Futures 0,05% gelijk (GEZIEN kraken.com/pro/fees, tier 1). **Gate geeft 0,075%** (`taker_fee_rate`), de radar rekent 0,05%. OKX, Hyperliquid, dYdX niet nagekeken, terecht GOK. | Feit | hoog | |
| A13 | **Perps voor Nederlanders: als GOK gemerkt, maar voor Kraken nu na te gaan.** support.kraken.com ("Changes to Derivatives offerings for EEA clients", bijgewerkt 3 juli 2025): Kraken biedt futures aan EER-klanten via een MiFID II-vergunning op Cyprus (CySEC), met een geschiktheidsvragenlijst. Of dat dezelfde perps zijn als de `PF_`-markten die de radar meet, zag ik niet. Voor OKX, Gate, KuCoin, BingX niets nagekeken: blijft GOK. | Feit (Kraken), GOK (rest) | midden | |
| A14 | **API-grenzen.** Per beurs elke 15 s één ticker en hooguit 4 boeken: bij Kraken ±20 verzoeken per minuut, onder ±1 per seconde. In beide runs `fouten: {}` en 24 boeken per ronde (639 in 26 rondes). Alleen bij veel nieuwe noteringen tegelijk kan Kraken een uitbarsting van tot 12 boeken tegelijk krijgen (Kraken staat vooraan in `elders`). | Feit (tellingen), vermoeden (uitbarsting) | midden | een run met veel noteringen |
| A15 | **Workflow veilig.** Schrijft alleen naar `ai-handel-data`, map `radar/`; verse clone per poging, gewone push, nooit geforceerd; main blijft schoon; alleen `GITHUB_TOKEN` (contents: write), geen eigen sleutels. Invoer `minuten` via `env:` en in de shell op cijfers gecontroleerd. De afgebroken run 44557336325 bewaarde netjes zijn data (stap Opslaan OK na STOP). Regel in `opdracht.py` heeft een reden. | Feit | hoog | |
| A16 | **Rapport voor Thijs.** De uitleg is eerlijk, maar een antwoord staat er niet: geen zin bovenaan als "A: nog niets gezien; B: 0 van 27 pieken met winst; C: alleen EURQ, en die komt niet terug". In de tabel van B staat `None%` bij prijsverschil, "0.2 uur" met een punt, en jargon (r8, "Max per 8u", "Verrekend 0.0% (0x)"). Thijs leest nu tabellen vol nullen en een "Per week" die hij als belofte kan lezen. | Feit | hoog | |
| A17 | **Tests controleren echte sommen** (handgetallen voor winst, funding, kosten, basis, haalbaarheid, proefruns). Ze missen: basis die niet 0 is, ontbrekende spotkoers (A5), een munt die structureel naast zijn koppeling staat (A8) en de Kraken-taker. | Feit | hoog | |
| A18 | dYdX `nextFundingRate` (0,0000000022) is veel kleiner dan de laatste verrekende rate uit `historicalFunding` (0,0000046 per uur). Mogelijk een lopend gemiddelde, niet de rate die betaald wordt. | Vermoeden | laag | dYdX-documentatie of een paar uur vergelijken |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| B1 | Tests niet aangepast om te slagen; 22 groen in deze map zonder internet. | Feit | hoog | tests groen |
| B2 | `radar.py` heeft 713 regels. | Feit | hoog | bestanden onder ±400 regels |
| B3 | GEZIEN en GOK staan bij cijfers in README en rapport. Perp-takers en "perps voor NL" als GOK, terecht waar niet nagekeken. Kraken Futures-taker en de Kraken-EER-regeling zijn nu GEZIEN (A12, A13). README zegt bij Kraken "minimale opname niet openbaar", maar kraken.com/pro/fees toont ze (USDC min. 0,9354). | Feit | hoog | eerlijk |
| B4 | Geen persoonsgegevens; `check.py` zegt OK. | Feit | hoog | openbare repo |
| B5 | README zegt dat runs "op elkaar aansluiten, met een paar minuten ertussen"; met klok 6 uur en runs van 5 uur 25 is het ±35 minuten per 6 uur (meer als GitHub een geplande run laat vallen). | Feit | midden | eerlijk |
| B6 | Elke wijziging aan een tekst in de radar-map (README, deze keuring) breekt de meting af en knipt alle pieken door (A6). | Feit | hoog | |

## Moet (blokkeert akkoord)
1. **B: ontbrekende spotkoers is geen "ander ding"** (A5). Alleen `spot_anders` als er een echte spotprijs is die niet past; zonder koers de spot houden en later instappen (zoals bij een open piek al gebeurt). Met een test.
2. **B: kosten van overmaken meetellen** als spot en perp op verschillende beurzen zitten (A4): minstens één opname van een stablecoin uit de wallet-data, als vast bedrag per keer (weegt bij €100 zwaar).
3. **B: doorgeknipte pieken niet dubbel laten betalen** (A6): open pieken meegeven aan de volgende run via de datatak, of pieken met `einde_run`/`al_bij_start` buiten de som houden en apart tonen.
4. **C2: EURQ (en elke munt die structureel naast zijn koppeling staat) is geen kans** (A8). Bijv. vergelijken met de eigen mediaan van de laatste dagen, of die munten apart zetten met de zin "staat al weken onder €1, komt niet vanzelf terug". Uit de som halen.
5. **Sommen per inleg eerlijk maken voor geld dat vastzit** (A9): bij €100 tot €200 alleen tellen wat met dat geld tegelijk kan, of naast elke som zetten hoeveel geld er tegelijk nodig was.
6. **Kraken-taker** (A10): klok ook laten kijken naar `platformen/ai-handel/scanner/beurzen.py` en `scanner.py`; data van vóór de fix (taker 0,004 bij Kraken) in het rapport herrekenen of apart zetten.
7. **Rapport: bovenaan per hoek één zin in gewone woorden** met het antwoord tot nu toe (hoeveel echte momenten, wat het bij €100 na alle kosten deed, GOK erbij), en geen `None%` of punt als decimaalteken (A16).

## Kan (mag later)
- Perp-takers uit de API lezen waar die het geeft (Gate 0,075% i.p.v. 0,05%; MEXC, Bitget, KuCoin, BingX geven het ook) (A12).
- README: Kraken Futures-taker en Kraken-futures voor EER-klanten als GEZIEN met bron; Kraken-minima voor opname staan op kraken.com/pro/fees (A13, B3).
- `STABIEL_FIAT` in de scanner mist EURQ, EURR, RLUSD, USDQ en andere; Kraken rekent 0,20% op "stablecoin-base pairs". Melden bij de eigenaar van de scanner.
- Klok alleen laten starten op `*.py`, `*.sh` en `radar.yml`, niet op teksten (B6).
- `radar.py` splitsen na de meetweek (B2).
- Risico van 2x hefboom bij B noemen (een sprong van ±50% liquideert de short).
- Tests bij voor A5, A8, basis niet 0 en de Kraken-taker (A17).
- C2 telt "met winst" op het maximum maar de winst uit de eerste meting; één van de twee kiezen.
- Gat tussen runs eerlijk beschrijven (B5); dYdX-rate nakijken (A18).

akkoord nee: moet 1 t/m 7 (B: spotkoers, overmaken, doorknippen; C2: EURQ; sommen per inleg; Kraken-taker en klok; samenvatting voor Thijs)
