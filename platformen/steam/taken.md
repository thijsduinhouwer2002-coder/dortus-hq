# Steam: taken (Het Hol, Olaf bouwt, belangrijkste bovenaan)

Opgeruimd 13 nov 2026 door Olaf. De oude lijst (tot 10 nov 06:45 UTC) staat volledig in `logboek.md` onder "13 nov 2026, Olaf: oude takenlijst verplaatst".
Wat telt is de vaste demolijst in `planning-fest-2027.md` (demo af vr 18 dec). **Geen nieuwe features buiten die lijst.** Ploeg: Olaf (bouw, elk uur op :13) en Daan (ontwerp, elk uur op :23). Bram, Sanne en Mila staan uit; hun bestanden in `producten/steam-hol/godot/systemen/` en `kunst/` mag Olaf nu aanpassen als de demolijst dat nodig heeft (met een regel in het logboek).

## Demolijst: wat is klaar (eerlijk, 13 nov 12:30 UTC)
| # | Punt | Stand | Bewijs |
|---|---|---|---|
| 1 | Volle toetsrun groen op Windows, geen crash in 60 min | **half** | Toetsrun groen op 10 nov (run 42770401405: toetsen 0 FOUT, strook 96/120/160, film). Opnieuw op de huidige main (92884c4): run 43415980604 **groen**, toetsen 0 FOUT (GEZIEN 13 nov 12:55 UTC). Nooit langer dan ±60 s gedraaid; daarvoor nu de duurtest `steam-hol-duur.yml` (nieuw, controleur akkoord), eerste run 43416412054. |
| 2 | Zuinig: onder 1 CPU-s per 10 s op 120 px, stil bijna 0 | **niet aangetoond** | Alleen in de drukke demo gemeten: 0,61 (9 nov), 1,01 en 1,27 (10 nov, run 42770401405), 1,02 (13 nov, run 43415980604). Dat is boven de grens. Gewoon spel nooit gemeten; de duurtest meet het een uur lang per 10 s (gemiddeld, mediaan, laagste). |
| 3 | Eerste tien minuten: binnen 30 s iets leuks, binnen 10 min één keer gekocht | **grotendeels** | Vaste stappen `BEGIN` in `kern/strook.gd` (vallen, vluchten, opgegeten, terug, doorlopen); eerste held valt na 4 s. Film 10 nov: alles binnen een minuut (demo). Eerste aankoop mogelijk na 45 tot 193 s, maar dat is de simulatie (`sim/UITKOMST.md`, GEZIEN), niet het spel zelf. Nog: in het spel loggen wanneer je voor het eerst iets kunt kopen. |
| 4 | Nooit straffen als je weg bent (8 uur weg geeft alleen winst) | **klaar** | `systemen/voortgang.gd`: alleen winst, plafond 12 uur; toetsen in `toets_systemen.gd` ("plafond 12 uur: week = nacht") groen op 10 nov. Nog niet gezien in een echte herstart op Windows. |
| 5 | Strook 96, 120 en 160 px; klikken door de lucht | **grotendeels** | Rechtsklik kiest de hoogte en bewaart die (10 nov 00:30, controleur akkoord); schermen op 96/120/160 elke run. Klikken door de lucht alleen lokaal getest, niet op de Windows-runner (`e2e/klik.ps1` bestaat maar zit niet in de workflow). |
| 6 | Demo-einde na ±2 uur: vriendelijke regel, spel blijft draaien, save gaat mee | **niet gebouwd** | Niets in de code. |
| 7 | Ja van Thijs op het uiterlijk | **open** | Gloop: Daan, blad voor Thijs vr 20 nov. Helden en winkelbeelden wo 25 nov. |

## Open, in volgorde
- [ ] **1 en 2: duurtest uitlezen** (run 43416412054, klaar ±13:30 UTC). Groen: punt 1 af (60 min). CPU boven 1: oorzaak zoeken in `kern/strook.gd` (tekenen alleen als er iets beweegt, fps) en opnieuw meten. Ook de gewone toetsrun 43415980604 nakijken.
- [ ] **6: demo-einde bouwen** (ontwerp staat in `producten/steam-hol/ontwerp.md`, sectie Demo-einde, controleur akkoord ronde 2 op 13 nov; bouwen op tak `claude/steam-hol-demo-einde` volgens dat ontwerp, de samenvatting hieronder is oud): speeltijd tellen in de save (alleen open tijd), na 2 uur één vriendelijke regel in de kroniek en een klein teken in het paneel, het spel blijft draaien (helden komen nog, geen nieuwe aankopen of juist wel: kiezen in het ontwerp), de save is dezelfde als in het volle spel. Een vlag `demo_versie` in `project.godot` of een argument, zodat het volle spel geen einde heeft.
- [ ] **5: klikken door de lucht op de runner** testen met `e2e/klik.ps1` in `steam-hol.yml` (klik op de lucht boven het hol moet bij Kladblok aankomen).
- [ ] **3: bewijs in het spel**: logregel "HOL eerste koop mogelijk na N s" (de eerste keer dat het goud de goedkoopste prijs haalt), uitlezen in de duurtest.
- [ ] **4: bewijs op Windows**: in de duurtest of een eigen stap de save 8 uur terugzetten, opnieuw starten, goud vooraf en achteraf loggen.
- [ ] **Daan: elk nieuw figuur meteen in het spel** zodra hij erom vraagt (`berichten/daan.md`, `ontwerp/steam/`), en hem elke keer een beeld op ware grootte (120 px) uit de echte Windows-build leveren: `strook-120.png` op tak `schermen`, map `steam-hol/main/` (en de duurtest maakt elke 10 min een scherm in `steam-hol-duur/main/`).
- [ ] **Klein, alleen als het past:** `kern/strook.gd` is 485 regels (regel: onder ±400). Splitsen als ik er voor punt 6 toch in moet.

## Na het fest (staat niet op de demolijst, niet aan beginnen)
Heldenboek stap 2 (boekje bij hover, bladzijde bij klik), muziek en geluid in het rechtsklikmenu, graven en put die goud kosten in het spel, trailer (begin 42 tot 44 s), oude schacht in één beeld dicht, wand van aartsvijanden, voorraad regels via `kroniek.gd`. Komt een van deze toch nodig blijken voor de demolijst (bijvoorbeeld voor punt 3), dan zet ik hem hierboven met de reden.

## Vragen tussen ons
(Olaf en Daan; nieuwste onderaan; "(antwoord <naam> <tijd>: ...)" erachter. De oude vragen met Bram, Sanne en Mila staan in het logboek.)
