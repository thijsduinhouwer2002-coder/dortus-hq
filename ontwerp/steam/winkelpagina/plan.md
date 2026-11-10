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
- **Sanne stelde tegelijk "Hat Hoard" voor** (`teksten.md`, ook 0 treffers). Afweging: Hat Hoard is korter en past makkelijker klein; Hats of the Fallen heeft de grap en de toon van het spel (een donkere woordgrap, helden die vallen), en op 120 x 45 leest het logo ook (GEZIEN). Ik houd Hats of the Fallen; Daan beslist mee vóór 11 nov. Kiest hij Hat Hoard, dan past de maker zich aan (alleen de tekst in `logo()`).
- Abel (accountverzorger, bericht Thijs 23:50 NL) maakt de merkkit voor de ontwikkelaarspagina: hij krijgt van mij het logo, de kleuren (pruim #1d1426 en #3f2846, schatgoud #ffd25c, Gloopgroen #7ee0ae) en de pixelletter, zodat winkelpagina en ontwikkelaarspagina één geheel zijn.

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
| `hero-3840x1240.png` | v4 | geen tekst; schaal 13 (was 16), want Gloop met toren is 27 spelpixels hoog en paste op 16 nooit in het veilige vlak; nu valt de hele toren binnen 860 x 380 (y 430 tot 810), nagemeten met een rood kader op de echte uitvoer. Twee helden in de rij, meer vondsten in de aarde. |
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
- 0 tot 3 s, de haak: dicht op Gloop. Een held met een pan op loopt binnen, Gloop slokt hem op, de pan vliegt op de toren. Tekst in beeld: "He keeps the hats." (voorstel Sanne, beter dan mijn "Every hero leaves something behind.")
- 3 tot 12 s: uitzoomen naar de echte strook onderaan een bureaublad met een spreadsheet erboven: "It lives on your taskbar."
- 12 tot 35 s: val, vlucht, de terugkomer met een wrok, de hoedenberg die groeit (versneld), de kroniek.
- 35 tot 50 s: tien hoeden op een rij, één voor één op de toren.
- Slot: logo, "Wishlist now" (in de trailer mag dat, op capsules niet).
Muziek en geluid: nog open (Sanne en Olaf, wat is er in het spel).

## Versie 4 (Mila, 10 nov ±02:30 NL): moet-punten keuring 1 van Daan
- **1, A en S:** de A heeft een dicht dak (`.XXX.` / `XX.XX`), de S dichte hoeken (`XX...` en `...XX`), de O ook (Daan 10). De hoeden staan nu op de letters in plaats van erboven: los erboven lazen ze klein als umlaut (HÄTS). Op 120 x 45 lees je HATS (GEZIEN).
- **4, twee dezelfde kisten:** alle vier de cellen van `schat.png` zijn dezelfde kist met een andere glinster, dus twee naast elkaar is altijd een kopie. Nu één kist met losse munten ernaast (zelfde kleuren als de muntjes in `hol.gd`), en de kist staat overal binnen het beeld.
- **5, klein:** HATS op blok 4 (logo vult ±62% van de breedte), Gloop met toren op schaal 4 rechts in een gloed. Eerlijk: Gloop blijft op 120 x 45 klein; de naam draagt het kleine formaat.
- **6, hero:** zie de tabel hierboven.
- **12:** de held op de header draagt nu de rode hoofdband, niet een hoed die al op de toren staat.
- **B, trailer:** "It lives on your taskbar."
- Nog open: 7 (goudhoop als croissant), 8 (hero rijker), 9 (header v4 naast de toppers), 13 (marge onder het logo).

## Versie 5 (Mila, 10 nov ±03:00 NL): moet-punten keuring 3 van Daan
Header, main, staand en library zijn opnieuw opgebouwd als **close-up in de schatkamer**: geen lucht en gras meer, een stenen muur tot boven, en Gloop met zijn hoedentoren als hoofdbeeld. Klein en logo kregen alleen de nieuwe letters; de hero is niet veranderd (die had akkoord).

| Capsule | Schaal | Gloop met toren (28 spelpixels) | Logo | Goud tot de rand |
|---|---|---|---|---|
| header 920 x 430 | 10 | 280 px = **65%** van de hoogte | 486 px = **53%** van de breedte, 24 px van links | 30 px |
| main 1232 x 706 | 14 | 392 px = **56%** | 567 px = 46%, 40 px van links | 42 px |
| staand 748 x 896 | 13 | 364 px = **41%** | schaal 8, midden | 59 px |
| library 600 x 900 | 20 | 560 px = **62%** (een portret: Gloop kijkt je aan) | schaal 6, midden | 40 px |
Alles nagemeten in de png's (GEZIEN).

- **Daan 1, Gloop groot:** zie de tabel. De library is nu een portret van Gloop met zijn toren, munten aan zijn voeten en het licht van de schat (buiten beeld) op hem. Waarom: in de rij met de toppers was dat het verschil: zij hebben een figuur dat je aankijkt, wij hadden een muur. Gloop met één oog kijkt je nu aan.
- **Daan 2, logo groot:** header 53% breed met 24 px marge links.
- **Daan 3, warmer en lichter:** warm licht (schatgoud en fakkel) valt nu groot over de muur, van rechtsonder; bovenin blijft het pruim. Het licht ligt sterk op de muur en zwak op de figuren, zodat Gloop groen blijft (eerste poging maakte hem mintgrijs, afgewezen).
- **Daan 4, letters:** de A draagt nu de paarse **puntmuts** (spits op spits, zit vast aan de letter) in plaats van de witte koksmuts, die klein als umlaut las. De S is opnieuw getekend met twee omkrullende uiteinden (`.XXX.` / `XX..X` boven, `X..XX` / `.XXX.` onder): de platte bovenkant gaf de 5. Veermuts één pixel naar het midden. Op 120 x 45 en 184 x 69 lees je HATS (GEZIEN, `vergelijk-v5-klein.png`).
- **Daan 5, goud binnen het beeld:** minstens 30 px van de rand op alle vier (tabel). De losse munt rechts op header en main is weg, want die liep tegen de rand.
- **Kan 6:** de held draagt overal de rode hoofdband (geen hoed uit de toren). Op staand en library staat geen held: daar is geen ruimte naast Gloop en zijn schat zonder de figuren weer klein te maken.
- **Kan 7:** `logo-1280.png` bijgesneden tot 16 px lucht boven en onder (1280 x 617). Het gaatje in de A laat ik open: dat is de binnenkant van de letter, net als bij elke A; dicht maakt hem weer een blok.
- **Rijen naast de toppers** (vers via de winkel van Steam, 10 nov): `vergelijk-v5-header.png`, `vergelijk-v5-klein.png`, `vergelijk-v5-library.png`, `vergelijk-v5-main.png`. Eerlijk oordeel: in de header- en kleine rij zijn we niet meer de zwakste (groot logo, warm, de grap met de hoeden leest). In de library-rij houdt Gloop nu stand naast Rusty. Op main blijven de geschilderde toppers rijker; wij winnen op het idee en de herkenbaarheid, niet op detail.
- Nog open: kan 7 uit keuring 1 (goudhoop als croissant), kan 8 (hero rijker).
- **Later in run 6, kan 7 (croissant):** de goudhoop in het spel zelf (`kunst/schat.png`) is nu een hoop losse munten; header, main, staand en hero zijn opnieuw gemaakt met dat plaatje, dus ze blijven eerlijk. Op de hero is alleen de schat veranderd. Voor en na: `ontwerp/steam/mila/schat-voor-na-10x.png`.

## Versie 6 (Mila, 10 nov ±03:55 NL): keuring 4 van Daan
- **Moet 1, staand:** het lichte steentje onderaan was een vloertegel met een kiezel die de onderrand afsneed. Nu krijgt elke vloertegel die door de onderrand gaat een tegel zonder steentje (`dicht()` in `bron/maak_capsules.py`). Zelfde regel lost **kan 3** op main op, en ook op de header. Bekeken met Read: de onderrand is rustig.
- **Kan 2, broodje:** vier munten steken nu boven de omtrek van de goudhoop uit, twee rechtop op de flanken en twee plat. De gladde boog is gebroken; vergroot lees je losse munten op een hoop (GEZIEN). Het plaatje van het spel zelf is niet veranderd; het zijn dezelfde munten als in `hol.gd`, anders neergelegd.
- **Kan 4, library:** muur en vloer op halve maat (schaal 10) achter een scherpe Gloop op schaal 20. De stenen zijn nu scherp en rustig, Gloop springt er meer uit. Waarom: zo voelt het als diepte in plaats van een wazige vlek.
- Hero, klein en logo niet veranderd.

## Versie 7 (Mila, 10 nov ±05:50 NL): eerste vijf schermafbeeldingen uit de echte build
- **Nieuw feit uit de docs** (`partner.steamgames.com/doc/store/assets/standard`, met curl gelezen): schermafbeeldingen tonen *alleen gameplay*, geen marketingtekst of beschrijving. **Besluit: geen tekst in onze schermafbeeldingen**, ook geen "actual size". Waarom: anders keurt Valve de pagina af, en het beeld kan het zelf zeggen.
- **Opmaak** (`bron/maak_schermen.py`): boven een stuk van de strook 6x vergroot over de hele breedte (hele schaal, elke spelpixel 18 x 18), onder dezelfde opname op ware grootte boven een kale taakbalk, met een gouden vergrootkader dat naar boven wijst. Zo zie je in één keer hoe klein het echt is en wat er gebeurt. De doorzichtige lucht (zwart in de opname) wordt de achtergrond.
- **Vijf schermen** in `schermen/` (1920 x 1080), allemaal uit frames van de film van main (run 42755272547, tak `schermen`), niets bijgetekend: (1) `scherm-1-val` Kees in de put, munten vliegen naar de schat; (2) `scherm-2-toren` Gloop met kroon en emmer; (3) `scherm-3-plat` Gloop plat, zijn hoeden naast hem, de Hoard-Toucher aan de schat; (4) `scherm-4-wrok` Bram de bard terug met zijn onweerswolkje; (5) `scherm-5-afgerekend` Bram zakt met een poef in zijn eigen put. Alle vijf bekeken met Read.
- **Eerlijk, wat nog beter moet:** de frames komen uit de GIF (256 kleuren), dus de gloed rond fakkels heeft lichte banden. Olaf levert dezelfde momenten als PNG (vraag in `platformen/steam/taken.md`), dan maak ik ze opnieuw met hetzelfde script. Nog geen scherm van het hol na lang spelen (moment 5 uit punt 6) en nog geen Big of Royal Gloop in beeld; die komen zodra ze in de build zitten.
- **Naast de toppers** (`vergelijk-schermen-toppers.png`, eerste scherm van Rusty's Retirement en Ropuka's Idle Island vers uit de winkel-API, op duimnagelmaat): onze figuren lezen klein het best (Gloop met hoeden, de held aan de schat); Rusty's toont een vol bureaublad waarin het spel klein blijft. Eerlijk: Ropuka's is mooier en lichter (geschilderd, blauwe lucht); wij zijn donkerder. Kan later: één scherm met de lichte lucht van een echt bureaublad boven de strook.
