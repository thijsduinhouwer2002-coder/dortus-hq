# Filmpjes week 1: Click Joints, Ebb en Hats of the Fallen (Daans moet-punten verwerkt in run 49, wacht op zijn laatste blik; filmpje 5 pas na Pro live)

**Stand 16 nov, run 49:** Daan keurde alle zes (`ontwerp/filmpjes/keuring-week-1.md`): 2 ja; 1, 3, 5 en 6 ja met één moet; 4 nee tot rond op donker. Zijn vijf json's (`ontwerp/filmpjes/voorstel-daan/`) staan nu ongewijzigd in `commercie/filmpjes/week-1/` en de workflow bouwde de release opnieuw. Daan kijkt de nieuwe release na; daarna mag hij op de lijst van Thijs. De tabellen hieronder volgen de nieuwe versie.

Door Chris, 15 nov 2026, run 45. Opdracht: besluit Thijs 15 nov 22:53 (`berichten/chris.md`). Onderzoek vooraf: `commercie/filmpjes/formats.md`.

**Niemand plaatst zonder akkoord van Daan en het ja van Thijs.** Thijs kiest bij het plaatsen zelf een geluid uit de app; de bestanden hebben geen geluid.

## Waar de bestanden staan
- Release `filmpjes-week-1` in dortus-hq (gemaakt door de workflow `.github/workflows/filmpjes-week-1.yml`): drie mp4's, per filmpje een strook met één beeld per seconde (`-beelden.jpg`) en `SHA256SUMS.txt`. https://github.com/thijsduinhouwer2002-coder/dortus-hq/releases/tag/filmpjes-week-1
- Bron om ze opnieuw te maken: `commercie/filmpjes/week-1/` (`maak.py`, `f1.json` tot `f3.json`, `bronnen.sha256`). Tekst of timing aanpassen = het json-bestand aanpassen en pushen; de workflow bouwt dan opnieuw.
- Alle drie: 1080 x 1920, H.264 (`-preset veryfast`), 30 beelden per seconde, geen geluid, Engelse tekst in beeld bovenaan (buiten de knoppen van TikTok en Shorts onderaan en rechts). Alleen het kleine label met de naam (op 82% van de hoogte) kan onder het onderschrift van de app vallen; dat is niet erg, de naam staat ook bovenaan en op de eindkaart.

## Alleen echte beelden
- Film v2 van Bram (`click-joints-filmisch-v2.mp4`, gerenderd in de echte Blender met de add-on, Thijs zei 9 nov "film Click Joints ja"; sha256 `f6d54416…`).
- De twee previews van de gratis versie 0.1.0 op extensions.blender.org (`3-preview-buigen.png`, `4-preview-paneel.png`, schermen uit de echte add-on).
- Geen gezicht, geen stem, geen nep-persoon, geen AI-beeld. "I made" in de eerste persoon klopt: Thijs maakt het met AI-agents; de AI-zin staat niet meer in het onderschrift (besluit Thijs 16 nov 20:09).
- Alleen de **gratis** versie. Pro staat er niet in, want Pro is nog niet te koop (Superhive keurt nog). Een Pro-filmpje komt na de goedkeuring.

## De drie filmpjes

### 1. `click-joints-1-bend-far-enough.mp4` (16,8 s; run 49 zonder de rode close-up van de hals, moet M1 van Daan), format 2: vraag boven, beeld in het midden
| tijd | beeld | tekst in beeld |
|---|---|---|
| 0 tot 0,5 s | gloeiende ring, close-up | Will this joint bend far enough? |
| 0,5 tot 4,5 s | tekenpop die schopt | (tot 2,2 s de vraag) I made a free Blender add-on that **checks** it |
| 4,5 tot 8,4 s | arm buigt, ring op het gewricht, kogel en kom gaan in de arm uit elkaar (±8,9 tot 9,9 s) | Place the joint. **Drag** the bend. (tot 8,4 s), dan Exploded view: ball and socket apart (8,4 tot 10,8 s) |
| 10,8 tot 13,8 s | arm buigt verder | Green ring = **good fit**, in mm |
| 13,8 tot 16,8 s | pop vervaagt in de eindkaart uit film v2 | Free on Blender Extensions, link in bio |

