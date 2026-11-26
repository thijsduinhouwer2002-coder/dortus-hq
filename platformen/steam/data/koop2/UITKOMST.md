# Meting: van koop 1 naar koop 2 (Sanne, 26 nov 2026)

Aanleiding: Iris, keuring build 499fd9f punt 3 (`producten/steam-hol/keuring-iris/2026-11-26-build-499fd9f.md`): van koop 1 naar koop 2 nog 175 tot 197 s bij 4 van de 6 zaden. Dat is minuut 1 tot 5, precies wat Thijs als eerste ziet als hij opnieuw speelt (#19 punt d).

Opzet (GEZIEN): Godot 4.3 Linux, headless, `--fixed-fps 5`, args `hoogte=120 vers=1 zaad=Z uitleg_klik=6 koper=1 koper_wacht=8 balk=0 duur=1200` (zelfde als Iris, #134 en #145). Zaad 2 tot 9, elk 3 runs, twee rondes van 24 runs per variant. Script `meet.sh`, tellen met `tel.py <map>`. Ruwe uitkomst `uitkomst-ruw.txt`, koop 1 tot 3 per run in `koop1-3-per-run.txt`.

## Gekozen: stap 1 kost 40 (was 45)
| | voor (45), 48 runs | na (40), 48 runs |
|---|---|---|
| koop 1 | 73 tot 79 s (mediaan 75) | 73 tot 79 s (mediaan 75), gelijk |
| koop 2, mediaan | 257 en 260 s | **219 en 224 s** |
| gat koop 1 tot 2, mediaan | 183 en 186 s | **143 en 147 s** |
| gat koop 1 tot 2 boven 170 s | 41 van 48 | **17 van 48** |
| koop 3, mediaan | 369 en 364 s | 334 s |
| langste gat minuut 11 tot 20, mediaan | 152 en 138 s | 143 en 145 s, gelijk |
| ontsnapt na minuut 4 | 6 tot 8 procent | 9 procent |

De max van het gat koop 1 tot 2 blijft ±210 s (pech: een reeks vluchten). Dat vangt de droogteregel al op; verder omlaag zou het begin weggeven.

## Geprobeerd en niet gekozen
- Stap 1 op 35: koop 1 schuift naar 22 s, dus vóór de eerste les ("Click the dirt to dig"). Weg.
- Koopgeluk ook bij een held die vanzelf valt (dubbel goud meteen na de koop in plaats van alleen als redding): koop 2 juist later (mediaan 270 s, gat 195 s) en 17 procent ontsnapt. De redding is meer waard dan het dubbele goud. Teruggedraaid.

## Demo
De demo-film (`demo=1`) houdt 45 voor stap 1 (`DEMO_EERSTE` in `systemen/upgrades.gd`, vlag gezet in `kern/strook.gd`). Let op: de demo-log van 60 s is headless na ±42 s ook vóór deze wijziging niet elke run gelijk (3 runs voor en 3 na: dezelfde twee varianten van de log kwamen in beide voor, md5 204e52b7 en d1f82c68; GEZIEN). Tot 42 s gelijk, koop op 20,2 s met goud 27 gelijk.

## Toetsen
8 toetsen 0 FOUT op Linux (toets_systemen met drie nieuwe regels: stap 1 kost 40, demo houdt 45, strook zet de vlag).
