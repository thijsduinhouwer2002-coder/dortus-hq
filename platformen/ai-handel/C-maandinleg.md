# C. Vaste maandinleg: welke aanpak en welke bot (zoeker C)

Taakverdeling (BRIEF, 19 nov): C zoekt uit wat past bij een vaste inleg van een paar honderd euro per maand. Strategie in het algemeen staat bij A, gereedschap en veiligheid bij B, arbitrage bij D. Geen persoonlijk advies, geen "koop dit". Rekenvoorbeelden gebruiken een algemeen bedrag (100 of 300 euro per maand), niet het bedrag van Thijs.

## Run 1 (19 nov 2026, nacht)

### 1. De kern in één alinea
Voor een vaste maandinleg is gewoon elke maand hetzelfde bedrag kopen (DCA) in mijn eigen meting op bijna 7 jaar data moeilijk te verslaan. Slimme varianten (meer kopen na een daling, wachten op een dip, herbalanceren) wonnen soms, maar niet vaker dan ze verloren, en voor BTC nooit (punt 2). Procentuele kosten van 0,15 tot 0,25% doen bij een maandaankoop bijna niets; een **vaste** prijs per aankoop (1 euro, of 1 tot 2% bij een app) doet wel pijn (punt 3). Periodiek kopen zit al ingebouwd bij Bitvavo, Kraken, Coinbase, Trade Republic en andere, dus een eigen bot voegt voor gewone DCA bijna niets toe (punt 4). Een eigen bot heeft pas zin als je een regel wilt die de beurs niet heeft, en die regel moet zich eerst bewijzen op papier.

### 2. Eigen meting: DCA tegen slimme varianten (GEZIEN)
**Data:** dagkoersen BTC-EUR en ETH-EUR, Binance openbare archieven (`data.binance.vision/data/spot/monthly/klines/BTCEUR/1d/`), 3 jan 2020 tot 31 okt 2026, 2494 dagen, zonder account gehaald. Script stond in /tmp en is niet in de repo gezet (de opzet staat hieronder, zodat iemand het kan nadoen).

**Opzet:** elke 1e van de maand komt 100 euro binnen (bedrag maakt voor de verhouding niet uit). Kosten 0,25% per aankoop (Bitvavo taker, GEZIEN door B). Geld dat niet belegd is, telt aan het eind gewoon mee als contant (geen rente). Uitkomst = eindwaarde gedeeld door totaal ingelegd. Getest over alle 45 vensters van 36 maanden (elke startmaand), plus de hele periode van 80 maanden.

Varianten:
- **dca:** elke maand alles kopen.
- **mult:** meer kopen als de koers onder het gemiddelde van 200 dagen ligt, minder erboven (bedrag = inleg x (gemiddelde / koers)², max 3x, nooit meer dan je hebt gespaard).
- **dip:** sparen, en alles kopen zodra de koers 20% of meer onder de top van het laatste jaar staat.
- **half:** altijd de helft kopen, de andere helft bewaren voor als de koers 30% onder de top van het laatste jaar staat.

**Uitslag, vensters van 36 maanden (GEZIEN, eigen meting):**

| Munt | Variant | Mediaan | Slechtste | Beste | Wint van dca |
|---|---|---|---|---|---|
| BTC | dca | x1,72 | x0,95 | x3,13 | |
| BTC | mult | x1,58 | x0,94 | x2,87 | 6 van 45 |
| BTC | dip | x1,54 | x0,85 | x2,79 | 0 van 45 |
| BTC | half | x1,55 | x0,84 | x2,77 | 0 van 45 |
| ETH | dca | x1,25 | x0,62 | x2,57 | |
| ETH | mult | x1,24 | x0,66 | x2,36 | 30 van 45 |
| ETH | dip | x1,19 | x0,64 | x2,33 | 22 van 45 |
| ETH | half | x1,20 | x0,64 | x2,13 | 25 van 45 |

