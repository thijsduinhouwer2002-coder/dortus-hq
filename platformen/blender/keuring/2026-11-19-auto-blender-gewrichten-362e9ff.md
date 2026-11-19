# Keuring blender-gewrichten (architectuur.md, Xvfb-regel), 19-11-2026, automatische keurder
Wat ik keurde: commits 1ce44c0..362e9ff, alleen `producten/blender-gewrichten/architectuur.md` (twee regels erbij)
Akkoord: ja

## Deel A: doet het wat beloofd is?
De wijziging is alleen documentatie. Ze verandert niets aan de add-on of aan wat de opdracht belooft (`ontwerp.md`, release 0.1.1 en Pro 1.0.2).

| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | Er is geen code, manifest of zip aangeraakt. Het akkoord van 16 nov voor Click Joints 0.1.1 en Pro 1.0.2 blijft daardoor ongemoeid. | Feit (lijst gewijzigde bestanden en diff) | Hoog | Een diff buiten `architectuur.md` zou dit weerleggen. |
| 2 | De nieuwe regel zegt dat `bpy.ops.screen.screenshot` onder Xvfb een zwart beeld geeft en dat alleen `import -window root` werkt. Dat past bij de al genoemde `*-x.png`-bestanden en de Xvfb-opzet in het ontwerp. | Vermoeden | Midden | Het log van een run uit de e2e-workflow met een zwarte schermafbeelding. De diff laat dat niet zien. |
| 3 | Er staat dat `scherm_basis.schiet` sinds 19 nov geen zwarte versie meer maakt. Die codewijziging zit niet in deze diff. | Vermoeden | Laag | Een diff of commit van `scherm_basis.py` van 19 nov. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Er zijn geen tests aangepast. | Feit | Hoog | Tests niet aangepast om te slagen |
| 2 | `architectuur.md` is bijgewerkt. Dat is de hele wijziging. | Feit | Hoog | architectuur.md bijgewerkt |
| 3 | De bestandslengte kan ik niet nagaan, want de tekst is afgekapt. De regels zijn wel erg lang. | Vermoeden | Laag | Bestanden onder ±400 regels |
| 4 | Er staan geen persoonsgegevens, sleutels of wachtwoorden in de wijziging. | Feit | Hoog | Geen persoonsgegevens |
| 5 | "Alle versies" en "R4 19 nov" hebben geen GEZIEN-label of runnummer. | Feit | Hoog | Cijfers met GEZIEN/DERDEN/GOK |
| 6 | De commit noemt "notitie R4 rechtgezet", maar alleen `architectuur.md` is meegestuurd. Welke notitie dat is, zie ik niet. | Vermoeden | Midden | Wijziging moet bij de commitomschrijving passen |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Zet bij "alle versies" een GEZIEN-label met het runnummer waarin het zwarte beeld is vastgesteld.
- Verwijs bij de claim over `scherm_basis.schiet` naar de commit waarin dat is veranderd, of controleer die claim bij de volgende keuring met de code erbij.
- Maak duidelijk in welk bestand de "notitie R4" stond die is rechtgezet, of vermeld in de commit dat ze buiten deze diff valt.
- Houd `architectuur.md` in de gaten op lengte; splits het bestand als het ruim boven de ±400 regels komt.

---
Automatische keurder, model `claude-sonnet-5-5`, 17963 tokens in, 2044 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
