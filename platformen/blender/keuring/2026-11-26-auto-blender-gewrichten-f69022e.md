# Keuring blender-gewrichten Check parts (label Wall), 26-11-2026, automatische keurder
Wat ik keurde: commit f69022edf (b6da2e5..f69022e), `check_delen.py`, `KAART.md`; de twee schermbeelden in `keuring/` kreeg ik niet te zien
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De code-wijziging is één regel: het label van het veld voor de wanddrempel gaat van "Min wall" naar "Wall". Er is geen logica veranderd. | Feit (uit de diff) | Hoog | n.v.t. |
| 2 | Het label past nu in de smalle zijbalk. De commentaarregel zegt dat "Min wall" werd afgekapt tot "Min w..." op plaatje 20 in 5.3.0. | Vermoeden | Midden | Het plaatje `check-parts-paneel-5.3.0.png` met Read bekijken: staat "Wall" er volledig op, naast de knop? |
| 3 | In de zijbalk staat ook de uitvoerregel "Wall: 1.62 mm" (gemeten wand). Het invoerveld heet nu ook "Wall", dus twee verschillende dingen hebben dezelfde naam. | Vermoeden | Midden | Op het paneelplaatje zien of invoerveld en uitvoerregel dicht bij elkaar staan, en of de tooltip "Minimum wall" zegt. |
| 4 | De KAART-regel zegt dat Check parts niet in 1.2.9 zit en pas na de uitgave van 1.2.9 wordt samengevoegd. Dat past bij de tak en de opdracht. | Feit (tekst) | Hoog | n.v.t. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Geen test aangepast. Alleen een label en een kaartregel veranderden. | Feit | Hoog | Tests niet aanpassen om te slagen |
| 2 | Het e2e-resultaat (run 45720771384 op b6da2e5, groen in 4.2.23, 5.2.3 en 5.3.0) staat als GEZIEN in KAART.md. Het is niet gedraaid op f69022e, de commit met de labelwijziging. Een toets die op de labeltekst controleert, zou dus nog niet gedraaid zijn. | Vermoeden | Laag | Cijfers met GEZIEN/DERDEN/GOK |
| 3 | `architectuur.md` is in deze wijziging niet bijgewerkt. Ik zie niet of Check parts er al in staat, want mijn uittreksel is afgekapt. Bij het samenvoegen controleren. | Vermoeden | Laag | architectuur.md bijgewerkt |
| 4 | Geen persoonsgegevens, sleutels of wachtwoorden in de wijziging. Het bestand blijft zoals het was; de omvang van `check_delen.py` kan ik niet zien, de wijziging begint pas bij regel 247. | Feit | Hoog | Geen persoonsgegevens, bestanden onder ±400 regels |
| 5 | Check parts staat in `betaald/`, dus niet in de gratis build en niet in de gratis CHANGELOG. Dat past bij het ontwerp. | Feit | Hoog | Gratis en betaald gescheiden |

## Deel C: zou een gebruiker het leuk en fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | Een volledig leesbaar label is beter dan een afgekapt "Min w...". Dat is een kleine winst, als het plaatje dat bevestigt. | Een tooltip "Minimum wall thickness (mm)" op het veld, zodat "Wall" alleen niet vaag blijft. | Klein |
| 2 | Invoer en uitvoer heten allebei "Wall". | Het veld "Min wall" laten staan en de zijbalk iets breder laten tekenen, of het veld "Wall min" noemen. | Klein |

## Deel C: is het goed genoeg?
Ik zag geen beelden. Daarom geef ik geen cijfers voor "top op het niveau van de beste" en "zou ik het kopen"; die zijn aan Daan, zoals KAART.md al zegt (keuring Daan open). Het is ook geen beeld dat een klant als eerste ziet, dus de blinde test geldt niet.
| Vraag | Cijfer 1 tot 10 | Waarom |
|---|---|---|
| Ziet het er top uit, op het niveau van de beste in de winkel? | niet te geven | Geen beeld gezien, geen vergelijking met een concurrent mogelijk. |
| Zou ik het zelf kopen of bekijken op basis van dit? | niet te geven | Idem. |
| Zou Thijs er trots op zijn? | niet te geven | Idem; oordeel Daan en Iris. |

## Moet (blokkeert akkoord) / Kan (mag later)
Moet:
- Geen.

Kan:
- Plaatje `check-parts-paneel-5.3.0.png` met Read bekijken: staat het label "Wall" volledig in beeld, en zijn veld en uitvoerregel te onderscheiden (Daan).
- E2e opnieuw draaien op f69022e of de kop van de tak voor het samenvoegen, als een toets op labeltekst bestaat.
- Tooltip toevoegen aan het veld, of een andere naam kiezen, zodat het niet dezelfde naam heeft als "Wall: 1.62 mm".
- Controleren dat `architectuur.md` Check parts noemt voor het samenvoegen.

---
Automatische keurder, model `claude-sonnet-5-5`, 19068 tokens in, 3241 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
