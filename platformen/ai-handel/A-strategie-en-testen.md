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
