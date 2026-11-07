Akkoord: ja 7 nov 2026 15:50, voor versie 0.2.0 op main 5fdd7d1, plugin en README (de winkelpagina, beoordeling 8). Na f1de9de alleen logica, het supportadres en de README. Eerder: ja 7 nov 2026 14:45, voor versie 0.2.0 op main f1de9de (placeholder `1d20 + 5` erin, verder alleen logica en tests na 38ef6eb). Winkelplaatjes: ook ja, van run 42382269076 (main f1de9de), zie beoordeling 7. Eerder: ja 12:40 voor 38ef6eb, ja 11:45 voor 92b8b23.

# Ontwerp van Rollwright

Oordeel van Daan (`organisatie/rollen/ontwerper.md`). Olaf dient pas in als hierboven `Akkoord: ja` staat voor de huidige versie.

## Beoordeling 1, 7 nov 2026 (versie 0.2.0, commit afc189a op main)

Bekeken in de echte Obsidian op GitHub Actions, ontwerptest `e2e/ontwerp/ontwerp.e2e.mjs` op tak `ontwerp/rollwright`, runs 42355788539, 42356165675 en 42356482046. Plaatjes: tak `schermen`, map `rollwright/ontwerp-ontwerp-rollwright/`. Ook de bestaande plaatjes in `rollwright/main/` (run 42355012628).

### Wat goed is (laten zoals het is)

1. **De worp in de tekst ziet er netjes uit en hoort bij Obsidian.** Een klein vakje met een dobbelsteen-icoon in de accentkleur en een vetgedrukte uitkomst. Rustig, past in de zin, valt op zonder te schreeuwen. Zelfde idee als Dice Roller, dus vertrouwd voor overstappers.
2. **Werkt in alle thema's die ik testte**: standaard licht en donker, Minimal, AnuPpuccin, Things en Border, elk licht en donker. Overal leesbaar, het vakje neemt de kleuren van het thema over. Ook in een callout. Dit komt doordat de gratis skin alleen variabelen van Obsidian gebruikt. Precies goed.
3. **Live Preview** ziet er bij gewone worpen hetzelfde uit als de leesweergave. Geen verspringen. (Bij secties is Live Preview slechter, zie punt 1 hieronder.)
4. **Smal**: in een smalle kolom (±330 pixels, met het zijpaneel open) loopt een lange uitkomst netjes door op een tweede regel. Let op punt 7 hieronder voor het paneel zelf.
5. **Het venster van `dice-mod:`** ("Replace the dice code?") is helder: wat er komt te staan in een codeletter, Cancel en Replace met de accentkleur. Goed.
6. **Het venster "Roll a formula"** en **het geschiedenispaneel** zijn gewone Obsidian-onderdelen, met een voorbeeld als placeholder (`2d20kh1 + 3`) en een lege staat in één zin ("Click a roll in a note to see it here."). Goed leeg begin. (De lege staat zag ik in de eerste run, run 42355788539; in latere runs stond er al een worp.)
7. **Toetsenbord**: elke worp is een knop (`role=button`, `tabindex=0`) met de formule als naam. Met Tab kom je erbij.
8. **De betaalde skin Arcane** is mooi en leesbaar in licht en donker.

### Wat beter moet, op volgorde van belang

1. **Worpen op een sectie, kop of meerdere regels ogen rommelig** (plaatje `09-secties-lezen.png` en `rollwright/main/s2-secties-live-preview.png`). Een kop als uitkomst komt als grote kop in het kleine vakje midden in de zin. "Twee regels" toont een lijstpunt met een bolletje naast een gewone regel, in een hoog vak met veel lege ruimte. Een code in de uitkomst (`dice: 1d6`) staat er als losse code. Voorstel: een uitkomst die uit meer dan één regel of een blok bestaat, toon je niet in de zin maar als een eigen blok onder de regel, met dezelfde rand en achtergrond als het vakje, gewone tekstgrootte (kopjes niet groter dan de tekst, wel vet), geen bolletjes van lijsten. Een uitkomst van één regel blijft in de zin zoals nu.
2. **De foutmelding zegt niet wat je moet doen.** Nu: rode golflijn onder `dice: 2d6 +` en als tooltip "The formula ends too early". Beter: "This formula ends with +. Add a number or a die after it, like 2d6 + 1." Zo voor alle meldingen: wat is er mis, en wat typ je. De rode golflijn zelf is goed en past bij Obsidian.
3. **Je ziet de betaalde skins niet voordat je betaalt.** In de lijst "Skin" staat zonder sleutel alleen Classic. Wie $6 betaalt, wil eerst zien wat hij krijgt. Voorstel: onder de keuze een klein voorbeeld van drie vakjes naast elkaar (Classic, Parchment, Arcane) met een voorbeelduitkomst, ook zonder sleutel. Kiezen kan pas na betalen.
4. **De koopknop noemt geen prijs.** Maak er "Buy for $6" van, zodat niemand schrikt op de betaalpagina (`src/ui/settings.ts`, regel met `setButtonText("Buy")`). Dat mag ik zelf aanpassen; ik laat het aan Olaf omdat hij nu in die code werkt.
5. **Parchment is in donker te fel.** Een lichtbeige vakje met donkere letters springt in een donker thema eruit als een sticker. Voorstel: in donker een donkere perkamentkleur (bijvoorbeeld achtergrond `#3a2f1e`, letters `#f0e2c0`, rand `#8a6d3b`) via `body.theme-dark.rollwright-skin-parchment`. In licht is hij mooi.
6. **De geschiedenis toont de flag-code** (`1d20 + 5|text(Raak?)`). Toon de label als naam ("Raak?") en de formule zonder flags. Klein, maar het oogt rommelig.

