# Bewijs Hol 2.0 proef (Olaf, 28 nov, issue #388)

Tak `hol2-proef`; main is niet veranderd. Ontwerp: `../ontwerp-hol2/LEESMIJ.md` (Sanne). Code: `godot/hol2/`, uitleg in `../architectuur.md` onderaan.

## (a) CPU: Hol 2.0 op 120 kost minder dan het hol van nu op 96

Binnen één meetronde, om en om, met een placebo (twee keer precies hetzelfde hol van nu, A tegen A'). Linux, Xvfb 1920 x 1080, software-tekenen, Godot 4.3, gewoon spel (geen film), beide op 12 beelden per s, 3 rondes van 30 s na 15 s opwarmen. Script `meet_cpu.py`, ruwe getallen `cpu.json` (GEZIEN):

| stand | CPU-s per 10 s (3 rondes) | gemiddeld |
|---|---|---|
| hol van nu, 96 px | 1,153 / 1,160 / 1,033 | 1,115 |
| placebo: hol van nu, 96 px, nog eens | 1,080 / 1,083 / 1,183 | 1,115 (verschil 0,0 procent) |
| **Hol 2.0, 120 px** | 0,890 / 0,907 / 0,907 | **0,901 (19 procent minder)** |

Eis uit het issue (niet meer dan nu): gehaald, met 4 keer zoveel hol in beeld. Eerste poging kostte 65 procent meer (1,81, GEZIEN, eerste ronde van een eerdere meting): de achtergrond waren duizenden losse tegels die elk beeld opnieuw naar de kaart gingen. Nu wordt die één keer gebakken in een eigen beeld (`SubViewport`, `UPDATE_ONCE`) en als één plaatje getekend; op schaal 1 slaan we ook de extra kopie van de rekstand over. Windows, echte .exe, run 46145708250 (alleen ter info, `steam-hol2-proef/cpu.txt` op tak schermen, GEZIEN): hol van nu 96 gemiddeld 1,47, placebo 2,05, Hol 2.0 op 120 gemiddeld 1,14 CPU-s per 10 s. De placebo zit daar 39 procent naast het origineel, dus de gedeelde runner is te onrustig om er een procent uit te halen; de richting is wel dezelfde. De Linux-meting hierboven is de maat.

## (b) Film van 2 minuten

Op tak schermen, map `steam-hol2-film/` (commit 8e54faf): `hol2-film-2min-1x.mp4` (hele strook, ware maat), `...-links-2x.mp4` en `...-rechts-2x.mp4` (helft, 2 keer). Godot 4.3 onder Xvfb, `--write-movie --fixed-fps 12`, `hoogte=120 film=1 zaad=7`. Wat erin gebeurt (log, GEZIEN):
- 5 s klik op verdieping 2 links: Gloop loopt van de troon weg; 22 s klik op verdieping 1: hij loopt naar de ladder en klimt (36,9 s op verdieping 1); 45 s klik in de tuin: klimt naar boven (55,6 s in de tuin).
- 70 s besturen-stand aan (gouden rand), D en A lopen, 79 s Esc.
- **72,7 s: Bert valt in een luik op verdieping 2**; daarna nog 4 keer op verdieping 2 en 3 keer op verdieping 1.
- 82 s klik op verdieping 3, 84 s muiswiel omlaag: het beeld schuift 48 px naar verdieping 3, na 10 s zonder muis zacht terug.

Beelden hier: `hol2-120-1x-25s.png` (ware maat), `hol2-120-geschoven-85s.png` (geschoven naar verdieping 3), `hol2-240-1x-60s.png` (op 240 px: tuin en 5 verdiepingen, figuren niet groter), `val-verdieping2-2x.png` (drie beelden van de val op verdieping 2, 2 keer). De lucht is zwart in de filmbeelden: de filmmaker kent geen doorzichtigheid; in het spel is hij doorzichtig.

## (c) Toetsen

`systemen/toetsen/toets_hol2.gd`: indeling (ladders, geen val op een ladder, maten 22, 70, 118), klikken om te lopen naar tuin, 1, 2 en 3 (aankomst op de juiste plek), 15 min scharrelen (nooit langer dan 2 s stil zonder gedraging, 13 soorten gedrag uit de tabel), helden vallen op verdieping 1 en 2 en niemand blijft hangen, W/S klimt alleen bij een ladder. Lokaal 0 FOUT (GEZIEN). De workflow draait deze plus de 11 van main op Windows.

## (d) .exe

Artifact `hol2-proef-windows` (33 MB) van run 46145708250 op commit eef8866, 14 dagen: https://github.com/thijsduinhouwer2002-coder/dortus-hq/actions/runs/46145708250/artifacts/15263283507 (ophalen met een GitHub-account), met `LEES-MIJ-EERST.txt`. In die run: alle 12 toetsen groen op Windows, de .exe start op 120 en 240 px boven de taakbalk met Kladblok erachter, geen SCRIPT ERROR, Gloop loopt na de klik (`starten.txt`, `hol2-240.png` op tak schermen, GEZIEN). Link staat in het issue en onderaan `berichten/hoofdchat.md` en `berichten/sanne.md`.

## Wat er (nog) niet in zit, eerlijk

- Kunst is de oude, verkleind (Gloop 20, helden 16, nearest, klein palet) plus eenvoudige tegels van mij. De figuren lezen op 1x nog vlekkerig; de kleine figuren van Mila wissel ik in zodra ze er zijn (`hol2/maak_kunst.py`).
- Geen kopen, eerste minuut, menu, systeemvak of app-balk. Stoppen met rechtsklik. De proef bewaart niets.
- Gewicht en duur in de tabel zijn de GOK van het ontwerpblad; zonnen, spugen en ploppen kwamen in de toets van 15 min niet voor (kleine gewichten).
- Op Windows met de app-balk uit valt een gemaximaliseerd venster achter de strook; voor een proef om te voelen laat ik dat zo.

## (e) Daan #394 moet 1 tot 3 (Olaf, 28 nov, issue #401)

- **Moet 1, maat:** `hoogte` is nu spelpixels; het venster is `hoogte x schaal`. Onder Xvfb op 3840 x 2160: `schaal=2 spelpixels=1920x120 venster=(3840, 240)`, op 1920 x 1080: `schaal=1 spelpixels=1920x120 venster=(1920, 120)` (GEZIEN, log). Vroeger op 4K: 60 spelpx, alleen de tuin en verdieping 1. Toets: schaal 1, 2 en 3 geven 120 spelpx en 3 lagen in beeld; een te grote schaal op een klein scherm gaat omlaag.
- **Moet 2, focus terug:** hulpje `godot/hol2/focus.exe` uit `focus.c` (42 kB, sha256 `ee1c86119da401b979915f1ec3573a08b44dfd3788bc321f9c69c2bd4cf16594`, mingw 13.2.0-6ubuntu1+26.1 met dezelfde vlaggen als hol-balk). Het onthoudt bij besturen aan welk venster vooraan stond en zet dat bij Esc en na 10 s stil weer vooraan; is dat venster weg, dan het bovenste gewone venster (zoals Alt+Tab).
- **Moet 3, bewijs op Windows:** stap "Besturen krijgt echte toetsen" in de workflow (`e2e/hol2_focus.ps1`): Kladblok vooraan, echte klik op Gloop, echte D 1,2 s, Esc, dan een echte q. Uitslag in `focus.txt` op tak schermen (`steam-hol2-proef/`).
- **Moet 4** blijft: bij samenvoegen `run/main_scene` terug naar `res://main.tscn`.
- **Sanne #401 punt 5, stuurknop:** vierkant van 9 spelpx met vier pijltjes links van het bord (`stuurknop-4x.png`); een klik zet de besturen-stand aan of uit, een klik op Gloop niet meer (die is voor zijn kaartje in het echte spel). De Windows-stap klikt eerst op Gloop (stand moet uit blijven), dan op de knop. Punt 6 (stilstaan bij de muis) en de Height-maat 120, 168, 216 komen hierna.
- Uitslag run 46156590473 (vóór de stuurknop, GEZIEN): D liet Gloop 42 spelpx lopen, na Esc stond een getypte q in Kladblok, na 10 s stil Kladblok weer vooraan.
