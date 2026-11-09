# dortus.com: kant-en-klaar plan (Abel)

Versie 1, 10 nov 2026 01:20 NL. Status: **heeft een ja van Thijs nodig**, want de regels verbieden ons bestaande pagina's van dortus.com te veranderen (`organisatie/regels.md`, "De website dortus.com").

## Het probleem (GEZIEN 10 nov 00:40)
- De hoofdpagina dortus.com heet "Dortus: Mermaid and LaTeX editors for Confluence Cloud" en opent met "Editors for Confluence Cloud". Het deelplaatje (`assets/og-home.png`, 1200 x 630) toont een Confluence-editor.
- We zijn op 6 nov met Atlassian gestopt (`organisatie/middelen.md`, Gestopt).
- Elk ander account linkt naar dortus.com: JetBrains (url van de verkoper), Steam (straks), Polar, GitHub. Een programmeur die vanaf Bison & Flex doorklikt, of een speler vanaf Steam, landt bij Confluence-apps. Dat ziet eruit als een ander bedrijf, of een bedrijf dat zijn eigen site niet bijhoudt. Dit is de grootste vertrouwensbreuk van alle accounts.
- Goed nieuws: de productpagina's zijn wel verzorgd en eigentijds: /bison-flex/, /click-joints/, /rollwright/ (alle drie 200, eigen deelplaatje), en /atlassian.html ("All apps") bestaat al voor de oude Confluence-apps.

## Voorstel
1. **Nieuwe hoofdpagina** (alleen `index.html` en `assets/og-home.png` vervangen, plus favicon in de stijl van het uniform):
   - Bovenaan het beeldmerk van Mila en de korte zin uit `merk/teksten.md`: "Small games and focused tools that fill a real gap."
   - Daaronder een kaart per product dat live of bijna live is, met het eigen plaatje dat er al staat: Bison & Flex (JetBrains), Click Joints (Blender), Rollwright (Obsidian), straks het spel (Steam, zodra "binnenkort").
   - Onderaan: "Earlier: our Confluence apps" met een link naar /atlassian.html. Zo blijven alle oude gidsen en hun Google-verkeer werken, er gaat niets weg.
   - Contact thijs@dortus.com, privacy en voorwaarden zoals nu.
2. **Alle oude Confluence-gidsen** (±60 losse pagina's) blijven staan: ze kosten niets en kunnen nog verkeer geven. Alleen de hoofdpagina verandert.
3. **Eerste versie staat klaar:** `platformen/abel/dortus-com/index.html`, met `voorbeeld-desktop.png` en `voorbeeld-telefoon.png` (GEZIEN met de Read-tool, 10 nov 00:37 NL: kaarten tonen de posters heel, leesbaar op 390 px breed). Gebruikt alleen bestaande bestanden van de site (posters, letters, het oude D-logo). Zodra Mila's beeldmerk er is, wissel ik het logo (regel met BEELDMERK) en de kleuren naar het uniform, en maak ik een nieuw `og-home.png`. Daarna Daan, dan na het ja van Thijs de hoofdchat in de repo dortus (alleen `index.html` en `assets/og-home.png`).

## Wat Thijs moet doen (±1 min)
Ja of nee zeggen in de projectchat: "Abel mag de hoofdpagina van dortus.com vervangen door de nieuwe pagina, oude pagina's blijven staan." Staat op `organisatie/lijst-thijs.md`.

## Klaar als
Thijs zei ja, de nieuwe pagina staat live (curl toont de nieuwe titel), en Daan zette `Akkoord: ja`.
