# Filmpjes week 1: Click Joints en Ebb (concept, wacht op Daan; filmpje 5 pas na Pro live)

Door Chris, 15 nov 2026, run 45. Opdracht: besluit Thijs 15 nov 22:53 (`berichten/chris.md`). Onderzoek vooraf: `commercie/filmpjes/formats.md`.

**Niemand plaatst zonder akkoord van Daan en het ja van Thijs.** Thijs kiest bij het plaatsen zelf een geluid uit de app; de bestanden hebben geen geluid.

## Waar de bestanden staan
- Release `filmpjes-week-1` in dortus-hq (gemaakt door de workflow `.github/workflows/filmpjes-week-1.yml`): drie mp4's, per filmpje een strook met één beeld per seconde (`-beelden.jpg`) en `SHA256SUMS.txt`. https://github.com/thijsduinhouwer2002-coder/dortus-hq/releases/tag/filmpjes-week-1
- Bron om ze opnieuw te maken: `commercie/filmpjes/week-1/` (`maak.py`, `f1.json` tot `f3.json`, `bronnen.sha256`). Tekst of timing aanpassen = het json-bestand aanpassen en pushen; de workflow bouwt dan opnieuw.
- Alle drie: 1080 x 1920, H.264 (`-preset veryfast`), 30 beelden per seconde, geen geluid, Engelse tekst in beeld bovenaan (buiten de knoppen van TikTok en Shorts onderaan en rechts). Alleen het kleine label met de naam (op 82% van de hoogte) kan onder het onderschrift van de app vallen; dat is niet erg, de naam staat ook bovenaan en op de eindkaart.

## Alleen echte beelden
- Film v2 van Bram (`click-joints-filmisch-v2.mp4`, gerenderd in de echte Blender met de add-on, Thijs zei 9 nov "film Click Joints ja"; sha256 `f6d54416…`).
- De twee previews van de gratis versie 0.1.0 op extensions.blender.org (`3-preview-buigen.png`, `4-preview-paneel.png`, schermen uit de echte add-on).
- Geen gezicht, geen stem, geen nep-persoon, geen AI-beeld. "I made" in de eerste persoon klopt: Thijs maakt het met hulp van AI, en dat staat ook in het onderschrift.
- Alleen de **gratis** versie. Pro staat er niet in, want Pro is nog niet te koop (Superhive keurt nog). Een Pro-filmpje komt na de goedkeuring.

## De drie filmpjes

### 1. `click-joints-1-bend-far-enough.mp4` (18,5 s), format 2: vraag boven, beeld in het midden
| tijd | beeld | tekst in beeld |
|---|---|---|
| 0 tot 0,5 s | gloeiende ring, close-up | Will this joint bend far enough? |
| 0,5 tot 4,5 s | tekenpop die schopt | (tot 2,2 s de vraag) I made a free Blender add-on that **checks** it |
| 4,5 tot 7,5 s | arm buigt, ring op het gewricht | Place the joint. **Drag** the bend. |
| 7,5 tot 9,2 s | exploded view | Exploded view: ball and socket apart |
| 9,2 tot 15,5 s | arm buigt verder | Green ring = **good fit**, in mm |
| 15,5 tot 18,5 s | pop vervaagt in de eindkaart uit film v2 | Free on Blender Extensions, link in bio |

**Onderschrift:** `I made a free Blender add-on that shows how far a joint bends before you 3D print it. Place a joint, drag the bend, check the fit in mm, export STL or 3MF. Click Joints, free on Blender Extensions (link in bio). Built with help from AI. #blender #3dprinting #b3d #blenderaddon #articulated`

### 2. `click-joints-2-satisfying-bend.mp4` (10,2 s), format 1: één vaste regel, loopt rond
Ring gloeit (0,5 s), arm buigt (3,9 s), arm buigt verder met de ring (5,8 s). Vaste tekst: "See how far a joint **bends**, before you print." en klein onderaan "Click Joints, a free Blender add-on". Dit is de winkelzin van de listing, dus overal hetzelfde.

**Onderschrift:** `See how far a joint bends, before you print. Click Joints is a free Blender add-on for articulated, poseable 3D prints (link in bio). Built with help from AI. #blender #3dprinting #printinplace #blenderaddon`

### 3. `click-joints-3-three-checks.mp4` (16,7 s), format 4: lijstje zonder gezicht
| tijd | beeld | tekst in beeld |
|---|---|---|
| 0 tot 3 s | ring, tekenpop | 3 things my free Blender add-on **checks** before you print |
| 3 tot 7 s | preview: buig 28°, rode wig | 1. How far it bends. **Red** means too far. |
| 7 tot 11 s | preview: paneel met Good fit, wand, speling | 2. The fit, measured in **mm**: wall and clearance |
| 11 tot 13,7 s | exploded view, arm | 3. Exploded view, then one STL or 3MF per part |
| 13,7 tot 16,7 s | eindkaart | Free on Blender Extensions, link in bio |

