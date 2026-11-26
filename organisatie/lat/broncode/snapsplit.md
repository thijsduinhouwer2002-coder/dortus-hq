# Broncode: SnapSplit (Blender-add-on, directe concurrent van Click Cuts)

Uitgeplozen door de Afkijker, do 26 nov 2026 ±18:30 NL (issue #20). Code gelezen met `git clone --depth 1` in /tmp, niets uitgevoerd, daarna weggegooid.

## Wie en hoeveel
- Repo: https://github.com/Betakontext/snapsplit, laatste commit 19 nov 2026 ("V_0.2.1_multiple_cuts"), versie 0.2.1 (GEZIEN `snapsplit/blender_manifest.toml`). Eén maker (Christoph Medicus, Betakontext).
- Licentie: GPL-3.0-or-later (GEZIEN `snapsplit/LICENCE.txt` en manifest). Dus: alleen ideeën overnemen, geen code.
- Omvang: ±16.200 regels Python in 13 bestanden, waarvan 3.069 regels vertalingen (GEZIEN `wc -l`).
- **Zelfde add-on gratis én betaald:** gratis op extensions.blender.org, 2.037 downloads sinds 21 sep 2026, 0 reviews (GEZIEN, https://extensions.blender.org/add-ons/snapsplit/); $20 op Superhive, "Sales 30+" in 8 maanden, 12 maanden support (GEZIEN, https://superhivemarket.com/products/snapsplit). Wie betaalt, koopt dus alleen steun en support.
- Issues op GitHub kon ik deze run niet lezen: de GitHub-API en de issuepagina geven in deze geplande run "access not enabled" (de repo staat niet in de toegang van deze taak). Reviews op extensions.blender.org: 0.

## Wat ze slim doen (bestand en regels)
1. **Startspeling per materiaal.** `profiles.py` r. 40 tot 47: PLA 0,20, PETG 0,30, ABS 0,25, ASA 0,25, TPU 0,35, SLA (hars) 0,10 mm per kant. Kies je PETG, dan krijg je meteen 0,30; een eigen getal (`tol_override`, r. 514 tot 525) gaat er alleen overheen als het groter dan 0 is.
2. **19 talen via Blenders eigen vertaling.** `localization.py` (Duits, Frans, Spaans, Italiaans, Portugees, Nederlands, Pools, Japans, Chinees, Russisch, Oekraïens, Turks, Sloveens, Koreaans, Swahili, Arabisch, Perzisch, Hindi, Bengaals), geregistreerd in `__init__.py` r. 87 tot 107 met alleen de talen die Blender kent (`bpy.app.translations.locales`). Het paneel volgt vanzelf de taal van Blender.
3. **Vrije snede met een getekende streep en kleuren in de preview.** `ops_freehand.py` r. 57 tot 59: oranje is wat gesneden wordt, grijs niet, rood (`INVALID_COLOR`) een doorsnede die open of vertakt is en dus niet dicht kan. Shift bij loslaten zet de snede recht op een as; Enter voert uit, Esc stopt; het origineel blijft onaangeroerd en verborgen (README, "Freehand Cut workflow"). Zelfde les als Bool Tool, nu bij een directe concurrent.
4. **Live preview met een plafond.** `ops_connectors.py` r. 131: hooguit 200 preview-verbinders, zodat het paneel niet vastloopt op een groot raster.
5. **Eerlijke grenzen in de handleiding.** De README zegt per functie wat het niet doet ("It does not create an arbitrary curved cutting path", "is not a printability or fit guarantee", voorkeuren "integration is incomplete"). Goed voor vertrouwen, slecht voor verkoop: de Superhive-pagina is daardoor droge uitleg (lat, Etalage).

## Wat kopers vragen of klagen
Geen reviews op beide winkels, issues niet leesbaar deze run (zie boven). Wel zichtbaar: 2.037 gratis downloads tegen 30+ verkopen, dus vrijwel niemand betaalt als dezelfde add-on gratis staat (GEZIEN, beide pagina's).

## Welk product van ons wordt er beter van
**Click Cuts, `split_joints/eigenschappen.py` r. 31 tot 33 en 62 tot 65, `split_joints/passing.py` r. 27 tot 31.**
Bij ons staat de speling standaard op 0,20 mm voor elk materiaal. Materiaal kiezen verandert alleen iets als je voor die printer en dat materiaal al een passingproef bewaarde (`passingproef.py` r. 82 tot 88). En de passingproef zelf test vier waarden rond de huidige speling in stappen van 0,05: rond 0,20 is dat 0,15 / 0,20 / 0,25 / 0,30 (GEZIEN, `spelingen()`).
Gevolg (GOK, uit de getallen): een koper met een harsprinter print een proefblok zonder de waarde die bij hars hoort (±0,10 volgens SnapSplit); met TPU (±0,35) zit de passende waarde er ook niet in. De eerste proef mislukt dan net bij de kopers met een harsprinter, die veel figuren printen.
Idee voor 1.0.1 (na de lancering, niet nu: de zip ligt vast en Superhive keurt al): geef elk materiaal een eigen startspeling zolang er niets bewaard is (bijvoorbeeld PLA 0,20, PETG 0,25 tot 0,30, ABS/ASA 0,25, TPU 0,35, Resin 0,10; Other 0,20), en laat de passingproef rond die startwaarde testen. Getallen eerst naast een tweede bron leggen; SnapSplit is één bron.

Tweede, groter maar later: vertalingen. SnapSplit doet 19 talen in één bestand; Click Cuts en Click Joints Pro zijn alleen Engels. Zinvol pas als er verkopen zijn om te zien uit welke landen ze komen (Meter).
