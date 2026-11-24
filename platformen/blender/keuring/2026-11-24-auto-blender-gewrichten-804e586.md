# Keuring blender-gewrichten Pro 1.2.8, 24-11-2026 22:12 NL, automatische keurder
Wat ik keurde: commits 098fee7..804e586 (e9fa8d397, 64e1eefbe, 6c671a6e1), vijf bestanden, alleen de tekst van de wijziging
Akkoord: ja

## Deel A: doet het wat beloofd is?
Beloofd (commit en ontwerpregel): een scharnier precies op het midden van de robotknie hoort te lukken, en de rand van de kniekap telt niet als onderkant van het lid.

| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | `zaag_diepte` slaat de randstralen over als het midden onder de volle sleuf nog doorloopt (`nodig`) en het lid daar aan beide kanten minstens half zo breed is als bij H (`_anker_breed`). Dat past bij de beschreven oorzaak: een uitstekende rand telt niet als onderkant. | Feit (code gelezen) | hoog | Groene run van `toetsen_knie_midden` op beide knieën, midden en 12 mm hoger. |
| 2 | Of het midden van de robotknie nu echt een groen scharnier geeft, is uit de tekst niet te halen. Er staat geen uitslag in de wijziging, alleen "lokaal gemeten" in de commit. | Vermoeden | midden | Het log met `KLAAR 0 FOUT` in 4.2.23, 5.2.3 en 5.3.0. |
| 3 | In Blender 4.2 mag de toets op 12 mm hoger de melding "mesh is unchanged" accepteren zonder delen. 1.2.7 deed dat ook, dus het is geen nieuwe fout. Een koper op 4.2 krijgt daar nog steeds geen scharnier. | Feit (code), oorzaak is vermoeden | hoog | Een reproductie op 4.2 en een besluit of dit een bekende beperking blijft. |
| 4 | De nieuwe parameter `u` in `zaag_diepte` is in beide aanroepers meegegeven (`scharnier.py`, `hulp_neus.py`). De standaardwaarde 1.0 geeft verkeerde maten als een andere aanroeper hem vergeet in een scene in meters. | Feit (diff), andere aanroepers onbekend | midden | Zoeken naar andere aanroepen van `zaag_diepte` in de repo. |
| 5 | Een lid dat onder H smaller wordt en toch aan beide kanten half zo breed blijft, kan nu zonder randstraal een sleuf krijgen die dichter bij een schuine rand komt. De beschrijving zegt dat de wang dan nog aan het lid eronder hangt. | Vermoeden | laag | Een toets op een lid met een uitstekende rand dichtbij, bijvoorbeeld een kleinere robot of een gebogen been. |

## Deel B: houdt het zich aan onze regels?

| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | `architectuur.md` is bijgewerkt: 1.2.8, `_anker_breed` en de toets staan erin. De uitzondering voor 4.2 (geen scharnier op 12 mm hoger) staat er niet in. | Feit | hoog | architectuur.md bijgewerkt (gedeeltelijk) |
| 2 | Er zijn geen bestaande toetsen aangepast om te slagen. De 4.2-uitzondering zit in een nieuwe toets, is in een commentaar uitgelegd en hoort bij een eerder bestaand gedrag. | Feit | midden | Tests niet aangepast om te slagen |
| 3 | `toetsen_knie_midden.py` is niet aangeroepen vanuit `test_betaald.py` of een workflow in deze wijziging, en gebruikt een map buiten de productmap (`commercie/filmpjes/studio`). Misschien draait hij in CI via een eerder commit. Anders bewaakt niets deze fix automatisch. | Vermoeden | midden | Toetsbaar in de echte Blender op Actions (ontwerp) |
| 4 | De commits heten "Pro 1.2.8", maar `blender_manifest.toml` en een changelog staan niet in de wijziging. Het versienummer is misschien niet verhoogd. | Vermoeden | laag | Versie en uitgave kloppen |
| 5 | `toetsen_knie_midden.py` is 132 regels. De 400-regelgrens voor `scharnier_neus.py` kan ik niet nagaan. Die file wordt in elk geval groter. | Vermoeden | laag | Bestanden onder ±400 regels |
| 6 | Er staan geen persoonsgegevens, sleutels of wachtwoorden in de wijziging. | Feit | hoog | Geen persoonsgegevens |
| 7 | De cijfers in de nieuwe tekst ("lokaal gemeten", "19 mm onder H", "12 mm hoger") hebben geen GEZIEN, DERDEN of GOK. Het commentaar in de toets noemt wel GEZIEN en een run. | Feit | midden | Cijfers met GEZIEN/DERDEN/GOK |

## Deel C: zou een gebruiker het leuk en fijn vinden?

| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | Een koper klikt vanzelf op het midden van de knie. Als dat nu werkt, is dat een duidelijke verbetering. Of het werkt, kan ik niet zien. | Een schermafbeelding van het scharnier op de robotknie op het midden. | klein |
| 2 | Op Blender 4.2 krijgt een koper op 12 mm hoger een melding over een ongewijzigde mesh. Dat zegt niet wat hij moet doen. | Een melding met een tip, bijvoorbeeld de cursor iets verplaatsen, of dit oplossen op 4.2. | midden |
| 3 | Beeld en speelplezier kan ik niet beoordelen. Er is geen beeld meegestuurd en deze wijziging verandert geen beeld dat een klant als eerste ziet. Cijfers 1 tot 10 geef ik daarom niet. | Daan of Iris keuren het uiterlijk van het scharnier bij de volgende uitgave. | klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Haak `toetsen_knie_midden` aan een bestaande e2e-run, of laat zien dat hij al draait. Zet er de groene run bij met 4.2.23, 5.2.3 en 5.3.0.
- Schrijf in `architectuur.md` dat 12 mm hoger op Blender 4.2 geen scharnier geeft en alleen een melding.
- Controleer of het versienummer (manifest) naar 1.2.8 is gegaan en of er een uitgavenotitie is.
- Controleer of `zaag_diepte` nog ergens zonder `u` wordt aangeroepen.
- Voeg GEZIEN of GOK toe aan de gemeten getallen in de commits en de tekst.

---
Automatische keurder, model `claude-sonnet-5-5`, 29487 tokens in, 5146 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
