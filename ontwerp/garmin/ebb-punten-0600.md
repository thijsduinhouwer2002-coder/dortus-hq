# Vijf punten van de hoofdchat (12 nov 06:00), Mila run 54

Antwoord op `berichten/mila.md`, bericht "run 52 en 53 bekeken, akkoord, en vijf kleine punten".

## 1. Menu: de gekozen knop zoals Resume
Script `bron/menu_v4.py`, beelden `menu4/` (krab, schildpad, clownvis; dag en nacht; 260 en 454).
- Gekozen knop overdag: vlak 00FFFF, geen rand, tekst 000055. Bij nacht: vlak 0055AA, rand 55AAFF (2 px), tekst wit. Precies de regel van Resume op het pauzescherm (`bron/onderwater_v1.py`).
- Andere knop: donker vlak (MIP 000055, AMOLED 001E3C overdag en 000028 bij nacht), rand 00AAFF overdag en 0055AA bij nacht, tekst wit.
- Eén regel voor alle menu's: menu, pauze en instellingen.
- Voor Gijs: de knoppen horen bij de uitzondering van de nachtregel, net als de tekst. Ze zijn al in nachtkleuren getekend.
- GEZIEN met Read: `menu4/overzicht-menu-krab-2x.png`. Rounds springt er nu in één blik uit.

## 2. Menu nacht: voetregel gemeten
Gemeten in `menu_v4.py` (geel FFFFAA tegen de lichtste pixel in een ring van 2 tot 3 px rond de letters, achtergrond na de nachtregel):
- 260 nacht 17,8 op 1, 454 nacht 19,8 op 1 (alle drie de werelden).
- Overdag: 260 7,0 en 454 5,8 (laagste).
Kleur blijft dus FFFFAA. Dat hij dof oogde komt door de kleine letter (16/260), niet door het contrast. Leest hij op het echte horloge toch dof, dan is de volgende stap wit; maar wit maakt hem gelijk aan de knoptekst.

## 3. Familie licht: roze band wordt licht geel
`bron/werelden_v5_lucht.py`: band van de familie licht (kwal, zeepaardje, maanvis, haai) van FFAAFF naar FFFFAA (AMOLED onderste stap FFF0A0). De roze kwal staat nu los van de lucht. Past bij de naam van de familie (licht, zon met stralen). Zon blijft erboven, raakt de band niet.
GEZIEN met Read: de vijf in de nieuwe lucht op 260 (`werelden5/*-in-dag-260.png`).

## 4. Inktvis op het eilandje
`bron/werelden_v4_koud.py`: inktvis kleiner (m 50 in plaats van 54) en 26 lager, half in de zee; het eilandje staat nu links van hem zodat zijn ogen langs de palm gluren (de palm bedekte ze eerst).
Gemeten op 260: punt van de inktvis bij inademen op y 78 (was ±62), ruim 30 px rechts van de "12"; bij uitademen y 114 en bij Calm y 90, allebei onder de onderkant van het cijfer (97).
Eerlijk: bij inademen staat de punt nog naast het cijfer, op 30 px afstand (veilige zone is 6). Helemaal onder het cijfer (y 93 of lager) heb ik geprobeerd: dan blijft alleen een paarse punt boven de zee over en is het geen inktvis meer. Weggegooid. Hij leest nu als een grote inktvis die zich slecht verstopt achter een piepklein eilandje.

## 5. Today bij nacht: zand een trede lichter
`bron/strand_v2.py`: bij nacht vóór de regel droog zand AAAAFF en nat zand AAAAAA; na de regel 5555AA en 555555, de zee 000055. Het strand blijft dus zichtbaar. De uurlabels en "first shell" bij nacht van AAAAAA naar FFFFAA (zoals 8 weeks al had), want op het lichtere zand zakten ze naar 2,8.
Gemeten met `meet_strand_v2.py`: alle regels 5,06 of hoger (was 12 regels onder 4,5 direct na de zandwijziging).
GEZIEN met Read: today-3 dag en nacht op 260 en 454, weeks-5 nacht.
