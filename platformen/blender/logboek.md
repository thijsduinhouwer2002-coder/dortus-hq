# Blender: logboek

Alleen aanvullen, nooit iets weghalen.

## 7 nov 2026, Hans
- Map aangemaakt na besluit Blender ja (7). Manager Bram, geplande taak elk uur om :07 van 08:00 tot 19:00. Eerste taak: uitzoeken wat we bouwen.

## 7 nov 2026, 22:08 tot 22:35, Bram (eerste run)
- Berichten gelezen (welkom van Hans, lat van Thijs over uiterlijk). Taak 1 opgepakt: wat bouwen we.
- Zelf de steekproef van Vera per categorie uitgesplitst: modelleren levert het meeste (zie `kandidaten-2026-11-07.md`).
- Onderzoeker: toppers, reviews, wensen op BlenderArtists en StackExchange. Reddit geblokkeerd, zoekfunctie Superhive geeft 500 (tagpagina's werken wel). Vijf kandidaten gescoord.
- Controleur: akkoord met correcties. Cijfers klopten, maar mijn voorlopige keus A (printbare gewrichten) rustte op een gat dat er niet is: Cleave heeft sinds v1.6 precies die kogelgewrichten. Besluit: A valt af. Goed dat de controle vóór het besluit kwam.
- Ronde 2 op B en C: geen van beide overtuigt (B zwak betaalbewijs, C sterke goedkope marktleider). Besluit: nog geen bouwbesluit, want geen kandidaat haalt vraag, betaalbewijs en zwakke concurrentie tegelijk; haasten mag niet (besluit Thijs 6 nov). Volgende run een andere aanpak: systematisch klachten per tag doorzoeken.
- Niet gedaan: devtalk, ronde 2 nakijken.
- 22:25 tot 22:45, zelfde run: ronde 2 nagekeken (akkoord met correcties, verwerkt: Seamless CAD draait ook op Mac en Linux, drie producten niet terug te vinden, Quadify toegevoegd). Ronde 3: systematisch per categorie de bestsellers en hun slechtste reviews gelezen. Sterkste vondst: Pie Menu Editor ($16, 2.400+) wordt niet meer bijgewerkt voor Blender 5 en kopers vragen erom. Besluit: nog geen bouwbesluit, eerst nakijken en concurrent PieMaster doorlichten, want een kandidaat afschieten na de controle (zoals A) gebeurde vandaag al één keer.
- 22:30 tot 22:50, zelfde run: ronde 3 nagekeken en gat 1 (opvolger Pie Menu Editor) doorgelicht door twee agents tegelijk. Beiden vonden de bestaande betaalde fork van Pluglug ($36, Blender 5, leest PME-menu's in) en PieMaster ($20, 5 sterren). Besluit: gat 1 valt af. Les vastgelegd in sectie 7: bij een verlaten bestseller eerst zoeken naar forks en opvolgers. Run gestopt na ±45 minuten; geen bouwbesluit, want nog geen kandidaat overleefde de controle.
- 22:32 tot 22:45, zelfde run: bone-jiggle doorgelicht en de zoektocht naar verlaten bestsellers verbreed (120 producten). Besluit: bone-jiggle niet als eerste product (te vol, verkoopverhaal "betrouwbaar" lastig te tonen), verlaten-bestsellers-aanpak gestopt (alles opgevolgd). Volgende run een nieuwe aanpak: nieuwe Blender-functies zonder add-ons. Run gestopt rond 22:47.
- 22:38 tot 22:50, zelfde run: eerste verkenning nieuwe Blender-functies (sectie 10). Lege plekken (Action Slots, VSE 5.0) maar kleine vraag. Geen besluit; volgende run kiezen tussen route "vroeg op nieuwe functie" en route "mooier en beter in een volle markt". Run afgesloten.

## 7 nov 2026, 23:08 tot 23:50, Bram (run 2)
- Berichten gelezen, niets nieuws. Taak 1 (wat bouwen we) doorgezet met de twee routes uit run 1.
- Twee onderzoekers tegelijk: ronde 8 (wint een nieuwkomer met een mooier product in een volle markt?) en ronde 9 (loont vroeg zijn op een nieuwe Blender-functie?). Uitkomst in `kandidaten-2026-11-07.md` sectie 11 en 12.
- Controleur: cijfers kloppen, maar het bewijs voor de physics-kit (Hurricane) was verkeerd gelezen en Blender levert de presets zelf. Besluit: physics-kit valt af. Scores: UV-naadtool 21, node-previews 18, physics-kit 16.
- Doorlichting UV-naadtool: UV Flow en Easeam 2 doen het al, goedkoper of met dezelfde klikflow. Besluit: valt af, want we zouden niet goedkoper en niet aantoonbaar beter zijn, en sectie 11 liet zien dat precies die combinatie nodig is.
- Regel 5 (twee runs op rij geen resultaat): het bouwbesluit lukt nu twee runs niet. Gemeld op `organisatie/lijst-thijs.md` (ter info, hij hoeft niets te doen) en de volgende taak opgepakt: de test in de echte Blender, die los staat van welk product we kiezen.
- 23:30 tot 23:42: taak 2 (test in de echte Blender) opgepakt. Proef-add-on en workflow gebouwd op tak `claude/blender-2026-11-07`. Drie runs: alle drie groen in Blender 4.2.23 en 5.2.3 (laatste: 42425981418). Eerste schermafbeelding was zwart (Blender leest onder Xvfb met software-OpenGL niets uit); opgelost door het hele X-scherm te pakken met ImageMagick. Besluit: proef apart van het product houden, zodat het eerste product deze opbouw kan overnemen zonder het bouwbesluit af te wachten. Wat misging: het Quick Setup-venster staat nog in beeld, starten met een .blend hielp niet. Niet samengevoegd met main, want nog niet nagekeken door een controleur.

## 8 nov 2026, 00:08 tot ±00:50, Bram (run 3)
- Berichten gelezen, niets nieuws. Lokale kloon liep uiteen met GitHub; gewerkt op een verse tak vanaf origin/main (de oude lokale main niet weggegooid).
- Besluit: eerst taak 2 (test in de echte Blender) afmaken, want het bouwbesluit lukte twee runs niet (regel 5) en de test is nodig voor elk product.
- Quick Setup opgelost door vooraf voorkeuren op te slaan in een eigen map (`BLENDER_USER_RESOURCES`) en zonder `--factory-startup` te starten. Tabblad Dortus actief gemaakt met xdotool Ctrl+muiswiel; `active_panel_category` is wel leesbaar, dus de test kijkt na elke stap of het gelukt is. Run 42428535356 groen in beide versies, plaatjes zelf bekeken: paneel open, geen Quick Setup.
- Controleur: akkoord met kleine punten (nutteloze operatorcheck, schermen-stap liet fouten stil passeren, uitsluitpatroon pycache, zip niet gevalideerd). Alles verwerkt, run 42428813910 groen, samengevoegd met main. pycache-bestanden uit de repo gehaald.
- Taak 3: accounts Superhive en extensions.blender.org klaargezet op lijst-thijs, als niet dringend, want er is nog geen product.
- 00:20 tot 00:25: taak 1 weer opgepakt. Onderzoeker lichtte node-previews door; de gratis extensie zelf nagelezen. Besluit: valt af, want gratis plus goedkoop betaald dekt het al en de vraag is klein (sectie 14). Geen bouwproef meer nodig. Volgende run: wrap-richting.
