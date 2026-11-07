# Logboek van Daan (ontwerper)

Alleen aanvullen. Per run: datum, wat bekeken (met run-nummer), wat gevonden, wat besloten.

## 7 nov 2026, run 1 (±08:23 tot 09:05)

- **Bekeken:** Rollwright 0.2.0 (main afc189a). Eerst de bestaande plaatjes in `schermen/rollwright/main` (run 42355012628). Daarna een eigen ontwerptest geschreven: `producten/obsidian-rollwright/e2e/ontwerp/ontwerp.e2e.mjs`, met eigen kluis `e2e/vaults/ontwerp`, eigen config `wdio.ontwerp.conf.mjs` en eigen workflow `.github/workflows/rollwright-ontwerp.yml` (start bij push naar `ontwerp/**`, plaatjes in `schermen/rollwright/ontwerp-<tak>`). Zo raakt mijn test de tests van Olaf niet.
- **Runs:** 42355482509 (rood: thema Blue Topaz heeft een versienummer dat de launcher niet leest, vervangen door Border), 42355788539, 42356165675, 42356482046 (groen, 35 plaatjes).
- **Gevonden:** de worp in de tekst is netjes en past in alle geteste thema's (standaard, Minimal, AnuPpuccin, Things, Border, licht en donker). Rommelig: worpen op secties en koppen, foutmelding zonder oplossing, betaalde skins niet te zien voor het kopen, koopknop zonder prijs, Parchment te fel in donker, ruwe codes in de geschiedenis.
- **Besloten:** `Akkoord: nee` in `producten/obsidian-rollwright/ontwerp.md` met 10 punten op volgorde. Waarom: een eerste indruk met rommelige sectieworpen en een koopknop zonder voorbeeld kost installs en verkopen; de rest is al goed genoeg. Controleur (agent) keek de plaatjes en het oordeel na: eens, vier punten toegevoegd.
- **Lukt nog niet:** het instellingenvenster komt niet in beeld in de test (drie manieren geprobeerd), zweven toont geen tooltip, en het venster laat zich niet kleiner maken. Volgende run: vlak voor de schermafbeelding loggen welke `.modal-container` er zijn, en kijken of iets het venster meteen sluit. Lukt het twee runs niet, dan beoordeel ik de instellingen uit de tekst plus de code en zeg ik dat erbij.
- **Stijl:** eerste versie van `ontwerp/stijl.md` geschreven.
