# Keuring handelsonderzoek ai-handel, 19 nov 2026, keurder (losse Claude, niet een van de zoekers)
Wat ik keurde: commit d872a705, bestanden `BRIEF.md`, `A-strategie-en-testen.md` (t/m run 7), `B-zelf-bouwen.md` (t/m run 8), `C-maandinleg.md` (t/m run 6), `D-arbitrage.md` (t/m run 7); `A-kant-en-klaar.md` als naslag.
Akkoord: **nee**, maar dicht bij ja. De cijfers zelf kloppen: alle 17 claims die ik zelf nakeek klopten, en mijn eigen herberekening van de trendtest gaf dezelfde uitkomst. Het nee komt door drie punten in hoe de nummer-1-route (Polymarket) wordt gebracht: de voorwaarden van Polymarket noemen Nederland met name, de kans op het doel verschilt tussen B en D een factor 2 tot 3, en de belastingplicht staat er als "nakijken" terwijl de Belastingdienst het zwart op wit zegt. Na die drie (zie "Moet") is het akkoord.

Dit is geen beleggingsadvies. Ik keur alleen of de informatie klopt en eerlijk gebracht is.

## Wat ik zelf nakeek (17 claims, alles met curl op 19 nov ±08:20 UTC, tenzij anders vermeld)