**Onderschrift:** `3 things my free Blender add-on checks before you 3D print a poseable figure: how far each joint bends, the fit in mm (wall and clearance), and clean parts as STL or 3MF. Click Joints, link in bio. Built with help from AI. #blender #3dprinting #b3d #blenderaddon #3dprint`

Elke bewering komt uit de listing of de previews: "Drag the bend. Red means too far", "Good fit, measured in mm", "One STL or 3MF per part, in mm", "Exploded view" (winkeltekst en previews 0.1.0, GEZIEN).

### 4. `ebb-4-sea-rises.mp4` (14,3 s), Ebb, format 2: tekst boven, horloge in het midden
Extra gemaakt in run 46 (extra run van Thijs, 15 nov 23:00), zodat de dagelijkse reeks wisselend Click Joints en Ebb kan beginnen. Bron: `commercie/ebb/ebb-film.mp4`, schermen uit de simulatorrun 43327097299 van de ingediende app (fenix 8 47 mm), zie `commercie/ebb/lancering.md` punt 3. Opgeschaald van 600 naar 1080 pixels.
| tijd | beeld | tekst in beeld |
|---|---|---|
| 0 tot 2,6 s | menu met de krab | I made a breathing app for **Garmin** watches |
| 2,6 tot 7,2 s | in- en uitademen, water op en neer | The sea **rises** and **falls** with your breath |
| 7,2 tot 9,5 s | inhouden, onder water met de krab | Hold, and you go **under water** |
| 9,5 tot 12 s | "new friend: Starfish", sea log "8 of 24" | New sea creatures join your **sea log** |
| 12 tot 14,3 s | sea log | Ebb, on the Connect IQ Store, link in bio |
Onderaan de hele tijd klein: "Screens from the Garmin simulator" (eerlijk: geen opname van een echt horloge, en het water is een overvloeier tussen twee schermen).

**Onderschrift:** `I made a breathing app for Garmin watches: the sea rises and falls with your breath, and when you hold, you go under water. Sea creatures join your sea log as you keep coming back. Ebb, $4.99 one time, no subscription (link in bio). For practice on land only: sit or lie down. Screens from the Garmin simulator. AI agents write the code, I direct and test. #garmin #connectiq #breathwork #garminwatch`

Bewust niet: geen gezondheidsclaim (geen "calmer", "better sleep", "lung capacity"), geen freediving, geen "every session a new animal" (dieren komen door sessies en weken op rij). Alle beweringen staan in de winkeltekst (stijgen en zakken, onder water bij inhouden, 24 dieren, $4,99 eenmalig zonder abonnement). Ebb Calm (gratis) noem ik niet: nog niet openbaar. Link in bio voor dit filmpje: de winkellink van Ebb uit `commercie/ebb/lancering.md`; één link in het profiel kan maar één product tonen, dus wissel hem mee of gebruik later één pagina op dortus.com met beide.
Nagekeken door een controleur (run 46): filmpje en workflow ja; tekst eerst nee ("as you keep going" las alsof langer inhouden dieren oplevert, en de vaste zin over alleen op het droge ontbrak), beide verwerkt, plus de precieze AI-zin uit `lancering.md`.
Voor Daan: de schermen hebben een witte achtergrond rond het horloge (zo uit de simulator); liever donker of bijgesneden tot het horloge?

### 5. `click-joints-5-pro-hinge-stops.mp4` (16,3 s), Click Joints Pro, format 2: tekst boven, beeld vult het scherm
**Pas plaatsen als Click Joints Pro live is op Superhive** (keuring loopt sinds 15 nov 19:45). Tot die dag is het een concept voor de lanceerdag van Pro. Gemaakt in run 47 uit de vijf staande opnames die Bram op 15 nov 22:35 maakte in de echte Blender 5.3.0 met de betaalde zip 1.0.1 (`ontwerp/click-joints/pro/film/staand/`, LEESMIJ daar). Deze opnames zijn al 1080 x 1920, dus geen uitsnede uit een liggende film: het beeld vult het hele scherm en het gewricht is groter dan in 1 tot 3. Het grijze label "Bends 0° to 115°" bovenaan zit in Brams opname zelf.
| tijd | beeld (opname van Bram) | tekst in beeld |
|---|---|---|
| 0 tot 2 s | deel 1: knie buigt van 0 naar 115° met de gradenboog | A printable **knee** that stops at 115° |
| 2 tot 5,3 s | deel 2: been draait, Place hinge, twee delen met groen | I made a Blender add-on that places a click **hinge** |
| 5,3 tot 9,8 s | deel 3: buigt van 0 naar 115° en blijft 1 s op de stop | It bends to 115° and **stops**, instead of flopping backwards |
| 9,8 tot 13 s | deel 4: 9° voorbij de stop, rood en "+9° past limit" | Past the stop? It turns red. |
| 13 tot 16,3 s | deel 5: kogel en kom uit elkaar (gratis versie) | Ball joints: **free**. Click hinges: **Pro**. Link in bio |
Klein, de hele tijd: "Click Joints Pro, a Blender add-on" op y 1380 en "Link in bio" op y 1290, boven de strook van ±420 px onderaan waar de apps naam en onderschrift zetten (moet-punt controleur). Het woord red staat in wit: de groene nadruk zou hier verwarren.

