# Keuring direct-zip met Pro-knoppen op slot, 21 nov 2026, Daan
Wat ik keurde: repo dortus-hq tak `claude/blender-direct-zip` (45fadb8, code c368201): `e2e/direct/direct.py`, `e2e/direct/init_direct.py`, `maak_zip.sh direct`, `toets_direct_zip.py`, workflowstap "Direct-zip", architectuur. De zip zelf uit run 44950200065 (artefact `click-joints-direct-zip-5.3.0`, sha256 d8041d85...), uitgepakt en vergeleken. Schermen `d1-slot-paneel.png` en `d2-venster.png` (5.2.3) met eigen ogen. Repo dortus tak `claude/direct-zip-download` (66d6031, één commit boven main): knop en zin in `click-joints/index.html` en `click-joints/click-joints-free.zip`. Regels 6.1 tot 6.3 in `platformen/blender/verwijzing-pro.md` opnieuw gelezen.
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De extensions-zip blijft gelijk: direct.py komt alleen via `maak_zip.sh direct` erbij, de gewone tak van het script is niet aangeraakt. Toets plus grep in de workflow vangen elke "pro" in de extensions-zip. | feit | hoog | diff, toets_direct_zip.py |
| 2 | Zip van de site heeft precies dezelfde inhoud als het artefact 5.3.0 (`diff -r` leeg; alleen de zip-tijden verschillen). Manifest: id click_joints, versie 0.1.1, geen extra rechten nodig (wm.url_open is een klik van de gebruiker). | feit | hoog | uitgepakt |
| 3 | De drie slotknoppen bestaan echt in Pro 1.1.0: "Figure from rig" (rig.py bl_label), scharnier met eindstop (scharnier_boog.py), zes lichaamsdeel-presets (figuur.py). Niets beloofd wat Pro niet doet. | feit | hoog | code betaald/ |
| 4 | Scherm d1: vak met drie slotknoppen onder stap 3, "Upgrade to Pro" eronder, "Report a problem" onderaan. Rustig, gratis stappen blijven bovenaan en volledig. d2: venster "Figure from rig / This is in Click Joints Pro / See Click Joints Pro" leesbaar. Venster staat ver rechts door de test, Bram zegt het al. | feit | hoog | beeld |
| 5 | Uit en weer aan: precies één tekenfunctie (test_direct), unregister haalt eerst het slot-deel weg. Run 44950178146 groen in 4.2.23, 5.2.3, 5.3.0 (Bram, GEZIEN API door hem). | feit op zijn melding | midden | run |
| 6 | Site: knop "Download the zip" naast "Get it on Blender Extensions", installatiezin klopt (Get Extensions, pijltje rechtsboven, Install from Disk bestaat zo in 4.2 en nieuwer). | feit | hoog | diff |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Regel 6.1 tot 6.3: ik lees het als Bram. 6.1 gaat over wat "inside the Blender UI" zit van een extensie op het platform, 6.2 letterlijk over "the version that is available on the platform", 6.3 over "Extension must not". De direct-zip gaat nooit naar het platform, de versie daar noemt Pro nergens. GPL laat een eigen verdeling met eigen knoppen toe. Dus: mag, zolang de direct-zip nooit wordt geüpload (toets bewaakt de extensions-zip). | vermoeden, goed onderbouwd | midden | 6.1 tot 6.3, GPL |
| 2 | Restrisico: een moderator volgt de Website-link van de listing en ziet een zip met upgradeknoppen. Geen regel verbiedt dat; de pagina toont het Pro-blok al sinds besluit regel 21. Klein. | vermoeden | midden | verwijzing-pro.md regel 21 |
| 3 | Geen prijs in Blender, geen persoonsgegevens, Engels in het product, geen "click" als belofte in de nieuwe teksten. | feit | hoog | harde regels |

## Deel C: zou een koper het fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | Beide links gaan naar `https://dortus.com/click-joints/`, de bovenkant van de pagina waar de gebruiker de zip net haalde. Hij moet zelf naar Pro scrollen, en in de cijfers zie je niet dat iemand uit Blender kwam. | URL `https://dortus.com/click-joints/?from=addon#pro`: landt meteen op het Pro-blok en telt mee in de bezoekcijfers (amami). Wel zip opnieuw bouwen. | klein |
| 2 | Wie hem al van Blender Extensions heeft en ook de zip installeert, krijgt dezelfde id twee keer. Blender laat dan één van de twee werken. | Op de site bij Install één zin: "Already installed from Blender Extensions? Remove that one first." | klein |
| 3 | De knop "Download the zip" zegt niet dat deze versie de Pro-knoppen laat zien. Geen bedrog (het is zichtbaar), maar eerlijker. | Onder de knop of in de Install-zin: "The zip also shows what Pro adds." | klein |
| 4 | Wie de zip gebruikt, krijgt geen updates uit Blender. | Bij een nieuwe gratis versie ook de direct-zip opnieuw bouwen en op de site zetten (in de uitbrengstappen). | klein |

## Moet (blokkeert akkoord) / Kan (mag later)
Moet: geen. Tak `claude/blender-direct-zip` (45fadb8) mag naar main; site-tak `claude/direct-zip-download` (66d6031) mag naar main.
Kan 1 (doe dit eerst, meetbaar geld): URL in direct.py naar `https://dortus.com/click-joints/?from=addon#pro`, zip opnieuw.
Kan 2 en 3: één zin op de site (al eerder geïnstalleerd; de zip laat Pro zien).
Kan 4: direct-zip in de uitbrengstappen opnemen.
