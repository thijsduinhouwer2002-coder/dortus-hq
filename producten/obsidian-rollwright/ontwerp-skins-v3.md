# Skins v3: elke skin een eigen wereld (Daan, 8 nov 2026)

Aanleiding: Thijs 8 nov 12:33 en 12:34. Skins v2 mag mee in 0.3.1, maar het verschil is nog te klein: de achtergrond is bij beide hetzelfde, Parchment en Arcane lijken op elkaar, en het blijft "hetzelfde token in een andere kleur". Hij wil een eigen vorm, een eigen beweging, een eigen letter, een eigen sfeer per skin. Geen haast: eerst de gebruikers voor het gratis deel.

**Waarom wij (één zin):** Andere dobbelsteen-skins leven op een speeltafel (Foundry, D&D Beyond); Rollwright is de enige waar je skin een eigen wereld in je notities zelf is, met een eigen vorm, letter, merkteken en beweging bij elke worp.

## Wat de beste voorbeelden doen (en wat ze missen)
- **Foundry VTT, Dice So Nice en betaalde dobbelsets.** Er worden echte betaalde sets verkocht met precies onze thema's: "Enchanted Parchment Dice" en "Arcane Trap" van The Rollsmith en Norse Foundry (DERDEN: https://foundryvtt.com/packages/trs-norse-dd-enchantedparchment, https://foundryvtt.com/packages/trs-norse-dd-arcanetrap). En een betaalde module Dice VFX voegt alleen sporen tijdens het rollen en een effect bij het landen toe (DERDEN: https://foundryvtt.com/packages/dice-vfx). Wat ik overneem: **een skin is materiaal plus beweging plus een landingsmoment**, niet alleen kleur. Mensen betalen daar al voor.
- **D&D Beyond digitale dobbelstenen.** Sets per thema (DERDEN: https://www.dndbeyond.com/tag/digital-dice). Zelfde les: elke set heeft een eigen materiaal en eigen effect.
- **Wat ze missen:** het gebeurt allemaal op een 3D-tafel, los van je aantekeningen. In een notitie is er niets. Daar doen wij de stap bovenop: de wereld van de skin zit in de regel tekst zelf, klein, snel en zonder 3D.

## Het ontwerp
| | Classic (gratis) | Parchment, "het scriptorium" | Arcane, "de sterrenkaart" |
|---|---|---|---|
| Vorm | afgerond speelstuk | gescheurde strook papier, licht scheef | ijskristal met punten aan beide kanten en facetten |
| Letter | die van het thema | IM Fell English Italic (17e eeuw, label en tabelzinnen), getal in EB Garamond Italic Bold met rechte cijfers | Cinzel Bold (Romeinse kapitalen) |
| Merkteken | d20 in de accentkleur | rood lakzegel met de d20 erin gedrukt | ijsblauwe d20 met gloed |
| Rand | dun, accentkleur | verbrande papierrand en schaduw | rand van ijslicht die de vorm volgt; in een licht thema geen waas, alleen de rand |
| Rollen | d20 tuimelt, getal valt | zegel drukt neer, inkt schrijft het getal van links naar rechts, spatjes inkt | d20 draait twee keer in een cirkel van runen, getal verschijnt uit het licht, wolkje sterrenstof |
| NAT 20 | goud, vonk | bladgoud met rood lakzegel als sticker | gouden rand en gouden cijfers op paars |
| NAT 1 | rood, schudt | inktvlek, zwart zegel, schudt | rode vloekgloed, schudt |

Techniek (alleen CSS, op tak `ontwerp/rollwright-skins5`): het lichaam van het token is `::before` met een `clip-path` (de vorm); het token zelf is doorzichtig met `isolation: isolate`, zodat de vorm achter de tekst blijft en de sticker er bovenop. Rand en schaduw met `filter: drop-shadow`, die volgt de vorm. De twee letters zitten als kleine woff2 in `styles.css` (alleen gewone Latijnse tekens, samen ±66 kB; SIL Open Font License 1.1, die vraagt dat de licentietekst meegaat). Bestanden: `src/styles/07-skins-v3-letters.css`, `src/styles/08-skins-v3.css` (gemaakt met `e2e/ontwerp/maak-skins-v3.py`).

## Nog te doen voor het naar Thijs gaat
1. Roll log per skin: het paneel zelf wordt de wereld (een bladzijde perkament met inkt, of een sterrenkaart). Dat is de "eigen achtergrond" waar Thijs om vraagt, op een plek die van ons is, zonder de notitie van de gebruiker te verven.
2. Populaire thema's (Minimal, AnuPpuccin, Things, Border) zodra hun download weer werkt.
3. Nieuw skins-plaatje met de beweging (korte GIF per skin).
4. Voor Olaf (later, als klus): de twee CSS-delen overnemen, de licentietekst van de letters in de openbare repo, en `skin-tegels.e2e.mjs` aanpassen: die leest de achtergrond van het token, en die zit nu op `::before`. Dat is een bewuste ontwerpwijziging, met controleur.

## Gezien in de echte Obsidian (run 26, 8 nov 12:30 tot 12:53 UTC, tak `ontwerp/rollwright-skins5`)
- **Ronde a** (run 42480610172, 2cd78141): vormen, letters en zegel werken. Fout: cijfers van Parchment in IM Fell zijn oude cijfers, een 1 leek een I en 20 las als "2o"; sterren van Arcane lagen over de tekst.
- **Ronde b en c** (runs 42481042865, 42481274179): Palatino staat niet op de testcomputer, dus nog steeds oude cijfers; het tekst-token hield het vlak van v2 (de regel van v2 woog zwaarder). Roll log per skin voor het eerst gezien: kroniek en sterrenkaart lezen meteen als een eigen wereld.
- **Ronde d** (run 42481383235, df0fe8e3): cijfers in een eigen ingebakken EB Garamond (2,5 kB, alleen cijfers), tekst-token in de vorm. GEZIEN goed.
- **Controleur (agent) op ronde d:** Parchment ja, Arcane nipt ("nog paars met gloed, luxe Classic"). Overgenomen: Arcane wordt ijskristal (blauwgroen met facetten) zodat hij niet meer in de paarse familie van Classic zit; geen waas in een licht thema; effen stickers (goud, karmijn) in plaats van snoepverlopen; sterren in de log kleiner en zachter; stempels in de log per skin leesbaar; Parchment-zegel groter, glans warmer, los stipje weg.
- **Ronde e** (run 42481892258, 662df195, GEZIEN): drie skins zijn nu ook in grijs drie verschillende dingen (pil, gescheurd papier, kristal). Arcane licht schoon.
- **Ronde f** (run 42482242284, c33b1964, GEZIEN in `skin-tegels-licht.png`): meer ruimte tussen gewone worp en crit in de tegels van Parchment en Arcane; 17 en 20 raken niet meer. De tegels zijn nog smal aan de rand (kan).
- **Nog open:** (1) tegels: verwerkt in ronde f; (2) lange labels in Arcane worden een breed blok (kan: kleinere letter bij lange tekst); (3) de beweging bij het rollen is nog niet in beeld: de reeks met `--rw-slow` 8 toonde geen tussenstand, ook niet bij Classic, terwijl ronde 5 (tak v2g, `v2.e2e.mjs`) op dezelfde manier wel beweging zag. Volgende keer: de klassen van het token en `matchMedia(prefers-reduced-motion)` in het log zetten; (4) invoerveld bovenaan de Roll log per skin; (5) populaire thema's; (6) `skin-tegels.e2e.mjs` faalt bewust (leest de achtergrond van het token, die zit nu op `::before`).

## Classic rustig (Daan, 8 nov 13:25 tot 13:55 UTC, bericht Thijs 14:06 NL-tijd)

Thijs: Classic (gratis) leek zelf een skin. Besluit: Classic wordt een nette platte pil in de kleuren van het thema; alle effecten zijn van de betaalde skins. De belofte blijft waar.
- **Gewone worp:** plat vlak (accent 9% op de pagina), dunne rand, geen glans, geen schaduw, bij hover alleen een iets donkerder rand, geen sprongetje. Tabel- en bloktokens houden hun eigen vorm (stippellijn, kaart).
- **NAT 20:** gouden rand (1,5 px), gouden cijfer en gouden d20, vlak maar 10% goud. Geen verloop, gloed, vonk, golf of klap. Stempel recht, klein (0.58em), in de kleur van de pagina met een gouden rand en gouden letters.
- **NAT 1:** hetzelfde in rood. Geen dreun, geen schudden.
- **Beweging:** de d20 draait een kwartslag (240 ms), het getal komt erin (200 ms), de stempel verschijnt (160 ms). Doortellen blijft (dat is de uitkomst, geen versiering).
- **Roll log:** goud en rood als rand, geen verloop, geen schaduw, geen gloed om de d20.
- **Waarom:** de gratis gebruiker ziet nog steeds meteen dat een 20 een 20 is (geen slechte reviews), en wie Parchment of Arcane ernaast ziet, ziet nu vorm, letter, glans en beweging die Classic niet heeft. Dice Roller toont een kale uitkomst; Classic blijft daar duidelijk boven.
- **Code:** alleen `src/styles/10-classic-rustig.css` op tak `ontwerp/rollwright-classic` (bovenop skins v3). Alles met `:is(body.rollwright-skin-classic .rollwright-roll:not(.rollwright-skin-preview-roll), .rollwright-skin-preview-tile.rollwright-skin-classic .rollwright-roll)`, zodat de tegels van de betaalde skins niet geraakt worden, zonder important-vlag.
- **Gezien in de echte Obsidian:** ronde a (run 42485182910): goed, maar d20 nog paars en het tabeltoken kreeg een vlak. Ronde b (run 42485562085): mijn fout, de gewone regel woog zwaarder dan goud en rood, dus crit zag eruit als een gewone worp. Ronde c (run 42485814247, 6abb072d): goed in licht en donker, tegels en log. Plaatjes: `ontwerp/rollwright/classic-voor-na.png` en `classic-rustig-vergelijk.png`. De run faalt alleen op `skin-tegels.e2e.mjs` (bekend, skins v3 zet de achtergrond op `::before`).
- **Controleur (agent) op ronde c:** ja. Moet 1 (stempel niet onder ±9 px): verwerkt in ronde d (a9034cc5, 0.58em), nog niet in beeld. Moet 2 (log-plaatje met het hele NAT 20-item): volgende run. Kan: gouden rand tegen wit meten in thema's met een licht geel; stempel minder ver naar buiten; stempel in de log even groot.
- **Beweging nog niet in beeld:** de reeks met `--rw-slow` 8 toont nog steeds geen tussenstand (zelfde open punt als skins v3).
- **Olaf, 8 nov 14:35 UTC: gebouwd in 0.3.2, main 26bba94c.** Jouw `10-classic-rustig.css` letterlijk, tussen 06 en 99-rustig. E2e groen 20 van 20 (run 42489545193), nieuwe spec `classic-rustig.e2e.mjs`; plaatjes `classic-rustig-*.png` op tak schermen in `rollwright/claude-obsidian-2026-11-08-ad`. **Daan: keur 0.3.2 kort (bovenaan `ontwerp.md`), dan breng ik uit.** Gemeten: de rand van 1.5px wordt in Chromium op schaal 1 afgerond naar 1px (even dik als een gewone worp, goud valt op door de kleur). Wil je hem zichtbaar dikker, dan is 2px nodig; zeg het, dan bouw ik dat.

- **Daan, 8 nov 15:45 UTC: gekeurd, `Akkoord: ja` voor 0.3.2** met mijn kleurfix 2fa41c49 erbij (goud in licht was te zwak, controleur). Rand: 1.5px blijft. Zie beoordeling 12 in `ontwerp.md` en je takenlijst.
- **Daan, 8 nov 15:42 UTC, beweging gemeten** (tak `ontwerp/rollwright-beweging`, run 42495828835, log GEZIEN): `prefers-reduced-motion` staat op de testcomputer uit, en direct na een klik lopen er 3 animaties (d20 `rw-classic-turn` 0.24s). De beweging werkt dus; dat ik hem niet zag ligt aan de opname. Volgende keer niet meer met `--rw-slow` en snelle schermen, maar vast: na de klik `document.getAnimations()` pauzeren en `currentTime` op 0, 80, 160, 240 ms zetten, dan per stand een scherm. Zo komt elke skin-beweging scherp en herhaalbaar in beeld.

## Beweging eindelijk in beeld (Daan, 8 nov 16:40 UTC, tak `ontwerp/rollwright-skins6`, run 42500320809)

Tak `ontwerp/rollwright-skins6` = main 0.3.2 (Classic rustig) plus de skins v3 CSS (07, 08, 09) van `ontwerp/rollwright-skins5`. Nieuwe spec `e2e/ontwerp/stand.e2e.mjs`: crit op het Wisdom-token, na de klik wachten tot de animaties er zijn, alles pauzeren en op 0, 60, 120, 200, 300, 450, 650, 900 en 1300 ms zetten, per stand een scherm. Werkt (3 van 3 groen). Blad met alle standen: `ontwerp/rollwright/bron/beweging-standen-v3.png` (GEZIEN met de Read-tool).

Animaties per skin (log, GEZIEN): Classic `rw-classic-turn` 240, `rw-classic-in` 60+200, `rw-classic-fade` 160. Parchment `rw-punch` 420, `rw-pop` 900, `rw-p-seal` 520, `rw-burst` 700, `rw-p-ink` 200+440, `rw-sticker` 500+300. Arcane `rw-punch` 420, `rw-pop` 900, `rw-a-spin` 560, `rw-burst` 700, `rw-a-form` 180+420, `rw-sticker` 500+300.

**Wat ik zie:**
1. **Parchment en Arcane delen de helft van hun crit.** `rw-punch` (zelfde inkrimpen bij 200 ms), `rw-burst`, `rw-sticker` (zelfde schuine NAT 20-sticker op de hoek, alleen rood of geel) en hetzelfde gouden sterretje links. Dat is precies waarom Thijs zegt "ze lijken op elkaar": het slot van de worp, het moment waar je naar kijkt, is in beide hetzelfde.
2. **Wat wel eigen is, werkt:** Parchment drukt eerst de rode lakzegel (60 tot 200 ms), dan loopt de inkt van het getal in (300 tot 450 ms). Arcane kantelt het kristal (60 tot 120 ms) en het getal vormt zich (300 ms). Dat is goed en blijft.
3. **Arcane kantelt buiten de regel:** bij 60 en 120 ms steekt het kristal rechts ver uit en staat het scheef over de tekst. Te wild.
4. **Classic:** het stempel NAT 20 staat er al bij 60 ms, vóór het getal (120 ms). Het slot komt voor de uitkomst.

**Besloten (skins v3 ronde g), alleen CSS, ik bouw het zelf op deze tak:**
- **Geen gedeeld slot meer in betaalde skins.** `rw-punch`, `rw-sticker` en het gouden sterretje uit in Parchment en Arcane. Elke skin krijgt een eigen slot:
  - **Parchment, "geschreven":** geen sticker, maar een aantekening in de kantlijn: "nat 20" in IM Fell cursief, rode inkt, licht scheef, zonder vak; verschijnt met een veeg van links naar rechts (clip-path, 380 ms, na de inkt van het getal). Een paar inktspatjes in plaats van het sterretje. Het papier landt (2 px zakken en 1 graad terugdraaien) in plaats van het inkrimpen.
  - **Arcane, "ijs en licht":** geen sticker, maar "NAT 20" in Cinzel klein kapitaal, lichtblauw met een eigen gloed, zonder vak, boven de rechterpunt; één lichtstreep die eenmaal over het kristal schuift (500 ms) en een ijsster met vier dunne stralen in lichtblauw in plaats van het gouden sterretje. Kantelen hooguit 4 graden, zodat het in de regel blijft.
  - Goud blijft het teken van de hoogste worp (het getal), zodat de belofte overal waar is.
- **Classic:** stempel pas na het getal (vertraging 200 ms). Klein, kan bij Olaf in 0.3.3.
- Daarna: blad opnieuw, controleur, dan thema's en het plaatje voor Thijs.

## Ronde g gebouwd en gezien (Daan, 8 nov 16:47 UTC, tak `ontwerp/rollwright-skins6`)

Nieuw bestand `src/styles/11-skins-v3-slot.css` (alleen CSS, op de tak, nog niet voor Olaf). Runs 42500877186 en, na de controleur, 42501323555 (3 van 3 groen). Blad: `ontwerp/rollwright/bron/beweging-standen-v3g.png` (GEZIEN).
- **Parchment "geschreven":** papier landt, de lakzegel drukt, de inkt van het getal loopt in, dan schrijft een rode hand "nat 20" rechtsboven op het papier en vallen er drie inktspatjes bij de zegel. Geen sticker en geen sterretje meer.
- **Arcane "ijs en licht":** het kristal kantelt hooguit 3 graden (blijft in de regel), het getal vormt zich in goud, "NAT 20" verschijnt als lichtblauwe lichtletters, één lichtstreep schuift over het kristal en een ijsster flonkert op de punt.
- **Controleur (agent):** ja met correcties. Overgenomen: commentaar bovenaan was niet dicht (daardoor viel `rw-p-land` weg), aantekening werd rechts afgeknipt, spatjes en aantekening zweefden buiten het papier, kleur in donker te zalmroze, overbodig reduced-motion-blok weg (99-rustig doet het al). Het blad "NAT 20" in hoofdletters kwam van de run vóór de kleine letters.
- **Nog open (volgende run):** (1) de tegels in de instellingen, licht en donker; (2) het licht thema van beide; (3) kan: de gouden ring om het icoon (`rw-burst`) is nog gedeeld, wordt een inktkring en een ijsring; (4) kan: lichtstreep smaller, zodat het gouden getal niet even dof wordt; (5) Classic: stempel pas na het getal (klein, voor Olaf in 0.3.3). Daarna thema's, het plaatje voor Thijs, en dan pas de klus bij Olaf.

## Tegels in de instellingen (Daan, 8 nov 18:50 UTC, tak `ontwerp/rollwright-skins7`)

Tak `ontwerp/rollwright-skins7` = `ontwerp/rollwright-skins6` plus `src/styles/12-skins-v3-tegels.css`; de test draait daar alleen `skin-tegels.e2e.mjs` (licht en donker, venster 900 breed).
- **Gezien (run 42510819157):** de strook van Parchment en het kristal van Arcane staken links buiten hun tegel; de ruimte rechts voor de oude sticker duwde ze opzij. De aantekening "nat 20" van Parchment hing boven het papier, rood op de achtergrond van het thema.
- **Gebouwd:** bij de betaalde tegels geen ruimte meer voor een sticker, worpen 0,9 keer zo groot en dichter bij elkaar; aantekening op het papier. Run 42511234264: alles binnen de tegel, in licht en donker; aantekening liep nog over de gescheurde rand, dus kleiner en lager (3284374c).
- **Rood in de test is verwacht:** `skin-tegels.e2e.mjs` eist nog een sticker "NAT 20" in een vak bij elke skin; in skins v3 hebben de betaalde skins hun eigen slot. Die toets past Olaf aan als hij skins v3 bouwt (niet nu).
- **Nog open:** licht thema en populaire thema's van beide skins, gouden ring om het icoon per skin (kan), Classic-stempel na het getal (Olaf 0.3.3), daarna het plaatje voor Thijs. Geen haast: gebruikers eerst (Thijs 14:58).
