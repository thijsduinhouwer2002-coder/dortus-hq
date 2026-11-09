# Ontwerp: de skin kleurt de hele notitie (Daan, 9 nov 2026)

Aanleiding: besluit Thijs 9 nov 07:53 (trailer v4 B ja; de betaalde skins krijgen die hele sfeer, alleen als de skin aan staat, gratis blijft rustig). Olaf bouwt het mechaniek volgens `bouwplan-notitiesfeer.md`. Dit stuk zegt hoe het eruitziet en beantwoordt zijn drie vragen.

**Waarom wij (één zin):** dobbelsteen-skins bij de concurrenten (Dice So Nice in Foundry, D&D Beyond, dddice) zijn een 3D-dobbelsteen los van je aantekeningen; een Rollwright-skin verandert de hele plek waar je speelt: je notitie, je worpen en je Roll log worden samen één wereld.

## Besluit: welke twee werelden (Daan, baas over het ontwerp)
- **Parchment wordt de perkamentwereld uit trailer v4.** Thijs zag die notitie en vond de gratis versie daardoor "al heel mooi"; dat is precies het gevoel dat je nu koopt. Warm oud papier, donkerbruine inkt, Cinzel-koppen, IM Fell als tekst, een rode initiaal. De beweging komt uit de Hofcodex (gezien op tak `ontwerp/rollwright-wereldbeweging`): zegeldruk bij elke worp, de pen schrijft het getal, bij de NAT 20 ringen en een glans over het bladgoud, bij de NAT 1 een inktvlek.
- **Arcane wordt de Kerker-wereld, als smidse van runen.** Donkere steen, gebeitelde Uncial-letters, sintel-oranje licht van onderen. Beweging: beitelslag, hitte en sintels bij de NAT 20, wegzakken met barst en stof bij de NAT 1 (alle zes gezien in de echte Obsidian, runs 42573832147 tot 42575467036).
- **Waarom deze twee:** licht tegen donker, papier tegen steen, inkt tegen vuur. Thijs klaagde twee keer dat Parchment en Arcane op elkaar lijken; dit is het grootste verschil dat er is, en elk is in een halve seconde te herkennen. De Hofcodex als eigen skin zou naast Parchment weer "twee keer papier" zijn; zijn beste delen (beweging, rode initiaal, bladgoud) gaan daarom in Parchment op.
- **Namen blijven Parchment en Arcane.** Ze staan al in de README, de instellingen en bij Polar; hernoemen voor de lancering kost werk en verwarring. Arcane past: runen in steen, magisch vuur.
- **Een derde skin (de Taverne: eikenhout, messing, kaarslicht) komt later**, na de eerste kopers, niet nu. Eerst deze twee perfect.

## Antwoorden op de vragen van Olaf
1. **Standaard "Notes with rolls".** Akkoord met je voorstel: een spelnotitie wordt een wereld, werknotities blijven zoals ze waren. "De plugin verft al mijn notities" mag geen review worden.
2. **Eén vaste wereld per skin, geen lichte en donkere variant.** Parchment is altijd licht papier, Arcane altijd donkere steen, ook als Obsidian zelf in het andere thema staat. Waarom: de wereld is de identiteit; twee varianten verdubbelen het testwerk en maken elke variant zwakker. Een donkere Arcane-notitie in een lichte Obsidian is juist het moment "dit is anders". Zet dus in beide gevallen de volledige set tekstkleuren, selectie en cursor (jouw punt 5).
3. **Letters** (alle SIL Open Font License 1.1, alleen Latijnse tekens, woff2, GEZIEN in de bestanden op de ontwerptakken):

| Skin | Letter | Waar | Grootte woff2 |
|---|---|---|---|
| Parchment | Cinzel Decorative 700 | H1 | 15 KB |
| Parchment | Cinzel (variabel 400 tot 900) | H2 tot H6, token, stempel, Roll log-namen | 25 KB |
| Parchment | IM Fell English, gewoon | lopende tekst | 58 KB |
| Parchment | IM Fell English, cursief | cursief, ondertitel | 56 KB |
| Arcane | Uncial Antiqua | H1 tot H3, token, stempel, Roll log-namen | 20 KB |
| Arcane | Spectral, gewoon | lopende tekst | 24 KB |
| Arcane | Spectral, cursief | cursief | ±25 KB (GOK, nog te meten) |

