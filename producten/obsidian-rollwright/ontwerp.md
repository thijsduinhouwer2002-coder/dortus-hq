# Rollwright: ontwerp

## Notatie 0.2 (6 nov 2026, Olaf)

**Wat het doet.** Rollwright 0.2 vult de notatie aan die gebruikers van Dice Roller al in hun notities hebben staan, zodat een overstap niets kapot laat. Bron voor de betekenis is alleen deel 4 van `platformen/obsidian/onderzoek-dice-roller.md` (README en openbare beschrijving), geen code van Dice Roller. In deze volgorde, omdat de eerste punten het vaakst in bestaande notities staan (GOK):
1. **Vlaggen die nu niets doen:** `|round` en `|noround` (afronden naar geheel getal, standaard aan volgens de instelling afronding), `|ceil`, `|floor`, `|signed` (altijd een plus- of minteken), `|paren` en `|noparen` (haakjes om de uitkomst).
2. **`dice+:` en `dice-:`**: `dice+:` bewaart de uitkomst over herstarts (in de plugindata, per notitie en regel), `dice-:` bewaart nooit, ook niet als bewaren standaard aan staat. `dice:` volgt de instelling.
3. **`dice-mod:`**: na een bevestiging vervangt de plugin de code in de notitie door `<formule> -> <volledige uitkomst> -> <totaal>` (formule weg als de instelling dat zegt). Eén stap, met Ctrl-Z terug te draaien via de editor. Bij sectie- en tabelrollers zonder block id doet `dice-mod` niets en meldt dat, omdat het anders de bronnotitie wijzigt.
4. **Klikken:** Ctrl- of Cmd-klik op een sectie, tabel of lijst opent de bron. Alt-klik rolt opnieuw en toont het gemiddelde.
5. **Notitievelden als getal:** `dice: str` en `1d20 + str` lezen een getal uit de frontmatter van de notitie zelf (geen Dataview nodig). Onbekend veld geeft de gewone foutmelding.
6. **`1dS`** (stuntsteen): toont totaal en stuntpunten bij een dubbel, zoals beschreven in 4.2.
7. **Narratief (Genesys en Star Wars):** alleen als de hele uitdrukking uit narratieve stenen bestaat, zodat `2d6` of `1D6KH1` nooit verkeerd gelezen wordt (de fout die Dice Roller in maart 2025 had). Eigen tekens of tekst, niet het lettertype van Dice Roller.

**Wat het bewust niet doet.** Geen Dataview `dv(...)`, geen 3D-stenen, geen dobbelpaneel met knoppen, geen codeblok `dice`. Geen koopknop of nieuwe betaalde functies. Geen tekst, iconen of lettertypes uit Dice Roller. Elk punt is los uit te brengen; lukt narratief niet schoon, dan gaat 0.2 zonder.

**Hoe het aansluit.** Vlaggen in `src/rollers/spec.ts` (ze staan nu in `IGNORED_FLAGS`) en de weergave in `src/engine/format.ts`. Het voorvoegsel (`dice`, `dice+`, `dice-`, `dice-mod`) wordt gelezen waar nu `formulaFromCode` staat, en `src/rollers/defuse.ts` moet alle vier onschadelijk maken (toets dat met de L9-tests). Bewaren gebruikt de bestaande opslag van de plugin. `dice-mod` schrijft via de editor (`Editor.replaceRange`) of `app.vault.process`, nooit buiten de eigen notitie. Velden via `metadataCache.getFileCache(file).frontmatter`.

**Wanneer het af is (toetsbaar).**
- Elk punt hierboven heeft tests in de rekenkern of met de nep-Obsidian; `npm test`, `npm run build` en `npm run lint` (0 fouten) slagen.
- `2d6|round`, `1d6/4|ceil`, `1d6/4|floor`, `1d6-3|signed` en `1d6|paren` geven de juiste weergave; combineren met `|text(x)` en `|nodice` werkt.
- `dice-mod: 3d100 + 12` geeft precies de vorm `3d100 + 12 -> [a, b, c] + 12 -> totaal`.
- Een uitkomst met `dice+:`, `dice-:` of `dice-mod:` erin rolt niet opnieuw (defuse-test).
- Narratief: `3g2p` herkend, en geen enkele bestaande test of gewone notatie (`2D6`, `1d20kh1`, `4dF`) verandert van uitkomst.
- OPEN.md en README bijgewerkt; wat alleen in Obsidian te bewijzen is, staat op de handmatige testlijst.

### Goedgekeurd met voorwaarden (controleur, 6 nov 2026). Deze gaan voor op de tekst hierboven.
1. **Eigen keuzes.** De werking van `round`, `ceil`, `floor`, `signed`, `paren` (4.6 noemt alleen de namen), de bevestiging en Ctrl-Z bij `dice-mod`, Ctrl-klik op een lijst, notitievelden alleen uit de frontmatter (inline velden zoals `str:: 3` werken niet, 4.2 zegt "via Dataview") en de precieze werking van `1dS` zijn eigen ontwerp. Zo vermelden in OPEN.md.
2. **Afronden verandert niets bestaands.** `|round` staat standaard uit, zodat `10 / 4` 2.5 blijft. Eis: geen bestaande test verandert van uitkomst.
3. **`dice-mod` alleen in de eigen notitie,** na een klik en bevestiging, op de code in `ctx.sourcePath`. Nooit in een gerolde uitkomst, een geneste cel, een ingevoegde notitie (`![[Andere]]`) of een kop van een opzoektabel. Sectie-, regel-, tag- en lijstrollers: `dice-mod` schrijft de uitkomsttekst, maar wijzigt nooit de bronnotitie en maakt geen block id. Tests met de nep-Obsidian.
4. **Alle plekken die `dice:` lezen:** `formulaFromCode` (`src/rollers/inline.ts`), `run.ts` (geneste cellen) en `table.ts` (kop van een opzoektabel). Daar worden `dice+:`, `dice-:` en `dice-mod:` herkend of bewust geweigerd, met test.
5. **Defuse** vangt `dice+:`, `dice-:` en `dice-mod:` ook, met tests naast de L9-tests.
6. **Bewaren met `dice+:`** vraagt nieuwe opslag op schijf (het uitkomstgeheugen staat nu alleen in het werkgeheugen), met een grens op de grootte.
7. **Notitievelden:** een formule uit de instellingen gaat voor op een veld met dezelfde naam. Veldnamen die als notatie te lezen zijn (`d`, `dh`, `k`, `s`, `F`) blijven notatie. Tests daarvoor.
8. **`1dS` precies:** eigen keuze, vast te leggen voor de bouw (drie zesvlakken, een ervan de stuntsteen; bij een dubbel zijn de stuntpunten de waarde van de stuntsteen). Zo in de tests.
9. **Narratief:** een uitdrukking die als gewone notatie te lezen is, blijft altijd gewone notatie. Tests voor `2d`, `d`, `3d`, `1dS`, `4dF`. Letters en betekenis in de tests vastleggen per teken; waar 4.3 een letter dubbel geeft (`p`), alleen de uitleg uit 4.3 volgen ("bij A, C of D betekent P Proficiency") en anders een melding. Lukt dit niet schoon, dan gaat 0.2 zonder narratief.
10. **Ctrl-klik op `|none`** (opnieuw leeg) hoort bij punt 4 van de lijst hierboven.
