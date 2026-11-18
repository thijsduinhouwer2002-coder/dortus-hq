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
