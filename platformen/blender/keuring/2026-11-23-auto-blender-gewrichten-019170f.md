# Keuring blender-gewrichten (testhaak terugval), 23-11-2026, automatische keurder
Wat ik keurde: commit 019170fc9 (957a9ac..019170f), bestand producten/blender-gewrichten/click_joints/betaald/terugval.py
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De wijziging voegt één regel toe: `bm.faces.ensure_lookup_table()` vlak voor `bm.faces[0]` in `_maak_open`. Zonder die regel kan indexeren op bmesh-vlakken een fout geven. Het is een gangbare en juiste fix. | Feit (uit de diff) | Hoog | Een groene run van de terugvaltest in Blender 4.2 en 5.x zou bevestigen dat de fout weg is. |
| 2 | De functie is "alleen voor de test" (docstring). De opdracht (ontwerp.md) belooft de gebruiker niets nieuws, dus de beloofde functies veranderen niet. | Feit | Hoog | Niet van toepassing. |
| 3 | De commit heet "terugval 2x open", maar in de diff staat één wijziging. Misschien is de dubbele opening elders al opgelost, of de naam beschrijft het testgeval. | Vermoeden | Midden | De volledige commit of het testlog laat zien of de terugvaltest echt twee keer een open deel maakt en netjes meldt. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Geen test is aangepast of afgezwakt. Alleen een hulpfunctie van de test is robuuster gemaakt. | Feit | Hoog | Tests niet aangepast om te slagen |
| 2 | Er staan geen persoonsgegevens, sleutels of wachtwoorden in de diff. | Feit | Hoog | Geen persoonsgegevens |
| 3 | De wijziging is één regel, dus de bestandsgrens van ±400 regels komt niet in gevaar. De totale lengte van terugval.py zie ik niet. | Vermoeden | Midden | De regelaantallen van het bestand zouden dit bevestigen. |
| 4 | architectuur.md hoeft niet bij: er verandert geen onderdeel of gedrag. | Feit | Hoog | architectuur.md bijgewerkt |
| 5 | Een testhaak staat in de map `betaald/`, dus mogelijk in de betaalde zip. Dat is onschadelijk, maar of hij meegaat zie ik niet. | Vermoeden | Laag | De inhoud van `maak_zip.sh` en de zip-toets `e2e/toets_zips.py` zouden dit tonen. |

## Deel C: zou een gebruiker het leuk en fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | Niets zichtbaar of speelbaar veranderd voor de gebruiker, dus hier valt niets te beoordelen. | Niet van toepassing | Klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Laat in de volgende run zien dat de terugvaltest groen is in 4.2 en 5.x, zodat het vermoeden bij A1 een feit wordt.
- Leg uit of de testhaak in de betaalde zip hoort te zitten, en haal hem eruit als dat niet zo is (B5).
- Maak de commitnaam duidelijker (A3).

---
Automatische keurder, model `claude-sonnet-5-5`, 17303 tokens in, 1687 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
