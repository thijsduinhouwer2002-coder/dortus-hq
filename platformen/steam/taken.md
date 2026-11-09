# Steam: taken (belangrijkste bovenaan)

## Taakverdeling Steam-team (Olaf, 9 nov 18:30 UTC; besluit Thijs 9 nov 19:00: team van vier, Olaf leidt en beslist over de bouw)
Iedereen draait elk uur. Werk alleen in je eigen bestanden hieronder; iets nodig van een ander: zet een regel onder "Vragen tussen ons" onderaan dit blok (met je naam en tijd) en de ander zet "(antwoord ...)" erachter. De opdracht van Thijs (`berichten/olaf.md` 18:50) is voor iedereen de toets: **tussendoor leuk (30 s tot een paar minuten), grappig om te onderhouden, niet tijdrovend en nooit straffen als je weg bent, later skins en DLC alleen uiterlijk en inhoud, nooit betalen om sneller te gaan.**

**Gedeelde productmap: `producten/steam-strook/`** (werknaam; de motor is voor alle drie de richtingen hetzelfde, het spel komt erin na de keuze van Thijs). Indeling, ieder zijn eigen deel:
- `producten/steam-strook/godot/kern/` en `ontwerp.md`: **Olaf** (venster, hoogte, klik door de lucht, zuinig tekenen, instellingen, opslag-aanroep, test op Actions).
- `producten/steam-strook/godot/systemen/` en `producten/steam-strook/sim/`: **Bram** (spelsystemen, voortgang terwijl je weg bent, balans-simulatie).
- `producten/steam-strook/godot/kunst/`: **Daan** (sprites, tegels, palet; Bram en Olaf lezen alleen).
- `platformen/steam/features.md`, `spelgevoel.md`: **Sanne**. `platformen/steam/idee.md`, `taken.md`, `status.md`: **Olaf**. `ontwerp/steam/`: **Daan**. Logboek: iedereen, een eigen regel met je naam.
- Workflow `.github/workflows/steam-strook.yml`: **Olaf** (Bram mag er een stap bij vragen).

**Olaf (hoofdbouwer)**
- [ ] (deels 9 nov 18:40 UTC) `idee.md` bijwerken met de opdracht van Thijs (vier eisen per richting getoetst), wat het niveau van de toppers betekent voor de bouw, en de gemeten strookhoogte van Rusty's Retirement en Ropuka's Idle Island.
- [ ] Kern van de strook in `producten/steam-strook/godot/kern/`: hoogte instelbaar door de gebruiker (standaard 120 px, keuze 96 tot 160), geen kaartjes over andere vensters (meldingen klein in de strook, meer pas bij hover binnen de strook), klik door de lucht, standaard 15 fps en niet tekenen als er niets beweegt, plaats voor opslaan. Test op de Windows-runner met schermafbeelding op 100, 120 en 140 px en CPU-meting. Richting-onafhankelijk, dus mag nu al.
- [ ] Na de plaatjes van Daan en features.md van Sanne: dossier met plaatjes op `organisatie/lijst-thijs.md`, Thijs kiest.

**Bram (tweede bouwer, features en systemen)** (Click Joints gaat voor als er iets is)
- [ ] **Proef pixel art en animatie in Godot** (`producten/steam-strook/godot/systemen/proef-pixel/` of een eigen scène die de kern van Olaf laadt; tot die er is, mag je uitgaan van `producten/steam-proef/` als voorbeeld): een tegelstrook van 120 px hoog in pixel art op schaal 3 (dus 40 spelpixels hoog), nearest-filter, hele schaal, 10 tot 20 bewegende figuurtjes van 16 bij 16 met 4 tot 6 frames op 15 fps. Meet op de Windows-runner de CPU (zelfde meting als `steam-proef`) en maak een GIF. Vraag: hoeveel kost "kleine animaties overal" zoals bij de toppers. Plaatjes: neem tijdelijke blokjes of vraag Daan om één testsprite onder "Vragen tussen ons".
- [ ] **Voortgang terwijl je weg bent, eerlijk** (`producten/steam-strook/godot/systemen/`): bij openen uitrekenen wat er gebeurde sinds de laatste keer (tijd uit de save, niet uit de klok alleen; klok terugzetten mag niets kapotmaken), met een samenvatting van één regel. Regel van Thijs: wie weg is, mist niets en verliest niets. Unittests.
- [ ] Na de keuze van Thijs: de spelsystemen van de gekozen richting volgens `features.md` van Sanne, en de balans-simulatie in `producten/steam-strook/sim/` (voortgang over honderden uren zonder muur).

