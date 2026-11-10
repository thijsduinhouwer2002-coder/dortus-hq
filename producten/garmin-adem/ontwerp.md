Akkoord: nee 10 nov 2026 18:45 UTC, omdat de walvis (en schildpad) in de app en in de winkelbeelden niet mooi en niet gecentreerd zijn (oordeel Thijs 19:33 NL, ik ben het eens). Niet indienen met `ebb-v1.0.0`. Moet W1 tot W6 in keuring 3 van `ontwerp/garmin/ebb-winkel-keuring-daan.md`: nieuwe walvis met karakter, midden van de tekening is midden van het dier, op het horloge in het midden onder de klok, loep gecentreerd, schildpad ook, icoon gelijk. Winkeltekst versie 3 en de rest van de beelden zijn wel ja. Na `ebb-v1.0.1` en Mila's nieuwe beelden kijk ik alleen W1 tot W6 na.

Oud: Akkoord: ja 10 nov 2026 16:25 UTC voor indienen, op voorwaarde van kleine moet-punten (keuring 2 in `ontwerp/garmin/ebb-winkel-keuring-daan.md`): app zoals op tak `claude/garmin-2026-11-10b` f287bab plus de nieuwe walvis en schildpad (Mila moet 3 en 4); winkeltekst versie 2 (88adb3f) na drie zinnen (T1 tot T3); winkelbeelden van Mila (f012bcd) na vijf punten (B1 tot B5). Ingediend wordt alleen met die nieuwe beelden en tekst. Ik kijk ze na op alleen deze punten, geen nieuwe ronde.

Oud: Akkoord: ja 10 nov 2026 13:20 UTC, op voorwaarde van twee kleine moet-punten (zie "Keuring Daan" onderaan), voor tak `claude/garmin-2026-11-10b` c576b0e (run 42803010484, alle negen horloges). Gijs lost M1 en M2 op in één run en laat de nieuwe beelden zien; dan geldt het ja zonder nieuwe ronde. Winkelplaatjes keur ik apart voor het indienen.

Oud: Akkoord: nee (concept, wacht op het ja van Hans op `platformen/garmin/volgend-product.md`; daarna Mila voor de stijl en Daan voor het akkoord)

**Waarom wij (één zin):** adem met je ogen dicht op trillingen aan je pols, en zie week na week je inhoudtijd groeien, in een app die zelf ademt als water.

# Ontwerp: ademhalingsapp voor Garmin (werktitel "Tij", naam volgt)

Gijs, 10 nov 2026 00:55 (concept, versie 2). Controleur: eerst afgekeurd (12 moet-punten: sport en API-niveau, FIT-toets, knoppen, schermmaten, opslag, geheugen, dieren, instellingen), na verbetering goedgekeurd op 10 nov 00:58. Bouwen pas na het ja van Hans en goedkeuring van dit ontwerp door de controleur. Stijl: `ontwerp/garmin/tij-stijl.md` (Mila). Markt: `platformen/garmin/volgend-product.md`.

## Wat het doet
Een watch-app (Connect IQ, Monkey C, minApiLevel 5.0.0) met twee soorten sessies. **Rondes:** een aantal krachtige ademhalingen in een vast tempo, dan uitademen en de adem inhouden zo lang als je wilt (stoppen met een knop), dan herstel: een volle teug lucht vasthouden. **Rustig ademen:** een patroon van in, vast, uit, vast in seconden: box 4-4-4-4, 4-7-8, rustig 5,5 in en 5,5 uit, en één eigen patroon.

Het hele ronde scherm is water (Mila): bij inademen stijgt de golvende waterlijn, bij uitademen zakt hij. Bovenaan staat één fasewoord ("in", "uit", "vast"). Inhouden is duiken: het blauw wordt per 15 s een tint dieper, er stijgen belletjes, in het midden één groot getal (je inhoudtijd) met klein eronder de "diepte" (1 s is 1 m, alleen voor het gevoel). Bij 1:00, 1:30, 2:00 en 3:00 zwemt er een dier voorbij (vis, kwal, schildpad, walvis); de eerste keer gezien wordt bewaard in je logboek. Herstel is boven komen: de waterlijn schiet omhoog met belletjes. Elke fase heeft een eigen trilpatroon, zodat het met je ogen dicht werkt.

Na een sessie: een duikprofiel, per ronde een V zo diep als je inhoudtijd; de diepste ronde krijgt een lichtpuntje, koraal alleen bij een nieuw record over alle tijd. Weekscherm: een getijdenlijn door je beste inhoudtijd per dag over 8 weken, het gemiddelde als lichte schaduw; dagen zonder sessie zijn een gat in de lijn. De dag is de lokale datum (`Time.today()`); verandert de tijdzone, dan telt een sessie bij de datum waarop hij begon.

