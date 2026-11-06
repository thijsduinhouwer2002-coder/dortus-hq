# Regels voor iedereen

## Houding
- **Dortus is een ondernemersbedrijf.** Thijs durft ergens voor te gaan en weet dat het moeite en tijd kost. Dat geldt voor de hele ploeg: geef niet op bij de eerste tegenslag, en vind een plan niet slecht omdat het veel werk is.
- Werk hard, met enthousiasme, en maak onderbouwde keuzes.
- Beslis zelf. Schrijf bij elke beslissing in één of twee zinnen waarom, in je logboek.
- Vraag Thijs alleen in nood (zie onder).
- Open blik: bouw wat op een platform ontbreekt, niet wat we toevallig al hebben.

## Wanneer Thijs vragen
- Er moet geld uitgegeven worden.
- Iets is niet terug te draaien: definitief verwijderen, een live product uit een winkel halen.
- Risico voor zijn accounts of juridisch.
- Een taak lukt twee runs op rij niet.
- Een stap die alleen Thijs kan doen: inloggen, een account aanmaken, betalen, voorwaarden accepteren, een sleutel (token) aanmaken. Ook berichten onder zijn naam (forum, Reddit, Discord, reviews): schrijf ze uit en zet ze klaar.

Zet zo'n vraag of stap in `organisatie/lijst-thijs.md`: wat, waarom, een link, en precies wat hij moet doen. Zet alles klaar wat klaargezet kan worden. Ga daarna door met ander werk.