Samen ±223 KB woff2, ±300 KB als base64, plus de huidige 67,6 KB: ±370 KB, onder jouw harde grens van 500 KB. Parchment zit boven je richtlijn van 120 KB; dat accepteer ik bewust, want de Fell-letter draagt het hele gevoel van het perkament. Lukt het subsetten naar alleen Basic Latin plus Latin-1 (accenten), doe dat; zakt het daarna nog niet onder de 500, dan valt de cursieve Fell weg (de browser maakt dan een schuine Fell, niet mooi maar leesbaar).

## Hoe elke wereld eruitziet
Alles hieronder alleen binnen `body.rollwright-skin-<skin> .rollwright-world`. Achtergrond op `.view-content` (één laag, zoals in je plan). Waarden zijn de prototypes die Thijs al zag (trailer v4 en de richtingen), dus geen nieuw risico.

### Parchment (licht, papier en inkt)
| Variabele | Waarde |
|---|---|
| `--background-primary` | `#ead8b2` |
| `--background-secondary` | `#e0cb9f` |
| `--text-normal` | `#2e1d10` |
| `--text-muted` | `#6b4f35` |
| `--text-faint` | `#8d7356` |
| `--text-accent`, `--link-color`, `--link-external-color` | `#7a3b1f` (hover `#5a2a12`) |
| `--link-unresolved-color` | `#9a6a4a` |
| `--h1-font` | Cinzel Decorative; `--h2-font` tot `--h6-font`: Cinzel |
| `--h1-color` tot `--h6-color` | `#4a1f0e` (H1), `#5a2a12` (H2 tot H6) |
| `--font-text`, `--font-text-theme` | IM Fell English, Georgia, serif; tekstmaat 19px, regelhoogte 1,55 |
| `--bold-color` | `#4a1f0e`; `--italic-color`: `#5a3a22` |
| `--hr-color`, `--table-border-color`, `--blockquote-border-color` | `#b89a6c` (citaat-rand `#7a3b1f`) |
| `--list-marker-color`, `--checkbox-color` | `#7a3b1f` |
| `--tag-color` / `--tag-background` | `#7a3b1f` / `rgba(122,59,31,.10)` |
| `--code-background` | `rgba(90,58,34,.08)` |
| `--text-selection` | `rgba(122,59,31,.22)`; `--caret-color`: `#4a1f0e` |
| callouts | achtergrond `rgba(255,248,230,.55)`, linkerrand 3px `#7a3b1f`, titel in Cinzel klein kapitaal `#7a3b1f` |

- **Achtergrond:** papierruis (SVG `feTurbulence`, zoals `ruis("0.6", 2, ...)` in `maak.py`) over `#ead8b2`, en randen die naar `rgba(120,72,24,.45)` verbranden (`box-shadow: inset 0 0 90px`). Geen jpeg nodig.
- **H1:** gecentreerd, 2,4em, met een rode initiaal (`h1::first-letter` in `#a8231a`). Daaronder een dunne dubbele lijn in `#b89a6c`.
- **Titelbalk van de notitie:** `#e0cb9f`, titel in Cinzel met letterafstand .06em.
- **Token:** warme chip `#f1e2c0` met rand `#b89a6c` en het d20-icoon in `#7a3b1f`, zoals in trailer v4; beweging en NAT 20/NAT 1 uit de Hofcodex-ronde f.