**Sanne (game-ontwerper)**
- [ ] `platformen/steam/features.md` voor Het Hol (advies), met de vier eisen van Thijs als kern en per feature de toets; een korte vergelijking waarom niet de andere twee. Let op twee punten uit mijn weging (idee.md, 18:40): (1) Het Hol mag niet straffen als je weg bent (helden die ontsnappen nemen geen schat mee die je kwijt bent); (2) de strook wordt 100 tot 140 px hoog, dus een doorsnede met veel lagen past niet: ontwerp het hol zo dat het in de breedte groeit, of laat dieper zien bij hover.
- [ ] Reviews van de vier toppers tellen (Rusty's Retirement 2666510, Ropuka's Idle Island 3416070, Tiny Pasture 3167550, Deskrawl 4623570): wat prijzen ze, wat missen ze, waarom stoppen ze. Hoe verdienen ze aan DLC (zie idee.md: Tiny Pasture verkoopt thema en dieren als DLC).

**Daan (ontwerp)** (zijn opdrachten staan in `berichten/daan.md` 18:45 en 18:50; hier alleen de afspraak met de bouw)
- [ ] Nieuwe plaatjes op het niveau van de toppers, strook 100 tot 140 px, vergelijkingsbeeld (zijn bericht van Thijs). Voor de bouw graag: welke pixelgrootte en schaal (voorstel bouw: 16 px figuren op schaal 3 bij 120 px), en het palet, zodat Bram de proef op jouw maat doet.

**Vragen tussen ons** (nieuwste onderaan, "(antwoord <naam> <tijd>: ...)" erachter)
- Olaf 18:30 aan Daan: pixel art of rijk getekend? Jij beslist; zeg het hier, dan richt Bram de proef erop in. Mijn bouw-weging staat in `idee.md` (18:40).

## Eerder (Olaf, alleen)

Olaf, 9 nov 2026: de opdracht van Thijs (`berichten/olaf.md`, 15:40 en 16:00) vervangt de eerste taak van Hans hieronder.

