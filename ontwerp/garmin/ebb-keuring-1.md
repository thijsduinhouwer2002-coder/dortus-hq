# Ebb, keuring 1 van Mila (10 nov 2026, ±15:40 UTC)

Gekeurd op: simulatorbeelden van run 42836983971 (commit 2009aa6, tak `claude/garmin-2026-11-10b`, map `garmin-adem/claude-garmin-2026-11-10b/` op `schermen`) en de winkelplaatjes van run 42836983972 (`garmin-adem/plaatjes/`). Alles bekeken met Read, op ware maat en vergroot.

**Oordeel: stijl ja, met vijf moet-punten.** De duik met het dier is de haak en hij zit erin: een koraalrood visje in al dat donkerblauw zie je met een halve blik op je pols, en "123 m" onder een grote tijd is een grapje dat je snapt zonder uitleg. Geen enkele concurrent heeft dit (die zijn kale tekst of een cirkel). Het grote cijfer haalt overal 30 tot 33% (GEZIEN in `metingen.txt`). Wat nog niet af is, staat hieronder op volgorde.

## Vraag 3 van Gijs (cijferletter): overrule, op alle negen
Barlow Condensed Medium **op alle horloges**, niet alleen op de epix. Waarom: het cijfer is het grootste ding op elk scherm, dus het is ons gezicht; met een systeemletter op acht horloges en Barlow op één ziet Ebb er per horloge anders uit. Geheugen is geen bezwaar (hoogste 4 tot 6%, GEZIEN). Maat: dezelfde 31% van de breedte als nu op de epix.

## Moet
1. **Dieptetekst raakt het cijfer** (fenix847mm, "123 m" plakt onder "2:03"; ook bij 1:03). Zet hem minstens 4% D onder de onderkant van de cijfers, of boven het cijfer. Het dier zakt mee zodat het niet door de tekst zwemt.
2. **Belletjes over het cijfer heen.** De kringetjes gaan nu vóór de "2" en de "0" langs (fenix847mm en fr265). Teken de belletjes vóór het cijfer in `Teken.mc`, zodat ze erachter langs gaan. Water, belletjes, dier, dan pas tekst.
3. **De walvis leest als een grote vis.** Op 3:00 is het hetzelfde silhouet als het visje, alleen groter. Maak het een walvis met drie dingen die je klein ziet: (a) een **staart als een liggende V** (twee punten naar boven en onder, niet de visstaart), (b) een **spuitje**: drie korte streepjes of een kleine fontein in 0x55AAFF boven de kop, (c) een **platte buik**: onderkant recht, bovenkant bol, kop stomp. Dat spuitje onder water is de grap, niet erg als het niet klopt.
4. **De schildpad leest als een varkentje of kever.** Geef het schild twee of drie lijnen in de waterkleur (0x000055) door het koraal, zodat er vakjes in komen, en maak de vier pootjes plat als peddels die schuin naar achteren wijzen. Kop iets verder naar voren. Op de lijst "met so far" geldt hetzelfde.
5. **Startmenu op vivoactive5 is wit** (systeemthema licht). Dat breekt de patrijspoort meteen bij het openen. Teken het menu zelf (`WatchUi.CustomMenu` met eigen `drawBackground`/`drawTitle`, of een eigen lijstscherm): zwarte achtergrond, gekozen regel met een golfje 0x00FFFF eronder, titel "Ebb" in Barlow. Dan is het menu op elk horloge hetzelfde en van ons.

## Kan
- Titel "Ebb" in het menu met een klein golflijntje erachter, zoals de waterlijn: het eerste wat je ziet als je de app opent.
- Duikprofiel: "0:05" staat tegen de stip aan; schuif de tijd 2% D verder naar links.
- Getijdenlijn: leest goed. Let op dat de gaten alleen vallen op dagen zonder sessie; in de nagebootste 8 weken ziet de lijn er overal gestippeld uit. In het echt eerlijk, voor de winkelplaatjes liever een week of acht met 2 tot 3 gaten.
- Icoon (`winkel/icoon-500.png`): helder en rustig, maar het mist de haak. Zet het koraal visje in het water (klein, rechts onder het midden). Dan staat in het icoon al wat Ebb anders maakt.

## Winkelplaatjes en poster
- Poster "Breathe like the tide": goed begin, maar het horloge is klein en de grap ontbreekt. **Voorstel:** het horloge groot op 3:03 met de walvis (na moet 3), kop **"Hold your breath. Meet the whale."** en eronder klein "Breath-hold rounds · calm patterns · your sea log". Eerlijk, want de walvis komt echt op 3:00. Dat is waar iemand stopt met scrollen.
- Volgorde van de plaatjes: poster, 1:03 met vis, 2:03 met schildpad, "met so far", duikprofiel, getijdenlijn, ademen (water). Het menu niet in de winkel.

Daan heeft het eindakkoord; dit is mijn stijlkeuring, geen `Akkoord`.
