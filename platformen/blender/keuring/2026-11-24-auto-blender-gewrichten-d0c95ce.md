# Keuring blender-gewrichten (Pro 1.2.6, kan A3), 24-11-2026, automatische keurder
Wat ik keurde: commits fedd1bf..d0c95ce (8b012bb5f en 249647626): `click_joints/betaald/rig.py` (alleen commentaar) en `e2e/toetsen_robot_meer.py` (nieuwe toets A3)
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | Aan het gedrag van de add-on verandert niets: in `rig.py` is alleen een commentaar herschreven. De zip voor gebruikers blijft gelijk. | Feit (uit de diff) | hoog | Een diff van de zip van 1.2.6 tegen de vorige bouw. |
| 2 | De nieuwe toets A3 controleert dat een echt weggevallen voet nog door het vangnet wordt gevangen (scheen alleen boven 6% verloren, scheen met voet op of onder 6%). Dat past bij de belofte van 1.2.6: het vangnet blijft werken nu de bol groter is. | Feit (uit de code) | hoog | Een groene run met regels `A3 Left ankle` en `A3 Right ankle`. |
| 3 | De eis geldt alleen voor Blender 4.5 en nieuwer. In 4.2 wordt A3 niet gedraaid, en dat staat ook in de docstring. | Feit | hoog | Een run op 4.2.23 die de rest van de toetsen groen laat. |
| 4 | "Lokaal 5.3.0 groen" staat alleen in de commitmelding. Een CI-run voor deze twee commits in 5.2.3 en 5.3.0 zie ik niet. | Vermoeden | midden | De Actions-run voor d0c95ce, met de A3-regels in het log. |
| 5 | Het getal in het commentaar is gecorrigeerd van "±48%" naar "32 tot 35%". Dat klopt met de toetsdocstring, maar ik kan de meting zelf niet nagaan. | Vermoeden | midden | De logregels `zonder voet N% verloren` uit een run. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | De toets is nieuw en geen bestaande toets is versoepeld. De grenzen (6% en de 32 tot 35% uit de meting) zijn niet aangepast om te slagen. | Feit | hoog | Tests niet aanpassen om te slagen |
| 2 | `toetsen_robot_meer.py` is na de wijziging ruim onder de 150 regels. `rig.py` is al ruim langer dan 700 regels, maar deze wijziging maakt hem niet langer. | Feit | hoog | Bestanden onder ±400 regels |
| 3 | `architectuur.md` is niet bijgewerkt. Dat hoeft hier niet, want de structuur van de add-on verandert niet. | Feit | midden | architectuur.md bijgewerkt |
| 4 | Er staan geen persoonsgegevens, sleutels of wachtwoorden in de wijziging. Wel noemt het commentaar de namen Daan en Olaf als bron. | Feit | hoog | Geen persoonsgegevens |
| 5 | De cijfers in het commentaar (26 mm, 32 tot 35%) hebben geen label GEZIEN, DERDEN of GOK. De bron ("lokaal 5.3.0") staat wel in de docstring. | Feit | hoog | Cijfers met GEZIEN, DERDEN of GOK |
| 6 | De toets rekent de bol zelf uit (`max(0.6 * lengte, 15 * u)`) en kopieert die formule uit `rig.py`. Als `rig.py` verandert, kan de toets stil afwijken. De toets gebruikt dus niet dezelfde constanten als de code. | Vermoeden (ik zie `rig.py` niet helemaal) | midden | Een gedeelde constante of functie, of een toets die de bol uit `rig.py` zelf opvraagt. |

## Deel C: zou een gebruiker het leuk en fijn vinden?
Niet van toepassing: er is niets te zien of te spelen. Het gaat om een toets en commentaar.

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
1. Wacht op de CI-run voor deze commits (5.2.3 en 5.3.0) voordat je 1.2.6 uitbrengt, want nu staat alleen een lokale run in de commitmelding (A4).
2. Haal de bolformule in de toets uit `rig.py` zelf, zodat toets en code niet uit elkaar kunnen lopen (B6).
3. Zet GEZIEN voor de 32 tot 35% in het commentaar (B5).
4. `rig.py` is veel langer dan 400 regels. Dat was al zo; splits hem bij een volgende ronde.
5. De hashes 8b012bb5f en 249647626 in de lijst komen niet letterlijk overeen met het eind van de reeks (d0c95ce). Controleer of de keuring de goede commits dekt.

---
Automatische keurder, model `claude-sonnet-5-5`, 20246 tokens in, 4077 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
