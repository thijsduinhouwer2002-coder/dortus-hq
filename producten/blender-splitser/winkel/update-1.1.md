# Click Cuts 1.1.0: plakbundel voor de dag na de lancering (CONCEPT tot Daan ja)

Productbouwer, vr 27 nov 2026 ±07:00 NL, issue #248. Voor de hoofdchat, die plakt in de Chrome van Thijs (inloggen alleen Thijs). **Niet vóór 1.0.0 live staat op Gumroad.** Op Superhive pas als 1.0.0 daar Approved is: tijdens de keuring kan niets veranderen (DERDEN, artikel 195, zie `lancering.md` punt 0).

Waarom 1.1 snel na de lancering: alle vier de rechters in de blinde test vroegen om zelf te kiezen waar het snijdt ("doesn't slice through my character's face", `organisatie/lat/click-cuts.md` gat 3). Met 1.1 zegt de FAQ daar "Yes" in plaats van "Partly". En hars- en TPU-printers vinden de passende speling nu op het eerste proefblok (gat 5). Effect op verkoop: GOK.

Elke tekst hieronder staat letterlijk in een bestand op de tak, en `winkel/controleer_update.py` kijkt dat na, samen met de woorden in de code.

## 1. Volgorde
1. Tak `claude/click-cuts-1.1` naar main (Productbouwer, na het live gaan van 1.0.0).
2. De e2e van die push op main geeft `click-cuts-kandidaat` met `click_cuts-1.1.0.zip`. Vastzetten met tag `click-cuts-uitgave-<run_id>` (hoofdchat): de uitgave-workflow leest de versie nu uit de zip (#248), dus geen aanpassing nodig.
3. Gumroad, dan Superhive, zoals hieronder. Docs-tab en FAQ-tab: het blok "Tekst voor de tab" uit `winkel/docs.md` en `winkel/faq.md` van main na stap 1 (beide al gekeurd voor 1.1, Daan #240).

## 2. Releasenote 1.1.0 (Engels, Gumroad en Superhive)
Gelijk aan de kop 1.1.0 in `producten/blender-splitser/CHANGELOG.md`.
```
Click Cuts 1.1.0
- New: Draw cut. After Split to fit, click a part, press Draw cut and drag a line where you want it cut, for example under the chin or at the shoulder.
- New: before you cut, the part that comes off lights up white with an arrow that says "comes off". Wrong part? Press Flip side.
- New: the clearance starts at a value for your material until you save a fit test: Resin 0.10, PLA 0.20, PETG and ABS / ASA 0.25, TPU 0.30 mm. The fit test block covers that value.
- Better: after Split to fit, the result box names the clearance the parts were cut with, and tells you to split again when you change it.
```

## 3. Update log Superhive (bovenaan erbij)
```
1.1.0: Draw cut: drag a line across a part where you want it cut. The part that comes off lights up white first. The clearance now starts at a value for your material (Resin 0.10 mm, TPU 0.30 mm) until you save a fit test.
```

## 4. Beschrijving (Gumroad en Superhive): twee regels vervangen
In het blok Description uit `lancering.md` punt 2 verandert alleen dit. De rest blijft woord voor woord.

Regel **Free cut** wordt:
```
- **Draw cut:** after Split to fit, click a part and drag a line where you want it cut, for example under the chin or at the shoulder. The part that comes off lights up white before you cut. Or add a free cut and set it with G, R and S.
```
Regel **Fit test** wordt:
```
- **Fit test:** print one small block with your own pin at four clearances, pick the one that fits, and Click Cuts keeps it for that printer and material. Until then it starts at a clearance that suits your material, from 0.10 mm for resin to 0.30 mm for TPU.
```
Titel, haak, beelden, tags en prijs blijven gelijk (titel en haak GESLAAGD in de blinde test; een nieuwe titel zou een nieuwe test vragen).

## 5. Bestand
- Gumroad: in Content de zip `click_cuts-1.0.0.zip` vervangen door `click_cuts-1.1.0.zip` (Standard en Supporter). Wie al kocht, downloadt de nieuwe zip van dezelfde pagina.
- Superhive: nieuwe versie uploaden met `click_cuts-1.1.0.zip`, Blender 4.2 en nieuwer.
- Een mail aan kopers via Gumroad gaat onder de naam van Thijs: alleen met zijn ja op de tekst. Concept als hij dat wil: de releasenote van punt 2, zonder meer.

## 6. Wat ik niet kon nakijken
- Of het Superhive-formulier voor een nieuwe versie het update log apart vraagt of in de beschrijving (GOK; bij Pro staat het bovenaan de beschrijving, `platformen/blender/pro-1.2.9.md` punt 3).
- Of een nieuwe versie op Superhive opnieuw gekeurd wordt (GOK, niet gezien).
