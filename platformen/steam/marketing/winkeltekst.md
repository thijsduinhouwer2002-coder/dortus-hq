# Korte winkeltekst: wat de winnaars doen (Sem, run 10, 16 nov 2026)

Waarom nu: Thijs schrijft de winkeltekst zelf en moet hem vóór ma 30 nov af hebben (vertaling, `talen.md`). Dit is de meetlat waarmee hij snel kan schrijven. De voorstellen staan als CONCEPT in `platformen/steam/teksten-thijs.md` (Z5).

## Gemeten
Script `data/winkeltekst.py`, uitkomst `data/winkeltekst-2026-11-16.csv` (GEZIEN 16 nov ±20:55 UTC, openbare appdetails, Engels). 47 spellen in vier groepen: 13 winnaars en 4 kerkerflops (lijst van Fenna, verhaal 8), 10 aangekondigde spellen met 20+ spelers tegelijk in de demo en de eerste 20 die op Hats lijken met 0 spelers (nulmeting 16 nov).

| | Winnaars (13) | Kerkerflops (4) | Demo 20+ (10) | Demo 0, lijkt op Hats (20) |
|---|---|---|---|---|
| Woorden korte beschrijving (mediaan) | 36 | 42 | 42,5 | 38,5 |
| Noemt de plek (scherm, bureaublad, taakbalk, hoek) | **12** | 4 | 8 | 16 |
| Noemt "idle" | **10** | 3 | 6 | **4** |
| "idle" al in de eerste zin | 7 | 3 | 5 | 4 |
| Vorm "zit, leeft of speelt op [plek]" | **8** | 1 | 3 | 6 |
| Noemt toetsaanslagen of muis | 0 | 1 | **5** | 2 |
| Noemt "dungeon" | 0 | 2 | 0 | 0 |
| Talen (mediaan) | 11 | 3 | 7,5 | 4,5 |
| Schermafbeeldingen, filmpjes (mediaan) | 8, 1 | 9, 1 | 10, 1 | 8, 1 |

## Wat ik eruit haal (eerlijk)
1. **De plek noemen is de norm, geen onderscheid**: ook 16 van de 20 stille demo's doen het. Het moet erin, maar het maakt het verschil niet.
2. **Wat winnaars wel vaker doen: zeggen wat voor spel het is ("idle") en waar het zit, in één zin van ±16 woorden.** Rusty: "A relaxing idle-farming simulator that sits at the bottom of your screen while you do other things." (17). Desktop Defender nam die vorm bijna letterlijk over: "An idle auto-battler that sits in the corner of your screen while you do other things." (16). Ropuka, Cozy Mining, Black Cat en Cornerpond doen hetzelfde. 10 van 13 winnaars noemen "idle", tegen 4 van 20 stille demo's. GOK over de oorzaak: wie in de zoeklijst of een festrij langs scrolt, moet in één regel weten wat het is.
3. **De haak staat bij de winnaars in zin twee**, na de soort en de plek (Cozy Mining: "Click to send your miner digging", Black Cat: "Help the black cat study ancient tomes"). Voor ons dus: eerst "idle dungeon op je taakbalk", dan de hoed.
4. **"Dungeon" staat bij 0 winnaars en bij 2 van de 4 kerkerflops** (Idle Squire, Dungeoneers Idle). Vier flops is te weinig voor een regel (GOK), maar het past bij wat Fenna zag: kerkerspellen zijn een vol vak. Ons woord voorop is dus "idle", en het verschil zit in de hoed en Gloop.
5. **Nieuw bij de demo's met 20+: 5 van de 10 groeien op je toetsaanslagen** (Character House, Little Writer, Hamster Time, Widget Idle, Keyboard Farm), bij de winnaars 0. Dat is een nieuwe golf van "productiviteitsmaatjes" uit 2026. Hats doet dat niet en dat hoeft niet; ik meld het aan Sanne als observatie, geen voorstel.
6. **Talen**: winnaars mediaan 11, stille demo's 4,5. Past bij `talen.md` (Chinees eerst).

