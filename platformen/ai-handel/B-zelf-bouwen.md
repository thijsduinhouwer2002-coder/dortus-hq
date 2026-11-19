# B. Zelf een handelsbot bouwen met AI: gereedschap en bouwplan

Onderzoek voor Thijs zelf (geen Dortus-product). Alleen algemene informatie over tools; niets over zijn geld of accounts.
Labels: GEZIEN = zelf gelezen op de bron (link), DERDEN = iemand anders zegt het (link), GOK = eigen inschatting.
Taakverdeling (BRIEF, 19 nov): A doet strategie, data en eerlijk testen. B (dit bestand) doet gereedschap, beurzen en API's, kosten, veiligheid en een bouwplan.

## Run 1 (19 nov 2026, nacht)

### 1. De kern in één alinea
Laat de AI (Grok, Claude, ChatGPT) **niet zelf handelen**. Gebruik hem als programmeerhulp om een strategie te schrijven in een bestaand, bewezen open source framework (Freqtrade is voor crypto in Nederland de logische keus). Dat framework regelt de saaie, gevaarlijke delen: orders, stop-loss, terugtesten, op papier handelen, en de koppeling met de beurs. Eigen code vanaf nul laten schrijven door een chatbot is waar de fouten en verliezen zitten. (GOK, volgt uit wat hieronder staat.)

### 2. Frameworks (code gelezen op GitHub en de docs, niets uitgevoerd)

