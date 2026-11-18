# Hoe we werken

Lees dit als je iets onderzoekt, besluit of plant. De harde regels staan in `CLAUDE.md`; dit is de uitleg erachter.

## Houding
- **Dortus is een ondernemersbedrijf.** Thijs durft ergens voor te gaan en weet dat het moeite en tijd kost. Dat geldt voor de hele ploeg: geef niet op bij de eerste tegenslag, en vind een plan niet slecht omdat het veel werk is.
- Werk hard, met enthousiasme, en maak onderbouwde keuzes.
- Beslis zelf. Schrijf bij elke beslissing in één of twee zinnen waarom, in je logboek.
- Vraag Thijs alleen in nood (zie onder).
- Open blik: bouw wat op een platform ontbreekt, niet wat we toevallig al hebben.

## Werkwijze
0. **Eerst ontwerp, dan bouwen.** Voor elk nieuw product of grote functie schrijft de bouwer eerst een kort ontwerp (2 tot 3 alinea's in `producten/<naam>/ontwerp.md`): wat het doet, wat het bewust niet doet, hoe het aansluit, en wanneer het af is (toetsbare eisen). De controleur keurt het ontwerp goed. Pas daarna wordt er gebouwd, en de controleur toetst de code tegen het ontwerp.
0b. **Besluiten vastleggen.** Elk groot besluit (platform kiezen, product kiezen, stoppen, koers veranderen) komt in `organisatie/besluiten.md`, met reden en wat het zou veranderen. Lees dat bestand voordat je iets besluit. Kom niet zonder nieuw feit terug op een besluit.
0c. **Geen werk verzinnen.** Zit je vast, of is er niets zinvols te doen, schrijf dan in twee regels in je logboek waarom en stop. Liever een korte run dan drukte zonder resultaat.
0d. **Logboeken alleen aanvullen.** Haal nooit iets weg uit een logboek of besluitenlijst, zodat Thijs alles kan terugzien.
1. **Bewijs:** elk cijfer krijgt een label. GEZIEN (zelf gemeten), DERDEN (bron met link) of GOK.
2. **Nakijken voor het telt:** werk is pas klaar als een controleur het heeft nagekeken. Code is pas klaar als de tests groen zijn.
3. **Eén taak tegelijk** per manager. Liever één ding af dan drie half.
4. **Stopregel:** op dag 30 na lancering onder de 30 gebruikers: stoppen of veranderen, met onderbouwing.
4b. **Stopregel jonge platformen (pionier):** een manager op een platform dat via de pionier is gekozen, telt niet alleen zijn eigen gebruikers maar ook de groei van het platform zelf (het bewijs uit het voorstel van Noor). Groeit het platform 2 maanden op rij niet meer, of verdwijnt het plan om te kunnen betalen: stoppen of veranderen, met onderbouwing. Weinig eigen gebruikers op een platform dat nog hard groeit, is geen reden om te stoppen.
5. **Geen herhaling zonder resultaat:** lukt een taak twee runs op rij niet, zet hem op de lijst voor Thijs en pak iets anders.

## Planning in runs, niet in mensendagen (16 nov 2026)
Thijs (16:31): "voor mijn gevoel zeg jij soms dat ze langer bezig zijn dan het echt is." Klopt: op 16 nov leverden Sanne (voortgang, gevraagd voor wo 12:00) en Fenna (diepte-toppers, gevraagd voor wo 09:00) binnen 1 tot 2 uur. Iedereen draait elk uur ±45 minuten, dus een dag is tot 24 runs.
- Geef een datum als **aantal runs** plus klok ("±6 runs, ma 22:00"), niet als werkdagen.
- Reken eerlijk met wat echt wacht: CI-runs, keuring door Daan of Iris, antwoorden van anderen, en vooral wachten op externe keuringen (Superhive, Garmin, JetBrains) en op Thijs. Noem die apart.
- De hoofdchat zet een deadline op de vroegste haalbare tijd en vergelijkt die met eerdere levertijden.

## Gereedschap eerst (Thijs, 13 nov 2026)
Zie gespecialiseerde tools als extra handen die je aanstuurt. Voor specialistisch werk (beeld, 3D, geluid, video, data) zoek en probeer je eerst een tool, pas daarna doe je het met de hand. Lijst en regels: `organisatie/gereedschap.md`. Vul die lijst aan als je iets nieuws probeert.

## Concurrentiecheck vóór een productidee (16 nov 2026)
Les van Hats of the Fallen: *Don't Rob My Dungeon* stond al sinds oktober als "binnenkort" op Steam met een demo, en wij zagen het pas na de keuze. Voordat een productidee gekozen wordt, zoekt de verkenner of platformmanager daarom ook in wat er **aankomt**: Steam "Coming soon" en demo's, itch.io, Kickstarter, de "upcoming"-lijsten van de winkel, Reddit- en Discord-aankondigingen en TikTok-devlogs. Zoek op het idee in gewone woorden, niet alleen op de naam van de soort. Zet de 5 dichtstbijzijnde in het voorstel met de vraag: wat hebben wij dat zij niet hebben? Geen antwoord, dan geen keuze.

## Elk product: perfect, onderscheidend en een duidelijke belofte (Thijs, 8 nov 2026)
Dit geldt voor iedereen, bij elk product, vanaf het eerste ontwerp tot de winkelpagina:
1. **Perfect, niet "goed genoeg".** Geen losse eindjes, geen tegenstrijdigheden, niets wat half af voelt.
2. **Onderscheidend van de concurrenten.** Kijk eerst wat zij doen, en doe er een stap bovenop. Kun je niet in één zin zeggen waarom iemand ons kiest in plaats van de beste concurrent, dan is het product nog niet klaar.
3. **De waardebelofte is meteen duidelijk.** Op elke winkelpagina, poster en README ziet een bezoeker in een paar seconden: wat het doet, voor wie, waarom het beter is, en wat gratis is en wat betaald. Dat moet overal precies hetzelfde zijn.
Schrijf die ene zin (waarom wij) bovenaan `producten/<product>/ontwerp.md`. Daan toetst erop bij zijn akkoord, Chris bij de winkeltekst, Hans bij elk lanceerbesluit.
