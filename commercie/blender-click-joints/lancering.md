# Click Joints (Blender): lancering

Door Chris, run 4, 8 nov 2026 ±17:00 tot 17:30 UTC. Concept: Click Joints is nog niet live en heeft nog geen akkoord van Daan. Niets hiervan wordt geplaatst voordat de voorwaarden hieronder kloppen en Hans over de plekken heeft beslist (advies 23). Plaatsen gaat via de hoofdchat (een geplande run kan niet bij Chrome).

## Stand (GEZIEN 8 nov ±17:10 UTC)
- Product op main e8602097, ronde n. Beweegproef, rood voorbij de grens en de weigeringen zijn gebouwd en groen in Blender 4.2.23 en 5.2.3 (runs van Bram, zie `platformen/blender/status.md`).
- `producten/blender-gewrichten/ontwerp.md`: "Akkoord: nee" van Daan, 16:27 (beoordeling 3: gradenboog in plaats van waaier, smalle naadband).
- Niet live: geen extensie "click joints" op extensions.blender.org (API, 1.622 extensies), geen pagina op Superhive. De accounts op beide plekken zijn een stap voor Thijs (staat op lijst-thijs, niet dringend).
- Het betaalde deel (scharnier met eindstop, printerprofielen, alle ledematen) is nog niet gebouwd. Deze berichten gaan daarom alleen over de gratis versie.

## Voorwaarden voor het eerste bericht
1. Daan zet `Akkoord: ja` en de lijstplaatjes staan (de gradenboog is ons beeld; zonder dat plaatje geen bericht).
2. De gratis versie staat live op extensions.blender.org (link werkt, met curl gezien).
3. **Een echte print.** Bram noemt in het ontwerp een handmatige printproef. Wie print, is nog open: of Thijs een printer heeft, staat nergens in de repo; Bram schreef op de lijst van Thijs (8 nov 01:35) dat hij later misschien vraagt of Thijs of iemand die hij kent één testgewricht kan printen; de vraag staat ook in advies 23. Op een printforum is de eerste vraag "did you print it?". Zonder foto van een geprint gewricht dat buigt, plaatsen we niet op r/3Dprinting. Op r/blender mag het wel zonder, maar dan staat er eerlijk dat het nog niet geprint is.
4. Hans heeft over de plekken beslist in `berichten/chris.md` (de toestemming van Thijs noemt alleen de drie Obsidian-plekken). **Bijwerking 8 nov run 13:** Hans nam advies 23 over met "de plekken voor de lancering kiest Chris, plaatsen gaat via Thijs of de hoofdchat". r/3Dprinting, r/blender en BlenderNation zijn daarmee gekozen; plaatsen alleen via de hoofdchat of Thijs. Nieuwe plekken staan in `verspreiding.md`.
5. De hoofdchat leest vlak voor het plaatsen de regels van de plek in de browser (Reddit-regels zijn met curl niet te lezen, zie onder).

## Plekken en hun regels

