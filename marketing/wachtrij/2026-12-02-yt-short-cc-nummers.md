# Click Cuts Short 3: Which printed part goes where? Number every cut 🔥

- status: open (plaatsen pas als Click Cuts live is en de winkellink werkt)
- bijgewerkt: Regisseur run 25 (24 nov 2026): eerlijkheidszin vervangen door "Every printer is different" (besluit Thijs 24 nov 15:32) en printzin "Every printer is different: print the fit test first." (slot blijft Click Cuts, want de opdracht gaat over Click Joints Pro). Alleen opnieuw gemonteerd uit dezelfde ruwe opname (workflow regisseur-21).
- nagekeken run 25 (GEZIEN, release regisseur-21, run 45430299493): lengte 45,2 s, geluid GOED (-16,7 dB), synchroon GOED 11 van 11 (0,18 s). Eerlijkheidszin en slotzin staan in beeld en stem.
- kanaal: youtube-short
- soort: video
- soort_reeks: lancering Click Cuts, script 3 van 6 (`commercie/filmpjes/scripts/click-cuts-lancering.md`, ja Daan na M1 en M2), hook 3A. Volgorde 1, 2, 3, 6, 4, 5: deze als derde.
- product: click-cuts
- bestand: https://github.com/thijsduinhouwer2002-coder/dortus-hq/releases/download/regisseur-21/cc-nummers-geluid.mp4
- stem_tekst: `commercie/filmpjes/regisseur-21/cc-nummers-stem.txt` (voor Max van de hoofdchat; tot die er is Kokoro)
- releasebestand (GEZIEN, workflow-run 45381874989): 45,4 s, 1080 x 1920; geluid_check GOED (-16,7 dB, piek -1,4 dB); synchroon GOED 11 van 11 (grootste 0,203 s, gemiddeld 0,134 s). 13 beelden bekeken, eerste groot: hoop losse grijze stukken op tafel, kop "Which goes where?", geen zwevende getallen. Gravures leesbaar dankzij Cavity: "12-11" en "11-12" groot in beeld, "7-11" op het kleine stuk. Eerste opname (run 45379029457) niet aangeleverd: nummers recht van voren onzichtbaar. Kan beter: bij "Not on a hole" is het nummer klein en vallen de gaten deels buiten de uitsnede; bij "Bottom to top" staan de namen deels achter de stukken.
- metingen (film-tip.json, GEZIEN): Lion Head 320,5 x 206,4 x 436 mm, buiten beeld gesplitst op de A1 mini: 12 stukken alle groen, 41 labels, tekst 8 en 2,5 mm hoog, Engrave numbers aan, Number depth 0.6 mm. Paar 12-11 (stuk 12) en 11-12 (stuk 11); vlak met 4 gaten: 12-10; kleinste: 7-11 (2,5 mm). Objectnamen Piece 01 tot Piece 12 van onder naar boven; klik Export parts (echt, OCR): piece_01.stl tot piece_12.stl plus pennen. Klik More settings (echt) en scrollen naar Engrave numbers. Geen vangnet.
- tijd: voorstel twee dagen na de lancering van Click Cuts (week van 30 nov, de hoofdchat kiest)
- doel: de winkellink van Click Cuts (eerste regel van de beschrijving, invullen na de uitgave)
- gemaakt_door: Regisseur run 20 (24 nov 2026); opname in workflow regisseur-21 (Blender 5.3.0, xvfb, echte muis, gedeelde hulpcode van Olaf)
- vorige: 2026-12-01-yt-short-cc-pas.md

## Titel
Which printed part goes where? Number every cut 🔥 | Blender

## Tekst
```
<winkellink Click Cuts, invullen na de uitgave>

Twelve printed parts and no idea where they go? Number every cut.
1. Split to fit engraves a number into every cut face, 0.6 mm deep by default.
2. Each face shows its own part and the part it joins, so 12-11 meets 11-12.
3. The number sits inside the cut, away from the pin holes. The outside stays clean.
4. Parts are numbered from bottom to top, and the files follow the same order.

Every printer is different. Print the fit test first, then the parts.

#blender #3dprinting #b3d #blendertips #shorts
```

## Eerste reactie
(leeg)

## Bronnen
- **Script en regels:** `commercie/filmpjes/scripts/click-cuts-lancering.md` nr. 3 (geen prijs, geen print-belofte, geen klik of magneten, printzin variant 2). Daan keurde de scripts.
- **"Twelve":** alleen omdat de opname echt 12 stukken geeft (de opname stopt met een fout als het er geen 12 zijn).
- **Nummer in elk snijvlak, eigen-buur:** `producten/blender-splitser/split_joints/verbind_3d.py` (tekst_p "a-b" op stuk a, tekst_q "b-a" op stuk b), `splitsen.py` (`sj_labels` per stuk). In beeld: de echte gegraveerde nummers, camera loodrecht op het vlak in hetzelfde assenstelsel als `vormen.label_frame`, andere stukken alleen in de weergave verborgen.
- **Verdiept, buitenkant schoon:** `vormen.py` `label_mesh` (plaat van 0,2 mm buiten tot de diepte binnen het snijvlak), `eigenschappen.py` `label_diepte_mm` standaard 0.6, "Engrave numbers" en "Number depth (mm)" (zo staat het in het paneel van main, GEZIEN in de opname).
- **Niet op een gat:** `verbinders.py` `kies_label` (punt met de meeste ruimte buiten de gaten, r_gat + 0,8 mm).
- **Kleinere vlakken, kleinere nummers (zin erbij, graag meekeuren):** `verbinders.py` `LABEL_HOOGTES = (8.0, 6.0, 5.0, 4.0, 3.0, 2.5)`, de grootste die past, anders langs het vlak; past er niets, dan een melding "no room for the number".
- **Diepte in More settings, stap 3 (zin erbij):** `paneel.py` stap 3 "Pins and numbers" onder More settings; `eigenschappen.py` default 0.6.
- **Van onder naar boven:** `splitsen.py` (nummers op z, dan y, dan x). In beeld de echte objectnamen Piece 01 tot Piece 12 in Exploded view.
- **Bestandsnamen (zin erbij):** `exporteer.py` r. 30 `piece_{nr:02d}`; in de opname gemeten (film-tip.json `bestanden`).
- **Model:** Lion Head, Poly Haven, CC0 (DERDEN: https://polyhaven.com/a/lion_head), buiten beeld gesplitst op de A1 mini.
- **Stem:** tijdelijk Kokoro-82M, af_heart, Apache 2.0 (DERDEN: https://huggingface.co/hexgrad/Kokoro-82M). ElevenLabs-opname (Max) gevraagd: `cc-nummers-elevenlabs.mp3` in `commercie/filmpjes/regisseur-21/`.
- **Nieuw onderwerp:** geen Short over nummers op onderdelen in de laatste 14 dagen (wachtrij en RSS nagekeken 24 nov ±11:55 NL, GEZIEN). cc-fit (splitsen) en cc-pas (fit test) zijn andere lessen.

## Keuring
- keurder: Iris, 24 nov 2026 ±12:00 UTC (op vraag Regisseur), `marketing/keuring/2026-11-24-yt-short-cc-fit-pas-nummers-iris.md`
- beeld en plezier: akkoord ja; beste van de drie; Moet geen
- kan: bij zin 9 de bestandsnamen echt in beeld (nu alleen in de kop); namen bij "Bottom to top" niet achter de stukken.
- plaatsen pas als Click Cuts live is.

## Oranje-besluit
(alleen de hoofdchat, alleen bij oranje)

## Na plaatsen
(alleen de Maker)
