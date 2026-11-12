# Ebb: Today en 8 weeks, blad strand v2 (Mila, run 53, 12 nov 04:40 UTC)

Opdracht hoofdchat (berichten/mila.md, 05:15 NL): strand afmaken. Script `bron/strand_v2.py`, beelden `strand2/` (rij 260 2x en rij 454, losse schermen). Meting `bron/meet_strand_v2.py`: **elke tekstregel 4,5 of hoger (laagste 4,92), op 260 en 454, dag en nacht.** GEZIEN met Read: beide rijen.

Inhoud en regels blijven zoals in strand v1 (`ebb-strand-v1.md`): een schelp per sessie op haar uur, alle schelpen even groot, geen inhoudtijd op Today; 8 golven, een gehaald weekdoel is een brekende golf, een gemiste week een lage golf in hetzelfde blauw; het dier surft op de golf van deze week.

## Wat er nieuw is
- **Zelfde stijl als de werelden:** zachte AMOLED-verlopen en de ronde rand, witte golflijn en witte getijdenlijn, schelpen als waaierschelp met witte rand en glimpje, golven met witte rand en een schuimbolletje; dieren op MIP met de donkere omtrek van 1 px (keuring 2 punt 3).
- **De haak: je dag als strandwandeling.** Een loper (schildpad, krab) laat een spoor van pootjes na langs de getijdenlijn van de eerste schelp tot waar hij nu staat; een zwemmer laat een rij belletjes na in het ondiepe water. Het spoor zit echt in het product: het loopt van de eerste tot de laatste sessie van vandaag.
- **Lucht volgt de klok** (van 6 tot 18 uur): krab-lucht 0055AA/00AAFF (AMOLED 001E5F, 004BA5, 00A5FA), zon FFFF55 straal 9 met witte rand op een boog x = 40 + t × 180, y = kam − 14 − 16 × sin(π t), t = (uur − 6)/12; een zeilbootje op de horizon aan de andere kant (x 214 als de zon links staat, anders 50). 's Nachts nachtlucht met vier sterren en maan, en dan de nachtregel.
- **8 weeks:** geen zon (die viel achter de golven), wel dezelfde lucht. "one wave a week" in AAFFFF (cyaan haalde op AMOLED maar 4,47).
- **Nacht:** droog zand AAAA55 en nat zand 555500 als basis, daarna de nachtregel (`ebb-nachtregel-v1.json`, nu v1.1); alle tekst die overdag donker op het zand staat wordt FFFFAA.

## Maten (1/260 D, y van boven)
- Today: kam 78, getijdenlijn 128, droog zand 152. Kop "today" 00FFFF maat 26 op 18. Uurstreepjes 1,2 breed van 152 tot 155, labels maat 14 op 155, x = 36 + uur/24 × 188.
- Schelp: punt onder op (x, getijdenlijn + 13), tweede rij 15 hoger; ligt de vorige minder dan 19 dichtbij, dan tweede rij of 19 naar rechts. Waaier van 9 punten, straal 9, roze FFAAAA met witte rand 1,4, vier ribben en een voetje FF5555, glimpje wit.
- Pootjes: elke 7, om en om 1,6 boven en onder getijdenlijn + 6, ovaaltje 1,9 × 1,4 in 555500. Belletjes voor zwemmers: elke 11 op getijdenlijn − 9, straal 2, wit.
- Dier gespiegeld (kijkt naar de schelpen), maat 26, 30 naast de nieuwste schelp (links als dat voorbij x 212 valt); lopers y 132, zwemmers y 112. Zonder sessies op het uur van nu.
- Tekst: "3 shells today" maat 22 op 178, "first shell 7:12" (of "one session leaves one") maat 16 op 204, 000055.
- 8 weeks: kam 150, nat 164, droog 178. Golven x = 28 + i × 25,5, voet 154, hoog 36. Dier maat 16 op (x + 14, top − 8). "5 big waves" wit 22 op 62, "one wave a week" AAFFFF 15 op 88, "8 wk ago" op x 56 en "now" op x 208, maat 14 op 182 in 555500, "this week: 2 of 3" 000055 16 op 204.

## Voor Gijs
Bouwen na de krabpunten en het eenheidsblad. Kosten zoals v1 plus ±8 punten per pootje of belletje (alleen tussen eerste schelp en dier). Krab op het strand: zonder zwemband (hij loopt op het zand), of met de band om zijn buik als dat in één plaatje goedkoop is; jouw keuze.

