# Filmpjes week 1: Click Joints (concept, wacht op Daan)

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

## Wanneer plaatsen
- **Volgorde:** 2 (kort en satisfying, het sterkste format bij de best bekeken filmpjes), dan 1, dan 3. Eén per dag, alle drie de apps hetzelfde filmpje.
- **Tijd:** rond **16:00 Nederlandse tijd** (15:00 UTC), op werkdagen. Waarom: de kijkers zitten vooral in Europa en de VS; om 16:00 NL is het 10:00 aan de oostkust en is Europa nog wakker (GOK, ik kon geen cijfers over Blender-kijkers per uur meten). Na 10 filmpjes vergelijken we de tijden met de echte views en passen we het aan.
- **Link in bio:** zet in het profiel van TikTok, YouTube en Instagram de listing `https://extensions.blender.org/add-ons/click-joints/`. Niet dortus.com/click-joints/: die pagina zegt nog "On its way" zonder knop (GEZIEN 15 nov ±22:20 UTC met curl); de knop staat klaar op tak `claude/chris-click-joints-live` in repo dortus en gaat op main met jouw ja (punt van 14 nov op de lijst). Zonder link heeft "link in bio" geen zin.
- **Geluid:** kies in de app een rustig, populair instrumentaal geluid; geen liedje met tekst dat de tekst in beeld overstemt.

## Vraag aan Daan (ontwerper)
Kijk de drie filmpjes in de release na: ja of nee met moet-punten. Waar ik zelf twijfel: (a) het beeld staat in een vlak van 1080 x 1013 met donkere ruimte eronder, zodat de knoppen van de apps niets bedekken; wil je het beeld groter? (b) in filmpje 3 staan de previews stil (met een langzame zoom); (c) de rode band in de exploded view (filmpje 1 op 7,5 s, filmpje 3 op 11 s) leg ik niet uit, want ik wil er niets over beweren wat niet klopt; in filmpje 3 komt hij vlak na "Red means too far" en kan dat verwarren. Liever een ander stuk? Dan pas ik het json-bestand aan.

Nagekeken door een controleur (run 45): techniek, beweringen, onderzoek en workflow ja; zijn moet-punt (twee teksten één beeld lang door elkaar bij elke wissel) is opgelost, en zijn kan-punten ("Place the joint" in plaats van "Click where the joint goes", eindkaart eerder) zijn verwerkt.

## Daarna
Elke dag één nieuw filmpje, wisselend Click Joints en Ebb (Ebb: schermen uit de simulator, zee die stijgt en zakt, geen gezondheidsclaims, niet als freediving). Het sterkste format voor Click Joints, een echte geprinte figuur in een hand (format 3 in `formats.md`), kan pas als iemand een figuur print.
