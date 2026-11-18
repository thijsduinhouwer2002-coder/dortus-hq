# Steam-app aanmaken: checklist voor woensdag 18 nov (Olaf, 16 nov 2026 ±20:45 UTC)

Opdracht hoofdchat 16 nov 20:20 (`berichten/olaf.md`). Thijs en de hoofdchat lopen dit woensdag 18 nov in ±15 minuten door. Daarna gaat het formulier van Laughs & Smiles in (deadline do 20 nov, appid en paginalink nodig).

**Bijgewerkt 17 nov 2026 ±14:45 UTC (Olaf):** (1) welk bestand in welk vak hoort, met maten en keuring, staat nu in `winkelpagina-klaar.md`; de tabel "Winkelpagina" hieronder is daardoor deels oud (Mila staat uit; de capsules in `ontwerp/steam/winkelpagina/` zijn nog de pixelversies van 10 nov, niet uploaden). (2) Paginadag is ±8 dec (besluiten 17 nov), niet 30 nov; daarvoor indienen uiterlijk vr 27 nov (7 werkdagen, GEZIEN 17 nov). (3) Sem staat uit tot ±1 dec: het formulier van Laughs & Smiles vult de hoofdchat zelf in met de antwoorden uit `marketing/teksten-makers.md`. (4) Wat Thijs moet doen gaat naar `berichten/hoofdchat.md`, niet meer naar `lijst-thijs.md`. Maten nagekeken in de docs op 17 nov: niets veranderd; event cover 800 x 450 is verplicht voor aankondigingen (stond er al).

**Bijgewerkt 17 nov 2026 ±16:55 UTC (Olaf):** ID-controle bij Valve loopt nog (hoofdchat, GEZIEN 17 nov); staat "Create new app..." grijs, volg dan `plan-b-id-controle.md` (één scherm: wat schuift bij eind december of eind januari). Winkelset volledig onder de Steam-namen in `ontwerp/steam/winkelpagina/`, header nu ronde 9 (Daan 15:55); blad voor Thijs wo 20:00 opnieuw gemaakt. Wat in welk vak: `winkelpagina-klaar.md`.

Alle bronnen zijn Steamworks-docs, gelezen met curl op 16 nov 2026 ±20:30 UTC (GEZIEN). Waar de docs niets zeggen staat **GOK**. Persoonsgegevens, nummers en inloggegevens komen hier nooit: "staat bij Thijs".

Stand nu (hoofdchat, 16 nov 20:12): nog geen app, **1 appcredit**, instapproces nog niet af ("Doorgaan met het instapproces"). $100 betaald op 9 nov (lijst-thijs).

## 0. Eerst: kan het al?
- De docs zeggen: "Once you have set up your account and your bank, tax and company information has been verified, you can add more users and start to set up your first product." Bron: `partner.steamgames.com/doc/gettingstarted`.
- Dus: staat "Create new app..." grijs of komt er een melding, dan moet eerst het instapproces af (punt 3). Dat is geen fout van ons; dan schuift de app tot Valve klaar is.
- Belasting wordt door een derde partij nagekeken, "up to 30 days", en je kunt de belastinggegevens niet wijzigen tot dat klaar is. Bron: `.../gettingstarted/onboarding`.
- **Gevolg voor Laughs & Smiles:** lukt de app woensdag niet, dan is er do 20 nov geen appid. Zet dan in het formulier wat zonder appid kan, of sla dit festival over (er past geen ander, zie `marketing/festivals.md`). Niet gokken met een nep-link.

## 1. "Nieuwe app maken": wat je kiest

| Stap | Wat | Later te veranderen? | Bron |
|---|---|---|---|
| Waar | Steamworks-startpagina, "Create new app..." onder "Create A New Application". Alleen een **Administrator** kan dit, en de credit kan alleen worden gebruikt door **wie de fee betaalde** (dus Thijs zelf, met zijn account). | | `.../store/application`, `.../gettingstarted/appfee` |
| Naam | **Hats of the Fallen** (precies zo, hoofdletters H, F; "of the" klein). | **Ja, tot de keuring van de winkelpagina.** Daarna niet meer zonder Valve te vragen. | `.../store/editing/name` |
| Type | **Game.** Desktop-apps zoals Rusty's Retirement staan ook als Game. | Ja: in App Admin, "General Application Settings". | `.../store/application` |
| Wat er verder gevraagd wordt | **GOK:** de docs beschrijven alleen naam en credit. Verwacht een bevestiging dat de credit wordt gebruikt. Vraagt het iets anders, kies het rustigste antwoord en schrijf het op voor dit bestand. | | |
| Appid | Komt meteen na aanmaken. **Verandert nooit.** Schrijf hem op in `platformen/steam/status.md` (een appid is openbaar, geen persoonsgegeven). | Nee | `.../store/application` |
| Credit | Is na aanmaken op. De $100 komt niet terug, wel verrekend zodra het spel $1.000 omzet haalt. | Nee | `.../gettingstarted/appfee` |

