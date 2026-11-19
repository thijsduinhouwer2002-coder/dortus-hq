# A. Strategie, data en eerlijk testen (zoeker A)

Onderzoek voor Thijs zelf, geen Dortus-product, geen advies en geen "koop dit". Niets over zijn geld of accounts.
Labels: GEZIEN = zelf gelezen of zelf gemeten (met bron), DERDEN = iemand anders zegt het (met link), GOK = eigen inschatting.
Taakverdeling (BRIEF): A doet welke strategieën iets doen, eerlijk terugtesten, papier handelen, risico, data en de inzet van Grok of een ander model. Gereedschap en bouwplan staan bij B (`B-zelf-bouwen.md`), maandinleg bij C, arbitrage bij D. Wat chatbots met echt geld deden (Alpha Arena) staat al in `A-kant-en-klaar.md`, punt 4.

## Run 1 (19 nov 2026, ±01:00 tot 01:35)

### 1. De kern in één alinea
Een terugtest die er mooi uitziet zegt bijna niets over de toekomst. Het enige wat telt is hoe een strategie het doet op data die je niet gebruikte om haar te kiezen, na kosten. Dat heb ik zelf nagemeten op vier jaar BTC en ETH in euro (punt 2): de beste instelling uit het verleden zakte daarna van een Sharpe van 1,86 naar 0,33. Een simpele trendregel verloor minder dan kopen en vasthouden in slechte tijden, maar verdiende geen fortuin. Een taalmodel als Grok is in de bot hooguit een extra filter, geen voorspeller (punt 6). (GOK als samenvatting van wat hieronder staat.)

### 2. Eigen meting: een simpele trendregel op echte data (GEZIEN)
**Wat:** dagkoersen BTC-EUR en ETH-EUR van Bitvavo, 11 dec 2022 tot 19 nov 2026, 1440 dagen, openbare API zonder account (`api.bitvavo.com/v2/BTC-EUR/candles?interval=1d&limit=1440`). Regel: sloot de koers gisteren boven het gemiddelde van de laatste N dagen, dan in de munt, anders in euro. Kosten 0,25% per wissel (Bitvavo taker, GEZIEN door B). Getest voor N = 10, 20, ... 200. Eerste 60% van de periode om te kiezen (in-sample), laatste 40% om te controleren (out-of-sample, vanaf 23 apr 2025). Script in een paar regels Python; ik kan het zo in dit bestand zetten als Thijs het zelf wil draaien.

| | BTC in-sample (jun 2023 tot apr 2025) | BTC out-of-sample (apr 2025 tot nov 2026) |
|---|---|---|
| Kopen en vasthouden | x2,99, grootste daling 32% | x0,70, grootste daling 52% |
| Beste N in-sample (SMA 40) | x2,75, Sharpe 1,86, 38 wissels | x0,98, Sharpe 0,33, grootste daling 33% |
| Tweede (SMA 70) | x2,72, Sharpe 1,74 | x0,94, Sharpe 0,19 |
| Mediaan van alle 20 instellingen | | x0,94 |

| | ETH in-sample | ETH out-of-sample |
|---|---|---|
| Kopen en vasthouden | x0,92, grootste daling 65% | x1,04, grootste daling 67% |
| Beste N in-sample (SMA 60) | x1,57, Sharpe 0,97 | x1,47, Sharpe 0,87 |
| Mediaan van alle 20 instellingen | | x1,30 |

**Walk-forward** (elke 90 dagen de beste N kiezen op het jaar ervoor, dan 90 dagen handelen, jun 2024 tot nov 2026): BTC x1,17 tegen kopen en vasthouden x1,00; ETH x1,10 tegen x0,50 (GEZIEN, zelfde data). De gekozen N sprong heen en weer (BTC van 20 tot 170), een teken dat er geen vaste "beste" instelling is.

**Wat dit leert** (GOK, op basis van de meting):
- De beste instelling uit het verleden is daarna veel slechter. Precies wat de grote studie hieronder ook vond.
- De trendregel deed vooral één ding: **grote dalingen kleiner maken** (BTC 33% in plaats van 52%). Dat is de bekende rol van trendvolgen, geen geldmachine.
- Kosten deden ertoe: SMA 10 met ±100 wissels ging out-of-sample van x0,92 zonder kosten naar x0,71 met kosten.
- Vier jaar is kort en het zijn maar twee munten; dit bewijst niets, het is een eerlijk voorbeeld van hoe je test.