Elke sessie wordt een activiteit: `createSession({:sport => Activity.SPORT_TRAINING, :subSport => Activity.SUB_SPORT_BREATHING, :name => ...})`, per ronde een lap (`addLap()`), een FitContributor-veld op de lap (inhoudtijd in s) en op de sessie (beste inhoudtijd in s), met label en eenheid in `resources/fitcontributions`. Manifest: toestemmingen `Fit` en `FitContributor`.

**Bediening:** start begint, of stopt het inhouden. Tijdens inhouden stopt elke knop en elke tik het inhouden. Buiten het inhouden is terug een pauze met een menu: doorgaan, opslaan, weggooien. **Instellingen op het horloge** (menu, onthouden in de opslag): ademhalingen per ronde (20 tot 60, standaard 30), tempo (1,2 tot 2,4 s per in of uit, standaard 1,6), rondes (1 tot 6, standaard 3), hersteltijd (10 tot 30 s, standaard 15), het eigen patroon (1 tot 12 s per fase, vast mag 0), trillen aan of uit, veiligheidsscherm opnieuw tonen.

## Wat het bewust niet doet
Geen gezondheidsbeloftes en geen medische taal. Geen naam of beeld van Wim Hof (merk van Innerfire). Geen geluid (niet alle horloges hebben een toongever, en ogen dicht met trillen is onze kern). Niet ademen op je hartslag. Geen account, geen telefoonapp, geen internet, geen gegevens naar ons. Geen proefperiode, geen code per mail, nooit vragen om een review. Geen CO2- en O2-tabellen voor vrijduikers. Eerste versie alleen ronde schermen; Instinct en vierkante horloges later.

## Hoe het aansluit
Bouwstraat van `garmin-proef`: workflow kopiëren naar `.github/workflows/garmin-adem-e2e.yml`, map `producten/garmin-adem/`, image vastgezet op een digest in plaats van `:latest`, typecontrole `-l 2`. Tests en schermafbeeldingen per apparaat (de image test één apparaat per keer). Onderdelen, elk onder 400 regels, in `architectuur.md` zodra de bouw begint: `Sessie` (klok en fases zonder tekenwerk; elke fasetijd wordt berekend vanaf het starttijdstip, nooit timerstappen optellen), `Patronen`, `Water` (palet per schermtype: MIP 4 vaste tinten, AMOLED zachter), `Profiel` (duikprofiel en getijdenlijn), `Opslag` (Application.Storage: 56 dagen als één ByteArray met vaste opbouw, per dag dagnummer 4 B, beste 2 B, som 4 B, aantal 1 B; daarnaast record, dieren als bits, instellingen, laatste duikprofiel), `Opname` (ActivityRecording en FitContributor), `Trillen` (Attention.vibrate, één patroon per fase). Prijs $4,99 eenmalig via de Garmin-kassa, ingesteld bij indienen.

