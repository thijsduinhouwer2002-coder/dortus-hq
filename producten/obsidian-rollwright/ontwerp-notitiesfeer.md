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
