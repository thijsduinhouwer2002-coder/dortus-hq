# Balans-simulatie Het Hol: uitkomst (Bram, 9 nov 2026)

## 16 nov 2026 ±17:35 UTC (Bram): de speler die niet meteen koopt (voortgang.md "Wat nog niet klopt" punt 5)
Uitvoer `voortgang-kijken-uitkomst.txt` (8 zaden, GEZIEN), script `voortgang_kijken.py`, nieuwe sleutel `"koop_elke_s"` in `sim.py` (de speler kijkt hooguit elke X open seconden in de winkel, en altijd meteen als hij het spel weer opent). Spec versie 3 definitief met de eigen helden en hun tegenzet. Zonder de sleutel verandert er niets (nagekeken: `voortgang-v3-eind-uitkomst.txt` byte voor byte gelijk).

| speler (6 uur open per werkdag) | hol 20 / 30 / 40 / 50 (open uur) | hol 50 | goud op de bank (mediaan) |
|---|---|---|---|
| koopt meteen (de sim tot nu) | 10,5 / 37,7 / 76,0 / 127,9 | werkdag 22 | 1.001 |
| kijkt elke 10 min | 10,5 / 37,2 / 75,6 / 127,4 | werkdag 22 | 1.068 |
| kijkt elke 30 min | 10,5 / 37,3 / 75,3 / 127,0 | werkdag 22 | 1.433 |
| kijkt elk uur | 10,4 / 37,2 / 74,6 / 126,5 | werkdag 22 | 1.957 |
| kijkt elke 2 uur | 10,4 / 37,6 / 75,7 / 127,4 | werkdag 22 | 2.551 |
| kijkt alleen bij het openen (1 x per dag) | 11,3 / 41,6 / 78,0 / 132,0 | werkdag 23 | 4.432 |

Tussendoor-speler (15 / 30 / 60 min per dag, kijkt alleen bij het openen): hol 50 op dag 63 / 57 / 50, tegen 63 / 58 / 49 als hij meteen koopt.

**Wat dit zegt:** (1) **later kopen maakt het spel bijna niet langzamer.** Tot "elke 2 uur kijken" blijft hol 50 op werkdag 22; zelfs wie maar één keer per dag koopt, is één werkdag later. Het hol-niveau komt van vangen, en een gang die al 80% vangt wordt van één val meer niet veel beter. De zorg in punt 5 ("een echte speler klikt minder, dus langzamer") klopt dus nauwelijks; de tabel in echte dagen kan blijven. (2) **Wat wel verandert is de berg goud:** wie elke 2 uur kijkt heeft er ±2.500 liggen, wie 1 x per dag kijkt ±4.400. Dat is precies waar de doelregel en het bordje voor zijn: laat zien wat er te koop is, dan klikt de speler vanzelf vaker. (3) De gaten van wie 1 x per dag koopt zijn natuurlijk een werkdag (de aankopen vallen dan allemaal op het openen); de hol-niveaus lopen gewoon door.


## 16 nov 2026 ±17:20 UTC (Bram): de eigen helden per laag met hun tegenzet nagerekend (vraag Sanne 17:00)
Uitvoer `voortgang-laaghelden-uitkomst.txt` (8 zaden, GEZIEN; ook 16 zaden voor de krapste punten), script `voortgang_laaghelden.py` (`ijk` geeft de varianten), spec versie 3 definitief plus de nieuwe sleutel `"laag_helden"` in `sim.py`. Zonder de sleutel verandert er niets (nagekeken: `voortgang-v3-eind-uitkomst.txt` komt byte voor byte terug).

**Hoe het in de sim zit:** mijnwerker (vanaf hol 21, laag 2+, gewicht 20) slaat de eerste val die hij tegenkomt over (kans 0, geen klap), slijm x 1,2; met het valluik valt hij daar met kans 0,8. Ontdekker (hol 31, laag 3+, gewicht 15): eerste bezoek put x 1,2, als terugkomer x 0,3 op elke val die hem eerder raakte. Nep-schat: wie de echte schat zou halen, valt erin met 0,75 (ontdekker), 0,5 (hebzuchtig) of 0,3 (schijterig). Heks (hol 36, laag 3+, gewicht 10) x 1. Hoedenjager (hol 41, laag 4, gewicht 15) alle vallen x 0,7, met de lokker de eerste val x 2 (hooguit 0,95). Gekroonde niet (telt niet mee). **Aannames die niet in jouw tekst staan:** een tegenzet koop je één keer voor ±1 uur goud en hij zit daarna in elke nieuwe laag; het valluik vangt alleen de mijnwerker (gewone helden lopen eroverheen). Vangkans = gevangen gedeeld door alle helden in de laag die je ziet.

| | laag 2 heel | laag 3 heel | laag 4 heel | hol 21 (held, nog geen valluik) | hol 31 (held, nog geen nep-schat) | hol 30 / 40 / 50 (open uur) | hol 50 | langste gat week 4 (mediaan / ergste) |
|---|---|---|---|---|---|---|---|---|
| versie 3 | 0,808 | 0,813 | 0,891 | 0,534 | 0,591 | 37,4 / 76,2 / 127,8 | werkdag 22 | 2,8 / 3,2 |
| helden zonder tegenzet | x 1,00 | x 0,99 | x 0,99 | x 0,92 | x 0,93 | 37,8 / 76,8 / 129,2 | werkdag 22 | 2,9 / 5,8 |
| **jouw getallen (0,8 / 0,75-0,5-0,3 / x 2)** | **x 1,01** | **x 1,03** | **x 1,02** | **x 0,92** (16 zaden x 0,94) | x 1,06 (16 zaden x 1,08) | 37,7 / 76,0 / 127,9 | werkdag 22 | 2,8 / 5,4 |

**Wat dit zegt:**
1. **Jouw getallen kloppen, ik verander niets.** Per laag x 1,01 / 1,03 / 1,02, binnen de band x 1,0 tot 1,05. Hol 50 blijft op werkdag 22 (127,9 tegen 127,8 open uur).
2. **Het krapste punt is hol 21, en dat ligt aan de held, niet aan de tegenzet:** x 0,92 (8 zaden) tot x 0,94 (16 zaden), net onder de ±0,95, ±2,3 open uur lang. Daar is laag 2 net gekocht en heeft hij maar Gloop en één put; slaat de mijnwerker er één over, dan blijft er weinig. Een sterker valluik helpt hier niet, want het is er nog niet. Wil je het toch boven 0,95: zet het valluik op hetzelfde niveau als de mijnwerker (zoals de lokker op 41), dan wordt hol 21 x 1,07 (proef 8 zaden). Mijn advies: zo laten, het kost niets aan de voortgang en het is precies het raadsel dat je wilde.
3. **Hol 31 gaat omhoog (x 1,06), niet omlaag:** het valluik vangt ook de mijnwerkers in laag 3 al, en de ontdekker komt in zijn eerste bezoek gewoon x 1. Hij wordt pas lastig als terugkomer, en dan staat de nep-schat er al.
4. **Zonder tegenzet gebeurt er per laag bijna niets** (x 0,99 tot 1,00): in een gang met 6 tot 8 vallen maakt één overgeslagen val weinig uit. De tegenzet is dus vooral voor het gevoel ("ik heb hem door"), wat goed is: hij kan niet stuk.
5. **Prijs van de tegenzet:** met de koopregel "steeds het goedkoopste" koopt de sim het valluik pas ±5 open uur na hol 22 (19,6 u), de nep-schat op ±48 u, de lokker op ±90 u. Bij 0,25 / 0,5 / 2 uur goud blijven de lagen x 1,01 tot 1,03 en hol 50 op werkdag 22. Het ergste gat in week 4 springt bij elke variant tussen 4,1 en 5,9 uur (bij versie 3 3,2): dat is hetzelfde schuiven van aankopen als bij de gevoeligheid van 16:45, de mediaan blijft 2,8 tot 3,8. Lokker weglaten maakt laag 4 x 1,01 in plaats van 1,02; hij mag dus blijven of weg, voor de balans maakt het niet uit.
6. **Opbrengst van de eigen helden:** mijnwerker gevangen 81% zonder en 95% met valluik; hoedenjager 81% zonder en 91% met lokker; ontdekker 87% (de nep-schat vangt hem meestal pas als terugkomer).


