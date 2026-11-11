# Ebb blad v10: "Voor Mila" uit keuring bouw 5 (run 34, 11 nov)

Blad `ebb-blad-v10.png`, losse schermen in `blad10/` (260 en 454), bron `bron/blad_v10.py` (tekent met `horloge_sim.py`, dus zoals `DierenData.mc`, met Barlow Condensed uit `bron/fonts/`, OFL). Poster: `blad10/winkel-poster-v3.png`, bron `bron/poster_v3.py`. Meting `blad10/meting-v10.txt`. Dieren: v8.3, vormen niet veranderd.

Eerst bekeken met Read: de echte `einde-sea-complete` op FR255 en fr965 (tak `schermen`, `garmin-adem/plaatjes/namen/`). Op FR255 vallen de twee bogen over elkaar (kluwen) en staan de belletjes boven de kamlijn. Op fr965 is het scherm leeg (dat is punt 3 van Gijs, de opbouw).

## 1. Sea complete: een groepsfoto van je zee
De glimlach van v9 werd op 260 een kluwen. Nieuw: **een klassenfoto.** De walvis is de ster in het midden, de 23 anderen staan er netjes omheen in rijen, zoals op een schoolfoto. Rustig, elk dier los te zien, en de vorm volgt het ronde scherm (rijen worden onderin korter).

Maten in 1/260 van de diameter: x vanaf het midden, y vanaf de bovenkant. Keer D/260 voor elk horloge (op 454: keer 1,746).

| Wat | Waarde op 260 | Op 454 |
|---|---|---|
| Kamlijn (zee begint) | y 58 | y 101 |
| Walvis | x 0, y 100, maat 32 | maat 56 |
| Fontein (3 belletjes, rand in schuim) | (0, 71) straal 3; (-6, 64) straal 2; (5, 62) straal 2 | keer 1,746, straal minstens 2 |
| Vrienden | maat 11 | maat 19 |
| Rij 0 (naast de walvis), y 100 | x -86, -58, 58, 86 (nr 1 tot 4) | |
| Rij 1, y 136 | x -87, -58, -29, 0, 29, 58, 87 (nr 5 tot 11) | |
| Rij 2, y 160 | x -76, -47, -18, 18, 47, 76 (nr 12 tot 17) | |
| Rij 3, y 188 | x -72, -45, -17, 17, 45, 72 (nr 18 tot 23) | |
| "sea complete" | y 18, SemiBold 25, geel FFFFAA | |
| "24 of 24 friends" | y 206, Medium 17, schuim | |
| "12 weeks" (beste reeks) | y 226, Medium 15, schuim | |

y van de tekst is de bovenkant. De dieren staan op hun zwaartepunt (zoals `DierenData.mc` ze al tekent). Volgorde nr 1 tot 23 van links naar rechts, van boven naar onder: zo lees je je hele reis terug.

- **Fontein onder de kamlijn:** alle drie de belletjes liggen tussen y 60 en 74, de kamlijn op 58. Het witte straaltje hoort bij de walvis zelf.
- **Gemeten op pixels** (`overlap_check` in `blad_v10.py`): op 260 en 454 raakt geen dier een ander, ook niet met 1 px marge; 0 dierpixels buiten 0,85 R.
- **Voor de watchdog:** 24 dieren één keer in het plaatje tekenen, zoals keuring punt 3 zegt (walvis eerst, dan per beurt een rij). De rijen zijn daar handig voor: 5 beurten (walvis, rij 0, 1, 2, 3).
- Geen tijden op dit scherm, zoals in v9.

Toets: de groepsfoto is de grap (je hele zee poseert voor je), en het is het rustigste beeld van alle 25 dieren tegelijk. Zwakste: op 260 zijn de vrienden ±26 px breed; herkenbaar als je kijkt, maar het gaat om het geheel.

## 2. Pauzemenu in Ebb-stijl
Nu staat er het witte systeemmenu. Nieuw: een eigen scherm (Custom View met omhoog, omlaag, kiezen).

- **De zee staat stil:** platte kamlijn zonder golf op y 84 (schuim, 2 px), daaronder één tint 0055AA, onderin vanaf y 208 de diepte 000055. Dat de golf weg is, zegt "pauze" zonder woorden.
- Bovenin "paused" (SemiBold 26, schuim, y 24) en "round 2 · 1:12" (Medium 17, wit, y 56): welke ronde en hoe lang je al bezig was.
- **Drie keuzes** Resume, Save, Discard (SemiBold 24), middenlijnen op y 106, 144, 182. De gekozen keuze in een pil van schuim (110 x 32, helemaal rond) met tekst in 000055; de andere wit, zonder pil.
- **De haak: je eigen dier wijst je keuze aan.** Het dier dat met je meezwemt (maat 12 op 260, 21 op 454) staat links van de pil, midden 22 px links van de pilrand, en schuift mee als je omhoog of omlaag gaat. Eerlijk: het is het dier dat je zelf koos in de sea log.
- Onderin "the sea waits" (Medium 15, schuim, y 214).
- Startkeuze: Resume (wie per ongeluk op de knop komt, verliest niets). Discard vraagt geen extra bevestiging in dit blad; wil Gijs die toch, dan dezelfde opmaak met "Discard?" en Yes, No.
- Beelden: `blad10/pauze-1-260.png` tot `pauze-3-454.png`.

## 3. Winkelposter: "Breathe in rounds. Make sea friends."
Eén beeld dat zegt wat Ebb is: ademrondes op je pols, de zee, en dieren die je krijgt door terug te komen.

- **Opbouw (1000 x 1000):** kop in twee regels (Barlow Condensed ExtraBold 96, wit, "sea friends." in schuim), regel eronder "Come back, and a new friend swims in.  24 to find." (Medium 36, 00AAFF). Daaronder één zee met kamlijn over de hele breedte op y 300, in banden die dieper donkerder worden.
- **Het horloge in het midden** (520 px hoog) met de echte opname van inhouden met dier. Gijs vult dit met de opname uit zijn plaatjesrun na besluit 2 (dier 90 x 70); `poster_v3.py <simulator.png> <uit.png>` knipt het horloge zelf uit de simulator-opname.
- **De optocht:** de 23 dieren zwemmen in een U om het horloge, links omlaag, langs de bodem, rechts omhoog, op volgorde van het echte schema, en worden langzaam groter. Aan het eind komt **de walvis boven aan de kamlijn en blaast**: jij houdt je adem in, hij haalt adem. Dat is de grap.
- **Drie kale feiten uit `TrouwDieren.mc`:** "1 session" bij de vis, "12 sessions" bij de octopus, "50 sessions" (geel) bij de walvis. Zo zie je in één blik dat dieren komen door terug te komen, niet door langer inhouden. Geen meters, geen tijden-belofte.
- Voet: "One payment · no subscription · no account" (SemiBold 34, wit).
- Dieren getekend met `horloge_sim.py`: precies de vormen en kleuren uit de app, alleen groter. Ze raken elkaar niet (de optocht kiest zelf de grootste maat die past, nu 25 tot 30).
- Klein bekeken (300 px, zoals in de lijst van de winkel): kop en tijd leesbaar, de optocht leest als een kleurige rij dieren om het horloge.

Wat Gijs nog doet: echte opname erin (s2 na besluit 2), en dan de andere winkelbeelden (s17, s4, s7, sea complete) zoals in zijn lijst. Oude `0-poster-v2.png` beloofde de walvis voor 3:00 inhouden: dat klopt niet meer en gaat weg.
