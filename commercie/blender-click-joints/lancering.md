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

## Run 30 (Chris, 9 nov ±11:45 tot 12:30 UTC): het filmpje in de lanceerberichten

Aanleiding: bericht Thijs 9 nov 12:00 (NL): "film Click Joints ja, gebruik hem in de lanceerberichten". Dit deel gaat voor op run 16, run 27 en de bijwerking van run 29 waar het verschilt; de rest blijft geldig.

### Stand (GEZIEN 9 nov 11:46 UTC)
- Nog niet goedgekeurd: API 1.627 extensies zonder `click_joints`, listing 404. Dag 0 is er dus nog niet.
- Het filmpje: `click-joints-filmisch-v2.mp4` op de tak `schermen` (link op lijst-thijs, punt van Bram 9 nov 11:20). Zelf gedownload: sha256 `f6d544166dc8c383b41317aeab16b0ae81ea72cbd85ff02a01cec81d6794c049` (gelijk aan die van Bram en Daan), 19,5 s.
- **Wat er echt in beeld is** (GEZIEN, contactvel van 20 beelden, één per seconde): groene ring flitst aan op een houten arm (haak), de hele houten tekenpop, het gewricht op de elleboog, de onderarm buigt, een close-up in Exploded view (label "Exploded view" in beeld) met het rode vlak, de delen schuiven uit elkaar en klikken terug, elleboog en knie met groene ring, eindkaart "Click Joints for Blender / See how far it bends, before you print. / Free on Blender Extensions / Ball and pin joints · STL and 3MF · Blender 4.2 to 5.2 / Made by Thijs at Dortus". Het label "Exploded view" in beeld is achteraf in de letter Inter over de stempel van Blender gezet (ontwerp.md); het is niet de letter van de add-on.
- **Wat er niet in staat:** geen paneel, geen getallen over buigen of passing (±20°, "+8° past limit"), geen witte boog, geen koppen. Het is een render met licht en gloed, geen schermopname van het viewport. Daarom: de getallen blijven in de tekst van de berichten (die beschrijft de add-on, niet het filmpje), en elk bericht met het filmpje krijgt één eerlijke zin dat het een render is. Zelfde soort zin als bij Rollwright (perkament is eigen CSS).