De naam staat op drie plekken, zet hem op alle drie gelijk: winkel ("Basic Info" onder "Edit Store"), Steamworks ("General Application Settings", voor bibliotheek en community) en elk winkelpakket. Bron: `.../store/editing/name`.

**Vertaalde naam:** Thijs koos Engels plus Vereenvoudigd Chinees (besluit 16 nov 20:04). Een vertaalde naam moet er **vóór de keuring** in, want daarna zit de naam vast. Advies: laat de Chinese vertaler een naam voorstellen, of kies bewust "Hats of the Fallen" ook in het Chinees. Bron: `.../store/editing/name`.

## 2. Na het aanmaken: winkelpagina en demo-app

### Winkelpagina ("binnenkort")
Alles in "Your Store Presence" op de checklist is verplicht vóór je hem als binnenkort zet. Bron: `.../store/coming_soon`.

| Wat | Eis Steam | Wie levert | Stand |
|---|---|---|---|
| Header capsule | 920 x 430, logo leesbaar | Mila, keurt Daan | v3 in `ontwerp/steam/winkelpagina/` |
| Small capsule | 462 x 174 | Mila | v2 |
| Main capsule | 1232 x 706 | Mila | v1 |
| Vertical capsule | 748 x 896 | Mila | v1 |
| Schermafbeeldingen | minstens 1920 x 1080, 16:9, **alleen spelbeeld** (geen tekst, prijzen of concept art) | Olaf uit de echte build | nog niet (plan.md punt 6) |
| Library capsule 600 x 900, hero 3840 x 1240, logo 1280 breed, library header 920 x 430 | verplicht | Mila | klaar, v1 tot v4 |
| Shortcut icon 256 x 256, app icon 184 x 184 | verplicht | Mila (`ontwerp/steam/icoon/`) | nakijken op maat |
| Event cover 800 x 450 | verplicht voor aankondigingen | Mila of Chris | nog niet |
| Trailer | niet verplicht, wel sterk aangeraden | Chris en Sem, draaiboek Daan (`trailer.md`) | voor 30 nov |
| Beschrijving, korte beschrijving, tags | samenhangend en gedetailleerd, **geen links** naar andere sites in de tekst | Sanne (`teksten.md` v3a), keurt Daan | klaar op tekst |
| Prijsvoorstel | Valve keurt de voorgestelde prijs mee | Thijs kiest (advies $6,99, kennisbank `winkelpagina.md` punt 4) | voorstel |
| Content Survey met **AI-deel** | zie valkuil 5 | hoofdchat met Thijs | open |
| Ontwikkelaar en uitgever | vrij in te vullen | "Dortus", gelijk aan de ontwikkelaarspagina van Abel | |

Bronnen: `.../store/assets`, `.../store/review_process`, `.../store/page`.

Daarna: "Mark As Ready For Review". **Lever minstens 7 werkdagen voor de gewenste datum in**, de keuring duurt meestal 3 tot 5 werkdagen. Na goedkeuring drukt Thijs zelf op de groene knop "Post as Coming Soon". Bron: `.../store/coming_soon`, `.../store/releasing`.

**Nieuw sinds 3 nov (nagekeken door Olaf, 18 nov ±21:30 UTC, met curl in de bron):**
1. **Buildkeuring duurt nu tot 12 werkdagen** (doel blijft 3 tot 5). DERDEN: https://www.invenglobal.com/articles/28152/valve-says-steam-pre-release-reviews-now-take-up-to-12-business-days (4 nov 2026, over de Steamworks-aankondiging van 3 nov). De officiele doc zegt nog 3 tot 5 werkdagen voor pagina en build (DERDEN: https://partner.steamgames.com/doc/store/review_process, gelezen 18 nov). Wij rekenen voor een build (spel of demo) **3 weken**; de pagina houden we op 7 werkdagen.
2. **Vóór het inzenden van een build: minstens 5 minuten spelen via de Play-knop van Steam**, binnen de laatste 7 dagen of na de laatste upload (speeltijd van elke gebruiker telt). Zelfde bron. Dus: na elke upload naar tak `intern` speelt Thijs of de hoofdchat 5 minuten via Steam, pas dan inzenden.
3. **Nieuwe punten op de checklist** (zelfde bron): kiezen welke redistributables Steam installeert (bij Godot: "geen nodig", GOK, nakijken bij de eerste build); onvolledige achievements worden gemarkeerd (wij hebben er nu geen, dan niets invullen); wie Steam Cloud opgeeft moet vóór de keuring een save naar de cloud schrijven (wij geven het niet op zolang er geen GodotSteam in zit); **minstens 5 schermafbeeldingen met het label "gameplay"** (labels nu: gameplay, menu, concept art, cinematic). Keurders kijken naar: pagina duidelijk en compleet, build doet wat de pagina belooft, gevoelige inhoud en AI-gebruik eerlijk in de Content Survey.
4. **Discounts & Events wordt vanaf begin 2027 door het algoritme gevuld** (geen handmatige plekken meer; Valve zag zo 10x meer spellen per dag in dat vak, met meer verlanglijsten). DERDEN: https://www.gamedeveloper.com/pc/steam-s-discounts-and-events-tab-will-soon-be-fully-algorithm-driven (29 sep 2026). Voor ons: verlanglijsten en klikratio tellen nog zwaarder; geen plek om "aan te vragen".

