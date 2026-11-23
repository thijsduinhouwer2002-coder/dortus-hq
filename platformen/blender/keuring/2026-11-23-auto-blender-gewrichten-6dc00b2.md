# Keuring omhulsel: voxel-H alleen bij mislukte vereniging met Manifold, 23-11-2026, automatische keurder
Wat ik keurde: commit 6dc00b290 (78ac6d9..6dc00b2): `betaald/omhulsel.py`, `architectuur.md` en `proeven/betrouwbaar-rig-2026-11-23/uitslag.md`
Akkoord: ja

## Deel A: doet het wat beloofd is?
Opdracht: de commitregel (met Manifold alleen voxel bij een mislukte vereniging, met Exact altijd) en de bijstelling in uitslag.md.

| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De logica in `samen_schoon` doet wat de commitregel zegt. Bij Exact gaat het altijd naar `voxel_h`, met de oude weg als terugval. Bij Manifold gaat het eerst naar de oude vereniging, en alleen bij `h_soort == "los"` naar de voxelvorm. | Feit (uit de diff) | Hoog | n.v.t. |
| 2 | Bij Manifold wordt `voxel_h` aangeroepen met `Matrix.Identity(4)`. Dat klopt alleen als `_oud[0]` `hb` en `lb` echt naar wereldcoördinaten omzet, zoals het commentaar zegt. Dat staat niet in de diff. | Vermoeden | Midden | Een toets of meting waarbij de Manifold-tak "los" haalt en de voxel-H op de juiste plek ligt (overlap van A en B in rust is nul). |
| 3 | De nieuwe tak leest `_l.LAATSTE.get("h_soort")` direct na de oude vereniging. Wordt `LAATSTE` per snede niet eerst leeggemaakt, dan kan een oude waarde "los" onterecht de voxeltak starten. | Vermoeden | Laag | De plek in `een_lid.py` waar `LAATSTE` wordt gereset, of een toets met twee sneden na elkaar. |
| 4 | `from ..gewricht import solver_naam` komt uit een bestand dat niet in de diff staat. Bestaat de functie niet, dan faalt elke Pro-snede. De diff laat niet zien of dit is gedraaid. | Vermoeden | Midden | Een groene run in 4.2.23 en 5.2.3 op deze commit, of een zoekopdracht naar `solver_naam` in `gewricht.py`. |
| 5 | De reden voor de wijziging (Meshy-knight verliest met altijd voxel 8,2 tot 9,2% van de punten, tegen 5,3 tot 5,6% zonder) is bij run 45264302449 gezien, maar die run draaide de oude code. Een run op de nieuwe code staat niet in de stukken. | Feit (reden), vermoeden (dat het nu goed is) | Midden | Een nieuwe run van `betrouwbaar-rig.yml` met de knight onder de 6% en nul slechte sneden in 5.x. |
| 6 | Na de terugval van Pro 1.2.2 staat `STAND["solver"]` op EXACT. Leest `solver_naam()` dat, dan gaat de herhaalsnede door de voxeltak, wat logisch is. Leest hij de Blender-versie, dan niet. | Vermoeden | Laag | De toets `solver_terugval` met de voxelmeting erbij. |

## Deel B: houdt het zich aan onze regels?

| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Er zijn geen tests aangepast, en er zijn er ook geen bij gekomen of gedraaid voor dit gedrag. De meetlat (`meet_drempel.json`) staat niet in de diff, dus er is niets versoepeld. | Feit | Hoog | Tests niet aangepast om te slagen: ok. |
| 2 | `architectuur.md` en `uitslag.md` zijn bijgewerkt met de nieuwe regel "Wanneer". | Feit | Hoog | architectuur.md bijgewerkt: ok. |
| 3 | De zin "elke H in de eindmeting is voxel, nul slechte sneden in 5.x" staat nog bovenaan in uitslag.md. Met Manifold is H nu meestal niet meer voxel. De zin eronder corrigeert dat, maar het "nul slechte sneden" geldt nu voor oude code. | Feit | Hoog | Cijfers met GEZIEN/DERDEN/GOK: de oude meting mag niet voor de nieuwe code doorgaan. |
| 4 | De cijfers 8 tot 9% en 5,6% in de code en in architectuur.md noemen de run, maar architectuur.md zet er geen GEZIEN bij. In uitslag.md staat het wel. | Feit | Midden | Cijfers met GEZIEN/DERDEN/GOK. |
| 5 | In de diff komen geen persoonsgegevens, sleutels of wachtwoorden voor. De bestandsgrootte van `omhulsel.py` is niet te zien, maar de wijziging is klein. | Feit (persoonsgegevens), vermoeden (400 regels) | Midden | Geen persoonsgegevens, bestanden onder ±400 regels. |
| 6 | Alleen `betaald/` verandert. De gratis zip en `gewricht.py` blijven gelijk, dus `toets_zips.py` blijft naar verwachting groen. | Vermoeden | Midden | Gratis deel ongewijzigd (014172e). |

## Deel C: zou een gebruiker het leuk en fijn vinden?
Er is niets te zien of te spelen in deze wijziging, dus ik kan alleen redeneren.

| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | Een koper met Blender 4.2 (Exact) krijgt altijd voxel-H. Zijn knie kan dan meer materiaal verliezen (8 tot 9%) dan op 5.x (±5,6%). Hetzelfde figuur geeft dus per Blender-versie een ander resultaat. | Meet de punten-verlies ook in 4.2 en noem het in de lijst "Skipped" of de uitgavenotities, of zoek een verfijning voor 4.2. | Midden |
| 2 | Het gewricht kan na deze keuze op 5.x in een holte lichter of anders klikken dan op 4.2. De koper merkt dat pas na het printen. | Toon in het paneel of de uitslag welke H-soort is gebruikt (`h_soort`). | Klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
1. Draai `betrouwbaar-rig.yml` opnieuw op deze commit (4.2.23, 5.2.3, 5.3.0) en zet het resultaat in uitslag.md. Het zou bevestigen dat de knight onder de 6% blijft en dat er nul slechte sneden zijn (Deel A 5).
2. Controleer dat `solver_naam` bestaat in `gewricht.py` en dat `LAATSTE` per snede wordt gereset (Deel A 3 en 4). Een groene run in 4.2 en 5.x dekt dat meteen af.
3. Pas de zin "elke H in de eindmeting is voxel, nul slechte sneden in 5.x" aan, zodat hij niet meer naar de oude code verwijst (Deel B 3).
4. Zet GEZIEN of DERDEN bij de procenten in architectuur.md (Deel B 4).
5. Voeg een toets toe voor de Manifold-tak met `h_soort == "los"` (voxel-H op de goede plek, delen gesloten, geen overlap in rust), zodat die tak niet alleen via de meetrun gedekt is.

---
Automatische keurder, model `claude-sonnet-5-5`, 23588 tokens in, 5006 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
