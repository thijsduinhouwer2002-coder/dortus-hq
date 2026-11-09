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
- **Zuinig:** 15 fps en alleen tekenen als er iets beweegt. Gemeten (in software, zonder grafische kaart): stil beeld 0,02 CPU-seconden per 10 s, de strook met helden ±1 tot 1,2. Daarom bewegen fakkels en schat alleen als er toch al getekend wordt (er loopt een held). Elke run van `steam-hol.yml` meet het opnieuw.
- **Wie bouwt wat** (`platformen/steam/taken.md`): Olaf de kern (`kern/strook.gd` venster, tekst, opslag; `hol/hol.gd` raster, graven, kamers, vallen, tekenen), Bram de systemen (`systemen/`: held, slijm, kroniek, voortgang, toetsen), Daan de kunst (`kunst/`, gemaakt door een script, geen beeldgenerator), Sanne features, spelgevoel en balans.
- **Afspraak kern en systemen:** helden en bewoners gebruiken alleen `is_gang`, `cel_naar_pos`, `pos_naar_cel`, `pad`, `ingang`, `schat`, `val_op`, `put_klap` en het signaal `gegraven`.
- **Opslag:** `user://hol.json` (versie 2: gangen, kamers, vallen, schat, goud, terugkomers, kroniek, of de eerste held al geweest is). Een onleesbare save geeft een vers begin, geen crash.

## Spelen in de eerste versie
- Klik naast de gang in de aarde: een stuk gang erbij; graaf je voorbij de schat, dan verhuist de schatkamer (twee rijen hoog) mee naar achteren en blijft de oude kamer staan.
- Klik in de aarde boven de gang: een kamer (later woont daar een bewoner).
- Klik op de gang: een stekelput erbij of weg.
- Helden komen gemiddeld elke ±50 s (balans Sanne). De eerste held van een nieuw spel valt altijd, zodat er in de eerste minuut goud komt.

## Testen
`.github/workflows/steam-hol.yml` op een echte Windows-runner met Kladblok erachter: toetsen van Bram (0 FOUT), scripts laden zonder fout, schermafbeelding op 96, 120 en 160 px, CPU op 120 px, een film van een minuut (Movie Maker, 15 fps) als GIF. Alles op de tak `schermen` onder `steam-hol/<tak>/`.

## Nog niet (bewust)
Exporttemplates en een echte .exe (komt pas als Thijs het prototype goedkeurde), instellingenmenu voor de hoogte (nu een startargument), geluid (kunnen wij niet keuren), Steam zelf (niets betalen of publiceren tot Thijs ja zegt).