| Plek | Regels gelezen | Bewijs voor bereik | Oordeel |
|---|---|---|---|
| extensions.blender.org (de listing zelf) | ToS 6.1 tot 6.3, zie `platformen/blender/kandidaten-2026-11-07.md` sectie 18: geen verwijzing naar de betaalde versie | ±1.000 tot 1.500 downloads per nieuwe add-on (GEZIEN 6 nov, Vera) | ja, dit is de lancering zelf |
| r/3Dprinting | niet te lezen met curl (403, inlogmuur), niet omzeild; ook niet via spiegelsites | "We made 5 joint cutters for 3D printing", 314 punten (GEZIEN 8 nov, https://www.reddit.com/r/3Dprinting/comments/1t6lo3g/) | ja, eerste bericht na de listing, alleen met echte print |
| r/blender | idem, 403 | groot publiek, geen eigen meting voor add-on-berichten (GOK) | ja, minstens één dag na r/3Dprinting |
| BlenderNation (nieuwssite) | GEZIEN, https://www.blendernation.com/submit-news/: een bericht over iets commercieels kost € 25 of een Patreon-lidmaatschap; een gratis product niet | GOK | alleen de gratis versie, zonder Superhive, na besluit Hans; nooit betalen |
| BlenderArtists, Released Add-ons and Extensions | GEZIEN: hoogstens één bericht over eigen werk per week, updates in dezelfde draad, tag `free` of `commercial` verplicht (https://blenderartists.org/t/1276424, https://blenderartists.org/t/1416473); een nieuw account kan daar niet plaatsen tot het "some time engaging with the community" heeft meegedaan (moderator, 17 okt 2026, https://blenderartists.org/t/1655257) | zwak: "Bed Fit Splitter", een print-add-on, 88 keer bekeken en 0 likes in 7 weken (GEZIEN, https://blenderartists.org/t/1653313) | nee bij de lancering: eerst meedoen op het forum, en dat zou posten onder de naam van Thijs zijn buiten een lanceerbericht |
| Superhive (de listing zelf) | pas als het betaalde deel gebouwd is | 31% van nieuwe betaalde add-ons 10+ verkopen (Vera) | later |

## Eerlijk over wie het maakte
Zelfde vorm als bij Rollwright: "I made Click Joints", en één zin dat AI-agents van Dortus de code schrijven, Thijs stuurt het werk, en dat elke versie automatisch in de echte Blender 4.2 en 5.2 getest wordt. Slotregel "Made by Thijs at Dortus". Geen persoonlijke printverhalen die niet van Thijs zijn ("I print a lot of figures" schrijven we niet).

## Concept A: r/3Dprinting (na echte print; nagekeken door controleur, akkoord mits, moet-punten verwerkt)
**Titel:** `I made a free Blender add-on that cuts a ball joint into your figure and tells you how far it bends before you print`

**Tekst:**
> I made Click Joints, a free Blender add-on for turning a sculpt into a poseable print.
>
> You set the 3D cursor where the joint goes and click Place joint. It cuts the mesh into two watertight parts with a ball and socket (or a pin and hole), with the clearance you set in mm (0.1 to 0.3 mm is typical).
>
> Right after the cut it shows two things:
> - How far the ball joint bends before the parts collide, measured in 8 directions, for example "Bends ±25°". Tilt the part past that and the spot where it hits turns red.
> - The fit: a ring on the cut is green (good), yellow (tight) or red (too thin), and the panel gives the wall thickness in mm.
>
> If a spot is too thin for a ball joint, it says so instead of giving you a broken part. Export is STL or 3MF, one file per part, in mm.
>
> [foto: het geprinte gewricht, gebogen] [plaatje: de gradenboog in Blender]
>
> Free on the Blender Extensions platform: <link>. Tested on Blender 4.2 LTS and 5.2 LTS.
>
> Honest note: the code is written by AI agents that my small studio, Dortus, runs. I direct the work; every version is tested automatically in real Blender 4.2 and 5.2.
>
> A question for people who print jointed figures: which clearance works for ball joints on your printer?
>
> Made by Thijs at Dortus

Waarom zo: de titel zegt wat het doet en wat je eraan hebt, zonder "the only" (we hebben de concurrenten niet gekocht). Het buigen staat bovenaan, want dat laat de gradenboog zien. De vraag aan het eind geeft reacties waar wij van leren (welke speling), en die kunnen we met feiten beantwoorden.

## Concept B: r/blender (minstens één dag later)
**Titel:** `I made Click Joints: cut a printable ball joint into a mesh and see how far it bends (free extension)`

**Tekst:**
> I made Click Joints, a free extension for 3D printing poseable figures from Blender.
>
> Set the 3D cursor where the joint goes and click Place joint. It cuts the mesh into two watertight parts with a ball and socket or a pin, with clearance in mm. For a ball joint it measures the bend range in 8 directions and shows it in the viewport ("Bends ±25°"); past the limit the colliding spot turns red. A ring on the cut shows the fit in green, yellow or red, with the reason in the panel.
>
> Tested on Blender 4.2 LTS and 5.2 LTS. Exploded view, "Make watertight" on a copy, export to STL or 3MF in mm.
>
> <link>
>
> Honest note: the code is written by AI agents that my small studio, Dortus, runs. I direct the work; every version is tested automatically in real Blender 4.2 and 5.2.
>
> Made by Thijs at Dortus

Zonder echte print: zin erbij "I haven't printed a joint with it yet; the fit and bend are measured in Blender." (run 16: "a joint" in plaats van "a full figure", want er is nog niets geprint) Dan geen beweringen over hoe het geprint aanvoelt.

## Concept C: BlenderNation (alleen na besluit Hans, alleen de gratis versie)
Vraag "Is your post about a commercial product?": **No**, alleen als de tekst niets over Superhive zegt. Zodra het betaalde deel bestaat en genoemd wordt, is het commercieel en kost het geld: dan niet.
> **Click Joints: printable ball joints that show how far they bend (free)**
>
> Thijs writes: I made Click Joints, a free extension that cuts a ball and socket or a pin joint into a mesh for 3D printing. For a ball joint it measures how far the joint bends in 8 directions before the parts collide, and shows the angle in the viewport. A ring on the cut shows whether the wall is thick enough. Export to STL or 3MF in millimetres. Tested on Blender 4.2 LTS and 5.2 LTS.
>
> <link naar extensions.blender.org> <link naar korte video>

## Volgorde
1. Listing op extensions.blender.org live (Thijs doet de eerste aanmelding, Bram stuurt in).
2. r/3Dprinting, alleen met echte print.
3. Minstens één dag later, en alleen als 2 niet verwijderd is en geen moderator waarschuwde: r/blender.
   Kan niemand printen: dan r/blender als eerste bericht na de listing (met de zin "I haven't printed a joint with it yet", aangepast in run 16), en r/3Dprinting pas na een echte print.
4. BlenderNation na besluit Hans.
5. BlenderArtists niet bij de lancering.
Per plek één bericht. Reageren alleen in de eigen draad, als concept in `berichten-geplaatst.md` (nog niet aangemaakt, komt bij het eerste bericht).

## Wat dit plan zou veranderen
- De regels van r/3Dprinting of r/blender verbieden eigen add-ons of eisen iets wat we niet kunnen (bijvoorbeeld minimaal karma): die plek valt af, zet het op de lijst van Thijs.
- De printproef mislukt (het gewricht klikt niet of breekt): geen r/3Dprinting, eerst de vorm repareren (Bram).
- Een gratis gewrichten-extensie verschijnt eerder op extensions.blender.org: de titel en de eerste zin opnieuw toetsen.

---

## Run 16 (Chris, 8 nov ±21:45 tot 22:30 UTC): klaar voor het moment van goedkeuring

Opdracht Thijs (8 nov 22:18, zijn tijd): Click Joints is ingediend, zet het verspreidingsplan klaar voor de goedkeuring; Bram en Daan maken een filmpje van 15 tot 20 seconden. Dit deel gaat voor op alles hierboven waar het verschilt. De concepten A, B en C hierboven blijven staan als geschiedenis; geldig zijn de versies run 16 hieronder.

### Stand (GEZIEN 8 nov ±21:45 UTC)
- Ingediend, status "Awaiting Review" (lijst-thijs, 8 nov 22:18). De API van extensions.blender.org heeft 1.622 extensies en nog geen `click_joints`; https://extensions.blender.org/add-ons/click-joints/ geeft 404.
- Daan: `Akkoord: ja` voor main 920dc77f en de productpagina. https://dortus.com/click-joints/ geeft 200.
- Filmpje: ontwerp van Daan klaar (`ontwerp/click-joints/film.md`, 18,5 s, houten tekenpop, ±20° en "+8° past limit"), opname bij Bram, nog niet gekeurd. `storyboard.mp4` is een proef en **niet** voor buiten.
- Nog steeds geen echte print. Daarom is r/blender het eerste Reddit-bericht, met de zin dat het nog niet geprint is (voorwaarde 3 hierboven).
- **Nieuw gevonden:** een listing op extensions.blender.org kan een MP4 als preview tonen. In een steekproef van 29 listings hadden er 17 een filmpje (GEZIEN, `data-galleria-content-type="video/mp4"` in de HTML, bijvoorbeeld mat-baker, moldsizer, sculpt-subtools). Zie advies 27.
- **Downloads meten:** de API heeft geen veld voor downloads (GEZIEN, velden id tot tags). Het getal staat in de HTML van de listing, onder `<dt> Downloads </dt>` (GEZIEN bij mat-baker: 357). Het plan noemde de API; dat klopt dus niet, de meting gaat via de pagina.

### Het seintje: is hij goedgekeurd?
Wie het eerst kijkt (Chris in elke run, of de hoofdchat als Thijs een mail van de moderatoren krijgt):
```
curl -s https://extensions.blender.org/api/v1/extensions/ | python3 -c "import json,sys; d=json.load(sys.stdin)['data']; print([e['version'] for e in d if e['id']=='click_joints'])"
curl -s -o /dev/null -w "%{http_code}\n" https://extensions.blender.org/add-ons/click-joints/
```
Goedgekeurd = de eerste regel geeft een niet-lege lijst (nu `['0.1.0']`, of hoger als er tijdens de keuring een nieuwe versie kwam) en de tweede `200`. Daarmee is dat dag 0. De link wordt dan https://extensions.blender.org/add-ons/click-joints/ (zelfde vorm als andere listings: id met liggend streepje wordt een streepje in de link, GEZIEN bij mat_baker en nk_auto_ik).
Wordt hij afgekeurd of komt er een vraag: niets uit dit plan gaat door; Bram verwerkt de reden.

### Dag 0 (zonder Thijs, Chris in de eerstvolgende run)
1. Seintje met curl gezien (zie boven), en de listing zelf gelezen: titel, tagline, plaatjes, geen woord over betaald.
2. **Nulmeting downloads:** `curl -sL https://extensions.blender.org/add-ons/click-joints/ | tr -s ' \n' ' ' | grep -o 'Downloads </dt> <dd>[0-9,]*'` in `commercie/blender-click-joints/cijfers.md` (nieuw bestand), met tijd. Daarna elke run één keer.
3. **dortus.com/click-joints/ bijwerken** (repo dortus, map `click-joints/`, alleen deze regels; kan-punt 1 van Daan):
   - regel 73, oud: `Version 0.1.0, free. On its way to Blender Extensions.`
     nieuw: de hele pil wordt een link, zoals op de andere pagina's van de site (een `<a>` midden in de `inline-flex`-pil geeft extra ruimte): `<a class="status enter enter-3" href="https://extensions.blender.org/add-ons/click-joints/">Version 0.1.0, free on Blender Extensions</a>` in plaats van de `<span>`.
   - in `<div class="btns ...">` (regel 69 tot 71, niet de Install-knop in de kopbalk) een eerste knop erbij: `<a class="btn btn-light" href="https://extensions.blender.org/add-ons/click-joints/">Get it on Blender Extensions <span class="arrow" aria-hidden="true">&rarr;</span></a>`, en "How to install" wordt `btn-line` (dan twee lijnknoppen naast elkaar; Daan laat ik het zien).
   - bij Install een zin erachter: `Or download it from <a href="https://extensions.blender.org/add-ons/click-joints/">its page on Blender Extensions</a>.`
   Niet eerder: tot de goedkeuring zou die link 404 geven.
4. `commercie/blender-click-joints/berichten-geplaatst.md` aanmaken (leeg, met kop), zoals bij Rollwright.
5. Op `organisatie/lijst-thijs.md` één regel: "Plaatsen via de hoofdchat: r/blender, op zijn vroegst dag 1, tekst in `commercie/blender-click-joints/lancering.md`, deel run 16, versie B16; op zijn vroegst dag 1 of twee dagen na het r/ObsidianMD-bericht van Rollwright, wat het laatste is."

### Dag 1: r/blender (via de hoofdchat, onder de naam van Thijs)
**Voorwaarden:** dag 1, of twee dagen na het geplaatste Rollwright-bericht op r/ObsidianMD, wat het laatste is (dat bericht mag op zijn vroegst 9 nov 13:45 UTC, dus r/blender op zijn vroegst 11 nov ±13:45 UTC; staat r/ObsidianMD nog open, dan gaat dat voor, want Rollwright is al live, en wacht r/blender tot twee dagen daarna), zodat het Reddit-account van Thijs niet twee eigen projecten kort na elkaar plaatst (GOK: Reddit en moderatoren letten op accounts die vooral eigen werk plaatsen); het Rollwright-bericht is niet verwijderd en er kwam geen waarschuwing (regel 7). Is het filmpje door Daan gekeurd, dan gaat het mee; zo niet, dan de poster.
**Regels eerst:** de hoofdchat leest in de browser de regels en de zijbalk van r/blender (met curl 403, GEZIEN, niet omzeild), en volgt ze precies: flair, regels over zelfpromotie, of een link in de tekst mag. Mag eigen werk niet, of twijfel: niet plaatsen, op de lijst van Thijs met de vraag.
**Vorm:** een bericht met het filmpje (MP4 geüpload naar Reddit, beter dan een link, GOK) en de tekst eronder. Kan er bij een video geen tekst, dan de tekst als eerste reactie van Thijs in de eigen draad. Zonder filmpje: de poster (https://dortus.com/click-joints/poster.jpg) als afbeelding.

**Titel (B16):** `I made Click Joints: cut a printable ball joint into a mesh and see how far it bends before the parts collide (free extension)`

**Tekst (B16):**
> I made Click Joints, a free extension for 3D printing poseable figures from Blender.
>
> Put the 3D cursor where the joint goes and click Place joint. It cuts the mesh into two watertight parts with a ball and socket or a pin, with the clearance you set in mm. For a ball joint it measures how far it bends in 8 directions before the parts collide, and shows that range on the model and in the panel ("Bends ±20°"). Drag the Bend slider past the limit and the spot that collides turns red ("+8° past limit"). A ring on the cut shows the fit in green, yellow or red, and the panel says why.
>
> Exploded view, "Make watertight" on a copy, export to STL or 3MF in mm, one file per part. Tested on Blender 4.2 LTS and 5.2 LTS.
>
> I haven't printed a joint with it yet; the fit and the bend range are measured in Blender.
>
> https://extensions.blender.org/add-ons/click-joints/
>
> Honest note: the code is written by AI agents that my small studio, Dortus, runs. I direct the work; every version is tested automatically in real Blender 4.2 and 5.2.
>
> Made by Thijs at Dortus

Wat er veranderde tegen concept B: ±25° werd ±20° (gelijk aan poster, winkelplaatjes, productpagina en filmpje, regel "Elk product"), de Bend-schuif en "+8° past limit" staan erin omdat het filmpje dat laat zien, de zin over niet geprint is vast, en de link is de echte vorm.

### Later, met een echte print: r/3Dprinting (versie A16)
Alleen met een foto of filmpje van een geprint gewricht dat buigt. Dan minstens een dag voor of na r/blender, nooit op dezelfde dag.
**Titel (A16):** `I made a free Blender add-on that cuts a ball joint into your figure and tells you how far it bends before you print`
**Tekst (A16):** zoals concept A hierboven, met twee wijzigingen: "for example "Bends ±25°"" wordt "for example "Bends ±20°"", en de link wordt https://extensions.blender.org/add-ons/click-joints/ . De vraag aan het eind over de speling blijft.

### Dag 3 tot 5: BlenderNation (versie C16, Thijs of de hoofdchat, formulier)
Alleen als r/blender gelukt is en niet verwijderd werd. Formulier https://www.blendernation.com/submit-news/ , vraag "Is your post about a commercial product?": **No** (geen woord over betaald, nooit betalen).
> **Click Joints: printable ball joints that show how far they bend (free)**
>
> Thijs writes: I made Click Joints, a free extension that cuts a ball and socket or a pin joint into a mesh for 3D printing, with the clearance you set in millimetres. For a ball joint it measures how far the joint bends in 8 directions before the parts collide, and shows that range on the model; bend it further and the spot that collides turns red. A ring on the cut shows whether the wall is thick enough. Export to STL or 3MF. Tested on Blender 4.2 LTS and 5.2 LTS. I haven't printed a joint with it yet; fit and bend are measured in Blender. The code is written by AI agents that my small studio Dortus runs; I direct the work.
>
> Made by Thijs at Dortus
>
> https://extensions.blender.org/add-ons/click-joints/
> More images: https://dortus.com/click-joints/

Is het filmpje gekeurd, dan komt het op dortus.com/click-joints/ (Chris, eigen productmap) en gaat die link mee. De zin over niet geprint valt weg zodra er een echte print is.

### Dag 7 of later: awesome-blender (pull request via de hoofdchat of Thijs)
Regel en voorwaarden staan in `verspreiding.md` plek 3 (op zijn vroegst dag 7, na eerste downloads en reacties). Link in de regel is de echte vorm hierboven.

### Meten
Dag 0 nulmeting, dan elke run de downloads van de listing. Twee dagen na elk bericht kijk ik of er een sprong is; een soort plek die niets doet valt af. Dag 14: meting en voorstel aan Hans over de rest (persmail, Printables, makers), zie advies 26.

### Antwoorden klaar (alleen in de eigen draad, kort, geen discussie)
- "Did you print it?": "Not yet, that's why I wrote it. The clearance and wall thickness are measured in Blender, so a test print of one joint is the honest next step. If you try it, I'd like to hear which clearance worked on your printer."
- "How is it different from other joint cutters?": "It also measures how far a ball joint bends before the parts collide, shows that range on the model, and turns the spot red when you bend past it, so you can check before printing." Geen namen van anderen.
- AI-argwaan: "Fair point. It's tested automatically in real Blender 4.2 and 5.2 on every change, and it's free, so you can judge the result yourself." Daarna niet meer reageren.
- "Does it do hinges / knees that bend one way?": "Not in this version: it does ball joints and pins. A pin turns around one axis, but nothing stops it from bending backwards." (Geen belofte over later; het scharnier is nog niet af.)
- Klachten over geld, privacy of juridische vragen: niet beantwoorden, bovenaan lijst-thijs.

---

## Run 27 (Chris, 9 nov ±08:45 tot 09:30 UTC): de eigen repo voor meldingen in het draaiboek

Aanleiding: bericht Thijs 9 nov ±09:20 NL. Click Joints heeft een eigen openbare repo, https://github.com/thijsduinhouwer2002-coder/click-joints (README, GPL-3.0, broncode gratis build 0.1.0, issues aan), en Report Issues op extensions.blender.org wijst daarheen. Dit deel gaat voor op run 16 waar het verschilt; de rest van run 16 blijft geldig.

### Stand (GEZIEN 9 nov 08:50 UTC)
- Wachtrij: nog **Awaiting Review**, enige activiteit de inzending (8 nov 22:09 en 22:18, tijd van de site), geen opmerking van een moderator. API 1.622 extensies zonder `click_joints`, listing 404.
- Op de wachtrijpagina staat bij Report Issues nu `github.com/thijsduinhouwer2002-coder/click-joints/issues`. Daarmee is de opmerking die bij 4 van de 27 add-ons met een ronde wijzigingen kwam (wachtrij.md, punt 1) vooraf opgelost; advies 33 is uitgevoerd.
- README en LICENSE in de nieuwe repo geven 200 (raw.githubusercontent.com). De README noemt installeren, "Report a problem" met de issues-link en wat je moet meesturen, en thijs@dortus.com.
- **Wat ik niet kan zien:** de issues zelf. Mijn geplande run mag alleen dortus-hq, dortus en rollwright lezen; de API en github.com geven voor click-joints 403 ("not enabled for this session"). Niet omzeild. Op lijst-thijs staat hoe dat opgelost wordt; tot dan kijkt de hoofdchat bij een seintje van Thijs.
- Ook niet te zien: of er in die repo een release met het zip staat. De README zegt "download the zip from the releases"; staat er geen release, dan klopt die zin niet (advies 36).

### Gedaan zonder Thijs
- **dortus.com/click-joints/** (repo dortus, commit 4aba37e, alleen de eigen map): bij License staat nu "GPL 3.0 or later, source on GitHub" met de link naar de repo, en bij Support "Found a bug? Open an issue on GitHub, so others can see it too. A question or an idea? Write to thijs@dortus.com." Niets anders veranderd. Live gezien: https://dortus.com/click-joints/ geeft 200 en bevat de issues-link (curl, 9 nov, GEZIEN door de controleur). Daan kijkt hem na (advies 36).

### Wat er verandert in de berichten
Open broncode is op r/blender en bij awesome-blender een pluspunt (GOK: GPL en een openbare repo maken een gratis add-on van een onbekende maker betrouwbaarder), en geeft mensen een plek om fouten te melden die iedereen ziet. Daarom één regel erbij in elk bericht, verder niets.

**r/blender, versie B27.** Dit is nu de geldige tekst om letterlijk te plakken (B16 plus één regel na de link). Twee links: lees in de regels van r/blender of dat mag; zo niet, dan gaat de regel "Free and open source" als eerste reactie van Thijs in de eigen draad.

**Titel (B27):** `I made Click Joints: cut a printable ball joint into a mesh and see how far it bends before the parts collide (free extension)`

**Tekst (B27):**
> I made Click Joints, a free extension for 3D printing poseable figures from Blender.
>
> Put the 3D cursor where the joint goes and click Place joint. It cuts the mesh into two watertight parts with a ball and socket or a pin, with the clearance you set in mm. For a ball joint it measures how far it bends in 8 directions before the parts collide, and shows that range on the model and in the panel ("Bends ±20°"). Drag the Bend slider past the limit and the spot that collides turns red ("+8° past limit"). A ring on the cut shows the fit in green, yellow or red, and the panel says why.
>
> Exploded view, "Make watertight" on a copy, export to STL or 3MF in mm, one file per part. Tested on Blender 4.2 LTS and 5.2 LTS.
>
> I haven't printed a joint with it yet; the fit and the bend range are measured in Blender.
>
> https://extensions.blender.org/add-ons/click-joints/
>
> Free and open source (GPL-3.0-or-later). Code and bug reports: https://github.com/thijsduinhouwer2002-coder/click-joints
>
> Honest note: the code is written by AI agents that my small studio, Dortus, runs. I direct the work; every version is tested automatically in real Blender 4.2 and 5.2.
>
> Made by Thijs at Dortus

**BlenderNation, versie C27:** gelijk aan C16, met onder "More images" één regel:
> Source code and issues: https://github.com/thijsduinhouwer2002-coder/click-joints

**r/3Dprinting, versie A27:** gelijk aan A16, met de regel "Free and open source (GPL-3.0-or-later). Code and bug reports: ..." uit B27 als eigen alinea direct na de alinea met de link.

**awesome-blender:** de regel in de lijst linkt naar de listing op extensions.blender.org (dat is de voorwaarde in CONTRIBUTING.md: een goedgekeurde listing). Vraagt de lijst bij de regel om een repo, dan de repo-link erbij. Verder ongewijzigd: op zijn vroegst dag 7.

### Dag 0 erbij
5. (vervangt stap 5 van run 16) Op lijst-thijs: "Plaatsen via de hoofdchat of door Thijs zelf: r/blender, tekst in `commercie/blender-click-joints/lancering.md`, deel run 27, versie B27", met dezelfde voorwaarde over het r/ObsidianMD-bericht.
6. Bij de nulmeting ook de repo: sterren en open issues, zodra mijn run de repo mag lezen (anders de hoofdchat). In `cijfers.md` naast de downloads.

### Antwoorden erbij (alleen in de eigen draad)
- "Found a bug" of een foutmelding in de draad: "Thanks! Could you open an issue at https://github.com/thijsduinhouwer2002-coder/click-joints/issues with your Blender version and the message the panel showed? A small .blend helps a lot." Daarna niet in de draad debuggen.
- "Is it open source?": "Yes, GPL-3.0-or-later, the code is on GitHub: https://github.com/thijsduinhouwer2002-coder/click-joints"

### Nog steeds waar
Geen woord over een betaalde versie in welk bericht dan ook; ±20° overal; "I haven't printed a joint with it yet" blijft tot er een echte print is; r/blender op zijn vroegst twee dagen na het geplaatste r/ObsidianMD-bericht van Rollwright (dat plaatst Thijs nu zelf, lijst-thijs 9 nov ±09:25).

## Bijwerking 9 nov 2026 (run 29): r/ObsidianMD vervalt, dus andere voorwaarden voor r/blender en r/3Dprinting

Door Chris. Thijs liet weten (hoofdchat 9 nov 11:45, `berichten/chris.md`) dat het Rollwright-bericht op r/ObsidianMD **niet** geplaatst wordt: regel 4 daar bant wie als eerste post een AI-gebouwd project promoot. Ook schreef hij dat reddit.com voor Claude in Chrome geblokkeerd is. Twee gevolgen voor dit draaiboek; dit deel gaat voor op run 16 en run 27 waar ze botsen:
1. **De voorwaarde "twee dagen na het r/ObsidianMD-bericht van Rollwright" vervalt** (run 16 B16 en stap 5, run 27 stap 5 en de slotregel). r/blender kan op zijn vroegst dag 1 na de goedkeuring, en alleen als er op geen enkele plek een waarschuwing of verwijdering kwam (regel 7 van Thijs).
2. **"De hoofdchat leest in de browser de regels en de zijbalk van r/blender" kan niet meer.** Nieuwe stap vóór r/blender en vóór r/3Dprinting: de hoofdchat vraagt Thijs om een screenshot van de uitgeklapte regels in de zijbalk (en de wiki over zelfpromotie, als die er is). Niet plaatsen als er staat: geen AI-gemaakte inhoud of software, zelfpromotie alleen voor actieve leden, een verhouding meedoen en promoten die Thijs niet haalt, of een minimum aan karma of accountleeftijd. Het account van Thijs (u/Immediate_Offer_630, 2 jaar, 1 karma) valt bij zo'n filter af, en een eerste post die reclame is, wordt op veel subreddits gezien zoals op r/ObsidianMD (GOK). Twijfel: niet plaatsen, vraag op lijst-thijs (regel 3).
3. BlenderNation (C27) is geen subreddit en blijft zoals in run 27; ook daar leest wie inzendt eerst de regels.
