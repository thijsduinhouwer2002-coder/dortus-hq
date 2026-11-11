# Ebb blad v6 (stand v6.2): de 12 moet-punten van de keuring van v5 (Mila, 11 nov run 24)

**Blad:** `ontwerp/garmin/ebb-blad-v6.png` (22 schermen, per scherm links 454 px AMOLED, rechts 260 px MIP op ware grootte).
**Naast elkaar:** `blad6/vier-holds-454.png` en `blad6/vier-holds-260.png` (0:30, 1:45, 2:30, 3:04).
**Dieren:** `ontwerp/garmin/ebb-dieren-v6.png` (alle 25 op 260, boven gevonden, onder als silhouet). Losse beelden en meting in `blad6/` (`meting-v6.txt`). Bron: `bron/ebb_blad_v6.py` en `bron/ebb_dieren_v6.py` (bouwen op v5; alleen wat verandert staat erin).
**Stand:** nog niet bouwen en nog niet naar Thijs. Twee frisse beoordelaars gaven allebei een 7 (op v6.0 en v6.1). De lat is 8. Hun punten die ik nog niet deed staan onderaan.

## Afvinklijst moet-punten (keuring v5 door drie beoordelaars)
- [ja] 1. Geen koppeling inhoudtijd en dier: 6b (met Starfish) heeft 1:10, 1:25, 1:40; 6c (geen dier) heeft 1:20, 1:45, 3:04. De inhoudschermen 3a tot 3c horen bij de avondsessie van 6c.
- [ja] 2. Today: zes staande staven in één egale tint (W1), geen trechters, geen "deeper = longer", langste zonder nadruk. Onderregel "6 holds · avg 1:44" (nagerekend: 624 s / 6).
- [ja] 3. 3c: trilteken als twee gespiegelde gele boogjes om "time to breathe". Op 3a, 3b, 3d en 3c staat "press START to breathe".
- [ja] 4. "breathe in" (2), "3 rounds · 30 breaths" (1b), menu alleen "Rounds", 9b "Sound off". De "s" is op 260 13 tot 15 px.
- [ja] 5. Zee elke 30 s een stap donkerder tot 2:30, daarna gelijk. Vanaf 2:00 geen lichtstralen, vanaf 2:30 geen belletjes en alleen 000055 met de dunne schuimrand. 3d (2:30) en 3c (3:04) hebben precies dezelfde zee; het seintje is tekst, trilteken en buzz.
- [ja] 6. Niet gevonden: één egaal vlak 0000AA met alleen een buitenrand 0055FF (geen binnenlijnen, geen ogen), met het nummer erop. Ook op 6c. Bonus heeft "+".
- [ja] 7. Manta AAAAAA, reuzeninktvis AA55FF, zeeotter FFAA55, orka met lichte rand van 2 px, kreeft nu FF5555 met rand FFAAAA.
- [deels] 8. Walvis blauw met fontein en 1,3 keer groter; narwal wit met vlekken, ronde kop, rechte slagtand, geen rugvin; reuzeninktvis 1,25 keer en paars; zeekomkommer zonder mutsje; zeeotter op zijn rug met schelp en voeten omhoog; zeehond liggend met voorflipper, staartflippers en witte snor. Nog niet opnieuw: dolfijn tegenover haai (beoordelaar 2 vond ze wel verschillend, 1 niet).
- [ja] 9. 8 weeks: grafiek 54 px hoger (nu y -7,5 px), lege weken als lichtblauwe stip op de lijn, getallen 13 tot 14 px.
- [ja] 10. Ster 0,145 D (v5 0,222), helemaal onder water, ±15 px tot de tekst, stralenkrans weg. Golf iets hoger (0,32 D) zodat het past.
- [deels] 11. 3b schildpad recht, belletjes links en rechts. Sea log: ring dunner, halve laatste rij in het midden, naam en eis op twee regels. Kader 8 en 8d nog -4,5 en +5,5 px (door slagtand en voelsprieten), zwaartepunt binnen 2,7 px.
- [ja] 12. Menu: twee gelijke pillen, selectie = dikke schuimrand. Schildpad helemaal onder de golf.

**Besluiten hoofdchat 11 nov 00:55:** zee (ja, zie 5) en reeks: zeekomkommer is bonus nr. 25. Omdat 24 van 24 dan zonder hem moet, vult de Lobster (al getekend in v4) nr. 23 op 46 sessies; Whale blijft nr. 24 op 50. Sea log "7 of 24", blad 3 heeft 19 tot 24 plus de bonus.

## Gemeten (`blad6/meting-v6.txt`, Python)
- Kader binnen 0,5 px op alle schermen behalve sea log 8 (-4,5), 8b (-2,0), 8d (+5,5). Zwaartepunt op 260 overal binnen 3,4 px (8 weeks +3,4 door de staven rechts: eerlijke data van een nieuwe gebruiker).
- Tekst binnen 0,80 van de straal op alle 22 schermen op 260 (golfschuim telt niet mee).
- 0 pixels buiten de 64 MIP-kleuren. Kleinste letter 20 px op 260.

## Nog open (frisse keuring v6.1, cijfer 7)
1. "Clipart": de grote ogen op ster en sea log; de sea log met felle dieren naast blauwe genummerde silhouetten. Idee: silhouetten rustiger (000055 met rand 0000AA) en nummer kleiner.
2. "Kaal": today en 8 weeks met de data van een nieuwe gebruiker (6 stippen, 2 staven). Idee: water of diepte in het vlak zonder nadruk op de langste.
3. Teksten: "found: 3 days in a row" wordt "found after 3 days in a row"; "swims with you" duidelijker; twee buzz-regels in 9 en 9b uit elkaar; tempo gelijk aan de code (G2 van Gijs).
4. Sea log op celmidden centreren in plaats van op tekenranden.
