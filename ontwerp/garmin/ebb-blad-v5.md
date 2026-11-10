# Ebb blad v5: alle schermen na de keuring van v4.1 (Mila, 11 nov 00:05 NL, run 23)

**Blad: `ontwerp/garmin/ebb-blad-v5.png`.** Links 454 px (AMOLED), rechts 260 px (MIP), ware grootte. 21 schermen.
**De zee per 30 s in één blik: `ontwerp/garmin/blad5/zee-standen-260.png`.** **De drie inhoudschermen naast elkaar: `blad5/drie-holds-454.png`.**
Losse beelden en meting: `ontwerp/garmin/blad5/` (`meting-v5.txt`), bron `ontwerp/garmin/bron/ebb_blad_v5.py` (bouwt op v4 en v3).
Vervangt v4.1. Twee frisse keuringen in dezelfde run: v5.0 een 6 (M1 tot M8, verwerkt in v5.1), v5.1 een 6 (N1 tot N6, vijf verwerkt in v5.2, N2 spoken open). Zie `ebb-blad-v5-frisse-keuring.md`. Volgende stap: N2, dan frisse keuring op v5.2, pas bij 8 of hoger naar Thijs; Gijs bouwt de schermen pas na zijn ja.
Beeldtaal en de 10 regels: ongewijzigd, bovenaan `ebb-blad-v1.md`.

## Wat er veranderde, punt voor punt (keuring `ebb-blad-v4-keuring-drie.md`)
| punt | ja/nee | waar en hoe |
|---|---|---|
| T1 eigen dier | ja | Op 3a/3b/3c zwemt je eigen dier mee: de schildpad die je in de sea log koos (8c, knop "swims with you"). Zonder keuze: het laatst gevonden dier. Hij kantelt per scherm iets anders; de belletjes staan op elk scherm ergens anders. |
| T2 zee donkerder | ja | Zes vaste standen, elke 30 s een stap (0:00, 0:30, 1:00, 1:30, 2:00, 2:30). MIP: de lichte banden schuiven omhoog en vallen weg, W3 groeit (zie strook). AMOLED: dezelfde banden plus het hele water 10 % donkerder per stap. Vanaf 3:00 terug naar stand 4: iets lichter, samen met de tekst. 0:30, 1:45 en 3:04 zijn alle drie anders. |
| P1 instellingen | ja | 9: Rounds 3, **Breathing pace 10 per min**, Breaths 30, Buzz every 30 s on. 9b: Buzz last 3 breaths on, **Buzz only on (no sound)**, Touch lock on, Safety info. Geen "tick" of "normal" meer. |
| P2 Connect | ja (beschreven) | Zie onder. |
| P3 hartslag en ronde | ja | Elk inhoudscherm onderaan: hartje, bpm, "· round 2". Op 3c op de tweede regel. |
| P4 na 3:00 | ja | "3:00 · time to breathe" in wit met trilicoon, geen geel. |
| P5 8 weeks | ja | Staven = sessies per week (2 tot 5), getal eronder; "sessions per week"; "avg hold 1:41" over alle sessies (today zegt 1:49 over vandaag, het eindscherm per ronde). Staven van een nieuwe gebruiker: 0 0 0 0 0 0 3 6 = 9 sessies, past bij 7 dieren (v5.2). |
| P6 kloppende cijfers | ja (v5.1) | Eén verhaal: je hebt 7 dieren (Fish tot Starfish = 8 sessies, 4 dagen op rij). Ochtend 7:40: rondes 1:20, 1:45, 3:04 (3a, 3b, 3c en 6b: Starfish voor 4 dagen op rij). Avond 21:15: 1:15, 1:38, 1:52 (6c: volgende is Pufferfish, 5 dagen op rij, dus "Pufferfish tomorrow"). Today: deze zes, avg 1:49 (nagerekend). Herstel: "round 2 held 1:45". 8: "7 of 24". Geen clownvis meer naast de vis. |
| P7 today en eindscherm | ja | Today laat de hele dag zien: twee sessies (7:40 en 21:15), zes trechters, "2 sessions · 6 holds", "avg 1:49". |
| P8 teksten | ja | 2: groot "23", klein "of 30 · round 2". 4: "big breath in, hold" boven "15 s". Eindscherm: r1 r2 r3 boven de tijden. |
| P9 regels | ja | Zie onder. |
| V1 sea log | ja | 3 x 3 per blad, 3 bladen ("1 / 3"). Kleinste dier 30 px op 260 en 52 px op 454 (gemeten, kwal), de rest groter. |
| V2 silhouetten | ja | Kleur 0x0055FF (3,7:1 op zwart, MIP) en onder elk silhouet hoe je hem krijgt: "12x" = 12 sessies, "6d" = 6 dagen op rij, "break" bij de zeekomkommer. |
| V3 grijs | ja | Geen grijs meer op 6b/6c (wit en lichtcyaan 0xAAFFFF). Overal elders ook lichtcyaan in plaats van grijs. |
| V4 6b = 6c | ja | Zelfde skelet: kop met drie tijden, dier op 0,515, naam op 0,695, reeks op 0,775, stippen op 0,85. Het silhouet zit helemaal onder water, de golf loopt erboven. |
| V5 groot dier | ja | Zeester op 6b ±40 % van de breedte. |
| V6 tekenregel 24 dieren | ja | `ebb-dieren-v5.png`, bron `bron/ebb_dieren_v5.py` (`delen_v5`, zelfde vorm als `dier_delen()`). Opnieuw: **zeekomkommer met slaapmuts** (de grap: hij komt na een pauze), zeeotter op zijn rug met licht gezicht, oortjes, schelp en voetjes omhoog, zeehond met snuit, snorpuntjes en vlekjes. Rog is nu een kleine teal ruit met stippen, manta een brede zwarte met witte buik en hoorntjes. Haai lichter (lavendel), zwaardvis lichtblauw met zichtbaar zwaard en zeil (was onzichtbaar op diep water), orka, manta, zwaardvis en haai met een lichte rand van 1 tot 2 px. Zelfde oog voor alle 24. 0 pixels buiten MIP op 260. |
| V7 geen 24 stipjes | ja | 8c: groot dier, naam, hoe gekregen, knop "swims with you". |
| S1 veiligheid | ja | Drie korte bladen (Next, Next, OK), tekst hieronder letterlijk voor de code. |
| S2 startcheck | ja | 1b: "Seated or lying?" met knop Start, bij elke Rounds-start. |

