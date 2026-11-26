# Keuring blender-gewrichten: Pro zet de gratis versie zelf uit (issue 114), 26-11-2026, automatische keurder
Wat ik keurde: commit f43c3c67d (range f973683..f43c3c6), alleen de tekst van de diff in `betaald/__init__.py`, `e2e/betaald/init_betaald.py` en `e2e/test_betaald.py`
Akkoord: ja

## Deel A: doet het wat beloofd is?
(Opdracht: issue 114 volgens de commitregel en de docstring. Pro zet de gratis uit in plaats van te weigeren. Het ontwerp zegt zelf niets over issue 114.)
| # | Bevinding | Feit of vermoeden | Zekerheid (hoog/midden/laag) | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | `zet_gratis_uit` zet elke andere `click_joints`-module uit met `addon_utils.disable(default_set=True)`. Daarna controleert `weiger_dubbel` of er nog een over is, dus er staan nooit twee tegelijk aan. De init-stap roept dit aan vóór `_register_kern()`. | Feit (uit de diff) | hoog | n.v.t. |
| 2 | De regel "Free Click Joints was turned off..." komt bovenaan het paneel via `kern.BOVEN.insert(0, ...)` en gaat weg bij unregister. | Feit (uit de diff) | hoog | n.v.t. |
| 3 | `_meld` wordt aangeroepen vóór de kern en `betaald.register` draaien. Of `_meld` dan al werkt, is niet te zien, want de functie staat niet in de diff. | Vermoeden | laag | De e2e-stap "(a) melding: gratis uitgezet" groen in 4.2.23, 5.2.3 en 5.3.0. |
| 4 | `GRATIS_UIT` wordt alleen gevuld, nooit leeggemaakt, ook niet bij unregister. Gaat Pro uit en later weer aan zonder dat de module herlaadt, terwijl de gratis niet aan was, dan kan de regel ten onrechte blijven staan. | Vermoeden | midden | Een test: Pro aan met gratis aan, Pro uit, gratis uit, Pro aan, en dan kijken of de regel er staat. |
| 5 | De andere richting werkt nog zoals voorheen: gratis aanzetten terwijl Pro aan staat zet Pro opzij. Bij een start waarbij beide aan staan hangt de uitkomst dus van de volgorde af. | Vermoeden | midden | Een e2e-stap met beide in de voorkeuren en Pro als eerste. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | De test is aangepast omdat het gedrag bewust verandert: van weigeren naar overnemen. Er zijn meer controles bijgekomen (voorkeuren, niet verwijderd, paneelregel eerst, winkellinks), dus dit is geen aanpassing om te slagen. | Feit | hoog | Tests niet aangepast om te slagen |
| 2 | `architectuur.md` en `ontwerp.md` staan niet in de gewijzigde bestanden. Het gedrag bij dubbel aanstaan ("weigering", eis 7) verandert wel. Of daar nog "weigert" staat, kan ik niet zien, want de tekst is afgekapt. | Vermoeden | midden | architectuur.md bijgewerkt |
| 3 | De nieuwe testregels gebruiken `toetsen_paneel` en `traceback`. Of die bovenin `test_betaald.py` geïmporteerd zijn, staat niet in de diff. Ontbreekt `traceback`, dan faalt de foutafhandeling zelf. | Vermoeden | laag | Bewijs met een groene run |
| 4 | Er staat geen e2e-run bij de commit en hij staat niet op main. Eerdere akkoorden eisten een groene run in 4.2.23, 5.2.3 en 5.3.0. | Feit (niets genoemd) | hoog | Cijfers en uitslagen met bron |
| 5 | Geen persoonsgegevens, sleutels of wachtwoorden in de diff. Alle bestanden blijven vermoedelijk ruim onder de 400 regels, maar de lengte van `betaald/__init__.py` kan ik niet zien. | Feit, deels vermoeden | midden | Persoonsgegevens, bestandslengte |

## Deel C: zou een gebruiker het leuk en fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite (klein/midden/groot) |
|---|---|---|---|
| 1 | Wie van gratis naar Pro overstapt, hoeft niets meer uit te zetten. Dat is een duidelijke verbetering ten opzichte van de foutmelding. | Niets nodig. | n.v.t. |
| 2 | De infoteller bovenaan het paneel blijft de hele sessie staan, ook als de gebruiker hem allang gezien heeft. | Laat de regel na een klik of na de eerste export verdwijnen. | klein |
| 3 | De Superhive-beschrijving zei volgens de code-opmerking "Disable it first". Die tekst klopt na deze wijziging niet meer. | Pas de winkeltekst en de documentatie aan als dit live gaat. | klein |

## Deel C: is het goed genoeg?
Er is geen beeld, geen winkeltekst en geen spel om te beoordelen, alleen één regel in het paneel. Zonder scherm geef ik geen cijfers en ga ik niet vergelijken met een concurrent. De eindkeuring van het uiterlijk blijft bij Daan, die de regel moet zien in Blender.

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Laat de e2e groen draaien in 4.2.23, 5.2.3 en 5.3.0 voor samenvoegen naar main. Controleer daarbij de imports `toetsen_paneel` en `traceback` en de stap "(a) melding: gratis uitgezet" (Deel A 3, Deel B 3 en 4).
- Maak `GRATIS_UIT` leeg bij unregister, zodat de regel niet blijft staan (Deel A 4).
- Controleer of `architectuur.md` en `ontwerp.md` (eis 7) nog "weigert" zeggen, en pas ze aan (Deel B 2).
- Overweeg de andere richting gelijk te trekken, of leg uit waarom Pro opzij gaat voor de gratis (Deel A 5).
- Pas de Superhive-winkeltekst of documentatie aan als die nog "Disable it first" zegt (Deel C 3).

---
Automatische keurder, model `claude-sonnet-5-5`, 22028 tokens in, 7515 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