**Onderschrift:** `I made a free Blender add-on that shows how far a joint bends before you 3D print it. Place a joint, drag the bend, check the fit in mm, export STL or 3MF. Click Joints, free on Blender Extensions (link in bio). #blender #3dprinting #b3d #blenderaddon #articulated`

### 2. `click-joints-2-satisfying-bend.mp4` (10,2 s), format 1: één vaste regel, loopt rond
Ring gloeit (0,5 s), arm buigt (3,9 s), arm buigt verder met de ring (5,8 s). Vaste tekst: "See how far a joint **bends**, before you print." en klein onderaan "Click Joints, a free Blender add-on". Dit is de winkelzin van de listing, dus overal hetzelfde.

**Onderschrift:** `See how far a joint bends, before you print. Click Joints is a free Blender add-on for articulated, poseable 3D prints (link in bio). #blender #3dprinting #articulated #blenderaddon`

### 3. `click-joints-3-three-checks.mp4` (16,7 s), format 4: lijstje zonder gezicht
| tijd | beeld | tekst in beeld |
|---|---|---|
| 0 tot 3 s | ring, tekenpop | 3 things my free Blender add-on **checks** before you print |
| 3 tot 7 s | preview: buig 28°, rode wig | 1. How far it bends. Red means too far. (*Red* in wit sinds run 49, moet M2) |
| 7 tot 11 s | preview: paneel met Good fit, wand, speling | 2. The fit, measured in **mm**: wall and clearance |
| 11 tot 13,7 s | ring, kogel en kom gaan in de arm uit elkaar en weer terug (bron 10,2 tot 12,9 s; de rode close-up is eruit, moet M2) | 3. Exploded view, then one STL or 3MF per part |
| 13,7 tot 16,7 s | eindkaart | Free on Blender Extensions, link in bio |

**Onderschrift:** `3 things my free Blender add-on checks before you 3D print a poseable figure: how far each joint bends, the fit in mm (wall and clearance), and clean parts as STL or 3MF. Click Joints, link in bio. #blender #3dprinting #b3d #blenderaddon #3dprint`

Elke bewering komt uit de listing of de previews: "Drag the bend. Red means too far", "Good fit, measured in mm", "One STL or 3MF per part, in mm", "Exploded view" (winkeltekst en previews 0.1.0, GEZIEN).

### 4. `ebb-4-sea-rises.mp4` (14,3 s; run 49 rond uitgesneden op donker, moet M4 van Daan), Ebb, format 2: tekst boven, horloge in het midden
Extra gemaakt in run 46 (extra run van Thijs, 15 nov 23:00), zodat de dagelijkse reeks wisselend Click Joints en Ebb kan beginnen. Bron: `commercie/ebb/ebb-film.mp4`, schermen uit de simulatorrun 43327097299 van de ingediende app (fenix 8 47 mm), zie `commercie/ebb/lancering.md` punt 3. Opgeschaald van 600 naar 1080 pixels.
| tijd | beeld | tekst in beeld |
|---|---|---|
| 0 tot 2,6 s | menu met de krab | I made a breathing app for **Garmin** watches |
| 2,6 tot 7,2 s | in- en uitademen, water op en neer | The sea **rises** and **falls** with your breath |
| 7,2 tot 9,5 s | inhouden, onder water met de krab | Hold, and you go **under water** |
| 9,5 tot 12 s | "new friend: Starfish", sea log "8 of 24" | New sea creatures join your **sea log** |
| 12 tot 14,3 s | sea log | Ebb, on the Connect IQ Store, link in bio |
Sinds run 49: horloge rond uitgesneden op de donkere achtergrond (zoals filmpje 6), horloge op y 490. De hele tijd klein, direct onder de tekst op y 425: "Screens from the Garmin simulator" (eerlijk: geen opname van een echt horloge, en het water is een overvloeier tussen twee schermen).

**Onderschrift:** `I made a breathing app for Garmin watches: the sea rises and falls with your breath, and when you hold, you go under water. Sea creatures join your sea log as you keep coming back. Ebb, $4.99 one time, no subscription (link in bio). For practice on land only: sit or lie down. Screens from the Garmin simulator. #garmin #connectiq #breathwork #garminwatch`

