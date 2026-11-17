# CPU in het gewone spel: waarom is de graver zuiniger? (Bram, 16 nov 2026 ±21:35 UTC)

Vraag Iris (keuring 9, `platformen/steam/keuring/2026-11-16-21.md` punt 3): gewoon spel 0,84 tot 1,23 CPU-s per 10 s, de graver (`koper=1`) maar 0,59.

## Wat ik deed
1. De vier Windows-duurtests van 16 nov (tak `schermen`, `steam-hol-duur/main-1920x1080`, `main-koper-1-1920x1080`, `main-koper-2-1920x1080`, `main-1920x1080-exe`) naast elkaar gelegd: `cpu-per-10s.txt` tegen de regels `HOL meting t= beelden= helden= hol_vast=` uit `hol.log`. Script `cpu_per_beeld.py` en `cpu_plat.py`, uitkomst `uitkomst.txt`.
2. Hetzelfde spel (main, `zaad=4242`, 250 s, 1920 breed, strook 120) op Linux gedraaid met Godot 4.3 onder xvfb (opengl3, software), gewoon en `koper=1`. Script `meet_linux.sh`, uitkomst in `linux/`.

## Wat de cijfers zeggen (GEZIEN)
- **Op Windows kost een beeld bij de graver een derde:** gewoon 16,7 ms CPU per getekend beeld, koper=2 (koopt, graaft niet) 15,3, de .exe 14,1, **koper=1 (koopt en graaft) 5,6**. De graver tekent juist meer beelden (105 per 10 s tegen 67 tot 73), dus het ligt niet aan minder tekenen.
- CPU volgt het aantal beelden (correlatie 0,57 tot 0,69): zonder held in beeld tekent het spel ±1 beeld per s en kost het bijna niets, met een held 10 tot 20 per s. Daarom het patroon hoog, hoog, laag in het ritme van de helden.
- **Niet Gloop plat:** binnen een run is de CPU met en zonder plat ongeveer gelijk (gewoon 1,41 tegen 1,27 met held; koper-2 1,03 tegen 1,10).
- **Niet het vaste hol opnieuw tekenen:** de graver tekent het vaste hol het vaakst (1,4 keer per 10 s tegen 0,25) en is toch het zuinigst.
- **Op Linux is er geen verschil per beeld:** gewoon 9,7 ms, koper=1 10,2 ms per beeld; daar kost de graver juist meer (meer beelden). Het voordeel van de graver bestaat dus alleen op Windows.

## Lezing (GOK, nog niet bewezen)
Het verschil zit in iets dat alleen op Windows telt en dat graven verandert, niet kopen (koper=2 koopt ook en blijft duur). Graven doet op Windows één ding extra: na elk nieuw vast beeld meet `hol_vast.gd` de bovenrand opnieuw en zet `strook.gd` `rand_veranderd()` het muisvlak opnieuw (`DisplayServer.window_set_mouse_passthrough`). Op Windows is dat een vensterregio: buiten het vlak tekent het venster niets. Mogelijk is het vlak dat bij de start één keer gezet wordt (vóór de bovenrand gemeten is, of met de volle hoogte) groter of anders dan nodig, en kost elk beeld daardoor meer om op het scherm te zetten; de graver zet het vlak steeds opnieuw.

## Proef die het beslist (Windows, voor Olaf)
Duurtest gewoon spel met één regel erbij die het muisvlak elke 30 s opnieuw zet (`_muis_vlak(vlak_paneel)` in `_process`, alleen met een startargument). Zakt de CPU naar ±0,6, dan is het het vlak: dan het vlak na de eerste meting van de bovenrand nog één keer zetten. Blijft hij hoog: dan zit het in iets anders dat graven verandert (bijvoorbeeld de helden die bij een gegraven hol korter over het gras lopen), en meet ik dat met een logregel per held boven of in de gang.

## Proef gestart (16 nov ±21:35 UTC, Bram)
Tak `claude/steam-hol-vlak-proef` (7808f65): startargument `vlak_elke=<s>` zet het muisvlak elke s seconden opnieuw, alleen met het argument (2 regels in `kern/strook.gd`, 1 in `kern/proef.gd`; toets_systemen en toets_held lokaal 0 FOUT). Twee duurtests tegelijk op die tak, 20 min, 1920x1080, `zaad=1794860558` (zelfde helden als Olafs gewone run 43948989836): met `vlak_elke=30` (run 43961482697) en zonder (run 43961487906). Uitkomst op tak `schermen` → `steam-hol-duur/claude-steam-hol-vlak-proef-zaad-1794860558-vlak-elke-30-1920x1080/` en `.../claude-steam-hol-vlak-proef-zaad-1794860558-1920x1080/`. Lezing: proef duidelijk lager dan zonder (±0,6 tegen ±1,2) = muisvlak; gelijk = GOK fout, dan meet ik de helden boven en in de gang. De tak gaat niet naar main; Olaf beslist wat er van komt.


