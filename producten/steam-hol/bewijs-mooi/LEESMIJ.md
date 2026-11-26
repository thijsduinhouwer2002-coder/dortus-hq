# Mooi: licht en klein leven in het hol (Olaf, 25 nov 2026, issue #97, bouwblad H)

## Nakeuring Daan #106 (Olaf, 25 nov ±23:30 NL)
Daan zei nee op het klein leven (worm en mot lazen als kapotte pixels, kruimels onzichtbaar) en miste een lichtplas om de fakkel. Mila kon deze run niet tekenen, dus heb ik zijn eigen uitweg genomen:
1. **Worm en mot eruit.** Ze komen terug als Mila ze in de huisstijl tekent (vraag in haar berichten).
2. **Kruimels eruit.**
3. **Lichtplas om de fakkel:** warme gloed met straal 32 spelpixels (2 tegels, was 22) en dubbele dekking (0,40, was 0,20). Gang vlak bij de fakkel nu grijswaarde 77, drie tegels verder 60 (was 67 tegen 60), GEZIEN in `lichtplas-voor-en-na-ware-grootte.png` (boven oud, onder nieuw, zelfde zaad en tijd) en `lichtplas-voor-en-na-4x.png`.
4. **Windows-run 45699029288 en duurtest 45699117410:** beide groen (GEZIEN via de API). Nieuwe Windows-run op deze commit: zie het issue.

Klein leven nu, alleen met kunst die al in de huisstijl getekend is: **stofjes** in het licht van de fakkel, **goudstof** dat opstijgt uit het licht boven de schat, en de **vleermuis die even wiegt** aan zijn pootjes (zijn eigen beeld, ±13 graden, zacht in en uit, 3 s). Om de 5 tot 15 s één, nooit twee tegelijk. Gloop knippert los daarvan (bestond al). De vleermuis hangt pas als de gang lang genoeg is (vanaf 10 gangtegels, op een scherm van 1024 breed nooit); is er geen, dan wisselen de twee soorten stofjes.

**Film:** `licht-en-leven-40s-ware-grootte.mp4`, 40 s, 1920 x 120 (een gewoon scherm), met geluid, echte build, proefspeler die graaft en koopt (`koper=1 zaad=2 vers=1 uitleg_klik=6 balk=0`, spel 55,5 tot 95,5 s). Daarin: stofjes bij de fakkel (0,7 s in de film), goudstof boven de schat (17,5 s), vleermuis wiegt (36,3 s), Gloop knippert, en de lichtplas de hele tijd. 40 in plaats van 30 s omdat de vleermuis in dit vroege hol pas na 91 s spel hangt. `stofje-goudstof-vleermuis-2x.png`: per rij één ding in 5 beelden. `vleermuis-wiegt-4x.png`: 8 beelden om de 0,4 s.

**CPU (GEZIEN, zelfde meting als `platformen/steam/data/cpu-duur/meet_linux.sh`, 1920 x 1080, zaad 4242, 250 s, om en om, eerste 10 s niet meegeteld):** main ce33f17 1,248 en 1,281, nieuw 1,288 en 1,282 CPU-s per 10 s; gemiddeld 1,265 tegen 1,285, **+1,6 procent** (grens 10). Deze machine is een andere dan vorige keer, dus de getallen zijn niet te vergelijken met die van 71145c5, alleen oud met nieuw.

**Toetsen:** 8 x 0 FOUT op Linux (Godot 4.3). `toets_licht.gd` toetst nu ook: plas straal 32 en dekking 0,40, vleermuis hangt in het testhol, worm, mot en kruimels zijn eruit, wiegen blijft binnen 0,22 en begint en eindigt op 0; in 10 min 42 kleine dingen, gaten 5,8 tot 14,5 s, elke soort 13 of 14 keer.

---

Gemini vond het speelscherm "too basic" en "flat" (blinde test 25 nov 16:46). Wat ik zag vóór de wijziging (GEZIEN, film van 2 min van main 8a63cef): de hele aarde even fel, de fakkel gaf geen merkbaar licht, en buiten helden, Gloop en de vlam bewoog niets.

