# Ebb blad v12 (Mila, run 36, 11 nov ±21:15 NL): poster v4, icoon met blauwe walvis, instellingen blad 2

Opdracht: "Voor Mila" in `ebb-bouw-7-keuring-drie.md`. Bron: plaatjesrun op tak `schermen` (`garmin-adem/plaatjes/`, stand 11 nov avond), fenix847mm en fr255. Alle beelden in `blad12/`.

## 1. Poster v4 (één stijl met de kaarten)
Beeld `blad12/poster-v4.png` (1000 x 1000, 163 KB), op winkelformaat `blad12/poster-v4-150.png`. Script `bron/poster_v4.py <fenix847mm-scene24.png> <uit.png>`.

- **Zelfde taal als kaarten v4:** nachtblauw 000055, zee met schuimlijn en drie banden, belletjes, kop wit met één woord geel FFFF55, geen zwart, geen rood, horloge als patrijspoort zonder band (de echte opname, ronde uitsnede met de 60-streepjes, `winkel_v4.uitsnede`).
- **Kop:** "Hold your breath. / Make **sea friends**." in twee korte regels, 116 px op 1000: op 150 px nog 17 px hoog en leesbaar (GEZIEN met Read). Ondertekst wit "Come back, and a new friend swims in."
- **Groot scherm:** schermstraal 250 (50 procent van de breedte, met kastring 58 procent; v3 had 32 procent). Groter kan niet zonder dat de optocht van vrienden wegvalt, en die is de haak.
- **Haak:** de 23 vrienden zwemmen in een U om de patrijspoort, in de volgorde waarin je ze vindt (vis linksboven, kreeft rechts), en de blauwe walvis met fontein sluit de optocht af. Je ziet in één blik: er is veel te vinden.
- **Onder:** "One payment · no subscription · no extra account" (zoals gevraagd met "extra").
- **Eerlijk:** scherm is scène 24 (inhouden 1:45 met krab), dieren zijn de app-dieren v8.3. Geen getallen meer bij de dieren (v3 noemde "50 sessions" bij de walvis, dat klopt niet meer met het schema).
- **Voor Gijs:** draai het script op de verse scène 24 uit de eindrun en zet hem als `winkel/0-poster-v4.png`.

## 2. Icoon v3: blauwe walvis
Beelden `blad12/icoon-500-v3.png` (winkel), `blad12/launcher-40.png`, `-65.png`, `-80.png` (startpictogram). Naast de toppers: `blad12/icoon-v3-onder-toppers.png`. Script `bron/icoon_v3.py winkel <uit> [500]` en `bron/icoon_v3.py start <uit> <maat>`.

- **Winkel:** de patrijspoort blijft (staalring met acht klinknagels, ons teken op kaarten en poster), binnenin de zee van de app met schuimlijn en de blauwe walvis nr. 24 (dieren v8.3, met eigen fontein en glimlach) half boven het water, drie belletjes erboven.
- **Blauw op blauw viel weg** (eerste proef, GEZIEN naast de toppers op 64 px). Daarom een dikke witte stickerrand om de walvis, zoals de dieren op poster en kaarten: nu springt hij er op 40 px nog uit.
- **Startpictogram:** zonder ring en zonder belletjes onder 60 px, walvis groter (84 procent van de straal). Maak per horloge de maat die nu in `resources-*/drawables/launcher_icon.png` staat (bijv. 40 en 65).

## 3. Instellingen blad 2 (scène 20): onderaan ben je op de bodem
Beelden `blad12/instellingen-oud-nieuw.png` (boven 454 ware grootte, onder 260 dubbel; links oud, midden regel 13, rechts regel 14), losse schermen `blad12/instellingen-*.png`. Script `bron/blad_v12.py <uitmap>`.

Regel (alles in D, gemeten op scène 19):
- **Bij de laatste twee regels** (Start my pattern, Safety info) komt de zee hoger: kamlijn op **0,745 D** in plaats van 0,872. De vaste zin staat **wit in het water** op 0,802 D, lettermaat fX: **"Ebb is silent. Buzz only."** (eerlijk en vrolijker dan "Ebb makes no sound", en hij zegt meteen wat er wel is). Het eigen dier (zoals sea log en pauzemenu) zit eronder op 0,890 D, maat 12/260 D.
- **Bij de laatste regel** (Safety info) blijft de lijst staan en zakt de pil één plek: twee regels erboven (0,304 en 0,384), pil midden op **0,564 D** (hoogte 0,207 D zoals nu). Zo staat er niets leeg.
- **Safety info krijgt een waarde in de pil: "read again"** (lichtcyaan, zoals de waarden van de andere regels). Na kiezen blijft het "next start" zoals nu.
- De regel "Ebb makes no sound" als losse regel vervalt.
- **Waarom:** het blad was een pil in het zwart met een grijze zin; nu heeft het einde van de lijst een plek: de zee komt omhoog, je dier zit er, en de zin hoort bij de zee in plaats van als knop te lezen. Gemeten: tekst ligt binnen 1 px van het midden, onderste zin binnen 0,38 R op 260.
