# Architectuur van Rollwright

Werk dit bij als je een bestand toevoegt, weghaalt of een taak verplaatst. Elk bestand blijft onder ±400 regels.

## src/

- `main.ts`: de plugin zelf. Laadt en bewaart instellingen, opgeslagen formules, geschiedenis en bewaarde resultaten (`dice+:`), houdt resultaten per plek in de notitie vast zodat scrollen niet opnieuw gooit, en meldt weergave, Live Preview, geschiedenisvenster, opdrachten en instellingen aan bij Obsidian.

### src/engine/ (rekenkern, zonder Obsidian)
- `index.ts`: de ingang; de rest van de plugin importeert de kern alleen hiervandaan.
- `types.ts`: gedeelde typen (tokens, knopen, modifiers), `DiceError`, de grenzen `LIMITS`, de foutmeldingen die op meer plekken nodig zijn en het budget per worp. Elke foutmelding zegt wat er mis is en wat je typt, met een voorbeeld (getest in `tests/error-hints.test.ts`).
- `tokenizer.ts`: knipt een formule in tokens.
- `parser.ts`: maakt van de tokens een boom (`parseFormula`), met dobbelstenen, modifiers en namen.
- `evaluate.ts`: rekent een boom uit tot totaal en uitsplitsing (`roll`), inclusief namen en rekenkunde.
- `modifiers.ts`: houden en weggooien, ontploffen, opnieuw gooien, uniek, en hoe een losse steen getoond wordt.
- `faces.ts`: welke zijden een steen heeft (getal, procent, bereik, Fudge, eigen zijden, cijfers).
- `state.ts`: de toestand tijdens een worp, een steen gooien en het budget aftellen.
- `average.ts`: het gemiddelde (`averageOf`): precies waar het kan, anders een schatting uit gesimuleerde worpen.
- `compare.ts`: vergelijkingen zoals `>=5` voor modifiers en tellen.
- `format.ts`: getallen tonen en afronden.
- `random.ts`: de standaard toevalsbron.
- `stunt.ts`: de stuntsteen van Fantasy AGE (`1dS`).
- `narrative.ts`: verhalende stenen van Genesys en Star Wars.

### src/rollers/ (van tekst in de notitie naar een uitkomst)
- `inline.ts`: vindt `dice:`, `dice+:`, `dice-:` en `dice-mod:` in een regel of codeblok.
- `spec.ts`: leest wat na `dice:` staat: formule of verwijzing plus vlaggen achter `|`.
- `run.ts`: gooit een spec (`rollSpec`): formules, tabellen, blokken en regels uit andere notities, geneste worpen.
- `markdown.ts`: een klein blokmodel van een notitie om uit te kiezen.
- `table.ts`: markdowntabellen lezen en opzoektabellen (`1-2 | ...`).
- `fields.ts`: getallen uit de frontmatter als namen voor formules.
- `defuse.ts`: maakt uitkomsten veilig om te tonen, zodat een uitkomst nooit zelf opnieuw gooit.
- `modify.ts`: de tekst waarmee een `dice-mod:` code in de notitie wordt vervangen.

### src/ui/ (wat de gebruiker ziet)
- `widget.ts`: toont een uitkomst als klikbaar blokje; gebruikt door leesweergave en Live Preview. Na het renderen bepaalt `isBlockValue` of de uitkomst meer is dan één gewone regel (meer elementen, geen `<p>`, of een `<br>`); dan krijgt het vakje `rollwright-roll-block` (`BLOCK_CLASS`), bij elke nieuwe uitkomst opnieuw bepaald. Dobbelstenen en fouten nooit.
- `reading-view.ts`: zoekt codes in de leesweergave en zet er widgets in.
- `live-preview.ts`: hetzelfde in de editor (CodeMirror).
- `dice-mod.ts`: vraagt bevestiging en vervangt een `dice-mod:` code in de notitie. In Live Preview krijgt de widget zijn regel en nummer op de regel mee (zoals in de sleutel) en schrijft met `replacementInLine` uit `rollers/modify.ts` in één `view.dispatch`; geen `posAtDOM`.
- `history-view.ts`: het zijpaneel met de geschiedenis van worpen. Toont elke worp via `historyLabel`; de ruwe formule staat in de `title` en blijft de formule voor "Roll again".
- `history-label.ts`: `historyLabel`, een pure functie die van een opgeslagen formule een naam (de `text(...)` label) en een nette formule maakt: zonder flags, en bij een verwijzing de bestandsnaam met tabel of kop ("Tabellen, gasten", "2× Bron", een alias als naam). Gebruikt `parseSpec` en `splitPipes` uit `rollers/spec.ts`; valt bij onleesbare tekst terug op de ruwe formule.
- `modal.ts`: venster om snel een formule te gooien.
- `settings.ts`: het instellingenscherm. Eén lijst van rijen (`sections()`: naam, uitleg en de velden en knoppen met hun opslaan) is de enige bron. `display()` tekent die rijen voor Obsidian onder 1.13; `getSettingDefinitions()` geeft dezelfde rijen als definities met `render`, zodat ze in de zoekfunctie van Obsidian 1.13 en later staan. Na toevoegen, weghalen, importeren of Activate tekent de tab opnieuw met `update()` (1.13 en later) of `display()` (ouder), gekozen met `requireApiVersion`. De groep Skins is: Skin, een rij zonder naam met het voorbeeld van de skins, Get the paid skins, License key (zonder Polar-ids alleen Skin, voorbeeld en "coming soon").
- `skin-preview.ts`: het voorbeeld onder de keuze Skin: drie vakjes met een voorbeelduitkomst, elk met de klasse van zijn skin. `styles.css` zet de kleuren van een skin op `body.<skin>` en ook op `.rollwright-skin-preview-tile.<skin>`, zodat een vakje zijn eigen skin toont, los van de skin op body.

