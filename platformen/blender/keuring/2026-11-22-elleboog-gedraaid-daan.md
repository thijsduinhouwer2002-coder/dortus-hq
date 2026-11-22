# Keuring elleboog gedraaid (Click Joints Pro, Figure from rig), 22-11-2026, Daan
Wat ik keurde: tak `claude/blender-elleboog-2026-11-22`, commit 86800a6, `click_joints/betaald/rig.py` (functie `gedraaid` en het vangnet in de knop). Zelf gedraaid in Blender 5.3.0 (eigen sessie) met de betaalde zip van deze tak, op Quaternius Yeti en Orc (Big/Blends, CC0) met het script van Chris (`commercie/filmpjes/monsters/proef_monster.py`), daarna de scharnieren 90 graden gebogen en van boven en opzij gerenderd.
**Akkoord: nee** (één moet)

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | Yeti krijgt 6 gewrichten (beide ellebogen 0 tot 135, knieën, schouders), Orc 4 (beide ellebogen erbij, was 2 bij Chris). Alle delen 1 stuk. | Feit (GEZIEN, log van mijn run) | hoog | |
| 2 | **De gedraaide ellebogen buigen naar achteren.** Op de Yeti wint bij beide ellebogen de laatste kandidaat (i 8 van 9, GEZIEN met een tijdelijke printregel), dat is `gedraaid(kandidaten[0])[1]`, de stand naar achteren. De vier naar voren gedraaide plekken (i 4 tot 7) worden alle vier geweigerd. `cj_buigkant` van de ellebogen is (0, +1, 0), net als de knieën; de Yeti kijkt naar -Y (snuit onderaan in het bovenbeeld). Beelden: `2026-11-22-elleboog-gedraaid-yeti-boven.png` en `-zij.png`: onderarmen gaan bij 90 graden naar de rug. | Feit (GEZIEN) | hoog | Zelfde print op Orc; ik heb Orc niet gebogen gerenderd (GOK: zelfde patroon). |
| 3 | De volgorde in `gedraaid` klopt: naar voren komt eerst. Het probleem is dat naar voren nergens lukt en de terugvaloptie naar achteren dan stil wint. | Feit (GEZIEN, volgorde i) | hoog | |
| 4 | Rigs die al werkten veranderen niet: de lus stopt bij de eerste geslaagde plek, en de e2e op de tak is groen (run 45007495690, GEZIEN API). Knieën op de Yeti winnen met i 0. | Feit | hoog | |
| 5 | Lege `kandidaten` kan niet: `scharnier_plekken` begint altijd met `[(m, 0.0)]`. Punt A4 van de automatische keurder vervalt. | Feit (code gelezen) | hoog | |
| 6 | Het vangnet geldt voor elk scharnier (elleboog, knie, enkel). Faalt een knie op de as uit de rig, dan krijgt hij zo een knie die opzij buigt (lidas verticaal, beide gedraaide standen hebben een buigkant opzij). | Vermoeden (code gelezen, niet gezien op een rig) | midden | Een rig waar de knie eerst geweigerd wordt. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Geen test voor het vangnet; architectuur.md niet bijgewerkt (zie automatische keuring B1, B2). | Feit | hoog | bouwen.md |
| 2 | Cijfers in het commentaar (16%, z 126) hebben GEZIEN; mijn run bevestigt de uitkomst 6, niet die cijfers. | Feit | midden | eerlijk |
| 3 | Geen persoonsgegevens of sleutels. | Feit | hoog | |

## Deel C: zou een koper het fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | Een elleboog die naar achteren buigt is een kapot figuur: de koper print het en de arm vouwt de verkeerde kant op. Erger dan "place it by hand", want de lijst zegt "Left elbow · Hinge · 0–135°" alsof het goed is. Voor de Shorts van Chris zou dit ook direct opvallen. | Zie moet. | |
| 2 | Wel winst: de snede in de gedraaide stand laat het hoofd heel, dus het idee werkt. | | |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:**
1. Geen elleboog die naar achteren buigt. Haal de extra kandidaat `gedraaid(kandidaten[0][0])[1]` weg, of laat hem alleen toe als het gewricht geen elleboog of knie is. Liever: zoek uit waarom de vier plekken naar voren worden geweigerd (welke `fout`: verloren stuk, los stuk, te dun?) en los dat op, bijvoorbeeld door de stop naar voren met een kleinere hoek of de plek iets verder het onderste lid in. Lukt naar voren niet, dan "place it by hand" zoals voorheen. Bewijs: Yeti gebogen gerenderd van boven, onderarmen naar de buik.

**Kan:**
1. Beperk het vangnet tot de elleboog (of tot leden die in de rust bijna horizontaal liggen), zodat een knie nooit opzij gaat buigen (A6).
2. Een kleine toets op `gedraaid`: kolom 2 gelijk, determinant 1, eerste stand naar -Y.
3. Een regel in architectuur.md over het vangnet.

## Hoe ik keek
Render: `pose.py` in mijn sessie: elk scharnierdeel B krijgt `cj_pose_graden` 90 via `scharnier_beweeg.zet_scharnier`, Workbench, orthografisch van voor, boven en +X. Voorkant van de Yeti is -Y (snuit en tong wijzen in het zijbeeld naar links, -Y).
