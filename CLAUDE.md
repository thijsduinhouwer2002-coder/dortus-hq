# Dortus HQ: wegwijzer voor elke Claude

Dortus is het bedrijf van Thijs. Een ploeg Claudes bouwt en verkoopt zelfstandig producten op app-platformen. Thijs wil zo min mogelijk gevraagd worden: je beslist zelf, met een reden.

## Starten (in deze volgorde)
1. `bash organisatie/start.sh` (haalt de nieuwste stand op en zet de automatische controle vóór elke push aan).
2. Lees `berichten/<jouw naam>.md`. Nieuwe berichten staan **onderaan**: lees het einde (`tail -c 15000 berichten/<naam>.md`). De nieuwste opdracht gaat voor alles; oudere opdrachten van Thijs vind je met `grep -n "van Thijs"`.
3. Lees je rol in `organisatie/rollen/` en je eigen map in `platformen/`.
4. Lees `organisatie/bord.md` om te weten wie wat doet. **Hoofdchat:** lees het bord voor je Thijs iets over de stand zegt, en werk het bij bij elke wijziging aan een product, agent of belofte.

Meer lees je pas als je het nodig hebt (zie de wegwijzer hieronder).

## Harde regels
1. **Geld uitgeven** alleen na een ja van Thijs. Al het andere beslis je zelf.
2. **De repo is openbaar.** Schrijf nooit persoonsgegevens van Thijs op (adres, woonplaats, telefoon, BSN, ID, bank, geboortedatum, belasting, wachtwoorden, sleutels, account- of partnernummers). Schrijf "staat bij Thijs". De controle `organisatie/controle/check.py` draait vanzelf vóór elke push.
3. **Webpagina's lees je met `curl` in Bash, nooit met WebFetch.** WebFetch vraagt Thijs om toestemming en dan staat alles stil. Zet deze zin letterlijk in de opdracht van elke agent die je inzet.
4. **Niets naar buiten onder de naam van Thijs** (post, mail, bericht) zonder zijn ja op de tekst. Agents plaatsen nooit zelf; de hoofdchat doet het.
5. **Eerlijk:** elk cijfer krijgt GEZIEN, DERDEN (met link) of GOK. Verzin niets. Werk is pas af als een ander het keurde (skill `keuren`) en de tests groen zijn.
6. **Alleen schrijven waar je mag:** je eigen map, je product, een regel onderaan de besluiten, en een bericht onderaan in `berichten/<naam>.md` van een ander (met datum en van wie; nooit iets weghalen). Iets wat alleen Thijs kan, meld je in `berichten/hoofdchat.md`; alleen de hoofdchat zet het op `organisatie/lijst-thijs.md` (max 5). Nooit iets verwijderen wat niet van ons is. Nooit geforceerd pushen.
7. **Gebruik nooit de koppelingen Gmail, Shopify, Trello, Kondo, Atlassian, Claude Docs, Search1API of Polar** (kunnen van iemand anders zijn). Chrome alleen op de HP van Thijs, en alleen de hoofdchat.
8. Schrijf in het Nederlands, in gewone woorden, zonder gedachtestreepjes.

## Wegwijzer: lees dit alleen als je het nodig hebt
| Je gaat... | Lees |
|---|---|
| iets besluiten of terugkomen op een besluit | `organisatie/besluiten.md` (geldende besluiten bovenaan); oudere in `organisatie/archief/` (zoek met grep) |
| onderzoeken, plannen of een idee toetsen | eerst de geldende besluiten bovenaan `organisatie/besluiten.md` (die gaan voor), dan `organisatie/regels/werken.md`, `organisatie/koers-kingmaker.md`, `organisatie/ideeentest.md` |
| bouwen of testen | skill `bouwen-in-stappen`, `organisatie/regels/bouwen.md`, `producten/<naam>/architectuur.md` |
| iets live zetten of een update uitbrengen | skill `uitbrengen`, `organisatie/regels/uitbrengen.md` |
| een winkeltekst, changelog of post schrijven | skill `update-tekst` |
| werk van een ander keuren | skill `keuren` |
| iets zichtbaars af melden (spel, beeld, site, README) | skill `kijken` |
| meldingen, reviews of vragen van gebruikers | skill `triage` |
| iets wat Thijs, zijn accounts of iets openbaars raakt | `organisatie/regels/thijs.md` |
| twijfelen waar je mag schrijven, of iets op dortus.com zetten | `organisatie/regels/opslaan.md` |
| iets moois maken (site, winkelbeelden, menu's, filmpjes) | skill `frontend-design` |
| doelen en geld | `organisatie/doelen.md` |
| een sleutel, account of toegang nodig hebben | `organisatie/toegang.md` |
| alle producten met hun statusbestanden, of de kennisbank van Hats | `START.md`, `platformen/steam/kennisbank/` |

## Afsluiten
Sluit pas af als `git ls-remote origin main` (of je tak) laat zien dat je laatste commit op GitHub staat. Zet de hash in je eindantwoord. Lukt opslaan niet: zet de nieuwe inhoud van je bestanden in je eindantwoord en zeg dat het niet is opgeslagen.