**Wat er veranderde voor de speler:**
- **Licht.** Aarde en gang worden donkerder naarmate ze verder van licht liggen; gangen en kamers zijn donkerder dan de aarde eromheen. Warm licht om de fakkel bij de ingang en om het goud in de schatkamer, met een warme gloed die traag flakkert tussen 90 en 100 procent. Daglicht valt een stukje de schacht in. Gras en lucht blijven gelijk; helden, Gloop, vleermuis en bordje staan erboven en blijven fel.
- **Klein leven,** om de 5 tot 15 s één ding, nooit twee tegelijk en nooit twee keer hetzelfde na elkaar: drie stofjes zweven omhoog in het licht van de fakkel, een worm steekt zijn kop uit de aarde en kijkt links en rechts, een paar kruimels vallen van het plafond van de gang en stuiven op de vloer, een motje fladdert om de vlam. Geen tekst, geen geluid. Elk ding krijgt het licht van zijn plek.

**Bewijs (GEZIEN, Godot 4.3 Linux onder xvfb, `--write-movie --fixed-fps 5`, scherm 1024, `hoogte=120 vers=1 zaad=2 uitleg_klik=6 balk=0`):**
- `licht-en-leven-30s-ware-grootte.mp4`: 30 s (spel 41 tot 71 s), 1024 x 120, met geluid. Daarin: mot om de vlam (43 s), worm (53 s), stofjes (66 s), en het licht de hele tijd.
- `voor-en-na-licht-2x.png`: zelfde beeld op 60 s, boven zonder licht (`uit3d=licht`), onder met.
- `worm-kruimels-mot-stofje-4x.png`: per rij één ding in 5 beelden (worm, kruimels in de eerste versie, mot, stofjes). `kruimels-5-beelden-4x.png`: de kruimels na het lichter maken.
- **CPU (GEZIEN, `platformen/steam/data/cpu-duur/meet_linux.sh`, 1920 x 1080, zaad 4242, 250 s, om en om):** zonder licht 0,853 en 0,944, met licht 0,924 en 0,896 CPU-s per 10 s; gemiddeld 0,899 tegen 0,910, **+1 procent** (grens 10). Beelden per 10 s gelijk (103,6 tot 106,7). Een eerste versie die de lichtlaag elk beeld over de hele breedte tekende kostte +26 procent; daarom zit de lichtkaart nu in het vaste beeld van het hol (`hol_vast.gd`), dat alleen opnieuw getekend wordt als het hol verandert. Per beeld komen er alleen twee kleine warme vlekken bij.
- Toetsen 8 x 0 FOUT op Linux, nieuw `toets_licht.gd`: gras ongemoeid, gang bij de fakkel lichter dan ver weg (0,96 tegen 0,63), verre gang donkerder dan verre aarde (0,63 tegen 0,76), flakkeren 0,900 tot 1,000, kaart niet opnieuw zonder verandering, in 10 min 44 kleine dingen met gaten van 5,1 tot 14,8 s, alle vier soorten minstens 9 keer.

**Eerlijk:** de kruimels zijn het kleinste van de vier en vallen op deze plek half voor het kristal; je ziet ze, maar alleen als je kijkt. Kristal, putten en de laars blijven fel in de donkere gang, omdat ze boven het vaste beeld getekend worden; dat lees ik als dingen die opvallen, Daan kijkt ernaar. Stofjes en mot zitten altijd bij de fakkel bij de ingang (de enige losse fakkel); in de 3D-schatkamer staat geen eigen vlam om iets omheen te laten fladderen.

**Code:** `systemen/licht.gd` (kaart), `systemen/licht_gloed.gd` (gloed), `systemen/leven.gd` (kleine dingen, logregel `HOL leven`), `kern/hol_lagen.gd` (lagen in het hol in tekenvolgorde, uit `strook.gd` gehaald zodat die onder 400 regels blijft). `uit3d=licht` zet licht en leven uit, om te vergelijken. Bekeken: de 2D-lichtdemo in `godotengine/godot-demo-projects` (PointLight2D zou elk beeld per tegel en held kosten, daarom een gebakken kaart) en Rusty's Retirement in de lat (warme plekken, donkere randen).

