Akkoord: nog niet (Daan zet hier `Akkoord: ja` of zijn punten als het prototype er goed uitziet)

# Het Hol: ontwerp van de bouw (Olaf, hoofdbouwer)

## Waarom wij
In elk ander taakbalkspel ben je de held; in Het Hol ben je de kerker, en de helden die erin vastlopen komen terug met een wrok, een litteken en een bijnaam, zodat je ze leert kennen.

Eerlijk wat nieuw is (`platformen/steam/idee.md`, GEZIEN): in de 405 Desktop Companion-apps is geen spel waarin je de kerker bent. Het idee "kerker bouwen tegen helden met karakter" bestaat wel: Dungeon Architect: Idle (5368130, gepland Q4 2026, gewoon venster, niet op de taakbalk). Nieuw aan ons: klein aan de rand van je scherm, en helden die terugkomen met een wrok, met een kroniek.

## De opdracht van Thijs (de toets voor elke bouwkeuze)
1. Tussendoor: een blik van een halve minuut levert al iets op; het loopt door als je niet kijkt.
2. Grappig om te onderhouden: helden met een naam en een wrok, bewoners met een eigen leven.
3. Niet tijdrovend en nooit straffen: wie ontsnapt neemt niets mee dat jij kwijt bent; voortgang terwijl je weg bent is alleen winst, met een plafond van 12 uur (Bram), zodat niemand dagelijks hoeft te kijken.
4. Later skins en DLC: alleen uiterlijk en inhoud (hoeden, holthema's, bewoners), nooit betalen om sneller te gaan.

## Hoe het gebouwd is
- **Motor:** Godot 4.3, GDScript. Eén doorzichtig venster zonder rand over de hele breedte, net boven de taakbalk, altijd boven. Alleen de strook vangt klikken; de lucht laat ze door (proef 9 nov, GEZIEN op de Windows-runner).
- **Strook:** standaard 120 px, instelbaar 96 tot 160. Pixel art op cellen van 16 spelpixels, schaal 3 (schaal 2 onder 120 px), 40 spelpixels hoog: maaiveld 8 en twee rijen (besluit Daan). Geen kaartjes over andere vensters: de kroniek staat klein in de strook, meer regels bij hover.
- **Zuinig:** 10 fps (20 tijdens een moment: val, hap, muntjes; `kern/beeldtempo.gd`, Daan 13 nov) en alleen tekenen als er iets beweegt. Gemeten (in software, zonder grafische kaart): stil beeld 0,02 CPU-seconden per 10 s, de strook met helden ±1 tot 1,2. Daarom bewegen fakkels en schat alleen als er toch al getekend wordt (er loopt een held). Elke run van `steam-hol.yml` meet het opnieuw.
- **Wie bouwt wat** (`platformen/steam/taken.md`): Olaf de kern (`kern/strook.gd` venster, tekst, opslag; `hol/hol.gd` raster, graven, kamers, vallen, tekenen), Bram de systemen (`systemen/`: held, slijm, kroniek, voortgang, toetsen), Daan de kunst (`kunst/`, gemaakt door een script, geen beeldgenerator), Sanne features, spelgevoel en balans.
- **Afspraak kern en systemen:** helden en bewoners gebruiken alleen `is_gang`, `cel_naar_pos`, `pos_naar_cel`, `pad`, `ingang`, `schat`, `val_op`, `put_klap` en het signaal `gegraven`.
- **Opslag:** `user://hol.json` (versie 2: gangen, kamers, vallen, schat, goud, terugkomers, kroniek, of de eerste held al geweest is). Een onleesbare save geeft een vers begin, geen crash.

## Spelen in de eerste versie
- Klik naast de gang in de aarde: een stuk gang erbij; graaf je voorbij de schat, dan verhuist de schatkamer (twee rijen hoog) mee naar achteren en blijft de oude kamer staan.
- Klik in de aarde boven de gang: een kamer (later woont daar een bewoner).
- Klik op de gang: een stekelput erbij of weg.
- Helden komen gemiddeld elke ±50 s (balans Sanne). De eerste held van een nieuw spel valt altijd, zodat er in de eerste minuut goud komt.

## Demo-einde (demolijst punt 6, Olaf 13 nov 2026; ontwerp controleur akkoord ronde 2, nog niet gebouwd)
**Wat het doet.** De gratis Steam-demo is hetzelfde spel met één verschil: na **2 uur open tijd** (speeltijd met het spel open, niet de tijd dat je weg was) komt er één vriendelijke regel in de kroniek: `That's the demo. Your hole keeps going.` (39 tekens). Daarna draait alles door: helden komen, vallen, vluchten, komen terug met hun wrok, Gloop eet en draagt hoeden, goud groeit, ook terwijl je weg bent (alleen winst, zoals altijd). Wat stopt is alleen **groeien**: graven, kopen en upgrades. Een klik op een koopbaar object opent het kaartje met `Full game: keep this hole.` in plaats van Buy. Undo en Remove blijven werken (je krijgt de volle prijs terug, niets is fout gekozen). Bij elke start na het einde staat bovenaan de kroniek nog één keer `Demo over. The full game keeps it all.` (38 tekens, past ook op 96 px).
**Hoe.** Nieuw veld `speeltijd_s` in de save (ook in oude saves vanaf 0). De demo-versie herkent het spel aan de Godot-feature `steamdemo` (eigen export-preset voor de demo) of het startargument `steamdemo=1`; het argument `demo_einde=<s>` zet de grens lager voor de test (standaard 7200). Zonder `steamdemo` is er nooit een einde. Om de save mee te nemen naar het volle spel gebruiken demo en vol dezelfde map: `application/config/use_custom_user_dir=true`, `custom_user_dir_name="Dortus/Het Hol"` in `project.godot` (er zijn nog geen spelers, dus de verhuizing kost niemand iets). De controle zit op één plek (`kern/demo_einde.gd`, klein en statisch): `voorbij(s) -> bool`, `regel_bij_einde(s)`, `regel_bij_start(s)`. Vragen eerst `voorbij` (controleur 13 nov ronde 1): `strook._input` vóór `hol.klik` (graven, kamer, put erbij; `hol.gd` kent de strook niet), `kaartje.koop` (de enige plek waar gekocht wordt, de demo-stap loopt er ook doorheen), `kaartje.beschrijving` en `tekst.gd` (`knop_koop`: tekst in plaats van de knop, zonder klikvlak; `ververs` zet een open kaartje meteen om), en `kaartje.tik` (geen muntje of koop-hint meer na het einde). `speeltijd_s` telt in `strook._process`; `opslag.gd` leest en schrijft alleen (`data.get("speeltijd_s", 0)`, versie blijft 3). De week-save in `.github/workflows/steam-hol-winkel.yml` (nu `%APPDATA%/Godot/app_userdata/Het Hol`) verhuist mee naar `%APPDATA%/Dortus/Het Hol`; de hoogte-keuze in `instellingen.json` raakt één keer kwijt (geen spelers).
**Bewust niet.** Geen aftelklok, geen schermvullende melding, geen knop "koop nu" (eerlijk en rustig, past bij nooit straffen). Geen andere save of ander formaat. Niets wordt afgepakt of op slot gezet wat je al had.
**Af als:** (1) toets in `systemen/toetsen` of een eigen toets: met `steamdemo=1 demo_einde=60` komt de regel na 60 s precies één keer, graven en kopen doen daarna niets (logregel `HOL demo voorbij: graven/kopen geweigerd`), helden blijven komen; (2) zonder `steamdemo` na dezelfde tijd geen regel en kopen werkt; (3) herstart met dezelfde save (zonder `vers=1`): speeltijd loopt door, startregel één keer; (4) toetsrun op Windows groen en `hol.json` staat echt in `%APPDATA%/Dortus/Het Hol`; (5) `demo_einde.gd` getoetst in `toets_systemen.gd`; winkelbeelden van de week laden de save nog.

## Testen
`.github/workflows/steam-hol.yml` op een echte Windows-runner met Kladblok erachter: toetsen van Bram (0 FOUT), scripts laden zonder fout, schermafbeelding op 96, 120 en 160 px, CPU op 120 px, een film van een minuut (Movie Maker, 15 fps) als GIF. Alles op de tak `schermen` onder `steam-hol/<tak>/`.

## Nog niet (bewust)
Exporttemplates en een echte .exe (komt pas als Thijs het prototype goedkeurde), instellingenmenu voor de hoogte (nu een startargument), geluid (kunnen wij niet keuren), Steam zelf (niets betalen of publiceren tot Thijs ja zegt).
