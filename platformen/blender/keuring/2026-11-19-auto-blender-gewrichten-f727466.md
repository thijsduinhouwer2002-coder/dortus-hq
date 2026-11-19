# Keuring blender-gewrichten plaatje 19 (hoofdpaneel inklappen), 19-11-2026, automatische keurder
Wat ik keurde: commit f72746613 (bereik 01e317a..f727466), bestanden `e2e/scherm_basis.py` en `e2e/scherm_mens.py`
Akkoord: ja

## Deel A: doet het wat beloofd is?
De opdracht is de commitboodschap: teller en lijst van Figure joints in beeld op plaatje 19, door het paneel Click Joints in te klappen in plaats van te scrollen. De add-on zelf is niet veranderd (alleen proefscripts).

| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | `klap_hoofdpaneel` klikt met xdotool op de kop bovenaan de zijbalk. Dat is een andere aanpak dan de twee scrollpogingen, die volgens de commit geen effect hadden. | Feit (uit de diff) | Hoog | n.v.t. |
| 2 | Of het paneel echt dichtklapt, hangt af van de klikpositie: `regio.x + 60` en bovenkant van de regio plus 12 px. Als de zijbalk een marge boven de eerste kop heeft of met overlappende regio draait, kan de klik naast de kop vallen. | Vermoeden | Midden | Een nieuw plaatje 19 uit de run, waarop Figure joints met teller en lijst zichtbaar is |
| 3 | De functie geeft `True` zodra de zijbalk gevonden is, niet als het paneel echt dicht is. Het logregel "ingeklapt: True" bewijst dus niets over het resultaat. | Feit | Hoog | Een controle op de paneelstatus na de klik, of het plaatje zelf |
| 4 | Of het paneel Figure joints los staat van het paneel Click Joints (dus overblijft na het inklappen) staat in de commit, maar de architectuurtekst die ik kreeg is afgekapt. | Vermoeden | Midden | `paneel.py` of het plaatje |

## Deel B: houdt het zich aan onze regels?

| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Er is geen test aangepast om te slagen. Dit zijn schermscripts zonder asserties, en er is niets afgezwakt. | Feit | Hoog | Tests niet aanpassen om te slagen |
| 2 | `zijbalk_omlaag` is verwijderd en alleen de import in `scherm_mens.py` is bijgewerkt. Een andere `scherm_*.py` die hem nog importeert zou breken. Ik zie alleen deze twee bestanden. | Vermoeden | Midden | Een grep naar `zijbalk_omlaag`, of een groene run |
| 3 | In `scherm_mens.py` is het `subprocess.run`-blok weggehaald. Is `subprocess` daar nu ongebruikt, dan is dat alleen een kleine opruimkwestie. | Vermoeden | Laag | Lint of grep |
| 4 | Geen persoonsgegevens, sleutels of wachtwoorden in de wijziging. | Feit | Hoog | Persoonsgegevens |
| 5 | `architectuur.md` is niet bijgewerkt. Dat hoeft niet, want de add-on en de structuur zijn onveranderd. Bestandsgroottes zijn niet te zien in de diff. | Feit | Midden | architectuur.md, ±400 regels |

## Deel C: zou een gebruiker het leuk en fijn vinden?
Ik kan het plaatje niet zien. Dit gaat over een winkel- of ontwerpplaatje, niet over de add-on.

| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | Het plaatje toont straks een ingeklapt hoofdpaneel. De koper ziet dan niet de knoppen van stap 1 tot 3, alleen de lijst met gewrichten. | Daan beoordeelt of dat nog het juiste verhaal vertelt. Eventueel ook een apart plaatje met het paneel open. | klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Controleer na de klik of het paneel echt dichtgeklapt is, en meld dat in het log. Of laat de functie `False` geven als het niet zo is, zodat een mislukte klik niet stilletjes doorgaat.
- Zoek in de repo of `zijbalk_omlaag` nog ergens wordt gebruikt (mogelijke ImportError) en haal de ongebruikte `subprocess`-import weg, als die ongebruikt blijkt.
- Daan keurt het nieuwe plaatje 19 uit de volgende run op beeld. Pas dan is bevestigd dat de klik de kop raakt.

---
Automatische keurder, model `claude-sonnet-5-5`, 18791 tokens in, 2769 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