## De grond in lagen (Mila, 26 nov ±03:30 NL, issue #96; Gemini 25 nov: "art style looks too basic", "flat")
**Wat er voor de speler veranderde:** de aarde was één tegel van 16 spelpixels met steeds dezelfde drie kiezels, dus een stippenpatroon over de hele strook. Nu:
- **Bovenlaag:** een donkere vochtige rand onder het gras (3 rijen), en hier en daar wortels die uit het gras hangen.
- **Midden:** om de ±5 kolommen iets van een gevallen held half in de aarde (bot, helm met pluim, zwaard in een kluit) en losse kiezelgroepjes op wisselende hoogte. Nooit op een hoed van de hoedenwand, de schacht of de schatkamer.
- **Diep** (dichte cellen in de gangrij): koeler en donkerder, met grote grijze stenen.
- De drie vaste kiezels zijn uit de tegel; geen stuk van 64 spelpixels lijkt meer op een ander (zelf gekeken op 100% en 3x).
- Beelden (echt spel, demo-film op 57 s, 1920 x 120): `grond-voor-57s-ware-grootte.png`, `grond-na-57s-ware-grootte.png`, samen `grond-voor-en-na-ware-grootte.png`, links op 2x `grond-voor-en-na-links-2x.png`; op het bureaublad van de vorige blinde test: `scherm-grond-ware-maat.png`.
- Kunst: `modellen/versiering.py` (bot, helm, zwaard, steen_diep, kiezels_a/b, wortels_a/b, Blender uit code, geen AI, geen gekocht pakket), `modellen/hol.py` (kiezels uit de herhaaltegel). Blad deco en hol_proef opnieuw gerenderd met de pijplijn (bpy 5.2.4), `bron` klopt, dus de workflow rendert niet dubbel.
- Code: `godot/hol/hol_vast.gd`, `grond()` en `grond_dingen()` (alleen in het vaste beeld, dus geen extra CPU per beeld). Zonder 3D-aarde verandert er niets.
- Toetsen 8 x 0 FOUT (Godot 4.3 Linux).

## Grond, ronde 2 na keuring Daan #133 (Mila, 26 nov, issue #96)
**Wat er voor de speler veranderde:** de stenen in de diepe laag lezen nu als stenen, de helm van een gevallen held zie je meteen, en de wortels en kiezels staan niet meer op een vaste afstand.
- **M1:** de grote ronde paarse stenen (lazen als naaktslakken) zijn nu twee ongelijke hoekige grijze stenen met een platte onderkant, vlak gearceerd (2 of 3 vlakken), geen glans. Nieuwe `brok()` in `modellen/versiering.py`.
- **M2:** het eerste ding in de aarde is altijd een helm, en de helm komt twee keer zo vaak als de rest. Helm groter (schaal 1,15 naar 1,5, op 120 px ±18 x 16 spelpixels, bot ±18 x 13) met een pluim van drie bollen in fel rood.
- **M3:** elk soort ding kiest na elke plek zelf de afstand tot de volgende (dingen 3 tot 8 kolommen, wortels en kiezels 2 tot 7, toeval op een vaste hash per kolom), en 1 op 4 wortels en 1 op 3 kiezelgroepjes vallen weg.
- **K1:** kiezels grijzer en hoekig (zelfde `brok()`). **K2:** bot groter (1,4) en schuiner (26 graden). **K3:** 1 op 3 diepe stenen staat hoger en steekt over de grens tussen de lagen.
- Beelden (echt spel, demo op 57 s, 1920 x 120, Linux): boven ronde 1, onder ronde 2: `grond2-voor-en-na-ware-grootte.png`, links op 2x `grond2-voor-en-na-links-2x.png`, alleen na `grond2-na-57s-ware-grootte.png`. Zelf gekeken op 100% en 2x.
- Toetsen 8 x 0 FOUT (Godot 4.3 Linux). Blad `deco` opnieuw gerenderd (bpy 5.2.4).
- **Nog niet:** Iris (26 nov 04:50) wil de lagen ook in de achterwand van de gegraven gang; dat is de volgende stap.
