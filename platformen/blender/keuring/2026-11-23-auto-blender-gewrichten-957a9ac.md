# Keuring blender-gewrichten, Click Joints Pro 1.2.2 (terugval Exact en Figure from rig), 23-11-2026, automatische keurder
Wat ik keurde: commits 542c4be..957a9ac (957a9ac87, 3cf0d7d83, 80417b858), alleen de zes meegestuurde bestanden
Akkoord: ja

## Deel A: doet het wat beloofd is?
Het ontwerp in `ontwerp.md` beschrijft de gratis 0.1.1 en Pro 1.0.2. Voor deze Pro-spoor 1.2.2 (Olaf) stond er geen eigen opdracht bij. Ik toets daarom tegen de commitberichten en de uitleg in `architectuur.md`.

| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | `terugval.py` omhult nu ook `gewricht.markeer`. Een deel met `cj_solver_terugval` krijgt daardoor `cj_solver` EXACT. Dat repareert dat de operator de solver pas na de snede zet, met de eerste solver. | Feit (uit de diff) | Hoog | De toets controleert nu `solvers == [verwacht] * 2`. Een groene run op 5.2.3 en 5.3.0 bevestigt het. |
| 2 | De toets in `toetsen_correcties.py` is strenger geworden, niet losser. Hij test 0, 1 en 2 keer open, met solver MANIFOLD, EXACT en een nette weigering (figuur heel, zichtbaar, geen hulpresten). | Feit | Hoog | Dezelfde groene run. |
| 3 | `rig.py` zoekt na "no watertight parts" nu een volgende plek, net als bij "too close". De mesh blijft dan onveranderd volgens de code-opmerking, en de nepsnede in de toets sluit dat niet uit. | Feit voor de code, vermoeden voor het effect (CI 9 in plaats van 8 gewrichten) | Midden | Een CI-run met `CJ_HERKANS=1` waarin het log 9 gewrichten toont en `nep == ["Left shoulder"]` slaagt. |
| 4 | De nieuwe herkansingstoets draait alleen als `CJ_HERKANS=1` is gezet. De workflow staat niet in de wijziging. | Vermoeden | Midden | Een regel `CJ_HERKANS: "1"` in de workflow, of een logregel van de nieuwe stap `mislukte snede nagedaan`. |
| 5 | In `_snij` staat nu `global FORCEER_OPEN` midden in de functie. Gebruikt het ongeziene stuk erboven de naam al, dan is dat in Python een SyntaxError en laadt het hele betaalde deel niet. | Vermoeden | Laag | Een groene Pro-run waarin `solver_terugval` draait. Een import-fout zou al bij het laden rood zijn. |
| 6 | De handtekening van `_markeer(ob, kleur, gegevens, maat=None, u=1.0)` moet gelijk zijn aan die van `gewricht.markeer`. Dat is in de wijziging niet te zien. | Vermoeden | Laag | De bestaande kern- en scharniertoetsen in dezelfde run. |

## Deel B: houdt het zich aan onze regels?

| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Er is geen test losser gemaakt om te slagen. De terugvaltoets is uitgebreid en zijn eis aangescherpt. | Feit | Hoog | Tests niet aanpassen om te slagen |
| 2 | `architectuur.md` beschrijft `terugval.py` bijgewerkt: de omhulling van `markeer`, de volgorde en de testhaak. De nieuwe zoekregel in `rig.py` (doorgaan na "no watertight parts") staat er niet in. | Feit | Midden | architectuur.md bijwerken |
| 3 | `rig.py` is ruim boven de ±400 regels (de wijziging zit rond regel 743). Dat was al zo en dit maakt het niet veel erger. | Feit | Hoog | Bestanden onder ±400 regels |
| 4 | De gratis `gewricht.py` is niet geraakt, dus de gratis zip blijft gelijk (`toets_zips.py`). In de Pro-code komen geen verboden woorden in de gratis build terecht. | Feit | Hoog | Twee builds uit één bron |
| 5 | In de wijziging staan geen persoonsgegevens, sleutels of wachtwoorden. | Feit | Hoog | Geen persoonsgegevens |
| 6 | De opmerking "CI 8 tegen lokaal 9" heeft geen label GEZIEN, DERDEN of GOK. | Feit | Hoog | Cijfers met label |
| 7 | De volgorde bij afmelden (omgekeerd) staat in de uitleg. De `unregister` in `__init__.py` is niet meegestuurd en dus niet te controleren. | Vermoeden | Midden | architectuur.md klopt met de code |

## Deel C: zou een gebruiker het leuk en fijn vinden?
Dit is werk aan de achterkant, ik kan hier niets zien of spelen. Het is een vermoeden dat een gebruiker er alleen iets van merkt doordat er minder vaak "no watertight parts" komt.

| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | De terugval naar Exact gebeurt stil. Het enige spoor is `cj_solver_terugval` op de delen. | Een korte regel in het paneel, bijvoorbeeld "Cut redone with the slower solver", zodat de gebruiker begrijpt waarom het even langer duurde. | klein |
| 2 | Bij Figure from rig slaat de knop nu een plek over. Zegt de samenvatting niet welke plek werd overgeslagen, dan weet de gebruiker niet waarom een gewricht ergens anders zit. | De overgeslagen plek in de melding noemen. | klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Controleer in de workflow dat `CJ_HERKANS=1` is gezet, anders draait de herkansingstoets niet (A4).
- Laat de run zien dat de `global`-regel in `_snij` en de handtekening van `_markeer` kloppen (A5, A6). Het gaat om een groene Pro-run op 5.2.3 en 5.3.0.
- Voeg de zoekregel na "no watertight parts" toe aan `architectuur.md` (B2).
- Controleer de volgorde van afmelden in `__init__.py` (B7).
- Splits `rig.py` op, het bestand is ruim boven de ±400 regels (B3).
- Voeg bij "CI 8 tegen lokaal 9" een label toe (B6).
- Overweeg de twee kleine gebruikersmeldingen uit deel C.

---
Automatische keurder, model `claude-sonnet-5-5`, 26136 tokens in, 6240 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
