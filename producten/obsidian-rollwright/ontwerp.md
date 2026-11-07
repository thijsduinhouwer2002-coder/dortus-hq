Akkoord: nee 7 nov 2026, omdat de worpen op secties nog rommelig ogen, de foutmelding niet zegt wat je moet doen, je de betaalde skins niet kunt zien voor je koopt, en ik de instellingen met de koopknop nog niet in beeld heb gekregen.

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

- **De instellingen met de koopknop.** In de test opent het instellingenvenster niet in beeld (`app.setting.open()` en het commando geven geen venster, ook mijn noodweg met een eigen venster niet). Uit de tekst in Olafs test weet ik dat Buy en Activate er staan, maar ik keur niets goed wat ik niet gezien heb.
- **De tooltip bij zweven.** Nagebootst zweven toont geen tooltip in de schermafbeelding. De naam staat wel goed op de knop.
- **Een echt smal venster** (telefoonbreedte). Het venster laat zich in de test niet kleiner maken.

### Wanneer akkoord

Punten 1 tot en met 4 en 10 opgelost en de instellingen in beeld goedgekeurd. Punten 5 tot en met 9 mogen ook na de eerste versie, maar zijn klein.

Nagekeken door een controleur (agent, 7 nov): alle punten klopten met de plaatjes, hij voegde 7 tot en met 10 toe en is het eens met `Akkoord: nee`.