### 3. Wat het bewijs zegt over strategieën
- **Een terugtest voorspelt weinig.** Quantopian keek naar 888 strategieën met minstens 6 maanden echte uitslag na de terugtest: de Sharpe uit de terugtest voorspelde de latere Sharpe nauwelijks (R² kleiner dan 0,025). Hoe meer iemand had getest, hoe groter het gat. Volatiliteit en grootste daling voorspelden wel iets (DERDEN, [Quantpedia over Wiecki e.a.](https://quantpedia.com/quantopians-academic-paper-about-in-vs-out-of-sample-performance-of-trading-alg/)). Gevolg: kijk bij je eigen test meer naar de daling en de schommeling dan naar het rendement (GOK).
- **De koers van bitcoin voorspellen lukt niet aantoonbaar.** Een overzicht van honderden studies uit juni 2026: geen enkele peer-reviewed studie liet op 1 tot 6 maanden overtuigend zien dat ze beter is dan "de prijs van vandaag"; dagelijkse voorspelbaarheid is er misschien, maar "may not survive transaction costs" (DERDEN, [arXiv 2606.00071](https://arxiv.org/abs/2606.00071)). Ze raden aan: walk-forward testen, meerdere marktfasen apart houden, altijd vergelijken met het naïeve antwoord, en "niets doen" als optie in je instellingen meenemen (DERDEN, zelfde link).
- **Trendvolgen in crypto** heeft de meeste steun in onderzoek, maar let op te mooie papers. Voorbeeld: "AdaptiveTrend" claimt een Sharpe van 2,41 en een grootste daling van maar 12,7% over 150+ munten, 2022 tot 2024 (DERDEN, [arXiv 2602.11708](https://arxiv.org/abs/2602.11708)). Dat is niet peer-reviewed en gebruikt veel bouwstenen tegelijk (eigen stop, eigen muntkeuze, 70/30 lang/kort); zulke getallen halen echte fondsen zelden (GOK). Gebruik het als idee, niet als belofte.
- **Mean reversion, grid en market making** deze run nog niet onderbouwd met bronnen; grid hoort deels bij C, market making bij D.

### 4. Eerlijk terugtesten: de checklist
1. **Splits de data** voor je begint: een stuk om te kiezen, een stuk dat je pas aan het eind één keer bekijkt. Beter nog walk-forward (punt 2). (GOK, standaardpraktijk; aanbevolen in [arXiv 2606.00071](https://arxiv.org/abs/2606.00071), DERDEN.)
2. **Tel hoeveel varianten je probeerde.** Wie 20 instellingen test en de beste kiest, moet die Sharpe omlaag bijstellen; daar is de "Deflated Sharpe Ratio" voor (DERDEN, [Bailey en López de Prado, pdf](https://escholarship.org/content/qt2329p290/qt2329p290.pdf)). Een AI die "even 50 varianten probeert" maakt dit probleem juist groter (GOK).
3. **Echte kosten erin**, per kant, plus een stukje slippage. Bij Bitvavo taker 0,25% per kant (GEZIEN door B). Test ook met dubbele kosten: houdt het dan nog stand? (GOK)
4. **Geen blik in de toekomst.** Signaal op de slotkoers van gisteren, handelen vanaf vandaag. Freqtrade heeft `lookahead-analysis` en `recursive-analysis` om dit te controleren (GEZIEN door B in de README). AI-code maakt deze fout vaak (GOK).
5. **Vergelijk altijd met kopen en vasthouden** en met "niets doen" over precies dezelfde periode (GOK; zie punt 2 waar dat het hele beeld bepaalt).
6. **Kijk naar meerdere marktfasen**: stijging (2023 tot begin 2025), daling (BTC apr 2025 tot nu, x0,70, GEZIEN). Een strategie die alleen in één fase werkt, is een gok op die fase (GOK).
7. **Dan op papier**: Freqtrade dry-run met echte koersen, minstens een paar weken (GOK voor de duur, zie B stap 5). Vergelijk de papieren uitslag met wat de terugtest over dezelfde weken zou zeggen; een groot verschil betekent een fout in de test (GOK).

### 5. Risico beheren (regels in gewone code, niet in de AI)
Deze run nog geen bronnen nagelezen; dit zijn gangbare regels, als GOK gelabeld.
- **Positiegrootte**: riskeer per trade een vast klein deel van de pot (vaak 1 tot 2% wordt genoemd), en reken de grootte terug vanaf je stop-loss (GOK).
- **Verwacht de daling**: kopen en vasthouden had in deze vier jaar al dalingen van 52% (BTC) en 67% (ETH) (GEZIEN, punt 2). Wie dat niet aankan, moet kleiner of met een trendregel (GOK).
- **Maximaal verlies per dag en per week**: de bot stopt vanzelf bij bijvoorbeeld 3% verlies op een dag en wacht op een mens (GOK). Freqtrade heeft hiervoor "protections" (zoals een stop na een reeks verliezen); nog niet zelf nagelezen.
- **Geen hefboom** in het begin: met hefboom kan één slechte dag alles wegvagen, en perpetuals zijn voor particulieren in de EU beperkt (zie D en `A-kant-en-klaar.md`) (GOK).
- **Stop-loss op de beurs** waar het kan (Kraken wel, Bitvavo niet via Freqtrade; GEZIEN door B).

### 6. Grok of een ander model inzetten: wat zegt het bewijs
- **Kosten van X lezen via Grok**: de tool `x_search` kost $5 per 1000 opgehaalde posts, plus de tokens; elke teruggegeven post telt, ook geciteerde posts (GEZIEN, [docs.x.ai pricing](https://docs.x.ai/developers/pricing.md)). Rekenvoorbeeld: 100 posts per uur, dag en nacht, is 72.000 posts per maand, dus ±$360 per maand alleen voor het zoeken (GOK, eigen som op GEZIEN-prijs). 20 posts per uur is ±$72. Dat is veel meer dan de ±$5 die B rekende voor een vraag per uur zonder zoeken.
- **Sentiment van tweets voorspelt bitcoin-rendement niet aantoonbaar.** Een studie met tweet-sentiment (VADER): aandacht op X voorspelde het handelsvolume, niet het rendement; een strategie op aandacht won alleen in 2018 en niet in de andere jaren (DERDEN, [UTS, "On the predictive power of tweet sentiments and attention on bitcoin"](https://opus.lib.uts.edu.au/handle/10453/161851)).
- **Bij aandelen werkt LLM-sentiment wel iets, maar de test is lastig.** Een model kent de afloop van oude nieuwsberichten (blik in de toekomst) en laat zich afleiden door wat het al over een bedrijf weet. Verrassend: berichten zonder bedrijfsnaam deden het in de test béter (DERDEN, [arXiv 2309.17322](https://arxiv.org/abs/2309.17322)). Een andere studie met 12 bevroren OpenAI-versies vond dat een "vooruitzicht-score" van het model samenhing met rendement een maand later over ±7.000 Amerikaanse aandelen (DERDEN, [arXiv 2604.21433](https://arxiv.org/abs/2604.21433)). Dat gaat over aandelen en over langzame informatie, niet over snel crypto handelen (GOK).
- **Live tests met chatbots als trader** verloren meestal (zie `A-kant-en-klaar.md`, Alpha Arena).
- **Zinvolle inzet** (GOK, volgt uit het bovenstaande):
  1. De AI schrijft en controleert de code; de strategie zelf is gewone regels (zie B).
  2. Als signaal: alleen als filter ("is er groot nieuws, handel vandaag niet" of "beurs gehackt, alles dicht"), niet als koop- of verkoopknop.
  3. Test een LLM-signaal alleen op de periode ná de kennisgrens van het model, anders kent het de afloop al. Haal munt- of bedrijfsnamen weg als dat kan (DERDEN, arXiv 2309.17322).
  4. Sla elke vraag en elk antwoord op, zodat je later kunt terugtesten wat het model echt zei; je kunt het verleden niet opnieuw vragen zonder dat het model meer weet (GOK).

### 7. Data: wat je gratis kunt halen
- **Bitvavo**: dagcandles tot 1440 stuks per verzoek, zonder account (GEZIEN, gebruikt in punt 2). Kortere intervallen bestaan ook (`1h`, `5m`); de grens van 1440 per verzoek betekent: in stukken ophalen (GOK).
- **Binance openbare archieven**: maandbestanden met candles per paar, bijv. BTCEUR per uur vanaf jan 2020, te lezen zonder account en ook vanaf deze server bereikbaar (GEZIEN, `data.binance.vision`, lijst van `data/spot/monthly/klines/BTCEUR/1h/`). Handig om lang terug te testen, ook als je op een andere beurs handelt (GOK; kleine prijsverschillen tussen beurzen zijn klein, zie D punt 1).
- **Kraken**: API geeft maar 720 candles; voor meer: trades downloaden of hun CSV-bestanden (GEZIEN door B).
- **Funding rates** (voor wie later perpetuals bekijkt): OKX en Hyperliquid openbaar (GEZIEN door D).
- **Freqtrade** haalt zelf data op met `download-data` (GEZIEN door B).

### 8. Richting €10.000 in 3 maanden (doel uit de BRIEF), vanuit deze hoek
- Een trendbot op spot zonder hefboom deed in mijn meting out-of-sample tussen x0,98 (BTC) en x1,47 (ETH) over ±19 maanden (GEZIEN). Over 3 maanden is een realistisch goede uitkomst dus enkele procenten tot misschien 10 à 20%, en verlies kan net zo goed (GOK). Voor €10.000 winst in 3 maanden heb je dan een pot van tienduizenden euro's nodig (GOK, eigen som).
- Met hefboom kan het getal kloppen op papier, maar de kans op een grote of totale daling gaat evenredig omhoog (GOK).
- Rangorde van routes binnen hoek A op kans maal opbrengst (GOK):
  1. **Simpele trendregel op spot, weinig wissels, limietorders**: kleine kans op groot geld, wel de beste kans om de grote dalingen te ontwijken. Inleg: een paar avonden bouwen, daarna ±1 uur per week (GOK).
  2. **Trend over meer munten met vaste risico per trade**: iets meer kans op een uitschieter, meer werk en meer kans op overfitting (GOK).
  3. **LLM-sentiment als hoofdsignaal**: geen bewijs dat het in crypto werkt, kost tientallen tot honderden dollars per maand aan zoekopdrachten (GOK op GEZIEN-prijs). Valt af als hoofdroute.
  4. **Hefboom om het doel te halen**: hoogste opbrengst op papier, hoogste kans op alles kwijt. Valt af als startpunt.

### Nog te doen (volgende runs)
- Freqtrade "protections" en stop-loss-opties nalezen in de docs (curl).
- Bronnen voor mean reversion en voor positiegrootte in crypto (volatiliteit richten).
- Meting uitbreiden: uurdata van Binance-archieven, meer munten, test met dubbele kosten, en vergelijken met maandelijks kopen (afstemmen met C).
- Is er een openbaar, controleerbaar verslag van iemand die Grok of een ander model live liet meebeslissen over maanden?

## Stand na run 01:35 (19 nov 2026)
1. **Eigen meting** (GEZIEN): de beste trendinstelling op BTC uit 2023 tot 2025 zakte daarna van Sharpe 1,86 naar 0,33; wel was de grootste daling 33% tegen 52% bij kopen en vasthouden. Trendvolgen beperkt dalingen, het is geen geldmachine.
2. **Terugtest-Sharpe voorspelt bijna niets** (R² kleiner dan 0,025 over 888 strategieën, DERDEN); hoe meer je test, hoe groter het gat. Altijd walk-forward, kosten erin, vergelijken met kopen en vasthouden.
3. **Bitcoin-koers voorspellen** op 1 tot 6 maanden lukt in geen enkele peer-reviewed studie overtuigend (DERDEN, juni 2026); tweet-sentiment voorspelde volume, geen rendement (DERDEN).
4. **Grok laten meelezen op X is duur**: $5 per 1000 posts (GEZIEN), dus tientallen tot honderden dollars per maand bij uurlijkse checks (GOK). Gebruik een model hooguit als filter, en test alleen na zijn kennisgrens.
5. **Gratis data genoeg**: Bitvavo-candles en de Binance-archieven zijn zonder account te halen (GEZIEN). €10.000 in 3 maanden past niet bij een eerlijke spot-strategie met een kleine pot (GOK).