### src/pro/ en src/import/
- `pro/license.ts`: de licentiesleutel van Polar. De constanten `POLAR_ORG_ID`, `POLAR_BENEFIT_ID`, `BUY_URL` en `PRICE_TEXT` (de prijs op de koopknop "Buy for $6"; ingevuld met onze Polar-organisatie, benefit en afrekenpagina; is er één leeg, dan "coming soon", geen koopknop en geen sleutelveld), `validateLicense` (vraagt Polar en geeft geldig, ongeldig, onze fout of geen verbinding), `activateLicense` (alleen geldig bewaart sleutel en datum), `recheckLicense` (stil, hoogstens eens per 30 dagen, alleen ongeldig sluit) en `obsidianRequest`, de enige plek in `src/` die `requestUrl` aanroept. De request-functie, de klok en de ids worden meegegeven, zodat tests geen netwerk nodig hebben.
- `pro/skins.ts`: de uiterlijken van de stenen, gratis en betaald.
- `import/dice-roller-data.ts`: haalt opgeslagen formules uit de data van de plugin Dice Roller.

## styles.css

- `.rollwright-roll`: het vakje in de zin. `.rollwright-roll-block`: dezelfde rand en achtergrond (de variabelen `--rollwright-*`), maar als blok met volle breedte onder de regel, koppen in gewone grootte en vet, lijsten zonder bolletjes. Daarna de skins, het skinvoorbeeld en het zijpaneel.

## Hoe het samenhangt

Een code zoals `` `dice: 2d6+3` `` staat in een notitie. `ui/reading-view.ts` (leesweergave) of `ui/live-preview.ts` (editor) vindt hem met `rollers/inline.ts` en zet er een widget uit `ui/widget.ts` neer. De widget vraagt `main.ts` om de uitkomst; die geeft een vastgehouden of bewaard resultaat terug, of laat `rollers/run.ts` gooien. `run.ts` leest de code met `spec.ts`, haalt waar nodig tabellen, blokken of frontmatter uit de kluis via de `RollContext` die `main.ts` aanlevert, en laat formules uitrekenen door de rekenkern in `engine/` (`roll` of `averageOf`, via `engine/index.ts`). In de kern gaat een formule van `tokenizer` naar `parser` naar `evaluate`, met `faces`, `modifiers` en `state` als hulp. De uitkomst gaat terug naar de widget, wordt veilig gemaakt met `defuse.ts` en getoond. Een worp waar iemand om vroeg komt in de geschiedenis (`history-view.ts`). Skins: `main.ts` heeft `isLicensed` als enige vraag (sleutel met `licenseCheckedAt`, en betaling klaar), `activateLicense` voor de knop in `ui/settings.ts` en `recheckLicense` na `onLayoutReady`; beide roepen `pro/license.ts` aan met `licenseRequest`, `now` en `polarIds` van de plugin. `main.ts` slaat instellingen, formules, geschiedenis en `dice+:` resultaten op met `saveData`. Bij `dice-mod:` schrijft `ui/dice-mod.ts` met `rollers/modify.ts` de uitkomst terug in de notitie.

## Tests

- `tests/` (vitest, `tests/**/*.test.ts`): de nep-Obsidian staat in `tests/obsidian-stub.ts`. Voor `dice-mod:`: `dice-mod.test.ts` (lezen van de code, `modifiedText`, defuse), `dice-mod-plugin.test.ts` (leesweergave, Live Preview met een nep-`EditorView`, het venster), `dice-mod-replace.test.ts` (`rollers/modify.ts`), met gedeelde hulp in `dice-mod-helpers.ts`.
- `e2e/specs/` (de echte Obsidian op GitHub Actions): wdio draait elk `*.e2e.mjs` bestand als spec (`e2e/wdio.conf.mjs`). Gedeelde hulp heet daarom anders, zoals `dicemod-hulp.mjs` voor `dicemod-live.e2e.mjs` (Live Preview) en `dicemod-lezen.e2e.mjs` (leesweergave en Enter).

## Lint

- `eslint.config.mjs` (`npm run lint`): de `recommended`-instelling van `eslint-plugin-obsidianmd`.
- `eslint.scanner.config.mjs` (`npm run lint:scanner`): zo streng als de scanner van de communitygids voor een plugin die vandaag wordt ingediend, met dezelfde genegeerde bestanden (`tests`, `.mjs`). Draai beide vanuit de productmap, dan doen `manifest.json` en `LICENSE` mee. Werk deze bij als de docs van de plugin veranderen.