## Stand 16 nov ±22:30 UTC (Bram, na Iris keuring 10 punt 3)
- `vlak_elke=30` gaf 1,357 CPU-s per 10 s tegen 0,844 voor main op hetzelfde zaad (Iris). Niet lager, dus **mijn GOK muisvlak is waarschijnlijk fout**. Ik trek hem in tot de controle er is.
- De controle-run zonder argument (43961487906) stond om 22:30 nog op `in_progress` (gestart 21:34), en staat nog niet op `schermen`. De twee runs liepen tegelijk; Iris ziet 0,59 tot 1,36 voor ongeveer hetzelfde spel, dus de machine per run kan meer schelen dan wat we zoeken.
- **Volgende stap (eens met Iris):** zodra de controle binnen is, dezelfde run (main, zaad 1794860558) twee keer **na elkaar** draaien, niet tegelijk. Liggen die twee meer dan 0,2 uit elkaar, dan is CPU per run op deze runners ruis en meten we alleen nog CPU per getekend beeld binnen één run (zoals `cpu_per_beeld.py`), niet tussen runs. De vlak-proeftak blijft een proef en gaat niet naar main.

## Controle binnen, en een betere proef (Bram, 16 nov ±23:20 UTC)
- **Controle zonder argument (run 43961487906) is binnen:** 0,948 CPU-s per 10 s (14,5 ms per beeld) tegen 1,357 (19,5 ms) mét `vlak_elke=30`, zelfde tak en zaad, tegelijk gedraaid. Het muisvlak elke 30 s opnieuw zetten maakt het dus niet zuiniger. **GOK muisvlak als oorzaak van de zuinige graver: fout.**
- **Ruis tussen runs, GEZIEN:** drie keer dezelfde .exe op zaad 4242 na elkaar (`main-zaad-4242-herhaal-a/b/c`): 0,86 / 0,71 / 0,77, en 17,2 / 13,0 / 15,3 ms per beeld. Hetzelfde spel op zaad 1794860558 gaf 0,84 tot 1,28 over vier runs. Een verschil tussen twee runs onder ±0,4 CPU-s (±30% per beeld) zegt dus niets. Daarom vergelijk ik niet meer tussen runs.
- **Nieuwe proef binnen één run** (tak `claude/steam-hol-wissel-proef`): startargument `wissel=vlak` zet het muisvlak in oneven minuten uit (hele venster getekend en klikbaar) en in even minuten aan, met een logregel `HOL wissel vlak aan/uit`. `cpu_wissel.py` deelt de CPU per 10 s in naar aan en uit (alleen het midden van elke minuut). Keurder (aparte agent): Godot-kant goed (hoog), randen in het script aangepast.
- **Meetlat (placebo):** hetzelfde script op tien oude runs zonder wissel geeft tussen de "aan"- en "uit"-minuten 0 tot 2,6 ms per beeld verschil (gemiddeld ±1,2). Pas een verschil van meer dan ±3 ms per beeld (±20%) in de wissel-runs telt.
- Twee wissel-runs gestart (20 min, 1920x1080, zaad 1794860558): de .exe en de editor-Godot. Uitkomst op tak `schermen` in `steam-hol-duur/claude-steam-hol-wissel-proef-zaad-1794860558-wissel-vlak-1920x1080(-exe)/`; draai `python3 cpu_wissel.py <map>`.
- **Derde proef gestart:** `wissel=doorzicht` (zelfde tak, 5e3282e) maakt het doorzichtige venster in oneven minuten dicht (zwarte lucht). Het doorzichtige venster en het muisvlak zijn de twee dingen die alleen op Windows zo werken, dus daar zoek ik het verschil Windows tegen Linux. Run .exe, 20 min, zaad 1794860558; map `...-wissel-doorzicht-1920x1080-exe/`. Lokaal op Linux 135 s: wissels op 60,0 en 120,0 s, 0 scriptfouten.
- **Lezing straks:** scheelt een van beide meer dan ±3 ms per beeld, dan is dat de plek; scheelt geen van beide, dan zit de Windows-kost in het tekenen zelf (ANGLE) en meet ik `--rendering-driver opengl3` tegen `d3d12` op dezelfde manier. De proeftak gaat niet naar main; Olaf beslist wat er van komt.

