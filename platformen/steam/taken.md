# Steam: taken (belangrijkste bovenaan)

## Taakverdeling Steam-team: Het Hol bouwen (Olaf, 9 nov 18:35 UTC)
Besluit Thijs 9 nov 19:20 (`organisatie/besluiten.md`): **de richting is Het Hol en we bouwen meteen het spel**, geen rondes concepten meer. Thijs ziet het pas als het speelbaar is en er goed uitziet. Niets betalen of publiceren tot hij het prototype goedkeurde. Team (19:00): Olaf hoofdbouwer en beslist over de bouw, Bram tweede bouwer (systemen), Sanne game-ontwerper, Daan ontwerp. Iedereen draait elk uur.

**De toets voor elke keuze** (Thijs 18:50): tussendoor leuk (30 s tot een paar minuten levert al iets op), grappig om te onderhouden (helden met een wrok, gekke bewoners), niet tijdrovend en **nooit straffen als je weg bent**, later skins en DLC alleen uiterlijk en inhoud, nooit betalen om sneller te gaan. **Strook:** standaard 120 px hoog, instelbaar 96 tot 160 px, geen kaartjes over andere vensters (meldingen klein in de strook, meer pas bij hover binnen de strook). Op dat formaat moeten detail en karakter overeind blijven.

**Productmap: `producten/steam-hol/`** (werknaam van het spel: Het Hol). Ieder werkt in zijn eigen deel:
| Wie | Schrijft in | Wat |
|---|---|---|
| Olaf | `producten/steam-hol/godot/project.godot`, `main.tscn`, `godot/kern/`, `godot/hol/`, `ontwerp.md`, `.github/workflows/steam-hol.yml`, `producten/steam-hol/e2e/` | venster en strook (hoogte, klik door de lucht, zuinig tekenen, hover), het hol zelf (raster, graven, kamers, schat), opslaan, de test en de GIF van een minuut spelen op Actions |
| Bram | `producten/steam-hol/godot/systemen/` (helden, bewoners, vallen, kroniek), `producten/steam-hol/sim/`, unittests daarvoor | helden die binnenkomen en door het hol lopen, karakter, vallen en bewoners, ontsnappen en terugkomen met wrok, litteken en bijnaam, kroniek, voortgang terwijl je weg bent, balans-simulatie |
| Sanne | `platformen/steam/features.md`, `spelgevoel.md` | welke features in de eerste speelbare versie, getoetst aan de opdracht; toetst elke GIF |
| Daan | `producten/steam-hol/godot/kunst/`, `ontwerp/steam/` | de echte stijl voor het spel zelf, op het niveau van Rusty's Retirement en Ropuka's Idle Island, op 120 px; `Akkoord:` bovenaan `ontwerp.md` |
`platformen/steam/idee.md`, `taken.md`, `status.md`: Olaf. Logboek `platformen/steam/logboek.md`: iedereen, een eigen kopje met je naam en tijd.

**Afspraak tussen kern en systemen (Olaf en Bram):** het hol is een raster van cellen (`Vector2i`), in `godot/hol/hol.gd` (Olaf). Bram gebruikt alleen deze functies en signalen en bouwt zijn helden en bewoners als losse scènes onder de node `Hol/Wezens`:
- `is_gang(cel) -> bool`, `cel_naar_pos(cel) -> Vector2`, `pos_naar_cel(pos) -> Vector2i`, `pad(van, naar) -> Array[Vector2i]`, `ingang() -> Vector2i`, `schat() -> Vector2i`, `val_op(cel) -> String` ("" of soort), signaal `gegraven(cel)`.
- Spelpixels: Daan kiest de maat; tot dan rekent de bouw met figuren van 16 bij 16 spelpixels op schaal 3 in een strook van 120 px (40 spelpixels hoog).
Wil je iets anders of extra: zet het onder "Vragen tussen ons".

**Olaf**
- [ ] **Eerste speelbare kern (nu):** `producten/steam-hol/`: strook van 120 px boven de taakbalk, instelbare hoogte, klik door de lucht, 15 fps en niet tekenen als er niets beweegt; een hol in de breedte met een ingang, gangen, één kamer met schat, graven met een klik; tijdelijke blokjes tot Daans kunst er is. Een eenvoudige held van mij als stand-in tot Bram de zijne levert. Workflow `steam-hol.yml` op de Windows-runner: echte schermafbeelding op 96, 120 en 160 px, CPU-meting, en een GIF van een minuut spelen (Godot Movie Maker). Daarna `ontwerp.md` met "Waarom wij" bovenaan.
- [x] (af 9 nov 18:40 UTC) `idee.md`: opdracht van Thijs, niveau van de toppers voor de bouw, gemeten strookhoogte van de toppers.

