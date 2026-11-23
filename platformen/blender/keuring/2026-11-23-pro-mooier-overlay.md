# Keuring Pro mooier overlay (code en beeld), 23 nov 2026, keurder (Claude, opdracht hoofdchat)
Wat ik keurde: tak `claude/pro-mooier-overlay` tegen main, kop 2250ff6c58f87a74d880e8a8eb4141b08cebcae8 (5 commits, 15 bestanden, +647 -29); voorstel `platformen/blender/mooier-overlay-2026-11-23.md`; release `pro-mooier-1` (RUN.txt: run 45163344015 op 2250ff6); e2e-run 45163344163; plaatje 19 in stand All op de tak `schermen`.
Akkoord: **ja voor samenvoegen naar main.** Uitbrengen pas na de drie moet-punten onderaan (die raken de winkeltekst en de test op main, niet de code van de tak).

Ik heb niets gebouwd. Daan keurde het ontwerp al (`2026-11-23-pro-mooier-overlay-daan.md`, ja); dit is de aparte keuring van code en regels. Zijn B1 (e2e rood) is inmiddels achterhaald, zie B1 hieronder.

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| A1 | Schakelaar "Labels Selected / All / None", standaard Selected, staat in het paneel Figure joints onder de samenvatting (na-m7-paneel, zelf bekeken). In de code: `WindowManager.cj_labels`, `default="SELECTED"`, `figuur.py` toont hem alleen als de eigenschap bestaat. | Feit (GEZIEN beeld en diff) | hoog | |
| A2 | Van 9 getallen plus kopregel naar 1 label met naam ("Right knee 0–120°") bij het gekozen gewricht, 0 als niets gekozen is, geen kopregel meer over het hoofd. Logregels voor/na: `getallen=9 ... koppen=['Right knee: bends 0° to 120°']` tegen `getallen=1 ... koppen=[]`, m2: 9 tegen 0. Zelf bekeken: vergelijk-m1, m2, m3, m5. | Feit (GEZIEN, mooi-voor.log en mooi-na.log) | hoog | |
| A3 | Echt mooier en duidelijker: het figuur leest als een mens met groene banden in plaats van een meetblad; de pil leest goed op het grijze been. Zwak: van voren staat de knieboog op zijn kant (m1, m5), dus voor opnames schuin filmen (zoals m3/m4). | Feit (GEZIEN), oordeel | hoog | |
| A4 | Voorbij de stop is bij een figuur het hele deel B (onderbeen met voet) rood, met een rode pil "+12° past limit" (vergelijk-m4). Log: rode vlakken 17 voor, 1025 na. | Feit (GEZIEN) | hoog | |
| A5 | Het rood gaat terug binnen de stop: `pose()` roept altijd eerst `_terug(a)` en `_terug(b)` aan; `_terug` zet eerst `cj_rood_deel` en dan `cj_rood_vlakken` terug, de omgekeerde volgorde van hoe ze rood werden. Toets zonder scherm in alle drie Blenders: "voorbij de stop: hele deel B rood (871 vlakken)" en "binnen de stop: alle vakken van A en B weer zoals eerst". | Feit (code gelezen, GEZIEN in de joblogs van 4.2.23 en 5.3.0) | hoog | |
| A6 | Export verandert niet. De pose staat in delta_rotation/delta_location (al zo sinds 1.0); de wijziging raakt alleen `material_index` van vlakken. STL gaat via `wm.stl_export` (geen materiaal), en `drie_mf.py` bevat geen enkel woord material, color, base of pid: de 3MF schrijft alleen vorm. Geen nieuw object, geen nieuwe mesh, geen modifier. | Feit (code gelezen), niet met een echte export nagemeten | hoog | een 3MF van deel B voorbij de stop exporteren en vergelijken met binnen de stop |
| A7 | Gratis deel ongemoeid: buiten `betaald/` veranderen alleen `e2e/` (toetsen en scripts), `architectuur.md` en twee workflows. Geen bestand in `click_joints/*.py`, `toets_zips.py` niet aangeraakt. | Feit (`git diff --name-only`) | hoog | |
| A8 | Buiten wat het voorstel noemt: `blender-gewrichten-e2e.yml` start nu ook op `claude/pro-mooier-*`, en een nieuwe workflow `pro-mooier.yml` (alleen op deze tak, `contents: write` om de release te vullen). Onschuldig, maar na samenvoegen dode takken (zie kan 3). | Feit | hoog | |
| A9 | Los scharnier en losse kogel tekenen zoals eerst: `labels.toon` geeft True zonder `cj_figuur`, `kleur_deel` draait alleen bij `cj_figuur`, de rode pil alleen bij een figuur. e2e-stap "plaatjes 11 en 12" en "Winkelplaatjes Pro 13 en 14" groen. | Feit (code, GEZIEN run 45163344163) | hoog | |
| A10 | In stand All tekent een figuur nu ook pillen in plaats van witte tekst met rand (plaatje 19 op de tak `schermen`, zelf bekeken): netter, de 40 px tussen vakken blijft gehaald. Dit verandert dus ook het beeld van de bestaande winkelplaatjes 15 tot 19 bij een nieuwe run. | Feit (GEZIEN) | hoog | |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| B1 | e2e-run 45163344163 op 2250ff6: uitslag success, jobs e2e (4.2.23), (5.2.3) en (5.3.0) groen, ook "Beeldvergelijking" en "Referentiebeelden bijwerken" (die bewaart per taknaam, raakt main niet). De zes nieuwe `[cj-figuur] OK`-regels van `mooier` staan in de joblogs van 4.2.23 en 5.3.0. | Feit (GEZIEN, `actions.py 45163344163` en joblogs) | hoog | tests groen |
| B2 | Schermtests 15, 16, 17, 19 zetten zelf Labels op All (`alle_labels()`, vóór `bouw()`). Eerlijk: geen enkele check is weggehaald of losser gemaakt; die plaatjes toetsen de plek van alle getallen, en dat gedrag bestaat alleen nog in All. De functie doet niets op oude code zonder schakelaar. De reden staat in de docstring en in architectuur.md. | Feit (diff gelezen) | hoog | tests niet aangepast om te slagen |
| B3 | Maar: de standaardstand Selected wordt op het scherm alleen getoetst door `scherm_mooi.py` in `pro-mooier.yml`, en die draait alleen op deze tak. Na samenvoegen heeft het beeld dat elke koper als eerste ziet geen schermtest meer op main; alleen de keuze-logica (`toon`, `met_naam`) blijft zonder scherm getoetst. | Feit (workflows gelezen) | hoog | testen in de echte app |
| B4 | Regels: `labels.py` 163, `figuur_teken.py` 301, `scharnier_beweeg.py` 311, `figuur.py` 288, `scherm_mooi.py` 213, `toetsen_figuur.py` 197. `scharnier_boog.py` 437 (was al 420 op main, nu +17). | Feit (`wc -l`) | hoog | onder ±400 regels |
| B5 | Dode code: `FIGUUR_X` in `figuur_teken.py` en `scharnier_boog.py` wordt nergens meer gelezen (vervangen door `labels.figuur_x`), en `figuur_teken.tekst_rand` ook niet. Drie keer 0,7 op drie plekken. | Feit (`git grep`) | hoog | opruimen hoort erbij |
| B6 | `architectuur.md` bijgewerkt met een volledige regel over `labels.py`, `kleur_deel`, de toets en de schermtests op All. | Feit | hoog | architectuur bijgewerkt |
| B7 | Geen persoonsgegevens in de diff (alleen `GH_TOKEN: ${{ github.token }}` in de workflow, geen sleutel). Cijfers in het voorstel hebben GEZIEN/DERDEN/GOK. | Feit | hoog | openbare repo, eerlijk |
| B8 | De tak staat 25 commits achter main, maar main veranderde sinds de basis niets aan de add-on (alleen `kijk_figuur.py`, `proef_ai_figuren.py` en proefbeelden), en `git merge-tree` geeft geen conflict. | Feit | hoog | |