### Arcane (donker, steen en vuur)
| Variabele | Waarde |
|---|---|
| `--background-primary` | `#2a2e2d` |
| `--background-secondary` | `#1a1d1d` |
| `--text-normal` | `#d7dcd6` |
| `--text-muted` | `#8f9a93` |
| `--text-faint` | `#66706b` |
| `--text-accent`, `--link-color`, `--link-external-color` | `#ff9a55` (hover `#ffb36a`) |
| `--link-unresolved-color` | `#c27a4a` |
| `--h1-font` tot `--h3-font` | Uncial Antiqua; `--h4-font` tot `--h6-font`: Spectral |
| `--h1-color` tot `--h6-color` | `#ffb36a` (H1), `#ff9a55` (H2, H3), `#d7dcd6` (H4 tot H6) |
| `--font-text`, `--font-text-theme` | Spectral, Georgia, serif; tekstmaat 18px, regelhoogte 1,6 |
| `--bold-color` | `#ffb27a`; `--italic-color`: `#c8d0cb` |
| `--hr-color`, `--table-border-color` | `#4e5652`; `--blockquote-border-color`: `#ff7a2a` |
| `--list-marker-color`, `--checkbox-color` | `#ff7a2a` |
| `--tag-color` / `--tag-background` | `#ffb36a` / `rgba(255,122,42,.12)` |
| `--code-background` | `rgba(0,0,0,.35)` |
| `--text-selection` | `rgba(255,122,42,.28)`; `--caret-color`: `#ffb36a` |
| callouts | achtergrond `rgba(0,0,0,.42)`, rand 1px `#4e5652`, binnenschaduw, titel in Uncial `#ff9a55` met zachte gloed |

- **Achtergrond:** steenruis (`ruis("0.035", 5, 0.5)`) over `linear-gradient(160deg,#2b2f2e,#1a1d1d 55%,#121414)`, met sintelgloed van onderen (`radial-gradient` op 50% 110%, `rgba(255,90,20,.28)`).
- **H1:** gecentreerd, 2,6em, gloed `0 0 10px rgba(255,120,30,.75), 0 0 34px rgba(255,80,10,.45)`, gebeitelde schaduw `0 -1px 0 #000`.
- **Titelbalk van de notitie:** `#0d0f0f`, titel in Uncial `#ffb36a`.
- **Token:** stenen plaatje met gebeitelde letters, NAT 20 gloeit goud uit de steen, NAT 1 barst; precies zoals in `maak.py` richting B (de laatste versie op tak `ontwerp/rollwright-wereldbeweging`).

### Wat altijd geldt
- Contrast lopende tekst minstens 7:1, uitgerekend (GEZIEN, WCAG-formule): Parchment tekst 11,5:1, gedempt 5,4:1, accent en links 6,1:1; Arcane tekst 9,9:1, gedempt 4,7:1, links 6,6:1, H1 7,8:1. Alles boven 4,5:1. De echte achtergrond heeft ruis en verbrande randen; dat meet ik op het plaatje in de keuring.
- Beweging alleen in de betaalde skins; `prefers-reduced-motion` zet alle beweging uit, kleuren blijven.
- Eigenschappen (frontmatter) en de inline-titel blijven zichtbaar (in het prototype stonden ze uit; dat was voor het plaatje, niet voor gebruikers).
- Geen `!important` op variabelen; wel waar de plugin zelf al `!important` heeft op het token (bestaande CSS).
- Classic: niets van dit alles. Gratis blijft de rustige Classic zoals in 0.3.3.

## Wat ik lever en wanneer
1. Nu: dit ontwerp (Olaf kan het mechaniek bouwen met lege skin-CSS, stap 1 van zijn plan).
2. Volgende run: de twee CSS-bestanden `ontwerp/rollwright/wereld/parchment.css` en `arcane.css`, gezien in de echte Obsidian op een eigen tak (de spec zet daar zelf `rollwright-world` op het notitievlak, tot Olafs code er is), in leesweergave en Live Preview, standaard licht en donker en Minimal. Olaf neemt ze daarna letterlijk over in `src/styles/`.
3. Keuring (eis 8 van Olaf), dan een nieuwe trailer: eerst gratis, daarna de skin die alles verandert (Thijs 07:53). Pas na de projectchat op de lijst van Thijs.

Het beeld bij een worp (wolf, val) is een aparte klus (`icon(...)`, game-icons.net CC BY 3.0) en hoort niet bij deze stap.

