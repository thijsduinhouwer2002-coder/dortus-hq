# Broncode van spellen onderaan het scherm: wat Hats ervan leert (25 nov 2026)

**De 5 technieken die de klachten van Thijs (issue #19) het meest oplossen, op volgorde:**
1. **App-balk:** meld het venster bij Windows aan met SHAppBarMessage (ABM_NEW, ABM_QUERYPOS, ABM_SETPOS met rand onder, ABM_REMOVE bij stoppen), zodat gemaximaliseerde vensters boven het spel eindigen. Voorbeeld: WpfAppBar `AppBarWindow.cs` r. 144 tot 230 (MIT). Lost op: typvak onzichtbaar, virus-gevoel.
2. **Doorklikbaar zonder bijknippen:** zet WS_EX_TRANSPARENT aan of uit door de muis te volgen in plaats van `window_set_mouse_passthrough` (dat knipt op Windows ook het beeld af). Standaard doorklikbaar. Voorbeeld: godot-native-click-through `native_click_through.cpp` r. 253 tot 321 (MIT). Plus een icoon in het systeemvak met Pauze, Geluid, Stoppen (Desktop Truck Simulator `system_tray.gd`, MIT). Lost op: virus-gevoel, te veel zonder controle.
3. **Loopbeeld aan afgelegde weg koppelen:** elk loopbeeld schuift een vast aantal pixels (Shimeji `actions.xml` r. 17 tot 24, `Pose.java` r. 43 tot 48), voeten als ankerpunt, even stilstaan voor het omdraaien (goob `pet.gd` r. 334 tot 342). Bij ons kiest `held_beeld.gd` r. 25 het beeld op de klok en schuift `held.gd` op een andere klok: daardoor glijden ze. Lost op: poppetjes lopen raar.
4. **Gedrag als gewogen keuzes met rust ertussen, en een val die altijd zichtbaar iets doet:** goob `pet.gd` r. 256 tot 330 (stilstaan, rondkijken, schrikken, rust na beweging), Shimeji `behaviors.xml` met eigen gewichten per karakter. Een held die niet valt, laat zien waarom (springt er zichtbaar overheen met een icoon). Lost op: lopen over vallen heen, helden niet bijzonder.
5. **De speler is de baas:** één zichtbaar doel tegelijk (Windowstead `rotating_goal.gd` r. 51), gebeurtenissen alleen als de speler er is, met een keuze uit/zelden/normaal/vaak en een vaste keuze als niemand klikt (idle.exe `event_director.gd` r. 1 tot 40 en 125, MIT), een knop voor tempo en voor grootte. Lost op: te veel zonder controle, niet duidelijk wat je moet doen, tekst te klein en te veel.

---

## Hoe gelezen
Alle repo's met `git clone --depth 1` in /tmp gezet en alleen gelezen, niets uitgevoerd. Licenties GEZIEN in het LICENSE-bestand van elke repo. Sterren DERDEN via shields.io (`https://img.shields.io/github/stars/<eigenaar>/<repo>.json`, 25 nov 2026), omdat de GitHub-API voor andere repo's dicht zat in deze sessie. Repo's gevonden via de opdracht en via GitHub-zoek (`search/repositories`, zoekwoorden: SHAppBarMessage, appbar C#, desktop pet godot, godot click through window, taskbar game idle, shimeji godot, idle bottom of screen). Op "tower defense bottom screen" en "SHAppBarMessage godot" gaf GitHub niets bruikbaars (GEZIEN).

**Overnemen:** alleen bij MIT, BSD, Apache of CC0, en dan met naamsvermelding (licentietekst plus naam in `producten/steam-hol/godot/LEESMIJ` of een bestand `DERDEN.txt` naast de exe). Bij GPL, geen licentie of een niet-commerciële licentie: alleen het idee, geen regel code.

## Hoe ons spel nu werkt (GEZIEN, `producten/steam-hol/godot/`)
- `project.godot`: randloos, altijd bovenop, doorzichtig, `no_focus`, viewport 1280 x 120.
- `kern/strook.gd` r. 162 tot 166: zet het venster onderaan de werkruimte (`screen_get_usable_rect`). Windows weet niet dat het spel daar ligt, dus een gemaximaliseerd venster loopt eronder door. Dat is de klacht van Thijs over het typvak.
- `kern/muisvlak.gd` r. 18: `window_set_mouse_passthrough`. Onze eigen notitie (r. 7 tot 9) zegt al: op Windows tekent het venster niets buiten dat vlak.
- `systemen/held_beeld.gd` r. 25: `frame = int(t * 8) % 4` (4 loopbeelden op 8 per seconde, op de klok).
- `systemen/held.gd` r. 47 tot 50: lopen in stappen van 1 spelpixel elke 0,1 s (eigen klok, los van het beeld).
- `systemen/held.gd` r. 368: `var valt := rng.randf() < kans`, met `KANS` slijm 0,45 en stekelput 0,35 (r. 51). Dus meestal loopt een held over een val heen zonder dat je ziet waarom.
- Geen icoon in het systeemvak, geen app-balk, geen eigen Windows-code (geen GDExtension, geen C#).

---

## Per repo

### 1. Windowstead
- Link: https://github.com/misospace/windowstead
- Licentie: **GPL-3.0** (GEZIEN, `LICENSE`). **Overnemen mag niet** (ons spel is gesloten); alleen ideeën.
- Sterren: 5 (DERDEN, shields.io).
- Wat het is: Godot 4 idle kolonie in een strook aan de rand van het scherm, 2 werkers, 3 gebouwen (README, GEZIEN).
- Wat we leren:
  - `scripts/main.gd` r. 458 tot 469 (`apply_dock_position`): plek berekend uit `screen_get_usable_rect`, net als wij. En r. 1413 tot 1423: elke 0,5 s kijken of de werkruimte veranderde (taakbalk verschoven, ander scherm) en dan opnieuw plaatsen. Hebben wij niet.
  - `scripts/main.gd` r. 627 tot 630 (`keep_window_pinned`): de vensterinstellingen (randloos, bovenop, doorzichtig) om de 20 tikken opnieuw zetten (r. 130 tot 131), omdat Windows ze soms kwijtraakt.
  - `scripts/main.gd` r. 122 tot 127: drie tempo's (Slow 1,6, Normal 1,0, Fast 0,65) die de speler kiest. Geeft controle.
  - `scripts/rotating_goal.gd` r. 25 tot 33 en r. 51 (`select_next_active_goal`): een vaste lijst doelen, steeds alleen het eerste nog niet gehaalde doel zichtbaar. Plus `milestone_manager.gd` voor vaste mijlpalen in het begin. Precies "altijd één zichtbaar volgend doel".
  - Ook Windowstead zelf heeft geen app-balk: het zet zich alleen in de werkruimte (GEZIEN, geen SHAppBarMessage in de code).
- Toepassen bij ons: werkruimte elke 0,5 s nakijken in `kern/strook.gd`; één doel tegelijk in `systemen/voortgang.gd` (of een nieuw `systemen/doel.gd`) met één regel tekst in groot schrift; tempo-keuze in het instellingenmenu.

### 2. goob
- Link: https://github.com/NovusEdge/goob
- Licentie: **geen** (GEZIEN: geen LICENSE-bestand, niets in README). **Overnemen mag niet**; alleen ideeën.
- Sterren: 2 (DERDEN, shields.io).
- Wat het is: Godot 4 kat over het hele scherm, doorklikbaar behalve de kat zelf.
- Wat we leren:
  - `scripts/main.gd` r. 310 tot 330 (`_update_passthrough`): het klikvlak volgt alleen wat nu onder de muis kan zijn (de kat, of het tekstballonnetje als de muis daarop staat). Alles daarbuiten gaat door naar het bureaublad.
  - `scripts/pet.gd` r. 8 tot 27: twee lagen. Gedrag (stilstaan, rondlopen, volgen, spelen, naar een hoek en slapen) en korte clips (verschijnen, schrikken, oppakken) die één animatie afspelen en dan terugkeren.
  - `scripts/pet.gd` r. 82 tot 95: een clip duurt altijd hele lussen van de animatie (`loop_lens`), nooit half afgebroken.
  - `scripts/pet.gd` r. 256 tot 322 (`_decide`): gewogen loting, met een stemming die de gewichten verandert, en r. 324 tot 330: na bewegen is rust waarschijnlijker (`SETTLE_BIAS` 1,8), na rust bewegen (`ROUSE_BIAS` 1,3). Geeft een ritme met rust en uitschieters.
  - `scripts/pet.gd` r. 334 tot 342 (`_move`): bij omdraaien eerst 6 tikken stilstaan (`TURN_PAUSE`), anders trilt hij heen en weer.
- Toepassen bij ons: in `systemen/held.gd` een staat "rondkijken" en "schrikken" als clip van hele lussen; draaipauze bij `vluchten`; per heldensoort (`systemen/heldensoort.gd`) eigen gewichten zodat de bange vaker stilstaat en de dappere doorloopt.

### 3. Godot Click Through Transparent Window (C#)
- Link: https://github.com/mbMayer/Godot-Click-Through-Transparent-Window-CSharp
- Licentie: **MIT** (GEZIEN, Copyright 2025 mbMayer). **Overnemen mag**, met naamsvermelding.
- Sterren: 11 (DERDEN, shields.io).
- Wat we leren:
  - `TransparencyWindow.cs` r. 9 tot 21 en 41 tot 45: Windows-functies aanroepen vanuit Godot C# met `DllImport` (GetActiveWindow, SetWindowLong met WS_EX_LAYERED, SetLayeredWindowAttributes met een kleursleutel, SetWindowPos HWND_TOPMOST). Het hele venster wordt doorzichtig op één kleur.
  - Nadeel: werkt alleen met de .NET-versie van Godot; ons spel is GDScript (`project.godot`). Een kleursleutel geeft rafelranden bij half doorzichtige pixels.
  - `screen_borders.gd`: muren langs de rand van het venster zodat dingen niet van het scherm vallen. Niet nodig voor ons.
- Toepassen bij ons: alleen als voorbeeld hoe DllImport eruitziet. Voor ons is een kleine GDExtension of hulp-exe beter (zie 6 en 7), zodat het spel GDScript blijft.

### 4. godot-click-through-transparent-window (GDScript, het origineel)
- Link: https://github.com/atadenizoktay/godot-click-through-transparent-window
- Licentie: **MIT** (GEZIEN, Copyright 2023 Ata Deniz Oktay). **Overnemen mag**, met naamsvermelding.
- Sterren: 104 (DERDEN, shields.io).
- Wat we leren: `src/scenes/godot.gd` r. 10 tot 20: het klikvlak elke natuurkundetik gelijk zetten aan een `CollisionPolygon2D` die met het figuurtje meebeweegt (`mouse_passthrough_polygon`). `src/scenes/canvas.gd` r. 21 tot 22: venster schermgroot maken in code om het opstartscherm te vermijden. Dit is wat wij al doen; het heeft hetzelfde nadeel (op Windows knipt het beeld mee).
- Toepassen bij ons: niets nieuws; bevestigt dat onze huidige aanpak de standaard is en dat de grens ervan bekend is.

### 5. godot-native-click-through (GDExtension)
- Link: https://github.com/KhangQuachUnique/godot-native-click-through
- Licentie: **MIT** (GEZIEN, Copyright 2026 Khang Quach). **Overnemen mag**, met naamsvermelding.
- Sterren: 3 (DERDEN, shields.io).
- Wat we leren:
  - README: meerdere klikbare veelhoeken die mogen bewegen, zonder `mouse_passthrough_polygon` en zonder WM_NCHITTEST.
  - `src/native_click_through.cpp` r. 253: muispositie ophalen met GetCursorPos; r. 315 tot 321: als de muis buiten alle veelhoeken staat WS_EX_TRANSPARENT aan (klik gaat door), anders uit. Het venster blijft dus helemaal getekend; alleen de muis gaat erdoorheen.
  - Wordt geleverd met kant-en-klare debug- en release-dll's (README).
- Toepassen bij ons: vervangt `kern/muisvlak.gd`. Dan mogen gras, helden die afdalen, hoeden en tekstballonnen boven het hol staan zonder dat ze wegvallen, en blijft alles erboven doorklikbaar. Eerst nakijken of hun dll voor Godot 4.3 werkt; anders zelf bouwen (zie 7).

### 6. WpfAppBar (de app-balk)
- Link: https://github.com/mgaffigan/WpfAppBar
- Licentie: **MIT** (GEZIEN, Copyright 2023 In Touch Technologies). **Overnemen mag**, met naamsvermelding.
- Sterren: 74 (DERDEN, shields.io).
- Wat we leren (de volledige app-balk, zoals de taakbalk zelf):
  - `WpfAppBar/NativeMethods.cs` r. 20 tot 28: de structuur APPBARDATA (cbSize, hWnd, uCallbackMessage, uEdge, rc, lParam); r. 140 en verder: de nummers van ABM en ABN; r. 170: `SHAppBarMessage` uit Shell32.
  - `WpfAppBar/AppBarWindow.cs` r. 135 tot 140: WS_EX_TOOLWINDOW zodat er geen knop in de taakbalk staat. r. 144 tot 145: `ABM_NEW` bij het openen.
  - `AppBarWindow.cs` r. 183 tot 230 (`OnDockLocationChanged`): rechthoek = heel scherm, `ABM_QUERYPOS` (Windows schuift hem langs de taakbalk), dan bij rand onder `rc.top = rc.bottom - hoogte`, dan `ABM_SETPOS`, en pas daarna het venster echt op die plek zetten. Vanaf dat moment maakt Windows de werkruimte kleiner: gemaximaliseerde vensters eindigen erboven.
  - `AppBarWindow.cs` r. 161 tot 166: `ABM_REMOVE` bij sluiten, anders blijft er een lege strook.
  - `AppBarWindow.cs` r. 286 tot 306: bij WM_ACTIVATE `ABM_ACTIVATE`, bij WM_WINDOWPOSCHANGED `ABM_WINDOWPOSCHANGED`, en bij de melding ABN_POSCHANGED opnieuw plaatsen (taakbalk verplaatst).
  - Wat het niet doet: ABN_FULLSCREENAPP (een spel of film op volledig scherm). Dat moeten wij zelf afhandelen (zie 8).
- Toepassen bij ons: de kern van issue #19. Omdat ons spel GDScript is, zit dit in een kleine eigen Windows-module: of een GDExtension (patroon 7) die `DisplayServer.window_get_native_handle(DisplayServer.WINDOW_HANDLE)` krijgt, of een hulp-exe naast het spel (patroon 8) die het proces-id krijgt, de app-balk aanmeldt en bij het einde van het spel `ABM_REMOVE` doet. `kern/strook.gd` r. 162 tot 166 roept die aan in plaats van alleen `window_set_position`. Of de hulp-exe-weg werkt voor een venster van een ander proces is een GOK: eerst proberen op Windows; de GDExtension-weg is zeker (zelfde proces, zelfde venster).

### 7. Desktop Truck Simulator
- Link: https://github.com/hubacekjakub/Godot-DesktopTruckSimulator
- Licentie: **MIT** (GEZIEN, Copyright 2025 hubacekjakub). **Overnemen mag**, met naamsvermelding.
- Sterren: 4 (DERDEN, shields.io).
- Wat het is: Godot 4.7 vrachtwagentje dat over de onderkant van het scherm rijdt, met icoon in het systeemvak (README, GEZIEN).
- Wat we leren:
  - `gdextension/src/win32_passthrough.cpp` r. 32 tot 47: de kleinste GDExtension die er is. Haalt het HWND op via `DisplayServer::window_get_native_handle(WINDOW_HANDLE)` en zet WS_EX_LAYERED en WS_EX_TRANSPARENT, met SWP_NOACTIVATE zodat het nooit de focus pakt. Hier kunnen de vier SHAppBarMessage-aanroepen uit repo 6 precies naast.
  - `.github/workflows/build.yml` r. 17: bouwt de GDExtension op `ubuntu-latest` (GEZIEN), dus wij kunnen hem in onze eigen GitHub-workflow bouwen zonder Windows-pc.
  - `bin/win32_passthrough.gdextension`: hoe Godot de dll laadt.
  - `autoloads/system_tray.gd` r. 14 tot 57: icoon in het systeemvak met Godot's eigen `StatusIndicator` (geen extra code nodig) en een `PopupMenu` (Zichtbaar, Aanpassen, Stoppen), rechtsklik opent het menu, menu blijft boven de taakbalk (r. 50 tot 56).
- Toepassen bij ons: een map `producten/steam-hol/godot/addons/dortus_venster/` met één GDExtension (app-balk plus doorklikken), gebouwd in een workflow. Een nieuw `kern/systeemvak.gd` naar het voorbeeld van `system_tray.gd` met: Pauze, Geluid aan/uit, Grootte, Stoppen. Dat geeft Thijs de "uit-knop" die bij een virus ontbreekt.

### 8. idle.exe (XYMYX)
- Link: https://github.com/XYMYX/idle.exe
- Licentie: **code MIT** (GEZIEN, `LICENSE`, Copyright 2026 XYMYX); **tekeningen CC BY-NC 4.0** (GEZIEN, `LICENSE-ART.md`). **Code overnemen mag** met naamsvermelding; **tekeningen niet** (niet-commercieel).
- Sterren: 0 (DERDEN, shields.io).
- Wat het is: Godot 4.7 idle spel voor Windows dat boven de taakbalk leeft (README, GEZIEN). Het dichtste bij ons van alles wat ik vond.
- Wat we leren:
  - `scripts/fullscreen_watch.gd` r. 1 tot 66 en `tools/sysinfo/sysinfo.cpp` r. 155 tot 200: een kleine hulp-exe (`idle-sysinfo.exe --watch <pid> fullscreen notaskbar`) die het spel start met `OS.execute_with_pipe`. Die verstopt het figuurtje als een ander programma het scherm vult (spel, film), geeft het venster WS_EX_TOOLWINDOW (geen taakbalkknop, niet in Alt+Tab) en stopt vanzelf als het spel weg is. Gebouwd met één regel g++ (`tools/sysinfo/README.md`). Dit is het patroon voor een hulp-exe zonder GDExtension.
  - `scripts/event_director.gd` r. 1 tot 40: gebeurtenissen alleen als de speler er is (muis beweegt) en het spel niet op pauze staat; wacht 180 s (GEZIEN, `TIMEOUT_SEC`) op een keuze en kiest dan zelf een vaste, veilige keuze (r. 114 tot 118); nooit dezelfde van de laatste 6 (r. 11). r. 125 tot 127: tussentijd uit de instellingen.
  - `docs/DESIGN.md` r. 289: instellingen grootte (auto, 1x tot 4x), muisreacties aan/uit, in slaap na 5/10/20 min of nooit, gebeurtenissen uit/zelden/normaal/vaak.
  - `scripts/mouse_watch.gd` r. 1 tot 20: kijkt alleen naar de muispositie (10 keer per seconde), geeft "weg", "terug", "geschrokken" (snelle muis vlakbij) en "hover 1,5 s". Het figuurtje reageert op jou, zonder toetsen te lezen.
  - `scripts/play_director.gd` r. 1 tot 5: een speelmoment elke 20 tot 45 minuten, of meteen bij een klik op de speelgoedkist. Rust is de standaard, de speler kan het opwekken.
- Toepassen bij ons: de verstop-bij-volledig-scherm en de geen-taakbalkknop in dezelfde Windows-module als de app-balk. Instellingen grootte en gebeurtenissen-frequentie in het menu (lost "tekst te klein" en "te veel zonder controle" op). Helden alleen laten komen als de speler er is, met een rustig ritme; `kern/wachtrij.gd` en `kern/binnenkomst.gd` zijn de plekken.

### 9. Shimeji-ee
- Link: https://github.com/chaoskagami/shimeji-ee
- Licentie: **New BSD** volgens `readme.txt` r. 97 (GEZIEN), plus de oorspronkelijke zlib/libpng-achtige licentie van Yuki Yamada in `originallicense.txt` (GEZIEN). GitHub herkent geen licentie (DERDEN, shields.io). **Code overnemen mag** met naamsvermelding; de plaatjes zijn van de makers van de figuren, niet gebruiken. We nemen in de praktijk alleen het idee over (Java, ander spel).
- Sterren: 0 (DERDEN, shields.io; het is een kopie van het oude project).
- Wat we leren:
  - `conf/actions.xml` r. 17 tot 24: Lopen is 4 houdingen (`shime1, shime2, shime1, shime3`), elk 6 tikken van 40 ms (`Manager.java` r. 28, `TICK_INTERVAL = 40`), en **elke houding heeft zijn eigen snelheid** (`Velocity="-2,0"`). Rennen is dezelfde reeks met 2 tikken en snelheid 4, Dash met snelheid 8 (r. 26 tot 42). Beeld en beweging zijn dus één ding: geen glijden.
  - `src/com/group_finity/mascot/animation/Pose.java` r. 43 tot 48: per tik eerst het ankerpunt verschuiven met de snelheid van de houding, dan het plaatje van die houding zetten.
  - `ImageAnchor="64,128"`: het ankerpunt zit onder de voeten, midden onder, zodat een figuur nooit door de vloer zakt of zweeft.
  - `conf/actions.xml` r. 327 tot 345: rustacties met willekeurige duur (`500+Math.random()*1000` tikken), en een zitreeks met benen omhoog, omlaag, bungelen, omlaag, omhoog. Kleine gebaren maken het levend.
  - `conf/behaviors.xml` r. 42 tot 94: keuzes met gewichten (opstaan 200, gaan zitten 200, lopen 100, kruipen 10) en voorwaarden (`Condition`). En drie losse gedragsbestanden (`CalmBehavior.xml`, `MischievousBehavior.xml`, `ProfessionalBehavior.xml`): **zelfde figuur, ander karakter door alleen andere gewichten**.
- Toepassen bij ons: in `systemen/held_beeld.gd` het loopbeeld kiezen op afgelegde spelpixels in plaats van `int(t * 8) % 4`, met minstens 6 loopbeelden (Mila tekent, `kunst/held_lijf_kleuren.png` en `kunst/held_soort.png` hebben er nu 4, GEZIEN in `held_beeld.gd` r. 7 en 12). In `systemen/heldensoort.gd` per soort een gewichtentabel (de bange: vaak stilstaan en rondkijken; de dappere: rent door; de rijke: blijft staan om goud te laten vallen), zoals Shimeji drie karakters met één figuur maakt.

### 10. Taskbar Legion
- Link: https://github.com/Nyhz/taskbar-legion
- Licentie: **PolyForm Noncommercial 1.0.0** (GEZIEN, `LICENSE.md`). **Overnemen mag niet** (wij verkopen); alleen ideeën.
- Sterren: 1 (DERDEN, shields.io).
- Wat het is: auto-vechtend RPG in een dunne strook onderaan het scherm, Tauri (README, GEZIEN).
- Wat we leren: `src/platform/desktopOverlay.ts` r. 14 en r. 256 tot 271: muis volgen en per stuk kiezen of klikken doorgaan, met als regel "standaard doorklikbaar: als het volgen ooit hapert, mogen we het bureaublad niet vastzetten". Dat is de veilige keuze die het virus-gevoel voorkomt.
- Toepassen bij ons: dezelfde regel in de Windows-module: bij twijfel of fout gaat de muis door het spel heen.

---

## Commerciële spellen (geen open code, alleen openbare info)
- **Rusty's Retirement** (Steam 2666510): uit onze eigen verzameling negatieve reviews (`platformen/steam/data/reviews-2026-11-09/top4.json`, GEZIEN, opgehaald 9 nov): "Having to manually adjust all other windows to fit this game is more hassle than its worth" (0,3 uur gespeeld), "Unable to opt out of events" (9,0 uur), een speler die zegt dat het spel beter zonder geluid zou zijn omdat geluid afleidt (158,4 uur), en klachten dat robots "clip right through" bomen (10,6 uur). Dat zijn dezelfde klachten als die van Thijs: vensters eronder, geen controle over gebeurtenissen, geluid, figuren die door dingen heen lopen. De app-balk lost de eerste op; een uit-knop voor gebeurtenissen en geluid de tweede en derde; techniek 3 en 4 de vierde.
- **Desktop Heroes** en de rest: zie issue #19 (hoofdchat, 24 nov). Niets gedecompileerd.

## Wat we niet vonden
- Geen enkel open Godot-spel dat SHAppBarMessage gebruikt (GEZIEN, GitHub-zoek gaf 0 Godot-treffers). Hats wordt dus de eerste in dit genre met een echte app-balk in Godot; de code daarvoor komt uit WpfAppBar (MIT) in een GDExtension naar het patroon van Desktop Truck Simulator (MIT).
- Geen open "tower defense onderaan het scherm".

## Naamsvermelding als we code overnemen
In `producten/steam-hol/godot/DERDEN.txt` (nieuw, gaat mee in de build): naam van de repo, link, de MIT- of BSD-tekst met de copyrightregel. Voor nu: WpfAppBar (In Touch Technologies, MIT), Desktop Truck Simulator (hubacekjakub, MIT), godot-native-click-through (Khang Quach, MIT), idle.exe code (XYMYX, MIT) als we iets uit `sysinfo.cpp` gebruiken.

## Issues voor Olaf (25 nov)
- #24 app-balk, doorklikken, systeemvak
- #25 lopen en vallen die altijd zichtbaar iets doen
- #26 de speler is de baas (één doel, rustig ritme, grootte en gebeurtenissen instelbaar)
