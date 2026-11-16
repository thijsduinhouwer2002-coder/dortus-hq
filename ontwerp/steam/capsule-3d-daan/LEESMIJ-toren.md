# Capsule TOREN: richting voor "He wears their hats" (Daan, 16 nov 2026)

Aanleiding: besluit hoofdchat 16 nov 08:05 NL (advies Fenna, `platformen/succes/onderscheid-hats.md`): de hoedentoren moet het grootste ding op de capsule zijn, ook op 120 px en in grijs. Mila is eigenaar van de capsule; dit is een richting om op voort te bouwen, geen vervanging.

## Bestanden
- `capsule_toren.py`: kopie van Mila's `capsule3d.py` met omgevingsgetallen `TOREN_*`. Gloop draagt alleen de helm uit `gloop.py`; daarop stapelt het script hoeden uit `hoeden.py` (meet elke hoed en zet de volgende erop, `TOREN_ZAK` = hoe diep hij erin zakt). Minder goud (`TOREN_BERG`), geen beker, geen hoed op de berg, linker fakkel weg (stond achter de titel), ridder kleiner.
- `maak_toren.sh`: ronde 1 (header en klein), op dubbele grootte en verkleind.
- Ronde 1: `toren-header-920x430.png`, `toren-klein-462x174.png` (6 hoeden: helm, kroon, koksmuts, veermuts, emmer, puntmuts).
- Ronde 2, alleen klein: `toren-klein-ronde2-462x174.png` (4 groter: helm, kroon, koksmuts, hoge hoed, puntmuts; donkere muur). Instellingen: `TOREN_ZAK=0.12,0.38,0.32,0.15 TOREN_HOEDEN=4,5,7,1 TOREN_KANTEL=4,-9,10,-12 TOREN_S=1.1 TOREN_GROOT=1.0 TOREN_KRS=0.8 TOREN_WANDGLOED=60 TOREN_RAND=150 CAP_WANDLAMP=120 CAP_WAND1=3a2420 CAP_WAND2=4e3028 TOREN_KCZ=3.2 TOREN_KLENS=24 TOREN_KTZ=1.45 TOREN_KTM=1.5 TOREN_KTX=-0.2 python capsule_toren.py uit.png 924 348 32 klein`.
- Toetsen op 120 px, kleur en grijs, naast Don't Rob My Dungeon (header uit de openbare appdetails-API): `toren-toets-120-grijs-1x.png` (ronde 1, ook de header) en `toren-toets-120-grijs-ronde2-1x.png`.
- Let op: hoed 3 (pet) meet verkeerd in het script (de klep geeft een kader tot -2,8), daarom zit hij er niet in.

## Wat ik zag (GEZIEN met Read, ook 3x vergroot)
- **Ronde 1:** groot ziet het er speels uit, een wiebelende toren die je wilt bekijken. Maar op 120 px is het een dun paaltje met strepen boven een klein slijm. Blinde kijker: nu 4, toren r1 5 op het doel "slijm met een stapel hoeden". Fouten: toren te smal (6 tot 8 px op 120), lichte hoeden verdwijnen in de lichtvlek op de muur, veel lege muur.
- **Ronde 2:** donkere muur, minder en grotere hoeden, een donkere hoge hoed tussen de lichte. Op 120 lees je nu wel "hoeden" (puntmuts en hoge hoed vallen op, ook in grijs). Nog zwak: Gloop is te klein en de punt van de puntmuts raakt de bovenrand.

## Les voor de capsule (wat werkt op 120 px)
1. **Lager en breder, niet hoger.** Een capsule is breed; een hoge toren wordt een stokje. Liever 4 of 5 grote hoeden dan 6 kleine.
2. **Afwisselend licht en donker.** Grijswaarde telt meer dan kleur: hoge hoed (donker) tussen koksmuts en kroon (licht). Emmer en bruin verdwijnen tegen de muur.
3. **Donkere muur achter de toren**, geen lichtvlek daar; het licht hoort óp de hoeden (randlicht van boven).
4. **Gloop groter dan nu in r2**, het oog is het tweede herkenningspunt. De ridder mag een stipje zijn of weg in klein.
5. Wat nog te proberen (Mila): toren licht scheef naar de titel toe, zodat hij de breedte gebruikt; elke hoed een donkere rand (zoals het icoon van het Gloop-spel).