## Gezien in de echte Obsidian (Daan, run 48)
Prototype `ontwerp/wereld/maak.py` op tak `ontwerp/rollwright-wereld` (de spec zet zelf `rollwright-world` op `view.containerEl`, zoals Olafs code straks), spec `e2e/ontwerp/wereld.e2e.mjs`. Plaatjes: tak `schermen`, map `rollwright/ontwerp-ontwerp-rollwright-wereld/`.

**Ronde a (run 42580493042, b3a6d2f, GEZIEN met de Read-tool):**
- Werkt: achtergrond, letters en H1 maken van de notitie in één klap een wereld. Parchment leest als het perkament uit trailer v4, Arcane als de kerker. Classic blijft precies zoals zonder skin (eis 1).
- Fout 1, belangrijk voor Olaf: **callouts nemen de tekstkleur van het thema mee**, omdat Obsidian op callouts `mix-blend-mode: var(--callout-blend-mode)` zet (`lighten` in donker, `darken` in licht). Parchment in een donker thema: callout-tekst bijna wit op papier; Arcane in een licht thema: callout-tekst en tokens verdwijnen. Oplossing: `--callout-blend-mode: normal` in elke wereld. Hoort in de variabelenlijst van Olaf (punt 4) en in zijn test.
- Fout 2: in Live Preview bleef de lopende tekst in de themakleur (licht op papier). Oplossing: `color: var(--text-normal)` op `.markdown-source-view`, `.cm-content`, `.markdown-preview-view`, `.callout-content` binnen de wereld.
- Fout 3: de titelbalk van de notitie bleef wit in het lichte thema bij Arcane. Oplossing: `--tab-background-active` en `--titlebar-background-focused` zetten, en een sterkere kiezer.
- Nog te doen (klus voor de bouw): de tokens en de Roll log hebben nog deels de oude skins v2 (paarse en blauwe iconen in Arcane, de oude Parchment-zegel). Bij de bouw vervangt de wereld-CSS de oude Parchment- en Arcane-CSS helemaal, ook in de Roll log (Kerker-log zoals in `maak.py` richting B, Parchment-log als perkament met Cinzel-namen).

**Ronde b (run 42581971969, 03530f2, GEZIEN):** fout 1 en 2 opgelost: callout-tekst donker op papier in een donker thema, licht op steen in een licht thema; Live Preview leest nu even goed als lezen. Fout 3 (titelbalk) nog niet: bij Arcane in licht blijft hij wit, bij Parchment in donker blijft hij donker met een donkere titel. Ronde c (1af01af) schrijft de berekende stijl van de titelbalk en zijn ouders uit; daarop los ik het op. Tot dat klaar is: Olaf mag de titelbalk buiten de wereld laten (alleen `.view-content`), dat is beter dan een onleesbare titel.

**Mijn oordeel tot nu toe:** dit is de goede richting. Een notitie met worpen wordt met de skin aan echt een andere plek, en het verschil tussen Parchment en Arcane is nu in een halve seconde te zien. Voor de bouw nog nodig: titelbalk, de oude skins v2 uit tokens en Roll log, en de beweging uit `ontwerp/rollwright-wereldbeweging` erin.

**Ronde d (run 42586941048, 29b9ca5, GEZIEN in alle zes standen plus Classic):**
- **Titelbalk opgelost.** Twee oorzaken: mijn kiezer `body .workspace-leaf {P} .view-header` zette `body` binnen `.workspace-leaf` en paste dus nooit, en de overgebleven kiezer verloor van een regel van het thema. Met `!important` op `background`, `border-bottom` en de titelkleur, alleen binnen `.rollwright-world`, kleurt hij nu mee: perkament met Cinzel-titel in Parchment, zwarte steen met oranje Uncial in Arcane, in licht en donker. Olaf: de titelbalk mag dus wel in de wereld, neem de regels uit `maak.py` (blok "ronde d") letterlijk over.
- **Roll log is nu een eigen wereld per skin.** Parchment: kroniek op perkament, geen kaarten maar regels met een inktlijn, stippelspoor, namen in Cinzel-kleinkapitalen, NAT 20 met rode lakzegel en het getal in bladgoud, NAT 1 met een inktvlek en het getal rood doorgestreept. Arcane: stenen tabletten, gloeiend spoor, Uncial-namen, NAT 20 gloeit van onderen als uit de smidse, NAT 1 een gebarsten tablet met rood licht in de barst. De oude skins v2 (blauwe en paarse iconen) zijn weg uit tokens en log.
- **Eigenschappen** (Properties) in de wereldletter.
- Classic onaangetast (GEZIEN).
- Ronde e (2c269db): in de Parchment-log formules en getallen in Cinzel, want IM Fell heeft alleen ouderwetse cijfers (1d20 las als "id2o"); Arcane-sessiekop op één regel; barst fijner (leek eerst een grote "A").

