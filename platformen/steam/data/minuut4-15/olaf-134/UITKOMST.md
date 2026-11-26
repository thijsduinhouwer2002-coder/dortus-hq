# Meting #134: langste stuk zonder koop in minuut 4 tot 12 (Olaf, 26 nov 2026)

Opzet (GEZIEN): Godot 4.3 Linux, headless, `--fixed-fps 5`, args `hoogte=120 vers=1 zaad=Z uitleg_klik=6 koper=1 koper_wacht=8 balk=0 duur=900`. Hetzelfde zaad geeft niet steeds dezelfde run (Daan #109 K2), dus elk zaad meerdere keren. Script: `run.sh`, meten met `meet2.py` en `meet3.py`.

## Voor (main 883ea9d, zaad 2 tot 7, 3 runs per zaad = 18 runs)
- Langste gat zonder koop, minuut 4 tot 12: max 286 s, mediaan 212 s, onder 180 s in 4 van 18 runs.
- Minuut 4 tot 15: max 333 s, mediaan 245 s.
- Helden die na minuut 4 niet vallen: 25 procent.

## Na (zaad 2 tot 7, 8 runs per zaad = 48 runs)
- Langste gat zonder koop, minuut 4 tot 12: max 202 s, mediaan 134 s, onder 180 s in 43 van 48 runs (90 procent). Proefronde ervoor met dezelfde getallen: 36 van 36.
- Per zaad, hoogste van 8 runs: zaad 2 152 s, zaad 3 182, zaad 4 181, zaad 5 158 (was 272 bij Iris), zaad 6 202, zaad 7 187.
- De eerste run van elk zaad (zoals Iris filmt): 130, 117, 125, 131, 106, 128 s.
- Minuut 4 tot 15: max 352 s, mediaan 223 s. Na de zesde koop (mediaan 677 s) is er niets meer te koop; dat stuk zit in deze maat.
- Helden die na minuut 4 niet vallen: 17 procent (wrok blijft).
- Minuut 0 tot 4 gelijk: koop 1 mediaan 75 s voor en na, alles wat veranderde werkt pas vanaf 240 s open tijd, dus goud en kopen voor 240 s zijn gelijk. Koop 2 valt meestal net na 240 s en komt daardoor iets eerder (mediaan 254 s, was 299 s).

## Wat veranderde
1. `kern/afloop.gd`: vanaf 240 s open tijd (`speeltijd_s`) +4 goud per vangst (`GOUD_LAAT`).
2. `kern/ritme.gd`: vanaf 240 s, al 60 s geen koop en er is nog iets te koop, dan valt na 30 s zonder vangst de volgende held zeker (was alleen na 75 s). Wie net kocht ziet gewoon helden ontsnappen.
3. `systemen/upgrades.gd`: stap 2 en 3 kosten 60 en 70 (was 60 en 90).

## Geprobeerd en niet gekozen (elk 30 tot 36 runs)
- Droogte altijd 30 s na minuut 4: gat goed, maar maar 7 tot 9 procent van de helden ontsnapt nog. Weg met de wrok.
- Prijzen 55 en 60 met +4: gat met iets te koop 48 van 48 onder 180, maar de winkel is in de mediaan op 609 s leeg (daarna 5 min niets).
- Alleen goud of alleen prijzen: 27 tot 33 van 36, door reeksen vluchten.

## Wat overblijft (voor Sanne)
Er zijn maar 6 dingen te koop. Na de zesde (mediaan 677 s) is er niets meer te kiezen. Wie minuut 12 tot 15 een keuze wil, heeft een zevende stap of iets anders nodig; dat valt buiten #134 (geen nieuwe dingen).
