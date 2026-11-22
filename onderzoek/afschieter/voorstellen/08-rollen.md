Wat verandert: de leesstap en de agentstap in de rollen van de actieve Claudes, zodat ze gelijk lopen met voorstel 01, 03 en 07. Voer dit **in dezelfde commit** door als 01, 03 en 07, anders zeggen CLAUDE.md en de rollen weer iets anders (dat vond de controleur van mijn voorstellen terecht).
Waarom: elke rol heeft nu een eigen leeslijst ("Elke run", stap 1) die afwijkt van CLAUDE.md en van de opdracht. `hoofdmanager.md` is in lagen gerepareerd en gaat nog uit van zoekers als hoofdzaak.

---

## A. Overal dezelfde stap 1 (vervangt stap 1 van "Elke run" in elke rol)

> 1. Begin zoals CLAUDE.md zegt (berichten zonder "verwerkt", je rol, het bord, je `status.md`). Lees daarnaast alleen wat deze taak nodig heeft.

Betreft: `platformmanager.md` regel 6, `ontwerper.md` regel 47, `game-ontwerper.md` regel 19, `ontwerper-wow.md` regel 19, `hoofdmanager.md` regel 15 (die van Hans mag daarna nog `rapporten/` van gisteren en `lijst-thijs.md` lezen).

## B. `platformmanager.md`, nieuwe stappen 2 tot 5 van "Elke run"

> 2. Pak de bovenste taak ("Volgende taak") uit `status.md`. Klopt de volgorde niet meer, pas hem aan en schrijf in één zin waarom.
> 3. Doe kleine taken zelf. Zet een agent in als het werk echt parallel kan of veel leeswerk vraagt: geef een doel, een vorm voor het antwoord en een grens. Een controleur-agent (die het werk niet maakte) alleen bij een ontwerp, iets wat naar buiten gaat (release, winkeltekst, bericht voor Thijs) of een getal waar een besluit op rust; zeg hem stijlpunten over te slaan. Voor code zijn groene tests de controle. Zet in elke agentopdracht letterlijk: "Lees webpagina's met curl in Bash, nooit met WebFetch. WebFetch vraagt om toestemming en dan staat alles stil."
> 4. Afgekeurd: één keer verbeteren. Lukt het dan nog niet, schrijf in `status.md` wat er misging.
> 5. Werk bij: `status.md` volgens het sjabloon (`organisatie/sjablonen/status.md`, hooguit 25 regels); `taken.md` als de lange lijst verandert; `logboek.md` één blok met wat er is opgeleverd of besloten en waarom (niet wat je las).

## C. `hoofdmanager.md`, wat eruit en wat erin
- **Eruit:** regel 3 "Je draait elke dag om 20:44" (botst met de alinea erna). Het hele deel over voorstellen van de verkenner en de pionier beoordelen (regels 20 tot 28 van "Elke run"): zoeken staat stil; zet het in `organisatie/rollen/uit/hoofdmanager-zoekers.md` voor als Thijs het weer aanzet. "afsluitregel uit regels.md" wordt "afsluitregel uit CLAUDE.md". "Jij bent de enige die managers stuurt" past niet meer als Thijs voorstel 05 kiest.
- **Erin (als Thijs voorstel 05 kiest):** "Je bent de controleur van het bedrijf. Eén run per dag om 08:44. Je schrijft een dagkaart van hooguit 10 regels in `rapporten/<datum>.md`: (1) op koers tegen het tussendoel, (2) wat er gisteren af, ingediend of live kwam, (3) wie draaide maar leverde niets op (runs zonder commit buiten logboek en status), (4) welke opdracht, rol of status.md niet meer klopt met het bord, (5) wat al twee dagen hangt. Bij (3) tot (5) zet je één regel in het berichtenbestand van wie het aangaat. Productkeuzes van managers (`volgend-product.md`) keur je goed of af. Koers, ploeg en geld beslist de hoofdchat met Thijs."
- Kiest Thijs voorstel 05 niet: alleen de drie "Eruit"-punten doorvoeren.

## D. Verwijzingen die meeverhuizen
- Gaan de uitgezette rollen naar `organisatie/rollen/uit/`: pas `hoofdmanager.md` (regel 30) en `zijpadzoeker.md` (regel 13) aan, die naar `pionier.md` en `herweger.md` verwijzen.
- `hoofdmanager.md` regel 21 noemt het "sjabloon Chris" in `geplande-taken.md`. Met voorstel 03 is er één sjabloon voor iedereen; pas de verwijzing aan.