## Frisse keuring (run 53) en wat er daarna veranderde
Eerste keuring van v2: Today dag 6, nacht 4, 8 weeks dag 6, nacht 5 (onderwater: start 6, pauze 7, sea log 7). Drie punten, alle drie gedaan:
1. **Nacht niet rustig** (fel olijfgeel zand, felle cyaan koppen): zand bij nacht nu koel blauwgrijs (basis droog 5555AA, nat 000055, daarna de nachtregel: MIP 000055 en zwart, AMOLED bijna zwart), koppen "today", "8 weeks", "paused" en "the sea waits" bij nacht 55AAFF. Ook in de onderwaterschermen.
2. **8 weeks, grap te klein:** de zeven vorige weken klein (x 20 + i × 21, hoog 32), een gemiste week plat en kalm (4 hoog). **Deze week is één grote golf** van 50 breed op x 168, hoogte 30 + 26 × voortgang, altijd met schuimkrul, en het dier maat 26 staat erop op een gele surfplank met rode streep. Koppen 8 links (x 112) zodat de surfer vrij staat.
3. **Today te standaard:** schelpen groter (1,3; afstand 23, tweede rij 17 hoger), schaal alleen streepjes met cijfers 0, 12 en 24 (maat 13), pootjes groter (2,4 × 1,7). Zwemmers liggen niet meer op het zand: ze **springen uit de branding** (dier op y 100, schuimboogje en vier druppels eronder).
Meting na de wijzigingen: laagste 5,03, 0 te laag. GEZIEN met Read: rij 260 2x.

## v2.1 na de tweede frisse keuring (run 53)
Tweede keuring: Today dag 6, nacht 5, 8 weeks dag 5, nacht 4 (start 7, pauze 7, sea log 8). Punten: onderste helft leeg en modderig, golven lezen als tanden, nacht nog niet donker genoeg. Gedaan:
- **Today nieuwe opbouw:** kam 64, getijdenlijn 112, droog zand 160. Kop "today" 22 op 8 (cyaan, nacht 55AAFF), het aantal ("3 shells" of "no shells yet") wit 22 op 28 in de lucht (nacht AAAAFF). Schelpen **2,0** (afstand 30, punt op getijdenlijn + 34, tweede rij 20 hoger), dier maat 36 (lopers op getijdenlijn + 22, zwemmers springen op getijdenlijn − 22 met schuimboog en druppels), pootjes op getijdenlijn + 12. Streepjes op 162 tot 165, cijfers 0, 12, 24 maat 13 op 165. "first shell 7:12" maat 16 op 198.
- **Droog zand leeft:** twaalf korrels AAAA55, een oranje zeestertje FFAA00 met witte rand op (210, 206), een krabgaatje op (52, 208). AMOLED zand warmer: droog FFEBAA, nat D7C37D (MIP blijft FFFFAA en AAAA55).
- **Zon nooit achter tekst:** staat hij tussen x 56 en 204, dan zie je hem als vier gele streepjes schittering op het water onder zijn plek. AMOLED-lucht wordt pas vlak boven de horizon licht (knik 0,8), MIP-band pas 5 boven de horizon.
- **Nacht:** zee een trede donkerder als basis (MIP 0000AA, AMOLED 001E78 tot 000F50), tekst op het zand AAAAAA.
- **8 weeks:** zeven golven 24 breed en 44 hoog met een donkerder vlak 0055FF in het lijf (diepte), gemiste week een platte golf van 6 hoog met witte rand 1,6; deze week 58 breed op x 170, hoogte 40 + 30 × voortgang, dier maat 34 op de surfplank. Koppen: "8 weeks" 24 op 12, "5 big waves" 22 op 40 en "one wave a week" 15 op 64, beide op x 104.
Meting: laagste 5,06, 0 te laag. GEZIEN met Read: rij 260 2x en 454.

## v2.1b na de derde frisse keuring (run 53)
Derde keuring: Today dag 6, nacht 6, 8 weeks 5 en 5, start 6, pauze 6, sea log 7. De keurders verschillen per keer, maar twee punten kwamen elke keer terug, en die zijn gedaan:
- **Schelp op het uur lees je niet:** de uurlijn (streepjes en cijfers 0, 6, 12, 18, 24, maat 13) staat nu direct onder de schelpen op de grens van nat en droog zand (droog vanaf 150, streepjes 151 tot 154, cijfers op 154); schelppunt op getijdenlijn + 33, tweede rij 19 hoger; dier op getijdenlijn + 16; "first shell" maat 16 op 176.
- **Golven lezen als ijspegels:** 8 weeks is nu **één doorlopende zee met acht toppen** (oppervlak = basis 160 min een bult per week: gehaald 34 hoog en 10,5 breed met schuimkrul naar rechts, gemist 7 hoog met een witte stip erboven; deze week een bult van 44 + 26 × voortgang en 13 breed op x 206 met grote krul en het dier op zijn plank). Lichte zee 00AAFF, daaronder een diepere laag 0055FF, witte schuimrand 1,8.
Meting: laagste 5,06, 0 te laag. GEZIEN met Read: rij 260 2x en `weeks-5-454.png`.
Nog open: per scherm een eigen kleine grap (keurder 3), dieren bij nacht minder verzadigd (voorstel voor nachtregel v1.2: na het dimmen 30 procent naar grijs), en de onderste rand van Today nog voller.
