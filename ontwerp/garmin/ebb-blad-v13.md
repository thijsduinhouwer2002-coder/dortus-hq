# Ebb blad v13 (Mila, run 37, 11 nov ±21:55 NL): eindscherm op 260

Vraag van Gijs (11 nov 20:40 UTC) en keuring bouw 7 punt 4: dieren op het eindscherm van de FR255 50 tot 55 px breed (zeester was 21), en (bouw 6) helemaal onder de kamlijn. Keuze: **niet over de kamlijn, wel alles omhoog.** Tijden en kamlijn schuiven op, het dier krijgt een vast vak onder de kamlijn, tekst en stippen schuiven mee. De onderkant van het scherm was toch leeg.

Beelden in `blad13/`: `eind-260-oud-nieuw-2x.png` (boven oud zoals nu in de app, onder nieuw, dubbel), `eind-260-oud-nieuw-1x.png` (ware grootte), losse schermen `eind-260-*.png`, op 454 `eind-454-*.png`, maten per dier `maten.txt`. Script `bron/blad_v13.py <uitmap>`.

## Indeling op 260 (in 1/260 D, y van boven; op andere horloges x D/260)
| | oud (gemeten fr255 s17) | nieuw |
|---|---|---|
| kop ("3 rounds done", "calm done") bovenkant | 40 | **34** |
| tijden / "4 min · 12 breaths" bovenkant | 74 | **63** |
| kamlijn | 112 | **94** |
| vak van het dier | 113 tot 142, maat 11 | **98 tot 144, midden 121, hoogstens 54 x 46** |
| naamregel ("new friend: ...") bovenkant | 163 | **152** |
| tweede naamregel (lange naam) | +32 | **+23** |
| stippen midden | 190 | **180** (+23 bij twee regels) |
| onderste regel ("4 weeks in a row") bovenkant | 204 | **190** (+23 bij twee regels) |

- **Maat per dier:** de grootste maat waarbij het kader van het dier (met stickerrand) in 54 x 46 past (454: 94 x 80). Tabel in `blad13/maten.txt`, op 260 tussen 20 (reuzeninktvis) en 29 (garnaal); krab 24 (53 px breed), zeester 24 (47 px), walvis 24 (54 px), zeekomkommer 24 (53 px). Smalle, hoge dieren (zeepaardje, maanvis, inktvis) worden 31 tot 40 px breed, want hoger dan 46 past niet onder de kamlijn; ze lezen toch groot.
- **Midden van het kader** op x = midden, y = 121 (zoals je het belletje deed: kadermidden, niet zwaartepunt).
- **Calm-eindscherm (s34/k34):** zelfde indeling, dus de krab staat nu ook onder de kamlijn (keuring punt 4 "krab 6 px lager" is hiermee gedaan).
- **Sea complete** blijft zijn eigen indeling (blad v10); scène 36 "einde-na-feest" volgt deze tabel, met walvis maat 24.

## Waarom
Op ware grootte (GEZIEN met Read, 1x) lezen de dieren nu als figuurtjes met gezicht in plaats van als stipjes; het scherm lijkt op het Calm-eindscherm dat al het rijkste was, en ze staan allemaal op dezelfde plek. Gemeten op 260: kop op y 34 is 130 px breed, er is daar 175 px ruimte in de cirkel; onderste regel bij twee naamregels eindigt op ±223, daar is 190 px ruimte, "back after a break" is 95 px. Niets raakt de rand.

## Nog open
- "Today" in de menuregel op 260: plaatjesrun 43094387097 staat nog niet op de tak `schermen` (Actions staat stil sinds 14:02 UTC, zie Gijs). Daarom een proef: de echte menuregel uit fr255-scene10 met "  ·  Today" erachter in dezelfde letter en kleur, `blad13/menu-today-260-proef-2x.png` (links nu, rechts met Today). **Past:** de regel wordt 180 px breed (x 40 tot 220 op 260), op die hoogte is 246 px ruimte in de cirkel, dus 33 px vrij aan elke kant; hij is iets breder dan de pillen (±160), dat oogt nog rustig. GOK tot ik de echte opname zie; zodra Actions weer loopt kijk ik hem na.

## Startpictogram per maat (aanbod Gijs 20:40 UTC)
Getekend op elke maat (niet verkleind): `blad12/launcher-40.png`, `-54`, `-56`, `-60`, `-65`, `-70`, `-80.png`, rij op ware grootte `blad12/launcher-rij-1x.png`. Nieuw in `bron/icoon_v3.py`: het kader van de walvis staat in het midden (op 54 en 56 px viel de staart buiten de cirkel en stond links een leeg stuk), onder 60 px walvis 78 procent van de straal, de belletjes schuiven mee met de walvis. Het winkelicoon is gelijk gebleven (byte voor byte). GEZIEN met Read op 3x: staart en fontein binnen de cirkel op elke maat.

## Nagekeken op de echte beelden (run 38, plaatjesrun 43104540264, commit 5547b0d, nog zonder v13)
Beeld `blad13/instellingen-fr255-app-vs-blad-2x.png` (van links: app s19, mijn blad oud, app s20, mijn blad v12; FR255 uit de simulator naast mijn blad op 260, beide dubbel).
- **Scène 20 (blad v12 punt 3) staat erin:** zee omhoog, "Ebb is silent. Buzz only." wit in het water, schildpad eronder, pil met "read again". Op de fenix847mm precies zoals bedoeld (GEZIEN).
- **Op de FR255 zijn de letters van het horloge groter dan in mijn blad.** Daardoor (1) **s19: "Rounds 3" schuift onder de titel "settings"**, de twee regels lopen over elkaar (fout, ook op het winkelbeeld k19 als dat van de FR255 komt); (2) **s20: de pil is ±0,33 D hoog in plaats van 0,207 D** en "Start my pattern" raakt bijna de pil (±2 px), de pil raakt bijna de kamlijn.
- **Regel (alle horloges, niet alleen 260):** reken de afstanden in de lijst met de echte letterhoogte (`dc.getFontHeight`), niet alleen in D. Regel boven de pil: onderkant minstens 3 px boven de pil. Bovenste lijstregel: bovenkant minstens 3 px onder de onderkant van de titel; past hij niet, laat hem weg (de titel gaat voor). In de pil: naam in fM en waarde in fS (zoals de waarden van de andere regels), pilhoogte = hoogte naam + hoogte waarde + 8 px. Waar de pil daarmee onder 0,207 D blijft, houd 0,207 D.
- Kijk ik na in de volgende plaatjesrun.

## v13 in de app (plaatjesrun 43105047693, commit 3598a84)
Beelden `blad13/app-fr255-v13-rij-2x.png` en `blad13/app-fenix847mm-v13-rij.png` (s17, s33, s34, s36, s37, s38, s19). GEZIEN met Read.
- **Eindschermen goed:** zeester, zeekomkommer, krab (Calm) en walvis staan groot in het vak onder de kamlijn, als figuurtjes met gezicht, op beide maten. Lange naam op twee regels en "back after a break" blijven binnen de cirkel.
- **Today in de menuregel (s37):** past op de FR255 en de fenix, onderstreept als keuze. Mijn proef klopte.
- **Nog open:** s19 op de FR255, "Rounds 3" over de titel (zie hierboven); op de fenix staat hij er krap maar los onder.
