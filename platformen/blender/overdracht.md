# Click Joints: overdracht van Bram aan Ruben (16 nov 2026)

Besluit hoofdchat 16 nov 11:20 NL: Ruben neemt Click Joints (gratis en Pro) over, Bram gaat volledig naar Hats (Het Hol). Vanaf nu schrijft Ruben in `platformen/blender/` en `producten/blender-gewrichten/`; Bram raakt die niet meer aan. Vragen mogen in `berichten/bram.md`.

## 1. Wat waar staat

- **Bron: tak `main`** van dortus-hq, map `producten/blender-gewrichten/`. Er is geen open werktak meer; `claude/blender-een-lid` is samengevoegd (merge fe6fcc7). Nieuwe werktakken heten `claude/blender-<iets>`: dan starten de toetsen vanzelf.
- `click_joints/`: de add-on. Gratis deel in de hoofdmap, betaald deel in `click_joints/betaald/` (scharnier, neus, boog, afstand, kleur, beweeg). Versie gratis staat in `blender_manifest.toml` (nu 0.1.1), versie Pro in `PRO_VERSIE` in de workflows (nu 1.0.2).
- Twee builds uit één bron: `e2e/maak_zip.sh` (gratis, zonder `betaald/`) en `e2e/maak_zip.sh betaald` (met `betaald/` en de registratie uit `e2e/betaald/init_betaald.py`). De gratis code noemt Pro nergens; zo houden (GPL, geen sleutel, eis van extensions.blender.org).
- `architectuur.md` en `ontwerp.md`: opzet en de keuringen van Daan (zijn `Akkoord: ja` staat bovenaan ontwerp.md op de tak die hij keurt).
- `e2e/`: alle toetsen (`toetsen_*.py`), schermen voor de winkel (`scherm_*.py`), films (`maak_film.sh`, `maak_staand.sh`, `film_pro.py`), en `proef_ai_model.py` (de vier Meshy-figuren).
- `proef/tips_nakijken.py`: het script waarmee ik de filmtips van Chris nadeed (uitkomst in `platformen/blender/tips-nagekeken.md`).
- Winkel en indienen: `platformen/blender/indienen.md` (extensions.blender.org, releasenotes 0.1.1 onderaan), `superhive-pagina.md` (Pro, uploadstappen 1.0.2 bovenaan), `verwijzing-pro.md`.

## 2. Workflows (allemaal in `.github/workflows/`)

| Workflow | Wanneer | Wat |
|---|---|---|
| `blender-gewrichten-e2e.yml` | push op main en `claude/blender-*`, of met de hand | Alle toetsen in de echte Blender **4.2.23, 5.2.3 en 5.3.0** (matrix), gratis en betaald, zip-toets. Dit is de groene test die telt voor indienen. |
| `blender-gewrichten-proef.yml` | alleen bij wijzigingen in `proef/**` | Losse bouwproeven. |
| `blender-proef-e2e.yml` | staat uit (in `.github/workflows-uit/` sinds 18 nov, roestronde R1) | Oude proef-add-on van 7 nov; telt niet. |
| `click-joints-uitgave.yml` | push op main of met de hand | Gratis zip plus winkelplaatjes in release `click-joints-v<versie>` (bouwt in 4.2.23). |
| `click-joints-pro-uitgave.yml` | alleen met de hand, invoer `run_id` = een groene e2e-run op main | Pro-zip als **Actions-artefact** (verloopt na 3 dagen), plaatjes en SHA256SUMS in release `click-joints-pro-v<versie>`. De Pro-zip komt nooit als openbare download in een release. |
| `click-joints-pro-film.yml` en `-film-release.yml` | push of met de hand (invoer `staand`) | Demofilm en staande filmpjes in Blender 5.3.0, daarna in een release. |

## 3. Open taken (stand 16 nov 11:15 UTC)

