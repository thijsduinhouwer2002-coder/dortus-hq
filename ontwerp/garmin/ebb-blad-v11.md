# Ebb blad v11 (Mila, run 35, 11 nov ±10:40 NL): winkelkaarten v4 en keuzemarkering sea log

Opdracht: "Voor Mila" in `ebb-bouw-6-keuring-drie.md`. Bron: plaatjesrun 42991019138 (tak `schermen`, f2699ce), fenix847mm.

## 1. Winkelkaarten v4 (ingezoomd)
Beelden: `winkel4/` (800 x 800, elk onder 150 KB), overzicht `winkel4/ebb-winkel-v4-rij.png`, op winkelformaat naast v3: `winkel4/v3-naast-v4-220.png`. Script: `bron/winkel_v4.py alles <plaatjesmap> <uitmap>`.

- **Scherm 66 procent van de kaartbreedte** (eis minstens 60). Ronde uitsnede van de echte opname: scherm plus een smalle ring kast met de 60-streepjes en GARMIN, geen band. Schermcirkel in de fenix847mm-opname: midden (361, 476), straal 227.
- **Geen zwart meer:** achtergrond nachtblauw 000055, achter het horloge drie golven zee (MIDDEN met schuimlijn, DIEP, donkerder) met belletjes. Het horloge hangt als patrijspoort in de zee.
- **Kop wit met één woord in geel FFFF55, ondertekst wit en groot (58/800).** Geen rood. Lange koppen worden kleiner in plaats van afgesneden.
- **Waarom:** op 220 px was v3 een klein horloge op zwart; nu lees je het scherm (cijfers, dieren, tekst) op winkelformaat (GEZIEN met Read, `v3-naast-v4-220.png`).

**Keuze vijf (voorstel, Gijs kijkt mee):**

| Nr | Bestand | Scène | Kop (geel woord) | Ondertekst |
|---|---|---|---|---|
| 1 | 1-hold.png | 24 inhouden 1:45 met krab | Hold. Bring a **friend**. | Breath-hold rounds. The sea darkens as you hold. |
| 2 | 2-new-friend.png | 34 new friend: Crab | Come back. Meet a **crab**. | New sea friends for sessions and weeks in a row. |
| 3 | 3-sea-log.png | 4 sea log 8 of 24 | Fill your **sea log**. | 24 sea friends to find. Who is that shadow? |
| 4 | 4-sea-complete.png | 25 sea complete | Then the whole sea **parties**. | Find all 24 and every friend comes to celebrate. |
| 5 | 5-sea-cucumber.png | 33 new friend: Sea cucumber | Took a break? Meet the **sea cucumber**. | A bonus friend for coming back after a break. |
| extra | extra-pause.png | 35 pauzemenu | Pause. The sea **waits**. | Resume, save or discard. Any time. |
| extra | extra-calm.png | 7 Calm 4-7-8 | Calm **4-7-8**, drawn as water. | Breathe in 4, hold 7, out 8. A buzz per phase. |

- **Waarom deze vijf:** het verhaal in vijf tikken: je houdt in met een vriend (1), terugkomen geeft een nieuwe vriend (2), je verzamelt ze en raadt de schaduwen (3), het eind is een feest (4), en zelfs een pauze levert een vriend op (5). De Calm-kaart gaat eruit zoals de keuring vroeg, maar staat klaar als extra, want de titel noemt 4-7-8. Wil Gijs zes beelden, dan extra-calm als zesde.
- **Haak:** "Then the whole sea parties." en "Took a break? Meet the sea cucumber." zijn de grappen; geen andere ademapp beloont je voor een pauze.
- **Frisse toets** (agent zonder uitleg, op v4 eerste versie): 6 van 10. Verwerkt: ondertekst was op 220 px 6 px hoog (nu wit en 30 procent groter, GEZIEN in `winkel4/v4-op-220.png`); pauzekaart was saai en zonder dier (nu de zeekomkommer, pauze als extra); sea log met 24 of 24 verklapte kaart 4 (nu 8 of 24 met schaduwen). Niet te verhelpen in de kaart: het zwart boven in Calm en de kleine dieren van sea complete op 220, dat is het echte scherm.
- **Eerlijk:** elke kaart is één echte opname. Kaart 5: in scène 33 staat nu "4 weeks in a row" onder de zeekomkommer, dat botst met "after a break"; gevraagd aan Gijs om daar "back after a break" te tonen, daarna kaart 5 opnieuw. Tot dan is kaart 5 niet klaar voor de winkel. Kaart 3 toont 8 of 24 met schaduwen; "+ bonus" komt pas op 24 of 24 en staat dus niet op deze kaart. Kaart 2 is na een Calm-sessie: klopt, Calm telt als sessie.
- Sea complete was 189 KB (veel kleur); het script zet een kaart boven onze grens van 150 KB terug naar minder kleuren (zoals v1 tot v3).

## 2. Keuzemarkering in de sea log: het belletje (variant B)
Beelden: `blad11/keuze-A-B.png` (260 dubbel boven, 454 ware grootte onder), losse schermen `blad11/sealog-*-B-260.png` en `-454.png`. Script `bron/blad_v11.py`.

- **Het gekozen dier zit in een belletje:** platte ellips gevuld in MIDDEN 0055AA, rand SCHUIM 00FFFF, wit glimpje linksboven. Teken eerst het belletje, dan het dier erin.
- Maten (midden van het dier is het midden van de ellips):

| | 260 | 454 |
|---|---|---|
| straal x, y | 30, 22 | 52, 38 |
| rand | 2 px | 3 px |
| glimpje | straal 2 op (cx − 19, cy − 11) | straal 4 op (cx − 32, cy − 19) |

- Algemeen: rx = 30/260 D, ry = 22/260 D, glimpje op (cx − 0,62 rx, cy − 0,50 ry). Rand 2 px onder 390, anders 3.
- **De keuzestip onder het dier gaat weg**; het raster blijft in het midden (kolommen −62, 0, +62, rijen 103 en 150 in 1/260 D, zoals v9).
- **Waarom het belletje en niet alleen een ring (A):** de dieren zijn op 260 tot 45 px breed en de rijen staan 47 px uit elkaar, dus een ronde ring om het dier past niet en een dunne ring valt weg achter de poten (GEZIEN: eerste proef met ring straal 20 was onzichtbaar). De gevulde ellips leest in één blik als "deze", ook op 260, en belletjes zijn al ons teken bij inhouden: het dier zit bij jou in het water. De ellips raakt de buren niet (ruimte 2 px horizontaal op 260); een hoog dier als de inktvis eronder mag er iets in steken, dat leest goed.
- Code: `dc.setColor(0x0055AA); dc.fillEllipse(cx, cy, rx, ry); dc.setColor(0x00FFFF); dc.drawEllipse(cx, cy, rx, ry)` (en één keer `rx-1, ry-1` voor 2 px), `dc.setColor(0xFFFFFF); dc.fillCircle(gx, gy, g)`.
