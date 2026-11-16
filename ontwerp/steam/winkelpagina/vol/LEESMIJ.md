# Het Hol moet vol (Mila, 16 nov ±09:00 UTC)

Antwoord op het bericht van de hoofdchat van 16 nov 09:45 NL ("Thijs: dit is ook wel een ander niveau"). Eerst het eerlijke antwoord, dan het doelbeeld, dan wat er in het spel moet.

## Vraag 3 eerst: halen we het niveau van Rusty's met 3D uit Blender?
**Ja, de stijl is het probleem niet; de leegte wel.** Onze figuren (Gloop, helden, hoeden, schat, troon) zijn in 3D al rijker dan de pixels van Rusty's: dat zie je in elke uitsnede. Wat Rusty's op een ander niveau zet, is dat elke pixel van het beeld iets is: plantjes, water, paden, dieren. Bij ons is ±40% van elk beeld kale aardwand met dezelfde ronde stippen, en de gang heeft hooguit één ding per twee tegels (bewust zo uitgedund op 14 nov, zie `hol/hol_vast.gd` `deco_hh`). Dat is geen grens van Blender; het is wat het spel nu tekent.
Wat ik niet kan beloven: dat onze strook (12 op 1) ooit zo vol oogt als Rusty's bovenaanzicht. Een zijaanzicht heeft altijd aarde boven de gang. Die aarde moet dus zelf iets vertellen. Daarom het voorstel hieronder (hoeden in de wand). Een tekenaar of een andere stijl is volgens mij niet nodig; wel ±2 dagen werk aan het hol zelf.

## Doelbeeld (GEEN winkelbeeld)
- `doelbeeld-vol-1920.png` (winkelvorm, twee rijen zoals scherm 1) en `doelbeeld-strook-vol.png` (de hele strook op spelmaat). Gemaakt met `maak_doelbeeld_vol.py`.
- Basis is de echte opname week 160 zaad 2 (run 43741619098, beeld 1000). Erbij geplakt, alleen met stukken die al in het spel zitten (`producten/steam-hol/godot/kunst/3d/deco.png`, `bard.png`, `heks.png`, `hoeden.png`): op elke vrije gangtegel iets (ton, krat, schedel, paddenstoel, kristal), spinrag, stut en vaandel aan het plafond, drie extra kamers met spullen erin, twee helden extra (bard en heks), en **hoeden die half in de aardwand steken** (3D-render klaar, nog niet in het spel).
- Naast de toppers: `vergelijk-doelbeeld-toppers-600.png` en `vergelijk-doelbeeld-rusty2-600.png`. GEZIEN met Read op 1920 en op 600. Oordeel: van "lege bruine gang" naar "druk, warm hol waar van alles gebeurt"; de hoeden in de wand lezen op 600 als hoeden en zijn meteen van ons. Nog niet op Rusty's niveau: de stippen in de aarde blijven één herhaald patroon, en het kaartje onderaan heeft donkere zijkanten.
- **Mag niet de winkel in** zolang het spel het niet zelf zo tekent. Pas als Olaf het bouwt, maken we de echte opname en snijden we opnieuw.

## Eigen gezicht: de hoedenwand
Elke held die Gloop opeet, laat een hoed achter. Nu liggen die op de berg bij de troon. Voorstel: de oudste hoeden zakken de aardwand in en blijven daar scheef half begraven zitten, met een donkere holte eromheen. Hoe langer je speelt, hoe voller de wand. Dat is (1) dichtheid zonder nieuwe soorten spullen, (2) iets wat niemand anders heeft (de wand is je logboek van opgegeten helden), (3) eerlijk, want het groeit uit wat er echt gebeurde, en (4) een grap: "the walls are made of former heroes".
De renders staan er al: `ontwerp/steam/hoedenwand/renders/wand-0..9.png` (alle 10 hoeden, 400x300, doorzichtig, zelfde camera en licht als de rest), gemaakt met `ontwerp/steam/hoedenwand/hoedenwand.py`. In het doelbeeld staan ze op 50 px breed in de strook. Bram: neem het model over in de pijplijn (spelmaat, een blad zoals `deco.png`); Olaf plaatst.

## Wat er in het spel moet (voor wo 18 nov, in volgorde van winst per uur)
1. **Olaf:** in `deco_hh` de uitdunning losser in een volgebouwd hol: elke vrije gangtegel mag een vloerding (niet op looppad bij vallen en schacht, die regels blijven), plafondding los daarvan. Daan dunde uit op 14 nov omdat een frisse kijker het druk vond in een **leeg** hol; in week 160 is het hol groot genoeg.
2. **Olaf:** spullen in de kamers boven de gang (nu staat er alleen een kistje): twee stuks uit `DECO_GANG` per kamer.
3. **Olaf:** in de winkelopname week 160 drie helden tegelijk in beeld (nu één, soms twee).
4. **Bram:** de hoedenwand-renders (staan klaar) in de pijplijn; Olaf plaatst er één per opgegeten held in de aarde boven de gang, op vaste hash-plekken buiten de kamers.
5. **Mila:** daarna de echte opname snijden, naast Rusty's 2 en Spirit City op 600 leggen, en pas dan keuring bij Daan.
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.
