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

## Run 4 (19 nov 2026, ±04:00 Nederlandse tijd)

Deze run: het gereedschap voor de route die D nu bovenaan zet (een bot die de liquiditeitsbeloning van Polymarket pakt), want daar ontbrak nog een bouwplan. Plus de Freqtrade-config met alle remmen uit mijn lijst "nog te doen". Niets geïnstalleerd of uitgevoerd; code alleen gelezen.

### 21. Welke software: de oude Polymarket-bibliotheken zijn afgeschreven
- De officiële Python-bibliotheek heet nu **`polymarket-client`** (versie 0.20.0, 16 nov 2026), één pakket voor marktdata, account en handel, met een async-versie voor bots (GEZIEN, [docs Python SDK](https://docs.polymarket.com/getting-started/python.md), [PyPI](https://pypi.org/project/polymarket-client/)).
- **`py-clob-client` en `py-clob-client-v2` zijn "deprecated"**; Polymarket vraagt over te stappen (GEZIEN, PyPI-pagina van py-clob-client-v2 en het [changelog van 12 nov 2026](https://docs.polymarket.com/changelog/predictions.md)). Bijna alle bots en uitlegfilmpjes op internet gebruiken nog die oude pakketten (GOK, op basis van wat ik las, zie punt 25).
- Op **14 december 2026** veranderen drie zoekopdrachten voor orders en trades op de CLOB-API; oude code die op `asset_id` filtert krijgt dan foutmelding 400 (GEZIEN, zelfde changelog). Een bot die je nu van GitHub haalt, kan dus over een maand stuk zijn.

### 22. Nederland en de API: de site blokkeert, de API niet
- Polymarket zet Nederland op de lijst **"Close-Only on Frontend"**, met de zin: "Close-only on the Polymarket frontend; the API itself is not restricted" (GEZIEN, [docs Geographic Restrictions](https://docs.polymarket.com/api-reference/geoblock.md)). Ook Ierland, Japan en Zuid-Korea staan daar. België, Frankrijk, Duitsland en Italië zijn wel ook via de API op slot (alleen sluiten).
- Je kunt vooraf controleren wat Polymarket van je IP vindt met `GET https://polymarket.com/api/geoblock` (GEZIEN, zelfde pagina; vanaf deze cloudmachine gaf hij `"blocked":true` met land US, dus het werkt).
- De servers staan in **eu-west-2 (Londen)** (GEZIEN, zelfde pagina). Een VPS in Londen geeft de kortste weg (GOK, volgt uit de docs).
- Dit verandert niets aan de wet: de Ksa ziet Polymarket als illegaal gokken in Nederland (D, run 1). Dat de API openstaat, maakt het technisch makkelijk, niet legaal. Risico blijft grijs: bij een nieuwe blokkade kun je alleen nog sluiten, en je hebt geen Nederlandse rechter als het saldo vast komt te zitten (GOK).

### 23. Veiligheid: gebruik een Session Key, nooit de hoofdsleutel in de bot
- Polymarket heeft sinds kort **Session Keys**: een aparte sleutel die mag handelen maar "cannot withdraw funds from the Deposit Wallet", geldig tot 180 dagen, en te beperken tot alleen de orderboek-handel (scope `CLOB`) (GEZIEN, [docs Session Keys](https://docs.polymarket.com/trading/session-keys.md)). Dat is hetzelfde idee als een beurssleutel zonder opnamerecht.
- Werkt alleen met een **Deposit Wallet**; elke account-wallet die op of na 4 mei 2026 is gemaakt is er een (GEZIEN, [docs Wallets](https://docs.polymarket.com/trading/wallets-auth.md)).
- De open bots die ik las vragen nog de **privésleutel van je wallet** in een `.env`-bestand (GEZIEN, README van poly-maker: "`PK`, the private key of your signer wallet"). Wie die sleutel heeft, kan alles opnemen. Met een Session Key is een gestolen sleutel "alleen" slechte trades, geen lege wallet (GOK, volgt uit de docs).
- **Malware rond Polymarket-bots is een echt en groot probleem**:
  - Maart 2026: de geverifieerde GitHub-organisatie `dev-protocol` (568 volgers) werd gekaapt en verspreidde een Polymarket-copybot "with a polished README, hundreds of stars" die echt werkte, maar via twee nagemaakte npm-pakketten de sleutel uit `.env` stal en een SSH-achterdeur opende (DERDEN, [StepSecurity](https://www.stepsecurity.io/blog/malicious-polymarket-bot-hides-in-hijacked-dev-protocol-github-org-and-steals-wallet-keys)).
  - Mei 2026: negen npm-pakketten van één nep-account, waaronder **`polymarket-claude-code`** en `polymarket-ai-agent`, vroegen bij installatie om je privésleutel ("stays encrypted") en stuurden die onversleuteld weg (DERDEN, [SafeDep](https://safedep.io/malicious-polymarket-npm-crypto-wallet-drainer/)). Dit richt zich precies op mensen die met een AI-assistent een handelsbot bouwen.
  - Regels: alleen `polymarket-client` van PyPI met die exacte naam; geen npm-pakketten met "polymarket" in de naam van onbekenden; sterren en een nette README zeggen niets; laat je AI-assistent nooit zelf een pakket kiezen en installeren zonder dat je de naam naast de officiële docs legt (GOK, volgt uit de twee zaken).

### 24. Remmen die Polymarket zelf al heeft (hoef je niet te bouwen)
- **Heartbeat als dodemansknop**: stuur elke 5 seconden een heartbeat; na 10 seconden zonder probeert Polymarket al je open orders te annuleren. Let op: "Cancellation timing and success are not guaranteed" (GEZIEN, [CLOB OpenAPI](https://docs.polymarket.com/api-spec/clob-openapi.yaml), `/heartbeats` en `/v1/heartbeats`). Zet hem aan: als je VPS of internet uitvalt, blijven je orders anders liggen terwijl het nieuws binnenkomt.
- **Cancel-all** werkt ook als de beurs in "cancel-only" staat (GEZIEN, [API-overzicht](https://docs.polymarket.com/_llms/en/api-reference/predictions.txt)).
- **Herstarts van de matching engine**: worden ±2 dagen vooraf aangekondigd; daarna 2 minuten alleen post-only orders. Een bot moet die foutmelding herkennen en wachten (GEZIEN, [docs Matching Engine Restarts](https://docs.polymarket.com/trading/matching-engine.md)).
- **Snelheidslimiet** voor een nieuwe gebruiker: 40 orders per seconde (piek 60) en 80 annuleringen per seconde (piek 120), per sleutel (GEZIEN, [docs Trading Rate Limits](https://docs.polymarket.com/api-reference/trading-rate-limits.md)). Ruim genoeg voor een paar honderd markten als je niet elke seconde alles vervangt (GOK).
- Polymarkets eigen advies voor market makers: beide kanten quoten, scheef zetten naar je voorraad, oude orders direct weghalen, **GTD-orders die vanzelf verlopen voor een bekend moment** (uitslag, debat), en een kill switch (GEZIEN, [docs Market Making](https://docs.polymarket.com/trading/market-making.md)).

### 25. Bestaande open bot gelezen: warproxxx/poly-maker
Gelezen met `git clone --filter=blob:none` (alleen lezen, niets geïnstalleerd). Sterren kon ik niet zien (GitHub-API voor andere repo's staat dicht in deze sessie).
- Eerste commit 31 maart 2025, laatste 9 juli 2026, 37 commits; in juli 2026 herschreven voor **CLOB V2**, alleen maker-orders (post-only), papiermodus (`run --paper`), heartbeat aan, en harde grenzen in `config.toml`: maximaal totaal risico, maximaal per markt, en een **dagverlies-stop** (GEZIEN, code en config).
- In de broncode alleen adressen van Polymarket zelf en openbare Polygon-RPC's (publicnode, ankr, llamarpc); geen `eval`, `exec` of base64 (GEZIEN, korte zoektocht met grep; dat is geen volledige controle, en de afhankelijkheden zijn niet nagekeken).
- Hangt vast aan **`py-clob-client-v2==1.0.2`**, dus aan het afgeschreven pakket (GEZIEN, `pyproject.toml`). Goed om van te leren, niet om blind te draaien.
- Het mooiste stuk is `TIPS.md`, een verslag van een echte sessie met toezicht. Uitkomst: **ongeveer −$15,51** over twee markten, waarvan ±$10 door één te grote order in een dunne markt (GEZIEN, TIPS.md; DERDEN in de zin dat ik het niet kan controleren). Hun lessen, op volgorde van wat het kostte:
  1. In een dunne markt alleen de **minimale grootte** neerzetten die nog beloning krijgt; een vulling moet klein en weg te gooien zijn.
  2. Orders onder `rewardsMinSize` verdienen niets, en die grens verandert (zij zagen 50 naar 100). Ververs de marktinfo regelmatig.
  3. Niet te vaak vervangen: dan verlies je je plek en word je minder vaak meegeteld voor de beloning.
  4. De positie-API loopt achter bij snelle bewegingen; vertrouw het orderboek en de keten.
  5. Uitstappen met een marktorder kost takerkosten; zij zagen ±$4 op ±$127.
- Ouder en eenvoudiger: Polymarkets eigen **`poly-market-maker`** (elke 30 seconden het midden ophalen en orders bijzetten, strategie "Bands" of "AMM", "experimental") (GEZIEN, [README](https://raw.githubusercontent.com/Polymarket/poly-market-maker/main/README.md)). Te traag en te simpel voor nieuwe markten (GOK).

### 26. Wat er misgaat als je beloning jaagt (verslagen van anderen)
- **Een bot leeggetrokken met een val**: in november 2025 zette een handelaar een kleine order neer die de spread net binnen de beloningsgrens bracht; de bot "sunshines" sprong er direct met een grote order naast, waarna de handelaar die opkocht. Zo herhaald vier uur lang, samen **ruim $1.500**, tot het account van de bot leeg was (DERDEN, [BlockBeats via ChainCatcher](https://www.chaincatcher.com/en/article/2223433)). Les: als je bot voorspelbaar reageert op een prikkel, kunnen anderen daarop handelen (GOK).
- **Een gekloonde market-making-bot** gaf beloning en wat spread, maar "net profit was negative after accounting for bugs, testing losses, and directional hits"; beweeglijke markten "can wipe out weeks of rewards in minutes" (DERDEN, [dev.to](https://dev.to/fatherson/i-cloned-a-polymarket-market-making-bot-and-ran-it-heres-what-i-learned-46ag); geen cijfers, dus zwak bewijs).
- Hetzelfde patroon bij Hummingbot in 2021: 3 tot 4% beloning per week op gewone paren, daarna in 20 minuten 20% kwijt op een dunne munt met hoge beloning (DERDEN, [CryptoQuants](https://thecryptoquant.substack.com/p/how-i-lost-20-in-20-minutes)).
- Samengevat: de beloningspot is echt (D meet hem), maar **de bot is vooral een risicobeheer-probleem**, niet een slimheidsprobleem. De meeste winst of verlies zit in welke markten je mijdt en hoe klein je orders zijn (GOK, uit de verslagen hierboven).

### 27. Bouwplan voor een beloningsbot op Polymarket (van nul tot schaduw, zonder account)
Elke stap kan zonder account, behalve stap 7. De AI (Claude, ChatGPT, Grok) schrijft de code; jij legt elke regel die geld raakt naast de docs.
1. **Lezen (2 uur)**: docs Market Making, Liquidity Rewards, Matching Engine, Session Keys (links hierboven). Laat de AI daaruit een lijst eisen maken.
2. **Marktenlijst (dag 1)**: elke 10 minuten `clob.polymarket.com/rewards/markets/current` plus de startdatum uit Gamma ophalen; houd alleen markten jonger dan 2 dagen, met beloning boven een drempel, en zonder bekende uitslag binnen 48 uur (D punt 13 voor de filters). Openbaar, geen account (GEZIEN door D).
3. **Orderboek live bijhouden (dag 2 tot 3)**: de openbare market-websocket per token (docs Real-Time Data). Alles opslaan in SQLite; dat is meteen je eigen historie om later terug te testen (A raadt hetzelfde aan).
4. **Schaduwbot (week 1 tot 2)**: rekent elke minuut uit welke orders hij zou zetten (minimale grootte, binnen de beloningsgrens, scheef naar voorraad) en **doet alsof hij gevuld wordt** als een echte trade door zijn prijs gaat. Hij telt zijn beloning met de formule uit de docs en zijn verlies op die nepvullingen. Dit is de meting die nu bij iedereen ontbreekt.
5. **Remmen erin, vóór er geld bij komt**: dagverlies-stop, maximum per markt en totaal, GTD-orders die 1 uur voor een bekend moment verlopen, heartbeat elke 5 seconden, cancel-all bij elke onverwachte fout, herstart-afhandeling (punt 24).
6. **Beslismoment**: draait de schaduwbot na 2 weken netto plus (beloning min nepverlies) in de meeste dagen? Zo nee: stoppen, kost niets. Zo ja: verder (GOK op de drempel; zet hem vooraf vast en schuif niet).
7. **Pas dan echt, klein**: een Deposit Wallet met een **Session Key, scope alleen CLOB**, geen hoofdsleutel op de VPS; eerst één markt met minimale orders (grijs in Nederland, zie punt 22; geld uitgeven en account aanmaken alleen na eigen besluit van Thijs).
Uren: GOK 25 tot 40 voor stap 1 tot 5 met een AI als programmeur, daarna 3 tot 5 per week kijken. Kosten tot stap 6: alleen een VPS van een paar euro per maand (run 2, punt 12), of gratis op een eigen pc.

### 28. Freqtrade-config met alle remmen (alleen tekst, sleutelnamen GEZIEN in [config_full.example.json](https://raw.githubusercontent.com/freqtrade/freqtrade/develop/config_examples/config_full.example.json) en [protections.md](https://raw.githubusercontent.com/freqtrade/freqtrade/develop/docs/includes/protections.md))
Let op: de beschermingen staan sinds een tijd **in de strategie** (een `protections`-property), niet meer in de config (GEZIEN, protections.md). De getallen zijn voorbeelden (GOK), geen advies.

Config (stukje):
```json
{
  "dry_run": true,
  "dry_run_wallet": 1000,
  "max_open_trades": 3,
  "stake_amount": "unlimited",
  "tradable_balance_ratio": 0.9,
  "stoploss": -0.08,
  "cancel_open_orders_on_exit": true,
  "force_entry_enable": false,
  "initial_state": "stopped",
  "api_server": { "enabled": true, "listen_ip_address": "127.0.0.1", "listen_port": 8080 }
}
```
Strategie (stukje):
```python
@property
def protections(self):
    return [
        {"method": "CooldownPeriod", "stop_duration_candles": 5},
        {"method": "StoplossGuard", "lookback_period_candles": 24, "trade_limit": 3,
         "stop_duration_candles": 12, "only_per_pair": False},
        {"method": "MaxDrawdown", "calculation_mode": "equity", "lookback_period_candles": 48,
         "trade_limit": 10, "stop_duration_candles": 24, "max_allowed_drawdown": 0.10},
        {"method": "LowProfitPairs", "lookback_period_candles": 24, "trade_limit": 2,
         "stop_duration_candles": 24, "required_profit": 0.0},
    ]
```
Waarom zo: `dry_run` aan tot de terugtest en weken papier kloppen; `initial_state: stopped` zodat een herstart van de server niet vanzelf gaat handelen; `force_entry_enable` uit zodat een AI via MCP of Telegram niet zelf kan kopen (run 3); API alleen op 127.0.0.1. `calculation_mode: "equity"` raadt Freqtrade aan voor nieuwe opzetten (GEZIEN). Dry-run geldt pas als echt geld als je hem bewust op `false` zet (GEZIEN, voorbeeldconfig).

### 29. Rangorde van bouwroutes na run 4 (kans maal opbrengst, alles GOK)
Wat verandert: de beloningsbot op Polymarket krijgt een eigen plek bovenaan, omdat D de pot heeft gemeten, de API vanuit Nederland niet geblokkeerd is en er nu een veilige sleutel bestaat. De kans blijft onder die van D (15 tot 25%), omdat elk verslag van een echte bot dat ik vond op verlies eindigde.

| # | Route en gereedschap | Inleg geld / uren per week | Kans op €10.000 netto in 3 mnd | Ergste geval | Gedaan door anderen? |
|---|---|---|---|---|---|
| 1 | Beloningsbot Polymarket (`polymarket-client`, Session Key, eerst 2 weken schaduw); grijs in NL | €2.000 tot €5.000 / 25 tot 40 bouwen, daarna 3 tot 5 | 8 tot 15% | groot deel inleg kwijt bij nieuws of een val (punt 26); saldo vast, niet af te dwingen | ja, maar de verslagen die ik vond eindigden op verlies (punt 25 en 26) |
| 2 | Voorspellingsmarkt-maker op favorieten 70 tot 90 cent (A), zelfde gereedschap | €1.000 tot €5.000 / 20+ | 5 tot 10% | inleg kwijt, account dicht | voordeel gemeten door A en Kalshi-studie, geen live bot gevonden |
| 3 | Freqtrade futures op Hyperliquid; grijs | €2.000+ / 10 tot 15 | 2 tot 5% | inleg in dagen kwijt | verhalen, zelden controleerbaar |
| 4 | NautilusTrader op HIP-4 | €500+ / 15+ | onder 2% | inleg kwijt | niet gevonden |
| 5 | Freqtrade op Kraken of Bitvavo (legaal, duur of traag) | €10.000+ / 5 tot 10 | onder 2% | daling plus kosten | ja, bescheiden (A) |
| 6 | Grok-sentiment als hoofdsignaal | $40 tot $600 per maand API / 10 | bijna 0% | API-kosten plus verlies | niet gevonden |

Reden voor 8 tot 15% bij route 1: D's model geeft na een zware korting $5.000 tot $30.000 in 90 dagen; de drie verslagen hierboven laten zien dat vullingen en fouten dat makkelijk wegvreten; de schaduwbot (stap 4) maakt de gok binnen 2 weken gratis een meting.

### Nog te doen
- De schaduwbot (punt 27, stap 2 tot 4) als losse code uitschrijven in tekst, met de echte veldnamen uit de OpenAPI-bestanden.
- AFM-waarschuwingslijst nalezen op Hyperliquid en Polymarket.
- Kalshi-beloning en of Kalshi Nederlandse gebruikers toelaat (samen met D).
- Hyperliquid: maximale hefboom per munt en incidenten met de brug.

## Stand na run 4 (19 nov 2026, ±04:00)
1. **Voor de beloningsbot op Polymarket (D's route 1) is het gereedschap er**: officieel `polymarket-client` (de oude `py-clob-client` pakketten zijn afgeschreven, en op 14 dec veranderen API-routes), de API is volgens Polymarket zelf vanuit Nederland niet geblokkeerd (alleen de site), servers in Londen (GEZIEN). Juridisch blijft het grijs (Ksa).
2. **Veilig kan nu**: een Session Key handelt maar "cannot withdraw", 180 dagen, scope alleen CLOB; heartbeat elke 5 seconden annuleert je orders als de bot uitvalt (GEZIEN). Nooit de hoofdsleutel van de wallet in een `.env`.
3. **Malware is hier extreem**: een gekaapte geverifieerde GitHub-organisatie met een werkende Polymarket-bot die sleutels stal (maart 2026), en npm-pakketten als `polymarket-claude-code` die je sleutel vragen (mei 2026) (DERDEN). Alleen het officiële pakket, niets van onbekenden.
4. **Elk verslag van een echte beloningsbot dat ik vond eindigde op verlies**: poly-maker ±−$15 in een korte sessie, een gekloonde bot netto negatief, een bot met een val leeggetrokken voor ruim $1.500 (DERDEN). De winst zit in klein blijven, dunne markten en momenten vlak voor nieuws mijden.
5. **Bouwplan in 7 stappen**, waarvan 6 zonder account en zonder geld: marktenlijst, orderboek opslaan, 2 weken schaduwbot die zijn eigen beloning en nepverlies telt, remmen erin, dan pas beslissen (GOK op uren: 25 tot 40). Voor Freqtrade staat nu een config met alle remmen klaar (punt 28).

## Run 5 (19 nov 2026, ±05:00 Nederlandse tijd)

Deze run: de schaduwbot uit punt 27 uitgeschreven met de echte veldnamen uit de docs, de beloningsformule omgezet in iets wat je zelf kunt narekenen, en de openbare beloningslijst van vannacht zelf gemeten. Niets geïnstalleerd of uitgevoerd van anderen; alleen openbare API's gelezen met curl.

### 30. De beloningsformule in gewone woorden (GEZIEN, [docs Liquidity Rewards](https://docs.polymarket.com/programs/liquidity-rewards.md))
- Elke markt heeft een **maximale afstand** `rewards_max_spread` (in centen, v) en een **minimale grootte** `rewards_min_size`. Orders daarbuiten tellen niet.
- Een order krijgt punten = **((v − afstand) / v)² × grootte**. Kwadratisch: op 1 cent van het midden bij v = 3 krijg je 44% van het maximum, op 2 cent maar 11% (GEZIEN plus eigen rekensom). Dicht bij het midden staan loont dus veel meer dan groot staan.
- Twee kanten: je kooporders op JA tellen samen met je verkooporders op NEE (kant één), en andersom (kant twee). Je score is het **minimum van de twee kanten**; staat het midden tussen 10 en 90 cent, dan telt één kant ook, maar gedeeld door 3. Onder 10 of boven 90 cent: **alleen tweezijdig telt**.
- Elke minuut, op een willekeurig moment, kijkt Polymarket naar het boek: jouw score gedeeld door die van alle makers. Over een UTC-dag (tot 1.440 metingen) opgeteld en dan verdeeld over de pot van die markt. Uitbetaling dagelijks om middernacht UTC, minimaal $1.
- Bij sportwedstrijden tellen orders na de aftrap pas als ze zo lang liggen als de vertraging voor takers. Daarvoor tellen ze direct.
- Wat de docs **niet** precies zeggen: hoe het "size-cutoff-adjusted midpoint" wordt berekend. De schaduwbot moet dat benaderen (GOK: het midden van de beste bied- en laatprijs waar nog minstens `rewards_min_size` staat).

### 31. Gemeten vannacht: de openbare beloningslijst (GEZIEN, `GET https://clob.polymarket.com/rewards/markets/multi`, zonder account, 19 nov ±04:05 UTC)
- De lijst is **groot**: ik haalde 20.000 verschillende markten op en was nog niet aan het eind (GEZIEN). Een volledige download duurt langer dan 10 minuten; filter dus altijd met `order_by=rate_per_day` en `position=DESC`.
- Top 1.000 markten op beloning per dag samen: **±$57.000 per dag** aan actieve beloning (GEZIEN, eigen optelling van `rate_per_day` waar vandaag tussen `start_date` en `end_date` valt; de munt is het adres in `asset_address`, USDC op Polygon bij de markten die ik zag). De 10 grootste samen ±$6.400 per dag; nummer 500 krijgt $30 per dag, nummer 1.000 $13 (GEZIEN).
- 306 van die 1.000 markten zijn op of na 17 nov gemaakt, samen ±$13.300 per dag (GEZIEN). Dat past bij D: jonge markten krijgen veel beloning.
- Er is een veld **`market_competitiveness`** dat nergens in de docs wordt uitgelegd (GEZIEN, alleen als voorbeeldwaarde in de [CLOB OpenAPI](https://docs.polymarket.com/api-spec/clob-openapi.yaml)). Mediaan in de top 1.000: ±5. Er staan markten tussen met **$300 tot $400 per dag en een waarde rond 0** (bijvoorbeeld kleine vragen over de Anthropic-beurs en GTA VI-streams), naast drukke markten met 50 tot 170 (GEZIEN). GOK: het is de som van de scores van de makers die er nu staan. Als dat klopt, is "beloning per dag gedeeld door (competitiveness + 1)" de snelste filter voor de marktenlijst. **Dit is precies wat de schaduwbot als eerste moet toetsen**, want het is een gok op een ongedocumenteerd veld.
- Let op: een markt met $400 per dag en bijna geen makers is ook de markt waar de val uit punt 26 het makkelijkst is en waar weinig handel is om je orders netjes te vullen (GOK).

### 32. Hoe de schaduwbot de concurrentie schat zonder te weten wie wie is
Het openbare boek toont per prijs alleen de totale grootte, niet van welke maker. Je kunt de score van de anderen dus niet exact uitrekenen. Wel twee grenzen (GOK, eigen wiskunde op de formule van punt 30):
- **Optimistisch** (jij krijgt veel): neem voor de anderen samen het minimum van de twee kanten, berekend over het hele boek. Dat is te hoog geschat voor jou, want losse makers zijn vaak eenzijdig.
- **Pessimistisch** (jij krijgt weinig): tel de twee kanten van het hele boek bij elkaar op als score van de anderen.
- Je echte aandeel ligt daartussen. Log beide. Als de pessimistische schatting na kosten nog plus is, is dat een sterk teken; als alleen de optimistische plus is, niet doorgaan (GOK).
- Toets daarna `market_competitiveness`: ligt het dicht bij een van je twee schattingen, dan weet je wat het veld is.

### 33. De schaduwbot als tekst (veldnamen GEZIEN in [Real-Time Data](https://docs.polymarket.com/market-data/realtime-data.md) en de beloningsdocs; de logica is GOK)
Dit is een opzet om aan een AI te geven, geen kant-en-klare code. Alles gebruikt alleen openbare data, dus geen account en geen sleutel.

```text
ELKE 10 MINUTEN  (marktenlijst)
  GET clob.polymarket.com/rewards/markets/multi?order_by=rate_per_day&position=DESC&page_size=500
  houd markten met:
    actieve rewards_config (start_date <= vandaag <= end_date), rate_per_day >= drempel
    created_at jonger dan 2 dagen (D)  of  rate_per_day / (market_competitiveness + 1) hoog
    geen bekende uitslag binnen 48 uur (end_date, eigen lijst met momenten)
  bewaar per markt: condition_id, tokens[].token_id, rewards_min_size, rewards_max_spread

DOORLOPEND  (orderboek, openbaar)
  websocket wss://ws-subscriptions-clob.polymarket.com/ws/market
  of in polymarket-client: client.subscribe(MarketSpec(asset_ids=[...]))
  berichten:
    "book"             -> volledig boek: bids[], asks[] (price, size), tick_size, min_order_size
    "price_change"     -> één prijsniveau veranderd: price, size, side, best_bid, best_ask
    "last_trade_price" -> echte trade: price, size, side, timestamp   <- hiermee nepvullingen
    "tick_size_change" -> nieuwe tick_size: orders opnieuw afronden
  alles naar SQLite (eigen historie voor later terugtesten)

ELKE MINUUT, op een willekeurige seconde  (zoals Polymarket zelf meet)
  midden  = benadering van het adjusted midpoint (punt 30)
  plan    = 1 bod en 1 laat per kant, grootte = rewards_min_size, op 1 tick binnen v,
            scheef naar eigen nepvoorraad
  score   = formule punt 30 voor plan; concurrentie optimistisch en pessimistisch (punt 32)
  beloning_nu = rate_per_day / 1440 * aandeel   (twee getallen)

BIJ ELK "last_trade_price"
  als de trade door de prijs van een geplande order gaat: neem aan dat die order vol is
  (strenger: alleen als de trade groter is dan alles wat vóór jou in de rij stond)
  boek nepvoorraad en nepverlies op de koers 5 en 60 minuten later

ELKE DAG om 00:00 UTC
  regel per markt: beloning (2 schattingen), nepverlies, aantal nepvullingen, max nepvoorraad
```

Waarom de vulling streng geteld moet worden: je staat in de rij achter orders die er al lagen. Telt de bot elke trade op jouw prijs als vulling, dan is hij te somber; telt hij alleen trades die groter zijn dan de rij vóór jou, dan klopt het beter. Log beide (GOK, het probleem van de wachtrij is bekend bij elke terugtest van market making).

Wat de AI vaak fout doet bij deze opzet (GOK, uit ervaring met gegenereerde handelscode en de valkuilen in punt 21 en 25): de oude `py-clob-client` gebruiken in plaats van `polymarket-client`, op `asset_id` filteren in de oude stijl (stuk na 14 dec), prijzen als float in plaats van Decimal (afrondingsfouten op ticks), en de nepvulling op de eigen order zonder wachtrij tellen. Vraag er expliciet naar.

### Nog te doen
- De echte top-lijst een paar dagen achter elkaar meten (wordt de pot groter of kleiner, hoe snel zakt de beloning van een nieuwe markt).
- Uitvinden wat `market_competitiveness` is (forum, Discord-verslagen, of door vergelijken met het boek).
- AFM-waarschuwingslijst nalezen op Hyperliquid en Polymarket (laadt met JavaScript; zoeken naar een andere ingang).
- Hyperliquid: maximale hefboom per munt en incidenten met de brug.

## Stand na run 5 (19 nov 2026, ±05:00)
1. **De beloningsformule is openbaar en na te rekenen**: kwadratisch naar afstand tot het midden, minimum van twee kanten, elke minuut gemeten, dagelijks uitbetaald (GEZIEN). Dicht bij het midden met de minimale grootte staan is de kern; groot staan helpt weinig en vergroot het risico.
2. **De pot is echt groot**: de top 1.000 beloonde markten samen ±$57.000 per dag, waarvan ±$13.300 in markten van de laatste 3 dagen (GEZIEN vannacht). Wat jij daarvan krijgt, hangt af van de concurrentie en is nog niet gemeten.
3. **Er zijn markten met $300 tot $400 per dag en bijna geen concurrentie** volgens een ongedocumenteerd veld (GEZIEN plus GOK op de betekenis). Dat is de eerste hypothese voor de schaduwbot, en ook waar de grootste val ligt.
4. **De schaduwbot staat als tekst klaar** (punt 33), met alleen openbare data, zonder account of geld, met twee schattingen voor concurrentie en twee voor vullingen, zodat de beslissing na 2 weken niet op één optimistisch getal rust (GOK op de opzet).
5. **De vaste regels blijven**: alleen `polymarket-client`, Session Key en nooit de hoofdsleutel, malware rond Polymarket-bots is echt, juridisch grijs in Nederland, en elk verslag van een echte beloningsbot dat ik vond eindigde op verlies (runs 4 en eerder).

## Run 6 (19 nov 2026, ±06:00 Nederlandse tijd)

Deze run: het ongedocumenteerde veld `market_competitiveness` getoetst tegen de echte orderboeken, een eerste ruwe schatting van wat een kleine bot uit de beloningspot zou halen, de pot een tweede keer gemeten, en de Nederlandse rechtszaak nagelopen. Alleen openbare API's gelezen met curl, geen account, niets uitgevoerd van anderen.

### 34. `market_competitiveness` getoetst: het meet de diepte bij het midden (GEZIEN, eigen meting 19 nov ±05:00 UTC)
Werkwijze: de top 120 beloonde markten opgehaald (`/rewards/markets/multi`), per markt het openbare boek van het JA-token (`GET https://clob.polymarket.com/book?token_id=...`), en daarop de formule van punt 30 losgelaten: midden zoals in punt 30 benaderd, elke prijs binnen `rewards_max_spread` telt mee met ((v − afstand)/v)² × grootte, biedkant en laatkant apart.
- De docs geven alleen "Competitiveness score of the market" als uitleg (GEZIEN, [Get raw rewards for a specific market](https://docs.polymarket.com/api-reference/rewards/get-raw-rewards-for-a-specific-market.md)).
- Het verband is sterk: correlatie ±0,9 (op log-schaal) tussen `market_competitiveness` en de score die ik uit het boek reken, het best met "minimum van twee kanten, of de grootste gedeeld door 3" (0,90), net als de echte regel in punt 30 (GEZIEN, eigen berekening over 120 markten).
- Het veld is ongeveer 0,4% van mijn boekscore (mediaan), maar die verhouding schommelt per markt met een factor 2 tot 4 en verschilt per instelling van v en minimale grootte (GEZIEN). GOK: het is een gemiddelde over de dag van de echte makerscores, terwijl ik één momentopname heb en niet weet welke orders onder de minimale grootte vallen. **Conclusie: de gok uit run 5 klopt in grote lijnen.** "Beloning per dag gedeeld door (competitiveness + 1)" is een bruikbare eerste filter, maar de schaduwbot moet de echte deling zelf uit het boek rekenen.

### 35. Eerste ruwe schatting: wat zou een kleine bot krijgen (GOK op GEZIEN-data, één momentopname, géén resultaat)
Aanname: per markt één bod en één laat met de minimale grootte, op de beste prijs aansluitend (afstand = halve spread, minstens 0,5 cent), dus ongeveer de minimale grootte in dollars aan inzet per markt. Aandeel = mijn score / (mijn score + die van de rest), met de rest optimistisch (de regel uit punt 30) en pessimistisch (beide kanten opgeteld, punt 32).
- Mediaan over de top 120: **±$5 per dag per $100 inzet optimistisch, ±$2 pessimistisch** (GEZIEN als rekensom, GOK als verwachting).
- Uitschieters met $70 tot $245 per dag per $100 zitten allemaal in markten met bijna geen makers, zoals de prijsbandjes rond de beursgang van Anthropic, "zegt Trump woord X" en een OpenRouter-markt (GEZIEN).
- **Waarom dit geen opbrengst is:** het telt geen verlies op vullingen. In precies die markten springt de prijs bij nieuws (beursgang, toespraak) en word je dan vol gelopen aan de verkeerde kant; de verslagen in punt 26 eindigden daardoor op verlies. Ook: één momentopname, andere makers reageren zodra jij er staat, en Polymarket meet elke minuut. Dit getal zegt alleen dat de schaduwbot het waard is om te draaien, niet dat de route werkt (GOK).
- Wat dit wel oplevert voor het bouwplan: de schaduwbot moet per markt **nepverlies tegenover beloning** loggen, en markten met een bekend nieuwsmoment (beursgang op een vaste dag, een toespraak) uitsluiten of vlak ervoor alle orders weghalen. Dat stond als regel in punt 33; de meting bevestigt dat de duurste markten juist die nieuwsmarkten zijn.

### 36. De pot een uur later (GEZIEN, zelfde meting als punt 31, 19 nov ±05:00 UTC)
Top 1.000: **±$56.200 per dag** (run 5: ±$57.000). Top 10: ±$6.460. Nummer 500: $29, nummer 1.000: $12. Markten van 17 nov of later: 321 stuks, samen ±$13.500 per dag. Binnen een uur dus vrijwel gelijk; over dagen meten blijft nodig.

### 37. Nederland: Polymarket vecht het verbod aan bij de rechter (DERDEN)
Polymarket is in oktober 2026 naar de rechter in Den Haag gestapt tegen het verbod van de Ksa. Het stelt dat het financiële producten verkoopt (afgeleiden, toezicht door de AFM) en geen kansspel (DERDEN, [DutchNews 5 okt 2026](https://www.dutchnews.nl/2026/10/polymarket-goes-to-court-to-overturn-dutch-gambling-ban/), [NL Times](https://nltimes.nl/2026/10/05/us-prediction-site-polymarket-fight-dutch-ban-court), [Gambling Insider](https://www.gamblinginsider.com/nl/?p=109438)). Een uitspraak vond ik niet. Voor een gebruiker verandert het nu niets: het verbod en de blokkade gelden, meedoen kan alleen via een VPN en breekt de voorwaarden (zie punt 22 en D). Wint Polymarket, dan wordt het mogelijk legaal maar onder AFM-regels; verliest het, dan blijft het grijs of wordt het strenger (GOK).

### Nog te doen
- De meting van punt 34 en 35 een paar keer per dag herhalen om te zien of de verhouding stabiel is (dan kan de bot op het veld vertrouwen).
- Per markt het nepverlies op vullingen schatten uit `last_trade_price` over een paar uur (dat is het getal dat beslist).
- Uitspraak in de zaak Polymarket tegen de Ksa volgen.
- Hyperliquid: maximale hefboom per munt en incidenten met de brug.

## Stand na run 6 (19 nov 2026, ±06:00)
1. **`market_competitiveness` is in grote lijnen de score van de makers bij het midden**: correlatie ±0,9 met wat ik zelf uit het openbare boek reken (GEZIEN). Bruikbaar als eerste filter, niet als exacte deling.
2. **Ruwe papieren beloning voor een kleine bot: mediaan $2 tot $5 per dag per $100 inzet** in de top 120, met uitschieters in lege nieuwsmarkten (GOK op GEZIEN-data, momentopname zonder vullingsverlies). Dit is reden om de schaduwbot te draaien, geen belofte.
3. **Het echte risico zit in de vullingen bij nieuws**: de markten met de hoogste beloning per maker zijn juist markten met een vast nieuwsmoment. Elk verslag van een echte beloningsbot dat ik vond eindigde op verlies (runs 4 tot 6).
4. **De pot is stabiel groot**: ±$56.000 per dag in de top 1.000, ±$13.500 daarvan in markten van de laatste dagen (GEZIEN, twee metingen een uur uit elkaar).
5. **Vaste regels blijven**: alleen `polymarket-client`, Session Key en nooit de hoofdsleutel, malware rond Polymarket-bots is echt, en in Nederland is het verboden door de Ksa; Polymarket vecht dat sinds oktober aan bij de rechter, zonder uitspraak (DERDEN).
