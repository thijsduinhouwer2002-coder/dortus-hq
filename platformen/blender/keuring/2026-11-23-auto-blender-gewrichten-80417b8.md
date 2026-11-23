# Keuring blender-gewrichten, 23-11-2026, automatische keurder
Wat ik keurde: commits 65159a5..80417b8 (80417b858), bestanden `click_joints/betaald/rig.py` en `e2e/toetsen_mens.py`
Akkoord: ja

## Deel A: doet het wat beloofd is?
De opdracht noemt deze wijziging niet. Ik toets haar daarom tegen de bedoeling in de commit: de knop "Figure from rig" zoekt verder na "no watertight parts", zodat CI en lokaal hetzelfde aantal gewrichten geven.

| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | Bij een melding met "no watertight parts" probeert de knop nu de volgende plek, net als bij "too close". De lus blijft begrensd: op de laatste kandidaat stopt hij. | Feit (uit de diff) | hoog | Niets nodig. |
| 2 | De aanname dat de mesh na zo'n mislukte snede ongewijzigd is, staat alleen in een opmerking ("gewricht.py zegt dat zelf"). Ik zie `gewricht.py` niet. | Vermoeden | midden | Een e2e-controle dat de mesh (punten-hash) na de mislukte snede gelijk is aan ervoor. |
| 3 | De oorzaak (één slechte rand per machine) is een verklaring van de bouwer. De test bootst die nep na en bewijst niet dat CI nu ook 9 haalt. | Vermoeden | midden | Een groene CI-run op het studio-figuur met 9 gewrichten. |
| 4 | De toets telt alleen of de nep één keer werd geraakt. Dat het daarna een andere plek van de linkerschouder werd gebruikt, of dat het totaal 9 is, staat niet in deze diff. | Feit | midden | Een check op het aantal gewrichten of de gekozen plek na de herkansing. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | De test wordt niet aangepast om te slagen. Er komt een extra geval bij en geen bestaande eis wordt verzwakt. | Feit | hoog | Tests niet aanpassen om te slagen: voldaan. |
| 2 | De toets draait alleen met `CJ_HERKANS=1`. De workflow staat niet in de wijziging. Het is dus onzeker of CI hem ooit aanzet. | Vermoeden | midden | Regel over toetsbaarheid: kijk of `CJ_HERKANS` in een workflow of script wordt gezet. |
| 3 | `rig.py` loopt in de diff al door tot regel 743 en is dus ver boven de ±400 regels. De wijziging verergert dat weinig (+6 regels). | Feit | hoog | Bestanden onder ±400 regels: al overschreden, nu niet nieuw. |
| 4 | `architectuur.md` is niet bijgewerkt voor dit nieuwe zoekgedrag. In het stuk dat ik zie staat de rig-knop niet, dus ik kan niet zeker zijn. | Vermoeden | laag | Regel: architectuur.md bijwerken. Kijk of daar de "verder"-regel voor de rig staat. |
| 5 | De opmerking "CI 8, lokaal 9" is een cijfer zonder label GEZIEN of DERDEN. | Feit | hoog | Cijfers met GEZIEN/DERDEN/GOK. |
| 6 | Er staan geen persoonsgegevens, sleutels of wachtwoorden in de diff. | Feit | hoog | Geen persoonsgegevens: voldaan. |
| 7 | Dit is betaald werk (`betaald/`). Het gratis `CHANGELOG.md` hoeft dus niet mee. | Feit | midden | Twee builds, gratis zip bevat geen betaalde modules. |

## Deel C: zou een gebruiker het leuk en fijn vinden?
Ik zie geen beeld of spel, dus dit is alleen uit de tekst.

| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | De gebruiker krijgt na deze wijziging vaker alle gewrichten van een figuur. Dat is een duidelijke winst. | Niets nodig. | klein |
| 2 | Verschuift de knop stil een gewricht naar een andere plek na een mislukte snede, dan merkt de gebruiker dat misschien niet. | Een korte melding "Left shoulder: moved to a nearby spot". | klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Zet `CJ_HERKANS=1` in de workflow of het e2e-script, als dat nog niet gebeurt, zodat de toets echt draait.
- Voeg een check toe dat na de herkansing het volgende kandidaat-punt wordt gebruikt en dat het totaal 9 is.
- Controleer in de e2e dat de mesh na een mislukte snede ongewijzigd is (punten-hash).
- Zet GEZIEN of DERDEN bij het cijfer "CI 8 tegen lokaal 9".
- Werk `architectuur.md` bij met het nieuwe zoekgedrag van "Figure from rig".
- Splits `rig.py` op, want het bestand is veel groter dan ±400 regels.
- Meld de gebruiker als een gewricht naar een andere plek is geschoven.

---
Automatische keurder, model `claude-sonnet-5-5`, 18496 tokens in, 3138 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
