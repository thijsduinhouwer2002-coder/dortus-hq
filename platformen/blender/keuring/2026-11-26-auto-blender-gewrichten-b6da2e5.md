# Keuring blender-gewrichten, plaatje 20 Check parts (e2e/scherm_check.py), 26-11-2026, automatische keurder
Wat ik keurde: commit b6da2e554 (bestand `producten/blender-gewrichten/e2e/scherm_check.py`, nieuw, 115 regels)
Akkoord: ja

## Deel A: doet het wat beloofd is?
Er is geen tekst van issue 42 meegestuurd. Ik toets tegen de commitregel ("schermbeeld 20 van Check parts in de e2e") en de kop van het script.

| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | Het script bouwt een staaf met kogel, zet Min wall net boven de gemeten wand, draait Check parts en opent deel B in Edit Mode. Daarna maakt het een hele schermafbeelding en een uitsnede van de zijbalk, één keer boven (20a) en één keer omlaag gescrold (20). Dat past bij de kop. | Feit (uit de tekst) | Hoog | n.v.t. |
| 2 | De regel "CHECK BEELD OK" eist een dunne wand op B (`dun > 0`), de operator `check_toon` met FINISHED, modus EDIT_MESH, actief object Arm_B en beide uitsneden. Dat is een echte controle, geen vinkje om te slagen. | Feit | Hoog | n.v.t. |
| 3 | Het script staat niet in een workflow die ik in deze wijziging zie. Of de e2e het draait, hangt dus af van een bestaande workflow die alle `scherm_*.py` pakt. | Vermoeden | Midden | Een regel in `.github/workflows/` die `scherm_check.py` noemt, of een logregel "CHECK BEELD OK" in een groene run. |
| 4 | Het script leunt op `scherm_basis` (`log`, `open_paneel`, `schiet`, `toestand`, `uitmap`, `wiel_naar_tabblad`, `zijbalk`, `zip_pad`) en op `figuren.staaf`, `mm_scene` en `zet_cursor`. Die zie ik niet. | Vermoeden | Midden | Die bestanden bestaan met deze namen, of een groene run. |
| 5 | Het scrollen naar stap 3 gebeurt blind met 25 muiswielklikken. Of Check parts dan echt in beeld staat, zie ik niet. | Vermoeden | Midden | Plaatje 20-check-paneel.png bekijken met de Read-tool. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Er is geen bestaande test aangepast. Er is alleen een nieuw script toegevoegd. | Feit | Hoog | Tests niet aangepast om te slagen |
| 2 | Het bestand is 115 regels. | Feit | Hoog | Bestanden onder ±400 regels |
| 3 | Er staan geen persoonsgegevens, sleutels of wachtwoorden in. | Feit | Hoog | Geen persoonsgegevens |
| 4 | `architectuur.md` is niet bijgewerkt. Het is een testscript en geen onderdeel van de add-on, dus dat hoeft hier niet per se. Staat er een lijst met e2e-scripts in `architectuur.md`, dan hoort dit script daar bij. | Vermoeden | Laag | architectuur.md bijgewerkt |
| 5 | Er staan geen cijfers voor de winkel in, geen spelerstekst en geen AI-beeld of -geluid. | Feit | Hoog | GEZIEN/DERDEN/GOK, Steam |

## Deel C: zou een gebruiker het leuk en fijn vinden?
Er zijn geen beelden meegestuurd en het script zelf is geen klantproduct. Ik kan hier niets zien.

| # | Bevinding | Wat het beter maakt | Moeite (klein/midden/groot) |
|---|---|---|---|
| 1 | Het plaatje is bedoeld voor Daan. Of de rode dunne vlakken in Edit Mode op het plaatje leesbaar zijn, is niet te zien. | Daan bekijkt 20 en 20a. Zijn de dunne vlakken niet goed te zien, dan de kijkhoek of de afstand (`view_distance = 45`) aanpassen. | klein |
| 2 | Het blinde scrollen kan een plaatje geven waarop Check parts net buiten beeld valt. | Scrollen tot de knop in beeld is, of een vaste scrollpositie instellen. | klein |

## Deel C: is het goed genoeg?
Dit is een test- en keuringsplaatje en geen beeld dat een klant als eerste ziet. De blinde test is dus niet van toepassing. Zonder beeld en zonder concurrentievoorbeeld geef ik geen cijfers.

| Vraag | Cijfer 1 tot 10 | Waarom, en waarmee vergeleken |
|---|---|---|
| Ziet het er top uit, op het niveau van de beste in de winkel? | niet te beoordelen | Geen beeld ontvangen. Het gaat niet naar de winkel zonder keuring van Daan. |
| Zou ik het zelf kopen of bekijken op basis van dit? | niet te beoordelen | Zelfde reden. |
| Zou Thijs er trots op zijn? | niet te beoordelen | Zelfde reden. |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
1. Zet de timerstappen in een `try/finally` die `bpy.ops.wm.quit_blender()` aanroept. Gaat de installatie van de zip of `bouw()` mis, dan stopt de timer met een fout en blijft Blender in de e2e hangen tot de timeout, zonder duidelijke logregel.
2. Eis dat `wiel_naar_tabblad()` is gelukt voordat het plaatje wordt geschoten. Na `n >= 20` gaat het script nu gewoon door.
3. Controleer of de workflow dit script echt draait (zie A3 en A4).
4. Laat Daan 20 en 20a bekijken op leesbaarheid, want beeld keur ik niet.

---
Automatische keurder, model `claude-sonnet-5-5`, 20037 tokens in, 3525 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
