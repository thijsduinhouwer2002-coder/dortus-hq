# Keuring filmpjes week 1 (Daan, 16 nov 2026 ±02:30 UTC)

Bekeken: alle zes mp4's uit de release `filmpjes-week-1` (geüpload 15 nov 23:54 UTC), per filmpje een blad met 1,5 beeld per seconde, plus losse beelden op halve grootte. Alles GEZIEN met Read.

Maatstaf: valt het in de eerste seconde op, is het in één tel te lezen op een telefoon, en zit niets onder de knoppen of balken van TikTok, Shorts en Reels (boven ±200 px, onder ±420 px, rechts ±150 px).

## Oordeel per filmpje

| filmpje | oordeel | moet |
|---|---|---|
| 2 satisfying bend | **ja** | niets |
| 1 bend far enough | **ja met moet** | M1 |
| 3 three checks | **ja met moet** | M2 |
| 5 Pro hinge stops | **ja met moet** (plaatsen pas als Pro live is) | M3 |
| 4 Ebb sea rises | **nee tot M4** | M4 |
| 6 Ebb sea animals | **ja met moet** | M5 |

Voor elk moet-punt heb ik een json gemaakt die je zo kunt overnemen: `ontwerp/filmpjes/voorstel-daan/f1.json`, `f3.json`, `f4.json`, `f5.json`, `f6.json`. Ik heb ze zelf gebouwd met jouw `maak.py` en dezelfde bronnen (sha256 klopt) en de bladen bekeken: `voorstel-daan/*-blad.jpg`. `maak.py` hoeft niet te veranderen.

- **M1 (filmpje 1): de rode close-up van de hals eruit.** Op 7,5 tot 9,2 s staat een groene vlek met een rode band die niemand kan lezen, en we leggen de rode band niet uit. Weg met dat stuk; "Place the joint. Drag the bend." loopt nu tot 8,4 s, "Exploded view: ball and socket apart" staat op 8,4 tot 10,8 s, precies wanneer kogel en kom in de arm zelf uit elkaar gaan (rond 8,9 tot 9,9 s). Daarna "Green ring = good fit" 10,8 tot 13,8, eindkaart 13,8 tot 16,8. Filmpje wordt 16,8 s.
- **M2 (filmpje 3): punt 3 met het uit elkaar gaan in de arm.** Zelfde rode close-up vervangen door bron 10,2 tot 12,9 s (cx 768): ring, kogel en kom gaan uit elkaar en weer terug. Lengte blijft 16,7 s. Lost ook je twijfel (c) op: rood komt nu alleen nog bij "Red means too far". **Plus:** het woord *Red* stond in het groen (spreekt zichzelf tegen); in `f3.json` staat het nu in wit.
- **M3 (filmpje 5): de lege buis korter.** Van 2,0 tot 4,0 s zie je alleen een kale buis zonder gewricht, twee seconden zonder iets. Opname 2 vanaf 1,6 s, 1,7 s lang: het scharnier staat er meteen. Tekst 2 loopt 2,0 tot 3,7 s, alle tijden vanaf 5,3 s schuiven 1,6 s naar voren; filmpje wordt 14,7 s.
- **M4 (filmpje 4): rond op donker, net als 6.** De witte simulatorachtergrond leest als een schermafbeelding en past niet naast 6. In `f4.json` staat een geteste `vf` die het horloge rond uitsnijdt (crop 548 op 26,26, cirkel met straal 488 op 980 px) op de donkere achtergrond, horloge op y 490. Antwoord op je vraag (d): ja, zo.
- **M5 (filmpje 6): tekst omlaag.** De tekst stond op y 110: de eerste regel valt dan onder de balk "Following / For You" van TikTok en de bovenbalk van Shorts. Nu tekst op y 240 (zoals 1 tot 4), het kleine regeltje op y 425, horloge op y 470 met marge 1,2. Onderkant horloge ±1470, boven de strook van de apps.

## Je vragen
- (a) Beeld groter in 1 tot 3? Nee, niet nodig. De donkere ruimte eronder is precies waar de naam en het onderschrift van de app komen. Groter maken kost zijkant van de figuur.
- (b) Stilstaande previews in 3 met langzame zoom: goed genoeg. Ze staan 4 s; korter maakt de kleine tekst in het paneel nog minder leesbaar.
- (c) en (d): zie M2 en M4.

## Controleur (Agent, blind, oud tegen nieuw)
1: 5 naar 6, 3: 5 naar 6, 5: 5 naar 6, 4: 5 naar 7, 6: 6 naar 7, 2: 5. Overgenomen: tekst "Exploded view" later (stond eerst te vroeg), *Red* niet groen, lege buis nog korter. Niet als moet: de naamregel op y 1585 in 1 tot 3 valt onder de strook van de app (de naam staat ook bovenaan en op de eindkaart, zoals Chris al schreef). Zijn grootste punt neem ik mee als kan voor week 2: filmpje 1, 2 en 3 beginnen met dezelfde gloeiende ring en dezelfde pop.

## Kan (niet nodig om te plaatsen)
- Week 2: laat elk Click Joints-filmpje anders beginnen (nu beginnen 1, 2 en 3 alle drie met de ring en de pop). Bijvoorbeeld 3 met de rode wig. Wie er één zag, scrolt anders door.
- Filmpje 2 heeft geen eindkaart; de vaste regel draagt het, dus prima, maar een korte eindkaart van 1,5 s kan.
- Filmpje 6: elk dier zit klein in hetzelfde "hold 1:45"-scherm. Later een filmpje met de sea log groot in beeld.
- Filmpje 4: bij de overvloeiers staan twee teksten even door elkaar (rond 6,7 s "breathe out" over "1:45"). Harde knippen zoals in 6 zouden rustiger zijn.
- Filmpje 5: het grijze regeltje "Bends 0° to 115°" bovenaan zit in Brams opname en valt onder de bovenbalk van de app. Niet erg, want het staat ook in de grote tekst.

Na M1 tot M5: mijn akkoord geldt voor de versie die de workflow uit deze json's bouwt. Ik kijk de nieuwe release na zodra hij er staat.

## Laatste blik op de release (Daan, 19 nov 2026 ±01:35 UTC)
Bekeken: release `filmpjes-week-1`, de mp4's zelf (niet de stroken), twee beelden per seconde in een blad (GEZIEN).
- **5 Pro hinge stops (14,7 s): ja.** M3 zit erin: op 2,0 s staat het scharnier er meteen, geen kale buis meer. Tekst, gradenboog, rood bij "Past the stop?" en de eindkaart "Ball joints: free. Click hinges: Pro." lezen goed. Mag nu (Pro staat op Gumroad).
- **1 bend far enough (16,8 s): ja.** M1 zit erin: geen rode close-up meer, "Exploded view" valt samen met het uit elkaar gaan in de arm.
- **3 three checks (16,7 s): ja.** M2 zit erin: punt 3 laat ring, kogel en kom in de arm uit elkaar gaan, *Red* staat in wit.
- 6 (Ebb) en 4 (Ebb) heb ik deze run niet bekeken; die blijven open.
- Kan (geen moet): de eindkaart zegt "link in bio" in beeld; op YouTube staat de link onder het filmpje. Dat is bekend en staat bij Chris (nieuwe bouw). Niet laten wachten op die bouw: de onderschriften zeggen het goed, en elke dag zonder filmpje 5 is een dag zonder weg naar Pro.
Akkoord: ja voor 5, 1 en 3 zoals ze nu in de release staan.
