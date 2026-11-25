# Keuring blender-gewrichten KAART, 25-11-2026, automatische keurder
Wat ik keurde: commit fa3c5cfca (fd0a704..fa3c5cf), alleen `producten/blender-gewrichten/KAART.md`, één regel aangepast
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid (hoog/midden/laag) | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De commit past alleen de kaartregel over Paneel 1.2.9 aan, zoals het bericht zegt. De add-on-code zit niet in deze wijziging. | Feit | hoog | De lijst met gewijzigde bestanden bevat alleen KAART.md. |
| 2 | De regel zegt dat stap 3 "Hinge placed" toont, dat het een Pro-deel is en dat e2e 45644233399 groen is in 4.2.23, 5.2.3 en 5.3.0. Dat staat er als GEZIEN, maar ik zie de run en commit c393c55 niet. | Vermoeden | midden | Het log van run 45644233399 en de diff van c393c55 (de tekst "Hinge placed" alleen in de betaalde build). |
| 3 | De regel zegt "Daan #83: punt 2 en 3 ja, punt 1 alleen nog beeld 16a nakeuren (#89)". Er staat dus geen vals akkoord: de kaart noemt het openstaande punt zelf. De uitspraken van Daan kan ik niet nalezen. | Vermoeden | midden | Bericht #83 en #89 van Daan. |
| 4 | De regel zegt "uitbrengen niet vóór ma 30 nov" en het ontwerp heeft nog geen ja voor 1.2.9, alleen voor 1.2.8. Dat klopt met elkaar. | Feit | hoog | `ontwerp.md` bevat geen akkoord voor 1.2.9. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Er zijn geen tests gewijzigd. | Feit | hoog | Tests niet aangepast om te slagen |
| 2 | KAART.md is een kort bestand en de diff is één regel. | Feit | hoog | Bestanden onder ±400 regels |
| 3 | De architectuur verandert niet in deze commit, dus `architectuur.md` hoeft hier niet mee. Of de code-commit c393c55 dat deed, kan ik niet zien. | Vermoeden | midden | architectuur.md bijgewerkt |
| 4 | Het e2e-resultaat heeft het label GEZIEN. De eerdere cijfers op de kaart (blindtest, verkoop, sale) staan er al met bron. Persoonsgegevens, sleutels en wachtwoorden zie ik niet. | Feit | hoog | Cijfers met GEZIEN/DERDEN/GOK, geen persoonsgegevens |
| 5 | De regel noemt geen spelerstekst van Hats en geen AI-beeld of -geluid op Steam. | Feit | hoog | Regels Hats en Steam |

## Deel C: zou een gebruiker het leuk en fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite (klein/midden/groot) |
|---|---|---|---|
| 1 | Dit is een interne kaart, een koper ziet hem niet. Er valt niets te zien of te spelen. | n.v.t. | n.v.t. |
| 2 | De regel is erg lang en bevat veel nummers (#70, #83, #89, c393c55, run-id). Dat is lastig lezen voor wie de kaart opent. | Een korte statusregel bovenaan en de details op een aparte regel. | klein |

## Deel C: is het goed genoeg?
Niet van toepassing: er is geen beeld, video, winkeltekst, spel of site voor een klant. De blinde test geldt hier niet, dus geen cijfers. Beeld 16a staat nog open bij Daan (#89). Dat gaat vóór het uitbrengen van 1.2.9 nog langs een eigen keuring.

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Zet bij het e2e-resultaat een link naar de run of het log, zodat het GEZIEN te controleren is.
- Verwijs bij Daan #83 en #89 naar het bestand of bericht waar zijn oordeel staat.
- Splits de lange regel in een korte status en een detailregel.
- Houd bij de echte keuring van 1.2.9 de tekst "Hinge placed" tegen de code van c393c55 en laat het beeld 16a door Daan nakijken (hoort bij het Pro-deel, niet in de gratis build).

---
Automatische keurder, model `claude-sonnet-5-5`, 18638 tokens in, 2478 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
