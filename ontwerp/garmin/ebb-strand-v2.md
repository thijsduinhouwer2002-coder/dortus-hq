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