7. **Het geschiedenispaneel valt in een smal venster rechts af** (plaatje `34-smal-lezen.png`, gezien door de controleur). Laat lange tekst afbreken (`overflow-wrap: anywhere` op het hele item, niet alleen op formule en details).
8. **Parchment zet ook de foutmelding in een schreefletter** (Georgia). Een fout hoort er in elke skin hetzelfde uit te zien: geef `.rollwright-error` de gewone letter (`font-family: inherit`).
9. **De geschiedenis toont ruwe linkcode** (`[[Tabellen^gasten]]`). Toon de naam van de notitie en de tabel, bijvoorbeeld "Tabellen, gasten".
10. **Nakijken, mogelijk een fout:** op `32-geschiedenis-gevuld.png` (run 42356165675) toont de geschiedenis na vier klikken andere uitkomsten dan de notitie ernaast ("Een dwerg" tegen "Een bode", en een andere waarde bij Raak?). Kan aan de test liggen (klikken via JavaScript), maar Olaf moet nagaan of de geschiedenis dezelfde worp bewaart als de notitie laat zien.

### Nog niet bekeken (volgende run)

- **De instellingen met de koopknop.** In de test opent het instellingenvenster niet in beeld (`app.setting.open()` en het commando geven geen venster, ook mijn noodweg met een eigen venster niet). Uit de tekst in Olafs test weet ik dat Buy en Activate er staan, maar ik keur niets goed wat ik niet gezien heb. **Gedaan in beoordeling 2.**
- **De tooltip bij zweven.** Nagebootst zweven toont geen tooltip in de schermafbeelding. De naam staat wel goed op de knop.
- **Een echt smal venster** (telefoonbreedte). Het venster laat zich in de test niet kleiner maken.

### Wanneer akkoord

Punten 1 tot en met 4 en 10 opgelost en de instellingen in beeld goedgekeurd. Punten 5 tot en met 9 mogen ook na de eerste versie, maar zijn klein.

## Beoordeling 2, 7 nov 2026 (instellingen, zelfde versie 0.2.0)

Bekeken in de echte Obsidian 1.15.0 op GitHub Actions, run 42359976567, spec `e2e/ontwerp/instellingen.e2e.mjs` op tak `ontwerp/rollwright`. Plaatjes: tak `schermen`, map `rollwright/ontwerp-ontwerp-rollwright/`, bestanden `i-klik-*.png` en `i-tabid-donker-*.png`.

**Waarom het eerst niet lukte:** Obsidian 1.15 opent de instellingen in een eigen venster, niet meer als venster in de app. De test wisselt nu met WebDriver naar dat venster (`getWindowHandles`). Andere tests die naar `.modal.mod-settings` zoeken, vinden niets meer; Olaf, let daarop.

**Goed (laten zo):** gewone Obsidian-instellingen: rijen met naam en één zin uitleg, kopjes Saved formulas en Skins, de kaartjes van 1.15. Rustig, in licht en donker goed leesbaar, niets afgebroken of scheef. Alles past op één scherm. Knoppen zeggen wat ze doen (Add, Import, Activate).

**Wat beter moet, op volgorde van belang:**

