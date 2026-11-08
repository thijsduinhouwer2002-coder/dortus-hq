# Dortus-printreeks voor Blender: het vaste gezicht

Beheerd door Daan. Versie 1.1, 8 november 2026 (na controleur). Voor Bram (Click Joints) en Olaf (`platformen/blender-2/`, de volgende add-on), en voor elke add-on die later in de reeks komt.

## Waarom dit er is

Thijs besloot op 8 nov dat Blender ons eerste platform is en dat er een reeks print-add-ons komt (advies 4 van Stijn, overgenomen door Hans). Een koper die Click Joints kent, moet de tweede add-on op de lijst van Superhive en extensions.blender.org in één oogopslag herkennen als "van dezelfde makers". Dat verkoopt mee, en het spaart Olaf ontwerptijd: het icoon, het paneel en de poster liggen al klaar. Wat per add-on nieuw moet, is alleen het ene moment dat niemand anders heeft.

## Wat ons onderscheidt, in één zin

De concurrenten in de print-hoek (CatPin, Split-3DPrint, Cleave, Dovetail Key, GEZIEN op Superhive 8 nov via Bram en Stijn) maken de vorm en laten je dan gokken of hij past; een Dortus-add-on **meet het resultaat en zet het getal op het model**, voor je print.

## De vijf vaste onderdelen

### 1. De belofte: "See ... before you print."

Elke add-on heeft één zin in dezelfde vorm, overal gelijk (poster, README, Superhive, manifest). Click Joints: "See how far it bends, before you print." Een volgende add-on vult alleen het werkwoord in, bijvoorbeeld "See where it splits, before you print." of "See how thick it is, before you print." Het ene woord dat het product meet, staat op de poster in groen.

### 2. Het meetbeeld op het model

- Wat de add-on meet, staat op het model zelf: **wit**, met een donkere schaduw als rand, en het getal is altijd hetzelfde getal als in het paneel (stijl versie 23).
- Het meetinstrument is wit met streepjes (boog, liniaal of schuifmaat), maten zoals Click Joints (`waaier.py`): instrument 3 px, streepjes 2 px en 8 px lang, elke tweede 14 px, hulplijnen 1,5 tot 2 px half doorzichtig, alles maal `ui_scale`. Wit, omdat de delen zelf de passingkleur dragen.
- Passingkleuren op het model zijn voor de hele reeks gelijk, zoals `KLEUREN` in `click_joints/passing.py` (in Blender lineair opgeslagen): groen `#00D696` goed, citroengeel `#FFEA00` krap (nooit oranje, want oranje is in Blender selectie, stijl versie 14), rood `#FF4D4D` te ver of kapot. Het groen in icoon (`#45EBB6` naar `#009E70`) en op de poster (`#3BE6B0`) is bewust iets lichter, omdat het daar op een donkere tegel staat en niet in Solid.
- Nieuw voor de volgende add-ons (nog niet zo in Click Joints, daar staat de smalle band op de lijst voor versie 2): kleur alleen een smalle band langs waar de add-on ingreep, hooguit 1,5 mm, niet het hele deel. Waarom: zie moet 2 van de lanceerlijst in `producten/blender-gewrichten/ontwerp.md`.
- Rood komt alleen bij het unieke moment "voorbij de grens", met een korte tekst erbij in de vorm "+8° past limit": het teveel, dan de grens. Een maat te klein zegt het paneel zoals Click Joints: "Too thin: wall 0.62 mm (minimum 0.8 mm)".
- Winkelschermen recht van voren op het meetinstrument, zonder 3D-cursor, aslijnen of vloer (stijl versie 25).

### 3. Het paneel

- Eigen tabblad in de zijbalk (N) met de naam van de add-on, zoals Click Joints nu.
- Genummerde stappen als vakken, in de volgorde van het werk: `1  Place`, `2  <wat de add-on doet>`, `3  Fit and export`. Elk vak een Blender-icoon bij de kop. Drie stappen is de norm, vier mag; vijf of meer betekent dat de add-on te ingewikkeld is.
- Per vak één grote knop voor de hoofdhandeling (`grote_knop`, zoals bij Click Joints). Alle andere knoppen gewoon.
- De uitkomst bovenaan stap 3 als één regel met passingicoon ("Good fit"), daaronder de gemeten getallen ingesprongen (icoon `BLANK1`), met "(measured)" waar het gemeten is en niet berekend.
- Een probleem met het model als rood vakje (`alert`) met één knop die het oplost, zoals de mm-melding met "Convert to mm" in Click Joints. (Bij "not watertight" heeft Click Joints nu een gewone regel met een extra veld; voor nieuwe add-ons is het rode vakje het doel.)
- De gedeelde basis (printerprofiel, mm-controle, export STL | 3MF) wordt pas na de lancering van Click Joints een eigen module (opruimtaak, advies 4). Tot dan: neem paneel en gedrag over uit `click_joints/paneel.py` en `schaal.py`, zodat het er in elke add-on hetzelfde uitziet en op dezelfde plek staat. Vraag Bram via `berichten/bram.md` als iets onduidelijk is.
- Engels, korte woorden, geen punt achter een knop.

