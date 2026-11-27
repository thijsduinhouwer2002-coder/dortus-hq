# Broncode: RetopoFlow 4 (Blender-add-on, betaald op Superhive, code open op GitHub)

Uitgeplozen door de Afkijker op vr 27 nov 2026 (±13:30 NL), voor issue #20. Code gelezen uit `git clone --depth 1 -b 4.0.3` van https://github.com/CGCookie/retopoflow (laatste commit ba1f729, 17 feb 2026, manifest versie 4.1.0; niets uitgevoerd). Winkelpagina, alle 7 reviewpagina's en de hulp van Superhive met curl gelezen op 27 nov.

## Waarom dit project
- **Superhive: Sales 11800+, 62 beoordelingen, gemiddeld 4, prijs $59,99** (GEZIEN, [productpagina](https://superhivemarket.com/products/retopoflow)). Verdeling 5 tot 1 ster: 67%, 15%, 4%, 10%, 7% (GEZIEN, [ratings](https://superhivemarket.com/products/retopoflow/ratings)). Dat is ruwweg 1 beoordeling per 190 verkopen (GEZIEN, gerekend).
- Prijs is inclusief 12 maanden support en updates; verlengen kost 50% van de prijs (GEZIEN, productpagina).
- **"Featured in Bundles 5"**, waaronder de bundel "Creature and Character Creation" van Superhive zelf (24 producten, $365; GEZIEN). Een koper schrijft: "I learned about this tool through a Superhive bundle I bought several months ago" (terry g morse, GEZIEN op ratings pagina 3).
- De code is gratis op GitHub "especially for students, teachers" en wie betaalt krijgt voorrang bij support (GEZIEN, `README.md` op main, kop Downloading). Licentie: GPL (manifest `SPDX:GPL-2.0-or-later`, kop van de bestanden GPL-3 of later; GEZIEN). Wij lenen dus alleen ideeën.

## Wat ze slim doen (bestand en regels)
1. **Alles wat ze aan Blender veranderen, zetten ze terug.** Een klein hulpje `Resetter` onthoudt de oude waarde van elke instelling vóór ze hem wijzigen en zet hem terug bij het verlaten (`addon_common/common/resetter.py` r. 26 tot 96). Bij het starten gaan snappen, draadmodel, vervagen, puntgrootte en de retopologie-laag via dat hulpje aan (`retopoflow/rfcore.py` r. 364 tot 409), elk met een eigen schakelaar in de voorkeuren. Op de winkelpagina is dit een verkoopzin: "switching to any other tool puts all your settings back".
2. **Opslaan zonder rommel.** Vlak voor het opslaan zetten ze het gewone gereedschap terug en na het opslaan hun eigen gereedschap weer aan; bij het openen van het bestand komt het terug (`rfcore.py` r. 578 tot 600). Een bestand dat een klant deelt, heeft dus nooit hun modus vast.
3. **Hulp per gereedschap.** De hulptoets opent de pagina van het gereedschap dat nu actief is, anders de inhoudsopgave (`retopoflow/rfoperators/launch_browser.py` r. 79 tot 93). In de kop van het scherm staat een Help-menu met drie knoppen: "Read the Docs", "Report an Issue", "View on Superhive" (`retopoflow/rfpanels/help_panel.py` r. 25 tot 36).
4. **Waarschuwingen met een naam.** Een verkeerd ingepakte zip (map met een streepje, zoals de GitHub-zip) geeft een eigen melding met de oplossing (`help/warnings.md` op main, "Installation: Invalid add-on folder name"); de README zegt het ook vetgedrukt: "Do _not_ use the zip files created by GitHub".

## Wat kopers klagen (alle 62 reviews gelezen, GEZIEN 27 nov)
- **Instellingen bleven hangen na het verlaten** (snappen, auto-merge, overlay; dfw2412, 6 maanden geleden). Dat is precies punt 1: gaat het terugzetten één keer mis, dan komt er meteen een lange klacht.
- **Beloofd maar nog niet af:** "Patches feature that has been 'coming soon' from the beginning ... is the same as it was from when I purchased" (Vard). Lex en Misho zeggen hetzelfde over functies uit versie 3.
- **Opnieuw betalen voor de nieuwe grote versie:** "I paid for V3 ... then they require you to purchase a whole new license for V4" (eli).
- **Werkt niet op de nieuwste Blender:** "Why it doesn't work with blender 4.5??????" (gleb, Blender 4.5 was toen minder dan een week uit).
- **Geen proefversie:** "It would be nice if there were a trial version" (ohya).
- **Wat het goed maakt:** bij elke kritische review die ik las (Kim, James, dfw2412, eli, Grant, Rhonda, Antonino, Lex, Ivo, ohya, gleb) staat een antwoord van de maker, met de oplossing of de instelling, "message us", en één keer "If we can't fix it, you can get a full refund". Wie later terugkwam, zette er een betere review onder (Ryan Ernst: "a developer reached out to me personally after my first review").
- Issues op GitHub kon ik niet lezen: die repo zit niet in de toegang van deze geplande taak (API weigert), de webpagina geeft 403.

## Nieuw over Superhive (bijvangst, belangrijk voor geld)
- **Makers kunnen sinds kort zelf bundels maken op Superhive.** De hulp "Creating and Selling Your Own Bundles" is bijgewerkt op 24 nov 2026 (GEZIEN, [artikel 403](https://support.superhivemarket.com/article/403-creating-bundles)). Alleen eigen producten, minstens 2; eigen prijs of treden ("starter" en "complete"); een tabblad Scheduling met start- en eindtijd; de prijs wordt verdeeld naar de gewone prijs van elk product; zelfde commissie als losse verkoop. De bundel staat **bovenaan je winkelpagina, in de bundellijst van Superhive en in de zoekresultaten**.
- Onze winkeltekst zegt nog "Hoe je hem aanmaakt staat niet in de openbare hulp" (`platformen/blender/superhive/click-cuts-winkeltekst.md` r. 87). Dat is nu wel zo.
- **Bundels van Superhive zelf** (zoals die van $365 met RetopoFlow) krijg je alleen met de schakelaar "First Party Bundles" (en "Third Party Bundles") aan in Marketing Preferences (GEZIEN, [artikel 337](https://support.superhivemarket.com/article/337-marketing-preferences)): "Creators with the relevant preference enabled are our starting point". Wij hebben daar sitewide sales aan (`commercie/geplaatst.md` r. 91); of de bundelschakelaars aan staan, staat nergens.
- Een bundel voor 3D-printen zag ik niet tussen de 95 bundels op pagina 1 tot 5 van https://superhivemarket.com/bundles (GEZIEN, gezocht op print, mini, figure, maker in de adressen).

## Welke van onze producten er beter van wordt
- **Click Joints Pro en Click Cuts (samen):** de bundel "Figure Print Kit" kan nu ook op Superhive, en met de Scheduling-tab vooraf klaargezet voor na 14 dec (`click-cuts-winkeltekst.md` punt 5). Plus de schakelaars voor bundels van Superhive aan. Gezet als #270 bij Bram.
- **Click Cuts:** wij veranderen geen instellingen van de koper (geen `tool_settings`, `overlay` of `shading` in `producten/blender-splitser/split_joints/`, GEZIEN met grep), en `exporteer.py` r. 120 en 153 en `passingproef.py` r. 149 en 207 zetten het actieve object terug. Zo houden; mocht 1.1 snappen of een kijkstand aanzetten, dan alleen met terugzetten zoals punt 1. De Help-knop staat al in #268; hulp per stap (zoals punt 3) is een kleine uitbreiding daarvan.
- **Winkelteksten van alle Blender-producten:** nooit "coming soon" of een toekomstige functie in de etalage, en een gratis versie of de Fit test strip noemen als "proef" voor wie twijfelt (ohya). Elke kritische review krijgt binnen een paar dagen een antwoord met de oplossing (geldt ook voor Extensions en Gumroad).
- **Na een nieuwe Blender-versie:** dezelfde dag de e2e op die versie draaien en het bereik op de pagina bijwerken (gleb).
