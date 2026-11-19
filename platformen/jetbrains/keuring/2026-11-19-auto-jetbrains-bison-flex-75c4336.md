# Keuring beeldvergelijking kleurenpagina (architectuur.md), 19-11-2026, automatische keurder
Wat ik keurde: commit 75c4336d (cb66e04..75c4336), alleen `producten/jetbrains-bison-flex/architectuur.md`
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid (hoog/midden/laag) | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De wijziging raakt alleen de architectuurtekst en niet de belofte, de winkeltekst of de plugincode in het ontwerp. De gratis en Pro-beloften blijven dus ongewijzigd. | Feit | Hoog | Het diff bevat één bestand en één alinea. |
| 2 | De alinea beschrijft nu dat op de kleurenpagina alleen het paneel rechts (x 560 tot 1920) telt, vergeleken met de best passende horizontale verschuiving, en dat het beeldbericht aan Chris uit staat. Dat is intern testgereedschap en geen spelerskant of gebruikerskant. | Feit | Hoog | Diff-regel in de alinea "Week-test en beeldvergelijking". |
| 3 | De commit zegt dat de code is aangepast (masker met `%` in `beeldvergelijk.py`, `l1-logboek-tekst` met gemaskeerde kloktijden). In de meegestuurde wijziging staat alleen de tekst. Of de code er ook zo uitziet kan ik niet zien. | Vermoeden | Midden | De diff of de huidige inhoud van `organisatie/controle/beeldvergelijk.py` en `beelden.sh`, met het `%`-masker en de kloktijd-maskering. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | `architectuur.md` is bijgewerkt in dezelfde commit als het onderwerp. | Feit | Hoog | architectuur.md bijgewerkt |
| 2 | De nieuwe cijfers (±55 px, run 44481997077) staan met GEZIEN. De zin "bleef in zes runs op zijn plek" heeft geen label. Het zijn eigen run-waarnemingen, dus dat is klein. | Feit | Hoog | Cijfers met GEZIEN/DERDEN/GOK |
| 3 | De commit noemt de maskering van kloktijden in `l1-logboek-tekst`, maar de alinea in `architectuur.md` noemt die niet. De beschrijving is dus waarschijnlijk niet compleet. | Vermoeden | Midden | architectuur.md bijgewerkt |
| 4 | Ik zie geen persoonsgegevens of sleutels. Er zijn geen tests aangepast en er is geen AI-beeld of -geluid. | Feit | Hoog | Geen persoonsgegevens, tests niet aangepast |
| 5 | De alinea is één erg lange regel. Het bestand is door de afkapping niet te tellen op de grens van ±400 regels. | Vermoeden | Laag | Bestanden onder ±400 regels |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Controleer of de code (`beeldvergelijk.py`, `beelden.sh`) echt zo werkt als de tekst zegt. In deze wijziging zit alleen de tekst, dus de commitregel over code en de alinea staan hier los van elkaar.
- Voeg de maskering van kloktijden in `l1-logboek-tekst` toe aan de alinea, zodat de tekst bij de commit past.
- Geef "bleef in zes runs op zijn plek" een label (GEZIEN, met runnummers).
- Splits de lange alinea in een paar kortere, zodat hij leesbaar blijft.

---
Automatische keurder, model `claude-sonnet-5-5`, 21182 tokens in, 2763 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
