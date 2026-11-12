# Ebb werelden v3: schildpad en clownvis (Mila, run 47, 12 nov 2026)

Opdracht: hoofdchat 12 nov 03:10 NL (besluit 03:10): schildpad en clownvis in de opzet van de krab v2.2, zes schermen, dag en nacht, 454 en 260. Elk een eigen plek en een eigen grap, geen kopie van de krab.

Bestanden: `werelden3/<schild|clown>-<in|uit|calm|hold|menu|eind>-<dag|nacht>-<454|260>.png`, overzichten `werelden3/overzicht-<schild|clown>-454-1x.png`, `-260-2x.png`, `-260-1x.png` (ware grootte). Script: `bron/werelden_v3.py` (`python3 werelden_v3.py ../werelden3`), leunt op `werelden_v21.py` voor water, bundel, stofjes en tekst.

## De twee werelden
- **Schildpad: zeegrasweide.** Onder water een lichte zandvlakte met veel ruimte in het midden, hoge sprieten aan beide randen, een schelp en een steentje. De schildpad graast: er komt een spriet uit het zand die in zijn bek eindigt, met twee groene kruimels ervoor (een groene zeeschildpad eet echt zeegras).
- **Grap boven water: de schildpad is een eilandje en er lift een meeuw mee op zijn schild.** De meeuw kijkt de andere kant op dan de schildpad. Hij drijft IN het water (een golfje met schuimrand voor zijn buik), kop en schild erboven. Op het eindscherm staat de meeuw er ook bij: hij gaat overal mee. Nieuwe vriend hier: Jellyfish.
- **Clownvis: rif met zijn anemoon als huis.** Rechts een donkerpaarse rifbult met een grote roze anemoon (acht vingers, lichte toppen), twee vingers liggen voor de vis; links een paarse waaier en een geel takje. Nieuwe vriend hier: Seahorse.
- **Grap: hij is een clown, dus hij jongleert.** Boven water springt hij uit de golf (spatkroontje onder hem, bij inademen het hoogst, bij uitademen bijna in het water) en houdt drie belletjes in de lucht. Onder water en op het eindscherm jongleert hij gewoon door.

## Uit keuring 13 en Gijs run 51 meegenomen (geldt voor alle drie de werelden)
1. **Twee golfrijen onder de kam** in plaats van drie of vier (Gijs: ±120 punten per beurt past, ±240 niet).
2. **AMOLED-lucht overdag**: bovenin 001E5F, naar 004BA5 halverwege, fel 00A5FA alleen als band boven de horizon (minder fel, minder stroom).
3. **Geen baan van licht onder de zon**: drie losse vonkjes op het water (bij nacht drie puntjes), geen vlak (Gijs: de trapezium was hard).
4. **Eigen detail onderin het water**: de schaduw van de volgende vriend (vis), vaste donkere tint, alleen als hij binnen de cirkel past (niet bij uitademen).
5. **De held kantelt mee**: 8 graden neus omhoog bij inademen, 3 bij Calm, plat bij uitademen. Het dier zelf blijft zoals het is, het draait alleen als geheel.
6. **"press START to breathe" blijft altijd staan tijdens inhouden** (veiligheid), de bpm-regel is een maat groter (18 in plaats van 16).
7. Geen doorschijnend vullen nodig: alle gloed en de bundel zijn 3 vaste tinten zoals in v2.1 (FR165 en vivoactive 5 kennen geen doorschijnend vullen). **Wit altijd als gewone kleur**, nooit als doorschijnende kleur (op de fenix 8 was wit met volle dekking hetzelfde getal als "doorzichtig", Gijs run 51 punt 2).

## Bouwgegevens voor Gijs (1/260 D)
- Boven water schildpad: maat 44 op (166, kam − 4), bij uitademen x 128; kantelen zoals punt 5; golfje voor de buik op kam + 10, breedte 2 x maat; meeuw schaal 1,4 op de schildtop (dier + (0,16 m, −0,6 m) gedraaid, dan 11 hoger).
- Boven water clownvis: maat 32 op (188, kam − sprong), bij uitademen x 176; sprong 26 / 18 / 12 (in / Calm / uit); kantel + 10; belletjes in een boog met straal 24 rond (x + 2, y − 16), drie bollen r 4,4 met witte rand, negen stipjes als worp.
- Inhouden: schildpad maat 46 op (136, 182); clownvis maat 33 op (150, 184), anemoonvoet (206, 200). Menu: schildpad 42 op (132, 188), weide gespiegeld; clownvis 30 op (142, 188). Eind: held links (76, 134) maat 36 of (74, 128) maat 29, vriend in het belletje (184, 122), rx 40, ry 35.
- Punten: weide ±20 sprieten van 26 punten is te veel voor direct tekenen, maar alles behalve held, spriet in de bek en jongleerbellen ligt stil en hoort in het plaatje van de wereld (grens 140 in het plaatje).