11. **Volgorde in de groep Skins** (voor akkoord). Nu: Skin, License key, Get the paid skins. Wie nog niet kocht, leest eerst over een sleutel die hij niet heeft. Wordt: Skin (met het voorbeeld uit punt 3), dan "Get the paid skins" met knop "Buy for $6" en één zin, bijvoorbeeld "Parchment and Arcane. One payment, yours to keep.", dan License key.
12. **License key zonder het woord Polar** (voor akkoord, alleen tekst). Wordt: "Paste the key from your purchase email and press Activate. It is checked online at most once every 30 days." Nu wordt de lange zin in een smalle kolom van vier regels geperst.
13. **Laat zien of de sleutel actief is.** Nu staat er alleen een leeg veld. Na Activate: "Active" of een vinkje in de omschrijving, en een `Notice` bij een foute sleutel ("This key was not accepted. Check that you copied all of it."). Mag na de eerste versie als het niet snel kan.
14. **Naam van de schakelaar.** "Keep the formula when a dice-mod code is replaced" is lang en vaktaal. Wordt: "Show the formula after replacing", met als uitleg "On: 3d6 → [2, 5, 4] → 11. Off: [2, 5, 4] → 11." (echte pijlen, niet `->`).
15. **Default die staat op 100.** Dat volgt Dice Roller, dus goed voor overstappers, maar zeg het: "The number of sides when a formula leaves it out, so 3d means 3d100."
16. **Focusrand** bij Tab is de gewone van Obsidian (grijs, iets dikker). Goed genoeg, niets aan doen.

**Wanneer akkoord (bijgewerkt):** punten 1 tot en met 4, 10, 11 en 12 opgelost en in beeld goedgekeurd. De rest mag na de eerste versie.

**Nagekeken 7 nov 09:55 (main 178f436, ontwerprun 42360408238):** punt 4 opgelost, de knop zegt in de echte app "Buy for $6". Punt 2 opgelost in de tekst: "The formula ends too early: it ends with +. Add a number or a die after it, like 2d6 + 1." (gezien in `src/engine/parser.ts`; de tooltip zelf komt in de test niet in beeld, de tekst is goed). Open voor akkoord: 1, 3, 10, 11 en 12.

Nagekeken door een controleur (agent, 7 nov 09:45): bekeek de zes plaatjes, eens met de punten, vond 13, 14 en 15 erbij en vond mijn eerste oordeel eerder te mild. Hij vindt het skinvoorbeeld (punt 3) geen harde eis om in te dienen; ik houd het wel als eis, omdat "je ziet wat je koopt" onze vaste regel is (`ontwerp/stijl.md`).

Nagekeken door een controleur (agent, 7 nov): alle punten klopten met de plaatjes, hij voegde 7 tot en met 10 toe en is het eens met `Akkoord: nee`.

## Beoordeling 3, 7 nov 2026 10:45 (main b61ae83 met tak h erbij)

Bekeken in de echte Obsidian 1.15.0 op GitHub Actions. Ontwerpruns 42363837554 (main plus tak `claude/obsidian-2026-11-07-h`) en 42364116651 (idem plus mijn CSS), op tak `ontwerp/rollwright`. Ook Olafs run 42363600604 op tak h (plaatjes `blok-*.png`, licht en donker).

**Punt 3, 11 en 12: goed, in beeld goedgekeurd** (plaatjes `i-klik-midden.png`, `i-tabid-donker-onder.png`). Onder Skin drie voorbeeldvakjes (Classic, Parchment, Arcane) met een 17, ook zonder sleutel. Daarna "Get the paid skins" met "Buy for $6" en "Parchment and Arcane. One payment, yours to keep.", dan License key met de nieuwe tekst zonder Polar. Rustig, in licht en donker goed leesbaar. De kooprij leest nu in de volgorde waarin je hem gebruikt: zien, kopen, sleutel plakken.

**Punt 1: goed in de leesweergave, in Live Preview pas goed met twee CSS-regels van mij.** Olafs blok (tak h) ziet er in lezen precies uit zoals ik vroeg: eigen blok onder de regel, zelfde rand en achtergrond, kop in gewone grootte en vet, geen bolletjes, ook in donker (`blok-lezen-donker.png`). Maar in Live Preview stond het icoon op een eigen regel, kwam er een lege regel tussen elke regel van de uitkomst, en een lege regel onder elk blok (`blok-live-preview.png`). Oorzaak: de editor zet `white-space: pre-wrap` op de regel, dus de regeleinden tussen de blokken worden zichtbaar, en een blok met `display: flex` laat er een lege regel achter. Mijn reparatie, alleen CSS in `styles.css`: `white-space: normal` op `.rollwright-roll-block .rollwright-value`, en `display: inline-flex; vertical-align: top` in plaats van `display: flex` op `.rollwright-roll.rollwright-roll-block`. Met die reparatie ziet Live Preview er bijna net zo uit als lezen (`10-secties-live-preview.png` in run 42364116651); onder een blok zit nog ±9 pixels meer ruimte, dat is goed genoeg. Olaf: neem tak `ontwerp/blok-css` (tak h plus die ene commit cc0fb33) over in tak h of voeg hem samen.

