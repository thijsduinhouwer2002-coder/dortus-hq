# Keuring blender-gewrichten, 23-11-2026, automatische keurder
Wat ik keurde: commits f9391c8..2a79af9 (alleen `uitslag.md` en twee jpg's in `proeven/studio-figuren-2026-11-23/`)
Akkoord: ja

## Deel A: doet het wat beloofd is?
Er is geen add-on-code veranderd, alleen een proefverslag en twee beelden. Ik toets daarom of het verslag klopt met zichzelf en past bij de belofte in `ontwerp.md`.

| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De add-on is ongemoeid: geen wijziging in de add-on, dus 0.1.1 en 1.0.2 blijven gelden. | Feit (lijst gewijzigde bestanden) | hoog | `git diff` op `click_joints/` is leeg |
| 2 | De aantallen in de tabel kloppen onderling (adventurer 4 = ellebogen en knieën, knight 3 = twee ellebogen en één knie, robot 0). Bij king staat 4, maar knieën, nek en schouders vallen weg. Dan moeten het ellebogen en heupen zijn, en de heupen worden niet genoemd. | Vermoeden | midden | `kandidaten.txt` van release `studio-1` |
| 3 | De bronnen (`kandidaten.txt`, logs, `figuur-a-meting.json`) en de twee jpg's zaten niet in wat ik kreeg. "GEZIEN, alles gelezen" kan ik niet bevestigen. | Vermoeden | laag | Release `studio-1` openen en de tabel ernaast leggen |
| 4 | De drie voorstellen (volgende kandidaat bij "no watertight parts", een NECK-zin, de tip bij "cheek too stiff") passen bij de belofte dat de add-on altijd een heldere reden geeft. De NECK-zin is het sterkst onderbouwd: 4 van 6 figuren hebben "not placed" zonder reden. | Feit (tekst) | midden | Bram bouwt het en de studio draait opnieuw |
| 5 | Het verslag zegt zelf dat de stand van het filmfiguur veranderd is door studio f9391c8 (9 gewrichten, "nog niet zelf gezien"). De uitslag voor figuur a is dus mogelijk al verouderd. Dat is eerlijk gemeld. | Feit | hoog | Een nieuwe studio-run na f9391c8 |

## Deel B: houdt het zich aan onze regels?

| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Er is niets in tests aangepast om te slagen. | Feit | hoog | Tests niet aanpassen om te slagen |
| 2 | `uitslag.md` is 39 regels. | Feit | hoog | Bestanden onder ±400 regels |
| 3 | `architectuur.md` is niet bijgewerkt. Dat hoeft niet, want de code is niet veranderd. | Feit | hoog | architectuur.md bijgewerkt |
| 4 | Geen persoonsgegevens of sleutels in de diff. | Feit | hoog | Geen persoonsgegevens |
| 5 | Veel beweringen hebben GEZIEN, GOK of "nog niet zelf gezien". Een paar niet: "zo'n knie breekt bij het printen" (punt 5), "in elk filmpje mist nu een schouder" en de verwijzing naar spacetrooper1. | Feit | midden | Cijfers met GEZIEN/DERDEN/GOK |
| 6 | De beelden zijn studio-opnames van figuren. Ik kan niet zien of er AI-beeld in zit, en het gaat niet naar Steam. | Vermoeden | laag | Geen AI-beeld of -geluid op Steam |

## Deel C: zou een gebruiker het leuk en fijn vinden?
Ik kan de beelden niet zien. Dit zijn vermoedens uit de tekst.

| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | Een koper met een figuur zonder schouder (linkerschouder valt weg) zal denken dat de add-on halfwerk levert. Een tweede poging op een andere plek zou dat opvangen. | Voorstel 1 van Bram uitvoeren | midden |
| 2 | "Neck (not placed)" zonder reden voelt stroef en geeft de koper geen weg vooruit. | Een NECK-zin met de reden en de tip om met de hand te plaatsen | klein |
| 3 | De tip "Try a thicker spot" bij dikke ledematen stuurt de koper de verkeerde kant op. | De tip herschrijven | klein |
| 4 | Voor promotiefilmpjes is alleen het makehuman-figuur bruikbaar. Verder zijn er vooral ellebogen en knieën, en de robot valt af. Dat is weinig variatie. | Meer figuren met lange armen testen | midden |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Na studio f9391c8 de uitslag voor figuur a opnieuw draaien en de tabel bijwerken (8 van 9 wordt waarschijnlijk 9).
- Bij king uitleggen welke 4 gewrichten er zijn.
- Bij de claim over de wand onder 1 mm (medieval) een label GOK of GEZIEN zetten.
- De licentie (CC0 of niet) van de Quaternius- en makehuman-modellen noemen, voordat ze in filmpjes of op een winkelpagina komen.
- `figuur-a-staand-pose.jpg` wordt in de tekst niet genoemd. Noem het, of haal het weg.

---
Automatische keurder, model `claude-sonnet-5-5`, 19387 tokens in, 3728 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