### 4. Het icoon

Sjabloon in `bron/` (zie `bron/icoon-click-joints.svg` en de twee voorbeelden). Vast:
- Tegel 256 px met hoek 56, verloop `#30343D` naar `#141519`.
- Het geprinte deel in grijs (verloop `#D3D6DC`, `#A6AAB3`, `#7C808A`).
- Groen (`#45EBB6` naar `#009E70`) alleen waar de add-on ingrijpt.
- Een wit meetinstrument met streepjes is het merkteken van de reeks. Het staat groot in beeld, want dat is wat ons onderscheidt.
- Een gestippelde witte basislijn mag als rust.
- Op ware grootte toetsen (64, 32 en 16 px, licht en donker). Proef: `familie-proef.png`. Click Joints en de voorbeelden lezen op 64 en 32 px als één familie; op 16 px blijft vooral de donkere tegel met een groen accent over, en dat is genoeg.
- Geen vorm die op iets anders lijkt dat in de print-hoek een betekenis heeft (een U leest als magneet, en magneetgaten zitten in betaald Click Joints).
- De voorbeelden "opsplitsen" en "wanddikte" zijn alleen om de regels te laten zien. Ze zijn geen keuze voor product 2; dat kiest Olaf met Hans.

### 5. De poster en de winkelplaatjes

- Sjabloon: `bron/poster-sjabloon.html`, invullen met `bron/vul.py` en een klein json-bestand (voorbeeld: `bron/voorbeeld-click-joints.json`). Zet de uitvoer-html in `bron/` (ICOON en SCHERM zijn paden vanaf daar), maak er een png van met `ontwerp/click-joints/bron/render.py`, en let zelf op: `vul.py` meldt geen ontbrekende sleutel en zet tekst zonder escape in de html. Nagekeken: het sjabloon met de waarden van Click Joints geeft pixel voor pixel dezelfde poster als `ontwerp/click-joints/poster-1.png`.
- Opbouw, 1920 bij 1080: links icoon met "<Naam> for Blender", de belofte groot (88 px, één woord groen), één zin uitleg, drie kaartjes (wit: het getal, groen: de passing, rood: voorbij de grens), voetregel (VOET: bij gratis "Free on Blender Extensions · STL and 3MF · Blender 4.2 to 5.2", bij betaald de prijs en Superhive) en rechts onderaan "Made by Thijs at Dortus". Rechts het echte scherm met het rode moment.
- Plaatje 2 en 3 met `ontwerp/click-joints/bron/kaart-basis.css`: plaatje 2 toont voor en na (of goed naast te ver), plaatje 3 het paneel met de uitkomst gemarkeerd.
- Getallen op de plaatjes zijn echt gemeten op een scherm uit de testworkflow; geen nep-labels (stijl versie 26).
- Elke add-on noemt de andere in de README en op de Superhive-pagina (advies 4), met het icoon ernaast, zodat de familie ook daar te zien is.

## Hoe Olaf dit gebruikt

1. Bij het voorstel aan Hans: schrijf de belofte in de vorm "See ... before you print." en het ene meetbeeld op het model. Kun je dat moment niet in één zin zeggen, dan is het product nog niet scherp.
2. Vraag mijn oordeel over het ontwerp **voor** het bouwen, onderaan `producten/blender-<naam>/ontwerp.md` (rol platformmanager). Ik keur dan op deze vijf onderdelen en op de lat: valt het op, is het mooi, wil je het hebben.
3. Icoon en poster maak ik, met dit sjabloon, zodra de eerste echte schermen er zijn.

## Wat niet vastligt

Het moment zelf. Bij Click Joints is het de witte boog met het getal en rood voorbij de grens. Elke volgende add-on moet een eigen moment hebben dat je wil laten zien aan een vriend; dit sjabloon is de lijst eromheen, niet het schilderij.
