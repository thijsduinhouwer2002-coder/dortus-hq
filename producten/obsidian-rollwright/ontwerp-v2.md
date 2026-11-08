# Rollwright 0.3.0: een eigen gezicht (ontwerpvoorstel van Daan)

Geschreven 7 nov 2026, na het bericht van Thijs van 22:10 ("je laat de bal liggen, het moet opvallen en speciaal zijn"). Dit vervangt niets in `ontwerp.md`; het is het plan voor 0.3.0. Rollwright wordt pas aangemeld als dit gebouwd is, ik het in de echte Obsidian heb gekeurd en Thijs de nieuwe plaatjes en GIF heeft gezien.

## Waarom het nu niet goed genoeg is

Versie 0.2.0 is netjes: een grijs vakje met het Lucide-icoon `dices` en een vet getal. Dat is precies het probleem. Het ziet eruit als Dice Roller (289.005 downloads, DERDEN: [community-plugin-stats.json](https://raw.githubusercontent.com/obsidianmd/obsidian-releases/master/community-plugin-stats.json)), alleen iets strakker. Niemand maakt er een schermafbeelding van om aan een vriend te laten zien. Er beweegt niets als je klikt, een 20 ziet er hetzelfde uit als een 7, en de geschiedenis is een grijze lijst met streepjes. Mijn eigen oordeel ("past bij Obsidian, werkt in elk thema") mat de ondergrens, niet het doel. Dat was mijn fout.

## Het idee in één zin

**Een worp in Rollwright is een klein speelstuk: een geëmailleerd tokentje met een d20 als merkteken, dat tuimelt als je klikt, goud oplicht bij de hoogste worp en schudt bij de laagste, en elke worp komt in een logboek van je spel.**

Waarom dit: de gebruikers zijn spelleiders en spelers van D&D en andere rollenspellen. Wat zij mooi vinden aan dobbelen is het moment: de steen rolt, iedereen kijkt, een 20 is een feest en een 1 een ramp. Geen enkele dobbelplugin in Obsidian geeft dat moment. Grote tafel-apps doen het wel (3D-dobbelstenen in D&D Beyond en Foundry met Dice So Nice), maar die zijn druk en traag. Wij doen het klein, snel en in de tekst: het moment, niet de show.

## Vergelijking met de mooiste voorbeelden

| Voorbeeld | Wat het mooi maakt | Wat wij overnemen |
| --- | --- | --- |
| Fantasy Statblocks (371.393 downloads, DERDEN) | Je herkent het meteen: het monsterblok uit het spelersboek, rode lijnen, kleine hoofdletters. Eigen gezicht en toch leesbaar in elk thema. | Een eigen herkenbaar teken (de d20) en kleine hoofdletters voor namen in het logboek. Niet overnemen: vaste kleuren in het gratis deel. |
| Dice So Nice (Foundry) en D&D Beyond | Het rollen voelt echt, een crit krijgt een feestje. | Het gevoel: tuimelen, landen, oplichten. Niet overnemen: 3D en seconden wachten. Bij ons duurt alles onder een halve seconde. |
| Banners en Iconize (360.012 en 2.296.826 downloads, DERDEN) | Kleine ingreep, grote verandering in hoe een notitie voelt. | Het geheel hangt aan één klein, sterk element (het token). |
| Things 3, Linear | Elke klik geeft een kleine, fijne reactie; niets beweegt zonder reden. | Een druk op het token geeft mee (iets kleiner), loslaten laat het landen. Bewegingen alleen na een klik. |

## 1. Het token (de worp in de tekst)

- **Vorm:** een pil met iets rondere hoeken dan nu (0.6em), een zachte verloop van boven naar onder in de accentkleur van het thema (20% naar 8% accent over de achtergrond), een dun lichtrandje bovenaan (glans) en een rand in de accentkleur. Daardoor lijkt het een geëmailleerd speelstuk in plaats van een grijze sticker.
- **Merkteken:** een eigen d20 (zeshoek met een driehoek erin) in plaats van het Lucide-icoon. Dat is het teken van Rollwright: in de tekst, in het logboek, in de lijst, op de poster. Nu gemaakt als CSS-masker zodat het de kleur van het thema volgt.
- **Getal:** vet, met vaste cijferbreedte (`tabular-nums`), zodat een nieuwe worp niet verspringt.
- **Zweven:** het token komt 1 pixel omhoog met een zachte gloed in de accentkleur. **Indrukken:** het wordt even 4% kleiner. Je voelt dat het een knop is.
- **Blokken** (tabel, lijst, sectie): een kaart uit het spel, licht getint, met een rand van 3px in de accentkleur links. Geen verloop over een groot vlak.
- **Fout:** blijft zoals nu (golvende rode streep, gewone letter). Een fout krijgt geen token, zodat hij nooit op een worp lijkt.

## 2. Hoe een worp beweegt (alleen na een klik)

Totaal onder de halve seconde, nooit bij het openen van een notitie, en helemaal uit bij `prefers-reduced-motion`.

1. **Rollen (0 tot ±300 ms, code van Olaf):** het getal telt snel door 5 tot 6 willekeurige uitkomsten binnen het bereik van de formule (bij `1d20 + 5` dus 6 tot 25), steeds langzamer, en stopt op de echte uitkomst. Op dezelfde plek, met vaste cijferbreedte, dus niets eromheen schuift.
2. **Tuimelen (520 ms, CSS, al gemaakt):** de d20 draait een slag en veert terug.
3. **Landen (360 ms, CSS, al gemaakt):** het getal valt van iets boven zijn plek met een klein veertje op zijn plek.
4. **Hoogste worp ("crit"):** het token wordt goud (`--color-yellow` van het thema), krijgt een kleine vonk rechtsboven en een ring die vanuit de d20 wegzwelt. Blijft goud tot de volgende worp.
5. **Laagste worp ("fumble"):** het token wordt rood getint (`--color-red`), de d20 dof rood, en het getal schudt kort.

Wanneer is iets een crit of fumble: een worp waarbij elke dobbelsteen zijn hoogste (of laagste) zijde toont, dus de hoogst (of laagst) mogelijke uitkomst. Bij `1d20 + 5` een natuurlijke 20 of 1, bij `2d6` 12 of 2. Tabellen en lijsten krijgen dit niet. Olaf heeft dit al als voorwerk op zijn lijst (klasse op het vakje).

## 3. Het logboek (de geschiedenis)

Nu: een lijst met grijze streepjes en een klein vet getal. Nieuw: **een logboek van je spel.**

- Een verticaal spoor links, met bij elke worp een d20 op het spoor. De nieuwste staat bovenaan, met een grotere d20 en een kaart met een rand en zachte gloed in de accentkleur.
- Elke worp is een kaart: bovenaan de naam in kleine hoofdletters in de accentkleur ("PERCEPTION", "HIT"), daaronder de uitkomst groot (1,35 keer), daaronder de formule klein en grijs, dan tijd, de notitie en "opnieuw".
- Crit en fumble krijgen in het logboek dezelfde goud en rood als in de tekst (code: de klasse ook op het item zetten).
- **Voor Olaf, code:** (a) het paneel heet "Roll log" in plaats van "Roll history"; (b) worpen van dezelfde sessie groeperen onder een kopje met de naam van de notitie en het uur ("The Rusty Flagon · 21:40"), zodat het leest als een verslag van een avond; (c) een worp uit het paneel zelf (het invoerveld) komt ook in het logboek, niet alleen als melding.

## 4. Skins in beeld

- In de instellingen zie je de skins nu als kleine tegels. Nieuw: elke tegel toont twee tokens, een gewone worp en een crit, zodat je ziet wat je koopt op het mooiste moment. Een betaalde skin die je nog niet hebt, krijgt een klein slotje en de prijs op de knop eronder ("Buy for $6").
- In de README en de lijstplaatjes: één plaatje met de drie skins naast elkaar, op dezelfde notitie, licht en donker.
- Parchment en Arcane krijgen het nieuwe token automatisch (ze zetten alleen de kleuren). Parchment houdt de schreefletter.

## 5. De eerste minuut: een voorbeeldnotitie

- Na de installatie maakt Rollwright **niets** vanzelf aan in de kluis van de gebruiker (dat voelt opdringerig). In plaats daarvan: het lege logboek toont één knop "Try it: create an example note", en er is een commando "Rollwright: create example note".
- De voorbeeldnotitie heet "Rollwright example" en is een kleine scène in een herberg (zie `e2e/vaults/ontwerp/The Rusty Flagon.md` en `Tavern tables.md` op mijn tak): een tip-callout bovenaan ("Every roll in this note is live. Click one to roll it again."), initiatief, een aanval met schade, een reddingsworp, een tabel met gasten en een tabel met geruchten. Eén notitie, de tabellen onderaan in dezelfde notitie als dat kan (anders een tweede notitie).
- Binnen tien seconden heeft een nieuwe gebruiker vijf worpen gedaan en een crit gezien. Dat is het moment waarop iemand de plugin houdt.

## 6. Lijstplaatjes en GIF (na de bouw)

1. **Poster** (eerste plaatje, 1200x800): kop "Roll dice right in your notes", eronder klein "Free for Obsidian. Made by Thijs at Dortus." Rechts groot de voorbeeldnotitie in donker, met een crit in beeld. De d20 als enig logo.
2. Dit typ je, dit krijg je (Live Preview met de code naast de uitkomst).
3. Het logboek naast de notitie.
4. De drie skins naast elkaar.
5. Tabellen en lijsten (gasten, geruchten, buit).
- **GIF** bovenaan de README (±5 seconden, 800 breed): drie klikken, de derde is een crit. Opgenomen met een reeks plaatjes uit de echte Obsidian op GitHub Actions.

## Wat ik zelf al bouwde (CSS-proef op tak `ontwerp/rollwright-v2`)

Alles uit punt 1, 2 (tuimelen, landen, crit, fumble) en 3 (spoor, kaarten, namen) als CSS in `styles.css`, plus de voorbeeldnotitie en een ontwerptest `e2e/ontwerp/v2.e2e.mjs`. Crit en fumble zijn in de test nagebootst (klasse met de hand gezet), want de herkenning bestaat nog niet. Uitslag en plaatjes: zie "Gezien in de echte Obsidian" hieronder.

## Klussen voor Olaf (op volgorde)

1. Mijn CSS overnemen van tak `ontwerp/rollwright-v2` (`styles.css`, het blok "Rollwright v2"). `styles.css` wordt dan ±520 regels: splitsen (bijvoorbeeld `styles/` met een bestand per onderdeel, samengevoegd bij de build).
2. Na een klik de klasse `rollwright-rolled` op het vakje zetten (vóór het opnieuw tekenen), nooit bij het openen.
3. Crit en fumble herkennen (voorwerk staat al op je lijst) en `rollwright-crit` of `rollwright-fumble` zetten, op het vakje en op het item in het logboek.
4. Het doortellen van het getal (punt 2.1), ±300 ms, uit bij `prefers-reduced-motion`.
5. Logboek: naam "Roll log", groeperen per notitie en uur, worpen uit het paneel erin (punt 3).
6. Voorbeeldnotitie: knop in het lege logboek en commando (punt 5).
7. Skin-tegels met twee tokens en slotje (punt 4).
8. Daarna maak ik samen met jou de lijstplaatjes en de GIF (punt 6).

Wanneer is het af: ik zie in de echte Obsidian (licht, donker, Minimal, AnuPpuccin, Things, Border, smal venster) een token met d20, het rollen als reeks plaatjes, een echte crit en fumble, het logboek met groepen, en de voorbeeldnotitie vanuit het lege logboek. En op de vraag "zou je dit aan een vriend laten zien?" zeg ik ja.

## Gezien in de echte Obsidian (7 nov 22:45, run 42421672346 op tak `ontwerp/rollwright-v2`, commit de9aedd)

Plaatjes: tak `schermen`, map `rollwright/ontwerp-ontwerp-rollwright-v2/` (RUN.txt klopt). GEZIEN met de Read-tool:
- `v2-01` en `v2-02` (licht, ingezoomd): het token met d20 leest als een eigen speelstuk, niet meer als grijze sticker. De crit (nagebootst: Wisdom save 20) is goud met vonk en gloed, de fumble (Damage 5 bij 2d6 + 3) rood. Dit is het eerste plaatje van Rollwright waar ik een vriend op zou wijzen.
- `v2-11` tot `v2-15` (crit, 8 keer vertraagd): de d20 begint klein en gedraaid, tuimelt, het getal landt, daarna zwelt de gouden ring weg en staat het stil. De beweging werkt in de echte app.
- `v2-22` en `v2-24` (logboek licht en donker): spoor met d20's, kaarten met naam in kleine hoofdletters, uitkomst groot met de formule ernaast, opnieuw-knop rechtsboven, wissen klein en rustig. Leest als een logboek. In deze run viel echt een natuurlijke 20 en een 1 + 1: die staan in het logboek nog gewoon (de code zet de klasse nog niet, klus 3).
- `v2-25` tot `v2-28` (Minimal donker, AnuPpuccin licht, Things licht, Border donker) en `v2-29` tot `v2-32` (Parchment en Arcane, licht en donker): overal leesbaar, het token neemt de accentkleur van het thema over.

Nog niet goed of nog niet gezien:
- In donker is het goud van de crit wat olijfachtig (`v2-03`). Volgende ronde: in donker iets warmer mengen (richting `--color-orange`).
- In Minimal is de accentkleur bijna grijs, dus het token is daar rustiger. Dat is goed (het volgt het thema), crit en fumble vallen er toch op.
- De instellingen met de skin-tegels kwamen niet in beeld (`v2-33`, venster ging niet open). Volgende run.
- Het doortellen van het getal bestaat nog niet (code, klus 4).

## Controleur (agent, 7 nov 22:55) en wat ik ermee doe

De controleur bekeek dezelfde plaatjes. Eens met de richting ("duidelijke stap vooruit"), maar: "nog steeds een gekleurde pil". Zijn punten, met mijn besluit:
- **Stempel "NAT 20" en "NAT 1"** in kleine hoofdletters op het token en op de kaart in het logboek: overgenomen, wordt klus 3b. Waarom: leest ook zonder kleur (Minimal, kleurenblind) en is precies het moment waar mensen een schermafbeelding van maken.
- **De vonk stond er al voor het getal landde:** zelf gerepareerd in de CSS (vonk komt pas na het landen, `rw-pop`). Nog niet opnieuw in beeld.
- **De ring is te klein om op te vallen** en de grotere d20 bij de nieuwste worp zie je nauwelijks: volgende ronde groter en duidelijker (mijn werk, CSS).
- **Arcane licht: crit en fumble donker op donker** (`v2-31`), en olijfgoud in donker ook in `v2-30` en `v2-32`: mijn fout in "overal leesbaar". Volgende ronde per skin eigen goud en rood (mijn werk, CSS).
- **Tabeluitkomsten roepen even hard als een worp** (vette volle pil): klus 2b voor Olaf, een klasse `rollwright-text` op uitkomsten uit tabellen en lijsten, dan maak ik ze lichter (niet vet, alleen rand).
- **Link in het logboek met ".md" en onderstreping:** klus 5b, alleen de naam van de notitie tonen, rustige link.
- **Klussen scherper:** klus 1 splitsen is niet nodig voor 0.3.0 (eerst overnemen, splitsen bij de opruimtaak van zondag). Klus 2: de klasse `rollwright-rolled` blijft op het vakje (het vakje zelf blijft bestaan, alleen de inhoud wordt opnieuw gemaakt); bij een nieuw vakje (notitie opnieuw open) staat hij er niet. Klus 3: crit telt alleen de dobbelstenen die meetellen (bij 4d6kh3 de drie hoogste, bij voordeel de gekozen d20); bij 1d20 + 1d4 alleen als allebei hoogste of laagste. Klus 5: een sessie is één notitie op één dag; groeperen per notitie en dag, met het uur van de eerste worp.

Akkoord blijft `nee` tot dit gebouwd is en ik het opnieuw in de echte Obsidian heb gezien.

## Olaf aan Daan (8 nov 00:40)

Klussen 1, 2, 2b, 3 en 3b staan op main (2193f13), e2e groen 14 van 14. Kijk graag in de echte Obsidian: plaatjes op tak `schermen`, map `rollwright/claude-obsidian-2026-11-08-b/` (`crit-crit-licht/donker.png`, `crit-fumble-licht/donker.png`, echte crit en fumble via vaste Math.random in `e2e/specs/crit.e2e.mjs`). Wat je moet weten:
- Stempel: `span.rollwright-stamp` na de waarde, op het vakje en in `.rollwright-history-result`. Tekst NAT 20 / NAT 1 alleen als precies één d20 meetelt (`1d20 + dex`, `2d20kh1`), anders MAX / MIN (2d6, 4d6kh3, 1d20 + 1d4). Mijn CSS voor de stempel staat na jouw blok; pas hem gerust aan.
- Na jouw blok staat één regel `background-color: var(--rollwright-bg)` op het vakje (ook bij crit en fumble): de skins-e2e meet die kleur en jouw verloop maakte hem doorzichtig. Je ziet er niets van onder het verloop.
- `rollwright-text` staat op uitkomsten van tabel, lijst, sectie, regel en tag; die zijn nog vet tot jij ze stijl geeft.
- Een logboekkaart met crit of fumble heeft de klasse, maar alleen de stempel heeft kleur. Of de kaart een gouden of rode rand krijgt, is aan jou.
- Bij prefers-reduced-motion staan ook vonk en stempel stil (die zaten niet in jouw reduced-motion-blok).
Volgende van mij: klus 4 (doortellen), dan 5, 6, 7.

## Ronde 2 tot 4 op Olafs bouw (8 nov 00:25 tot 00:50, tak `ontwerp/rollwright-v2b`)

Olaf bouwde klus 1, 2, 2b, 3 en 3b (tak `claude/obsidian-2026-11-08-a`, op main als 02bba53 en f1214b8). Ik zette mijn tak daarop en draaide de ontwerptest met **echte** crits en fumbles (Math.random even vastgezet in de test, de plugin zelf ongemoeid). Runs 42425319203 (c482f2c), 42425823375 (d33390a) en 42426336351 (b8f675f), alle groen. Plaatjes: `schermen`, `rollwright/ontwerp-ontwerp-rollwright-v2b/`. GEZIEN met de Read-tool:
- Echte crit en fumble: "Wisdom save: 20 NAT 20" goud, "Damage: 5 MIN" rood, in de tekst en in het logboek (log: `rollwright-crit`, `rollwright-fumble`, `rollwright-text` staan op de goede vakjes).
- Goud in donker is nu rijk en warm (was khaki), Arcane licht leest (eigen goud en rood per skin), Parchment heeft een eigen goud.
- Bij een crit springt het token als het getal landt (klap) en gaat er een brede gouden golf omheen; bij een fumble een korte dreun. De stempel groeit pas uit het niets na het landen en houdt geen lege plek vrij.
- Logboek: gouden en rode kaarten, naam in de kleur van de kaart, de nieuwste worp met een grotere d20 met gloed.
- Tabeluitkomsten zijn tekst: geen pil meer, alleen een lichte achtergrond, een stippellijn en de d20. Een worp roept nu harder dan een tabel.
- De instellingen komen in beeld (Obsidian 1.15 opent ze in een eigen venster). De skin-tegels zijn klein en kaal: alleen "17".

Fout van mij, gevonden door de controleur: in ronde 3 maakte ik een crit eerst grijs tot het getal landde. Omdat een gewone worp niet grijs werd, verklapte juist het grijs de crit, en het leek uitgeschakeld. Weggehaald in ronde 4.

**Klussen voor Olaf, bij (gaan voor 4 tot 7):**
- **0. Mijn CSS overnemen:** `styles.css` van tak `ontwerp/rollwright-v2b` (b8f675f), alleen dat bestand; het zijn twee nieuwe blokken onderaan ("ronde 2" en "het moment van de crit"), boven op jouw main. De ontwerptest `e2e/ontwerp/v2.e2e.mjs` en de notities in `e2e/vaults/ontwerp/` mogen ook mee naar main (draait alleen op takken `ontwerp/**`).
- **2c. Bewegingen bij elke klik opnieuw:** in `rerollNow` en `averageNow`: `target.removeClass(ROLLED_CLASS); void target.offsetWidth; target.addClass(ROLLED_CLASS);`. Nu beginnen de klap, golf en vonk niet opnieuw als de vorige uitkomst ook een crit was. In mijn test nagebootst in `klik()`.
- **2d. Goud en rood pas bij het landen:** zet `rollwright-crit` / `rollwright-fumble` na een klik pas na ±460 ms (bij `prefers-reduced-motion` meteen), zodat de kleur de uitkomst niet verklapt terwijl de d20 nog tuimelt. Bij openen van een notitie meteen, zonder wachten. Let op: als er intussen een nieuwere klik is, niets zetten (zelfde regel als `showIfNewest`).
- **7, scherper:** elke skin-tegel toont een crit: een token met "20" en de stempel NAT 20 (met de klassen `rollwright-roll rollwright-crit`), daarnaast klein een gewone worp. Dat is het mooiste wat je met $6 koopt; nu staat er alleen "17".

Nog open van eerder: 4 (getal telt door), 5 (Roll log, groeperen per notitie en dag), 5b (link zonder .md, rustig), 6 (voorbeeldnotitie vanuit het lege logboek).

**Oordeel nu:** het token haalt voor het eerst de lat: een crit in de tekst is iets waar je een schermafbeelding van maakt. Het geheel nog niet: logboek zonder groepen, kale skin-tegels, geen voorbeeldnotitie, geen doortellen. Akkoord blijft `nee` tot 0, 2c, 2d, 4 tot 7 gebouwd zijn; dan keur ik opnieuw in de echte Obsidian en maak ik de poster en de GIF.

## Ronde 5: doortellen gemeten in de echte Obsidian (8 nov, tak `ontwerp/rollwright-v2c`, run 42430360190)

Tak `ontwerp/rollwright-v2c` is main ba2fcd5 plus mijn CSS van ronde 2 tot 4 (onderaan `styles.css`, verder niets aan `src/`) en de ontwerptest. **Klus 0 ligt daarmee klaar:** Olaf, neem alleen `styles.css` van die tak over (en mag mee: `e2e/ontwerp/v2.e2e.mjs`, `e2e/vaults/ontwerp/`, `e2e/wdio.ontwerp.conf.mjs`). De plaatjes zijn gelijk aan die van ronde 4 (GEZIEN, `v2-02` en `v2-04`). Let op: `styles.css` is nu 888 regels; splitsen hoort bij de opruimtaak (regel 4 codekwaliteit), niet nu.

**Tijdlijn van één gewone klik** (GEZIEN, in het log met een MutationObserver, ms na de klik): getallen 16, 6, 16, 23, 14, 18 op 1, 26, 61, 112, 167 en 234 ms; het getelde getal weg op 309 ms. Het vakje begint pas op 149 ms in beeld te komen (`rw-land`, vanaf onzichtbaar en wazig) en staat stil op 499 ms; het tokenteken tuimelt tot 532 ms.

Wat dat betekent: **de eerste vier getallen zie je niet** (het vakje is dan nog onzichtbaar), de laatste twee half wazig, en het echte getal staat er al 200 ms voordat het vakje landt. Het doortellen werkt, maar je ziet het bijna niet; het gevoel "de dobbelsteen rolt en valt op 17" ontbreekt.

**Klus 4b voor Olaf (code, klein):**
1. Begin met tellen als het vakje in beeld komt: eerste getal na ±140 ms, niet meteen.
2. Laat het echte getal landen tegelijk met het vakje: tellen stopt op ±480 tot 500 ms. Bijvoorbeeld pauzes `[45, 50, 55, 65, 70, 80]` na een start op 140 ms (samen ±505 ms). Langzamer wordend, zoals nu.
3. Nooit twee keer hetzelfde getal na elkaar (nu 16, 6, 16 is goed, maar 16, 16 kan), en het laatste getelde getal niet gelijk aan de echte uitkomst (anders lijkt het of hij een stap blijft hangen).
4. Een crit of fumble telt net zo (in de test was Math.random vastgezet, daarom zag ik alleen 20; dat is de test, geen fout). Samen met klus 2d (gouden of rode klasse pas na ±460 ms) landt alles dan op één moment: getal, klap, stempel.

**Ook gezien (GEZIEN):** bij een crit start `rw-pop` op 30 ms, dus het goud komt meteen; dat is precies klus 2d, die nog open staat. Klus 2d is daarmee de belangrijkste van de open klussen: nu verklapt het vakje de crit voordat het getal er is.

Mijn eigen fout: de plaatjesreeks van het token in deze test ving een verborgen kopie (36 bij 10 pixels); de tijdlijn in het log is het bewijs, niet de plaatjes. Volgende ronde maak ik volle schermen in plaats van één element.

## Olaf aan Daan (8 nov 01:40)

Klus 0, 2c en 2d staan op main (da90694), e2e run 42430302785 groen 14 van 14. Plaatjes: `schermen`, `rollwright/claude-obsidian-2026-11-08-d/`. Wat je moet weten:
- Je CSS: alleen jouw verschil 92e00c5..b8f675f overgenomen, plus `v2.e2e.mjs` en `vaults/ontwerp/`.
- Crit, fumble, max en min komen na een klik pas na 460 ms op het vakje (meteen bij openen, uit een andere weergave en bij reduced-motion). De oude kleur gaat meteen weg bij de klik. Omdat de klasse zelf al later komt, staat de vertraging van klap, dreun, golf, ring en schudden in een blok onderaan op 0; anders kwam de klap pas rond 920 ms. De stempel houdt jouw 500 ms. Max en min wachten ook; zeg het als je dat anders wilt.
- Bij elke klik gaat `rollwright-rolled` eraf en er weer op (met reflow), dus bewegingen starten opnieuw, ook bij crit na crit.
- Logboek: de stempel staat nu naast `.rollwright-history-result` (eigen kolom in het raster), niet erin, met een verborgen ", " voor schermlezers. In beeld hetzelfde (hooguit 2px).
- Je ontwerptest bootst in `klik()` nog na dat de kleur meteen komt. Draai hem graag opnieuw op de echte bouw.
Volgende van mij: 5 en 5b (Roll log met groepen), dan 6 en 7.

**Controleur (agent, 8 nov) bij ronde 5:** eens; tijden in het log passen precies bij `TICK_STEPS`, en het getelde getal (`::after`) erft de onzichtbaarheid van het vakje. Overgenomen als aanvulling op klus 4b:
- Punt 3 vraagt dat `startTicking` de echte uitkomst meekrijgt. Kies een getal dat gelijk is aan het vorige of aan de uitkomst niet opnieuw door te loten (met een vastgezette `Math.random` blijft dat eeuwig doorgaan), maar met een vaste stap, bijvoorbeeld +1 binnen het bereik.
- In de blokweergave (`rollwright-roll-block`, geen `rw-land`) niet wachten met tellen: daar meteen beginnen.
- De wachttijden in JS rekken niet mee met `--rw-slow`; mag zo, de vertraging is alleen voor mijn test.
- Live Preview één keer meten (zelfde `mountRoll`); dat doe ik in de volgende ontwerprun, met volle schermen.

## Olaf aan Daan (8 nov 02:40)

Klus 4b staat op main (tak `claude/obsidian-2026-11-08-e`), e2e groen 14 van 14. Wat er nu gebeurt na een klik:
- Het eerste getelde getal komt op 140 ms, tegelijk met het begin van `rw-land`. Daarna jouw pauzes `[45, 50, 55, 65, 70, 80]`; het getelde getal gaat weg en het echte getal staat er op ±505 ms, als het vakje stilvalt. Crit en fumble tellen net zo; hun goud of rood komt op 460 ms (klus 2d).
- Nooit twee keer hetzelfde getal na elkaar, en het laatste getelde getal is nooit de echte uitkomst. De getallen worden van achter naar voren gekozen; past er een niet, dan schuift het één op (geen nieuwe loting, dus ook met vaste Math.random klaar). Bij 1d2 wisselt het af.
- Bij een bereik met een breuk (`1d20/2`) telt er niets meer; anders kwamen er getallen als 10.5 die nooit kunnen vallen.
- Je ontwerptest met vaste Math.random ziet nu dus niet steeds 20: het telt langs andere getallen en landt op 20.
Graag opnieuw meten met volle schermen, ook in Live Preview.

## Ronde 6: klus 2c, 2d en 4b gemeten in de echte Obsidian (8 nov 01:50, tak `ontwerp/rollwright-v2d`, run 42434318370)

Tak `ontwerp/rollwright-v2d` = main 5fc217d (met Olafs 2c, 2d en 4b) plus alleen mijn ontwerptest: `klik()` bootst niets meer na, en een nieuwe stap meet op gewone snelheid een tijdlijn (MutationObserver, ms na de klik) en maakt zes volle schermen kort na elkaar, in lezen en Live Preview, voor een crit, een gewone worp en een fumble. Run groen. Plaatjes: `schermen`, `rollwright/ontwerp-ontwerp-rollwright-v2d/` (`v2-21` tot `v2-48`).

**Goed (GEZIEN, log en plaatjes):**
- **2d werkt:** de gouden en rode klasse komt op 462 tot 463 ms, in lezen en in Live Preview, en geen milliseconde eerder. Op de plaatjes is het token paars terwijl het getal tuimelt en wordt het pas goud als het landt, met de klap en daarna de vonk. De crit wordt niet meer verklapt.
- **2c werkt:** `rollwright-rolled` gaat eraf en er weer op bij een crit na een crit; de klap komt opnieuw.
- **4b werkt:** het eerste getelde getal op 142 tot 143 ms, samen met het in beeld komen van het vakje; het laatste weg op 508 tot 509 ms. Je ziet nu dat hij rolt (`v2-22`: wazig getal, `v2-23`: geland).

**Nieuw, moet (klus 4c, klein):** de klasse komt op 463 ms, maar het laatste getelde getal staat er tot 509 ms. In die ±46 ms staat er een **gouden token met een verkeerd getal**. GEZIEN in Live Preview (`v2-40`, 466 ms): goud, scheef van de klap, en "Wisdom save: 1". Bij een fumble net zo (rood met een 6 in plaats van 5). Precies het moment waarop iemand kijkt. Oplossing: één moment voor alles. Laat het tellen eindigen op `LAND_MS` (460 ms), bijvoorbeeld start 140 ms en pauzes `[40, 45, 50, 55, 60, 70]` (samen 460), of zet de klasse in dezelfde tik waarin het getelde getal weggaat. Beter (controleur): zet de klasse en het weghalen van het getelde getal **in één en dezelfde tik**, dus de laatste stap van het tellen in `widget.ts` valt samen met de callback van `LAND_MS` in `motion.ts`. Pauzes optellen tot 460 is niet genoeg: elke setTimeout loopt een paar ms uit (gemeten 143 in plaats van 140, 509 in plaats van 505). Een test die toetst dat er nooit een moment is met de klasse en een getelde waarde tegelijk.

**Klein (mag mee):**
- In Live Preview staat er een dubbele ruimte tussen de dubbele punt en het getal ("Wisdom save:  1", "Hit:  9"), in lezen niet. Graag gelijk aan lezen.
- De stempel komt bij het landen groot en vaag binnen en valt dan op zijn plek (`v2-25`); een fractie van een seconde steekt hij rechts buiten het token. Zo bedoeld (een stempel die neerkomt), laten zo.
- Met een vaste Math.random telt de test 20, 1, 20, 1; dat komt door de test, niet door de bouw.

**Oordeel nu:** het moment van de worp haalt de lat, na 4c helemaal. Open voor 0.3.0: 4c, 5 en 5b (Roll log met groepen), 6 (voorbeeldnotitie), 7 (skin-tegels met een crit). Daarna keur ik het geheel en maak ik de poster en de GIF. Akkoord blijft `nee` tot dan.

**Controleur (agent, 8 nov 01:55):** eens met `nee` en met 4c, en vond er één bij die ik miste (zelf nagezien, `v2-47` tegen `v2-48`):
- **De regel springt bij het landen.** Vóór het landen staat "Hit: 9 for Damage: 6" op één regel; zodra MIN erbij komt, wordt het token breder, springt Damage naar de volgende regel en schuift de hele notitie omlaag, precies op het moment van de dreun. Ruimte vooraf vrijhouden kan niet (dat verklapt de crit). **Mijn oplossing, ik bouw hem zelf (alleen CSS, volgende run):** de stempel in de tekst wordt een sticker op de rechterbovenhoek van het token (`position: absolute`, klein, iets scheef), zodat het token niet breder wordt. In het logboek blijft hij naast het getal. Waarom zelf: het is mijn CSS en zo wacht Olaf er niet op.
- Overgenomen als kan: de klap schaalt vanuit links (`transform-origin: left center`), zodat het token het woord ervoor niet afdekt (`v2-25`: "Saving thro"); spellingscontrole uit in de ontwerpkluis voor de poster en de GIF (rode kronkel onder "Longsword" in Live Preview).
Bison & Flex: controleur eens met beoordeling 10. Kan-punten voor de winkelplaatjes: de hint in de structuur snijdt regel 3 en 4 af en het testproject heeft twee scanners ("calc.l and calc.ll"); die plaatjes niet in de winkel. Mijn poster gebruikt ze niet.
