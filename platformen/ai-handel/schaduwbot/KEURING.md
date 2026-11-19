# Keuring schaduwbot Polymarket, 19 nov 2026, keurder (losse Claude, niet de bouwer)
Wat ik keurde: commit 2b7c002e (code op main) en 6c976d4f (code van de lopende run), bestanden `schaduwbot.py`, `rapport.py`, `test_schaduwbot.py`, `README.md` in deze map en `.github/workflows/schaduwbot.yml`; data op de tak `ai-handel-data` tot commit 738f53d4 (`dag/2026-11-19/*-44492859030-000`, eerste 32 minuten van run 44492859030).
Akkoord: **nee**, maar dicht bij ja. De rekenregels kloppen met de docs, de vullingen kloppen met de echte trades (10 van 10 nagekeken), de stopregel klopt met de marktregels, de workflow is veilig en de grenzen staan eerlijk in de README. Eén moet-punt: de opschaling naar €2.000 en €5.000 telt alleen het geld in open orders en niet het geld dat vastzit in gevulde voorraad tot de uitslag. Daardoor lijkt de opbrengst per euro tot ±2 keer hoger dan hij is.

Dit is meten, geen beleggingsadvies. Ik keur alleen of de meting klopt en eerlijk gebracht is.

## Wat ik zelf nakeek (curl en eigen scripts, 19 nov ±09:40 UTC)