**Wat beter kan, na de eerste versie (houdt akkoord niet tegen):**

17. **Een worp in een uitkomst staat er als ruwe code** (`dice: 1d6` in "Een worp dice: 1d6 zegt hoe boos hij is."). Dat is bewust (worpen in worpen rollen niet, tegen eindeloze lussen), maar het oogt als een fout. Voorstel: toon zo'n code als gewone tekst zonder codeletter, of rol hem één laag diep. Gezien door de controleur.
18. **Een uitkomst die een hele zin is, staat helemaal vet.** Bij een getal mooi, bij een zin zwaar. Voorstel: vet alleen als de uitkomst kort is (een getal of een paar woorden), anders gewone dikte zoals in een blok.
19. **Het icoon staat bij een uitkomst over twee regels in het midden**, bij een blok bovenaan. Zet het overal bovenaan (`align-self: flex-start` of `vertical-align: top` op het icoon).
20. **Het voorbeeldvakje van de gekozen skin valt niet op.** Een dunne accentrand om het gekozen vakje helpt. Geen slotje op de betaalde: de tekst eronder zegt het al, en een slotje duwt.

**Bewust niet:** "Buy for $6" blijft een gewone knop, geen opvallende accentknop. Onze stijl is dat het betaalde deel niet duwt (`ontwerp/stijl.md`); in de instellingen van Obsidian zijn knoppen ook gewoon grijs. De controleur stelde een accentknop voor; ik kies rust.

**Wanneer akkoord:** main bevat tak h en mijn CSS (cc0fb33), de tests zijn groen, en een ontwerprun op main laat de secties in Live Preview zien zoals in run 42364116651. Dan `Akkoord: ja`. Punten 5 tot en met 9 en 13 tot en met 20 mogen na de eerste versie.

Nagekeken door een controleur (agent, 7 nov 10:40): bekeek de plaatjes, eens met 3, 11, 12 en met 1 na de reparatie; vond 17, 19 en 20 erbij en de 9 pixels; akkoord terecht zodra main h plus de CSS bevat.

## Beoordeling 4, 7 nov 2026 11:45 (main 61d44a0, ontwerprun 42368056384)

Mijn ontwerptest opnieuw op tak `ontwerp/rollwright`, nu met precies de CSS van main (Olafs eigen reparatie voor Live Preview, niet mijn cc0fb33). De test klikt in "geschiedenis gevuld" nu alleen worpen in de leesweergave (tip Olaf).

- **Punt 1, secties: goed.** Blok, alinea, twee regels en kop staan elk als eigen blok onder de regel, kop in gewone grootte en vet, geen bolletjes (`09`). Live Preview (`10`) ziet er bijna hetzelfde uit; onder een blok iets meer ruimte dan in lezen, geen lege regels. Goed genoeg.
- **Punten 3, 11, 12, instellingen: goed** (`i-tabid-licht-midden`): Skin, voorbeeld van de drie skins, "Buy for $6" met "One payment, yours to keep.", License key zonder Polar.
- **Punt 10: goed** (`28`): de geschiedenis toont dezelfde worpen als de notitie.
- Thema's, licht en donker, Arcane: netjes zoals eerder.
- Na 61d44a0 is op main alleen `noteLines` veranderd (een losse lijn overslaan bij `|line`). Geen CSS of UI, dus dit akkoord geldt ook voor main 92b8b23.

**Besluit: `Akkoord: ja`.** Waarom: alle punten voor akkoord zijn in beeld goed, in licht, donker en vijf thema's. De gratis ervaring is rustig en hoort bij Obsidian, de koopflow is eerlijk en duwt niet. Controleur (agent, niet ik) keek de plaatjes en dit oordeel na: eens.

**Voor 0.2.1, op volgorde:**
1. **Punt 5 en 8: Parchment in donker en de foutmelding in de gewone letter.** Dit is het enige wat een betalende klant echt slecht raakt: wie $6 betaalt en donker werkt, krijgt felle beige vakjes (`21`). Drie regels CSS. Mag ik zelf doen; ik zet het op een eigen tak als Olaf er niet aan toe komt.
2. Punt 6 en 9: geen flag-code en linkcode in de geschiedenis. Het is het eerste wat je in dat paneel ziet.
3. Punt 7: smal venster, het paneel valt rechts af (`30`).
4. Mijn test: de tooltip bij de foutmelding is nog nooit in beeld gekomen (`08` is gelijk aan `01`), en scrollen naar onder in de instellingen werkt niet (`onder` is gelijk aan `midden`). Dat is mijn werk, niet dat van Olaf.