Rekenvoorbeeld (bijgewerkt 17 nov): winkelpagina live op di 8 dec betekent inleveren uiterlijk vr 27 nov; inleveren di 1 dec geeft op zijn vroegst do 10 dec. Beide ruim voor het Desktop Companion Fest van 14 jan.

### Demo-app
| Wat | Hoe | Bron |
|---|---|---|
| Aanmaken | Vanaf de pagina van het spel: "All associated packages, DLC, demos and tools", dan "Add Demo". **Kost geen credit**, krijgt een eigen appid, gekoppeld aan het spel. | `.../store/application/demos`, `.../store/application` |
| Instelling | Type "Demo" en het appid van het spel invullen in "General Application Settings", anders werkt hij niet goed. | idem |
| Eigen checklist | Korter dan van het spel; een eigen winkelpagina voor de demo is optioneel. Kies je die, dan: eigen trailer, **minstens 5 eigen schermen**, en capsules die duidelijk "Demo" zeggen. Advies: geen eigen pagina, de demoknop op de spelpagina is genoeg. | idem |
| Volgorde | Demo vóór het spel uitbrengen mag, **maar alleen als het spel als binnenkort zichtbaar is**. | idem |
| Build | Eigen depots en builds, net als het spel, geüpload met het demo-appid. Olaf maakt de build; het uploaden zelf zie valkuil 6. | idem |
| Prestaties | Valve raadt aan ze in de demo uit te zetten. Wij hebben er geen. | idem |

## 3. Instapproces Steamworks: alleen Thijs
Wat de docs vragen (bron `.../gettingstarted/onboarding`). Niets hiervan komt in de repo; alles "staat bij Thijs".
- **Digitaal papierwerk tekenen:** NDA en Steam Distribution Agreement. Alleen Thijs, voorwaarden accepteert niemand anders.
- **Wie tekent:** echte voor- en achternaam, geen bijnaam. Als particulier: vorm "Sole Proprietorship" en je eigen naam als "Company Name". De naam moet gelijk zijn aan die bij de bank en de belasting.
- **Bank:** de naam op de rekening moet gelijk zijn aan de naam bij het instapproces.
- **Belasting:** korte vragenlijst; buiten de VS met een belastingverdrag lijkt het op formulier W-8BEN. Thijs vulde het formulier al in op 9 nov (lijst-thijs). Nakijken door een derde partij duurt tot 30 dagen; let op mails die om extra papieren vragen.
- **Identiteit:** controle van wie je bent. Liep op 9 nov, "tot 30 werkdagen" (lijst-thijs).
- **Fee:** al betaald (9 nov).
- Wat wij wel kunnen doen: na het aanmaken de checklist in Steamworks lezen en invullen wat geen persoonlijke gegevens vraagt, maar alleen als Thijs zelf inlogt en wij meekijken. Wij loggen nooit in.

