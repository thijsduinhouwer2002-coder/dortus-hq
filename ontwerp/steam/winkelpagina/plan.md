# Winkelpagina Het Hol: pakket (eigenaar wow: Mila, keurt: Daan, tekst: Sanne, beelden uit het spel: Olaf)

Opdracht Thijs 9 nov 23:45 NL: compleet pakket klaar uiterlijk **1 december**, zodat de hoofdchat het op de dag dat Valve het account vrijgeeft in één keer invult. Doel daarna: Steam Desktop Companion Fest, 14 tot 18 jan 2027.

## 1. Maten (GEZIEN met curl in de Steamworks-docs, 9 nov 23:45 UTC)
Bron: `partner.steamgames.com/doc/store/assets/standard`, `.../libraryassets`, `.../rules`.

| Bestand | Maat | Let op (docs) |
|---|---|---|
| Header capsule | 920 x 430 | logo goed leesbaar, kleinere maten maakt Steam zelf |
| Small capsule | 462 x 174 | Steam maakt er 120 x 45 en 184 x 69 van: **logo moet bijna het hele vlak vullen** |
| Main capsule | 1232 x 706 | voorpagina, logo leesbaar |
| Vertical capsule | 748 x 896 | |
| Schermafbeeldingen | 1920 x 1080 minimaal, 16:9 | minstens 5 (eis Thijs) |
| Page background | 1438 x 810 | optioneel, anders maakt Steam er een |
| Library capsule | 600 x 900 | |
| Library header | 920 x 430 | |
| Library hero | 3840 x 1240 | **geen tekst**, belangrijk spul in het midden 860 x 380 |
| Library logo | 1280 breed en/of 720 hoog | alleen het logo, doorzichtige achtergrond |
| (Bundle 707 x 232) | | niet nodig |

**Regels voor capsules (rules):** alleen spelbeeld, de naam en een officiële ondertitel. Geen reviewcijfers, prijzen, "wishlist now", kortingstekst of andere tekst. Tekst bij een update alleen als tijdelijke override van 14 dagen. Alles PG-13.

## 2. Naam (besluit Mila 9 nov 23:50 UTC, Daan en Sanne mogen tegenspreken tot 11 nov)
**Hats of the Fallen.** "Het Hol" blijft de werknaam binnen het team.
- Waarom: (1) de naam ís de haak: Gloop draagt de hoeden van wie hij opat, dat lees je in de naam en zie je in het logo; (2) een donkere grap op "Hall of the Fallen", past bij helden met een wrok en een kroniek; (3) uniek: Steam-zoeken op "Hats of the Fallen" geeft 0 treffers (GEZIEN, storesearch 9 nov).
- Afgewezen: alles met **Gloop** in de naam. Op Steam bestaan al "Gloop", "Gloop: Liquid Physics", "All Hail Gloop!" en "Walkabout Mini Golf: Gloop Lair" (GEZIEN). Gloop blijft wel de naam van het slijm in het spel. Ook afgewezen: "Lair Below" (0 treffers maar zegt niets grappigs), "Hatpile" (leest als rommel), "Underlair" (botst met "A Scoundrel in the Underlair").
- Wat het zou veranderen: een merk of spel met (bijna) dezelfde naam, of Thijs wil iets anders.

## 3. Logo (versie 2, 9 nov)
- Eigen pixelletter in hetzelfde spelpixelrooster als het spel. **HATS** groot in goud (de kleur van de schat), **OF THE FALLEN** kleiner in muntgroen (de kleur van Gloop). Dikke bijna zwarte pruimrand, zodat het op elke achtergrond leest.
- **Op elke letter van HATS staat een echte hoed uit het spel**: kroon op de H, koksmuts op de A, pan op de T, veermuts op de S. De letters zijn zelf ook opgegeten helden. Dat is de grap die je in 120 x 45 nog ziet.
- v2: HATS dikker (letterpixel 3 in plaats van 2) met reliëf: bovenste rij licht, onderkant en rechterkant donker goud; de hoeden staan nu óp de letters, zodat de punt van de A niet meer onder de koksmuts verdwijnt (las als H).
- Maker: `bron/maak_capsules.py` (functie `logo()`), leest alleen de echte plaatjes uit `producten/steam-hol/godot/kunst/`.

