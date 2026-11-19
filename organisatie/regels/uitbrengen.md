# Uitbrengen

Lees dit als je een product of versie live zet. Laad ook de skill `uitbrengen`.

## Uitbrengen: eigen openbare repo per product
- Elk product dat live gaat, krijgt een eigen openbare repo onder het account van Thijs (bijvoorbeeld `thijsduinhouwer2002-coder/rollwright`). Daar staat alleen wat openbaar hoort: code, tests, README, LICENSE, CHANGELOG. Geen interne notities, geen e2e, geen ontwerpstukken. Het werk zelf blijft in dortus-hq. Betaalde code (Hats, Bison & Flex, Click Joints Pro) gaat vóór de paginadag van Hats naar een privé-repo; de openbare repo blijft dan het loket voor meldingen en voor gratis producten (besluiten, Twijfel 9).
- Zo'n repo maakt Thijs aan (één klik, het systeem staat het ons niet toe). Uitbrengen gaat daarna met een tag-push (bijvoorbeeld `click-joints-v0.1.3`): die start de uitgave-workflow, met dezelfde controles (tests groen, Daan akkoord). Zie `organisatie/toegang.md` en de skill `uitbrengen`.
- Uitbrengen gaat zonder Thijs: het script `producten/<product>/publiceer.sh` zet de openbare bestanden in die repo. Met `release` als tweede woord maakt de workflow daar vanzelf een release met de versie uit `manifest.json` (sjabloon: `organisatie/sjablonen/obsidian-release.yml`). Updates pikt Obsidian daarna zelf op.
- Alleen uitbrengen als de e2e-test groen is en Daan akkoord gaf, ook voor de README (dat is de winkelpagina).
- De allereerste aanmelding bij een platform (bijvoorbeeld Obsidian via community.obsidian.md) doet Thijs één keer met zijn eigen login. Zet die klaar op zijn lijst met precies wat hij moet invullen.

## Wie zet live (18 nov 2026)
Eerste lancering, nieuwe winkel of prijswijziging: de hoofdchat, na Daan. Update van een product dat al live staat: de eigenaar via de workflow, na een keuring (skill `keuren`). Dit vervangt voor updates de oudere regel dat alleen de hoofdchat live zet.

## Ritme na het uitbrengen (18 nov 2026, afgekeken bij de winnaars)
Bron: `platformen/ideeen/afkijken-2026-11-18/UITKOMST.md` en `J-brede-scan.md`. Winnaars zijn niet beter in bouwen maar in alles daarna. Voor elk live product waar we in investeren (nu Hats, Click Joints en Pro, Bison & Flex). Geparkeerde producten krijgen alleen bugfixes.
1. **Uitbrengen met één knop.** Een workflow bouwt, test en zet de versie in de winkel (zoals `submit-blender` bij CAD Sketcher, één workflow naar VS Code én Open VSX bij GitLens). Thijs klikt niet per update. Waar de winkel geen sleutel toestaat, zet de workflow alles klaar tot de laatste klik.
2. **Elke 2 tot 3 weken een kleine versie met een post erbij**, ook als het weinig is. Winnaars brengen 16 tot 45 versies per jaar uit. Let op (onderzoek marketing 18 nov): een versie geeft zelden een betere plek in de winkel (JetBrains ±45 min bovenaan, Blender en Garmin niets); de waarde zit in de post bij de versie, de bestaande gebruikers en bij Obsidian de downloadteller.
3. **Eén `CHANGELOG.md` per product** die alles voedt: de release, de "wat is nieuw" in de winkel en de post. Maak de tekst met de skill `update-tekst`.
4. **README en winkelpagina zoals de winnaars:** bovenaan een beeld of GIF van het resultaat, daarna de belofte in één zin, daarna gratis tegenover Pro in een lijstje. Geen muur van tekst.
5. **Gratis naast betaald, als twee aparte producten** waar de winkel dat toestaat (Rainbow Brackets Lite, Nginx Configuration naast Pro). De gratis versie vangt de zoekers en wijst door.
6. **Ken je gebruikers.** Zet de gratis versie ook op Gumroad als "$0+" (CAD Sketcher, Blosm): dat geeft een maillijst en zichtbare beoordelingen.
7. **Eén vaste plek om gevonden te worden** per product (zoeken in de winkel, één SEO-pagina, één community), en die goed. Niet tien plekken half.
8. **Meten op dag 1, 7 en 14** en daarna elke week in `organisatie/scorebord.md`.

## Lanceerlijst (17 nov 2026, na de rondgang met Thijs)
Elk product loopt deze lijst door vóór het "af" heet, en opnieuw bij elke nieuwe versie. De stand per product staat in `organisatie/lanceerlijst.md`.
- **Echt getest** zoals de koper het gebruikt (een echte print, een echt horloge of een mens die speelde, een echte installatie). Nog niemand het echt gebruikt: geen geld vragen en geen beloftes die dat vragen.
- **Waarde en prijs:** in één zin wat de koper krijgt en waarom het beter is dan gratis; gratis of betaald om een reden met cijfers; prijs gelijk in winkel, site en posts.
- **Winkelpagina:** zoekwoord vooraan in de titel; elke zin bewezen; beelden van het resultaat; elk veld van de winkel gebruikt (banner, video, alle beelden, supportadres); gratis linkt naar betaald waar het mag; geen resten van een oude versie.
- **Verspreiden, dezelfde dag:** pagina op dortus.com, bericht waar de gebruikers zitten (regels gelezen; TikTok en YouTube via Roep in `marketing/wachtrij/`, andere plekken via de hoofdchat), filmpje, reacties binnen 24 uur beantwoorden.
- **Meten:** dag 1, 7 en 14 en een stopregel vooraf.