## 4. Valkuilen
1. **Wachttijd na de fee: de docs zeggen nu 21 dagen, niet 30.** "A 21-day waiting period between when you paid the app fee and when you can release that game." Betaald 9 nov, dus uitbrengen kan op zijn vroegst rond 30 nov. Voor ons plan (uitbrengen begin maart) maakt het niets uit. Bron: `.../gettingstarted/onboarding`.
2. **Minstens 2 weken binnenkort vóór uitbrengen.** Geldt voor nieuwe producten. Geen probleem bij een pagina in december en uitbrengen in maart. Bron: `.../store/coming_soon`, `.../store/releasing`.
3. **Naam zit vast na de keuring van de winkelpagina.** Ook de Chinese naam moet er dus vóór in (punt 1). Bron: `.../store/editing/name`.
4. **Op de pagina alleen wat er bij uitbrengen in zit.** Schermen en trailer met dingen die nog niet klaar zijn moeten eruit; wat later komt moet als "nog niet uit" vermeld. Sannes **[v1]**-regel in `teksten.md` past daar precies op. Schermen alleen spelbeeld, geen tekst of prijzen erin. Bron: `.../store/review_process`.
5. **AI-deel van de Content Survey eerlijk invullen.** Steam vraagt naar inhoud die "ships with your game and is consumed by players" en met hulp van AI is gemaakt: "artwork, sound, narrative, localization". Bij ons schrijft Claude de code, de Engelse teksten en de Blender-scripts die de 3D-beelden maken; er is geen beeldgenerator gebruikt en er draait geen AI in het spel zelf. Dat valt onder "Pre-Generated". Advies: dat zo melden, in gewone woorden (voorstel: "Game code, English texts and the Blender scripts that build our 3D models were written with the help of an AI assistant (Claude). No image-generation tools were used, and no AI runs inside the game."). Past bij het besluit van Thijs van 16 nov 16:51: AI eerlijk melden, niet verstoppen. Valve kijkt in de keuring of het spel klopt met wat de pagina belooft. Bron: `.../gettingstarted/contentsurvey`. Thijs kiest de zin.
6. **Builds uploaden kan alleen met een Steam-account dat rechten heeft.** De build gaat met de Steamworks SDK (steamcmd) naar Steam en daarvoor moet iemand inloggen. Wij loggen nooit in op accounts van Thijs. Opties voor Thijs, later: zelf uploaden met een script dat wij klaarzetten, of een apart bouwaccount maken met alleen uploadrechten (alleen Thijs maakt accounts aan). **GOK** op de werkwijze; nodig vóór de demo van 4 jan, niet voor woensdag. Bron: `.../gettingstarted` (SDK en "Uploading to Steam"). **Bijgewerkt 18 nov (Olaf):** gekozen voor het aparte bouwaccount. De workflow `.github/workflows/steam-uitbrengen.yml` staat klaar: alleen met de hand te starten, bouwt vol en demo, en zet ze met `game-ci/steam-deploy` (v3.3.0, vastgepind) op een niet-openbare Steam-tak (standaard `intern`; `default` en `public` weigert hij). Proefdraaien staat standaard aan en heeft geen sleutel nodig. Wat Thijs één keer doet staat in `berichten/hoofdchat.md` (18 nov). Starten kan ook met een tak `uitgave/hats-steam-v1.2.3` of een tag met die naam, met controles vooraf; zie `platformen/steam/uitgaven.md`.
7. **Rechten voor uitbrengen.** Voor "binnenkort" en uitbrengen zijn twee rechten nodig: "Publish app changes to Steam" en "Manage pricing and discounts". Thijs heeft ze als eigenaar; voegt hij later iemand toe, dan die rechten bewust wel of niet geven. Bron: `.../store/releasing`.
8. **Publiceren maakt alles openbaar,** ook schermen en bibliotheekbeelden van een pagina die nog verborgen is (sites lezen dat uit). Wil je eerst kijken: "Preview changes in store" (beta-modus), niet publiceren. Bron: `.../store/page`.
9. **Uitbrengen doe je zelf.** Een goedgekeurd spel gaat niet vanzelf live; Thijs drukt op "Release App" op het moment dat hij wil. Bron: `.../store/releasing`.
10. **De appid moet in de build.** Nu zit er geen Steamworks-koppeling in het spel (geen GodotSteam, geen `steam_appid.txt` in `producten/steam-hol`). Voor alleen downloaden via Steam is dat niet nodig; voor een winkelknop vanuit de demo (`ActivateGameOverlayToStore`) of Steam Cloud wel, met het **demo-appid** in de demo en het **spel-appid** in het spel. Als we dat bouwen: twee aparte appids, niet verwisselen. Bron: `.../store/application/demos`.
11. **Paginalink voor het festival:** de link `store.steampowered.com/app/<appid>/` bestaat na aanmaken, maar toont pas iets voor iedereen na keuring en "Post as Coming Soon". Schrijf dat erbij in het formulier als het om een openbare pagina vraagt. **GOK** dat de organisator een nog niet openbare link accepteert.

## 5. Woensdag in 15 minuten (volgorde)
1. Thijs logt in; kijk of het instapproces klaar is (punt 0). Niet klaar: stoppen, alleen noteren wat er nog openstaat (zonder gegevens).
2. "Create new app...", naam **Hats of the Fallen**, credit gebruiken.
3. Appid opschrijven in `platformen/steam/status.md`.
4. App Admin: type Game nakijken, naam in "General Application Settings" gelijk.
5. "Add Demo": demo-app aanmaken (type Demo, appid van het spel erin). Naam: "Hats of the Fallen Demo".
6. Ontwikkelaar en uitgever "Dortus".
7. Appid en link in het formulier van Laughs & Smiles (deadline do 20 nov), door de hoofdchat met de antwoorden uit `marketing/teksten-makers.md` (Sem staat uit tot ±1 dec).
8. Rest van de winkelpagina later: niets publiceren tot Daan de beelden keurde. Welk bestand in welk vak: `winkelpagina-klaar.md`.
