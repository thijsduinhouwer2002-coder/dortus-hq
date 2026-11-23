# Keuring blender-gewrichten (Click Joints Pro, herstel en leesbare reden), 23-11-2026, automatische keurder
Wat ik keurde: commit 3ac8b893b (fc5b58f..3ac8b89), vijf bestanden in `click_joints/betaald/`
Akkoord: nee

## Deel A: doet het wat beloofd is?
Getoetst aan `ontwerp.md`: twee gesloten delen per gewricht, een nette melding in plaats van een kapot model, Engelse tekst voor de koper.

| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | `herstel.py` splitst een paar randen met 4 vlakken met `bmesh.ops.split_edges` en eist daarna dat elke rand 2 vlakken heeft en het volume positief is. Dat is de bedoelde oplossing voor "no watertight parts" bij Exact op 4.2. | Feit (code) | Hoog | Geen. |
| 2 | Niets in de wijziging laat zien dat het herstel werkt. Of `split_edges` bij een rand met 4 vlakken er twee randen met elk 2 vlakken van maakt, is hier niet te zien. De controle `goed` voorkomt kapotte meshes, maar het herstel kan stilletjes nooit slagen. | Vermoeden | Midden | Een groene run in 4.2.23 met een deel dat zo'n rand heeft: `cj_herstel_randen` is groter dan 0 en het deel is daarna gesloten. |
| 3 | De punten blijven na het splitsen waarschijnlijk op dezelfde plek, dus de vorm verandert niet. In de STL kan de rand dan nog steeds als 4-vlaksrand overkomen, ook al telt de add-on hem als gesloten. | Vermoeden | Laag | Exporteer zo'n deel naar STL en laad hem in een slicer of met een controle op de losse driehoeken. |
| 4 | `herstel.herstel` importeert `from ..gesloten import is_gesloten`. In `terugval.py` staat `_gw[0].is_gesloten` (de gewrichtsmodule). In het gezien deel van `architectuur.md` staat geen `gesloten.py`. Bestaat dat bestand niet, dan geeft elke scharniersnede een ImportError. Dat vangt `except RuntimeError` in `scharnier.py` niet op. | Vermoeden | Midden | Zie of `click_joints/gesloten.py` bestaat, en een groene run waarin `scharnier.py` het herstel echt aanroept. |
| 5 | `redenen.leesbaar` vertaalt twee technische snijmeldingen naar een zin met een tip (met de hand een paar mm verder plaatsen). Op Blender 4.2 tot 4.4 komt daar "use Blender 4.5 or newer" bij. De zinnen zijn gewoon Engels. | Feit (code) | Hoog | Geen. |
| 6 | "It would be blocked" is een geometrieprobleem en geen snijfout, maar krijgt ook het advies voor Blender 4.5. De docstring zegt juist dat meldingen over geen ruimte ongewijzigd blijven. | Feit (code) | Hoog | Een test van `leesbaar("...it would be blocked...")` op 4.2, met de uitkomst in het log. |
| 7 | Het advies dat 4.5+ betrouwbaarder snijdt, rust op de release notes van Blender (derden) en op het ontwerp. De metingen in de docstring zijn alleen met Exact gedaan. | Vermoeden | Midden | Dezelfde snede op 4.5+ met de Manifold-solver, zonder open delen. |

## Deel B: houdt het zich aan onze regels?

| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Geen test in de wijziging voor `herstel.py` of `redenen.py`. Er zijn dus geen groene resultaten voor deze code. De runs in de docstring (45255097554, 45256924126) staan op een andere tak en tonen alleen het probleem. | Feit | Hoog | Eisen in `ontwerp.md` moeten toetsbaar zijn in de echte Blender op Actions. |
| 2 | Er is geen test aangepast om te slagen. | Feit | Hoog | Tests niet aanpassen om te slagen. |
| 3 | `architectuur.md` is niet bijgewerkt, terwijl er twee nieuwe modules zijn: `betaald/herstel.py` en `betaald/redenen.py`. Misschien staat de Pro-architectuur in een ander bestand dat hier niet is meegestuurd. | Vermoeden | Midden | architectuur.md bijgewerkt. |
| 4 | `rig.py` heeft minstens 780 regels (de hunk begint bij regel 780). Dat was al zo. De bouwer zette de nieuwe code wel in aparte kleine bestanden (43 en 32 regels). | Feit | Hoog | Bestanden onder ±400 regels. |
| 5 | Cijfers in `herstel.py` hebben een bron (GEZIEN met run-id's). Het getal "27 tot 93 mm" en de runs kan ik niet nakijken. | Vermoeden | Laag | Cijfers met GEZIEN, DERDEN of GOK. |
| 6 | Geen persoonsgegevens, sleutels of wachtwoorden in de wijziging. Geen AI-beeld of -geluid. | Feit | Hoog | Geen persoonsgegevens. |

## Deel C: zou een gebruiker het leuk en fijn vinden?

| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | De nieuwe reden zegt wat de koper moet doen, in gewoon Engels. Dat is een stuk bruikbaarder dan de oude technische zin. | Niets nodig. | klein |
| 2 | De tip "place it by hand a few mm along the bone" laat de koper het zelf proberen. Dat is saai en lastig voor iemand met veel gewrichten. | Figure from rig laat zelf een of twee keer een kleine verschuiving langs het bot proberen voordat het opgeeft. | midden |
| 3 | Een lange reden in een lijst wordt snel afgekapt in de smalle zijbalk (vermoeden: de tekst is bijna 150 tekens). | Kijk op een scherm of de regel leesbaar blijft, en kort hem zo nodig in. | klein |
| 4 | Het Blender 4.5-advies helpt alleen wie kan upgraden. Een koper met een vaste Blender (bijvoorbeeld door andere add-ons) heeft er niets aan. | Zet in de productbeschrijving dat Pro het best werkt op 4.5+. | klein |

## Moet (blokkeert akkoord) / Kan (mag later)

**Moet**
1. Bewijs dat de nieuwe code draait en werkt. Dat is een groene run in 4.2.23 met een test die de uitkomst van `herstel` toont: `cj_herstel_randen` en `is_gesloten` voor en na. Controleer daarbij dat `click_joints/gesloten.py` bestaat; zo niet, gebruik dezelfde import als `terugval.py` (A4, A2, B1). Het herstel zit nu op de weg van elke scharniersnede en een ImportError wordt niet opgevangen.

**Kan**
1. Laat "it would be blocked" ongewijzigd, of laat de Blender 4.5-tip bij die melding weg (A6).
2. Controleer of de herstelde delen als STL en in een slicer ook gesloten zijn, en niet alleen in de eigen telling (A3).
3. Werk `architectuur.md` bij met `herstel.py` en `redenen.py` (B3).
4. Splits `rig.py` verder, want het is ruim boven ±400 regels (B4).
5. Overweeg een automatische verschuiving langs het bot als eerste herstelpoging (C2).
6. Toets op een scherm of de lange reden leesbaar blijft (C3).

---
Automatische keurder, model `claude-sonnet-5-5`, 20653 tokens in, 8251 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