| # | Claim in het onderzoek | Waar | Mijn controle | Uitslag |
|---|---|---|---|---|
| 1 | Bitvavo, Kraken, Coinbase, Bybit EU, OKX Europe hebben een MiCA-vergunning; Binance, Bitget, Pionex, MEXC niet | A-kant-en-klaar 2 | [ESMA CASPS.csv](https://www.esma.europa.eu/sites/default/files/2024-12/CASPS.csv) zelf gedownload: 409 regels, Bitvavo (NL, 26 jun 2025), Kraken/Payward (IE, 25 jun 2025), Coinbase (LU), Bybit EU (AT), OKX Europe (MT) staan erin; Binance, Bitget, Pionex, MEXC 0 treffers | klopt. Kleine noot: laatste wijziging in het bestand is nu 18 nov 2026, niet 30 sep |
| 2 | Bitvavo 0,15% maker, 0,25% taker bij weinig volume | B 3, C 26 | [bitvavo.com/en/fees](https://www.bitvavo.com/en/fees): €0+ 0,15% / 0,25%, €100.000+ 0,10% / 0,20% | klopt |
| 3 | Kraken Pro spot sinds juli 2026 instap 0,40% maker, 0,80% taker | B 8, C 9 | [Kraken support, fee tier changes (juli 2026)](https://support.kraken.com/articles/cross-platform-fee-tier-changes): Tier 1 $0+ 0,40 / 0,80; $2,5K+ 0,30 / 0,60; $10K+ of $20k bezit 0,22 / 0,38 | klopt |
| 4 | Polymarket takerkosten = aandelen × tarief × p × (1 − p), makers betalen niets | A 19, D 8 | [docs fees](https://docs.polymarket.com/trading/fees.md) en [wijzigingen nov 2026](https://docs.polymarket.com/programs/fee-and-rebate-changes-november-2026.md) | klopt |
| 5 | Vanaf 20 nov 23:59 UTC: sport 0,05, weer/economie/cultuur 0,01, geopolitiek 0; onder $200.000 volume geen korting meer; liquiditeitsbeloning blijft | A 19, D 8 | zelfde pagina: tabel en "Accounts with less than $200,000 in 30-day taker weighted volume will earn no taker rebate", "Liquidity rewards remain unchanged" | klopt |
| 6 | Nederland staat bij Polymarket op "Close-only on frontend; the API itself is not restricted" | B 22 | [docs geoblock](https://docs.polymarket.com/api-reference/geoblock.md): letterlijk zo, samen met Ierland, Japan, Malta (sport), Zuid-Korea | klopt als technisch feit, maar zie claim 7 |
| 7 | (niet in het onderzoek) Wat de voorwaarden van Polymarket zeggen over Nederlanders | B 22, D 3 | [polymarket.com/tos](https://polymarket.com/tos): "THE NETHERLANDS" staat in de lijst; wie daar woont is een "Restricted Person" en mag niet handelen via "THE SITE, PLATFORM OR ANY OF THE TECHNOLOGY FEATURES", en "USE OF A VIRTUAL PRIVATE NETWORK ... TO CIRCUMVENT ... IS STRICTLY PROHIBITED"; straf: wallet in "close-only" | **ontbreekt in het onderzoek**, zie Moet 1 |
| 8 | Ksa verbood Polymarket, dwangsom €420.000 per week, geen vergunning | D 3, B 11 | [NOS](https://nos.nl/l/2602855): "De Amerikaanse website Polymarket is verboden in Nederland ... dwangsom van 420.000 euro per week" | klopt |
| 9 | Kalshi geeft buitenlanders geen liquiditeitsbeloning | D 16 | [Kalshi Help](https://help.kalshi.com/incentive-programs/liquidity-incentive-program): "International, non-U.S. users (ineligible for rewards)" | klopt |
| 10 | Grok `x_search` kost $5 per 1.000 posts, elke post telt, ook geciteerde | A 6, B 15 | [docs.x.ai pricing](https://docs.x.ai/developers/pricing.md): "$5 / 1k posts, $10 / 1k profiles", "billed per item fetched" | klopt |
| 11 | Hyperliquid perps instap 0,045% taker / 0,015% maker, spot 0,070 / 0,040 | B 16 | [Hyperliquid fees](https://hyperliquid.gitbook.io/hyperliquid-docs/trading/fees.md): zelfde getallen in de tabel | klopt |
| 12 | Freqtrade: Bitvavo heeft geen stop-loss op de beurs | B 2, A 5 | [Freqtrade exchanges](https://www.freqtrade.io/en/stable/exchanges/): "Bitvavo spot ❌ (not available)" | klopt |
| 13 | Kansspelbelasting 2026 is 37,8% | D 22 | [Rendement](https://www.rendement.nl/contact-belastingdienst/nieuws/kansspelbelasting-verschuldigd-bij-wk-voetbalpool.html): "37,8% kansspelbelasting" (DERDEN) | klopt |
| 14 | Speler moet zelf aangifte doen bij een buitenlandse aanbieder | D 22 ("nakijken") | [Belastingdienst, formulierpagina](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/themaoverstijgend/programmas_en_formulieren/aangifte_kanspelbelasting_over_prijzen_uit_buitenlandse_kanspelen): "Hebt u een prijs gewonnen bij een online kansspel waarvoor in Nederland geen vergunning is verleend ... Dan moet u aangifte kansspelbelasting doen." | klopt, en is nu bevestigd door de bron zelf, zie Moet 3 |
| 15 | Box 3 2026: forfait overige bezittingen 6%, heffingsvrij €59.357, tegenbewijs mogelijk | C 10 | [SRA](https://www.sra.nl/nieuws/259001/2026/01/box-3-percentages-vrijstellingen-en-bedragen-2026): "Overige bezittingen 6,00% (definitief)", "€ 59.357", tegenbewijsregeling | klopt |
| 16 | Terugtest-Sharpe voorspelt bijna niets, R² < 0,025 over 888 strategieën | A 3 | [Quantpedia](https://quantpedia.com/quantopians-academic-paper-about-in-vs-out-of-sample-performance-of-trading-alg/): "888 algorithmic trading strategies ... (R² < 0.025)" | klopt |
| 17 | De papers arXiv 2606.00071, 2610.13593 en 2508.03474 bestaan en gaan over wat er staat | A 3, A 9, D 3 | titels via export.arxiv.org: "Bitcoin Price Prediction: Peer-Reviewed Evidence...", "Time-Varying Favorite-Longshot Bias in Polymarket Weather Markets", "Unravelling the Probabilistic Forest: Arbitrage in Prediction Markets" | klopt (alleen titels, niet de inhoud) |

## Rekenvoorbeelden zelf nagerekend

1. **Trendtest van A (punt 2), opnieuw gedraaid op dezelfde openbare data** (`api.bitvavo.com/v2/BTC-EUR/candles?interval=1d&limit=1440`, 11 dec 2022 tot 19 nov 2026, splitsing op 60% = 23 apr 2025, 0,25% per wissel; eigen script, GEZIEN):
   BTC kopen en vasthouden out-of-sample **x0,70** (A: x0,70); SMA 40 in-sample **x2,75**, out-of-sample **x0,98**, grootste daling **33%** (A: x2,75, x0,98, 33%); kopen en vasthouden in-sample vanaf dag 200 **x2,99** (A: x2,99). ETH SMA 60 out-of-sample **x1,47** (A: x1,47). Alles gelijk.
2. **Polymarket-kosten:** 0,05 × 0,8 × 0,2 = 0,008 per aandeel = 1,0% van 80 cent; bij 70 cent 1,5%; 100 aandelen op 50 cent: $1,25 (tarief 0,05) en $0,25 (0,01). Klopt met A 19 en D 8.
3. **"Bijna zeker" (A 23):** 1,008^13 = 1,109, dus ±10% in 3 maanden; één misser op 99,2 cent kost 99,2 / 0,8 = 124 keer de winst ("±120"). Klopt.
4. **Funding (D 2):** €7.000 × 8% / 4 = €140. Klopt. Maar "€500.000 nodig" is de **positie**; met de eigen verhouding van D (70% van de inleg als positie) is het ±€714.000 inleg. Kleine onderschatting, zie Kan.
5. **Belasting (D 22):** €10.000 / (1 − 0,378) = €16.077 bruto. Klopt, als de belasting over de nettowinst gaat; dat laatste is niet nagekeken.
6. **Kosten per rondje:** Kraken 2 × 0,80 = 1,6%, Bitvavo 2 × 0,25 = 0,5%, Hyperliquid 2 × 0,045 = 0,09%. X Search: 100 posts per uur × 24 × 30 × $0,005 = $360 per maand. Kalshi bij 50 cent: 0,07 × 0,25 = 1,75 cent = 3,5%. Tweedehands: €10.000 / €60 tot €100 = 100 tot 167 stuks = 8 tot 13 per week. Alles klopt.

## Deel A: doet het wat beloofd is? (toets tegen BRIEF.md)

| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| A1 | Alle vier vragen zijn beantwoord met eigen metingen op openbare data, routes met inleg, uren, kans, ergste geval en rangorde, zoals de BRIEF vraagt | feit | hoog | n.v.t. |
| A2 | De metingen zijn eerlijk opgezet: vooraf vastgelegd, knippen op het beslismoment, echte nemer-prijzen, bootstrap per event. A laat zelf vier keer zien hoe een terugtest loog en corrigeert zichzelf | feit | hoog | n.v.t. |
| A3 | **Polymarket-voorwaarden ontbreken.** B 22 schrijft "de site blokkeert, de API niet" en "een VPS in Londen geeft de kortste weg". De voorwaarden zeggen dat inwoners van Nederland via geen enkele weg mogen handelen, ook niet via de API, en dat ontwijken met VPN of iets vergelijkbaars verboden is (claim 7). Een server in Londen helpt niet: de voorwaarden kijken naar waar je woont. Wie dit leest als "via de API mag het", loopt het risico dat de wallet midden in een positie op alleen-sluiten gaat | feit | hoog | tekst van [polymarket.com/tos](https://polymarket.com/tos) |
| A4 | D en B 37 zeggen "meedoen kan alleen met een VPN"; volgens B 22 en de docs werkt de API technisch zonder VPN. De twee bestanden spreken elkaar tegen; beide zijn volgens de voorwaarden verboden | feit | hoog | claim 6 en 7 |
| A5 | **Kans op €10.000 voor dezelfde route verschilt:** D zet "Polymarket-beloning" op 25 tot 30%, B op 8 tot 15%. B heeft het nieuwere en strengere cijfer (verlies dicht bij het midden −1,05% per gevulde dollar, B 42; "elk verslag van een echte beloningsbot eindigde op verlies", B stand run 6). Er is geen enkel controleerbaar geval van een kleine bot die dit netto haalde. D's getal is te hoog voor de bewijzen | feit (het verschil), vermoeden (welke juist is) | hoog / midden | twee weken schaduwbot op nieuwe markten met vastgezette woordenlijst (B 44) |
| A6 | Belasting staat bij D als "nakijken", maar de Belastingdienst zegt het zelf: prijs bij een online kansspel zonder Nederlandse vergunning = zelf aangifte kansspelbelasting (claim 14), tarief 37,8% in 2026 (claim 13). Open blijft alleen of de beloning voor liquiditeit een "prijs" is en over welk bedrag het gaat | feit | hoog | formulier en toelichting van de Belastingdienst |
| A7 | Succesverhalen (0x8dxd $300 naar $400.000, gopfan2 $1,48 miljoen, "14 van 20 top-wallets zijn bots") komen uit blogs en tweets. D noemt ze zwak en zegt "verliezers schrijven geen blogs"; dat is netjes. Ze mogen alleen niet de hoge kans van route 1 dragen | feit | midden | n.v.t. |
| A8 | C (maandinleg) en A (trend) zijn sterk en nuchter: DCA wint van slimme regels, kosten en aanbieder zijn de knop, een eigen bot voegt ±0,1% toe | feit (metingen), vermoeden (toekomst) | hoog | n.v.t. |
| A9 | De TikTok-scams staan in de BRIEF genoemd maar nergens uitgewerkt; hieronder in de lijst "wat te mijden" gezet | feit | hoog | n.v.t. |

## Deel B: houdt het zich aan onze regels?

| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| B1 | Geen persoonsgegevens of financiële gegevens van Thijs gevonden: geen bedragen, rekeningen, wallets, IBAN, mail of telefoon (grep op 0x-adressen, IBAN, mail, 06-nummers, "zijn rekening/wallet/inleg"). Rekenvoorbeelden gebruiken algemene bedragen (100, 300, €2.000 tot €5.000) | feit | hoog | harde regel 2 |
| B2 | De BRIEF noemt dat Thijs "een paar honderd euro per maand" wil inleggen. Dat is vaag, geen bedrag of rekening, en volgens mij aanvaardbaar; strikt gezien is het wel een financiële wens van Thijs in een openbare repo. Liever "een vast maandbedrag" | feit | midden | harde regel 2 |
| B3 | Namen van derden (0x8dxd, gopfan2, neobrother, sunshines) zijn openbare leaderboard-namen uit nieuwsbronnen, niet van Thijs | feit | hoog | harde regel 2 |
| B4 | Elk cijfer heeft GEZIEN, DERDEN of GOK; kansen staan als GOK met reden | feit | hoog | harde regel 5 |
| B5 | Geen accounts gemaakt, niets ingelogd, niets gekocht; poly-maker alleen gelezen met `git clone --filter=blob:none` (B 25). Een clone is meer dan "alleen lezen", maar er is niets uitgevoerd | feit | midden | BRIEF werkwijze 4 |
| B6 | Bestanden zijn 450 tot 610 regels, boven de ±400 uit de bouwregels. Voor onderzoek is dat minder erg, maar Thijs vindt de kern lastig terug; zie de samenvattingen hieronder | feit | hoog | bouwregels (±400) |
| B7 | Geen gedachtestreepjes gevonden | feit | hoog | harde regel 8 |

## Scams, verkooppraat en adviezen die Thijs in de problemen kunnen brengen

**Goed gevonden door de zoekers (klopt met wat ik zag):**
- Er bestaat geen officiële Grok-handelsbot van xAI; "Grok" in de naam van een handelssite is vooral een teken van oplichting (A-kant-en-klaar 4 en 5).
- Nep-bots op GitHub met gekochte sterren die sleutels en wallets stelen, vooral rond Polymarket (gekaapte organisatie `dev-protocol`, npm-pakket `polymarket-claude-code`) (B 5 en 23, DERDEN).
- API-opnames bij Bitvavo gaan zonder 2FA of mail, dus nooit opnamerecht aan een bot geven (B 3, GEZIEN door B).
- Chatbots die echt geld beheerden verloren meestal (Alpha Arena, A-kant-en-klaar 4, DERDEN).

**Wat Thijs in de problemen kan brengen (mijn oordeel, met bron):**
1. **Polymarket vanuit Nederland, via API of VPN.** Verboden door de Ksa (claim 8), verboden door de eigen voorwaarden voor inwoners van Nederland (claim 7), en een gokovereenkomst met een aanbieder zonder vergunning is in Nederland nietig (D 11, DERDEN). Gevolg: wallet kan op alleen-sluiten, saldo niet af te dwingen. Strafbaar voor de speler zelf vond niemand (GOK, niet weerlegd).
2. **Belasting.** Winst bij een online kansspel zonder Nederlandse vergunning: zelf aangifte kansspelbelasting doen, 37,8% (claim 13 en 14). Niet aangeven is belasting ontduiken en valt volgens de BRIEF af. Of een beloning voor liquiditeit een "prijs" is, is onbekend: vraag een belastingadviseur voor er geld in gaat.
3. **Wallet koppelen.** Voor Polymarket en Hyperliquid heb je een eigen crypto-wallet nodig. Nooit de privésleutel of herstelwoorden in een bot, `.env`, chat of "AI-assistent" zetten; alleen een Session Key (Polymarket) of API-wallet (Hyperliquid) die niet kan opnemen (B 16 en 23, GEZIEN door B). Nooit iets laten "tekenen" op aanwijzing van iemand die je benaderde.
4. **Hefboom via een partij zonder EU-vergunning** (Hyperliquid en dergelijke). Geen toezicht, geen bescherming tegen negatief saldo of hack; een fout in de bot kan de inzet in minuten kosten (B 10 en 16). In de EU is crypto-hefboom voor particulieren naar verwachting 2x (DERDEN).
5. **Beurzen zonder MiCA-vergunning** (Binance, Bitget, Pionex, MEXC): geen vergunning in het ESMA-register (claim 1).
6. **Tweedehands opkopen:** IMEI en iCloud nakijken (helen is strafbaar), scrapen breekt de voorwaarden van Marktplaats, en stelselmatig met winst doorverkopen is inkomen, mogelijk met KvK-plicht (D 12, GOK van D, niet nagekeken).

## Wat te mijden (lijst voor Thijs)

| Wat | Waarom | Bron |
|---|---|---|
| TikTok **@ptrading2, "GrokBot V3"** | Profiel bestaat (GEZIEN: ±1.131 volgers, bio "Putting ppl on new meta ... Please don't share script"). Patroon: nep-winstkaartjes, "DM me", een "script" of bot via een privébericht. Een script van een onbekende is precies hoe de wallet-stelers werken | verslag hoofdchat 19 nov; profiel GEZIEN met curl |
| TikTok **@s0fyx_fx, "Grok Bot x Phantom"** | Profiel bestaat (GEZIEN: ±848 volgers, bio "Profitable with my grokbot ... 19yo"). Laat je je Phantom-wallet koppelen en een transactie "tekenen": daarmee geef je toestemming om je wallet leeg te halen (wallet drainer). Nooit doen | verslag hoofdchat 19 nov; profiel GEZIEN met curl |
| Elke site of app met "Grok" in de naam die handelt of rendement belooft | Geen officiële Grok-handelsbot; meerdere waarschuwingen (IOSCO, scanners) | A-kant-en-klaar 4 en 5 |
| "Download mijn gratis bot", forks, "verbeterde versies", npm-pakketten met "polymarket" van onbekenden | Malware die `.env`, sleutels en wallets steelt; sterren worden gekocht | B 5 en 23 |
| Vast rendement per dag of week, winstkaartjes, WhatsApp- of Telegramgroepen met "coaches" | Klassiek patroon van nep-platforms: saldo groeit op het scherm, opnemen lukt niet | A-kant-en-klaar 5, AFM via accountant.nl (DERDEN) |
| Geld naar een "bot" of "fonds" sturen in plaats van alleen een API-sleutel geven | Dan is het geen software maar een fonds zonder vergunning of oplichting | A-kant-en-klaar 6 |
| API-sleutel met opnamerecht, privésleutel in een bot | Gestolen sleutel = lege rekening | B 3, 5, 23 |
| Aan een meetstation of uitslag "helpen" (Parijs-weermarkt), wash trading, spoofing | Fraude en marktmanipulatie | D 19, D "valt af" |

## Samenvatting per vraag (kort en eerlijk)

### 1. Zelf een bot bouwen (B, met A)
- **Opties:** Freqtrade (gratis, spot en futures, terugtesten, papier handelen, ingebouwde remmen) met de AI als programmeur; NautilusTrader voor voorspellingsmarkten (zwaarder); een LLM als handelaar.
- **Voor:** goedkoop gereedschap, alles eerst gratis op papier; de AI schrijft de code snel.
- **Nadeel:** geen enkele spot-strategie liet een betrouwbaar voordeel zien. De beste trendinstelling zakte van Sharpe 1,86 naar 0,33 op nieuwe data (GEZIEN door A, door mij nagerekend). Kosten per rondje: Bitvavo 0,5%, Kraken 1,6% (nagekeken). Sentiment uit X voorspelt geen rendement (DERDEN) en kost $40 tot $600 per maand.
- **Risico:** malware-repo's en gestolen sleutels (het grootste echte gevaar); bij Bitvavo zit de stop-loss in de bot, dus die moet dag en nacht draaien.
- **Wat het bewijs zegt:** een trendregel beperkt vooral de diepste dalingen (33% tegen 52% bij BTC), het is geen geldmachine. Een LLM hooguit als filter.

### 2. Vaste maandinleg (C)
- **Opties:** ingebouwd spaarplan (Bitvavo, Trade Republic, DEGIRO en anderen), gewone DCA, DCA met regels, grid, herbalanceren.
- **Voor:** gewone DCA wint in de metingen van bijna alle slimme regels; geen bouwtijd; procentuele kosten wegen licht.
- **Nadeel:** brengt binnen weken geen noemenswaardig geld op. Een eigen bot voegt ±0,1% toe tegenover een sleutel als risico.
- **Risico:** grote dalingen op papier (alleen BTC zonder uitzonderlijke groei: 39 tot 46% kans op verlies na 3 jaar, GOK van C); de beurs zelf (hack). Box 3 in 2026: 6% forfait op beleggingen (nagekeken).
- **Wat het bewijs zegt:** aanbieder kiezen is de grootste knop (0,2% tot 2% per aankoop); een brede ETF met eventueel een klein vast deel BTC gaf het beste evenwicht in het verleden, maar die BTC-groei is niet door te trekken.

### 3. Arbitrage (D)
- **Opties en uitkomst:** prijsverschil tussen beurzen (0,007% tegen 0,2 tot 0,8% kosten: dood), funding-arbitrage (3 tot 11% per jaar: veilig-ish, maar ±€500.000 tot €700.000 nodig voor het doel), sportbonussen (eenmalig €1.000 tot €4.000, GOK), tweedehands met een zoekbot (legaal, schaalt met uren), Polymarket-beloning voor liquiditeit.
- **Voor:** de Polymarket-pot is echt en groot (±$56.000 tot $75.000 per dag, GEZIEN door B en D) en hangt niet af van gelijk hebben; in rustige, telbare markten (weer) was het verlies op vullingen klein.
- **Nadeel en risico:** Polymarket is in Nederland verboden, de voorwaarden verbieden Nederlanders het via elke weg, saldo is niet af te dwingen, winst valt onder kansspelbelasting 37,8%, en geen enkel controleerbaar geval van een kleine bot die netto won. Tweedehands is een baan van 20 tot 30 uur per week.
- **Wat het bewijs zegt:** echte risicoloze arbitrage levert een percentage van je inleg op en is met weinig geld nooit €10.000. Wat met weinig geld schaalt, is snelheid in jonge markten of eigen uren.

### 4. Routes naar €10.000 winst in 3 maanden
- **Eerlijk antwoord:** geen enkele route heeft aantoonbaar een goede kans. De kansen hieronder zijn GOK.
- **Polymarket-beloningsbot:** hoogste opbrengst per euro, maar tegen de Nederlandse wet in voor de aanbieder, tegen de voorwaarden in voor Thijs, met belastingplicht. Kans volgens B 8 tot 15%, volgens D 25 tot 30%; mijn oordeel (GOK): eerder 5 tot 15%, omdat het nieuwste verlies-cijfer (−1,05% per gevulde dollar dicht bij het midden) en de concurrentie nog niet in D zitten, en één close-only-maatregel de route in één keer beëindigt. Ergste geval: inleg vast of weg, plus een belastingaanslag.
- **Tweedehands doorverkopen met een zoekbot:** legaal en bewezen haalbaar als werk; kans 15 tot 25% (GOK van D) bij 8 tot 13 verkopen per week. Ergste geval: gestolen of kapotte toestellen, voorraad.
- **Hefboom om het doel te halen:** de snelste manier om alles kwijt te raken; geen bewezen voordeel om te versnellen (A, B).
- **Spot-trend, maandinleg, funding:** onder 1% kans op het doel met een kleine pot.

## Moet (blokkeert akkoord) / Kan (mag later)

**Moet** (de schrijver van het bestand past het aan; daarna keur ik alleen deze punten opnieuw):
1. **B punt 22 en 37, D punt 3 en 13:** zet erbij dat de voorwaarden van Polymarket Nederland met name noemen, dat inwoners via geen enkele weg (site, platform of API) mogen handelen, dat VPN of iets vergelijkbaars verboden is, en dat de straf alleen-sluiten van de wallet is ([polymarket.com/tos](https://polymarket.com/tos)). Haal "een VPS in Londen geeft de kortste weg" weg of zet erbij dat het niets verandert aan wat mag. Maak "meedoen kan alleen met een VPN" kloppend: technisch werkt de API, volgens de voorwaarden mag het niet.
2. **D stand na run 08:00:** de kans voor route 1 (25 tot 30%) in lijn brengen met B (8 tot 15%) of uitleggen waarom D hoger zit, en het nieuwste verlies-cijfer van B (punt 42) meenemen.
3. **D punt 22:** "nakijken" vervangen door wat de Belastingdienst zelf zegt: bij een prijs van een online kansspel zonder Nederlandse vergunning moet je zelf aangifte kansspelbelasting doen ([formulierpagina](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/themaoverstijgend/programmas_en_formulieren/aangifte_kanspelbelasting_over_prijzen_uit_buitenlandse_kanspelen)), 37,8% in 2026. Open blijft alleen of de beloning een "prijs" is en over welk bedrag.

**Kan:**
- D punt 2: "€500.000 nodig" is de positie; met de eigen 70%-verhouding is de inleg ±€714.000.
- A-kant-en-klaar 2: de datum van het ESMA-bestand is nu 18 nov 2026; de Binance-hack van oktober 2026 rust op een kopje "Gerelateerd", dat is een zwakke bron.
- BRIEF: "een paar honderd euro per maand" vervangen door "een vast maandbedrag" (B2).
- Bovenaan elk bestand een korte samenvatting van een paar regels, of deze keuring als ingang gebruiken; de bestanden zijn 450 tot 610 regels.
- D punt 12: KvK-plicht en belasting bij stelselmatig doorverkopen nakijken (staat als GOK).