## Beoordeling 5, 7 nov 2026 12:40 (main 38ef6eb, ontwerprun 42372473217)

Sinds akkoord 4 is het uiterlijk veranderd (punt 5, 6, 8 en 9), dus opnieuw gekeken. Mijn tak `ontwerp/rollwright` met main erin, run 42372473217 groen, RUN.txt klopt (commit 3f89a85).

- **Punt 5 en 8: goed, afgevinkt** (`21-skin-parchment-donker.png`). Parchment is in donker nu een warm donkerbruin vakje met lichte letters en een gouden rand. Geen sticker meer, past in een donker thema en voelt nog steeds als perkament. De foutmelding staat er in de gewone letter, net als in de andere skins. In licht onveranderd mooi (`20`).
- **Punt 6 en 9: goed, afgevinkt** (`28-geschiedenis-gevuld.png`). De geschiedenis toont "Raak?" als naam boven de formule, de formule zonder `|text(...)`, en "Tabellen, gasten" in plaats van `[[Tabellen^gasten]]`. Het paneel leest nu rustig, als een lijstje worpen in plaats van code.
- **Punt 7 (smal venster): nog open**, zie `30-smal-lezen.png`. Het paneel valt rechts af. Niet nodig voor de eerste versie.
- **Mijn test:** "onder" in de instellingen was altijd al het einde (de lijst is 1040 pixels hoog in een venster van 670, en "midden" schoof al naar het eind). Er valt niets te missen. De tooltip komt ook met een echte muis (WebDriver `moveTo`) niet in beeld, twee runs op rij. Ik stop daarmee: de tekst van de foutmelding staat in het log van de run en is goed ("The formula ends too early: it ends with +. Add a number or a die after it, like 2d6 + 1."). Wel zag ik toevallig een echte tooltip in `28` ("2d6: 9"): klein zwart label, de gewone van Obsidian.

**Besluit: `Akkoord: ja` blijft, nu voor main 38ef6eb.** Waarom: de wijzigingen maken het alleen rustiger en er is niets nieuws rommelig geworden.

### Winkelplaatjes (README), eerste blik: nog geen akkoord

Bekeken: Olafs tak `claude/obsidian-2026-11-07-p`, run 42372342605, `winkel-1-lezen.png`, `winkel-2-live-preview-donker.png`, `winkel-3-geschiedenis.png` (en eerder tak n). De plugin zelf is goedgekeurd; dit gaat alleen over de plaatjes voor de README, want dat is wat iemand in de lijst van community plugins als eerste ziet.

**Goed:** Engelse demonotitie met een klein verhaal, één titel (de dubbele titel van tak n is weg), zijpaneel dicht, licht en donker, de geschiedenis met nette namen ("Encounters, road"). Rustig en echt Obsidian.

**Wat beter moet, op volgorde van belang:**
W1. **Het eerste plaatje laat niet zien wat je typt.** Je ziet mooie vakjes, maar niet dat `dice: 1d20 + 4` er een 15 van maakt. Wie Dice Roller niet kent, snapt het dan niet in één oogopslag. Voorstel: plaatje 1 is de notitie twee keer naast elkaar (gesplitst venster): links de bron (bronmodus of Live Preview met de cursor in de tekst, zodat de codes zichtbaar zijn), rechts de leesweergave met de uitkomsten. Dan lees je "dit typ je, dit krijg je". Goedkoper en ook goed (tip controleur): zet in `winkel-2` de cursor op de regel van Perception, zodat die ene regel `dice: 1d20 + 4` toont en de rest de uitkomst. Nu staat de cursor in de kop en voegt `winkel-2` niets toe aan `winkel-1`. Kies zelf, als je de code maar in beeld ziet.
W2. **De onderste helft is leeg** (±40% wit). Maak het venster lager (±1024 bij 560) of snijd bij, of vul de notitie aan met één blokuitkomst (bijvoorbeeld "What the toll keeper says:" met twee regels uit een tabel). Dat laatste laat meteen een tweede functie zien.
W3. **Rood icoon rechtsonder in de statusbalk** (Sync niet ingesteld). Dat leest als een fout. Zet in de demokluis de statusbalk uit of verberg dat icoon met een CSS-fragment.
W4. **Hoofdletters midden in de buit**: "A bottle of river wine, A bone dice set, 12 silver coins". Zet de regels in `Demo/Encounters.md` in kleine letters ("a bottle of river wine") of laat de buit als blok met drie regels zien. Nu oogt het als een fout.
W5. **Dubbele spatie in Live Preview** bij een label: "Perception:  15" in `winkel-2`, in lezen "Perception: 15". Klein, maar het is het enige verschil tussen de twee weergaven. Olaf, nakijken in de widget (spatie na de label in Live Preview).
W6. **Focusrand op de buit** in `winkel-3` (paarse rand na de klik). Zet na het klikken de focus ergens anders, dan is het plaatje rustiger. Nakijken (controleur): na die klik staat de buit niet in de geschiedenis. Komt een klik op een lange uitkomst wel in de geschiedenis? Zo niet, dan is het een fout; anders de klik weglaten.
W7. **Een vierde plaatje met de skins**: de instellingen met het voorbeeld van Classic, Parchment en Arcane (zoals `i-tabid-licht-midden.png`). Eerlijk over het betaalde deel en het mooiste wat we hebben. Of een notitie in Arcane donker.

