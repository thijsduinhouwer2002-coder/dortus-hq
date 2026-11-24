# Click Cuts Short 3: Which printed part goes where? Number every cut 🔥

- status: open (plaatsen pas als Click Cuts live is en de winkellink werkt)
- kanaal: youtube-short
- soort: video
- soort_reeks: lancering Click Cuts, script 3 van 6 (`commercie/filmpjes/scripts/click-cuts-lancering.md`, ja Daan na M1 en M2), hook 3A. Volgorde 1, 2, 3, 6, 4, 5: deze als derde.
- product: click-cuts
- bestand: https://github.com/thijsduinhouwer2002-coder/dortus-hq/releases/download/regisseur-21/cc-nummers-geluid.mp4
- stem_tekst: `commercie/filmpjes/regisseur-21/cc-nummers-stem.txt` (voor Max van de hoofdchat; tot die er is Kokoro)
- releasebestand: RELEASE_REGEL
- metingen: METING_REGEL
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
2. Each face shows its own part and the part it joins, so 2-3 meets 3-2.
3. The number sits inside the cut, away from the pin holes. The outside stays clean.
4. Parts are numbered from bottom to top, and the files follow the same order.

Not print tested by us yet. Print the fit test first, then the parts.

#blender #3dprinting #b3d #blendertips #shorts
```

## Eerste reactie
(leeg)

## Bronnen
- **Script en regels:** `commercie/filmpjes/scripts/click-cuts-lancering.md` nr. 3 (geen prijs, geen print-belofte, geen klik of magneten, printzin variant 2). Daan keurde de scripts.
- **"Twelve":** alleen omdat de opname echt 12 stukken geeft (de opname stopt met een fout als het er geen 12 zijn).
- **Nummer in elk snijvlak, eigen-buur:** `producten/blender-splitser/split_joints/verbind_3d.py` (tekst_p "a-b" op stuk a, tekst_q "b-a" op stuk b), `splitsen.py` (`sj_labels` per stuk). In beeld: de echte gegraveerde nummers, camera loodrecht op het vlak in hetzelfde assenstelsel als `vormen.label_frame`, andere stukken alleen in de weergave verborgen.
- **Verdiept, buitenkant schoon:** `vormen.py` `label_mesh` (plaat van 0,2 mm buiten tot de diepte binnen het snijvlak), `eigenschappen.py` `label_diepte_mm` standaard 0.6, "Engrave numbers" en "Depth (mm)".
- **Niet op een gat:** `verbinders.py` `kies_label` (punt met de meeste ruimte buiten de gaten, r_gat + 0,8 mm).
- **Kleinere vlakken, kleinere nummers (zin erbij, graag meekeuren):** `verbinders.py` `LABEL_HOOGTES = (8.0, 6.0, 5.0, 4.0, 3.0, 2.5)`, de grootste die past, anders langs het vlak; past er niets, dan een melding "no room for the number".
- **Diepte in More settings, stap 3 (zin erbij):** `paneel.py` stap 3 "Pins and numbers" onder More settings; `eigenschappen.py` default 0.6.
- **Van onder naar boven:** `splitsen.py` (nummers op z, dan y, dan x). In beeld de echte objectnamen Piece 01 tot Piece 12 in Exploded view.
- **Bestandsnamen (zin erbij):** `exporteer.py` r. 30 `piece_{nr:02d}`; in de opname gemeten (film-tip.json `bestanden`).
- **Model:** Lion Head, Poly Haven, CC0 (DERDEN: https://polyhaven.com/a/lion_head), buiten beeld gesplitst op de A1 mini.
- **Stem:** tijdelijk Kokoro-82M, af_heart, Apache 2.0 (DERDEN: https://huggingface.co/hexgrad/Kokoro-82M). ElevenLabs-opname (Max) gevraagd: `cc-nummers-elevenlabs.mp3` in `commercie/filmpjes/regisseur-21/`.
- **Nieuw onderwerp:** geen Short over nummers op onderdelen in de laatste 14 dagen (wachtrij en RSS nagekeken 24 nov ±11:55 NL, GEZIEN). cc-fit (splitsen) en cc-pas (fit test) zijn andere lessen.

## Keuring
(leeg tot de Keurder komt)

## Oranje-besluit
(alleen de hoofdchat, alleen bij oranje)

## Na plaatsen
(alleen de Maker)
