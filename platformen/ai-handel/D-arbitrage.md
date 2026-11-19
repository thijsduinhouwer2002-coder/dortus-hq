# D. Arbitrage en prijsverschil-handel (zoeker D)

Onderzoek voor Thijs zelf, geen advies en geen "koop dit". Elk cijfer: GEZIEN (zelf gemeten of gelezen, met bron), DERDEN (met link) of GOK.
Rekenvoorbeelden gebruiken een algemeen bedrag, niet dat van Thijs.

De kernvraag uit de brief: welke vorm kan met weinig startgeld en een bot richting **€10.000 winst in 3 maanden**?

## De rode draad (run 1)
Echte arbitrage (risicoloos prijsverschil) levert een **percentage van je inleg** op. Met weinig geld is dat percentage nooit €10.000. Wie met weinig geld veel verdient, doet dat bijna altijd waar het voordeel uit **snelheid in een jonge markt** komt (voorspellingsmarkten) of uit **eigen uren** (bonussen, doorverkopen). Zie de som per vorm hieronder.

---

## 1. Crypto: prijsverschil tussen beurzen (spot)
**Gemeten**, 19 nov ±01:24, BTC-EUR, beste bod en laat via openbare API's zonder account (GEZIEN):

| Beurs | Bod | Laat |
|---|---|---|
| Kraken | 57084,6 | 57084,7 |
| Bitvavo | 57084 | 57085 |
| Coinbase | 57076,66 | 57086,38 |
| Bitstamp | 57088,82 | 57089,06 |

Het grootste verschil tussen kopen op de ene en verkopen op de andere was rond **€4 op €57.000, dus 0,007%** (GEZIEN, 2 metingen 3 seconden na elkaar; bronnen: `api.kraken.com/0/public/Ticker`, `api.bitvavo.com/v2/ticker/book`, `api.exchange.coinbase.com/products/BTC-EUR/ticker`, `bitstamp.net/api/v2/ticker/btceur`).
Gewone takerkosten zijn per kant rond 0,1 tot 0,4% (GOK, standaardtarieven, deze run niet opnieuw nagekeken), dus heen en terug 0,2 tot 0,8%. Het verschil is **30 tot 100 keer te klein**. Plus opnametijd: tussen beurzen schuiven duurt minuten tot uren, dan is het verschil weg.
**Oordeel:** valt af voor een gewone gebruiker. Driehoeksarbitrage binnen één beurs heeft hetzelfde probleem (drie keer kosten). Hummingbot (zie B) kan het technisch, maar wint dan alleen bij een beurs met 0% kosten of als market maker met korting.

