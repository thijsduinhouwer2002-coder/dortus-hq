# Onderzoek AI-handelsbots (prive voor Thijs, 19 nov 2026)

Thijs wil met eigen geld gaan handelen met hulp van een AI-bot en ziet op TikTok en X veel over Grok-tradingbots en varianten. Hij vraagt: zoek het goed uit, help, rem niet af. Dit is geen Dortus-product; het is onderzoek voor Thijs zelf.

**De repo is openbaar.** Schrijf nooit bedragen, rekeningen, accounts, wallets of andere persoonlijke of financiële gegevens van Thijs op. Alleen algemene informatie over tools en werkwijzen.

## Vraag van Thijs 19 nov 01:11 (gaat voor, beide zoekers)
Thijs wil elke maand een vast bedrag van een paar honderd euro inleggen en zoekt een bot of opzet die daarbij past, gevonden op GitHub en in forums. Zoek daarom ook, elk in je eigen hoek:
- **A (strategie en testen):** welke aanpakken passen bij een vaste maandelijkse inleg van die grootte: periodiek kopen (DCA), DCA met regels (meer kopen na een daling), grid, herbalanceren tussen een paar munten of ETF's, en wat terugtests en ervaringen daarover zeggen tegenover gewoon elke maand kopen en vasthouden. Let op kosten: bij kleine bedragen eten kosten per trade de winst op; reken een voorbeeld door met echte tarieven (DERDEN met link).
- **B (gereedschap):** open source projecten op GitHub die precies dit doen (bijv. DCA-bots, Freqtrade met DCA, herbalanceer-scripts) met sterren, laatste update, beurzen die ze steunen, en of ze in Nederland bruikbaar zijn (Bitvavo, Kraken). Plus wat beurzen en brokers zelf al ingebouwd hebben voor automatisch periodiek kopen of beleggen, zodat duidelijk is wanneer een eigen bot niets toevoegt. Plus ervaringen uit forums (r/algotrading, r/freqtrade, r/BitcoinBeginners, Tweakers, het forum van Freqtrade): wat werkt bij kleine maandbedragen en wat niet.
Geen persoonlijk advies en geen "koop dit": alleen wat er is, wat het kost, wat de bewijzen zeggen, en de risico's.

## Bijgesteld 19 nov 00:55 (Thijs: "kant en klare sws niks")
Thijs wil zelf bouwen. Zoeker A stopt met kant-en-klaar; wat hij al vond blijft staan in `A-kant-en-klaar.md` als lijst van wat te mijden. Vanaf nu:
- **A. Strategie, data en testen** (`A-strategie-en-testen.md`): welke strategieën voor een eigen bot aantoonbaar iets doen (met bronnen, geen verkooppraat), hoe je eerlijk terugtest (overfitting, kosten, slippage), op papier handelt, risico beheert (stop-loss, positiegrootte, maximaal verlies per dag), welke data je nodig hebt en waar je die gratis haalt, en hoe je Grok of een ander model zinvol inzet (bijv. sentiment van X) en wat dat in de praktijk opleverde.
- **B. Gereedschap en bouwen** (`B-zelf-bouwen.md`): frameworks, beurzen en hun API's in Nederland, kosten, veiligheid, en een concreet bouwplan.

## Oorspronkelijke opzet (A is vervangen, zie hierboven)
- **A. Kant-en-klaar:** platforms en apps met AI- of botfuncties waarmee je zonder te programmeren kunt handelen (bijv. Pionex, 3Commas, Cryptohopper, Bitsgap, TradingView-koppelingen, copy trading bij eToro of Bitget, Grok-bots in X, wat er op TikTok gepromoot wordt). Per platform: wat doet het, wat kost het, beschikbaar in Nederland, vergunning of registratie (MiCA, AFM, DNB), echte gebruikerservaringen en bewezen resultaten (geen verkooppraat), en rode vlaggen. Plus de oplichting: welke namen zijn bekend als scam (AFM-waarschuwingslijst, nieuws).
- **B. Zelf bouwen met AI:** een eigen bot met Grok, Claude of ChatGPT als hulp, gekoppeld aan een beurs met een API (bijv. Bitvavo, Kraken, Coinbase, Binance; ook aandelen via Interactive Brokers of Alpaca). Open source frameworks (Freqtrade, Hummingbot, Jesse, OctoBot, en wat er op GitHub met Grok of LLM's bestaat), hoe je terugtest en op papier handelt, welke strategieën mensen echt gebruiken, wat het kost, veiligheid (API-sleutels zonder opnamerecht, nep-repo's met malware), en de claims van TikTok nagetrokken.

## Werkwijze per run
1. Lees eerst je eigen bestand (`A-kant-en-klaar.md` of `B-zelf-bouwen.md`). Bouw erop voort; herhaal niets wat er al staat. Zoek elk uur een nieuwe hoek of verdiep wat er al staat.
2. Elk cijfer en elke claim krijgt GEZIEN (zelf gelezen, met link), DERDEN (met link) of GOK. Geen verkooppraat overnemen als feit.
3. Onderaan je bestand: een korte sectie **"Stand na run <tijd>"** met de 5 belangrijkste dingen tot nu toe.
4. Geen accounts maken, nergens inloggen, niets kopen, niets downloaden en uitvoeren van GitHub (alleen lezen), geen geld of crypto aanraken.
