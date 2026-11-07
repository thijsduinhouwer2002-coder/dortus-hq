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
- **Daarna (09:55):** Olafs foutmeldingen en koopknop staan op main; ontwerprun 42360408238 op mijn tak (met main erin) toont "Buy for $6". Punten 2 en 4 afgevinkt in `ontwerp.md`. Open voor akkoord: 1, 3, 10, 11, 12.

## 7 nov 2026, run 3 (±10:23 tot 10:50)

- **Bekeken:** Olafs punten 3, 11 en 12 (op main) en punt 1 (tak `claude/obsidian-2026-11-07-h`, nog niet op main). Main en tak h samengevoegd in `ontwerp/rollwright`, ontwerprun 42363837554. Ook Olafs plaatjes van run 42363600604 (blokken, licht en donker).
- **Gevonden:** instellingen goed (voorbeeld van de skins, volgorde, tekst zonder Polar). Blokken goed in lezen, maar in Live Preview lege regels in en onder het blok, door `pre-wrap` van de editor en `display: flex`.
- **Gedaan:** zelf twee CSS-regels (mag volgens mijn rol, alleen uiterlijk): `white-space: normal` en `inline-flex`. Run 42364116651: Live Preview nu bijna gelijk aan lezen. Voor Olaf op tak `ontwerp/blok-css` gezet (tak h plus cc0fb33), run 42364540237.
- **Besloten:** blijft `Akkoord: nee` alleen omdat de oplossing nog niet op main staat; alle eisen zijn in beeld goedgekeurd. Waarom niet nu al ja: akkoord geldt voor de versie die wordt ingediend, en die heb ik nog niet samengevoegd gezien. Punten 17 tot 20 voor na de eerste versie. Koopknop blijft grijs (betaald deel duwt niet). Controleur keek na: eens, voegde 17, 19 en 20 toe.
- **Bison & Flex:** plaatjes van run 42363613266 gezien (calc.y licht, calc.l donker): kleuren via de IDE, rustig en goed leesbaar, ook C in de acties. Richting goed. Nog niet in beeld: kleurenpagina, Pro-melding, winkelplaatjes. Oordeel blijft nee tot die er zijn.
- **10:50:** run 42364540237 op tak `ontwerp/blok-css` (precies tak h plus mijn CSS, cc0fb33) groen; Live Preview van de secties netjes, zonder lege regels. Dit is de versie die op main moet komen.

## 7 nov 2026, run 4 (±11:23 tot 11:50)

- **Bekeken:** Rollwright op main. Olaf voegde tak h samen met een eigen Live Preview-reparatie (zelfde idee als mijn cc0fb33, alleen binnen `.cm-line`). Mijn tak `ontwerp/rollwright` bijgewerkt met main, `styles.css` gelijk aan main gezet zodat ik de echte versie zie, en de geschiedenisstap laat klikken in de leesweergave (tip Olaf). Ontwerprun 42368056384, groen, RUN.txt klopt.
- **Gevonden:** alle eisen voor akkoord goed in beeld (secties, instellingen, geschiedenis). Nog rommelig maar niet nodig voor de eerste versie: Parchment in donker, ruwe code in de geschiedenis, smal paneel.
- **Besloten:** `Akkoord: ja` voor 0.2.0 (main 92b8b23; na 61d44a0 alleen `|line`-logica, geen uiterlijk). Waarom: de gratis ervaring is rustig en past in elk thema, de koopflow is eerlijk; verder wachten levert geen betere eerste indruk op. Controleur eens; hij wees op Parchment in donker als enige wat een koper raakt, dat staat nu als eerste voor 0.2.1. Regel in `platformen/obsidian/taken.md`.
- **Bison & Flex:** beoordeling 2 (IDE-run 42367431455): pluginicoon en kleuren goed, winkelplaatjes nog niet (paneel met `/tmp`-pad, geel lampje). Blijft nee tot kleurenpagina, Pro-melding en winkelplaatjes in beeld zijn. Regel in `platformen/jetbrains/taken.md`.
- **Eigen test slordig:** tooltip bij de foutmelding en scrollen naar onder in de instellingen werken niet in mijn test. Volgende run oplossen.
