# Ontwerp driehoek-meter (19 nov 2026)

**Wat en voor wie:** een meting voor Thijs: bestaan er binnen één beurs driehoeken (bijv. EUR naar BTC naar ETH
naar EUR) die na drie keer takerkosten winst geven, minstens €100 diepte hebben en een paar seconden blijven
staan? **Af** = de workflow draait 4 keer per dag ±5,5 uur tot en met 27 nov 2026, de data staat op de tak
`ai-handel-data` in `driehoek/`, `rapport.py` maakt er per dag en totaal echte driehoeken, mediane winst, beste
driehoeken per beurs en een GOK-som voor €2.000 en €5.000 van (MiCA en grijs apart), en de tests zijn groen.

## Drie aanpakken
1. **Elke ronde alle orderboeken van alle driehoeken.** Op Kraken en OKX zijn dat ±1.200 driehoeken met
   honderden paren: honderden verzoeken per paar seconden. Daar gaan de grenzen van de openbare API overheen.
   Valt af.
2. **Websockets per beurs.** Snelst (milliseconden), maar 8 verschillende protocollen en lang bouwen. Te groot
   voor deze opdracht.
3. **Gekozen: middenweg, zoals de scanner.** Per beurs een eigen draad met een eigen ritme (3 tot 5 seconden).
   Elke ronde één verzoek voor bod en laat van alle paren (bulk-ticker). Daarmee rekent hij elke driehoek in
   beide richtingen door tegen de beste prijzen met de takerkosten. Een driehoek die met de beste prijzen al
   verlies geeft, geeft met het boek ook verlies (verder in het boek wordt de prijs alleen slechter). Alleen voor
   de driehoeken die met de beste prijzen winst geven, haalt hij de drie orderboeken op en loopt ze af. Een
   budget per beurs per ronde (3 tot 10 boeken) houdt het binnen de grenzen; open driehoeken gaan voor.

## Keuzes
- Hergebruik: de koppelingen van `../scanner/beurzen.py` (zelfde paren, ticker, boek, takerkosten uit de API).
  De scanner kijkt alleen naar USDT, USDC, EUR en USD als quote; de meter zet die grens open, zodat ook paren
  als ETH-BTC meedoen.
- Kosten per stap: takertarief (laagste trede). Waar het tarief onzeker is (Bitvavo categorie B, C, D: "lager"
  volgens Bitvavo, maar geen getal), rekent hij twee keer: **hoog** (0,25%, het maximum dat Bitvavo noemt) en
  **laag** (0%, "zelfs als het gratis was"). Het rapport telt met hoog; laag staat apart als bovengrens.
- Kraken: 0,80% taker op cryptoparen, 0,20% op FX-, stablecoin- en pegged-token paren (TBTC/BTC, WBTC/BTC),
  0,01% op USDG-paren en 0% op alle USDe-paren (GEZIEN, kraken.com/pro/fees, 19 nov). Bitstamp 0,40%, op FX- en
  stablecoinparen 0,08% (DERDEN, TradingView). OKX 0,10% (DERDEN, okx.com/en-eu/fees); de lijst met 0%-paren van
  OKX staat niet in de pagina, die rekenen we niet mee (te somber op die paren).
- Een driehoek opent als het boek winst na kosten geeft en sluit als de ticker of het boek dat niet meer geeft.
  Duur = laatste keer winst min eerste keer winst; resolutie = het ritme van die beurs (3 tot 5 s). Eén keer
  gezien = 0 s.
- **Echt na de keuring (moet 1):** pas echt als twee metingen die minstens 3 seconden uit elkaar liggen (en alle
  metingen daartussen) elk minstens €100 diepte met winst hadden, en de latere meting minstens €0,05 winst gaf.
  Alle bedragen in het rapport zijn die van die latere meting (wat er na 3 seconden nog stond), niet van het beste
  moment. Code: `volgen.py` (bevestigd), grenzen ook in `rapport.py` (dat draait met python3 -I).
