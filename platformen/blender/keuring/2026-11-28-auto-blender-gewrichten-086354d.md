# Keuring blender-gewrichten tenen bij het lid (#306), 28-11-2026, automatische keurder
Wat ik keurde: commits 7de51b8..086354d (6e7a20767 en 086354dc0), alleen als tekst gelezen
Akkoord: nee

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid (hoog/midden/laag) | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De aanpak past bij de klacht. `_samen` telt de vereniging pas als goed als elk punt van het lid zelf in het omhulsel ligt. Lukt dat niet, dan volgt een voxel-remesh en pas daarna de oude terugval. | Feit (uit de code) | Hoog | Alleen een run bewijst dat het werkt, zie 2. |
| 2 | Of de teenstukjes echt weg zijn, kan ik uit de tekst niet halen. Er is geen run-nummer of loguitvoer van `toetsen_tenen.py` bijgevoegd. | Vermoeden | Midden | Een groene run met de regels `[cj-tenen]` voor 4.2.23 en 5.x: deel A alleen lijf en ogen, deel B één stuk, beide gesloten. |
| 3 | De test eist `buiten == 0` zonder ruimte. Het gewone omhulsel in Pro (`omhulsel.py`) laat bewust tot 2% buiten toe, omdat het controlepunt in holtes niet klopt. Pro roept deze `_samen` aan via `samen_schoon`, dus meer figuren kunnen nu in de voxel-weg of in "los" terechtkomen. | Vermoeden | Midden | Groene e2e voor Pro op army_man, Rigify en Meshy-knight, met het verlies per figuur (was 5,6%). |
| 4 | `_lid_buiten` doet `find_nearest` voor elk lidpunt, bij elke poging. De eis blijft onder 5 s per gewricht op 200K driehoeken. | Vermoeden | Laag | De tijdmeting uit de bestaande e2e (was 3,2 tot 3,3 s op 4.2). |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | `toetsen_tenen.py` is nieuw, maar er is geen workflow in de gewijzigde bestanden. De test krijgt zijn bestand en zip als argument, dus iets moet het figuur downloaden en de test starten. | Vermoeden | Midden | Tests moeten echt draaien |
| 2 | Commit 086354d versoepelt de test: ogen mogen met het hoofd samensmelten. Fout blijft elk stukje kleiner dan 2% van het lijf, dus de bug wordt nog gevangen. Er staat wel geen log bij dat de samensmelting met Exact echt voorkomt. | Vermoeden | Midden | Tests niet aangepast om te slagen |
| 3 | In `toets_zips.py` zijn de hashes van manifest en `een_lid.py` vernieuwd. Dat hoort bij de wijziging, maar ik kan de waarden niet narekenen. De regel "Wacht op keuring Daan" staat er terecht bij. | Vermoeden | Laag | Gratis zip is bewust gekeurd |
| 4 | `architectuur.md` is bijgewerkt, met GEZIEN voor de lokale meting (25 tot 35 weggelaten punten, 5 losse teenstukjes per knie). | Feit | Hoog | architectuur.md bijgewerkt, cijfers met GEZIEN |
| 5 | De CHANGELOG-regel staat in gewoon Engels vanuit de gebruiker en noemt Pro niet. Dat klopt met de regels van extensions.blender.org. Een persoonsgegeven zag ik nergens. | Feit | Hoog | Geen persoonsgegevens, geen Pro op extensions |
| 6 | De lengte van `een_lid.py` kan ik niet zien. Het bestand kreeg bijna 70 regels erbij en zat al ver boven de 300. | Vermoeden | Laag | Bestanden onder ±400 regels |

## Deel C: zou een gebruiker het leuk en fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite (klein/midden/groot) |
|---|---|---|---|
| 1 | Er is niets te zien of te spelen in deze wijziging, dus ik kan hier niets over zeggen. Een gebruiker merkt hoogstens dat zijn knie schoon snijdt. | Een voor-en-na-beeld van de voet in deel A voor de release-notes, als Daan dat wil. | klein |

## Deel C: is het goed genoeg?
Er is geen nieuw klantbeeld of nieuwe winkeltekst, dus de blinde test is niet van toepassing. Cijfers geef ik niet: ik kan niets zien en niets met een concurrent vergelijken. Het uiterlijk blijft bij Daan en Iris.

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet**
1. Laat een groene e2e-run zien met `toetsen_tenen.py` erin, op 4.2.23 en 5.x, plus de bestaande Pro-toetsen (army_man, Rigify, Meshy-knight). Zonder dat is niet bewezen dat de teenfout weg is en dat `buiten == 0` Pro niet raakt (A2, A3, B1).
2. Maak duidelijk welke workflow `toetsen_tenen.py` start en hoe het Human Base Meshes-bestand binnenkomt. Als dat niet gebeurt, draait de test nooit (B1).

**Kan**
1. Zet in de test een logregel waaruit blijkt dat bij Exact het samensmelten van de ogen echt voorkomt, om de versoepeling te onderbouwen (B2).
2. `h_pogingen` heeft nu 5 in plaats van 4 velden. Controleer of een andere toets of tool de tuple uitpakt.
3. Meet de tijd van `_lid_buiten` op het figuur van 200K driehoeken (A4).
4. Het Pro-manifest en de Pro-changelog zijn niet bijgewerkt, terwijl `betaald/een_lid_diep.py` wel veranderde.

---
Automatische keurder, model `claude-sonnet-5-5`, 30639 tokens in, 4998 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
