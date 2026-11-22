# Keuring driehoek-meter, 19 nov 2026, keurder (losse Claude, niet de bouwer)
Wat ik keurde: commit c0ad6ec9 op main (`driehoek.py`, `rapport.py`, `opslaan.sh`, `test_driehoek.py`, `README.md`,
`ontwerp.md`, `.github/workflows/driehoek.yml`, regel `driehoek.yml` in `organisatie/controle/opdracht.py`); data
op de tak `ai-handel-data`, map `driehoek/` (proefrun 44555682966, rapport.md); runs van de workflow tot 15:53 UTC.
Akkoord: **nee**. De rekensom klopt tot op de cent in beide richtingen, de workflow is veilig en de kosten van
Kraken (crypto), Bitvavo en OKX kloppen. Het nee komt door drie punten die het antwoord voor Thijs te mooi maken
(echt en opschaling) of op Kraken juist te somber (kosten van een paar stablecoinparen), plus een rapport zonder
kort antwoord bovenaan. Alle vier zijn klein om te maken (zie "Moet").

Geen beleggingsadvies. Ik keur alleen of de meting klopt en eerlijk gebracht is.

## Deel A: doet het wat beloofd is?
(getoetst tegen `ontwerp.md`, `README.md` en de opdracht: kosten, rekensom, echt, opschaling, workflow, tests)

| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| A1 | **Kraken klopt voor crypto en de meeste FX- en stablecoinparen.** Met curl op kraken.com/pro/fees (19 nov, 15:50 UTC): Tier 1 spot maker 0,40% taker 0,80%; "Symmetric maker and taker fees for FX, stablecoin-base and pegged-token pairs": tier 1 0,20%. Korting van 0,02% op 634 paren: bestaat, de meter rekent hem niet mee (voorzichtig, staat in de README). | feit | hoog | |
| A2 | **Kraken: drie soorten paren te duur gerekend.** Dezelfde pagina: USDG-paren taker 0,01%, **alle USDe-paren 0,00%**, en pegged-token paren (voorbeeld TBTC/BTC; ook WBTC/XBT staat in de API) 0,20%. `kosten()` geeft USDE/USDG-paren 0,20% en TBTC/XBT en WBTC/XBT 0,80%. Op Kraken zitten 18 driehoeken (beide richtingen) met USDE of USDG (zelf geteld uit AssetPairs), zoals EUR>USDE>USDT>EUR: echt 0% + 0% + 0,20% = 0,20%, de meter rekent 0,60%. Juist stablecoin-driehoeken zijn waar kleine winst kan zitten; die mist de meter nu. Het label "GEZIEN ... FX en stablecoin 0,20%" klopt voor die paren niet. | feit | hoog | |
| A3 | **Bitvavo 0,25% klopt.** Tarievenpagina en supportpagina geven ook mij 403, maar de Zendesk-API van dezelfde pagina (`support.bitvavo.com/api/v2/help_center/en-us/articles/4405175148689.json`, bijgewerkt 24 okt 2026) zegt: "we reserve the maximum fee of 0.25%" en "Trading pairs involving USDC typically have lower fees". Categorieën uit de API: A 419 EUR-paren, B 10 USDC-paren, C 5, D 1 (GEZIEN). Hoog 0,25% en laag 0% voor B, C, D is een eerlijke aanpak. Ook uit die pagina: Bitvavo rondt kosten **naar boven** af op de cent; bij €100 en drie stappen tot €0,03 extra. | feit | hoog | |
| A4 | **OKX 0,10% kan van GOK naar DERDEN.** `okx.com/en-eu/fees` (curl, 19 nov) heeft de tabel als data in de pagina: tab "Spot", "Standard", munt EUR, "Regular user" makerFee 0.0008, takerFee 0.001. Er is ook een tab "Zero-fee pairs" (paren met 0%); die rekent de meter niet mee (te somber op die paren). | feit | midden (de pagina toonde ook een banner voor de VS; de data zelf is de EU-tabel in euro) | de lijst "Zero-fee pairs" ophalen |
| A5 | **Bitstamp 0,40% niet officieel te bevestigen.** De officiële pagina blokkeert curl (Incapsula). Derden: [TradingView](https://www.tradingview.com/broker/Bitstamp/): taker van "0.40%" tot "0.03%", "FX/Stablecoin pairs receive an 80% reduction", "Fee free if < $1,000" (30 dagen volume). 0,40% klopt dus als laagste trede (DERDEN), maar FX- en stablecoinparen zijn dan 0,08%, niet 0,40%. Voorzichtig, maar te somber op die paren. | feit (wat TradingView zegt), juistheid vermoeden | midden | de pagina van Bitstamp in een browser |
| A6 | **Rekensom met de hand nagerekend, beide richtingen.** Kraken live (15:49 UTC): BTC/EUR bod 57.161,9 laat 57.178,4; ETH/BTC 0,028204 / 0,028217; ETH/EUR 1.612,64 / 1.613,22. EUR>BTC>ETH>EUR = (1/57.178,4) x (1/0,028217) x 1.612,64 x 0,992³ = 0,975730 (min 2,427%); EUR>ETH>BTC>EUR = (1/1.613,22) x 0,028204 x 57.161,9 x 0,992³ = 0,975571 (min 2,443%). `top()` geeft precies dezelfde getallen; koop en verkoop staan per stap goed (koop tegen de laat, verkoop tegen het bod). Op de echte boeken met €100: mijn som 97,571600, `rondje()` 97,57160 en past=True. Zonder kosten verliezen beide richtingen al 0,05 en 0,06%. | feit | hoog | |
| A7 | **Orderboek en minimum goed meegenomen.** `loop` loopt de lagen af en geeft None als het opgehaalde boek op is (diepte is dan een ondergrens, staat in ontwerp.md). Minimum per stap op munten en quote-bedrag, uit de API van alle 8 beurzen (proef: minima voor alle paren, bijv. Kraken 1352 van 1352). Bitstamp-formaat "10.00 USD" en Kraken `ordermin`/`costmin` zelf bekeken: worden goed gelezen. Kosten als factor na elke stap: gelijk aan hoe beurzen het in de quote of de munt afhouden, op afronding na. | feit | hoog | |
| A8 | **Afronding op de stapgrootte niet meegenomen** (staat eerlijk als GOK in README en rapport, "een paar cent bij €100"). Maar de enige winst uit de proef was €0,02 op MEXC USDT>BTC>BDX>USDT, en BDXBTC handelt volgens de MEXC-API alleen in hele BDX (`baseAssetPrecision` 0). Bij winsten van centen kan afronding (en de opronding van Bitvavo, A3) de hele winst opeten. "Echt" heeft geen ondergrens voor de winst; €0,0001 telt ook. | feit | hoog | |
| A9 | **"Echt" eist diepte en duur niet tegelijk.** De diepte is de hoogste over alle metingen en de duur loopt van eerste tot laatste meting met winst. Zelf nagespeeld met `Meter.verwerk`: meting 1 €75.000 diepte, meting 2 (4 s later) nog maar €19,53 diepte, meting 3 geen winst: `echt()` = True, met diepte €75.231 en winst €1.274. Wie na 3 seconden komt (en dat zijn wij op zijn best), kan er dan nog €20 doorheen halen, geen €100. De README belooft "minstens €100 diepte" en "minstens 3 seconden blijven staan" als één eis. | feit | hoog | |
| A10 | **Opschaling neemt het beste moment.** `winst_bij` is de hoogste winst over alle metingen, dus meestal de eerste keer dat hij gezien werd. Dat is juist het moment dat een trage speler mist. Het rapport schrijft wel "op het beste moment", maar telt het daarna toch op als wat je had kunnen pakken. | feit | hoog | |
| A11 | **Opschaling telt dezelfde kans meerdere keren.** Eén scheve prijs op een altcoin/BTC-paar zit op Kraken in mediaan 8 driehoeken (4 per richting: via EUR, USD, USDT, USDC; zelf geteld). Gaat die prijs scheef, dan opent de meter tot 4 echte driehoeken tegelijk die **hetzelfde stukje boek** willen hebben, en het rapport telt hun winst bij elkaar op (ook "echte driehoeken per dag"). Je kunt dat boek maar één keer leeghalen. Het woord "bovengrens" dekt dit niet; de som kan zo een paar keer te hoog uitvallen. | feit (geen ontdubbeling in de code), grootte vermoeden | hoog (werking), midden (grootte) | per dag het aantal unieke (beurs, paar, moment) naast het aantal driehoeken |
| A12 | **GOK goed gemerkt.** De kop "Opschaling ... (GOK)", de kolom "Per maand (GOK)", de lijst "Waarom dit te rooskleurig is" en bovenaan "Lees dit eerst" met de waarschuwing dat snelle bots in milliseconden werken en dat wij zien wat er overbleef. Ook in README en ontwerp.md. Goed. | feit | hoog | |
| A13 | **5% verdacht, MiCA en grijs apart:** in trechter, per dag, opschaling en kleine inleg. Status per beurs komt uit dezelfde bron als de scanner. Goed. | feit | hoog | |
| A14 | **Workflow veilig.** Geen sleutel nodig (alleen `GITHUB_TOKEN` voor de eigen repo, openbare API's). `opslaan.sh` pusht alleen naar `refs/heads/ai-handel-data` met een gewone push, haalt bij weigering vers op en probeert 5 keer; nooit `--force`. Main blijft schoon: de meter schrijft daar niets. Invoer `minuten` gaat via `env:` en wordt op cijfers gecontroleerd en op 325 begrensd. Proefrun in een eigen concurrency-groep, raakt de vaste run niet. Na `EINDE` (27 nov) slaat de klok het meten over. Regel in `opdracht.py` heeft een reden en klopt. | feit | hoog | |
| A15 | **API-grenzen:** per beurs een minimale tijd tussen verzoeken, een boekenbudget per ronde en terugval van 10 tot 120 s bij 429/418/403. Proef van 10 minuten op een GitHub-runner: 0 fouten, 0 keer "te veel", alle 8 beurzen (GEZIEN, samenvatting.json). De grenzen in de README-tabel zijn GOK (niet nagekeken), dat staat er eerlijk bij. | feit | hoog (voor 10 minuten) | de kolom "Fouten (te veel)" na de eerste vaste run |
| A16 | **Laatste runs (skill `actions`, 15:53 UTC):** vaste run 44558290940 loopt sinds 15:44:56 (push c0ad6ec9), stap "Meten" bezig. Run 44558227937 (push 6852aeab) is na ±20 s afgebroken door de push van c0ad6ec9 (cancel-in-progress); de opslaan-stap liep wel, maar er kwam niets op de tak (vermoedelijk nog geen bestanden). Latere pushes (15:45 tot 15:49) sloegen de meetjob over: de klok werkt. Let op: elke push in `onderzoek/ai-handel/driehoek/` start de vaste run opnieuw, ook een push met alleen tekst, **ook deze keuring**. | feit | hoog | |
| A17 | **Tests:** 19 groen, zelf gedraaid (`python3 -m unittest test_driehoek`). Ze controleren echt iets: lagen aflopen, te dun boek, beide richtingen, kant per stap, kosten eten winst, diepte stopt waar het boek duurder wordt, boek nooit beter dan de beste prijs, minimum in munten en in quote, Kraken- en Bitvavo-kosten, openen en sluiten van een driehoek met duur, `echt()`, MiCA/grijs en dat proefruns niet meetellen. Sinds de eerste commit niet aangepast. Niet gedekt: A9, A11, de minima-lezers per beurs en de USDe/USDG-kosten. | feit | hoog | |
| A18 | **Rapport op de tak is nu leeg** (0 uur, 0 driehoeken), omdat alleen de proefrun er staat en die niet meetelt. Klopt met de opzet; eerste echte cijfers na de eerste tussentijdse opslag van de vaste run. | feit | hoog | |

## Deel B: houdt het zich aan onze regels?

| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| B1 | `driehoek.py` heeft 619 regels, ruim boven de ±400. `rapport.py` 274, `test_driehoek.py` 196. | feit | hoog | bouwen.md 4 |
| B2 | Geen persoonsgegevens of sleutels; `check.py` OK. Geen geld, geen account, geen handel. | feit | hoog | harde regels 1, 2 |
| B3 | Cijfers in README met GEZIEN, DERDEN of GOK; Kraken staat als GEZIEN maar klopt niet voor USDe, USDG en pegged-token paren (A2). OKX kan DERDEN worden (A4); Bitstamp DERDEN via TradingView met de korting op FX en stablecoins (A5). | feit | hoog | harde regel 5 |
| B4 | `ontwerp.md` spreekt zichzelf tegen: bij "Keuzes" staat dat de minimale ordergrootte uit de API meetelt, bij "Bekende grenzen" dat die niet meetelt. De code telt hem wel mee. | feit | hoog | eerlijk, architectuur bijgewerkt |
| B5 | Tests niet aangepast om te slagen; workflow pusht nooit geforceerd. | feit | hoog | harde regel 6 |

## Deel C: snapt Thijs het rapport?
- **Goed:** gewone Nederlandse zinnen, "Lees dit eerst" staat bovenaan, elke tabel heeft een uitleg, bedragen in euro met komma, GOK staat erbij. De trechter laat stap voor stap zien waar het afvalt; dat is helder.
- **Niet goed:** er staat nergens in één zin het antwoord op zijn vraag ("kan ik hiermee met €100 tot €200 geld verdienen?"). Het eerste wat hij ziet na de uitleg is een tabel met 15 kolommen vol vaktaal (kandidaten, bekeken, overgeslagen, zelfde, beste marge). Woorden als takerkosten, diepte, bulk-ticker, quote en orderboek worden niet uitgelegd of staan pas verderop. Thijs moet dus zelf drie tabellen combineren om tot "ja" of "nee" te komen.
- **Klein:** onder "Waarom dit te rooskleurig is" mist een lege regel voor "Waarom het te somber kan zijn", waardoor die zin in Markdown aan het laatste opsommingspunt plakt.

## Moet (blokkeert akkoord)
1. **Echt = diepte en duur tegelijk** (A9, A10). Tel een driehoek pas als echt als hij op minstens twee metingen die minstens 3 s uit elkaar liggen elk minstens €100 diepte met winst had. Gebruik voor de opschaling (en de winst per dag) de winst die er bij de latere meting nog stond (of de laagste van die metingen), niet het beste moment. Met een test zoals het voorbeeld in A9.
2. **Dezelfde kans niet meerdere keren optellen** (A11). Driehoeken op dezelfde beurs die tegelijk open stonden en een paar delen, tellen in de opschaling en in "echte driehoeken per dag" als één kans (neem de beste). Of zet het aantal unieke kansen ernaast en reken de som daarmee. Met een test.
3. **Kraken-kosten voor USDe (0%), USDG (0,01%) en pegged-token paren zoals TBTC/XBT en WBTC/XBT (0,20%)** zoals op kraken.com/pro/fees (A2), met test, en de README-tabel bijwerken.
4. **Kort antwoord bovenaan het rapport** (Deel C): één alinea in gewone woorden vóór alle tabellen, bijvoorbeeld "Tot nu toe: X echte driehoeken op vergunde beurzen, met €100 samen ±€Y per maand (GOK). Op de grijze beurzen: ...". Zolang er niets is: "Nog geen enkele driehoek die je met €100 had kunnen pakken." Leg daar ook in één zin uit wat takerkosten en diepte zijn.

## Kan (mag later)
1. Een ondergrens voor de winst bij "echt" (bijvoorbeeld €0,05 per keer bij €100), of afronding op de stapgrootte uit de API meerekenen (Kraken `lot_decimals`, MEXC `baseAssetPrecision`, OKX `lotSz`), plus de opronding naar de cent van Bitvavo (A3, A8).
2. Bitstamp FX- en stablecoinparen op 0,08% (80% korting, DERDEN TradingView) en de "Zero-fee pairs" van OKX meenemen; OKX in de README naar DERDEN met de bron uit A4 (A4, A5).
3. `ontwerp.md` "Bekende grenzen" gelijktrekken met de code (B4).
4. `driehoek.py` opsplitsen, bijvoorbeeld `kosten()` en `minima()` naar een eigen bestand (B1).
5. In `klok.py --paden` alleen de code meenemen (`*.py`, `opslaan.sh`, de workflow), zodat een push met alleen tekst (README, KEURING.md) de lopende vaste run niet afbreekt (A16).
6. Lege regel in het rapport voor "Waarom het te somber kan zijn" (Deel C).
7. Tests voor de minima-lezers per beurs (Bitstamp "10.00 USD", MEXC-velden).

akkoord nee: moet 1 (echt = diepte en duur tegelijk, opschaling niet op het beste moment), moet 2 (dezelfde kans niet dubbel tellen), moet 3 (Kraken-kosten USDe, USDG, pegged-token paren), moet 4 (kort antwoord bovenaan het rapport)

## Herkeuring, 19 nov 2026 ±16:15 UTC, keurder (dezelfde losse Claude, niet de bouwer)
Wat ik keurde: commit ee5dcf62 op main (`kosten.py`, `reken.py`, `volgen.py`, `driehoek.py`, `rapport.py`,
`test_driehoek.py`, README, ontwerp, workflow); data op `ai-handel-data` tot commit fb8a67b2 (16:07 UTC); een eigen
lokale run van 50 s met stopsignaal.
Akkoord: **nee**, nog één moet-punt: het samenvoegen tot één kans is te ruim. De rest is goed opgelost.

| # | Punt | Uitkomst | Feit of vermoeden | Zekerheid |
|---|---|---|---|---|
| H1 | Moet 1: na_3s | **Opgelost.** Mijn voorbeeld nagespeeld met `Meter.verwerk`: €75.231 diepte, 4 s later €19,53: `na_3s` = None, niet echt. Zelfde met 4 s later €200 diepte: echt, met de winst van de latere meting (€3,39, niet de €1.274 van het beste moment) en `winst_bij` van die meting. Onderbroken reeks (€75.000, €19, €75.000, €75.000) telt pas vanaf de herstart. Twee metingen 2 s uit elkaar: niet echt. Ondergrens €0,05 staat in `echt()` met test. | feit | hoog |
| H2 | Moet 2: dubbel tellen | **Dubbel tellen is weg** (zelfde scheve X/BTC via EUR en via USDT wordt één kans; test). **Maar het samenvoegen is te ruim**, zie H3. | feit | hoog |
| H3 | Samenvoegen te ruim | `kansen()` voegt samen bij zelfde beurs, overlappende **hele open-tijd** en **elk** gedeeld paar, en doet dat als ketting (A met B, B met C, dan ook A met C). Zelf nagespeeld: (a) EUR>BTC>X en EUR>BTC>Y, twee losse scheve paren die alleen het diepe BTC/EUR delen: één kans; (b) ketting via USDT/EUR: drie driehoeken zonder gezamenlijk paar worden één kans; (c) een driehoek die 2 uur open staat, voegt twee kansen samen die 80 minuten uit elkaar liggen. Dit speelt echt: in de data van vandaag delen USDT>BTC>BDX>USDT (15 keer) en USDT>BTC>SOL>USDT (13 keer) op MEXC alleen BTCUSDT, en driehoeken staan daar tot 357 s open. Gevolg: aantallen en geld in kort antwoord en opschaling kunnen te laag uitvallen, juist op drukke momenten. | feit (werking en data), grootte vermoeden | hoog / midden |
| H4 | Moet 3: kosten | **Opgelost.** Kraken USDe 0%, USDG 0,01%, TBTC/WBTC-BTC 0,20% (in mijn lokale run: 4, 3 en 2 paren met die tarieven, GEZIEN in `beurs-kraken.json`). Bitstamp 0,08% op FX en stablecoins, OKX 0,10% als DERDEN met bron, 0%-paren van OKX als "te somber" gemeld. Mijn lokale run gaf Kraken beste marge mediaan -0,205%, gelijk aan de -0,21% in de README. | feit | hoog |
| H5 | Afronden op de stapgrootte | **Klopt.** Velden bestaan in de API (Bitvavo `quantityDecimals` bij 435 van 435, Kraken `lot_decimals`, Gate `amount_precision`, Bitget `quantityPrecision`, Bitstamp `base_decimals`; curl 19 nov). Met de hand nagerekend: €123, BTC-stap 0,0001, ETH-stap 0,01, 0,1% per stap: terug €76,4235, deel 0,610977, winst €1,2733; `rondje()` geeft precies hetzelfde. Wat door afronden blijft liggen, telt tegen kostprijs (geen winst of verlies); dat is redelijk, de kosten om dat restje later te verkopen tellen niet mee (klein). Bitvavo €0,01 per euro-order voor de opronding: ok. | feit | hoog |
| H6 | Moet 4: kort antwoord | **Opgelost.** Staat vóór alle tabellen, in gewone woorden, met uitleg van takerkosten en diepte en de waarschuwing over bots. Ik draaide het nieuwe `rapport.py` op de data van de tak (16:07): "nog geen enkele driehoek die je met €100 tot €200 had kunnen pakken", vergund mediaan -0,28%, grijs +0,03%. Klopt met de data: 47 driehoeken met winst, alle op MEXC, maar één ooit €100 diepte en die stond korter dan 3 s. Het `rapport.md` op de tak is nog van de oude code (gemaakt door de afgebroken run om 16:07); het nieuwe verschijnt bij de eerste opslag van run 44562420725 (±16:37). | feit | hoog |
| H7 | Paths-filter en beurzen.py | Het filter is nu `driehoek/*.py, driehoek/opslaan.sh, workflow`. **`scanner/beurzen.py` staat er niet in** (stond er ook vóór de keuring niet in, toen was het `driehoek/**`). Een wijziging daar komt pas bij de volgende vaste run (hooguit 6 uur later). beurzen.py veranderde vandaag 3 keer; meenemen zou dus vaker herstarten. Geen moet, wel een keuze die er moet staan (kan 2). | feit | hoog |
| H8 | Afgebroken run | **Schrijft zijn data weg.** Lokaal: na SIGTERM stopte de meter in 1,8 s, met `stand.jsonl`, `beurzen.json` en `samenvatting.json`. Op de tak staan van alle drie de afgebroken runs (44558227937, 44558290940, 44560155433) `samenvatting.json` en `driehoeken.jsonl` (met reden "stop" waar nodig). Correctie op A16: ook de eerste afgebroken run kwam wel op de tak, alleen later dan ik keek. | feit | hoog |
| H9 | Push met alleen KEURING.md | `KEURING.md` past niet op `*.py`, `opslaan.sh` of de workflow, dus de klok hoort "niet aan de beurt" te zeggen. Uitslag na de push van deze herkeuring: zie "Na de push" onderaan. | zie onder | |
| H10 | Tests | driehoek 29, scanner 31, radar 22: alle groen (zelf gedraaid). Oude tests zijn naar de nieuwe bestanden verhuisd met dezelfde verwachtingen; geen test zwakker gemaakt om te slagen. Nieuw: na_3s, `bevestigd`, €0,05, afronden, Bitvavo-cent, kosten per soort paar, Bitstamp-minimum, samenvoegen, kort antwoord bovenaan. Niet gedekt: H3 (te ruim samenvoegen). | feit | hoog |
| H11 | Regels | Alle bestanden onder 400 regels (grootste `rapport.py` 358). `check.py` OK. ontwerp.md spreekt zichzelf niet meer tegen. | feit | hoog |

### Moet (blokkeert akkoord)
1. **Samenvoegen niet te ruim** (H3). Voeg alleen samen wat echt hetzelfde stukje boek wil: (a) gebruik voor "tegelijk" de bevestigde tijd (rond `na_3s`), niet de hele open-tijd; (b) geen ketting via verschillende paren; (c) tel een gedeeld paar van twee hoofdmunten (EUR, USD, USDT, USDC, BTC, ETH, zoals BTCUSDT of BTC/EUR) niet als reden om samen te voegen. Of, als dat te veel is: zet in kort antwoord en opschaling beide getallen, los (bovengrens) en samengevoegd (ondergrens). Met een test zoals (a), (b) of (c) in H3.

### Kan (mag later)
1. Oude regels op de tak (van vóór ee5dcf62) hebben geen `na_3s` en tellen daardoor nooit als echt. Voor de data van vandaag maakt het niets uit (geen enkele haalde 3 s met €100), maar zet in het rapport dat runs van vóór 19 nov 16:07 UTC zo meetellen.
2. Kies bewust of `onderzoek/ai-handel/scanner/beurzen.py` in het paths-filter hoort (H7), en zet de keuze in de workflow.
3. `USDGO` op Kraken telt als crypto (0,80%); waarschijnlijk een stablecoin (0,20%). Voorzichtig, klein.

### Na de push
H9 nagekeken (skill `actions`, 16:17 UTC): run 44563925310 voor de push van deze herkeuring (c3336d63, alleen KEURING.md): job klok OK, job meet **overgeslagen**; de vaste run 44562420725 (ee5dcf62) loopt door. Een push met alleen tekst herstart de meting dus niet meer (GEZIEN).

akkoord nee: moet 1 (samenvoegen tot één kans te ruim: open-tijd, ketting, gedeeld hoofdpaar)

## Tweede herkeuring, 19 nov 2026 ±16:40 UTC, keurder (dezelfde losse Claude, niet de bouwer)
Wat ik keurde: commit 5ad279ea op main (`kans.py`, `rapport.py`, `kosten.py`, `test_driehoek.py`, workflow,
README, ontwerp); data op `ai-handel-data` tot 3ebeb2ed (16:30 UTC), waaronder de afgebroken run 44562420725 en
een eigen proefrun van 3 minuten (44566193252, via opdrachtbestand) met deze code.
Akkoord: **ja**. Het moet-punt over samenvoegen is opgelost en de kan-punten zijn verwerkt.

| # | Punt | Uitkomst | Feit of vermoeden | Zekerheid |
|---|---|---|---|---|
| T1 | Geval (a): alleen BTC/EUR gedeeld | EUR>BTC>X en EUR>BTC>Y tegelijk: **2 kansen** (nagespeeld met `kans.kansen`). Paren van twee hoofdmunten tellen niet mee als reden. | feit | hoog |
| T2 | Geval (b): ketting | EUR>BTC>X, EUR>USDT>X, EUR>USDT>Z: 2 kansen (de eerste twee delen X/EUR, terecht samen; Z apart). Ketting met alt-paren (EUR>X>Y, EUR>Y>Z, EUR>Z>W): 2 kansen, nooit A en C samen. Een driehoek komt alleen in een groep als hij met elk lid samen mag. | feit | hoog |
| T3 | Geval (c): lange open-tijd | Tijd is nu het moment van `na_3s`, binnen 5 s. Zelfde X/BTC 80 minuten uit elkaar: 2 kansen; 6 s uit elkaar: 2; andere beurs: 2. Zelfde X/BTC via EUR en USDT binnen 2 s: 1 kans (dubbel tellen blijft weg). | feit | hoog |
| T4 | MEXC-data van vandaag | De regels van vandaag (vóór 16:07) hebben geen `na_3s`; ik gaf ze voor deze proef een `na_3s` op hun eindtijd. 53 driehoeken worden 49 kansen. Samen: USDT>SOL>BTC, USDC>SOL>BTC, EUR>SOL>BTC en BTC>BRL>SOL om 16:02:08 (delen allemaal SOL/BTC: terecht één kans). BDX en SOL werden nooit binnen 5 s van elkaar bevestigd, dus niet samen; en als ze dat wel waren, delen ze alleen BTCUSDT en blijven ze apart (T1). Klopt. | feit | hoog |
| T5 | Twee getallen | Kort antwoord, trechter, per dag en opschaling tonen samengevoegd (ondergrens) en los (bovengrens), bijvoorbeeld "1,0 / 2,0" en "€5,00 / €8,00" in de test. | feit | hoog |
| T6 | `python3 -I` vindt kans.py | `rapport.py` zet zijn eigen map vooraan in het zoekpad (alleen de map van de code, niet de datamap). Lokaal met `python3 -I` vanuit `/` op de data van de tak: werkt. Op een runner: proefrun 44566193252 groen, `opslaan.sh` zette om 16:30:30 commit 3ebeb2ed op de tak, en `rapport.md` op de tak is nu het nieuwe rapport (met kort antwoord en "samengevoegd / los"). | feit | hoog |
| T7 | Afgebroken run met de nieuwe code | Run 44562420725 (ee5dcf62) werd om 16:21 afgebroken door de push van 5ad279ea (code, dus terecht). Data staat op de tak (commit 0a73315b, 16:21:21) met `samenvatting.json`: 13,9 minuten, 8 beurzen. | feit | hoog |
| T8 | Kan-punten | Zin over regels van vóór 16:07 UTC staat in het rapport. `scanner/beurzen.py` zit in het paths-filter, met reden in de workflow. USDGO op 0,20% met bron (DERDEN). | feit | hoog |
| T9 | Tests | driehoek 32, scanner 31, radar 22: alle groen (zelf gedraaid). Nieuwe tests voor (a), (b), (c) en voor 5 s / andere beurs. De oude samenvoegtest is vervangen door strengere gevallen, niet zwakker gemaakt. | feit | hoog |
| T10 | Eerste echte data met `na_3s` | Run 44562420725: 3 driehoeken met winst, alle MEXC. USDT>LUNC>USDC>USDT had €100 diepte, maar de twee metingen lagen **2,9 s** uit elkaar (`duur_100_s` 2,9), dus niet bevestigd. Op beurzen met een ritme van 3 s (OKX, KuCoin, Bitget, MEXC) liggen twee metingen na elkaar soms net onder 3 s; dan zijn er drie metingen nodig (±6 s). Iets strenger dan "twee metingen na elkaar" in de README. | feit | hoog |

### Moet
Geen.

### Kan (mag later)
1. T10: een kleine marge in de duur (bijvoorbeeld 2,5 s), of in README en rapport schrijven dat het op beurzen met 3 s ritme soms drie metingen zijn.
2. De zin "Daar zat ook niets in dat 3 seconden met €100 diepte stond" staat vast in de code; klopt nu (nagekeken in de herkeuring), maar laat hem liever uitrekenen.

Opmerking: voor deze keuring zette ik twee opdrachtbestanden op main (`organisatie/opdrachten/2026-11-19-keurder-driehoek-*.json`): één om een log op te halen (er bleek geen log van afgebroken runs te zijn) en één voor de proefrun van 3 minuten. Er is geen geld uitgegeven en niets veranderd aan de code.

akkoord ja
