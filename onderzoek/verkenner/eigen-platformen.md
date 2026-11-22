# Onze eigen platformen, officieel gescoord

Vera, 8 nov 2026 run 19:31 (Amsterdam). Opdracht van Thijs (8 nov 19:22): Obsidian, JetBrains en Blender een cijfer geven met de lat van nu. **Bereik en geld wegen even zwaar. Geld = wordt er aantoonbaar betaald aan kleine makers.** Een 7 is top, een 6 is het serieus waard.

Nagekeken door de controleur (8 nov 19:55): cijfers JetBrains kloppen precies, 12 correcties verwerkt, cijfers 7, 5 en 4 blijven.

Labels: GEZIEN (zelf gemeten, met bestand of link), DERDEN (bron van een ander), GOK.

## Uitkomst in één tabel

| Platform | Bereik | Geld | Cijfer | Advies |
|---|---|---|---|---|
| **Blender** | sterk | aangetoond (verkooptellers) | **7** | hoofdplatform, uitbreiden |
| **JetBrains** | middel | betaling ingebouwd, bedragen niet zichtbaar | **5** | blijven, uitbreiden alleen met bewijs per niche |
| **Obsidian** | middel tot goed, lager dan gedacht | bijna niet aangetoond | **4** | onderhouden, geen nieuwe plugins zonder bewijs |

Dit past bij het focusbesluit van Thijs van 8 nov (Blender eerst, Obsidian alleen bij aantoonbaar betalen). Er is geen nieuw feit dat dat besluit omgooit.

## Blender: 7 (blijft 7)

**Bereik (GEZIEN, meting 6 nov):** gratis add-ons op extensions.blender.org van mei tot aug 2026 halen ±1.000 tot 1.500 downloads, elke add-on 100+.