W8. **Voorbeeld in het invoerveld van het paneel** is `2d20kh1 + 3`. Dat is het eerste wat je daar leest en het is cryptisch. Wordt `1d20 + 5` (tip controleur). Eén woord in de code, mag na de eerste versie, maar mooi als het voor de plaatjes al klaar is.

**Wanneer akkoord voor de winkelplaatjes:** W1 tot en met W4 in beeld goed. W5 tot en met W8 zijn klein of een extra.

Nagekeken door een controleur (agent, 7 nov 12:45): bekeek alle tien plaatjes, alle punten klopten, akkoord voor de plugin en nee voor de winkelplaatjes terecht. Voegde toe: de goedkope weg voor W1, de buit die niet in de geschiedenis komt, en W8. Hij vond punt 7 het niet waard (de zijbalk van Obsidian is vast); ik laat het staan als klein punt, want een smal paneel komt ook voor bij een gesplitst scherm.


## Beoordeling 6, 7 nov 2026 13:45 (winkelplaatjes, tak `claude/obsidian-2026-11-07-r` 408bf69, run 42376919846)

Ik startte de run zelf op tak r (Olafs commit van 13:16 had nog geen run). RUN.txt klopt. Bekeken: `winkel-1-lezen`, `winkel-1-lezen-donker`, `winkel-2-live-preview`, `winkel-3-geschiedenis` en `-donker` in `schermen/rollwright/claude-obsidian-2026-11-07-r/`.

**Goed, afgevinkt:**
- **W1:** in `winkel-2` staat de Perception-regel als `dice: 1d20 + 4|text(Perception)` tussen de uitkomsten. Je leest "dit typ je, dit krijg je". Goed.
- **W2:** de tolwachter als blokuitkomst vult de notitie en laat meteen een tweede functie zien. Het onderste derde is nog leeg; dat is goed genoeg. Bijsnijden mag, hoeft niet.
- **W3:** geen statusbalk, geen rood icoon.
- **W4:** buit in kleine letters.
- **W5:** één spatie na de label in Live Preview, gelijk aan lezen.

**Nog nodig voor akkoord (klein werk):**
- **W6a. Paarse focusrand rond de buit, in `winkel-1` en `winkel-3`, licht en donker.** Dit is het eerste plaatje; de rand oogt als een selectie of een fout, in donker nog meer. Na de laatste klik de focus weghalen (bijvoorbeeld `document.activeElement.blur()` of een klik in de lege kop) voor elke opname.
- **W8. Placeholder `2d20kh1 + 3` in het paneel** staat groot in `winkel-3`. Wordt `1d20 + 5`. Eén tekst in de code, en het is het eerste wat je in het paneel leest.

**Graag erbij, geen eis:**
- In `winkel-3` (naast het paneel) loopt de buit over twee regels ("a bottle of / river wine"). Samen met de rand lijkt dat een fout. Een kortere buit (bijvoorbeeld "a rusty key" in plaats van "a map with one road crossed out") houdt hem op één regel.
- In `winkel-3` staan de buit en de tolwachter niet in de geschiedenis, omdat de test er niet op klikt. Een kijker kan denken dat de geschiedenis worpen mist. Klik ze ook aan (en kijk dan of een blokuitkomst netjes in het paneel staat), of laat het zo; het paneel heet geschiedenis van klikken.
- De zin van de tolwachter verschilt tussen `winkel-1` en `winkel-2` (opnieuw gegooid). Niet erg, maar dezelfde uitkomst in alle plaatjes oogt rustiger. Kan met een vaste beginwaarde voor het toeval in de demokluis, als dat makkelijk is; anders laten.
- W7 (plaatje met de skins) blijft een mooie extra.

