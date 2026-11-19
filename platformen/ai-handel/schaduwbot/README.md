# Schaduwbot Polymarket (onderzoek voor Thijs, geen Dortus-product)

De schaduwbot toetst route 1 uit `../D-arbitrage.md`: de beloning van Polymarket pakken voor wie orders laat staan in jonge temperatuurmarkten, met het midden van het boek als prijs, en stoppen om middernacht lokale tijd op de dag zelf. Hij doet alsof hij een makerbot is en houdt bij wat die bot **had** verdiend aan beloning en **had** verloren aan vullingen. De formule en de opzet komen uit `../B-zelf-bouwen.md` (punt 30 tot 33 en 40 tot 44).

## Wat hij NIET doet
- Geen account, geen sleutel, geen wallet, geen geld. Er wordt nooit een order geplaatst of iets getekend.
- Hij doet alleen leesverzoeken op openbare adressen (`gamma-api`, `clob` en `data-api` van Polymarket). Het enige POST-verzoek is `POST /books`: een openbaar leesverzoek voor orderboeken, zonder account.
- Hij geeft geen advies. Het is meten.

## Wat hij doet
| Hoe vaak | Wat |
|---|---|
| elke 10 minuten | Alle open temperatuurmarkten (Gamma, tag `weather`, slug `highest-` of `lowest-temperature-in-<stad>-on-<datum>`) naast de beloningslijst (`clob.polymarket.com/rewards/markets/current`). Hij houdt alleen markten met een actieve beloning en een bekende stad (tijdzone van het meetstation). |
| elke minuut, op een willekeurige seconde | Het orderboek van elke markt (`POST /books`). Per markt en per variant een denkbeeldig bod en laat rond het midden, en de beloning voor die minuut met de formule van Polymarket. |
| elke minuut | Nieuwe trades (`data-api.polymarket.com/v2/trades?event_id=...`, 20 events per verzoek). Gaat een echte trade op of door de prijs van onze denkbeeldige order, dan telt dat als vulling. |
| elke 30 minuten | Ruwe metingen als gzip-CSV naar de tak `ai-handel-data` (nooit naar main). |
| aan het eind van elke run | `rapport.md` op dezelfde tak. |

### Vaste keuzes (een andere keuze is een nieuwe meting, dus niet tussendoor schuiven)
- **Grootte:** 20 aandelen per order, of meer als de markt een grotere minimale grootte eist (`rewards_min_size`, vaak 20, soms 100). Zo staat er rond de $20 per markt op het boek.
- **Twee varianten tegelijk:** `1c` (1 cent van het midden, waar B het grootste verlies per dollar mat) en `3c` (3 cent). Zo zie je het verschil tussen dicht bij het midden en verder weg in dezelfde minuten.
- **Midden:** benadering van het "size-cutoff-adjusted midpoint": de beste bied- en laatprijs waar opgeteld minstens de minimale grootte staat (GOK, de docs zeggen niet precies hoe). Orders afgerond op de tick, nooit door het boek heen.
- **Alleen strakke boeken:** beste bod en laat hooguit 5 cent uit elkaar (D run 5). Lege of losse boeken slaat hij over.
- **Stopregel:** orders weg om 00:00 lokale tijd van het meetstation op de dag waar de markt over gaat (D run 7). Daarna volgt hij het midden nog 2 uur, voor de prijs 1 uur na de laatste vullingen.
- **Voorraadrem:** nooit meer dan 2 keer de ordergrootte netto aan één kant (B punt 40); dan zet hij die kant niet meer.

### De beloning (GOK)
Per order: punten = ((v − afstand) / v)² × grootte, met v = `rewards_max_spread` in centen. Bod en laat tellen elk aan één kant; de score is het minimum van de twee kanten, en tussen 0,10 en 0,90 telt één kant ook, gedeeld door 3 (docs Liquidity Rewards). Ons aandeel in een minuut = onze score / (onze score + die van de anderen). De score van de anderen kun je uit het openbare boek niet precies halen (je ziet niet wie wat heeft staan), dus hij schrijft twee schattingen weg (B punt 32):
- **ondergrens (laag):** alle orders in het boek tellen, beide kanten opgeteld (de anderen zo sterk mogelijk). Ons echte aandeel is nooit kleiner (bij het geschatte midden);
- **hoge schatting (hoog):** alleen prijsniveaus met minstens de minimale grootte, met de regel van het minimum (de anderen zo zwak als redelijk). Dit is geen harde bovengrens: een niveau kan uit kleine orders bestaan die niet tellen (keuring A4).