## Wissel-uitslag: muisvlak en doorzicht zijn het niet (Bram, 17 nov ±00:40 UTC)
`python3 cpu_wissel.py <map>` op de drie wissel-runs (tak `claude/steam-hol-wissel-proef`, zaad 1794860558, 20 min, 20 wissels in elke log, GEZIEN op tak `schermen`):

| run | aan (even minuten) | uit / dicht (oneven minuten) | verschil per beeld |
|---|---|---|---|
| `wissel=vlak`, .exe (43978311250) | 13,6 ms (1,042 CPU-s per 10 s) | 14,5 ms (1,030) | 0,9 ms |
| `wissel=vlak`, editor (43978315655) | 17,4 ms (1,201) | 19,8 ms (1,312) | 2,4 ms |
| `wissel=doorzicht`, .exe (43979424003) | 14,8 ms (1,077) | 16,9 ms (1,159) | 2,1 ms |

Alle drie onder de meetlat van ±3 ms per beeld (placebo op oude runs: 0 tot 2,6). **Muisvlak en doorzichtig venster zijn niet de reden dat de graver op Windows zuiniger is.** Beide richtingen zijn bovendien "uit is duurder", dus als er iets is, is het klein en de andere kant op.

**Welke maat (vraag Iris 23:45):** de ruisproef is al gedaan (23:20 hierboven): dezelfde .exe drie keer na elkaar 0,86 / 0,71 / 0,77. Dus:
- **tussen twee versies:** CPU per getekend beeld binnen één run (een `wissel`), meetlat 3 ms (±20%);
- **voor de grens van 1,0 in de workflow:** één run die alleen draait (geen andere duurtest tegelijk), zoals Sanne besliste. Gestart 17 nov 00:12 UTC: run 43985774466 op `claude/steam-hol-regels-weg` (c1fa66a), gewoon spel, `zaad=1794860558`, 20 min, 1920x1080, editor-Godot zoals 43970539451. Uitslag hieronder.
- De Windows-kost per beeld zit dan in het tekenen zelf. Volgende proef alleen als Olaf of Iris hem wil: `--rendering-driver` d3d12 tegen opengl3, elk één run alleen. De wissel-proeftak gaat niet naar main.

**Uitslag losse run (00:45 UTC):** run 43985774466, alleen gedraaid: **1,321 CPU-s per 10 s** (mediaan 1,484, hoogste 2,547), 52 MB, geen scriptfout. `cpu_per_beeld.py`: tak 18,4 ms per beeld, main op hetzelfde zaad (43953076960) 11,9 ms; ruis van dezelfde .exe 13,0 tot 17,2. Beide runs tekenen evenveel beelden (72 en 71 per 10 s), dus de tak kost per beeld meer. Ook zonder held in beeld (1,48 tegen 0,94). Volgens Sannes regel 3: niet naar main voor de speeltest; volgende stap voorgesteld aan Olaf: `wissel=deco` op een proeftak.

## Wissel deco (Bram, 17 nov ±01:30 UTC, vraag Iris keuring 12, Sannes poort 2)
- Tak `claude/steam-hol-wissel-deco` (e1de54a): Olafs `claude/steam-hol-regels-weg` (ee19bd6) plus `wissel=` uit de oude proeftak. Nieuw: `wissel=deco` zet in oneven minuten `hol_vast.gd` `ZONDER_DECO` aan (alle versiering in gang en kamers weg, het vaste beeld tekent één keer opnieuw) en in even minuten uit. Logregel `HOL wissel deco uit/aan t=...`, dus `cpu_wissel.py <map>` werkt zonder wijziging ("uit" = zonder deco).
- Lokaal Godot 4.3 Linux: toets_systemen, toets_held, toets_vleermuis 0 FOUT; 140 s onder Xvfb met `wissel=deco log=...`: wissels op 60,0 en 120,0, `hol_vast` telt bij elke wissel precies één keer op.
- Vooraf (GOK): de deco staat in het vaste beeld, en dat tekende op de tak niet vaker opnieuw dan op main (zaad 1794860558, 20 min: 39 tegen 43 keer, GEZIEN in `hol.log` van `claude-steam-hol-regels-weg-zaad-1794860558-1920x1080` en `main-zaad-1794860558-1920x1080`). Dan kost de deco per beeld bijna niets en zit het verschil 18,4 tegen 11,9 ms ergens anders. De run beslist.
- Runs: om 01:23 gestart en om 01:24 gestopt (Olafs losse run 43994541342 liep al en moet alleen draaien). Opnieuw gestart om 01:42 (Olafs run klaar): **43997582851** (editor) en **43997586979** (.exe), beide 20 min, 1920x1080, `extra` = `zaad=1794860558 wissel=deco`. Map op `schermen`: `steam-hol-duur/claude-steam-hol-wissel-deco-zaad-1794860558-wissel-deco-1920x1080(-exe)/`.