## Werkwijze
0. **Eerst ontwerp, dan bouwen.** Voor elk nieuw product of grote functie schrijft de bouwer eerst een kort ontwerp (2 tot 3 alinea's in `producten/<naam>/ontwerp.md`): wat het doet, wat het bewust niet doet, hoe het aansluit, en wanneer het af is (toetsbare eisen). De controleur keurt het ontwerp goed. Pas daarna wordt er gebouwd, en de controleur toetst de code tegen het ontwerp.
0b. **Besluiten vastleggen.** Elk groot besluit (platform kiezen, product kiezen, stoppen, koers veranderen) komt in `organisatie/besluiten.md`, met reden en wat het zou veranderen. Lees dat bestand voordat je iets besluit. Kom niet zonder nieuw feit terug op een besluit.
0c. **Geen werk verzinnen.** Zit je vast, of is er niets zinvols te doen, schrijf dan in twee regels in je logboek waarom en stop. Liever een korte run dan drukte zonder resultaat.
0d. **Logboeken alleen aanvullen.** Haal nooit iets weg uit een logboek of besluitenlijst, zodat Thijs alles kan terugzien.
1. **Bewijs:** elk cijfer krijgt een label. GEZIEN (zelf gemeten), DERDEN (bron met link) of GOK.
2. **Nakijken voor het telt:** werk is pas klaar als een controleur het heeft nagekeken. Code is pas klaar als de tests groen zijn.
3. **Eén taak tegelijk** per manager. Liever één ding af dan drie half.
4. **Stopregel:** op dag 30 na lancering onder de 30 gebruikers: stoppen of veranderen, met onderbouwing.
5. **Geen herhaling zonder resultaat:** lukt een taak twee runs op rij niet, zet hem op de lijst voor Thijs en pak iets anders.

## Codekwaliteit (zodat een product heel blijft als het groeit)
1. **Tests niet aanpassen om ze te laten slagen.** Faalt een test, dan repareer je de code, niet de test. Een bestaande test wijzigen of weghalen mag alleen met een reden in de commit, en de controleur keurt dat apart goed. De controleur bekijkt bij elke beurt welke tests er veranderd zijn.
2. **Eerst kijken wat er al is.** Lees voor je iets toevoegt de bestaande code en `producten/<naam>/architectuur.md`. Bouw voort op wat er is, maak niets dubbel.
3. **Elke fout is jouw fout.** Faalt er iets na jouw wijziging, ook als het er "niets mee te maken lijkt te hebben", zoek de oorzaak. Zeg nooit "dat komt niet door mij" zonder bewijs.
4. **Klein en overzichtelijk.** Een bestand blijft onder de ±400 regels. Wordt het groter, splits het op. Elk product heeft een `architectuur.md` met de onderdelen en hoe ze samenhangen, en de bouwer werkt dat bij als er iets verandert.
5. **Opruimen hoort erbij.** Elke week (na het weekbesluit van zondag) zet de manager één opruimtaak bovenaan: dubbele code weg, grote bestanden splitsen, `architectuur.md` bijwerken. Pas daarna weer nieuwe functies.

## Opslaan
- Begin met `git pull --rebase`.
- Je mag alleen schrijven in je eigen map in `platformen/` (de strateeg in `strategie/`), in je eigen bestand in `berichten/` (alleen "verwerkt" erachter zetten), een regel bovenaan in `organisatie/besluiten.md`, de code van je eigen product in `producten/`, en een regel toevoegen aan `organisatie/lijst-thijs.md`. Alleen de hoofdmanager schrijft in `organisatie/bord.md` en `rapporten/`.
- Code: werk op een tak `claude/<platform>-<datum>`. Voeg samen met `main` als de controleur akkoord is en de tests groen zijn.
- Notities in je eigen map mag je direct op `main` zetten.
- Mislukt het opslaan omdat iemand anders net iets opsloeg: `git pull --rebase` en opnieuw. Nooit geforceerd overschrijven.

## Gedeeld account (tijdelijk)
Het Claude-account wordt gedeeld met de vader van Thijs, die er zijn eigen werk mee doet. Tot Dortus een eigen account heeft:
- **Gebruik nooit de koppelingen Gmail, Shopify, Trello, Kondo of Claude Docs**, ook niet als ze in je run beschikbaar zijn. Dat kunnen de accounts van iemand anders zijn.
- **Chrome:** gebruik alleen de browser van Thijs' HP (deviceId 869e8714-0c9c-4923-be63-c9ffa1fecfc0). Kies nooit een andere browser.
- Open of wijzig nooit chats, projecten of geplande taken die niet bij Dortus horen. Dortus-taken heten Stijn, Hans, Vera, Olaf, Jet (of beginnen met "Dortus").

## Webpagina's lezen
- Het netwerk van de cloudomgeving staat open (Full). Lees webpagina's daarom met `curl` in Bash (bijvoorbeeld `curl -sL <url>`), of met een klein script. Dat vraagt geen toestemming.
- De leestool WebFetch kan per website om toestemming vragen. In een run zit niemand om te antwoorden, dus dan sta je stil. Gebruik WebFetch alleen als `curl` niet werkt (bijvoorbeeld een pagina die alleen in een browser laadt), en stop als er een toestemmingsvraag komt: noteer de site en ga door met ander werk.
- WebSearch (zoeken) mag gewoon.
- Zet deze regel letterlijk in de opdracht van elke agent die je inzet: agents lezen `CLAUDE.md` niet vanzelf.

## Middelen
- Alle sites en programma's staan in `organisatie/middelen.md`. Begin je iets nieuws te gebruiken, zet het er meteen bij, met wie er mag inloggen.

## De website dortus.com
- De site staat in de repo `thijsduinhouwer2002-coder/dortus` (statische HTML, gepubliceerd op dortus.com). De ploeg mag hem gebruiken voor productpagina's, privacybeleid en support van onze producten.
- Werk alleen in een eigen map per product: `<productnaam>/` in de repo, dus dortus.com/<productnaam>/. Bijvoorbeeld `dice-roller/index.html`, `dice-roller/privacy.html`, `dice-roller/support.html`.
- Verander of verwijder niets wat er al staat. Dat geldt voor elke bestaande pagina, `assets/`, `styles.css`, `index.html`, `sitemap.xml` en alle andere bestaande bestanden en mappen.
- Bekijk de bestaande pagina's alleen om de stijl en de opbouw over te nemen. Linken naar bestaande bestanden (zoals `/styles.css` of `/assets/fonts/`) mag. Wil je iets aanpassen, kopieer het dan naar je eigen productmap.
- Support op winkelpagina's en productpagina's: **support@dortus.com**.
- Opslaan op de site gaat via dezelfde regels: `git pull --rebase`, nooit geforceerd, en afsluiten met `git ls-remote` voor die repo.

## Afsluiten
Sluit je run pas af nadat je met `git ls-remote origin main` (of `refs/heads/<tak>` bij een tak) hebt laten zien dat jouw laatste commit op GitHub staat. Zet de hash van je commit en de uitkomst van `git ls-remote` in je eindantwoord (niet in een bestand, want dat levert weer een nieuwe commit op). Heeft iemand daarna ook opgeslagen, dan mag de hash van jouw commit ook in `origin/main` zitten na `git fetch`.

Lukt opslaan niet: zet de volledige nieuwe inhoud van je bestanden in het eindantwoord en meld in je laatste zin dat het niet is opgeslagen. De status "geslaagd" van de taak zegt niets over opslaan.
