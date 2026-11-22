# Ontwerp kansenradar (19 nov 2026)

**Wat en voor wie:** een meting voor Thijs: leveren drie zeldzame momenten (nieuwe noteringen, funding-pieken,
stablecoins naast hun koppeling) na alle kosten geld op, ook met een kleine inleg? **Af** = de workflow draait 4
keer per dag ±5,5 uur, de data staat op de tak `ai-handel-data` in `radar/`, `radar_rapport.py` maakt er per hoek
per dag het aantal momenten, mediane winst, duur, MiCA en grijs apart en een som bij €100 tot €5.000 van, en de
tests zijn groen.

## Drie aanpakken
1. **Drie losse scripts en workflows.** Eenvoudig per hoek, maar drie keer de lijsten met paren en de
   opnamestatus ophalen, drie workflows en drie klokken. Meer verzoeken bij dezelfde beurzen. Valt af.
2. **Websockets per beurs.** Sneller (we zouden noteringen en afwijkingen binnen een seconde zien), maar 15 tot 24
   protocollen en veel langer bouwen dan de ±2 uur. De vraag is of deze momenten bestaan en hoe lang ze duren;
   als ze minuten duren, ziet een meting per 15 seconden ze ook. Valt af, staat bij "wat hij niet ziet".
3. **Gekozen: één lus met drie ritmes.** Eén script, één workflow, één klok. Lijsten met paren, opnamestatus en
   minima worden gedeeld door A, B en C. Elke hoek heeft zijn eigen ritme (3 minuten, 2 minuten, 15 seconden), en
   zware verzoeken (orderboeken) alleen waar de goedkope blik (ticker) iets laat zien. Hergebruik van
   `../scanner/beurzen.py` en de rekensom van de scanner (`vul`, `bereken`, opname- en netwerkstatus), zodat A en
   C1 op precies dezelfde manier rekenen als de scanner. De bestanden van de scanner worden alleen gelezen.

## Keuzes
- **Noteringen:** een munt die de beurs nog nooit had (ook niet in de lijst van de vorige run, die op de datatak
  staat). Een munt die even weg was en terugkomt, telt niet. Meer dan 25 nieuwe munten tegelijk of een lijst die
  ineens half zo groot is: storing, niet tellen. Alleen dezelfde quote vergelijken (zoals de scanner).
- **Funding:** in- en uitstap met een marge (in boven 0,1%, uit onder 0,05% per 8 uur), uitstappen pas na minstens
  één verrekening. Zonder die regels gaf de proef bij perps die elk uur verrekenen tientallen "pieken" van 2
  minuten die alleen kosten waren (de voorspelde rate schommelt per minuut). Verrekening = het tijdstip van de
  volgende verrekening schuift op; dan telt de laatste rate van daarvoor.
- **Spot bij funding:** dezelfde beurs als die de munt heeft, anders de laagste takerkosten. Prijscontrole (5%, of
  een macht van 10) om een andere munt met dezelfde naam of een aandeel-token uit te sluiten.
- **Stablecoins:** eerst de bulk-ticker (één verzoek per beurs), orderboek alleen bij een afwijking of gat, hooguit 4
  per beurs per ronde. Eerste versie haalde elke 15 s alle 160 boeken; dat was 38 boeken bij Kraken per 15 s, boven
  hun limiet van ±1 per seconde.
- **Kleine inleg:** op verzoek van Thijs (via de hoofdchat) ook €100, €150, €200, met de minimale bedragen uit de
  API's. Onbekend minimum telt bij een kleine inleg niet mee (voorzichtig), wel apart getoond.
- **Rapportnaam** `radar_rapport.py`: `../scanner/scanner.py` zet zijn eigen map vooraan in het zoekpad, dan zou
  `import rapport` het rapport van de scanner pakken.
- **Opslaan** zoals de scanner: verse clone per poging, gewone push, nooit geforceerd, eigen map `radar/`.

## Bekende grenzen
Stap van 15 seconden tot 3 minuten (snellere partijen zijn eerder); perp-diepte niet gemeten (laatste prijs);
overmaaktijd niet gemeten; minima en opnamestatus niet bij elke beurs openbaar; perp-takerkosten GOK; perps voor
EU-particulieren niet per beurs nagekeken. Alles staat in README.md.

## Na de keuring (19 nov, KEURING.md, akkoord nee)
- B: een ontbrekende spotkoers is geen "andere munt" meer; de piek wacht op een koers en staat anders als "onbekend"
  apart. Overmaken (één opname van USDT of USDC) telt mee als spot en perp op twee beurzen zitten.
- B: open pieken gaan via `pieken-open.json` op de datatak naar de volgende run; geen doorgeknipte pieken meer die
  twee keer kosten betalen. Gekozen boven "doorgeknipte pieken apart zetten", omdat pieken die langer dan een run
  duren juist de interessante zijn. De 27 doorgeknipte pieken uit de eerste uren staan apart in het rapport en tellen
  niet mee (de rest van zo'n piek is niet gevolgd, dus niet na te rekenen).
- C2 meet tegen een basislijn (mediaan per dag over 45 dagen uit de OHLC-API), niet tegen 1 dollar of 1 euro.
- Rapport: sommen met één pot (geen geld dat tegelijk op tien plekken zit), een zin per hoek bovenaan, komma's.
- Kraken-taker via `beurzen.taker_standaard` (0,80%, stablecoin- en FX-paren 0,20%); oude data apart.
- Klok start alleen op code (`*.py`, `*.sh`, de workflow, `beurzen.py` en `scanner.py`), niet op teksten.
- `radar.py` gesplitst in `radar.py`, `rekenen.py`, `hoek_a.py`, `hoek_b.py`, `hoek_c.py` en `basislijn.py`.
- Gate perp-taker 0,075% (GEZIEN in de API).

