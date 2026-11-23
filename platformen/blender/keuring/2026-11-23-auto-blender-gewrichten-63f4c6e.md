# Keuring blender-gewrichten, 23-11-2026, automatische keurder
Wat ik keurde: commit 63f4c6ef2 (da1c134..63f4c6e): `click_joints/betaald/scharnier.py` en `architectuur.md`
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | Met Exact (Blender 4.2) gebruikt het scharnier nu het diepe omhulsel in plaats van de gratis `een_lid.bereid`. De schakelaar `DIEP_EXACT = [True]` staat erbij, met de oude weg als `False`. | Feit (uit de diff) | Hoog | Dit is de enige codewijziging. |
| 2 | Run 28 koos juist de gratis weg omdat het diepe omhulsel in 4.2 het andere onderbeen kwijtraakte. De commit zegt dat H nu schoon is, maar levert geen run of meting mee. De kernbelofte van de kniefout (alleen het lid onder de cursor wordt gesneden) kan dus in 4.2 weer stuk zijn. | Vermoeden | Midden | Een groene run in 4.2.23 met de toets "alleen het lid onder de cursor" voor het scharnier op een figuur met twee benen. Rood zou het weerleggen. |
| 3 | De commit heet "Proef". Er is geen oordeel of uitgebrachte versie aan gekoppeld. | Feit | Hoog | Het blijft een proef tot de 4.2-run groen is. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Er zijn geen tests aangepast of weggehaald. Alleen de twee genoemde bestanden veranderden. | Feit | Hoog | Tests niet aanpassen om te slagen |
| 2 | `architectuur.md` is bijgewerkt voor `omhulsel.py`, `herstel.py`, `redenen.py` en de testset. De nieuwe schakelaar `DIEP_EXACT` en het terugdraaien van de run-28-keuze staan er niet in. | Feit | Midden | architectuur.md bijgewerkt |
| 3 | Het document noemt een aanroep van `herstel.splits_vier` in `scharnier.py` "direct na `vorm.snij`". Die regel zit niet in deze diff. | Vermoeden | Laag | Controle bij de eerdere commit of in het volledige bestand |
| 4 | Geen persoonsgegevens of sleutels gezien. De cijfers in het document zijn niet allemaal als GEZIEN, DERDEN of GOK gemarkeerd, bijvoorbeeld de grenzen 2% en 250000. | Feit | Laag | Cijfers met GEZIEN/DERDEN/GOK |
| 5 | Bestandslengte van `scharnier.py` is niet te zien in de diff. | Vermoeden | Laag | Regelaantal ±400 nakijken |

## Deel C: zou een gebruiker het leuk en fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | Er is niets te zien of te spelen, alleen tekst. Ik kan niets over beeld of gevoel zeggen. | Een schermafbeelding van een scharnier op een tweebenig figuur in 4.2, voor Daan of Iris | klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Zet de run-id van een groene 4.2.23-run met de "één lid"-toets bij dit scharnier in de commit of in `ontwerp.md`. Dat bewijst dat het onderbeen niet weer verdwijnt (A2). Dit weegt zwaar voordat een Pro-zip met deze wijziging wordt uitgebracht.
- Noem `DIEP_EXACT` en het terugdraaien van de run-28-keuze in `architectuur.md`, bij de regel over `een_lid_diep` of `omhulsel.py` (B2).
- Controleer de aanroep van `herstel.splits_vier` in `scharnier.py` (B3).

---
Automatische keurder, model `claude-sonnet-5-5`, 22945 tokens in, 3079 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
