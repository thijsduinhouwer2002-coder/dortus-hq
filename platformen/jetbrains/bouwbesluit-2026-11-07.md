# JetBrains: bouwbesluit (7 nov 2026, Jet)

**Besluit (nagekeken, zie onderaan):** de eerste betaalde JetBrains-plugin wordt een plugin voor **Yacc/Bison en Lex/Flex** (`*.y`, `*.yy`, `*.l`, `*.ll`), freemium, gericht op CLion. Tcl valt af als eerste product. Alles hieronder komt uit `marktmeting-2026-11-06.md` deel 10 tot 13.

## Scoreschema (1 = slecht, 5 = goed)

| | Yacc/Bison + Lex/Flex | Tcl | Maatstaf: Jenkinsfile (betaald, groeit) | Maatstaf: Procfile (betaald, blijft klein) |
|---|---|---|---|---|
| **Vraag** | 2: `*.y` 137.984 bestanden, 72% groter dan 2 kB; `*.l` 361.472, waarvan ruwweg een derde Lex (GOK); 8 stemmen in YouTrack; Bison Language Support 13.020 downloads sinds mei 2021, de laatste versie ruwweg 200 per maand (GOK, gemiddelde) | 4: 2.150.400 bestanden, 66% groot, maar veel gegenereerd (GOK); 38 stemmen in CLion; Tcl Language Support ±450 downloads per maand sinds mei 2026 (GEZIEN, 2.737 in ±6 maanden) | 5: 204.800 bestanden, 44% groot, tientallen stemmen | 1: 2% groot, geen stemmen |
| **Betaalbewijs** | 2: geen betaalde plugin voor deze soort. Wel: C/C++-ontwikkelaars in CLion, een betaalde IDE die veel bedrijven kopen (GOK). Betaalde niche-taalplugins bestaan: de reeks "Flexible" van Ilscipio GmbH, ±20 plugins, $49 tot $79 per jaar, downloads opgeblazen door bijna dagelijkse versies, verkoop niet aangetoond (GEZIEN door de controleur) | 2: geen betaalde plugin. Chipontwerpers werken bij bedrijven met dure licenties (GOK), maar ze hebben al een uitgebreide gratis plugin | 5: reviews van kopers | 3: kopers onbekend |
| **Concurrentie** | 4: geen IDE kent de soorten (GEZIEN, 2026.3); voor Lex/Flex geen enkele plugin; maar voor `*.y` bestaat de gratis Bison Language Support met kleuren, folding en structuur, laatste versie 2023 | 2: Tcl Language Support (AGPL, taalserver met aanvullen, ga naar definitie, hernoemen, formatter) plus HDL and Vivado. Wel zwak punt: nog niet voor 2026.3, sinds 10 september stil | 3 | 4 |
| **Bouwtijd** | 4: twee kleine talen met een vaste opbouw; parser met Grammar-Kit en JFlex, zoals elke JetBrains-taalplugin (GOK, ±2 tot 3 weken voor een eerste versie, optimistisch: de koppeling tussen `.y` en `.l` en zeker uitleg van conflicten kosten meer) | 2: een volledige taal met veel dialecten (Tk, Expect, iRules, EDA-commando's); om de gratis plugin te verslaan is veel nodig (GOK) | | |
| **Totaal** | **12** | **10** | | |

**Gevoeligheid (nagekeken):** bouwtijd telt hier even zwaar als vraag, terwijl de doelen zeggen dat de markt het probleem is, niet het bouwen. Zonder bouwtijd staat het 8 tegen 8. Telt vraag dubbel (zonder bouwtijd), dan wint Tcl met 12 tegen 10. Op de cijfers alleen is er dus geen duidelijke winnaar. De doorslag geeft de concurrentie: bij Tcl moet een betaalde plugin opboksen tegen een gratis, volledige taalserver, bij Bison/Flex niet. Dat is een oordeel (GOK), geen meting.

## Waarom Yacc/Bison + Flex
- **Het gat is echt en leeg.** Wie in CLion een `.y`- of `.l`-bestand opent, krijgt een onbekend bestand. Voor `.l` is er niets, voor `.y` alleen oude plugins. Een nieuwe plugin die de soort aanmeldt wordt door de IDE vanzelf aangeraden (deel 10, eis 2). Dat is het mechanisme dat BatchCraft liet groeien (deel 6, GOK voor het verband).
- **Het betaalde deel is te trekken (GOK, niet bewezen dat iemand ervoor betaalt).** Gratis: kleuren, folding, structuur voor `.y` en `.l`. Betaald: wat de oude plugins niet hebben, zoals ga naar definitie en hernoemen over `.y` en `.l` heen (tokens uit Bison die Flex teruggeeft), fouten zoals ongebruikte of niet gedefinieerde regels en tokens, en uitleg van shift/reduce-conflicten. Het ontwerp legt dit vast.
- **Geld gaat voor bereik** (doelen): bij Tcl moet een betaalde plugin opboksen tegen een gratis plugin die al veel kan. Bij Bison/Flex is er alleen een oude gratis plugin voor `.y` en niets voor `.l`, dus wie meer wil dan kleuren heeft weinig keus (GOK dat dat tot betalen leidt; zonder plugin kan iemand ook gewoon verder).
- **Snel klaar, weinig risico.** De bouwtijd laat ruimte voor de IDE-test, het ontwerp met Daan en de beoordeling door JetBrains.

## Eerlijk: wat tegen dit besluit spreekt
- **De markt is klein.** Op ruwweg 200 downloads per maand (GOK) en 2 tot 5% betalers (GOK) bij $20 per jaar (GOK, prijs nog niet gekozen) is dit enkele tientjes per maand, ver onder de €300 tot €400 van maart (doelen). Dit product haalt het doel niet alleen. **Dit is daarom uitdrukkelijk geen keuze om het meeste geld, maar een eerste product dat de hele weg bewijst** (bouwen, testen in de echte IDE, keuren door Daan, verkopen, uitbetalen) met het kleinste risico, en de basis voor een tweede. Ook de tussenstap van €100 per maand in februari haalt dit product niet alleen. Daarom staat het zoeken naar een tweede, grotere kandidaat als vaste taak hieronder.
- **Vraag is zwak gemeten:** 8 stemmen, en de downloads zijn een gemiddelde over jaren, geen meting van nu.
- **Niet getest of de oude Bison-plugin nog werkt** in 2026.3 (alleen afgeleid uit gegevens). Werkt hij goed, dan is het gat voor `.y` kleiner; voor `.l` blijft het.

## Wat dit besluit zou veranderen
- Op dag 30 na lancering onder de 30 gebruikers: stoppen of veranderen (stopregel).
- Tcl Language Support stopt of wordt niet bijgewerkt voor 2026.3 en 2027.1: dan Tcl opnieuw bekijken als tweede product.
- Een nieuwe Bison/Flex-plugin van iemand anders vóór onze lancering: opnieuw bekijken. Concreet risico: Ilscipio GmbH brengt snel nieuwe betaalde taalplugins uit (reeks "Flexible") en kan er ook een voor Bison maken.

## Volgende stappen
1. Ontwerp in `producten/jetbrains-bison-flex/ontwerp.md` (wat gratis, wat betaald, toetsbare eisen), keuren door een controleur en Daan.
2. IDE-test op GitHub Actions met schermafbeeldingen licht en donker naar de tak `schermen`.
3. Bouwen vanuit `bouwsjabloon.md`, op een tak `claude/jetbrains-<datum>`.
4. Naast de bouw: een tweede, grotere kandidaat zoeken binnen wat al gemeten is (Tcl met een kleinere insteek, Jenkinsfile-achtige soorten), zodat er na de eerste lancering meteen een tweede product klaarligt.

**Nakijken (7 nov 08:20 UTC):** controleur mat de getallen opnieuw (Bison ±217 per maand op de laatste versie, Tcl ±480 per maand sinds 18 mei, geen Lex/Flex-plugin, de Flexible-reeks) en koos met dezelfde gegevens ook Bison/Flex. Akkoord mits 7 punten: bouwtijd wegen en gevoeligheid tonen, concurrentie naar 4, drie zinnen als GOK, Flexible-reeks preciezer, Ilscipio als risico, doel van het product helder plus een tweede kandidaat, en een fout getal in deel 11. Alle 7 verwerkt.
