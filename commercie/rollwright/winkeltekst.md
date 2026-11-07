# Rollwright: winkeltekst

Door Chris, 7 nov 2026. Voor Olaf (platformmanager) bij de aanmelding op community.obsidian.md. De README is de winkelpagina op GitHub en in Obsidian; die is al door Daan goedgekeurd en verander ik niet. Dit bestand gaat over de vermelding (listing) op community.obsidian.md en over zoekwoorden.

## Belangrijkste punt: categorie TTRPG
- community.obsidian.md heeft een eigen categorie **TTRPG** (GEZIEN 7 nov: de pagina van Dice Roller linkt naar `/search?type=plugin&categories=ttrpg`, en Dice Roller staat in die categorie).
- In `platformen/obsidian/aanmelding-community.md` staat nu "Editing en Visualization (GOK)". Advies: **TTRPG als eerste categorie**, Editing als tweede als er twee mogen. Daar zoeken en bladeren de mensen die we willen, en daar staat de grote concurrent. Advies 1 in `commercie/adviezen.md`.

## Titel
`Rollwright` (zoals in manifest.json). Geen concurrent in de titel, volgens de regel.

## Korte beschrijving (staat al in manifest.json, 135 tekens)
Roll dice inside your notes with a full formula notation, draw from tables, lists, sections and tags, and keep a history of every roll.

Oordeel: goed. Bevat de zoekwoorden dice, tables, history. Niet veranderen, want een andere korte tekst dan in manifest.json zou verwarren.

## Lange beschrijving (voorstel, iets sterker dan in aanmelding-community.md)
Roll dice and random tables right inside your notes. Write a formula, read the result, click to roll again. Made for game masters and solo players who keep their sessions in Obsidian.

- Uses the `dice:` notation known from the Dice Roller plugin, so most of your existing notes should keep working.
- Roll on your own tables, lists, sections, lines and tagged notes. Lookup tables pick the matching row.
- Keep a result after a restart with `dice+:`, or write it into the note with `dice-mod:`.
- Use numbers from your frontmatter or saved formulas: `dice: 1d20 + str`.
- Keep highest, exploding, rerolls, success counting, Fudge and Genesys narrative dice.
- A roll history panel, in reading view and Live Preview, light and dark.

All rolling is free. Two extra skins, Parchment and Arcane, are a one-time $6 purchase. No account, no telemetry.

Waarom zo: de eerste zin zegt wat het doet, de tweede voor wie. Daarna de dingen die de nieuwe concurrenten (Dice Tray, Dice Rolls) niet allemaal hebben: frontmatter, `dice-mod:`, lookup-tabellen, tags, narratieve dobbelstenen. Alles staat in de README en is op het bureaublad in de echte app getest (zie `platformen/obsidian/status.md`); mobiel is nog niet getest, daarom noemen we mobiel niet, dus geen beloftes die het product niet waarmaakt. Dice Roller noemen in de tekst is eerlijk en nodig (dat is de notatie), niet in de titel.

## Zoekwoorden (waarop mensen zoeken)
GOK op basis van de namen en beschrijvingen van de 10.075 plugins in community-plugins.json (GEZIEN 7 nov): de woorden die makers van dobbelplugins zelf gebruiken.
- dice, dice roller, roll, random table, random tables
- TTRPG, RPG, D&D, solo RPG, game master
- lookup table, oracle, loot, encounter
Al aanwezig in korte tekst, lange tekst of README: dice, roll, tables, game masters, solo. Niet aanwezig: "TTRPG" en "D&D". De categorie TTRPG dekt het eerste. "D&D" laat ik weg: we testen niet specifiek op D&D-regels en het is een merk.

## Plaatjes
- Bureaublad: 5 plaatjes van 1200 bij 800 staan klaar in `platformen/obsidian/lijst-plaatjes/` (Daan akkoord).
- **Ontbreekt: plaatjes voor mobiel.** De site neemt ook tot 5 plaatjes van 900 bij 1600 voor mobiel (DERDEN, [Manage your plugin or theme](https://github.com/obsidianmd/obsidian-developer-docs/blob/main/en/Community%20directory/Manage%20your%20plugin%20or%20theme.md), regel "Screenshots can include up to 5 desktop images at 1200 by 800 pixels, and up to 5 mobile images at 900 by 1600 pixels"). Rollwright staat mobiel toe (`isDesktopOnly: false`), maar is daar nog niet getest; eerst testen, dan plaatjes. Advies 2 in `commercie/adviezen.md`, voor Olaf en Daan, na de aanmelding. Niet nodig om de aanmelding op te houden.

## Wat de concurrent mist en wij hebben (GEZIEN 7 nov, uit community-plugins.json en de README's)
| | Dice Roller (289.005 downloads) | Dice Tray (97) | Dice Rolls (343) | Rollwright |
|---|---|---|---|---|
| Laatste release | 24 mrt 2025 | nov 2026 | nov 2026 | 7 nov 2026 |
| `dice:` notatie | ja | ja | leest het | ja |
| Tabellen, lijsten, secties | ja | ja | onbekend | ja, plus regels en tags |
| Waarde uit frontmatter | via Dataview | onbekend | onbekend | ja, zonder Dataview |
| Resultaat in de notitie schrijven | ja (`dice-mod`) | onbekend | onbekend | ja, met bevestiging en undo |
| Geschiedenis | nee (GOK) | onbekend | ja | ja |
| Getest in de echte app | onbekend | onbekend | onbekend | ja, elke release |

"Onbekend" betekent: niet nagekeken in hun code. Niet gebruiken in openbare tekst. In de openbare tekst noemen we alleen wat wij doen, niet wat een ander niet doet.
