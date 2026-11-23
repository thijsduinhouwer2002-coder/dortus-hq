# Keuring blender-gewrichten (Olaf diag ronde 3, extra kogelplek), 23-11-2026, automatische keurder
Wat ik keurde: commit dd1237d99 (489f4bd..dd1237d), alleen `producten/blender-gewrichten/click_joints/betaald/rig.py`
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid (hoog/midden/laag) | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De wijziging voegt in `kogel_schuif` één laatste kandidaatplek toe: 0,3 mm verder het lid in, alleen als die nog binnen de helft van `lengte` valt. | Feit (uit de diff) | hoog | Niet nodig. |
| 2 | De commit zegt dat de plek alleen na een weigering aan de beurt komt. Dat klopt alleen als de aanroeper de lijst van voor naar achter afloopt en bij de eerste geslaagde plek stopt. Die code staat niet in de diff. | Vermoeden | midden | De aanroeper van `kogel_schuif` lezen, of een toets met een figuur waar de eerste plek al lukt en de uitkomst gelijk blijft. |
| 3 | De heupfout op de AMD-runner (1110 overlappende driehoeken, "blocked") zou hiermee verdwijnen. In de tekst staat geen groene run na deze wijziging. | Vermoeden | laag | Een groene CI-run op de robot (studio-2) met 9 gewrichten, met de DIAGMESH-regels erbij. |
| 4 | `t_vrij`, `u` en `lengte` worden in het getoonde stuk niet gedefinieerd. Ze zullen er hoger in de functie al staan, want `u` en `lengte` worden daar al gebruikt. | Vermoeden | midden | Een run van de bestaande toets: een NameError zou direct zichtbaar zijn. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Er is geen toets aangepast. Het is een kleine wijziging van 7 regels, met uitleg in het commentaar. | Feit | hoog | Tests niet aangepast om te slagen: in orde. |
| 2 | Het commentaar noemt run 45206324187 als GEZIEN en geeft "lokaal 9, CI 8". Er staan geen persoonsgegevens of sleutels in. | Feit | hoog | Cijfers met GEZIEN/DERDEN/GOK, geen persoonsgegevens: in orde. |
| 3 | De regelaantallen van `rig.py` zijn uit de diff niet te zien. | Vermoeden | laag | Regelaantal van `rig.py` controleren tegen de grens van ±400. |
| 4 | `architectuur.md` is niet bijgewerkt voor de extra kandidaatplek, voor zover dat daar beschreven staat. Het is een klein detail. | Vermoeden | midden | Zoeken naar `kogel_schuif` of kandidaatplekken in `architectuur.md`. |
| 5 | De goedkeuring in `ontwerp.md` voor Pro 1.0.2 geldt voor tak `claude/blender-een-lid` 4b7e722. Deze wijziging verandert Pro-code en valt dus buiten die goedkeuring. | Feit | hoog | Het ja bij de opdracht geldt voor een bepaalde bouw. |

## Deel C: zou een gebruiker het leuk en fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite (klein/midden/groot) |
|---|---|---|---|
| 1 | Er is niets te zien of te spelen in deze tekst. Het gewricht verschuift hooguit 0,3 mm, en alleen na een weigering. Voor de speler is dat een verbetering omdat de heup dan mogelijk wel lukt. | Na de CI-run een beeld van de heup van de robot bekijken, bij voorkeur van de AMD-run. | klein |
| 2 | De fout hangt af van de processor. Een figuur dat bij de ene gebruiker lukt, kan bij een andere nog steeds weigeren, ook na deze wijziging. Voor de gebruiker voelt dat willekeurig. | De echte oorzaak zoeken in het verschil tussen de Boolean-uitkomsten per processor. Dit is een noodoplossing met één extra kandidaat. | midden |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Pro 1.0.2 niet uitbrengen met deze wijziging zonder een nieuwe groene run in alle drie de Blender-versies. De goedkeuring in `ontwerp.md` dekt alleen de bouw van voor deze commit.
- Een groene run bij de commit zetten die laat zien dat de robot op CI nu 9 van 9 gewrichten haalt. Dat bevestigt vermoeden 3 uit deel A.
- De toets voor de weigering uitbreiden met een geval waarin de extra kandidaat nodig is. Dan blijft het gedrag gedekt.
- Kijken of `architectuur.md` een korte regel over de extra kandidaatplek moet krijgen, en het regelaantal van `rig.py` nalopen.
- Later de oorzaak van het verschil tussen AMD en Intel uitzoeken, in plaats van steeds een extra plek erbij te zetten.

---
Automatische keurder, model `claude-sonnet-5-5`, 17531 tokens in, 3056 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
