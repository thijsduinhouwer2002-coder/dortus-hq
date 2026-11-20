# Keuring trechter gratis naar Pro (README-concept en Short-beschrijving), 20 nov 2026, keurder A
Wat ik keurde: commit b45fa6ea5 op main: `commercie/blender-click-joints/trechter-2026-11-20.md` en `producten/blender-gewrichten/repo-click-joints/README.md` (verschil met 34021f72, de versie die Daan op 18 nov keurde).
Akkoord: nee

Kort: de tekst van de README klopt (functies, prijzen, anker). Hij mag pas de repo in samen met de GIF en de CHANGELOG, anders staat er bovenaan een kapot plaatje. De nieuwe Short-tekst klopt zelf ook, maar stuurt mensen naar dortus.com/yt, en daar staat nog de tekst van Pro 1.0 met "Hinges that click" en geen woord over de rig.

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | Alle zes punten in het blok "Pro, in addition to everything above" staan ook in de gekeurde Gumroad-tekst `platformen/blender-2/gumroad-1.1.md` deel 4, en de code van 1.1.0 (commit f727466) kan ze: botnamen Rigify, Mixamo, Auto-Rig Pro, Unreal, CC, VRoid, Biped en Daz, Limit Rotation met eindstop 30 tot 150, spiegelen (`rig.py`), zes presets Shoulder, Hip, Neck, Elbow, Knee, Ankle (`figuur.py`). De intro-zin ("hinge with an end stop at every elbow and knee, ball joint at shoulders, hips and neck") is dezelfde belofte als Gumroad. | feit (GEZIEN, git show f727466) | hoog | |
| 2 | Geen belofte die niet in 1.1.0 zit: geen testkaart, nergens "clicks" of "holds a pose". "click" komt alleen voor als werkwoord (op een knop klikken) en in de naam. "Measured in Blender, not print tested by us yet" staat er eerlijk bij. | feit (GEZIEN, grep op de README) | hoog | |
| 3 | Prijzen kloppen met Gumroad: Personal $19 (price_cents 1900), Studio +$40 = $59, Supporter +$5 = $24 (README noemt Supporter niet, mag). dortus.com/click-joints noemt ook $19 en $59. | feit (GEZIEN, curl 20 nov ±15:00 NL) | hoog | |
| 4 | Superhive staat op $12 / $45 en belooft daar "12 months of updates", niet "all Pro 1.x updates". In de README hangt "(also on Superhive)" achter de zin met $19, $59 en "all Pro 1.x updates included". Wie daar klikt, ziet een lagere prijs en andere updatevoorwaarden dan die zin zegt. Niet in het nadeel van de koper, wel onnauwkeurig. | feit (GEZIEN, curl Superhive) | hoog | |
| 5 | Links werken: Gumroad Pro 200, Superhive 200, extensions.blender.org/add-ons/click-joints 200, issues 200. | feit (GEZIEN, curl) | hoog | |
| 6 | Anker `#pro-in-addition-to-everything-above` klopt met de manier waarop GitHub ankers maakt: kleine letters, komma weg, spaties worden streepjes. Gecontroleerd op de huidige README van click-joints (koppen geven `user-content-click-joints-pro`, `report-a-problem`). Rendering via de markdown-API kon niet vanuit deze sessie. | feit voor de regel, vermoeden voor deze kop | hoog | na het pushen één keer op de link klikken |
| 7 | **De repo click-joints heeft geen `media/click-joints.gif` en geen `CHANGELOG.md`** (404 op raw, en de boom via de GitHub-API toont alleen LICENSE, README.md en click_joints/). De README verwijst bovenaan naar de GIF en onderaan naar CHANGELOG.md. Het bestand zegt bij "Wie doet het" alleen "README pushen". Wordt alleen de README gepusht, dan staat er bovenaan een kapot plaatje en een dode link: slechter dan nu. In `berichten/hoofdchat.md` regel 363 stond het plan al voor drie bestanden (README, GIF, CHANGELOG zonder de interne eerste 5 regels). | feit (GEZIEN) | hoog | |
| 8 | Short-tekst: geen Gumroad-adres, geen `<` of `>`, het adres `dortus.com/yt` zonder https om over te typen. Dat past bij REGELS (Short: links niet klikbaar, geen Gumroad in posts). Een Short is altijd oranje, dus de hoofdchat beslist; de hoofdchat voert het hier ook zelf uit, en de keuring door een ander is deze. De huidige beschrijving op YouTube is gelijk aan "Nu" in het bestand (GEZIEN, 1.216 weergaven). | feit (GEZIEN) | hoog | |
| 9 | dortus.com/yt bestaat (301 naar /yt/, 200, noindex, Amami-script) en heeft twee knoppen naar Gumroad Pro, prijs $19. **Maar de pagina beschrijft Pro 1.0**: kop "Hinges that click and stop at 115°", "printable click hinge", geen woord over rig, figuur of presets. De Short belooft "reads your rig"; wie dortus.com/yt overtypt, vindt die belofte niet terug. En "click" is precies de bewering die we nergens willen zolang er niet geprint is. Het trechterbestand noemt /yt "in orde": dat geldt alleen voor de prijs. Hetzelfde geldt voor de lange video van 17:00 (wijziging 3), die ook naar /yt wijst. | feit (GEZIEN, curl dortus.com/yt) | hoog | |
| 10 | Ook het Pro-blok op dortus.com/click-joints is nog Pro 1.0 ("Hinges that click and stop at 115°", "Click hinge"). Dat is een lek dat het bestand niet noemt: de pagina die de README en de gratis add-on als website noemen, verkoopt Pro zonder de nieuwe hoofdfunctie. | feit (GEZIEN, curl) | hoog | |
| 11 | Op het YouTube-kanaal gaat de eerste link rechtstreeks naar Gumroad (GEZIEN in de kanaalpagina). Volgens `marketing/REGELS.md` heet die link "Click Joints Pro ($12)": dan is dat hetzelfde lek als de oude README ($12 beloofd, $19 op Gumroad). Het label zelf kon ik met curl niet lezen. Ook REGELS zelf noemt bij "Doel" nog $12. | vermoeden | midden | label bekijken in YouTube Studio, Aanpassen, Links |
| 12 | Het Pro-blok in de README noemt drie dingen niet die op Gumroad, Superhive of dortus.com wel staan: gratis en Pro kunnen niet tegelijk aan; Pro werkt het best in Blender 4.5 en nieuwer (in 4.2 soms met de hand); een gewricht dat niet past wordt overgeslagen met een reden. De regel "Blender 4.2 LTS, 5.2 LTS and 5.3" staat boven de Pro-zin en lijkt zo ook voor Pro te gelden. Geen onwaarheid, wel minder eerlijk dan de winkel. | feit | midden | |
| 13 | De Short gebruikt `dortus.com/yt`, het meetadres van de lange video. Bezoek uit de Short en uit de lange video valt zo samen. REGELS kent geen adres voor Shorts; nu tellen tt en yt toch nog onder "overig", dus het kost nu niets aan meting. | feit | hoog | |

