# Keuring blender-gewrichten AI-figuren proef, 23-11-2026, automatische keurder
Wat ik keurde: commit de4d115fa (5371409..de4d115), twee proefscripts, log.txt en uitslag.md. De vijf beelden zag ik niet.
Akkoord: nee

## Deel A: doet het wat beloofd is?
De add-on zelf is niet veranderd. Ik toets dus of de proef de vraag beantwoordt: werkt Figure from rig op AI-figuren, en waar valt een gewricht weg?

| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | Het log laat per figuur zien welke gewrichten er kwamen en welke wegvielen, elk met de reden van de add-on. Alle delen zijn gesloten en elk is één stuk (`open []`, `stukken [1,1,...]`). | Feit | Hoog | Staat in log.txt. |
| 2 | Bij man_cap staat "armen nee links, nee rechts", en bij spacetrooper1 "nee rechts". Schouders en ellebogen worden daar niet geprobeerd en staan niet onder OVERGESLAGEN. uitslag.md noemt dit niet, terwijl de vraag "waar valt een gewricht weg" was. | Feit | Hoog | Een regel in uitslag.md over waarom de armbotten niet gevonden zijn (model of proefrig). |
| 3 | De oorzaak "knie geweigerd door de add-on, verkeerde tip bij een dik been" is een redenering over `maten_neus`. Het stuk is zelf gemarkeerd als GOK. | Vermoeden | Midden | Een run op spacetrooper1 met de wang- en sleufmaten uit `scharnier_neus` gelogd. |
| 4 | "Schouder: onze proefrig" en "elleboog: terecht" staan er als feit, maar de bewijsstukken zijn beelden die ik niet zag. | Vermoeden | Laag | Het voor- en zijbeeld van spacetrooper1 met de botkoppen. |
| 5 | Dat man_cap na de draai beide knieën kreeg, volgt uit het log (twee knieën, 90 graden gedraaid). De juiste voorkant (tenen naar -y) is alleen uit een beeld te controleren. | Feit voor de knieën, vermoeden voor de richting | Midden | Het vooraanzicht van man_cap. |

## Deel B: houdt het zich aan onze regels?

| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | uitslag.md zegt "Heupen vallen ... bijna altijd weg (5 van 6 hier)". Het log toont 4 heupen die wegvallen, bij de twee figuren die een rig kregen. Businessman kreeg geen rig en dus geen heupen. 5 van 6 klopt niet met het log. | Feit | Hoog | Cijfers moeten kloppen en een label hebben (GEZIEN/DERDEN/GOK). |
| 2 | "Ook gedraaid met CJ_HEUP_PCT=52 ... zelfde uitslag" en de melding "keep 21 mm apart" staan alleen in de tekst. Het log hoort bij de standaardrun. | Vermoeden | Midden | GEZIEN vraagt bewijs in de wijziging. |
| 3 | "(MIT)" voor de Meshy-set staat zonder label. Het is ook niet gezegd of renders van die modellen in de repo mogen. | Vermoeden | Laag | Cijfers en bronnen met GEZIEN/DERDEN. |
| 4 | Tests zijn niet aangepast. Er zijn geen persoonsgegevens, geen sleutels en geen bestanden boven de 400 regels. architectuur.md hoeft niet mee, want de add-on veranderde niet. | Feit | Hoog | Regels voor tests, omvang, persoonsgegevens en architectuur. |
| 5 | `kijk_figuur.py` schrijft `.png`, maar in de map staan `.jpg`. De omzetting is nergens beschreven. Er staat een `-rig-voor.jpg` van businessman terwijl diens rig mislukte. | Vermoeden | Laag | Reproduceerbaarheid. |

## Deel C: zou een gebruiker het leuk en fijn vinden?

| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | Op beide figuren met rig vallen alle vier de heupen weg. De belofte "hele figuur in één keer" geldt voor AI-figuren dan maar half. | Een heupstrategie voor korte dijen, bijvoorbeeld een kleinere bal of een andere plek, of een duidelijke tip. | Midden |
| 2 | "Tight: cheek too stiff ... Try a thicker spot" is misleidend op een al dik been. De koper zoekt dan de verkeerde kant op. | Een aparte tekst voor "wang dik maar sleuf te kort" of "rek te hoog". | Klein |
| 3 | "Place it by hand" bij de heupen zegt niet waar of hoe. | Een voorgestelde hoogte of een knop "Place here anyway". | Klein |
| 4 | Een figuur in een lange jas (businessman) krijgt geen enkel gewricht. | Een bericht dat uitlegt dat een jas of gesloten rok niet werkt, of dat er eerst gesplitst moet worden. | Klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet**
1. Corrigeer "5 van 6" in uitslag.md naar wat het log toont (4 van 4 bij figuren met een rig, businessman buiten beschouwing), of voeg het log toe dat 5 van 6 onderbouwt.

**Kan**
1. Zet het log van de CJ_HEUP_PCT=52-run erbij, of haal die zin weg.
2. Noem in uitslag.md de ontbrekende armbotten bij man_cap en spacetrooper1 rechts.
3. Label de gevolgtrekkingen over schouder en elleboog duidelijk als vermoeden.
4. Leg vast hoe de png's jpg's werden, en waarom er een rig-beeld van businessman is.
5. Controleer de licentie van de Meshy-set voor renders in de repo, en label die als DERDEN.
6. Het `exec` van `proef_meshy_rig.py` met een `replace` op `\nmain()\n` is breekbaar. Importeer liever een functie.

---
Automatische keurder, model `claude-sonnet-5-5`, 23546 tokens in, 5153 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
