# Keuring jetbrains-bison-flex, 23-11-2026, automatische keurder
Wat ik keurde: commit 695917c9c (reeks e292277..a3f5e85), alleen `producten/jetbrains-bison-flex/ontwerp.md`
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid (hoog/midden/laag) | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De wijziging raakt alleen het ontwerp: een nieuwe regel "Akkoord: ja 23 nov 2026" voor de uitgave 2026.1.2, en de vorige akkoordregel is naar "Oud" verplaatst. De belofte (wat, voor wie, gratis, Pro) is niet aangeraakt. | Feit | Hoog | Het diff laat de belofte ongewijzigd. |
| 2 | De akkoordregel noemt "change-notes met beide regels" en "Nothing is sent until you submit it yourself". Beide staan in het `CHANGELOG.md` onder 2026.1.2 (meldknop in het Help-menu en error handler). | Feit | Hoog | Tekstvergelijking met het changelog. |
| 3 | De groene runs (CLion 45197751752, e2e 45197752060), commit 2e46f5e2 en de keuring van Daan kan ik niet zien. Ze staan alleen als bewering in de tekst. | Vermoeden | Midden | De runs in de API, en het bestand `platformen/jetbrains/keuring/2026-11-23-bison-flex-2026.1.2-uitgave-daan.md`. |
| 4 | De commitboodschap noemt een keuring "terugval Pro (nee, testhaak)". Het diff laat niet zien of dat dit product raakt, en of die terugval in 2e46f5e2 zit. | Vermoeden | Laag | De keuring zelf lezen, en nagaan of de testhaak in de uitgave-commit staat. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Er is geen code of test gewijzigd, dus niets is aangepast om te slagen en er groeit geen bestand. | Feit | Hoog | Tests en ±400 regels |
| 2 | `architectuur.md` is niet bijgewerkt. Dat hoeft hier niet, want er is geen code veranderd. In het zichtbare deel staat nog "Stand 8 nov 2026: versie 0.2", wat achterloopt. | Feit | Midden | architectuur.md bijgewerkt |
| 3 | In het diff staan geen persoonsgegevens, sleutels of wachtwoorden. | Feit | Hoog | Geen persoonsgegevens |
| 4 | De akkoordregel is gemarkeerd als "Daan", maar de commit is door Claude geschreven. Of de keurder een ander is dan de bouwer, zie ik niet. | Vermoeden | Laag | Keurder is niet de bouwer |
| 5 | Het CLion-bewijs en de verifier-uitslag zijn gemarkeerd als "GEZIEN in de API". Dat kan ik hier niet nakijken. | Vermoeden | Midden | Cijfers met GEZIEN/DERDEN/GOK |

## Deel C: zou een gebruiker het leuk en fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite (klein/midden/groot) |
|---|---|---|---|
| 1 | Er is niets te zien of te spelen in deze wijziging, dus hier valt niets te keuren. De meldknop in het Help-menu en de error handler zou ik pas kunnen beoordelen met schermen. | Een scherm van het Help-menu en de ingevulde GitHub-melding bij de keuring leggen. | Klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Open de meldlink één keer en kijk of issues aan staan op de loketrepo. Daan noemt dit zelf als open punt. Staan ze uit, dan klopt de belofte in het changelog ("opens a bug report on GitHub") niet. Doe dit vóór het uitbrengen.
- Controleer dat de keuring "terugval Pro (nee, testhaak)" niet over code in 2e46f5e2 gaat. Zo ja, dan botst die met dit akkoord.
- Werk de regel "Stand 8 nov 2026: versie 0.2" in `architectuur.md` bij.

---
Automatische keurder, model `claude-sonnet-5-5`, 19204 tokens in, 3372 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
