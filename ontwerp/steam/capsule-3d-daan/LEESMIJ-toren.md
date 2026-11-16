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

## Ronde 3 (klein, scheef naar de titel), 16 nov ±07:55 UTC
`toren-klein-ronde3-scheef-462x174.png`, toets `toren-toets-120-grijs-ronde3-1x.png`, GEZIEN. Zelfde als ronde 2 met `TOREN_KANTEL=6,10,14,18 TOREN_SCHUIF=-0.12,-0.2,-0.28,-0.3 TOREN_KCX=0.9 TOREN_KCZ=3.6 TOREN_KLENS=21 TOREN_KTZ=1.6 TOREN_KTX=-0.6 TOREN_KRS=0.7`.
- Groot oogt hij levendiger (een toren die bijna omvalt naar de titel, past bij de grap). Op 120 px ongeveer gelijk aan ronde 2.
- Nog steeds te klein: Gloop. In klein staat `GROOT` vast op 1,3 in het script (`TOREN_GROOT` werkt alleen in de header), en de hoeden schalen mee met de helm. Gloop groter maken = `GROOT` voor klein instelbaar maken en `TOREN_S` iets omlaag.
- Fout om te verhelpen: witte glansvlek op de H van HATS (sleutellicht), en een donkere fakkelrest aan de rechterrand.

## Ronde 4 (Mila, klein, 16 nov ±11:00 UTC)
`toren-klein-ronde4-mila-462x174.png`, naast ronde 3 met 120 px in kleur en grijs: `voor-na-ronde3-ronde4-mila-met-120.png`. GEZIEN met Read. Gerenderd op 924x348 (16 samples) en verkleind.
- Script: `GROOT` voor klein is nu instelbaar (`TOREN_KGROOT`, standaard 1,3 zoals het was) en het sleutellicht ook (`CAP_SLEUTEL`, standaard 1600). Verder niets aan Daans script veranderd.
- Instellingen: `TOREN_ZAK=0.12,0.38,0.15 TOREN_HOEDEN=4,7,1 TOREN_KANTEL=6,12,24 TOREN_SCHUIF=-0.12,-0.22,-0.34 TOREN_S=0.9 TOREN_KGROOT=1.6 TOREN_KRS=0.7 TOREN_WANDGLOED=60 TOREN_RAND=150 CAP_WANDLAMP=120 CAP_WAND1=3a2420 CAP_WAND2=4e3028 TOREN_KTM=1.5 CAP_SLEUTEL=900 TOREN_KCX=1.0 TOREN_KLENS=23 TOREN_KCZ=3.9 TOREN_KTZ=1.9 TOREN_KTX=-0.9 python capsule_toren.py uit.png 924 348 16 klein`.
- **Wat anders is:** Gloop 1,6 in plaats van 1,3, drie hoeden in plaats van vier (kroon, hoge hoed, puntmuts), elk een eigen omtrek, en de hele toren in beeld, scheef naar de titel. Op 120 px lees je nu een groot slijm met een stapel hoeden in plaats van een paaltje boven een stipje.
- Geprobeerd en niet gekozen: vier hoeden met Gloop 1,75 (toren loopt boven uit beeld, dan is het geen toren meer), koksmuts bovenop voor licht-donker-licht (leest als popcorn of wolk, net als op het icoon).
- Nog open: in grijs vallen puntmuts en hoge hoed samen tot één donkere vorm (alleen de kroon is licht); de witte glansvlek op de H blijft ook met een zwakker sleutellicht, die komt van een ander licht. Volgende stap: puntmuts lichter paars (zoals op het Garmin-icoon, richting 8a6ad8) en de glans op de H zoeken.
- **Ronde 4b (keus):** zelfde als ronde 4 met `TOREN_PAARS=b89cf0` (nieuwe schakelaar, kleurt alleen het materiaal "paars" van de puntmuts). `toren-klein-ronde4b-mila-462x174.png`, rij ronde 3, 4 en 4b met 120 px kleur en grijs: `voor-na-ronde3-4-4b-mila-met-120.png`. GEZIEN: in grijs is de toren nu licht (puntmuts), donker (hoge hoed), licht (kroon), dus drie hoeden te tellen; op 120 px groot slijm met toren. 9a7ae8 geprobeerd, scheidt in grijs minder.
- **Header ronde 4 (Mila, 16 nov ±11:10 UTC):** `toren-header-ronde4-mila-920x430.png`, naast Daans ronde 1: `voor-na-header-ronde1-ronde4-mila.png` (met 120 px kleur en grijs). Zelfde drie hoeden en paars als klein 4b, plus `TOREN_GROOT=1.7 TOREN_CZ=3.8 TOREN_LENS=24 TOREN_TZ=1.1 TOREN_TM=1.45 HEADER_RY=-1.3`, 1840x860 met 16 samples, verkleind. GEZIEN: Gloop en toren vullen de rechterhelft, titel groter, ridder klein ervoor; geen lege muur meer boven de titel. Ook hier nog een lichte glans op de H.
