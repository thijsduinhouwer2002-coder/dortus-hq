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

## Bijwerking 8 nov 2026 (run 6): skins nee, aanmelden met het gratis deel

Door Chris. Aanleiding: oordeel Thijs 8 nov 08:40 (`berichten/daan.md`, `berichten/olaf.md`): poster, GIF en logboek ja; skins nee, want Classic, Parchment en Arcane verschillen te weinig en "zo betaalt niemand $6". Aanmelden mag nu al met het gratis deel; sterkere skins komen in een 0.3.x. Wat dat betekent voor de listing:

### Plaatjes voor de listing (vervangt de volgorde van run 5)
1. Poster (`winkel-1-poster.png`).
2. Roll log (`winkel-2-logboek.jpg`), in de nieuwe versie van Daan met verschillende tijden. Thijs: alles op 04:22 AM oogt nep. Zolang die nieuwe versie er niet is, mag de oude mee (Thijs zei ja op het plaatje), maar liever wachten op de nieuwe als die binnen een dag komt.
3. **Geen skins-plaatje.** Pas terug als de nieuwe skins er zijn en Thijs ze gezien heeft.

Twee plaatjes is weinig maar genoeg: de poster heeft de crit en de notatie, het logboek het verhaal. Een derde plaatje alleen om de rij te vullen verzwakt het geheel (GOK). Mijn vroegere plan 5 (tabellen en lijsten: gasten, geruchten, buit) is de beste kandidaat voor een derde plaatje, als Daan het de moeite waard vindt; geen moet.

### Lange beschrijving: de laatste alinea (vervangt de zin over de skins)
Oud: `All rolling is free. Two extra skins, Parchment and Arcane, are a one-time $6 purchase. No account, no telemetry.`

Nieuw: `All rolling is free. Optional extra skins are a one-time purchase. No account, no telemetry.`

