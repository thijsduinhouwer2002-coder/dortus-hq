# Keuring Bison & Flex architectuur (week-test en beeldvergelijking), 19-11-2026, automatische keurder
Wat ik keurde: commit 281d0a3b (reeks 3424f23..281d0a3), alleen het bestand `producten/jetbrains-bison-flex/architectuur.md`
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid (hoog/midden/laag) | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De wijziging raakt alleen documentatie. De belofte in `plugin.xml` (Bison/Yacc en Flex/Lex, gratis en Pro) blijft gelijk, en er is geen nieuw zichtbaar werk dat Daan eerst moet zien. | Feit | hoog | Het diff bevat één bestand, `architectuur.md`. |
| 2 | Het akkoord van Daan voor 2026.1.2 (c1ae19b) wordt door deze wijziging niet ongeldig, want er is geen code of winkeltekst veranderd. | Feit | hoog | Een latere commit die `src/` of `plugin.xml` aanpast zou dat wel veranderen. |
| 3 | De bijgeschreven alinea beschrijft de week-test (IDE-test met de nieuwste EAP, CLion-EAP, Plugin Verifier tegen de nieuwste releases) en de beeldvergelijking met een grens van 0,3 procent. Of de genoemde bestanden bestaan en zo werken, is uit deze tekst niet te zien. | Vermoeden | midden | De bestanden `week-test.yml`, `organisatie/controle/beelden.sh` en `weektest.py` moeten bestaan en de beschreven stappen bevatten. |
| 4 | Het commitbericht noemt ook maskers voor kluisnaam en melding in Rollwright en een verslag naast de schermen. Die wijzigingen zitten niet in wat ik kreeg en ik heb ze niet gekeurd. | Feit | hoog | Een keuring van de bestanden die bij die maskers horen, onder het product Rollwright. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | `architectuur.md` is bijgewerkt voor de week-test en de beeldvergelijking. | Feit | hoog | architectuur.md bijgewerkt |
| 2 | Er zijn geen tests aangepast en er staan geen persoonsgegevens, sleutels of wachtwoorden in de wijziging. | Feit | hoog | Tests niet aangepast om te slagen; geen persoonsgegevens |
| 3 | De ruis van 0,11 procent is gemarkeerd als GEZIEN met een bestandsnaam. De zin dat een EAP na 28 dagen verloopt (licentie) en de versies `2026.3` en `2026.3.0.1` hebben geen label. | Feit | midden | Cijfers met GEZIEN/DERDEN/GOK |
| 4 | Of `architectuur.md` nog onder de 400 regels blijft, is uit het diff niet te zien. De regels zijn wel erg lang, en één alinea telt bijna twintig zinnen. | Vermoeden | laag | Bestanden onder ±400 regels |
| 5 | De kop zegt nog "Stand 8 nov 2026: versie 0.2", terwijl de plugin op 2026.1.2 staat. Dat was al zo en is niet door deze wijziging gekomen. | Feit | hoog | architectuur.md bijgewerkt |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Zet bij "28 dagen (licentie verlopen)" en bij de versies `2026.3` en `2026.3.0.1` een label (GEZIEN of DERDEN met bron), zodat ze aan de regel voor cijfers voldoen.
- Werk de kop "Stand 8 nov 2026: versie 0.2" bij naar de huidige stand.
- Controleer dat `architectuur.md` onder de ±400 regels blijft, of splits de lange week-test-alinea in een eigen bestand.
- Laat de maskers voor Rollwright (en het verslag naast de schermen) apart keuren onder het product Rollwright, want die zaten niet in deze keuring.

---
Automatische keurder, model `claude-sonnet-5-5`, 18746 tokens in, 2580 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
