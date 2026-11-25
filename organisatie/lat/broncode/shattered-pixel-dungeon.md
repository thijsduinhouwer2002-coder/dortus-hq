# Broncode: Shattered Pixel Dungeon

Uitgeplozen door de Afkijker op 25 nov 2026, voor issue #20 (bijsturing hoofdchat 25 nov 10:55, project 3 van 4). Code gelezen met `git clone --depth 1` van https://github.com/00-Evan/shattered-pixel-dungeon (laatste commit 57a4e06, 6 okt 2026), alleen gelezen, niets uitgevoerd. Paden hieronder vanaf `core/src/main/java/com/shatteredpixel/shatteredpixeldungeon/`.

## Waarom dit project
- Een van de bekendste kleine pixelspellen: op Steam 2.202 aanbevelingen (GEZIEN, Steam appdetails-API, 25 nov 2026), "92% of the 882 user reviews in your language are positive" en "95% of the 49 user reviews in the last 30 days" (GEZIEN, https://store.steampowered.com/app/1769170/). Prijs 9,75 euro (GEZIEN). Op Steam sinds 23 mrt 2022, op de telefoon al ruim tien jaar (GEZIEN, reviews: "playing it for more than a decade").
- Klein beeld (figuren van 16 bij 15 pixels, `sprites/RatSprite.java` r. 34), toch leesbaar en levendig. Precies het probleem van Hats in een balk van 120 pixels hoog.
- **Licentie: GPL-3.0** (GEZIEN, `LICENSE.txt` r. 1 tot 2). Hats wordt gesloten verkocht, dus: **alleen leren hoe het werkt, niets kopiëren**, geen code, geen beelden.
- Sterren en GitHub-issues niet gelezen: de GitHub-API buiten onze drie repo's is in deze taak geblokkeerd (403). Klachten komen uit de Steam-reviews.

## Wat ze slim doen (bestand en regels)
1. **De grond onthoudt waar iemand liep.** Stapt een figuur in hoog gras, dan wordt dat vakje voorgoed kort gras (`levels/features/HighGrass.java` r. 55 tot 77, aangeroepen bij elke stap in `levels/Level.java` r. 1250 tot 1252). Na een tijdje zie je zonder uitleg waar het druk was: een pad door het gras. Kost niets extra: het is gewoon een andere tegel.
2. **Vuur laat as achter, en die groeit later weer dicht.** Brandt iets, dan wordt het vakje "embers", verbrande grond (`levels/Level.java` r. 930 tot 936, `destroy`). Die blijft liggen tot er iets groeit: een plant maakt van as weer gras (`levels/Level.java` r. 1057 tot 1064, `plant`; ook `actors/blobs/Regrowth.java` r. 49). Het hol vertelt zo wat er gebeurde, en heelt ook weer.
3. **Een dode verdwijnt niet in één beeld.** Na het sterfbeeld vervaagt het lijf in 3 seconden (`sprites/MobSprite.java` r. 34 `FADE_TIME = 3f`, r. 48 tot 55). Je oog heeft tijd om te zien wat er gebeurde.
4. **Leven met bijna niets.** Een rat in rust: 2 beelden per seconde, beelden 0, 0, 0, 1 (`sprites/RatSprite.java` r. 36 tot 37). Drie keer stil, één keer een trekje. Rustig, maar nooit dood. Dat is wat Hats bij Gloop al doet (knipperen elke 4 tot 7 s, `producten/steam-hol/godot/systemen/slijm.gd` r. 63 tot 67): goed.
5. **Elke tegel vast een eigen uiterlijk.** Bij het maken van een niveau krijgt elk vakje met een vast zaad een getal 0 tot 99, en daarmee kiest het spel een andere versie van dezelfde tegel (`tiles/DungeonTileSheet.java` r. 478 tot 489 en r. 548). Hats doet dat al met `_hash` (`producten/steam-hol/godot/hol/hol.gd` r. 407, `hol_vast.gd` r. 148 en 560): goed.

## Wat gebruikers zeggen (Steam, top-reviews in het Engels, GEZIEN https://steamcommunity.com/app/1769170/negativereviews/ en /positivereviews/, 25 nov 2026)
- Lof: "delightfully compact and lightweight you could run it on virtually anything"; "Easy to learn but hard to beat with frequent content updates"; "The golden standard for turn-based dungeon crawlers". Licht en klein is een verkoopargument, ook voor Hats (de top wordt afgekraakt om zware CPU, zie `organisatie/lat/hats.md`).
- Klacht 1, het vaakst: de bediening past niet bij de pc ("It says full controller support, but that's a lie. It just badly emulates a keyboard + mouse combo"; "Product refunded"). Les: beloof op de winkelpagina niets wat niet echt af is.
- Klacht 2: "the steam version can't be recommended as either you have the mobile version already" en "It just isn't the same" als op de telefoon. Les: de pc-versie moet iets hebben wat alleen op de pc kan. Voor Hats is dat juist de kern (het hol onder je taakbalk).
- Klacht 3: "being punished for exploring", "unbearably tedious". Straf voelt als werk. Past bij Thijs: Hats moet geen virus zijn (`organisatie/lat/wat-thijs-wil.md`).

## Zo doen zij het, zo doen wij het (Hats, `producten/steam-hol/godot/`)
| Wat | Shattered Pixel Dungeon | Hats nu |
|---|---|---|
| Wegkijken en terugkijken | de vloer zelf verandert: platgelopen gras, as, en later weer groen | alleen de hoedentoren en de hoedenberg rechts groeien (Olaf zelf, `producten/steam-hol/bewijs-wegkijken/LEESMIJ.md`: "de groei zit in de toren en de berg"); de gangen, het gras bovenop en de vallen zien er na 30 min hetzelfde uit (GEZIEN: `grep` op vlek, botje, voetstap en platgelopen in `godot/` vindt geen blijvend spoor; wel laat een gevallen held goud achter, `systemen/held.gd` r. 9) |
| Na een val | lijf vervaagt in 3 s | hoed vliegt naar de toren (goed, gekeurd) |
| Rust | 3 beelden stil, 1 beeld een trekje | Gloop knippert en ademt (goed) |
| Tegels | vaste versie per vakje | vaste versie per vakje met `_hash` (goed) |

**De les voor Hats:** laat niet één hoek groeien maar het hele hol sporen dragen. Bijvoorbeeld: waar veel helden langs liepen, raakt het gras bovenop plat en ontstaat een paadje naar de ingang; bij een val die vaak raak was, blijft een donkere vlek of een botje liggen; na een rustige tijd groeit het gras terug. Geen tekst, geen klok (tempo-regel 2). Alleen tegels wisselen, dus geen extra tekenwerk per beeld (licht blijven, zie lof hierboven). Dit is idee, geen code: GPL, niets overnemen.

## Wie er beter van wordt
- Olaf, issue #86 (wegkijken): nu 1 hoek die verandert, met sporen het hele hol. Bestanden: `godot/hol/hol_vast.gd` (maaiveld en gangen, r. 143 tot 151) en `godot/kern/afloop.gd` (waar een val raak is).
- Geen nieuw issue (bijsturing hoofdmanager 25 nov 15:45): #86 staat bijna klaar voor keuring en dit is een uitbreiding, geen groter gat. De les staat in `organisatie/lat/hats.md` onder "Lessen uit broncode".
