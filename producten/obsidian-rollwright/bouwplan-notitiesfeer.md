# Bouwplan: de skin kleurt de hele notitie (Olaf, 9 nov 2026)

Aanleiding: besluit Thijs 9 nov 07:53. De betaalde skins krijgen de hele sfeer van de notitie (achtergrond, lettertype, kleuren, beeld bij worpen), alleen als de skin aan staat. Gratis blijft rustig. Daan ontwerpt hoe het eruitziet, Olaf bouwt. Dit stuk gaat over het mechaniek: waar de sfeer komt, wanneer, en hoe het netjes blijft met andere thema's. Het uiterlijk zelf staat er bewust niet in.

**Waarom wij (één zin, van Daan):** een Rollwright-skin verandert de hele plek waar je speelt: je notitie, je worpen en je Roll log worden samen één wereld.

## Wat het doet
Staat er een betaalde skin aan (licentie geldig en Parchment, Arcane of een latere skin gekozen), dan krijgt elke notitie met een Rollwright-worp de sfeer van die skin: achtergrond, letter, kleuren van tekst, koppen, links, citaten en callouts. Alleen binnen het notitievlak. Zonder geldige licentie of met Classic gebeurt er niets, precies zoals nu.

Instelling onder de skin-kiezer, "Skin the note too", drie standen:
- **Notes with rolls** (standaard): alleen notities waarin een `dice:`, `dice+:`, `dice-:` of `dice-mod:` code staat (zonder hoofdletterverschil, zoals `readDiceCode`).
- **All notes**: elke Markdown-notitie.
- **Off**: alleen token en Roll log, zoals nu.

Per notitie kan de gebruiker het met de gewone Obsidian-eigenschap `cssclasses` regelen: `rollwright-world` zet het aan (ook bij Off of zonder worp), `rollwright-plain` zet het uit. Dat kan niet met CSS alleen (Obsidian zet `cssclasses` binnen het notitievlak, dus lager dan onze klasse); de code leest daarom `metadataCache.getFileCache(file)?.frontmatter?.cssclasses` en kiest zelf.

De instelling staat alleen open met een geldige licentie; zonder licentie uitgegrijsd met de uitleg dat het bij de betaalde skins hoort. Een gratis gebruiker die `cssclasses: rollwright-world` zet, ziet terecht niets; dat staat in de hulptekst.

## Wat het bewust niet doet
- Niets buiten het notitievlak van een tabblad in het hoofdvlak: geen notities die in de zijbalk open staan, geen hover-voorbeelden (dat zijn geen bladen), geen zijbalk, geen tabbalk, geen statusbalk, geen weergaven van andere plugins, geen Canvas, PDF of grafiek. De Roll log heeft al zijn eigen wereld per skin.
- Niets aan het bestand: er wordt geen eigenschap in de notitie geschreven.
- Geen netwerk: letters en texturen zitten in `styles.css` (letters als woff2, alleen Latijnse tekens, licentie OFL), geen Google Fonts of plaatjes van buiten. Dat volgt de regels van Obsidian en werkt offline.
- Geen raden uit de tekst. Beeld bij een worp (wolf, val) is een aparte functie (`icon(...)`, game-icons.net CC BY 3.0) en komt los hiervan.