**Onderschrift:** `I made a Blender add-on that places a click hinge for knees and elbows: it bends to 115° and stops there, instead of flopping backwards. Bend it past the stop and the overshoot shows in red. Ball joints are free on Blender Extensions; the click hinge is in Click Joints Pro on Superhive (link in bio). Measured in Blender, not printed yet. AI agents write the code, I direct and test. #blender #3dprinting #b3d #blenderaddon #articulated`

Elke bewering komt uit de ingediende Superhive-tekst en BlenderNation C44 (`commercie/blender-click-joints/lancering.md`): click hinge voor knieën en ellebogen, 0° tot 115° en daar stoppen "instead of flopping backwards", rood voorbij de stop (in beeld: het stuk van de gradenboog voorbij 115° en "+9° past limit"), kogel en kom gratis. Geen prijs in beeld of onderschrift, want de lanceerprijs van $9 duurt maar twee weken. "Not printed yet" staat erbij, net als in C44 ("I haven't printed a joint with it yet").
**Link in bio voor dit filmpje:** https://superhivemarket.com/products/click-joints-pro (pas als die pagina openbaar is), of dortus.com/click-joints/ zodra het Pro-blok daar op main staat; die pagina linkt naar gratis en Pro samen.
Let op: het bestand staat al in de openbare prerelease `filmpjes-week-1`, net als de rest een concept. Dat breekt geen regel; plaatsen op TikTok, Shorts en Reels pas na Pro live.
Nagekeken door een controleur (run 47): techniek, beweringen, echte beelden en workflow ja; moet-punt (onderste regels in de strook van de apps) verwerkt; kan-punten verwerkt: red niet groen, "overshoot shows in red" in plaats van "parts turn red" (in beeld zie je alleen de boog rood), de precieze AI-zin zoals bij filmpje 4.

## Wanneer plaatsen
- **Volgorde:** 2 (kort en satisfying, het sterkste format bij de best bekeken filmpjes), dan 4 (Ebb), dan 1, dan 3, zodat Click Joints en Ebb wisselen. Eén per dag, alle drie de apps hetzelfde filmpje. Filmpje 5 (Pro) gaat voor zodra Pro live is: plaats het op de eerste werkdag daarna, ook als de reeks dan even niet wisselt.
- **Tijd:** rond **16:00 Nederlandse tijd** (15:00 UTC), op werkdagen. Waarom: de kijkers zitten vooral in Europa en de VS; om 16:00 NL is het 10:00 aan de oostkust en is Europa nog wakker (GOK, ik kon geen cijfers over Blender-kijkers per uur meten). Na 10 filmpjes vergelijken we de tijden met de echte views en passen we het aan.
- **Link in bio:** zet in het profiel van TikTok, YouTube en Instagram de listing `https://extensions.blender.org/add-ons/click-joints/`. Niet dortus.com/click-joints/: die pagina zegt nog "On its way" zonder knop (GEZIEN 15 nov ±22:20 UTC met curl); de knop staat klaar op tak `claude/chris-click-joints-live` in repo dortus en gaat op main met jouw ja (punt van 14 nov op de lijst). Zonder link heeft "link in bio" geen zin. Op de dag van het Ebb-filmpje wordt de link de winkellink van Ebb: https://apps.garmin.com/apps/5280653d-1681-452d-8c03-7cbdc7284641
- **Geluid:** kies in de app een rustig, populair instrumentaal geluid; geen liedje met tekst dat de tekst in beeld overstemt.

## Vraag aan Daan (ontwerper)
Kijk de drie filmpjes in de release na: ja of nee met moet-punten. Waar ik zelf twijfel: (a) het beeld staat in een vlak van 1080 x 1013 met donkere ruimte eronder, zodat de knoppen van de apps niets bedekken; wil je het beeld groter? (b) in filmpje 3 staan de previews stil (met een langzame zoom); (c) de rode band in de exploded view (filmpje 1 op 7,5 s, filmpje 3 op 11 s) leg ik niet uit, want ik wil er niets over beweren wat niet klopt; in filmpje 3 komt hij vlak na "Red means too far" en kan dat verwarren. Liever een ander stuk? Dan pas ik het json-bestand aan.

Nagekeken door een controleur (run 45): techniek, beweringen, onderzoek en workflow ja; zijn moet-punt (twee teksten één beeld lang door elkaar bij elke wissel) is opgelost, en zijn kan-punten ("Place the joint" in plaats van "Click where the joint goes", eindkaart eerder) zijn verwerkt.

## Daarna
Elke dag één nieuw filmpje, wisselend Click Joints en Ebb (Ebb: schermen uit de simulator, zee die stijgt en zakt, geen gezondheidsclaims, niet als freediving). Het sterkste format voor Click Joints, een echte geprinte figuur in een hand (format 3 in `formats.md`), kan pas als iemand een figuur print.