## Deel C: zou een koper het mooi en fijn vinden? En de winkeltekst
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| C1 | Winkeltekst: "a degree arc and number at every joint" (changelog 1.1 in `winkeltekst-1.1.md` en `superhive-1.1.md`) blijft waar met All, maar de opsomming "**Every range in one view.** A small degree arc at each joint with its number" (`winkeltekst-1.1.md` regel 13, `superhive-1.1.md` regel 52, `superhive/where-to-find-it.md` regel 25) klopt na de update niet meer met wat een koper standaard ziet (één label). Dat raakt meer dan de ene zin die het voorstel noemt. | Bijvoorbeeld: "**Every range at a glance.** Select a joint to see its degree arc and range, or set Labels to All to show every joint at once; plus a list in the panel: name, type, range and where it came from." | klein |
| C2 | Bestaande kopers zien na de update ineens bijna niets meer (0 labels zonder keuze, m2). | In de releasenotes zeggen: "Labels: Selected is the new default; set it to All in Figure joints for the old view." | klein |
| C3 | Met niets gekozen staat er geen getal (m2). Goed voor een filmpje, maar een nieuwe koper weet niet dat hij moet klikken. | Eén korte regel onder de schakelaar zolang niets gekozen is, of na Figure from rig het eerste gewricht kiezen (zelfde als Daan C5). | klein |
| C4 | Eens met Daan C2 en C3: de boog in Selected is bleker dan voor (vergelijk-m3), en het groene bolletje in de naampil spreekt het rode been tegen (m4). | Boog feller in Selected; bolletje rood voorbij de stop. | klein |
| C5 | Wie de mesh bewerkt terwijl het been rood is (ander aantal vlakken), houdt een volledig rood deel: `_terug` gooit `cj_rood_deel` dan weg zonder terug te zetten. Zeldzaam, en ook zo bij de oude rakende vlakken (die worden deels teruggezet). Het rood blijft ook in een opgeslagen .blend zolang de schuif voorbij de stop staat (zoals eerst). | Bij een ander aantal vlakken het rode vak per vlak terugzetten naar vak 0 of naar het eerste niet-rode vak. | klein |
| C6 | Stand Labels staat op de WindowManager en gaat vermoedelijk niet mee in de .blend (Daan C7). | Later op de scene of in de voorkeuren. | klein |

