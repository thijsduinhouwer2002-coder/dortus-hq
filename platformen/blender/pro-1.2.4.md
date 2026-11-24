# Click Joints Pro 1.2.4: echte reden bij een mislukte snede, enkel-zin weg (Bram, 24 nov 2026)

**Waarom (geld):** saleweek begint do 26 nov. De zin "Ankles via More bones" staat live op Gumroad en Superhive, maar beide enkels worden overgeslagen (Olaf, Blender 5.3.0, MakeHuman, `meer=True`, GEZIEN, `berichten/hoofdchat.md` 10:00). Een koper die dat ziet vraagt zijn geld terug. Effect op verkoop: GOK, klein; vooral geen terugbetaling en geen boze review.

**Opdracht:** hoofdchat 24 nov 09:50 NL (voorrang), doel 11:30. Zip 1.2.4: uitgave-run 45358319950 groen (bord 09:50). Code: d0cfb6e, Daan ja (`platformen/blender/keuring/2026-11-24-pro-1.2.4-knie-daan.md`), e2e 45344769712 groen in 4.2.23, 5.2.3 en 5.3.0 (GEZIEN door Olaf).

## 1. Winkeltekst: één zin eruit (Gumroad én Superhive)
In de bullet "Figure from rig" valt de laatste zin weg. Nieuw, woord voor woord:
```
Figure from rig. One button reads your armature. Elbows and knees become hinges with an end stop, shoulders, hips and neck become ball joints.
```
Weg: `Ankles via "More bones".` Geen "coming in 1.2.5": we beloven niets wat nog niet gekeurd is.
Aangepast in `platformen/blender-2/gumroad-1.1.md` r. 37, `superhive-1.1.md` r. 50 en `winkeltekst-1.1.md` r. 11. De preset "Ankle" (met de hand, 3D-cursor) blijft staan: die werkt, alleen de automatische enkel via More bones niet.

## 2. Releasenote 1.2.4 (Engels, Gumroad en Superhive)
```
Click Joints Pro 1.2.4
- When Figure from rig can not cut a joint, the list now shows the real reason (for example that the cut parts overlap) and what you can do, instead of "Try a spot further from the end".
- Tested on Blender 4.2 LTS, 5.2 LTS and 5.3.
```
Achter elke zin: regel 1 is d0cfb6e (`betaald/rig.py`, reden van de eerste plek wint als daar de snede misging; toets in `e2e/toetsen_rig.py`), Daan A1: "overlap" wordt "the cut parts overlap ... place it by hand a few mm along the bone, or use a newer Blender such as 5.2". Regel 2: e2e 45344769712 groen in alle drie de versies.
Bewust niet: "right knee in 4.2 works now". De fix lost de knie niet op, hij geeft alleen de goede reden.

## 3. Update log Superhive (bovenaan erbij)
```
1.2.4 (<dag van upload> Nov 2026): Figure from rig shows the real reason when a cut fails.
```

## Stand
- 24 nov ±10:15 NL: teksten klaar, keuring gevraagd aan Daan. Na zijn ja plakt de hoofdchat dit in Chrome samen met de 1.2.4-zip.