- **Eén kans, niet vier (moet 2, herkeuring H3):** driehoeken worden één kans als ze op dezelfde beurs zitten,
  binnen 5 seconden van elkaar bevestigd werden (rond het moment na 3 seconden, niet over de hele open-tijd) en
  een paar delen dat geen paar van twee hoofdmunten is (EUR, USD, USDT, USDC, BTC, ETH). Geen ketting: de beste
  begint een groep, een andere driehoek komt erbij alleen als hij met elk lid dezelfde kans is (`kans.py`). Het
  rapport zet ernaast de som met elke driehoek los (bovengrens); samengevoegd is de ondergrens.
- Diepte in euro: hij rekent de winst uit bij ±45 bedragen van €10 tot ±€75.000 (stappen van 25%, plus €100,
  €150 en €200). Diepte = het kleinste bedrag waarmee je 99% van de hoogste winst pakt (meer erin levert niets
  meer op). Ook de winst bij €100, €150, €200, €500, €1.000, €2.000, €5.000 en €10.000 (je mag minder inleggen als
  dat meer oplevert). Het opgehaalde boek is 20 tot 50 niveaus: diepte is een ondergrens.
- Minimale ordergrootte en stapgrootte per paar komen uit de API (Bitvavo, Kraken, OKX, KuCoin, Gate, Bitget,
  MEXC, Bitstamp). Een bedrag telt alleen als alle drie orders het minimum halen; het aantal munten wordt per order
  naar beneden afgerond op de stapgrootte (wat niet rondgaat, blijft liggen). Bitvavo rondt de kosten in euro naar
  boven af op de cent: €0,01 extra per euro-order. Per beurs staat in `beurs-<naam>.json` hoeveel
  driehoeken met €100, €150 en €200 mogelijk zijn (vraag van Thijs: wat doet het met weinig geld?).
- Winst boven 5% per rondje is verdacht (dode markt of foute ticker); die telt niet als echt en staat apart.
- Euro: de begin-munt (EUR als die in de driehoek zit, anders USDT, USDC, USD, BTC, ETH) omgerekend met de
  middenkoers op dezelfde beurs, of via de koersen van Kraken en Bitvavo.
- Coinbase doet niet mee: geen openbare bulk-ticker met bod en laat (alleen de laatste prijs) en 1,20% taker
  (GOK), dus drie stappen kosten al 3,6%. Bybit en Binance antwoorden niet vanaf onze server.
- Opslaan zoals de scanner: verse clone per poging, gewone push, eigen map `driehoek/` op `ai-handel-data`.
- Na 27 nov 2026 slaat de workflow het meten over (een week); verlengen = de datum in de workflow aanpassen.

## Bekende grenzen
Wij meten elke 3 tot 5 seconden. Snelle partijen pakken een driehoek meestal binnen milliseconden; wat wij zien
is wat er overbleef. Een driehoek die korter dan een ronde stond, zien we vaak niet. De API is de wereldwijde
versie, niet altijd de EU-versie met vergunning. Bitstamp is gratis onder $1.000 handelsvolume per 30 dagen
(DERDEN); dat rekenen we niet mee, want het geldt maar voor een paar driehoeken.

## Bestanden en waarom zo gesplitst (keuring B1)
`kosten.py` (tarieven, minimum, stapgrootte, vergunning), `reken.py` (driehoeken zoeken, beste prijs, boek
aflopen), `volgen.py` (een driehoek volgen en bevestigen), `kans.py` (echt en samenvoegen), `driehoek.py` (de draden per beurs en het
wegschrijven), `rapport.py` (los, draait met python3 -I). Elk onder de 400 regels.

## Herstart en opslaan (na de keuring)
De klok start de vaste run alleen opnieuw bij een push die code raakt (`*.py`, `opslaan.sh`, de workflow, en
`../scanner/beurzen.py`, omdat dat de koppelingen en een deel van de kosten bepaalt), niet bij tekst (README,
KEURING.md). Na een stopsignaal wacht de meter hooguit 5 seconden op de draden en schrijft dan
alles weg; GitHub stopt een afgebroken stap na ±10 seconden hard, en de opslaan-stap draait daarna altijd.