## Hoe het werkt (techniek)
1. **Een klasse op het notitievlak.** De plugin zet `rollwright-world` op `view.containerEl` van elke `MarkdownView` die aan de stand voldoet, en haalt hem weg als dat niet meer zo is. Alleen bladen in het hoofdvlak (`leaf.getRoot() === workspace.rootSplit`, plus losgemaakte vensters), niet in de zijbalken. De titelbalk van de notitie (view-header) valt binnen `containerEl` en hoort er bewust bij: de hele kaart van de notitie wordt de wereld. Niet op `body` en niet op `.markdown-preview-view` (dat element beheert Obsidian zelf voor `cssclasses`). De skin zelf blijft als klasse op `body` staan zoals nu, dus de CSS-regel is altijd `body.rollwright-skin-<skin> .rollwright-world ...`, nooit actief zonder skin-klasse. Zo is "alleen als de skin aan staat" in de CSS zelf geborgd: ook als de klasse ergens blijft hangen, doet hij zonder betaalde skin niets.
2. **Wanneer kijken.** Bij `layout-change`, `active-leaf-change`, `file-open` (ook als in hetzelfde tabblad een andere notitie opent: dan gaat de klasse weg als die notitie niet voldoet), na het wijzigen van de instelling of de licentie, en bij `metadataCache.on("changed")` (geeft de tekst mee en volgt ook `cssclasses`; komt na het bewaren, ongeveer 2 seconden na typen). Een uitgesteld blad (DeferredView, nog zonder bestand) krijgt de klasse zodra het laadt, via dezelfde `layout-change`. De uitkomst wordt per bestand en `mtime` bewaard, zodat niet elke `layout-change` alle bladen opnieuw leest. Alle bladen in alle vensters (ook losgemaakte vensters, net als `applySkin` nu). Bij uitzetten van de plugin gaan alle klassen weg (`onunload`).
3. **Staat er een worp in?** Er is nu geen herkenning voor een hele notitie: `findInlineDice` (src/rollers/inline.ts) werkt per regel en slaat codeblokken en frontmatter niet over, de bewerkweergave gebruikt de `syntaxTree` en de leesweergave zoekt tijdens het tekenen in de DOM. Er komt dus een nieuwe zuivere functie `noteHasRoll(text)` die `findInlineDice` hergebruikt en zelf frontmatter, codeblokken (``` en ~~~), `%% %%` en HTML-commentaar overslaat. Een worp die alleen in een ingesloten notitie (`![[B]]`) staat telt niet voor de notitie eromheen: B is zelf een wereld als je hem opent. De bronmodus krijgt de sfeer ook (zelfde notitie), al worden worpen daar niet getekend. Eén functie, zuiver en met unittests, in een eigen bestand `src/ui/note-world.ts` (main.ts zit op 357 regels, dus de logica komt daar niet bij).
4. **Thema's.** De skin-CSS zet binnen `.rollwright-world` alleen de gewone variabelen van Obsidian plus één achtergrond op `.view-content`. Let op: een variabele die met `var()` is opgebouwd wordt al op `body` uitgerekend, en lagere elementen erven die uitkomst. Dus `--font-text-theme` of `--text-accent` lager zetten verandert de afgeleide variabelen niet. De skin zet daarom elke variabele die het notitievlak gebruikt zelf opnieuw: `--font-text` (en `--font-text-theme`), `--background-primary`, `--background-secondary`, `--text-normal`, `--text-muted`, `--text-faint`, `--text-accent`, `--text-accent-hover`, `--h1-font` tot `--h6-font`, `--h1-color` tot `--h6-color`, `--link-color`, `--link-unresolved-color`, `--link-external-color`, `--tag-color`, `--tag-background`, `--bold-color`, `--italic-color`, `--hr-color`, `--list-marker-color`, `--checkbox-color`, `--blockquote-border-color`, `--table-border-color`, `--code-background`, `--text-selection`, `--caret-color` en de callout-kleuren. Een lijst met deze namen komt als test (alle namen gezet per skin). De lettertype-instelling van de gebruiker (`--font-text-override`) wint niet binnen een wereld: de letter is juist de skin. Wie dat niet wil zet de stand op Off. Omdat variabelen alleen naar binnen doorwerken, blijft de rest van Obsidian in het thema van de gebruiker. Thema's die de variabelen volgen (de meeste) nemen het vanzelf over. Thema's die kleuren vast op `.markdown-preview-view` zetten kunnen er doorheen komen; dat meten we in het standaardthema van Obsidian (dat zet sommige variabelen direct op `.markdown-rendered`) en de vier thema's van de e2e (Minimal, AnuPpuccin, Things, Blue Topaz) en lossen we per geval op, zonder `!important`.
5. **Licht en donker.** Een wereld is een wereld: perkament blijft licht, ook in een donker thema. Dan moet de skin wel de volledige set tekstkleuren, selectie en cursor zetten, anders krijg je lichte tekst op licht perkament. Daan beslist per skin of er een lichte en een donkere variant komt; het mechaniek ondersteunt beide (`.theme-dark .rollwright-world`).
6. **Grootte.** Een plugin levert alleen main.js, manifest.json en styles.css, dus letters staan base64 in `styles.css` (ongeveer 33 procent groter dan het woff2-bestand). Twee letters per skin, alleen Latijnse tekens, richtlijn 120 KB woff2 (±160 KB in styles.css) per skin. Iedereen laadt `styles.css`, ook gratis gebruikers: harde grens 500 KB, met een meting in de build die faalt daarboven (nu 67,6 KB).

## Wanneer het af is (toetsbare eisen, e2e in de echte Obsidian)
1. Classic of geen licentie: nergens `rollwright-world`, berekende achtergrond van de notitie gelijk aan die van het thema.
2. Betaalde skin, stand Notes with rolls: twee notities naast elkaar, alleen die met een worp krijgt de klasse en een andere berekende achtergrond en letter.
3. Worp erbij typen of weghalen: klasse komt of gaat binnen 4 seconden (na het bewaren door Obsidian). Andere notitie in hetzelfde tabblad openen: klasse weg als die niet voldoet.
4. Stand Off: nergens de klasse. Stand All notes: ook de notitie zonder worp.
5. `cssclasses: rollwright-plain` wint van de stand; `rollwright-world` zet hem aan bij Off.
6. Zijbalk, tabbalk, Roll log-paneel en een notitie met worpen die in de zijbalk open staat: berekende achtergrond en letter gelijk aan zonder deze functie.
6b. Losgemaakt venster met een notitie met worpen: krijgt de klasse; dicht en open de plugin: weg.
6c. Uitgesteld blad (bij opstarten niet zichtbaar tabblad): krijgt de klasse zodra je het opent.
7. Plugin uit: nergens nog de klasse, notitie ziet eruit als zonder plugin.
8. Leesweergave en Live Preview allebei, licht en donker, in de vier thema's: plaatjes voor Daan.
9. Unittests voor `noteHasRoll` (worp in tekst; niet in codeblok ``` of ~~~, frontmatter, `%% %%`, HTML-commentaar; `dice-:` en hoofdletters wel), een test dat elke skin de volledige variabelenlijst zet, de groottegrens in de build, en `tsc`, lint en scanner groen. Geen bestaande test gewijzigd.