## 16 nov 2026 ±16:30 UTC (Bram): de tussendoor-speler, elke dag kort open (met en zonder rij)
Uitvoer `voortgang-tussendoor-uitkomst.txt` (8 zaden, 80 dagen, GEZIEN), script `voortgang_tussendoor.py`, spec versie 3 definitief. Elke dag M minuten open, de rest dicht (12 u x 0,25 = 3 u tempo erbij), ook in het weekend; dag n = de n-de keer open.

| per dag open | hol 12 | hol 20 | hol 30 | hol 40 | hol 50 | langste rij |
|---|---|---|---|---|---|---|
| 15 min | dag 2 | dag 6 | dag 20 | dag 38 | **dag 63** | 5 (alleen dag 2) |
| 30 min | dag 2 | dag 5 | dag 18 | dag 35 | **dag 57** (58 met rij) | 4 (alleen dag 2) |
| 60 min | dag 2 | dag 5 | dag 15 | dag 30 | **dag 49** | 1 (alleen dag 2) |

Twee dingen: (1) **voor wie het spel tussendoor speelt is het hol pas na 7 tot 9 weken af**, want de nachten dragen het (3 uur tempo per dag tegen 15 tot 60 minuten open). Dat is het "diep voor weken" dat Thijs misschien wil (`voortgang.md` "Wat nog niet klopt" punt 4): wie werkt met het spel 6 uur open is in ±4,5 werkweek klaar, wie het tussendoor even opent na ±2 maanden. (2) **De rij merk je alleen op dag 2** (de eerste terugkomst), daarna nooit meer, en hij stapelt niet op: elke dag is hij leeg voor je weer dichtdoet.


## 16 nov 2026 ±16:45 UTC (Bram): hoeveel mogen de eigen helden per laag kosten? (voortgang.md "Wat nog niet klopt" punt 2)
Uitvoer `voortgang-laagvang-uitkomst.txt` (8 zaden, GEZIEN), script `voortgang_laagvang.py`. Mijnwerker en archeoloog zijn nog niet uitgewerkt (hoe vaak ze komen, hoe goed valluik en nep-schat ertegen werken), dus geen GOK-model maar een gevoeligheid: nieuwe sleutel `"laag_vang": [1, f2, f3, f4]` in `sim.py`, de vangkans in de laag die je ziet x die factor. Zonder de sleutel verandert er niets (`voortgang-v3-eind-uitkomst.txt` komt byte voor byte terug).

| vangkans laag 2 tot 4 | hol 30 / 40 / 50 (open uur) | hol 50 op werkdag | langste gat week 2 / 3 / 4 (mediaan / ergste) |
|---|---|---|---|
| x 1 (versie 3 definitief) | 37,4 / 76,2 / 127,8 | 22 | 1,9/3,7; 2,7/2,9; 2,8/3,2 |
| x 1,1 (tegenzet wint) | 36,5 / 73,3 / 125,9 | 21 | 1,9/2,6; 2,6/2,8; 5,6/6,0 |
| x 0,9 | 39,1 / 78,6 / 135,8 | 23 | 3,1/4,2; 2,8/3,1; 4,4/5,7 |
| laag 2 x 0,9, laag 3 en 4 x 0,8 | 39,1 / 80,1 / 138,0 | 24 | 3,1/4,2; 3,0/3,1; 2,9/5,3 |
| x 0,8 | 40,6 / 81,2 / 138,3 | 24 | 3,0/4,0; 3,0/5,1; 3,0/4,3 |
| x 0,7 | 41,8 / 84,0 / 145,2 | 25 | 2,7/2,9; 3,0/3,7; 2,8/3,1 |

**Wat dit zegt:** (1) de hol-tijden zijn niet erg gevoelig: 10% minder vangen in laag 2 tot 4 kost ±1 werkdag tot hol 50, 20% ±2, 30% ±3 (helden die vluchten komen terug en worden later alsnog gevangen). (2) De gaten springen wel: al bij x 0,9 of x 1,1 komt er in week 2 of 4 een gat van 4 tot 6 uur (ergste), omdat aankopen en niveaus anders op elkaar vallen. Week 1 en hol 20 veranderen nergens (laag 2 opent pas op hol 20). (3) **Voorstel voor als mijnwerker en archeoloog ontworpen worden:** laat elke held zijn eigen tegenzet hebben die hem ongeveer even vaak terug vangt (valluik voor de mijnwerker, nep-schat voor de archeoloog), dan blijft het netto tussen x 0,95 en x 1,05 en kloppen de bouwgetallen. Wordt het netto lager, dan de drempels 21 tot 50 opnieuw ijken met `sim.ijken` (één run, zoals bij versie 3), niet de prijzen.


## 16 nov 2026 ±16:35 UTC (Bram): de rij bij de ingang in de sim (vraag Sanne 16:00)
Uitvoer `voortgang-rij-uitkomst.txt` (8 zaden, GEZIEN), script `voortgang_rij.py`, spec `voortgang-v3-eind-bram.json` (versie 3 definitief) met `"rij": {"meteen": 4, "elke_s": 180}`. Oude uitkomsten veranderen niet (nagekeken: `voortgang-v3-eind-uitkomst.txt` komt byte voor byte terug).

**Hoe de rij in `sim.py` zit:** na elke keer weg mag het hol hooguit 4 niveaus boven het niveau van vóór de nacht komen (hol 1 is de start, dus na een eerste nacht hooguit hol 5); elke 3 minuten open tijd daarna mag er één bij. Eigen faam die de rij inhaalt: een niveau komt meteen als de gevangen helden zonder het weg-deel dat nog in de rij zit de drempel halen. Is alles wat verdiend is getoond, dan is de rij weg. De sim kijkt na elke held (±40 tot 60 s), dus een niveau uit de rij valt tot ±1 held na zijn 3 minuten. Nieuw in de `weg`-spec: `keer` (hooguit zoveel nachten, voor deze proef 1) en `leeg_gevallen_s` (0 minuten gespeeld: tempo zoals `voortgang.gd`, 1 held per 47,5 s en 60% gevangen, geen goud).

**1. Eerste keer X minuten spelen, dan één nacht weg (12 u x 0,25), mediaan van 8 zaden:**

