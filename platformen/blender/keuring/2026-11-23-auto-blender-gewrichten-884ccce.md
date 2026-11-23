# Keuring Click Joints Pro: mooier overlay bij een figuur, 23-11-2026 11:51 NL, automatische keurder
Wat ik keurde: commit 884ccce1c (b94d5ae..884ccce), productmap producten/blender-gewrichten
Akkoord: nee

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid (hoog/midden/laag) | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De schakelaar Labels met Selected, All en None staat in `labels.py` en in het paneel Figure joints. De standaard is Selected. Alleen gewrichten met `cj_figuur` volgen de schakelaar, een los gewricht tekent altijd. | Feit (uit de code) | hoog | Een test of schermopname per stand die laat zien dat het gewricht in de stand Selected alleen verschijnt bij een gekozen deel. |
| 2 | Het label is nu een pil (donkere achtergrond, bolletje in de passingkleur, witte tekst), met een donkere onderlijn onder de boog. De code is logisch opgebouwd en de pil past bij de vakmaat die voor de plaatsing wordt gebruikt. | Vermoeden (ik zie geen beeld) | midden | Een schermopname van Blender 4.2 en 5.2 met een figuur op een licht, een grijs en een oranje model. |
| 3 | Voorbij de stop wordt bij een figuur het hele deel B rood via `kleur_deel`, en het eigen materiaalvak per vlak gaat terug via `cj_rood_deel` in `_terug`. De herstelvolgorde klopt op papier: eerst het hele deel, dan de rakende vlakken. | Vermoeden | midden | Een proef: pose voorbij de stop, dan terug binnen de stop, en controleren dat `material_index` gelijk is aan het begin. |
| 4 | `kleur_deel` wordt in `pose()` aangeroepen zodra het deel een figuur is, ook als `vlakken_b` leeg is. Ik zie niet of `pose()` alleen bij contact of voorbij de stop draait. Anders kleurt een pose binnen de stop het hele deel ten onrechte rood. | Vermoeden | laag | Een proef met pose binnen de stop: `cj_rood_deel` mag dan niet bestaan en geen vlak mag het rode vak hebben. |
| 5 | Bij een lid met veel vlakken (±200K driehoeken) wordt per pose-stap een lijst van alle vlakindexen als eigenschap op het object gezet. Dat kan traag gaan bij het slepen van de pose-schuif. | Vermoeden | laag | Meting van de tijd per pose-stap op de figuur van 261K driehoeken. |
| 6 | Het label in de stand Selected toont de naam in de pil ("Right knee  0 tot 120°"). De kopregel bovenin verdwijnt dan voor dat gewricht. | Feit (uit de code) | hoog | Een schermopname die laat zien dat de naam in de pil past zonder overlap met andere labels. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Er is een nieuw bestand `betaald/labels.py` met een nieuwe instelling, maar `architectuur.md` staat niet in de gewijzigde bestanden. | Feit | hoog | architectuur.md bijgewerkt |
| 2 | Er is geen nieuwe test voor `toon`, `kleur_deel` of het herstel in `_terug`. De docstring in `labels.py` zegt wel dat `toon` ook zonder scherm te toetsen is. | Feit | hoog | Nieuw gedrag hoort een toets te hebben (zie ontwerp, eis 6) |
| 3 | De vier schermscripts (`scherm_figuur`, `scherm_mens`, `scherm_rig`, `scherm_rig_armen`) zetten nu expliciet de stand All. Hiermee blijven ze meten wat ze mmmeten, maar de nieuwe standaard Selected wordt in geen enkel script bekeken. | Feit | midden | Tests niet aangepast om te slagen (hier waarschijnlijk geen overtreding) |
| 4 | De camerahoek en afstand in `scherm_mooi.py` zijn aangepast (van opzij naar rechts, afstand 120 naar 150). Dit lijkt een betere opname en geen versoepeling van een eis. | Vermoeden | midden | Tests niet aangepast om te slagen |
| 5 | `figuur_teken.py` en `scharnier_boog.py` kunnen over de ±400 regels gaan. De bestandsgroottes staan niet in de wijziging. | Vermoeden | laag | Bestanden onder ±400 regels (tel met `wc -l`) |
| 6 | Er staan geen persoonsgegevens, sleutels of wachtwoorden in de wijziging. De Pro-code hangt niet aan de gratis versie en de gratis zip verandert niet. | Feit | hoog | Geen persoonsgegevens; twee builds |

## Deel C: zou een gebruiker het leuk en fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite (klein/midden/groot) |
|---|---|---|---|
| 1 | Negen getallen tegelijk waren rommelig, dus Selected als standaard is rustiger. Een nieuwe gebruiker ziet daarna echter niets tot hij een lid kiest. Het bereik in graden is juist het onderscheid van het product. | Een korte hint in het paneel ("Select a joint to see its range") of bij het plaatsen van een figuur het eerste gewricht automatisch kiezen. | klein |
| 2 | De winkelplaatjes worden nu met de stand All gemaakt. Dat is niet wat een koper bij de eerste start ziet. | Eén plaatje per winkelfoto met de standaardstand, plus een met All. | klein |
| 3 | Het hele deel rood voorbij de stop is duidelijker dan een dunne strook. Een heel rood lid kan op een lichte of oranje kleur van het figuur heel hard overkomen. | Kijk op een schermopname of een iets doorzichtiger rood beter oogt. | klein |
| 4 | Een knop of sneltoets om snel tussen Selected en None te wisselen helpt bij renders. | Een kleine knop "Hide labels" naast de schakelaar. | klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet**
1. Werk `architectuur.md` bij met `betaald/labels.py` (schakelaar `cj_labels`, pil en onderlijn) en met `kleur_deel` en `cj_rood_deel` in `scharnier_beweeg.py`.

**Kan**
1. Voeg een toets toe voor `toon` in de drie standen, en voor het terugzetten van `material_index` na rood. Voeg ook een opname toe in de standaardstand Selected.
2. Controleer dat `kleur_deel` alleen draait bij een pose voorbij de stop (Deel A, punt 4).
3. Meet de pose-snelheid op een figuur met veel vlakken (Deel A, punt 5).
4. Tel de regels van `figuur_teken.py` en `scharnier_boog.py`.
5. Zet een hint bij Selected (Deel C, punt 1) en maak winkelplaatjes in de standaardstand.
6. Typefout in de docstring van de schermscripts is er niet, maar `alle_labels` staat met één lege regel voor `def stap`: pas de opmaak aan (klein).

---
Automatische keurder, model `claude-sonnet-5-5`, 32194 tokens in, 6182 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
