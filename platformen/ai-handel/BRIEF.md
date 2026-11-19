# Onderzoek AI-handelsbots (prive voor Thijs, 19 nov 2026)

Thijs wil met eigen geld gaan handelen met hulp van een AI-bot, liefst een vast bedrag van een paar honderd euro per maand, en wil zelf bouwen (kant-en-klare platforms vindt hij niks). Hij vraagt: zoek het goed uit, help, rem niet af. Dit is geen Dortus-product; het is onderzoek voor Thijs zelf. Geen persoonlijk advies en geen "koop dit": alleen wat er is, wat het kost, wat de bewijzen zeggen, en de risico's.

**De repo is openbaar.** Schrijf nooit bedragen van Thijs, rekeningen, accounts, wallets of andere persoonlijke of financiële gegevens van Thijs op. Alleen algemene informatie over tools en werkwijzen.

## Doel en denkwijze (Thijs, 19 nov 01:19, geldt voor alle vier)
Denk als iemand die **binnen 3 maanden €10.000 winst moet maken** met eigen tijd en bots. De vaste maandinleg van een paar honderd euro is een apart onderwerp (zoeker C) en is niet de grens voor de andere routes. Zoek dus niet alleen naar "netjes beleggen", maar naar de routes die dat doel echt zouden kunnen halen. Zet per route erbij: wat je moet inleggen (geld en uren per week), hoe groot de kans is dat het lukt (GOK mag, met reden), wat het ergste geval is, en of mensen het aantoonbaar gedaan hebben (bron). Eindig je stand met een rangorde van routes op kans maal opbrengst.

**Grijs gebied mag.** Grijs betekent: tegen de voorwaarden van een platform in (bijv. bonusjagen, meerdere accounts waar dat alleen een regel van het platform breekt), of juridisch onduidelijk (bijv. een beurs zonder MiCA-vergunning gebruiken als particulier). Zeg er per keer bij wat het risico is (account dicht, geld vastgezet, boete) en hoe groot.
**Niet doen, ook niet als grijs gebied:** iets wat duidelijk illegaal is: fraude, valse of andermans identiteit, witwassen, marktmanipulatie (pump and dump, wash trading, spoofing), belasting ontduiken, het geld van anderen beheren zonder vergunning, of iemand benadelen. Die routes noem je hoogstens als "bestaat, valt af, omdat".

## Vier zoekers, elk uur 's nachts tot ±08:00 (verdeeld 19 nov 01:15)
Elke zoeker heeft één hoek en één bestand. Lees bij de start ook de bestanden van de anderen kort, zodat je niets dubbel doet.