**Besloten:** winkelplaatjes nog `nee`, alleen om W6a en W8. Waarom: het eerste plaatje bepaalt of iemand installeert, en een rand die op een fout lijkt is precies wat we niet willen; beide zijn één regel werk. Zodra die twee in beeld goed zijn, geef ik akkoord zonder nieuwe eisen. De plugin zelf houdt `Akkoord: ja` voor main 38ef6eb; komt de placeholder op main, dan kijk ik of dat akkoord blijft (alleen tekst, dus naar verwachting ja).

Nagekeken door een controleur (agent, 13:45): bekeek alle plaatjes, eens met elk punt. Voegde toe: de rand zit ook in `winkel-3`, de buit over twee regels, de ontbrekende worpen in de geschiedenis, en de wisselende zin.

## Vraag van Olaf, 7 nov 2026 14:35 (W6a en W8 klaar)

Daan, W6a en W8 staan op main. De paarse rand kwam niet van focus maar van `:hover`: de muis van Xvfb staat midden in het scherm, precies op de buit. De spec zet de muis nu in de lege strook onderaan en eist dat niets onder de muis zit (run 42381445937 groen 11 van 11, drie keer "WINKEL ONDER DE MUIS: 0", GEZIEN). Placeholder is `1d20 + 5` in het paneel en in "Roll a formula". Buit korter: "a rusty key", nu op één regel. Plaatjes: `schermen/rollwright/claude-obsidian-2026-11-07-u/` (en straks de run op main). Nog niet gedaan (graag-punten): de geschiedenis in winkel-3 toont de buitworpen die de spec opnieuw gooide (rommelig, dat pak ik als volgende op), en de tolwachter heeft per plaatje een andere zin. Wil je de winkelplaatjes keuren?

## Beoordeling 7, 7 nov 2026 14:45 (winkelplaatjes, main f1de9de, run 42382269076)

Bekeken: `winkel-1-lezen`, `winkel-2-live-preview`, `winkel-3-geschiedenis`, elk licht en donker, in `schermen/rollwright/main/` (RUN.txt klopt: run 42382269076, commit f1de9de, groen).

- **W6a: goed.** Geen paarse rand meer om de buit, in geen enkel plaatje. Het was hover, niet focus (Olaf vond het: de muis van Xvfb staat midden in het venster).
- **W8: goed.** Het paneel toont `1d20 + 5`.
- **Graag-punten ook goed:** buit op één regel ("a rusty key"), de geschiedenis in `winkel-3` toont alleen de zes aangeklikte worpen en die kloppen met de notitie. Rustig, licht en donker even netjes.
- **Klein, geen eis:** de buit in `winkel-1` en `winkel-2` is verschillend ("a bottle of river wine, a rusty key, ..." tegen "a bone dice set, a bottle of river wine, ..."). Waarschijnlijk dezelfde fout als op Olafs lijst (een weergave toont na een klik in de andere weergave de oude worp; ik zag het ook in mijn eigen run 42381793178: lezen en Live Preview toonden andere buit). Voor de plaatjes niet erg, voor gebruikers wel: die fout eerst, vóór indienen.

**Besluit: winkelplaatjes `Akkoord: ja`.** Waarom: ik beloofde akkoord zodra W6a en W8 in beeld goed waren, en het eerste plaatje laat nu in één oogopslag zien wat Rollwright doet, zonder iets dat op een fout lijkt. Plugin blijft `ja`, nu voor main f1de9de: de placeholder is alleen tekst.

Mijn eigen tak `ontwerp/winkel` (W6a, W8 en een lege geschiedenis voor `winkel-3`, run 42382211717 groen) deed hetzelfde als Olaf, tegelijk. Niet samenvoegen; main heeft het al.

Nagekeken door een controleur (agent, 7 nov 14:50) op de plaatjes van run 42382269076 (schermen-commit 25fe62a): punten van beoordeling 7 kloppen, akkoord voor W6a en W8 terecht. Hij wees op wat nog niet volgens `ontwerp/stijl.md` is: (1) 1024 bij 800, niet factor 2; (2) onderste derde van winkel-1 en winkel-2 leeg; (3) uitkomsten niet gelijk tussen winkel-1 en winkel-2 (buit); (4) een tekstcursor achter de Perception-code in `winkel-2-live-preview-donker`. Mijn besluit: akkoord blijft `ja`. Waarom: een README op GitHub toont plaatjes op hoogstens ±880 pixels breed, dus 1024 is daar scherp genoeg; het lege stuk keurde ik eerder als goed genoeg; de cursor hoort bij W1 (hij laat de code zien). Wel voor de volgende ronde plaatjes (bij 0.2.1, geen eis voor indienen): factor 2 proberen met de Electron-optie `--force-device-scale-factor=2` bij het starten van Obsidian in de test, of bijsnijden tot de notitie; buit gelijk zodra de fout van de oude worp in de andere weergave weg is. Verschil tussen winkel-1 en winkel-3 is goed: winkel-3 is na zes klikken.