## Deel B: houdt het zich aan onze regels?
Doet keurder B. Wat ik onderweg zag: geen persoonsgegevens in de twee bestanden, behalve het mailadres van Dortus dat al in de gekeurde README stond.

## Deel C: zou een koper het fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | De nieuwe zin bovenaan de README is goed: in drie seconden weet je dat er een betaalde versie is, wat die doet en wat hij kost. | niets | |
| 2 | Wie vanuit de Short (rig, hele figuur) op /yt landt, ziet een andere belofte (één scharnier dat klikt). Dat voelt als een ander product. | /yt laten openen met de rig-belofte en het plaatje `1-figuur-uit-rig.png` | midden |

## Moet (blokkeert akkoord)
1. **README alleen samen met de GIF en de CHANGELOG naar click-joints** (deel A punt 7): `media/click-joints.gif` uit `producten/blender-gewrichten/repo-click-joints/media/` en een `CHANGELOG.md` (uit `producten/blender-gewrichten/CHANGELOG.md` zonder de interne uitleg bovenaan), in dezelfde push. Of de CHANGELOG-link weghalen. Zet het in "Wie doet het". Daarna deze README: akkoord.
2. **De Short (en de lange video van 17:00) pas naar dortus.com/yt laten wijzen als /yt de Pro 1.1-belofte draagt en nergens "click" als eigenschap van het scharnier zegt** (deel A punt 9). Tekst kan uit de gekeurde Gumroad-tekst deel 4. Gaat dat niet vandaag: de nieuwe Short-regel wacht. Daarna de Short-tekst zoals hij er staat: akkoord.

## Kan (mag later)
1. Superhive als eigen zin met een eigen voorwaarde, bijvoorbeeld "Also on Superhive (its own price and 12 months of updates)", of alleen "Also on Superhive" na de punt, los van $19 / $59 en "all Pro 1.x updates" (punt 4).
2. In het Pro-blok één regel: "Pro and the free Click Joints can not be enabled at the same time. Best in Blender 4.5 or newer; a joint that does not fit is skipped, with the reason." (punt 12).
3. Pro-blok op dortus.com/click-joints ook naar 1.1 en zonder "click" (punt 10). Hoort bij hetzelfde lek, valt buiten deze twee wijzigingen.
4. Het label van de kanaallink in YouTube Studio nakijken en de $12 eruit halen; en "$12" bij Doel in `marketing/REGELS.md` bijwerken (punt 11).
5. In `commercie/geplaatst.md` noteren dat /yt vanaf 20 nov ook bezoek uit Short 65JiRlDupNc telt, zodat het latere getal van yt niet alleen aan de lange video wordt toegeschreven (punt 13).
