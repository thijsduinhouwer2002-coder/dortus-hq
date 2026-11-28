# Keuring Iris: nieuwste speelversie voor Thijs (#356, #336), run 46109605955, commit 3ccb86f

Bron, zo dicht mogelijk bij Thijs:
- Artifact `speeltest-hats-of-the-fallen-windows` van run 46109605955: bovenste groene run van "steam-hol-exe" op main. Na 3ccb86f is er geen commit meer aan `producten/steam-hol/godot` of `speeltest` (GEZIEN, git log tot f81418a). Zip 34,2 MB met HetHol.exe, LEES-MIJ-EERST.txt en VERSIE.txt ("Gebouwd uit commit 3ccb86f..., run 46109605955") (GEZIEN).
- Gespeeld: precies deze HetHol.exe (`--main-pack HetHol.exe`) met Godot 4.3 Linux onder Xvfb, lege save in een eigen lege map, 5 beelden per s, `vers=1 zaad=13 uitleg_klik=6 koper=1 koper_wacht=8 balk=0`, net als bij 52507cc zodat de twee naast elkaar liggen.
  - 100%: `hoogte=200`, 600 s, venster 1920 x 200 (schaal 5). Log `thijsversie-3ccb86f-zaad13.log`.
  - 125%: `hoogte=240`, 150 s, venster 2304 x 240 (schaal 6). Log `thijsversie-3ccb86f-240-zaad13.log`.
- Windows zelf (SmartScreen, systeemvak) kan ik niet bedienen; de Windows-runner van deze run is groen.

## Uitslag
- **SCRIPT ERROR: 0** op 200 en 0 op 240 (GEZIEN, grep in beide logs).
- **Cijfers (GOK, mijn oordeel): leuk 8, aandacht 8, mooi 8.** Niets slechter dan 52507cc.

## Naast 52507cc (zelfde zaad, GEZIEN in log en film)
| | 52507cc (run 46097798308) | 3ccb86f (run 46109605955) |
|---|---|---|
| kopen in 10 min | 6 | 7 (76, 189, 296, 335, 416, 493, 535 s) |
| langste gat zonder koop | 154 s | 113 s (76 tot 189 s) |
| regels op het bord | 59 | 60 |
| goud op 600 s | 68 | 82 |
| toren op minuut 8 | troon met 5 hoeden | troon met 5 hoeden |

Het gat dat ik bij 52507cc als punt 1 voor een 9 noemde, is 41 s korter. Uitleg op 0, 9 en 15 s gelijk.

## Wat ik zag
- Palet vol: zelfde kleuren als 52507cc, beelden vrijwel gelijk naast elkaar (`thijsversie-3ccb86f-min2-10-ware-maat.png` tegen `thijsversie-52507cc-min2-10-ware-maat.png`).
- 240 px: bord, knoppen, tekst en uitlegpijl groeien mee en blijven scherp; geen afgesneden tekst (`thijsversie-3ccb86f-240px-ware-maat.png`).
- 2x: rand om de held nog dubbel en vlekkerig (`thijsversie-3ccb86f-2x.png`); op 1x valt het niet op.

## Wat ontbreekt voor een 9
1. Vaak maar één held tegelijk in beeld op minuut 2 tot 10; linker deel van het hol en de bovenste gang veranderen weinig.
2. Rand om de held op 2x.
3. Tweede koop pas op 189 s; rond 150 s zou het ritme gelijk lopen met de rest (40 tot 107 s).

## LEES-MIJ-EERST.txt
Height klopt nu: "Height (96, 120, 160, 200 of 240 px; start op 200)" (GEZIEN in de zip), gelijk aan het menu.
