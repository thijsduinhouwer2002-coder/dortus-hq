# A. Kant-en-klare AI-handelsbots en platforms

Onderzoek voor Thijs zelf (geen Dortus-product). Alleen algemene informatie over tools; niets over zijn geld of accounts.
Labels: GEZIEN = zelf gelezen op de bron (link), DERDEN = iemand anders zegt het (link), GOK = eigen inschatting.

## Run 1 (18 nov 2026, nacht)

### 1. De belangrijkste les eerst: de bot is niet waar je geld staat
Een kant-en-klare bot (3Commas, Cryptohopper, Bitsgap en dergelijke) is meestal alleen software. Hij praat via een API-sleutel met een beurs. Je geld staat op die beurs. Dus de vraag "is dit veilig en legaal in Nederland" gaat vooral over **de beurs**, en pas daarna over de bot. (GOK, volgt uit hoe deze diensten werken; Pionex is de uitzondering: dat is zelf een beurs met bots erin.)

### 2. Welke beurzen mogen in Nederland (MiCA)
Sinds MiCA mag alleen een beurs met een CASP-vergunning klanten in de EU bedienen. De overgangsperiodes zijn voorbij: uiterlijk 1 juli 2026 overal in de EU (DERDEN, [casptracker.eu Binance](https://casptracker.eu/exchange/binance/)). Ik heb het officiële ESMA-register zelf gedownload ([ESMA CASPS.csv](https://www.esma.europa.eu/sites/default/files/2024-12/CASPS.csv), 409 regels, laatste wijziging in het bestand 30 sep 2026; GEZIEN).

In het register (GEZIEN, zelfde bestand):
- **Bitvavo** (vergunning AFM, 26 jun 2025)
- **Kraken** (Ierland, 25 jun 2025)
- **Coinbase** (Luxemburg, 20 jun 2025)
- **Bybit EU** (Oostenrijk, 28 mei 2025)
- **OKX Europe** (Malta, 27 jan 2025)
- **Bitpanda** (Oostenrijk, Duitsland, Malta)
- **Crypto.com** (Malta), **Gate** (Malta), **KuCoin EU** (Oostenrijk, 27 nov 2025)
- **eToro Europe** (Cyprus, 16 jan 2025), **Revolut** (Cyprus, 20 okt 2025)
- Nederlandse partijen o.a. BLOX, Finst, Bitonic, BTC Direct, Coinmerce, Amdax, One Trading

**Niet** in het register (GEZIEN, 0 treffers): **Pionex, Bitget, Binance, MEXC, HTX**.
- Bitget: aanvraag bij de Oostenrijkse FMA ingediend (bevestigd 2 jul 2026), nog geen vergunning; Duitsland, Frankrijk en Oostenrijk staan in hun voorwaarden als verboden landen (DERDEN, [casptracker.eu Bitget](https://casptracker.eu/exchange/bitget/), gelezen 18 nov 2026).
- Binance: geen MiCA-vergunning per 18 nov 2026 (DERDEN, [casptracker.eu Binance](https://casptracker.eu/exchange/binance/)). Er was eind oktober 2026 ook een grote hack bij Binance (DERDEN, [accountant.nl](https://www.accountant.nl/nieuws/2026/11/afm-wijst-aanbieders-van-crypto-op-europese-regels/), kopje "Gerelateerd").
- Pionex: zie hieronder.

Gevolg (GOK): copy trading bij Bitget, of de gratis bots van Pionex of Binance, is voor iemand in Nederland nu een platform zonder Europese vergunning. Bij een probleem heb je dan geen toezichthouder om op terug te vallen.

### 3. Per platform

**Pionex** (beurs met ingebouwde bots)
- Wat: eigen beurs met 16+ gratis bots (grid, DCA, herbalanceren, spot-futures-arbitrage); 0,05% kosten per order, maker en taker (DERDEN, [blockport.io review, nov 2025](https://blockport.io/spot-trading/pionex-review/), zij openden een account en deden testorders van 200 dollar).
- Vergunning: noemt zelf een Amerikaanse MSB-registratie (DERDEN, zelfde link). Geen MiCA (GEZIEN, ESMA-register).
- Rode vlaggen: meldingen van vertraagde opnames in de community; diepte van de markt dunt uit bij snelle koersen (DERDEN, zelfde link). Hun voorwaardenpagina is achter een Cloudflare-muur, kon ik niet lezen (GEZIEN).
- Oordeel: technisch het makkelijkst, juridisch het zwakst voor Nederland (GOK).

**Bitsgap** (bot-software, koppelt aan beurzen)
- Prijzen (GEZIEN, [bitsgap.com/pricing](https://bitsgap.com/pricing), 18 nov 2026): Basic 23 dollar per maand bij jaarbetaling (29 per maand los), Advanced 55 (69), Pro 119 (149). 7 dagen gratis proberen. Gratis plan met demo-bots.
- Terugtesten: 30, 180 of 365 dagen afhankelijk van het plan (GEZIEN, zelfde pagina). Heeft een "AI Chat" en een "AI Portfolio Mode" (GEZIEN); hoe goed die werkt is onbekend.
- Vergunning: geen; als pure software is dat ook niet nodig (GOK). Belangrijk is aan welke beurs je hem koppelt.

**3Commas** (bot-software)
- Prijs: hun prijspagina laadt alleen met JavaScript, niet gelezen. Nog na te kijken.
- Rode vlag, belangrijk: in december 2022 werden API-sleutels van gebruikers gelekt. Volgens ZachXBT verloren 44 geverifieerde slachtoffers samen 14,8 miljoen dollar door ongeautoriseerde trades; gebruikers zochten een groepsrechtszaak (DERDEN, [Unchained, 21 dec 2022](https://unchainedcrypto.com/3commas-users-plan-class-action-lawsuit-after-losing-14m/)). Er is ook een aanklacht ingediend (DERDEN, [Freeman v 3Commas, PDF](https://truthinadvertising.org/wp-content/uploads/2024/03/Freeman-v-3Commas-Technologies-complaint.pdf), niet zelf gelezen).
- Les (GOK): ook bij een bekende bot is je API-sleutel het zwakke punt. Altijd een sleutel zonder opnamerecht en met IP-beperking.

**Cryptohopper** (bot-software)
- Nog niet onderzocht deze run; prijspagina laadt alleen met JavaScript.

**eToro copy trading**
- eToro Europe staat in het MiCA-register voor crypto (GEZIEN, ESMA). Hun Nederlandse en Engelse homepage gaf met curl geen leesbare risicotekst (GEZIEN). Het percentage verliezende CFD-klanten nog opzoeken.

### 4. Grok en andere chatbots als "handelsbot": wat zeggen echte tests
- **Er bestaat geen officiële Grok-handelsbot van xAI** die je kunt kopen of aanzetten (GOK, ik vond geen enkele bron daarvoor; wel tientallen sites die de naam gebruiken, zie oplichting).
- Alpha Arena (nof1) liet chatbots echt geld beheren. Seizoen 1 (okt-nov 2025, crypto, elk 10.000 dollar): Qwen3 eindigde op 12.231, DeepSeek 10.489, Claude Sonnet 4.5 5.799, Gemini 2.5 Pro 5.445, Grok 4.208, GPT-5 4.126 (DERDEN, [ForkLog, 8 dec 2025](https://forklog.com/en/news/ai-model-grok-4-2-triumphs-in-trading-tournament)). Dus vier van de zes verloren 40% of meer in een paar weken.
- Seizoen 1.5 (Amerikaanse aandelen, twee weken): Grok 4.2 won met gemiddeld +12% (DERDEN, zelfde link). Maar in totaal maakten maar 6 van de 32 uitslagen winst, en de hele pot zakte ongeveer een derde (DERDEN, [KuCoin/CoinDesk, 6 mei 2026](https://www.kucoin.com/news/flash/ai-trading-models-struggle-in-live-market-tests-majority-of-systems-report-losses)).
- De oprichter van nof1 zegt zelf: het is nog niet haalbaar om een taalmodel je geld te geven en het zelf te laten handelen (DERDEN, zelfde link).
- Wat er op TikTok en X rondgaat als "Grok verdiende X%" is meestal één winnende ronde uit zo'n test, zonder de verliezende rondes (GOK, past bij de cijfers hierboven).
- Extra risico: in mei 2026 werd Grok via een in morsecode verstopte opdracht misleid om een andere bot (Bankrbot) tokens ter waarde van ongeveer 200.000 dollar te laten overmaken (DERDEN, [Breitbart, 7 mei 2026](https://www.breitbart.com/tech/2026/05/07/ai-nightmare-scammer-tricks-grok-and-bankr-ai-bot-into-200k-crypto-transfer-using-morse-code/)). Een AI met toegang tot een wallet kan door anderen worden bespeeld.

### 5. Oplichting: bekende namen en patronen
- Sites die "Grok" in de naam gebruiken en door scanners of toezichthouders als verdacht zijn aangemerkt: "X Trade Grok 9.1 Nova" (IOSCO-waarschuwing, DERDEN, [IOSCO I-SCAN](https://www.iosco.org/i-scan/index.cfm?id=51747); pagina blokkeerde curl), groktrading.net, grokx.trade, tradegrok.net (DERDEN, [Gridinsoft](https://gridinsoft.com/online-virus-scanner/url/groktrading-net)), grok-trader.com (DERDEN, [scam-detector](https://www.scam-detector.com/validator/grok-trader-com-review/)), Grokrhot3 (DERDEN, [malwaretips](https://malwaretips.com/blogs/?p=350926)).
- Andere waarschuwingen: "Ai Trader Bot" (DERDEN, [FCA](https://www.fca.org.uk/news/warnings/ai-trader-bot)), "Autobot Traders", "AI Chain Trader", "Wisebit AI" (DERDEN, IOSCO-lijst, links in de zoekresultaten: [Autobot](https://www.iosco.org/i-scan/index.cfm?id=51664), [AI Chain Trader](https://www.iosco.org/i-scan/?id=37895), [Wisebit](https://www.iosco.org/i-scan/?id=40385)), "Alpha AI" (DERDEN, [Finanstilsynet Noorwegen](https://www.finanstilsynet.no/markedsadvarsler/2026/alpha-ai-1792541166/)).
- Patroon: nep-platform toont een groeiend saldo, opnemen lukt niet; vaak via WhatsApp- of Telegramgroepen met nep-papieren van toezichthouders. De SEC klaagde in 2026 firma's aan voor zo'n schema van ruim 15 miljoen dollar (DERDEN, [WealthManagement](https://www.wealthmanagement.com/regulation-compliance/sec-charges-two-firms-with-15m-crypto-fraud-scheme)). De AFM waarschuwt voor oplichting via chatgroepen en voor "onrealistische winstbeloftes op sociale media" (DERDEN, [accountant.nl, 6 nov 2026](https://www.accountant.nl/nieuws/2026/11/afm-wijst-aanbieders-van-crypto-op-europese-regels/); [bijzonderstrafrecht.nl](https://www.bijzonderstrafrecht.nl/home/afm-waarschuwt-beleggers-doelwit-van-oplichting-via-chatgroepen)).
- De AFM-waarschuwingslijst zelf laadt alleen met JavaScript; met curl kon ik er niet in zoeken (GEZIEN). Zelf checken op afm.nl voor je ergens geld stort.

### 6. Snelle toets voor elke bot die je ziet (GOK, samengevat uit het bovenstaande)
1. Staat de beurs waar het geld komt in het ESMA-register? Zo niet: niet doen.
2. Moet je geld naar de bot zelf sturen (in plaats van alleen een API-sleutel geven)? Dan is het geen bot-software maar een fonds of oplichting.
3. Belooft hij een vast rendement per dag of maand? Rode vlag.
4. Kun je hem gratis op papier of met terugtesten proberen? Echte tools kunnen dat (Bitsgap, Pionex).
5. API-sleutel altijd zonder opnamerecht.

### Nog te doen (volgende runs)
- 3Commas en Cryptohopper: prijzen, huidige stand, gebruikerservaringen (Trustpilot, Reddit).
- Hebben de MiCA-beurzen zelf bots? (OKX en Bybit hebben wereldwijd bots; geldt dat ook voor OKX Europe en Bybit EU? Bitvavo?)
- TradingView-koppelingen (signalen naar een beurs sturen).
- eToro: percentage verliezende klanten, kosten van copy trading, CopyPortfolios.
- Wat er concreet op TikTok gepromoot wordt (namen van apps).

## Stand na run 1 (18 nov 2026)
1. In Nederland mogen alleen beurzen met MiCA-vergunning; Pionex, Bitget en Binance hebben die niet (GEZIEN in het ESMA-register). Bitvavo, Kraken, Coinbase, Bybit EU, OKX Europe, Bitpanda en eToro wel.
2. Een bot als Bitsgap of 3Commas is alleen software; het risico zit in de beurs en in je API-sleutel. Bij 3Commas lekten in 2022 sleutels en verloren 44 mensen samen 14,8 miljoen dollar (DERDEN).
3. Er is geen officiële Grok-handelsbot. In echte tests met echt geld verloren de meeste chatbots; maar 6 van de 32 uitslagen waren winst (DERDEN).
4. "Grok" in de naam van een handelssite is vooral een teken van oplichting: meerdere waarschuwingen en verdachte domeinen gevonden.
5. Veiligste start (GOK): een MiCA-beurs, een bot-tool met gratis demo en terugtesten, eerst op papier, en een API-sleutel zonder opnamerecht.