## Wat er bij uitbrengen moet veranderen
- Versie (Bram beslist 1.2.1 of 1.3): `PRO_VERSIE` in `blender-gewrichten-e2e.yml` en `TAG`/`VERSIE` in `click-joints-pro-uitgave.yml`.
- Winkelteksten Gumroad en Superhive: de zin "Every range in one view ..." en de changelog-zin aanpassen (C1), plus een regel in de releasenotes over de nieuwe standaard (C2).
- Winkelplaatjes 15 tot 19 en de Shorts opnieuw opnemen: in All staan nu pillen (A10), en het eerste beeld kan beter Selected of None zijn, schuin gefilmd (A3).
- Na samenvoegen de branch-trigger `claude/pro-mooier-*` en `pro-mooier.yml` opruimen of bewust houden (kan 3).

## Moet (blokkeert uitbrengen, niet het samenvoegen)
1. Een schermtest van de standaard Selected in de gewone e2e op main (B3): bijvoorbeeld het na-deel van `scherm_mooi.py` als stap in `blender-gewrichten-e2e.yml`, met `MOOI OK` als eis, of één plaatje van een figuur in Selected met een check "1 label, met naam, geen kopregel". Anders bewaakt niets meer het beeld dat elke koper als eerste ziet.
2. Winkelteksten aanpassen op Gumroad en Superhive vóór de nieuwe zip erop staat (C1, en C2 in de releasenotes). Teksten naar buiten gaan via keuring en de hoofdchat.
3. Na samenvoegen met de nieuwste main opnieuw e2e groen in 4.2, 5.2 en 5.3 (geen conflict verwacht, B8).

## Kan (mag later)
1. Dode code weg: `FIGUUR_X` in `figuur_teken.py` en `scharnier_boog.py`, `tekst_rand` (B5).
2. `scharnier_boog.py` onder ±400 regels brengen, bijvoorbeeld de tekenfunctie `_teken_een` naar een eigen bestand (B4); hoort in de eerstvolgende opruimtaak.
3. Workflows: `claude/pro-mooier-*` uit de trigger van de e2e halen en `pro-mooier.yml` weg of op `workflow_dispatch` met een vaste voor-commit zetten (A8).
4. C3, C4 (sterk aangeraden vóór nieuwe opnames), C5, C6.
5. Eén echte 3MF-export voorbij de stop nameten (A6), voor de zekerheid.