## 4. Stand per bestand
| Bestand | Stand | Wat nog |
|---|---|---|
| `header-920x430.png` | v3 | v2 verloor naast de toppers (`vergelijk-header-toppers.png`, op 292 breed zoals de winkellijst): logo en figuren te klein, donker vlak. v3: close-up op schaal 12, Gloop met vier hoeden als hoofdfiguur, held met pan links onder het logo, schat met gloed rechts, logo groter. **Eerlijk oordeel: herkenbaar en de grap leest, maar nog minder rijk dan Rusty, Tiny Pasture en Deskrawl** (die zijn geschilderd, met een dik eigen logo). v4: Gloop en de hoeden opnieuw tekenen op 3x de spelmaat (zelfde figuur, meer detail, licht van de schat op zijn huid) en een dikker logo met een gouden rand en reliëf. |
| `klein-462x174.png` | v2 | schaal 3 zodat het hele logo past (v1 sneed OF THE FALLEN af toen het logo dikker werd); op 184 x 69 en 120 x 45 lezen HATS met hoeden en OF THE FALLEN (GEZIEN). Kan nog: logo groter, minder lucht. |
| `main-1232x706.png` | v1 | sterrenlucht, gras, logo, daaronder de schatkamer met held, hoedenberg, Gloop met 4 hoeden en schat. Logo valt half over het gras, leest goed door de rand (GEZIEN). |
| `staand-748x896.png` | v1 | logo groot in de lucht, schatkamer onderaan. Eerste versie met lege bakstenen wand afgewezen (leeg midden). |
| `library-600x900.png` | v1 | zelfde opbouw als staand, verkleind naar 300 x 450 nog leesbaar (GEZIEN). |
| `hero-3840x1240.png` | v1 | geen tekst; Gloops gezicht en toren in het veilige vlak 860 x 380 (nagemeten met een kader). Eerste versie op schaal 10 was leeg en klein, nu schaal 16 met vondsten in de aarde. |
| `logo-1280.png` | v1 | 1280 breed, doorzichtig, alleen het logo |
| 5 schermafbeeldingen 1920 x 1080 | nog niet | van Olaf uit de echte build (strook op 160 px op een rustig bureaublad, plus een ingezoomd stuk ernaast), zie stijl.md punt 5 |
| trailer 30 tot 60 s | nog niet | eerste 3 s: een held loopt binnen, Gloop eet hem, zijn hoed vliegt op de toren. Opname van de demo-modus van Olaf |
| teksten, tags, prijs, skins en DLC | Sanne schrijft mee | voorstel prijs en DLC: hoeden-skins passen precies op de haak |

## 5. Eerlijk
Alles wat erop staat zit in het spel: 10 hoedsoorten (held_hoeden.png), hooguit 4 hoeden op Gloops hoofd en de rest op de hoedenberg (slijm.gd, `OP_HOOFD`, `berg()`), het boze wolkje en het uitroepteken (tekens.png), ingang, fakkels, schat. De lucht met sterren is versiering voor de capsule; in het spel ligt de strook op je bureaublad.

## 6. Schermafbeeldingen en trailer: wat ik van Olaf nodig heb
Alles uit de echte build (eerlijk). Steam toont schermen op 1920 x 1080 en verkleind in de winkellijst; de strook is in het echt 120 tot 160 px hoog. Daarom per scherm: **de echte strook op 160 px onderaan een rustig bureaublad, plus bovenin een vergroting (schaal 2 of 3 van dezelfde opname) met een dun kader**, zodat je ziet hoe klein het echt is én wat er gebeurt. De opmaak (bureaublad, kader, vergroting) maak ik; Olaf levert de ruwe opnames.

**Opnames (PNG, venster op 1920 breed, strook 160 px, demo-modus):**
1. Gloop eet een held: het frame waarop de hoed van zijn hoofd op de toren vliegt.
2. Gloop met 4 hoeden op zijn hoofd en een hoedenberg (maat 3 of hoger) naast zich.
3. Een terugkomer met litteken en het boze wolkje boven zijn hoofd, met zijn kroniekregel ("Bram is back for the Spike Pit.").
4. De stekelput gaat open onder een held, drie muntjes vliegen naar de schat.
5. Het hol na lang spelen: veel gangen, fakkels met gloed, de schat groot.
6. (als het er is) het kroniekpaneel met namen, bijnamen en hoeden.

**Trailer 30 tot 60 s (opname van de demo-modus, 60 fps, 1920 x 1080):**
- 0 tot 3 s, de haak: dicht op Gloop. Een held met een pan op loopt binnen, Gloop slokt hem op, de pan vliegt op de toren. Tekst in beeld: "Every hero leaves something behind."
- 3 tot 12 s: uitzoomen naar de echte strook onderaan een bureaublad met een spreadsheet erboven: "It lives under your taskbar."
- 12 tot 35 s: val, vlucht, de terugkomer met een wrok, de hoedenberg die groeit (versneld), de kroniek.
- 35 tot 50 s: tien hoeden op een rij, één voor één op de toren.
- Slot: logo, "Wishlist now" (in de trailer mag dat, op capsules niet).
Muziek en geluid: nog open (Sanne en Olaf, wat is er in het spel).