| gespeeld | hol meteen na de nacht | niveaus in de rij | open minuten na de nacht tot hol 12 | open minuten tot de rij leeg is | zonder rij |
|---|---|---|---|---|---|
| 0 min | 5 | 8 | **21,6** | 24,3 | hol 12 meteen |
| 1 min | 5 | 9 | **21,2** | 27,3 | hol 12 meteen |
| 5 min | 6 | 7 | **18,3** | 21,4 | hol 12 meteen |
| 15 min | 9 | 5 | **9,8** (ergste 15,8) | 15,3 | hol 12 meteen (ergste 5,4 min) |
| 60 min | 13 | 1 (0 tot 1) | **0** (hol 12 zit bij de 4 meteen) | 3,3 | hol 12 meteen |

Dus: wie kort speelt en de volgende dag terugkomt, ziet hol 5 tot 12 in ±20 minuten, elk niveau met zijn eigen feestje, in plaats van in 12 seconden. Na 1 minuut spelen is de rij na ±27 minuten leeg (hol 14), iets sneller dan de ±35 minuten in Sannes tekst; de 4 meteen tellen vanaf hol 1, en na hol 12 haalt de eigen faam de rij al snel in.

**2. Week 1 tot 5: de rij verandert niets** (zoals Sanne verwachtte). Met en zonder rij precies dezelfde uitkomst: hol 12 / 20 / 30 / 40 / 50 op 2,0 / 10,5 / 37,4 / 76,2 / 127,8 open uur, langste gat per week 1,7 / 1,9; 1,9 / 3,7; 2,7 / 2,9; 2,8 / 3,2; 6,0 / 6,0 (mediaan / ergste). In geen van de 192 nachten (8 zaden, week 1 tot 5) stond er iets in de rij: een nacht na een werkdag van 6 uur geeft in de sim hooguit **1** hol-niveau, want vanaf ±6 uur open liggen de niveaus verder uit elkaar dan de 3 uur tempo van een nacht.

**Voor Olaf (code):** de rij grijpt dus alleen in bij korte eerste sessies (onder ±1 uur gespeeld). Een toets in het spel zou kunnen zijn: vers hol, 0 minuten spelen, 12 uur weg: hol 5 en "8 more levels wait at the door." (de sim zegt 8 als de nacht ±135 gevangen geeft; ±227 helden x 60%).



## 16 nov 2026 ±15:50 UTC (Bram): voortgang versie 3, laatste run (vraag Sanne 14:50)
Uitvoer `voortgang-v3-eind-uitkomst.txt` (8 zaden, 165 open uur, GEZIEN), spec `voortgang-v3-eind-bram.json`, opnieuw draaien: `python3 voortgang_v3_eind.py`. Zelfde werkdagen als versie 3 (6 uur open, weg x 0,25, plafond 12 u). Oude uitkomsten veranderen niet (nagekeken met `diff`, `voortgang-v3-uitkomst.txt` en de json komen byte voor byte terug).

**(2) Het eind, zoals afgesproken:** kamertje 4 en 5 van laag 4 pas vrij op hol 47 en 49 (`decor.laatste_op_hol` in `sim.py`, prijs uit het goud per uur van dat moment), geen stap 7.

**(1) Gat hol 38 naar 39: alleen drempels verschuiven lost het niet op.** Hol 35 tot 40 liggen al ±4 open uur uit elkaar en tussen ±55 en 75 u viel er niets te kopen (bank bij het luik naar laag 4 was 8.241 goud). Het gat was dus één hol-niveau lang, hoe je de drempels ook verdeelt; met hol 40 later (77, 79, 81 u) werd het zelfs langer (tot 4 tot 6 u). Wat wel werkt, en wat er nu in zit:
- **De kamertjes van laag 3 vrij zodra laag 3 gebouwd is** (±56 u), niet pas bij het luik naar laag 4 (`decor.vrij_gebouwd: [3]`). Dan koop je ze verspreid tussen hol 36 en 40, en heb je bij het luik geen berg goud meer.
- **Stap 4 tot 6 in laag 3 x 1,85 in plaats van x 2,0** (stap 6 was met 3.200 de duurste aankoop van het spel, 3,2 u sparen; nu 2.960).
- **Hol 36 tot 40 gelijk verdeeld tot 76 open uur** (drempels 11.884 / 13.345 / 14.823 / 15.668 / 17.131, waren 11.804 / 13.209 / 14.710 / 15.588 / 17.042): 36 op 60,0 u, 37 op 64,0, 38 op 68,2, 39 op 72,0, 40 op 76,2 (was 75,8).

| langste gat (open uren), mediaan / ergste van 8 zaden | versie 3 | **eind** |
|---|---|---|
| week 1 | 1,7 / 1,9 | 1,7 / 1,9 |
| week 2 | 2,0 / 3,7 | 1,9 / 3,7 (2 zaden wachten bij 36 tot 40 u op hol 30 voor het luik naar laag 3) |
| week 3 (hol 36 tot 40) | 4,2 / 5,1 | **2,7 / 2,9** |
| week 4 | 2,8 / 2,9 | 2,8 / 3,2 |
| week 5 (hol 48 tot 50) | 6,0 / 6,0 | 6,0 / 6,0 |

**Eerlijk: onder 2,5 u kom ik in week 3 niet.** Wat er nog over is, is sparen voor de duurste dingen van laag 3 (kamertje 5, stap 6, het luik: elk 2,5 tot 3 u goud), niet meer wachten zonder iets te doen. Goedkoper maken heb ik geprobeerd (kamertjes 1,0 tot 2,2 u, stap 4 tot 6 x 1,6, luik 2.000 of 2.400): dan schuift het gat naar week 4 en wordt het daar 4 tot 6 u. Week 5 blijft 6 u: dat is de afstand hol 48 naar 49 en 49 naar 50, en dan is alles gekocht. In dagen is dat één nieuw hol-niveau per werkdag.

**Hol 40: 76,2 open uur = werkdag 13 (week 3 dag 3). Hol 50: 127,8 open uur = werkdag 22 (week 5 dag 2).** Laag 2 / 3 / 4 open op werkdag 3 / 7 / 13, per week 42 / 15 / 13 / 8 / 4 niveaus, zelfde als versie 3.

**Extra: de eerste nacht weg tilt het hol al na 1 minuut spelen tot 12 of hoger** (8 van 8 zaden, mediaan hol 16; na 5 tot 60 minuten hol 13 tot 14). Twee oorzaken: (a) een nacht geeft 12 x 0,25 = 3 uur tempo, en hol 12 valt op 2,0 open uur, dus elke eerste nacht is genoeg; (b) met minder dan een uur gespeeld rekent het tempo met de eerste minuten door, en dan komen er veel helden snel achter elkaar (in de sim telt minstens 60 s). Dat past bij wat Olaf na 90 s zag. Voorstel (keuze voor Sanne en Olaf): **weg geeft hooguit zoveel als je die dag zelf open had** (eerste dag 20 min gespeeld, dan levert de nacht hooguit 20 min op), of het tempo pas meten na 10 minuten spelen. Dan blijft de demo (hol 12 rond 2 uur) zoals hij is. **Aanvulling 15:35 UTC:** in het spel zelf (Olafs `systemen/voortgang.gd` op tak `claude/steam-hol-weg`) hangt het niet eens van de speeltijd af: helden = 12 u x 0,25 / 47,5 s = ±227, met ±60% vangen ±135 gevangen, en hol 12 is 88. Dus ook na 0 minuten spelen tilt de eerste nacht het hol tot 12 of 13. Sanne besloot 14:50 (`berichten/olaf.md`) dat dat mag, als één optocht; dan hoeft er niets te veranderen en is het voorstel hierboven alleen nodig als jullie de demo-lijn van ±2 uur toch willen bewaren.


