Wat verandert: `organisatie/regels.md` van 13,2 KB naar ±6 KB. Weg wat nu in CLAUDE.md staat (opslaan, afsluiten, webpagina's, koppelingen, wat nooit mag), weg wat verouderd is (blok "Gedeeld account (tijdelijk)": de overstap naar het eigen account was 7 nov; "Dortus-taken heten Stijn, Hans, Vera, Olaf, Jet" klopt niet meer), en nieuw: wanneer een agent of controleur, hoe je een geplande taak wijzigt, en eerst de regels van een plek lezen voor je er iets plaatst.
Waarom: dubbele regels lopen uit elkaar (bron 7) en een regel die elke run gelezen wordt maar niet nodig is, kost context en naleving (bron 1, 5). Regels.md wordt zo een naslag: je leest het als je taak erom vraagt (bouwen, uitbrengen, website), niet elke run. De Chrome-regel (alleen de browser van Thijs' HP, deviceId 869e8714-...) hoort alleen bij de hoofdchat en gaat naar `organisatie/middelen.md`; geplande runs in de cloud hebben geen Chrome.

---

# Regels (naslag)

De harde regels die altijd gelden staan in `CLAUDE.md`. Hier staat hoe we werken. Lees het deel dat bij je taak hoort.

## Houding
- Dortus is een ondernemersbedrijf: geef niet op bij de eerste tegenslag, en vind een plan niet slecht omdat het veel werk is. Wel: liever een eerlijke gok met kans op geld dan nog een week zekerheid zoeken (Thijs 9 nov 22:56).
- Beslis zelf en schrijf in één of twee zinnen waarom. Bouw wat op een platform ontbreekt, niet wat we toevallig al hebben.
- Geen werk verzinnen. Niets zinvols te doen: twee regels in je `status.md` en stoppen.

## Wanneer Thijs vragen
Alleen bij: geld uitgeven; iets wat niet terug kan (definitief verwijderen, een live product uit een winkel halen); risico voor zijn accounts of juridisch; een taak die twee runs op rij niet lukt; een stap die alleen hij kan (inloggen, account, betalen, voorwaarden, een sleutel, een bericht onder zijn naam). Zet het in `organisatie/lijst-thijs.md` in de vorm die daar bovenaan staat, zet alles klaar wat kan, en ga door met ander werk.

## Besluiten
- Een groot besluit (platform, product, stoppen, koers) komt als één regel bovenaan `organisatie/besluiten.md`: `datum | wie | besluit | waarom | wat zou het veranderen`. De hoofdchat of Hans neemt het over in `organisatie/bord.md` als het geldt.
- Kom niet zonder nieuw feit terug op een besluit. Logboeken en besluiten alleen aanvullen, nooit iets weghalen; ouder dan 7 dagen mag de hoofdchat naar `organisatie/archief/` verplaatsen (verplaatsen is geen weghalen).

## Een taak goed doen
1. **Eén taak per run** (de bovenste uit je `status.md`). Liever één ding af dan drie half.
2. **Bewijs:** elk cijfer krijgt GEZIEN, DERDEN (met link) of GOK.
3. **Agents:** kleine taken doe je zelf. Een agent zet je in als het werk echt parallel kan of veel leeswerk vraagt; geef dan een doel, een vorm voor het antwoord en een grens ("hooguit 10 zoekopdrachten").
4. **Controle:** voor code zijn groene tests de controle. Een controleur-agent (die het werk niet maakte) alleen bij: een ontwerp, iets wat naar buiten gaat (release, winkeltekst, bericht voor Thijs), of een getal waar een besluit op rust. Zeg hem stijlpunten over te slaan.
5. **Twee keer mislukt:** zet het op de lijst van Thijs of in `berichten/hans.md` en pak iets anders.
6. **Stopregels:** dag 30 na lancering onder de 30 gebruikers: stoppen of veranderen, met onderbouwing. Jong platform via de pionier: groeit het platform 2 maanden niet meer, of verdwijnt het betaalplan: stoppen of veranderen.

## Elk product: perfect, onderscheidend, duidelijke belofte (Thijs 8 nov)
- Bovenaan `producten/<product>/ontwerp.md` de ene zin: waarom iemand ons kiest boven de beste concurrent. Kun je die niet schrijven, dan is het product niet klaar.
- Op elke winkelpagina, poster en README in een paar seconden: wat het doet, voor wie, waarom beter, wat gratis en wat betaald. Overal hetzelfde.
- Mooi en opvallend is de helft van het product ("geen brave zooi", Thijs 7 nov). Denk vanaf het begin met de ontwerper mee over uiterlijk en gevoel. Wel eerlijk: wat je laat zien, zit in het product.
- Betaald deel vanaf de eerste versie. Durf hoger te prijzen.

## Bouwen
- **Eerst ontwerp:** 2 tot 3 alinea's in `producten/<naam>/ontwerp.md` (wat het doet, wat bewust niet, hoe het aansluit, toetsbare eisen). Controleur keurt het ontwerp; daarna bouwen.
- **Eerst kijken wat er is:** lees de code en `architectuur.md`. Bouw voort, maak niets dubbel. Bestanden onder ±400 regels; groter: splitsen en `architectuur.md` bijwerken.
- **Tests niet aanpassen** om ze te laten slagen. Een test wijzigen of weghalen alleen met reden in de commit; de controleur keurt dat apart.
- **Elke fout is jouw fout:** faalt er iets na jouw wijziging, zoek de oorzaak.
- **Opruimen:** elke week één opruimtaak bovenaan (dubbele code, grote bestanden, architectuur.md).
- Code op een tak `claude/<platform>-<datum>`; samenvoegen als controleur akkoord en tests groen.

## Testen in de echte app (GitHub Actions)
- Elk product wordt getest in de echte app van het platform, op GitHub Actions (in de Claude-omgeving mogen gedownloade programma's niet starten; die beveiliging omzeil je nooit). Workflow `.github/workflows/<product>-e2e.yml`, tests in `producten/<product>/e2e/`. Voorbeeld: `rollwright-e2e.yml`.
- Laat de test opschrijven wat hij ziet (`console.log`) en zijn schermafbeeldingen op de tak `schermen` zetten (map `<product>/<taknaam>/`, stap kopiëren uit `rollwright-e2e.yml`).
- Uitslag lezen (repo is openbaar): `curl -s "https://api.github.com/repos/thijsduinhouwer2002-coder/dortus-hq/actions/runs?per_page=5"` en `curl -sL https://api.github.com/repos/thijsduinhouwer2002-coder/dortus-hq/actions/jobs/<job-id>/logs`.

## Uitbrengen
- Pas als de test in de echte app groen is en de ontwerper `Akkoord: ja` zette bovenaan `producten/<product>/ontwerp.md` (ook voor de README, dat is de winkelpagina).
- Eerste lancering van elk product: Thijs ziet plaatjes en README eerst en zegt ja of nee. Een live product krijgt hooguit één versie per week via Thijs, behalve bij een echte fout.
- Elk live product heeft een eigen openbare repo onder thijsduinhouwer2002-coder met alleen code, tests, README, LICENSE, CHANGELOG. Thijs maakt die repo aan; `producten/<product>/publiceer.sh` zet de bestanden erin, met `release` maakt de workflow een release (sjabloon `organisatie/sjablonen/obsidian-release.yml`).
- De eerste aanmelding bij een platform doet Thijs met zijn login; zet die klaar op zijn lijst.

## Gevonden worden
- Elk product heeft vóór de lancering een verspreidingsplan: 5 tot 10 plekken waar de gebruikers al zijn, met per plek de regels.
- **Lees eerst de regels van een plek, dan pas schrijven.** Veel plekken verbieden reclame van een eerste post of door AI gemaakte inhoud (r/ObsidianMD regel 4 "No slop", ontdekt door Thijs op 9 nov 11:45, nadat de tekst al dagen klaar stond). Past de plek niet, dan valt hij af voordat er werk in gaat.
- Wat zonder Thijs kan (zoekwoorden, plaatjes, pagina op dortus.com, pull request naar een lijst) doet de ploeg zelf.

## De website dortus.com
- Repo `thijsduinhouwer2002-coder/dortus`. Alleen in een eigen map per product (`<productnaam>/`): index, privacy, support.
- Verander of verwijder niets wat er al staat (bestaande pagina's, `assets/`, `styles.css`, `index.html`, `sitemap.xml`). Linken mag; aanpassen alleen in een kopie in je eigen map.
- Support op elke pagina: thijs@dortus.com.

## Geplande taken
- Wie een geplande taak aanmaakt, wijzigt of uitzet, werkt in dezelfde run `organisatie/geplande-taken.md` en `dashboard/ploeg.json` bij.
- De opdracht is voor iedereen dezelfde korte tekst (staat in `geplande-taken.md`). Wat verandert, staat in de rol of in het bord, nooit in de opdracht.
- Een herinnering noemt nooit wie er draait, maar zegt: "lees organisatie/bord.md en beslis dan".

## Middelen
Alle sites en programma's staan in `organisatie/middelen.md`, met wie er mag inloggen. Begin je iets nieuws te gebruiken, zet het er meteen bij.
