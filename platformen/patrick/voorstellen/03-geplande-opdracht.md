Wat verandert: elke geplande taak krijgt dezelfde korte opdracht (±12 regels, alleen naam, rol en map verschillen). Alles wat verandert (taken, team, prioriteit, leeslijst) staat alleen nog in de rol, in `organisatie/nu.md` of in `status.md`. Plus een sjabloon voor `status.md` en een nieuwe vorm voor `organisatie/geplande-taken.md`.
Waarom: de huidige opdrachten (gezien met list_triggers, 9 nov 23:30 NL) zijn verouderd: Olaf krijgt nog "eerst alleen de ideefase, Thijs kiest", Hans "nieuwe platformen zijn nu de hoofdzaak", Tess "bouw pas na een ja van Hans" en "elke 3 uur". Anthropic: een geplande prompt moet op zichzelf staan en zeggen wat klaar is (bron 18); bij tegenspraak kiest Claude willekeurig (bron 7).

---

## A. De opdracht (zelfde tekst voor iedereen, vul de drie haakjes in)

```
Vaste toestemming van Thijs, eigenaar van Dortus: je mag alles doen wat nodig is voor het werk van Dortus zonder het eerst te vragen: alles lezen wat openbaar is (rustig, bij anderen alleen lezen), lezen en schrijven in de repo's van thijsduinhouwer2002-coder volgens de afspraken in CLAUDE.md, die repo's koppelen met push, GitHub Actions starten, en uitbrengen als de test groen is en de ontwerper akkoord gaf. Nooit: inloggen op mijn accounts of accounts aanmaken, betalen, bankgegevens, ID-nummers of wachtwoorden invullen, voorwaarden accepteren, andermans spullen verwijderen, of posten onder mijn naam.

Staat dortus-hq er al, gebruik die. Zo niet, koppel met add_repo (owner thijsduinhouwer2002-coder, repo dortus-hq, access push) en kloon hem (--depth 50 is genoeg). Andere repo's alleen koppelen als je taak erom vraagt.

Je bent <NAAM>, <ROL> van Dortus. Volg CLAUDE.md in dortus-hq precies: daar staat wat je leest, hoe je werkt en hoe je afsluit. Je rol staat in organisatie/rollen/<ROLBESTAND>.md, je stand in <MAP>/status.md.

Webpagina's lees je met curl in Bash, nooit met WebFetch. WebFetch vraagt om toestemming en dan staat alles stil. Zet die zin letterlijk in de opdracht van elke agent die je inzet. Gebruik nooit de koppelingen Gmail, Trello, Atlassian, Claude Docs, Search1API of Polar, ook niet als ze in je run beschikbaar zijn.

Klaar is: één taak uit je status.md af en opgeslagen, of in twee regels waarom niet. Werk hooguit 45 minuten.

Afsluiten, harde eis: sluit pas af nadat `git ls-remote origin main` (of je tak) jouw laatste commit laat zien. Zet hash en uitkomst in je eindantwoord. Lukt opslaan niet: zet de volledige nieuwe bestanden in je eindantwoord en zeg in je laatste zin dat het niet is opgeslagen.
```

Waarom zo: de toestemming, de curl-zin, de koppelingen en het afsluiten moeten in de opdracht staan omdat die vóór het klonen nodig zijn (de curl-zin en koppelingen ook omdat agents CLAUDE.md niet lezen). Al het andere staat op één plek in de repo. Een besluit van Thijs werkt dan door zonder 8 opdrachten aan te passen.

## B. Sjabloon `platformen/<map>/status.md` (hooguit 25 regels, eigenaar overschrijft hem elke run)

`status.md` bestaat al: de rol platformmanager zegt "maximaal 10 regels". In de praktijk: blender 61, obsidian 65, verkenner 63, pionier 84 regels (GEZIEN, 9 nov). Geen nieuw bestand dus, wel een vaste vorm en echt kort houden. Daarmee wordt status.md het startpunt van elke run in plaats van taken.md plus logboek.

```
# Stand <product of rol>
Bijgewerkt: <datum tijd> door <naam>

Doel nu: <één zin, bijvoorbeeld: Het Hol speelbaar en mooi genoeg voor Thijs>
Lanceerdatum (richt): <datum>
Cijfers: installs <n> | verkopen <n> | euro's <n> (GEZIEN, datum)

Laatste uitkomst: <wat is er af, met commit of run-id>
Volgende taak: <één taak, zo klein dat hij in één run af kan>
Daarna: <hooguit drie>
Wacht op: <naam of Thijs, sinds wanneer> (leeg als niets)
Twee runs mislukt op: <taak> (dan staat hij op de lijst van Thijs of bij Hans)
```

Het oude `taken.md` en `logboek.md` blijven bestaan voor wie meer wil terugzien, maar niemand hoeft ze aan het begin van een run te lezen.

## C. Nieuwe vorm `organisatie/geplande-taken.md`

Alleen een tabel (naam, rol, schema, map, id, aan/uit) plus de opdracht hierboven één keer. Bij elke wijziging met create_trigger of update_trigger werkt dezelfde run dit bestand bij, in dezelfde commit. Regel in `regels.md`: "Wie een geplande taak aanmaakt, wijzigt of uitzet, werkt geplande-taken.md en dashboard/ploeg.json in dezelfde run bij." Nu staan Gijs, Mila, Kees, Lotte en Patrick er niet in en kloppen Sanne en Tess niet.

## D. Herinneringen zonder bevroren stand
De herinnering "Na reset: Chris en Daan terug naar elk uur" (11 nov) noemt een stand die al twee keer veranderd is. Schrijf in herinneringen nooit wie er draait, maar: "lees organisatie/nu.md en beslis dan".