Hele periode (feb 2020 tot nov 2026, 80 maanden): BTC dca x2,82, mult x2,76, dip x2,32, half x2,55. ETH dca x2,49, mult x2,35, dip x2,33, half x2,18 (GEZIEN).

**Herbalanceren 50/50 BTC en ETH** (elke maand terug naar half om half, met verkopen als dat nodig is) tegen gewoon elke maand half om half kopen zonder bijsturen: herbalanceren won in 31 van 45 vensters, maar de mediaan was lager (x1,59 tegen x1,65). Over de hele periode x2,94 tegen x2,66 (GEZIEN). Let op: de kosten van het verkopen zitten er niet in, dus herbalanceren is iets te gunstig gemeten.

**Wat ik eruit haal:**
- Wachten op een dip kost bij BTC elke keer geld: het geld staat stil terwijl de koers verder stijgt. Dat klopt met een bekende test op 100 jaar aandelen: zelfs met perfecte kennis van elke bodem verloor "buy the dip" van DCA in meer dan 70% van de gevallen, en wie de bodem 2 maanden mist, verloor in 97% (DERDEN, [Of Dollars and Data](https://ofdollarsanddata.com/even-god-couldnt-beat-dollar-cost-averaging/)).
- Bij ETH, dat in deze periode lang daalde, wonnen de varianten in ongeveer de helft van de vensters. Dat is toeval van deze ene periode, geen regel (GOK).
- Een verhaal als "mijn dip-bot koopt 5 tot 10% goedkoper dan DCA" (DERDEN, [Cointelegraph, feb 2022](https://cointelegraph.com/news/trader-builds-bitcoin-buy-the-dip-bot-outperforms-dca)) meet de prijs per munt, niet wat je eindigt met. Het geld dat stilstaat en de keren dat de dip niet komt, tellen dan niet mee. Mijn meting telt dat wel (GOK dat dit het verschil verklaart).
- Ergste geval met gewone DCA in deze data: na 3 jaar x0,95 bij BTC en x0,62 bij ETH, dus 38% minder dan je erin stopte (GEZIEN). Bij een enkele munt kan het altijd naar bijna nul; spreiden of een brede ETF erbij verkleint dat (GOK).

### 3. Kosten: wat je echt betaalt bij een maandaankoop
**Procentuele kosten wegen licht.** Eigen som op dezelfde BTC-data, hele periode, gewone DCA (GEZIEN): 0% kosten x2,831; 0,15% x2,827; 0,25% x2,824; 1% x2,803; 1,49% x2,789; 2% x2,775. Een procent per aankoop kost over bijna 7 jaar zo'n 1% van de eindwaarde, omdat je elk bedrag maar één keer koopt en nooit heen en weer handelt.

**Vaste kosten per aankoop wegen zwaar bij kleine bedragen** (eigen som, GOK op de GEZIEN/DERDEN-tarieven): 1 euro op 100 euro is 1%; op 300 euro 0,33%. Wekelijks kopen met een vaste prijs maakt het vier keer duurder dan maandelijks.

**Tarieven voor periodiek kopen in Nederland** (DERDEN, [CryptoTicker vergelijking, bijgewerkt 10 nov 2026](https://cryptoticker.io/nl/vergelijking/bitcoin-spaarplan/); let op: die site verdient aan partnerlinks):

| Aanbieder | Kosten per aankoop | Op 300 euro per maand (eigen som, GOK) |
|---|---|---|
| OKX | 0,2% | 0,60 euro |
| Bitvavo (periodiek kopen, vanaf 5 euro) | 0,25% | 0,75 euro |
| Bybit EU | 0,25% | 0,75 euro |
| Crypto.com | 0,8% | 2,40 euro |
| Bitpanda (spaarplan vanaf 1 euro) | 0,99% | 2,97 euro |
| Kraken (directe en periodieke aankoop) | 1% | 3,00 euro |
| Coinbase | tot 1,875% plus spread | tot 5,63 euro plus spread |

Opnemen naar een eigen wallet volgens dezelfde bron: Coinbase 0,24 euro, Bitvavo 1,31, Kraken 1,49, Bitpanda 2,91 (DERDEN).

- **Trade Republic, crypto:** spaarplan vanaf 1 euro zonder uitvoeringskosten; losse order 1 euro vast (DERDEN, [Capitalo](https://www.capitalo.de/anbieter/traderepublic/produkte/krypto)). De spread (verschil tussen koop- en verkoopprijs) staat er niet bij en kan het echte kostenpunt zijn (GOK; volgende run nameten).
- **Trade Republic, ETF's:** spaarplan gratis, losse order 1 euro (DERDEN, [Curvo](https://curvo.eu/nl/artikel/trade-republic-kosten)).
- **DEGIRO, ETF's:** 1 euro per aankoop voor de kernselectie op Tradegate; op een andere beurs 3 euro plus 2,50 euro per beurs per jaar (DERDEN, [Curvo, 22 okt 2026](https://curvo.eu/nl/artikel/degiro-kosten-etf)). Sinds 1 okt 2025 telt alleen Tradegate nog als kernselectie (DERDEN, [De Belegger](https://www.debelegger.nl/post/degiro-schrapt-kernselectie-buiten-tradegate-dit-veranderd-er-voor-beleggers)).

**Conclusie kosten (GOK):** bij een maandbedrag van een paar honderd euro is de keuze van aanbieder het verschil tussen ruwweg 0,2% en 2% per aankoop. Dat is meer dan wat een slimme koopregel in punt 2 opleverde. De goedkoopste route is dus eerst een goedkope aanbieder kiezen, pas daarna nadenken over regels.

### 4. Wanneer voegt een eigen bot iets toe?
**Niets toe, want de beurs doet het al:** gewoon elke week of maand een vast bedrag kopen. Bitvavo, Kraken, Coinbase, Bitpanda, Trade Republic en anderen hebben dit ingebouwd (DERDEN, zie punt 3). Een eigen bot op Bitvavo bespaart hooguit het verschil tussen maker 0,15% en taker 0,25% (GEZIEN door B): 0,30 euro op 300 euro per maand (eigen som, GOK). Daar staan een server, onderhoud en een API-sleutel tegenover die gestolen kan worden.

**Wel iets toe (maar bewijs eerst):**
- Een koopregel die de beurs niet heeft (meer kopen onder het gemiddelde, "mult"). In mijn meting geen voordeel bij BTC, gemengd bij ETH (punt 2).
- Herbalanceren tussen twee of meer munten. Gemengde uitslag in mijn meting, en verkopen kost extra en kan belasting raken (GOK).
- Kopen bij een beurs zonder ingebouwd spaarplan, of automatisch opnemen naar een eigen wallet. Dat laatste vraagt wel een sleutel met opnamerecht, wat B afraadt (bij Bitvavo gaan API-opnames zonder 2FA, GEZIEN door B).

**Open source projecten die precies DCA doen** (alleen gelezen, niets uitgevoerd; sterren en datum GEZIEN via api.github.com op 19 nov 2026):

| Project | Sterren | Laatste push | Wat | Let op |
|---|---|---|---|---|
| [jorijn/bitcoin-dca](https://github.com/jorijn/bitcoin-dca) | 85 | 7 jul 2025 | Docker-tool, koopt en neemt op; Bitvavo, Kraken, BL3P, Binance | README vraagt een sleutel met **read, trade en withdraw**. Zet withdraw uit als je de opname-functie niet gebruikt (GOK dat dat werkt, niet getest) |
| [raphaellueckl/kraken-dca](https://github.com/raphaellueckl/kraken-dca) | 35 | 30 okt 2026 | Eén bestand Node, zonder afhankelijkheden; verdeelt je maandstorting over zo veel mogelijk kleine aankopen | Alleen Kraken, alleen BTC. README zegt sleutel met alleen "Query Funds" en "Create & Modify Orders" (GEZIEN). Koopt via Kraken Pro, niet via de duurdere 1%-knop (GOK) |
| [Drakkar-Software/OctoBot](https://github.com/Drakkar-Software/OctoBot) | 6960 | 16 nov 2026 | Groot framework met DCA, grid en meer | Veel te zwaar voor alleen maandelijks kopen (GOK); B behandelt het als framework |
| [Open-Trader/opentrader](https://github.com/Open-Trader/opentrader) | 2936 | 29 jun 2025 | DCA en grid met een UI | Sinds juni 2025 geen push (GEZIEN) |
| [melroy89/auto-invest-bitvavo](https://github.com/melroy89/auto-invest-bitvavo) | 2 | 29 okt 2022 | Klein Bitvavo-script | Oud en bijna niet gebruikt |

Let op het woord "DCA bot" bij handelsbots als 3Commas en OctoBot: daar betekent het vaak bijkopen in een dalende positie om sneller winst te nemen (middelen tijdens een trade), niet maandelijks sparen. Dat is een ander en riskanter iets (GOK, volgt uit hoe die tools het beschrijven; B gaat over die tools).

### 5. Wat dit betekent voor het doel van 10.000 euro in 3 maanden (BRIEF)
Een maandinleg van een paar honderd euro haalt dat doel niet, met geen enkele aanpak hier: drie maanden inleg is maar een paar honderd keer drie, en zelfs het beste venster in punt 2 was x3,13 over 36 maanden, niet over 3 (GEZIEN en GOK). De maandinleg is een aparte, rustige pot; het doel van 10.000 euro moet uit de routes van A, B of D komen. Rangorde binnen deze hoek, op kans maal opbrengst (GOK, met reden):
1. **Goedkope ingebouwde spaarplan, gewone DCA** (BTC, een brede ETF, of beide). Kans op winst over jaren redelijk, ergste geval een grote daling op papier. Kost geen bouwtijd.
2. **Hetzelfde met een eigen script voor maker-orders of een eigen koopregel.** Hooguit enkele tienden van procenten beter, of slechter; alleen zinvol als leerproject.
3. **Wachten op dips, grid of veel handelen met de maandinleg.** In de meting slechter of gelijk, met meer kosten en meer werk.

### Nog te doen (volgende runs)
- Spread van Trade Republic crypto en van "simpel kopen" bij Bitvavo nameten (prijs in de app tegen de orderboekprijs).
- Dezelfde meting voor een brede ETF (bijv. een wereld-index) en een mix ETF plus BTC, met de echte 1-euro-kosten.
- Grid met maandinleg terugtesten, met kosten.
- Ervaringen uit forums (r/BitcoinBeginners, Tweakers, Freqtrade-forum) over spaarplannen en kleine bedragen ordenen.
- Wat er gebeurt met belasting bij herbalanceren en vaak verkopen in Nederland (algemeen, niets over Thijs).

## Stand na run 01:40 (19 nov 2026)
1. **Gewone DCA is moeilijk te verslaan.** Op BTC-EUR 2020 tot 2026 won geen enkele dip- of multiplier-regel vaker dan 6 van 45 vensters van 36 maanden; wachten op een dip won nooit (GEZIEN, eigen meting). Bij ETH ongeveer de helft, wat op toeval lijkt (GOK).
2. **Procentuele kosten doen bij maandelijks kopen weinig** (0,25% tegen 0%: x2,824 tegen x2,831 over 80 maanden, GEZIEN); **vaste kosten per aankoop wel** (1 euro op 100 euro is 1%).
3. **Aanbieder kiezen is de grootste knop:** periodiek kopen kost van 0,2% (OKX) en 0,25% (Bitvavo) tot 1% (Kraken) en bijna 2% plus spread (Coinbase) (DERDEN, [CryptoTicker](https://cryptoticker.io/nl/vergelijking/bitcoin-spaarplan/)). ETF-spaarplan bij Trade Republic gratis, DEGIRO 1 euro via Tradegate (DERDEN).
4. **Een eigen bot voegt voor gewone DCA bijna niets toe** (hooguit 0,1% maker-voordeel, GOK op GEZIEN-tarief) en brengt een API-sleutel als risico mee. Als leerproject zijn [raphaellueckl/kraken-dca](https://github.com/raphaellueckl/kraken-dca) (actief, één bestand, sleutel zonder opname) en [jorijn/bitcoin-dca](https://github.com/jorijn/bitcoin-dca) (Bitvavo en Kraken, vraagt wel opnamerecht) de bruikbare voorbeelden (GEZIEN).
5. **De maandinleg haalt het doel van 10.000 euro in 3 maanden niet** (GOK); zie het als aparte, rustige pot naast de routes van A, B en D.

## Run 2 (19 nov 2026, ±02:05 tot 02:35 UTC)
Deze run: een brede ETF en een mix ETF plus BTC doorgemeten over 12 jaar, grid met maandinleg teruggetest op uurdata, spreads nagemeten, en wat de belasting in Nederland doet met herbalanceren. Script en data stonden in /tmp en zijn niet in de repo gezet; de opzet staat erbij.

### 6. Eigen meting: wereld-ETF, BTC en een mix (GEZIEN)
**Data:** dagkoersen IWDA (iShares MSCI World, Euronext Amsterdam, in euro, stapelend) en BTC-EUR, openbare grafiek-API van Yahoo Finance via curl, zonder account. Gebruikt: de eerste handelsdag van elke maand, nov 2014 tot nov 2026, 146 maanden.

**Opzet:** elke maand 300 euro (voorbeeldbedrag), gesplitst in een vast deel ETF en een vast deel BTC. ETF zonder kosten (spaarplan Trade Republic is gratis, DERDEN in run 1), BTC 0,25% (Bitvavo). Variant "herb": eens per jaar terug naar de vaste verdeling (met 0,25% op BTC en 1 euro op de ETF; bij bijkopen van BTC heb ik de 0,25% niet gerekend, dus een fractie te gunstig). Uitkomst = waarde gedeeld door ingelegd. Vensters van 36 en 60 maanden over elke startmaand.

| Verdeling ETF/BTC | 36 mnd mediaan | 36 mnd slechtste | 36 mnd beste | 60 mnd mediaan | 60 mnd slechtste | Diepste tussenstand | Hele periode |
|---|---|---|---|---|---|---|---|
| 100/0 | x1,18 | x0,93 | x1,38 | x1,35 | x1,02 | x0,84 | x2,28 |
| 95/5 | x1,26 | x0,95 | x2,44 | x1,48 | x1,25 | x0,84 | x4,52 |
| 90/10 | x1,30 | x0,96 | x3,74 | x1,57 | x1,27 | x0,83 | x6,75 |
| 90/10 herb | x1,31 | x0,98 | x2,39 | x1,53 | x1,36 | x0,83 | |
| 80/20 | x1,42 | x1,00 | x6,34 | x1,78 | x1,31 | x0,83 | x11,22 |
| 80/20 herb | x1,43 | x1,03 | x3,89 | x1,76 | x1,40 | x0,83 | |
| 50/50 | x1,79 | x1,00 | x14,15 | x2,34 | x1,40 | x0,72 | x24,63 |
| 0/100 | x2,39 | x0,91 | x27,16 | x3,33 | x1,35 | x0,51 | x46,98 |

(Alles GEZIEN, eigen meting; "diepste tussenstand" = laagste waarde gedeeld door ingelegd op enig moment in enig venster.)

**Wat ik eruit haal:**
- **Een klein deel BTC naast een brede ETF verhoogde de uitkomst flink zonder dat de diepste dip veel dieper werd.** Bij 90/10 en 80/20 bleef de diepste tussenstand x0,83, bijna gelijk aan alleen de ETF (x0,84). Bij alleen BTC was dat x0,51: op enig moment stond je de helft van je inleg kwijt (GEZIEN).
- **Jaarlijks herbalanceren maakte de slechtste vensters iets beter en de beste vensters veel minder goed** (80/20: slechtste x1,03 tegen x1,00, beste x3,89 tegen x6,34). De mediaan bleef gelijk. Het is een rem op uitschieters, geen extra rendement (GEZIEN).
- **Grote waarschuwing:** deze 12 jaar bevatten de sterkste groei die BTC ooit had (van ongeveer 300 naar 57.000 euro). Dat de BTC-kolommen zo hoog uitkomen, zegt niets over de komende 12 jaar. Het "beste venster" x27 komt uit 2015 tot 2018 en is niet te herhalen op deze schaal (GOK, maar met een reden: een markt van biljoenen kan niet nog eens 190 keer groeien zoals bij een kleine markt).
- Ook de ETF had een gunstige periode (wereldaandelen in euro 2014 tot 2026). Een venster van 36 maanden met alleen de ETF eindigde 1 keer onder de inleg (x0,93), bij 60 maanden nooit (GEZIEN).

### 7. Eigen meting: grid met maandinleg tegen gewone DCA (GEZIEN)
**Data:** uurkoersen BTC-EUR, Binance openbare archieven (`data.binance.vision/data/spot/monthly/klines/BTCEUR/1h/`), jan 2023 tot okt 2026, 33.599 uren, zonder account. In die periode ging BTC van ongeveer 15.400 naar 68.600 euro (GEZIEN).

**Opzet:** elke maand 300 euro in kas. De grid koopt telkens als de koers een trede (1, 2 of 5%) lager komt, en verkoopt dat stukje weer zodra het een trede hoger staat. Kosten 0,15% per kant (Bitvavo maker, aanname dat elke limietorder vol wordt uitgevoerd, dus gunstig). Koopbedrag per trede: een vast bedrag (15, 30, 60 euro) of een deel van de kas (10 of 25%). Gewone DCA: elke 1e van de maand alles kopen, 0,25%.

| Aanpak | Eindwaarde / ingelegd | Aantal orders |
|---|---|---|
| Gewone DCA, maandelijks | **x1,48** | 46 |
| Grid 2%, 25% van kas per trede | x1,25 | 1.978 |
| Grid 5%, 25% van kas | x1,27 | 306 |
| Grid 1%, 10% van kas | x1,10 | 7.302 |
| Grid met vast bedrag 60 euro (stap 1 tot 5%) | x1,02 tot x1,07 | 306 tot 7.266 |
| 80% DCA, 20% grid 2% | x1,43 | 1.838 |

(GEZIEN, eigen meting.)

**Wat ik eruit haal:**
- **Grid verloor in alle varianten van gewone DCA**, ook met lage maker-kosten. Twee redenen: de grid verkoopt elk stukje na 1 tot 5% winst en mist zo de rest van de stijging; en met een vast koopbedrag bleef het grootste deel van het geld als kas liggen (GEZIEN).
- Dit was wel een stijgende periode. In een markt die jaren zijwaarts gaat, doet een grid het relatief beter (GOK; bekend uit hoe grid werkt, niet zelf gemeten op zo'n periode).
- Een grid met 2.000 tot 7.000 orders in vier jaar betekent ook een bot die dag en nacht draait, een API-sleutel met handelsrecht, en veel regels voor de belasting en de administratie (GOK).
- Conclusie voor deze hoek: grid past niet bij een vaste maandinleg die je jaren wilt laten groeien.

### 8. Spreads nagemeten
- **Bitvavo orderboek** (openbare API, zonder account, 19 nov 2026 02:12 UTC): BTC-EUR beste bod 57.217, beste vraag 57.218, dus een spread van 0,002%. ETH-EUR 1.618,80 tegen 1.618,89, 0,006% (GEZIEN, `api.bitvavo.com/v2/BTC-EUR/book`). Wie via de API of de Pro-weergave met een limietorder koopt, betaalt dus vrijwel alleen de 0,15 of 0,25%. De prijs bij "simpel kopen" in de app kan ik zonder account niet zien; nog open.
- **Trade Republic crypto:** naast 1 euro per losse order gemiddeld ongeveer **0,50% spread** (DERDEN, [Capitalo](https://www.capitalo.de/anbieter/traderepublic/produkte/krypto)). Ook bij een spaarplan zonder kosten betaal je die spread (GOK, de spread zit in de prijs). Op 300 euro is dat ongeveer 1,50 euro per aankoop (eigen som, GOK). Dat maakt Trade Republic voor crypto duurder dan Bitvavo of OKX periodiek kopen (0,2 tot 0,25%), en voor ETF's juist het goedkoopst (gratis spaarplan).
- Zelfde bron: Coinbase 0,60/1,20% plus 0,50% spread, Bitpanda 0,99%, 21Bitcoin 0,79% plus 1,25% spread (DERDEN, Capitalo).

### 9. Correctie op run 1: kraken-dca en de nieuwe Kraken-tarieven
In run 1 schreef ik dat [raphaellueckl/kraken-dca](https://github.com/raphaellueckl/kraken-dca) via Kraken Pro koopt en zo de 1%-knop ontwijkt. B vond dat Kraken Pro sinds juli 2026 voor kleine klanten **0,40% maker en 0,80% taker** rekent (DERDEN via B, [Kraken support](https://support.kraken.com/articles/cross-platform-fee-tier-changes)). Dat script bespaart op Kraken dus nog wel iets tegenover 1%, maar is duurder dan gewoon periodiek kopen bij Bitvavo (0,25%) of OKX (0,2%) (GOK, eigen vergelijking).

### 10. Belasting in Nederland (algemeen, niets over Thijs)
- **2026: box 3 met een vast verondersteld rendement.** Beleggingen en crypto vallen onder "overige bezittingen" met een forfait van **6%**; heffingsvrij vermogen 59.357 euro per persoon (DERDEN, [SRA, 8 jan 2026](https://www.sra.nl/nieuws/259001/2026/01/box-3-percentages-vrijstellingen-en-bedragen-2026)); tarief 36% (DERDEN, [Rendement](https://www.rendement.nl/inkomen-uit-sparen-en-beleggen/nieuws/box-3-tarief-blijft-36-in-2026.html)). Is het werkelijke rendement lager, dan kun je dat aantonen met de tegenbewijsregeling (DERDEN, SRA).
- **Gevolg voor de aanpak:** onder dit stelsel kost herbalanceren of verkopen op zich geen extra belasting; alleen de waarde op 1 januari telt (GOK op basis van hoe het forfait werkt). Herbalanceren is dus nu alleen een kostenvraag (punt 6), geen belastingvraag.
- **Vanaf 2028 verandert het waarschijnlijk.** In oktober 2026 koos het kabinet voor een vermogenswinstbelasting per 2028 voor financiële bezittingen zoals spaargeld en aandelen, en pas in 2030 met een nieuwe wet ook crypto. De Eerste Kamer moest het nog behandelen (DERDEN, [Eerste Kamer, 6 okt 2026](https://www.eerstekamer.nl/nieuws/20261006/mondeling_overleg_over_box_3)). Dan gaan jaarlijkse waardestijging en dus ook elke verkoop met winst meetellen (GOK, details nog niet vast). Een grid of vaak herbalanceren wordt dan voor de aangifte veel meer werk.

### 11. Bijgestelde rangorde binnen hoek C (kans maal opbrengst, GOK)
1. **Spaarplan in een brede ETF, met eventueel een klein vast deel BTC (5 tot 20%) via de goedkoopste aanbieder per soort** (ETF: Trade Republic gratis of DEGIRO 1 euro; BTC: OKX of Bitvavo 0,2 tot 0,25%). In de meting gaf dit het beste evenwicht tussen uitkomst en diepste dip (punt 6). Geen bot nodig.
2. **Hetzelfde, met eens per jaar herbalanceren** als je uitschieters wilt dempen. Kan met de hand in tien minuten per jaar (GOK); een bot voegt niets toe.
3. **Eigen script voor DCA met limietorders of een eigen koopregel.** Hooguit 0,1% goedkoper (punt 8), regels gaven geen voordeel bij BTC (run 1). Alleen als leerproject.
4. **Grid of wachten op dips met de maandinleg.** In beide metingen slechter dan gewone DCA (run 1 punt 2, run 2 punt 7).

Voor het doel van 10.000 euro in 3 maanden verandert er niets: geen van deze aanpakken haalt dat (run 1 punt 5).

### Nog te doen (volgende runs)
- Prijs bij "simpel kopen" en bij het spaarplan van Bitvavo tegenover het orderboek (kan alleen met een openbare bron of schermafbeelding van een ander; zelf niet inloggen).
- Grid testen op een zijwaartse periode (bijv. BTC 2018 tot 2020) om te zien of het daar wel wint.
- Forumervaringen ordenen (Tweakers, r/BitcoinBeginners, r/eupersonalfinance) over spaarplannen en kleine bedragen.
- Wekelijks tegen maandelijks kopen met echte vaste kosten (bijv. 1 euro bij DEGIRO) doorrekenen.

## Stand na run 02:35 (19 nov 2026)
1. **Gewone DCA wint van slimme regels en van grid.** BTC 2020 tot 2026: geen dip- of multiplierregel won vaker dan 6 van 45 vensters (run 1). Grid op uurdata 2023 tot 2026: x1,02 tot x1,27 tegen x1,48 voor gewone maandelijkse DCA (GEZIEN, eigen metingen).
2. **Een klein vast deel BTC naast een wereld-ETF gaf in 2014 tot 2026 veel meer uitkomst met bijna dezelfde diepste dip** (80/20: mediaan 36 maanden x1,42 tegen x1,18, diepste tussenstand x0,83 tegen x0,84; alleen BTC x0,51) (GEZIEN). Let op: dit was de uitzonderlijke groeiperiode van BTC; niet door te trekken (GOK).
3. **Aanbieder per soort kiezen is de grootste knop:** ETF-spaarplan gratis (Trade Republic) of 1 euro (DEGIRO); crypto 0,2 tot 0,25% (OKX, Bitvavo) tegen ongeveer 0,5% spread bij Trade Republic, 0,99% Bitpanda, tot bijna 2% bij Coinbase (DERDEN, links in run 1 en punt 8). Kraken Pro is sinds juli 2026 voor kleine klanten 0,40/0,80% (DERDEN via B).
4. **Een eigen bot voegt voor een maandinleg bijna niets toe:** het orderboek van Bitvavo heeft een spread van 0,002% (GEZIEN), dus het enige voordeel is maker tegen taker (0,1%), tegenover een API-sleutel als risico. Herbalanceren eens per jaar kan met de hand.
5. **Belasting:** in 2026 telt alleen de waarde op 1 januari (forfait 6% op beleggingen, DERDEN), dus herbalanceren kost nu geen extra belasting. Vanaf 2028 komt waarschijnlijk een vermogenswinstbelasting, voor crypto pas vanaf 2030; nog niet vast (DERDEN, Eerste Kamer). De maandinleg haalt het doel van 10.000 euro in 3 maanden niet (GOK).
