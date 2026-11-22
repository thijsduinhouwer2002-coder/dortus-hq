# Keuring elleboog naar voren (Click Joints Pro, Figure from rig), 22-11-2026, Daan
Wat ik keurde: tak `claude/blender-elleboog-2026-11-22`, commit becfa97 (`betaald/rig.py`, `betaald/een_lid_diep.py`, architectuur.md). Zelf gedraaid in Blender 5.3.0 (eigen sessie) met de betaalde zip van becfa97 (`e2e/maak_zip.sh betaald`), op Quaternius Yeti en Orc (Big/Blends, CC0, via gdown) met `commercie/filmpjes/monsters/proef_monster.py`. Daarna elk deel B van een scharnier 90 graden gebogen (`scharnier_beweeg.zet_scharnier`) en van boven en voor gerenderd, Workbench, ortho, alleen de zichtbare figuurdelen (script: `2026-11-22-elleboog-voren-daan-pose.py`).
**Akkoord: ja**, op voorwaarde dat de e2e van becfa97 (run 45017037371) groen eindigt. Bij mijn keuring liep die nog in alle drie de versies.

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | Yeti: 4 gewrichten (beide ellebogen 0 tot 135, beide knieën 0 tot 135), schouders vallen af met "too close to another joint, keep 34 mm apart". Orc: 4 (zelfde), was 2. Alle 5 delen 1 stuk. Gelijk aan wat Bram meldt. | Feit (GEZIEN, log van mijn run) | hoog | |
| 2 | **De ellebogen buigen nu naar voren.** `cj_buigkant` van beide ellebogen is (±0,02, -1,00, 0,00), de voorkant is -Y. Op de beelden gaan de onderarmen bij 90 graden naar voren, naar de buik; hoofd en romp heel. Knieën buigen naar achteren zoals het hoort. Beelden: `2026-11-22-elleboog-voren-daan-yeti-boven.png`, `-yeti-voor.png`, `-orc-boven.png`. | Feit (GEZIEN) | hoog | |
| 3 | De hele onderarm met hand is deel B (van elleboog tot vingers), niet alleen een stuk binnen het omhulsel. | Feit (GEZIEN, boven-beeld) | hoog | |
| 4 | De moet van mijn vorige keuring is weg: geen stand naar achteren meer in `gedraaid` (alleen `[0]` wordt gebruikt), alleen voor ELBOW. Knie en enkel krijgen het vangnet niet (kan 1 van toen ook gedaan). | Feit (code gelezen) | hoog | |
| 5 | `ALTIJD_H` staat alleen aan tijdens de gedraaide plekken en gaat in een `finally` weer uit, dus een fout in `plaats_gewricht` laat hem niet aan staan. | Feit (code gelezen) | hoog | |
| 6 | `gedraaid` kiest "voren" vast als -Y (Blender-gewoonte). Een figuur die naar +Y kijkt, krijgt in het vangnet een elleboog die naar achteren buigt. Quaternius en de MakeHuman-mens kijken naar -Y, dus voor nu geen probleem. | Vermoeden (code gelezen) | midden | Een rig die naar +Y kijkt door de knop halen. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Architectuur.md bijgewerkt met het vangnet en de reden. | Feit | hoog | bouwen.md |
| 2 | Nog geen toets op `gedraaid` of op `ALTIJD_H` (alleen de monsterproef buiten de e2e). | Feit | hoog | bouwen.md |
| 3 | Brams beelden (`2026-11-22-elleboog-voren-*.png` zonder "daan") tonen ook de verborgen bron-mesh in T-houding: de armen lopen door tot de rand en de benen lijken recht. Workbench rendert objecten die alleen in beeld verborgen zijn wel. De uitslag klopt, maar het beeld kan iemand op het verkeerde been zetten. Mijn beelden hebben `hide_render` op alles buiten de figuurdelen. | Feit (GEZIEN, vergelijking) | hoog | eerlijk |
| 4 | Cijfers in het commentaar (18 tot 21%, y -38 tot 10 mm) met GEZIEN; ik heb die niet nagemeten, wel de uitkomst. | Feit | midden | eerlijk |
| 5 | Geen persoonsgegevens of sleutels. | Feit | hoog | |

## Deel C: zou een koper het fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | Vier gewrichten die goed buigen zijn beter dan zes waarvan twee de verkeerde kant op. Een monster dat zijn armen naar voren vouwt is precies wat een Short wil laten zien. | | |
| 2 | Wel: de Yeti verliest zijn schouders. Een koper die eerst zes zag (oude Short of proef) ziet nu minder. | Kan 2. | midden |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen (alleen: e2e becfa97 groen afwachten voor main).

**Kan:**
1. Voren afleiden uit de rig in plaats van vast -Y, bijvoorbeeld tegen de buigkant van de knie in (die buigt naar achteren), zodat A6 niet kan gebeuren.
2. Schouders terug op de Yeti: kijk of de elleboogplek iets verder het onderste lid in (10 of 20%) de 34 mm vrijmaakt, of zet de schouder eerst.
3. Een kleine toets op `gedraaid` (kolom 2 gelijk, determinant 1, buigkant naar -Y) en op `ALTIJD_H` (staat na de knop altijd uit).
4. Keurbeelden voortaan met `hide_render` op de bron-mesh (zie mijn pose-script).

## Hoe ik keek
Blender 5.3.0 linux, `--factory-startup`, Pro-zip uit becfa97 (PRO_VERSIE 1.1.0). Render met `2026-11-22-elleboog-voren-daan-pose.py`: alleen delen met `cj_figuur` die zichtbaar zijn, delen die op `_B` eindigen krijgen `cj_pose_graden` 90.