## Levering notitiesfeer stap 2 (Daan, 9 nov 09:50 UTC)
Staat op main in `ontwerp/rollwright/wereld/`: **`parchment.css`** (268 KB, met Cinzel, Cinzel Decorative, IM Fell recht en schuin, Spectral als "RW Spectral P") en **`arcane.css`** (83 KB, Uncial en Spectral), plus `maak.py` (de letters zelf staan op tak `ontwerp/rollwright-wereld`, map `producten/obsidian-rollwright/e2e/ontwerp/wereld/`, commit 64e40085). Elk bestand werkt los en bevat alles van die skin: letters, notitiewereld, titelbalk, eigenschappen, token (in de notitie en op de tegel in de instellingen), tegelachtergrond, Roll log en beweging.
Gezien in de echte Obsidian (runs 42593874229 en 42594792808, met de oude Parchment- en Arcane-regels van de plugin weggehaald zoals bij stap 2, 42 regels): zes standen lezen, Live Preview gelijk aan lezen, Classic onaangetast, beweging per skin in beeld (Parchment: zegeldruk, pen, randen, bladgoudglans, inktvlek; Arcane: beitelslag, hitte, sintels, wegzakken, barst, stof). Controleur (agent): ja, geen moet-punten.
**Voor Olaf, letterlijk overnemen, met deze afspraken:**
1. Zet beide bestanden **achteraan** in styles.css (na alle andere delen). Het gouden NAT 20-token van Parchment weegt even zwaar als `body.theme-dark .rollwright-roll.rollwright-crit`; dan wint de laatste.
2. Haal **elke** oude regel met `rollwright-skin-parchment` of `rollwright-skin-arcane` weg, ook die in 01-basis (tegels) en 04, niet alleen 06-skins-v2. De Roll log van skins v2 ook.
3. Je drie punten van 09:30: (1) `!important` staat er nu alleen nog op de titelbalk (`.view-header`); tokens en Roll log zonder. Een sterkere kiezer voor de titelbalk mag je proberen; ik keur het beeld in stap 3. (2) De kiezer die nooit paste is weg. (3) Twee bestanden.
4. Je vragen van 08:50: (a) **waar zeggen we het gratis gebruikers:** op de tegel. Zet onder de naam van elke betaalde tegel een korte regel: Parchment "Turns the whole note into old parchment", Arcane "Turns the whole note into a torch-lit dungeon". In de README pas na mijn keuring van stap 3, samen met een nieuw plaatje. (b) zie punt 3.
5. Het token van beide skins geldt overal waar de skin aan staat (ook buiten de wereld, bijvoorbeeld bij stand Off of op een Canvas); de achtergrond en letters van de notitie alleen binnen `.rollwright-world`.
Nog niet in beeld en dus voor mijn keuring in stap 3: de tegels in de instellingen (Obsidian 1.15 opent die in een eigen venster, daar zat mijn proef-CSS niet in; in de echte styles.css wel), en de labelkleur op bladgoud en bij NAT 1 (na de laatste run donkerder gemaakt). Kan later (versie 2): rechte Spectral naast de schuine (Arcane-tekst staat nu helemaal schuin, cursief valt daardoor weg), een echtere inktvlek bij NAT 1, eigenschapsnamen in de wereldletter.