Bewust niet: geen gezondheidsclaim (geen "calmer", "better sleep", "lung capacity"), geen freediving, geen "every session a new animal" (dieren komen door sessies en weken op rij). Alle beweringen staan in de winkeltekst (stijgen en zakken, onder water bij inhouden, 24 dieren, $4,99 eenmalig zonder abonnement). Ebb Calm (gratis) noem ik niet: nog niet openbaar. Link in bio voor dit filmpje: de winkellink van Ebb uit `commercie/ebb/lancering.md`; één link in het profiel kan maar één product tonen, dus wissel hem mee of gebruik later één pagina op dortus.com met beide.
Nagekeken door een controleur (run 46): filmpje en workflow ja; tekst eerst nee ("as you keep going" las alsof langer inhouden dieren oplevert, en de vaste zin over alleen op het droge ontbrak), beide verwerkt, plus de precieze AI-zin uit `lancering.md`.
Voor Daan (vraag d): beantwoord in zijn keuring, ja rond op donker; verwerkt in run 49.

### 5. `click-joints-5-pro-hinge-stops.mp4` (14,7 s; run 49 lege buis korter, moet M3 van Daan), Click Joints Pro, format 2: tekst boven, beeld vult het scherm
**Pas plaatsen als Click Joints Pro live is op Superhive** (keuring loopt sinds 15 nov 19:45). Tot die dag is het een concept voor de lanceerdag van Pro. Gemaakt in run 47 uit de vijf staande opnames die Bram op 15 nov 22:35 maakte in de echte Blender 5.3.0 met de betaalde zip 1.0.1 (`ontwerp/click-joints/pro/film/staand/`, LEESMIJ daar). Deze opnames zijn al 1080 x 1920, dus geen uitsnede uit een liggende film: het beeld vult het hele scherm en het gewricht is groter dan in 1 tot 3. Het grijze label "Bends 0° to 115°" bovenaan zit in Brams opname zelf.
| tijd | beeld (opname van Bram) | tekst in beeld |
|---|---|---|
| 0 tot 2 s | deel 1: knie buigt van 0 naar 115° met de gradenboog | A printable **knee** that stops at 115° |
| 2 tot 3,7 s | deel 2 vanaf 1,6 s: scharnier staat er meteen, twee delen met groen | I made a Blender add-on that places a click **hinge** |
| 3,7 tot 8,2 s | deel 3: buigt van 0 naar 115° en blijft 1 s op de stop | It bends to 115° and **stops**, instead of flopping backwards |
| 8,2 tot 11,4 s | deel 4: 9° voorbij de stop, rood en "+9° past limit" | Past the stop? It turns red. |
| 11,4 tot 14,7 s | deel 5: kogel en kom uit elkaar (gratis versie) | Ball joints: **free**. Click hinges: **Pro**. Link in bio |
Klein, de hele tijd: "Click Joints Pro, a Blender add-on" op y 1380 en "Link in bio" op y 1290, boven de strook van ±420 px onderaan waar de apps naam en onderschrift zetten (moet-punt controleur). Het woord red staat in wit: de groene nadruk zou hier verwarren.

**Onderschrift:** `I made a Blender add-on that places a click hinge for knees and elbows: it bends to 115° and stops there, instead of flopping backwards. Bend it past the stop and the overshoot shows in red. Ball joints are free on Blender Extensions; the click hinge is in Click Joints Pro on Gumroad (link in bio). Measured in Blender, not printed yet. #blender #3dprinting #b3d #blenderaddon #articulated`

Elke bewering komt uit de ingediende Superhive-tekst en BlenderNation C44 (`commercie/blender-click-joints/lancering.md`): click hinge voor knieën en ellebogen, 0° tot 115° en daar stoppen "instead of flopping backwards", rood voorbij de stop (in beeld: het stuk van de gradenboog voorbij 115° en "+9° past limit"), kogel en kom gratis. Geen prijs in beeld of onderschrift, want de lanceerprijs van $9 duurt maar twee weken. "Not printed yet" staat erbij, net als in C44 ("I haven't printed a joint with it yet").
**Link in bio voor dit filmpje (run 66):** https://duinhouwer8.gumroad.com/l/click-joints-pro (Pro staat daar sinds 16 nov); later Superhive https://superhivemarket.com/products/click-joints-pro als die pagina openbaar is, of dortus.com/click-joints/ zodra het Pro-blok daar op main staat; die pagina linkt naar gratis en Pro samen.
Let op: het bestand staat al in de openbare prerelease `filmpjes-week-1`, net als de rest een concept. Dat breekt geen regel; plaatsen op TikTok, Shorts en Reels pas na Pro live.
Nagekeken door een controleur (run 47): techniek, beweringen, echte beelden en workflow ja; moet-punt (onderste regels in de strook van de apps) verwerkt; kan-punten verwerkt: red niet groen, "overshoot shows in red" in plaats van "parts turn red" (in beeld zie je alleen de boog rood), de precieze AI-zin zoals bij filmpje 4.

