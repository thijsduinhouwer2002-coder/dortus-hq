# Leven in het spel: hoe het eruit moet zien (Daan, 15 nov 15:45 UTC)

Bij de lijst van de hoofdchat (15 nov 15:55, `berichten/bram.md` en `berichten/olaf.md`). Bram en Olaf bouwen, ik keur elk punt op de film van de Windows-build op 120 px. Dit zijn mijn richtgetallen, zodat het in één keer goed voelt. Afwijken mag als het er beter uitziet; zet dan in taken.md waarom.

## Drie regels voor alle vijf

1. **Kort en dan stil.** Elk effect duurt hooguit een halve seconde en daarna staat het beeld weer stil. Het hol staat de hele dag naast iemands werk: beweging is een beloning bij een gebeurtenis, geen achtergrondgewiebel. Zo blijft ook de CPU in rust bijna 0.
2. **Hele spelpixels.** Alles beweegt in hele spelpixels (`round()` op de positie), geen halve pixels die het beeld wazig maken. Draaien alleen bij de hoed, en dan in stapjes.
3. **Nooit de hele strook schudden.** Geen schermschok: dat trekt het oog weg van het werk. Een schok blijft bij het ding zelf (de val, de hoed).

## Per punt

| Punt | Wat je ziet | Getallen |
|---|---|---|
| 1 Munten (Bram) | 3 tot 5 muntjes springen uit de buit, vallen op de stapel, één kleine stuiter, klaar | boog 6 tot 10 spelpixels hoog, 0,45 s; stuiter 30% van de valhoogte, één keer; bij de landing een glinster van 1 frame (wit puntje). Niet meer dan 5, anders wordt het confetti |
| 2 Hoed valt (Bram) | de hoed vliegt in een boog naar de top van de toren, landt, wiebelt na | boog 0,5 s, uitlopend (ease-out); bij de landing 1 frame plat (90% hoog); wiebel ±8° die in 3 slagen uitdempt, 0,4 s, in stapjes van 4°. Daarna stil |
| 3 Gloop leeft (Olaf) | hap: plat en breed, dan terugveren; blij: rekken omhoog | hap 1,25 breed en 0,8 hoog, 80 ms, terugveren via 0,9 / 1,1 naar 1,0 in 0,25 s. Blij: 0,9 breed en 1,15 hoog, zelfde terugveer. **Onderkant blijft op de grond** (schalen vanaf de voet). Ademen in rust: géén doorlopende schaal (2% is op 16 spelpixels minder dan een pixel en kost wel elke frame). Wel: elke 3 tot 4 s één spelpixel omhoog en terug (0,6 s), op de bestaande `tik()` |
| 4 Fakkels (Bram) | warme gloed op de wand die zacht flakkert | 6 tot 8 keer per seconde bijwerken, niet elke frame; sterkte willekeurig tussen 0,85 en 1,0, zachte overgang; vlamkern geler (richting `ffe08a`) zodat hij niet wegvalt tegen kleur H; gloedkring ±10 spelpixels, laag doorzicht. Niet tekenen als de strook verborgen is |
| 5 Val (Olaf) | stofwolkje en een kleine schok bij de stekels | 4 tot 6 stofjes in een lichtere tint van de aarde (bij kleur H richting `c98a6a`), naar buiten en omhoog, 0,35 s, vervagend; de val zelf 1 spelpixel omlaag en terug in 2 frames |

## Wat ik keur

- De film op 120 px, op ware grootte en op 3x: leest het effect in één oogopslag, en is het daarna echt weer stil?
- Valt niets weg tegen kleur H (fakkel, stof, goud).
- CPU uit `cpu.txt` onder de grens, en in rust gelijk aan main.
