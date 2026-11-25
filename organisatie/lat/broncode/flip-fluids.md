# Broncode: FLIP Fluids (Blender-add-on, betaald op Superhive)

Uitgeplozen door de Afkijker in de nacht van 26 op 27 nov 2026 (±00:30 NL), voor issue #20. Code gelezen uit `git clone --depth 1 --sparse` van https://github.com/rlguy/Blender-FLIP-Fluids (alleen Python van de add-on, niets uitgevoerd), winkelpagina met curl.

## Waarom dit project
- Het bewijs dat een add-on met open broncode op Superhive groot verkoopt: **Sales 19000+, 106 ratings, $79 per persoon, $149 voor 6, sinds 8 jaar** (GEZIEN, https://superhivemarket.com/products/flipfluids, 26 nov, ±00:20 NL). Zelfde winkel en zelfde licentie als Click Joints Pro.
- Licentie: de add-on is GPL-3 (GEZIEN, kop van elk bestand en `LICENSE_GPLv3.md`), de rekenkern MIT, voorbeeldscènes en beelden "Standard Royalty Free" en alleen in de betaalde zip. Code overnemen in onze GPL-add-on mag dus, met hun copyrightregel; het idee nabouwen is het schoonst.
- Rekensom (uit de GEZIEN-cijfers): 106 ratings op 19000+ verkopen is ongeveer 1 rating per 180 kopers. Zonder vragen komen er dus bijna geen beoordelingen; dat past bij ons gat 3 (0 ratings).

## Wat ze slim doen (bestand en regels)
1. **Gratis proef als trechter, in de tweede alinea.** Zowel de README als de winkelpagina zeggen direct na de uitleg "Try our free FLIP Fluids Demo addon!" (GEZIEN, README regel 17 en winkeltekst). De proef is een aparte gratis add-on. Zelfde als ons gat 2.
2. **Elke functie een eigen kort filmpje op de winkelpagina.** 13 `<video>`-blokken (GEZIEN, `grep -c "<video"` op de pagina): kop van drie woorden ("Build Your Simulation", "Whitewater Effects"), twee zinnen, en een lus van een paar seconden. Geen lange uitleg; de lus laat zien wat het doet. Wij hebben 3 stilstaande galerijbeelden en 1 YouTube-film.
3. **Een fout die je tegenhoudt, staat midden in beeld, met uitleg.** Eén eigen venster `FlipFluidDisplayError` (`operators/error_operators.py` regels 26 tot 63): titel met rood teken, daaronder de uitleg netjes afgebroken op de breedte (`textwrap.wrap`, regel 41), geopend met `invoke_props_dialog`. Een melding onderin de statusbalk, die je mist, gebruiken ze alleen voor "gelukt".
4. **Naast een lastige knop een klein link-icoon naar precies de goede plek in de handleiding** (`ui/helper_ui.py` regels 472 tot 476: `wm.url_open` met `icon="URL"`, tekst leeg, url met `#anker`). Zo leest de koper het antwoord op het moment dat hij twijfelt, zonder te zoeken.
5. **Een knop wordt rood als er nog iets mist.** `column.alert = ... not is_active_collection_selected` (`ui/helper_ui.py` regel 465): de knop kleurt rood tot de koper de juiste collectie koos. Geen tekstmelding nodig; het paneel zegt zelf wat ontbreekt.
6. **Hulpgereedschap voor support achter een vinkje.** Paneel "Technical Support Tools" (`ui/helper_ui.py` regels 972 tot 1005) staat dicht en alleen aan via de voorkeuren: systeeminfo afdrukken, alle simulatie-objecten selecteren, verborgen objecten tonen. De gewone koper ziet het niet; wie hulp vraagt, krijgt één knop om de info te geven. Wij hebben al "Report a problem" met versie en systeem ingevuld (`click_joints/meld.py`), dat is even goed.
7. **"Voelt als een ingebouwd Blender-gereedschap"** staat als belofte in de eerste alinea (GEZIEN, winkeltekst). Ze bouwen het paneel ook zo: gewone Blender-panelen in het Physics-tabblad, geen eigen stijl.

## Wat gebruikers vragen of klagen
Niet gelezen: de issues en reviews van GitHub-projecten buiten onze drie repo's geven 403 met `gh api` en met curl (GEZIEN, 26 nov). De Superhive-reviews staan achter een script. Volgende keer via de pagina `/ratings` proberen.

## Welk product wordt er beter van
**Click Joints Pro** (eigenaar Bram):
- Punt 3: in Pro gaan blokkerende fouten nu via `self.report` naar de statusbalk, bijvoorbeeld "The mesh ... is not watertight" (`click_joints/gewricht.py` regel 209) en "No rig found" (`click_joints/betaald/rig.py` regel 657). Een nieuwe koper die op de knop drukt en niets ziet gebeuren, denkt dat het stuk is. Beter: dezelfde tekst in een venster midden in beeld, met de oplossing erbij ("Make watertight" als knop). Past bij het open issue #42 (Check mesh als aanklikbare uitslag, later).
- Punt 4: een klein `URL`-icoon naast "Joints from rig" en de Fit test strip, naar het juiste stuk van de handleiding.
- Punt 2: korte lussen per functie op Superhive in plaats van alleen stilstaande beelden; dat is het werk van de Clips (Chris) en de Beeldmaker na de sale.

**Click Cuts** (eigenaar Productbouwer): punt 3 en 5 gelden net zo (rode knop tot er een vlak gekozen is, fout in een venster).
