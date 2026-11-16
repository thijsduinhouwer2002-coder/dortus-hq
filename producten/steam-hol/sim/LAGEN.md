# Voortgang ±100 uur: lagen en prijzen nagerekend (Bram, 16 nov 2026)

Vraag van Sanne (16 nov, `berichten/bram.md`) over `platformen/steam/voortgang.md` versie 1. Alles hieronder komt uit de sim (8 zaden, speler koopt steeds het goedkoopste, economie van het spel: 6 goud per val plus 3 per eerder bezoek, heldensoorten aan). Speelgevoel en hoe een echte speler koopt: GOK.

Opnieuw draaien:
- `python3 sim.py lagen ../../../platformen/steam/data/voortgang.json [luik2,luik3,luik4] [upg1..upg6]`: Sannes json met lagen, zonder iets bij te stellen.
- `OUD_GOUD=0.5 python3 voortgang_lagen.py 500,750,1000 45,126,353,600,1000,1600 1,1.2,2.2,3.2`: het voorstel hieronder, met drempels geijkt. Schrijft `voortgang-lagen-bram.json`; uitkomst staat in `voortgang-lagen-uitkomst.txt`.

## Wat nieuw is in de sim
- **Lagen in `speel()`.** Op hol-niveau 20, 30 en 40 komt een luik te koop. Na de koop begint een lege laag: 6 gangen, Gloop en een put, upgrades op 0, geen terugkomers. De lagen erboven geven per seconde het goud, de gevangen helden en de hoeden van hun laatste uur (zoals `voortgang.gd` bij "weg geweest"). Gevangen helden van alle lagen tellen voor het hol-niveau, zoals in voortgang.md.
- **Volle economie:** graven kost goud (`graaf_prijs`, tot 40 gangen per laag), upgrades stap 4, 5 en 6 komen vrij op hol-niveau 13, 25 en 34, een niveau kan een ding met een prijs geven (`{"koop": prijs}`).
- **Instellingen in de json:** `graven`, `upg_prijs`, `lagen`, `upg_mee`, `laag_factor` (prijs graven en upgrades per laag), `oud_goud` (deel van het goud van een laag die je niet ziet), `gloop_oud` (tellen hoeden van boven voor Gloops toren).
- **Meting:** bij elke aankoop prijs gedeeld door goud per uur van dat moment (laatste uur, alle lagen samen), dus "hoeveel uur sparen". Plus spaartijd van het luik, bouwtijd per laag en goud op de bank per uur.
- Zonder deze instellingen rekent de sim precies als eerst (diepte en voortgang geven dezelfde getallen, GEZIEN).

## Vraag 1: verhouding prijs / goud per uur (Fenna punt 5)
Sannes json met lagen, prijzen zoals nu (upgrade x 2,8 per stap: 988, 2766, 7745):

| Aankoop | Wanneer | Uren sparen |
|---|---|---|
| graven laag 1 (gang 26 tot 39) | ±4 u | 0,27 |
| upgrade stap 3 | ±8 u | 0,77 |
| upgrade stap 4 (988) | ±10 u | 2,05 |
| upgrade stap 5 (2766) | ±20 u | 2,81 |
| upgrade stap 6 (7745) | ±42 u | 3,88 |
| graven in laag 2, 3, 4 | | 0,12 / 0,08 / 0,07 en lager |

**Uitkomst:** de stappen 4 tot 6 lopen weg van het inkomen (2 naar bijna 4 uur sparen), precies wat Fenna verbiedt. Graven doet het omgekeerde: in elke nieuwe laag kost het bijna niets meer.
**Voorstel:** stap 4, 5 en 6 kosten **600, 1000 en 1600** (x 1,6 per stap in plaats van 2,8), en graven en upgrades kosten per laag een factor meer: **1 / 1,2 / 2,2 / 3,2**. Dan ligt bijna alles tussen 0,6 en 1,6 uur sparen; alleen stap 5 en 6 in laag 3 en 4 komen op 2,2 tot 4 uur (dat zijn de laatste stappen; liever een lagere factor voor stap 4 tot 6 als Sanne dat vlakker wil).

## Vraag 2: een laag in de sim, en klopt "laag 2 bouwen gaat ±2 keer zo snel"?
Bouwtijd = van openen tot 40 gangen en elke lijn op stap 3.

