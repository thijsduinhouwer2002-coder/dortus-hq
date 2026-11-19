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

---

## Run 3 (19 nov, ±03:25 tot 03:55 Nederlandse tijd)
Deze run: de gok uit run 2 over de liquiditeitsbeloning op Polymarket vervangen door een meting per markt, en een snelle controle of opkopers meer betalen dan particulieren op Marktplaats.

### 13. Eigen meting: wat zou een order van ±$200 per markt nu aan beloning pakken?
**Werkwijze (GEZIEN, openbare API's zonder account, 19 nov 02:25 en 02:28 UTC):** alle markten met beloning opgehaald (`clob.polymarket.com/rewards/markets/current`: 7.909 markten, $74.571 per dag, past bij run 2). Daarvan de 120 met de hoogste beloning plus 120 willekeurige tussen $5 en $50 per dag. Per markt het orderboek (`clob.polymarket.com/books`) en de puntentelling uit de docs nagerekend: per order `((v − s) / v)² × aantal`, met v de maximale afstand tot het midden en s de afstand van de order; tweezijdig telt vol, eenzijdig (midden tussen 0,10 en 0,90) voor een derde; elke minuut een steekproef, aan het eind van de UTC-dag naar verhouding uitbetaald, minimaal $1 (GEZIEN, [docs Liquidity Rewards](https://docs.polymarket.com/programs/liquidity-rewards.md)). Daarna uitgerekend welk deel een nieuwe order van 200 aandelen aan beide kanten zou krijgen (±$200 vastgezet geld per markt) naast wat er al ligt.

**Uitkomst (GEZIEN, mijn model; zie de kanttekeningen):**
| Groep | Markten | Mediaan per dag per $200 |
|---|---|---|
| beloning $50+ per dag | 120 | $5 tot $6 |
| beloning $5 tot $50 per dag | 120 | $1,3 tot $2 |

**Het eigenlijke punt zit in de leeftijd van de markt** (GEZIEN, startdatum uit `gamma-api.polymarket.com/markets`, de 120 duurste markten):
| Leeftijd markt | Markten | Mediaan aandeel dat een nieuwe $200-order zou krijgen | Mediaan per dag per $200 | Mediaan volume 24 uur |
|---|---|---|---|---|
| jonger dan 2 dagen | 29 | 32% | $62 | $936 |
| 2 tot 7 dagen | 21 | 2% | $4 | $8.556 |
| ouder dan 7 dagen | 70 | 2% | $4 | $15.342 |

Voorbeeld: "Anthropic IPO closing market cap above $1.4T?" gaat sinds 18 nov 21:34 UTC, geeft $400 per dag aan beloning, en had binnen 4,5 cent van het midden op het moment van meten maar een paar honderd aandelen aan orders staan, bij $769 volume in 24 uur (GEZIEN). Een tweede meting 3 minuten later gaf bijna dezelfde aandelen (GEZIEN), dus het is geen flits van één seconde.
Volgens het model zou $200 in elk van de 10 beste markten ($2.000 in totaal) ±$1.700 per dag opleveren (GEZIEN als rekenuitkomst). **Dat getal geloof ik niet als verwachting**, om deze redenen:
- Het midden waar Polymarket mee rekent negeert orders onder de minimale grootte; in dunne boeken ligt dat ergens anders dan ik aannam, dus mijn order kan verder van het midden staan dan in het model (GOK).
- Nieuwe markten hebben nog geen vaste prijs. Wie daar orders laat liggen, wordt gevuld door mensen die meer weten (bij de Anthropic-markten: elk nieuwtje over een beursgang). Dat verlies telt het model niet mee. Dit is het bekende risico van "adverse selection" (DERDEN, [Fifty Cent Dollars over Kalshi-beloningen](https://fiftycentdollars.substack.com/p/kalshis-new-liquidity-incentives)).
- Bots die dit al doen kunnen binnen minuten bijschuiven zodra er iemand bijkomt; dan zakt je aandeel naar de 2% van de oudere markten (GOK).
- De beloning voor nieuwe markten is groot omdat Polymarket juist dan liquiditeit wil; wie er als eerste staat pakt de pot, daarna zakt hij. Je moet dus elke dag nieuwe markten vinden en op tijd weg uit markten vlak voor een uitslag (DERDEN, [startpolymarket, reward farming](https://startpolymarket.com/strategies/reward-farming/): "avoid markets approaching a known catalyst").
- Kleine bedragen per markt vallen onder de $1-drempel en worden dan niet uitbetaald, ook niet later (DERDEN, zelfde bron).

**Som (GOK):** stel je haalt na al die aftrek 5 tot 20% van wat het model zegt, met $2.000 tot $5.000 aan orders verdeeld over 10 tot 25 jonge markten. Dat is $85 tot $500 per dag bruto, min verlies op vullingen, over 90 dagen grofweg **$5.000 tot $30.000**. De onzekerheid is enorm: niemand die ik vond laat dit met bewijs zien, en verslagen op dev.to zijn vaak verkooppraat. Wat wel vaststaat (GEZIEN): de pot is ±$75.000 per dag, blijft na 20 nov ongewijzigd, en in jonge markten ligt hij er voor het grijpen volgens het openbare boek.
**Ergste geval:** de bot koopt een berg aandelen vlak voor nieuws (bijv. een markt die van 70 naar 5 cent valt), dus een flink deel van wat er op de boeken staat kwijt; of het account wordt bevroren (Nederland, zie hieronder).
**Nederland (grijs, ongewijzigd t.o.v. run 2):** Polymarket is verboden door de Ksa, meedoen kan alleen met een VPN en breekt de voorwaarden, en een saldo is in Nederland niet af te dwingen (run 2, punt 11). Dat geldt hier net zo hard.
**Nuttige volgende stap die niets kost en niets riskeert:** een "schaduwbot" die alleen openbare data leest en elke minuut uitrekent welk aandeel en welk verlies op vullingen een order zou hebben gehad, een week lang, zonder account en zonder handel. Pas als die week een duidelijk plus laat zien, is er iets om over te beslissen.

Kleine bijvangst: de startdatum in de beloningsinstellingen zelf zegt niets over de leeftijd van de markt (1.740 instellingen "begonnen" vandaag, GEZIEN); ze worden kennelijk dagelijks vernieuwd. Gebruik de startdatum van de markt uit Gamma.

### 14. Tweedehands: betalen opkopers meer dan particulieren?
Coolblue geeft bij inruil **"tot €170"** voor een iPhone 13 128GB, en dat is de beste staat (DERDEN, [Coolblue, inruilwaarde iPhone 13](https://www.coolblue.nl/en/advice/what-is-the-value-of-your-iphone-13.html)). Particulieren op Marktplaats vroegen een mediaan van ±€190 (GEZIEN, run 2). Een opkoper betaalt dus **minder** dan de middelste particulier. Directe arbitrage (kopen op Marktplaats, meteen aan een opkoper verkopen) werkt alleen met de onderkant van de markt (€130 tot €150, GEZIEN in run 2), dus ±€20 tot €40 per toestel min reiskosten en risico (GOK). Dat is te weinig voor het doel; de marge zit bij verkopen aan een particulier of als handelaar met garantie (€249 tot €259, GEZIEN run 2), en dat is werk.

### Nog te doen (volgende runs)
1. Polymarket: het model verbeteren met het echte "aangepaste midden" en een schatting van verlies op vullingen uit de openbare trades van jonge markten (`data-api.polymarket.com/trades`), zodat de 5 tot 20% hierboven een meting wordt.
2. Kalshi heeft ook een beloning voor liquiditeit (DERDEN, Fifty Cent Dollars hierboven). Nakijken: hoe groot nu, en of Kalshi Nederland toelaat (Ksa overwoog actie, run 1).
3. Belasting op winst bij voorspellingsmarkten en doorverkoop (staat nog open sinds run 1).

---

## Stand na run 03:55 (19 nov, Nederlandse tijd)
**Vijf belangrijkste dingen tot nu toe**
1. Kapitaal-arbitrage (beurzen, driehoek, funding) haalt met weinig geld nooit €10.000 in 3 maanden: 0,007% verschil op BTC tegen 0,2 tot 0,8% kosten, funding 3 tot 11% per jaar (GEZIEN, run 1).
2. **Nieuw en het sterkste spoor:** in Polymarket-markten jonger dan 2 dagen zou een nieuwe order van $200 volgens het openbare boek een mediaan van **32% van de beloningspot** krijgen, tegen 2% in oudere markten; mediaan **$62 per dag per $200** tegen $4 (GEZIEN, eigen model op 120 markten, twee metingen). Het model mist verlies op vullingen en het echte midden, dus reken met 5 tot 20% daarvan (GOK): $5.000 tot $30.000 in 90 dagen met $2.000 tot $5.000 inleg, met enorme spreiding.
3. Dat spoor is in Nederland grijs: Polymarket verboden, VPN nodig, saldo niet af te dwingen (DERDEN, run 1 en 2). Een schaduwbot zonder account kan het gratis een week toetsen.
4. Echte arbitrage op voorspellingsmarkten (Kalshi tegen Polymarket, "bijna zeker" kopen) is klein na kosten: 3,5 tot 4,1 cent per paar nodig (DERDEN), een verslag van 176 trades eindigde op $2 (DERDEN).
5. Tweedehands schaalt met uren, niet met geld: €60 tot €100 per telefoon bij doorverkoop aan particulieren (GOK op marge, prijzen GEZIEN); opkopers betalen minder dan de middelste particulier (tot €170 tegen ±€190, DERDEN en GEZIEN), dus geen snelle arbitrage via opkopers.

**Rangorde op kans maal opbrengst richting €10.000 in 3 maanden** (alle kansen GOK, met reden)
| # | Route | Inleg geld / uren per week | Kans op €10.000 | Ergste geval |
|---|---|---|---|---|
| 1 | Polymarket: beloning voor liquiditeit pakken in markten jonger dan 2 dagen, met een eigen bot | €2.000 tot €5.000 / 15+ bouwen, daarna 5 tot 10 | 15 tot 25% (pot en lege boeken GEZIEN; verlies op vullingen en reactie van andere bots onbekend) | groot deel inleg kwijt bij nieuws in een dunne markt; saldo bevroren, niet af te dwingen in NL |
| 2 | Tweedehands doorverkopen met een zoekbot (Marktplaats) | €1.000 tot €2.000 / 20 tot 30 | 15 tot 25% (schaalt met uren, GEZIEN vraag en aanbod) | gestolen of kapot toestel, voorraad, blokkade |
| 3 | Voorspellingsmarkten: nieuwe gaten, Kalshi tegen Polymarket | €1.000 tot €5.000 / 20+ | 2 tot 5% | markten beslissen anders, beide kanten kwijt |
| 4 | Sportarbitrage en bonussen in Nederland | €1.000 tot €3.000 / 5 tot 10 | onder 5% (plafond ±€4.000) | accounts beperkt |
| 5 | Odd-lot tenders, kleine promoties | een paar honderd / 1 | rond 0% | bod ingetrokken |
| 6 | Funding-arbitrage | groot kapitaal / 2 | rond 0% met weinig geld | beurs valt om, liquidatie |
| 7 | Spot- en driehoeksarbitrage, CS2-skins, kaartjes, airdrops, opkopers | n.v.t. | rond 0% | kosten en tijd kwijt |

Verschil met run 2: route 1 stijgt van 5 tot 10% naar 15 tot 25% omdat de beloning per markt nu gemeten is en jonge markten bijna leeg blijken; hij staat boven tweedehands omdat de opbrengst niet aan uren vastzit, maar hij is grijs en het verlies op vullingen is nog niet gemeten. Wie geen grijs wil, kijkt naar route 2.

---

## Run 4 (19 nov, ±04:25 tot 04:55 Nederlandse tijd)
Deze run: het grootste gat uit run 3 gemeten, namelijk hoeveel makers in jonge Polymarket-markten verliezen op orders die op het verkeerde moment gevuld worden. Plus: of Kalshi een uitweg is.

### 15. Eigen meting: verlies op vullingen tegen beloning in de eerste 48 uur
**Hoe gemeten (GEZIEN, openbare API's, geen account):** de 40 markten met de hoogste beloning (uit de 400 duurste in `clob.polymarket.com/rewards/markets/current`) die 2 tot 6 dagen oud zijn, zodat hun eerste 48 uur al voorbij is en er 24 uur na elke trade een prijs bestaat. Per markt alle trades uit `data-api.polymarket.com/v2/trades` (let op: de oude v1 is uitgezet, GEZIEN) en de prijsreeks per 10 minuten uit `clob.polymarket.com/prices-history`. Voor elke trade: wat de maker (de kant die liet liggen) won of verloor als je de prijs 1 uur en 24 uur later neemt ("markout"). Dat bevat zowel de winst op de spread als het verlies door nieuws.

**Uitkomst (GEZIEN, eigen berekening, 19 nov):**
| | Eerste 48 uur, alle 40 markten |
|---|---|
| Gevuld bij makers | ±$103.600 |
| Resultaat makers na 24 uur | **−$3.470** (−3,3% van wat gevuld werd); na 1 uur −$4.130 |
| Beloning in die 2 dagen (dagbedrag nu × 2) | **±$5.950** |
| Mediaan per markt: verlies als deel van de beloning | **8%** |
| Markten waar het verlies groter was dan de beloning | 9 van 40 |

**Het verlies zit bijna helemaal in nieuwsmarkten** (indeling door mij gemaakt na het zien van de cijfers, dus met korrel zout):
| Soort markt | Markten | Gevuld 48 uur | Resultaat makers | Beloning 2 dagen |
|---|---|---|---|---|
| Nieuws, politieke peilingen, roddel (Jensen Huang, "odds leader", Fed, Democratische meerderheid) | 16 | ±$98.900 | −$3.380 | $2.220 |
| Telbaar of gepland (scheepvaart door Suez en Bab el-Mandeb, bbp Mexico, Codex-resets, openingskoers Anthropic) | 24 | ±$4.700 | **−$89** | **$3.730** |

**Wat dit betekent:**
- In de rustige, telbare markten werd bijna niets gevuld en ging bijna niets verloren, terwijl daar de grootste helft van de beloning lag. Daar betaalt Polymarket dus vooral voor het laten liggen, niet voor het risico (GEZIEN als som over 24 markten).
- In nieuwsmarkten verliezen makers meer dan de hele beloning. Een bot moet die markten mijden of daar heel ver van het midden staan (GEZIEN).
- Samen met run 3 (in jonge markten zou een order van $200 een mediaan van 32% van de pot krijgen): de gok "5 tot 20% van het model" uit run 3 was vooral bang voor verlies op vullingen. Dat verlies blijkt in rustige markten klein. **De grootste onzekerheid is nu de concurrentie, niet het verlies** (GOK, met reden: als het in de cijfers zo makkelijk is, zullen anderen het ook doen).

**Kanttekeningen (eerlijk):**
- De beloning per dag heb ik van nu genomen; of die in de eerste 2 dagen even hoog was, weet ik niet (GOK).
- De prijsreeks is een punt per 10 minuten, niet het echte midden op het moment zelf; dat geeft ruis, maar geen vaste kant op (GOK).
- Dit zijn alle makers samen. Een beloningsbot die vlakbij het midden staat wordt eerder gevuld dan iemand ver weg, dus zijn verlies per dollar kan hoger zijn dan het gemiddelde (GOK).
- 40 markten, 2 dagen, één week van het jaar. Klein.

**Bijgestelde som (GOK, vervangt die van run 3):** alleen rustige, telbare markten jonger dan 2 dagen, $2.000 tot $5.000 aan orders. Als je daar 10 tot 30% van het modelbedrag uit run 3 haalt (in plaats van 5 tot 20%) en het verlies op vullingen 10% van de beloning is: grofweg **$150 tot $900 per dag** bruto, $13.000 tot $80.000 over 90 dagen. Dat bovenste getal is niet geloofwaardig zolang niemand het met bewijs laat zien; het onderste ligt rond het doel. De schaduwbot (run 3) blijft de goedkope toets, nu met een duidelijke regel: alleen telbare of geplande markten, nooit peilingen of roddel.

### 16. Kalshi is geen uitweg voor Nederland
- Kalshi heeft een eigen beloning voor liquiditeit tot 1 jan 2027, maar **"International, non-U.S. users (ineligible for rewards)"** (GEZIEN, [Kalshi Help, Liquidity Incentive Program](https://help.kalshi.com/incentive-programs/liquidity-incentive-program)). Voor iemand in Nederland valt die route dus af.
- Kalshi heeft in Nederland ook geen vergunning; het kreeg nog geen sanctie zoals Polymarket, maar de Ksa zegt dat vergelijkbare sites ook onder haar toezicht vallen (DERDEN, [Bright](https://www.bright.nl/nieuws/2123798/kalshi-mag-op-deze-plek-geen-weddenschappen-meer-aanbieden.html), [Cointelegraph, 5 mei 2026](https://cointelegraph.com/news/kalshi-hyperliquid-offer-prediction-markets-to-dutch-users-despite-polymarket-ban)).
- Volgens het FD (via Cointelegraph, DERDEN) bieden ook Hyperliquid en Interactive Brokers voorspellingsmarkten aan Nederlanders aan; Interactive Brokers noemt ze financiële contracten. Of daar een beloning voor liquiditeit bestaat, nog niet nagekeken.

### Nog te doen (volgende runs)
1. Hyperliquid-voorspellingsmarkten en ForecastTrader van Interactive Brokers: is er een beloning voor makers, hoe groot, en zijn de boeken leeg? Dat zou dezelfde route zijn met minder grijs (Interactive Brokers) of zonder VPN (Hyperliquid, GOK).
2. Concurrentie meten: in een paar nieuwe telbare Polymarket-markten elk kwartier het boek binnen 4,5 cent lezen in de eerste uren, om te zien hoe snel andere bots erbij komen.
3. Belasting op winst bij voorspellingsmarkten en doorverkoop (staat nog open sinds run 1).

---

## Stand na run 04:55 (19 nov, Nederlandse tijd)
**Vijf belangrijkste dingen tot nu toe**
1. Kapitaal-arbitrage (beurzen, driehoek, funding) haalt met weinig geld nooit €10.000 in 3 maanden: 0,007% verschil op BTC tegen 0,2 tot 0,8% kosten, funding 3 tot 11% per jaar (GEZIEN, run 1).
2. Polymarket betaalt ±$75.700 per dag aan wie orders laat liggen; in markten jonger dan 2 dagen zou een nieuwe order van $200 een mediaan van 32% van de pot krijgen (GEZIEN, run 2 en 3).
3. **Nieuw:** het verlies op vullingen in de eerste 48 uur is in rustige, telbare markten klein: makers samen −$89 tegen $3.730 beloning in 24 markten; in nieuws- en peilingmarkten −$3.380 tegen $2.220 (GEZIEN, eigen meting op 40 markten). Een bot die alleen telbare, geplande markten pakt, ontloopt het grootste risico.
4. Het is grijs: Polymarket is in Nederland verboden (VPN, saldo niet af te dwingen), en Kalshi geeft buitenlanders geen beloning (GEZIEN). Een schaduwbot zonder account kan het gratis een week toetsen.
5. Tweedehands blijft de schone route, maar schaalt met uren: €60 tot €100 per telefoon, 8 tot 13 per week voor het doel (GOK op marge, prijzen GEZIEN).

**Rangorde op kans maal opbrengst richting €10.000 in 3 maanden** (alle kansen GOK, met reden)
| # | Route | Inleg geld / uren per week | Kans op €10.000 | Ergste geval |
|---|---|---|---|---|
| 1 | Polymarket: beloning pakken in telbare of geplande markten jonger dan 2 dagen, eigen bot, nooit nieuws of peilingen | €2.000 tot €5.000 / 15+ bouwen, daarna 5 tot 10 | 25 tot 35% (verlies op vullingen nu gemeten en klein; concurrentie en echte vulkans onbekend) | saldo bevroren, niet af te dwingen in NL; een fout in de bot laat orders staan bij nieuws |
| 2 | Tweedehands doorverkopen met een zoekbot (Marktplaats) | €1.000 tot €2.000 / 20 tot 30 | 15 tot 25% | gestolen of kapot toestel, voorraad, blokkade |
| 3 | Voorspellingsmarkten: gaten tussen Kalshi en Polymarket | €1.000 tot €5.000 / 20+ | 2 tot 5% | markten beslissen anders, beide kanten kwijt |
| 4 | Sportarbitrage en bonussen in Nederland | €1.000 tot €3.000 / 5 tot 10 | onder 5% (plafond ±€4.000) | accounts beperkt |
| 5 | Kalshi-beloning | n.v.t. | 0% (buitenlanders uitgesloten, GEZIEN) | n.v.t. |
| 6 | Odd-lot tenders, kleine promoties | een paar honderd / 1 | rond 0% | bod ingetrokken |
| 7 | Funding-arbitrage | groot kapitaal / 2 | rond 0% met weinig geld | beurs valt om, liquidatie |
| 8 | Spot- en driehoeksarbitrage, CS2-skins, kaartjes, airdrops, opkopers | n.v.t. | rond 0% | kosten en tijd kwijt |

Verschil met run 3: route 1 stijgt van 15 tot 25% naar 25 tot 35% omdat het verlies op vullingen nu gemeten is en in rustige markten klein blijkt. Hij blijft grijs; wie dat niet wil, kijkt naar route 2, of wacht op punt 1 van "nog te doen" (Interactive Brokers en Hyperliquid).

---

## Run 5 (19 nov, ±05:25 tot 06:00 Nederlandse tijd)
Deze run: punt 1 en 2 van "nog te doen" uit run 4. Zijn Hyperliquid (HIP-4) en Interactive Brokers een minder grijze plek voor dezelfde route? En hoeveel concurrentie zit er nu in jonge Polymarket-markten, per soort markt?

### 17. Hyperliquid HIP-4: groot geworden, nul kosten, maar al strak bezet
**Gemeten (GEZIEN, `api.hyperliquid.xyz/info` met type `outcomeMeta`, `l2Book` op munt `#<10 × outcome>` en `candleSnapshot`, geen account, 19 nov ±04:25 UTC):**
- Niet meer alleen een dagelijkse BTC-markt (zoals B in een eerdere run zag): nu **303 uitkomsten en 27 vragen** met meerdere uitkomsten. Vooral sport (voetbalwedstrijden, kampioenen van Premier League, Champions League, NFL, NBA), koersmarkten op aandelen en grondstoffen, beursgangen en de Fed-beslissing van december.
- Handel over de afgelopen 7 dagen op de uitkomsten die nu open staan: **±$13 miljoen** (GEZIEN, benadering: aantal contracten maal slotprijs per dag). Grootste: "Arsenal wint de Premier League" ±$1,8 miljoen.
- **Kosten nul** "for initial testing" (GEZIEN, [HIP-4 docs](https://hyperliquid.gitbook.io/hyperliquid-docs/hyperliquid-improvement-proposals-hips/hip-4-outcome-markets.md)).
- **Maar de boeken zijn al strak:** in de drukke markten zit tussen bod en laat **0,001 cent** (bijv. Juventus wint: 0,72199 tegen 0,722; Arsenal kampioen: 0,75485 tegen 0,75486), met $3.000 tot $7.000 binnen 1 cent van het midden (GEZIEN). De prijzen liggen precies op het midden van Polymarket (Man City tegen Fulham: Hyperliquid 0,6975, Polymarket 0,69 tot 0,70, GEZIEN). Er zit dus een professionele market maker die Polymarket volgt.
- **Geen beloning voor makers** gevonden in de docs (GEZIEN, niet genoemd). Met nul kosten en een spread van 0,001 cent valt er voor een kleine maker niets te halen.
- **Binnen-vraag-arbitrage:** bij 19 voetbalwedstrijden telden de laatprijzen van winst, gelijk en verlies op tot 0,9987 tot 1,0046 (GEZIEN). Onder 1 lijkt gratis geld, maar het gat (±0,07 cent) is precies de prijs van de vierde uitkomst "anders" (wedstrijd gestaakt), die geen boek heeft. Geen echte arbitrage.
- **Tussen platforms:** één echt verschil gevonden. Fed december "verhoging": Hyperliquid laat 0,955, Polymarket bod op "25 bps omhoog" plus "50+ bps omhoog" samen ±0,972 (GEZIEN, beide openbaar). Dat is ±1,7 cent, maar op Hyperliquid stond maar 46 tot 60 contracten aan de beste prijs, het geld zit vast tot de beslissing, en de regels verschillen mogelijk (Hyperliquid kijkt naar de bovengrens van de rente-band). Een paar dollar, geen route.

**Wat dit wel betekent:** Hyperliquid is nu de **goedkoopste plek om in te dekken**. Wie op Polymarket als maker gevuld wordt in een vraag die ook op Hyperliquid staat, kan die positie daar zonder kosten en tegen het eerlijke midden wegzetten. Dat haalt het grootste risico uit run 4 (verlies op vullingen) weg. Helaas: op Polymarket hebben juist die overlappende markten nauwelijks beloning. 21 voetbalwedstrijden: **$0 beloning** per dag; Champions League-, NFL- en NBA-kampioen samen ±$44 per dag (GEZIEN). Alleen Fed december heeft veel beloning ($1.050 per dag, GEZIEN), maar daar zou een order van 200 aandelen **0,04 tot 0,07%** van de pot krijgen, dus minder dan $1 per dag (GEZIEN, eigen model). Oude, grote markten zijn vol.
**Nederland:** Hyperliquid vraagt geen KYC en heeft geen vergunning; de Ksa noemde vergelijkbare sites (DERDEN, run 4). Grijs, net als Polymarket, maar zonder VPN (GOK).

### 18. Interactive Brokers (ForecastEx): schoon, maar geen route
- ForecastEx-contracten geven een **"incentive coupon" van 3,38% per jaar** over de waarde van je posities, dagelijks opgebouwd, maandelijks uitbetaald (GEZIEN, [IBKR Ireland, Event Contracts](https://www.interactivebrokers.ie/en/trading/products-event-contracts.php)). Kosten **$0,00 commissie plus $0,01 beursvergoeding per contract** (GEZIEN, [IBKR Ireland, commissies](https://www.interactivebrokers.ie/en/pricing/commissions-events.php)). Beschikbaarheid hangt af van land en IBKR-dochter (GEZIEN, zelfde pagina).
- Een beloning voor wie orders laat liggen, zoals bij Polymarket, vond ik niet. 3,38% per jaar is rente, geen route naar €10.000.
- **Waar het wel past:** als legale tweede kant voor arbitrage tegen Hyperliquid of Polymarket op dezelfde economische vraag (Fed, inflatie). Prijzen van ForecastEx zijn zonder account niet openbaar uit te lezen gevonden in deze run, dus niet gemeten.

### 19. Concurrentie in jonge Polymarket-markten, per soort (eigen meting)
**Werkwijze (GEZIEN, openbare API's, 19 nov ±04:30 UTC, twee keer gemeten):** alle markten met beloning van $10 of meer per dag die jonger zijn dan 48 uur (`clob.polymarket.com/rewards/markets/multi` voor de leeftijd, `/rewards/markets/current` voor de pot, `/books` voor het boek): 414 tot 420 markten. Per markt dezelfde puntentelling als run 3, met een nieuwe order van 200 aandelen aan beide kanten op 1 cent van het midden. Nieuw: apart gekeken naar markten met een **strak boek** (spread hoogstens 5 cent), omdat een "lege" markt (bod 0,01, laat 0,99) wel 100% aandeel geeft, maar niemand weet wat de echte prijs is; daar word je meteen leeggehaald.

| Leeftijd | Markten | Waarvan boek leeg (spread > 20 cent) | Strak boek: mediaan aandeel | Strak boek: mediaan $ per dag per $200 |
|---|---|---|---|---|
| 0 tot 12 uur | 124 tot 126 | ±94 van 122 | 46% (11 markten) | $23 |
| 12 tot 24 uur | 116 tot 128 | 3 | 52% (95 markten) | $11 |
| 24 tot 48 uur | 147 tot 162 | 42 | 61% (70 markten) | $14 |

(GEZIEN, eigen model; de tweede meting gaf hetzelfde beeld: 52 en 61% op dezelfde 176 markten.) Dit is lager per markt dan de $62 uit run 3, omdat ik nu ook de kleinere potten ($10 tot $50) meetel; het aandeel is vergelijkbaar of hoger.

**Per soort markt (GEZIEN, zelfde meting):**
| Soort | Markten < 48 uur | Pot per dag | Strak boek | Mediaan aandeel | Som als je overal $200 zet |
|---|---|---|---|---|---|
| Temperatuur per stad | 200 | $5.347 | 129 | 64% | $1.780 per dag |
| Streamers die GTA VI uitspelen | 31 | $3.801 | 10 | 47% | $575 per dag |
| Senaat (dagvaarding) | 9 | $450 | 7 | 47% | $174 per dag |
| Box office openingsweekend | 24 | $297 | 0 | n.v.t. (alle boeken leeg) | n.v.t. |
| Tweets en posts tellen | 10 | $176 | 5 | 24% | $24 per dag |

**De belangrijkste ontdekking van deze run:** de grootste pot in jonge markten zit in **temperatuurmarkten**: 200 markten, $5.347 per dag, en twee derde heeft een strak boek waar een order van $200 nu het grootste deel van de beloning zou pakken (GEZIEN). Die markten zijn telbaar: ze worden beslist op één meetstation (bijv. Londen: de hoogste uurwaarde in de METAR van London City Airport, GEZIEN in de marktregels), en er bestaat gratis weerdata (Open-Meteo, ECMWF-ensemble, zonder account).
Dat maakt een betere bot mogelijk dan "orders rond het midden van het boek": een bot die **zijn eigen eerlijke prijs uit de weerverwachting** haalt, daar omheen orders zet voor de beloning, en dus minder vaak aan de verkeerde kant gevuld wordt.
- Eén proef, geen bewijs (GEZIEN): Londen, hoogste temperatuur 20 nov. Markt: 10°C ±54%, 9°C ±34%. Ruwe ECMWF-ensemble (51 leden, rasterpunt bij London City): 9°C 61%, 10°C 22%, 8°C 18%. Groot verschil, maar ruwe modeldata hebben een afwijking per station (en de METAR meet per uur, niet het echte maximum). Zonder terugtest op afgelopen weken zegt dit niets over wie gelijk heeft.
- Er wordt aantoonbaar verdiend in deze markten: account gopfan2 **$1,48 miljoen** winst over 18 maanden volgens PolymarketAnalytics (DERDEN, via [PrintMoneyLab](https://www.printmoneylab.com/2026/03/weather-bot-episode-1-betting-on-temperature-polymarket.html)); neobrother ruim **$20.000** met een "ladder" van goedkope temperaturen (DERDEN, [KuCoin/Odaily](https://www.kucoin.com/news/flash/traders-on-polymarket-earn-millions-by-predicting-weather)). Zoeker A vond dat favorieten vlak voor sluiten te duur zijn in weermarkten (DERDEN, arXiv in `A-strategie-en-testen.md`). Dat zijn winnaars die bovenaan staan; verliezers schrijven geen blogs.
- **Valt af:** twee accounts verdienden $37.000 aan vreemde pieken bij het meetstation van Parijs, met vermoeden van geknoei aan de meting (DERDEN, [Blockchain.News](https://blockchain.news/news/polymarket-paris-weather-glitch)). Aan een meetstation zitten is fraude en marktmanipulatie.

**Som (GOK):** temperatuurmarkten alleen, $200 per markt in ±40 tot 60 markten tegelijk (een paar steden, elke dag nieuwe), dus $8.000 tot $12.000 aan orders. Model: rond $500 tot $700 per dag. Neem daar net als in run 4 10 tot 30% van: **$50 tot $200 per dag, $4.500 tot $18.000 in 90 dagen**. Met $2.000 tot $5.000 inleg de helft daarvan. Het verlies op vullingen hoort klein te zijn als de eigen prijs goed is, en groot als hij slecht is: precies dat moet de schaduwbot eerst meten.

### Nog te doen (volgende runs)
1. Terugtest weer: voor 5 steden de ruwe ensemble-verwachting van de dag ervoor tegen de echte METAR-uitslag van de afgelopen weken (Open-Meteo heeft archief, aviationweather.gov heeft de METAR). Zo weet je of de eigen prijs beter is dan het boek, en welke afwijking per station je moet corrigeren.
2. Prijsgeschiedenis van afgelopen temperatuurmarkten (`clob.polymarket.com/prices-history`) naast de uitslag: hoeveel zou een maker met de beloning verdiend en op vullingen verloren hebben (zelfde aanpak als run 4, nu alleen weer).
3. Belasting op winst bij voorspellingsmarkten en doorverkoop (staat nog open sinds run 1).

---

## Stand na run 06:00 (19 nov, Nederlandse tijd)
**Vijf belangrijkste dingen tot nu toe**
1. Kapitaal-arbitrage (beurzen, driehoek, funding, sport-overlap tussen Hyperliquid en Polymarket) haalt met weinig geld nooit €10.000 in 3 maanden: 0,007% verschil op BTC tegen 0,2 tot 0,8% kosten, funding 3 tot 11% per jaar (GEZIEN, run 1); Hyperliquid HIP-4 heeft spreads van 0,001 cent en volgt Polymarket precies (GEZIEN, run 5).
2. Het enige "geld voor werk" dat niet van gelijk hebben afhangt: de beloning van Polymarket voor wie orders laat liggen, ±$75.500 per dag (GEZIEN). In grote oude markten krijgt een kleine order bijna niets (Fed december: 0,04 tot 0,07%, GEZIEN); in markten jonger dan 48 uur met een strak boek 46 tot 61% (GEZIEN, run 5).
3. **Nieuw:** de grootste pot in jonge markten zit in temperatuurmarkten: 200 markten, $5.347 per dag, 64% mediaan aandeel voor een order van $200 (GEZIEN). Ze zijn telbaar met gratis weerdata, en er wordt aantoonbaar verdiend ($1,48 miljoen en $20.000, DERDEN). Dat maakt "beloning pakken met een eigen weer-prijs" de scherpste vorm van route 1.
4. Er is geen schone uitweg voor Nederland: Polymarket verboden, Hyperliquid zonder vergunning, Kalshi geeft buitenlanders geen beloning (run 4), Interactive Brokers geeft alleen 3,38% coupon en geen makerbeloning (GEZIEN). Route 1 blijft grijs: saldo kan bevroren worden en is in Nederland niet af te dwingen (DERDEN, run 2).
5. Tweedehands blijft de schone route, maar schaalt met uren: €60 tot €100 per telefoon, 8 tot 13 per week voor het doel (GOK op marge, prijzen GEZIEN, run 2).

**Rangorde op kans maal opbrengst richting €10.000 in 3 maanden** (alle kansen GOK, met reden)
| # | Route | Inleg geld / uren per week | Kans op €10.000 | Ergste geval |
|---|---|---|---|---|
| 1 | Polymarket: beloning pakken in temperatuurmarkten (en andere telbare markten < 48 uur) met een eigen bot die zijn prijs uit weerdata haalt; nooit nieuws, peilingen of lege boeken | €2.000 tot €5.000 / 15 tot 20 bouwen, daarna 5 tot 10 | 25 tot 35% (pot en aandeel GEZIEN; of de weer-prijs beter is dan het boek is nog niet getest) | saldo bevroren, niet af te dwingen in NL; slechte eigen prijs zorgt voor verlies op elke vulling |
| 2 | Tweedehands doorverkopen met een zoekbot (Marktplaats) | €1.000 tot €2.000 / 20 tot 30 | 15 tot 25% | gestolen of kapot toestel, voorraad, blokkade |
| 3 | Voorspellingsmarkten: gaten tussen platforms (Polymarket, Hyperliquid, Kalshi, ForecastEx) | €1.000 tot €5.000 / 20+ | 1 tot 3% (zakt: Hyperliquid volgt Polymarket tot op 0,001 cent, GEZIEN) | markten beslissen anders, beide kanten kwijt |
| 4 | Sportarbitrage en bonussen in Nederland | €1.000 tot €3.000 / 5 tot 10 | onder 5% (plafond ±€4.000) | accounts beperkt |
| 5 | Hyperliquid HIP-4 als maker | n.v.t. | rond 0% (geen beloning, spread 0,001 cent, GEZIEN) | n.v.t. |
| 6 | Kalshi-beloning, ForecastEx-coupon | n.v.t. | 0% (buitenlanders uitgesloten; 3,38% per jaar, GEZIEN) | n.v.t. |
| 7 | Odd-lot tenders, kleine promoties | een paar honderd / 1 | rond 0% | bod ingetrokken |
| 8 | Funding-arbitrage | groot kapitaal / 2 | rond 0% met weinig geld | beurs valt om, liquidatie |
| 9 | Spot- en driehoeksarbitrage, CS2-skins, kaartjes, airdrops, opkopers | n.v.t. | rond 0% | kosten en tijd kwijt |

Verschil met run 4: route 1 blijft op 25 tot 35% maar is scherper: het meeste geld in jonge markten zit in temperatuur, en daar kan een bot een eigen prijs maken. Hyperliquid en Interactive Brokers vallen af als minder grijze kopie; Hyperliquid is wel nuttig om gratis in te dekken als een vraag op beide staat. Gaten tussen platforms zakken van 2 tot 5% naar 1 tot 3%.