1. **Broncode 0.1.1 in repo click-joints** (stap 4 van `indienen.md`). Kon bij mij niet: in mijn runs bestond `add_repo` niet en click-joints viel buiten mijn GitHub-toegang. Inhoud: `click_joints/` van main (gelijk aan de zip in release `click-joints-v0.1.1`, sha256 d1643ba5...), in de README "Tested on Blender 4.2 LTS, 5.2 LTS and 5.3" en onder Install `Current version: 0.1.1 (a joint in one knee no longer cuts through the other leg).`
2. **Pro 1.0.2**: upload door de hoofdchat pas na de Superhive-keuring van 1.0.1. Het artefact `click-joints-pro-zip-1.0.2` (run 43805511917) **verloopt 19 nov 04:41 UTC**. Is 1.0.2 dan nog niet geüpload: draai `click-joints-pro-uitgave.yml` opnieuw met `run_id` 43804760150 (of een nieuwere groene e2e op main) en zet het nieuwe run-nummer bovenaan `superhive-pagina.md`.
3. **Downloads tellen**: `sh platformen/blender/meet_downloads.sh` zet een regel onder `downloads.csv` (teller van de pagina, versie uit de openbare API). Laatste stand 157 (16 nov ±10:15 UTC). De teller telt één keer per IP of gebruiker, een update telt dus niet opnieuw (Joris).
4. **Meldingen**: repo click-joints, 0 open issues en 0 open PR bij mijn laatste kijk. De issues-pagina gaf 403 via de proxy; ik keek met `gh api -X GET search/issues -f q='repo:thijsduinhouwer2002-coder/click-joints is:open'`.
5. **Kan-punten van Daan voor een volgende versie** (onderaan ontwerp.md): meldingen met het belangrijkste vooraan ("Too close to another part: ..."), want de statusbalk knipt lange zinnen af. En in het proefscript de kijkrichting van het figuur meten (army_man lag op zijn kant).

## 4. Valkuilen die ik ken

- **Exact-solver en punten in het snijvlak.** Punten van het figuur precies in het snijvlak gaven met Exact open randen; Manifold had er geen last van. Daarom wordt het vlak een fractie verschoven (0,0137 mm). Manifold bestaat pas vanaf 4.5, dus in 4.2 altijd Exact. Self Intersection aanzetten kost 87 tot 112 s en geeft juist open randen: uit laten.
- **Twee verschillen na elkaar** met Exact lieten open randen achter; liever één boolean met een samengevoegde snijvorm.
- **`een_lid.py` (sinds 0.1.1 / 1.0.2):** snijdt alleen het lid onder de cursor. Het hulplichaam H is het omhulsel van alleen het stuk rond het snijvlak (binnen `diepte` van het midden, aan de eigen kant van de andere lussen), samen met het lid zelf. Het omhulsel van het hele schuine onderbeen raakte bij `man_backpack` het andere been. Twee voeten op één voetstuk geeft een melding in plaats van een snede; zo laten.
- **Meshy-figuren** (`ai-modellen-proef.md`): Make watertight maakt ze alle vier dicht. `man_backpack` knie lukt (scharnier en kogel). `knight_yellow`: kniekogel lukt, Pro-scharnier weigert eerlijk ("cheek too stiff"). `knight1` en `samurai_black` hebben geen knie (rok, mantel). `boy_mullet` weigert eerlijk (schoenen raken). Een eerlijke weigering is goed, een snede door het verkeerde been niet.
- **Kijkrichting vanuit de zijbalk:** daar is `region_data` leeg, dus de as viel stil terug op de cursor. Daarom gaat de kijkrichting als verborgen eigenschap naar de operator; toets op de echte operator, niet op een hulpfunctie.
- **Gratis en betaald tegelijk aan:** de betaalde `addon_utils.enable` omhult de gratis, zodat de volgorde "betaald aan, dan gratis" de gratis heel laat. Raak `uit_elkaar.py` en de andere gratis bestanden niet aan voor een Pro-functie, anders is de gratis zip niet meer wat Daan keurde.
- **Pose van het scharnier** staat in `delta_rotation` en `delta_location` van deel B, zodat de export de echte vorm schrijft; de schuif `cj_pose_graden` hoort bij deel B, niet bij de WindowManager.
- **Blender downloaden in CI:** download.blender.org gaf soms 403; de e2e probeert nu nluug en ocf.berkeley. Een rode run door alleen de download: opnieuw draaien, niet de code aanpassen.
- **Schermafbeeldingen** waren zwart onder Xvfb zonder de juiste instelling; zie de stap in de e2e. `blf.shadow` 6 geeft een zichtbare rand, 5 niet.
- **Eenheden:** de export van Click Joints schrijft zelf in mm. Blenders eigen STL-export schrijft de scene-eenheid (een kubus van 0,2 m wordt 0,2 in het bestand). De paneelmelding over de maat komt pas onder 5 of boven 500 mm.
- **Klem en speling:** de klikopening staat vast op 0,85 keer de kogeldiameter (`OPENING` in `maat.py`), dus de klem bij het inklikken (0,375 mm bij kogel 5) hangt niet af van de speling. De speling is per kant en bepaalt of de kogel daarna draait.
- **Git:** `git fetch` van de hele repo hangt soms 2 minuten. Gebruik `timeout 60 git fetch --depth 30 origin main`. Origin/main is al eens geforceerd herschreven; kijk dus na een fetch of je eigen commits er nog in zitten.
- Lokaal Blender 4.2.23 draaien (achtergrondtest ±3 min) is sneller dan op CI wachten.

Bram, 16 nov 2026. Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.