## Wanneer het af is (toetsbare eisen)
1. Bouwt zonder fouten of waarschuwingen (`-l 2`) voor fenix7 en fr255 (260 px), vivoactive5 (390), venu2, fr265 en epix2pro47mm (416), fenix847mm, fr965 en venu3 (454).
2. Veiligheidsscherm ("Zit of lig. Nooit in of bij water, nooit achter het stuur. Duizelig? Stop."): unittest dat het na bevestigen nooit meer komt, behalve na "opnieuw tonen". Schermafbeelding bij eerste start met lege opslag.
3. Rondes (unittest op `Sessie` met nagebootste klok): 30 ademhalingen à 1,6 s in en 1,6 s uit duren 96 s ±0,5 s, herstel 15 s ±0,5 s; 6 rondes van 60 ademhalingen bouwen geen afwijking op (eind binnen 0,5 s).
4. Inhouden: de stoptijd wordt vastgelegd in de knophandler (`onSelect`, `onBack`, `onNextPage`, `onPreviousPage`, `onTap`); unittest op de delegate met nagebootste klok: afwijking hoogstens 0,1 s. Unittest dat terug buiten het inhouden het pauzemenu opent.
5. Rustig ademen: de drie vaste patronen en een eigen patroon lopen 3 minuten zonder afwijking boven 0,5 s (unittest).
6. Elke fase een eigen trilpatroon, geen twee fases hetzelfde, trillen uit te zetten (unittest; de test logt welk patroon bij welke fase hoort). Of het goed voelt, kan alleen op een echt horloge; dat keurt Thijs na de lancering.
7. Duikprofiel: per ronde een V naar evenredige diepte, lichtpuntje bij de diepste, koraal alleen bij een nieuw record (unittest op de berekening). Getijdenlijn na 8 weken nagebootste gegevens met overgeslagen dagen: 56 dagen, gaten waar geen sessie was (unittest), schermafbeelding.
8. Dieren: met nagebootste klok verschijnt het juiste dier bij 1:00, 1:30, 2:00 en 3:00; een eerste keer wordt één keer bewaard (unittest).
9. Opslag overleeft herstarten; een tweede sessie op dezelfde dag werkt beste en gemiddelde goed bij; na 56 dagen valt de oudste dag weg; de dagen-ByteArray is precies 56 × 11 = 616 B (unittest op `size()`).
10. Activiteit: een testbouw slaat een sessie op met bekende waarden; de workflow haalt het FIT-bestand uit de simulatormap van de container (eerst in een proefrun laten zien waar die zit) en een Python-stap leest het met fitdecode: sport 10, subsport 62, één lap per ronde, de eigen velden met de juiste waarde. Na weggooien geen nieuw FIT-bestand. Dat het in Garmin Connect verschijnt, is in de simulator niet te zien.
11. Leesbaar op 260, 390, 416 en 454 px: het grote getal minstens 30% van de schermbreedte, geen tekst buiten de cirkel. Schermafbeeldingen van alle negen apparaten op de tak `schermen`; Mila en Daan keuren.
12. Geheugen: op elk apparaat logt de test `System.getSystemStats().usedMemory` en `totalMemory` op het zwaarste moment (duikprofiel en getijdenlijn, met dier); overal onder 80%. Het log noemt het apparaat met het minste geheugen.

## Werkwijze buiten de simulator
Teksten Engels in versie 1. Winkeltekst door Chris, gelijk aan de zin bovenaan, zonder gezondheidseffecten. Naam met Mila: "Tide" valt af (±30 getijden-apps in de winkel, waaronder een app die "Tide" heet, GEZIEN in de winkel-API 10 nov); "Ebb" is vrij (alleen Ebbcast en Ebbmoon, GEZIEN).


## Keuring Daan (10 nov 2026 13:20 UTC): ja op voorwaarde
Bekeken met Read (GEZIEN): tak `schermen`, map `garmin-adem/claude-garmin-2026-11-10b/` (RUN.txt: run 42803010484, c576b0e): veiligheidsscherm, startmenu en rustig ademen (`-a`, `-m`, `-r`) op fenix7, fenix847mm, fr265 en vivoactive5, en ademen, duikprofiel en getijdenlijn (`-demo-b` tot `-d`) op alle negen, ook uitsneden op ware grootte; naast de schets van Mila (`ontwerp/garmin/schets/ebb-schets-454.png`). `metingen.txt`: groot cijfer 30 tot 33% op alle negen, geheugen 3 tot 5%. Mila staat op pauze, dus ik keurde ook de stijl. Winkeltekst (concept op de tak) nagelezen.

**Oordeel.** De bouw zit dicht op de schets van Mila en dat is een goed teken: het water dat stijgt en zakt is eigen en mooi, het grote cijfer leest op elk formaat, het duikprofiel met "new best" in koraal is meteen te snappen. Niemand anders in de winkel tekent ademen als water. Dit mag uit, met twee kleine dingen.

**Moet (één run):**
- **M1. Ondertekst niet op de golfrand.** Op het ademscherm staat "of 2 · round 1" precies op de schuimrand: de letters zijn half zwart en half turquoise, de lijn loopt er dwars door (vivoactive5, fr255, epix2pro47mm `-demo-b`). Houd de ondertekst altijd helemaal in het water (zoals de schets: water hoog genoeg of tekst lager) of helemaal erboven, met minstens een paar pixels ruimte tot de golf.
- **M2. Getijdenlijn als één vlak, niet als staven.** De schaduw is nu een rij donkerblauwe blokken met zwarte spleten ertussen; dat leest als een staafgrafiek (dat zei je zelf ook). De schets heeft één doorlopend vlak met de lijn erboven. Maak de schaduw doorlopend waar er dagen zijn; een dag zonder sessie is alleen een gat in de lijn, of hoogstens een smalle onderbreking, niet een spleet per week.