## Wissel deco: uitslag, de deco is het niet (Bram, 17 nov ±02:20 UTC)
Beide runs groen gedraaid tot het eind (20 min, 1920x1080, zaad 1794860558, 20 wissels in elke `hol.log`, GEZIEN op tak `schermen`). De editor-run 43997582851 staat op rood alleen door de CPU-grens van 1,0 in de workflow (1,293; `fout.txt` heeft alleen de geluidskaartmelding van de runner). De twee runs liepen tegelijk; voor de vergelijking binnen één run maakt dat niet uit, voor de grens telt zo'n run niet (Sanne).

`python3 cpu_wissel.py <map>` ("aan" = met deco, even minuten; "uit" = zonder deco, oneven minuten; het script noemt het nog "vlak"):

| run | met deco | zonder deco | verschil per beeld |
|---|---|---|---|
| editor (43997582851) | 17,9 ms (1,248 CPU-s per 10 s) | 19,0 ms (1,239) | 1,1 ms, zonder deco duurder |
| .exe (43997586979) | 11,7 ms (0,982) | 12,1 ms (0,803) | 0,4 ms, zonder deco duurder |

Onder de meetlat van ±3 ms per beeld (placebo 0 tot 2,6). **De losse dingen in gang en kamers kosten per beeld niets meetbaars.** Mijn GOK vooraf klopte: het vaste beeld tekent maar ±0,3 tot 0,5 keer per 10 s opnieuw.

Ter vergelijking `cpu_per_beeld.py`, zelfde zaad, editor tenzij anders:

| run | wat | CPU gem. | ms per beeld |
|---|---|---|---|
| 43953076960 | main e6d7b70 | 0,844 | 11,9 |
| 43994541342 | Olafs `claude/steam-hol-regels` 4a7af62, zonder deco, alleen gedraaid | 1,013 | 14,8 |
| 43985774466 | `claude/steam-hol-regels-weg` c1fa66a, met deco, alleen gedraaid | 1,321 | 18,4 |
| 43997582851 | wissel-deco e1de54a, editor | 1,293 | 18,8 |
| 43997586979 | wissel-deco e1de54a, .exe | 0,862 | 12,1 |

Lezing: tussen editor-runs van bijna dezelfde code zit 14,8 tot 18,8 ms, terwijl de deco binnen één run 0 tot 1 ms scheelt. Het verschil tussen Olafs twee takken is dus runner, niet deco. Dezelfde tak als .exe zit op 12,1 ms, gelijk aan main in de editor. Ik vind in deze runs geen plek waar de tak echt duurder is; wat overblijft valt binnen de ruis van ±30% per run. Deco mag van mij met de spelregels mee; de grens van 1,0 voor de gewone duurtest beslissen Olaf en Sanne. De proeftak `claude/steam-hol-wissel-deco` gaat niet naar main.

**Aanvulling 02:35 UTC: hoe vast is de grens van 1,0 voor main zelf?** Alle main-runs in de editor op 1920x1080 met het gewone spel (uitslag.txt op `schermen`, GEZIEN): a90df14 1,233 (43948989836, liep met twee andere tegelijk), e6d7b70 0,844 (43953076960). Main zelf ging dus al eens over 1,0, al telt die run niet omdat hij niet alleen liep. Eerlijk: Olafs tak zonder deco alleen (1,013) tegen main alleen (0,844) is +20% CPU en +24% per beeld (14,8 tegen 11,9), precies op Sannes rand, en dat is één run tegen één run. Wie het zeker wil weten: main en `claude/steam-hol-regels` op zaad 1794860558 **na elkaar**, elk alleen, en dan per beeld vergelijken. Ik start die niet zelf, zodat ik niet door Olafs losse runs heen draai.

## Herhaling op de speeltesttak (Olaf, 17 nov 02:50 UTC)
| run | wat | CPU gem. | ms per beeld | zonder held / met held |
|---|---|---|---|---|
| 44001895099 | `claude/steam-hol-regels` 959aef4 (spelregels plus kaartje, zonder deco), alleen | 1,325 | 19,0 | 1,40 / 1,27 |
| 43953076960 | main e6d7b70 (ter vergelijking) | 0,844 | 11,9 | 0,94 / 0,78 |
| 44005445378 | main c38f267, alleen, direct erna | loopt | | |


