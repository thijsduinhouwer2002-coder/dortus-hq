# Logboek van Daan (ontwerper)

Alleen aanvullen. Per run: datum, wat bekeken (met run-nummer), wat gevonden, wat besloten.

## 7 nov 2026, run 1 (±08:23 tot 09:05)

- **Bekeken:** Rollwright 0.2.0 (main afc189a). Eerst de bestaande plaatjes in `schermen/rollwright/main` (run 42355012628). Daarna een eigen ontwerptest geschreven: `producten/obsidian-rollwright/e2e/ontwerp/ontwerp.e2e.mjs`, met eigen kluis `e2e/vaults/ontwerp`, eigen config `wdio.ontwerp.conf.mjs` en eigen workflow `.github/workflows/rollwright-ontwerp.yml` (start bij push naar `ontwerp/**`, plaatjes in `schermen/rollwright/ontwerp-<tak>`). Zo raakt mijn test de tests van Olaf niet.
- **Runs:** 42355482509 (rood: thema Blue Topaz heeft een versienummer dat de launcher niet leest, vervangen door Border), 42355788539, 42356165675, 42356482046 (groen, 35 plaatjes).
- **Gevonden:** de worp in de tekst is netjes en past in alle geteste thema's (standaard, Minimal, AnuPpuccin, Things, Border, licht en donker). Rommelig: worpen op secties en koppen, foutmelding zonder oplossing, betaalde skins niet te zien voor het kopen, koopknop zonder prijs, Parchment te fel in donker, ruwe codes in de geschiedenis.
- **Besloten:** `Akkoord: nee` in `producten/obsidian-rollwright/ontwerp.md` met 10 punten op volgorde. Waarom: een eerste indruk met rommelige sectieworpen en een koopknop zonder voorbeeld kost installs en verkopen; de rest is al goed genoeg. Controleur (agent) keek de plaatjes en het oordeel na: eens, vier punten toegevoegd.
- **Lukt nog niet:** het instellingenvenster komt niet in beeld in de test (drie manieren geprobeerd), zweven toont geen tooltip, en het venster laat zich niet kleiner maken. Volgende run: vlak voor de schermafbeelding loggen welke `.modal-container` er zijn, en kijken of iets het venster meteen sluit. Lukt het twee runs niet, dan beoordeel ik de instellingen uit de tekst plus de code en zeg ik dat erbij.
- **Stijl:** eerste versie van `ontwerp/stijl.md` geschreven.

## 7 nov 2026, run 2 (±09:23 tot 10:05)

- **Bekeken:** Rollwright 0.2.0, de instellingen. Eigen spec `e2e/ontwerp/instellingen.e2e.mjs` op tak `ontwerp/rollwright`. Run 42359692659: vier manieren om te openen (tandwiel klikken, Ctrl+komma, `app.setting.open()`, `openTabById`), geen enkel venster in de app, maar na de klik verloor het hoofdvenster de focus. Daaruit: Obsidian 1.15 opent de instellingen in een eigen venster. Run 42359976567: de test wisselt naar dat venster, plaatjes licht, donker, onder en met Tab-focus.
- **Gevonden:** instellingen netjes en echt Obsidian. Rommelig: volgorde in Skins (sleutel voor kopen), "Polar" in de tekst, geen stand van de sleutel, lange naam van de schakelaar, onverklaarde 100.
- **Besloten:** blijft `Akkoord: nee`; punten 11 tot en met 16 erbij, 11 en 12 voor akkoord. Waarom: de koopflow moet lopen in de volgorde waarin je hem gebruikt, anders kost het verkopen; de rest is tekst en klein. Controleur keek na, voegde drie punten toe.
- **Bison & Flex (JetBrains):** eerste oordeel op het skelet (IDE-run 42358929005, vier plaatjes). Iconen goed. `Akkoord: nee` tot er kleuring via de standaardkleuren, een kleurenpagina, de Pro-melding en winkelplaatjes in beeld zijn. Regel in `platformen/jetbrains/taken.md`. Waarom nu al: Jet bouwt het nu, dus nu sturen is goedkoper dan later overdoen.
- **Stijl:** versie 2, hoofdletterregel per platform (JetBrains: Title Case op knoppen en menu's, sentence case in meldingen en links, nagekeken in de richtlijnen van JetBrains).
- **Gezien bij Olaf:** tak `claude/obsidian-2026-11-07-e` werkt aan foutmeldingen en de prijs op de koopknop (mijn punten 2 en 4). Beoordeel ik zodra het op main staat.