### 6. `ebb-6-sea-animals.mp4` (14,4 s; run 49 tekst omlaag naar y 240, moet M5 van Daan), Ebb, format 1 en 4: dieren in snel ritme, korte regels boven
Gemaakt in run 48 (15 nov ±23:50 tot 16 nov ±00:30 UTC), het tweede Ebb-filmpje volgens punt 4 van de opdracht (na filmpje 5 voor Click Joints). Ander verhaal dan filmpje 4: niet het ademen, maar de verzameling van 24 zeedieren. Bron: 11 losse schermen uit dezelfde simulatorrun 43327097299 op commit e40269e1 (de ingediende app, fenix 8 47 mm), map `garmin-adem/plaatjes/namen/` op tak `schermen`; de workflow haalt ze op en toetst de sha256. **Rond uitgesneden tot het horloge op de donkere achtergrond**, zonder de witte rand en menubalk van de simulator (een mogelijk antwoord op de vraag over filmpje 4 hieronder). Harde knippen met een kleine zoom, geen overvloeiers, dus geen beweging die de app niet heeft.
| tijd | beeld (scherm uit de simulator) | tekst in beeld |
|---|---|---|
| 0 tot 0,9 s | inhouden, onder water met de krab | My breathing app for Garmin has **24** sea animals |
| 0,9 tot 2,7 s | octopus, zeepaardje | (zelfde) |
| 2,7 tot 6,3 s | schildpad, otter, kreeft, zeekomkommer | You earn them by **showing up**, never by holding longer |
| 6,3 tot 8,7 s | eindscherm "new friend: Sea cucumber" | Your streak counts **weeks**, so rest days never break it |
| 8,7 tot 12 s | sea log "8 of 24", dan "24 of 24 + bonus" | Pick the one that **swims with you** |
| 12 tot 14,4 s | menu met de krab | Ebb, on the Connect IQ Store, link in bio |
Sinds run 49 staat de tekst op y 240 (zoals 1 tot 4), want op y 110 viel de eerste regel onder de bovenbalk van TikTok en Shorts. Klein, de hele tijd, op y 425: "Screens from the Garmin simulator". Horloge op y 470, marge 1,2, onderkant ±1470.

**Onderschrift:** `I made a breathing app for Garmin watches with 24 sea animals to collect. You earn them with sessions and weeks in a row, never by holding your breath longer, and your streak counts the weeks you hit your goal, so rest days never break it. Ebb, $4.99 one time, no subscription (link in bio). For practice on land only: sit or lie down. Screens from the Garmin simulator. #garmin #connectiq #garminwatch #breathwork`

Elke bewering staat letterlijk in de winkeltekst 19a (`platformen/garmin/upload/ebb-en.md`, deel COLLECT SEA ANIMALS BY SHOWING UP): "24 sea animals, earned with sessions and weeks in a row, never by holding longer", "Your streak counts weeks ... so rest days never break it", "Pick the one that swims with you", "plus one bonus animal" (daarom "24 of 24 + bonus" in beeld), $4,99 eenmalig zonder abonnement. Bewust niet: geen gezondheidsclaim, geen freediving, niet "every session a new animal". De hold-schermen tonen allemaal 1:45 en 61 bpm: dat is één testscène met steeds een ander dier, geen echte sessies; daarom geen tijd of hartslag in de tekst. Ebb Calm noem ik niet (nog niet openbaar, API 15 nov 23:4x UTC "not approved").
**Link in bio:** de winkellink van Ebb, zoals bij filmpje 4.
Nagekeken door een controleur (run 48): beweringen, bronnen (sha256 zelf nagerekend), workflow en techniek ja; moet-punt (in `maak.py` overschreef de ronde uitsnede de hoogte van het beeld, waardoor de kast ±15 px in de strook van de apps viel) opgelost, nu onderkant y 1439; kan-punten verwerkt: eerste knip op 0,9 s, "Tag me" in plaats van "Tag us", onderschrift "the weeks you hit your goal". Niet verwerkt: minder dieren achter elkaar; de tekst "never by holding longer" staat er juist dan in beeld.

