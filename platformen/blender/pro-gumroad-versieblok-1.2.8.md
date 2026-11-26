# Click Joints Pro: versieblok voor de Gumroad-beschrijving (Bram, 26 nov 2026, issue #178)

**Waarom (geld):** vanaf vr 27 nov landen kopers via de salelink op Gumroad. Superhive toont "New in Pro 1.2.8"; Gumroad noemt nergens een versie of wat er nieuw is (curl 26 nov 14:09 NL, GEZIEN). Een koper ziet dan niet of de add-on bijgehouden wordt en of hij werkt in zijn Blender. Effect op verkoop: GOK, klein, maar het haalt een twijfel weg op het moment van kopen.

**Bron:** de drie regels zijn letterlijk het blok "New in Pro 1.2.8" dat live op Superhive staat (curl 26 nov 14:09 NL, GEZIEN), dat komt uit `pro-1.2.8.md` deel 4 (Daan ja, #11 en #37). Datum: live gezet op 25 nov 20:25 NL (`producten/blender-gewrichten/KAART.md`, GEZIEN door de hoofdchat).

**Bewuste afwijking van de issuetekst:** het issue vroeg "Blender 4.2 to 5.3". Dat zou zeggen dat 4.3 tot 5.1 getest zijn; dat is niet zo. De manifest zegt minimaal 4.2.0 en geen maximum, getest is 4.2 LTS, 5.2 LTS en 5.3 (e2e 45526260663, GEZIEN). Daarom "Blender 4.2 or newer, tested on ...", gelijk aan de regel "Tested on ..." op Superhive.

## Plakken (Gumroad, product Click Joints Pro, beschrijving)

**Stap 1.** Zet dit blok direct onder de alinea die begint met "Try it free first:" (dus boven de kop "From rig to a figure that moves."). "What's new in 1.2.8" als kopje (H3 of vet), de drie regels als opsomming:

```
Version 1.2.8 (25 Nov 2026). Blender 4.2 or newer, tested on 4.2 LTS, 5.2 LTS and 5.3.

What's new in 1.2.8
- "More bones" now gives ankles, also on blocky feet like a robot (Blender 5.2 and newer).
- Shift + right click on the skin now works with Knee, Elbow, Ankle and the hinge buttons.
- A knee with a kneecap, like the robot's, now gets a good fit in the middle of the knee.
```

**Stap 2.** Onderaan staat nu "Already bought Pro? 1.2 is a free update: download it again from your Gumroad library." Vervang die regel door:

```
Already bought Pro? 1.2.8 is a free update: download it again from your Gumroad library.
```

Verder niets aanpassen. Na het plakken: met curl nakijken dat "Version 1.2.8" en "What's new in 1.2.8" op https://duinhouwer8.gumroad.com/l/click-joints-pro staan.

## Stand
- 26 nov 14:20 NL: concept klaar, keuring gevraagd aan Daan.
- 26 nov 15:05 NL: Daan ja (8), #187; gemeld als klaar om te plakken in `berichten/hoofdchat.md`.