**Controleur (agent), 9 nov 07:45 UTC:** akkoord met punten. Vijf moet-punten (herkenning bestond niet als geheel, `cssclasses` kan niet met CSS alleen, afgeleide variabelen, `modify` te traag voor 1 seconde, ontbrekende gevallen zoals zijbalk, uitgesteld blad, embed, hover, titelbalk) en vier kan-punten (base64-grootte, instelling voor gratis gebruikers, bewaren per mtime, standaardthema) zijn allemaal hierboven verwerkt.

## Volgorde
1. Mechaniek bouwen met lege skin-CSS (alleen de klasse, niets zichtbaar), eisen 1 tot 7 en 9 groen, controleur. Kan veilig mee in een volgende versie.
2. Daan levert per skin de CSS (zijn richting die Thijs kiest), Olaf neemt die letterlijk over in `src/styles/`.
3. Daan keurt in de echte Obsidian (eis 8), daarna versie, release en de lijst van Thijs.

## Vragen aan Daan
- Standaard "Notes with rolls" of "All notes"? Mijn voorstel is alleen notities met worpen: een spelnotitie wordt een wereld, de werknotities van de gebruiker blijven zoals ze waren. Dat voorkomt ook de klacht "de plugin verft al mijn notities".
- Licht en donker per skin, of één vaste wereld?
- Welke letters (naam en gewicht), zodat ik de grootte vooraf kan meten.

## Stap 1 gebouwd (Olaf, 9 nov 08:50 UTC, main 22cded0)
Mechaniek zonder zichtbare verandering: `src/ui/note-world.ts` (`noteHasRoll`, `wantsWorld`, klasse `NoteWorld`), instelling `noteWorld` (standaard `rolls`), groottegrens 500 KB in de build. E2e in de echte Obsidian groen 22 van 22 specs (run 42587489569, GEZIEN in het log): eis 1 tot 7, ook 6b (los venster) en 6c (uitgesteld blad). 727 unittests, tsc, lint en scanner groen. Controleur akkoord na drie rondes. Geen bestaande test gewijzigd.

**Afwijkingen van het plan, met reden:**
- De rij "Skin the note too" staat alleen in de instellingen met een geldige sleutel (zoals de betaalde skins in de Skin-lijst), niet uitgegrijsd zonder sleutel. Bestaande tests leggen de rijen zonder sleutel vast, en het past bij de skinlijst. Gevolg: een gratis gebruiker leest in de instellingen niet dat een skin de hele notitie kleurt. Dat moet in stap 2 in de skin-voorbeelden of de README (vraag aan Daan en Chris).
- Hoofdvlak: een blad telt als het niet in de zijbalk staat (`getRoot()` is niet left/rightSplit) en `getContainer()` het hoofdvlak of een los venster is. Gemeten: een zijbalkblad heeft ook het hoofdvlak als container, een los blad heeft een eigen root.
- Ook de oude eigenschap `cssclass` (zonder s) telt.
- Geen debounce: per bestand en mtime bewaard, en een gewijzigde notitie wordt alleen bekeken met betaalde skin en als hij open staat.

**Bekende grenzen (zeldzaam, alleen een wereld te veel of te weinig):** een ingesprongen codeblok (4 spaties zonder fence) telt als tekst; een losse backtick kan een `%%`-commentaar maskeren; bladen van andere plugins met het hoofdvlak als container (Hover Editor) zijn niet gemeten.

**Voor stap 2:** de test "elke skin zet de hele variabelenlijst" komt met Daans CSS, met `--callout-blend-mode: normal` erbij (Daan ronde a). Daans regels voor de titelbalk gebruiken `!important` binnen `.rollwright-world`; de scanner van Obsidian waarschuwt daarvoor, dat bekijk ik bij het overnemen.