## 2. Funding-rate-arbitrage (spot kopen, perpetual shorten)
**Gemeten funding** (GEZIEN, openbare API's, zonder account; Binance en Bybit weigeren vanaf deze server door hun landenblokkade):

| Beurs, munt | Periode | Gemiddeld per jaar | Tijd negatief |
|---|---|---|---|
| OKX BTC | laatste 93 dagen | 5,9% | 11% |
| OKX ETH | laatste 94 dagen | 4,3% | 16% |
| OKX SOL | laatste 94 dagen | 3,3% | 30% |
| Hyperliquid BTC | laatste ±21 dagen (500 uur) | 10,3% | 5% |
| Hyperliquid ETH | idem | 10,4% | 3% |
| Hyperliquid SOL | idem | 8,5% | 13% |
| Hyperliquid HYPE | idem | 11,7% | 9% |

Bronnen: `okx.com/api/v5/public/funding-rate-history`, `api.hyperliquid.xyz/info` (type fundingHistory en metaAndAssetCtxs).
Op Hyperliquid stonden op dat moment bijna alle grote munten op 11% per jaar (GEZIEN). Dat is de vaste "rente"-bodem van hun formule, geen kans; alleen XMR stak eruit met 56% per jaar bij $23 miljoen dagvolume (GEZIEN), en zulke uitschieters draaien vaak binnen dagen om (GOK).
**Kant-en-klare maatstaf:** Ethena (een stablecoin die precies deze truc doet) gaf sUSDe **5,2% gemiddeld over 30 dagen en 4,9% over 90 dagen** (GEZIEN, `ethena.fi/api/yields/protocol-and-staking-yield`, stand 11 nov 2026). Een eigen bot moet dat na kosten verslaan, anders voegt hij niets toe.

**Som:** stel €10.000 inleg, verdeeld over spot en onderpand voor de short, dus rond €7.000 aan positie (GOK, bij 2 tot 3x op de shortkant). Bij 8% per jaar is dat over 3 maanden **±€140**, min 4 orders van 0,05 tot 0,1% (±€20) = **±€120** (GOK, uit de gemeten rentes). Voor €10.000 in 3 maanden bij 8% per jaar heb je **rond €500.000** nodig (GOK, rekensom). Zelfs bij 50% per jaar op uitschieters nog ±€80.000 (GOK).
**Ergste geval:** de beurs valt om of zet opnames stil (FTX 2022), de short wordt geliquideerd bij een snelle stijging als het onderpand op een andere beurs staat, funding draait wekenlang negatief (SOL: 30% van de tijd, GEZIEN).
**Nederland:** perpetuals bij een EU-partij met vergunning zijn voor particulieren beperkt (zie brief). Hyperliquid vraagt geen KYC en is een grijs gebied (geen MiCA-vergunning); risico is vooral technisch (smart contract, brug) en dat het geld vastzit als iets misgaat (GOK).
**Oordeel:** veilig-ish rendement, maar **0% kans op het doel** met weinig geld. Hoort eerder bij hoek C als parkeerplek.

## 3. Voorspellingsmarkten (Polymarket, Kalshi)
Hier zit aantoonbaar het meeste geld voor kleine spelers met een bot.
- **Binnen-markt-arbitrage:** onderzoekers vonden op Polymarket tussen apr 2024 en apr 2025 **±$40 miljoen** aan gerealiseerde arbitragewinst, uit twee soorten: alle uitkomsten samen onder of boven $1 (rebalancing) en tegenstrijdige prijzen tussen gekoppelde markten (combinatorisch) (DERDEN, [arXiv 2508.03474](https://arxiv.org/abs/2508.03474v1)).
- **Bots winnen:** 14 van de 20 winstgevendste wallets op het leaderboard zijn bots, volgens een telling van maart 2026 (DERDEN, [Finance Magnates](https://www.financemagnates.com/trending/prediction-markets-are-turning-into-a-bot-playground/), bron is een tweet, dus zwak).
- **Bekendste voorbeeld:** wallet 0x8dxd zou in een maand van ±$300 naar meer dan $400.000 zijn gegaan op 15-minuten-cryptomarkten, door de vertraging tussen Polymarket en de koers op grote beurzen te pakken (DERDEN, [Finance Magnates](https://www.financemagnates.com/trending/prediction-markets-are-turning-into-a-bot-playground/)). **Dit gat is dicht:** Polymarket voerde in jan 2026 dynamische takerkosten in op juist die markten, met als doel deze latency-arbitrage te stoppen (DERDEN, [Finance Magnates](https://www.financemagnates.com/cryptocurrency/polymarket-introduces-dynamic-fees-to-curb-latency-arbitrage-in-short-term-crypto-markets/), [The Block](https://www.theblock.co/post/384461/polymarket-adds-taker-fees-to-15-minute-crypto-markets-to-fund-liquidity-rebates)). Les: zo'n gat bestaat een paar maanden, wie het als eerste ziet verdient, daarna sluit het platform het.
- **Eigen meting** (GEZIEN, `gamma-api.polymarket.com/events`, de 1000 events met het meeste volume, 19 nov): 188 events met meerdere uitkomsten; bij 9 telden de beste laatprijzen op tot onder $0,995, bij 2 telden de biedprijzen op tot boven $1,005. Bij nader zien zijn de grote "gaten" (bijv. 0,343 of 0,906) **geen echte arbitrage**: de lijst uitkomsten is niet volledig (een "andere"-uitkomst ontbreekt in de API) of er staat maar een paar dollar op het boek. Echte gaten zijn klein en worden in seconden gepakt (GOK, past bij het arXiv-stuk).
- **Kalshi** zegt sinds okt 2025 in meer dan 140 landen te werken (DERDEN, [Cointelegraph](https://regional-front.cointelegraph.com/news/kalshi-300-million-raise-prediction-markets-140-countries)); de Ksa overwoog actie (DERDEN, [InGame](https://www.ingame.com/kalshi-global-exchange-european-regulator-action/)). Arbitrage tussen Kalshi en Polymarket op dezelfde vraag is een bekende route met veel gidsen; het grootste risico is dat beide platforms een vraag **anders beslissen** (andere regels), dan verlies je beide kanten (GOK).

**Nederland (grijs):** de Ksa verbood Polymarket in feb 2026 met een dwangsom van €420.000 per week; Polymarket heeft geen Nederlandse vergunning (DERDEN, [NOS](https://nos.nl/l/2602855)). Nederlanders zijn afgesloten (DERDEN, [Welingelichte Kringen](https://www.welingelichtekringen.nl/economie/nederlandse-gebruikers-kunnen-niet-meer-gokken-op-polymarket)). Met een VPN meedoen breekt de voorwaarden van Polymarket. De wet richt zich op de aanbieder, niet op de speler (GOK, nog na te kijken). Risico: account of saldo bevroren, en winst op een illegaal kansspel valt in Nederland mogelijk onder kansspelbelasting of box 3 (GOK, nakijken; belasting ontduiken mag niet).
**Oordeel:** de enige vorm in dit onderzoek waar mensen met honderden dollars aantoonbaar tienduizenden verdienden. Maar de makkelijke gaten zijn dicht en de concurrentie bestaat uit bots. Kans op het doel klein maar niet nul.

## 4. Sportweddenschappen en bonussen in Nederland
- Sinds okt 2024 moet een Nederlandse aanbieder een toets doen boven **€300 netto per maand voor 18 tot 24 jaar en €700 voor 24 en ouder**, per aanbieder (DERDEN, [iGaming Business](https://igamingbusiness.com/legal-compliance/ksa-tightens-rules-online-gambling-deposit-means-tests/)). Dat begrenst hoeveel geld je per bookmaker kunt laten werken.
- Casino's mogen spelers die regelmatig winnen uitsluiten van bonussen (DERDEN, [Gambling.com](https://www.gambling.com/nl/online-casinos/strategie/bonus-verbod-casino-nederland)). Arbitrage tussen bookmakers leidt bekend tot "limieten" op je account (DERDEN, vele gidsen, bijv. [Startuphub](https://www.startuphub.ai/news/sports-arbitrage-best-books-limits-explained)).
- **Som (GOK):** ±25 Nederlandse vergunninghouders, per stuk een paar honderd euro winst voordat je beperkt wordt, geeft een eenmalige pot van **€1.000 tot €4.000**, niet herhaalbaar. Buitenlandse bookmakers zonder vergunning: grijs (account dicht, saldo vast).
- **Oordeel:** echte, bijna risicoloze euro's, maar een plafond ver onder €10.000. Bot helpt alleen bij het vinden (odds vergelijken).

## 5. Verzamelobjecten: CS2-skins (iets wat niemand verwacht)
Eigen meting (GEZIEN, 19 nov): openbare Skinport-API (`api.skinport.com/v1/items`, EUR) tegen de laagste prijs op de Steam-markt (`steamcommunity.com/market/priceoverview`), 12 items met veel aanbod:

| Item | Skinport laagste | Steam laagste | Steam na 15% kosten |
|---|---|---|---|
| Operation Breakout Weapon Case | €5,80 | €8,56 | €7,44 |
| CS:GO Weapon Case 2 | €14,06 | €20,76 | €18,05 |
| AK-47 Redline (Field-Tested) | €20,96 | €26,99 | €23,47 |

Alle 12 waren op Steam na kosten 3 tot 33% duurder (GEZIEN). **Dit lijkt arbitrage maar is het niet:** wat je op Steam verkoopt wordt Steam-tegoed, en dat kun je niet opnemen. Het verschil is precies de prijs van "contant geld tegen Steam-tegoed". Alleen nuttig als je dat tegoed toch zou uitgeven. Echte handel tussen sites met contant geld (CSFloat, Skinport, Buff) is kennis en speculatie, met een week handelsblokkade per item (GOK, nog na te kijken).
**Oordeel:** valt af als arbitrage.

## 6. Aandelen: odd-lot tender offers (VS)
Bij sommige Amerikaanse terugkoopbiedingen krijgen bezitters van minder dan 100 aandelen voorrang. Voorbeeld OPTU (2026): kopen rond $1,05, aanbod $2,50, **±$145 per account** (DERDEN, [Doctor of Credit](https://www.doctorofcredit.com/odd-lot-tender-opportunity-buy-optu-for-1-05-sell-for-2-5-145-money-maker/)). Het risico: het bod wordt ingetrokken en je zit met aandelen.
**Som (GOK):** een handvol zulke kansen per jaar, ±$50 tot $300 per stuk, dus enkele honderden euro's per jaar. Vanuit Nederland via een broker met VS-aandelen (GOK, nakijken welke deelnemen aan tender offers).
**Oordeel:** bijna gratis geld, te klein voor het doel.

## 7. Airdrops "farmen" met meerdere wallets
Grijs (voorwaarden van het project). Detectie is sterk verbeterd: Polymarket zegt Sybil-accounts te filteren, Arbitrum en LayerZero sporen clusters van wallets op (DERDEN, [BlockEden](https://blockeden.xyz/blog/2026/01/19/airdrop-farming-2026-polymarket-opensea-hyperliquid-base/)). Opbrengst is een loterij met inleg aan kosten en uren.
**Oordeel:** geen arbitrage; hoogstens een gok met een lage kans.

## Valt af, omdat
- **Wash trading, spoofing, pump and dump** op kleine munten of voorspellingsmarkten: marktmanipulatie, illegaal.
- **Kimchi-premie** (Koreaanse beurzen duurder): vraagt een Koreaanse rekening; als buitenlander niet zonder valse gegevens (GOK).
- **Andermans identiteit** voor extra bookmaker- of bonusaccounts: fraude.

## Nog te doen (volgende runs)
1. Tweedehands en kaartjes: scraper-bot op Marktplaats/Vinted voor te laag geprijsde spullen, en TicketSwap-regels. Hier zit mogelijk de hoogste kans op €10.000 met weinig geld, omdat het met uren schaalt in plaats van met kapitaal. Nog niets gemeten.
2. Voorspellingsmarkten verdiepen: wat er nu nog werkt na de kosten (market making met de rebates, bijna-zekere uitkomsten op 97 tot 99 cent, Kalshi tegen Polymarket) en code op GitHub lezen.
3. Nakijken: Nederlandse wet bij meedoen aan een onvergund kansspel (speler strafbaar of niet), belasting op die winst, en welke EU-partij perpetuals voor particulieren biedt.

---

## Stand na run 01:30 (19 nov)
**Vijf belangrijkste dingen**
1. Prijsverschil tussen beurzen is dood voor een gewone gebruiker: gemeten 0,007% verschil op BTC tegen 0,2 tot 0,8% kosten (GEZIEN plus GOK op kosten).
2. Funding-arbitrage geeft rond 3 tot 11% per jaar (GEZIEN, OKX en Hyperliquid); kant-en-klaar via Ethena 5,2% (GEZIEN). Voor €10.000 in 3 maanden heb je ±€500.000 nodig (GOK). Kans op het doel met weinig geld: nul.
3. Voorspellingsmarkten zijn de enige plek waar kleine spelers met een bot aantoonbaar groot verdienden ($40 miljoen arbitrage in een jaar, DERDEN; $300 naar $400.000, DERDEN). Het bekendste gat is in jan 2026 dichtgezet met kosten (DERDEN), en Polymarket is in Nederland verboden (DERDEN), dus grijs.
4. Bonussen, sportarbitrage en odd-lot tenders geven echte maar kleine, eenmalige bedragen (GOK €1.000 tot €4.000 voor sport; enkele honderden per jaar voor tenders).
5. "Gaten" die je in openbare data ziet zijn vaak schijn: onvolledige uitkomstlijsten op Polymarket, Steam-tegoed dat niet uit te betalen is (beide GEZIEN). Een bot die ze blind koopt verliest geld.

**Rangorde op kans maal opbrengst richting €10.000 in 3 maanden** (alle kansen GOK)
| # | Route | Inleg geld / uren per week | Kans op €10.000 | Ergste geval |
|---|---|---|---|---|
| 1 | Voorspellingsmarkten met een bot (nieuwe gaten zoeken, Kalshi tegen Polymarket, market making) | €1.000 tot €5.000 / 20+ | 5 tot 10% | inleg kwijt aan foute beslissing van een markt of bevroren account |
| 2 | Tweedehands/verzamel doorverkopen met een zoekbot (nog niet onderzocht) | €1.000 tot €3.000 / 20+ | onbekend, mogelijk 10% | onverkochte voorraad |
| 3 | Sportarbitrage en bonussen in Nederland | €1.000 tot €3.000 / 5 tot 10 | onder 5% (plafond ±€4.000) | accounts beperkt, kleine verliezen bij foute inzet |
| 4 | Odd-lot tenders en kleine promoties | een paar honderd / 1 | rond 0% | bod ingetrokken, klein verlies |
| 5 | Funding-arbitrage | groot kapitaal nodig / 2 | rond 0% met weinig geld | beurs valt om, liquidatie |
| 6 | Spot- en driehoeksarbitrage, CS2-skins, airdrops | n.v.t. | rond 0% | kosten en tijd kwijt |
