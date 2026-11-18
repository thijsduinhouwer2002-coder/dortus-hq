# Keuring werkwijze (ombouw 18 nov 19:30), 18 nov 2026, nieuwe agent (testrun als Olaf)
Wat ik keurde: commit 62e4282d ("Werkwijze omgebouwd naar het model van de winnaars"): `CLAUDE.md`, `organisatie/regels/`, `organisatie/besluiten.md`, `.claude/skills/` (keuren, uitbrengen, update-tekst), `.claude/settings.json`, `organisatie/start.sh`, `.githooks/pre-push`, `organisatie/controle/check.py`, `organisatie/sjablonen/agent-opdracht.md`. Vergeleken met `archief/regels-t-m-2026-11-18.md`, `archief/besluiten-t-m-2026-11-18.md` en de oude `CLAUDE.md` (HEAD~1).
Akkoord: nee (8 moet-punten, allemaal klein om op te lossen; de opzet zelf is een grote stap vooruit)

## Testrun: 8 vragen, alleen via CLAUDE.md en de wegwijzer
Start (CLAUDE.md stap 1 tot 4): 5 bestanden open: `CLAUDE.md`, `berichten/olaf.md` (442 regels, 145 KB), `rollen/platformmanager.md` (welke rol bij Olaf hoort moest ik zoeken met grep), `organisatie/regels.md` (de rol stuurt daarheen, is nu een doorverwijzing), `bord.md`. `start.sh` gaf geen pull-melding.

| # | Vraag | Antwoord | Gevonden in | Bestanden open |
|---|---|---|---|---|
| 1 | Click Joints-versie zelf in de winkel? | Als Olaf nee: Click Joints is van Bram (bord), en harde regel 6 laat alleen schrijven in je eigen product. De eigenaar volgt de skill `uitbrengen`: versie gelijk aan CHANGELOG, tests groen op die commit (Actions-API met curl), keuring door een ander plus Daan bij uiterlijk, lanceerlijst, uitbrengen met `click-joints-uitgave.yml`, met curl zien dat het live is, scorebord en bord via de hoofdchat. Maar wie de knop drukt is tegenstrijdig (zie moet 3). | `.claude/skills/uitbrengen/SKILL.md`, `regels/uitbrengen.md`, `bord.md` | 2 nieuw (3 met bord) |
| 2 | AI-beeld of AI-geluid in Hats? Spelerstekst? | Nee, geen AI-beeld of -geluid op Steam. Spelerstekst schrijft Thijs; agents zetten voorstellen als CONCEPT in `platformen/steam/teksten-thijs.md`. | `regels/thijs.md` (ook `besluiten.md`) | 1 |
| 3 | Waar een nieuw besluit, waar het oude over Atlassian? | Nieuw besluit onderaan in `besluiten.md` bij "Nieuwe besluiten", en de regel in het overzicht bovenaan aanpassen als het iets vervangt. Atlassian: `besluiten.md` deel "Platformen" (gestopt 6 nov, bevestigd 18 nov 18:40); volledig in `archief/besluiten-t-m-2026-11-18.md` (grep "Atlassian"). | `besluiten.md` | 1 |
| 4 | Hoe keur ik het werk van Bram? | Skill `keuren`: zelf niets bouwen, alleen oordelen; echt kijken (Read op beelden, testlog, curl op bronnen); formulier met deel A (doet het wat beloofd is) en deel B (regels), elk met feit/vermoeden en zekerheid, dan moet/kan; daarna Iris (spel) of Daan (uiterlijk). | `.claude/skills/keuren/SKILL.md` | 1 |
| 5 | Gmail-koppeling? Chrome? | Gmail nooit (harde regel 7). Chrome niet: alleen de hoofdchat, alleen op de HP van Thijs. | `CLAUDE.md` | 0 extra (maar `regels/thijs.md` geeft een andere lijst, zie moet 8) |
| 6 | Wat voor ik push? | `git pull --rebase`, code op een tak `claude/<platform>-<datum>`, naar main pas na akkoord van de controleur en groene tests, nooit geforceerd. De controle `check.py` draait vanzelf via de hook (na `start.sh`). Daarna `git ls-remote` en de hash in je eindantwoord. | `regels/opslaan.md`, `CLAUDE.md` | 1 |
| 7 | Hoe vaak een update voor een live product? | Elke 2 tot 3 weken een kleine versie. Botst met "geparkeerd, 0 tokens" voor Rollwright en Ebb (zie kan 4). | `regels/uitbrengen.md` | 0 extra (al open) |
| 8 | Koers van Dortus in één zin? | Eerst investeren in wat we hebben: geen nieuw product, de werkwijze van de winnaars toepassen op Hats, Click Joints en Bison & Flex, meten op wo 9 dec (18 nov 18:40). | `besluiten.md` bovenaan | 1, maar de wegwijzer stuurt naar `koers-kingmaker.md` en `doelen.md`, die het tegendeel zeggen (zie moet 4). Ik had 3 bestanden nodig om zeker te zijn. |