- **A. Strategie en testen** (`A-strategie-en-testen.md`): welke strategieën voor een eigen bot aantoonbaar iets doen (met bronnen, geen verkooppraat), hoe je eerlijk terugtest (overfitting, kosten, slippage), op papier handelt, risico beheert (stop-loss, positiegrootte, maximaal verlies per dag), welke data je nodig hebt en waar je die gratis haalt, en hoe je Grok of een ander model zinvol inzet (bijv. sentiment van X) en wat dat in de praktijk opleverde.
- **B. Gereedschap en bouwplan** (`B-zelf-bouwen.md`): frameworks (Freqtrade, Hummingbot, Jesse, OctoBot en wat er met LLM's op GitHub bestaat), beurzen en hun API's in Nederland, kosten, veiligheid (sleutels zonder opnamerecht, nep-repo's met malware), en een concreet bouwplan van nul tot een bot die op papier draait.
- **C. Vaste maandinleg** (`C-maandinleg.md`): welke aanpak past bij een vaste inleg van een paar honderd euro per maand: periodiek kopen (DCA), DCA met regels (meer kopen na een daling), grid, herbalanceren tussen een paar munten of ETF's; wat terugtests en ervaringen zeggen tegenover gewoon elke maand kopen en vasthouden. Reken voorbeelden door met echte tarieven (bij kleine bedragen eten kosten de winst op). Wat beurzen en brokers zelf al ingebouwd hebben voor automatisch periodiek kopen of beleggen, zodat duidelijk is wanneer een eigen bot niets toevoegt. Open source projecten die precies dit doen, en ervaringen uit forums (r/BitcoinBeginners, r/freqtrade, Tweakers, het forum van Freqtrade).
- **D. Arbitrage** (`D-arbitrage.md`): zoek zelf, zonder vooraf ingevulde conclusie, alle vormen van arbitrage en prijsverschil-handel die iemand met weinig startgeld en een bot kan doen: in crypto, aandelen, valuta, voorspellingsmarkten, bonussen en promoties, tweedehands en verzamelobjecten, kaartjes, of iets wat niemand verwacht. Zoek vooral waar mensen het nu echt doen en verdienen (GitHub, Reddit, Discord-verslagen, forums, Telegram-kanalen die openbaar te lezen zijn), en reken per vorm door wat er na kosten overblijft.

`A-kant-en-klaar.md` is van de eerste run (kant-en-klare platforms, MiCA-lijst, oplichting) en blijft staan als naslag; daar schrijft niemand meer in. Twee TikTok-voorbeelden van oplichting ("GrokBot V3", @ptrading2, en "Grok Bot x Phantom", @s0fyx_fx) staan in het verslag van de hoofdchat van 19 nov.

## Werkwijze per run
1. Lees eerst je eigen bestand. Bouw erop voort; herhaal niets wat er al staat. Zoek elk uur een nieuwe hoek of verdiep wat er al staat.
2. Elk cijfer en elke claim krijgt GEZIEN (zelf gelezen, met link), DERDEN (met link) of GOK. Geen verkooppraat overnemen als feit.
3. Onderaan je bestand: een korte sectie **"Stand na run <tijd>"** met de 5 belangrijkste dingen tot nu toe.
4. Geen accounts maken, nergens inloggen, niets kopen, niets downloaden en uitvoeren van GitHub (alleen lezen), geen geld of crypto aanraken.

## Geschiedenis van deze opdracht
(Hieronder de oude versies, ter naslag. De verdeling hierboven gaat voor.)
> Thijs wil met eigen geld gaan handelen met hulp van een AI-bot en ziet op TikTok en X veel over Grok-tradingbots en varianten. Hij vraagt: zoek het goed uit, help, rem niet af. Dit is geen Dortus-product; het is onderzoek voor Thijs zelf.
> 
> **De repo is openbaar.** Schrijf nooit bedragen, rekeningen, accounts, wallets of andere persoonlijke of financiële gegevens van Thijs op. Alleen algemene informatie over tools en werkwijzen.
> 
> ## Vraag van Thijs 19 nov 01:13: arbitrage (gaat voor, zoeker A)
> Thijs denkt aan een arbitrage-bot (crypto, aandelen of een andere markt). Zoek uit, met cijfers en bronnen: (1) prijsarbitrage tussen beurzen en driehoeksarbitrage voor iemand met een klein bedrag: wat blijft er na kosten, opnametijd en snelheid over, en waar wint de gewone gebruiker nog; (2) funding-rate-arbitrage (spot kopen en de perpetual shorten): echte rendementen over 2025 en 2026, de risico's (funding draait om, liquidatie, beurs valt om), hoeveel geld je minimaal nodig hebt, en of en waar dit in Nederland mag met een MiCA- of MiFID-partij (perpetuals zijn voor particulieren in de EU beperkt); (3) arbitrage in kleine, weinig efficiënte markten (bijv. tweedehands, kaartjes, verzamelobjecten, voorspellingsmarkten): waar een bot prijsverschillen vindt die grote spelers laten liggen, wat het oplevert en wat het kost. Open source arbitrage-projecten op GitHub (bijv. Hummingbot) en ervaringen op forums horen erbij.
> 
> ## Vraag van Thijs 19 nov 01:11 (gaat voor, beide zoekers)
> Thijs wil elke maand een vast bedrag van een paar honderd euro inleggen en zoekt een bot of opzet die daarbij past, gevonden op GitHub en in forums. Zoek daarom ook, elk in je eigen hoek:
> - **A (strategie en testen):** welke aanpakken passen bij een vaste maandelijkse inleg van die grootte: periodiek kopen (DCA), DCA met regels (meer kopen na een daling), grid, herbalanceren tussen een paar munten of ETF's, en wat terugtests en ervaringen daarover zeggen tegenover gewoon elke maand kopen en vasthouden. Let op kosten: bij kleine bedragen eten kosten per trade de winst op; reken een voorbeeld door met echte tarieven (DERDEN met link).
> - **B (gereedschap):** open source projecten op GitHub die precies dit doen (bijv. DCA-bots, Freqtrade met DCA, herbalanceer-scripts) met sterren, laatste update, beurzen die ze steunen, en of ze in Nederland bruikbaar zijn (Bitvavo, Kraken). Plus wat beurzen en brokers zelf al ingebouwd hebben voor automatisch periodiek kopen of beleggen, zodat duidelijk is wanneer een eigen bot niets toevoegt. Plus ervaringen uit forums (r/algotrading, r/freqtrade, r/BitcoinBeginners, Tweakers, het forum van Freqtrade): wat werkt bij kleine maandbedragen en wat niet.
> Geen persoonlijk advies en geen "koop dit": alleen wat er is, wat het kost, wat de bewijzen zeggen, en de risico's.
> 
> ## Bijgesteld 19 nov 00:55 (Thijs: "kant en klare sws niks")
> Thijs wil zelf bouwen. Zoeker A stopt met kant-en-klaar; wat hij al vond blijft staan in `A-kant-en-klaar.md` als lijst van wat te mijden. Vanaf nu:
> - **A. Strategie, data en testen** (`A-strategie-en-testen.md`): welke strategieën voor een eigen bot aantoonbaar iets doen (met bronnen, geen verkooppraat), hoe je eerlijk terugtest (overfitting, kosten, slippage), op papier handelt, risico beheert (stop-loss, positiegrootte, maximaal verlies per dag), welke data je nodig hebt en waar je die gratis haalt, en hoe je Grok of een ander model zinvol inzet (bijv. sentiment van X) en wat dat in de praktijk opleverde.
> - **B. Gereedschap en bouwen** (`B-zelf-bouwen.md`): frameworks, beurzen en hun API's in Nederland, kosten, veiligheid, en een concreet bouwplan.
> 
> ## Oorspronkelijke opzet (A is vervangen, zie hierboven)
> - **A. Kant-en-klaar:** platforms en apps met AI- of botfuncties waarmee je zonder te programmeren kunt handelen (bijv. Pionex, 3Commas, Cryptohopper, Bitsgap, TradingView-koppelingen, copy trading bij eToro of Bitget, Grok-bots in X, wat er op TikTok gepromoot wordt). Per platform: wat doet het, wat kost het, beschikbaar in Nederland, vergunning of registratie (MiCA, AFM, DNB), echte gebruikerservaringen en bewezen resultaten (geen verkooppraat), en rode vlaggen. Plus de oplichting: welke namen zijn bekend als scam (AFM-waarschuwingslijst, nieuws).
> - **B. Zelf bouwen met AI:** een eigen bot met Grok, Claude of ChatGPT als hulp, gekoppeld aan een beurs met een API (bijv. Bitvavo, Kraken, Coinbase, Binance; ook aandelen via Interactive Brokers of Alpaca). Open source frameworks (Freqtrade, Hummingbot, Jesse, OctoBot, en wat er op GitHub met Grok of LLM's bestaat), hoe je terugtest en op papier handelt, welke strategieën mensen echt gebruiken, wat het kost, veiligheid (API-sleutels zonder opnamerecht, nep-repo's met malware), en de claims van TikTok nagetrokken.
> 
> ## Werkwijze per run
> 1. Lees eerst je eigen bestand (`A-kant-en-klaar.md` of `B-zelf-bouwen.md`). Bouw erop voort; herhaal niets wat er al staat. Zoek elk uur een nieuwe hoek of verdiep wat er al staat.
> 2. Elk cijfer en elke claim krijgt GEZIEN (zelf gelezen, met link), DERDEN (met link) of GOK. Geen verkooppraat overnemen als feit.
> 3. Onderaan je bestand: een korte sectie **"Stand na run <tijd>"** met de 5 belangrijkste dingen tot nu toe.
> 4. Geen accounts maken, nergens inloggen, niets kopen, niets downloaden en uitvoeren van GitHub (alleen lezen), geen geld of crypto aanraken.
