# Logboek jetbrains

Nieuwste blok onderaan.

## 6 nov 2026, eerste run
- **Gedaan:** eerste ronde onderzoek, `kandidaten.md` geschreven, blokkade op de lijst voor Thijs gezet.
- **Beslissing:** voorlopig C, de betaalde visuele editor, want alleen daar is nu een gevraagde prijs bekend. Of mensen betalen is onbekend. Geen bouwbesluit, want de Marketplace-cijfers ontbreken.
- **Beslissing:** A afgewezen als eerste keus, want de JetBrains-help (datum 4 nov) noemt zelf diff en terugdraaien voor agentwijzigingen.
- **Nakijken:** controleur keurde de eerste tekst af op te sterke beweringen, ontbrekende link en twee geschrapte feiten. Verbeterd.
- **Misging:** `plugins.jetbrains.com` onleesbaar via curl (403) en leestool (toestemming niet op tijd beantwoord). Maven en Gradle ook geweigerd. Niet opnieuw geprobeerd en geen omweg gezocht.

## 6 nov 2026, 14:52 UTC
- **Gedaan:** bereikbaarheid getest en één echte build van een lege plugin geprobeerd. Beide geweigerd of mislukt, zie `status.md`. Java 21 en Gradle 8.14.3 staan er wel.
- **Beslissing:** gestopt met de kandidaten-controle. WebSearch gaf alleen titels en links, en die pagina's zijn niet te lezen, dus geen bewijs om een keuze op te baseren. Geen omweg gezocht via GitHub Actions: die keuze is aan Thijs, staat op de lijst.
- **Nakijken:** geen controleur ingezet, er is alleen een meting genoteerd en geen werk opgeleverd.

## 6 nov 2026, 15:52 UTC
- **Gedaan:** curl naar `plugins.jetbrains.com` en `plugins.gradle.org` nog steeds 403 (niet herhaald). Daarna de Marketplace-API via de leestool (WebFetch) geprobeerd: dat werkt. Controle uit `kandidaten.md` gedaan, `marktmeting-2026-11-06.md` geschreven.
- **Beslissing:** richting D, betaalde taalondersteuning voor een bestandssoort die de IDE niet goed kent, want in de betaalde top 48 zitten 9 zulke plugins met 37.000 tot 620.000 downloads, tegen 6 betaalde visuele editors met 7.000 tot 89.000 en veel gratis diagramplugins. C blijft reserve. Nog geen bouwbesluit: de soort is niet gekozen.
- **Beslissing:** WebFetch is geen omweg, het is de gewone leestool die de eerste run ook al probeerde. Bouwen via GitHub Actions blijft aan Thijs.
- **Nakijken:** controleur keurde af op het totaal (533 bij zijn telling, 539 bij de mijne), "de grootste groep" zonder telling, "minder gratis concurrentie" zonder meting en een te stellige zin. Alles verbeterd of weggehaald, verschil in totaal staat erbij.
- **Misging:** Gradle nog dicht, dus geen build. Het verschil 539 en 533 is niet verklaard.

