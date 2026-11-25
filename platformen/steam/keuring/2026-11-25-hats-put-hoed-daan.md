# Keuring Hats hoed uit de put op de toren, 25 nov 2026, Daan
Wat ik keurde: commit c52c9a2 (Olaf), `producten/steam-hol/bewijs-wegkijken/`, `kern/afloop.gd` (`put_hoed`), `systemen/toetsen/toets_klap.gd` (issue #92)
Akkoord: ja

## Deel A
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| A1 | Vraag 1: in alle 5 paren zie ik zonder uitleg een verschil (paar 1 toren van 2 naar 4, paar 5 andere bovenste hoed en een groene erbij). `na-30-min-voor-en-na.png`: één kroon tegen een toren van 4 plus een berg. Groot verschil voor wie niets koopt. | feit (beelden bekeken) | hoog | |
| A2 | Vraag 2: zelf beelden uit de film gehaald rond 247 tot 250 s (5 per s): de hoed valt in één beeld van boven, landt, Gloop knijpt even zijn oog dicht, klaar. Geen knipperen, niets wat aandacht trekt. Rustig. | feit | hoog | |
| A3 | Code: `put_hoed` stopt in de demo, vóór Gloops eigen eerste hoed en tijdens een vast moment; `gegeten -= 1` heft de +1 van `krijg_hoed_later` op, en de toets checkt dat. Klopt. | feit (code gelezen) | hoog | |
| A4 | `start_nacht` zet bij elke put-hoed de klok van de nacht opnieuw (nacht_gelegd = 0, nacht_van = t + 1,2). Valt er net een rij hoeden van de nacht (terugkomen na lang weg), dan pauzeert die rij even en gaat dan door. Geen dubbele hoeden (gelegde hoeden gaan uit de rij). | vermoeden (code gelezen, niet gezien) | midden | film van terugkomen met 10 nachthoeden en een put-val in die seconden |

## Deel B
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| B1 | Toetsen 7 x 0 FOUT op Linux (GEZIEN door Olaf); nieuwe toetsen voor demo, eerste hoed en gegeten. Geen toets aangepast om te slagen. Windows en duurtest lopen (in #86). | feit volgens issue | midden | tests |
| B2 | Geen spelerstekst, geen nieuw beeld of geluid. | feit | hoog | |

## Deel C: speler
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| C1 | Vraag 3: bij 10 of meer hoeden ligt de berg bijna helemaal voor de blauwe kristallen (paar 5: alleen een puntje steekt eruit). Niet storend, de berg leest als een berg. Wel jammer van de kristallen, het enige blauwe licht in die hoek. | Berg iets naar rechts laten groeien, of de kristallen een stuk naar links, zodat beide te zien zijn. | klein |
| C2 | De toren staat op paar 5 iets links van Gloops kruin en wordt hoog (5 hoog op 1024 x 120). Bij 27 hoeden gaat het grootste deel naar de berg, dus dat blijft binnen het beeld. Goed. | | |
| C3 | Dit is precies wat Rusty's Retirement doet: na 2 min wegkijken is er iets te zien. 95 procent van de vensters van 2 min heeft een nieuwe hoed (GEZIEN door Olaf). | | |

## Deel C: goed genoeg?
| Vraag | Cijfer | Waarom |
|---|---|---|
| Top, naast de beste? | 8 | Naast Rusty's Retirement (boerderij verandert terwijl je werkt): hier groeit de toren zichtbaar, rustig. |
| Zelf spelen? | 8 | Een hoed van wie viel op de toren is een grap die je zelf ontdekt. |
| Thijs trots? | 8 | Rustig, geen tekst, past bij de naam. |

## Moet
Geen.
## Kan
- C1: berg en kristallen uit elkaar.
- A4: bij een lopende rij van de nacht de put-hoed achteraan zetten zonder de klok opnieuw te starten.
