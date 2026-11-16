# Begraven dingen in de dichte aarde (Mila, proef 1, 16 nov ±22:15 UTC)

Vraag van Daan (16 nov 20:50, voor de demo van 18 dec, geen haast): op 1920 is in de eerste uren ±1200 px links kale aarde. Een handvol gedempte stukken in de aarde, ver uit elkaar, zodat de lege kant belooft dat graven iets oplevert. Eerst een proef op 1x en 4x.

## Wat er ligt
- `begraven.py`: vier stukken in Blender (bpy 5.2.4, met `gedeeld.py`, zelfde camera en licht als de rest), elk in een vak van 64 x 64 bladpixels = één cel van 16 x 16 spelpixels: een paarse punthoed met gouden band (van een held die het niet haalde), een bot, een kistje met goud beslag, een wortel met loof. Allemaal schuin, alsof ze zo in de grond gezakt zijn. Uit: `stukken-4x.png` (256 x 64).
- `leg_in_aarde.py`: dempt ze en legt ze in de echte dichte aarde uit `godot/kunst/3d/hol_proef.png`: 35 procent minder verzadigd, 28 procent richting de aardekleur, een donker holletje eromheen en kruimels aarde over de bovenrand. Ver uit elkaar: cel 3, 11, 18 en 26 van 30.
- `proef-blad.png`: boven de vier op 4x (2x vergroot), onder een strook op ware grootte (1x), 3x vergroot zonder verzachten. Losse bestanden: `proef-4x.png`, `proef-1x.png`, `proef-stukken-4x.png`.

## GEZIEN met Read, eerlijk
- Op 4x: alle vier lezen meteen, speelgoedachtig zoals Gloop en de kist, en ze zitten in de grond in plaats van erop.
- Op 1x: hoed, bot en wortel lees je; het **kistje is op 1x een bruine vlek** (te klein en te bruin op bruin). Volgende proef: kistje 20 procent groter, deksel op een kier met een glimp goud, zodat het zegt "hier zit schat".
- De herhaling van de steentjes in de achtergrond is van mijn proefveld (één tegel herhaald), niet van het spel.
- Nog niet gedaan: toetsen in een echte opname van 1920 naast Rusty's Retirement, en met Olaf afspreken hoe het spel ze neerlegt (vaste cellen, en wat er gebeurt als je erdoor graaft: oppakken met een klein moment, of gewoon weg). Wat je laat zien moet in het product zitten: als graven ze niet oplevert, moeten het gewone vondsten zonder belofte blijven. Dat beslist Sanne met Olaf.

## Proef 2 (16 nov ±23:20 UTC): moets van Daan (22:45), in een ECHTE opname van 1920
- **Echte opname:** `strook-10min.png` van tak `schermen`, `steam-hol-duur/main-1920x1080/` (run 43948989836, a90df14). Het spel staat daar op 3x: een cel van 16 spelpixels is 48 schermpixels. Stukken dus van 64 naar 48 en op de echte rijen (y 940 en 987). Script `leg_in_echt.py`, de opname zelf staat niet in deze map (staat op `schermen`).
- **Kistje:** 20 procent groter, deksel open naar achteren, vijf gouden muntjes steken boven de rand uit (`begraven.py`, uit: `stukken2-4x.png`). Op 1x lees je nu een schatkist in plaats van een bruine vlek.
- **Minder demping:** 20 procent minder verzadigd (was 35), 15 procent naar de aarde (was 28), niet meer donkerder, en een lichte rand van 1 px bovenaan. Holletje iets sterker (70 procent) zodat ze in de grond zitten.
- `proef2-echt-1x.png` (ware grootte), `proef2-echt-3x.png`, `proef2-stukken-1x-4x.png` (elk stuk uit de 1x, 4x vergroot), `proef2-blad-1x.png` (boven A met alle vier, onder B).
- **GEZIEN met Read op 1x en 4x van de 1x:** alle vier lezen op ware grootte (paarse hoed, bot, kistje met goud, wortel), ook naast de steentjes van het spel: die zijn even licht maar rond en kleurloos, de stukken hebben kleur en vorm. Eerlijk minder: met de lichte rand liggen ze iets meer óp de aarde dan in proef 1; het holletje maakt dat goed op de hoed en het kistje, de wortel zit door zijn schuine punt het best in de grond.
- **Eerlijkheid (moet):** variant B (`proef2-echt-B-1x.png`) heeft alleen bot en wortel, als gewone vondst. Hoed en kistje alleen als graven ze echt oplevert; dat vraag ik aan Sanne en Olaf (bericht 23:20).

## Proef 3 (16 nov ±23:50 UTC): moet Daan (23:30), half IN de aarde
- `leg_in_echt3.py`, uit: `proef3-echt-1x.png` (ware grootte), `proef3-echt-3x.png`, `proef3-stukken-1x-4x.png`, `proef3-voor-na-4x.png` (boven proef 2, onder proef 3).
- **Moet gedaan:** het onderste derde van elk stuk zit onder de aarde. De aarde ervoor is de echte grond van die plek, met een bultige rand, een zachte lichte lip (de kleur van de bovenrand van de gang), een schaduwrandje van 1 px op het stuk vlak boven de aarde en een paar kluitjes op het stuk. Eerst geprobeerd: een eigen hoopje verse aarde, lichter dan de grond. GEZIEN, las als een licht blok met een stippellijn erom; weggegooid.
- **Holletje** van 70 naar 15 procent, en alleen om het zichtbare deel (eerst zat er een spookschaduw van het begraven deel onder, GEZIEN en weg).
- **Kan gedaan:** bot 12 procent minder wit.
- GEZIEN met Read op 1x (2x vergroot) en 4x van de 1x: alle vier lezen op ware grootte en zitten erin in plaats van erop. Eerlijk minder: van het bot is één knobbel begraven, het leest nog als bot; de lip is op 1x maar een zweem, het werk doet vooral de afgesneden vorm.

## Spelblad voor Olaf (16 nov ±23:50 UTC, vraag Olaf 23:40)
- `producten/steam-hol/godot/kunst/3d/begraven.png` (320 x 64) met `begraven.png.import` en `begraven.json`. Vijf cellen van 64 x 64 bladpixels = 16 x 16 spelpixels bij px 4, zoals `holbord`. Cel linksboven = linksboven van de spelcel. Volgorde: `hoed`, `bot`, `kist`, `wortel`, `kist_open`.
- Demping en begraven zitten er al in: het onderste derde is in de cel **doorzichtig** (met lip en schaduwrandje erop), dus de echte aarde van het spel komt er doorheen, waar het ook ligt. Holletje 15 procent zit in de alfa.
- `kist_open`: dezelfde kist na het doorgraven, deksel helemaal open en plat naar achteren, kist 38 graden naar je toe gekanteld zodat je van boven het lege donkere binnenste ziet; niet begraven (die cel is dan gang), zachte schaduw eronder. Eerst met het deksel rechtop: GEZIEN op 1x, las als een tweede kist of ton, weggegooid. Eerlijk: hij is nu hoger dan de dichte kist omdat je in hem kijkt.
- Gemaakt met: `BLAD=1 <bpy-python> begraven.py stukken3-blad-4x.png` en daarna `python3 maak_blad.py <strook-10min.png>`. Proef in de echte opname: `blad-echt-1x.png` en `blad-proef.png` (boven 4x uit de 1x, de vijfde = na het doorgraven; onder het blad zelf).