**Freqtrade** (crypto, Python, gratis)
- Gratis en open source, licentie GPLv3; nieuwste versie 2026.10 van 30 okt 2026 (GEZIEN, [PyPI freqtrade](https://pypi.org/pypi/freqtrade/json)).
- Heeft alles wat je nodig hebt: dry-run (op papier met echte koersen), terugtesten, hyperopt (parameters zoeken), FreqAI (machine learning), bediening via Telegram of een webscherm. De README zegt zelf: "Always start by running a trading bot in Dry-Run and do not engage money" (GEZIEN, [README](https://raw.githubusercontent.com/freqtrade/freqtrade/develop/README.md)).
- Heeft ook ingebouwde controles tegen valsspelen in je eigen test: `lookahead-analysis` en `recursive-analysis` (GEZIEN, commando's in dezelfde README). Dat zijn precies de fouten die AI-code vaak maakt (in een test naar de toekomst kijken).
- Beurzen officieel: o.a. Kraken, Bybit EU, Gate EU, MyOKX (OKX EEA), Binance, Bitget. **Bitvavo** staat bij "confirmed working by the community", dus niet officieel getest (GEZIEN, README).
- Bitvavo-beperking: geen stop-loss op de beurs zelf ("Stoploss on exchange: not available"); de bot moet dan zelf de stop-loss bewaken, dus als de bot of je server uitvalt is er geen stop (GEZIEN, [Freqtrade exchanges](https://www.freqtrade.io/en/stable/exchanges/)). Kraken spot heeft het wel (market en limit) (GEZIEN, zelfde pagina).
- Kraken-beperking voor terugtesten: de API geeft maar 720 historische candles; je moet trades downloaden (`--dl-trades`) of de CSV-bestanden van Kraken gebruiken (GEZIEN, zelfde pagina).

**Jesse** (crypto, Python)
- Kern MIT-licentie (GEZIEN, [LICENSE](https://raw.githubusercontent.com/jesse-ai/jesse/master/LICENSE)); versie 3.6.1 op PyPI (GEZIEN, [PyPI jesse](https://pypi.org/pypi/jesse/json)).
- Nieuw en relevant: een **Jesse MCP** waarmee Claude, Codex of Cursor rechtstreeks in je lokale Jesse-project strategieën kan schrijven, terugtesten draaien, optimaliseren en Monte Carlo-tests doen (GEZIEN, [docs.jesse.trade](https://docs.jesse.trade/)).
- Maar: live en papier handelen gaat via een officiële plugin waarvoor je een betaalde licentie nodig hebt ("access is limited to those with an active license") (GEZIEN, [Jesse live trading](https://docs.jesse.trade/docs/livetrade)). Prijs niet kunnen lezen (pagina laadt met JavaScript). Terugtesten is gratis (GOK, volgt uit dat alleen live een licentie vraagt).

**Hummingbot** (market making en arbitrage, Python)
- Apache 2.0, versie van 18 nov 2026 (GEZIEN, [PyPI hummingbot](https://pypi.org/pypi/hummingbot/json)).
- Ondersteunt o.a. Kraken, Coinbase, Bitstamp, OKX, Bybit; **Bitvavo staat niet in de lijst** (GEZIEN, [hummingbot.org/exchanges](https://hummingbot.org/exchanges/)).
- Gemaakt voor market making (veel kleine orders aan beide kanten). Voor een beginner met een kleine pot is dat moeilijk winstgevend door kosten (GOK).

**CCXT** (bibliotheek, geen bot)
- De laag onder Freqtrade die met 100+ beurzen praat (GEZIEN, Freqtrade exchanges-pagina); actief onderhouden, versie 4.5.93 van 17 nov 2026 (GEZIEN, [PyPI ccxt](https://pypi.org/pypi/ccxt/json)). Alleen nodig als je echt alles zelf bouwt.

**TradingAgents** (LLM-agenten, onderzoek)
- Een groep LLM-"analisten", "onderzoekers" en een "trader" die samen een besluit nemen over een aandeel; werkt met Grok (`XAI_API_KEY`), Claude, GPT, Gemini en meer (GEZIEN, [README](https://raw.githubusercontent.com/TauricResearch/TradingAgents/main/README.md)).
- Zegt zelf: "designed for research purposes ... not intended as financial, investment, or trading advice" (GEZIEN, zelfde README). Geen beurskoppeling om echt te handelen; het geeft een advies per aandeel en datum (GOK, op basis van de README).
- Nuttig om te zien hoe je een LLM netjes inzet (alleen data van vóór de besluitdatum, zo staat in hun changelog van sep 2026: "backtests that see only data published by each analysis date") (GEZIEN). Niet als bot om geld aan te geven.

Niet gelukt deze run: sterren en laatste activiteit via de GitHub-API ophalen (die is voor deze sessie dicht; raw-bestanden lezen werkte wel). OctoBot en NautilusTrader nog niet bekeken.

### 3. Beurzen en API's die in Nederland mogen
Welke beurzen een MiCA-vergunning hebben, staat al in `A-kant-en-klaar.md` (Bitvavo, Kraken, Coinbase, Bybit EU, OKX Europe, en andere; Binance, Bitget, Pionex niet). Hier wat de API zelf doet.

**Bitvavo** (Nederlands, AFM-vergunning)
- Kosten bij weinig volume: 0,15% maker, 0,25% taker per order (GEZIEN, [bitvavo.com/en/fees](https://www.bitvavo.com/en/fees)). Er staat ook een tweede tabel met 0,05% en 0,05%; volgens de tekst eronder geldt die voor stablecoins (GOK, de tekst was half afgekapt).
- API-sleutel heeft losse rechten: "View access", "Trade digital assets", "Withdraw digital assets" en nog drie voor subaccounts (GEZIEN, [docs.bitvavo.com llms-full.txt](https://docs.bitvavo.com/llms-full.txt)).
- **Belangrijk:** "Withdrawals made using Bitvavo API do not require 2FA and e-mail confirmation" (GEZIEN, zelfde bron). Zet het opnamerecht dus nooit aan voor een bot.
- IP-whitelist kan per sleutel; Bitvavo zegt zelf dat dat je account beschermt als de sleutel gestolen wordt (GEZIEN, zelfde bron).
- Limiet: standaard 1000 "weight points" per minuut (GEZIEN, zelfde bron). Ruim genoeg voor een bot die per minuut of per uur kijkt (GOK).
- Geen gewone testomgeving (sandbox) voor de REST-API gevonden; alleen een testomgeving voor de FIX-API voor instellingen (GEZIEN, zelfde bron). Papier handelen doe je dus in de bot zelf (Freqtrade dry-run), niet bij Bitvavo.

**Kraken** (MiCA via Ierland)
- Officieel ondersteund door Freqtrade, met stop-loss op de beurs (GEZIEN, zie boven). Kostentabel niet kunnen lezen met curl (laadt met JavaScript); volgende run.

**Aandelen**
- **Alpaca:** papier-account is voor iedereen na aanmelden met e-mail; live voor "195+ countries" (GEZIEN, [Alpaca non-US](https://alpaca.markets/learn/live-trading-account-non-us)). Alpaca Europe (overname WealthKernel, apr 2026) is een **Broker API voor bedrijven**, niet voor particulieren (GEZIEN, [Alpaca blog](https://alpaca.markets/blog/alpaca-expands-into-europe-and-launches-european-equities-trading/) en [Alpaca EU docs](https://docs.alpaca.markets/eu/docs)). Een Nederlander die live handelt via Alpaca US valt dus niet onder Europees toezicht (GOK).
- **Interactive Brokers:** heeft een EU-entiteit en een API (TWS API / IB Gateway) met papier-account; NautilusTrader heeft er een koppeling voor (DERDEN, [IBKR TWS API](https://interactivebrokers.github.io/tws-api/introduction.html), [NautilusTrader IB](https://nautilustrader.io/docs/latest/integrations/ib/)). Nog niet zelf nagelezen.

### 4. Wat kost het (zonder het geld waarmee je handelt)
- Software: Freqtrade, Hummingbot, CCXT gratis (GEZIEN, licenties boven). Jesse live: betaalde licentie (GEZIEN, prijs onbekend).
- Een AI-model in de bot (bijv. om nieuws of posts te lezen): Grok 4.3 kost $1,25 per miljoen invoertokens en $2,50 per miljoen uitvoertokens; Grok 4.7 $2 en $6 (GEZIEN, [docs.x.ai pricing](https://docs.x.ai/developers/pricing.md)). Claude Sonnet 5.5: $2 in, $10 uit (GEZIEN, [Claude pricing](https://platform.claude.com/docs/en/about-claude/pricing.md)).
- Rekenvoorbeeld: één vraag per uur met 5.000 tokens in en 500 uit op Grok 4.3 is ongeveer $0,0075 per vraag, zo'n $5 per maand (GOK, eigen som op de GEZIEN-prijzen).
- Een server die dag en nacht draait: een kleine VPS van een paar euro per maand is genoeg voor Freqtrade (GOK; prijs niet nagelezen). Een laptop die dichtklapt werkt niet, zeker niet op Bitvavo waar de stop-loss in de bot zit.
- **De echte kostenpost zijn de beurskosten.** Bij Bitvavo taker is een rondje kopen en verkopen 0,5% (GEZIEN, 2 x 0,25%). Een bot die elke dag een rondje doet, moet dus ruim 0,5% per dag winnen om quitte te spelen, en meer door slippage (GOK, eigen som). Gebruik limietorders (maker 0,15%) waar het kan en handel weinig.

### 5. Veiligheid
**API-sleutels**
1. Alleen "View" en "Trade" aan; "Withdraw" nooit (GEZIEN dat het bij Bitvavo los kan; zie boven).
2. IP-whitelist aan, met het IP van je server (GEZIEN dat het kan).
3. Een aparte sleutel per bot, en een subaccount met alleen het bedrag dat de bot mag gebruiken als de beurs dat heeft (GOK; Bitvavo heeft subaccounts volgens de rechtenlijst).
4. Sleutels nooit in code, nooit in een chat met een AI plakken, nooit in een openbare repo. Gebruik een `.env`-bestand dat niet in git komt (GOK, standaardpraktijk).

**Nep-repo's en malware (dit is het grootste gevaar voor wie zelf bouwt)**
- Check Point vond in 2026 een campagne met nep "sniper bots" en "predictors" op GitHub en SourceForge, met nep-sterren, nep-reviews, YouTube-uitleg met AI-stem en zelfs positieve stemmen op VirusTotal; de software verving gekopieerde wallet-adressen door die van de dief (meer dan 15.500 adressen in de lijst) (DERDEN, [Help Net Security, 19 jun 2026](https://www.helpnetsecurity.com/2026/06/19/fake-github-stars-crypto-stealing-malware/)).
- Bij Polymarket-bots: een echt, geverifieerd GitHub-account (dev-protocol) werd rond feb 2026 overgenomen en gebruikt voor 20+ nep-bots; het gif zat in typosquat-pakketten in `package.json` die `.env`-bestanden en sleutels stalen (DERDEN, [dev.to](https://dev.to/abrownfox001/why-almost-every-polymarket-trading-bot-on-github-is-malicious-28o7)). Eerder al een nep Solana-bot op GitHub die wallets leegtrok (DERDEN, [Cointelegraph](https://cointelegraph.com/news/solana-trading-bot-github-malware-scam)).
- Regels die hieruit volgen (GOK):
  - Alleen de officiële repo van een bekend framework (freqtrade/freqtrade, jesse-ai/jesse, hummingbot/hummingbot). Nooit een "verbeterde versie", fork of "winstgevende strategie" van een onbekende.
  - Sterren zeggen niets: die worden gekocht.
  - Geen kant-en-klaar `.exe` of installer van een bot. Freqtrade installeer je uit de officiële bron (pip of Docker-image van freqtrade).
  - Strategiebestanden van anderen eerst laten lezen door een AI met de vraag "doet dit iets anders dan handelen, zoals netwerk, bestanden of sleutels lezen?"
  - Draai de bot op een aparte server, niet op de computer met je wallets of wachtwoorden.

**De AI zelf**
- Laat een LLM nooit rechtstreeks orders sturen zonder harde grenzen in gewone code (maximale positie, maximaal verlies per dag, alleen toegestane paren). Een model kan een getal verkeerd lezen of verzinnen (GOK).

### 6. Bouwplan (concreet, in stappen)
Elke stap pas na de vorige. Stap 1 tot en met 4 kosten geen geld (GOK, volgt uit het bovenstaande).
1. **Server of laptop klaarzetten**: Docker, en Freqtrade uit de officiële bron. Een AI (Claude of ChatGPT) helpt bij elke foutmelding.
2. **Data ophalen**: `freqtrade download-data` voor een paar grote paren (BTC/EUR, ETH/EUR) van een officieel ondersteunde beurs. Voor Kraken met `--dl-trades` (GEZIEN, zie boven).
3. **Strategie laten schrijven door de AI** in een Freqtrade-strategiebestand. Begin met iets simpels wat A onderbouwt (zie `A-strategie-en-testen.md`). Vraag de AI expliciet: geen toekomstige data gebruiken, kosten meenemen.
4. **Terugtesten en controleren**: `freqtrade backtesting` met de echte kosten van je beurs, daarna `lookahead-analysis` en `recursive-analysis` (GEZIEN dat deze bestaan). Test op een periode die je niet gebruikte om de strategie te maken.
5. **Op papier handelen**: `dry_run` aan, minstens enkele weken, op de server die het straks echt doet (GOK voor de duur).
6. **Klein live**: MiCA-beurs, API-sleutel zonder opnamerecht en met IP-whitelist, een klein bedrag dat je kwijt mag, Telegram-meldingen aan. Grenzen in de config: maximaal aantal open trades, stop-loss.
7. **Pas daarna** eventueel Grok of een ander model erbij als extra signaal (bijv. sentiment), en alleen als A laat zien dat dat in tests iets toevoegt.

Waar Bitvavo het handigst lijkt (euro, Nederlands), is Kraken voor een Freqtrade-bot technisch veiliger: officiële ondersteuning en stop-loss op de beurs (GOK, op basis van de GEZIEN-punten in 2 en 3).

### 7. TikTok-claims nagetrokken (eerste ronde)
- "Grok schreef mijn bot en ik verdien X per dag": niemand laat een controleerbare test zien (terugtest met kosten, of papier-resultaten over maanden). De echte live-tests met chatbots die A vond, verloren meestal (zie `A-kant-en-klaar.md`, punt 4). (GOK voor de eerste zin, DERDEN via A voor de tweede.)
- "Download mijn gratis bot via de link in bio": precies het patroon van de malware hierboven (DERDEN, Help Net Security). Niet doen.

### Nog te doen (volgende runs)
- Kraken: kosten en API-sleutelrechten lezen (pagina met JavaScript; via support-artikelen proberen).
- OctoBot, NautilusTrader en IBKR-koppeling bekijken; prijs Jesse-licentie.
- Freqtrade: hoe goed werkt Bitvavo echt (issues en forum lezen, via raw-bestanden of docs).
- Een voorbeeld van een nette Freqtrade-strategie stap voor stap uitschrijven (code alleen lezen).
- VPS-prijzen in de EU nalezen.

## Stand na run 1 (19 nov 2026)
1. Bouw met **Freqtrade** (gratis, GPLv3, versie okt 2026) en laat de AI alleen de strategie schrijven; het framework doet terugtesten, papier handelen en controles op valsspelen (GEZIEN).
2. **Bitvavo werkt** met Freqtrade maar alleen "community"-getest en zonder stop-loss op de beurs; **Kraken** is officieel ondersteund met stop-loss op de beurs (GEZIEN). Bitvavo kost 0,15% maker en 0,25% taker (GEZIEN).
3. **API-sleutel nooit met opnamerecht**: bij Bitvavo gaan API-opnames zonder 2FA of mail (GEZIEN). Wel IP-whitelist aan.
4. **Het grootste gevaar is nep-bots op GitHub** met gekochte sterren en malware die sleutels en wallets steelt (DERDEN, 2026). Alleen officiële repo's van bekende frameworks.
5. Een AI-model in de bot is goedkoop (Grok 4.3 orde $5 per maand bij één vraag per uur, GOK op GEZIEN-prijzen); de **beurskosten** (0,5% per rondje bij Bitvavo taker) zijn de echte drempel.

## Run 2 (19 nov 2026, ±02:00)
Nieuw doel uit de BRIEF: denk als iemand die binnen 3 maanden €10.000 winst moet maken. Deze run: wat het gereedschap daarvoor echt kost en kan, en een rangorde van bouwroutes.

### 8. Grote correctie: Kraken is voor een kleine bot nu duur
- Kraken heeft in juli 2026 de kosten omgegooid. Instapniveau op Kraken Pro spot: **0,40% maker en 0,80% taker** (GEZIEN, [Kraken support, cross-platform fee tiers](https://support.kraken.com/articles/cross-platform-fee-tier-changes)). Daarvoor was het 0,25% en 0,40% (DERDEN, [Datawallet](https://www.datawallet.com/crypto/kraken-fees-explained)).
- Goedkoper wordt het pas bij $2.500 handelsvolume per 30 dagen (0,30/0,60%) of bij $10.000 volume of $20.000 aan bezit op Kraken (0,22/0,38%) (GEZIEN, zelfde Kraken-pagina).
- Een rondje kopen en verkopen met marktorders kost op instapniveau dus **1,6%**, tegen 0,5% bij Bitvavo (0,25% taker, GEZIEN in run 1) (GOK, eigen som). Met limietorders: 0,8% bij Kraken tegen 0,3% bij Bitvavo (GOK, eigen som).
- Gevolg voor het bouwplan: in run 1 schreef ik dat Kraken technisch veiliger is (stop-loss op de beurs). Dat klopt nog steeds, maar voor een bot die vaak handelt met een kleine pot is **Bitvavo nu de goedkopere keus**. Wie Bitvavo neemt, moet de bot dag en nacht laten draaien, want de stop-loss zit in de bot (GEZIEN in run 1). (GOK voor de afweging.)
- Perps in de Kraken-app kosten 0,25% openen plus 0,25% sluiten (GEZIEN, [Kraken fees](https://www.kraken.com/help/fees)).

### 9. Kraken API-sleutel: welke vinkjes (GEZIEN, [Kraken docs, API key permissions](https://docs.kraken.com/exchange/guides/rest/api-keys.md))
- Voor een handelsbot: Query Funds, Query Open Orders & Trades, Create & Modify Orders, Cancel/Close Orders. **Niet** Withdraw Funds, niet Deposit Funds.
- Kraken zelf: IP-whitelist "prevents almost all key misuse even if the key is leaked", en een aparte sleutel per doel. Subaccounts met eigen sleutels kunnen ("strategy isolation").
- Dat is hetzelfde patroon als bij Bitvavo (run 1): alleen kijken en handelen, nooit opnemen, IP vastzetten.

### 10. Hefboom: wat het gereedschap kan en wat in de EU mag
Met een kleine pot €10.000 halen in 3 maanden kan alleen met hefboom of met een markt die meer rendement geeft dan spot (GOK). Daarom:
- **Freqtrade kan futures** op Binance, Bitget, Bybit, Gate, Hyperliquid, Kraken en OKX (GEZIEN, [README](https://raw.githubusercontent.com/freqtrade/freqtrade/develop/README.md)). Voor Kraken Futures: exchange-naam `krakenfutures`, alleen "isolated" marge, afgerekend in USD, en stop-loss op de beurs werkt (market en limit) (GEZIEN, [Freqtrade exchanges](https://www.freqtrade.io/en/stable/exchanges/)). Bitvavo heeft geen futures in Freqtrade (GEZIEN, zelfde pagina, alleen spot).
- **Regels:** ESMA zei op 24 feb 2026 dat perpetuals voor particulieren vrijwel zeker onder de Europese CFD-regels vallen: hefboomgrens, verplichte waarschuwing, gedwongen sluiten bij verlies, geen negatief saldo, geen bonussen (DERDEN, [Finance Magnates](https://www.financemagnates.com/forex/regulation/esma-tells-firms-perpetual-futures-fall-under-eu-cfd-rules/)). Voor crypto is die grens 2x ("10x Down to 2x", DERDEN, [Finance Magnates](https://www.financemagnates.com/forex/10x-down-to-2x-has-europe-killed-crypto-perps-even-before-it-started/); artikel zelf niet kunnen lezen, alleen de kop).
- Kraken biedt sinds mei 2025 perpetuals aan in de EER via een MiFID-vergunning (DERDEN, [Cointelegraph](https://cointelegraph.com/news/kraken-launches-regulated-crypto-derivatives-europe)). Welke hefboom een Nederlandse particulier daar nu krijgt, niet kunnen nalezen.
- **Grijs:** hogere hefboom via een beurs zonder EU-vergunning (bijv. Hyperliquid, een DEX die Freqtrade ondersteunt). Risico: geen toezicht, geen bescherming tegen negatief saldo of faillissement, en bij een fout in de bot ben je de inzet in minuten kwijt door liquidatie (GOK). Hefboom maakt winst én verlies groter; zonder bewezen voordeel (zie A) versnelt het vooral het verlies (GOK, steunt op A punt 1 en 2).

### 11. Voorspellingsmarkten: gereedschap (D rangschikt dit als route 1)
- **NautilusTrader** (LGPL-3.0, versie 1.231.0 van 2 aug 2026, GEZIEN, [PyPI](https://pypi.org/pypi/nautilus_trader/json)) heeft koppelingen voor **Kalshi, Polymarket en Betfair**, plus Kraken, Bybit, OKX, Coinbase, Hyperliquid, Interactive Brokers en dataleveranciers als Databento en Tardis (GEZIEN, [NautilusTrader integrations](https://nautilustrader.io/docs/latest/integrations/)). De status per koppeling (beta of stabiel) stond in een plaatje en kon ik niet lezen.
- Het is het enige open source framework dat ik vond dat crypto, aandelen en voorspellingsmarkten in één terugtest-motor doet (GOK; Freqtrade en Hummingbot doen geen Kalshi of Polymarket als markt, Hummingbot noemt Kalshi wel op zijn beurzenpagina maar het verband kon ik niet lezen, GEZIEN, [hummingbot.org/exchanges](https://hummingbot.org/exchanges/)). Nadeel: veel moeilijker dan Freqtrade, gemaakt voor professionals (GOK).
- **Kalshi** heeft een officiële API met een **demo-omgeving met nepgeld** (`demo.kalshi.co`, eigen inloggegevens, los van echt) (GEZIEN, [Kalshi docs demo](https://docs.kalshi.com/getting_started/demo_env.md)). Waarschuwing van Kalshi zelf: prijzen in de demo lijken niet altijd op de echte markt (GEZIEN). Daar kan een bot dus op papier draaien zonder geld.
- **Grijs in Nederland:** Polymarket is in feb 2026 door de Kansspelautoriteit verboden; Kalshi, Hyperliquid en Interactive Brokers boden in mei 2026 nog steeds voorspellingsmarkten aan Nederlanders aan zonder Nederlandse vergunning (DERDEN, [Cointelegraph, 5 mei 2026](https://cointelegraph.com/news/kalshi-hyperliquid-offer-prediction-markets-to-dutch-users-despite-polymarket-ban)). Risico: account dicht of geld vast als de Ksa ingrijpt; de Ksa dreigde een Amerikaanse site met een dwangsom van €420.000 per week (DERDEN, [NL Times](https://nltimes.nl/2026/02/17/regulators-order-us-betting-site-stop-operations-threaten-eu420000-weekly-fine)). De boete trof de aanbieder, niet de speler (GOK).
- Veiligheid: Polymarket-bots op GitHub zijn de bekendste malware-val (run 1, punt 5). Alleen bouwen op de officiële API of een groot framework, nooit een "Polymarket arbitrage bot" van een onbekende.

### 12. Server: wat het nu kost
- Hetzner verhoogde in 2026 twee keer de prijzen; de CX22 is vervangen door de CX23 voor €5,49 per maand plus €0,50 voor een IPv4-adres, samen €5,99 per maand (DERDEN, [prijsvergelijking aug 2026](https://kimmo.suominen.com/stuff/cpc-2026-08.txt)). Genoeg voor Freqtrade met een paar paren (GOK). Een vast IPv4-adres is nodig voor de IP-whitelist bij de beurs (GOK).
- NautilusTrader of FreqAI met machine learning vraagt meer geheugen; reken op het dubbele (GOK).

### 13. Ingebouwde remmen die je niet zelf hoeft te bouwen (Freqtrade)
- In het voorbeeld-strategiebestand staan vaste velden: `stoploss` (standaard -0,10), `trailing_stop`, `minimal_roi`, `timeframe`, `startup_candle_count`, `can_short` (GEZIEN, [sample_strategy.py](https://raw.githubusercontent.com/freqtrade/freqtrade/develop/freqtrade/templates/sample_strategy.py)). Laat de AI alleen die velden en de in- en uitstapregels invullen, niet de rest.
- In de config: `max_open_trades` (maximaal aantal open trades) en `dry_run_wallet` (nepsaldo voor papier handelen) (GEZIEN, [Freqtrade configuration](https://www.freqtrade.io/en/stable/configuration/)).
- "Protections": o.a. `StoplossGuard` ("Stop trading if a certain amount of stoploss occurred within a certain time window") en `MaxDrawdown` (GEZIEN, [Freqtrade plugins](https://www.freqtrade.io/en/stable/plugins/)). Dat is je maximaal verlies per dag, zonder eigen code.
- Een vaste opdracht voor de AI (GOK, eigen voorstel): "Schrijf een Freqtrade-strategie (INTERFACE_VERSION 3) voor timeframe 1h. Gebruik alleen data tot en met de huidige candle. Vul stoploss, minimal_roi en de in- en uitstapregels in. Geen netwerk, geen bestanden, geen sleutels. Leg elke regel uit." Daarna altijd `lookahead-analysis` en `recursive-analysis`.

### 14. Rangorde van bouwroutes richting €10.000 in 3 maanden (kans maal opbrengst)
Alle kansen zijn GOK, gebaseerd op A (geen bewezen voordeel bij spot-strategieën), D (arbitrage) en de kosten hierboven. Uren zijn voor bouwen plus bijhouden.

| # | Route en gereedschap | Inleg geld / uren per week | Kans op €10.000 netto in 3 mnd | Ergste geval | Gedaan door anderen? |
|---|---|---|---|---|---|
| 1 | Voorspellingsmarkt-bot (Kalshi-API of NautilusTrader), eerst op de Kalshi-demo; grijs in NL | €1.000 tot €5.000 / 20+ | 5 tot 10% (zelfde als D) | inleg kwijt, account dicht | ja, grote bedragen (DERDEN via D punt 3) |
| 2 | Freqtrade futures met hefboom op een beurs zonder EU-vergunning; grijs | €2.000+ / 10 tot 15 | 2 tot 5% | inleg in dagen kwijt door liquidatie | verhalen op fora, zelden controleerbaar (GOK) |
| 3 | Freqtrade futures op Kraken met EU-hefboom (2x) | €10.000+ / 10 | onder 2% | grote daling plus kosten | niet gevonden |
| 4 | Freqtrade spot op Bitvavo (trend of DCA met regels) | €10.000+ / 5 tot 10 | onder 1%; nuttig om dalingen te beperken, niet voor het doel | trage daling, kosten | ja, maar met bescheiden rendement (A punt 1) |
| 5 | LLM laat zelf handelen (TradingAgents-achtig, Grok op X) | €0 tot €500 aan API / 10 | bijna 0% | inleg kwijt aan een fout van het model | live tests verloren meestal (A-kant-en-klaar punt 4) |

Rekensom achter de kans van route 4 (GOK): €10.000 winst in 3 maanden op een pot van €10.000 is 100% rendement in een kwartaal; de beste trendinstelling van A haalde na de testperiode Sharpe 0,33.

### Nog te doen
- Hefboom en kosten van Kraken Futures voor Nederlandse particulieren (pagina's laden met JavaScript; via support-artikelen proberen).
- NautilusTrader-koppelingen Kalshi en Polymarket: status lezen (beta of stabiel) op de losse pagina's.
- OctoBot: GPL-3.0, versie 2.1.1 van 29 mrt 2026 (GEZIEN, [PyPI octobot](https://pypi.org/pypi/octobot/json)); verder nog niet bekeken. Laatste release is acht maanden oud, dus trager onderhouden dan Freqtrade (GOK).
- Sterren en activiteit van repo's: de GitHub-API is in deze sessie dicht voor andere repo's dan die van Dortus (GEZIEN, foutmelding); PyPI-datums gebruikt als vervanging.

## Stand na run 2 (19 nov 2026, ±02:00)
1. **Freqtrade blijft de basis** (gratis, spot en futures, ingebouwde remmen zoals StoplossGuard en MaxDrawdown, controles op valsspelen) (GEZIEN). Laat de AI alleen de strategievelden invullen.
2. **Kraken is sinds juli 2026 duur voor kleine bots**: 0,40% maker en 0,80% taker op instapniveau, dus 1,6% per rondje met marktorders, tegen 0,5% bij Bitvavo (GEZIEN plus eigen som). Bitvavo is goedkoper maar heeft geen stop-loss op de beurs, dus de bot moet dag en nacht draaien (server ±€6 per maand, DERDEN).
3. **API-sleutels**: zowel Kraken als Bitvavo laten je opnemen uitzetten en het IP vastzetten; Kraken zegt zelf dat de IP-whitelist bijna alle misbruik tegenhoudt (GEZIEN).
4. **€10.000 in 3 maanden** kan met een eigen bot alleen via hefboom of voorspellingsmarkten; in de EU is crypto-hefboom voor particulieren 2x (DERDEN), hogere hefboom en Kalshi zijn grijs (DERDEN). Kans op het doel blijft klein: hoogstens 5 tot 10% voor de beste route (GOK).
5. **Voor voorspellingsmarkten bestaat goed gereedschap**: NautilusTrader (Kalshi, Polymarket, Betfair) en een Kalshi-demo met nepgeld om eerst op papier te draaien (GEZIEN). Malware-repo's rond Polymarket blijven het grootste gevaar (DERDEN).

## Run 3 (19 nov 2026, ±03:00 Nederlandse tijd)
Nieuwe hoeken deze run: wat Grok als "ogen op X" echt kost, de goedkoopste plek voor een bot (Hyperliquid) en het risico daarvan, de status van de koppelingen voor voorspellingsmarkten, en AI die via MCP je bot bedient.

### 15. Grok als sentimentbron: X Search kost per post, niet per vraag
- De Grok-API heeft een ingebouwde tool `x_search`. Prijs: **$5 per 1.000 opgehaalde posts** en $10 per 1.000 profielen, bovenop de tokens. Elke post telt, ook geciteerde en bovenliggende posts in een draad (GEZIEN, [docs.x.ai pricing](https://docs.x.ai/developers/pricing.md)). Web Search kost $5 per 1.000 aanroepen (GEZIEN, zelfde pagina).
- Je kunt de zoektocht vastzetten op maximaal 20 accounts (`allowed_x_handles`) en op datums (`from_date`, `to_date`, hele dagen in UTC); `max_turns` beperkt hoe vaak het model zoekt (GEZIEN, [docs.x.ai X Search](https://docs.x.ai/developers/tools/x-search.md)). Datums gaan per dag, niet per uur (GEZIEN, "Dates in any other format, including full date-times, aren't applied").
- xAI heeft zelf een voorbeeld-app "X Sentiment Tracker": één zoektocht geeft hoogstens 10 posts, dus de app zoekt 10 dagen tegelijk, haalt tot 100 posts op, doet er ongeveer anderhalve minuut over en **kost ongeveer 80 cent per run**, vooral voor X Search (GEZIEN, [xAI cookbook](https://docs.x.ai/cookbook/examples/x-sentiment-tracker.md)).
- Correctie op run 1: daar rekende ik ±$5 per maand voor één vraag per uur, maar dat was alleen tokens. Met X Search erbij (GOK, eigen som op de GEZIEN-prijzen):
  - elk uur 10 posts over één munt: 24 x 10 x $0,005 = $1,20 per dag, plus tokens, samen orde **$40 tot $50 per maand**;
  - elk uur een volle run van 100 posts zoals het voorbeeld: 24 x $0,80 = ±$19 per dag, orde **$550 tot $600 per maand**.
- Wat A vond over het nut van sentiment geldt hier: zonder test die laat zien dat het signaal na kosten iets toevoegt, is dit vooral een kostenpost (GOK, steunt op A punt 6). Begin met de goedkope variant (vaste lijst van een paar accounts, 1 keer per uur of per dag) en sla de scores op, zodat je ze later kunt terugtesten tegen de koers. Grok-scores van het verleden kun je niet achteraf eerlijk maken, want het model weet nu wat er daarna gebeurde (GOK; TradingAgents zegt hetzelfde, zie run 1).

### 16. Hyperliquid: veruit de goedkoopste plek voor een bot, maar grijs
**Kosten** (GEZIEN, [Hyperliquid fees](https://hyperliquid.gitbook.io/hyperliquid-docs/trading/fees.md)):
- Perpetuals instapniveau: **0,045% taker en 0,015% maker**. Spot instapniveau: 0,070% taker en 0,040% maker. Niveau gaat op 14 dagen volume.
- Een rondje perps met marktorders is dus 0,09%, tegen 0,5% bij Bitvavo spot en 1,6% bij Kraken spot (GOK, eigen som op GEZIEN-tarieven uit run 1 en 2). Voor een bot die vaak handelt is dat een factor 5 tot 18 goedkoper.
- Voorspellingsmarkten op Hyperliquid (HIP-4 "outcome markets"): de eerste markt is een dagelijkse ja/nee op de BTC-prijs, afgerekend om 06:00 UTC; **kosten nu nul** "for initial testing"; geen hefboom en geen liquidatie (GEZIEN, [HIP-4](https://hyperliquid.gitbook.io/hyperliquid-docs/hyperliquid-improvement-proposals-hips/hip-4-outcome-markets.md)). NautilusTrader ondersteunt HIP-4 al (zie punt 17).

**Veiligheid: API-wallet in plaats van een sleutel**
- Hyperliquid is een DEX: er is geen API-sleutel maar een "API wallet" (ook "agent wallet") die namens je hoofdaccount alleen ondertekent (GEZIEN, [Hyperliquid API wallets](https://hyperliquid.gitbook.io/hyperliquid-docs/for-developers/api/nonces-and-api-wallets.md)). Freqtrade zegt erover: "This key won't allow withdrawals, only trading" (GEZIEN, [Freqtrade exchanges](https://www.freqtrade.io/en/stable/exchanges/)).
- Je kunt een vervaldatum zetten, hoogstens 180 dagen; per account 1 naamloze en 3 benoemde API-wallets (GEZIEN, [exchange endpoint](https://hyperliquid.gitbook.io/hyperliquid-docs/for-developers/api/exchange-endpoint.md)). Hyperliquid raadt sterk aan een oude API-wallet nooit opnieuw te gebruiken, omdat oude ondertekende opdrachten anders opnieuw afgespeeld kunnen worden (GEZIEN, API wallets-pagina).
- Freqtrade raadt aan: aparte software-wallet met alleen het handelsgeld, nooit je echte wallet-sleutel of de woorden van je hardware wallet op de server, en let op "supply chain attacks, like pip package poisoning" (GEZIEN, Freqtrade exchanges).

**Wat Freqtrade erop kan** (GEZIEN, Freqtrade exchanges):
- Futures (isolated en cross) met stop-loss op de beurs (stop-limit); spot zonder stop-loss op de beurs.
- Geen echte marktorders: CCXT doet een limietorder met tot 5% slippage. Bij een dunne markt kan een "marktorder" dus flink slechter uitvallen (GOK, volgt uit die 5%).
- **Maar 5.000 historische candles**: op 1h is dat ruim een half jaar, op 5m nog geen 18 dagen (GOK, eigen som). Je moet zelf data gaan verzamelen of een andere bron gebruiken; terugtesten op Hyperliquid zelf is dus beperkt.

**Het grijze deel**
- ESMA zei op 24 feb 2026 dat perpetuals voor particulieren waarschijnlijk onder de CFD-regels vallen met een hefboomgrens van 2:1 (DERDEN, [CryptoTicker](https://cryptoticker.io/en/perpetuals-mifid-classification-leverage-cap/)). De Hyperliquid Policy Center vroeg de Europese Commissie op 30 sep 2026 om perps onder MiFID II te regelen (DERDEN, zelfde bron en [CoinMarketCap](https://coinmarketcap.com/academy/article/hyperliquid-policy-group-urges-eu-to-classify-perpetuals-under-mifid)). Hyperliquid heeft dus geen EU-vergunning en de regels zijn nog niet af.
- Er is een waarschuwing van de Britse FCA over Hyperliquid (DERDEN, kop van [FinTelegram](https://fintelegram.com/hyperliquid-after-the-fca-warning-defi-branding-meets-regulated-derivatives-reality/); artikel zelf niet kunnen lezen). Een AFM-waarschuwing niet gevonden (GOK, niet volledig gezocht).
- Risico als particulier (GOK): geen toezicht, geen bescherming als het platform of de brug naar Arbitrum gehackt wordt, en met hoge hefboom kan een bot de inzet in minuten kwijtraken. Juridisch treft een eventuele maatregel vooral de aanbieder; voor jou is het ergste geval dat je geld vastzit of weg is (GOK).

### 17. NautilusTrader: hoe rijp zijn de koppelingen (GEZIEN, losse integratiepagina's op nautilustrader.io)
- **Hyperliquid**: spot, perps, HIP-3-perps staan als "Stable"; HIP-4 outcome markets worden ondersteund ([NT Hyperliquid](https://nautilustrader.io/docs/latest/integrations/hyperliquid)).
- **Kalshi**: data (orderboek, trades, candles) en uitvoering met **alleen limietorders**; RFQ niet. Belangrijk: in terugtests en in de sandbox kan het model geen "NO"-positie openen, en de eigen saldoberekening klopt niet met hoe Kalshi geld verrekent, dus `calculate_account_state=false` voor live ([NT Kalshi](https://nautilustrader.io/docs/latest/integrations/kalshi)). Gevolg: een Kalshi-strategie die ook op NEE inzet, kun je in NautilusTrader nog niet eerlijk terugtesten (GOK, volgt uit die beperking).
- **Polymarket**: marktorders KOPEN gaan in pUSD-bedrag, VERKOPEN in aantal; sommige ordersoorten worden vooraf geweigerd; posities van de hele wallet kan de koppeling niet opvragen ([NT Polymarket](https://nautilustrader.io/docs/latest/integrations/polymarket)). Polymarket is in Nederland verboden (run 2).
- **Kalshi-kosten**: taker betaalt 0,07 x P x (1 - P) per contract, met P de prijs; het meest bij 50 cent: 1,75 cent per contract, dus 3,5% van de inzet (DERDEN, [Whirligig Bear](https://whirligigbear.substack.com/p/makertaker-math-on-kalshi); eigen deling voor de 3,5%). Sommige markten hebben ook een makerfee (DERDEN, zelfde). Een bot die als maker met limietorders werkt, ontloopt dat meestal (GOK). API-limieten gaan met "tokens": de meeste aanvragen kosten 10 tokens, met aparte budgetten voor lezen en schrijven per niveau (GEZIEN, [Kalshi rate limits](https://docs.kalshi.com/getting_started/rate_limits.md)).

### 18. De AI je bot laten bedienen via MCP: handig, maar zet één ding uit
- Er bestaan open source MCP-servers waarmee Claude (of een andere AI) via de REST-API met een draaiende Freqtrade praat, bijv. kukapay/freqtrade-mcp (code gelezen, niet uitgevoerd) en het PyPI-pakket freqtrade-mcp-server 0.2.0 van aug 2026 (GEZIEN, [README kukapay](https://raw.githubusercontent.com/kukapay/freqtrade-mcp/main/README.md), [PyPI](https://pypi.org/pypi/freqtrade-mcp-server/json)). Dat is iets anders dan de officiële Jesse MCP (run 1): dit zijn projecten van derden.
- In de code van kukapay staat een tool `place_trade` die `forcebuy` en `forcesell` aanroept, naast `start_bot`, `stop_bot`, `reload_config` en `delete_lock` (GEZIEN, [__main__.py](https://raw.githubusercontent.com/kukapay/freqtrade-mcp/main/__main__.py)). Een AI kan dus zelf trades openen en een beveiligingsslot weghalen.
- Freqtrade zelf heeft een rem: **`force_entry_enable` staat standaard uit** "for security reasons", en dan werken gedwongen aankopen via Telegram en REST niet (GEZIEN, [Freqtrade configuration](https://www.freqtrade.io/en/stable/configuration/)). Laat dat uit: dan kan de AI wel kijken (status, winst, trades), maar geen eigen aankopen doen (GOK, volgt uit de docs; verkopen en `stop_bot` kunnen nog wel).
- De REST-API luistert standaard alleen op de eigen machine; Freqtrade raadt sterk af hem op internet te zetten en zegt: gebruik een ssh-tunnel of VPN naar je VPS. In Docker: `127.0.0.1:8080:8080`, niet `8080:8080` (GEZIEN, [Freqtrade REST API](https://www.freqtrade.io/en/stable/rest-api/)).
- Zelfde malware-regel als in run 1: een MCP-server draait code op je machine met toegang tot je bot. Alleen gebruiken na zelf lezen van de code (het is hier ±300 regels), en nooit een kopie of fork van een onbekende (GOK).

### 19. Kleine correctie Freqtrade en Bitvavo
- Op de beurzenpagina van Freqtrade staat Bitvavo nu in het overzicht van "supported exchanges" (spot, geen stop-loss op de beurs), met een aparte notitie over `operatorId` (GEZIEN, [Freqtrade exchanges](https://www.freqtrade.io/en/stable/exchanges/)). In de README staat Bitvavo nog onder "Community tested" (GEZIEN, [README](https://raw.githubusercontent.com/freqtrade/freqtrade/develop/README.md)). De twee bronnen zijn het dus niet eens; behandel Bitvavo als werkend maar minder getest (GOK).
- Bybit heeft een demomodus met echte markten en nepgeld die Freqtrade ondersteunt (`exchange.demo_trading`); Bybit EU staat officieel in de README (GEZIEN, beide bronnen). Niet in te zetten naast dry-run (GEZIEN). Een tweede manier om op papier te handelen, dichter bij echte uitvoering dan dry-run (GOK).

### 20. Bijgewerkte rangorde van bouwroutes (kans maal opbrengst, alles GOK)
Wat verandert ten opzichte van run 2: Hyperliquid maakt route 2 qua kosten veel beter, maar niet qua kans (er is nog steeds geen bewezen voordeel, zie A). HIP-4 is een nieuwe, kleine route.

| # | Route en gereedschap | Inleg geld / uren per week | Kans op €10.000 netto in 3 mnd | Ergste geval | Gedaan door anderen? |
|---|---|---|---|---|---|
| 1 | Voorspellingsmarkt-bot als maker (Kalshi-API, eerst demo); grijs in NL | €1.000 tot €5.000 / 20+ | 5 tot 10% | inleg kwijt, account dicht | ja (DERDEN via D punt 3 en 10) |
| 2 | Freqtrade futures op Hyperliquid, API-wallet, lage kosten; grijs | €2.000+ / 10 tot 15 | 2 tot 5% | inleg in dagen kwijt door liquidatie of hack | verhalen, zelden controleerbaar |
| 3 | NautilusTrader op HIP-4 (dagelijkse BTC ja/nee, nu zonder kosten); grijs | €500+ / 15+ | onder 2% (markt is nieuw en klein) | inleg kwijt; kosten kunnen terugkomen | niet gevonden |
| 4 | Freqtrade futures op Kraken met EU-hefboom 2x | €10.000+ / 10 | onder 2% | grote daling plus kosten | niet gevonden |
| 5 | Freqtrade spot op Bitvavo | €10.000+ / 5 tot 10 | onder 1% | trage daling, kosten | ja, bescheiden rendement (A) |
| 6 | Grok-sentiment als hoofdsignaal | $40 tot $600 per maand aan API / 10 | bijna 0% zonder eerst eigen data te verzamelen | API-kosten plus verlies | niet controleerbaar gevonden |

### Nog te doen
- AFM-waarschuwingslijst nalezen op Hyperliquid, Kalshi en andere DEX'en (de lijst laadt mogelijk met JavaScript).
- Hyperliquid: maximale hefboom per munt en wat de brug naar Arbitrum aan risico heeft gehad (hacks of storingen).
- Grok-sentiment: kijken of iemand een eerlijke, vooraf vastgelegde test heeft gedaan (samen met A).
- Een volledig voorbeeld van een Freqtrade-config met alle remmen (StoplossGuard, MaxDrawdown, max_open_trades, force_entry_enable uit), alleen als tekst.

## Stand na run 3 (19 nov 2026, ±03:00)
1. **Freqtrade blijft de basis**, met de AI als schrijver van de strategie; laat `force_entry_enable` uit en zet de REST-API nooit open op internet, dan kan een AI via MCP wel meekijken maar niet zelf kopen (GEZIEN).
2. **Kosten bepalen alles**: een rondje kost 1,6% op Kraken spot, 0,5% op Bitvavo spot en 0,09% op Hyperliquid perps (GEZIEN tarieven, eigen som). Hyperliquid is de goedkoopste en heeft een API-wallet zonder opnamerecht, maar heeft geen EU-vergunning (grijs) en geeft maar 5.000 candles voor terugtesten (GEZIEN).
3. **Grok als ogen op X is duurder dan gedacht**: $5 per 1.000 posts; het voorbeeld van xAI kost ±80 cent per run, dus van ±$40 tot ±$600 per maand afhankelijk van hoe vaak (GEZIEN plus eigen som). Eerst goedkoop verzamelen en terugtesten.
4. **Voor voorspellingsmarkten**: Kalshi kost een taker tot 3,5% van de inzet (DERDEN), NautilusTrader kan Kalshi alleen met limietorders en kan NEE-posities niet terugtesten; HIP-4 op Hyperliquid is nieuw en nu zonder kosten (GEZIEN).
5. **Veiligheid blijft het grootste punt**: nooit opnamerecht, IP of API-wallet vastzetten, alleen officiële repo's, en MCP-servers van derden eerst zelf lezen (GEZIEN en GOK, zie per punt).