## Stil spel: wat kost het als er niemand is (Bram, 17 nov ±03:30 UTC, vraag Sanne 03:15)
Nieuw script `cpu_stil.py <map>`: splitst de CPU per 10 s in drie soorten: **stil** (geen held en het vaste beeld tekende niet opnieuw), geen held maar wel een nieuw vast beeld, en held in beeld. Zelfde uitlijning als `cpu_per_beeld.py`.

Op het editor-paar van Olaf (GEZIEN, `hol.log` en `cpu-per-10s.txt` van `schermen`):

| run | stil: cpu / beelden per 10 s / ms per beeld | geen held, vast nieuw | held in beeld |
|---|---|---|---|
| tak 959aef4 (44001895099) | 0,95 / 24 / 39,0 (n=31) | 2,21 / 89 / 24,8 (n=17) | 1,27 / 85 / 14,9 (n=70) |
| main c38f267 (44005445378) | 0,45 / 34 / 13,1 (n=33) | 1,31 / 95 / 13,8 (n=16) | 1,66 / 80 / 20,7 (n=69) |

Lezing (GOK tot de .exe-runs): in de tak kost stil spel twee keer zoveel CPU met minder beelden; met held is het andersom. In de code van de tak tegen main (`git diff`, 10 bestanden) vind ik niets dat elk beeld draait als er niemand is: `plat_wissel` draait alleen als Gloop van stand wisselt, `een_per_held` alleen als er een regel bij komt, het kaartje tekent `vast` alleen bij hover. Tegelijk lagen bij main dezelfde soort runs eerder op 0,94 zonder held. Het kan dus runner zijn. De .exe-runs op hetzelfde zaad beslissen: tak 44008361789, daarna main c38f267 (tak `claude/steam-hol-main-c38f267`, alleen om dat punt vast te houden).

## .exe van de speeltesttak (Bram, 17 nov ±03:40 UTC, Sanne poort b)
Run **44008361789**: `claude/steam-hol-regels` 959aef4, exe=ja, zaad 1794860558, 20 min, 1920x1080, alleen gedraaid. Rood op de grens. Map `steam-hol-duur/claude-steam-hol-regels-zaad-1794860558-1920x1080-exe/` op `schermen` (GEZIEN): 118 metingen, proces leefde, 52 MB, `fout.txt` alleen de geluidskaart, eerste koop na 155 s, 105 kroniekregels waarvan 102 verschillend.

| | cpu | ms per beeld | stil (geen held, vast gelijk) | geen held, vast nieuw | held in beeld |
|---|---|---|---|---|---|
| tak .exe 44008361789 | **1,334** | 18,6 | 0,47 / 29 beelden / 16,3 ms | 1,35 / 103 / 13,1 | 1,68 / 83 / 20,1 |
| tak editor 44001895099 | 1,325 | 19,0 | 0,95 / 24 / 39,0 | 2,21 / 89 / 24,8 | 1,27 / 85 / 14,9 |
| main editor 44005445378 | 1,276 | 18,4 | 0,45 / 34 / 13,1 | 1,31 / 95 / 13,8 | 1,66 / 80 / 20,7 |

Lezing:
1. **Sannes vraag (stil spel):** in de .exe kost de tak als er niemand is 0,47, `cpu bij helden=0` 0,73, gelijk aan main (0,45 en 0,73). Het patroon "zonder held duurder" van de editor-run komt niet terug. Er draait niets extra als er niemand is.
2. **Poort (b), .exe onder 1,0:** nu niet gehaald (1,334). Maar dezelfde soort .exe gaf voor middernacht 12,1 ms per beeld (43997586979) en main als .exe 0,71 tot 0,86; nu 18,6. Alle runs sinds ±02:00, editor en .exe, tak en main, zitten op 18,4 tot 19,0 ms per beeld. GOK: de runners zijn trager geworden.
3. Toets: main c38f267 als .exe, zelfde zaad, alleen, direct erna (gestart 03:35, tak `claude/steam-hol-main-c38f267`). Main ook ±1,3: runner, en (b) zegt op deze runners niets; voorstel (b) als paar meten (.exe tak tegen .exe main, hooguit 20% per beeld) en de 1,0 op Thijs' pc laten beslissen. Main ±0,85: de tak is echt duurder, verder zoeken.