### Gedaan zonder Thijs
- **dortus.com/click-joints/** (repo dortus, commits 3b63e0e en 7282c25, alleen de eigen map): het filmpje (`film.mp4`, zelfde bestand, plus `film-first.jpg` als eerste beeld) bovenaan het deel "What it does", vóór "Drag the bend". Speelt vanzelf, zonder geluid, in een lus, zoals het filmpje op dortus.com/rollwright/. Onderschrift: "19 seconds, no sound. Rendered in Blender from joints the add-on placed. In your viewport you see the same colours, without the glow." Poster bovenaan blijft (eis Daan). Met `controls`, zodat een bezoeker het kan stilzetten (WCAG 2.2.2, punt van de controleur; ook op dortus.com/rollwright/ erbij gezet). Lokaal getest in Chromium op 1280 en 390 px breed: video laadt en speelt, geen zijwaarts scrollen (GEZIEN). De eindkaart zegt "Free on Blender Extensions", net als de poster die er al staat; na de goedkeuring klopt dat helemaal.
- Waarom nu en niet op dag 0: Thijs zei ja, Daan keurde hem, en de pagina is de plek waar BlenderNation en reacties naar verwijzen. Een bezoeker ziet dan meteen beweging in plaats van alleen plaatjes.

### Wat er verandert per plek

**r/blender, versie B30.** Vorm: een videobericht met het MP4-bestand zelf geüpload naar Reddit (niet de link). Kan er bij een videobericht geen tekst onder, dan gaat de tekst als eerste reactie van Thijs in de eigen draad. De screenshot-stap van run 29 (regels in de zijbalk, karma, AI-regel) blijft vóór alles; geen screenshot of twijfel: niet plaatsen.

**Titel (B30):** `I made Click Joints: cut a printable ball joint into a mesh and see how far it bends before the parts collide (free extension)`

**Tekst (B30):**
> I made Click Joints, a free extension for 3D printing poseable figures from Blender.
>
> Put the 3D cursor where the joint goes and click Place joint. It cuts the mesh into two watertight parts with a ball and socket or a pin, with the clearance you set in mm. For a ball joint it measures how far it bends in 8 directions before the parts collide, and shows that range on the model and in the panel ("Bends ±20°"). Drag the Bend slider past the limit and the spot that collides turns red ("+8° past limit"). A ring on the cut shows the fit in green, yellow or red, and the panel says why.
>
> Exploded view, "Make watertight" on a copy, export to STL or 3MF in mm, one file per part. Tested on Blender 4.2 LTS and 5.2 LTS.
>
> The video is a render in Blender of joints the add-on placed; the glow comes from the render. In the viewport you get the same green ring and red spot, plus the arc and the panel with the numbers.
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

Enige verschil met B27: de alinea over de render. Twee links blijft een punt voor de screenshot-stap (zie run 27).

**BlenderNation, versie C30:** gelijk aan C27, met twee wijzigingen. (1) In de tekst na "Export to STL or 3MF." de zin: `The video is a render in Blender of joints the add-on placed.` (2) "More images: https://dortus.com/click-joints/" wordt `Video and more images: https://dortus.com/click-joints/` (het filmpje staat daar nu). Laat het formulier een bestand of een videolink toe, dan het MP4-bestand of de link https://dortus.com/click-joints/film.mp4 ; een YouTube-link hebben we niet (een kanaal aanmaken is een stap van Thijs en niet nodig voor dit bericht).

**r/3Dprinting, versie A30:** de voorwaarde blijft een foto of filmpje van een **echte print**. Het render-filmpje is daar niet het hoofdbeeld (het is geen print; dat zou de plek misleiden). Mag een bericht meerdere beelden hebben, dan mag het filmpje als tweede, met de render-zin uit B30 in de tekst. Verder gelijk aan A27.

**awesome-blender:** geen wijziging (een regel tekst met een link, geen beeld).

**De listing zelf:** het filmpje als eerste preview op extensions.blender.org staat al op lijst-thijs (punt van Bram). Daar hoort geen render-zin bij: het onderschrift van Bram ("Place a joint, drag the bend, see red past the limit, split into printable parts.") beschrijft wat de add-on doet.

### Antwoorden erbij (alleen in de eigen draad)
- "Is that the real add-on or a render?": "Both: the joints in the video were placed by the add-on in Blender, then rendered with nicer light. In the viewport you get the same green ring and red spot without the glow, and the arc and the panel show the numbers. The red spot is easiest to see with Exploded view on. The screenshots on the listing show the panel."
- "What did you use for the mannequin?": "A simple wooden mannequin made from basic shapes in Blender, just for the video. It doesn't come with the add-on." (Waar: gemaakt in Blender uit eenvoudige vormen, `ontwerp/click-joints/film.md`; niet "I modelled", want dat deden de agents.)

### Dag 0, aangepast
- Stap 5: op lijst-thijs "Plaatsen via de hoofdchat of door Thijs zelf: r/blender, tekst in `commercie/blender-click-joints/lancering.md`, deel run 30, versie B30, met het filmpje (link op de tak `schermen`, sha256 hierboven)". Eerst de screenshot-stap.
- Stap 3 (knop en pil op dortus.com/click-joints/) blijft; het filmpje staat er al.

### Discord
Thijs is geen lid van de Obsidian-Discord (bericht 9 nov 12:00); voor Click Joints stond geen Discord in het plan. Geen wijziging.

### Wat dit deel zou veranderen
Wordt Click Joints afgekeurd, of staat hij over 3 weken (30 nov) nog op Awaiting Review: dan gaan het filmpje en de zin "Free on Blender Extensions" van de pagina af of worden ze aangepast, samen met Daan (de poster bovenaan zegt het ook). Tot dan zegt de pil op dezelfde pagina eerlijk "On its way to Blender Extensions".

### Controleur
Akkoord mits. Moet: (1) "geen getallen" klopte niet helemaal, de eindkaart heeft een regel met versies; (2) de video kon niet stilgezet worden. Beide verwerkt (`controls` op de Click Joints- en de Rollwright-pagina). Kan-punten ook: aria-label met de hele eindkaart, render-zin met de boog, Exploded view in het antwoord, het label in Inter genoemd, regel over afkeuring hierboven.

## Run 37 (Chris, 14 nov ±14:45 tot 15:30 UTC): Click Joints staat 4 dagen live zonder één bericht; draaiboek bijgewerkt en de vraag "starten?" bij Thijs

Dit deel gaat voor op alles hierboven waar het verschilt.

### Stand (GEZIEN 14 nov 14:50 UTC)
- Live sinds 10 nov (besluit hoofdchat 10:45). API extensions.blender.org: `click_joints` versie 0.1.0, zelfde zip (sha256 `6798ce4e...61432a`). Listing: **115 downloads**, 0 reviews, Website dortus.com/click-joints, Report Issues naar de repo click-joints. Bram telde 113 om 13:20 (`platformen/blender/status.md`), dus ±25 per dag zonder enige verspreiding.
- Er is nog **geen enkel lanceerbericht** geplaatst. Reden: het besluit van 10 nov 10:45 zegt "lancering start alleen als Thijs het zegt", en die vraag stond niet duidelijk op zijn lijst. Die staat er nu.
- dortus.com/click-joints/ zei nog "On its way to Blender Extensions", zonder knop naar de listing (dag-0-stap 3 uit run 16 was nooit gedaan). Klaargezet op tak `claude/chris-click-joints-live` in repo dortus (commit 3044979): knop "Get it on Blender Extensions", de pil wordt een link "Version 0.1.0, free on Blender Extensions", en bij Install de zin "Or download it from its page on Blender Extensions". Main niet aangeraakt (afspraak: niets online zonder dat Thijs het zag). Schermafdrukken: `pagina-live-breed.jpg` en `pagina-live-telefoon.jpg` in deze map. Lokaal getest op 1280 en 390 px: geen zijwaarts scrollen, drie links naar de listing (GEZIEN).
- Nog steeds geen echte print. "I haven't printed a joint with it yet" blijft in elk bericht.

### Nieuwe volgorde (mijn besluit) en waarom
1. **BlenderNation eerst (versie C37 hieronder), niet meer pas na r/blender.** Reden: r/blender hangt aan de screenshot-stap en aan het karmafilter (account van Thijs heeft 1 karma, run 29); dat kan dagen duren of nooit lukken. BlenderNation is een formulier zonder account, zonder karma, en een gratis product kost niets (GEZIEN vandaag op https://www.blendernation.com/submit-news/: "Commercial promotions require a 'Commercial Blender User' membership ... EUR 25 per post"; voor een niet-commercieel bericht staat er geen prijs). Er staat geen regel over AI op het formulier (GEZIEN).
2. **r/blender (B30)** alleen na de screenshot van de regels en als er geen AI-, zelfpromotie- of karmaregel is. Geen screenshot of twijfel: niet plaatsen.
3. **awesome-blender** (pull request, via de hoofdchat of Thijs): dag 7 is 17 nov; regel en voorwaarden in `verspreiding.md` plek 3.
4. **r/3Dprinting** blijft wachten op een echte print.

### Regels BlenderNation, letterlijk gelezen (GEZIEN 14 nov 14:55 UTC)
- Kies "Full post" (niet "Message"). Vraag "Is your post about a commercial product or service?": **No**. Dit bericht gaat alleen over de gratis add-on; er staat geen woord over Pro in, en Pro is nergens te koop. "Are you already supporting BlenderNation on Patreon?": **No**. Nooit betalen.
- Titel: geen clickbait, geen hoofdletters.
- Categorie: **Development, Add-ons**.
- De tekst verschijnt als "(your name) writes:", gevolgd door onze tekst. **Daarom begint de tekst niet meer met "Thijs writes:"** (in C16/C27/C30 stond dat erin; dan zou het er dubbel staan).
- Video: geen HTML-embed, alleen de link op een eigen regel.
- Eén hoofdbeeld, jpg/png/gif, 728 x 336 of 1456 x 672 voor retina, liefst "clean images without any text or logo overlays". Onze poster heeft tekst, dus die niet. **Nieuw beeld: `blendernation-1456x672.jpg`** in deze map: één beeld uit het gekeurde filmpje (seconde 15,5: de hele houten tekenpop op één been, met een groene ring op de elleboog en op de knie, het onderwerp in het midden), zonder tekst, verkleind naar 672 hoog en links en rechts aangevuld met de donkere achtergrond tot 1456 x 672, zodat het bij het bijsnijden op de voorpagina in beeld blijft. Eigen beeld, dus rechten in orde. Het is een render; dat staat in de tekst.
- Velden: Your name: `Thijs (Dortus)`, Your email: thijs@dortus.com (het openbare supportadres).

### BlenderNation, versie C37 (letterlijk plakken)
**Post Title:** `Click Joints: free add-on that cuts printable ball joints and shows how far they bend`

**Post Body:**
> I made Click Joints, a free extension that cuts a ball and socket or a pin joint into a mesh for 3D printing, with the clearance you set in millimetres. For a ball joint it measures how far the joint bends in 8 directions before the parts collide, and shows that range on the model; bend it further and the spot that collides turns red. A ring on the cut shows whether the wall is thick enough. Export to STL or 3MF, one file per part. Tested on Blender 4.2 LTS and 5.2 LTS.
>
> I haven't printed a joint with it yet; fit and bend are measured in Blender. The image and the video are renders in Blender of joints the add-on placed.
>
> It's free and open source (GPL-3.0-or-later). The code is written by AI agents that my small studio Dortus runs; I direct the work, and every version is tested automatically in real Blender.
>
> Get it: https://extensions.blender.org/add-ons/click-joints/
>
> Video and more images: https://dortus.com/click-joints/
>
> Made by Thijs at Dortus

Elke bewering nagelegd tegen de live listing van vandaag (8 richtingen, rood voorbij de grens, ring op de snede, STL en 3MF, Blender 4.2 en nieuwer, GPL-3.0-or-later): klopt. "5.2 LTS" staat in de tests van Bram (run 30 en eerder).

**Na het versturen:** BlenderNation stuurt een bevestigingsmail naar thijs@dortus.com; daarop hoeft niets terug. Ik kijk in elke run met curl of het bericht op blendernation.com staat (zoeken op "Click Joints") en meet de downloads 2 dagen erna. Reacties onder een BlenderNation-bericht staan op hun site; antwoorden alleen daar, met de antwoorden uit run 16 en 30.

- BlenderNation schrijft zelf een korte inleiding boven ons bericht ("we'll add an introduction text"); die sturen we niet mee.
- De link naar de repo staat niet in C37: de listing linkt de meldingen al, en zo blijft het bericht bij voornaam en supportadres.

### Op de pagina
De knop "What it does" (naar #features) is vervangen door "How to install" als tweede knop; de eerste knop is nu "Get it on Blender Extensions". Twee knoppen is rustiger dan drie. Daan krijgt de schermafdrukken via deze regel en via lijst-thijs te zien.

### Later, bij Pro
Komt Pro op Superhive en op dortus.com/click-joints/: geen aanpassing van het BlenderNation-bericht vragen. Pro gaat als eigen commercieel bericht (alleen met Thijs, het kost geld) of helemaal niet naar BlenderNation.

### Controleur
Akkoord mits. Moet: het beeld was verkeerd beschreven; vervangen door een beter beeld (hele pop in het midden, kan-punt 1) en de beschrijving klopt nu. Kan-punten 2 tot 5 verwerkt (repo-link uit C37, knop benoemd, inleiding van BlenderNation, regel voor Pro).

### Wat Thijs beslist (één ja dekt drie dingen)
"Click Joints lancering ja" in de hoofdchat betekent: (1) de hoofdchat zet tak `claude/chris-click-joints-live` van repo dortus op main (alleen `click-joints/index.html`, 4 regels); (2) de hoofdchat stuurt C37 in bij BlenderNation, met het beeld hierboven; (3) de screenshot-stap voor r/blender mag gevraagd worden. Nee of later: niets verandert, de downloads lopen vanzelf door.

### Wat dit deel zou veranderen
Komt het BlenderNation-bericht er niet door (na 7 dagen niet op de site), dan geen tweede inzending; dan telt alleen r/blender en awesome-blender. Komt er een vraag van BlenderNation over "commercial" omdat er later een Pro komt: niet beantwoorden zonder Thijs, op zijn lijst.

## Run 44 (Chris, 15 nov ±20:45 tot 21:30 UTC): lancering van Click Joints Pro klaar voor de dag dat Superhive hem goedkeurt

Dit deel gaat voor op alles hierboven waar het verschilt. Aanleiding: bericht van de hoofdchat 15 nov 19:55 (Pro ingediend bij Superhive, status Pending, keuring 3 tot 5 dagen).

### Stand (GEZIEN 15 nov 20:46 tot 20:55 UTC)
- **Superhive vanuit mijn run niet te lezen:** `curl https://superhivemarket.com/products/click-joints-pro` geeft **403**, ook de voorpagina. Dat is de beveiliging van Superhive tegen de cloud, niet een teken dat de pagina er niet is. Ik heb het niet omzeild. Of Pro live is, zie ik dus niet zelf; Superhive bericht Thijs in de Superhive-inbox. Daarom op lijst-thijs: de hoofdchat zet "Pro live" in `berichten/chris.md` zodra die mail er is. Ik probeer de curl elke run opnieuw.
- Gratis Click Joints op extensions.blender.org: **140 downloads** (was 115 op 14 nov 14:50), 0 reviews, versie 0.1.0. Nog steeds geen enkel lanceerbericht; de vraag "Click Joints lancering ja" (run 37) staat nog open op lijst-thijs.
- dortus.com/click-joints/ zegt live nog "On its way to Blender Extensions" (tak `claude/chris-click-joints-live` is nooit op main gezet).

### Pagina dortus.com/click-joints/ met Pro (klaar op een tak, NIET online)
Repo dortus, tak **`claude/chris-click-joints-pro`** (commits d3212e4 en 8172d32). Die tak bevat ook de knop van run 37 (3044979), dus één samenvoeging doet beide. Wat er verandert:
- Bovenaan verandert niets ten opzichte van run 37: de gratis versie en de knoppen **"Get it on Blender Extensions"** en "How to install". Pro staat bewust niet in de knoppen bovenaan en niet in het menu (zie de regels hieronder).
- Nieuw blok `#pro` ná Install: kop "Hinges that click and stop at 115°.", poster 3 van Pro (Daan ja 14 nov) als `pro.jpg`, de zes punten uit de ingediende Superhive-tekst (`platformen/blender/superhive-pagina.md`), de prijzen **$12 personal, $45 studio tot 5 personen, 12 maanden updates**, dat gratis en Pro niet tegelijk aan kunnen, en de knop **"Get Click Joints Pro on Superhive"** naar https://superhivemarket.com/products/click-joints-pro.
- Lokaal getest op 1280 en 390 px: geen zijwaarts scrollen, één link naar Superhive (GEZIEN).
- **Waarom ná Install en niet bovenaan:** de pagina is ook de "Website" op de gratis listing. De regels van extensions.blender.org (GEZIEN vandaag, https://extensions.blender.org/terms-of-service/) verbieden reclame voor betaalde versies in Blender zelf (6.1, 6.3) en in de beschrijving en plaatjes op hun site (6.2). 6.1 noemt ook "links to commercial ... websites" in Blender, en de controleur wees erop dat de website van een extensie in Blender als link te zien kan zijn. Daarom gaat de pagina bovenaan alleen over de gratis add-on, zonder knop of menu naar Pro, en staat Pro alleen als apart blok onderaan. Een eigen website noemen de regels verder niet.
- **De lanceerprijs van $9** staat bewust niet op de pagina: die loopt maar 14 dagen en moet dan weer weg. Op Superhive ziet de koper de echte prijs.
- **Pas samenvoegen als Pro live is** (anders is de knop naar Superhive een dode link) en Thijs ja zei.

### BlenderNation: Pro kost geld
Regels opnieuw letterlijk gelezen (GEZIEN 15 nov 20:50, https://www.blendernation.com/submit-news/): "Commercial promotions require a 'Commercial Blender User' membership on our Patreon ... If you'd rather do a one-off post, we'll charge you EUR 25 per post." Een bericht dat Pro noemt, is commercieel. **Dus: een BlenderNation-bericht met Pro kost € 25, en geld uitgeven beslist Thijs.** Twee berichten kort na elkaar (eerst gratis, dan Pro) stuur ik niet in; dat is dubbel werk voor de redactie en kan als herhaling gezien worden. Daarom één van deze twee:

- **Keuze A, C44 (met Pro, € 25 eenmalig, Thijs betaalt):** tekst hieronder. Vraag "Is your post about a commercial product or service?": **Yes**. Patreon: **No**, dus de eenmalige € 25.
- **Keuze B, C37 (alleen gratis, € 0):** de tekst uit run 37, ongewijzigd, maar zonder de regel "Video and more images: https://dortus.com/click-joints/" zodra de Pro-pagina op main staat. Anders linkt een bericht dat "niet commercieel" heet naar een pagina met een koopknop, en dat is niet eerlijk tegenover BlenderNation. Vraag commercieel: **No**.

**Mijn advies: A, in de 14 dagen van de lanceerprijs.** Reden: Thijs gaf 9 nov 22:56 ruimte voor kleine bedragen als dat tijd wint, en een nieuwsbericht helpt het meest in de eerste weken. Terugverdienen: bij $9 houdt Dortus per verkoop ±$5,81 over (70% min $0,49, zelfde som als `superhive-pagina.md`), dus € 25 is ±5 verkopen (GOK; het bereik van één BlenderNation-bericht heb ik niet kunnen meten). Zegt Thijs nee tegen de € 25: B, zonder kosten.

### BlenderNation, versie C44 (letterlijk plakken, alleen na ja van Thijs op € 25 en als Pro live is)
**Post Title:** `Click Joints: printable ball joints for free, and click hinges that stop at 115° in Pro`

**Post Category:** Development, Add-ons

**Post Image:** `commercie/blender-click-joints/blendernation-pro-1456x672.jpg` (nieuw, 1456 x 672: het gebogen been met het groene scharnier uit het schone Pro-scherm 13, zonder tekst of logo, onderwerp in het midden; eigen beeld)

**Post Body:**
> I made Click Joints, a Blender extension that cuts joints into a mesh for 3D printing, with the clearance you set in millimetres.
>
> The free version cuts a ball and socket or a pin joint. For a ball joint it measures how far it bends in 8 directions before the parts collide, and shows that range on the model; bend it further and the spot that collides turns red. A ring on the cut shows whether the wall is thick enough. Export to STL or 3MF, one file per part.
>
> Click Joints Pro adds a click hinge for knees and elbows. It bends from 0° to 115° and stops there, instead of flopping backwards. A pose slider shows the bend in the viewport, the spots that collide past the stop turn red on both parts, and hinges and ball joints placed too close together are refused with a clear message. Personal license $12 (launch price $9 for the first two weeks), studio license for up to 5 people $45, with 12 months of updates.
>
> I haven't printed a joint with it yet; fit and bend are measured in Blender. The image is a screenshot from Blender of a hinge the add-on placed.
>
> The code is written by AI agents that my small studio Dortus runs; I direct the work, and every version is tested automatically in real Blender. The free version works in Blender 4.2 and newer, Pro is tested on Blender 4.2 to 5.3.
>
> Free, on Blender Extensions: https://extensions.blender.org/add-ons/click-joints/
>
> Pro, on Superhive: https://superhivemarket.com/products/click-joints-pro
>
> Video and more images: https://dortus.com/click-joints/
>
> Made by Thijs at Dortus

- **Lanceerprijs:** staat de $9 op het moment van insturen niet (meer) op Superhive, haal dan "(launch price $9 for the first two weeks)" weg. Niets anders veranderen.
- Velden: Your name `Thijs (Dortus)`, Your email thijs@dortus.com. Video niet insluiten, alleen de link.
- Bewering voor bewering: gratis deel gelijk aan C37 (nagelegd op 14 nov tegen de live listing); Pro-deel uit de ingediende Superhive-tekst; prijzen $12 en $45 en 12 maanden uit `superhive-pagina.md` (concept compleet 15 nov 19:35); "4.2 and newer" voor gratis: `blender_version_min` 4.2.0 (API, GEZIEN vandaag); Pro "4.2 to 5.3": getest in 4.2.23, 5.2.3 en 5.3.0, zoals op Superhive.

### Dag 0 van Pro (wie, wat)
1. **Hoofdchat** zet "Pro live" met tijd in `berichten/chris.md` en bovenaan lijst-thijs "Click Joints Pro LIVE" (dat vroeg de hoofdchat mij, maar ik zie de pagina niet door de 403; daarom ligt de eerste melding bij wie de mail ziet). Daarna stelt de hoofdchat de lanceerprijs $9 in (besluit Bram, `superhive-pagina.md`).
2. **Na ja van Thijs:** de hoofdchat (of ik in de volgende run) zet tak `claude/chris-click-joints-pro` van repo dortus op main. Ik kijk daarna met curl of de pagina en `pro.jpg` 200 geven.
3. **BlenderNation:** A of B, zie boven. Plaatsen doet de hoofdchat.
4. **Meten:** verkopen ziet alleen Thijs in Superhive; ik vraag ze via de lijst op dag 7 en dag 14. Downloads van de gratis versie meet ik zelf.

### Wat dit deel zou veranderen
- Keurt Superhive Pro af of vraagt om wijzigingen: de tak blijft staan, niets naar main.
- Vindt een moderator van extensions.blender.org de Pro-knop op dortus.com toch reclame: Pro-blok naar een eigen pagina dortus.com/click-joints/pro/ en de listing blijft naar de gratis pagina wijzen. Dat is één verplaatsing van het blok.

### Controleur
Akkoord mits. Moet 1: de lezing van regel 6 was te ruim en Pro stond al in de tweede knop en het menu; verwerkt, Pro alleen nog als blok onderaan (8172d32). Moet 2: "Both versions work in Blender 4.2 and newer" was voor Pro niet getoetst; verwerkt naar "Pro is tested on Blender 4.2 to 5.3". Kan 1: onderschrift van pro.jpg is nu "Poster with a screenshot", verwerkt. Kan 2 (stop ook op 90 of 135 graden noemen): niet gedaan, de ingediende Superhive-tekst noemt alleen 115 en de pagina moet gelijk blijven aan de winkel. Kan 3: bij keuze B linkt de gratis listing nog steeds naar dortus.com met het Pro-blok; geen regelbreuk, genoteerd.

## Run 64 (Chris, 16 nov ±17:45 tot 18:35 UTC): lijst voor de dag dat Superhive Pro goedkeurt

Op het bericht van de hoofdchat van 16 nov 18:50 NL (advies Stijn) in `berichten/chris.md`. Dit deel gaat voor op "Dag 0 van Pro" van run 44 waar het verschilt. Per punt: wat, wie, of Thijs nodig is. **De hoofdchat zegt per punt ja of nee.**

### Stand (GEZIEN 16 nov ±18:05 UTC, curl)
- Superhive: nog steeds 403 vanuit mijn run, dus of Pro al goedgekeurd is zie ik niet. Ingediend 15 nov 19:45 NL, keuring 3 tot 5 dagen: goedkeuring waarschijnlijk wo 18 tot vr 20 nov (GOK op de termijn van Superhive).
- Gumroad: Pro live, $12, pagina 200. De titel is nog `Click Joints Pro for Blender` (de nieuwe titel uit `reddit.md` deel 1 staat er nog niet op).
- Gratis Click Joints: 167 downloads op extensions.blender.org (was 166 om 16:57 UTC), versie 0.1.1, zip sha256 `d1643ba56f09540986a3a951d78fbc5046ad5744fd30c324730ae5b9f980fe3d` (API).

### De lijst, in volgorde van de dag

| # | Wat | Wie | Thijs nodig? |
|---|---|---|---|
| 0 | "Pro live" melden in `berichten/chris.md` en bovenaan lijst-thijs; daarna 1.0.2 uploaden (Bram, `platformen/blender/superhive-pagina.md`) | hoofdchat (ziet de mail) | nee, alleen zijn browser |
| 1 | Gratis variant $0 op de Superhive-pagina | hoofdchat in Thijs' Chrome | ja op het idee; dan ±3 min in zijn browser |
| 2 | Titel en tags met de woorden van de koper | hoofdchat in Thijs' Chrome | ja op de tekst |
| 3 | Eén regel over updates, en Superhive en Gumroad gelijk trekken | Bram of Hans beslist, hoofdchat voert uit | ja op de keuze |
| 4 | Cyber Sale-vinkje, en wat het met de lanceerprijs doet | Thijs of hoofdchat in zijn browser | ja, het is een prijs |
| 5 | Lanceerdraad Blender Artists: **mijn advies nee**, BlenderNation in de plaats | hoofdchat | ja op de € 25 (staat al op lijst-thijs) |
| 6 | Filmpje 5 (Pro): mag nu al, met Gumroad in het onderschrift | Thijs plaatst | ja op tekst en beeld |
| 7 | Makersmails: pas na Pro 1.1 | hoofdchat verstuurt vanaf thijs@dortus.com | ja, het is een mail onder zijn naam |
| 8 | dortus.com/click-joints/: Pro-knop naar Gumroad (en Superhive als die live is), plus de twee zinnen van Joris | Chris op de tak, naar main na ja | ja (main van de site) |

### 1. Gratis variant $0 op de Superhive-pagina
- **Wat:** naast Personal $12 en Studio $45 een derde variant `Free (ball joints only)` voor $0 met de gratis zip `click_joints-0.1.1.zip`, precies het bestand van extensions.blender.org (sha256 hierboven; staat ook in `producten/blender-gewrichten/uitgave/`). Eén regel in de beschrijving: `The Free option is the same Click Joints as on Blender Extensions: ball and pin joints with the fit colour. Pro adds the click hinge with an end stop.`
- **Waarom:** de enige winnaar in onze hoek zonder eigen publiek, Split 3D Print (400+), heeft een gratis variant op dezelfde pagina; gratis gebruikers mogen daar een beoordeling geven (DERDEN, Lars verhaal 8 en 9, `platformen/succes/verhalen.md`; hoofdles "gratis variant" in `lessen.md`). Wij hebben 167 gebruikers van de gratis versie die Superhive nu niet ziet. Het kost niets: de gratis versie is al openbaar en GPL.
- **Let op:** gratis en Pro kunnen niet tegelijk aan in Blender (zelfde id); die zin staat al onder Good to know. Of Superhive "Sales" ook gratis downloads telt, weet niemand van ons (Lars: waarschijnlijk niet). Mag een $0-variant niet bij Superhive, dan overslaan; niets anders verandert.
- **Thijs:** ja op het idee. Uitvoeren in zijn browser ±3 min (Edit, Variations).

### 2. Titel en tags
- **Titel op Superhive:** `Click Joints Pro: Ball Joints and Hinges with End Stop for 3D Printed Figures` (Lars, verhaal 9). Ik neem hem over: de zoekvolgorde van Superhive gaat op woorden in titel en tags (GEZIEN door Lars op 11 zoekwoorden), en op "ball joint" en "action figure" staan alleen splitsers (Cleave eerste op "ball joint") en Articulator ($1, 30+), geen echte gewrichtentool met eindstop. Gumroad krijgt de titel uit `reddit.md` deel 1 (die woorden werken daar, gemeten op de Gumroad-zoek-API); het verschil is klein en allebei zeggen ze hetzelfde product.
- **Tags (Superhive, voor zover ze er nog niet staan; welke 9 er nu staan, staat niet in de repo):** `ball joint`, `hinge`, `articulated`, `action figure`, `figurine`, `3d printing`, `cosplay`, `resin`, `fdm`. Zelfde als Lars. Geen namen van anderen.
- **Thijs:** ja op de tekst. Pas na de goedkeuring aanpassen (GOK dat wijzigen de keuring opnieuw start).

### 3. Eén regel over updates, en een tegenspraak tussen de twee winkels
- **De tegenspraak (GEZIEN 16 nov ±18:05 UTC):** Gumroad zegt `All Pro 1.x updates included`. Superhive staat op Support Period: 12 maanden updates, daarna verlengen voor 25% (`superhive-pagina.md`). Thijs besloot om 16:09 dat Pro 1.1 gratis is voor wie Pro al kocht; dat klopt in beide winkels. Maar duurt 1.x langer dan een jaar, dan krijgt de Gumroad-koper meer dan de Superhive-koper. Dat breekt "overal precies hetzelfde" (regels, 8 nov).
- **Mijn advies (keuze A):** op Superhive de Support Period laten staan (besluit 9 nov, advies 7, en verlengen geeft terugkerend geld), en op Gumroad de regel gelijk maken aan Superhive. Regel voor allebei, onder Good to know (zin van Lars, verhaal 7, in de lijn van Cablerator):
  `Includes 12 months of updates, including Pro 1.1. Every version you download is yours to keep. After a year you can extend updates for 25% of the price; it is never required.`
  Op Gumroad kan verlengen niet als knop. Daar wordt de regel: `Includes 12 months of updates, including Pro 1.1. Every version you download is yours to keep.`
  **Belangrijk (moet-punt controleur):** wie sinds 16 nov 15:02 NL op Gumroad kocht, kreeg "All Pro 1.x updates included". Die belofte houden we: die kopers krijgen alle 1.x-versies. Gumroad stuurt een nieuwe zip toch naar alle kopers, dus "12 months" is daar niet af te dwingen. Daarom eerlijk gezegd: keuze A maakt de tekst gelijk, niet de praktijk op Gumroad. Dat maakt keuze B sterker dan het eerst leek.
  `including Pro 1.1` pas in de tekst zetten als 1.1 er echt is; tot dan zonder die woorden.
- **Keuze B:** Support Period op Superhive uit en overal `All Pro 1.x updates included` (zoals Cleave). Eenvoudiger voor de koper, maar dan valt het verlenggeld weg en draaien we het besluit van 9 nov terug; dat is aan Hans.
- **Thijs:** ja op de keuze. Wie beslist: Bram als eigenaar van het product, bij twijfel Hans (prijs is een besluit van de platformmanager, rol).

### 4. Cyber Sale-vinkje, en wat het met de lanceerprijs doet
- **Wat:** in het Superhive-dashboard, Sale Campaigns, Sitewide Sale Settings, het vinkje "Opt-in to all sitewide sales", of Pro apart in de Cyber-campagne (Lars, verhaal 10; staat al op lijst-thijs). Cyber Sale begint rond vr 27 nov (GOK op het vaste patroon).
- **Wat het met de prijs doet:** de lanceerprijs $9 (14 dagen, besluit Bram) loopt dan door tot ±2 tot 4 dec en botst met de Cyber Sale: een eigen campagne staat uit zolang een sitewide sale loopt (GEZIEN door de controleur van run 17, `prijs.md`). In de praktijk merkt de koper niets: $12 min 25% is ook $9. Na de Cyber Sale weer $12. Dortus houdt bij $9 ±$5,61 per verkoop (`prijs.md` regel 8: (prijs min 5,5% min $0,49) keer 70%; de $5,81 uit run 44 was te hoog).
- **Gumroad:** ook $9 in dezelfde dagen, met een kortingscode of tijdelijke prijs, zodat dezelfde koper niet in de ene winkel meer betaalt dan in de andere (GOK dat dit klachten voorkomt; kost niets extra).
- **Let op Pro 1.1:** Thijs noemde daarna $15 tot $19 (besluit 16:09). Komt 1.1 vóór of in de Cyber Sale, dan rekent de korting vanaf de nieuwe prijs. Dan reken ik het opnieuw.
- **Thijs:** ja, het gaat om een prijs. ±2 min in zijn browser.

### 5. Lanceerdraad Blender Artists: mijn advies nee, en wat wel
**Nee, om drie regels van Blender Artists zelf** (GEZIEN 16 nov ±18:20 UTC met curl):
1. **AI-regel:** "This site is for humans to share artwork ideated and made by humans using words ideated and written by humans. AI can help as a tool, but majority AI generation is a no-go." En: "Did an AI do 51% or more of the work? If so, it's not allowed." (staf, https://blenderartists.org/t/1598841, 24 jun 2025). De regel noemt "artwork" en "words", geen code: dat hij ook voor AI-code geldt is onze uitleg. Voor de tekst van een post geldt hij wel letterlijk ("Using AI to write a reply is not" fine), en een tekst van mij is door AI geschreven. Gevolg volgens dezelfde draad: de draad gaat dicht en wordt verborgen. Eerlijk melden dat AI de code schreef (wat wij overal doen) maakt het juist zichtbaar.
2. **Nieuw account kan er niet eens plaatsen:** de categorie Released Add-ons and Extensions is alleen-lezen tot je eerst gewoon meedoet ("You need to spend some time engaging with the community outside of self promotion before you can post there", moderator, https://blenderartists.org/t/1655257, 17 okt 2026). Thijs heeft daar voor zover wij weten geen account met geschiedenis.
3. **Eén zelfpromotiebericht per week, en antwoorden in je eigen draad tellen mee** ("we count replies to your self-promotions too", https://blenderartists.org/faq). Vragen beantwoorden zou de regel dus ook raken.
- Ook gezien: de categorie eist de tag `free` of `commercial` ("Must be tagged free or commercial", https://blenderartists.org/t/294166).
- **Wat wel (de versie die werkt):** BlenderNation, keuze A (C44, met Pro, € 25 eenmalig) of B (C37, gratis, € 0), staat al uitgeschreven in run 44 hierboven en de vraag staat op lijst-thijs. BlenderNation hoort bij dezelfde Bart Veldhuizen, heeft geen AI-regel in de inzendregels die ik las (14 en 15 nov), en daar plaatst de redactie zelf. Mijn advies blijft A in de 14 dagen van de lanceerprijs, maar met Gumroad erbij: zie de aanvulling hieronder.
- **Aanvulling C44:** de regel `Pro, on Superhive: <link>` wordt `Pro: Superhive https://superhivemarket.com/products/click-joints-pro or Gumroad https://duinhouwer8.gumroad.com/l/click-joints-pro`. Verder letterlijk run 44.
- **Thijs:** ja op de € 25 (A) of op B. Wil Thijs Blender Artists toch, dan alleen in zijn eigen woorden, na eerst een tijd gewoon meedoen, en met het risico dat de draad dicht gaat om regel 1. Dat schrijf ik niet voor hem.

### 6. Filmpje 5 (Pro): mag nu al, los van Superhive
- **Wat:** `click-joints-5-pro-hinge-stops.mp4` (14,7 s) uit release `filmpjes-week-1`, Daan ja met één moet (verwerkt run 49, `commercie/filmpjes/week-1.md`). In het beeld staat alleen "Click hinges: Pro. Link in bio", geen winkelnaam, dus het beeld blijft gelijk.
- **Nieuw onderschrift** (alleen de winkel en de AI-zin veranderen; de AI-zin zei dat Thijs zelf test, dat klopt niet, controleur run 63):
  `I made a Blender add-on that places a click hinge for knees and elbows: it bends to 115° and stops there, instead of flopping backwards. Bend it past the stop and the overshoot shows in red. Ball joints are free on Blender Extensions; the click hinge is in Click Joints Pro on Gumroad (link in bio). Measured in Blender, not printed yet. The code is written by AI agents at my studio and tested automatically in real Blender. #blender #3dprinting #b3d #blenderaddon #articulated`
- **Link in bio:** zolang Pro alleen op Gumroad staat, wijst de bio van TikTok en YouTube naar dortus.com/click-joints/ (als punt 8 op main staat) of naar de Gumroad-link. Komt Superhive live, dan "on Superhive and Gumroad".
- **Wanneer:** de eerstvolgende werkdag om ±16:00 NL, voor de reeks (week-1.md: filmpje 5 gaat voor zodra Pro te koop is). Joris' les (Reddit en filmpjes geven de winkel weinig) geldt ook hier: geen sprong verwachten.
- **Thijs:** ja op tekst en beeld; hij plaatst (of de hoofdchat waar de browser het toelaat).

### 7. Makersmails: pas na Pro 1.1
- Zoals in `organisatie/goedkeuren.md` ("na 1.1 | 10 mails aan makers"): een maker die Pro gratis krijgt, moet de versie zien waar Pro om draait (Rig to Figure, besluit 16:09). Eerder sturen verspilt de ene kans per maker.
- **Op de dag zelf:** in `makers.md` `<LINK PRO>` invullen (Superhive als die live is, anders Gumroad) en `<CODE>` (een 100%-kortingscode op Gumroad of een gratis code via Superhive; maakt de hoofdchat in Thijs' browser). De zinnen over Pro opnieuw naast 1.1 leggen; dat doe ik in de run waarin 1.1 klaar is.
- **Thijs:** ja op de mails (onder zijn naam, vanaf thijs@dortus.com). Wie: hoofdchat verstuurt.

### 8. dortus.com/click-joints/
- Tak `claude/chris-click-joints-pro` in repo dortus wijst de Pro-knop nog naar Superhive. In mijn volgende run zet ik daar: knop naar Gumroad (nu), Superhive erbij zodra die live is, en de twee zinnen van Joris (16 nov 17:45 UTC): `Free in Blender: Edit > Preferences > Get Extensions, search "joints".` en `If it helped, an honest rating on extensions.blender.org helps other makers find it.` Nooit om 5 sterren vragen, niets geven voor een review.
- **Thijs:** ja voor main (regel website: alleen na zijn ja). De hoofdchat noemde dit ook in het besluit van 15:02 ("link op dortus.com (na ja)").

### Controleur
Akkoord mits (16 nov run 64, los van mij, bronnen en webpagina's zelf nagelezen). Moet 1: $5,81 bij $9 was verouderd, nu $5,61; verwerkt. Moet 2: Gumroad-kopers houden hun 1.x-belofte; verwerkt in punt 3. Kan verwerkt: Cleave op "ball joint", AI-regel noemt geen code, "including Pro 1.1" pas na 1.1, C44-zin. Kan verwerkt in `lanceerposts.md`: prijs in de Pro-reactie nakijken op de dag zelf.

### Wat dit deel zou veranderen
- Superhive staat geen $0-variant toe: punt 1 vervalt, de rest blijft.
- Pro 1.1 komt vóór de goedkeuring: punt 2 en 6 krijgen de woorden van 1.1 (rig), punt 4 de nieuwe prijs.
- Blender Artists verandert de AI-regel, of Thijs heeft daar al een account met geschiedenis: punt 5 opnieuw bekijken.
