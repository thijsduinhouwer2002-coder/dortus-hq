# Gloop-spel voor Garmin: ontwerp van de speelbare proef

Akkoord: nog niet voor uitbrengen. Daan keurde het spel in de simulator op stijl (16 nov ±05:38 UTC, run 43808547911 op e5dbbf2: beide moets ja, geen nieuwe ronde nodig voor het spel zelf); winkelbeelden en icoon keurt hij apart. De keuring van Mila van de slok in het spel staat nog open. Niemand heeft het gespeeld.

**Waarom wij (één zin, voorlopig):** het enige horlogespel waarin je toren van hoeden letterlijk hoger wordt dan je horloge, met een eigen figuur met karakter in plaats van blokjes of een kloon.

## Wat het doet
Een held valt door de schacht. Druk op START (of tik) als hij bij de bek van Gloop is: GULP, de hoed van de held vliegt op de toren rechts. Een ronde duurt 30 seconden; de rand van het scherm loopt leeg als klok. Aan het eind: het aantal hoeden en "NEW BEST!" of je beste score. Eén knop, verder niets. Dit volgt het voorstel "Hat Tower" van Mila (`ontwerp/garmin/gloop-spel/LEESMIJ.md`) en de eisen van Vera (eigen spel, alles met knoppen, licht voor oude horloges).

Wat het spel spannend moet maken: precies in het midden van de bek drukken geeft "GULP!" en een reeks ("GULP! x3"); elke vangst laat de volgende held 6 procent sneller vallen; de helden komen met een onregelmatige pauze, zodat je moet kijken en niet op ritme kunt drukken.

Sinds 16 nov ±03:00 UTC (commit bd04a60) ook: **de slok** (voorstel Mila v3: de held steekt 0,3 seconde ondersteboven uit de open bek en zakt weg, nog met eenvoudige vormen), **een korte trilling bij elke vangst** (steviger bij een voltreffer, alleen op horloges die kunnen trillen), het cijfer onderaan in het midden, en de Venu Sq 2 (vierkant scherm) in het manifest.

## Wat het bewust niet doet
- **Nooit straffen.** Missen kost geen hoed en geen leven: de held loopt weg ("bye!") en de volgende valt 15 procent langzamer. Te vroeg drukken: Gloop hapt in de lucht en heeft een kwart seconde zijn bek dicht. Er is geen game over, alleen de klok.
- Geen plaatjes in de proef: alles is getekend met rechthoeken en cirkels. Eerst leuk, dan mooi (`organisatie/onderzoek-youtube-werkwijze.md`). De echte Gloop, held en hoeden komen pas als de regel leuk blijkt.
- Geen stappen, geen account, geen internet, geen rechten.
- Nog geen prijs en geen winkeltekst (opdracht hoofdchat 15 nov 23:20).

## Hoe het aansluit
`producten/garmin-gloop/`, Monkey C, zelfde bouwstraat als de eerste Garmin-proef (`.github/workflows/garmin-gloop.yml`, kopie van `garmin-proef.yml`): toetsen in de simulator en schermafbeeldingen op tak `schermen`, map `garmin-gloop/<tak>/`. Voor de beelden speelt het spel zichzelf (`Bouw.AUTO`), omdat de simulator in de bouwstraat geen knoppen kan indrukken.

## Wanneer de proef af is (toetsbaar)
1. De toetsen zijn groen in de simulator: start, vangen, te vroeg, missen straft niet, einde na 30 seconden, beste score.
2. Eerste hoed binnen 2,5 seconde na de start (toets), en een speler die alles raakt haalt 15 of meer hoeden, dus de toren gaat over de bovenrand (13 passen op het scherm).
3. Beelden uit de simulator op FR255 (MIP 260), fenix 7 (MIP 260) en Venu 3S (AMOLED 390): startscherm, vallende held, GULP met vliegende hoed, eindscherm. Gijs heeft ze bekeken.
4. Daan en Mila hebben de beelden gezien en gezegd wat anders moet. Of het leuk is kan alleen een mens zeggen: Thijs speelt de proef op zijn horloge of in de simulator (komt op zijn lijst zodra 1 tot 3 groen zijn).

## Stand van de proef (16 nov ±03:10 UTC, run 43795386009 op bd04a60, groen)
- Punt 1 en 2 gehaald: toetsen groen; de zelfspeler (vangt alles, laat één held lopen) haalt in de simulator 15 hoeden en de toren komt op de FR255 tot de bovenrand.
- Punt 3 gehaald op vier horloges (FR255, fenix 7, Venu 3S, Venu Sq 2): start, vallen, "bye!", GULP met reeks, toren, eindscherm "15 HATS / NEW BEST!", opnieuw. Vier overzichtsbladen van 26 beelden bekeken, vier beelden uitvergroot.
- Niet goed: op de vierkante Venu Sq 2 is de klok een cirkel midden in beeld die door de toren loopt (moet een balk of de schermrand worden). Het eindscherm dekt Gloop half af. De slok is alleen aan het eind van het wegzakken in beeld gezien, niet het begin.
- Punt 4 open: niemand heeft het gespeeld. Er is nog geen bestand dat Thijs op een horloge kan zetten.
- Uitgezocht: het verschil tussen 8 hoeden (simulator) en 19 (toets) kwam niet door de klok. De oude zelfspeler liet één soort held lopen en die viel toevallig drie keer vroeg; elke misser kost tijd en maakt de volgende 15 procent trager. Nagerekend in Python met hetzelfde toevalsgetal: 10 hoeden bij tikken van 50 ms, 8 bij 200 ms. Wel een les: bij tikken van 150 ms of trager springt een snelle held in één stap over de bek heen.

