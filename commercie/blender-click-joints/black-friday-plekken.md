# Click Joints Pro: gratis plekken voor Black Friday (Chris, 20 nov 2026, run 87)

Opdracht: hoofdchat 19 nov 23:55 punt 3 (bereik: Gumroad 8 keer bekeken in 30 dagen, 0 verkopen). Per plek: wat het is, wat het oplevert, wie het doet, en een concept met meetadres. Niets is verstuurd of geplaatst. Alles onder de naam van Thijs wacht op zijn ja; plekken zonder zijn naam doet de hoofdchat.

**Meetadres:** `https://dortus.com/click-joints/?van=<code>` (code per plek hieronder). De pagina telt bezoeken met Umami (script staat op de pagina, GEZIEN); of Umami de `?van=` apart laat zien is een GOK, de verwijzende site staat er in elk geval bij. Op plekken die zelf naar Superhive linken meten we via Superhive.

**Eerst repareren (voor alles hieronder):** dortus.com/click-joints/, /yt/ en /tt/ zeggen "$12", maar de knop gaat naar Gumroad, waar Pro $19 kost (GEZIEN 20 nov, curl: Personal $19, Supporter $24, Studio $59; Superhive $12 en $45). Wie vanaf de lange video van vandaag 17:00 klikt, ziet dus een hogere prijs dan beloofd. Wijziging voor de Click Joints-pagina staat klaar als patch: `prijs-site-2026-11-20.patch` (repo dortus, pushen mocht deze run niet). /yt/ en /tt/ zijn van Roep: daar hetzelfde nodig.

| # | Plek | Waarom | Wie | Thijs nodig? | Code |
|---|---|---|---|---|---|
| 1 | Addon Radar, formulier "Submit an add-on" | Gratis vermelding. Heeft een eigen Black Friday-pagina met afgeprijsde Superhive-add-ons (data bijgewerkt 19 nov, GEZIEN) plus "New on Superhive" en een nieuwsbrief. 7.805 add-ons in hun sitemap, Click Joints niet (GEZIEN). Met de sitebrede Cyber Sale van Superhive kan Pro dan vanzelf op hun Black Friday-pagina komen (GOK). | hoofdchat | nee: anoniem formulier, e-mail optioneel. Daan: ja (20 nov) | Superhive-link |
| 2 | BlenderArtists, categorie "Released Add-ons and Extensions" | Hier zetten makers hun add-ons, ook betaalde (regel van de categorie: "Must be tagged free or commercial", GEZIEN). Nieuwe topics deze week: 49 tot 117 keer bekeken in 1 tot 3 dagen (GEZIEN, categorie-JSON 20 nov). Klein, maar precies Blender-mensen, en het topic blijft staan. | hoofdchat met account | ja: account (aanmaken doet Thijs) en tekst onder zijn naam of Dortus | `ba` |
| 3 | CG Channel, Black Friday-lijst | Verstuurd 20 nov 09:27 (lijst-thijs). Niets meer doen; op 27 nov met curl kijken of we op de lijst staan. | Chris kijkt | nee | (Gumroad-link in de mail) |
| 4 | BlenderNation | Gratis inzending van 16 nov staat nog niet online (GEZIEN 20 nov, zoeken op "click joints"). Een bericht over een sale is commercieel en kost € 25 (GEZIEN eerder, submit-news), dus geld: alleen met ja van Thijs. Advies: niet doen; geen tweede gratis inzending vóór 23 nov. | - | ja (geld) | - |
| 5 | Gumroad Discover | Gumroad laat producten zien in Discover op categorie en tags. Kost niets, 2 minuten in de productinstellingen: categorie 3D, tags "blender", "blender addon", "3d printing", "ball joint", "action figure". Effect: GOK. | hoofdchat | nee (Gumroad beheert de hoofdchat al) | - |

