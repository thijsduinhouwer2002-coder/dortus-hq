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

---

## Run 2 (19 nov, ±02:00 tot 02:30 Nederlandse tijd)
Deze run: wat er na de kosten op voorspellingsmarkten echt overblijft (met een grote kostenwijziging van morgen), een eigen meting van de beloningspot voor liquiditeit, en de eerste meting aan tweedehands (Marktplaats).

### 8. Polymarket verandert morgen de kosten en kortingen (belangrijk voor elke bot)
Vanaf **vrijdag 20 nov 2026, 23:59 UTC** (GEZIEN, [docs Polymarket, fee and rebate changes](https://docs.polymarket.com/programs/fee-and-rebate-changes-november-2026.md)):
- Takerkosten blijven `aandelen × tarief × prijs × (1 − prijs)`. Tarief 0,05 voor sport, finance, tech, verkiezingen, combo's en de 5- en 15-minuten-BTC-markten; **0,01** voor overige crypto, overige politiek, economie, cultuur, weer en "mentions"; **0** voor geopolitiek. Makers (wie een order laat liggen) betalen niets.
- **Kortingen voor kleine spelers verdwijnen:** onder $200.000 gewogen volume per 30 dagen krijg je geen takerkorting en geen makerkorting meer. De dagelijkse makerpotten worden vervangen door treden (3 tot 15% van de takerkosten die jouw orders opleveren), alleen boven die drempel.
- **De beloning voor liquiditeit blijft** ("Liquidity rewards remain unchanged", GEZIEN, zelfde pagina). Dat is dus de enige vergoeding die een kleine bot nog krijgt voor het neerzetten van orders.

Rekenvoorbeeld (GEZIEN uit de formule): 100 aandelen op 50 cent in een markt met tarief 0,05 kost $1,25 aan takerkosten, dus 2,5% van de inleg; met tarief 0,01 nog $0,25 (0,5%). Elk "gat" moet daar dus eerst overheen, en twee kanten nemen betekent twee keer kosten.

### 9. Eigen meting: hoe groot is de beloningspot voor liquiditeit?
Openbare API `clob.polymarket.com/rewards/markets/current`, alle 16 pagina's, 19 nov ±02:15 (GEZIEN):
- **7.963 markten** hebben een beloning, samen **±$75.700 per dag** (rond $2,3 miljoen per maand, rekensom).
- De pot is scheef: 156 markten geven $100 of meer per dag (samen $30.700), 316 markten $50 of meer (samen $39.800); de **mediaan is $3 per dag** per markt.
- Voorwaarden per markt: meestal minstens 20 aandelen per order en hooguit 4,5 cent van het midden (GEZIEN, velden `rewards_min_size` en `rewards_max_spread`). Hoe dichter bij het midden en hoe groter, hoe meer je krijgt (formule in de docs, kwadratisch in de afstand).

Wat dit betekent: er ligt elke dag echt geld voor wie orders neerzet, en het hangt niet af van gelijk hebben. Maar (1) iedereen met een bot ziet dezelfde lijst, dus de dikke markten zijn vol (GOK); (2) wie orders laat liggen wordt geraakt als er nieuws komt ("adverse selection"): je koopt net voordat de prijs instort. Een ontwikkelaar die een open source market-making-bot kloonde en draaide, beschrijft precies dat probleem (DERDEN, [dev.to](https://dev.to/fatherson/i-cloned-a-polymarket-market-making-bot-and-ran-it-heres-what-i-learned-46ag)).
**Som (GOK):** stel een bot pakt gemiddeld $30 tot $100 per dag aan beloning in een paar honderd kleine markten waar weinig concurrentie is, met €2.000 tot €5.000 op de boeken. Over 90 dagen is dat **$2.700 tot $9.000 bruto**, waarvan een onbekend deel weer weglekt via verliezen op orders die op het verkeerde moment gevuld worden. Reden voor deze gok: de mediaanmarkt geeft $3 per dag, dus $30 tot $100 vraagt dat je in tientallen markten een flink deel van de pot pakt. Niemand die ik vond laat aantoonbaar zien dat hij dit haalt; wel claims op dev.to zonder bewijs.

### 10. Wat kleine bots echt verdienden (verslagen, geen verkooppraat)
- **176 trades, $2 winst:** een bouwer probeerde drie routes op de 15-minuten-cryptomarkten. Alleen de echte binnen-markt-arbitrage (beide kanten samen onder $1) won, 97% van de keren, maar met $0,10 tot $0,30 per trade. "Laat momentum" en "late snipe" (kopen op 93 tot 97 cent) verloren geld, en half gevulde arbitrage veranderde in een gok met verliezen tot $20 per keer (DERDEN, [dev.to, 176 trades](https://dev.to/manja316/176-trades-on-polymarket-what-my-bot-actually-made-its-not-what-you-think-3iib)). Les: de "bijna zekere" uitkomst kopen werkt niet als één misser tien winsten opeet.
- **Kalshi tegen Polymarket:** rond 50 cent moet het prijsverschil **3,5 tot 4,1 cent per paar** zijn om alleen de twee takerkosten te betalen; in het voorbeeld met 3 cent verschil verlies je met twee takerorders $0,38 tot $1,01 per 100 paar, en win je alleen $0,67 tot $1,30 op $97 als de Kalshi-kant als makerorder vol loopt (DERDEN, [Bot for Kalshi, 9 nov 2026](https://www.botforkalshi.com/blog/kalshi-polymarket-arbitrage.md); let op, de schrijver verkoopt zelf een Kalshi-bot). Dat is ±1% per gebeurtenis, met het geld vast tot de uitslag. Plus het risico dat de twee platforms de vraag anders beslissen.
- **Eigen meting "bijna zeker" (GEZIEN, `gamma-api.polymarket.com/markets`, 800 actieve markten met het meeste volume, 19 nov):** 64 uitkomsten stonden op 95 tot 99,5 cent met 1 tot 30 dagen te gaan. Opbrengst per keer 0,8 tot 4,8%. De hoge getallen horen bij echte twijfel (bijv. een voetbaluitslag op 97 cent, aantal tweets van Musk), dus het is geen gratis geld maar een eerlijke prijs voor een klein risico (GOK). Omgerekend naar "per jaar" ziet het er absurd hoog uit; dat getal zegt niets omdat je het niet elke dag opnieuw kunt doen met hetzelfde geld en dezelfde kans.

### 11. Nederland: wat betekent een verbod voor jou als speler
- De Wet op de kansspelen verbiedt het **aanbieden** zonder vergunning. Dat de speler zelf strafbaar is, vond ik niet (GOK, alleen bronnen over aanbieders gezien).
- Wel belangrijk: de rechtbank Overijssel oordeelde in apr 2024 dat een gokovereenkomst met een aanbieder zonder vergunning **nietig** is; Bwin en PokerStars moesten spelers hun verlies terugbetalen (rond €200.000 elk) (DERDEN, [NJB](https://www.njb.nl/nieuws/illegale-gokbedrijven-moeten-geld-aan-spelers-terugbetalen/), ECLI:NL:RBOVE:2024:2078). De keerzijde (GOK): winst bij zo'n aanbieder kun je in Nederland ook niet afdwingen. Als Polymarket je saldo bevriest, heb je geen poot om op te staan.
- Belasting: nog niet nagekeken.

### 12. Tweedehands: eerste meting op Marktplaats
Openbare zoek-JSON van Marktplaats (`marktplaats.nl/lrp/api/search`, zonder account), zoekterm "iphone 13 128gb", 19 nov (GEZIEN): 1.658 advertenties. Van de eerste 30 waren 11 een gewone iPhone 13 (geen Pro) met een prijs van een particulier: **€130 tot €250, mediaan rond €190**. Handelaren met garantie vroegen €249 en €259 voor hetzelfde toestel (GEZIEN, zelfde zoekopdracht).
- **De route:** een bot die elke paar minuten nieuwe advertenties leest en meldt wat ver onder de mediaan staat, dan zelf ophalen, nakijken en doorverkopen. Er zijn kant-en-klare scrapers en "monitors" voor Marktplaats op Apify (DERDEN, [Apify Marktplaats Monitor](https://apify.com/bostomate/marktplaats-monitor), en tien andere), dus het idee is niet nieuw.
- **Som (GOK):** €60 tot €100 marge per telefoon na nakijken, kleine reparaties en verzendkosten. Voor €10.000 in 3 maanden zijn dat **100 tot 170 toestellen, dus 8 tot 13 per week**, met €1.000 tot €2.000 in voorraad. Dat is een (bij)baan van 20 tot 30 uur per week. Het kan, maar het is werk, geen bot die geld maakt.
- **Risico's:** gestolen toestellen of iCloud-slot (helen is strafbaar: altijd IMEI en iCloud nakijken), oplichting, onverkochte voorraad. Marktplaats verbiedt scrapen in de voorwaarden (grijs: kans op blokkade van je IP of account, GOK). Wie stelselmatig met winst doorverkoopt, moet dat als inkomen opgeven en is mogelijk ondernemer met KvK-plicht (GOK, nakijken).
- **Kaartjes:** TicketSwap staat doorverkopen hoger dan 20% boven de oorspronkelijke prijs niet toe (DERDEN, [TicketSwap op Medium](https://medium.com/ticketswap/how-to-change-the-secondary-ticketing-market-part-3-the-120-rule-9e52a92e4b24)). Met verkoopkosten blijft er hooguit een paar euro per kaartje over. Valt af als route naar €10.000.

### Nog te doen (volgende runs)
1. Tweedehands verder meten: een tweede product (consoles, Lego, Pokemonkaarten verzegeld) en de inkoopprijzen van opkopers (Swappie, Back Market) tegen de laagste prijzen op Marktplaats; dat zou een echte arbitrage zonder doorverkopen aan particulieren zijn.
2. Liquiditeitsbeloning: per markt uitrekenen wat een order van 20 tot 100 aandelen nu zou verdienen gegeven het boek (openbaar), om de gok van $30 tot $100 per dag te vervangen door een meting.
3. Belasting op winst bij voorspellingsmarkten en doorverkoop.

---

## Stand na run 02:30 (19 nov, Nederlandse tijd)
**Vijf belangrijkste dingen tot nu toe**
1. Kapitaal-arbitrage (beurzen, driehoek, funding) levert met weinig geld nooit €10.000 in 3 maanden: gemeten 0,007% verschil op BTC tegen 0,2 tot 0,8% kosten, funding 3 tot 11% per jaar (GEZIEN, run 1). Voor het doel heb je bij funding ±€500.000 nodig (GOK).
2. Polymarket haalt op **20 nov 23:59 UTC** alle maker- en takerkortingen weg voor wie onder $200.000 volume per maand zit (GEZIEN). Wat een kleine bot overhoudt is de **liquiditeitsbeloning: ±$75.700 per dag over 7.963 markten, mediaan $3 per markt** (GEZIEN, eigen telling). Dat is de grootste pot "geld voor werk" die ik vond die niet van gelijk hebben afhangt, maar de risico's (geraakt worden bij nieuws, concurrentie van bots) zijn niet gemeten.
3. Echte arbitrage op voorspellingsmarkten bestaat maar is klein: Kalshi tegen Polymarket vraagt 3,5 tot 4,1 cent verschil alleen voor de kosten (DERDEN), en een eerlijk verslag van 176 bot-trades eindigde op $2 winst (DERDEN). "Bijna zeker" kopen op 95 tot 99 cent is een eerlijke prijs, geen gratis geld (GEZIEN plus GOK).
4. In Nederland is een gokovereenkomst met een aanbieder zonder vergunning nietig (DERDEN, rechtbank Overijssel 2024). Dus: winst bij Polymarket is niet af te dwingen als het saldo bevroren wordt (GOK). Dat maakt route 1 grijzer dan het lijkt.
5. De enige route die met weinig geld wél lineair richting €10.000 schaalt, is **tweedehands doorverkopen met een zoekbot**: op Marktplaats zit tussen particulier (mediaan ±€190) en handelaar (€249 tot €259) voor een iPhone 13 rond €60 tot €100 per stuk (GEZIEN prijzen, GOK marge). Het doel vraagt dan 8 tot 13 verkopen per week: haalbaar, maar het is een baan, geen passief inkomen.

**Rangorde op kans maal opbrengst richting €10.000 in 3 maanden** (alle kansen GOK, met reden)
| # | Route | Inleg geld / uren per week | Kans op €10.000 | Ergste geval |
|---|---|---|---|---|
| 1 | Tweedehands doorverkopen met een zoekbot (Marktplaats, telefoons en ander spul met vaste prijsband) | €1.000 tot €2.000 / 20 tot 30 | 15 tot 25% (schaalt met uren; vraag en aanbod zijn er, GEZIEN) | gestolen of kapot toestel, onverkochte voorraad, IP of account geblokkeerd |
| 2 | Polymarket: liquiditeitsbeloning pakken met een eigen market-making-bot | €2.000 tot €5.000 / 15+ bouwen, daarna 5 | 5 tot 10% (pot is groot, GEZIEN; eigen aandeel en verlies op vullingen onbekend) | inleg deels kwijt aan vullingen vlak voor nieuws; saldo bevroren, niet af te dwingen in NL |
| 3 | Voorspellingsmarkten: nieuwe gaten zoeken, Kalshi tegen Polymarket | €1.000 tot €5.000 / 20+ | 2 tot 5% (bekende gaten dicht, kosten 3,5 tot 4,1 cent per paar, DERDEN) | verkeerde of verschillende beslissing van een markt, beide kanten kwijt |
| 4 | Sportarbitrage en bonussen in Nederland | €1.000 tot €3.000 / 5 tot 10 | onder 5% (plafond ±€4.000, run 1) | accounts beperkt |
| 5 | Odd-lot tenders, kleine promoties | een paar honderd / 1 | rond 0% | bod ingetrokken |
| 6 | Funding-arbitrage | groot kapitaal / 2 | rond 0% met weinig geld | beurs valt om, liquidatie |
| 7 | Spot- en driehoeksarbitrage, CS2-skins, kaartjes (TicketSwap max 20% erboven), airdrops | n.v.t. | rond 0% | kosten en tijd kwijt |

Verschil met run 1: tweedehands stijgt naar plek 1 omdat het als enige met uren schaalt en nu gemeten is; voorspellingsmarkten splitsen zich in market making (blijft kansrijk door de beloningspot) en pure arbitrage (zakt door de kosten en het wegvallen van kortingen op 20 nov).