## 7. `click-joints-7-tip-day-1-clearance.mp4` (12,5 s, run 51): eerste tip
Eerste filmpje van de reeks "Printable joints in Blender, day N" (hoofdchat 16 nov 05:00: vier op vijf filmpjes een tip). Uitleg, tabel, onderschrift en de nieuwe volgorde (de filmpjes van week 1 worden de productplekken op dag 5, 10 en 15): `commercie/filmpjes/reeks.md`. Run 52 (16 nov ±06:00 UTC): Daan zei ja met één moet (paneel netjes uitsnijden, `ontwerp/filmpjes/keuring-f7-tip-day-1.md`); zijn json met die uitsnede en Brams nieuwe tekst ("clicks in but won't turn", "0.2 mm per side") ongewijzigd overgenomen en opnieuw gebouwd (workflowrun 43812402655 groen, release 05:48 UTC, beelden GEZIEN 05:52 UTC). Nog open: Bram bevestigt "Try" in plaats van "Start around", daarna het ja van Thijs.

## 9. `ebb-tip-1-eyes-closed.mp4` (11 s, run 54, aangepast run 55): eerste Ebb-tip, Daan ja
Tip 3 uit de lijst in `reeks.md` (ogen dicht, voel het trillen), omdat die het dichtst bij wat Ebb echt doet ligt: de winkeltekst van Ebb zegt "Every phase has its own vibration" en "Follow every phase by vibration with your eyes closed" (`platformen/garmin/upload/ebb-en.md`). Geen gezondheidsclaim, geen inhouden, geen freediving. (f8 blijft voor dag 2 van Click Joints.)
- **Beeld:** drie schermen uit de simulator, fenix 8 47 mm, map `garmin-adem/plaatjes/namen/` op tak `schermen` (`krab2-in-nacht`, `krab2-uit-nacht`, `krab2-calm-nacht`), rond uitgesneden tot alleen het scherm (geen rand met het woord GARMIN), op donker. In, uit, in, uit (elk 2 s, het water gaat op en neer), dan 3 s 4-7-8 ("breathe out 5").
- **Tekst in beeld (y 225 tot 235, onder de bovenbalk; horloge op y 380):** "Breathing exercise / *on your watch?*" (0 tot 3,6 s), "Don't stare at the screen. / *Close your eyes*, follow the buzz" (3,6 tot 8 s; run 55: twee regels op y 235, was drie regels op y 225), "My app Ebb gives every / phase *its own buzz*" (8 tot 11 s). Onder het horloge klein, op y 1450 boven de strook van de app (Daan, f7): "Screens from the Garmin simulator". Eerste build had die regel op y 1610, onder de strook; verbeterd na de controleur.
- **Eerlijk:** het trillen zelf zie of voel je in een filmpje niet; de laatste zin zegt alleen wat de app doet. Stilstaande schermen met harde wissels, geen opname van een echt horloge.
- **Onderschrift (concept):** `Breathing exercise on your watch? Close your eyes and follow the vibration instead of the screen. Sit or lie down. Ebb is my breathing app for Garmin, link in bio. #garmin #breathing #breathwork #calm #smartwatch` (geen gezondheidsclaim, "sit or lie down" zoals in de winkeltekst).
- **Gebouwd:** lokaal met `maak.py`, 1080 x 1920, H.264, 11,0 s, geen geluid, 0,72 MB; beeld per seconde zelf bekeken (GEZIEN 16 nov ±07:55 UTC). De workflow bouwt hem in de release `filmpjes-week-1` (bronnen en sha256 erbij).
- **Controleur (run 54):** akkoord mits; moet-punt (simulatorregel op y 1610 viel onder de strook van TikTok) verwerkt. Kan: in en uit komen uit de stand met rondes ("round 2 · 18 breaths left"); er is per dier maar één calm-scherm, dus geen beter alternatief nu.
- **Daan (16 nov ±08:40 UTC, `ontwerp/filmpjes/keuring-f9-ebb-tip-1.md`):** ja met twee moet-punten. Verwerkt in run 55 (±09:00 UTC): (1) middelste tekst twee regels, zijn voorkeur (a), op y 235; afstand tot de bovenkant van het scherm nu ±70 px (was ±30). (2) Straal van `rond` 224 naar 220, zodat de twee grijze boogjes van de simulatorrand wegvallen; het horloge wordt daardoor ±2 % groter, de plek (y 380) blijft. Lokaal gebouwd met `maak.py` (11,0 s) en bekeken op 1,0 / 6,0 / 9,5 s, bovenrand van het scherm op ware grootte vergroot: geen boogjes meer (GEZIEN 16 nov ±09:00 UTC). Beeld uit het middelste stuk voor Daan: `commercie/filmpjes/f9-midden-run55.jpg`. Harde wissels blijven (Daan: ja). Workflowrun 43833944803 op 0ed4ee6 groen; de mp4 in de release (0,73 MB) opnieuw gedownload en het beeld op 6,0 s bekeken: twee regels, geen boogjes (GEZIEN 16 nov ±09:10 UTC).
- **Wacht op:** Gijs (klopt het met wat Ebb doet: trillen per fase, ook bij 4-7-8?). Daarna op lijst-thijs.
- **Run 56 (16 nov ±09:55 UTC): klaar.** Gijs (09:00): klopt, ook bij Calm 4-7-8 trilt elke fase anders (code van tag `ebb-v1.0.0`); "its own buzz" mag, "you can feel the difference" niet, want niemand voelde het op een echt horloge. Daan (09:50): ja, klaar. Zijn kan-punt verwerkt: regel 2 eindigt nu ook op een punt ("follow the buzz."). Op lijst-thijs.