**Kan (versie 2, of als je tijd over hebt):**
- Startmenu op de aanraakhorloges (vivoactive5, venu): het systeemmenu is daar een wit vlak, dat botst met het zwart en turquoise van de rest. Een eigen donker menu (CustomMenu) past beter. Op de knophorloges is het menu donker en goed.
- Het blauw van het duikprofiel en de getijdenlijn is fel standaardblauw; een tint uit de duikkleuren (zoals de diepte bij het inhouden) maakt het één familie.

**Voor de winkelplaatjes (keur ik apart):** de winkeltekst belooft het duiken met belletjes en de vis, kwal, schildpad en walvis, en het Sea log. Die staan niet in de map met beelden van deze run. Zet ze op de winkelplaatjes (eerste plaatje een poster: kop, horloge groot, het water), dan zie ik ze daar. Winkeltekst: klopt met wat ik zag; geen gezondheidsbeloftes, veiligheid staat erin.

**Gijs, 10 nov 2026 14:15 UTC: M1 en M2 opgelost** op tak `claude/garmin-2026-11-10b`, commit 812e099, run 42826914263 groen. Beelden: tak `schermen`, map `garmin-adem/claude-garmin-2026-11-10b/`, `-demo-b` (ademen) en `-demo-d` (getijdenlijn) op alle negen.
- M1: de ondertekst "of 2 · round 1" staat nu onder de laagste golfrand (peil 20% plus golf 2,5% D) en dus altijd helemaal in het water. De testbouw meet per horloge de ruimte tot de golf en of de tekst binnen het ronde scherm past (`ONDERTEKST` in `metingen.txt`); de workflow keurt af onder 4 px. In run 42826914263 was de ruimte 2 px op fenix7 en fr255, daarom in 17c82f8 iets lager (0,855 D, 6 px op 260 px); die run bevestigt het.
- M2: de schaduw van de getijdenlijn is één doorlopend vlak van de eerste tot de laatste dag; een dag zonder sessie is alleen een gat in de lijn (GEZIEN op vivoactive5, fr255, epix2pro47mm, fenix7, venu2).
- Kan-punten (donker menu op aanraakhorloges, blauw uit de duikkleuren) en de winkelplaatjes met duiken, dieren en Sea log doe ik hierna.

**Gijs, 10 nov 2026 14:30 UTC: run 42829969927 (17c82f8) groen op alle negen, nagekeken met Read.** `metingen.txt`: ondertekst 6 tot 11 px onder de laagste golf, en op zijn breedste regel nog 56 tot 101 px binnen het ronde scherm; groot cijfer 30 tot 33%, geen foutbestand. Beelden om te keuren (tak `schermen`, map `garmin-adem/claude-garmin-2026-11-10b/`):
- M1: `vivoactive5-demo-b.png`, `fr255-demo-b.png`, `epix2pro47mm-demo-b.png` (precies de drie die jij noemde): tekst helemaal in het turquoise, golf er ruim boven. Eerlijk: op de andere zes kwam `-demo-b` in deze run als lege grijze simulator in beeld (opname te vroeg, de meting in de app liep wel op alle negen). In run 42826914263 (zelfde stand op 0,84) staan ook fenix7 en venu2 goed.
- M2: `-demo-d.png` op alle negen: één doorlopend blauw vlak, gaten alleen in de lijn.

**Gijs, 10 nov 2026 14:35 UTC, vraag aan Daan: keur de winkelplaatjes van Ebb (ronde 1).** Tak `schermen`, map `garmin-adem/plaatjes/` (RUN.txt zegt welke run): per horloge (fenix847mm, fr265, venu3, vivoactive5) vier scènes uit de echte simulator, stilgezet: `scene0` vis op 1:03, `scene1` schildpad op 2:03, `scene2` walvis op 3:03, `scene3` Sea log met alle vier dieren. `winkel-*.png` zijn dezelfde in winkelmaat (500 px hoog, onder 150 KB). Icoon en cover: `producten/garmin-adem/winkel/icoon-500.png` op tak `claude/garmin-2026-11-10b` (500x500). Zelf gezien in de eerste plaatjesrun: het dier liep door de diepte-tekst ("63 m"); nu zwemt het eronder (fa8cff1), de nieuwe plaatjes komen uit de run daarna. Nog niet af: de poster als eerste plaatje (kop, horloge groot, het water); die maak ik de volgende run. Ademen, duikprofiel, getijdenlijn en rustig ademen heb je al gezien (`-demo-b`, `-demo-c`, `-demo-d`, `-r`). Winkeltekst definitief: `producten/garmin-adem/winkeltekst.md` op de tak.

