# Keuring galerijbeeld 3 Click Joints Pro 'Every joint knows its limit', 25 nov 2026, Daan
Wat ik keurde: `ontwerp/pro-galerij/beelden/bereik-2400x1200.jpg` en `bereik-1920x1080.jpg` (main), naast Cleave 'Connectors that fit' (met curl opgehaald en met Read bekeken).
**Akkoord: ja** (Superhive meteen; Gumroad na één kleine fix, zie Moet).

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid |
|---|---|---|---|
| 1 | Vier kaartjes kloppen met `bereik.json` (nek ball ±20°, schouder ball ±30°, elleboog hinge 0–140°, knie hinge 0–120°) | feit | hoog |
| 2 | 0.20 mm klopt met de standaard speling in de add-on (`cj_speling_mm` 0.2 in `afstand.py`, `maat.py`) | feit | hoog |
| 3 | Blinde test GESLAAGD (Gemini 2,0, ChatGPT 1,0), uitslag in `organisatie/blindtest/uitslag/click-joints-pro-galerij-knie-2026-11-25-0859.md` | feit, GEZIEN | hoog |
| 4 | Geen printfoto, geen bewering over printen of klikken. "it can't bend past the limit of your rig" gaat over het ontwerp van het scharnier (eindstop), dat is wat Pro maakt | feit | hoog |

## Deel B: regels
| # | Bevinding | Regel |
|---|---|---|
| 1 | Geen AI-beeld (render uit Figure from rig), geen persoonsgegevens, geen AI genoemd | in orde |
| 2 | In `bereik.json` staat linkerheup ±22° en rechterheup ±30°: niet in beeld, dus niet erg, maar kijk of de preset van de heup echt gespiegeld is voor een volgend beeld | vermoeden, laag |

## Deel C: zou een koper het fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | Groot verschil met ronde 1 en 2: één figuur, vier gewrichten van twee soorten, meteen duidelijk wat Pro doet. Cleave laat kubussen zien, wij een figuur | niets | |
| 2 | Het kaartje met de knie van dichtbij leest pas na de tekst: afgesneden been, het scharnier is klein en het gele stopje valt weg tegen het oranje | volgende keer: iets verder uitzoomen, gradenboogje of pijl bij de stop | midden |
| 3 | Gumroad 1920x1080: "0.20" staat aan het eind van een regel en "mm clearance" op de volgende. Getal en eenheid los van elkaar oogt slordig | vaste spatie tussen 0.20 en mm, of de regel anders afbreken | klein |

## Deel C: is het goed genoeg?
| Vraag | Cijfer | Waarom, en waarmee vergeleken |
|---|---|---|
| Top, op het niveau van de beste? | 8 | Rijker en specifieker dan [Cleave 'Connectors that fit'](https://assets.superhivemarket.com/store/productimage/1385307/image/xlarge-217a3e0da44f8801d1e83b7bcbae19f5.jpg); Cleave is strakker in opbouw, wij hebben het mooiere onderwerp. Het knie-kaartje houdt een 9 tegen |
| Zou ik het kopen op basis hiervan? | 8 | Ik zie in één blik welke gewrichten ik krijg en met welk bereik |
| Zou Thijs er trots op zijn? | 8 | Echt een mooi stuk techniek, rustig, geen ruis |

## Moet
- Gumroad-versie: 0.20 en mm op één regel. Geen nieuwe keuring nodig; zelf kijken (Read) en dan klaar om te plakken.

## Kan
- Knie-kaartje leesbaarder (Deel C punt 2), heupwaarden in de json nakijken.

Superhive-versie mag zo naar de hoofdchat als klaar om te plakken.

Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.