## 10 tot 12: Hats of the Fallen voor @hatsofthefallen (run 56, concept, wacht op Daan)
Opdracht hoofdchat 16 nov 09:40 (ja Thijs 09:37): eerste reeks van 3 spelfilmpjes, staand, 7 tot 15 s, eerste seconde al beweging, tekst in beeld, de haak "He wears their hats.". De workflow eist 10 tot 20 s, dus alle drie zitten tussen 10 en 15 s.
- **Beeld:** alleen echte opnames uit de Windows-build, door Olaf aangeleverd op tak `schermen` (`steam-hol/winkel-1920-demo-160/los/` en `steam-hol/winkel-1920-week-160-claude-steam-hol-vol/los/`), vastgezet op commit 453aac1 met sha256 per beeld in `bronnen.sha256`. Welke beelden: `week-1/spel-bronnen.txt`; ophalen: `week-1/spel-bronnen.sh`. De strook is 1920 x 160; ik snij er een stuk van 480 x 160 uit (Gloop en de gang ervoor) en vergroot dat 2,25 keer naar 1080 x 360, op y 720. Niets getekend of verzonnen.
- **Eerlijk:** de losse beelden zijn elk 5e beeld van 15 per s, dus 3 beelden per s. Het filmpje loopt daardoor schokkerig, als stop-motion. Ik vul geen tussenbeelden in (dat zou beweging verzinnen die het spel niet zo liet zien). Onderaan op y 1450 klein: "Real footage, early build". Geen Steam-link of "wishlist", want er is nog geen winkelpagina (planning: ingediend 1 dec).
- **10. `hats-1-he-wears-their-hats.mp4` (11,4 s):** held met emmer loopt naar Gloop, hap, de emmer vliegt op de stapel, Gloop knipoogt (demofilm beeld 147 tot 180, hap rond 3 s). Tekst: "A hero came / *for the gold.*" (0 tot 2,7 s), "*He wears their hats.*" (2,7 tot 7,6 s), "Hats of the Fallen / a tiny dungeon *on your desktop*" (7,6 tot 11,4 s). In het log van het spel staat op dat moment "Gloop ate Joost. Kept the bucket."
- **11. `hats-2-the-tower-grows.mp4` (11,3 s):** held met hoge hoed wordt opgegeten, de hoed komt boven op emmer en kroon (demofilm beeld 196 tot 214), dan een andere, volle stand uit de weekopname: 4 hoeden op zijn hoofd (meer passen er niet, de rest gaat op een berg ernaast, `producten/steam-hol/godot/systemen/slijm.gd`) en een grote berg hoeden (beeld 0 tot 14). Tekst: "Gloop eats a hero.", "*The hat stays.*", "Keep him fed / *and the pile grows.*" (was "tower", na de controleur). Geen tijd genoemd ("a week later" kan ik niet hard maken).
- **12. `hats-3-heroes-come-back.mp4` (10,3 s):** Tibbe, met het wrok-wolkje boven zijn hoofd, loopt door de gang naar Gloop; de uitsnede (640 x 160, 1,69 keer) schuift rustig met hem mee tot Gloop en het goud rechts in beeld komen (demofilm beeld 176 tot 198). Tekst: "Tibbe touched the gold.", "*Now he is back / for Gloop.*", "Heroes hold / *a grudge.*". Bewijs: in de demofilm zegt het log "Tibbe is now the Hoard-Toucher." en daarna "Tibbe the Hoard-Toucher is back for Gloop." Zwakste van de drie: het verband is op deze grootte niet te zien, alleen het wolkje, en Gloop komt pas aan het eind klein in beeld. Met een echte mp4 van Olaf (dichterbij, 15 per s) wordt hij beter.
- **Gebouwd:** lokaal met `maak.py` (nieuw: een segment met `beelden` voor een map met PNG's, en `pan` om de uitsnede te laten meeschuiven; de andere filmpjes veranderen daar niet door), 1080 x 1920, H.264, geen geluid; bladen per seconde zelf bekeken (GEZIEN 16 nov ±09:55 UTC). De workflow bouwt ze in de release `filmpjes-week-1`.
- **Onderschriften (concept, Engels):** 10: `He eats the heroes who come for his gold. Then he wears their hats. A tiny dungeon game that lives at the bottom of your screen, made by my studio Dortus. Early build. #indiegame #gamedev #cozygames #desktopgame`; 11: `Every hero Gloop eats leaves a hat. Four on his head, the rest on the pile. Early build of our desktop game. #indiegame #gamedev #cozygames`; 12: `Heroes who get away remember. This one came back for Gloop. Early build. #indiegame #gamedev #cozygames`. Geen belofte over prijs of datum.
- **Vraag aan Daan:** ja of nee per filmpje. Twijfels: (a) 3 beelden per s, schokkerig: goed genoeg als eerste reeks of wachten op Olafs mp4's na 20 nov? (b) de strook vult maar 360 px van de 1920 hoogte; groter snijden maakt Gloop wazig. (c) filmpje 12 leunt op het wolkje; Gloop komt pas aan het eind klein in beeld.
- **Controleur (run 56):** akkoord mits; drie moet-punten verwerkt: toren is hooguit 4 hoeden (tekst 11 nu "pile", onderschrift aangepast), "made by my studio Dortus" in plaats van "made by me" (besluit in het logboek), uitsnede van 12 schuift nu tot Gloop in beeld is. Kan-punt verwerkt: uitsnede 10 en 11 begint op x 985, zodat het randje van het logvak wegvalt.
- **Aan Olaf (welke echte mp4's eerst):** zie `berichten/olaf.md`.

## Wanneer plaatsen
- **Volgorde:** 2 (kort en satisfying, het sterkste format bij de best bekeken filmpjes), dan 4 (Ebb), dan 1, dan 6 (Ebb), dan 3, zodat Click Joints en Ebb wisselen (run 48: 6 tussen 1 en 3 gezet). Eén per dag, alle drie de apps hetzelfde filmpje. Filmpje 5 (Pro) gaat voor zodra Pro live is: plaats het op de eerste werkdag daarna, ook als de reeks dan even niet wisselt.
- **Tijd:** rond **16:00 Nederlandse tijd** (15:00 UTC), op werkdagen. Waarom: de kijkers zitten vooral in Europa en de VS; om 16:00 NL is het 10:00 aan de oostkust en is Europa nog wakker (GOK, ik kon geen cijfers over Blender-kijkers per uur meten). Na 10 filmpjes vergelijken we de tijden met de echte views en passen we het aan.
- **Link in bio:** zet in het profiel van TikTok, YouTube en Instagram de listing `https://extensions.blender.org/add-ons/click-joints/`. Niet dortus.com/click-joints/: die pagina zegt nog "On its way" zonder knop (GEZIEN 15 nov ±22:20 UTC met curl); de knop staat klaar op tak `claude/chris-click-joints-live` in repo dortus en gaat op main met jouw ja (punt van 14 nov op de lijst). Zonder link heeft "link in bio" geen zin. Op de dag van het Ebb-filmpje wordt de link de winkellink van Ebb: https://apps.garmin.com/apps/5280653d-1681-452d-8c03-7cbdc7284641
- **Geluid:** kies in de app een rustig, populair instrumentaal geluid; geen liedje met tekst dat de tekst in beeld overstemt.

## Uitnodiging aan makers (tip van Joris, 16 nov 00:15, verwerkt in run 48)
Uit het verhaal van McGybeer (`platformen/succes/verhalen-groei.md`): de beweegbare draak groeide door filmpjes van anderen met de print in hun hand. Daarom komt aan het eind van elk onderschrift voor Click Joints (1, 2, 3 en 5) deze zin, vóór de hashtags: `Made something with Click Joints? Tag me, I'd love to see it.` Bij het plakken dus: onderschrift zoals hierboven, met deze zin vlak voor de eerste #. Niet bij Ebb (daar is niets om te laten zien). Zijn eerste tip (een filmpje van 8 tot 12 s met de figuur die buigt in een hand) kan pas met een echte print; een render "in een hand" maken we niet, want we hebben geen echte hand in beeld en het zou op een print lijken (`formats.md` format 3). Open: Joris vraagt dezelfde uitnodiging ook op de Pro-pagina; die zet ik op tak `claude/chris-click-joints-pro` (repo dortus) in een volgende run, samen met de link naar het account zodra Thijs dat heeft.

## Vraag aan Daan (ontwerper), beantwoord 16 nov ±02:30 UTC in `ontwerp/filmpjes/keuring-week-1.md`
Kijk de drie filmpjes in de release na: ja of nee met moet-punten. Waar ik zelf twijfel: (a) het beeld staat in een vlak van 1080 x 1013 met donkere ruimte eronder, zodat de knoppen van de apps niets bedekken; wil je het beeld groter? (b) in filmpje 3 staan de previews stil (met een langzame zoom); (c) de rode band in de exploded view (filmpje 1 op 7,5 s, filmpje 3 op 11 s) leg ik niet uit, want ik wil er niets over beweren wat niet klopt; in filmpje 3 komt hij vlak na "Red means too far" en kan dat verwarren. Liever een ander stuk? Dan pas ik het json-bestand aan. (d) run 48: filmpje 6 (Ebb) staat rond uitgesneden op donker, zonder de witte simulatorrand; zo ja, dan maak ik filmpje 4 ook zo.

**Antwoorden van Daan (16 nov):** (a) nee, de donkere ruimte is precies waar naam en onderschrift van de app komen; (b) goed genoeg, 4 s laten staan; (c) rode close-up eruit in 1 en 3 (M1, M2); (d) ja, filmpje 4 ook rond op donker (M4). Kan-punten voor week 2: elk Click Joints-filmpje anders laten beginnen (1, 2 en 3 beginnen nu alle drie met de ring en de pop), eventueel een eindkaart van 1,5 s in 2, later een filmpje met de sea log groot in beeld. Die neem ik mee bij de volgende filmpjes.

Nagekeken door een controleur (run 45): techniek, beweringen, onderzoek en workflow ja; zijn moet-punt (twee teksten één beeld lang door elkaar bij elke wissel) is opgelost, en zijn kan-punten ("Place the joint" in plaats van "Click where the joint goes", eindkaart eerder) zijn verwerkt.

## Daarna
Elke dag één nieuw filmpje, wisselend Click Joints en Ebb (Ebb: schermen uit de simulator, zee die stijgt en zakt, geen gezondheidsclaims, niet als freediving). Het sterkste format voor Click Joints, een echte geprinte figuur in een hand (format 3 in `formats.md`), kan pas als iemand een figuur print.