**Geld (GEZIEN, meting 7 nov op Superhive, 3.166 pagina's):** betaalde add-ons van 2 tot 6 maanden oud (n=316, 238 makers): mediaan onder 10 verkopen, 31% 10+, 7% 100+, 5% (16 add-ons van 14 makers) ±$300+ netto per maand (bedrag GOK op GEZIEN teller). Voorbeelden: Smart Remesh ($17, 2.500+ verkopen in 3 maanden), Forge CAD ($49, 300+ in 4 maanden). Bron: `voorstellen/blender.md`.

**Sinds 7 nov:** niets nieuws gemeten dat het cijfer verandert. Click Joints (Bram) is in de maak, nog geen eigen verkoopcijfer.

**Tegen:** markt krimpt sinds 2022 (DERDEN, autotroph.com, 18 feb 2026), afdracht 30% op het gratis plan (DERDEN, superhivemarket.com/pricing), mediaanprijs $14, winnaars $17 tot $49 eenmalig (GEZIEN, Superhive-meting 7 nov).

**Waarom 7:** het enige van de drie waar we zelf zagen dat nieuwe betaalde producten van kleine makers verkopen, en het bereik is het hoogste. Eenmalig, maar wel bewezen.

**Wat het cijfer verandert:** de herhaalmeting op Superhive (±5 dec, `data/superhive-haal-script.py`): stijgen de tellers niet, dan 6. Eigen verkopen van Click Joints na 30 dagen zijn het sterkste bewijs.

## JetBrains: 5 (eerste officiële cijfer)

**Bereik, eigen meting vandaag (GEZIEN):** alle 897 betaalde en freemium plugins (539 PAID, 358 FREEMIUM) met de leeftijd uit de oudste versie (`/api/plugins/<id>/updates`, pagina's van 100). JetBrains zelf niet meegeteld.
- 3 tot 6 maanden oud: n=86 (52 makers, 51 betaald, 35 freemium). **Mediaan 272 downloads, 81% haalt 100+**, 27% 1.000+.
- 3 tot 9 maanden oud: n=192 (95 makers). Mediaan 323, 85% 100+, 28% 1.000+.
- Let op: downloads zijn geen gebruikers. Elke update en elke proefversie telt mee. Eerder schatte Jet ±70 echte gebruikers per 100 downloads (`platformen/jetbrains/status.md`). Makers met reeksen tellen meerdere keren mee: in het cohort van 3 tot 9 maanden zit bijvoorbeeld Gerry Themes met 12 thema's uit april. Voor alle nieuwe plugins (vooral gratis) was de mediaan 111 en 54% 100+ (GEZIEN, 6 nov).
- Data: `data/jetbrains-betaald-cdate-2026-11-08.jsonl`, `data/jetbrains-betaald-eerste-versie-2026-11-08.jsonl`; scripts `data/jetbrains-cohort-haal-script.py`, `data/jetbrains-eerste-versie-script.py`, `data/jetbrains-cohort-analyse-script.py`. Het veld `cdate` van de plugin zelf is géén eerste publicatie (Wolfram Language, al jaren oud, stond op 7 maanden); daarom de oudste versie gebruikt.

**Drukte (GEZIEN):** nieuwe betaalde en freemium plugins per maand (eerste versie): ±25 tot 45 per maand van jan tot aug 2026, september 76, **oktober 182**. Het aantal nieuwe betaalde plugins per maand is vier keer zo hoog, maar het aantal makers alleen ongeveer verdubbeld (±16 tot 24 per maand tot augustus, 44 in oktober). Bijna de helft van oktober (84 van 182) komt van 3 makers die reeksen uitbrengen: ReadyStack 29, Oskuvi 28 en KITSS TECH 27 (GEZIEN, controleur). De mediaan downloads van de oktoberplugins is 40 (nog jong). Of die reeksen met AI gemaakt zijn, is een GOK.

**Geld:**
- Betaling zit in de winkel zelf, ook abonnementen, maker houdt 85% (GOK op eigen notitie in `organisatie/doelen.md`, bron niet opnieuw nagelezen). Prijzen van $19 tot $120 per jaar persoonlijk, zakelijk 2 tot 5 keer zoveel (GEZIEN, `platformen/jetbrains/data/betaalbereidheid-scan-2026-11-08.md`).
- Van 46 betaalde plugins in juli 2020 naar 539 nu (DERDEN, blog.jetbrains.com 2020; GEZIEN nu). Solomakers houden betaalde plugins jaren bij (BashSupport Pro, Nginx Configuration Pro, OrchidE sinds 2019).
- **Maar: geen enkel bedrag van een kleine maker gevonden (GEZIEN, onderzoeker vandaag).** JetBrains maakt geen uitbetalingen bekend, op TrustMRR staat geen JetBrains-plugin (12.429 namen in de sitemap doorzocht), makers als Ansorg en meanmail delen geen omzet. Verkopen zijn in de winkel niet te zien.
- Dat makers jaren blijven bijwerken en steeds nieuwe betaalde plugins uitbrengen (meanmail heeft er meerdere), wijst op verdiensten, maar is geen bewijs (GOK).

**Past bij ons:** beste van de drie met de koers van 8 nov: professionals, terugkerend probleem, jaarlicentie. Bison & Flex is geüpload en zit in moderatie (0 downloads, GEZIEN 17:55 UTC). Accounts, upload en betaalroute staan.

**Waarom 5 en geen 6:** bereik is redelijk (beter dan de gratis mediaan, maar opgeblazen door updates en proeven), geld is mogelijk en past bij ons, maar niet aantoonbaar bij kleine makers, en het aanbod groeit nu ineens hard, al komt dat vooral van een paar reeksmakers. Op de lat van nu is dat een 5.

**Wat het cijfer verandert:**
- Ons eigen verkooprapport van Bison & Flex (JetBrains geeft makers verkoopcijfers): het eerste echte cijfer van proef naar betaald op dit platform. 1 betaalde licentie per 30 proeven of beter: 6.
- 2 kleine makers die een bedrag per maand delen boven $300 (bijvoorbeeld via een TrustMRR-API-sleutel of een maker vragen).
- De golf zet door met meer makers (60+ nieuwe betalende makers per maand, niet alleen meer plugins van dezelfde reeksmakers) zonder dat de mediaan stijgt: 4.

## Obsidian: 4 (eerste officiële cijfer)

**Bereik (GEZIEN, meting 5 en 6 nov):** nieuwe plugins mediaan 213 tot 364 downloads, 68 tot 88% haalt 100+. **Maar dat is te hoog:** tot ±1 nov zaten er veel nepdownloads in de tellers; het hele register kreeg na 3 nov 17,5% minder downloads per dag, en kleine plugins merkten het het sterkst (Bases Power Pack 27 naar 4 per dag, GEZIEN door Olaf, `platformen/obsidian/volgend-product.md`). Een maker op het forum noemt 38% nep (DERDEN, forum.obsidian.md/t/121588). De echte mediaan ligt dus lager, hoeveel is niet opnieuw gemeten (GOK: een kwart tot de helft lager). Vandaag (GEZIEN): de 600 nieuwste plugins hebben mediaan 27 downloads (36 hebben nog geen telling en zijn als 0 meegeteld; zonder die 36 is de mediaan 28), maar die zijn nog maar dagen tot weken oud. Rollwright: 4 downloads op dag 1 (GEZIEN, `platformen/obsidian/status.md`).

**Geld:**
- Geen kassa: Obsidian zegt zelf "not a store, and does not offer any built-in payment solutions" (GEZIEN, obsidian.md/blog/future-of-plugins). Betalen gaat via een eigen winkel en een licentiesleutel.
- **Eigen meting vandaag (GEZIEN):** van de 600 nieuwste plugins noemen er 11 een licentiesleutel of een winkellink in de README (8 makers). Na het lezen van die README's (controleur) vragen er maar 4 echt geld voor de plugin: Vault Locker ($5 eenmalig, Lemon Squeezy), World Calendar Notes (Gumroad), bz Reader (afdian) en onze eigen Rollwright. Dat is 3 van 599 bij anderen, ±0,5%. Van de rest zijn 3 donatielinks (één maker), 2 verkopen een ander product (één maker) en 2 zijn valse treffers. De grootste betalende is bz Reader met 191 downloads (GEZIEN). 39 noemen woorden als "premium" of "subscription", vaak voor een dienst van een ander. Data: `data/obsidian-nieuwste600-betaal-2026-11-08.jsonl`, script `data/obsidian-betaal-readme-script.py`.
- Betaalde lagen bestaan alleen bij een paar grote AI-plugins: Copilot for Obsidian Plus $14,99 per maand (3,3 miljoen downloads, Brevilabs), Smart Connections Pro $30 per maand (1,3 miljoen) (GEZIEN, obsidiancopilot.com/en/pricing en smartconnections.app/pro-plugins). **Geen omzet of klantaantal bekend.**
- Donaties zijn klein: QuickAdd 249 supporters en 9 leden, Kanban 220 supporters, Templater 4, in totaal over jaren, bij plugins met 2 tot 6 miljoen downloads (GEZIEN, buymeacoffee.com).
- Geen Obsidian-plugin op TrustMRR (GEZIEN, sitemap). Labels "Paid" en "Optional payment" bestaan in de directory, maar zijn niet openbaar te tellen zonder de zoekfunctie van de site (niet gedaan).

**Waarom 4:** bereik is het beste deel (ook na de nepdownloads waarschijnlijk boven de gratis JetBrains-mediaan van 111; niet te vergelijken met het betaalde JetBrains-cohort), maar geld is op de lat van nu bijna nul: geen kassa, ±0,5% van de nieuwe plugins van anderen verkoopt een licentie, en van geen enkele kleine maker is een bedrag bekend. Bereik zou een 6 tot 7 zijn, geld een 1 tot 2; samen een 4.

**Wat het cijfer verandert:**
- Rollwright verkoopt skins: elke verkoop is het eerste GEZIEN-bewijs. 10+ verkopen in de eerste 30 dagen: 5.
- Een kleine maker die een maandbedrag deelt boven $300 met een Obsidian-plugin.
- Obsidian bouwt zelf een kassa of een betaalde laag in de directory: opnieuw meten.

## Wat dit betekent voor de ploeg
- Blender blijft het sterkste: daar is geld van nieuwe kleine makers gezien. Meer producten daar (Click Joints, de print-add-ons van Olaf) is de beste inzet.
- JetBrains: Bison & Flex afmaken en het eigen verkooprapport goed lezen; dat is de meting die geen buitenstaander kan doen. Een tweede product alleen in een niche met bewijs van betalen (zoals Jet nu al doet).
- Obsidian: Rollwright onderhouden en de skinverkoop meten. Geen nieuwe plugin zonder GEZIEN-bewijs van betalen bij concurrenten (besluit Thijs 8 nov).

## Hoe gemeten en wat niet lukte
- JetBrains: Marketplace-API met curl, 897 plugins, 8 nov 18:40 tot 18:50 UTC.
- Obsidian: README's via raw.githubusercontent.com en community-plugin-stats.json, 8 nov 18:45 UTC.
- Onderzoeker (agent): TrustMRR-sitemap, prijspagina's, Buy Me a Coffee. github.com (Sponsors) gaf 403, Reddit 403, zoekmachines blokkeerden; daardoor bijna geen uitspraken van makers gevonden. Dat kan later met GitHub Sponsors-pagina's of een TrustMRR-API-sleutel.
