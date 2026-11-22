# Keuring blender-gewrichten (Click Joints Pro, gedraaide elleboog), 22-11-2026, automatische keurder
Wat ik keurde: commits bc90c70..01ac949 (becfa9715, f1a171e0c, 26c7aca73, 86800a638): `rig.py`, `een_lid_diep.py` en `architectuur.md`
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De gedraaide elleboog komt alleen aan de beurt voor `sleutel == "ELBOW"`, en pas na een weigering van de eigen plekken. De knie en enkel worden niet gedraaid. | Feit (uit de diff) | hoog | Niets nodig. |
| 2 | Alleen de stand die naar voren buigt wordt gebruikt (`gedraaid(k)[0]`). De tweede stand, naar achteren, wordt dus niet meer geprobeerd. | Feit | hoog | Een test met een figuur dat naar +Y kijkt. |
| 3 | "Voorkant is -Y" staat vast in de code (`voor=Vector((0,-1,0))`). Kijkt een rig naar +Y of naar een andere kant, dan kan de elleboog toch naar achteren of zijwaarts buigen. Dat is precies wat de keuring van Daan verbood. | Vermoeden | midden | Een Quaternius-rig of de Yeti gedraaid om Z, en dan de buigrichting meten. |
| 4 | `scharnier_plekken(...) or [(m, 0.0)]` geldt voor elk scharnier. Een knie of enkel zonder plek krijgt nu de plek van het bot zelf, terwijl dat eerst waarschijnlijk werd overgeslagen. | Vermoeden | midden | Een rig waarbij `scharnier_plekken` een lege lijst geeft voor de knie, en dan kijken of de knie nu toch snijdt. |
| 5 | De claim "Yeti 4 gewrichten, ellebogen naar voren" is alleen lokaal gezien (Blender 5.3.0). In deze wijziging staat er geen CI-run of test bij. | Feit dat het alleen lokaal is, uitkomst onbekend | midden | Een groene run in 4.2.23 en 5.2.3 met een gedraaide-elleboogtest. |
| 6 | Het laatste Akkoord in `ontwerp.md` gaat over gratis 0.1.1 en Pro 1.0.2. "Pro 1.1" en "keuring Daan" uit de commits zijn daar niet terug te vinden. | Vermoeden | midden | Een Akkoord van Daan voor Pro 1.1 in `ontwerp.md`. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | `architectuur.md` is bijgewerkt voor `rig.py` en de gedraaide elleboog. Het hulpvlag `ALTIJD_H` van `een_lid_diep.py` is alleen in een code-opmerking en niet in `architectuur.md` te vinden. | Feit | hoog | architectuur.md bijgewerkt (kan: voeg een zin toe). |
| 2 | Er zijn geen tests toegevoegd of aangepast voor het nieuwe pad. Er is dus ook niets aangepast om te slagen. Het pad is wel ongetoetst. | Feit | hoog | Tests niet aangepast om te slagen: niet geschonden. Toetsbaar bewijs ontbreekt wel. |
| 3 | `rig.py` is minstens ±700 regels (hunks bij regel 652 en 707) en wordt groter. De grens is ±400. | Feit | midden | Bestanden onder ±400 regels. Dit was al zo, maar het groeit. |
| 4 | De cijfers in de opmerkingen zijn met GEZIEN gemarkeerd, maar spreken elkaar tegen. In `rig.py` staat 16% en alles boven z 126 mm, in `een_lid_diep.py` staat 18 tot 21%. Het kan gaan om andere metingen, maar dat staat er niet bij. | Feit | hoog | Cijfers met GEZIEN/DERDEN/GOK. |
| 5 | Geen persoonsgegevens, sleutels of beeld- en geluidsmateriaal gezien in de diff. | Feit | hoog | Geen persoonsgegevens, geen AI-beeld of -geluid. |

## Deel C: zou een gebruiker het leuk en fijn vinden? (alles wat je kunt zien of spelen)
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | Ik zie geen beelden en kan dus niet beoordelen of de gedraaide elleboog er natuurlijk uitziet. Op papier is "alleen naar voren buigen" een goede keuze. | Een schermafbeelding van de Yeti met gebogen ellebogen op tak `schermen`, voor Daan en Iris. | klein |
| 2 | Bij de Yeti vallen de schouders af met "too close to another joint". De koper krijgt dan 4 gewrichten in plaats van 6. | Een duidelijke regel in de lijst na afloop: "Shoulders skipped: elbow joint is too close". | klein |
| 3 | Een knie of enkel die niet past wordt stil overgeslagen. | Zet het in de uitslag als "overgeslagen, met reden", zodat de koper niet denkt dat het kapot is. | klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** niets.

**Kan:**
- Voeg een test toe met een rig die naar +Y kijkt en een rig in T-houding met de onderarm voor-achter. Meet dat de elleboog nooit naar achteren buigt en dat de snede minder dan 6% verliest (B2, A3, A5).
- Bepaal "voor" uit de rig zelf (bijvoorbeeld de ooghoogte of de teenrichting) in plaats van vast -Y (A3).
- Controleer of `or [(m, 0.0)]` ook voor de knie en enkel zo bedoeld is. Zo niet, beperk het tot de elleboog (A4).
- Haal de ongebruikte tweede stand uit `gedraaid()` weg of pas de docstring aan.
- Zet `ALTIJD_H` en de Orc-uitslag (4 gewrichten) ook in `architectuur.md` (B1).
- Laat Daan Pro 1.1 expliciet goedkeuren in `ontwerp.md` voor het live gaat (A6).
- Splits `rig.py` op (B3).

---
Automatische keurder, model `claude-sonnet-5-5`, 24234 tokens in, 4670 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