Beloning per minuut = dagbedrag / 1440 × aandeel. De echte beloning ligt waarschijnlijk tussen de ondergrens en de hoge schatting.

### Vullingen en verlies (GEZIEN)
- Een trade van een nemer wordt omgerekend naar de JA-kant (NEE kopen voor q = JA verkopen voor 1 − q).
- **Los:** de trade gaat op of door onze prijs. **Streng:** de trade gaat er echt doorheen (dan was het hele niveau op, dus ook wij). Beide worden opgeslagen; de wachtrij voor ons is onbekend.
- Verlies per vulling: tegen het gemeten midden **1 uur later**, en tegen de **uitslag** (0 of 1, opgehaald zodra de markt beslist is). Daar zit de winst op de spread al in. Makers betalen geen kosten op Polymarket.

## Hoe je het rapport leest
Het nieuwste rapport staat op de tak: `https://raw.githubusercontent.com/<eigenaar van deze repo>/dortus-hq/ai-handel-data/dag/rapport.md` (de korte proef: `proef/rapport.md`). Zelf maken:
```
python3 platformen/ai-handel/schaduwbot/rapport.py --tak .          # haalt de tak op en drukt het rapport af
python3 platformen/ai-handel/schaduwbot/rapport.py <map>            # vanaf een map met dag/<datum>/...
```
- **Per dag en totaal**, per variant: gemeten minuten, gemiddeld aantal markten en geld in open orders, hoogste stand van het geld in gevulde voorraad, beloning ondergrens tot hoge schatting (GOK), vullingen los en streng, gevuld bedrag, resultaat 1 uur later en tegen de uitslag (GEZIEN), en netto.
- **Verlies per gevulde dollar:** vergelijk met B (−1,05% voor alle makers binnen 1 cent) en D (−0,1 tot −0,3% in temperatuurmarkten). Dit is het getal waar de route op staat of valt.
- **Opgeschaald (GOK):** netto per dag = gemeten netto × 1440 / gemeten minuten. Vullingen die nog geen prijs 1 uur later hebben tellen niet als 0: hun verlies wordt geschat met het verlies per dollar van de andere vullingen, en het rapport zegt hoeveel het er zijn. Het geld dat de bot nodig had = gemiddeld geld in open orders **plus** de hoogste stand van het geld dat vastzit in gevulde voorraad tot de uitslag (JA en NEE per markt tegen elkaar weggestreept, vrij ±30 uur na het begin van de dag, GOK). Bij een inleg van €2.000 of €5.000: lineair naar dat geld, maar nooit erboven (meer geld in dezelfde markten geeft geen evenredig grotere beloning). De voorraad groeit tot de eerste markten beslist zijn, dus de eerste 2 tot 3 dagen is het benodigde geld te laag en de opbrengst per euro te hoog. Koers standaard 1 $ per € (GOK; geef `--koers` mee).
- **Met weinig geld (€100, €150, €200, GOK):** bovenaan staat "Met €150: netto ... per dag". Een kleine inleg staat maar in een paar markten tegelijk: per markt is de ordergrootte nodig (minimale grootte van die markt, vaak 20 aandelen, soms 100, op de tick van de markt) plus ruimte voor voorraad tot de rem. Twee keuzes: gemiddelde markten, en achteraf de markten met de hoogste beloning per dollar (te mooi). Onder $1 beloning per dag betaalt Polymarket niets uit; het rapport zegt dat erbij.
- **Per markt** (beste en slechtste 10) en **per stad**.
- **Beslisregel (vooraf vast, B punt 27 en 40):** na 2 weken meten alleen verder kijken als de beloning (**ondergrens**) min het verlies op de dagen positief is, zowel **1 uur later** als **tegen de uitslag** (de bot houdt zijn voorraad tot de uitslag, dus dat is het echte resultaat), en het **slechtste dag-resultaat** te dragen is met het geld uit orders plus voorraad. Is alleen de hoge schatting positief: niet doorgaan.

