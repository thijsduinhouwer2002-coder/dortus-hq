# Keuring opruimen fase 2, 22 nov 2026, keurder (losse Claude, bouwde niets)
Wat ik keurde: commits 17605dfd, 7c385090, c8c429ad, 69ea1bd1, 25929e93, 1950481e en ca48a202 op main (en kort a097e163 van de hoofdchat), getoetst op main a097e163 (22 nov ±11:00 NL). Getoetst tegen `organisatie/opruimen/voorstel-2026-11-19.md`, het besluit van Thijs 19 nov 17:31 (`besluiten.md` r165), het verslag `organisatie/opruimen/fase2-2026-11-22.md` en `organisatie/archief/verhuizingen.md`.
Akkoord: nee (één moet-punt: de release zet ruwe winkeldumps met ±1.100 mailadressen van anderen opnieuw openbaar; de verhuizing zelf is in orde)

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| A1 | **Verhuistabel klopt met wat er echt gebeurde.** 69ea1bd1 en 25929e93 hebben samen precies 536 hernoemingen (`git show -M --name-status`, 512 keer R100, de rest R095 tot R099 door bijgewerkte paden in de bestanden zelf). Elke regel uit de tabel in het verslag en in `verhuizingen.md` komt terug; niets verhuisde wat niet in de tabel staat. De drie lege `r*.json` zijn weg (1950481e). | feit (GEZIEN) | hoog | `git show -M --name-status --format= 69ea1bd1 25929e93` |
| A2 | **Op elke oude plek staat een doorverwijzing.** `VERHUISD.md` in alle 10 oude mappen onder `platformen/`, in `rapporten/` en `strategie/`; losse bestanden in `organisatie/VERHUISD.md`, `organisatie/rollen/VERHUISD.md`, `commercie/VERHUISD.md` (die noemt ook `.github/workflows-uit/`). `ARCHIEF-RELEASE.md` op alle 8 plekken waar beelden of data uit main gingen. | feit | hoog | `git ls-tree HEAD <map>/` per oude map |
| A3 | **Hats niet aangeraakt.** Geen enkel bestand onder `platformen/steam/`, `producten/steam-hol/` of `ontwerp/steam/` staat in een van de zeven commits (grep op de naamlijsten). | feit | hoog | zelfde lijsten |
| A4 | **Wel een bijwerking op Hats:** `platformen/steam/marketing/data/demo-spelers.py` r5 leest `platformen/verkenner/data/steam-desktop-kaart-2026-11-16.csv` (722 kB). Dat bestand ging in c8c429ad naar `onderzoek-data.zip`. Het script draait in geen workflow (grep `.github`), maar Sem (marketeer, terug ±1 dec) wil het volgens `berichten/olaf.md` r309 op de demo zetten. Het verslag zegt "geen workflow leest ze": klopt, maar dit script wel. Een ander script dat een verdwenen bestand leest, vond ik niet. | feit | hoog | `git grep -n "platformen/verkenner/data" -- '*.py'` |
| A5 | **Release klopt.** `archief-beelden-2026-11-22` heeft 4 zips en 4 lijsten (samen 296 MB, API). De 4 lijsten in de release zijn regel voor regel gelijk aan `organisatie/opruimen/archief-beelden/*.txt` (diff 0), en die 2.766 regels zijn precies de 2.766 bestanden die c8c429ad uit main haalde (`comm`, geen verschil). `abel-beelden.zip` en `onderzoek-data.zip` zelf gedownload met curl: HTTP 200, `unzip -t` zonder fouten, 50 en 824 bestanden; drie bestanden uit de abel-zip hebben dezelfde sha1 als in git (`c8c429ad^`). | feit | hoog | curl en unzip, zie hierboven |
| A6 | **Geen link naar buiten kapot.** Alle 71 raw-links naar dortus-hq in de repo wijzen naar bestanden die er nog zijn (o.a. `demo-v3.mp4`, `v4/demo-v4-b.mp4`, `wereld/polar`, `richtingen`, winkelbeelden; curl 200). De README's van rollwright, click-joints en bison-flex gebruiken hun eigen beelden; dortus.com gebruikt zijn eigen `/assets/` en linkt niet naar dortus-hq (curl). Er is geen `docs/` in dortus-hq. | feit | hoog | grep op `raw.githubusercontent.com`, curl van de drie README's en dortus.com |
| A7 | **Wel dode github.com/blob-links** in de notities naast de gearchiveerde beelden: `ontwerp/rollwright/v3/voor-projectchat.md` r6 tot r13, `v4/voor-projectchat.md` r16 tot r27, `v4/extra-run/voor-projectchat.md` r14 en r15 (12 links, bv. `v4/demo-v4-b.gif` geeft nu 404). Oude werknotities van 8 en 9 nov; de post op r/ObsidianMD gebruikte de mp4 die bleef staan (`commercie/rollwright/lancering.md` r517). | feit | hoog | curl -I op een van de links |
| A8 | **ai-handel:** paden mee in `scanner.yml`, `radar.yml`, `driehoek.yml`, `schaduwbot.yml` (ook de `--paden` van de klok en de sparse-checkout) en `projecten.json` (alleen paden veranderd, `dashboard/controle.py` OK). Geen oud pad meer in de scripts onder `onderzoek/ai-handel/`. Past bij Thijs vraag 3 (eigen map onder onderzoek, blijft openbaar). | feit | hoog | `git show 25929e93 -- .github` |
| A9 | **start.sh in een lege map werkt.** Kopie van het script buiten een kloon, in een lege map: 3 s, 56 MB, 6.894 commits, hook aan (`core.hooksPath=.githooks`), `python3 organisatie/controle/check.py` geeft "OK". Ook rechtstreeks `curl ... start.sh | bash` in een lege map: kloon goed. In een bestaande kloon doet het hetzelfde als eerst (getest op mijn eigen kloon). | feit | hoog | zelf gedraaid |
| A10 | Afwijkingen van het voorstel staan eerlijk in het verslag met reden: één archief in `organisatie/archief/` in plaats van `archief/` in de hoofdmap; `platformen/ideeen`, `succes`, `blender-2`, `tiktok-shop`, `commercie/xeneon-widgets` bleven staan; takken weghalen, `check.py` met 5 MB-grens, samenvoegen en berichten nog niet gedaan. Takken weghalen had Thijs al goedgekeurd (vraag 2) en blijft dus open. | feit | hoog | verslag "Wat bleef staan" en "Bijwerkingen" |
| A11 | Cijfers in het verslag kloppen: 536 hernoemd, 2.766 weg, ±453 MiB weg (verslag ±451 MB), 4 zips 296 MB. Werkmap na fase 2 tel ik 4.804 bestanden en 568 MiB (±596 MB) met `git ls-tree -l` op ca48a202; het verslag zegt 4.803 en 581 MB. Klein verschil, andere manier van meten. | feit | midden | `git ls-tree -r -l ca48a202` |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| B1 | **`onderzoek-data.zip` in de openbare release bevat ruwe winkeldumps met mailadressen van anderen:** 1.115 verschillende adressen in 45 bestanden, waarvan 200 op gmail, hotmail, outlook en dergelijke (dus vaak privé). Grootste: `platformen/verkenner/data/clover-apps-2026-11-09.jsonl` (296), `pionier/data/attio-apps-2026-11-09.json` (245), `verkenner/data/trmnl-recipes-2026-11-09.json` (234); ook `pionier/data/xeneon-widgets-2026-11-08.json` (43), hetzelfde soort dump dat de hoofdchat vandaag om die reden uit main haalde (a097e163). Gezien in de zip zelf (clover: 296 adressen). Ze stonden al in main en blijven in de geschiedenis, maar de release zet ze opnieuw en makkelijker te downloaden online. Het verslag noemt dit risico bij xeneon wel, bij de release niet. Adressen hier niet overgenomen. | feit | hoog | `regels/opslaan.md` r19 ("geen ruwe dumps van winkel-API's met andermans mailadressen in de repo") |
| B2 | Geen persoonsgegevens van Thijs in de nieuwe bestanden; `check.py` OK op main a097e163, workflow "Controle openbare repo" groen op alle commits. | feit | hoog | harde regel 2 |
| B3 | Geen geschiedenis herschreven: `4aa4f078` (meetpunt voorstel) en alle vorige commits zijn voorouders van main; verwijderde bestanden staan nog in `c8c429ad^`. Bestanden pas uit main na de groene run 45009000040. Niets geforceerd. | feit | hoog | harde regel 6 |
| B4 | Niets weggehaald wat niet van ons is: alles wat verdween is eigen werk (beelden, eigen meetdata, drie lege json). | feit | hoog | harde regel 6 |
| B5 | **Workflows na de verhuizing allemaal groen.** Sinds 09:42 UTC: dashboard, wegwijzer, scorebord, ideeen-radar, keurder-hats, loket-meldingen, week-test, steam-fest-meting, controle-openbaar, schaduwbot, scanner, radar en driehoek: alleen `success` of nog bezig, geen enkele rode run (API, 3 pagina's). `keurder.yml` en `opdracht.yml` draaiden niet; hun paden bestaan nog. Scanner (45009436930), radar en driehoek meten weer vanaf `onderzoek/ai-handel/` (stap Meten bezig). `wegwijzer.py` lokaal: "alle verwijzingen kloppen". | feit | hoog | skill `actions` |
| B6 | Bijwerking: de oude scanner-run 44997001734 werd afgebroken terwijl hij aan zijn eindopslag bezig was; op `ai-handel-data` staat van de scanner niets na 09:32 UTC (radar en driehoek wel om 09:50). Dus ±17 minuten scannerdata kwijt. Het verslag zegt "tussentijds opgeslagen data blijft": klopt, maar het laatste stuk van de scanner niet. | feit | midden | eerlijk (regel 5) |
| B7 | Oude paden in geldende bestanden: grep in `.github/workflows`, `.claude`, `organisatie/rollen`, `start.sh`, `organisatie/controle`, `START.md`, `CLAUDE.md`, `README.md`, `bord.md`, `projecten.json`, `hoofdchat-ronde.md`, sjablonen, regels, `dashboard` en alle `*.py`, `*.sh`, `*.yml`, `*.json`: geen verwijzing naar een pad dat niet bestaat en geen `VERHUISD.md` heeft. Wat overblijft is commentaar (`ontwerp/merk/bron/maak_upload.sh` r3 "draai vanuit platformen/abel/", `blender-2/data/nieuwkomers-ronde2-script.py` r3, `xeneon-widgets/data/ondergrens-downloads.py` r4, `ontwerp/garmin/bron/ebb_*_v8.py` r1 of r2, `platformen/ideeen/repo-radar/opslaan.sh` r7) en het script uit A4. `wegwijzer.py` r17 noemt nog `strategie/` en `rapporten/`: onschuldig, die mappen bestaan nog. | feit | hoog | opdracht keuring punt B |
| B8 | Nieuwe workflow `archief-beelden.yml` schrijft in een release bij elke push naar main die de map `organisatie/opruimen/archief-beelden/` raakt. Veilig gebouwd (tag moet met `archief-beelden-` beginnen, bestaande zips worden overgeslagen, stopt als een bestand ontbreekt), maar het is een tweede route om in een release te schrijven naast de tag-route. | feit | hoog | skill `actions` ("alles wat in een release schrijft via de tag-route") |
| B9 | Gedachtestreepjes: geen in de nieuwe tekst (`check.py` OK). Cijfers in het verslag hebben GEZIEN. | feit | hoog | regel 5 en 8 |

## Deel C: zou een gebruiker het leuk en fijn vinden?
(De gebruikers hier zijn de agents en Thijs.)
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| C1 | De snelle kloon is echt fijn: 3 s in plaats van ±45 s, en `check.py` werkt meteen. Maar in die sparse kloon geeft `wegwijzer.py` valse meldingen (bv. `ontwerp/` en `platformen/steam/logboek.md` "bestaan niet"), want die mappen zijn niet uitgepakt. Een agent die dat niet weet, gaat "repareren". | Eén regel in `start.sh` (na "Uitgepakt") of bovenaan `wegwijzer.py`: in een sparse kloon klopt de wegwijzer niet, draai hem in Actions of na `git sparse-checkout disable`. | klein |
| C2 | De melding "Uitgepakt: de hoofdmap plus ... .github ." eindigt met een losse punt als er geen extra mappen zijn. | cosmetisch | klein |
| C3 | `START.md` wijst nu naar `onderzoek/`, het archief, `verhuizingen.md` en de release: wie iets zoekt, vindt het in twee stappen. Goed. | geen | |
| C4 | Wie de oude beelden van Garmin of Rollwright wil zien, moet een zip van 83 tot 145 MB halen. De lijsten in `organisatie/opruimen/archief-beelden/` maken duidelijk wat erin zit. Prima voor oud werk. | geen | |

## Moet (blokkeert akkoord)
1. **`onderzoek-data.zip` zonder andermans mailadressen** (B1). Release `archief-beelden-2026-11-22`, lijst `organisatie/opruimen/archief-beelden/onderzoek-data.txt`. Maak de zip opnieuw zonder de 45 bestanden met mailadressen (of met de mailvelden eruit) en vervang het bestand in de release, zoals de hoofdchat dat met de xeneon-dump deed. Alleen de cijfers die nog nodig zijn bewaren (`regels/opslaan.md` r19). Agents hebben geen GitHub-sleutel, dus dit moet via een workflow; de huidige `archief-beelden.yml` slaat een bestaande zip over en kan dit nog niet. Wat al in de git-geschiedenis staat, valt buiten deze klus (dat vraagt herschrijven, en dat doen we niet).

## Kan (mag later)
1. **`platformen/steam/marketing/data/demo-spelers.py` r5** (A4): het invoerbestand staat nu alleen in de release. Vóór Sem terug is (±1 dec): de csv (722 kB, zonder mailadressen) terugzetten in `onderzoek/verkenner/data/` en het pad in het script laten aanpassen door de eigenaar van `platformen/steam/` (Hats-afspraak), of Sem een bericht sturen.
2. Dode blob-links in de drie `voor-projectchat.md` onder `ontwerp/rollwright/` (A7): één regel bovenaan elk bestand dat de beelden in `ontwerp-rollwright.zip` zitten.
3. Valse meldingen van `wegwijzer.py` in een sparse kloon uitleggen (C1).
4. `ontwerp/merk/bron/maak_upload.sh` r3: commentaar zegt nog "draai vanuit platformen/abel/"; het script maakt `upload/` naast `merk/`, dus nu in `ontwerp/`.
5. In het verslag het stukje scannerdata noemen dat bij het afbreken verloren ging (B6), en bij een volgende verhuizing van ai-handel eerst wachten tot de scanner net heeft opgeslagen.
6. Takken weghalen (Thijs zei ja op vraag 2) staat nog open; zet het op het bord met een eigenaar.
7. De beschrijving van het claude.ai-project noemt nog `organisatie/overstap-account.md` (nu in het archief; `organisatie/VERHUISD.md` vangt het op). Alleen Thijs kan die tekst aanpassen; past op de lijst als er plek is.

## Nakeuring, 22 nov 2026 ±11:20 NL, zelfde keurder
Wat ik keurde: commits cffd0060 en c2d5fe66, run 45010921615 (Archief beelden naar release, groen), release `archief-beelden-2026-11-22` zoals hij nu online staat.
Akkoord: nee (het moet-punt is bijna weg: nog 3 gmail-adressen in 2 gzip-bestanden in `onderzoek-data.zip`)

| # | Wat ik zag | Feit of vermoeden | Zekerheid |
|---|---|---|---|
| N1 | **Oude zip weg.** API van de release: `onderzoek-data.zip` is nu 32.602.691 bytes (nieuw asset-id, bijgewerkt 10:08 UTC), de lijst 43.640 bytes. De zip van 48.948.851 bytes staat er niet meer. De andere zes bestanden zijn ongewijzigd (09:45 UTC). | feit (GEZIEN) | hoog |
| N2 | **Nieuwe `onderzoek-data.zip`:** curl -L HTTP 200, `unzip -t` zonder fouten, 778 bestanden (824 min de 46 uit `onderzoek-data.weglaten`; `onderzoek-data.txt` heeft nu 778 regels). Uitgepakt en `grep -rEoa` met een regex op mailadressen over alles: 0 treffers. | feit | hoog |
| N3 | **Maar:** 13 bestanden in de zip zijn zelf gzip (`.json.gz`, `.jsonl.gz`). Die ziet grep niet, en de controle in `archief-beelden.yml` (stap "Zips schoonmaken") ook niet: die leest alleen tekstextensies en pakt `.gz` niet uit. Na `zcat`: `platformen/verkenner/data/davinci-gumroad-newest-2026-11-15.json.gz` heeft 2 gmail-adressen (veld `seller` van Gumroad-verkopers) en `platformen/verkenner/data/csa-alle-mei-aug-2026-11-08.jsonl.gz` 1 gmail-adres (veld `clip_user_handle`). Echte adressen, geen toeval in beelddata; hier niet overgenomen. De andere 11 gzip-bestanden: 0. Dezelfde blinde vlek zat in mijn eerste telling. | feit | hoog |
| N4 | **`ontwerp-garmin.zip` en `ontwerp-rollwright.zip`:** alle 1.827 en 65 bestanden zijn png, jpg, gif of mp4, geen enkel tekstbestand en geen gzip. De treffers (5 en 7) zitten in gecomprimeerde beelddata en zien eruit als `x@Y.WTW`, `s@8.XA`, `@-.gm`: toevallige tekens, geen adressen. `abel-beelden.zip`: 0, ook in de zip erin (`dortus-beelden.zip`, 21 beelden en een md). | feit | hoog |
| N5 | **Kan 1:** `onderzoek/verkenner/data/steam-desktop-kaart-2026-11-16.csv` staat terug, zelfde git-blob als het origineel in `c8c429ad^`, 0 mailadressen. Bericht aan Olaf onderaan `berichten/olaf.md` met het nieuwe pad; `demo-spelers.py` zelf niet aangepast (Hats). Goed. | feit | hoog |
| N6 | **Kan 3:** `organisatie/start.sh` r28 tot r30 waarschuwt voor valse meldingen van `wegwijzer.py` in de sparse kloon; in een lege map getest, de melding komt, en de losse punt na `.github` is weg. Goed. | feit | hoog |
| N7 | **Kan 4:** `ontwerp/merk/bron/maak_upload.sh` r3 zegt nu "draai vanuit ontwerp/". Goed. | feit | hoog |
| N8 | `check.py` OK op main c2d5fe66. Geen geschiedenis herschreven. | feit | hoog |

### Moet (blokkeert akkoord)
1. De twee gzip-bestanden uit N3 erbij zetten in `organisatie/opruimen/archief-beelden/onderzoek-data.weglaten`, en in `archief-beelden.yml` de controle `.gz` laten uitpakken voor de regex (anders slaagt de controle terwijl er nog adressen in zitten). Daarna opnieuw: 776 bestanden, 0 adressen, ook na `zcat`.

### Kan
1. In het verslag (`fase2-2026-11-22.md` r61) staat "GEZIEN met een regex over alle 824 bestanden": zonder gzip uitpakken was die telling niet volledig. Een regel erbij als het moet-punt klaar is.

## Nakeuring 2, 22 nov 2026 ±11:30 NL, zelfde keurder
Wat ik keurde: commit f356f0e0, run 45011361382 (Archief beelden naar release, groen, alle stappen OK), release `archief-beelden-2026-11-22` zoals hij nu online staat.
Akkoord: ja

| # | Wat ik zag | Feit of vermoeden | Zekerheid |
|---|---|---|---|
| M1 | **Eén `onderzoek-data.zip` in de release** (API): 31.972.503 bytes, asset-id 778644968, bijgewerkt 10:13 UTC; de lijst 778644970. De vorige asset-ids 778632073 en 778632079 geven 404 via de API. De oorspronkelijke zip van 48,9 MB stond er bij de vorige nakeuring al niet meer. De andere zes bestanden zijn ongewijzigd. | feit (GEZIEN) | hoog |
| M2 | **Nieuwe zip:** curl -L HTTP 200, `unzip -t` zonder fouten, **776 bestanden** (gelijk aan `onderzoek-data.txt`; de 2 gzip-dumps staan nu in `onderzoek-data.weglaten`, dat er 48 heeft). | feit | hoog |
| M3 | **0 mailadressen.** Uitgepakt en `grep -rEoa` met de regex over alles: 0. Daarna elk ingepakt bestand uitgepakt met een eigen script (gz, bz2, xz, zip, tar, tgz): 11 `.gz`-bestanden, geen bz2, xz, zip of tar; ook daarin 0 adressen. | feit | hoog |
| M4 | **De controle in `archief-beelden.yml` pakt echt uit.** Ik haalde het Python-stuk uit de workflow en draaide het zelf: op een proefzip met een `.json.gz` en een `.txt.xz` die elk een nep-adres bevatten meldt hij beide en stopt met code 1; op de echte zip meldt hij "776 bestanden, met mailadres (ook na uitpakken): 0" en code 0. Hij kijkt nu ook naar alle bestanden behalve beeld en film, niet alleen naar een lijst tekstextensies. Dat is strenger dan eerst. | feit | hoog |
| M5 | `check.py` OK op main f356f0e0; geen geschiedenis herschreven. | feit | hoog |

### Moet
Geen. Het moet-punt van de eerste keuring is opgelost.

### Kan
1. De controle pakt `.tgz` niet uit (wel `.tar.gz`, `.gz`, `.bz2`, `.xz`, `.zip`). Nu zit er geen `.tgz` in een zip; noem het als er ooit een bij komt.
2. Wat in de git-geschiedenis staat (de dumps stonden tot 22 nov op main) blijft openbaar; daar is herschrijven voor nodig en dat doen we niet. Dit is geen opdracht, alleen ter info.
3. De kan-punten uit de eerste keuring die nog openstaan: dode blob-links in de drie `voor-projectchat.md` onder `ontwerp/rollwright/`, de korte uitval van scannerdata in het verslag noemen, takken weghalen met een eigenaar op het bord, en de beschrijving van het claude.ai-project (alleen Thijs).
