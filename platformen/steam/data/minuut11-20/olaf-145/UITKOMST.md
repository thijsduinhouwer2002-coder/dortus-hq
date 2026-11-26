# Meting #145: langste stuk zonder koop in minuut 11 tot 20 (Olaf, 26 nov 2026)

Opzet (GEZIEN): Godot 4.3 Linux, headless, `--fixed-fps 5`, args `hoogte=120 vers=1 zaad=Z uitleg_klik=6 koper=1 koper_wacht=8 balk=0 duur=1200` (zelfde als Iris en #134, alleen 1200 s in plaats van 900). Hetzelfde zaad geeft niet steeds dezelfde run, dus elk zaad 8 keer. Script `run.sh`, meten met `meet.py <map> -v`. Per run: `voor-per-run.txt`, `na-per-run.txt`; de logs van run 1 per zaad in `logs-na-r1/`.

## Voor (main 5faa494, spel gelijk aan 4af7dae; zaad 2 tot 7, 8 runs = 48)
- Langste stuk zonder koop, minuut 11 tot 20: max 540 s, mediaan 517 s, onder 180 s in 0 van 48.
- Altijd precies 6 kopen; koop 6 mediaan 683 s, daarna niets meer.

## Na (zaad 2 tot 9, 8 runs = 64)
- Langste stuk zonder koop, minuut 11 tot 20: **max 195 s, mediaan 142 s, onder 180 s in 62 van 64** (97 procent).
- De twee runs boven 180: zaad 3 run 4 (189 s) en zaad 9 run 7 (195 s), beide een reeks vluchten.
- Eerste run per zaad (zoals Iris filmt): 175, 120, 167, 137, 165, 140, 171, 168 s.
- 8 tot 12 kopen per run tot 1200 s.
- Eerdere ronde met dezelfde getallen: zaad 2 tot 7 47 van 48 (max 181), zaad 2 tot 9 62 van 64 (max 229).

## Minuut 0 tot 11 gelijk
Niets verandert voor een soort op stap 3 staat: stap 1 tot 3 en hun prijzen (45, 60, 70) zijn gelijk, het extra goud komt pas vanaf stap 4. Gemeten (zaad 2 tot 7, 48 runs elk), koop 1 tot 5 gemiddeld: voor 75, 259, 368, 460, 562 s; na 75, 258, 370, 462, 569 s. Langste gat in 0 tot 660 s: voor mediaan 181 max 237, na 188 en 217 (ruis, de runs zijn niet vast).

## Wat veranderde (`producten/steam-hol/godot/systemen/upgrades.gd`)
1. Per soort stap 4, 5 en 6 (Gloop: Sticky Gloop, Greedy Gloop, Gloop Prime; put: Sharp Spikes, Endless Pit, Doom Pit). Prijs 75, 95, 115; de put 10 meer (85, 105, 125), zodat Gloop en de put om en om klaar zijn.
2. Elke stap 4 tot 6: +2 goud per vangst (`goud_erbij()`, opgeteld in `kern/afloop.gd`). Sticky Gloop ligt ook maar 15 s plat (was 20). Geen extra kans.
3. Geen nieuwe kunst: `beeld_niveau()` geeft hooguit 3, dus Gloop en de put houden het beeld van stap 3. Het koopmoment (wip, schudden, kroniekregel met grap, kaartje "Bought.", Undo) is hetzelfde.
4. Tekst klopte niet: Bouncy Gloop zei "Back up in 40 s instead of 60", maar plat duurt 30 s en met Bouncy 20 s. Nu "20 s instead of 30".

## Geprobeerd en niet gekozen (elk 48 runs, zaad 2 tot 7)
- Stap 4 en 5 met +7 kans, 80 en 95: 38 van 48, en nog maar 6 procent ontsnapt.
- Stap 4 en 5 met goud, 75/90, 90/120, 80/115, 75/110: 36 tot 40 van 48. Vier dingen erbij is te weinig: wie vroeg klaar is heeft rond 950 tot 1000 s weer een lege winkel, wie laat is heeft na koop 6 een te dure stap.
- Stap 4 tot 6 met gelijke prijs voor beide soorten (80, 100, 125): 45 van 48; twee kopen vlak na elkaar en dan een gat.

## Let op (voor Sanne)
Na minuut 4 ontsnapt nu 7 procent van de helden (was 22 procent in de oude meting tot 1200 s). Dat komt niet door meer kans maar door de regel uit #134: zolang er iets te koop is en je 60 s niets kocht, valt na 30 s zonder vangst de volgende held zeker. Vroeger ging die regel na de zesde koop uit omdat er niets meer te koop was. Wil je meer wrok, dan is die regel de knop.
