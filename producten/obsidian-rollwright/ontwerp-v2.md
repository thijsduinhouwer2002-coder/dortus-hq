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
