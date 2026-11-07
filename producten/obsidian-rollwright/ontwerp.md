Akkoord: nee 7 nov 2026, omdat de worpen op secties nog rommelig ogen, de foutmelding niet zegt wat je moet doen, je de betaalde skins niet kunt zien voor je koopt, en de groep Skins in de instellingen in de verkeerde volgorde staat (zie beoordeling 2). De instellingen zijn nu wel in beeld en verder goed.

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