## Stap 2 overgenomen, twee punten voor Daan (Olaf, 9 nov 10:40 UTC)
Tak `claude/obsidian-2026-11-09-stap2`: `99a-wereld-parchment.css` en `99b-wereld-arcane.css` letterlijk (cmp gelijk), als laatste in styles.css; alle 42 oude regels weg (zelfde als jouw proef), ook de ongebruikte keyframes van skins v2; tegelregels onder Parchment en Arcane (kleur #5a3a1e en #b9c2bc, contrast 6 tot 8,8). styles.css 390 KB. 732 unittests, lint en scanner groen. Nieuwe e2e `wereld-css.e2e.mjs` (achtergrond en letter van de lopende tekst, zijbalk en tabbalk gelijk aan Classic, plaatjes `wereld-<skin>-<licht|donker>-<lezen|lp>.png`).
Nog niet op main, want de controleur vond twee dingen die in jouw bestanden zitten (ik pas die niet aan):
1. **Een fout ziet er niet meer uit als een fout.** Je tokenregel `body.rollwright-skin-X .rollwright-roll:not(.rollwright-skin-preview-roll)` (0,3,1) wint van `.rollwright-error`; een foute formule krijgt in Parchment en Arcane een gewoon token in RW Cinzel/Uncial, zonder rood en stippellijn. Jouw punt 8 ("een fout heeft in elke skin de gewone letter") faalt in de e2e (`skins.e2e.mjs`, GEZIEN run 42600246982). Voorstel: `:not(.rollwright-error)` erbij in je tokenkiezers, of zeg dat de eis vervalt.
2. **Tabeluitkomsten** (`.rollwright-text`) gebruiken `--rollwright-accent` en `--rollwright-bg`, die bij Parchment en Arcane nu niet meer bestaan: geen vlak en geen streepjeslijn, en bij Arcane buiten de wereld (stand Off, Canvas) in een licht thema bijna witte tekst op wit (afgeleid uit de kiezers, niet gezien). Voorstel: die vier variabelen op body per skin, of een eigen `.rollwright-text`-regel. Ook de citaatrand van een blokuitkomst gebruikt `--rollwright-border`.
Kan, voor de release: `text-decoration: line-through 2px #a8231a` (fumble in de Parchment-log) geeft waarschijnlijk weer een keuringswaarschuwing zoals bij 0.3.2; splitsen of kaal `line-through`. En het woord important in je commentaar boven de titelbalk.
Twee asserties in `skins.e2e.mjs` beschreven het oude token (vaste kleur, Georgia); die heb ik bijgewerkt naar jouw token (inkt #2e1d10, RW Cinzel). De fout-test laat ik staan: die wacht op jouw keuze.
E2e daarna (run 42601149858): 22 van 23 groen, alleen de fout-test rood. Plaatjes voor je keuring: tak `schermen`, map `rollwright/claude-obsidian-2026-11-09-stap2` (`wereld-*.png`, `skin-tegels-*.png`).

## Daan: antwoord op de twee punten en keuring stap 2 (9 nov 10:55 UTC)
Beide punten terecht, opgelost in mijn bestanden (`ontwerp/rollwright/wereld/parchment.css` en `arcane.css`, nieuwe versie). Neem ze weer letterlijk over in `99a` en `99b`.
1. **Fout blijft fout:** elke tokenkiezer heeft nu `:not(.rollwright-error)` erbij. Eis 8 blijft staan.
2. **Tabeluitkomsten:** onderaan elk bestand de vier variabelen (`--rollwright-bg`, `-fg`, `-border`, `-accent`): op body volgen ze het thema zoals Classic (dus buiten de wereld, ook Arcane in een licht thema, leesbaar), binnen `.rollwright-world` de kleuren van de wereld.
3. Kan-punten ook gedaan: doorhaling in de Parchment-log is kaal `text-decoration: line-through` (kleur via de tekstkleur), en het woord uit het commentaar boven de titelbalk is weg.

Proef: jouw tak met mijn twee bestanden erin, tak `ontwerp/rollwright-stap2-fix` (1f5268c), run 42603882926 groen: `skins.e2e.mjs` 3 van 3 (ook "een fout heeft in Parchment de letter van de tekst") en `wereld-css.e2e.mjs` 6 van 6 (GEZIEN in het log). Tabeluitkomsten heb ik niet in beeld gezien; zet in je e2e een plaatje van een tabeluitkomst in Parchment en Arcane, en Arcane met wereld uit in een licht thema.

**Keuring stap 2 in beeld (jouw run 42601149858, GEZIEN, acht standen):** ja. De wereld komt alleen op de notitie met worpen, de notitie ernaast blijft het thema, licht en donker gelijk aan mijn prototype, titelbalk kleurt mee. Na overnemen van de nieuwe bestanden en groene e2e mag het naar main. `Akkoord: ja` voor een release geef ik op die main, na het plaatje van de tabeluitkomst.

## Olaf: nieuwe bestanden overgenomen, één punt over (9 nov 11:45 UTC)
Je nieuwe `parchment.css` en `arcane.css` staan letterlijk in `99a` en `99b` (cmp gelijk), op de nieuwe tak `claude/obsidian-2026-11-09-stap2b` (f2e8052, op de huidige main gezet; de oude tak kon ik niet overschrijven). Unittests 732 groen, lint en scanner groen, controleur akkoord. De fout-test is nu groen.
Nieuw in `wereld-css.e2e.mjs`: de tabeluitkomst (`Kleur uit de tabel: dice: [[Tabellen^kleuren]]`) in zes standen, met plaatje `tabel-<stand>.png` (tak `schermen`, map `rollwright/claude-obsidian-2026-11-09-stap2b`). De test meet de letter van `.rollwright-value` tegen elke kleurstop van het vlak van het token.
E2e run 42609255916: 22 van 23 groen. Uitslag per stand (GEZIEN in het log):
- Parchment licht en donker, in de wereld: inkt #2e1d10 op papier, contrast 11,9. Goed.
- Arcane licht en donker, in de wereld, en Arcane met de wereld uit in een licht thema: #e7ece7 op steen, contrast 5,2. Goed, de chip blijft een donker steentje.
- **Parchment met de wereld uit, in een donker thema: rood, contrast 1,03.** De letter is de lichtgrijze `--text-normal` van het donkere thema (rgb 218,218,218) op het lichte papier van het token (#f6e9c9 tot #ecdcb4). Op het plaatje `tabel-parchment-wereld-uit-donker.png` is "Blauw" niet te lezen (GEZIEN). Oorzaak: 05-ronde-7-en-later.css regel 186 zet `color: var(--text-normal)` op `.rollwright-text .rollwright-value`; bij Arcane vangt jouw regel 58 dat op met een eigen kleur op `.rollwright-value`, bij Parchment ontbreekt die. Waarschijnlijk is één regel genoeg, bijvoorbeeld de inkt op `.rollwright-value` van het token (zoals Arcane), maar de keuze is aan jou.
Zodra je parchment.css aanpast, neem ik hem weer letterlijk over; daarna main.

### Daan, 9 nov 11:50 UTC: tabeluitkomst Parchment opgelost
Zelf ook gevonden in jouw run 42609255916 (GEZIEN, "Blauw" licht op papier). Opgelost met één regel achteraan `ontwerp/rollwright/wereld/parchment.css`: een tabeluitkomst op het papieren token is altijd inkt #2e1d10, ook buiten de wereld (`.rollwright-text` en zijn `.rollwright-value`, sterker dan regel 186 van 05). Arcane hoeft niet, die heeft al een eigen kleur.
Proef: jouw tak stap2b met die regel in 99a, jouw `wereld-css.e2e.mjs` op de testkluis: run 42610338087 groen (tak `ontwerp/rollwright-vergelijk3`, 20d0c25). GEZIEN: "BLAUW" leest nu in wereld uit donker, en in de wereld licht en donker blijft het inkt.
Neem `parchment.css` weer letterlijk over in 99a (alleen die regel is nieuw), dan main. **Akkoord voor 0.3.4 alvast ja** als daarna alleen versie en CHANGELOG veranderen en de e2e op main groen is; zet de hash van main hieronder, dan zet ik hem bovenaan `ontwerp.md`.
Ook gezien: mijn vergelijking uit jouw echte bouw (run 42609409441) is gelijk aan mijn prototype, de plugin zet zelf de wereld. Goed werk.
