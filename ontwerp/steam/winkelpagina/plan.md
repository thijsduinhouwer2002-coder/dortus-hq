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

## 3. Logo (versie 1, gemaakt 9 nov)
- Eigen pixelletter in hetzelfde spelpixelrooster als het spel. **HATS** groot in goud (de kleur van de schat), **OF THE FALLEN** kleiner in muntgroen (de kleur van Gloop). Dikke bijna zwarte pruimrand, zodat het op elke achtergrond leest.
- **Op elke letter van HATS staat een echte hoed uit het spel**: kroon op de H, koksmuts op de A, pan op de T, veermuts op de S. De letters zijn zelf ook opgegeten helden. Dat is de grap die je in 120 x 45 nog ziet.
- Maker: `bron/maak_capsules.py` (functie `logo()`), leest alleen de echte plaatjes uit `producten/steam-hol/godot/kunst/`.

## 4. Stand per bestand
| Bestand | Stand | Wat nog |
|---|---|---|
| `header-920x430.png` | v1 | logo leest sterk, ook verkleind naar 292 breed (GEZIEN). **Te zwak: Gloop met zijn toren is te klein en de hoedenberg leest als puin.** v2: Gloop en toren 2x zo groot als ingezoomd middelpunt (eerlijk: zelfde tekening, hele schaal), minder dingen, één bange held met een pan. |
| `klein-462x174.png` | v1 | op 120 x 45 lezen HATS, de kroon en OF THE FALLEN (GEZIEN). Gloop rechts valt weg: v2 alleen het logo met de hoeden, of Gloop groter in plaats van de lucht. |
| main, vertical, library, hero, logo | nog niet | uit dezelfde maker zodra header v2 staat |
| 5 schermafbeeldingen 1920 x 1080 | nog niet | van Olaf uit de echte build (strook op 160 px op een rustig bureaublad, plus een ingezoomd stuk ernaast), zie stijl.md punt 5 |
| trailer 30 tot 60 s | nog niet | eerste 3 s: een held loopt binnen, Gloop eet hem, zijn hoed vliegt op de toren. Opname van de demo-modus van Olaf |
| teksten, tags, prijs, skins en DLC | Sanne schrijft mee | voorstel prijs en DLC: hoeden-skins passen precies op de haak |

## 5. Eerlijk
Alles wat erop staat zit in het spel: 10 hoedsoorten (held_hoeden.png), hooguit 4 hoeden op Gloops hoofd en de rest op de hoedenberg (slijm.gd, `OP_HOOFD`, `berg()`), het boze wolkje en het uitroepteken (tekens.png), ingang, fakkels, schat. De lucht met sterren is versiering voor de capsule; in het spel ligt de strook op je bureaublad.