Totaal: 5 bestanden voor de start, daarna 7 voor alle 8 vragen. Snel en goed vindbaar; de wegwijzer werkt.

## Steekproef: 15 willekeurige oude besluiten (random.seed 1118 over 256 kopjes en regels)
| Oud besluit | In de nieuwe opzet? |
|---|---|
| 17 nov 05:50 Sem: vaste releasedatum, niet ma 29 mrt | Ja (samengevat; "routekaart 4 vakjes, bazen eruit" alleen in archief) |
| 9 nov 21:20 Thijs: Mila tweede ontwerper, Daan eindakkoord | Nee in `besluiten.md`; Daan-akkoord wel via `regels/bouwen.md` en skill `uitbrengen`. Mila staat uit. Geen probleem |
| 8 nov Vera: cijfers Blender 7, JetBrains 5, Obsidian 4 | Nee; verouderd. Geen probleem |
| 8 nov Hans: Overwolf en BOOTH nog niet klaar | Ja |
| 8 nov Noor: s&box nee | Ja |
| 7 nov Vera: Shopify | Ja |
| 6 nov Verkenner: Setapp nee | Ja |
| 6 nov Vera: Unity Asset Store nog niet klaar | **Nee** (Framer en Godot wel). Een zoeker kan het opnieuw gaan onderzoeken |
| 7 nov Thijs: managers draaien de klok rond | Terecht vervangen (alle agents uit, 18 nov 16:35) |
| 10 nov 14:56 Klopt in de kast | Ja |
| 13 nov 13:35 Het Hol in 3D | Ja |
| 15 nov 19:25 ruwe speeltest 21 nov | Ja ("gaat voor de winkelbeelden" alleen in archief) |
| 15 nov 23:05 hoofdchat komt zelf met ideeën, groeironde elk uur | Deels: compagnon ja; de ronde staat in `hoofdchat-ronde.md`, dat in de wegwijzer niet voorkomt |
| 16 nov 10:35 Ruben: Pro 1.1 | Ja |
| 10 nov 22:52 Thijs: de kwaliteitslat | Deels: punt 4 (kritiek wordt regel) ja, punt 1 terecht vervangen; punt 2 (hoofdchat kijkt zelf naar de echte schermen) niet als regel |

Uitslag: 10 van 15 vindbaar of terecht vervangen, 5 niet of deels. Geen van de 15 is kritiek. Wel belangrijk en buiten de steekproef gevonden: zie deel B punten 1, 9, 10, 11.

Oude regels: elke regel van `archief/regels-t-m-2026-11-18.md` staat letterlijk in `organisatie/regels/` of `CLAUDE.md` (met een script nagelopen), op de bewuste wijzigingen na (besluit "onderaan" in plaats van "bovenaan", WebFetch nu helemaal verboden, "hoofdchat" in plaats van "hoofdmanager"). Er is dus niets weggevallen uit de regels.

