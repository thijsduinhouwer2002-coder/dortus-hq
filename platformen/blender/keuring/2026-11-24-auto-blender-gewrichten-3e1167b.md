# Keuring blender-gewrichten, Pro 1.2.4 (reden van de eerste plek in Figure from rig), 24-11-2026, automatische keurder
Wat ik keurde: commit d0cfb6e1e (bereik 446b13a..3e1167b), bestanden `betaald/rig.py` en `e2e/toetsen_rig.py`
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid (hoog/midden/laag) | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De nieuwe functie `reden_eerste` geeft de reden van de eerste kandidaat terug als die een van drie snede-fouten bevat, anders de laatste reden. De operator slaat die eerste melding op (`eerste_kand`, alleen bij `i == 0`) en gebruikt hem na het `eerste`-blok. | Feit (uit de diff) | Hoog | Niet nodig. |
| 2 | Direct daarna staat nog `if not ok and vangnet: melding = vangnet`. Als `vangnet` gevuld is, overschrijft dat de nieuwe keuze en doet de fix niets. In de diff zie ik niet wanneer `vangnet` gevuld is. | Vermoeden | Midden | Een run met het kleding-figuur in 4.2 waarin de lijst bij de rechterknie de snedefout toont. Of een toets die de operator doorloopt met een gevuld `vangnet`. |
| 3 | De drie zoekteksten ("overlap before they move", "no watertight parts", "the cut failed") komen overeen met de meldingen die de toets zelf als voorbeeld gebruikt. Of de echte meldingen in `figuur.plaats_gewricht` zo luiden, kan ik in deze diff niet zien. | Vermoeden | Midden | De meldingsteksten in `figuur.py` naast `SNEDE_MIS` leggen. |
| 4 | De opdracht (`ontwerp.md`, voor zover meegestuurd) noemt dit gedrag niet. Het akkoord daar gaat over gratis 0.1.1 en Pro 1.0.2. De bedoeling blijkt alleen uit het commitbericht en het commentaar. Het einde van het bereik (3e1167b) staat niet in de commitlijst. | Feit | Hoog | Een ontwerpregel of bericht van Thijs of Daan over de redenlijst van Pro 1.2.x. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | De toets is aangevuld met twee nieuwe controles. Bestaande toetsen zijn niet aangepast. | Feit | Hoog | Tests niet aangepast om te slagen: voldaan. |
| 2 | `rig.py` is groot (de diff laat regels rond 700 en 790 zien, dus ruim boven de 400) en groeit met ongeveer 20 regels. Het was al te groot. | Feit | Hoog | Bestanden onder ±400 regels: niet gehaald, maar niet door deze wijziging veroorzaakt. |
| 3 | `architectuur.md` is niet bijgewerkt. De regel over de keuze van de reden in Figure from rig staat daar waarschijnlijk wel (tekst afgekapt, dus onzeker). | Vermoeden | Midden | architectuur.md bijgewerkt. |
| 4 | Het commentaar noemt run 45295977807 zonder GEZIEN, DERDEN of GOK. De run is wel een eigen meting. | Feit | Hoog | Cijfers met GEZIEN/DERDEN/GOK (klein). |
| 5 | Ik zie geen persoonsgegevens, sleutels of AI-beeld of -geluid in de diff. | Feit | Hoog | Persoonsgegevens, Steam: voldaan. |
| 6 | De toets controleert alleen de losse functie met zelfgekozen teksten. De koppeling in de operator (punt A2) wordt niet getoetst. | Feit | Hoog | Toetsbaar bewijs. |

## Deel C: zou een gebruiker het leuk en fijn vinden? (alles wat je kunt zien of spelen)
| # | Bevinding | Wat het beter maakt | Moeite (klein/midden/groot) |
|---|---|---|---|
| 1 | De lijst noemt nu de echte oorzaak (snede mislukt) in plaats van "Tight ... Try a spot further from the end". Dat voorkomt dat de gebruiker op de verkeerde plek gaat zoeken. Of het zo in beeld komt, kan ik niet zien. | Een Xvfb-schermafbeelding van de lijst bij de rechterknie van het kleding-figuur. | Klein |
| 2 | "The parts overlap before they move; the mesh is unchanged." zegt niet wat de gebruiker kan doen. | Een handelingstip erbij, bijvoorbeeld de plek of de grootte aanpassen, of het lid apart nemen. | Klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Controleer of `vangnet` de nieuwe keuze niet overschrijft (A2), en toets de operatorketen met het kleding-figuur in 4.2 (B6).
- Leg de zoekteksten van `SNEDE_MIS` naast de echte meldingen in `figuur.py` (A3).
- Werk `architectuur.md` bij met de nieuwe volgorde van redenen (B3).
- Splits `rig.py` op, want het is veel groter dan 400 regels (B2).
- Voeg een handelingstip toe aan de overlapmelding (C2).
- Zet bij het run-nummer in het commentaar GEZIEN (B4).

---
Automatische keurder, model `claude-sonnet-5-5`, 19276 tokens in, 4099 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
