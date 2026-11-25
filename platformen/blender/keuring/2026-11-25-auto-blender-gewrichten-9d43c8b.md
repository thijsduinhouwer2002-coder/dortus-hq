# Keuring blender-gewrichten KAART.md (Pro 1.2.9 stand), 25-11-2026 18:35 NL, automatische keurder
Wat ik keurde: commit 9d43c8ba9 (bereik a78e6d5..9d43c8b), alleen `producten/blender-gewrichten/KAART.md`
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De wijziging voegt één zin toe over run 45662127816 (e2e op main, groen in 4.2.23, 5.2.3 en 5.3.0) en verwijst naar #93. Dat past bij de commitbericht en bij de opdracht (stand bijwerken, 1.2.9 nog niet uitbrengen). | Feit (over de tekst) | Hoog | De diff zelf. |
| 2 | Dat de run echt groen is op main en in alle drie de versies, kan ik niet zien. Ik zie alleen de bewering met "GEZIEN" erbij. | Vermoeden | Midden | De uitslag van run 45662127816 in het Actions-log. |
| 3 | De commitbericht zegt "stand in note en kaart", maar alleen de kaart is gewijzigd. Of de note `platformen/blender/pro-1.2.9.md` ook is bijgewerkt, zie ik niet. | Vermoeden | Laag | Een diff van `pro-1.2.9.md` in dezelfde of een eerdere commit. |
| 4 | De regel "niet uitbrengen vóór ma 30 nov" en "workflow blijft op VERSIE 1.2.8" blijft staan, dus de wijziging brengt niets te vroeg uit. | Feit | Hoog | n.v.t. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Alleen een kaartbestand gewijzigd: geen tests aangepast, geen code, dus geen bestand boven ±400 regels erbij en `architectuur.md` hoeft niet mee. | Feit | Hoog | Tests niet aanpassen om te slagen; architectuur bijgewerkt |
| 2 | Het run-nummer heeft het label GEZIEN, zoals de regel vraagt. Of het echt gezien is, kan ik niet nagaan. | Vermoeden | Midden | Cijfers met GEZIEN/DERDEN/GOK |
| 3 | Geen persoonsgegevens, sleutels of wachtwoorden in de wijziging. | Feit | Hoog | Geen persoonsgegevens |
| 4 | Geen spelerstekst van Hats en geen AI-beeld of -geluid in de wijziging. | Feit | Hoog | Hats alleen als CONCEPT; geen AI op Steam |

## Deel C: zou een gebruiker het leuk en fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | Er is niets te zien of te spelen: dit is een interne statusregel. | n.v.t. | klein |

## Deel C: is het goed genoeg?
Niet van toepassing: de wijziging bevat geen beeld, video, winkeltekst, spel of site die een klant ziet. Er is geen blinde test nodig en ik geef geen cijfers.

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Controleer in het Actions-log dat run 45662127816 groen is in alle drie de Blender-versies (nu alleen beweerd).
- Controleer of `pro-1.2.9.md` ook is bijgewerkt, want de commitbericht noemt "note en kaart".
- "tot de plak van vanavond voorbij is" wordt snel verouderd. Een vaste datum of tijd leest later duidelijker.

---
Automatische keurder, model `claude-sonnet-5-5`, 18716 tokens in, 2098 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
