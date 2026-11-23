# Keuring blender-gewrichten changelog, 23-11-2026, automatische keurder
Wat ik keurde: commit 02ac53f9d (producten/blender-gewrichten/CHANGELOG.md), bereik 2560c3a..02ac53f
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid (hoog/midden/laag) | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De wijziging is één nieuwe regel onder "Unreleased / Fixed". Hij is in gewone woorden geschreven, vanuit de gebruiker, en hoort bij een lopende release (0.1.1 staat er al onder). | Feit | hoog | Het diff laat alleen deze drie regels zien. |
| 2 | De regel belooft dat een snede met een niet-waterdicht deel nog één keer met de Exact-solver wordt geprobeerd. Die code zit niet in deze wijziging, dus ik kan niet zien of dit echt gebouwd is. | Vermoeden | midden | Een eerdere commit in `gewricht.py` met die terugval en een test die het toont. Ontbreekt die, dan klopt de regel niet. |
| 3 | De meldtekst "no watertight parts" staat letterlijk in de regel. Of de add-on precies die tekst toont, kan ik niet zien. | Vermoeden | laag | De tekst in `gewricht.py` of in het log van de e2e-test. |
| 4 | Op Blender 4.2 tot 4.4 gebruikt de add-on al Exact (ontwerp en architectuur). Daar verandert de terugval dus niets. De regel geldt alleen voor 4.5 en hoger, maar dat staat er niet bij. | Vermoeden | midden | Een blik in de code of de terugval alleen bij Manifold draait. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Het changelogbestand blijft ruim binnen de grens van 5 regels per versie en 1024 tekens voor de uitgavetekst. | Feit | hoog | Kop van CHANGELOG.md |
| 2 | In deze wijziging staan geen persoonsgegevens, sleutels of wachtwoorden. | Feit | hoog | Regel persoonsgegevens |
| 3 | `architectuur.md` is niet bijgewerkt en noemt de terugval naar Exact niet (in het stuk dat ik zie, dat afgekapt is). Als de code in een eerdere commit kwam, kan dat daar al gedaan zijn. | Vermoeden | laag | Een regel over de terugval in `architectuur.md` bij `gewricht.py`. |
| 4 | Er zijn geen tests aangepast en geen bestanden groter gemaakt. | Feit | hoog | Regel tests en bestandsgrootte |

## Deel C: zou een gebruiker het leuk en fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite (klein/midden/groot) |
|---|---|---|---|
| 1 | Wat er in beeld of spel verandert, kan ik uit deze tekst niet zien. | Niets te beoordelen. | klein |
| 2 | "Exact solver" zegt een gewone gebruiker weinig. | Schrijf vanuit de gebruiker: "Cuts that failed now get a second try, so fewer spots end in 'no watertight parts'." | klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Controleer vóór de release van 0.1.2 dat de terugval echt in de code zit en dat de meldtekst klopt (A2, A3).
- Zet bij de regel dat het op Blender 4.5 en hoger speelt, of schrap de term "Exact solver" (A4, C2).
- Voeg een zin over de terugval toe aan `architectuur.md` als die er nog niet staat (B3).

---
Automatische keurder, model `claude-sonnet-5-5`, 17358 tokens in, 2041 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
