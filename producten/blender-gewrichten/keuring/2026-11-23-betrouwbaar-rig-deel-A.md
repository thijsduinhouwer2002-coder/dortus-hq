# Keuring betrouwbaar-rig (Figure from rig), 23 nov 2026, keurder deel A
Wat ik keurde: tak `claude/betrouwbaar-rig` op eaa1252 (add-on op 6dc00b2), `proeven/betrouwbaar-rig-2026-11-23/uitslag.md`,
het bericht van Betrouwbaarheid (23 nov ±22:55) in `berichten/hoofdchat.md` op die tak, de JSON-uitslagen op de tak
`betrouwbaar-uitslag` (tabel opnieuw gemaakt met `e2e/meet_tabel.py`) en de runs via `organisatie/controle/actions.py`
en de openbare jobs-lijst van GitHub (stand 23 nov 21:42 UTC).
Akkoord: nee

Kort: voor Blender 5.2 en 5.3 klopt de belofte en is hij sterk bewezen (60 van 60 in vier runs achter elkaar, nul
slechte sneden). Het cijfer voor 4.2 (55 van 60) klopt niet meer voor de testset zoals hij nu op de tak staat: het is
gemeten op de oude robot, voor main erin werd gevoegd. Op de nieuwe robot geeft dezelfde 4.2-code veel minder, of de job
stopt zonder uitslag. Dat staat niet in de uitslag.

## Deel A: doet het wat beloofd is?
Belofte: Figure from rig slaat geen haalbaar gewricht meer over op de vaste testset (60 per versie).

| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| A1 | Nulmeting 35 / 59 / 59 van 60 (run 45253697551, commit 196691e) komt cel voor cel overeen met de JSON. | Feit | hoog | Tabel uit `betrouwbaar-uitslag/45253697551`. |
| A2 | 5.2.3 en 5.3.0 eindmeting 60 van 60 met 0 slechte sneden (run 45267268513, commit 6dc00b2) klopt cel voor cel, ook de tijden. Alle meet-jobs voor 5.x groen. | Feit | hoog | Tabel uit `betrouwbaar-uitslag/45267268513`. |
| A3 | 5.x is niet één gelukstreffer: ook runs 45264302449 (7ea796e), 45266165562 (f804f10) en 45266243590 (78ac6d9) geven 60 van 60 in 5.2 en 5.3 met 0 slechte sneden, en eaa1252 (run 45272145878, nog bezig) geeft tot nu toe dezelfde cellen. | Feit | hoog | Tabellen van die vier runs. |
| A4 | **De kolom 4.2 (55 van 60) hoort bij een andere robot dan de rest van de eindmeting.** De samenvoeging met main (d17205c) bracht de robot van studio-3 mee (`figuur_robot.py` en `robot-dortus.glb` gewijzigd). In de JSON: robot-a 240112 punten in 45253697551 en 45264302449, 273112 punten in 45266165562 en later. De nulmeting en de 4.2-kolom gaan over de oude robot, de 5.x-kolom over de nieuwe. | Feit | hoog | `bron_punten` in `<run>/4.2.23/robot-a.json` en `<run>/5.3.0/robot-a.json`. |
| A5 | **Op de nieuwe robot geeft 4.2 veel minder.** Run 45266165562 op f804f10 (add-on precies gelijk aan 7ea796e, alleen drempel, architectuur en uitslag gewijzigd): robot-a 2 (was 7), robot-b 2 (was 7), robot-fijn 7 (was 9), met 15, 15 en 2 slechte sneden en 1074 en 1200 s per robot; rigify geen uitslag. Overgeslagen o.a. beide knieën, nek en schouder met "no watertight parts". Deze run staat niet in uitslag.md of het bericht. Samen in 4.2 dan ongeveer 2+2+7+8+9+8 = 36 van 53 zonder rigify, met rigify 7 erbij ongeveer 43 van 60 (GOK voor rigify). | Feit (cijfers), GOK (totaal met rigify) | hoog | Tabel uit `betrouwbaar-uitslag/45266165562`; een nieuwe 4.2-meting op 6dc00b2 die wel afloopt. |
| A6 | **Op de eindcode komt er in 4.2 voor de robots en rigify geen uitslag.** In 45266243590 (78ac6d9) en 45267268513 (6dc00b2) faalt de stap "Figure from rig" voor robot-a, robot-b en robot-fijn in 4.2, telkens na 2 tot 4 minuten (jobs 21:08 tot 21:13 en 21:20 tot 21:27 UTC); rigify in 4.2 liep om 21:42 nog (meer dan 20 minuten, eerder 291 s). De uitslag noemt dit "door GitHub afgebroken (exit 143, SIGTERM van de runner)", maar het is 6 van 6 keer en ver onder de tijdslimiet (`timeout 2700` en 50 minuten per job), dus het lijkt geen toeval. De oorzaak kan de nieuwe robot zijn, de extra metingen van `meet_diag` uit 78ac6d9, of de add-on zelf (bijvoorbeeld geheugen bij de voxelvorm op 273112 punten). Is het de add-on, dan loopt Blender 4.2 bij een koper vast of valt hij om. | Feit (de fouten en tijden), vermoeden (oorzaak) | hoog (feit), laag (oorzaak) | Het log van die stap (`actions-log.yml` met run 45267268513) of `<fig>-vol.log`; een 4.2-run op 6dc00b2 zonder `CJ_PROEVEN`. |
| A7 | "Rig-toetsen van de e2e groen in alle drie": voor 5.x klopt het op de eindcode (45267268513, FOUT.txt 0, alle logs "KLAAR 0 FOUT"). Voor 4.2 is het gezien op 78ac6d9 (45266243590, groen), niet op de eindcode: de regressie 4.2 van 45267268513 liep om 21:42 nog, en die van 45264302449 staat op FOUT in de stap Rig-toetsen. In 45266243590 was de regressie 5.3.0 rood (knight rechterknie "mirrored"); dat is daarna opgelost in 6dc00b2, maar het bericht noemt die run alleen als groen. | Feit | hoog | `betrouwbaar-uitslag/<run>/regressie-*/FOUT.txt` en `meshy_rig.log`. |
| A8 | Gewone e2e: 45266243549 (78ac6d9) helemaal groen in 4.2, 5.2 en 5.3. 45267268414 (6dc00b2): 5.2 en 5.3 groen, 4.2 om 21:42 nog bij stap 13 Figuurpresets. Het bericht zegt eerlijk "loopt". | Feit | hoog | Uitslag van 45267268414 als hij klaar is. |
| A9 | De 4.2-tijd voor kleding (205 s in de uitslag, uit 7ea796e) is op 78ac6d9 en 6dc00b2 811 en 634 s, met dezelfde Exact-weg in de add-on. Kan aan `meet_diag` of de runner liggen. | Feit (cijfers), vermoeden (oorzaak) | midden | Zelfde meting zonder diag. |
| A10 | **Redenen in het Engels:** `redenen.py` maakt van "no watertight parts" en "overlap before they move" een zin met wat de koper kan doen, gezien in de JSON van 4.2: "Right knee (the cut parts overlap before they move here, place it by hand a few mm along the bone, or use Blender 4.5 or newer, which cuts more reliably)". Duidelijk en juist Engels. Maar de echte meldingen bij de 5 gemiste 4.2-gewrichten zijn deels andere zinnen die redenen.py niet raakt: robotknie "the cut left a loose piece here, place it by hand" (zonder raad over 4.5 of een paar mm), aangeklede rechterknie "Tight: too little limb past this joint to click. Try a spot further from the end". Die zijn wel begrijpelijk. De uitslag zegt "de koper krijgt daar nu een zin met wat hij kan doen": klopt half. | Feit | hoog | `overgeslagen` in `45264302449/4.2.23/robot-a.json` en `45267268513/4.2.23/kleding.json`. |
| A11 | **Gratis deel gelijk:** de diff tegen main raakt in `click_joints/` alleen `betaald/` (omhulsel, herstel, redenen, rig, scharnier, terugval, `__init__`). Omhulsel vervangt `een_lid._samen` alleen bij het registreren van Pro. De e2e-stappen "Betaalde build", "Direct-zip" en "Geen terugval" zijn groen in 45266243549 (drie versies) en 45267268414 (5.x). | Feit | hoog | `git diff origin/main...origin/claude/betrouwbaar-rig --name-only`. |
| A12 | Oorzaak (H snijdt zichzelf, 16 van 16 slechte sneden in 5.x met H "los") en de oplossing passen bij de metingen: na de voxelvorm 0 slechte sneden in 5.x in vier runs. De verklaring voor CI 8 tegen lokaal 9 staat terecht als GOK. | Feit (meting), GOK (verklaring) | midden | Niet elke meetregel nagelezen, alleen de tabellen. |

