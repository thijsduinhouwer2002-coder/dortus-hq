# Keuring YouTube-titels Pro (#345), 28-11-2026, automatische keurder
Wat ik keurde: commits 250a529..5824048 (5824048bf): `producten/blender-gewrichten/KAART.md` en `vindbaar/youtube-titels-345.md`
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | Beide titels beginnen met het zoekwoord ("Ball Joints", "Hinges") en eindigen op "Click Joints Pro", zoals de opdracht vraagt. | Feit | Hoog | Staat zo in de tabel van het plakbestand. |
| 2 | De opgegeven lengtes kloppen: ik tel 97 en 83 tekens, onder de grens van 100. | Feit | Hoog | Zelf geteld uit de tekst. |
| 3 | "Stops at 115°" past bij het ontwerp: het scharnier met eindstop is betaald en heeft 0 tot 115°. "One Button from Your Rig" past bij "Figure from rig". | Feit | Midden | De code of het werkende scharnier. De wijziging laat dat zelf niet zien. |
| 4 | De plakstappen zijn compleet: waar, wat, en hoe je daarna met RSS nakijkt en na 3 dagen opnieuw meet. | Feit | Hoog | Alleen te bevestigen door het echt uit te voeren. |
| 5 | De nulmeting (plek 15 van 15, niet in de lijst, geen van beide in de eerste 16) kan ik niet narekenen. Er is geen ruwe uitvoer van `meet.py` bijgevoegd. | Vermoeden | Midden | De uitvoer van `organisatie/lat/vindbaar/meet.py` bij de #345-meting. |
| 6 | De wijziging noemt Daans akkoord (#335) en de miniatuur (#346, blinde test GESLAAGD). Beide staan in berichten die ik niet zie. Het miniatuurbestand zit niet in deze wijziging. | Vermoeden | Midden | De berichten #335, #346 en #349, en het bestand `yt-pro-r2-1280x720.jpg`. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Alleen tekstbestanden. Er is geen code gewijzigd, dus er zijn geen tests of architectuurbijwerking nodig. | Feit | Hoog | Tests niet aangepast, architectuur.md |
| 2 | Er staan geen persoonsgegevens of sleutels in. Het kanaal-id in de RSS-URL is openbaar. | Feit | Hoog | Geen persoonsgegevens |
| 3 | De cijfers dragen het label GEZIEN, ook de lengtecontrole (met Python). | Feit | Hoog | Cijfers met GEZIEN/DERDEN/GOK |
| 4 | Er is geen spelerstekst van Hats en geen AI-beeld of -geluid voor Steam. | Feit | Hoog | Hats-regel, Steam-regel |
| 5 | De tijden spreken elkaar licht tegen: de keuring is van 06:12, maar de wijziging zegt "±06:20" en meting "06:15". | Feit | Hoog | Alleen een administratiepuntje |

## Deel C: zou een gebruiker het leuk en fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | Beide titels lopen tegen de 100 tekens aan. In zoeklijsten op een telefoon wordt het einde vaak afgekapt. Dan blijft het onderdeel dat ze het meest laat opvallen ("One Button from Your Rig", "Stops at 115°") niet altijd zichtbaar. | Laat het kernvoordeel in de eerste ±60 tekens staan. | Klein |
| 2 | De titels bevatten veel zoekwoorden naast elkaar ("3D Printed Action Figures in Blender"). Dat leest iets minder prettig dan een korte zin. | Test na de meting van 3 dagen een kortere variant. | Klein |

## Deel C: is het goed genoeg?
| Vraag | Cijfer 1 tot 10 | Waarom, en waarmee vergeleken |
|---|---|---|
| Ziet het er top uit, op het niveau van de beste in de winkel? | Niet te geven | Ik zie alleen tekst en heb geen titel van een concurrent met link om naast te leggen. Vermoeden: duidelijk, maar zwaar met zoekwoorden. |
| Zou ik het zelf kopen of bekijken op basis van dit? | Niet te geven | Dezelfde reden. De titel zegt wel direct wat het is en voor wie. |
| Zou Thijs er trots op zijn? | Niet te geven | Dat kan ik uit tekst niet inschatten. Daan keurde de titels volgens de wijziging al. |

Ik geef hier geen cijfers, omdat ik ze niet kan onderbouwen. Het is een plakbestand met een nulmeting en geen nieuw beeld. De blinde test geldt voor beelden en valt hier niet onder.

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
1. Voeg de ruwe uitvoer van `meet.py` toe, of een verwijzing ernaar, zodat de nulmeting naast de meting van over 3 dagen te controleren is.
2. Zet de kernzin van elke titel vooraan, zodat afkappen op een telefoon niets verliest (deel C, punt 1).
3. Leg na het plakken de meting van 3 dagen later in #345 vast, vergelijk met de nulmeting en vergelijk de titels met de top 3 voor "ball joint blender addon".
4. Controleer of `yt-pro-r2-1280x720.jpg` echt in de repo staat. In deze wijziging zit het niet.
5. Maak de tijden in KAART.md en het plakbestand gelijk aan het echte moment.

---
Automatische keurder, model `claude-sonnet-5-5`, 20063 tokens in, 4130 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
