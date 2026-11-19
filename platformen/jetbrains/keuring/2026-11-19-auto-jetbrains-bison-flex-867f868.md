# Keuring Bison & Flex beeldbericht-aan in architectuur.md, 19-11-2026, automatische keurder
Wat ik keurde: commit 867f8689 (92e1989..867f868), bestand `producten/jetbrains-bison-flex/architectuur.md`
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid (hoog/midden/laag) | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De wijziging raakt alleen de architectuurtekst. De belofte uit `ontwerp.md` (winkeltekst, functies, Pro) en het uiterlijk veranderen niet, dus Daans akkoord blijft zoals het was. | Feit | hoog | Het diff bevat één regel in `architectuur.md` en geen code of winkeltekst. |
| 2 | De tekst zegt nu dat de job `beeldbericht` weer aan staat en op main per run één kort bericht aan Chris stuurt. In deze commit staat geen wijziging van de workflow. Of `if: false` echt weg is, kan ik hier niet zien. | Vermoeden | midden | In de e2e-workflow staat bij `beeldbericht` geen `if: false` meer (eerdere commit of ontbrekend bestand). |
| 3 | De tekst noemt drie runs met 0 groot (44500264197, 44500267041, 44503498367), gemarkeerd als GEZIEN. De voorwaarde "drie runs van dezelfde code" lijkt hiermee gehaald. Of het echt dezelfde code was en 0 groot, kan ik niet nalopen. | Vermoeden | midden | De logs of `BEELDVERSCHIL.md` van die drie runs op de tak `schermen` tonen 0 groot en dezelfde commit. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Er zijn geen tests gewijzigd of aangepast om te slagen. | Feit | hoog | Tests niet aangepast om te slagen |
| 2 | `architectuur.md` is zelf bijgewerkt in dezelfde commit als de beschreven stand. De oude zin "staat uit" is vervangen door de nieuwe stand. | Feit | hoog | architectuur.md bijgewerkt |
| 3 | De nieuwe cijfers (run-nummers) zijn als GEZIEN gemarkeerd. Er staan geen persoonsgegevens, sleutels of wachtwoorden in het diff. | Feit | hoog | Cijfers met GEZIEN/DERDEN/GOK, geen persoonsgegevens |
| 4 | Geen spelerstekst, geen AI-beeld of -geluid, geen winkeltekst. Daardoor geen nieuwe CHANGELOG-regel nodig. | Feit | hoog | Regels Hats en Steam, niet van toepassing |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Controleer dat de workflow echt overeenkomt met de tekst (`if: false` weg bij `beeldbericht`). Zo niet, dan klopt de documentatie niet en moet een van de twee aangepast worden (deel A, rij 2).
- De kop bovenaan zegt nog "Stand 8 nov 2026: versie 0.2", terwijl de plugin op 2026.1.2 zit. Dat staat los van deze wijziging maar maakt het document verwarrend.
- De bullet over de week-test is één zeer lange alinea. Splitsen in korte stukken leest makkelijker.

---
Automatische keurder, model `claude-sonnet-5-5`, 21728 tokens in, 2334 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
