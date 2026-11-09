Akkoord: nee (concept, wacht op het ja van Hans op `platformen/garmin/volgend-product.md`; daarna Mila voor de stijl en Daan voor het akkoord)

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