Niet nu: tweede Reddit-post (account van Thijs, r/blender kreeg op 16 nov al een post; zelfpromotieregels zijn met curl niet te lezen) en r/3Dprinting of Printables (pas met een echte print). Makers en nieuwsbrieven mailen valt onder "iemand benaderen": alleen Thijs.

## 1. Addon Radar (concept voor het formulier op https://addonradar.com/submit/)
- **Name of the add-on:** `Click Joints Pro`
- **Link to it:** `https://superhivemarket.com/products/click-joints-pro`
- **What does it do?:**
```
Turns a rigged figure into printable parts that move. One button reads the armature: elbows and knees become hinges with an end stop, shoulders, hips and neck become ball joints, and each joint shows its range in degrees before you print. Red where parts hit past the stop, a green fit band for the clearance, export to STL or 3MF. Also on Gumroad. Free version (ball and pin joints): https://extensions.blender.org/add-ons/click-joints/
```
- **Your e-mail:** leeg laten (of thijs@dortus.com als de hoofdchat antwoord wil; dat is het zakelijke adres).
- Meten: na 3 dagen `curl -s https://addonradar.com/sitemap.xml | grep click-joints`, en op 27 nov hun Black Friday-pagina.

## 2. BlenderArtists (concept, wacht op account en ja Thijs)
Categorie: Released Add-ons and Extensions. Tag: commercial. Beeld: `gumroad-1.1/1-figuur-uit-rig.png` en de buigfilm `reddit-pro-buig-11s.mp4`.

**Titel:** `[Addon] Click Joints Pro: rig to printable figure [$]`

Bovenaan het topic eerst de buigfilm (`reddit-pro-buig-11s.mp4`), dan de tekst.

```
Click Joints Pro turns a rigged figure into printable parts that move.

Pick your rigged figure and press one button. Elbows and knees get a hinge with an end stop, shoulders, hips and neck get a ball joint. If a bone has a Limit Rotation constraint, the hinge stops at that angle. Next to every joint you see how far it bends, in degrees, before you print.

Already split your model with another tool? Put the 3D cursor on the knee or elbow and Click Joints Pro cuts a hinge or ball joint right there, with the clearance you set.

- End stop from your rig (30 to 150 degrees), or 90, 115 or 135 when you place a hinge by hand, and a pose slider
- Red where the parts hit when you pose past the stop
- Green fit band for the clearance, wall thickness as a number
- Recognises Rigify, Mixamo, Auto-Rig Pro and other common bone names
- Export to STL or 3MF

Works best on figures about 200 mm tall or more with separate arms and legs. The panel tells you when a joint does not fit, and why.

$19 on Gumroad, 25% off from November 27 to December 1 with code CYBER25: https://dortus.com/click-joints/?van=ba
Also on Superhive: https://superhivemarket.com/products/click-joints-pro
Free version with ball and pin joints: https://extensions.blender.org/add-ons/click-joints/

Questions and bug reports welcome in this thread.
```
Bronnen: alle beweringen staan letterlijk op de Gumroad-pagina van Pro 1.1 (GEZIEN 20 nov, curl) en in de gekeurde video Pro 1 (90/115/135, rood voorbij de stop). Geen print beloofd. Zet hem op of na 27 nov, als de korting loopt; ervoor zonder de kortingsregel. Keuring Daan 20 nov: ja na moet 1 (`platformen/blender/keuring/2026-11-20-blackfriday-teksten-daan.md`). Moet 1 verwerkt: "with code CYBER25" in plaats van "(applied at checkout)"; kan 1, 2 en 3 ook verwerkt (stop uit de rig 30 tot 150, regel Superhive, kortere titel, film bovenaan). Klaar voor het ja van Thijs zodra er een account is.

## Wat dit oplevert (GOK)
Verwachting klein: samen tientallen tot een paar honderd bezoeken in de actieweek, bij 1 tot 3% kopers 0 tot 5 verkopen. Het grootste stuk blijft CG Channel en Superhive zelf (sitebrede sale). Na 1 dec meten per code; een plek zonder bezoek valt af.
