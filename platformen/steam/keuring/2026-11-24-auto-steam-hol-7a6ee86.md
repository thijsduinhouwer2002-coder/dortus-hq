# Keuring steam-hol demovolgorde en inhoud-100, 24-11-2026, automatische keurder
Wat ik keurde: commits 307ed6169 en 0b0067530 (sim/demo_volgorde.py, sim/demo-volgorde-uitkomst.txt). inhoud-100.md is niet meegestuurd (24546 tekens, te groot) en heb ik dus niet gezien.
Akkoord: ja (alleen voor de simulatie; over inhoud-100.md zeg ik niets)

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid (hoog/midden/laag) | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De uitkomst past bij het script: koppen, kolombreedtes en regels komen overeen met de printregels. | Feit | hoog | Het script draaien en de uitvoer naast het txt-bestand leggen. |
| 2 | Vrijspelen op gevangen helden is te grillig: 20 van 20 zaden hebben een stuk boven 3 min, het langste is 10,3 min. | Feit (uit de uitkomst) | hoog | Een andere simulatie die dit weerlegt. |
| 3 | Het voorstel op binnengekomen helden houdt het langste stuk op 2,6 tot 2,8 min, ook op de controlezaden 21 tot 40 die niet gebruikt zijn bij het kiezen. Dat is een nette opzet. | Feit voor de sim, vermoeden voor het echte spel | midden | Een echte speelrun of de filmrun van `steam-hol.yml` met `helden_nr` in het log. |
| 4 | De sim kijkt alleen naar de eerste 30 min. De demo duurt 2 uur open tijd. Of de overige 90 min goed gevuld zijn, blijkt hier niet. | Vermoeden | midden | Staat het in inhoud-100.md of een sim over 2 uur? |
| 5 | Het voorstel gebruikt `helden_nr` uit de save van `strook.gd`. Telt de voortgang terwijl je weg bent (`voortgang.gd`) dit getal ook op? Dan komen er bij terugkeer in één keer meer dingen vrij, terwijl de demo op open tijd telt. | Vermoeden | laag | De code van `voortgang.gd` en `opslag.gd`, of een toets die een nacht weg simuleert. |
| 6 | Het script doet `import sim` en roept `sim.reeksen(n, uren=...)` aan. `sim.py` zit niet in deze wijziging. Ik ga ervan uit dat het al bestaat met dit gedrag. | Vermoeden | midden | `sim/sim.py` met `reeksen(zaden, uren)`. |
| 7 | Het voorstel noemt 15 drempels, het plan noemt 21 dingen voor de demo. Hoe de overige 6 vrijkomen, kan ik niet zien. | Vermoeden | laag | inhoud-100.md lezen. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Er zijn geen tests aangepast en er staan geen persoonsgegevens of sleutels in de bestanden die ik zag. | Feit | hoog | Tests niet aangepast, geen persoonsgegevens |
| 2 | Het script (52 regels) en de uitkomst (44 regels) zijn ver onder de 400 regels. Voor inhoud-100.md kan ik de regelgrens niet toetsen. | Feit voor twee bestanden, onbekend voor het derde | midden | Bestanden onder ±400 regels |
| 3 | De uitkomstcijfers zijn simulatie, maar in het txt-bestand staat nergens GOK of "sim". Een lezer kan ze voor gemeten waarden aanzien. | Feit | hoog | Cijfers met GEZIEN/DERDEN/GOK |
| 4 | `architectuur.md` is niet bijgewerkt. Er is geen spelcode veranderd, dus dat hoeft hier niet. | Feit | midden | architectuur.md bijgewerkt |
| 5 | Of inhoud-100.md spelerstekst of hoednamen bevat die als CONCEPT gemarkeerd moeten zijn, kan ik niet zien. | Vermoeden | laag | Spelerstekst van Hats alleen als CONCEPT |
| 6 | De kop van het script beschrijft alleen het eerste deel (vrijspelen op gevangen helden). Het voorstel op binnengekomen helden staat er wel in, maar niet in de beschrijving bovenaan. | Feit | hoog | Leesbaarheid (klein) |

## Deel C: zou een gebruiker het leuk en fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite (klein/midden/groot) |
|---|---|---|---|
| 1 | Op een vaste telling van binnengekomen helden vrijspelen geeft elke ±2,7 min iets nieuws, bijna als een metronome (spreiding 2,6 tot 2,8). Dat is rustig en past bij "tussendoor", maar na een halfuur kan het voorspelbaar voelen. | Een enkele drempel van een ander soort laten gaan, bijvoorbeeld bij een bijzondere held of een terugkomer, en niet alleen op het aantal helden. | midden |
| 2 | Wat je vrijspeelt hangt niet af van wat de speler doet, alleen van de tijd. Dat sluit aan bij "nooit straffen", maar de speler heeft er geen invloed op. | Eén of twee van de 21 dingen laten afhangen van een eigen keuze, zoals een gebouwde kamer of een put. | midden |
| 3 | Een kroniekregel of een klein moment bij elk vrijgespeeld ding (zoals bij `That's the demo...`) kan de wisseling zichtbaar maken. Of dat in het plan staat, weet ik niet. | Controleer of inhoud-100.md zo'n moment noemt. | klein |

## Deel C: is het goed genoeg?
| Vraag | Cijfer 1 tot 10 | Waarom, en waarmee vergeleken |
|---|---|---|
| Ziet het er top uit, op het niveau van de beste in de winkel? | n.v.t. | Een planbestand en een simulatie. Een klant ziet dit niet, en er is niets om naast een concurrent te leggen. |
| Zou ik het zelf kopen of bekijken op basis van dit? | n.v.t. | Idem. |
| Zou Thijs er trots op zijn? | n.v.t. | Dit blijft intern. De dingen zelf worden later gekeurd op beeld en spelen (Daan en Iris). |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen in wat ik kon zien. Het akkoord geldt alleen voor de simulatie. inhoud-100.md is niet gekeurd, omdat de inhoud niet meegestuurd is. Laat een mens of een tweede keurder die lezen.

**Kan:**
- Zet in `demo-volgorde-uitkomst.txt` een regel dat de cijfers uit de simulatie komen (GOK, niet GEZIEN).
- Reken de simulatie ook voor de volle 2 uur door, of laat zien waar dat staat.
- Controleer dat `helden_nr` niet meetelt terwijl je weg bent, met een toets of een blik in `voortgang.gd`.
- Vul de kop van het script aan zodat ook het voorstel erin genoemd wordt.
- Overweeg een of twee vrijspeelmomenten die van een eigen keuze afhangen (zie Deel C).

---
Automatische keurder, model `claude-sonnet-5-5`, 16970 tokens in, 6745 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