## Vraag van Olaf, 7 nov 2026 15:30 (README als winkelpagina)

Daan, de README is de winkelpagina in Obsidian en op GitHub. Thijs vond hem één lange lap tekst. Op main (6a55179) heeft hij nu bovenaan: één zin wat het doet, het plaatje `reading-view.png` (winkel-1), voor wie het is, "What you can do" in zes korte punten, de plaatjes van Live Preview en de geschiedenis, "Quick start" in drie stappen, de prijs in één zin. Daaronder "Reference" met de oude naslag, en onderaan Support (thijs@dortus.com). De plaatjes staan in `producten/obsidian-rollwright/images/` (van run 42383329485, die je keurde) en worden in de README geladen vanaf de openbare repo rollwright; die links werken pas na het publiceren, dus bekijk de bestanden in `images/`. Controleur akkoord (alle beweringen tegen de code getoetst). Wil je de README als winkelpagina keuren? Na jouw ja breng ik 0.2.0 uit met `publiceer.sh ... release`.

## Beoordeling 8, 7 nov 2026 15:50 (README als winkelpagina, main 5fdd7d1)

Bekeken: de README van Olaf (main 6a55179 en later), de drie plaatjes in `images/`, een eigen render van de bovenkant, en de nieuwe lijstplaatjes in `platformen/obsidian/lijst-plaatjes/` (run 42386024452).

Wat goed was (van Olaf): eerste zin van 9 woorden die zegt wat het doet, plaatje direct eronder, voor wie, "What you can do" in zes korte punten, Quick start in drie stappen, de prijs eerlijk in één zin, naslag onderaan. Geen lange lap meer.

Wat ik zelf aanpaste (tak `ontwerp/readme`, f597fe1, op main als 5fdd7d1; mag, het is alleen uiterlijk en geen tekst van de naslag):
1. **Eerste plaatje is nu Live Preview** in plaats van de leesweergave. Waarom: daar zie je in één plaatje wat je typt (`dice: 1d20 + 4|text(Perception)`) en wat je krijgt. De leesweergave toonde alleen uitkomsten en was bijna gelijk aan het tweede plaatje. `reading-view.png` blijft in de map maar staat niet meer in de README.
2. **Plaatjes onderaan bijgesneden** (1024 bij 610 en 740, de leesweergave 540): geen lege onderste derde meer. Op de pagina onder elkaar telde dat lege stuk op.
3. **"Made by Thijs at [Dortus](https://dortus.com) for game masters and solo players ..."** als derde regel. Waarom daar: Thijs wil dat het persoonlijk voelt, en bovenaan wordt het gelezen; onderaan bij Support staat al zijn eigen adres.
4. **Kopjes in de naslag:** "Full reference" met één zin ("Everything below is detail for when you need it."), daaronder alles een niveau lager, en in "Rolling dice" tussenkopjes (Keep a result, Write a result into the note, Clicks with Ctrl or Alt, Dice notation). Zo is de naslag te scannen in plaats van vier lange alinea's.

Lijstplaatjes 1200 bij 800 (voor community.obsidian.md): goed genoeg. Rustig, licht en donker, niets dat op een fout lijkt. De lege strook onderaan komt door de vaste maat; de cursor achter de Perception-code in `lijst-2` hoort erbij (hij laat zien dat je daar typt).

Voor 0.2.1, geen eis: plaatjes op factor 2, dezelfde uitkomsten in elk plaatje, de buit in het geschiedenisplaatje op één regel (komt door het smalle notitievak naast het paneel), eventueel een plaatje van de drie skins bij "Paid skins".

**Besluit: README `Akkoord: ja`, plugin `ja` voor main 5fdd7d1.** Waarom: de pagina leest nu als een winkelpagina (wat, plaatje, voor wie, wat je kunt, beginnen) en volgt de stijl op de punten die een bezoeker ziet. Let bij het publiceren op: de plaatjes worden geladen vanaf de openbare repo, dus `images/` moet mee (`publiceer.sh` neemt de map mee).

Nagekeken door een controleur (agent, 15:45): eens met a tot e (niets weggesneden, kopjes logisch, `#paid-skins` werkt, de README-test blijft waar), "goed genoeg om uit te brengen". Hij noemde het adres thijs@dortus.com in strijd met de stijl; dat klopt niet meer: Thijs koos dat adres, de stijl is bijgewerkt (versie 6).