| # | Wat | Hoe | Uitslag |
|---|---|---|---|
| 1 | Formule beloning | [docs Liquidity Rewards](https://docs.polymarket.com/programs/liquidity-rewards.md) zelf gelezen: S(v,s) = ((v − s)/v)² · b; Q_one = biedingen op JA plus laatorders op NEE, Q_two andersom; Q_min = max(min(Q_one, Q_two), max(Q_one/c, Q_two/c)) tussen 0,10 en 0,90, anders min; c = 3,0; elke minuut een steekproef op een willekeurige seconde; Q_final over de UTC-dag | `punten`, `q_min`, `onze_score` volgen dit precies. Geen in-game-vermenigvuldiger b nodig (geen sport) |
| 2 | Boek van JA bevat ook NEE-orders | `POST /books` voor JA en NEE van dezelfde markt (London laagste 0°C): JA-biedingen 0,011 / 0,01 zijn NEE-laatorders 0,989 / 0,99, enzovoort | klopt: het boek is gespiegeld, dus Q_one en Q_two uit alleen het JA-boek is juist |
| 3 | Beloningsvelden | `clob.polymarket.com/rewards/markets/current`: `rewards_max_spread` 4,5, `rewards_min_size` 20, `rate_per_day`, `start_date`/`end_date` | velden bestaan zoals de code ze leest |
| 4 | Trades zonder dubbeltelling | [docs List trades](https://docs.polymarket.com/api-reference/feeds/list-trades.md): `taker_only` "Defaults to `true`: each fill is served once, on its taker side"; `event_id` hooguit 20 per verzoek | klopt: geen makerrijen die als nemer zouden tellen, en 20 events per verzoek |
| 5 | Stopregel | marktregel Tokio laagste 21 nov: "An observation counts if its time stamp, converted to the station's local time ... falls on the observation date"; in de meta: Houston 21 nov stop 06:00 UTC, Londen 21 nov 00:00 UTC; alle 49 steden in de open weer-events staan in `STEDEN` | klopt |
| 6 | Uitslag ophalen | Gamma, Londen hoogste 17 nov: `closed` true, `outcomePrices` ["1","0"] of ["0","1"] | werkt zoals `haal_uitslagen` verwacht |
| 7 | Beloning zelf nagerekend | eigen script los van de code, boek van Ankara 19°C (v 4,5, min 20): midden 0,50, onze orders 0,49 / 0,51, onze score 12,1, anderen Q_one + Q_two 57,0, aandeel laag 17,5% | zelfde orde als de data: over alle gemeten marktminuten (1c) pakt de bot 10,2% (laag) tot 20,8% (hoog) van de pot (GEZIEN, eigen optelling) |
| 8 | Vullingen nagekeken | 10 vullingen (8 van 1c, 2 van 3c) naast de echte trade in `data-api /v2/trades?condition=...` op dezelfde seconde | 10 van 10 kloppen: tijd, grootte, omzetting NEE naar JA (bijv. NEE kopen 0,7040 = JA verkopen 0,296), kant, en los of streng |
| 9 | Verlies 5 minuten later nagerekend | met de hand op het gemeten midden, 7 markten | gelijk aan `rapport.midden_op` op 4 decimalen. Voorbeelden: Lucknow 28°C bod 0,307 × 20, midden 5 min later 0,284: −$0,46; Shenzhen 19°C laat 0,36 × 20, midden 0,345: +$0,30 |
| 10 | Tests | `python3 -m unittest test_schaduwbot.py` | 12 tests groen |
| 11 | Run | `organisatie/controle/actions.py 44492859030` | bezig sinds 09:03 UTC (commit 6c976d4f), stap "Meten (5 uur 45)", eerste data om 09:34 op de tak. Opvolger 44497668837 (push 09:34): klok gaf geen beurt, `lang` overgeslagen, geslaagd. Zo hoort het |

## Eerste uitkomst (32 minuten, één tijdstip, GEZIEN als meting, alles daarboven GOK)
- Variant 1c: gemiddeld 251 markten, $4.899 aan orders, beloning $8,27 (laag) tot $16,87 (hoog) in 32 minuten; 72 vullingen (45 streng), $252 gevuld; 5 minuten later −$1,24, dus −0,53% per gevulde dollar.
- Variant 3c: $2,11 tot $4,67 beloning, 8 vullingen, −4,59% per gevulde dollar (te weinig om iets te zeggen).
- Lineair doorgetrokken is dat $370 tot $760 per dag op ±$4.900 aan orders (GOK: 32 minuten, één tijdstip, zonder verlies 1 uur later, zonder uitslag, zonder voorraadgeld, en zonder dat andere bots reageren). Dit is een reden om door te meten, geen opbrengst.

## Deel A: doet het wat beloofd is?
(toets tegen de opdracht, `B-zelf-bouwen.md` punt 30 tot 35 en 39 tot 44, `D-arbitrage.md` route 1 en de README)

| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| A1 | De beloningsformule volgt de docs precies (claim 1 en 2), inclusief eenzijdig gedeeld door 3 alleen tussen 0,10 en 0,90, max afstand v en minimale grootte (onze order is altijd minstens `rewards_min_size`) | feit | hoog | n.v.t. |
| A2 | Lege en losse boeken vallen af (beste bod en laat hooguit 5 cent uit elkaar, beide kanten nodig); na de stop geen beloning; bij de voorraadrem valt één kant weg en daalt de score zoals de regel zegt | feit | hoog | n.v.t. |
| A3 | De **lage** grens is echt een ondergrens voor ons aandeel (bij het geschatte midden): de echte score van de anderen, de som van hun Q_min, is nooit groter dan Q_one + Q_two van het hele boek | feit (wiskunde) | hoog | n.v.t. |
| A4 | De **hoge** grens is geen harde bovengrens: hij filtert per prijsniveau (een niveau van ≥ 20 aandelen kan uit kleine orders bestaan die niet tellen) en Q_min van het hele boek kan zowel boven als onder de som van de losse Q_min liggen. Als schatting prima; het woord "grens" in README en rapport is iets te sterk | feit | midden | voorbeeld: maker 1 (9 bod, 0 laat) en maker 2 (0,33 bod, 1 laat) geven samen 3,33, het hele boek 3,11 |
| A5 | Wat de beloning nog te mooi kan maken, staat in de README: andere bots reageren niet op een schaduw, het aangepaste midden is een benadering. Bij 1c staat onze order bijna altijd binnen de spread (we zijn het beste bod), dus we krijgen alle vullingen van die kant. Dat maakt de vullingen eerder te somber dan te mooi, en dat is de goede kant | feit (staat erin) / vermoeden (richting) | midden | echte bot, of vergelijken met `market_competitiveness` |
| A6 | Vullingen: los = trade op of door onze prijs, streng = erdoorheen; als onze order binnen de spread staat en de trade op het echte beste niveau gaat, telt hij terecht als streng (de nemer had ons eerst geraakt). Per trade hooguit één order per variant, hooguit de ordergrootte, daarna is de order weg tot de volgende minuut. 10 van 10 nagekeken vullingen kloppen (claim 8) | feit | hoog | n.v.t. |
| A7 | "Streng" is geen losse simulatie: voorraad en voorraadrem lopen op de losse vullingen, en strenge vullingen zijn een deel daarvan. Het strenge verlies per dollar is dus bruikbaar, een strenge voorraad of strenge netto niet | feit | hoog | n.v.t. |
| A8 | Verlies 5 minuten en 1 uur later wordt gemeten tegen het gemeten gewone midden, vooruit ingevuld binnen dezelfde run; tegen de uitslag via Gamma. Nagerekend en gelijk (claim 9). Na de stop volgt de bot het midden nog 2 uur, dus vullingen vlak voor de stop krijgen ook een prijs 1 uur later | feit | hoog | n.v.t. |
| A9 | Vullingen zonder prijs 1 uur later (laatste uur van een run als de volgende run later start) tellen in netto en opschaling als 0 verlies, terwijl hun beloning wel meetelt. Per dag staat "(n nog zonder prijs)" erbij, bij "Opgeschaald" niet. Kleine scheefheid naar mooi | feit | hoog | aandeel vullingen zonder prijs in het rapport na 2 dagen |
| A10 | De bot houdt voorraad tot de uitslag (geen afbouw), dus het echte resultaat is "tegen de uitslag". De beslisregel kijkt naar "1 uur later". D mat beide (0,1% en 0,3%), dus het scheelt waarschijnlijk weinig, maar de beslisregel hoort ook de uitslag te noemen zodra die er is | feit | midden | rapport na 2 tot 3 dagen |
| A11 | Stopregel middernacht lokale tijd van het meetstation klopt met de marktregels (claim 5). Laagste-temperatuurmarkten zitten erin, terwijl D alleen hoogste mat; bij "laagste" is de avond ervoor al veel bekend (de temperatuur om middernacht telt mee). Het rapport splitst per stad hoogste en laagste, maar niet het verlies per dollar | feit (dat ze erin zitten), vermoeden (meer risico) | midden | verlies per dollar apart voor hoogste en laagste |
| A12 | Voorraadrem werkt, maar te laat: in 32 minuten één keer 53 aandelen tegen een grens van 40 (markt 270579ae5a, twee vullingen 45 seconden na elkaar). Staat eerlijk in de README | feit | hoog | n.v.t. |
| A13 | **Opschaling telt het geld in gevulde voorraad niet mee.** "Kapitaal" is alleen het geld in open orders (±$4.900 bij 1c). Gevulde aandelen blijven tot de uitslag staan (1 tot 3 dagen) en kosten ook geld. Na 32 minuten zat er al ±$476 in voorraad (1c, 53 markten, bruto zonder JA en NEE tegen elkaar weg te strepen; eigen berekening op de vullingen). De rem staat tot 40 aandelen per kant per markt toe, bij ±250 markten kan dat in de orde van de orders zelf komen. Het rapport zegt dan "€5.000 haalt alles wat de bot gebruikte", terwijl er in werkelijkheid meer nodig is; de opbrengst per euro kan tot ±2 keer te hoog lijken | feit (voorraadgeld telt niet), vermoeden (factor) | hoog / midden | gemiddeld en grootste voorraadgeld per dag in het rapport |
| A14 | Opschaling verder eerlijk: gelabeld GOK, lineair naar het geld, nooit boven wat de bot gebruikte, belasting en verbod uitdrukkelijk niet meegerekend, koers 1 $/€ als GOK met `--koers`. Opbrengst staat in dollar, inleg in euro; met het $-teken erbij is dat leesbaar | feit | hoog | n.v.t. |
| A15 | Valuta van de beloning: de configuraties noemen een munt-adres (`asset_address`) dat niet het voorbeeld uit de docs is; de bot telt alle `rate_per_day` op als dollar. Waarschijnlijk een dollarmunt van Polymarket, niet nagekeken | vermoeden | laag | munt-adres opzoeken |
| A16 | "Jong" wordt niet apart gefilterd: alle open temperatuurmarkten met beloning tot de stop. Omdat ze ±2 dagen vooraf worden gemaakt (createdAt 19 nov 07:11 voor 21 nov), zijn ze vanzelf jong. Prima | feit | midden | n.v.t. |

## Deel B: houdt het zich aan onze regels?

| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| B1 | Geen account, geen sleutel, geen wallet, geen orders: alleen GET en `POST /books` (openbaar leesverzoek); `proxy_wallet` van derden alleen in het geheugen voor ontdubbelen, niet in de data op de tak | feit | hoog | opdracht, harde regel 1 |
| B2 | Geen persoonsgegevens van Thijs; README gebruikt `<eigenaar van deze repo>`; `check.py` zegt "Controle openbare repo: OK" | feit | hoog | harde regel 2 |
| B3 | Workflow: geen geheimen (alleen het eigen `GITHUB_TOKEN` van de checkout), nooit geforceerd (gewone push, bij botsing opnieuw ophalen, 5 pogingen), main blijft schoon (eigen `GIT_INDEX_FILE`, commit alleen naar `ai-handel-data`, klok alleen naar tak `klok`) | feit | hoog | harde regel 6 |
| B4 | Geen botsing met de koersverschil-scanner: andere map op dezelfde tak (`dag/`, `proef/` tegen `scanner/`), beide bouwen op de laatste stand en pushen gewoon; de tak toont al commits van beide door elkaar (738f53d4, 39217741, a26e7619) | feit | hoog | harde regel 6 |
| B5 | Een push in deze map start de lopende run **niet** opnieuw: de klok wordt aangeroepen zonder `--paden`, dus elke push geeft hooguit elke 5,5 tot 6 uur een beurt en een nieuwe lange run wacht (concurrency zonder annuleren). Anders dan bij de scanner | feit | hoog | n.v.t. |
| B6 | Krappe tijd: job-limiet 355 minuten, meten 345 plus 90 seconden plus wegschrijven plus rapport (tak ophalen, uitslagen per event). Loopt het rapport over de limiet, dan is de data al bewaard maar ontbreekt `rapport.md` van die run | vermoeden | midden | n.v.t. |
| B7 | README noemt de grenzen: voorwaarden van Polymarket verbieden handelen vanuit Nederland (ook via API, VPN verboden), verbod van de Ksa, nietige gokovereenkomst, mogelijk 37,8% kansspelbelasting, "meten, geen advies" | feit | hoog | opdracht punt 6 |
| B8 | Cijfers gelabeld: beloning GOK, vullingen GEZIEN, opschaling GOK | feit | hoog | harde regel 5 |
| B9 | `schaduwbot.py` heeft 603 regels, boven de ±400 uit de bouwregels. Nu splitsen raakt code onder een lopende meting; liever na de 2 weken | feit | hoog | bouwregels |
| B10 | Tests dekken formule, plan, rem, vulling, stopregel en rapport; niet `trades()` (bladeren, ontdubbelen) en niet `zet_op_tak` | feit | hoog | bouwregels |
| B11 | Data op de tak groeit: elke flush een meta-bestand van ±196 KB met alle markten opnieuw (±9 MB per dag), en `rapport.py --tak` haalt de hele tak op, ook de scanner. Over 2 weken nog te doen, daarna merkbaar | feit | midden | n.v.t. |
| B12 | Geen gedachtestreepjes gevonden; Nederlands | feit | hoog | harde regel 8 |

## Werkt het, en mag het? (apart, besluit 19 nov 09:40)
- **Werkt het (gemeten):** te vroeg. Na 32 minuten pakt een order van $20 per markt in ±250 temperatuurmarkten 10 tot 21% van de pot (GOK op GEZIEN-boeken) en kosten de vullingen na 5 minuten −0,53% per dollar (GEZIEN, 68 vullingen). Dat past bij D (64% aandeel voor $200, verlies 0,1 tot 0,3%). De meting is goed genoeg om na 2 weken op te beslissen, na het moet-punt hieronder.
- **Mag het (regels):** grijs tot verboden vanuit Nederland volgens de voorwaarden van Polymarket en de Ksa; belasting mogelijk 37,8%. Dat is een keuze voor Thijs, geen meetfout. De bot zelf leest alleen openbare data en mag dat.

## Moet (blokkeert akkoord)
1. **Voorraadgeld in de opschaling (A13).** Tel in het rapport het geld dat vastzit in gevulde voorraad mee (kosten van de open positie tot de uitslag, per markt JA en NEE tegen elkaar weggestreept), naast het geld in orders. Gebruik de som voor "op de boeken" en de grens in de tabel voor €2.000 en €5.000, of zet beide getallen naast elkaar met de duidelijke zin dat de inleg minstens orders plus voorraad moet dekken. Dit hoort in `rapport.py`; de ruwe vullingen bevatten alles wat nodig is, dus de lopende meting hoeft niet te stoppen.

## Kan (mag later)
1. Bij "Opgeschaald" ook melden hoeveel vullingen nog geen prijs 1 uur later hebben, of hun verlies schatten met het verlies per dollar van de rest (A9).
2. Beslisregel in README: naast "1 uur later" ook "tegen de uitslag" zodra die er is, want de bot houdt tot de uitslag (A10).
3. Verlies per gevulde dollar apart voor hoogste en laagste temperatuur (A11).
4. "Hoge grens" in README en rapport "hoge schatting" noemen (A4).
5. Munt-adres van de beloning nakijken (A15).
6. Na de 2 weken: `schaduwbot.py` splitsen (B9), tests voor `trades()` en `zet_op_tak` (B10), meta alleen bij wijziging wegschrijven en `rapport.py` alleen `dag/` laten ophalen (B11), wat meer speling in de job-limiet (B6).

## Herkeuring, 19 nov 2026 ±09:55 UTC, zelfde keurder
Wat ik keurde: commit 48b9ea30 (`rapport.py`, `README.md`, `test_schaduwbot.py`, `.github/workflows/schaduwbot.yml`).
Akkoord: **ja**. Het moet-punt is opgelost; de opschaling is nu eerlijk binnen wat 32 minuten data kan zeggen.

| # | Wat ik nakeek | Uitslag |
|---|---|---|
| H1 | `voorraad_geld`: JA gekocht kost de prijs, een gevulde laat op JA voor a is NEE kopen voor 1 − a; per markt worden paren JA plus NEE weggestreept (samen altijd $1, terug te ruilen) tegen de gemiddelde kostprijs; wat overblijft zit vast tot de uitslag | klopt. Eigen script los van de code (FIFO in plaats van gemiddelde) op de echte vullingen: hoogste stand 1c **$438,21**, 3c **$42,38**; het rapport geeft $438 en $42,38 (GEZIEN). Mijn eerdere $476 was bruto, zonder wegstrepen |
| H2 | Vrijkomen na de uitslag | voorraad van een markt valt weg op stop + 30 uur, als GOK gelabeld. Past bij de marktregel (uitslag bij de eerste METAR van de volgende dag, uiterlijk 23:59 ET de dag erna, plus tijd om te verzilveren); in het slechtste geval later. Test `test_voorraadgeld_streept_ja_en_nee_weg_en_komt_vrij` rekent wegstrepen en vrijkomen goed na |
| H3 | Opschaling | het benodigde geld is nu gemiddelde open orders **plus** de hoogste voorraadstand, en de inleg wordt daarop begrensd. Getoetst op een nagemaakte tweede run (eigen kopie van de data, 2 uur verschoven, alleen om de opschaling te laten verschijnen): €5.000 wordt $5.000 van $5.775 nodig, dus 87%, in plaats van "alles". Het rapport zegt er zelf bij dat de voorraad groeit tot de eerste markten beslist zijn en dat het getal tot dan te laag is. Eerlijk |
| H4 | Vullingen zonder prijs 1 uur later | tellen niet meer als 0: verlies geschat met het verlies per dollar van de rest (1 uur, anders 5 minuten), als GOK gelabeld, met het aantal erbij. De dagtabel zegt "alleen vullingen met prijs 1 uur later" |
| H5 | Kan-punten | ondergrens en hoge schatting hernoemd en uitgelegd; beslisregel noemt ook "tegen de uitslag" en het geld uit orders plus voorraad; verlies per dollar apart voor hoogste (−0,73%, 61 vullingen) en laagste (+1,63%, 7 vullingen) na 5 minuten (GEZIEN, te weinig om iets te zeggen) |
| H6 | Rapport op de echte tak | `python3 platformen/ai-handel/schaduwbot/rapport.py --tak .` draait zonder fout op `ai-handel-data` (tip 0e6cf34e): 32 minuten, nog geen opschaling (die verschijnt vanaf 60 minuten), wel de nieuwe kolom voorraadgeld |
| H7 | Tests en workflow | 13 tests groen; meten 335 minuten in een job van 358, dus ±20 minuten speling voor rapport en opslaan; verder niets aan de veiligheid veranderd (geen geheimen, geen geforceerde push, alleen de tak `ai-handel-data`) |

**Kan (blijft):**
1. Zodra de eerste markten beslist zijn: de 30 uur voor vrijkomen naast de echte tijd van beslissen leggen (Gamma geeft per markt wanneer hij sloot).
2. Kortere runs (5 uur 35) met de klok op 6 uur geven wat vaker een gat tussen twee runs. Het rapport rekent per gemeten minuut, dus geen fout, alleen minder data.
3. De punten uit de eerste Kan-lijst onder 5 en 6 blijven staan voor na de 2 weken.
