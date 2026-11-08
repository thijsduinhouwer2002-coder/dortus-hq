# Betaalbereidheid-scan: waar betalen mensen al, en waar is een gat? (8 nov 2026)

Onderzoeker voor Jet. Alles met `curl` (en `gh api` voor GitHub), alleen gelezen.
**Labels:** GEZIEN = zelf gemeten op 8 nov, met bron. GOK = schatting of oordeel.

## Methode (kort)

1. Alle betaalde en freemium plugins opgehaald: `https://plugins.jetbrains.com/api/searchPlugins?max=20&offset=N&pricingModels=PAID|FREEMIUM&orderBy=downloads`. Uitkomst: **897 plugins** (539 betaald, 358 freemium, zelfde aantallen als op 6 nov).
2. Per plugin `/api/plugins/{id}/updates?page=1&size=100` (nieuwste 100 versies) en `/api/plugins/{id}/rating`. Daaruit: laatste versie en datum, until-build, of er een versie is die in 262 en 263 werkt (open until telt als ja), downloads van versies uit de laatste 90 en 365 dagen, sterrenstemmen, gemiddelde, aantal 1- en 2-sterren.
3. Ruwe lijst: `betaalbereidheid-scan-2026-11-08.tsv` (alle 897, gesorteerd op downloads van versies uit de laatste 90 dagen). Script: `betaalbereidheid-scan-2026-11-08.py`.
4. Filter op taal, bestandssoort of viewer (tags Programming Language, Viewer, Completion, Formatting, Inspection; zonder thema's en AI): 306 plugins. Daarin gezocht naar (a) veel gebruik plus (b) een gat: veel lage sterren, werkt niet in 263, of klachten over prijs.
5. Voor de beste kandidaten: `meet-betaald-2026-11-06.py` (prijs, versies), `/comments` (letterlijk geciteerd), zoeken naar concurrenten (`/api/searchPlugins?search=...`), YouTrack (`https://youtrack.jetbrains.com/api/issues?query=summary: <woord>&fields=idReadable,summary,votes,resolved`) en GitHub (`gh api -X GET search/code -f q=...`, schatting van GitHub).

**Let op bij alle cijfers:** elke update telt als download, dus plugins met veel versies lijken groter. Wat een freemium-plugin echt verkoopt, is nergens te zien. "Betaalbereidheid" is hier dus: een betaalde plugin wordt aantoonbaar geïnstalleerd, gebruikers schrijven over betalen, en de prijs is bekend.

**Nagekeken (controleur, 8 nov 16:10 UTC): akkoord ja.** OrchidE, ExcelEditor en PY-23226 kloppen met de API, citaten letterlijk. Let op: het veld `meanRating` uit `/rating` is niet het gemiddelde van de plugin (bij beide 4,06); reken het gemiddelde altijd uit de stemmen, zoals hier gedaan.

## Uitkomst in één tabel

| # | Niche | Betaald aanbod (GEZIEN) | Gebruik (GEZIEN) | Gat (GEZIEN) | Vraag elders (GEZIEN) | Oordeel |
|---|---|---|---|---|---|---|
| 1 | **Ansible** (playbooks, rollen, vault) | OrchidE $59/$119 per jaar; Ansible Pro (freemium) $39/$79 | OrchidE 355.579 totaal, +129 sinds 6 nov; versies uit 2026 samen ±12.000; Ansible Pro 2.413 in 90 dagen, +143 sinds 6 nov | OrchidE gemiddeld 3,04 uit 54 stemmen, 23 keer 1 of 2 sterren, klachten over prijs, crashes, YAML-kaping; gratis plugins oud of kapot | YouTrack PY-23226 **49 stemmen**, IDEA-210328 16, FL-12753 11 (alle open); GitHub 562.176 `.yml` met `ansible.builtin` | **sterk (vraag en betaling), maar bezet door twee betaalde** |
| 2 | **Excel/XLSX bewerken** | ExcelEditor freemium $39 pers / **$390** zakelijk per jaar; XLSX Lens freemium $2,90/mnd | ExcelEditor 316.316, versie maart tot juli 2026 alleen al 18.584 | 6 van 14 stemmen 1 ster; "edit cells? Not even add rows"; kaapt CSV | YouTrack DBE-20824 2 stemmen; GitHub 120.064 `.xlsx` | **dun** |
| 3 | **HDL** (Verilog, SystemVerilog, VHDL) | SystemVerilog Studio $100/$500; WJCDX Verilog $69/$169, SV $79/$179, VHDL $69/$169 | klein: nieuwste versies 124 tot 663 downloads in maanden | duur, "doesn't do anywhere near enough to justify the cost"; gratis Verilog support uit 2018 | YouTrack bijna niets (CPP-19462, 5 stemmen); GitHub 2.150.400 `.sv`, 1.521.664 `.vhd` | **dun** |
| 4 | Wolfram Language | $120/$480 per jaar | 132.479 totaal; nieuwste versie 1.498 in 7 maanden | until 262.\*, werkt nog niet in 2026.3 (3 dagen oud) | YouTrack 0; GitHub 23.136 `.wl` | **nee** |
| 5 | QML (Qt) | QmlEditor betaald, 1,4 gemiddeld | 31.346 | verlaten sinds 2023 | gat al gevuld door gratis **QML van JetBrains** (1.039.115) | **nee** |
| 6 | Latte (Nette) | Latte Pro $50/$90 | 8.689 | 3,36 gemiddeld, CPU-klachten | gat gevuld door gratis Latte (29.205, 3.946 in 90 dagen) | **nee** |

## Per niche het bewijs

### 1. Ansible

**Betaald aanbod en gebruik (GEZIEN):**
- OrchidE - Ansible Language Support (id 12626), betaald, 30 dagen proef, **$59 persoonlijk / $119 zakelijk per jaar** (`/api/marketplace/plugin/12626/prices?countryCode=US`). 355.579 downloads (op 6 nov 355.450 volgens `marktmeting-2026-11-06.md`, dus +129 in ±2 dagen). 109 versies sinds 2019, dus het totaal is opgeblazen door updates. Versies uit 2026 (`/updates`): 5.006 (feb), 1.555 (mei), 2.845 (mei), 752 (aug), 1.847 (sept), samen ±12.000. Nieuwste versie werkt t/m 263.\*, bijgewerkt 3 sept 2026.
- Sterren (`/rating`): 16 keer 5, 9 keer 4, 6 keer 3, 7 keer 2, **16 keer 1**. Gemiddeld 3,04 uit 54 stemmen. Dat is van alle betaalde taalplugins het hoogste aantal lage stemmen.
- Ansible Pro (31743, maker meanmail.dev, die ook Nginx Configuration en Pro maakt), freemium, $39/$79 per jaar, sinds 13 mei 2026, 11 versies, 4.582 downloads (4.439 op 6 nov in `maker-meanmail-2026-11-06.tsv`, dus +143), 2.413 in versies uit de laatste 90 dagen. 1 review.

**Klachten bij OrchidE, letterlijk (GEZIEN, `/api/plugins/12626/comments`):**
- "Probably good but too expensive. Will not buy." (jan 2026, 2 sterren)
- "This plugin is junk. After less than 30 minutes trial is crashed PyCharm ... did not understand jinja2 templates properly ... generated TONS of incorrect "ansible" error" (okt 2025, 1 ster)
- "the price is a bit too much for what it does. Also it is weird to see it warn me about ansible.builtin.systemd_service not existing" (juni 2025, 2 sterren)
- "Far too expensive for what it does." (dec 2024, 1 ster)
- "it clashed with other yaml files e.g. my Kubernetes manifests" (juli 2024)
- Positief, en belangrijk voor betaalbereidheid: "Absolutely worth the price if you regularly work with Ansible" (nov 2023), "The only ansible plugins I know of, which actually supports ansible roles" (april 2024).

**Gratis aanbod (GEZIEN):** YAML/Ansible support (7792, 724.030) laatste versie okt 2020, until 222, dus werkt niet meer; klachten "hijacks all YAMLs and kills all Kubernetes support". Ansible (14893, 196.943) laatste versie 3 maart 2025, until open; reviews "Does not work on Phpstorm 2025.2" (dec 2025), "doesn't support the full module name ... ansible.builtin.include_role" (maart 2026). Losse vault- en lint-plugins (Ansible Vault Editor 108.524, Ansible Lint 90.489).

**Vraag (GEZIEN):** YouTrack PY-23226 "Ansible integration/support" 49 stemmen open, IDEA-210328 "Provide Ansible support" 16 open, FL-12753 "Native Ansible support" 11 open, IJPL-64506 "Support of ansible LSP" 5. GitHub: 562.176 `.yml`-bestanden met `ansible.builtin`, 67.968 keer `ansible.cfg`.

**Oordeel: sterk bewijs van betaalbereidheid, zwak gat (GOK voor het oordeel).** Mensen betalen aantoonbaar $59 per jaar voor Ansible, er zijn de meeste klachten van alle betaalde taalplugins, en JetBrains heeft het zelf niet (49 stemmen). Maar: (1) er zijn al twee betaalde plugins, waarvan Ansible Pro van een productieve maker die net is begonnen en elke paar weken uitbrengt; (2) Ansible is YAML met betekenis, geen eigen extensie, dus de IDE raadt geen plugin aan bij `.yml` en we missen de gratis aanloop die BatchCraft wel heeft (GOK); (3) het werk is groter dan een grammatica: modules, rollen, variabelen, Jinja2 in YAML. Alleen te doen als we bewust een betere en goedkopere OrchidE bouwen.

### 2. Excel/XLSX bewerken in de IDE

**Betaald aanbod en gebruik (GEZIEN):** ExcelEditor (18663, maker Observer & Creator, die ook de gratis ExcelReader met 1.242.777 maakt), freemium, $39 persoonlijk / $390 zakelijk per jaar, geen proef. 316.316 downloads, 48 versies; versie 2026.3.1 (maart tot juli) 18.584 downloads, 2026.7.1 2.947, nieuwste 2026.11.1 (until 263.\*) 638. Sterren: 7 keer 5, 1 keer 2, 6 keer 1 (gemiddeld 3,07). XLSX Lens (33721), freemium $2,90/mnd, 3.664 sinds sept.

**Klachten, letterlijk (GEZIEN, `/api/plugins/18663/comments`):**
- "Wait what? I pay for a plugin where I can... edit cells? Not even add rows and delete them?" (juli 2026, 1 ster)
- "I install and deinstall then my csv files got not seen at all" (mei 2025, 1 ster)
- "hides the fact that you NEED a paid license to use at all (so I guess the "freemium" badge is a straight up lie)" (dec 2023, 1 ster)
- "I don't want the plugin touching CSV files, but I also can't prevent it from doing so." (mei 2024)

**Vraag elders (GEZIEN):** YouTrack geen grote vraag naar een Excel-editor (DBE-20824 meerdere bladen in de XLSX-viewer, 2 stemmen; de grotere Excel-meldingen gaan over export en zijn dicht). GitHub 120.064 `.xlsx`.

**Oordeel: dun (GOK).** Veel installaties en concrete klachten, en het woord "pay" komt voor. Maar we zien niet hoeveel er echt betalen, de gratis ExcelReader van dezelfde maker vangt de kijkers, XLSX Lens zit er al met een lage prijs, en het is een binaire viewer, niet ons grammatica-patroon.

### 3. HDL (Verilog, SystemVerilog, VHDL)

**Betaald aanbod (GEZIEN, prijzen via `/prices?countryCode=US`):** SystemVerilog Studio (14203) $100 persoonlijk / $500 zakelijk, 13.047 totaal, nieuwste versies 124 en 119 downloads (okt 2026). WJCDX: Verilog Language Support (21813) $69/$169, nieuwste versie (maart 2026, until 263.\*) 663 downloads; SystemVerilog Language Support (26514) $79/$179, 319; VHDL Language Support (26267) $69/$169, 396. Nieuw: Hdlwise van KITSS TECH (freemium $10), 33 downloads sinds 9 okt.

**Klachten en signalen (GEZIEN, `/comments`):** SystemVerilog Studio: "It is very good, for what it does, but it doesn't do anywhere near enough to justify the cost ... gave away a 6 month free license" (feb 2026), "Complete trash." (nov 2025). Verilog Language Support: "I will upgrade to a paid license when my free license expires" (juni 2024), "I would pay for it after fix" (nov 2023). Gratis Verilog support (10612): laatste versie 2018, "crashes immediately when opening in 24.1 EAP".

**Vraag elders (GEZIEN):** YouTrack nauwelijks: CPP-19462 "No Vhdl syntax highlighting" 5 stemmen, de rest 0. GitHub wel veel: 2.150.400 `.sv` (deels ook andere soorten, GOK), 1.521.664 `.vhd`.

**Oordeel: dun (GOK).** Hoge prijzen worden gevraagd en gebruikers praten over betalen, maar het gebruik is klein (honderden downloads per versie), er zijn al vier betaalde plugins plus KITSS, en geen stemmen.

### 4. Wolfram Language: nee

Betaald $120/$480 (GEZIEN), 132.479 totaal, maar nieuwste versie 2026.2.0 (april) maar 1.498 downloads in 7 maanden, ±210 per maand (GEZIEN). until 262.\*, dus niet in 2026.3, maar 2026.3 is pas 3 dagen uit en de maker brengt elk jaar uit. Reviews vrijwel allemaal positief. YouTrack 0 stemmen, GitHub 23.136 `.wl`. Kleine, tevreden doelgroep met een bijgehouden plugin.

### 5. QML: nee

QmlEditor (14434), betaald, 31.346, gemiddeld 1,4 uit 10, laatste versie maart 2023, until 231 (GEZIEN). Letterlijk: "the only option I can find for QML support that hasn't been archived. However, this plugin appears to have been abandoned. Do not pay for this plugin" (dec 2022). Maar JetBrains heeft nu zelf een gratis plugin **QML** (25303) met 1.039.115 downloads (GEZIEN, zoeken op `qml`). Gat gevuld.

### 6. Latte (Nette): nee

Latte Pro (19661) $50/$90, 8.689, 7 keer 1 ster: "7 months of payments, stress, frustration, thanks, never again." (maart 2025), "Uses 100% of CPU for several minutes after any change in LATTE file" (feb 2024) (GEZIEN). Maar de gratis Latte van Noctud (24218) heeft 29.205 downloads, 3.946 in versies uit de laatste 90 dagen en 6 keer 5 sterren. Gat gevuld.

## Ook bekeken en afgevallen (GEZIEN, kort)

- **OpenAPI Editor** (12887, betaald, 47.803, until 253): JetBrains heeft gratis OpenAPI Specifications (10,9 mln).
- **SQLFormatter** (22742, betaald, 35.101, until 262): vooral Chinese gebruikers, SQL-opmaak zit al in DataGrip en Ultimate.
- **JetForcer** (9238, Salesforce, betaald, 342.094, until 261, laatste versie juli 2025): verlaten, maar Illuminated Cloud 2 (820.600, eigen licentie) is groot en bijgehouden; markt te groot voor ons.
- **Nginx, Jenkinsfile, Hex, Google Apps Script**: betaald aanbod groeit (Nginx Configuration Pro 9.556 en Hex Editor 10.712 in versies uit de laatste 90 dagen), maar geen gat: bijgehouden, weinig of geen lage sterren.
- **Algemeen (GEZIEN):** van de 897 betaalde en freemium plugins heeft 802 een versie die in 263 kan werken. Betaalde plugins worden dus bijna allemaal bijgehouden; "verlaten en betaald" komt weinig voor, en waar het voorkomt (QML, OpenAPI, Salesforce) heeft iemand anders het gat al gevuld.

## Eerlijk eindoordeel

- **Alleen Ansible haalt "sterk" voor betaalbereidheid**: een betaalde plugin van $59 per jaar met veel gebruik, de meeste klachten van alle betaalde taalplugins, en 49 + 16 + 11 stemmen in YouTrack voor iets wat JetBrains niet zelf levert. Het gat zelf is matig: Ansible Pro zit er sinds mei, het is geen bestandssoort die de IDE aanraadt, en het is veel werk. Mijn advies (GOK): niet als volgende snelle plugin, wel bewaren als grotere kandidaat als Bison & Flex verkoopt.
- **Excel en HDL zijn dun, Wolfram, QML en Latte nee.** Volgens de regel "dun bewijs is nee" levert deze scan dus geen snelle tweede plugin op die beter is dan wat al in `volgend-product-meting-2026-11-08.md` staat (DOT).
- **Bijvangst die DOT steunt (GOK):** de betaalde markt loont waar de IDE een bestand niet kent en een slechte gratis plugin aanraadt. Bij Ansible, Excel en HDL is dat niet zo; bij DOT wel.
