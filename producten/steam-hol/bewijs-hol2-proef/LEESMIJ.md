# Bewijs Hol 2.0 proef (Olaf, 28 nov, issue #388)

Tak `hol2-proef`; main is niet veranderd. Ontwerp: `../ontwerp-hol2/LEESMIJ.md` (Sanne). Code: `godot/hol2/`, uitleg in `../architectuur.md` onderaan.

## (a) CPU: Hol 2.0 op 120 kost minder dan het hol van nu op 96

Binnen één meetronde, om en om, met een placebo (twee keer precies hetzelfde hol van nu, A tegen A'). Linux, Xvfb 1920 x 1080, software-tekenen, Godot 4.3, gewoon spel (geen film), beide op 12 beelden per s, 3 rondes van 30 s na 15 s opwarmen. Script `meet_cpu.py`, ruwe getallen `cpu.json` (GEZIEN):

| stand | CPU-s per 10 s (3 rondes) | gemiddeld |
|---|---|---|
| hol van nu, 96 px | 1,153 / 1,160 / 1,033 | 1,115 |
| placebo: hol van nu, 96 px, nog eens | 1,080 / 1,083 / 1,183 | 1,115 (verschil 0,0 procent) |
| **Hol 2.0, 120 px** | 0,890 / 0,907 / 0,907 | **0,901 (19 procent minder)** |

Eis uit het issue (niet meer dan nu): gehaald, met 4 keer zoveel hol in beeld. Eerste poging kostte 65 procent meer (1,81, GEZIEN, eerste ronde van een eerdere meting): de achtergrond waren duizenden losse tegels die elk beeld opnieuw naar de kaart gingen. Nu wordt die één keer gebakken in een eigen beeld (`SubViewport`, `UPDATE_ONCE`) en als één plaatje getekend; op schaal 1 slaan we ook de extra kopie van de rekstand over. De workflow `steam-hol2-proef.yml` meet hetzelfde nog eens met de echte .exe op Windows (alleen ter info, `cpu.txt` op tak schermen).

## (b) Film van 2 minuten

Op tak schermen, map `steam-hol2-proef/film/`: `hol2-film-2min-1x.mp4` (hele strook, ware maat), `...-links-2x.mp4` en `...-rechts-2x.mp4` (helft, 2 keer). Godot 4.3 onder Xvfb, `--write-movie --fixed-fps 12`, `hoogte=120 film=1 zaad=7`. Wat erin gebeurt (log, GEZIEN):
- 5 s klik op verdieping 2 links: Gloop loopt van de troon weg; 22 s klik op verdieping 1: hij loopt naar de ladder en klimt (36,9 s op verdieping 1); 45 s klik in de tuin: klimt naar boven (55,6 s in de tuin).
- 70 s besturen-stand aan (gouden rand), D en A lopen, 79 s Esc.
- **72,7 s: Bert valt in een luik op verdieping 2**; daarna nog 4 keer op verdieping 2 en 3 keer op verdieping 1.
- 82 s klik op verdieping 3, 84 s muiswiel omlaag: het beeld schuift 48 px naar verdieping 3, na 10 s zonder muis zacht terug.

Beelden hier: `hol2-120-1x-25s.png` (ware maat), `hol2-120-geschoven-85s.png` (geschoven naar verdieping 3), `hol2-240-1x-60s.png` (op 240 px: tuin en 5 verdiepingen, figuren niet groter), `val-verdieping2-2x.png` (drie beelden van de val op verdieping 2, 2 keer). De lucht is zwart in de filmbeelden: de filmmaker kent geen doorzichtigheid; in het spel is hij doorzichtig.

## (c) Toetsen

`systemen/toetsen/toets_hol2.gd`: indeling (ladders, geen val op een ladder, maten 22, 70, 118), klikken om te lopen naar tuin, 1, 2 en 3 (aankomst op de juiste plek), 15 min scharrelen (nooit langer dan 2 s stil zonder gedraging, 13 soorten gedrag uit de tabel), helden vallen op verdieping 1 en 2 en niemand blijft hangen, W/S klimt alleen bij een ladder. Lokaal 0 FOUT (GEZIEN). De workflow draait deze plus de 11 van main op Windows.

## (d) .exe

Artifact `hol2-proef-windows` van de workflow `steam-hol2-proef.yml` op de tak (14 dagen), met `LEES-MIJ-EERST.txt`. Link staat in het issue en onderaan `berichten/hoofdchat.md` en `berichten/sanne.md`.

## Wat er (nog) niet in zit, eerlijk

- Kunst is de oude, verkleind (Gloop 20, helden 16, nearest, klein palet) plus eenvoudige tegels van mij. De figuren lezen op 1x nog vlekkerig; de kleine figuren van Mila wissel ik in zodra ze er zijn (`hol2/maak_kunst.py`).
- Geen kopen, eerste minuut, menu, systeemvak of app-balk. Stoppen met rechtsklik. De proef bewaart niets.
- Gewicht en duur in de tabel zijn de GOK van het ontwerpblad; zonnen, spugen en ploppen kwamen in de toets van 15 min niet voor (kleine gewichten).
- Op Windows met de app-balk uit valt een gemaximaliseerd venster achter de strook; voor een proef om te voelen laat ik dat zo.