## 16 nov 2026 ±14:20 UTC (Bram): voortgang versie 3 nagerekend, met weg in echte dagen
Vraag Sanne 14:05. Volledige uitvoer: `voortgang-v3-uitkomst.txt` (8 zaden, 165 open uur, GEZIEN), spec `voortgang-v3-bram.json`, het commando staat bovenaan de uitvoer.

**Wat nu echt in `sim.py` zit** (alles uit zonder de sleutel in de spec, oude uitkomsten blijven gelijk; nagekeken: `voortgang-lagen-uitkomst.txt` komt byte voor byte terug):
- `laag_factor_hoog`: eigen prijsfactor per laag voor upgrade stap 4 tot 6 (Sannes diff).
- `decor`: kamertjes per laag, niet meer aan een hol-niveau. Die van laag n komen vrij als het luik naar laag n+1 gekocht is (laag 1 dus na het luik naar laag 2), die van laag 4 als laag 4 gebouwd is. Prijs = uren goud x het goud per uur op dat moment, één getal of oplopend per kamertje.
- `weg`: echte werkdagen. Na elke 6 uur open is het spel dicht (nacht of weekend, allebei langer dan het plafond van 12 uur) en levert het 12 x 0,25 = 3 uur van het tempo van het laatste open uur op: goud, gevangen helden (faam, telt voor hol-niveau) en hoeden. Het weg-goud telt niet mee in het tempo zelf, anders groeit het vanzelf door.
- `UREN`, `REK`, `DINGEN`, `GPU`, `HOOG`, `DECOR`, `WEG` in `voortgang_lagen.py` (uitleg bovenaan dat script), en een blok "in echte dagen" in het rapport: werkdag per hol-niveau en laag, goud van één nacht weg, en per week wat er nieuw is.

**Grootste uitkomst: weg in echte dagen maakt elke werkdag 1,5 keer zoveel goud als de open uren alleen** (6 uur open plus 3 uur weg). Met Sannes prijzen van versie 3 en weg als echte dagen (eerste run) liep de bank op tot ±35.000 goud bij uur 99 en kwamen er gaten van 3 tot 5 uur, want alles was op. Daarom alle prijzen vanaf laag 2 x 1,5 (laag 1 blijft, want op de eerste dag is er nog geen nacht weg geweest):

| | Versie 3 voorstel Sanne | **Bram na narekenen** |
|---|---|---|
| luik naar laag 2 / 3 / 4 | 500 / 1100 / 2000 | **750 / 1650 / 3000** |
| prijsfactor per laag (graven, stap 1 tot 3) | 1 / 1,5 / 3,5 / 5,5 | **1 / 2,25 / 5,25 / 8,25** |
| factor stap 4 tot 6 per laag | 1 / 1,3 / 2 / 2,6 | **1 / 1,95 / 2,0 / 2,25** |
| ding met een prijs per laag | 450 / 1250 / 2250 / 3500 | **590 / 1410 / 1935 / 2430** |
| dingen in laag 4 | 3 (42, 43, 45) | **7 (41, 42, 43, 44, 45, 47, 49)** |
| kamertjes | 5 per laag, 1,25 uur goud | **5 per laag, oplopend 1,2 / 1,6 / 2,0 / 2,4 / 2,8 uur goud** (dan koop je ze verspreid, niet alle vijf op één avond) |
| weg | 0,25, plafond 12 | 0,25, plafond 12 (zo gelaten) |

**Laag 4 (vraag 2): nu 1 tot 2 uur sparen per aankoop in werkdag-tempo.** "Uren sparen" in het rapport is prijs / goud per open uur; met de nacht erbij spaar je 1,5 keer zo snel. Laag 4: dingen 1,96 (dus 1,3 in werkdag-tempo), kamertjes 1,90 (1,3), stap 3 2,36 (1,6), stap 4 1,09 (0,7), stap 5 1,80 (1,2), stap 6 2,83 (1,9). Duurste van het hele spel: stap 6 in laag 3, 3,17 (2,1).

**In echte dagen (vraag 3), iemand met 6 uur open per werkdag, weekend dicht:**
| | werkdag | week |
|---|---|---|
| hol 12 | 1 | 1 |
| hol 20, laag 2 te koop | 2 | 1 |
| laag 2 open | 3 | 1 |
| hol 25 | 4 | 1 |
| hol 30, laag 3 open | 7 | 2 dag 2 |
| hol 35 | 10 | 2 dag 5 |
| hol 40, laag 4 open | 13 | 3 dag 3 |
| hol 45 | 17 | 4 dag 2 |
| hol 50 | 22 | 5 dag 2 |

