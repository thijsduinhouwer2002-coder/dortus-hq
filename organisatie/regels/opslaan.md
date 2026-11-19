# Opslaan, schrijven en de site

Lees dit als je twijfelt waar je mag schrijven, of iets op dortus.com zet.

## Opslaan
- Begin met `git pull --rebase`.
- Je mag alleen schrijven in je eigen map in `platformen/` (de strateeg in `strategie/`, Chris in `commercie/`), in je eigen bestand in `berichten/` (alleen "verwerkt" erachter zetten), een regel onderaan bij "Nieuwe besluiten" in `organisatie/besluiten.md`, de code van je eigen product in `producten/`, en een bericht onderaan in het berichtenbestand van een ander (met datum en van wie). Wat alleen Thijs kan meld je in `berichten/hoofdchat.md`; alleen de hoofdchat schrijft in `organisatie/lijst-thijs.md`. Alleen de hoofdchat schrijft in `organisatie/bord.md` en `rapporten/`.
- Code: werk op een tak `claude/<platform>-<datum>`. Voeg samen met `main` als de keurder akkoord is en de tests groen zijn.
- Notities in je eigen map mag je direct op `main` zetten.
- Mislukt het opslaan omdat iemand anders net iets opsloeg: `git pull --rebase` en opnieuw. Nooit geforceerd overschrijven.

## Afsluiten
Sluit je run pas af nadat je met `git ls-remote origin main` (of `refs/heads/<tak>` bij een tak) hebt laten zien dat jouw laatste commit op GitHub staat. Zet de hash van je commit en de uitkomst van `git ls-remote` in je eindantwoord (niet in een bestand, want dat levert weer een nieuwe commit op). Heeft iemand daarna ook opgeslagen, dan mag de hash van jouw commit ook in `origin/main` zitten na `git fetch`.

Lukt opslaan niet: zet de volledige nieuwe inhoud van je bestanden in het eindantwoord en meld in je laatste zin dat het niet is opgeslagen. De status "geslaagd" van de taak zegt niets over opslaan.


## Controle openbare repo (15 nov 2026)
De repo is openbaar. Draai vóór elke push `python3 organisatie/controle/check.py`: die kijkt naar wat jij toevoegt en stopt bij persoonsgegevens (IBAN, telefoonnummer, gmail-adres), sleutels en gedachtestreepjes in tekst. GitHub draait dezelfde controle na elke push (workflow "Controle openbare repo"); rood betekent: meteen weghalen en opnieuw pushen. Zet ook geen ruwe dumps van winkel-API's met andermans mailadressen in de repo; bewaar alleen de cijfers die je nodig hebt.

## Webpagina's lezen
- Lees webpagina's met `curl` in Bash (`curl -sL <url>`) of een klein script. WebSearch (zoeken) mag gewoon.
- **WebFetch nooit.** Het vraagt Thijs om toestemming en dan staat alles stil. Sinds 18 nov staat WebFetch op "deny" in `.claude/settings.json`; zet de zin "Webpagina's lees je met `curl` in Bash, nooit met WebFetch." toch letterlijk in de opdracht van elke agent die je inzet, want een subagent of een sessie zonder de repo-instellingen kent die blokkade niet.
- Een site die je weigert (403, Cloudflare): niet omzeilen. Noteer het en ga door.

## Middelen
- Alle sites en programma's staan in `organisatie/middelen.md`. Begin je iets nieuws te gebruiken, zet het er meteen bij, met wie er mag inloggen.

## De website dortus.com
- De site staat in de repo `thijsduinhouwer2002-coder/dortus` (statische HTML, gepubliceerd op dortus.com). De ploeg mag hem gebruiken voor productpagina's, privacybeleid en support van onze producten.
- Werk alleen in een eigen map per product: `<productnaam>/` in de repo, dus dortus.com/<productnaam>/. Bijvoorbeeld `dice-roller/index.html`, `dice-roller/privacy.html`, `dice-roller/support.html`.
- Verander of verwijder niets wat er al staat. Dat geldt voor elke bestaande pagina, `assets/`, `styles.css`, `index.html`, `sitemap.xml` en alle andere bestaande bestanden en mappen.
- Bekijk de bestaande pagina's alleen om de stijl en de opbouw over te nemen. Linken naar bestaande bestanden (zoals `/styles.css` of `/assets/fonts/`) mag. Wil je iets aanpassen, kopieer het dan naar je eigen productmap.
- Support op winkelpagina's en productpagina's: **thijs@dortus.com** (sinds 7 nov 2026, keuze van Thijs: persoonlijker). Niet meer support@dortus.com gebruiken in nieuw werk.
- Opslaan op de site gaat via dezelfde regels: `git pull --rebase`, nooit geforceerd, en afsluiten met `git ls-remote` voor die repo.