## Deel A: doet het wat beloofd is?
(belofte: besluit 18 nov 19:30 in `besluiten.md`)
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| A1 | CLAUDE.md is kort (50 regels), de wegwijzer brengt je in 1 bestand bij elk antwoord. Testrun: 7 bestanden voor 8 vragen | Feit | hoog | |
| A2 | WebFetch staat op deny in `.claude/settings.json`; SessionStart draait `start.sh` | Feit | hoog | |
| A3 | `start.sh` haalt op en zet `core.hooksPath` op `.githooks`; daarna stopt de hook een push met IBAN, mobiel nummer (06-), gmail-adres of gedachtestreepje, ook op een nieuwe tak en in een ondiepe kloon | Feit (getest in `/tmp/keur`, kopie met eigen bare remote) | hoog | |
| A4 | Hook-gat: een bestand met een naam buiten ASCII (bijvoorbeeld `ideeën/mijn notitie.md`) wordt helemaal overgeslagen. Git zet zo'n naam tussen aanhalingstekens (`+++ "b/idee\303\253n/..."`) en `check.py` herkent alleen `+++ b/`. Getest: IBAN, mobiel nummer en gedachtestreepje gingen erdoor en stonden daarna op de remote | Feit | hoog | `git diff -c core.quotePath=false` of `-z` in `check.py` |
| A5 | Hook-gat: een hernoemd bestand met nieuwe regels wordt overgeslagen (`--diff-filter=AM` laat R weg). Getest met een groot bestand plus IBAN: "OK" | Feit | hoog | `--no-renames` toevoegen |
| A6 | Hook-gat: alleen de eindstand van de push wordt getoetst. Commit 1 zet een nummer erin, commit 2 haalt het weg: "OK", en het nummer staat in de openbare geschiedenis | Feit | hoog | per commit toetsen (`git rev-list van..tot`) |
| A7 | Niet gevonden door `check.py`: hotmail-adres, vaste nummers (020-1234567, +31 20 ...), mobiel met spaties (+31 6 1234 5678), BSN, geboortedatum, en-streepje, `sk_live_...`, `github_pat_...`, "wachtwoord: ...". CLAUDE.md belooft bescherming van BSN, geboortedatum en wachtwoorden | Feit | hoog | patronen toevoegen |
| A8 | De hook staat pas aan na `start.sh`; een verse kloon of een sessie buiten de repomap heeft geen controle. `--no-verify` slaat hem over. De GitHub-controle (`controle-openbaar.yml`) draait alleen op main, niet op takken | Feit | hoog | |
| A9 | `start.sh` regel 4: `dirname "$0"/..` geeft `organisatie/start.sh`, geen map. Alleen geraakt als `git rev-parse` faalt, dus klein | Feit | midden | |
| A10 | Het sjabloon voor agentopdrachten is kort en goed, maar zegt "zulke stappen gaan naar `berichten/hoofdchat.md`", wat botst met de regels (moet 1 en 2) | Feit | hoog | |

