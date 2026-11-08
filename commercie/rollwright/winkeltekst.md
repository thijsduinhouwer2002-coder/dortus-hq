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

## Bijwerking 8 nov 2026: versie 0.3.0 (nieuw uiterlijk)

Door Chris, run 3 voor Rollwright. Aanleiding: 0.3.0 is bijna af (klus 1 tot 5b van Daan op main, klus 6 voorbeeldnotitie en 7 skin-tegels nog niet, zie `platformen/obsidian/taken.md`). Rollwright wordt pas aangemeld met 0.3.0 (bericht Thijs 7 nov 22:10). De tekst hierboven gaat over 0.2.0; dit deel vervangt de korte en lange beschrijving zodra 0.3.0 uitkomt. De README houdt Olaf zelf bij (heeft "Roll log" al).

### Wat er voor de koper verandert
In 0.2.0 was Rollwright "Dice Roller, maar strakker". In 0.3.0 is het verschil iets wat je ziet in de eerste tien seconden: een worp tuimelt als je klikt, een hoogste worp licht goud op (stempel NAT 20 bij een natuurlijke 20 op één d20), een laagste worp wordt rood, en elke worp die je aanklikt komt in een Roll log, gegroepeerd per notitie en sessie. Geen andere dobbelplugin in de lijst doet dat (GOK: niet in hun code nagekeken, wel in hun README's en beschrijvingen gezocht, zie `cijfers.md`). Dat moment moet daarom vooraan in elke tekst, vóór de lijst met notatie.

### Korte beschrijving (voorstel voor manifest.json bij 0.3.0, 186 tekens)
`Roll dice right in your notes with a full formula notation. Click to roll again, see a natural 20 light up, draw from tables, lists, sections and tags, and keep your rolls in a Roll log.`

Waarom: de regels van Obsidian vragen hoogstens 250 tekens, beginnen met een werkwoord, eindigen met een punt, geen emoji (DERDEN, [Submission requirements for plugins](https://github.com/obsidianmd/obsidian-developer-docs/blob/main/en/Community%20directory/Submission%20requirements%20for%20plugins.md)). Alle zoekwoorden van de oude tekst blijven staan (dice, roll, tables, lists, sections, tags), "history" wordt "roll log" omdat het paneel nu zo heet. Nieuw is het enige wat ons onderscheidt: het moment van de natuurlijke 20. Advies 11 in `commercie/adviezen.md`.

### Lange beschrijving voor de listing (vervangt die hierboven bij 0.3.0)
Roll dice and random tables right inside your notes. Write a formula, read the result, click to roll again. Made for game masters and solo players who keep their sessions in Obsidian.

Every roll is a small game piece. Click it and it tumbles and lands in about half a second. The highest possible roll lights up gold, with a NAT 20 stamp on a natural 20; the lowest turns red. Every roll you click goes into a Roll log, grouped by note and session, so a session reads back like a story.

- Uses the `dice:` notation known from the Dice Roller plugin, so most of your existing notes should keep working.
- Roll on your own tables, lists, sections, lines and tagged notes. Lookup tables pick the matching row.
- Keep a result after a restart with `dice+:`, or write it into the note with `dice-mod:`.
- Use numbers from your frontmatter: `dice: 1d20 + str`.
- Keep highest, exploding, rerolls, success counting, Fudge and Genesys narrative dice.
- Reading view and Live Preview look the same, in light and dark. Roll animations are off when your system asks for reduced motion.

All rolling is free. Two extra skins, Parchment and Arcane, are a one-time $6 purchase. No account, no telemetry.

Pas aan als klus 6 af is: voeg na de tweede alinea toe "New to it? Open the empty Roll log and create an example note: a tavern scene with live rolls." Niet eerder, want het bestaat nog niet.

Wat ik bewust weglaat: "3D", "animated dice" (het is geen 3D-steen, het is een token dat beweegt), mobiel (niet getest), en elke vergelijking met wat een concurrent niet kan.

### Plaatjes voor de listing (volgorde, sluit aan op Daan, ontwerp-v2 punt 6)
De listing neemt alleen JPEG, PNG of WebP, tot 5 bureaubladplaatjes van 1200 bij 800 (DERDEN, [Manage your plugin or theme](https://github.com/obsidianmd/obsidian-developer-docs/blob/main/en/Community%20directory/Manage%20your%20plugin%20or%20theme.md)). Een GIF kan dus niet in de listing, alleen in de README. Of een bewegende WebP werkt, zegt de pagina niet (GOK, alleen te testen door wie inlogt). Daarom moet het moment in een stilstaand plaatje zichtbaar zijn:
1. **Poster** met een crit in beeld (NAT 20 in goud). Dit is het plaatje in de zoeklijst en het belangrijkste.
2. Dit typ je, dit krijg je (Live Preview, code naast uitkomst).
3. Roll log naast de notitie, met kopjes per notitie en sessie, één crit en één fumble zichtbaar.
4. De drie skins naast elkaar, elk met een crit (klus 7).
5. Tabellen en lijsten (gasten, geruchten, buit).
De oude vijf plaatjes in `platformen/obsidian/lijst-plaatjes/` (0.2.0) niet meer gebruiken als de nieuwe er zijn.

### Zoekwoorden
Blijven gelijk. Erbij als woorden in de tekst (niet als belofte): "natural 20", "session". Mensen schrijven "nat 20" en "natural 20" (GOK), beide staan nu in de tekst (stempel NAT 20, "natural 20").

## Bijwerking 8 nov 2026 (run 5): plaatjes van Daan en de productpagina

Door Chris. Daan heeft poster, logboek, skins en een GIF klaar (`ontwerp/rollwright/`, staan op lijst-thijs voor zijn ja) en een README-voorstel (`ontwerp/rollwright/README-voorstel.md`).

- **README-voorstel en deze winkeltekst spreken elkaar niet tegen** (nagekeken door de controleur). De eerste zin wordt overal "Roll dice right in your notes." (poster, README, productpagina). De lange beschrijving hierboven blijft voor de listing.
- **Voorbeeldnotitie bestaat nu** (klus 6). Zet dus in de lange beschrijving na de tweede alinea: "New to it? Open the empty Roll log and press Try it: create an example note: a tavern scene where every roll is live." De knoptekst is letterlijk "Try it: create an example note" (`src/ui/history-view.ts`).
- **"light and dark" wordt "light, dark and popular themes"**: getest in Minimal, AnuPpuccin, Things en Border (e2e ontwerp v2, gezien door de controleur), en zo staat het op de poster.
- **Plaatjesvolgorde voor de listing, nu met de echte bestanden:** 1 poster (`winkel-1-poster.png`), 2 roll log (`winkel-2-logboek.jpg`), 3 skins (`winkel-3-skins.jpg`). Alle drie 2400 bij 1600, dus 3:2 zoals de listing vraagt. Mijn eerdere plannen 2 (dit typ je) en 5 (tabellen) zitten nu op de poster en in het logboekplaatje; drie is genoeg. Op het logboekplaatje staat geen crit of fumble (wel in mijn plan); niet nodig, de poster heeft de crit.
- **Productpagina 0.3.0** klaar op tak `claude/rollwright-0.3.0` in de repo `dortus` (commit 475bf59): GIF als video bovenaan (210 kB in plaats van 1,7 MB, GEZIEN), poster, roll log en skins, tekst gelijk aan deze winkeltekst. Getest op 390 en 1280 breed, geen zijwaarts scrollen, geen kapotte links (GEZIEN). Controleur: akkoord mits; videolabel en twee kan-punten verwerkt. Gaat live op de dag van release 0.3.0, zie advies 14.
- **Kleine kanttekeningen die bewust niet op de pagina staan:** een "sessie" in het log is dezelfde notitie op dezelfde dag, en het log houdt de laatste 200 worpen (`src/main.ts`). Hoeft niet in een winkeltekst.