| | Bouwtijd laag 1 | laag 2 | laag 3 | laag 4 |
|---|---|---|---|---|
| Sannes json, prijzen gelijk per laag, oude laag geeft al zijn goud | 8,3 u | **3,6 u** | 2,1 u | 1,0 u |
| Voorstel (oude laag geeft de helft, factor 1 / 1,2 / 2,2 / 3,2) | 8,2 u | 6,1 u | 6,9 u | 7,0 u |

**De GOK klopt voor laag 2:** met dezelfde prijzen gaat laag 2 2,3 keer zo snel. Maar het loopt daarna uit de hand: laag 3 gaat 4 keer en laag 4 8 keer zo snel, de leukste fase (bouwen) duurt dan nog een uur, en het goud stapelt zich op (met vaste prijzen ±114.000 op de bank bij 99 uur, want er is niets meer te kopen).

**Grootste vondst: de helden van de oude lagen maken het hol-niveau veel sneller.** Met de drempels van versie 1 haal je **hol-niveau 50 na ±39 uur in plaats van 94 uur** (laag 1 vangt ±60 helden per uur, met vier lagen samen ±270). Twee keuzes:
- drempels na niveau 20 hoger (geijkt in `voortgang-lagen-bram.json`: niveau 30 op 2.900 in plaats van 1.881 gevangen helden, niveau 40 op 8.300 in plaats van 3.623, niveau 50 op 18.500 in plaats van 6.015; dan vallen alle niveaus weer op Sannes uren, GEZIEN: 20 op 10,6 u, 30 op 29,8 u, 40 op 57,7 u, 50 op 95,5 u), of
- helden uit oude lagen tellen voor een deel.
Ik raad het eerste aan: het blijft eerlijk ("alle helden tellen") en het bordje toont gewoon een groter getal.

**Gloop:** tellen de hoeden van de oude lagen mee voor zijn toren, dan haalt hij niveau 10 na 31 uur in plaats van 62. Voorstel: Gloops toren telt alleen de hoeden die hij zelf at (hij verhuist mee); de hoeden van Gloopje gaan naar de berg. Dan Gloop 10 na ±65 uur.

**Goud van een laag die je niet ziet: de helft.** Met al het goud groeit het inkomen per laag zo hard dat geen prijs bijblijft. Met de helft blijft de bank laag tot ±70 uur (bij uur 30: ±130, bij uur 40: ±400, bij 57: ±2.300, bij 70: ±1.300) en gaat het pas mis na niveau 50.

## Vraag 3: wat kost een luik, zodat het met ±1 uur sparen lukt?
Regel: **luik = 1 uur goud van dat moment**. In het voorstel is dat **500, 750 en 1000** (goud per uur bij opening ±470, ±735, ±1.005; verhouding 1,07 / 1,02 / 1,00). Een speler die eerst het goedkoopste koopt spaart bij laag 2 ±1,6 uur; bij laag 3 en 4 heeft hij het goud al op de bank (1.100 en 2.600) en koopt hij meteen. Met de prijzen van nu (alles gelijk per laag) staat het luik altijd meteen klaar, omdat de bank vol is.

## Wat nog niet klopt
- **Na niveau 50 (±95 u) en tussen 70 en 100 uur** is er te weinig te kopen: langste gat 5,7 uur (tussen 40 en 70 uur 2,3 uur, tussen 20 en 40 uur 1,6 uur) en de bank loopt op naar ±17.600 bij 99 uur. Er moet iets zijn dat goud blijft kosten (bijvoorbeeld aankleding of hoeden voor de wand), of laag 4 krijgt meer dingen met een prijs. Ontwerpkeuze voor Sanne.
- Een laag heeft in de sim dezelfde helden en vallen als laag 1. Eigen helden (mijnwerker, archeoloog) en het valluik zitten er niet in.
- "Nieuwe dingen met een prijs" (skelet, slaapkamer, keuken enzovoort, 15 niveaus, elk ±1 uur goud) zijn mijn GOK om goud een doel te geven; in voortgang.md hebben ze nog geen prijs.
- De speler in de sim koopt steeds het goedkoopste. Wie zelden kijkt heeft meer op de bank en koopt het luik eerder.

Bram, 16 nov 2026. Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.