## Deel B: houdt het zich aan onze regels en zichzelf?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| B1 | **Lijst voor Thijs.** `regels/opslaan.md` (mag "een regel toevoegen aan lijst-thijs.md"), `regels/thijs.md` ("zet zo'n vraag in lijst-thijs.md"), `regels/werken.md` punt 5, skill `uitbrengen` (laatste regel) en `rollen/platformmanager.md` zeggen: schrijf op `lijst-thijs.md`. De kop van `lijst-thijs.md` (Thijs 17 nov), het sjabloon en het bericht aan Olaf van 17 nov 14:45 zeggen: agents zetten daar niets, melden in `berichten/hoofdchat.md`, max 5 punten. Dat besluit van 17 nov staat in geen van beide besluitenbestanden. Daarnaast bestaat `goedkeuren.md` (16 nov 16:59) nog als tweede lijst | Feit | hoog | tegenspraak |
| B2 | **Berichten aan elkaar.** Harde regel 6 en `opslaan.md` laten alleen schrijven in je eigen berichtenbestand ("alleen verwerkt erachter zetten"). De ploeg stuurt elkaar juist berichten in andermans bestand (Bram, Sanne, Daan in `berichten/olaf.md`), en het sjabloon stuurt naar `berichten/hoofdchat.md`. Nergens staat hoe je een bericht aan een ander stuurt | Feit | hoog | tegenspraak, ontbrekende regel |
| B3 | **Wie zet een versie live?** `regels/thijs.md`: "de hoofdchat zet het live ... ook uploads van gekeurde versies". Skill `uitbrengen` stap 5, `regels/uitbrengen.md` ("uitbrengen gaat zonder Thijs" met `publiceer.sh`) en `rollen/platformmanager.md` ("indienen doe je zelf"): de agent doet het | Feit | hoog | tegenspraak |
| B4 | **Koers.** De wegwijzer stuurt wie plant naar `koers-kingmaker.md` (nieuwe platformen, live in 7 dagen) en `doelen.md` (tussenstappen van 6 nov). Het geldende besluit 18 nov 18:40 zegt: geen nieuw product, eerst wat we hebben. `koers-kingmaker.md` noemt dat nergens; `besluiten.md` zegt zelfs dat Kingmaker "voor oudere regels gaat" | Feit | hoog | tegenspraak |
| B5 | **Bord.** Kop: "vaste agents uit"; besluit 18 nov 16:35: alle agents uit. De tabel "Agents" zegt: Olaf aan, elk uur, en 11 anderen aan. Elke agent leest deze tabel bij de start | Feit | hoog | tegenspraak |
| B6 | **Besluiten bovenaan of onderaan:** consequent in de nieuwe bestanden (geldend bovenaan, nieuw onderaan, `opslaan.md` en `overdracht.md` zeggen hetzelfde). De wegwijzer noemt alleen "geldende besluiten bovenaan"; waar een nieuw besluit komt lees je pas in het bestand zelf. Prima | Feit | hoog | |
| B7 | **Wie schrijft in het bord:** consequent "alleen de hoofdchat" (`CLAUDE.md`, `opslaan.md`, skill `uitbrengen` stap 7). Alleen `rollen/hoofdmanager.md` regel 42 zegt nog dat de hoofdmanager het bord bijwerkt. Skill `uitbrengen` stap 7 laat de agent wel `scorebord.md` bijwerken, en dat staat niet in de schrijflijst van `opslaan.md` | Feit | hoog | kleine tegenspraak |
| B8 | **Koppelingen.** Harde regel 7, `start.sh` en het sjabloon: Gmail, Trello, Atlassian, Claude Docs, Search1API, Polar. `regels/thijs.md`: Gmail, Shopify, Trello, Kondo, Claude Docs. Shopify en Kondo zijn uit de harde regel verdwenen. `besluiten.md` Twijfel 10 zegt bovendien dat de overstap naar het eigen account al af is | Feit | hoog | tegenspraak, regel deels weg |
| B9 | **Kennisbank Hats** (besluit Thijs 16 nov 17:59: agents van Hats lezen eerst de inhoudsopgave, `START.md`): staat niet in `besluiten.md` en niet in de wegwijzer. Voor Olaf als Hats-bouwer is dat de belangrijkste leesplek die ontbreekt | Feit | hoog | besluit niet vindbaar |
| B10 | "Liever minder regels" (Thijs 8 nov) en "een 7 op 10 is top, niet te snel afschieten" (Thijs 6 nov) staan niet in `besluiten.md` | Feit | hoog | besluit niet vindbaar |
| B11 | "Elke 2 tot 3 weken een kleine versie" voor elk live product botst met "Rollwright, Ebb, Ebb Calm: geparkeerd, 0 tokens" | Feit | hoog | tegenspraak |
| B12 | `regels/werken.md`: "Vraag Thijs alleen in nood (zie onder)", maar dat stuk staat nu in `regels/thijs.md` | Feit | hoog | losse verwijzing |
| B13 | Skill `uitbrengen` stap 3: Daan alleen als uiterlijk of winkelpagina veranderde; `regels/uitbrengen.md`: alleen uitbrengen "als Daan akkoord gaf". `regels/uitbrengen.md` "eigen openbare repo per product" botst met besluit 18 nov 17:04 (productcode privé), staat al als Twijfel 9 | Feit | midden | kleine tegenspraak |
| B14 | `regels/thijs.md` noemt het device-ID van de Chrome op de HP van Thijs. Geen persoonsgegeven in de lijst van CLAUDE.md, wel een vast nummer van zijn apparaat in een openbare repo | Vermoeden | laag | privacy |
| B15 | Geen gedachtestreepjes en geen persoonsgegevens gevonden in de nieuwe bestanden; regels in gewone woorden | Feit | hoog | |

