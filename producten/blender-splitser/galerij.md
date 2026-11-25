# Click Cuts: galerij en beste momenten (voor de Beeldmaker)

Productbouwer, 24 nov 2026 ±23:15 NL, issue #3. Alleen wat 1.0.0 doet (`CHANGELOG.md`). Lat: `organisatie/lat/click-cuts.md`. Het hoofdbeeld maakt de Beeldmaker; dit is wat ik hem lever: welke modellen, welke stand, en de onderschrift per galerijbeeld (Engels, Amerikaanse spelling zoals de add-on).

## Winkeltekst kop: GESLAAGD (blinde test 24 nov, `organisatie/blindtest/uitslag/click-cuts-tekst-2026-11-24-2226.md`)
Gekozen: **B**, plek 1.0 bij Gemini en bij ChatGPT in beide rondes tegen Cleave, Split 3D Print en SnapSplit (GEZIEN). C scoorde gelijk; B is korter en de haak lijkt niet op die van Cleave. A (de oude tekst) haalde 1,5.

Titel:
`Click Cuts: Split Models for 3D Printing to Fit Your Printer Bed (One Click, Pin Connectors, Fit Test, Part Numbers)`

Haak:
> Pick your printer. Click once. Every part fits.

Eerste alinea:
> Press Split to fit and Click Cuts plans every cut for you, so each part fits your bed, with pins, pin holes and an engraved part number on the cut faces. Each part turns green when it fits, is watertight and has enough wall around its holes, or orange or red with the reason. Print the small fit test block first and you know which clearance fits your printer, so pins are not loose or stuck.

Wat alle rechters missen: "snijdt hij niet dwars door het gezicht?" en "kan ik een snede zelf leggen?". Eerlijk antwoord dat 1.0.0 al waarmaakt, voor de FAQ: *Can I choose where it cuts? Split to fit places the cuts for you. Want an extra cut somewhere else, say along a neck? Free cut adds one at any angle through one part.* Snijden langs de vorm (zoals Cleave) is een gat in de lat, niet in 1.0.

## Beste momenten (op volgorde van kracht)
1. **Het voor en na in één beeld.** Model staat heel en steekt ver buiten het gouden kader van het bed (256 mm, Bambu-maat). Na Split to fit: dezelfde stukken uit elkaar in een kleur per stuk, gouden pennen, en elk stuk past in het kader. Dit is de kern: "one click and every part fits". Stand: exploded view aan, kleur per stuk aan.
2. **Het snijvlak van dichtbij.** Twee pengaten en het gegraveerde nummer op één snijvlak, schuin belicht zodat de gravure leest. Geen concurrent graveert nummers (lat). Dit is het detail dat "mooi stuk techniek" zegt.
3. **Alles groen.** De stukken in hun controlekleur (groen) met het paneel ernaast, één regel per stuk (vorm zoals "210x180x160 mm, wall 3.2", getallen als voorbeeld). Liefst één stuk oranje met de reden, zodat je ziet dat het echt meet.
4. **Het proefblokje.** Blokje met je eigen pen op vier spelingen, de spelingen gegraveerd en leesbaar van boven (`e2e/scherm_passing.py`, `passing-2.png`). Ons voordeel tegen alle drie.
5. **Het paneel.** Echte Blender met de tab Click Cuts open: printer kiezen, Split to fit, Export (`e2e/scherm_paneel.py`).

## Modellen (alle CC0, zelf in Blender, geen AI-beeld)
- **Lion Head, Poly Haven** (al gebruikt voor de cover, `merk/bron/splits_scene.py`). Goed, maar de rechters vroegen bij de eerste test om meer detail en een "personage".
- **Nieuw voorstel, sterker in een lijst vol anime-figuren:** `gothic_statue` (Gothic Statue, een staand beeld met veel detail) of `marble_bust_01` (Marble Bust 01) van Poly Haven, beide CC0 (GEZIEN, `api.polyhaven.com/assets?t=models`, 24 nov). Een staand beeld van 50 cm laat het "past niet, nu wel" groter zien dan een kop. Ook `horse_statue_01` kan.
- Schedel van 1M vlakken uit de e2e (`e2e/modellen.py` `schedel`) voor een "zwaar model, toch in een klik"-beeld, als derde of vierde.

Kies zelf welk model de blinde test wint; zet Cleave (plek 1) ernaast.

## Onderschriften galerij (Engels, plakklaar)
1. Hoofdbeeld: naam plus de haak **Pick your printer. Click once. Every part fits.** (GESLAAGD als tekst). De rechters vroegen "visual proof" van de ene klik: laat het voor en na zien in één beeld.
2. **Too big for your printer.** Pick your printer from the list. In this picture the gold box marks its bed, and this model is far bigger.
3. **One click, every part fits.** Split to fit plans every cut, so each part fits your bed, with pins and pin holes on the cut faces.
4. **Numbered for assembly.** Cut faces get pin holes and an engraved part number, like 3-5 where part 3 meets part 5.
5. **Checked before you print.** Each part turns green when it fits, is watertight and has enough wall around its holes. Orange or red tells you why.
6. **Pins that fit your printer.** Print the small fit test block first: your own pin at four clearances. Pick the one that fits, and Click Cuts remembers it for that printer and material.
7. **Three steps in one tab.** Press N in the 3D viewport and open the Click Cuts tab: pick your printer, Split to fit, Export as STL or 3MF in millimeters.

Keuring Daan #12 verwerkt (25 nov): M1 letterlijk, K1 (gouden kader alleen in dit beeld), K2 (CHANGELOG nu ook Amerikaanse spelling, zoals de add-on).

Mag sinds 25 nov wel: "Lay parts flat" (aan bij export, elk stuk op een snijvlak dat op je bed past; zonder zo een snijvlak houdt een stuk zijn eigen stand). Dus niet "every part lies flat", wel "parts are exported lying on a cut face".

Niet beloven: andere verbinders dan ronde pennen, en nooit dat wij printten of dat het klikt (CLAUDE.md regel 5).
