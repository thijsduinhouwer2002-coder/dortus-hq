# Keuring blender-gewrichten (Click Joints Pro, scharnier), 19-11-2026, automatische keurder
Wat ik keurde: commit ca36d539 (dcb4d77..ca36d53), bestand `producten/blender-gewrichten/click_joints/betaald/scharnier.py`
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De wijziging zet `cj_passing = "groen"` op beide delen na "Place hinge". Dat past bij het doel dat stap 3 geen "No joint yet" meer zegt naast een scharnier. | Feit (de regel staat in de diff) | Hoog | Alleen een run in de echte Blender kan laten zien wat stap 3 daarna toont. |
| 2 | De aanname dat een scharnier alleen bij Good fit bestaat ("maten_neus weigert Tight") staat alleen in de commentaar. In de diff zie ik `maten_neus` niet. | Vermoeden | Midden | De code van `maten_neus` of een test met een dunne plek, waarbij het scharnier geweigerd wordt en `cj_passing` niet op groen komt. |
| 3 | Of het paneel `cj_passing` leest en dan "Good fit" toont, zie ik niet. Het commitbericht zegt dat wel. | Vermoeden | Midden | Een schermafbeelding van stap 3 na Place hinge in 4.2 en 5.2. |
| 4 | De waarde wordt voor beide delen gezet, ook als een deel al een oudere passing had van een eerder gewricht (bijvoorbeeld oranje). Die waarde wordt dan overschreven. | Vermoeden | Laag | Een test met eerst een kogelgewricht met Tight en daarna een scharnier op hetzelfde deel. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Er is geen test aangepast en er is er ook geen bij gekomen. De fout is gezien in een film en wordt niet door een test bewaakt. | Feit | Hoog | Tests: geen aangepaste test, wel een gemiste kans |
| 2 | Er staan geen persoonsgegevens of sleutels in de diff. | Feit | Hoog | Geen persoonsgegevens |
| 3 | De wijziging is 3 regels in een bestand van onbekende lengte. Of `scharnier.py` onder de ±400 regels blijft, kan ik niet zien. | Vermoeden | Laag | Bestanden onder ±400 regels |
| 4 | `architectuur.md` is niet bijgewerkt. Het gedrag dat stap 3 voor een scharnier groen zet is alleen in de commentaar beschreven. | Feit | Midden | architectuur.md bijgewerkt |
| 5 | De wijziging staat alleen in `betaald/`, dus de gratis zip blijft gelijk. | Vermoeden (de diff toont alleen dit bestand) | Midden | Twee builds uit één bron, `toets_zips` |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Voeg een toets toe in de echte Blender: na Place hinge is `cj_passing` gelijk aan "groen" op beide delen en toont stap 3 "Good fit".
- Kijk of een eerder gewricht op hetzelfde deel zijn passing verliest (A4).
- Zet één regel in `architectuur.md` over `cj_passing` bij het scharnier.
- Het bestaande ja van Daan op 16 nov geldt voor Pro 1.0.2 zoals het toen was (1d0c54c). Deze wijziging zit daar niet in. Voor een Pro-uitgave met deze regel is een nieuwe bevestiging nodig, en bij live zetten een keuring door een agent.

---
Automatische keurder, model `claude-sonnet-5-5`, 17263 tokens in, 2175 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