## Stand 16 nov ±04:15 UTC: echte plaatjes en opstelling (c)
Daan en Mila kozen allebei (c): de toren staat op de kop van Gloop, de held komt schuin van linksboven door een lichtbaan. Dat is nu gebouwd met de spritekit van Mila (`ontwerp/garmin/gloop-spel/kit/` op main, omgezet met `maak_kit.py`): Gloop rust, hap (in de vangzone), slok en blij, de vallende held, de vliegende helm en tien hoeden. De teller staat bovenaan met de kroon, het woord GULP staat met een boogje naast de START-knop, de klok rondom is goudgeel. De spelregels in `Spel.mc` en de toetsen zijn niet veranderd. Bewust nog niet: de held draagt altijd de helm terwijl de toren tien soorten hoeden krijgt (zo staat het op het blad van Mila; vraag aan haar of dat zo blijft), en de slok duurt nog 0,3 seconde.

## Stand 16 nov ±06:10 UTC: zeven horloges, slok van Mila, stilstand
- Het spel draait op zeven horloges in alle zes maten van de kit: FR255 en fenix 7 (260, MIP), fenix 7X (280, MIP), Venu Sq 2 (320, vierkant), Venu 3S (390), FR265 (416) en Venu 3 (454).
- De slok is de plaat van Mila (één grote mond, oog vrij, benen en buik van de held schuin erin); de helm vertrekt boven de kruin.
- Precies op het slikken staat alles 0,08 seconde stil (ook de klok van het potje), zodat de vangst zwaarder voelt zonder dat het tempo verandert. Dit zit alleen in het scherm; `Spel.mc` en de toetsen zijn niet veranderd. Of het zo voelt kan alleen een mens zeggen.
- De kreet ("GULP! x7") houdt altijd minstens 8 px lucht tot de toren. Past hij niet op één regel, dan staat de reeks op een tweede regel, in het grotere font als "GULP!" daarin past (260 en 280), anders klein.
- Staat de teller rechts naast een hoge toren, dan vliegt de helm links om (kan van Daan), zodat hij niet over het kroontje gaat.
- Op AMOLED heeft de lichtbaan een zachte rand; op MIP is hij effen.
- De regel onderaan ("START = GULP", "START = AGAIN") schuift op ronde schermen omhoog tot hij tussen de randen past (op de Venu 3S viel "START = AGAIN" links en rechts buiten beeld, gezien in run 43813600332).
- Nog niet: Instinct (zwart-wit, vraagt eigen plaatjes van Mila), een titelplaatje in plaats van het dunne systeemfont op AMOLED, naam, prijs en winkeltekst (voorstel staat sinds run 108 in `platformen/garmin/gloop-winkel-voorstel.md` op main, wacht op Daan en Chris).

## Stand 16 nov ±08:25 UTC (run 110): startscherm, vette letters, donkere grot, kleine horloges
- Startscherm (Mila, 07:55): de titel staat weer in het midden; het woord GULP is daar weg, alleen het witte boogje wijst de START-knop aan. Tijdens het spel staat het woord er wel.
- Op AMOLED (320 en breder) staat elke letter twee keer, één pixel naast elkaar, zodat het dunne systeemfont vetter oogt.
- Op AMOLED is de achtergrond het plaatje van de donkere grot van Mila (warm achter Gloop, bijna zwart aan de rand). MIP blijft effen.
- Erbij: Forerunner 55 (208 px) en Forerunner 245 (240 px), beide MIP. Of ze bouwen en hoe ze eruitzien staat in `platformen/garmin/status.md` op main, niet hier.

## Open vragen (voor na de proef)
- Is 30 seconden goed, of liever een vast aantal helden? Kiezen na het eerste echte potje.
- Rechthoekige horloges (Venu Sq) en de zwart-witte Instinct: de proef tekent al naar verhouding, maar is daar niet bekeken.
- Trilling bij een GULP (voelt goed, kost batterij): proberen in de volgende stap.

## Stand 16 nov ±09:10 UTC (run 111): PRESS op de Venu's, vet eindscherm, grot op de Forerunner 55
- Op de Venu 3, Venu 3S en Venu Sq 2 heet geen knop START. Daar zegt het spel `PRESS = GULP` en `PRESS = AGAIN` (Daan, 08:45). Op de ronde Venu's wijst het witte boogje de knop ook op het eindscherm aan. FR265, FR255, FR245, FR55 en fenix houden START.
- Op een vierkant scherm staat tijdens het spel geen los woord GULP meer: zonder boogje wees het nergens naar.
- Eindscherm: de drie regels in de zwarte balk staan op AMOLED ook twee keer naast elkaar (nep-vet).
- Forerunner 55 (8 kleuren): de grot is een plaatje van Mila in alleen zwart, rood en geel, met een dambord van 1 pixel voor de tussentinten.