## Recept voor Thijs (voorstel, CONCEPT)
- **Zin 1 (±16 woorden):** soort ("idle") plus plek ("on top of your taskbar" of "at the bottom of your screen"), plus "while you work" of iets gelijks.
- **Zin 2:** de haak: held valt, hoed op Gloop, wie ontsnapt komt terug met wrok.
- **Zin 3 (mag weg):** de belofte voor wie het laat draaien, eerlijk (Z1 of Z2).
- Samen ±35 woorden, net als de mediaan van de winnaars. Geen "dungeon" als eerste zelfstandig naamwoord, geen "tiny dungeon".

## Lange beschrijving (run 10, vervolg)
Script `data/winkeltekst_lang.py`, uitkomst `data/winkeltekst-lang-2026-11-16.csv` (GEZIEN 16 nov ±20:50 UTC, dezelfde 47 spellen). "Bewegend" telt gifs en filmpjes in de tekst.

| | Winnaars (13) | Kerkerflops (4) | Demo 20+ (10) | Demo 0, lijkt (20) |
|---|---|---|---|---|
| Woorden (mediaan) | **207** | 296 | 246 | 235 |
| Met bewegende beelden in de tekst | 12 | 4 | 9 | 17 |
| Bewegende beelden (mediaan) | 3 | 3,5 | 5 | 4 |
| Kopjes (mediaan) | 4 | 6,5 | 3 | 4 |

Lezing: bewegende beelden in de tekst doet bijna iedereen, dus dat is de norm. Winnaars schrijven iets korter (mediaan 207 woorden; Cornerpond 105, Desktop Defender 134, Black Cat 144). Kopjes zijn korte daden ("Cut grass", "Level up and unlock", "Unlock New Species"), geen verhaal. **Recept: ±200 woorden, 3 tot 5 gifs, 4 korte kopjes, elk kopje een gif en twee zinnen.** Dat past bij wat Thijs wil (minder tekst, meer beeld) en scheelt hem schrijfwerk. De gifs vraag ik aan Chris en Mila.

## Tags (run 10, vervolg)
Script `data/tags.py`, uitkomst `data/tags-2026-11-16.csv` (GEZIEN 16 nov ±20:55 UTC, de tags zoals de winkelpagina ze toont, op volgorde; let op: die volgorde komt deels van stemmen door spelers, de maker zet alleen de beginlijst).

| Tag | Winnaars (13) | Demo 20+ (10) | Demo 0 (20) | Ons voorstel (`ontwerp/steam/winkelpagina/teksten.md`), plek |
|---|---|---|---|---|
| Idler | 13 (12 in top 5) | 9 | 16 | 2 |
| Desktop Companion | 13 (11 in top 5) | 8 | 16 | 1 |
| Casual | 13 | 8 | 18 | 5 |
| Relaxing | 11 | 7 | 17 | 8 |
| Cute | 10 | 6 | 13 | 7 |
| Singleplayer | 10 | 9 | 16 | 15 |
| Incremental | 9 | 6 | 10 | 12 |
| Simulation | 8 | 8 | 13 | 17 |
| 2D | 7 | 7 | 16 | 14 |
| 3D | 0 | 3 | 0 | niet |
| Funny, Comedy, Villain Protagonist, Cartoony, Stylized | 0 | 0 | 0 | 4, 10, 9, 20, 3 |

Lezing: de kern (Idler, Desktop Companion, Casual) hebben alle 13 winnaars; dat is de toegang tot de rij "meer zoals dit" en de festfilters, geen onderscheid. Onze eigen tags (Funny, Villain Protagonist) heeft geen enkele winnaar; die maken ons anders, maar horen na de kern. **Fout gevonden in ons voorstel: "2D" staat erin, terwijl het spel sinds 13 nov 3D gerenderd is** (Olaf, zelfde bestand regel 93). Voorstel aan Sanne (haar bestand): **1 Desktop Companion, 2 Idler, 3 Casual, 4 Relaxing, 5 Cute**, dan Incremental, Singleplayer, Funny, Villain Protagonist, Management, Cozy, Simulation, Fantasy, Building, 3D (in plaats van 2D), daarna de rest. Waarom: filters kijken naar de eerste 15 (DERDEN, Valve-docs), en de vijf bovenste zijn precies wat 10 tot 13 van de 13 winnaars hebben.