## Wat ik als nieuwe agent mis
1. **Welke rol en welke map bij mijn naam horen.** `berichten/olaf.md` noemt Olaf "Obsidian-manager", het bord "Hats: hoofdbouwer"; de rol moest ik zoeken met grep, en Olaf heeft drie mappen (`obsidian`, `steam`, `blender-2`). Een tabel naam, rol, map in het bord of in CLAUDE.md lost dat op.
2. **De nieuwste opdracht vinden.** `berichten/olaf.md` is 145 KB. Bovenaan staan berichten van 17 nov (nieuwste eerst), onderaan de koppen van de hoofdchat (nieuwste laatst); de echte nieuwste ("18 nov: je staat uit, plan B geldt") staat op regel 441. CLAUDE.md zegt "de nieuwste opdracht gaat voor alles", maar niet waar die staat.
3. **Wat te doen als ik uit sta.** Besluit: alle agents uit; bericht: "je staat uit, lees dit bij je volgende run". Draai ik dan toch? Eén zin in CLAUDE.md: "Sta je uit (bord of besluiten), stop na het lezen."
4. **Hoe ik een andere agent iets vraag** (zie B2).
5. **`START.md` en de kennisbank** (zie B9), en `hoofdchat-ronde.md` voor de hoofdchat.
6. De harde regel over koppelingen wordt niet afgedwongen: in deze sessie waren Gmail, Atlassian, Claude Docs en Polar gewoon beschikbaar. Een `deny` op die tools in `.claude/settings.json` (zoals bij WebFetch) is goedkoop.

## Moet (blokkeert akkoord)
1. Lijst voor Thijs eenduidig maken (B1): kies `berichten/hoofdchat.md` (zoals Thijs 17 nov), pas `opslaan.md`, `thijs.md`, `werken.md` punt 5, skill `uitbrengen` en `rollen/platformmanager.md` aan, en zet het besluit van 17 nov in `besluiten.md`. Zeg wat er met `goedkeuren.md` gebeurt.
2. Regel voor berichten aan elkaar (B2): mag een agent onderaan in `berichten/<ander>.md` schrijven? Zet het in harde regel 6 en `opslaan.md`.
3. Eén antwoord op "wie zet een versie live" (B3), gelijk in `thijs.md`, `regels/uitbrengen.md`, skill `uitbrengen` en de rol.
4. Bovenaan `koers-kingmaker.md` (en in de wegwijzer bij "onderzoeken, plannen"): "Sinds 18 nov 18:40 geen nieuw product; zie `besluiten.md`" (B4).
5. Agenttabel in `bord.md` gelijk aan besluit 18 nov 16:35 (B5).
6. Pre-push: niet-ASCII-namen, hernoemde bestanden en tussencommits meenemen (A4, A5, A6). Getest en lek in alle drie.
7. Koppelingenlijst gelijk in CLAUDE.md, `thijs.md`, `start.sh` en sjabloon (Shopify en Kondo terug of bewust weg met reden) (B8).
8. In CLAUDE.md stap 2 zeggen waar de nieuwste opdracht staat (bijvoorbeeld: nieuwste bovenaan, ouder dan 3 dagen naar een archief) (gemis 2).

## Kan (mag later)
1. `check.py`: patronen voor andere mailadressen, vaste en gespatieerde nummers, BSN (11-proef), geboortedatum, en-streepje, `sk_live_`, `github_pat_` (A7); GitHub-controle ook op takken (A8).
2. Tabel naam, rol, map (gemis 1) en een stopregel voor agents die uit staan (gemis 3).
3. `START.md` in de wegwijzer bij Hats en de besluiten van 16 nov 17:59, 8 nov ("minder regels") en 6 nov ("7 is top") in `besluiten.md` (B9, B10); Unity Asset Store in de lijst afgewezen platformen.
4. Ritme "elke 2 tot 3 weken" beperken tot de producten die niet geparkeerd zijn (B11).
5. Losse eindjes: "zie onder" in `werken.md` (B12), `hoofdmanager.md` regel 42 en `scorebord.md` in de schrijflijst (B7), Daan-regel gelijk trekken (B13), `dirname`-fout in `start.sh` (A9), device-ID uit `thijs.md` (B14).
6. Deny op Gmail, Atlassian, Claude Docs, Polar, Trello en Search1API in `.claude/settings.json` (gemis 6).
