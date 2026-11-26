# Broncode: Battle for Wesnoth (Steam, gratis, tegelkaart met grotten en muren)

Uitgeplozen door de Afkijker op vr 27 nov 2026 (±00:30 NL), voor issue #20. Code gelezen uit `git clone --depth 1 --sparse` van https://github.com/wesnoth/wesnoth (laatste commit 260ce91, 26 nov 2026; alleen de tegelregels, de tegelbouwer en een paar grotplaatjes; niets uitgevoerd). Winkelpagina met curl gelezen.

## Waarom dit project
- **Steam: 94% van 3.261 Engelse reviews positief, laatste 30 dagen 95% van 43** (GEZIEN, https://store.steampowered.com/app/599390/, 27 nov). Het spel bestaat sinds 18 jun 2003 en is gratis.
- Het is het bekendste open spel dat een kaart uit losse tegels laat lezen als één stuk land, grotten en muren erbij. Precies waar Hats nu op vastloopt: de gangwand leest nog als "plat tegelpatroon" en "goedkoop behang" (blinde lezer, `producten/steam-hol/bewijs-gangsteen/LEESMIJ.md`), Iris geeft mooi een 7 (#223) en Olaf werkt aan de wand (#231).
- Licentie: GPL-2 (GEZIEN, `COPYING`), ook de plaatjes. Dus alleen het idee, geen code of beeld overnemen.
- Hun tegels zijn zeshoeken van 72 bij 72 pixels; Hats tekent op hele spelpixels in een strook. We lenen regels, geen vorm.

## Wat ze slim doen (bestand en regels)
1. **De gewone tegel komt het vaakst, de opvallende zelden.** Gras heeft 11 varianten, maar de eerste, de rustigste, krijgt vooraf een eigen kans van 20 tot 25% en doet daarna nog mee in de loting (`data/core/terrain-graphics.cfg` r. 605 tot 611, met de zin "The first grass tile of each kind is the most standard and generic one, thus it appears more frequently to space out the rest"; macro's `NEW:BASE` en `NEW:BASE_P` in `data/core/terrain-graphics/new-macros.cfg` r. 19 tot 62). Opvallende tegels staan zo verder uit elkaar, en het oog ziet geen herhaling.
2. **Het lijf van de muur is zwart; al het beeld zit aan de rand.** De grotmuur zelf is één zwarte zeshoek (`images/terrain/cave/wall-rough.png`, 72 x 72, GEZIEN). Wat je ziet als rots zijn alleen de stukken waar muur en vloer elkaar raken: 6 holle en 6 bolle hoeken (`wall-rough-concave-*.png`, `wall-rough-convex-*.png`), die groter zijn dan een tegel (126 x 144 en 126 x 180, GEZIEN) en dus over de buurtegel heen vallen. Aan de voet liggen losse brokjes op de vloer (GEZIEN in die plaatjes). De muur wordt per rand gekozen, niet per tegel (`NEW:WALL`, `NEW:WALL_MINOR_VARIANTS` in `new-macros.cfg` r. 3104 en 3292 tot 3337, met 6 varianten per hoek).
3. **Waar twee soorten elkaar raken, ligt de ene óver de andere, nooit ernaast.** Elke overgang is een eigen plaatje op de buurtegel met een laagnummer (bijvoorbeeld grotvloer laag -220, `terrain-graphics.cfg` r. 1235; muur als overlay op laag 0 met `BASE=144,144`, r. 638 en 639). De soort met de hoogste laag rafelt over de andere heen. Er is dus nooit een lijn waar de ene soort ophoudt en de andere begint.
4. **Drie soorten overgang per stof.** Gras heeft voor elke kant een harde (`green-abrupt-*`), een middel (`green-medium-*`) en een lange zachte overgang (`green-long-*`), 6 kanten elk (GEZIEN, map `images/terrain/grass/`). Welke er komt, hangt af van de buur.
5. **Vast toeval per plek, zonder ritme.** Elke keuze komt uit een vaste rekensom met x, y en de regel (`get_noise`, `src/terrain/builder.cpp` r. 178 tot 185), zodat de kaart bij elke start gelijk is. Ze delen de uitkomst eerst door een priemgetal "to break parity pattern" (r. 129 tot 132), omdat anders even en oneven plekken een patroon gaven. Een regel met een kans (`probability`) gebruikt dezelfde som (r. 1032 tot 1036).
6. **Versiering alleen waar het past.** Woestijnplantjes komen alleen naast een kasteel of kloof en dan met kans 17 (`terrain-graphics.cfg` r. 649 en 650). Kleine dingen staan dus aan randen, niet gelijk verspreid.

## Wat gebruikers klagen
Niet gelezen deze run: de review-lijst van Steam stuurt curl door naar de voorpagina, en de issuepagina's van hun GitHub geven 403. De cijfers hierboven komen van de winkelpagina zelf. Volgende keer via de communitypagina met negatieve reviews proberen.

## Welk product wordt er beter van
**Hats of the Fallen**, de gangwand in `producten/steam-hol/godot/hol/metsel.gd` (versie 5, GEZIEN `bewijs-gangsteen/v5-wand-4x.png`).
1. **Rust in het blok, detail aan de naad.** Nu krijgt elk blok één of twee lichte vlekjes en 1 op 4 een barstje (`_binnen`, r. 78 tot 96). Dat is precies wat Wesnoth vermijdt: overal een beetje maakt weer een patroon. Volgens hun regel: ongeveer de helft van de blokken egaal, vlekjes en barstjes alleen bij een op de drie, en liever bij een rand of een afgebrokkelde hoek dan midden in het blok.
2. **De voet van de muur is nu een rechte lijn op de vloer** (GEZIEN in v5, onderste rij blokken tegen de vloer). Bij Wesnoth valt de rots over de vloer heen met losse brokjes ervoor. Voor Hats: hier en daar een steentje of gruis van 1 tot 2 spelpx op de vloerrand onder de muur, vast per plek, nooit onder een held of val.
3. **Soorten wisselen nog per heel blok** (een heel blok oker naast een heel blok blauwgrijs, GEZIEN in v5). Wesnoth legt de ene soort óver de andere met een rafelrand. Voor Hats: bij de rand van een plek krijgt het eerste blok van de nieuwe soort aan de kant van de buur een paar spelpx in de tint van de buur (alsof leem over de steen is gelopen), in plaats van dat de kleur precies op een voeg omslaat.
4. **De bovenrand tegen de aarde:** Olaf deed in versie 5 een hap bij 1 op 3 blokken (`_bovenrand`). Wesnoth zou daar de aarde over de muur laten rafelen langs de hele lengte, met af en toe een groter stuk. Dat maakt de overgang aarde naar steen zacht, die de blinde lezer in versie 4 hard vond.

Beste les in één zin: bij Wesnoth is het lijf van een muur zwart en zit al het beeld waar twee dingen elkaar raken (rafelranden die over de buur vallen, brokjes aan de voet), terwijl onze gangwand zijn detail gelijk over elk blok strooit en de naden recht laat.

Geen nieuw issue (bijsturing hoofdmanager 25 nov 15:45): de les staat in `organisatie/lat/hats.md` en als reactie bij #231, waar Olaf al aan de wand werkt.
