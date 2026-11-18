# Roestronde 19 tot 21 nov 2026

Thijs, 18 nov 23:46: "ja we doen A, maar maak hem breed". Doel: de komende 30 dagen met een geoliede machine werken. Klaar uiterlijk za 21 nov 20:00, daarna volle kracht op distributie.

**Buiten de roestronde:** de Hats-code (`producten/steam-hol/`) en de speeltest van za 21 nov. Olaf, Bram, Sanne en Iris blijven daarop. Roestwerk dat Hats raakt (crashmeldingen) komt na de speeltest.

**Werkwijze:** zes roestagents (R1 tot R6) tegelijk, ingezet door de hoofdchat. Elk punt is pas af als een ander het keurde (skill `keuren`) en de tests groen zijn. Product-code van Click Joints en Bison & Flex mag op main, maar uitbrengen doet de eigenaar via de workflow (`organisatie/regels/uitbrengen.md`).

| # | Roest | Wie | Klaar als |
|---|---|---|---|
| R1 | **Workflows traag en rommelig.** De repo is 1,2 GB; een volledige checkout duurde 11 minuten (GEZIEN, keurder 18 nov). Workflows van gestopte producten draaien of staan nog in de lijst. Rode workflows. | agent R1 | elke workflow haalt alleen op wat hij nodig heeft; workflows van gestopte producten staan in `.github/workflows-uit/`; lijst rood/groen per workflow in dit bestand, rode van niet-Hats-producten gerepareerd |
| R2 | **Agents kunnen niets op GitHub zelf.** Hun GitHub-sleutel werkt niet, dus geen workflow starten of uitslag lezen; de hoofdchat doet dat met de hand in Chrome. | agent R2 | een agent start een workflow door een bestand te pushen, en leest uitslag en log zonder sleutel; getest; uitgelegd in een skill `actions` |
| R3 | **Rolbestanden te lang en verouderd** (100 KB in `organisatie/rollen/`, GEZIEN). Elke agent leest bij de start oude rommel. | agent R3 | elke rol kort (doel, wat je doet, wat je niet doet, waar je schrijft), oude versies in `organisatie/archief/`, geen tegenspraak met CLAUDE.md en de regels |
| R4 | **We testen alleen bij een push**, niet tegen de volgende Blender, IDE of Obsidian; en we zien niet vanzelf als een scherm verandert. | agent R4 | wekelijkse run tegen Blender alpha, IntelliJ/CLion EAP en de nieuwste Obsidian; beeldvergelijking met de vorige run in de e2e van Click Joints, Bison & Flex en Rollwright; rood komt in het berichtenbestand van de eigenaar |
| R5 | **Klachten komen in reviews in plaats van bij ons.** Geen meldknop, geen meldformulieren in de loketrepo's, foutmeldingen van Bison & Flex gaan nergens heen, listingvelden leeg. | agent R5 | error handler in Bison & Flex; meldknop in Bison & Flex, Click Joints (zonder enige Pro-verwijzing in Free) en Rollwright met versie en systeem ingevuld; meldformulieren in de loketrepo's klaar als bestanden (plaatsen in de repo's van Thijs na zijn ja); workflow die nieuwe meldingen naar `berichten/hoofdchat.md` zet |
| R6 | **Meten is half en filmpjes gingen zonder geluid.** Het scorebord mist cijfers die we voor 9 dec nodig hebben; geen controle op geluid voordat een filmpje live gaat. | agent R6 | scorebord meet elke dag alle openbare cijfers (Blender, JetBrains, Obsidian, Garmin, Gumroad, Kit-abonnees, Discord-leden, YouTube) met GEZIEN; filmpjes-workflows weigeren een filmpje zonder hoorbaar geluid |
| H | **Mensen die langskomen raken we kwijt.** Geen aanmeldvak op de productpagina's, geen Hats-pagina (dortus.com/hats geeft 404, GEZIEN). | hoofdchat | Kit-aanmelding op de productpagina's en `/hats`, CSP aangepast, getest met een echte aanmelding |

## Stand
(de roestagents schrijven hier per punt een regel onderaan: datum, wat af is, keuring, hash)
- 19 nov 00:15, hoofdchat, H deels af: aanmeldvak "Updates by email" op dortus.com/click-joints, /bison-flex en /rollwright (Kit-formulier 10210621, gewone HTML-post zonder script, CSP form-action uitgebreid met app.kit.com), live en bekeken in Chrome (GEZIEN). Open: (1) Thijs klikt de bevestigingslink van Kit aan, dan doet hij één proefaanmelding met zijn eigen adres; (2) pagina `/hats` wacht op tekst van Thijs (Hats-tekst schrijft hij zelf); (3) abonnees tellen in het scorebord doet R6. Site-commit dfcab05.