## Deel C: zou een koper het fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| C1 | In 5.x merkt de koper vooral dat het aangeklede figuur nu alle 9 gewrichten krijgt en in ±1 in plaats van ±8 minuten klaar is. Dat is precies de figuur van de filmpjes: een echte winst die je in een winkeltekst kunt noemen (na M1, en alleen voor 4.5 en nieuwer). | Bij de release in "wat is nieuw" zetten met "Measured in Blender 5.2 and 5.3". | klein |
| C2 | Een 4.2-koper met de nieuwe robot krijgt volgens 45266165562 maar 2 van 9 gewrichten en een lijst van 7 keer dezelfde lange zin, na 18 tot 20 minuten wachten. Dat voelt als kapot. | Eén regel boven de lijst ("Blender 4.2 cuts less reliably, see the tips below") en de raad één keer in plaats van per gewricht; of in 4.2 bij de start meteen zeggen dat 4.5+ beter werkt. | klein |
| C3 | "watertight parts" is een woord voor 3D-printers, voor een animator minder bekend. | "the cut did not give two closed pieces here" of een link naar een korte uitleg. | klein |
| C4 | De raad "place it by hand a few mm along the bone" zegt niet welke knop. | Naam van de knop erbij ("with Add Joint"). | klein |

## Moet (blokkeert akkoord)
- **M1 (A4, A5):** het cijfer 4.2 "35 naar 55 van 60" opnieuw meten of weghalen. Nulmeting en eindmeting moeten op dezelfde testset staan; die is sinds d17205c de nieuwe robot. Meet 4.2 op 6dc00b2 (of later) zodat elke figuur een uitslag heeft, en zet run 45266165562 in de uitslag. Pas dan het bericht aan de hoofdchat aan (nu staat daar 55, en "mist nog 5 knieën").
- **M2 (A6):** uitzoeken waarom alle drie robotjobs in 4.2 op 78ac6d9 en 6dc00b2 na 2 tot 4 minuten stoppen en rigify blijft hangen. Ligt het aan de add-on (Blender valt om of loopt vol), dan is dat erger dan een overgeslagen gewricht en mag het zo niet naar kopers. Ligt het aan `meet_diag`, laat dat zien met een run zonder de extra metingen.
- **M3 (A7, A8):** 4.2 groen op de eindcode laten zien: regressie 4.2 van 45267268513 en e2e 4.2 van 45267268414 liepen nog bij deze keuring. Pas "groen in alle drie" noemen als die klaar en groen zijn.

## Kan (mag later)
- K1 (A10): ook "the cut left a loose piece here" in 4.2 de raad over Blender 4.5 geven, zodat de zin bij elk gemist 4.2-gewricht hetzelfde helpt.
- K2 (A9): de 4.2-tijden uit dezelfde run als de aantallen halen.
- K3: C2 tot en met C4.
- Buiten deel A, voor de keurder van deel B: `betaald/rig.py` is 815 regels (was al 812 op main).

Voor 5.2 en 5.3 zou ik zonder bezwaar akkoord geven; het nee gaat alleen over de 4.2-cijfers en de vastlopende 4.2-jobs.