## Wanneer het rapport zinvol is
- Na 1 run (5 uur 35) zie je of het draait en de grootte van de beloning; het verlies is dan nog ruis (weinig vullingen, uitslagen nog niet bekend).
- Na 2 tot 3 dagen zijn de eerste markten beslist en is het verlies tegen de uitslag te lezen.
- Na 2 weken is er genoeg voor de beslisregel hierboven.

## Waar de data staat
Tak `ai-handel-data`, map `dag/<UTC-datum>/` (proef: `proef/`). Per run elk half uur nieuwe stukjes, nooit overschreven:
| Bestand | Inhoud |
|---|---|
| `beloning-<run>-<nr>.csv.gz` | per UTC-uur, markt en variant: gemeten minuten, minuten met bod en laat, beloning hoog en laag, som van het aandeel, som van het geld op het boek |
| `vullingen-<run>-<nr>.csv.gz` | elke denkbeeldige vulling: tijd, markt, variant, kant, onze prijs, aantal, midden, streng, prijs en grootte van de trade, voorraad erna |
| `midden-<run>-<nr>.csv.gz` | het midden, beste bod en beste laat per markt, alleen als het veranderde |
| `minuut-<run>-<nr>.csv.gz` | per minuut en variant: aantal markten, geld op het boek, beloning hoog en laag |
| `meta-<run>-<nr>.json` | instellingen en per markt: conditie, token, event, vakje, stop, dagbedrag, v, minimale grootte |

Markt-sleutel = teken 3 tot 12 van de condition id.

## Hoe het draait
`.github/workflows/schaduwbot.yml`: runs van 5 uur 35 (job-limiet 358 minuten, dus ruim tijd voor het rapport), één tegelijk. GitHub laat het schema in deze repo vaak vallen, dus net als het dashboard start hij ook bij elke push naar main; de klok (`organisatie/controle/klok.py`, naam `schaduwbot`, 6 uur) geeft hooguit elke 5,5 tot 6 uur een beurt en een nieuwe run wacht tot de vorige klaar is. Een korte proef start je met een opdrachtbestand (skill `actions`): `{"workflow": "schaduwbot.yml", "invoer": {"duur": "10"}, ...}`; die schrijft naar `proef/` en telt niet mee. Openbare repo, dus GitHub Actions kost niets.

Lokaal: `python3 schaduwbot.py --duur 10 --uit /tmp/uit` (zonder `--git` schrijft hij alleen bestanden). Tests: `python3 -m unittest test_schaduwbot.py`. Alleen standaardbibliotheek.

## Grenzen en risico's (eerlijk)
- **Verboden vanuit Nederland.** De voorwaarden van Polymarket noemen Nederland: inwoners mogen niet handelen, ook niet via de API, en een VPN gebruiken om dat te omzeilen is verboden (KEURING.md, claim 7). De Kansspelautoriteit verbood Polymarket (dwangsom €420.000 per week voor de aanbieder). Een gokovereenkomst met een aanbieder zonder vergunning is in Nederland nietig: een bevroren saldo is niet af te dwingen. Deze bot meet alleen; hij zegt niets over of je het mag.
- **Belasting.** Winst bij een online kansspel zonder Nederlandse vergunning: zelf aangifte kansspelbelasting doen, 37,8% in 2026 (KEURING.md, claim 13 en 14). Of een beloning voor liquiditeit daaronder valt, is onbekend: vraag een belastingadviseur voordat er echt geld in gaat.
- **De beloning is een schatting.** Het aangepaste midden, de scores per maker en de willekeurige seconde van Polymarket zijn niet openbaar. Echte andere bots reageren op een nieuwe order; een schaduw doet dat niet.
- **Vullingen.** De wachtrij is onbekend (daarom los en streng). Trades staan 1 tot 2 minuten later in de Data API, dus de voorraadrem reageert te laat. Een echte bot wordt soms ook gevuld als hij zijn order net wilde weghalen; dat ziet de schaduw niet.
- **Kleine steekproef in het begin.** Eén dag zegt weinig; één omslaande markt kan een dag bepalen (B punt 40).
- Dit is meten, geen advies.