Waarom: (a) de plugin heeft een koopknop, dus de listing moet zeggen dat er iets te koop is (betaaltype Optional payment, DERDEN, [FAQ](https://github.com/obsidianmd/obsidian-developer-docs/blob/main/en/Community%20directory/Frequently%20asked%20questions.md)), en de README zegt het ook (eis van Obsidian voor betaalde delen, DERDEN, [Developer policies](https://github.com/obsidianmd/obsidian-developer-docs/blob/main/en/Community%20directory/Developer%20policies.md), deel Disclosures: "Payment is required for full access" alleen als het duidelijk in de README staat). Eerlijk blijft eerlijk. (b) Thijs vindt de huidige skins hun $6 niet waard; dan zetten we ze niet als verkoopargument in de eerste tekst die iemand leest. (c) Geen bedrag en geen namen: die veranderen misschien met de nieuwe skins, en de listing past Thijs alleen met zijn login aan. Het bedrag staat in de README en in de plugin, voor wie het zoekt.

Wat ik bewust **niet** schrijf: "new skins coming soon" of "buyers get the redesign for free". Dat is een belofte over iets wat nog niet bestaat. Pas als de nieuwe skins uit zijn, komt er een zin bij.

### Korte beschrijving (manifest.json)
Blijft het voorstel van advies 11 (noemt geen skins). Goed zo.

### README (Olaf bouwt, ter controle)
Thijs vroeg Olaf het skins-plaatje uit de README te halen. De README moet het betaalde deel blijven noemen. Advies 16 punt (b): vervang de zin bovenaan ("All rolling is free. Two extra looks, Parchment and Arcane, are a one-time $6 purchase (see Paid skins).") door dezelfde rustige zin als in de listing, met het bedrag pas in het deel Paid skins.

### Productpagina dortus.com/rollwright/
Gedaan deze run (repo `dortus`, op main, samengevoegd vanaf mijn tak met de 0.3.0-pagina plus het weghalen; de oude tak `claude/rollwright-0.3.0` heeft skins.jpg nog en is vervallen): skins-plaatje weg. Het logboek-plaatje (`roll-log.jpg`) vervang ik door Daans versie met verschillende tijden zodra die er is, kop "Paid skins" wordt "Optional skins", tekst blijft feitelijk ($6, Polar, één sleutel voor alle apparaten). Zie `logboek.md`.

## Bijwerking 8 nov 2026 (run 7): versie 0.3.1, skins v2 mogen mee

Door Chris. Aanleiding: Thijs 8 nov 12:33 en 12:34 (`berichten/daan.md`): het skins-plaatje v2 is ja, Parchment en Arcane mogen mee in 0.3.1, maar het verschil is nog niet groot genoeg (zelfde achtergrond, Parchment en Arcane lijken op elkaar); Daan blijft verbeteren, "geen haast: eerst komen de gebruikers voor het gratis deel". Daan gaf `Akkoord: ja` voor 0.3.1; het uitbrengen wacht op één zin van Thijs (lijst-thijs, Olaf 11:50).

### Korte beschrijving
In `manifest.json` van 0.3.1 staat (GEZIEN): `Roll dice right in your notes with a full formula notation. Click to roll again. A natural 20 lands in gold. Draw from tables, lists, sections and tags, and keep your rolls in a Roll log.` Dat is iets anders dan mijn voorstel uit advies 11 ("see a natural 20 light up"), maar beter: "lands in gold" is dezelfde zin als in de README, het ontwerp en op de productpagina. In de lanceerberichten stond nog "lights up gold"; dat is gelijkgetrokken (`lancering.md`, run 7). **Dit is vanaf nu de korte tekst**, overal. Niets veranderen.

### Plaatjes voor de listing (blijft zoals run 6)
1. Poster (`winkel-1-poster.png`).
2. Roll log (`winkel-2-logboek.jpg`, de versie met verschillende tijden van 20:41 tot 21:02).
3. **Nog geen skins-plaatje in de listing.** Pas met de skins-versie waar Thijs volmondig ja op zegt.

Waarom niet: het plaatje noemt namen, $6 en een uiterlijk dat Thijs zelf nog niet af vindt, en de listing past alleen Thijs met zijn login aan. Dezelfde reden als voor de slotzin hieronder. Het plaatje v2 komt wel op de productpagina (en in README en Polar als Olaf en Daan dat willen), want die passen wij zelf aan. Advies 19 (a).

### Lange beschrijving
Blijft die van run 6, maar de slotzin wordt de vaste vorm van README en ontwerp: `All rolling is free. Optional skins are a one-time purchase. No account, no telemetry.` (zonder "extra", zie advies 19 (c)). Waarom niet terug naar het bedrag en de namen: Thijs vindt het verschil nog te klein en de skins worden verder verbeterd; namen en uiterlijk kunnen nog veranderen, en de listing past alleen Thijs met zijn login aan. Bedrag en namen staan in de README (deel Paid skins), op het plaatje en op de productpagina.

### Productpagina dortus.com/rollwright/
- **Op main (nu, repo `dortus`):** het logboek-plaatje is vervangen door Daans versie met verschillende tijden. Thijs vond alles op 04:22 AM nep ogen, en dit plaatje laat alleen gratis functies zien die al in 0.3.0 zitten, dus het hoeft niet op de release te wachten.
- **Op tak `claude/rollwright-0.3.1` (repo `dortus`):** "Version 0.3.1 is out", `softwareVersion` 0.3.1, en het skins-plaatje v2 onder "Optional skins" met een feitelijk onderschrift ("The same rolls in each skin, in dark and light."). Gaat naar main op de dag dat release 0.3.1 er staat. Getest op 390 en 1280 breed: geen zijwaarts scrollen, geen kapotte plaatjes, geen 404 (GEZIEN).

### Wat ik bewust niet schrijf
"Look like nothing else in Obsidian" (staat op het plaatje van Daan) neem ik niet over in eigen tekst: dat is een bewering over alle andere plugins en thema's die we niet nagekeken hebben, en Thijs zelf vindt de twee skins nog op elkaar lijken. Via het plaatje staat de zin wel op de productpagina; dat accepteer ik bewust tot Daans volgende versie, want Thijs keurde dit plaatje. Advies 19 (b).

## Bijwerking 8 nov 2026 (run 8): de listing staat live, dit is nu de tekst

Door Chris. Aanleiding: Thijs 8 nov 13:04: Rollwright staat live op https://community.obsidian.md/plugins/rollwright . De lange beschrijving mocht hoogstens 1000 tekens; mijn tekst (run 6 en 7, met de alinea over de voorbeeldnotitie) was langer, en de projectchat kortte hem in tot 877 tekens.

### De lange beschrijving zoals hij nu live staat (GEZIEN 8 nov met curl op de listing, 877 tekens)
```
Roll dice and random tables right inside your notes. Write a formula, read the result, click to roll again. Made for game masters and solo players who keep their sessions in Obsidian.

Every roll is a small game piece: click it and it tumbles and lands. A natural 20 lights up gold, a natural 1 turns red. Every click goes into a Roll log, grouped by note and session, so a session reads back like a story.

- Uses the `dice:` notation from Dice Roller, so most existing notes keep working.
- Roll on your own tables, lists, sections, lines and tagged notes.
- Keep a result with `dice+:`, or write it into the note with `dice-mod:`.
- Keep highest, exploding, rerolls, success counting, Fudge and Genesys dice.
- Same look in Reading view and Live Preview, in light and dark themes.

All rolling is free. Optional extra skins are a one-time purchase. No account, no telemetry.
```
**Dit is vanaf nu de lange beschrijving.** De versies hierboven (0.2.0, run 3, run 5, run 6, run 7) zijn geschiedenis. Een nieuwe versie moet onder de 1000 tekens blijven; houd ±100 tekens ruimte voor één zin bij de nieuwe skins.

### Wat de inkorting wegliet, en of dat erg is
- De alinea over de voorbeeldnotitie ("New to it? ... Try it: create an example note ..."). Niet erg: wie de plugin opent, ziet de knop in het lege Roll log.
- Frontmatter (`dice: 1d20 + str`) en lookup-tabellen. Jammer, want dat zijn twee echte verschillen met de kleine concurrenten (zie de tabel bovenaan), maar ze staan direct eronder in de README op dezelfde pagina. Niet de moeite van een nieuwe inlog van Thijs waard.
- "Reduced motion" en "popular themes". Prima, details.

### Drie kleine verschillen met de vaste vorm (regel "Elk product": overal hetzelfde)
| In de listing | Vaste vorm (README, manifest 0.3.1, productpagina, lanceerberichten) |
|---|---|
| A natural 20 **lights up** gold, a natural 1 turns red. | A natural 20 **lands in** gold. |
| Optional **extra** skins are a one-time purchase. | Optional skins are a one-time purchase. |
| Korte tekst bovenaan: "... keep a history of every roll." | Manifest 0.3.1: "... keep your rolls in a Roll log." |

Het derde lost zichzelf op: de korte tekst komt uit `manifest.json`, en die van 0.3.1 heeft de vaste vorm (GEZIEN in `producten/obsidian-rollwright/manifest.json`). Zodra 0.3.1 uit is en de directory de release heeft opgepikt, staat het goed. De eerste twee kan alleen Thijs veranderen met zijn login. De betekenis is gelijk (niemand wordt misleid), dus ik vraag hem dat niet apart: het staat als klein extra punt bij de lanceerberichten op zijn lijst, voor als hij toch de listing opent, bijvoorbeeld als de nieuwe skins er zijn.

Voorstel, 870 tekens (de alinea's 1, 3 en 4 blijven gelijk aan wat live staat):
- tweede alinea: `Every roll is a small game piece: click it and it tumbles and lands. A natural 20 lands in gold, a natural 1 turns red. Every click goes into a Roll log, grouped by note and session, so a session reads back like a story.`
- slotzin: `All rolling is free. Optional skins are a one-time purchase. No account, no telemetry.`

### Categorieën en plaatjes (GEZIEN op de listing en in lijst-thijs)
- Categorieën: TTRPG, Tables, Sidebar. TTRPG staat erbij, zoals advies 1 vroeg.
- Plaatjes: Daans poster en logboek (2400 bij 1600). Geen skins-plaatje, zoals in run 7.
- Betaaltype: Optional payment. Klopt met de koopknop in de plugin.

## Bijwerking 9 nov 2026 (run 18): de korte tekst loste zichzelf niet op
Door Chris. In run 8 schreef ik hierboven dat de korte tekst vanzelf goed komt zodra de directory een nieuwe release oppikt. **Dat klopt niet** (GEZIEN 8 nov ±23:45 UTC):
- De listing toont in `og:description` nog de tekst van 0.3.0: "Roll dice inside your notes with a full formula notation, draw from tables, lists, sections and tags, and keep a history of every roll."
- Dezelfde tekst staat in `community-plugins.json` van obsidianmd/obsidian-releases, die een bot ongeveer elk uur vanuit de directory bijwerkt (op 8 nov ontbraken enkele uren) (Rollwright erin sinds commit 7fd922de, 8 nov 13:20 UTC; nog zo in 320491c9, 23:20 UTC). Daaruit leest de lijst in de app (GOK: niet in de code van de app nagekeken), achter elke nieuwe plugin staat " - This plugin has not been manually reviewed by Obsidian staff."
- manifest.json 0.3.2 heeft de vaste vorm, en de listing toont al "Current version 0.3.2" (scan volgens de hoofdchat om 23:02), maar de korte tekst bleef oud. Het is het veld Short description dat Thijs bij de aanmelding invulde. Alleen met zijn inlog aan te passen.

**Wat nu:** stap 1 op lijst-thijs: de tekst van manifest 0.3.2 letterlijk op de listing. Stap 2 (advies 29, voor Olaf bij 0.3.3): "random tables" en "TTRPG" in de korte tekst, overal tegelijk. Voorstel van 209 tekens:
`Roll dice and random tables right in your notes, for TTRPG game masters and solo players. Click to roll again. A natural 20 lands in gold. Draw from lists, sections and tags, and keep your rolls in a Roll log.`

**Voortaan:** bij elke release waarin de korte tekst verandert, de Short description ook op de listing laten zetten, in de vaste stap "Check for new releases" van Olaf.

## Bijwerking 9 nov 2026 (run 31): Polar en dortus.com gelijk met de skins van 0.3.4
Opdracht: besluit Thijs 9 nov 12:55, "Polar-pagina gelijk met de skins van 0.3.4". Sinds 0.3.4 kleurt een betaalde skin de hele notitie, niet alleen de dobbelstenen.

**Zo staat het nu (GEZIEN ±14:45 UTC, met curl op de openbare afrekenlink uit `src/pro/license.ts`):** product Rollwright Skins, $6 eenmalig (`is_recurring: false`, `price_amount: 600`), geen plaatjes (`medias` leeg), beschrijving: `Two extra looks for the Rollwright dice roller in Obsidian: Parchment and Arcane. One payment, one license key for all your devices. All rolling features stay free.` Die zin klopt nog, maar verkoopt de skins als "looks" van de dobbelstenen; wat een koper sinds 0.3.4 echt krijgt, staat er niet in.

**Nieuwe beschrijving voor Polar** (zelfde woorden als de README van 0.3.4, "Paid skins"):

`Two optional skins for the Rollwright dice roller in Obsidian: Parchment and Arcane. A skin changes more than the dice: Parchment turns a note with rolls into old parchment, Arcane into a torch-lit dungeon, and the Roll log follows. The rest of Obsidian keeps your theme. One payment, one license key for all your devices. All rolling features and the Classic skin stay free.`

Plaatjes: de drie van Daan (`ontwerp/rollwright/wereld/polar/`), in zijn volgorde. Beide stappen kan alleen Thijs met zijn inlog; samen op lijst-thijs onder het punt van Daan.

**dortus.com/rollwright/ (zelf gedaan, repo dortus):** het deel "Optional skins" had nog het oude plaatje (alleen tokens, "night-sky token") en zei niets over de notitie. Nu: tekst gelijk aan de README van 0.3.4 (Parchment oud perkament, Arcane een kerker bij fakkellicht, de Roll log volgt, de rest van Obsidian houdt je thema, de instelling "Skin the note too" met notes with rolls, all notes of off; namen nagekeken in `src/ui/settings.ts` en `src/ui/note-world.ts`), plaatje `skins-worlds.jpg` (Daans "One note. Three worlds.", 1600 x 900) met de alt-tekst van de README, onderschrift "One note, three worlds." De bedankpagina zegt bij stap 3 nu dat de hele notitie verandert en welke instelling dat regelt. Getest op 390 en 1280 breed zonder zijwaarts scrollen (GEZIEN). Het oude `skins.jpg` blijft in de map staan, niets verwijderd; het wordt niet meer gebruikt en kan later weg.

Controleur (run 31): akkoord mits. Moet: hoofdletters van de drie keuzes zoals in de app, juiste meettijd. Kan: zin "The rest of Obsidian keeps your theme" en Classic gratis in de Polar-tekst, notitie over het oude plaatje. Alles verwerkt.