**Bram** (Click Joints gaat voor als er iets is)
- [ ] **Helden** in `godot/systemen/held.gd` en `held.tscn`: komen binnen bij `ingang()`, lopen met `pad()` naar de schat, twee karaktertrekken om mee te beginnen (hebzuchtig: gaat recht op de schat af; schijterig: keert om bij een val die hij heeft gezien), raken gewond door een val of een bewoner, sneuvelen (laten buit achter) of ontsnappen. **Ontsnapte helden komen terug** met een litteken, een wrok tegen wat hem raakte (de val of de bewoner bij naam) en een bijnaam die het spel ze geeft ("Bram de Driemaal Gevluchte"). Belangrijk: wie ontsnapt neemt niets mee dat jij kwijtraakt (geen straf).
- [ ] **Bewoners en vallen** in `godot/systemen/`: één bewoner (slijm) en één val (stekelput) om te beginnen.
- [ ] **Kroniek** in `godot/systemen/kroniek.gd`: houdt bij wie er binnenkwam, viel en ontsnapte; geeft één korte regel voor in de strook ("Bram de Driemaal Gevluchte is terug").
- [ ] **Voortgang terwijl je weg bent**: bij openen uitrekenen wat er gebeurde (tijd uit de save; klok terugzetten maakt niets kapot), één regel samenvatting, niets verliezen. Unittests (GUT of eigen kleine runner, jij kiest).
- [ ] Daarna: balans-simulatie in `producten/steam-hol/sim/` (voortgang over honderden uren zonder muur).

**Sanne**
- [ ] `platformen/steam/features.md`: welke features in de **eerste speelbare versie** (liever vijf echt goed dan twintig half), wat in versie 1, wat later (skins en DLC: holthema's, nieuwe heldengilden, bewoners, seizoenen). Per feature de toets van Thijs. Let op twee punten uit `idee.md` (18:40): niet straffen als je weg bent; en het hol groeit in de breedte, want 120 px heeft geen ruimte voor veel lagen (dieper zien bij hover kan).
- [ ] Reviews van de toppers tellen (Rusty's Retirement 2666510, Ropuka's Idle Island 3416070, Tiny Pasture 3167550, Deskrawl 4623570): wat prijzen ze, wat missen ze, waarom stoppen ze.
- [ ] Elke GIF van Olaf en Bram toetsen: is het leuk, duidelijk, grappig.

**Daan** (zijn opdrachten van Thijs staan in `berichten/daan.md`, 18:45, 18:50 en 19:20)
- [ ] De echte stijl voor het spel in `producten/steam-hol/godot/kunst/`: tegels voor aarde en gangen, schat, slijm, stekelput, een held met losse hoed en wapen (zo maken we veel verschillende helden uit weinig plaatjes, en hoeden zijn later skins). Zeg onder "Vragen tussen ons" welke spelpixelmaat en schaal je kiest.

**Vragen tussen ons** (nieuwste onderaan; "(antwoord <naam> <tijd>: ...)" erachter)
- Olaf 18:35 aan Daan: welke spelpixelmaat en schaal (voorstel bouw: 16 px figuren, schaal 3, strook 120 px = 40 spelpixels), en pixel art of rijk getekend? Jij beslist; tot dan bouw ik met blokjes op die maat. (antwoord Daan 18:40 UTC: **pixel art, cellen 16 x 16, schaal 3 op 120 px = 40 spelpixels: maaiveld 8 + twee rijen**, schaal 2 onder 120 px; precies jouw voorstel en je kern op `claude/steam-hol-kern`. Eerste bladen staan op main in `producten/steam-hol/godot/kunst/` met `kunst.json` en `LEESMIJ.md`: tegels als autotegel, gras, held met losse hoed en wapen, slijm, stekelput, schat, fakkel, ingang, versiering, gloed. Vervang je blokjes daarmee. Bram: held uit lijf + hoed + wapen, zie kunst.json.)
- Olaf 18:35 aan Bram: begin met `held.gd` tegen de functies hierboven. Ik zet vandaag of in mijn volgende run een eerste `hol.gd` met die functies op main; tot dan kun je de held los bouwen met een nep-hol dat dezelfde functies heeft.

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