## Wat ik zelf zag (Read, 260 2x en 454)
- Schildpad met meeuw leest meteen, op 260 ook; de meeuw is klein maar wit op blauw en heeft een donkere rand.
- Clownvis met belletjes leest als jongleren; de bogen raken het cijfer niet.
- Zwak: onder het schild steken flarden van de achterpoten onder het golfje uit (leest als poten in het water, mag); eindscherm clownvis heeft onderin weinig zand omdat het rif omlaag moest voor de naam "Seahorse".
- Frisse keuring volgt (regel: door bij een frisse 7 plus akkoord hoofdchat).

### Frisse keuring 14 (op v3): schildpad **7**, clownvis **6**
Schildpad: de meeuw als lifter komt zonder uitleg over, ook op 260. Clownvis: de sprong komt over, jongleren maar half (lichtblauwe belletjes lazen als luchtbellen of aureool). Meteen gedaan in deze run:
- Jongleerballen nu drie felle kleuren (geel, roze, groen) met witte rand: leest als jongleren.
- Spat onder de springende vis: losse druppels en een spatkroon in plaats van een witte schijf (las als bootje), ook kleiner bij uitademen en Calm.
- Meeuw ook bij nacht wit (verdween tegen de nachtlucht).
- Meeuw weg van het eindscherm (stond onder water, klopte niet).
Open voor de volgende run: zeegras eten duidelijker (breed blad tussen de kaken, spriet met hap ernaast), weide rijker (dichte plukken in twee tinten, zeester), overdag iets onder het eilandje, clownvis echt half in zijn anemoon, eindscherm clownvis met vis en anemoon samen in beeld. Daarna weer een frisse keuring; door naar Gijs bij een frisse 7 voor de clownvis plus akkoord hoofdchat.

## Versie 3.1 (run 48, 12 nov): punten keuring 13 en 14
Zelfde map en script; `werelden3/` heeft nu ook de krab (`krab-*.png`, `overzicht-krab-*`) met de gedeelde lucht en zee van v3, zodat alle drie de werelden hetzelfde water hebben.
- **Krab (keuring 13 punt 1 en 2):** de verre slipper is een derde van de bootslipper (k 2,4 op x 72) met een witte V; de bootslipper kantelt mee (hoek −5 min 8 / 3 / 0 graden bij in / Calm / uit), de krab draait 0,6 keer mee; teenpaaltje wit met donkerroze rand. Onder water en eindscherm zoals v2.2.
- **Schildpad eet zichtbaar:** een breed blad zeegras (00AA55, witte rand, nerf) steekt uit zijn bek, naast hem een spriet met een ronde hap uit de rand; de schildpad buigt 7 graden met de kop omhoog naar zijn spriet. Op het eindscherm kauwt hij nog op een blad. **Rijkere weide:** dichte plukken in twee groentinten vooraan en een oranje zeester.
- **Eigen detail onderin bij de ademschermen:** schildpad een losgeraakt blad zeegras dat onder het oppervlak drijft; krab en clownvis de schim van de volgende vriend, overdag nu lichter (0055AA op MIP) zodat hij ook overdag te zien is.
- **Clownvis:** zit nu half in zijn anemoon (vier vingers voor hem, kop en voorste band vrij); rifbult breed en laag (geen bloempot); spatwater als twee ringen in het water plus druppels (de spijlen lazen als hekje); jongleerballen geel, roze en groen; eindscherm met vis in een kleine anemoon samen in beeld.

### Frisse keuring 15 (op v3.1 vóór de laatste punten): schildpad **7**, clownvis **6**
Gedaan na keuring 15: blad twee keer zo groot en de schildpad schuin met de kop omhoog, blad in de bek op het eindscherm, drijvend zeegras als eigen detail, spat als ringen, rifbult zachter, vis verder uit de anemoon.
Niet gedaan: borstvinnen omhoog naar de ballen (dat is het dier zelf aanpassen, en de dieren liggen vast). Open: jongleren nog sterker zonder het dier te wijzigen (misschien een bal die net op zijn neus stuitert), lucht naast de zon bij de clownvis.
**Stand:** schildpad heeft een frisse 7 (twee keer); die kan met akkoord van de hoofdchat naar Gijs. Clownvis zit op 6 en blijft bij mij.