Per week (mediaan): week 1 42 niveaus en 96 aankopen, week 2 15 en 54, **week 3 13 en 50 (laag 4 gaat open, Thijs' lat gehaald)**, week 4 8 en 19, week 5 4 en 1, week 6 niets meer. Goud van één nacht weg: 1.260 na werkdag 1, 2.000 na dag 3, ±3.000 na dag 10, ±3.850 vanaf dag 15. Hol 50 na 127,9 open uur.

**Gaten (langste tijd zonder iets nieuws, open uren):** tot 40 u 1,9 u, 40 tot 70 u 2,0 u, 70 tot 100 u 4,2 u, 100 tot 130 u 6,0 u. Waar (3 zaden uitgeschreven): rond 67 tot 72 u tussen hol 38 en 39, vlak voor het luik naar laag 4 (in dagen een halve middag), en na ±110 u in week 4 en 5, als laag 4 af is en alleen hol 46 tot 50 nog komen. Grootste bank: ±2.650 bij uur 30 (wachten op hol 30 voor het luik naar laag 3). Voorstel als het eind beter moet: de laatste kamertjes van laag 4 pas vrij op hol 47 en 49, of een stap 7 voor één lijn; dat is een ontwerpkeuze voor Sanne.

**Eerlijk, wat dit niet meet:** de sim koopt alles meteen; de werkdag is een vast patroon (6 uur open, dan dicht); een weekend telt net als een nacht één keer 12 uur (plafond); de nieuwe dingen in laag 4 (niveau 41, 44, 47, 49) zijn plekken voor iets met een prijs, wat het wordt is aan Sanne. Fenna's toets "prijs volgende ontgrendeling / goud per uur" staat al in elk lagenrapport (blok "verhouding"). In dat blok staat bij kamertjes de laag waarin je ze koopt: "laag 2 kamertje" zijn dus die van laag 1 (vrij na het luik naar laag 2), "laag 4 kamertje" die van laag 3 en 4 samen.


## 16 nov 2026 12:45 UTC (Bram): klaar om de voortgang van ±100 uur na te rekenen (besluit Thijs 13:01 NL)
Sannes `platformen/steam/voortgang.md` is er nog niet (wo 18 nov). Wat er nu al staat, zodat het narekenen dan minuten kost:
- `python3 sim.py diepte`: wat een speler bij uur 1, 2, 5, 10, 20, 40, 70 en 100 open tijd heeft verzameld. Dat zijn de bronnen waar een hol-niveau of een bewonersniveau op kan lopen. Uitvoer: `uitkomst-diepte.txt`.
- `python3 sim.py drempels N uren p bron`: voorstel voor drempels, zodat niveau n valt op `uren x ((n-1)/(N-1))^p`. p groter = snel in het begin, trager aan het eind.
- `python3 sim.py voortgang bestand.json`: rekent een voortgang na (meerdere sporen, de 6 winkelstappen tellen mee): wanneer valt elk niveau, ontgrendelingen en langste gat per blok, aantal muren (gat langer dan 2 u open tijd, het plafond uit features.md), laatste ontgrendeling, en hoeveel er na 24 u (3 werkdagen) nog komt. Voorbeeld: `voortgang-voorbeeld.json` (geen ontwerp, alleen om het te laten zien), uitvoer `uitkomst-voortgang-voorbeeld.txt`.

**Eerst een fout in de sim zelf, nu hersteld voor deze drie stukken:** de sim rekende met goud `6 x (1 + 0,1 x faam) x (1 + gangen / 40)`, graven tegen betaling en extra bewoners te koop. Het spel doet dat niet: `kern/afloop.gd` geeft 6 + 3 per eerder bezoek, faam bestaat niet in het spel, graven is gratis, en de winkel is alleen de 6 stappen van `upgrades.gd` (45, 126, 353 per soort, samen 1048). `SPEL_ECONOMIE` rekent nu zoals het spel (met heldensoorten aan); `SIM_ECONOMIE=oud` geeft de oude. De oude commando's (`begin`, `ritme`, `10 8`) veranderen niet.

**Wat het spel nu geeft (8 zaden, mediaan, GEZIEN):**

| Open tijd | Helden binnen | Gevangen | Goud verdiend | Hoeden op Gloop | Winkelstappen |
|---|---|---|---|---|---|
| 1 u | 75 | 49 | 324 | 36 | 4 |
| 2 u | 149 | 108 | 717 | 80 | 5 |
| 5 u | 367 | 291 | 1.866 | 226 | 6 |
| 10 u | 732 | 590 | 3.780 | 463 | 6 |
| 20 u | 1.464 | 1.193 | 7.611 | 948 | 6 |
| 40 u | 2.925 | 2.390 | 15.309 | 1.912 | 6 |
| 70 u | 5.108 | 4.206 | 26.805 | 3.358 | 6 |
| 100 u | 7.296 | 6.030 | 38.355 | 4.809 | 6 |

Tempo na de winkel (20 tot 100 u): 73 helden, 60 gevangen, 384 goud en 48 hoeden per uur, en dat blijft gelijk.

**Wat dat zegt voor het ontwerp (aan Sanne, geen besluit):**
1. **De winkel is op na 2,8 u** (min 2,8, max 3,0; het echte spel vangt hooguit ±10% minder, zie hieronder), niet na ±7 u: die 7 u kwam uit de oude sim met graven en extra bewoners. Daarna staat er bij 100 u ±37.000 goud op de bank waar niets mee kan. Goud heeft nu geen bodem om in te zakken; een voortgang van 100 u heeft dus óf iets nodig om goud aan uit te geven (iets dat steeds duurder wordt), óf de niveaus lopen op iets anders dan goud.
2. **Alles groeit na uur 3 recht evenredig met de tijd.** Er is niets dat sneller gaat naarmate je verder bent. Drempels die exponentieel oplopen (zoals de winkel, x 2,8) worden dus heel snel een muur. Drempels die als `n^2` of `n^1,5` oplopen passen beter.
3. **Hoeveel ontgrendelingen zijn er nodig zonder muur?** Eén hol-niveau op gevangen helden over 100 u: 50 niveaus geeft 13 tot 19 muren (gat langer dan 2 u), wat de vorm ook is; 75 niveaus met p 1,5 nog 3; **100 niveaus met p 1,5 geen enkele, met 7 niveaus in de eerste 2 u (de demo) plus de 6 winkelstappen.** Hetzelfde kan met minder hol-niveaus als bewonersniveaus en lagen ertussen vallen: wat telt is ±100 ontgrendelingen in totaal, ±30 daarvan tussen uur 40 en 100.
4. **Hoeden als bron voor de niveaus van Gloop** werken al: de zes maten van de hoedenberg vallen op 10 min, 43 min, 2,4 u, 6,6 u, 21 u en 63 u. Dat is een mooie lange lijn, maar alleen tussen 21 en 63 u is het gat 42 u, dus daar moet iets anders tussen.
**Naast het echte spel gelegd (GEZIEN, `hol.log` van de duurtests op tak `schermen`, map `steam-hol-duur/`, daar wordt niets gekocht):** twee runs van 60 min op main: `main-1920x1080` 33 gevangen en 210 goud, `main-exe` 46 gevangen en 309 goud. De sim zonder kopen geeft na 3630 s (20 zaden): 41 gevangen (min 31, max 52) en 279 goud (min 207, max 354). Acht runs van 15 min (zaden 4242 en 777): 8 tot 12 gevangen, gemiddeld 10,6; sim na 930 s: 12 (min 7, max 15). Het spel valt dus binnen de spreiding van de sim, hooguit ±10% lager. De winkel is in het spel dus rond 2,8 tot 3 u op, en de tabel klopt op ±10%.

5. **De voortgang verandert het tempo, en de sim telt dat nu mee (12:35 UTC).** Een niveau in de JSON mag een `effect` hebben dat vanaf het ontgrendelen in het spel meetelt: `gat` (0,9 = 10% korter wachten op de volgende held), `kans` (+procentpunt vangen per slijm of put), `goud` (+ per val), `goud_x`, `bewoner` (een extra slijm of put in de gang). Voorbeeld `voortgang-voorbeeld-effect.json` (zelfde drempels, elk vijfde hol-niveau 3% sneller helden, een extra put op niveau 10 en een extra slijm op 25, Gloop-niveaus +2 vangen): het laatste niveau valt dan op **78,6 u in plaats van 99,7 u** en tussen uur 70 en 100 zit een gat van 21 u (`uitkomst-voortgang-voorbeeld-effect.txt`). Drempels moeten dus samen met de effecten worden gekozen; dat kan ik woensdag meteen doen zodra voortgang.md er is. Zonder effecten geeft de sim precies hetzelfde als eerst (nagekeken met `diff`).



## 16 nov 2026 (Bram): sim volgt nu het ritme en het begin van het spel (`python3 sim.py begin`)
De sim rekende nog met een held per 25 tot 75 s en alleen "eerste held valt" (bij Gloop, dus een te vroege hap op 21 s). Nu, zoals `kern/ritme.gd` en `BEGIN` in `kern/strook.gd` sinds 16 nov 07:31 UTC: eerste held op 4 s, vaste stappen vallen (put), opgegeten (Gloop), vluchten (met wrok tegen de put), terug (die vluchter naar zijn vijand), doorlopen (Hoard-Toucher), gaten 5 tot 7, 18 tot 22, dan 35 tot 45 s, na het begin 40 tot 60 s. `SIM_OUD=1` geeft de oude sim. Opdracht: Fenna (`platformen/succes/onderscheid-hats.md` punt 3, "Bram: sim en toets"). 40 zaden, GEZIEN:

| Wat | Sim nu | Sim oud | Echte spel (log, Godot 4.3, 16 nov) |
|---|---|---|---|
| Eerste hap met hoed op de toren | 26 tot 28 s (aankomst plus 17 s lopen) | 21 s (kunstmatig) | 26,3 tot 27,8 s |
| Vluchter terug en afgerekend | 64 tot 76 s, mediaan 69 | komt niet vast | ±63 tot 75 s |
| Eerste upgrade als je niet graaft | 140 tot 508 s, gemiddeld 210, mediaan 163 | 102 tot 499 s, gemiddeld 264, mediaan 250 | eerste koop gemiddeld 196 s (was 245) |
| Hoeden op Gloop in de eerste 10 min | 1 tot 8, mediaan 3 | 1 tot 10, mediaan 4 | |
| Hoeden op Gloop in uur 1 | 11 tot 29, mediaan 21 | 9 tot 33, mediaan 26 | |

Wat het zegt: de sim en het spel lopen weer gelijk voor de eerste minuten (hap, wrok, eerste koop). Prijs: in uur 1 iets minder hoeden op Gloop (mediaan 21 tegen 26), want drie van de vijf vaste helden gaan niet naar Gloop (put, vluchter, Hoard-Toucher) en het gemiddelde gat blijft 50 s. Geen probleem voor de berg: maat 25 komt in de 10-uursrun nog rond 1,0 tot 1,5 u. Niets aan de balans veranderd.

`sim.py` speelt het spel na met dezelfde regels als `godot/systemen/held.gd` (wrok kiest het doel, roekeloos tegen je vijand, Hoard-Toucher brutaler, slijm 60 s plat, eerste held valt) en de kosten en het goud van `platformen/steam/balans.md` (Sanne). De speler koopt steeds het goedkoopste. Draaien: `python3 sim.py 10 8` (10 uur open tijd, 8 zaden). Uitvoer van deze stand: `uitkomst-10u.txt`.

## Wat er met de startgetallen gebeurde (GEZIEN, 5 zaden, 10 uur)
Met slijm 30%, put 22%, faam x 0,9 per niveau en elke terugkomer 50% kans: **68 tot 74% van de helden vluchtte** en er kwam **8 tot 10 keer per uur een aartsvijand** langs. Twee oorzaken: (1) in het spel draait een held om na een klap, dus hij komt de verdediging verderop vaak niet tegen (de proef van Sanne liet iedereen langs alles lopen); (2) faam x 0,9 zonder bodem maakt na ±10 uur elke verdediging 3 keer zwakker, en wie vlucht komt altijd terug, dus de stapel terugkomers groeit.

## Besluit Bram (sim mag de startgetallen overrulen, Sanne 19:10)
| Wat | Was | Nu | Waarom |
|---|---|---|---|
| Kans slijm / put | 30% / 22% | **45% / 35%** | dan vlucht ±1 op 3 (doel features.md) |
| Schijterig draait om na een klap | altijd | **de helft van de keren** | anders loopt bijna niemand langs de tweede verdediging |
| Faam | x 0,9 per niveau | **x 0,97, bodem 0,75** | helden worden langzaam sterker, maar je verdediging wordt nooit nutteloos |
| Volgende held is een terugkomer | 50% | **25%** | meer nieuwe namen, terugkomers blijven bijzonder |
| Gevluchte held komt ooit terug | altijd | **60%** (aartsvijanden altijd) | de rest gaat met pensioen (kan een kroniekregel worden, geen straf) |
| Aartsvijand aan de beurt komt echt | altijd | **15%** | zeldzaam, dus een feest als hij komt |

## Uitkomst met de nieuwe getallen (GEZIEN, 8 zaden, 10 uur open tijd)
- Eerste held valt na 4 s (moet_vallen): goud in de eerste minuut. **Doel gehaald.**
- Vluchten **36 tot 41%**, Hoard-Toucher 3 tot 6%. **Doel ±1 op 3 gehaald.** In `held.gd` zelf (toets, 1 slijm en 1 put): 38%.
- Aankopen: 14 tot 17 in het eerste uur, 34 tot 38 na 3 uur, alles van de eerste versie gekocht na **6,4 tot 7,1 uur**.
- Langste wachttijd tot de volgende aankoop: 7 tot 11 min in het eerste uur, 9 tot 14 min tot 3 uur, 42 tot 49 min tot 10 uur (dat is na "alles gekocht": dan valt er niets meer te kopen). **Onder het plafond van 2 uur.**
- Aartsvijand: **0,2 tot 0,8 per uur**, dus bij 2 tot 3 uur open per dag ongeveer één keer per dag. **Doel gehaald.**
- 41 tot 55 wrokken afgerekend in 10 uur ("Grudge settled").

## Wat dit niet meet
- Of het **voelt** goed: dat toetst Sanne op de GIF.
- Voortgang terwijl je weg bent (`voortgang.gd`): rekent nog met eigen kansen (0,15 + 0,12 per val + 0,10 per bewoner). Volgende stap: dezelfde kansen als hier gebruiken.
- Versie 1 moet ±40 uur inhoud hebben; met deze winkel is alles na ±7 uur op. Dat is inhoud (Sanne), niet balans.
- Volgorde van de verdediging in de gang: de sim zet slijm en put om en om.

## Goud per val: +3 per eerder bezoek (Bram, 9 nov 20:20 UTC, vraag Sanne 19:55)
Regel nu in `sim.py`: **6 x (1 + 0,1 x faam) x (1 + gangen / 40) + 3 per eerder bezoek** (`GOUD_PER_BEZOEK`, derde getal op de opdrachtregel; `python3 sim.py 10 8 0` = zonder bonus). Nieuwe kolom: tijd tot de eerste aankoop. Uitvoer: `uitkomst-10u.txt`.
- **Eerste aankoop: 45 tot 193 s, gemiddeld 104 s** (GEZIEN, 8 zaden). De bonus verandert dit niet: de eerste aankoop komt voor er een terugkomer valt. Dus binnen het doel van Sanne (rond 100 tot 200 s), met één snelle uitschieter (45 s). Met 3 in plaats van 6 per val zou het ±2 keer zo lang duren.
- Met de bonus: aankopen 15 tot 18 in het eerste uur (was 14 tot 17), alles gekocht na 5,9 tot 6,7 uur (was 6,4 tot 7,1), langste wacht 5,5 tot 13,2 min in het eerste uur en 11 tot 18 min tot 3 uur. Vluchten 34 tot 38%, aartsvijand 0,1 tot 1,0 per uur. **Alle doelen blijven gehaald**; de winkel is alleen iets eerder op (inhoud, Sanne).
- Een aartsvijand die na drie vluchten valt brengt 6 x ... + 9 op (Sanne rekende 15 met bezoek 3: dat klopt als het bezoek telt waarop hij valt; de sim telt eerdere bezoeken, dus vluchten).

## Hoedentoren: teller `hap_slijm` (Bram, 9 nov 21:20 UTC, vraag Sanne toets 3 punt 4)
`sim.py` telt nu elke hap van een slijm (`hap_slijm`) en de tijden van de hoeden van Gloop zelf (de eerste slijm; elke slijm heeft zijn eigen toren). GEZIEN met `python3 sim.py 1 8` en `python3 sim.py 40 4` (open tijd, dus speeltijd plus wat voortgang meetelt):
- Eerste uur: Gloop eet 13 tot 27 helden (gemiddeld 22), dus Sanne's 13 tot 28 klopt. Vier hoeden op zijn hoofd na 2 tot 18 minuten.
- Daarna ±27 per uur voor Gloop (±30 voor alle slijmen samen, omdat je er een bij koopt).
- Maten van de hoedenberg voor Gloop: 5 na 0,1 tot 0,3 u, 25 na 1,0 tot 1,5 u, 100 na 3,8 tot 4,9 u, 300 na 10,7 tot 12,3 u, 1000 na 37 tot 38 u.
- Betekenis: wie de strook een werkdag (8 u) open heeft, ziet maat 100 op dag 1, maat 300 op dag 2 en maat 1000 rond dag 5. Groei over dagen, zoals Sanne wil, maar na een week is de berg af. Voorstel aan Sanne: een zesde maat bij 3000 (±2 weken werkdagen), of de hoeden van de hoedenberg in het Heldenboek tellen zodat er daarna nog iets groeit.

**9 nov 22:30 UTC, zesde maat (Sanne 21:50):** `BERG_MAAT` is nu 5, 25, 100, 300, 1000, 3000. GEZIEN met `python3 sim.py 150 5`: maat 3000 voor Gloop na 109,5 tot 114 u open tijd (maat 1000 na 37 tot 38 u). Met een werkdag van 8 u per dag is dat rond dag 14, zoals Sanne rekende. Maat 6 wordt breder, niet hoger: 33 hoeden zichtbaar in hooguit 6 rijen (maat 5: 21 in 6 rijen).

## 10 nov 00:30 UTC (Bram): upgrades met hun eigen effect
`sim.py` rekent nu ook wat stap 2 van elke upgrade doet (`godot/systemen/upgrades.gd`): Bouncy Gloop ligt 2/3 van de tijd plat (40 s), Deep Pit laat een schijterige held na zijn eerste klap van de put niet omkeren. Uitkomst (GEZIEN, 8 zaden, `uitkomst-10u.txt`): vluchten blijft 34 tot 39%, eerste aankoop gelijk (45 tot 193 s), aankopen per uur gelijk, Gloop eet iets meer (±30 per uur in plaats van ±27, hoed 300 na ±10 u). Langste wacht tot 10 u 38 tot 49 min (dat is na "alles gekocht"). Alle doelen blijven gehaald; de stappen maken het spel niet te makkelijk.

## 10 nov 01:35 UTC (Bram): ritme van de eerste upgrade (Sanne, features.md feature 5, "GOK, na te meten in Brams sim")
Nieuw: `python3 sim.py ritme` (20 zaden). Twee spelers: "spaar" koopt alleen upgrades en graaft nooit (Sannes "als je niet graaft"), "goedkoopst" koopt steeds het goedkoopste (zoals tot nu toe). GEZIEN:
- **Spaar: eerste upgrade (60) na 7,3 / 11,1 / 15,6 min open tijd** (min, mediaan, max). Sannes gok van ±10 min klopt.
- **Goedkoopst: geen enkele upgrade in de eerste 2 uur.** Graven kost 5 + 1,2 x gangen en blijft tot 40 gangen onder de 60, dus wie steeds het goedkoopste pakt graaft eerst het hele hol vol. In het eerste uur is er dan wel elke 5,5 tot 13,4 min iets te kopen.
- Spaar heeft in het eerste uur een gat van 10,6 tot 34,8 min zonder iets te kopen (de tweede stap kost 168).
- **Betekenis voor het kaartje:** de keuze is echt (graven of sparen), en dat is goed, maar een speler die het goedkoopste kiest, ziet de upgrades pas na uren. Het muntje boven Gloop (Sanne) helpt alleen als hij spaart. Voorstel aan Sanne: het muntje ook laten zien als de speler 60 heeft en het graven hem er weer onder zou brengen, of graven per gang duurder vanaf ±12 gangen. Dat is haar keuze (balans.md); de sim kan beide doorrekenen.
- **Fout gevonden en hersteld:** Deep Pit telde in de sim nooit mee (de put heet in `sim.py` "put", de regel keek naar "stekelput"). Na herstel (8 zaden, `uitkomst-10u.txt`): vluchten 33 tot 38%, aankopen per uur gelijk, alle doelen blijven gehaald. De uitspraak van 00:30 hierboven ("Deep Pit gerekend") klopte dus niet; nu wel.

## 10 nov 02:15 UTC (Bram): upgrade 45, 126, 353 en graven +3 per gang boven de 12 (Sanne 01:50, balans.md)
Sinds nu rekenen `sim.py` (`UPG_BASIS`, `graaf_prijs()`) en `godot/systemen/upgrades.gd` (`BASIS`) met Sannes nieuwe getallen; de metingen van 01:35 hierboven (60, 168, 470) zijn daarmee oud. Uitkomst (GEZIEN, 8 zaden, 10 uur, `uitkomst-10u.txt`):
- Eerste val na 4 s, vluchten 33 tot 39%, aartsvijand 0,1 tot 0,9 per uur, Hoard-Toucher 4 tot 6%. **Doelen gehaald.**
- Eerste aankoop gelijk (45 tot 193 s): dat is graven onder de 12 gangen, daar veranderde niets. Niet omdat de sim niet opnieuw draaide.
- Aankopen 12 tot 15 in het eerste uur (was 15 tot 18), alles gekocht na **7,1 tot 7,6 uur** (was 5,9 tot 6,7). Langste wacht: 6,7 tot 15,0 min in uur 1, 11 tot 16 min tot 3 uur. **Ver onder het plafond van 2 uur.**
- Ritme (`python3 sim.py ritme`, 20 zaden): **spaar** eerste upgrade na 5,1 / 9,3 / 13,3 min (was 7,3 / 11,1 / 15,6), langste gat in uur 1 16,6 tot 33,2 min; **goedkoopst** eerste upgrade na 50 / 61 / 72 min (was: nooit in 2 uur), langste gat in uur 1 6,7 tot 16,5 min. De toeslag op graven doet dus wat Sanne wilde: ook wie het goedkoopste koopt ziet binnen ±een uur zijn eerste upgrade.
- Gloop eet ±29 tot 31 helden per uur; hoedenberg 100 na 2,9 tot 4,4 u, 300 na ±10 u.

## 10 nov 02:20 UTC (Bram): heldensoorten (versie 1), `python3 sim.py soorten`
Ridder, dief, magiër en bard uit `features.md` (versie 1) als systeem in `godot/systemen/heldensoort.gd`, zelfde getallen in `sim.py` (`SOORTEN`, standaard uit, dus de tabel hierboven verandert niet: nagekeken, uitvoer gelijk). Na de eerste 10 helden: 55% gewoon, 15% ridder, 15% dief, 10% magiër, 5% bard. Een bard die ontsnapt zingt, dan komen er 2 helden snel achter elkaar (8 tot 20 s).
Uitkomst (GEZIEN, 8 zaden, 10 uur), zonder / met soorten:
- vluchten 33 tot 39% / **35 tot 39%** (doel ±1 op 3 blijft), helden per uur 71 tot 73 / 72 tot 75, alles gekocht na 7,1 tot 7,6 / 7,0 tot 7,6 u. (Na de controleur: de soortfactor geldt net als in held.gd alleen op de basiskans, niet op upgrade en ROEKELOOS.)
- langste wacht in uur 1: 6,7 tot 15,0 / 7,0 tot 19,8 min (ver onder 2 uur), aartsvijand 0,1 tot 0,9 / 0,2 tot 0,8 per uur, liederen 0,5 tot 1,6 per uur (een bard die zingt is dus ongeveer eens per uur een gebeurtenis).
- In `toets_held.gd` (120 helden per soort, 1 slijm en 1 put): magiër valt 2 keer in de put tegen 18 voor een gewone held, dief 8, ridder komt vaker tot de put (25, hij is taai) en loopt 19 s tegen 13 s; vluchten per soort 32 tot 44%. Getallen zijn een GOK, Sanne mag ze bijstellen.
- **02:30 UTC, karaktertrekken erbij** (versie 1): slaapkop (dutje van 4 s halverwege), wraakzuchtig (dubbel roekeloos tegen zijn vijand), opschepper (langzamer, pocht), na held 10 en dan 1 op 5 (`heldensoort.kies_trek`). In `sim.py soorten` mee: vluchten 34 tot 40%, langste wacht uur 1 6,6 tot 12,4 min, aartsvijand 0,3 tot 1,4 per uur. Doelen blijven gehaald. Toets: wraakzuchtig valt 41 van 150 keer in zijn eigen vijand tegen 27 voor een gewone held. "Verdwaald" uit features.md komt later: in één rij gangen zie je "de verkeerde gang" nog niet.

## 10 nov 03:20 UTC (Bram): ridder en bard volgens Sanne (balans.md 03:05)
Ridder slijm 0,7 en put 1,4 (held van de put), bard 1,1 en 1,1; zelfde getallen in `godot/systemen/heldensoort.gd`. `python3 sim.py soorten` (8 zaden, 10 uur, GEZIEN), zonder / met soorten: vluchten 32,9 tot 39,0% / **31,5 tot 40,6%** (doel ±1 op 3 blijft), helden per uur 71 tot 73 / 72 tot 76, langste wacht uur 1 6,7 tot 15,0 / 6,6 tot 9,3 min, alles gekocht na 7,1 tot 7,6 / 7,0 tot 7,9 u, aartsvijand 0,1 tot 0,9 / 0,4 tot 1,1 per uur, liederen 0,6 tot 1,7 per uur. Per soort zie Sannes tabel in balans.md (ridder 32 / 36 / 32%: de put vangt hem nu vaker dan Gloop).

## 10 nov 03:35 UTC (Bram): Trick Lid tegen de magiër (idee Sanne, features.md 03:10)
Trick Lid (stap 3 van de put) ziet eruit als vloer, dus de magiër ziet hem niet: factor put 0,3 wordt 1,0 (`heldensoort.VERBORGEN_X`, `sim.py TRICK_MAGIER`). Gemeten met een teller per soort (8 zaden, 10 uur, GEZIEN), alleen helden die kwamen terwijl Trick Lid er lag: magiër in de put **10,6% wordt 19,3%**, magiër Gloop 61,5 wordt 58,5%, magiër vlucht 27,9 wordt 22,2%. Gewone held en ridder gelijk (binnen ruis). Alle helden: vluchten 35,1 wordt 34,8%. `sim.py soorten`: vluchten 31,5 tot 40,7%, langste wacht uur 1 6,6 tot 9,3 min, alles gekocht na 7,0 tot 7,9 u. Doelen blijven gehaald. Klein effect op het geheel, wel een echte tegenzet die je in het Heldenboek kunt teruglezen.

## 10 nov 03:50 UTC (Bram): hoe snel vult het Heldenboek (Sanne features.md 03:10, "Bram meet na")
`python3 boek_meting.py` (sim met heldensoorten, 8 zaden, 140 uur, speler koopt het goedkoopste, GEZIEN), uren open tijd min / mediaan / max:
- hoofdstuk 1 vol (5 soorten x 3 stempels): 1,0 / 1,8 / 3,0 u; de laatste stempel is meestal de magiër in de put (0,2 / 1,8 / 3,0 u).
- alle 10 hoeden (als elke held een willekeurige hoed draagt): 0,6 / 1,1 / 1,9 u.
- hoedenberg 1000: 31 / 32 / 33 u, 3000: 93 / 94 / 96 u (Sanne rekende 110 u; Gloop eet nu iets meer door upgrades en soorten). 10.000 komt pas na ±300 u.
Dus: hoofdstuk 1 en de hoeden zijn op dag 1 klaar (zoals Sanne verwachtte), de bergstempels bij een werkdag open op dag ±4 en ±12, de aartsvijanden lopen altijd door. Karakters (hoofdstuk 2) zitten niet in de sim; de trekken komen na held 10 met 1 op 5, dus ook dag 1.

## Eerste aartsvijand (Bram, 10 nov 04:20 UTC, `python3 sim.py aarts`, 60 zaden, 6 u, GEZIEN)
Sanne vraagt in `features.md` (eerste tien minuten): geen aartsvijand in het eerste uur van een nieuw spel.
| regel | met soorten | aartsvijand in uur 1 | vroegste | mediaan eerste | binnen 6 u |
|---|---|---|---|---|---|
| geen regel (nu in strook.gd) | nee | 12 van 60 (20%) | 0,18 u | 1,82 u | 54 |
| geen regel (nu in strook.gd) | ja | 19 van 60 (32%) | 0,18 u | 1,60 u | 56 |
| pas na 3600 s open tijd | ja | 0 | 1,00 u | 2,29 u | 58 |
| pas vanaf 60 nieuwe helden | ja | 1 (0,98 u) | 0,98 u | 2,25 u | 58 |
In uur 1 komen 50 tot 69 nieuwe helden (mediaan 60). Advies: tel in nieuwe helden (`helden_nr` staat al in de save), dan hoeft er geen open tijd bij. `heldensoort.aarts_mag(helden_nr)` geeft true vanaf 60. De aartsvijand komt dan gemiddeld na ±2,3 u, nog steeds op dag 1.

## 13 nov 2026 (Olaf): eerste upgrade zonder graven, en startgoud 20
In het spel is graven gratis, dus de echte eerste koop is de upgrade van 45. `python3 sim.py ritme`, strategie spaar, 20 zaden (GEZIEN):
| Startgoud | eerste upgrade min / mediaan / max | langste gat uur 1 (goedkoopst) |
|---|---|---|
| 0 | 5,1 / 9,3 / 13,3 min | 6,7 tot 16,5 min |
| 20 (nu, `START_GOUD`) | 1,7 / 4,5 / 7,6 min | 6,6 tot 18,4 min |
In het spel zelf: duurtest run 43428675361 met 0 goud gaf 504 s.
