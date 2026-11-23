# Keuring blender-gewrichten (Click Joints Pro, omhulsel H), 23-11-2026, automatische keurder
Wat ik keurde: commit bbc1ff130 (196691e..bbc1ff1): `betaald/omhulsel.py` (nieuw), `betaald/__init__.py`, `e2e/meet_diag.py`
Akkoord: nee

## Deel A: doet het wat beloofd is?
De opdracht in `ontwerp.md` gaat over gratis 0.1.1 en Pro 1.0.2. Deze wijziging is een betrouwbaarheidsfix in Pro (1.2.3, volgens de code), dus ik toets hem aan de bedoeling uit de commit en de docstring.

| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | Het gratis deel blijft onaangeroerd: alleen `betaald/` en een diagnosescript zijn gewijzigd. `omhulsel.register()` vervangt `een_lid._samen` en `unregister()` zet het terug. | Feit | Hoog | `toets_zips.py` blijft groen. |
| 2 | De oorzaak (H snijdt zichzelf, Manifold en Exact gaan er verschillend mee om) en de meetcijfers staan alleen in een docstring, met een verwijzing naar run 45253697551. Die run is in deze tekst niet te zien. | Vermoeden | Midden | Een groene e2e-run op deze tak waarin Figure from rig op de robot geen gewricht meer overslaat, in 4.2 en 5.x. |
| 3 | De aanpak lijkt logisch: een voxel-remesh van beide schillen en daarna een controle op binnen/buiten (`BUITEN_MAX` 0,2%). Zo kan de fix niet stilzwijgend een te kleine H geven, want bij falen volgt de oude weg. | Vermoeden | Midden | Het logveld `h_soort` staat op "voxel" bij de rigtest, met `h_buiten` onder 0,002. |
| 4 | Op een figuur waar de voxelmaat groter is dan marge `m` kunnen de controlepunten buiten H vallen. De oude weg wordt dan weer gebruikt en het probleem blijft bestaan. Dat is veilig, maar niet verholpen. | Vermoeden | Laag | Meetwaarden `h_voxel` tegenover `marge` op de testfiguren. |
| 5 | `evaluated_get` wordt direct na het koppelen van een nieuw object gedaan, zonder `view_layer.update()`. Dat gaat waarschijnlijk goed, want `evaluated_depsgraph_get` werkt de graaf bij. | Vermoeden | Laag | `h_vlakken` is groter dan 0 in de run. |

## Deel B: houdt het zich aan onze regels?

| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Er is een nieuwe module (`betaald/omhulsel.py`) die een bestaande functie vervangt. `architectuur.md` staat niet in de gewijzigde bestanden. | Feit | Hoog | architectuur.md bijgewerkt |
| 2 | Er is geen toets bijgevoegd die de fix afdwingt. `meet_diag.py` krijgt alleen extra logvelden (`KEUS`). In deze tekst is niet te zien dat de e2e-workflow of de toetsen zijn aangepast. | Feit | Midden | Tests en bewijs |
| 3 | Er zijn geen tests aangepast om te slagen. | Feit | Hoog | Tests niet aangepast |
| 4 | Het nieuwe bestand is 120 regels, ruim onder de grens van ±400. | Feit | Hoog | Bestandsgrootte |
| 5 | Er staan geen persoonsgegevens, sleutels of wachtwoorden in de wijziging. | Feit | Hoog | Geen persoonsgegevens |
| 6 | De cijfers in de docstring zijn met GEZIEN gemarkeerd en hebben een runnummer. Ik kan ze hier niet nagaan. | Vermoeden | Midden | Cijfers met GEZIEN/DERDEN/GOK |

## Deel C: zou een gebruiker het leuk en fijn vinden?
Er zijn geen beelden of speelbare uitkomst meegestuurd, dus hier valt niets te zien.

| # | Bevinding | Wat het beter maakt | Moeite (klein/midden/groot) |
|---|---|---|---|
| 1 | Als de gebruiker merkt dat Figure from rig geen gewrichten meer overslaat, is dat de winst. Een voxel-H kan de vorm rond het snijvlak iets afronden en traag zijn bij grote figuren. Dat is niet te beoordelen uit tekst. | Een voor-en-na-schermafbeelding van de robotheup en de tijd per gewricht in de run. | Klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet**
1. Werk `architectuur.md` bij met `betaald/omhulsel.py`: wat het doet, dat het `een_lid._samen` vervangt, de terugval naar de oude weg en de instelling `AAN`.

**Kan**
1. Voeg een groene e2e-run toe als bewijs (rigtest op de robot, in 4.2 en 5.x, met `h_soort`, `h_voxel` en `h_buiten` in het log). Zonder die run blijft de oorzaak een vermoeden.
2. Maak een echte toets die faalt als een gewricht in Figure from rig wordt overgeslagen, in plaats van alleen extra logvelden.
3. Zet in `try/finally` het vrijmaken van de bmeshes (`a`, `b`), zodat een uitzondering ze niet laat hangen.
4. Voeg een regel toe aan het Pro-changelog (vanuit de gebruiker geschreven), want dit is zichtbaar gedrag.

---
Automatische keurder, model `claude-sonnet-5-5`, 21348 tokens in, 3600 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
