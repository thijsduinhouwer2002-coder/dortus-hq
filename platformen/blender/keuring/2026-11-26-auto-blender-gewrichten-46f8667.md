# Keuring blender-gewrichten Pro #114 (gratis uitzetten met waarschuwing), 26-11-2026, automatische keurder
Wat ik keurde: commit 46f8667c2 (0943e89..46f8667), vier bestanden: `betaald/__init__.py`, `e2e/test_betaald.py`, `architectuur.md`, `ontwerp.md`
Akkoord: ja

Ik zie alleen tekst. De e2e-uitslag van deze commit zit niet bij de stukken, dus ik heb niets gezien dat draait.

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | `addon_utils.disable(n, default_set=True, handle_error=fouten.append)` vangt fouten uit de unregister van de gratis versie op. Daarna komt er één consolregel "free version ... turned off with warnings". Dit is wat aanrader A1 van Daan (#138) vroeg. | Feit (uit de diff) | Hoog | Staat in de diff. |
| 2 | De parameter `handle_error` bestaat in Blender 4.2 tot 5.3 en wordt met het uitzonderingsobject aangeroepen. De `join` over `type(f).__name__` en `f` is daarop gebouwd. | Vermoeden (uit mijn kennis van Blender, niet gelezen in de bron) | Midden | Een groene e2e-run in 4.2.23, 5.2.3 en 5.3.0. Beter nog een toets met een gratis versie waarvan `unregister` met opzet een fout geeft. |
| 3 | Na uitzetten gaat `weiger_dubbel` nog steeds eerst langs. Lukt uitzetten niet, dan weigert Pro nog. Ontwerp en architectuur zeggen dat nu ook. | Feit (tekst) | Hoog | Staat in de diff. |
| 4 | `GRATIS_UIT[:] = []` in `unregister()` haalt de overnameregel weg als Pro uitgaat. De test controleert dat. | Feit (tekst), werking Vermoeden | Midden | Groene stap "(b) betaald uit: regel van de overname weg" in de e2e. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Er is een toets bijgekomen en geen enkele is aangepast of afgezwakt. | Feit | Hoog | Tests niet aangepast om te slagen |
| 2 | `architectuur.md` en `ontwerp.md` zijn in dezelfde commit bijgewerkt en spreken elkaar niet tegen over "weigert" of "zet uit". | Feit | Hoog | architectuur.md bijgewerkt |
| 3 | Er staan geen persoonsgegevens, sleutels of wachtwoorden in de diff. De consolregel bevat alleen modulenaam en fouttekst. | Feit | Hoog | Geen persoonsgegevens |
| 4 | De nieuwe tekst bevat geen nieuwe cijfers of claims, dus GEZIEN/DERDEN/GOK is hier niet van toepassing. | Feit | Hoog | Cijfers met label |
| 5 | De toets gebruikt de naam `betaald.GRATIS_UIT`, terwijl de regels eromheen `bm` gebruiken voor de betaalde module. Of `betaald` in dat bestand bestaat, zie ik niet. | Vermoeden | Midden | Een groene e2e. Een NameError zou de stap laten falen. |
| 6 | `ontwerp.md` en `architectuur.md` zijn veel langer dan 400 regels. Deze commit maakt ze niet merkbaar langer, en het zijn documenten. De regelaantallen van de twee Python-bestanden zie ik niet. | Vermoeden | Laag | `wc -l` op beide bestanden. |

## Deel C: zou een gebruiker het leuk en fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | De waarschuwing komt alleen in de console. Een koper ziet dus niet dat de gratis versie met fouten is uitgegaan. Dat is acceptabel, want het paneel zegt al dat de gratis versie is uitgezet. | Alleen als het vaak voorkomt: een korte tweede regel in het paneel met een verwijzing naar de console. | klein |
| 2 | Bij de overgang gratis naar Pro hoeft de koper niets meer uit te zetten. Dat is prettiger dan de oude weigering. De tekst op de Superhive-pagina moet wel aangepast worden zodra 1.2.9 live is. | Zet de aanpassing van de Superhive-zin op de lijst voor het uitbrengen. | klein |

## Deel C: is het goed genoeg?
Er is geen nieuw beeld, geen video, geen winkeltekst en geen nieuw spelelement. Er verandert alleen een consolregel en gedrag bij installeren. Een blinde test of cijfers 1 tot 10 hebben hier geen basis, en ik geef geen cijfers zonder iets gezien te hebben. Dat blokkeert dit akkoord niet. Het geldt wel opnieuw bij uitbrengen van 1.2.9: Daan keurt dan het paneel en de winkelpagina.

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
1. Controleer in de e2e-run van deze commit dat `betaald` in `test_betaald.py` bestaat (B5) en dat stap (b) groen is.
2. Voeg een toets toe waarin de unregister van de gratis versie met opzet faalt. Dan wordt de consolregel en het doorgaan van Pro echt bewezen (A2).
3. Haal de zin "turn the free one off first" van de Superhive-pagina zodra 1.2.9 live is (staat al in `ontwerp.md`).
4. Het akkoord van Daan van 25 nov geldt voor 1.2.8. Voor uitbrengen van 1.2.9 is een nieuwe keuring nodig.

---
Automatische keurder, model `claude-sonnet-5-5`, 24627 tokens in, 4850 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