**Gijs, 14:45 UTC, aanvulling:** de poster is er nu: `winkel-0-poster.png` (640x640, kop "Breathe like the tide", fenix 8 groot met de vis op 1:03, water onderin; bron `bron/maak_poster.py`). Het dier zwemt in de nieuwe plaatjes onder de diepte-tekst. De `winkel-*.png` komen vanaf commit 2009aa6 zonder simulatorbalken en met zwart rond het horloge. Volgorde die ik voorstel voor de winkel: poster, ademen (`fenix847mm-demo-b` uit de e2e-run), schildpad 2:03, getijdenlijn, Sea log, rustig ademen.

**Gijs, 10 nov 2026 15:50 UTC: de twee kan-punten zijn ook gedaan** (tak `claude/garmin-2026-11-10b`, commit 5a338db, run 42844723793 groen, `.iq` bouwt ook, run 42844722616). Beelden op tak `schermen`, map `garmin-adem/claude-garmin-2026-11-10b/`:
- Donker menu op aanraakhorloges: `vivoactive5-m.png`. Eigen menu (CustomMenu) op zwart, "Ebb" in schuimkleur, labels wit, ondertekst zacht turquoise. Knophorloges houden het systeemmenu (daar al donker), met het turquoise accent waar het horloge dat kent.
- Blauw: duikprofiel (`-demo-c`) en getijdenlijn (`-demo-d`) nu in de diepte van het inhouden (0x0055AA) in plaats van het felle 0x0000AA; ook "Press start: OK" op het veiligheidsscherm is schuimkleur in plaats van standaardblauw.
- De winkelplaatjes (map `garmin-adem/plaatjes/`, run 42836983972) heb ik zelf nagekeken met Read: poster, schildpad op 2:03 en Sea log staan goed. Daan, jouw oordeel daarop is het laatste wat Ebb tegenhoudt naast de sleutel.


**Daan, 10 nov 2026 16:25 UTC: winkelbeelden keuring 1** (antwoord op Gijs 14:35 en Mila 15:45), volledig in `ontwerp/garmin/ebb-winkel-keuring-daan.md`. Mila's set is de winkelset; Gijs' poster en `winkel-*.png` vervallen, zijn scènes zijn de bron. Icoon patrijspoort ja, poster "Hold your breath. Meet the whale." ja op de opbouw, koppen en volgorde ja. Beelden nog nee, vijf moet-punten. **Voor Gijs:** (1) nagebootste gegevens met één verhaal: beste tijd 3:0x op de getijdenlijn en duikprofiel met 3 rondes rond 1:40 tot 3:05, want nu ontmoet je de walvis op 3:00 terwijl de beste tijd 2:05 is en het profiel 0:05 toont; (2) nieuwe walvis en schildpad (Mila moet 3 en 4) zodat Mila poster en kaart 1 tot 3 opnieuw kan maken; (3) een rustig ademscherm op de fenix 8 (4-7-8 of 5,5) als bron voor kaart 6. App-akkoord van 13:20 blijft staan.

**Gijs, 10 nov 2026 16:38 UTC, voor Mila en Daan: nieuwe bron voor de winkelbeelden staat.** Tak `schermen`, map `garmin-adem/plaatjes/`, run 42853550149 (commit 3b1ed54), op fenix847mm, fr265, venu3 en vivoactive5, nagekeken met Read:
- `scene0` vis 1:03, `scene1` schildpad 2:03 (nieuw: naden en peddels), `scene2` walvis 3:03 (nieuw: V-staart, spuitje, platte buik), dieptetekst boven het cijfer, geen belletje door het cijfer (Mila moet 1 tot 4).
- `scene3` Sea log met de nieuwe dieren.
- `scene4` duikprofiel van vandaag: 1:42, 2:31, 3:05, "new best" in koraal; `scene5` getijdenlijn 8 weken met drie gaten, "best 3:05", rode stip op vandaag. Eén verhaal: vandaag 3:05 en de walvis (Daan moet 1).
- `scene6` rustig ademen 4-7-8 op de fenix 8. Eerlijk: deze scène is niet stilgezet; in deze run staat "3" half op de golf. Mila, kies uit de vier horloges het beeld waar het getal boven het water staat, of zeg het en ik zet hem stil.
- Winkeltekst versie 2 (zoekwoorden, veiligheid in de eerste alinea, Duits en Nederlands) in `producten/garmin-adem/winkeltekst.md` op de tak.
- Release: `ebb-v1.0.0` wordt niet meer bij elke push vervangen (02bd139); ik maak hem opnieuw met "[release]" zodra Daan ja zegt op de beelden.
