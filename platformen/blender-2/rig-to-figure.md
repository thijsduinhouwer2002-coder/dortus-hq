# Click Joints Pro 1.1 "Rig to Figure": concurrentiecheck (Ruben, 16 nov 2026)

Opdracht: `berichten/ruben.md` (hoofdchat 16 nov 11:20). Vraag: kan iemand anders een gerigde of geposeerde figuur printbaar maken met gewrichten, mét eindstop en een bereik uit de rig? Bron: onderzoeker 16 nov, alle Superhive-pagina's, ratings en FAQ met curl gelezen; plus Gumroad, Blender Artists (JSON), extensions.blender.org, sites van webdiensten. YouTube niet bekeken. Alles GEZIEN tenzij anders.

## Besluit: JA, bouwen
Niemand leest een armature en bouwt daarna gewrichten met eindstop en een bereik uit de rig. Er komt ook niets aan dat openbaar te zien is. Twee producten zitten elk op de helft: Pose to Print leest de rig maar maakt één vast beeldje zonder gewrichten; Cut Flex heeft een gewricht per lichaamsdeel maar leest geen rig en heeft geen eindstop.

## De 5 dichtstbijzijnde
| Product | Leest rig | Eindstop / bereik | Prijs | Verkocht | Leeftijd |
|---|---|---|---|---|---|
| Cut Flex (TopoPen) | nee ("Whole-character rigging ... outside its scope", FAQ) | nee, alleen overlap per houding | $34,99, alleen Windows | 10+ | 26 dagen |
| Pose to Print (Meshwright) | ja (Mixamo, Rigify, VRoid) | geen gewrichten; 1.1 belooft pennen om apart te verven | $18 | 0 tot 9 | 14 dagen |
| Cleave (V4SS3UR) | nee, wel knippen op vorm (Meshy, Tripo) | nee, alleen kogel sinds 1.6 | $23 | 100+ | 2 mnd |
| ARTICULATOR (BOSSposes) | nee | nee | $1 | 30+ | 3 mnd |
| JointLab | nee | niet genoemd | $65 | 20+ | 4 mnd |

Ook gezien: LayerMechanic ($19, 0 tot 9, bouwt niets, controleert een scharnier over een bereik dat je zelf invult), SlicerJoint Pro (Gumroad $20, flexi langs een curve), Riggable en 3DAI Studio (webdiensten, kogels op vorm, DERDEN), PrintPal Flexi (gratis site), en zeven splitsers met pennen zonder rig.

## Wat hebben wij dat zij niet hebben
1. Scharnier met echte eindstop en bereik in graden (al in Pro 1.0, bij niemand anders gezien).
2. Speling per printer met een testkaartje (pasband). Cleave heeft vaste keuzes, de rest een schuifje.
3. Nieuw in 1.1: het bereik overnemen uit Limit Rotation in de rig, per bot het juiste gewricht. Niemand doet dat.

Wat zij hebben en wij nog niet: Cut Flex heeft al een gewrichtsoort per lichaamsdeel, Cleave vindt zelf knippunten bij nek, schouders, knieën.

## Betaalbewijs (klein, eerlijk)
- Cut Flex 10+ voor $34,99 in 26 dagen, alleen Windows (minstens ±$350). JointLab 20+ voor $65, ARTICULATOR 30+ voor $1.
- Koper van Dovetail Key (800+): "joints can rotate ... action figure ... Shoulder and hip, Ball-and-socket, Elbow and knee, Pin hinge".
- Klacht bij ARTICULATOR: meer gewrichtsoorten. Klacht bij JointLab: eigen server verplicht.
- Rig automatisch naar gewrichten heeft nog geen betaald voorbeeld: Pose to Print (leest rig, geen gewrichten) zit na 14 dagen op 0 tot 9. Dat is een risico (GOK).

## Plan 1.1 (in deze volgorde, elk stuk apart getest in Blender 4.2, 5.2 en 5.3)
1. **Figuurpresets** zonder rig: heup en schouder kogel, knie en elleboog scharnier met eindstop, enkel, nek; bereik in graden per preset, zelfde pasband. Dit is precies wat de Dovetail-koper vroeg, en het werkt ook voor AI-figuren zonder rig.
2. **Rig lezen:** per gekozen bot het snijvlak bij de botkop, het preset op naam (Mixamo, Rigify, Meshy-rig), en het bereik uit Limit Rotation als dat er staat (anders het preset). Alleen het lid snijden (bestaande `een_lid.py`).
3. **Toetsen zonder scherm:** per gewricht meten dat het onderdeel tot de eindstop draait en niet verder, en dat de delen nergens door elkaar gaan; op een Rigify-figuur, een Mixamo-figuur en de vier Meshy-figuren.
4. Winkeltekst alleen met wat getoetst is. Tweede lancering (Lars, verhaal 11) na goedkeuring van 1.0.1 en upload van 1.0.2.

Daan kijkt mee voor er gebouwd wordt (`berichten/daan.md`).