## Teksten voor de code (letterlijk)
- 10: "Sit or lie down. / Never standing, / never in or near water, / never while driving." [Next]
- 10b: "You can faint / without warning. / Never force a hold. / Stop if dizzy." [Next]
- 10c: "Not if pregnant, / under 18, epilepsy, / heart or blood / pressure problems." geel: "Not a medical device." [OK]
- 1b: "Rounds 3 x 30" / "Seated or lying?" [Start]
- 3c: "3:00 · time to breathe" (wit), met een korte trilling (Gijs' zachte signaal).

## P2: wat je in Garmin Connect ziet na een Rounds-sessie
Activiteit "Breathwork" (of "Ebb"), met: duur, gemiddelde en hoogste hartslag (gewone grafiek van Garmin), en per ronde een lap. Eigen velden (FIT, al in de code van Gijs): per lap "Hold time" (m:ss) en "Breaths"; in de samenvatting "Rounds 3" en "Longest hold 3:04". Geen "best" of record. De hartslaggrafiek laat per ronde zien hoe je hart tijdens het inhouden zakt: dat is het mooie plaatje in Connect, zonder dat wij iets tekenen.

## P9: regels die vast liggen
- **Gemiste dag:** de reeks op het eindscherm begint opnieuw bij 1, maar dieren voor dagen op rij tellen met je **beste** reeks. Een gemiste dag pakt dus nooit een dier af. Na 7 of meer dagen zonder komt de zeekomkommer ("back after a break"), zodat terugkomen een cadeau is en geen schuld.
- **Schema van de 24:** hoogstens één nieuw dier per sessie, en sessiedieren tellen hoogstens 2 sessies per dag (Gijs G2). Bij 4 sessies per week, 5 dagen op rij in de eerste week: week 1 vier tot vijf dieren (Fish, Shrimp, Jellyfish, Turtle, Crab), week 2 en 3 elke 3 tot 4 dagen een (Seahorse tot Squid), daarna gemiddeld één per week, en de laatste (Narwhal 40x, Giant squid 30 dagen, Whale 60x) in maand 3 en 4. Wie elke dag komt is na ±2 maanden bij 22 van 24; de walvis blijft voor de trouwste.
- **Waarschuwing:** de drie veiligheidsbladen bij de eerste start en elke 30 dagen opnieuw; de regel "Seated or lying?" bij elke Rounds-start; "time to breathe" met trilling op 3:00 inhouden.

## Gemeten (`blad5/meting-v5.txt`) en bekeken
- Kader van alles wat getekend is: midden binnen 0,5 px op alle schermen op 260 en 454, behalve de sea log (8: -5 px op 260): dat is de ring om het gekozen dier links; zonder ring 0 px. Optisch midden binnen 2,7 px.
- Verste pixel die geen water of rand is (kolom "verst" in de meting, alleen zinvol op schermen zonder water): sea log 0,86 en 0,89 van de straal (onderste dieren en hints), instellingen, today, 8 weeks en veiligheid 0,70 tot 0,78. Op schermen met water meet de kolom het schuim van de golf (0,97); daar staat de tekst op het oog ruim binnen de rand.
- 0 pixels buiten de MIP-kleuren op 260. Kleinste letter 20 px op 260.
- Bekeken met de Read-tool: heel blad, de drie inhoudschermen naast elkaar en de zeven zee-standen, sea log 1 en 2 vergroot. Dieren v5 bekeken op diep water op 454 en 260. Zwakste nu: de otter leest als otter maar ook een beetje als beertje; het trilicoontje op 3c is klein en wat druk; de "r1 r2 r3" kop op het eindscherm is netjes maar zakelijk.

## Wat Thijs hier als eerste van zegt (besluit 23:39 punt 3)
Waarschijnlijk: "de zee wordt nu echt donkerder, goed; maar zijn de dieren al allemaal mooi?" In dezelfde run opnieuw getekend (V6). Tweede vraag die hij kan stellen: "zie ik op de pols dat het water donkerder wordt?" Ja op 454; op 260 zijn het vaste stappen in vier MIP-tinten, zie de strook.

## v5.1: de acht moet-punten van de frisse keuring (zelfde run)
- M1 en M2: één verhaal (zie P6). 3c is ronde 3 van de ochtend, r3 = 3:04, Longest hold 3:04; 6c is de avond met eigen tijden; today avg 1:49 = gemiddelde van de zes.
- M3: 6b en 6c allebei 7 stippen (een week), 4 gevuld.
- M4: zeester kleiner en lager (0,18 op 0,545), kogelvis 0,145 op 0,54: vrij van de tijden.
- M5: op 3c staat "time to breathe" met trilicoon bovenaan op de plek van "hold"; hart en ronde blijven op dezelfde hoogte als op 3a en 3b. "3:00 ·" viel weg: het grote getal zegt het al.
- M6: geen codes meer. Sea log: silhouetten als spook (donkerblauw met lichtcyaan rand van 2 px), onder de lijst voluit wat het gekozen silhouet vraagt ("12 sessions", "back after a break"); bovenaan "7 of 24 · page 2/3". Blad 3 getekend (8d).
- M7: spookvis op 6c en in de sea log: vulling W3 met lichtcyaan rand, geen volle 0055FF meer.
- M8: menu toont je eigen dier (de schildpad) in het lage tij in plaats van de walvis die je nog niet hebt.
- Meting v5.1: kader en optisch midden binnen 2,7 px behalve de sea log (ring om het gekozen dier en een halve laatste rij geven 2,5 tot 9 px kaderverschuiving; het raster zelf staat in het midden).
- Kan-punten K1 (today minder ijspegel), K2 (extra glans bij new friend, otter en zeekomkommer nog eens), K3 ("swims with you" schakelaar of toestand), K4 ("in" kaal) staan open voor de volgende run.

## v5.2: de punten van de tweede frisse keuring (v5.1 kreeg ook een 6)
- N1 cijfers tellen op: 8 weeks is nu een nieuwe gebruiker (0 0 0 0 0 0 3 6 = 9 sessies), "avg hold 1:41"; sea log rekent "more sessions" vanaf 9.
- N2 spoken herkenbaarder (kogelvis met staart en oog, kenmerk per dier groter, clownvis-spook niet gelijk aan de vis): **open, eerste werk volgende run.**
- N3 sea log: bovenaan wat het gekozen silhouet vraagt met naam ("Octopus · 3 more sessions"), de zeekomkommer blijft een verrassing ("comes after a break"); onderaan "2 / 3". 8c: "found: 3 days in a row", knop "swims with you: on".
- N4 nieuw dier als feest: zeester ±37 procent breed, lichtkrans van 12 stralen erachter (alleen onder water; op het horloge draait hij langzaam), "new friend!" in geel op een eigen regel, naam en reden eronder, meer belletjes.
- N5 eindscherm: "session done", "3 rounds", dan de drie tijden ruim boven de golf (geen r1 r2 r3 meer).
- N6 3c: trilicoon weg, alleen "time to breathe" (het horloge trilt).
- Kan: de kleine "s" op 4 en 5 nu lichtcyaan. Open: today minder ijspegel, OK op 10c gelijk met Next.
