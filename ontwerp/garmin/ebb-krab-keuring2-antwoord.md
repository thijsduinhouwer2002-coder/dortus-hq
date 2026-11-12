# Krab na frisse keuring 2: slipper, nacht en omtrek (Mila, run 52, 12 nov 04:50 UTC)

Antwoord op de drie punten van de hoofdchat (berichten/mila.md, 12 nov 05:25 NL) uit `ebb-krab-echt-keuring-2.md`.
Script: `bron/krab_keuring2.py` (bouwt op werelden v3.2, verandert daar niets). Beelden: `keuring2/`.
GEZIEN met Read: `keuring2/overzicht-krab-260-2x-wit.png`, `keuring2/overzicht-krab-454-1x-wit.png`, `keuring2/omtrek-naast-elkaar-260-2x.png`.

## 1. De slipper is weg: de krab zit in een rood-witte zwemband

Toets met frisse kijkers (drie agents, elk alleen het 260-beeld, zonder uitleg, bestandsnamen zonder dierennaam):
- Oude krab met slipper: "ligt op een roze luchtbed/slipper (roze vorm met witte streep) ... twijfel voorwerp". Geen slipper in één blik, dus weg.
- Nieuwe krab met zwemband: "Krab, zit in een rood-witte zwemband, scharen omhoog. Zeker."

De zwemband is het bekendste strandding dat er is, hij dobbert vanzelf (past bij ademen op de golf), en onder water draagt de krab hem gewoon nog: dat is de grap (een krab die niet kan zwemmen). Het tweede slippertje links op de golf en het witte teenpaaltje zijn ook weg.

Gegevens voor Gijs (maten in 1/260 D, k = 1,48 op de ademschermen; op hold en menu k = held_maat / 30 × 1,3 × 0,8 × 1,05; op het eindscherm k = 1,1 × 0,8 × 1,05):
- Midden van de band: krabmidden x − 4, krabmidden y + 9 (dezelfde plek waar de hak van de slipper lag, 3 hoger).
- Ellips: rx 23 k, ry 8,5 k, buis 6,5 k dik (buiten rx + 3,25 k, binnen rx − 3,25 k).
- 16 stukken van 22,5 graden, om en om FF0000 en FFFFFF, beginnend rechts met rood.
- Achterhelft (de 8 stukken boven het midden) eerst, dan de krab, dan de voorhelft (8 stukken onder het midden). Zo zit hij er echt in.
- Onder de voorhelft een donkere rand AA0000, dezelfde vorm 2,2 k lager (dikte van de band).
- Glimlijntje wit, 1,4 px dik, op de voorhelft links van het midden (x −14 k tot −6 k, y 6,1 k tot 7,4 k).
- Kantelen: de band draait 0,4 × de hoek van de slipper mee (één plaatje, net als het dier).
- Kleuren zitten alle drie in de 64 MIP-kleuren.

Let op, mogelijke dubbeling: de clownvis heeft bij Calm ook een rood-witte band als piste. De frisse kijker zag bij de clownvis alleen "feesthoedje en drie ballonnen", de band viel niet op. Voorstel: bij de clownvis de band weglaten en alleen de jongleerballen houden, zodat de zwemband van de krab is. Keuze voor de hoofdchat.

## 2. Nacht: één kleurregel voor alle werelden

Bestand: `ebb-nachtregel-v1.json`. Teken het scherm met de nachtkleuren van v3.2 en zet daarna alles behalve tekst door de regel:
- **MIP:** elk kanaal een trede omlaag (00 en 55 worden 00, AA wordt 55, FF wordt AA), daarna groen nooit sterker dan rood of blauw. Zo blijft alles in de 64 kleuren. De tabel van 64 naar 64 staat in de json (`mip`). Voorbeelden: water 0000AA wordt 000055, krab FF5500 wordt AA0000, groene stipjes 55FFAA worden 005555.
- **AMOLED:** per kanaal v' = 0,7 × 255 × (v/255)², daarna dezelfde groenregel. Wit wordt 178 (gedempt grijs), 105 wordt 30, alles wat donker was wordt bijna zwart. Tabel in de json (`amoled_kanaal`).
- **Uitgezonderd:** alle tekst met haar donkere rand van 2 px, de paginastipjes en de randen van de keuzeknoppen in het menu.
- Je mag de regel ook op de kleurconstanten zelf toepassen in plaats van op pixels; dat geeft hetzelfde beeld.

Wat je ziet (GEZIEN, 454 en 260): water en lucht bijna zwart, golflijn en maan gedempt, sterren grijs en weinig, geen groen meer, krab donkerrood met een grijze band. De tekst is ongewijzigd en de achtergrond alleen donkerder, dus het contrast gaat overal omhoog ten opzichte van v3.2 (daar al minstens 4,5).
Klein punt voor Gijs: bij nacht op het eindscherm worden de lege paginastipjes te zwak als ze mee gaan door de regel; daarom horen ze bij de uitzondering.

## 3. Omtrek van de dieren op MIP: donker 1 pixel

Naast elkaar op 260 (`keuring2/omtrek-naast-elkaar-260-2x.png`, inademen, hold, eind, hold bij nacht): wit (nu), donker 1 px, geen.
- Wit: korrelige trapjes rond de scharen, knipplaatje. Bevestigd.
- Geen: het oranje loopt bij de scharen in de oranje-achtige vlakken en de poten verdwijnen tegen het zand.
- **Donker 1 px (000000, in 8 richtingen 1 px):** strak, de krab staat los van zee en zand, de poten blijven leesbaar. **Gekozen.**

Voor Gijs: alleen op MIP. In `teken()` de vier schuine stickerkopieën van 2 of 3 px in de randkleur vervangen door acht kopieën op 1 px (boven, onder, links, rechts en de vier schuine) in 000000; daarna het dier zelf. Geldt voor alle 25 dieren op MIP. AMOLED houdt voorlopig de witte rand (daar is hij zacht en oogt hij als sticker); als je het gelijk wilt trekken, mag donker ook op AMOLED, maar dat heb ik nog niet bekeken.

## Grap-toets voor de andere 24 (zelfde frisse kijkers, inademen dag 260)

Telt als grap (in één blik goed genoemd): vis in fles met kurk, garnaal op surfplank, zeester met telescoop, octopus in bad met eendje, zeehond met hengel en dobber, narwal met ijsje op zijn tand, zwaardvis met donut, manta met spandoek en hartje, haai met tandenborstel, orka met strik en muzieknootjes, kreeft met strohoed, gieter en bloempot, walvis met regenboog, zeekomkommer met slaapmuts en zzz, otter met schelp op zijn buik, kogelvis als ballon aan een touwtje, schildpad met meeuw, clownvis met hoedje en ballen, en nu de krab met zwemband.

Telt niet (open, volgende ronde):
- **Maanvis:** zonnebril niet gezien ("geen voorwerp"). Bril veel groter en zwart met een wit glimstreepje.
- **Reuzeninktvis:** bootje niet gezien. Derde keer zwak: nieuw idee nodig.
- **Rog:** "vlieger?", vliegende schotel leest niet.
- **Kwal:** paraplu niet gelezen, alleen het regenwolkje.
- Half: zeepaardje (paal gezien als kapperspaal, draaimolen niet), dolfijn (snorkel gezien, dier niet herkend), aal (lampje gezien, dier gelezen als krokodil), zeekomkommer en manta (grap gezien, dier niet zeker).
