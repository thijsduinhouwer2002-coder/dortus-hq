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
1. **Bewijs:** elk cijfer krijgt een label. GEZIEN (zelf gemeten), DERDEN (bron met link) of GOK.
2. **Nakijken voor het telt:** werk is pas klaar als een controleur het heeft nagekeken. Code is pas klaar als de tests groen zijn.
3. **Eén taak tegelijk** per manager. Liever één ding af dan drie half.
4. **Stopregel:** op dag 30 na lancering onder de 30 gebruikers: stoppen of veranderen, met onderbouwing.
5. **Geen herhaling zonder resultaat:** lukt een taak twee runs op rij niet, zet hem op de lijst voor Thijs en pak iets anders.

## Opslaan
- Begin met `git pull --rebase`.
- Je mag alleen schrijven in je eigen map in `platformen/` (de strateeg in `strategie/`), de code van je eigen product in `producten/`, en een regel toevoegen aan `organisatie/lijst-thijs.md`. Alleen de hoofdmanager schrijft in `organisatie/bord.md` en `rapporten/`.
- Code: werk op een tak `claude/<platform>-<datum>`. Voeg samen met `main` als de controleur akkoord is en de tests groen zijn.
- Notities in je eigen map mag je direct op `main` zetten.
- Mislukt het opslaan omdat iemand anders net iets opsloeg: `git pull --rebase` en opnieuw. Nooit geforceerd overschrijven.

## Webpagina's lezen
- Het netwerk van de cloudomgeving staat open (Full). Lees webpagina's daarom met `curl` in Bash (bijvoorbeeld `curl -sL <url>`), of met een klein script. Dat vraagt geen toestemming.
- De leestool WebFetch kan per website om toestemming vragen. In een run zit niemand om te antwoorden, dus dan sta je stil. Gebruik WebFetch alleen als `curl` niet werkt (bijvoorbeeld een pagina die alleen in een browser laadt), en stop als er een toestemmingsvraag komt: noteer de site en ga door met ander werk.
- WebSearch (zoeken) mag gewoon.

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