- [x] (af 9 nov 15:35 UTC: in `idee.md` richting 3, vijf punten met citaten) **Richting 3: negatieve reviews lezen** van Spirit City (2113850), Virtual Cottage 2 (2943180) en Bongo Cat (3419430) (steamcommunity.com, zoals Vera's `steam-kans-klachten-script.py`), en "wat de top mist" in `idee.md` daarop baseren. Vóór Thijs kiest.
- [x] (af 9 nov 16:35 UTC: De Karavaan is richting 3, Toetsorkest afgevallen met reden, controleur akkoord na verbeteren; Silk Road Caravan 5495690 als dichtste concurrent erbij) **Daan, 9 nov 15:40 UTC: beeldtaal en De Karavaan wegen.**
- [ ] (deels 9 nov 17:40 UTC: drie sfeerbeelden staan, Het Hol v1 gezien en feedback over de strookhoogte in `idee.md`; nog: drie schermen) **Stap 2 met Daan:** hij maakt per richting een sfeerbeeld en een scherm (blok "Voor Daan" in `idee.md`). Daarna dossier met plaatjes op `organisatie/lijst-thijs.md`: Thijs kiest. Ik schrijf niet in `berichten/daan.md`; Thijs gaf Daan de klus al (9 nov 15:40). Antwoorden van Daan onderaan `idee.md`.
- [ ] **Stap 3 (pas na de keuze):** ontwerp in `producten/steam-<naam>/ontwerp.md` (waarom wij bovenaan), controleur, Daan; dan prototype in Godot, Windows-build en schermen via GitHub Actions.
- [ ] (stand 9 nov 17:20 UTC: alle zeven nog niet uit, zie logboek) **Volgen:** Silk Road Caravan: Desktop Idle (5495690, Q1 2027), Deskside Express: World Tour (5462890), Dungeon Architect: Idle (5368130), The Throne Below (5358260), Grave Ambition (5480960, 18 nov), Band Of Bots (4746850), Desktop Pet Band (4400730): uitkomst en reviews.
- [x] (af 9 nov 16:00 UTC: `idee.md`, controleur akkoord na verbeteren) **Stap 1: ideedossier met drie richtingen.**

Aangemaakt door Hans op 8 nov 2026. De berichten van Thijs in `berichten/sanne.md` gaan voor.

- [ ] **Eerste taak: uitzoeken wat we bouwen.** Lees `platformen/verkenner/voorstellen/steam-bureaublad.md` en de data van Vera in `platformen/verkenner/data/steam-*`. Bekijk de 20 best scorende Desktop Companion- en Idler-apps van 2026 (prijs, reviews, wat de reviews prijzen en klagen). Kies één klein product (Vera's idee "Desk-tuin": focus-timer en takenlijst waarbij een tuintje groeit, of iets beters) met de zin "waarom wij" en de 3 sterkste concurrenten. Laat een controleur het nalopen. Schrijf het bouwbesluit in `platformen/steam/bouwbesluit-<datum>.md` en zet het in `organisatie/besluiten.md`.
- [x] (af 9 nov 16:35 UTC, zie boven) **Daan, 9 nov 15:40 UTC: beeldtaal en een eigen concept voor je dossier** in `ontwerp/steam/beeldtaal.md`: huisstijl papieren theater en De Karavaan (met eerlijk wat niet nieuw is), sfeerbeelden `karavaan-sfeer.png` en `kerker-sfeer.png` (dat laatste is de idle-RPG van Vera in dezelfde taal). Neem de Karavaan mee als een van je drie als je hem sterk genoeg vindt; jij weegt het bewijs. Zet je richtingen in `idee.md`, dan maak ik per richting een sfeerbeeld en één echt scherm.
- [ ] **Vanaf het begin met Daan:** deze apps verkopen op sfeer en plaatjes. Vraag Daan via `berichten/daan.md` om mee te kijken bij de keuze van stijl, nog voor er gebouwd wordt.
- [ ] (deels 9 nov 16:30 UTC: technische proef `steam-proef.yml` groen, doorzichtige Godot-strook boven de taakbalk gezien; 16:40: klik door de lucht werkt, CPU gemeten (bijna een halve kern in software op 62 fps); 17:25: gewone exe zonder consolevenster, drie standen gemeten (63 fps 3,49 / 30 fps 2,94 / zuinig 15 fps 1,57 CPU-s per 10 s), zie logboek; 17:31: stilstaand beeld 0,02 CPU-s per 10 s, dus alleen tekenen als iets beweegt; nog: een echte export met exporttemplates, dat komt pas met het prototype) **Testen:** zet een test op GitHub Actions op (Windows-runner) die de app echt start en schermafbeeldingen maakt, net als bij de andere producten (`organisatie/regels.md`, deel Testen in de echte app).
- [ ] **Winkelpagina klaarzetten** (tekst, plaatjes, trailer) zodat die meteen live kan als Thijs het Steamworks-account heeft. Doel: verlanglijsten meten voor we afbouwen.
- [ ] **Betaald vanaf het begin:** het product is betaald ($3 tot $6, GOK). Geen gratis versie zonder reden.
