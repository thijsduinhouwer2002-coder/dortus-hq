# Keuringen 24 nov 2026 avond, Daan
Drie keuringen voor Click Joints: herkeuring clip 2 Pro video guide (Chris), persblad (Bram), Pro 1.2.7 Shift + rechtsklik (Olaf). Ik heb niets gebouwd.

## 1. Herkeuring clip 2 "Fit test" (Chris, 15:50)
Wat ik keurde: `commercie/blender-click-joints/pro-uitleg/2-fit-test.mp4` (13,0 s, 1920x1080, 30 fps, ffprobe), beeld per seconde en eerste en laatste beeld zelf bekeken (`2026-11-24-clip2-eerste-laatste.png`).
Akkoord: **ja**.

| # | Bevinding | Feit of vermoeden | Zekerheid |
|---|---|---|---|
| A1 | M1 opgelost: eerste beeld alleen de vijf staafjes, laatste beeld alleen staafjes (bal en scharnier), nergens de voetbalfiguur. | Feit (GEZIEN, 14 beelden) | hoog |
| A2 | C1 erin: "Five joints: 0.10 0.15 0.20 0.25 0.30 mm" staat 4 s in beeld, leesbaar. Slotzin "Keep the one that turns without wobble" gelijk aan de melding onderin Blender ("Print all five. Use the clearance of the one that turns without wobble."). | Feit (GEZIEN) | hoog |
| C1 | Kan: het paneel toont Clearance 0.20 terwijl de strip vijf maten heeft. Niet fout (dat is de instelling), wel iets om in clip 3 niet te herhalen. | | |

De hoofdchat mag clip 1 en 2 als "Click Joints Pro video guide" bij het product zetten.

## 2. Persblad Click Joints Pro (Bram, 16:20)
Wat ik keurde: `platformen/blender/persblad/press/` (index.html, 3 clips, 2 beelden), lokaal geopend met `/styles.css` en `/site.js` van dortus.com (curl), 390 en 1280 breed, hele pagina bekeken (`2026-11-24-persblad-390.png`). Superhive-pagina zelf met curl gelezen.
Akkoord: **ja**. Kan-punten mogen, hoeven niet voor het live zetten.

### Deel A: klopt het?
| # | Bevinding | Feit of vermoeden | Zekerheid |
|---|---|---|---|
| A1 | Prijzen $12 en $45 staan op superhivemarket.com/products/click-joints-pro (data-price="$12", "$45"). | Feit (GEZIEN 24 nov ±17:25 NL, curl) | hoog |
| A2 | "What it does not do" klopt met de productpagina: "Best in Blender 4.5 and newer", "Recognises common bone names: ... 3ds Max Biped and Daz", "can not be enabled at the same time"; enkels 5.2 of nieuwer klopt met de gekeurde note 1.2.6. | Feit (GEZIEN) | hoog |
| A3 | Geen zijwaarts scrollen op 390 en 1280 (scrollWidth gelijk aan breedte). Tekst overal leesbaar, ook Facts. | Feit (GEZIEN, Playwright) | hoog |
| A4 | Geen naam, adres of mail van Thijs; vragen gaan naar de supportlink. | Feit | hoog |

### Deel C: mooier
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| C1 | Clip 2 en 3 dragen bovenin nog de kop "Click Joints Pro · 1. Figure from rig", omdat ze uit clip 1 geknipt zijn. Een journalist die clip 3 "Exploded view" los gebruikt, ziet "1. Figure from rig". | Kop per persclip weglaten of gelijk aan de naam op de pagina. | klein |
| C2 | "can not" twee keer (ook op Superhive). Goed Engels is "cannot". | Op beide plekken "cannot". | klein |
| C3 | "with the parts in red where they would hit" kan lezen als botsingscontrole. Wat je ziet is rood voorbij de stop ("+12° past limit"). | "with the parts in red past the stop". | klein |

## 3. Pro 1.2.7 Shift + rechtsklik (Olaf, 16:50)
Wat ik keurde: tak `claude/blender-pro-1.2.7-shift` (b105332), diff tegen main gelezen: `betaald/cursor_lid.py` (nieuw, 132 regels), `betaald/scharnier.py` (296 regels), `e2e/toetsen_shift.py`, workflow PRO_VERSIE 1.2.7.
Akkoord: **ja voor de code**, uitbrengen pas na moet 1.

### Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| A1 | Alleen als het punt op de huid ligt (find_nearest binnen 0,5 mm) en as-bron View direction verandert er iets. Cursor binnen het figuur en as-bron Cursor: zelfde pad als voorheen (`bijstellen` geeft het oude punt en lid terug). | Feit (code gelezen) | hoog | toets (c) in toetsen_shift |
| A2 | Knee en de andere figuurknoppen lopen via `plaats_scharnier` (`figuur.py:122`), dus de reparatie geldt ook voor de knoppen uit de melding van de Regisseur. Testkaart ook, maar die zet de cursor zelf. | Feit (grep) | hoog | |
| A3 | Lidas uit de smalste breedte in 36 richtingen in het schermvlak, gemeten vanuit het midden in de diepte: bij een been van voren of opzij geeft dat een verticale as. Bij een plek waar het lid breder is dan lang (een vuist, een voet van boven) kan de smalste richting de verkeerde zijn. | Vermoeden | midden | Shift + rechtsklik op een enkel van boven gezien |
| A4 | Na `bvh` eerder bouwen wordt `me` op alle drie vroege uitgangen (geen as, al een scharnier, graden fout) weer opgeruimd; de graden-uitgang stond al na de bouw op main. | Feit (diff gelezen) | hoog | |
| A5 | De melding zegt wat er gebeurde: "Cursor on the surface: limb axis from the mesh and centred in the limb." Britse spelling, past bij "millimetres" op de site. | Feit | hoog | |

### Deel B: regels
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| B1 | e2e run 45424594725 op b105332 liep nog in 4.2.23, 5.2.3 en 5.3.0 toen ik keek (±17:20 NL). Automatische keurder groen. | Feit (GEZIEN, Actions-API) | hoog | tests groen voor af |
| B2 | Toetsen zijn toegevoegd, geen bestaande toets is verzwakt (toetsen_kijk blijft weigeren binnen het figuur). | Feit | hoog | |
| B3 | Bestanden onder 400 regels. | Feit | hoog | |

### Moet
1. e2e 45424594725 groen in alle drie versies voor de voeg naar main. Rood in 4.2: laten zien of het door deze wijziging komt.

### Kan
- K1: een vierde geval in toetsen_shift: Shift + rechtsklik op een lid dat schuin in beeld staat (bijvoorbeeld 45 graden), zodat de 30-gradengrens zelf getoetst is.
- K2: de nieuwe Shift-melding meenemen in de 1.2.7-note: "Shift + right click on the skin now works with Knee and the hinge buttons." Dat is een zin die kopers van clip 3 direct herkennen.
