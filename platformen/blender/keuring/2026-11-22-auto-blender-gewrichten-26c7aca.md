# Keuring blender-gewrichten, 22-11-2026, automatische keurder
Wat ik keurde: commit 26c7aca73 (range 86800a6..26c7aca), bestand producten/blender-gewrichten/click_joints/betaald/rig.py
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid (hoog/midden/laag) | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | Het vangnet met het gedraaide scharnier geldt nu alleen nog als `sleutel == "ELBOW"`. Knie en enkel krijgen het niet meer. Dat past bij de commitboodschap en bij de eis dat een knie niet zijwaarts mag buigen. | Feit (diff) | Hoog | Een run van de rig-toets met een knie waarvan de eerste plek faalt: die moet nu overgeslagen worden. |
| 2 | `scharnier_plekken(...) or [(m, 0.0)]` vangt een lege lijst op. Daarvoor gaf `kandidaten[0]` een IndexError. Het gedrag bij een lege lijst is dus beter. | Feit (diff) | Hoog | Een toets waarbij `scharnier_plekken` een lege lijst teruggeeft en de operator niet crasht. |
| 3 | Ik kan niet zien of `sleutel` op die plek in de functie al gevuld is en of de waarde precies "ELBOW" heet. Staat de naam anders (bijvoorbeeld "ELLEBOOG"), dan krijgt de elleboog het vangnet nooit meer, zonder foutmelding. | Vermoeden | Laag | De rest van `rig.py` rond regel 640 tot 670, of een toetslog waarin de elleboog het vangnet gebruikt. |
| 4 | Een knie of enkel zonder werkende plek wordt nu overgeslagen. Uit de diff blijkt niet of de gebruiker daar een melding van krijgt of dat het stil gebeurt. | Vermoeden | Laag | De code die `geblokkeerd` en `vangnet` verderop gebruikt, of een scherm van de lijst na "Figure from rig". |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Er is geen toets in de wijziging, en er staat geen groene run bij het oordeel. Er is ook geen toets aangepast om te slagen. | Feit (alleen `rig.py` gewijzigd) | Hoog | Tests niet aanpassen om te slagen. Dit is een tekort, geen overtreding. |
| 2 | `rig.py` is minstens 670 regels lang (de wijziging zit rond regel 669). Dat was al zo en de wijziging maakt het bestand korter, niet langer. | Feit | Midden | Bestanden onder ±400 regels. |
| 3 | `architectuur.md` is niet bijgewerkt. Het afgekapte deel kan ik niet nalezen, dus ik weet niet of daar het vangnet voor alle gewrichten staat beschreven. | Vermoeden | Laag | Architectuur.md bijgewerkt. |
| 4 | De akkoordregel in `ontwerp.md` geldt voor Pro 1.0.2 zoals die op 16 nov was. Deze wijziging verandert betaalde code erna. De goedkeuring van Daan dekt deze wijziging dus niet. Het CHANGELOG-deel noemt alleen de gratis versie. | Feit (tekst) | Midden | Eerst keuren, dan uitbrengen. |
| 5 | Geen persoonsgegevens, sleutels of wachtwoorden in de diff. | Feit | Hoog | Geen persoonsgegevens. |

## Deel C: zou een gebruiker het leuk en fijn vinden?
Er is niets te zien of te spelen in de wijziging, dus ik kan hier niets over de ervaring zeggen.
| # | Bevinding | Wat het beter maakt | Moeite (klein/midden/groot) |
|---|---|---|---|
| 1 | Een gebruiker met een rig waarvan de knie geen plek vindt, merkt het misschien alleen doordat er een gewricht mist. | Een korte melding in de lijst, zoals "Knee skipped: no safe spot found". | klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** niets.

**Kan:**
- Controleer dat `sleutel` en de waarde "ELBOW" kloppen met de rest van `rig.py` (B3 van Deel A).
- Voeg een toets toe voor de lege lijst en voor het overslaan van een knie.
- Meld de gebruiker als een knie of enkel wordt overgeslagen.
- Laat deze wijziging door Daan keuren voor Pro naar Superhive gaat.
- Werk `architectuur.md` bij als daar het vangnet voor alle gewrichten staat beschreven.
- Splits `rig.py` op, want het bestand is veel langer dan 400 regels.

---
Automatische keurder, model `claude-sonnet-5-5`, 17797 tokens in, 3012 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
