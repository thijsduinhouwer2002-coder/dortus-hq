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

## Run 2 (19 nov 2026, ±01:35 tot 02:05 UTC)
Nieuwe hoek: D en B zetten voorspellingsmarkten bovenaan als bot-route. Ik keek dus vanuit "strategie en testen" naar die markten: welke prijsfout is aangetoond, en kun je die zelf eerlijk nameten? Freqtrade-remmen (StoplossGuard, MaxDrawdown) staan al bij B punt 13; die herhaal ik niet.

### 9. Aangetoond op Kalshi: goedkope contracten verliezen, dure winnen een beetje (DERDEN)
Studie van University College Dublin, jan 2026, met transactiedata van meer dan 300.000 contracten op Kalshi, 2021 tot 2025 (DERDEN, [Bürgi, Deng en Whelan, "Makers and Takers", pdf](https://www.karlwhelan.com/Papers/Kalshi.pdf); samenvatting op [VoxEU](https://cepr.org/voxeu/columns/economics-kalshi-prediction-market)):
- Wie contracten van 10 cent of minder koopt, verliest gemiddeld **meer dan 60%** van zijn inleg. Contracten boven 50 cent geven een klein positief rendement, boven 70 cent statistisch zeker maar klein (DERDEN, zelfde pdf).
- Gemiddeld rendement van alle Kalshi-contracten: **ongeveer min 20%** (DERDEN).
- **Makers** (je zet een order in het boek) haalden gemiddeld -9,64%, **takers** (je pakt een bestaande order) -31,46%. Makers die contracten van 50 cent of meer kochten, haalden **+2,6%** (DERDEN, zelfde pdf, pag. bij figuur 6).
- De fout werd in 2025 kleiner (DERDEN): wie hierop bouwt, bouwt op iets wat langzaam verdwijnt (GOK).
- Op Polymarket weermarkten vond een studie uit okt 2026 dat vlak voor sluiten (laatste 1 tot 12 uur) juist de **favorieten te duur** zijn, bijna tien keer sterker dan de longshot-fout (DERDEN, [arXiv 2610.13593](https://arxiv.org/abs/2610.13593)). Dus: de richting van de fout verschilt per platform, soort markt en tijdstip.

**Wat dit betekent voor een bot** (GOK, volgt uit het bovenstaande): de enige strategie met echt bewijs is saai: **als maker** dure contracten kopen (50 cent en meer) en nooit longshots als taker. Opbrengst ±2 à 3% per contract vóór je geld weer vrij is. Dat past bij D punt 10 ("bijna zeker kopen is een eerlijke prijs") en maakt duidelijk dat €10.000 in 3 maanden hiermee alleen kan met een zeer grote pot of heel veel omloop.

### 10. Eigen meting op Polymarket: het tegendeel, en waarom je dat niet moet geloven (GEZIEN)
**Wat:** openbare API's zonder account. Gesloten ja/nee-markten uit `gamma-api.polymarket.com/markets` met de uitslag, en de dagkoers van "Ja" uit `clob.polymarket.com/prices-history` (`fidelity=1440`; uurdata gaf lege antwoorden). Per markt de prijs 1, 7 en 30 dagen voor sluiten, beide kanten (ja en nee) meegeteld. Twee steekproeven: (a) de 900 gesloten markten met het **meeste volume** sinds jan 2025 (892 met koersgeschiedenis), (b) de 900 laatst gesloten markten met minstens $20.000 volume, 6 tot 17 nov 2026 (867 met koers; 336 daarvan "Bitcoin Up or Down").

| Prijs 1 dag voor sluiten | (a) n | (a) gewonnen | (a) rendement | (b) n | (b) gewonnen | (b) rendement |
|---|---|---|---|---|---|---|
| 0 tot 10 cent (gem. 3 à 4) | 167 | 6,6% | +100% | 56 | 12,5% | +199% |
| 40 tot 60 cent | 297 | 50,2% | ±0% | 359 | 49,9% | ±0% |
| 90 tot 100 cent (gem. 96 à 97) | 167 | 93,4% | -3,4% | 56 | 87,5% | -8,7% |

(GEZIEN, eigen telling; zonder kosten, op de middenkoers. 7 en 30 dagen voor sluiten gaven hetzelfde beeld voor longshots, maar met grillige tussenbanden.)

Op het oog: longshots kopen wint, favorieten kopen verliest, precies andersom dan Kalshi. **Dat is vrijwel zeker een testfout** (GOK, met reden):
1. **Kiezen op volume lekt de uitslag.** Een markt waar een verrassing gebeurt, krijgt in de laatste dagen veel extra handel. Wie "markten met het meeste volume" kiest, kiest dus vooral markten waar de longshot won. Dat is een blik in de toekomst, net als in punt 4 regel 4.
2. **Middenkoers is geen prijs die je kon krijgen.** Bij dunne boeken ligt de laatprijs voor een longshot vaak een paar cent hoger; op 3 cent gemiddeld is 1 cent verschil al een derde van de inleg (GOK).
3. **Te weinig gevallen.** 56 tot 167 longshots, waarvan er maar 7 tot 11 wonnen. Een paar markten uit hetzelfde event (bijv. een WK-wedstrijd) hangen samen. De Kalshi-studie had 300.000 contracten.
4. **Dagkoers is grof.** De laatste dagnotering kan uren oud zijn op het moment dat het nieuws al bekend is.

**Les voor wie een voorspellingsmarkt-bot test** (GOK, eigen protocol uit deze meting plus de studies):
- Kies markten op iets wat je **vooraf** wist (aanmaakdatum, categorie, volume tot het moment van instappen), nooit op eindvolume.
- Gebruik de **laatprijs of biedprijs** op het moment van instappen (het orderboek bewaren vanaf nu; de API geeft geen oude boeken), niet de middenkoers.
- Minstens enkele duizenden markten, verdeeld over categorieën en maanden; reken per event, niet per contract.
- Kosten erin: Polymarket haalt op 20 nov de kortingen voor kleine handelaren weg (GEZIEN door D punt 8).
- Begin met papier: de koersen en uitslagen zijn openbaar, dus een bot kan weken meedraaien zonder geld en zonder account (GEZIEN, de API's hierboven werkten zonder inloggen).

### 11. Bijgestelde rangorde binnen hoek A (kans maal opbrengst, GOK)
1. **Voorspellingsmarkten als maker, alleen favorieten, eerst op papier**: de enige strategie in mijn hoek met groot bewijs (300.000 contracten), maar klein rendement per keer (±2,6% vóór je geld vrij is, DERDEN) en de fout krimpt. Voor €10.000 in 3 maanden: kans onder 5% met een kleine pot (GOK). Grijs in Nederland, zie D punt 3.
2. Simpele trendregel op spot (run 1): beperkt dalingen, geen geldmachine. Kans op het doel onder 1% (GOK, zelfde als B).
3. Longshots kopen omdat een terugtest dat mooi laat zien: **valt af**; mijn eigen meting laat zien hoe makkelijk die terugtest liegt.
4. LLM-sentiment als hoofdsignaal en hefboom: vallen af (run 1).

### Nog te doen (volgende runs)
- Meting op Polymarket zonder volumefout: markten kiezen op aanmaakdatum, meer dan 2.000 stuks; kijken of de gamma-API verder pagineert dan 900 (beide keren stopte het daar, GEZIEN).
- Momentum over meer munten tegelijk met volatiliteit richten, op Binance-archieven, met dubbele kosten (stond al op de lijst).
- Openbaar, controleerbaar verslag van een LLM die maanden live meebeslist.

## Stand na run 02:05 (19 nov 2026)
1. **Enige aangetoonde prijsfout die ik vond die een kleine bot kan pakken**: op Kalshi verliezen goedkope contracten (10 cent of minder) gemiddeld meer dan 60%, en makers die contracten van 50 cent of meer kopen haalden +2,6% (DERDEN, 300.000 contracten, UCD jan 2026). Klein per keer, en het gat wordt kleiner.
2. **Mijn eigen Polymarket-meting liet het tegendeel zien** (longshots +100% tot +199%, GEZIEN), maar dat is een testfout: kiezen op eindvolume lekt de uitslag. Dit is het schoolvoorbeeld waarom je een terugtest niet gelooft zonder vooraf vastgelegde keuzes en echte laatprijzen.
3. **Terugtests voorspellen weinig** (run 1: Sharpe 1,86 naar 0,33 in mijn eigen trendtest, GEZIEN; R² onder 0,025 over 888 strategieën, DERDEN). Trendvolgen beperkt dalingen, maakt geen fortuin.
4. **Grok of een ander model**: geen bewijs dat sentiment van X het rendement in crypto voorspelt (DERDEN), en meelezen kost $5 per 1000 posts (GEZIEN). Hooguit als filter; laat de AI vooral de code schrijven en controleren.
5. **€10.000 in 3 maanden** haalt geen van de routes in hoek A met een kleine pot (GOK). De beste kans binnen deze hoek is een maker-bot op voorspellingsmarkten die eerst weken op papier draait op openbare data (GEZIEN: alles zonder account op te halen), met de grijze risico's die D beschrijft.

## Run 3 (19 nov 2026, ±02:35 tot 02:55 UTC)
Hoek: de meting uit run 2 opnieuw doen **zonder de volumefout**. Dat is de belangrijkste open vraag in mijn hoek, want "maker op favorieten" staat bovenaan mijn rangorde.

### 12. Eigen meting op Polymarket, nu eerlijk gekozen: dezelfde richting als Kalshi (GEZIEN)
**Hoe gekozen** (alles vooraf te weten, niets over de uitslag):
- Gesloten markten met een einddatum tussen 1 sep en 10 nov 2026 die minstens 8 dagen vóór die einddatum begonnen (filter `start_date_max` op `gamma-api.polymarket.com/markets/keyset`, zonder account). **Geen filter op volume.** Zo vallen de snelle "Up or Down"-markten van een paar minuten vanzelf weg.
- Dat gaf 6.266 verschillende ja/nee-markten met een uitslag, uit 1.020 events (GEZIEN). Daaruit 3.000 willekeurig getrokken (vaste seed).
- Instapmoment: vast 1 of 7 dagen vóór de **geplande** einddatum, en alleen als de markt toen nog open was. Run 2 nam "1 dag voor sluiten"; dat lekt ook, want een markt die vroeg sluit doet dat meestal omdat er iets gebeurde.
- Prijs: de laatste dagnotering van "Ja" uit `clob.polymarket.com/prices-history` (`interval=max&fidelity=1440`) die niet ouder is dan 2 dagen; uurdata over deze periode gaf lege antwoorden (GEZIEN). Beide kanten meegeteld (ja tegen p, nee tegen 1 min p).
- Onzekerheid: bootstrap per **event** (1.000 keer), omdat markten uit hetzelfde event samenhangen.

**Uitslag, 7 dagen voor de einddatum** (1.909 markten, 672 events; GEZIEN, eigen telling, middenkoers, zonder kosten):

| Prijs | n | gem. prijs | gewonnen | rendement | 90%-band (per event) | met 1 cent duurder instappen |
|---|---|---|---|---|---|---|
| 0 tot 10 cent | 422 | 3,2 ct | 2,6% | -19% | -61% tot +21% | -38% |
| 10 tot 30 cent | 413 | 21,5 ct | 16,0% | **-26%** | -40% tot -10% | -29% |
| 30 tot 70 cent | 2.138 | 49,9 ct | 50,0% | ±0% | | -2% |
| 70 tot 90 cent | 422 | 78,2 ct | 83,4% | **+6,6%** | +2,2% tot +10,6% | +5,3% |
| 90 tot 100 cent | 423 | 96,8 ct | 97,4% | +0,7% | -0,7% tot +2,0% | -0,4% |

**1 dag voor de einddatum** (1.533 markten, 543 events, GEZIEN): 10 tot 30 cent -18% (band -34% tot -2%), 70 tot 90 cent **+4,9%** (band +0,4% tot +9,1%), 90 tot 100 cent -0,6%, onder 10 cent +14% maar met een band van -27% tot +60% (dus: niets te zeggen).

**Per deel** (70 tot 90 cent, 7 dagen ervoor, GEZIEN): sep +3,9% (n=150), okt +5,0% (n=176), nov +13,9% (n=96); sport +11,9% (n=218), overig +1,2% (n=204). Overal positief, maar de grootte springt flink.

**Wat dit leert** (GOK, op basis van de meting):
1. **Run 2 was inderdaad een testfout.** Zonder volumefilter verdwijnt de "longshots winnen"-uitslag (+100% tot +199%) helemaal. Zelfde API, zelfde rekenwijze, alleen de keuze van markten anders. Het beste bewijs in dit bestand dat de selectie de uitslag maakt.
2. **De richting klopt nu met de Kalshi-studie** (punt 9): ondergewaardeerde favorieten (70 tot 90 cent) en overgewaardeerde kanshebbers (10 tot 30 cent). Let op: dat zijn twee kanten van dezelfde markten, dus één bevinding, geen twee.
3. **Het voordeel is klein en zit in de middenband.** Rond +5% per contract op de middenkoers, en het overleeft 1 cent slechtere instap (+5,3%). Boven 90 cent is er niets te halen. Twee cent slechter of de nieuwe kosten van Polymarket vanaf 20 nov (D punt 8) kunnen het grotendeels opeten (GOK).
4. **Waarom je dit nog niet gelooft:** dagnoteringen tot 2 dagen oud, middenkoers in plaats van wat je echt kon krijgen, maar 2,5 maand data, en het verschil tussen sport (+12%) en de rest (+1%) is groot. De keyset-API gaf veel dubbele markten terug (113.600 regels voor 6.275 unieke), dus de steekproef per dag is niet compleet; die keuze hangt niet aan de uitslag, maar is wel onvolledig (GEZIEN voor de telling, GOK voor het effect).

**Ruw rekenvoorbeeld** (GOK, eigen som op bovenstaande): +5% per contract met je geld een week vast, en 30 tot 60 van zulke markten per week in de band 70 tot 90 cent. Dan is het rendement op de inzet in 3 maanden hooguit enkele tientallen procenten, vóór kosten en vóór de kans dat het gat in 2025 tot 2026 al kleiner werd. €10.000 in 3 maanden vraagt dan nog steeds een pot van tienduizenden euro's.

### 13. Het testprotocol voor een voorspellingsmarkt-bot (aangescherpt, GOK op basis van run 2 en 3)
1. Kies markten op **begin- en einddatum**, nooit op volume, nooit op de echte sluittijd.
2. Instappen op een **vast moment** ten opzichte van de geplande einddatum.
3. Bootstrap per event; meld een band, geen los getal.
4. Test met +1 en +2 cent slechtere instap. Wat bij +2 cent weg is, is te dun voor een echte bot.
5. Splits per maand en per soort markt; als één soort alles draagt (hier sport), test die apart verder.
6. Vanaf nu het **orderboek zelf opslaan** (de API bewaart geen oude boeken). Pas na een paar weken eigen opgeslagen boeken weet je wat een maker-order echt had opgeleverd.

### Bijgestelde rangorde binnen hoek A (kans maal opbrengst, GOK)
1. **Voorspellingsmarkten, favorieten 70 tot 90 cent, als maker, eerst op papier**: nu door twee onafhankelijke metingen gesteund (Kalshi 300.000 contracten, DERDEN; mijn eigen Polymarket-meting, GEZIEN). Wel klein (±5%) en wankel per soort markt. Kans op €10.000 in 3 maanden met een kleine pot: onder 5% (GOK, ongewijzigd). Grijs in Nederland (D punt 3).
2. Simpele trendregel op spot (run 1): beperkt dalingen, geen geldmachine.
3. Longshots, LLM-sentiment als hoofdsignaal, hefboom: vallen af.

### Nog te doen (volgende runs)
- Sport apart meten met meer maanden (jan tot aug 2026), en kijken of het voordeel in de band 70 tot 90 cent vlak voor de wedstrijd zit.
- De keyset-API netjes pagineren (dubbele resultaten), zodat elke dag volledig is.
- Momentum over meer munten met volatiliteit richten, op Binance-archieven, met dubbele kosten.
- Openbaar, controleerbaar verslag van een LLM die maanden live meebeslist.

## Stand na run 02:55 UTC (19 nov 2026)
1. **Eerlijke herhaling op Polymarket** (GEZIEN, 1.909 markten uit 672 events, gekozen op datum, niet op volume): favorieten van 70 tot 90 cent wonnen vaker dan hun prijs zei, **+6,6%** 7 dagen voor de einddatum (band +2,2% tot +10,6%), en +4,9% 1 dag ervoor. Contracten van 10 tot 30 cent verloren 18 tot 26%. Zelfde richting als Kalshi (DERDEN, 300.000 contracten).
2. **De longshot-winst uit run 2 was puur een selectiefout** (GEZIEN): zonder volumefilter is ze weg. Kies markten nooit op iets wat pas achteraf bekend is.
3. **Het voordeel is dun**: het overleeft 1 cent slechtere instap (+5,3%), maar twee cent of de nieuwe Polymarket-kosten kunnen het opeten (GOK); en het zit vooral in sport (+12%) tegen +1% bij de rest (GEZIEN, kleine aantallen).
4. **Terugtests voorspellen weinig** (run 1: Sharpe 1,86 naar 0,33 in mijn trendtest, GEZIEN; R² onder 0,025 over 888 strategieën, DERDEN). Trendvolgen beperkt dalingen, meer niet. Een taalmodel hooguit als filter; meelezen op X kost $5 per 1000 posts (GEZIEN).
5. **€10.000 in 3 maanden** haalt geen route in hoek A met een kleine pot (GOK). De beste kans blijft een maker-bot op favorieten in voorspellingsmarkten, eerst weken op papier met zelf opgeslagen orderboeken (alles zonder account te halen, GEZIEN).

## Run 4 (19 nov 2026, ±03:35 tot 04:05 UTC)
Hoek: de bevinding uit run 3 (favorieten van 70 tot 90 cent winnen ±5%) **toetsen op een periode die ik nog niet had bekeken**: jan tot aug 2026. Run 3 gebruikte sep tot nov. Ik legde vooraf vast wat telt: dezelfde keuze van markten, dezelfde instapmomenten, dezelfde band. Dat is de eerlijkste test die er is: een vooraf vastgelegde regel op nieuwe data.

### 14. Toets op nieuwe data: het voordeel bij favorieten blijft, de sportconclusie niet (GEZIEN)
**Hoe** (zelfde werkwijze als punt 12, alles openbaar en zonder account):
- Alle gesloten markten met een geplande einddatum van 1 jan tot 31 aug 2026 die minstens 8 dagen ervoor begonnen, per dag volledig gepagineerd via `gamma-api.polymarket.com/markets/keyset` (nu wel netjes: 278.256 unieke markten, 273.765 met een uitslag, uit 42.346 events; GEZIEN). Geen filter op volume.
- Daaruit 5.000 willekeurig getrokken (vaste seed), maximaal 2 per event, half "hoofdmarkt van een wedstrijd" (event met een datum in de naam, of over/onder), half de rest. Koersgeschiedenis per dag uit `clob.polymarket.com/prices-history` (4.959 met data, GEZIEN).
- Instap 7 of 1 dag vóór de geplande einddatum, alleen als de markt toen nog open was; dagkoers niet ouder dan 2 dagen; beide kanten; bootstrap per event (1.000 keer, 90%-band). Plus drie kostenscenario's: 1 cent duurder, 2 cent duurder, en de takerkosten van Polymarket vanaf 20 nov (`tarief × p × (1 − p)`, sport 0,05, de rest gerekend met 0,01; tarieven GEZIEN door D punt 8).

**Uitslag, alle markten** (GEZIEN, eigen telling, middenkoers):

| Prijs | 7 dagen ervoor: n, rendement, band | +2 cent | 1 dag ervoor: n, rendement, band | +2 cent |
|---|---|---|---|---|
| 0 tot 10 cent | 364, **-50%**, -77% tot -19% | -66% | 766, -10%, -37% tot +18% | -37% |
| 10 tot 30 cent | 550, **-20%**, -33% tot -7% | -28% | 947, **-18%**, -28% tot -7% | -26% |
| 30 tot 70 cent | 6.455, -2,5% | -6% | 2.926, -1,6% | -5% |
| 70 tot 90 cent | 555, **+4,4%**, +0,9% tot +7,7% | +1,8% | 933, **+4,3%**, +1,7% tot +6,9% | +1,7% |
| 90 tot 100 cent | 374, +2,5%, +1,0% tot +3,8% | +0,4% | 792, -0,1% | -2,1% |

Takerkosten maakten weinig uit (70 tot 90 cent: +3,8% en +3,5% na kosten), want ze zijn klein bij dure contracten. Een paar cent slechtere prijs weegt veel zwaarder (GEZIEN).

**Per soort** (70 tot 90 cent, GEZIEN):

| Soort | 7 dagen ervoor | 1 dag ervoor |
|---|---|---|
| Hoofdmarkt wedstrijd (wie wint, over/onder) | -2,4% (n=267, band -8% tot +4%) | +2,4% (n=563, band -1% tot +6%) |
| Bijzetmarkten sport (exacte uitslag, handicap, gelijk bij rust, "meeste sixes") | **+16,1%** (n=168, band +12% tot +20%; +13% bij 2 cent duurder) | **+6,8%** (n=279, band +3% tot +11%) |
| De rest (politiek, tweets van Musk, prijzen, "zegt Trump X") | +3,2% (n=120, band -4% tot +10%) | +8,3% (n=91, band +1% tot +15%) |

De spiegelkant klopt: in de bijzetmarkten verloren contracten van 10 tot 30 cent **62%** (7 dagen) en 34% (1 dag) (GEZIEN). Per maand (70 tot 90 cent, alles behalve hoofdmarkten, 7 dagen): 7 van de 8 maanden positief (GEZIEN).
De indeling in soorten deed ik met trefwoorden in de vraag en de eventnaam; dat is grof (GOK voor de nauwkeurigheid).

**Wat dit leert** (GOK, op basis van de meting):
1. **De hoofdbevinding houdt stand op nieuwe data.** Vooraf vastgelegd: band 70 tot 90 cent. Uitslag: +4,4% en +4,3%, band boven nul, tegen +6,6% en +4,9% in run 3. Twee perioden, twee keer dezelfde richting, plus de Kalshi-studie (punt 9). Dit is nu het best onderbouwde patroon in mijn hele bestand.
2. **Mijn sportconclusie uit run 3 was ruis.** Toen droeg sport alles (+12%); nu doen de hoofdmarkten van wedstrijden niets (-2,4% en +2,4%). Les: een uitsplitsing op een kleine groep (n=218) is een nieuwe hypothese, geen bevinding. Precies daarom toets je op nieuwe data.
3. **Waar het wel zit: de bijzetmarkten.** Mensen kopen graag "Ja" op een exacte uitslag of een grote handicap (een lot uit de loterij); "Nee" daarop is te goedkoop. Dat past bij de bekende longshot-fout bij bookmakers (GOK, zelfde mechanisme als Kalshi). Maar: dit is een uitsplitsing die ik pas ná het kijken maakte, dus het is een **nieuwe hypothese** die eerst op een derde periode moet (sep tot nov 2026, of de weken die nu komen op papier).
4. **Waarom je het nog steeds niet blind gelooft:** middenkoers per dag, en bijzetmarkten hebben vaak dunne boeken met een grote afstand tussen bied en laat (GOK; niet gemeten, want oude orderboeken zijn niet op te halen). Als je daar 3 tot 5 cent meer betaalt dan het midden, is +16% snel +5% of minder (GOK, eigen som: bij 80 cent is 4 cent 5%).

**Rekenvoorbeeld** (GOK, eigen som): +4% per contract op een week vastgezet geld, maar je kunt niet elke week alles inzetten (lang niet genoeg markten in de band met ruimte in het boek). Stel 20 tot 40% van de pot per week aan het werk: dan ±1 à 2% per week, ±12 à 25% in 3 maanden, vóór slechtere prijzen. €10.000 winst vraagt dan nog altijd een pot van ruwweg €40.000 tot €80.000, en de grootste onzekerheid is hoeveel je per markt echt kwijt kunt zonder de prijs te bederven.

### 15. Wat de bot hieruit moet doen (testplan voor de komende weken, GOK)
1. **Elke dag het orderboek opslaan** van alle open bijzetmarkten en "overige" markten waar een kant tussen 70 en 90 cent staat (openbaar, zonder account; zie B punt 27 voor het gereedschap).
2. Per markt vastleggen: beste laatprijs, hoeveel er op die prijs ligt, en de middenkoers. Na de uitslag rekenen met de **laatprijs** (taker) en met "had een maker-order 1 cent onder het midden gevuld worden?".
3. Vooraf vastleggen wat "werkt" betekent: na 300 markten, laatprijs, band per event boven +2%. Haalt het dat niet, dan valt de route af (GOK als drempel, gekozen omdat +2% de buffer is voor slechtere vullingen in het echt).
4. Pas daarna denken aan echt geld; en dan met de grijze risico's die D (punt 3 en 16) voor Nederland beschrijft.

### Bijgestelde rangorde binnen hoek A (kans maal opbrengst, GOK)
1. **Voorspellingsmarkten, kant van 70 tot 90 cent kopen, vooral in bijzetmarkten van sport en "overige" markten, eerst weken op papier met echte laatprijzen.** Nu gesteund door twee perioden van eigen meting (GEZIEN) en de Kalshi-studie (DERDEN). Klein (±4% gemiddeld, misschien meer in bijzetmarkten) en afhankelijk van hoe dun de boeken zijn. Kans op €10.000 in 3 maanden met een kleine pot: onder 5% (GOK, ongewijzigd, want de pot is de grens, niet het voordeel).
2. Simpele trendregel op spot (run 1): beperkt dalingen, geen geldmachine.
3. Hoofdmarkten van wedstrijden (wie wint): **valt af** als aparte route; op nieuwe data geen voordeel.
4. Longshots, LLM-sentiment als hoofdsignaal, hefboom: vallen af.

### Nog te doen (volgende runs)
- Bijzetmarkten apart toetsen op sep tot nov 2026 (derde periode), met een nette indeling op eventsoort in plaats van trefwoorden.
- Hoe dun zijn de boeken nu? Een momentopname van de bied-laat-afstand in open bijzetmarkten met een kant tussen 70 en 90 cent (`clob.polymarket.com/book`, openbaar).
- Momentum over meer munten met volatiliteit richten (blijft liggen; laagste kans op het doel).

## Stand na run 04:05 UTC (19 nov 2026)
1. **Vooraf vastgelegde toets op nieuwe data geslaagd** (GEZIEN): favorieten van 70 tot 90 cent op Polymarket wonnen in jan tot aug 2026 **+4,4%** (7 dagen voor de einddatum) en **+4,3%** (1 dag), band boven nul; in run 3 (sep tot nov) +6,6% en +4,9%. Zelfde richting als Kalshi (DERDEN, 300.000 contracten). Takerkosten eten weinig, 2 cent slechtere prijs halveert het ruwweg.
2. **Het zit in de bijzetmarkten van sport** (exacte uitslag, handicap, gelijk bij rust): "Nee"-kant op 70 tot 90 cent **+16%** 7 dagen ervoor, +6,8% 1 dag ervoor; de "Ja"-loten van 10 tot 30 cent verloren 34 tot 62% (GEZIEN). Dit is een uitsplitsing achteraf, dus een nieuwe hypothese voor de volgende toets, en die boeken zijn waarschijnlijk dun (GOK).
3. **Mijn sportconclusie uit run 3 was ruis** (GEZIEN): de hoofdmarkten van wedstrijden geven op nieuwe data geen voordeel (-2,4% en +2,4%). Les voor elke bot: een uitsplitsing op een kleine groep is pas iets na een toets op nieuwe data.
4. **Terugtests liegen makkelijk** (run 1: Sharpe 1,86 naar 0,33, GEZIEN; run 2: longshot-"winst" door volumekeuze, GEZIEN; R² onder 0,025 over 888 strategieën, DERDEN). Een taalmodel hooguit als filter; meelezen op X kost $5 per 1000 posts (GEZIEN).
5. **€10.000 in 3 maanden** haalt geen route in hoek A met een kleine pot (GOK): bij ±1 à 2% per week op de pot is er ruwweg €40.000 tot €80.000 nodig. De beste stap nu kost niets: weken lang openbare orderboeken opslaan en op papier rekenen met echte laatprijzen (testplan punt 15).

## Run 5 (19 nov 2026, ±04:35 tot 05:10 UTC)
Hoek: run 4 rekende met de **getoonde koers per dag**. De open vraag was: kun je die prijs in het echt krijgen? Twee metingen, allebei openbaar en zonder account: (a) hoe breed en hoe dun zijn de boeken nu, (b) wat verdienden mensen die in sep tot nov 2026 **echt** een favoriet van 70 tot 90 cent kochten (echte uitgevoerde trades, geen koers). Geen namen of wallets van handelaren opgeschreven.

### 16. Momentopname van de boeken: de getoonde prijs is vaak niet te krijgen (GEZIEN)
**Hoe:** open markten met een einddatum binnen 8 dagen die minstens 2 dagen eerder begonnen, via `gamma-api.polymarket.com/markets/keyset` (20.000 markten opgehaald; ik stopte bij 200 pagina's, dus niet compleet, en het zijn bijna allemaal sportmarkten: 19.626 van de 20.000; GEZIEN). Indeling nu niet meer met trefwoorden maar met het veld `sportsMarketType` dat Polymarket zelf meegeeft (bijv. `moneyline`, `totals`, `soccer_exact_score`, `spreads`, `soccer_halftime_result`; GEZIEN). Hoofdmarkt = `moneyline` en `totals`; bijzetmarkt = elk ander sporttype; overig = geen sporttype. Daarvan alleen markten waar een kant tussen 70 en 90 cent staat. Steekproef van 75 boeken nagekeken met `clob.polymarket.com/book` (GEZIEN; de cijfers kwamen overeen met de velden `bestBid` en `bestAsk`).

| Groep (kant 70 tot 90 cent) | n | halve bied-laat-afstand, mediaan | aandeel met halve afstand van 2 cent of minder |
|---|---|---|---|
| Bijzet, einde over minder dan 1 dag | 162 | 3,0 ct | 44% |
| Bijzet, 1 tot 3 dagen | 1.828 | 3,0 ct | 33% |
| Bijzet, 3 tot 8 dagen | 575 | **14,0 ct** | 23% |
| Hoofd, minder dan 1 dag | 78 | 1,5 ct | 78% |
| Hoofd, 1 tot 3 dagen | 1.169 | 3,5 ct | 38% |
| Overig (alle termijnen) | 48 | 5,5 ct | 29% |

In de 75 nagekeken boeken lag er bij de **mediane markt niets** te koop binnen 2 cent boven het midden; de beste laatprijs had een mediaan van $109 tot $208 aan stukken erop (GEZIEN).

**Polymarket toont het midden, maar bij een afstand van meer dan 10 cent de laatste handelsprijs** (GEZIEN, [docs Prices & Orderbook](https://docs.polymarket.com/concepts/prices-orderbook.md)). Dat raakt run 4 direct: de "+16% in bijzetmarkten 7 dagen ervoor" komt uit precies de groep met een halve afstand van ±14 cent, dus daar rekende ik met de laatste handelsprijs, niet met een prijs die te krijgen was. Kopen tegen de laatprijs kost daar ±15% van de inzet extra (GOK, eigen som: 14 ct op 80 ct is 17%). **Die +16% is voor een bot die koopt dus niet te halen.**

### 17. Wat echte kopers verdienden, sep tot nov 2026 (GEZIEN, vooraf vastgelegd)
**Vooraf vastgelegd** (voor ik keek): periode 1 sep tot 10 nov 2026 (de periode van run 3, maar toen niet per soort gesplitst), indeling met `sportsMarketType` zoals in punt 16, en als maat het rendement op elke **echt uitgevoerde** trade waarbij iemand de kant van 70 tot 90 cent kocht.
**Hoe:** per week en per sporttype de eerste pagina gesloten markten uit de keyset-API (filter `sports_market_types`), daaruit willekeurig getrokken: 520 markten, 356 met trades (207 bijzet, 149 hoofd; GEZIEN). Trades uit `data-api.polymarket.com/v2/trades?condition=...` (de oude v1 is uitgezet, GEZIEN). Een verkoop van de ene kant tegen p telde ik als koop van de andere kant tegen 1 min p. Ik neem aan dat het veld `side` de kant van de nemer is (GOK, niet in de docs nagelezen). Bootstrap per event, 90%-band. "Laat" = in de laatste 4 uur voor de laatste trade van die markt, dus meestal tijdens de wedstrijd (GOK voor die uitleg).

| Groep | trades | events | per trade | per dollar |
|---|---|---|---|---|
| Bijzet, alles | 1.066 | 86 | +9,4% (band -6,7% tot +20,2%) | +17,4% (-0,5% tot +26,7%) |
| Bijzet, vóór de laatste 4 uur | 503 | 30 | +10,5% (-18,4% tot +25,1%) | +20,7% (-1,8% tot +30,6%) |
| Hoofd, alles | 5.673 | 106 | +6,2% (-1,8% tot +13,7%) | **+17,9% (+10,9% tot +23,9%)** |
| Hoofd, vóór de laatste 4 uur | 717 | 44 | +6,5% (-15,2% tot +19,2%) | +20,0% (-8,4% tot +27,3%) |

De mediane trade in deze band was $13, de 90% grootste $313 (GEZIEN).

**Wat dit leert** (GOK, op basis van punt 16 en 17):
1. **Het patroon is niet alleen een rekenfout.** Mensen die echt een favoriet van 70 tot 90 cent kochten, verdienden gemiddeld; alle getallen zijn positief. Dat steunt de richting van run 3 en 4 en de Kalshi-studie.
2. **Maar het is niet bewezen voor een bot.** Bijna alle banden per trade lopen door nul, er zijn weinig events vóór de wedstrijd (30 en 44), en de enige band die ruim boven nul ligt (hoofd, per dollar) wordt gedragen door grote trades vlak voor of tijdens de wedstrijd. Wie tijdens de wedstrijd wint, weet vaak sneller wat er op het veld gebeurt; dat is geen voordeel dat een trage bot heeft.
3. **Mijn sterkste getal uit run 4 vervalt.** De +16% in bijzetmarkten een week vooraf kwam uit boeken met ±14 cent halve afstand (punt 16), dus uit laatste handelsprijzen. Voortaan test ik alleen met echte trades of met opgeslagen boeken, nooit met de getoonde koers in dunne markten.
4. **De ruimte is klein.** Een paar honderd dollar per markt op de beste prijs (punt 16), trades van gemiddeld $13 (punt 17). Zelfs als het voordeel echt is, kun je er per markt weinig geld in kwijt zonder de prijs te bederven. Dat maakt de route nog minder geschikt voor €10.000 in 3 maanden (GOK).

### 18. Les voor elke terugtest op dunne markten (GOK, volgt uit punt 16 en 17)
1. Vraag eerst: **welke prijs geeft de API?** Midden, laatste handel, of wat je kon krijgen? Bij Polymarket wisselt dat met de breedte van het boek.
2. Kijk naar de **bied-laat-afstand van de markten die je test**, niet van de markt in het algemeen. Het voordeel zat juist in de markten met de breedste boeken.
3. Gebruik **echte trades** als controle: wat verdienden mensen die echt kochten, op het moment dat jouw bot zou kopen.
4. Haal trades **tijdens de wedstrijd** eruit voor een bot die vooraf beslist.

### Bijgestelde rangorde binnen hoek A (kans maal opbrengst, GOK)
1. **Voorspellingsmarkten, favorieten van 70 tot 90 cent, alleen als maker (eigen bod in het boek), alleen vóór de wedstrijd, eerst weken op papier met opgeslagen boeken.** Richting gesteund door Kalshi (DERDEN), run 3 en 4 (GEZIEN) en echte trades (GEZIEN, punt 17), maar de banden lopen door nul en er past weinig geld in. Als nemer kopen valt af: de afstand eet het voordeel op (punt 16). Kans op €10.000 in 3 maanden: onder 3% (GOK, omlaag van 5%, omdat er per markt minder in past dan ik dacht).
2. Simpele trendregel op spot (run 1): beperkt dalingen, geen geldmachine, maar er past wel veel geld in.
3. Bijzetmarkten een week vooraf als nemer: **valt af** (punt 16).
4. Hoofdmarkten als losse route, longshots, LLM-sentiment als hoofdsignaal, hefboom: vallen af (run 1 en 4).

### Nog te doen (volgende runs)
- Punt 17 herhalen met alleen trades vóór de aftrap (aftraptijd uit `gameStartTime` of het event, als dat veld er is) en met meer events (de volledige pagina's, niet de eerste per week).
- Nalezen in de docs van de Data API v2 of `side` echt de nemer is.
- Hoe vaak wordt een maker-bod 1 à 2 cent onder het midden gevuld vóór de wedstrijd? Te meten uit trades: hoeveel volume ging er tegen een prijs onder het midden van dat moment.

## Stand na run 05:10 UTC (19 nov 2026)
1. **Echte kopers van favorieten (70 tot 90 cent) op Polymarket verdienden in sep tot nov 2026 gemiddeld** (GEZIEN, 356 markten, echte trades): sport hoofdmarkten +6,2% per trade en +17,9% per dollar (band +10,9% tot +23,9%), bijzetmarkten +9,4% per trade. Zelfde richting als Kalshi (DERDEN) en mijn runs 3 en 4. Maar de meeste banden lopen door nul en het grote geld zit vlak voor of tijdens de wedstrijd.
2. **De getoonde koers is in dunne markten niet te krijgen** (GEZIEN): bij bijzetmarkten een week vooraf is de halve bied-laat-afstand ±14 cent, en Polymarket toont daar de laatste handelsprijs. Mijn "+16%" uit run 4 vervalt; als nemer kopen eet het voordeel op.
3. **Er past weinig geld in** (GEZIEN): een paar honderd dollar op de beste prijs per markt, mediane trade $13. Ook met een echt voordeel is dit geen route naar €10.000 in 3 maanden met een kleine pot (GOK, kans onder 3%).
4. **Terugtests liegen makkelijk, drie keer gezien in dit bestand**: Sharpe 1,86 naar 0,33 (run 1), longshot-"winst" door volumekeuze (run 2), "+16%" door de getoonde koers (run 5). Altijd: vooraf vastleggen, nieuwe data, echte prijzen of echte trades. Een taalmodel hooguit als filter; meelezen op X kost $5 per 1000 posts (GEZIEN).
5. **Volgende stap kost niets**: boeken opslaan en alleen als maker vóór de wedstrijd op papier handelen; slaagt dat niet na 300 markten met band boven +2%, dan valt de route af (testplan punt 15). Voor groter geld blijft de trendregel op spot (run 1) de enige route in hoek A waar veel geld in past, maar zonder groot rendement.

## Run 6 (19 nov 2026, ±05:35 tot 06:05 UTC)
Hoek: de drie open punten van run 5. (a) Wat betekent het veld `side` echt, (b) wat verdienden kopers van favorieten **alleen vóór de aftrap** (het enige moment waarop een trage bot meedoet), apart voor nemer en maker, (c) hoe vaak wordt een maker vóór de aftrap gevuld. Plus iets wat ik in run 1 tot 5 vergat: **de kosten per trade op Polymarket**. Geen namen of wallets van handelaren opgeschreven.

### 19. Kosten op Polymarket: nemers betalen, en er verandert morgen iets (GEZIEN)
- Formule: kosten = aantal stukken × tarief × p × (1 − p). Makers betalen nooit. Tarief sport: 0,05 (GEZIEN, [docs Fees](https://docs.polymarket.com/trading/fees.md)). Bij een favoriet van 80 cent is dat 0,8 cent per stuk, dus **1,0% van de inzet**; bij 70 cent 1,5%. Gemiddeld over alle nemer-trades in mijn steekproef: 1,03% (GEZIEN, eigen som).
- **Vanaf 20 nov 2026 23:59 UTC** (GEZIEN, [docs wijzigingen nov 2026](https://docs.polymarket.com/programs/fee-and-rebate-changes-november-2026.md)): sport blijft 0,05; crypto (behalve de 5- en 15-minuten BTC-markten), economie, cultuur, weer en politiek zonder verkiezingen gaan naar 0,01; geopolitiek blijft gratis. Belangrijk voor een kleine bot: **onder $200.000 handelsvolume per 30 dagen krijg je geen terugbetaling meer**, niet als nemer en niet als maker. De losse beloning voor liquiditeit (liquidity rewards) blijft wel bestaan.
- Run 3 tot 5 rekenden zonder deze kosten. Voor nemers zakken die cijfers dus ±1 procentpunt (GOK, eigen som).

### 20. Het veld `side` is de nemer (GEZIEN)
De docs van `data-api.polymarket.com/v2/trades` zeggen: `taker_only` staat standaard aan, "each fill is served once, on its taker side" (GEZIEN, [docs List trades](https://docs.polymarket.com/api-reference/feeds/list-trades.md)). Mijn aanname uit run 5 klopt dus. Daarmee kun je per trade zien wie de maker was: verkoopt de nemer de favoriet, dan kocht een maker hem.

### 21. Alleen vóór de aftrap: het voordeel bij favorieten verdwijnt (GEZIEN, vooraf vastgelegd)
**Vooraf vastgelegd:** periode 1 sep tot 10 nov 2026, sportmarkten met een uitslag, indeling hoofd (`moneyline`, `totals`) en bijzet (andere `sportsMarketType`), aftrap uit het veld `gameStartTime` dat Polymarket meegeeft (GEZIEN). Maat 1: rendement per echte trade, gesplitst in nemer en maker en in tijdvakken. Maat 2 (de eerlijke maat voor een bot die per markt één keer koopt): koop de favoriet van 70 tot 90 cent tegen de laatste handelsprijs vóór de aftrap, min de nemer-kosten.
**Hoe:** per dag de eerste 400 gesloten markten uit de keyset-API (28.400 opgehaald; dus niet compleet per dag), daaruit per dag maximaal 7 hoofd en 7 bijzet, één per event, vaste seed: 823 markten, 619 met trades, alle trades volledig opgehaald (GEZIEN). Bootstrap per event of per markt, 90%-band.

**Maat 1, per trade (GEZIEN):**

| Groep | trades | events | per trade | per dollar |
|---|---|---|---|---|
| Hoofd, nemer, vóór de aftrap | 3.720 | 167 | **-36,5%** (-61,5% tot -3,7%) | -70,0% (-92,0% tot -11,8%) |
| Hoofd, nemer, tijdens of na | 11.995 | 295 | -4,8% (-14,1% tot +3,6%) | -9,6% (-34,7% tot +13,4%) |
| Hoofd, maker, vóór de aftrap | 131 | 30 | -30,5% (-64,1% tot +22,9%) | -56,0% (-95,7% tot +37,1%) |
| Hoofd, maker, tijdens of na | 1.464 | 167 | -0,4% (-8,6% tot +6,8%) | +8,6% (-4,1% tot +17,4%) |
| Bijzet, nemer, vóór de aftrap | 535 | 40 | -24,0% (-65,4% tot +18,2%) | +10,2% (-76,5% tot +30,6%) |
| Bijzet, nemer, tijdens of na | 700 | 66 | +4,4% (-6,4% tot +15,6%) | +17,6% (+5,3% tot +26,1%) |

De -36% per trade is **geen eerlijk beeld**: een paar events met heel veel trades die verloren trekken het omlaag (de banden zijn enorm). Daarom maat 2.

**Maat 2, één koop per markt, laatste prijs vóór de aftrap, na kosten (GEZIEN):**

| Groep | markten | winst per markt | 90%-band | raakkans |
|---|---|---|---|---|
| Hoofd | 140 | **-3,6%** | -11,5% tot +3,9% | 76% |
| Bijzet | 42 | +1,9% | -10,9% tot +13,3% | 83% |
| Alle | 182 | **-2,4%** | -8,8% tot +4,0% | 78% |
| Alle, 1 tot 24 uur vooraf | 151 | -4,3% | -11,7% tot +3,3% | 76% |
| Alle, meer dan 24 uur vooraf | 88 | -6,7% | -16,6% tot +2,9% | 74% |

Controle op de prijzen zelf (laatste prijs vóór de aftrap, per markt, beide kanten): band 70 tot 80 cent won 75% van de keren, band 80 tot 90 cent won 83% (GEZIEN, n = 112 en 64). Dat is precies wat de prijs zei. **Vóór de aftrap is de markt in deze steekproef gewoon eerlijk geprijsd**, en dan maken de kosten het netto negatief.

**Hoe vaak wordt een maker vóór de aftrap gevuld?** Bijna nooit in deze steekproef: 146 trades in 36 events waar een maker vóór de aftrap een favoriet van 70 tot 90 cent kocht, tegen 4.255 trades aan de nemerkant (GEZIEN). Van alle trades in hoofdmarkten gebeurt ±78% tijdens of na de wedstrijd (GEZIEN, 13.459 van 17.310 rijen). De laatste trade ligt mediaan 2,5 uur na de aftrap (GEZIEN).

**Wat dit leert** (GOK, op basis van punt 17 en 21):
1. Het voordeel bij favorieten uit run 3 tot 5 **zit tijdens de wedstrijd**, niet ervoor. Wie tijdens de wedstrijd koopt, weet vaak sneller wat er op het veld gebeurt (live beeld, snelle data). Dat is een snelheidsvoordeel, geen patroon dat een simpele bot vooraf kan oogsten.
2. Mijn hoofdroute in hoek A (favorieten als maker vóór de aftrap) **valt af** op deze data: de prijs is vooraf eerlijk, nemers betalen ±1% kosten, en makers worden vooraf bijna niet gevuld.
3. Dit verschilt van punt 17 (run 5) omdat dat alle trades samen nam, ook tijdens de wedstrijd. Zelfde les als eerder: **knip je data op het moment waarop jouw bot echt beslist**, anders test je het voordeel van iemand anders.

### Bijgestelde rangorde binnen hoek A (kans maal opbrengst, GOK)
1. **Simpele trendregel op spot (run 1)**: beperkt dalingen, geen geldmachine, maar het enige in hoek A dat de toetsen overleeft en waar veel geld in past. Kans op €10.000 in 3 maanden met een kleine pot: onder 1% (GOK).
2. **Voorspellingsmarkten tijdens de wedstrijd**: daar zit wel een voordeel (punt 17 en 21), maar het vraagt snelle live data en een bot die binnen seconden reageert; dat is een race tegen professionele partijen (GOK). Alleen te onderzoeken als iemand een eigen snelle databron heeft.
3. Favorieten vóór de aftrap, als nemer of maker: **valt af** (punt 21).
4. Bijzetmarkten als nemer, hoofdmarkten als losse route, longshots, LLM-sentiment als hoofdsignaal, hefboom: vallen af (run 1, 4 en 5).

### Nog te doen (volgende runs)
- Dezelfde toets (maat 2, alleen vóór het beslismoment) op de **niet-sport** markten met lage kosten na 20 nov (economie, weer, cultuur: tarief 0,01). Weinig kosten maakt een klein voordeel daar misschien wel netto positief.
- Liquiditeitsbeloningen (liquidity rewards) nalezen: wat krijgt een kleine maker per dag voor een bod in het boek, en weegt dat op tegen het risico dat alleen de verkeerde kant gevuld wordt.

## Stand na run 06:05 UTC (19 nov 2026)
1. **Vóór de aftrap is Polymarket-sport eerlijk geprijsd** (GEZIEN, 182 markten, sep tot nov 2026): favorieten van 70 tot 90 cent wonnen 75% en 83%, wat de prijs zei. Eén koop per markt vóór de aftrap gaf na kosten -2,4% (band -8,8% tot +4,0%). Het voordeel dat run 3 tot 5 zag, zit tijdens de wedstrijd en is een snelheidsvoordeel.
2. **Kosten**: nemers betalen bij sport ±1% van de inzet bij een favoriet van 80 cent; makers niets (GEZIEN). Vanaf 20 nov 23:59 UTC krijgen accounts onder $200.000 volume per 30 dagen geen terugbetaling meer; veel niet-sport markten gaan naar een laag tarief (0,01) (GEZIEN).
3. **Makers worden vóór de aftrap bijna niet gevuld** (GEZIEN: 146 maker-trades tegen 4.255 nemer-trades; ±78% van de handel is tijdens de wedstrijd). De maker-route uit run 5 valt af.
4. **Terugtests liegen makkelijk, nu vier keer gezien in dit bestand**: Sharpe 1,86 naar 0,33 (run 1), longshot-"winst" door volumekeuze (run 2), "+16%" door de getoonde koers (run 5), en "favorieten winnen" doordat trades tijdens de wedstrijd meetelden (run 6). Altijd: vooraf vastleggen, knippen op het beslismoment van de bot, echte prijzen en kosten.
5. **Wat overblijft in hoek A**: de simpele trendregel op spot (run 1) als rustige basis, geen route naar €10.000 in 3 maanden (GOK, kans onder 1%). Volgende toets: voorspellingsmarkten met tarief 0,01 buiten sport, met dezelfde strenge opzet.
