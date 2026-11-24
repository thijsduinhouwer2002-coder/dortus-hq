# Keuring blender-gewrichten Pro 1.2.5 proef, 24-11-2026, automatische keurder
Wat ik keurde: commit 485d31e1b (e97cf30..485d31e), bestanden `betaald/rig.py` en `betaald/scharnier_vorm.py`
Akkoord: nee

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De enkel gebruikt nu de assen van het scheenbot op de plek van de enkel, zodat deel A de scheen is en deel B de voet. Dat past bij het doel "alle ledematen in één keer" en bij de aanleiding (robot en MakeHuman kregen nooit een enkel). | Feit (uit de diff en de commentaar) | Hoog | Een run met een rig waarop ANKLE twee gesloten delen geeft. |
| 2 | `m.col[3][:3] = (...)` zet de plek van de enkel via een slice op een kolom. Of dat de matrix echt verandert, kan ik niet zien. Als het een kopie is, blijft de plek van het scheenbot staan en zit de enkel op de verkeerde plek. | Vermoeden | Laag tot midden | Een log of beeld met de gemeten plek van de cursor ten opzichte van de enkel. |
| 3 | Het scheenbot is het bot waarvan `pb` de ouder is. Dat hoeft niet de scheen te zijn (extra helperbotten, andere rigs). Of de lidas "omlaag" wijst, hangt af van wat `cursor_matrix` voor een ouderbot teruggeeft. | Vermoeden | Midden | Een proef op de robot, MakeHuman en een rig met een tussenbot, met de as in het log. |
| 4 | De afstandsregel tussen twee scharnieren is losser gemaakt van 2·max(r, eigen) naar r + eigen + 1 mm. Alleen als de twee reiken meer dan 1 mm verschillen is dat losser. Bij gelijke reiken is het 1 mm strenger. De commentaar noemt het een proef en zegt dat de reden van de oude regel nog niet is nagemeten. | Feit (rekensom uit de diff) | Hoog | Een meting op knie en enkel op 35 mm afstand met de oude en nieuwe regel, met delen die gesloten blijven en geen stopvlak dat tegen het schuine vlak loopt. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Er staat geen test in de wijziging voor de enkel of de nieuwe afstandsregel. Het enige "bewijs" is de commentaar. | Feit | Hoog | Toetsbaar in de echte Blender: gesloten delen en gemeten speling |
| 2 | `architectuur.md` is niet meegewijzigd. Daar staan `te_dicht` en de rig-opbouw beschreven, en de enkelregel en de nieuwe afstandsregel horen erbij. | Feit voor deze diff | Hoog | architectuur.md bijgewerkt |
| 3 | Het akkoord van Daan in `ontwerp.md` dekt Pro 1.0.2. Voor 1.2.5 zie ik in het stuk dat ik kreeg geen akkoord, maar het stuk is afgekapt. | Vermoeden | Midden | Akkoord ja bovenaan ontwerp.md voor wat naar Superhive gaat |
| 4 | Er staan geen persoonsgegevens of sleutels in de diff. De naam "Olaf" in de commentaar is een rolnaam. De bestanden zijn kort genoeg. | Feit | Hoog | Geen persoonsgegevens |

## Deel C: zou een gebruiker het leuk en fijn vinden?
Ik kan alleen tekst zien, dus geen beeld of spel.
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | Een enkel die eindelijk werkt op robot en MakeHuman maakt "alle ledematen in één keer" geloofwaardiger. | Een plaatje van een complete figuur met enkels in de winkel, pas na een kijk door Daan | Klein |
| 2 | Als de regel te los blijkt, krijgt de koper een gesneden figuur met een kapot gewricht in plaats van een nette melding. | De melding "Too close to another joint" behouden tot de meting er is | Klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet**
1. De afstandsregel `te_dicht` is losser gemaakt terwijl de commentaar zegt dat de reden van de oude regel nog niet is nagemeten. Het risico is twee delen die niet gesloten zijn of een stopvlak dat tegen het schuine vlak loopt. Meet dit eerst, met knie en enkel op ±35 mm, delen gesloten en speling binnen de eis. Of houd de oude regel tot dan toe en zet de proef achter een aparte schakelaar of tak.
2. Er is geen test voor het nieuwe gedrag (enkel via het scheenbot, nieuwe afstandsregel). Voeg een toets toe in de echte Blender die eist dat ANKLE op de robot en MakeHuman twee gesloten delen geeft.

**Kan**
1. Maak `m.col[3][:3] = ...` zeker door de plek in een hele matrix te zetten (bijvoorbeeld `m.translation = ...`), en toets die plek.
2. Werk `architectuur.md` bij met de enkelregel en de nieuwe afstandsregel.
3. Controleer wat er gebeurt als `pb.parent` geen scheen is, en geef dan een nette melding.
4. Zet een akkoord van Daan op 1.2.5 in `ontwerp.md` voordat het naar Superhive gaat.

---
Automatische keurder, model `claude-sonnet-5-5`, 18370 tokens in, 3463 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
