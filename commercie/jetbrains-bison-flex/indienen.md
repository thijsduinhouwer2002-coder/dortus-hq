# Bison & Flex (JetBrains): alles om in te dienen, klaar om te plakken

Door Chris, 8 nov 2026 (run 5). Eén plek met de definitieve teksten en het invulblad, zodat Jet en Thijs niet door vier bijwerkingen in `winkeltekst.md` hoeven te zoeken. Dit bestand gaat voor waar het afwijkt van `winkeltekst.md`. De andere stukken blijven staan als onderbouwing.

**Bijwerking 8 nov, ±07:00 (Chris, run 7), gaat voor de stand hieronder:**
- Prijs is besloten door Jet: $19 / $49 per jaar, $1,90 / $4,90 per maand, proef 30 dagen, onderwijs en open bron gratis, geen startupkorting (`organisatie/besluiten.md`, 8 nov). Dat is precies wat in deel 3 staat; het invulblad kan zo blijven.
- Daan gaf `Akkoord: ja` (8 nov 06:29, beoordeling 12) voor de naam `Bison & Flex` en de winkeltekst op tak `claude/jetbrains-2026-11-08-e` (0e667972). Die tekst noemt CLion al ("in CLion and other JetBrains IDEs"), want de CLion-test is groen (run 42450473711). De zin over CLion in deel 1 is dus verwerkt. Op main heet de plugin nog `Bison & Flex Support` (GEZIEN): tak `-e` moet nog naar main vóór de build voor de upload.
- `release-date` staat nu op `20261108` (Plugin Verifier weigert meer dan 5 dagen vooruit). Op de dag van de upload opnieuw zetten, zoals Jet al noteerde.
- Plaatjes: 1 tot 3 klaar en op lijst-thijs voor zijn ja; 4 en 5 wachten op schermen met Pro aan. Indienen mag met 1 tot 3, maar Hidden pas uit als 4 en 5 er zijn (Daan).
- https://dortus.com/bison-flex/ bijgewerkt (GEZIEN live, 8 nov): Pro-meldingen erbij, CLion, "2025.2 and later" (sinceBuild 252), geplande prijs met voorbehoud ("Planned price ... The price on JetBrains Marketplace is the one that counts"), en de privacyzin noemt nu ook de snelle oplossing als iets dat een bestand verandert.
- Nog te controleren vóór de upload (Jet): geen `until-build` in de gebouwde `plugin.xml`, anders klopt "and later" op de site niet.

**Stand (GEZIEN 8 nov):** Daan gaf `Akkoord: ja` voor indienen van 1.0 op main d9973fa (beoordeling 11). Eis 7 (meldingen) zit erin en is Pro. CLion zit nog niet in de IDE-test. `plugin.xml` heet nog `Bison & Flex Support` met de oude tekst "Early version: file types and syntax highlighting". Die tekst klopt niet meer met wat de plugin doet en moet vóór het uploaden vervangen worden (deel 1).

**Wat nog open is vóór het indienen (niet van mij):**
- Prijsbesluit van Jet (voorstel in `prijs.md`: $19 / $49 per jaar). Het invulblad in deel 3 gebruikt mijn voorstel; neemt Jet iets anders, dan alleen de twee bedragen aanpassen.
- Thijs leest de EULA (lijst-thijs, 7 nov 23:55). Pas daarna is https://dortus.com/bison-flex/eula.html de License-link.
- `release-date` in de `product-descriptor` staat op `20261215`. Volgens JetBrains is het product pas vanaf die datum te koop ("will be available for purchase starting ...", DERDEN, schermafbeelding van het formulier op [release-plugin](https://plugins.jetbrains.com/docs/marketplace/release-plugin.html)) en hangen de fallback-licentie en de looptijd van licenties eraan (DERDEN, [add-required-parameters](https://plugins.jetbrains.com/docs/marketplace/add-required-parameters.html)). Zet hem dus op de lanceerdag of eerder, niet later, anders kan niemand kopen tot 15 december (en de tussenstap is 6 december). **Hij moet goed staan in de build die Thijs uploadt en blijft daarna gelijk voor alle 2026.1.x:** een versie met een andere `release-date` of `release-version` geldt als nieuwe hoofdversie en zet lopende proeven opnieuw (DERDEN, add-required-parameters). Later rechtzetten is dus geen uitweg (controleur). Jet weet dit al (`architectuur.md`, regel 54); ik zet het hier zodat het niet vergeten wordt.
- Versie en `release-version` kloppen (2026.1.0 en 20261, GEZIEN in `build.gradle.kts` en `plugin.xml`), zoals JetBrains vraagt.

## 1. In `plugin.xml` (Jet)

### Naam
```
Bison & Flex
```
12 tekens. Waarom: hoogstens 20 tekens aanbevolen, geen "Support", geen `/` als scheiding (DERDEN, [best practices for listing](https://plugins.jetbrains.com/docs/marketplace/best-practices-for-listing.html)). Advies 7.

### Beschrijving (`<description>`)
De eerste 40 tekens ("Bison/Yacc and Flex/Lex files in the IDE") zijn het kaartje in de zoeklijst. Alles hieronder is gebouwd en in de code nagekeken (zie "Waar elke regel op steunt").

```html
<p>Bison/Yacc and Flex/Lex files in the IDE: highlighting, errors, navigation and rename.
For <code>.y</code>, <code>.yy</code>, <code>.l</code> and <code>.ll</code> files.
Made for C and C++ developers who write parsers and lexers.</p>

<p><b>Free</b></p>
<ul>
  <li>Bison, Yacc, Flex and Lex file types with their own icons</li>
  <li>Highlighting for directives, tokens, rules, start conditions and regular expressions,
      using your color scheme (light, dark and any theme)</li>
  <li>C code in actions highlighted: keywords, strings, comments and
      <code>$$</code>, <code>$1</code>, <code>@1</code></li>
  <li>Syntax errors in the grammar and the scanner</li>
  <li>Folding and a Structure view with rules, tokens and start conditions</li>
  <li>Comment and uncomment with the usual shortcut</li>
  <li>Go to definition, find usages and rename within a file
      (renaming a token your scanner also uses is Pro)</li>
</ul>

<p><b>Pro</b> (free 30-day trial, then a paid license): your grammar and scanner, connected.</p>
<ul>
  <li>Jump from a token in the scanner (<code>.l</code>) to its <code>%token</code>
      in the grammar (<code>.y</code>)</li>
  <li>Find usages and rename tokens across grammar and scanner at once</li>
  <li>Warnings for undefined symbols and start conditions, and for unused rules,
      tokens and start conditions, with a quick fix to remove the unused ones</li>
</ul>

<p>The free features keep working after the trial. No sign-up with us, no telemetry.</p>

<p>Another plugin for <code>.y</code> files installed? Disable it, so the IDE uses this one.</p>

<p>Questions or a bug: <a href="mailto:thijs@dortus.com">thijs@dortus.com</a>.
More at <a href="https://dortus.com/bison-flex/">dortus.com/bison-flex</a>.</p>
```

**CLion:** de tekst zegt "in the IDE" en noemt CLion bewust niet, want de IDE-test draait alleen IntelliJ IDEA Community. Zit CLion in de test en is hij groen, dan mag de tweede zin worden: `For .y, .yy, .l and .ll files in CLion and other JetBrains IDEs.` (CLion in de beschrijving mag, in de naam niet, regel 1.2h).

**Waar elke regel op steunt (GEZIEN in de code, 8 nov, main):**
- Bestandssoorten en iconen: `plugin.xml` (`fileType` voor `y;yy` en `l;ll`), `Bestandssoorten.kt`.
- Kleuren: `Kleuren.kt` en twee kleurenpagina's (`colorSettingsPage`); C-code in acties en `$$`/`$1`/`@1`: `Kleuren.kt` regel 52 en 156, `lexer/Scanner.kt` regel 185.
- Fouten: de parsers in `parser/`. Folding: `Folding.kt`. Structuur: `Structuur.kt` (Bison: "Declarations" met tokens en "Rules"; Flex: "Definitions" met naamdefinities en start-condities, en "Rules", regel 118 tot 154). Hernoemen van een token dat ook in een `.l` staat, is zonder Pro helemaal geblokkeerd, ook binnen het eigen bestand (`pro/ProHernoemen.kt` regel 347 tot 357); daarom de toevoeging tussen haakjes. De posterzin "finally connected" staat nu bij Pro, want die koppeling is Pro, en zonder "finally" (marketingwoorden afgeraden, best practices). Commentaar: `lang.commenter` voor beide talen.
- Binnen één bestand gratis, tussen `.l` en `.y` Pro: `pro/GaNaar.kt`, `psi/Verwijzingen.kt`, `pro/ProHernoemen.kt` (keuze van Jet en Daan).
- Meldingen alleen met Pro: `meldingen/Meldingen.kt` regel 21 en 22 ("Vier inspecties, alleen met Pro"), namen in `plugin.xml`: "Undefined symbol", "Unused rule or token", "Undefined start condition", "Unused start condition". Snelle oplossing alleen op ongebruikt ("Remove unused rule", "Remove unused token", ook start-condities): `meldingen/Oplossingen.kt` en het ontwerp van eis 7.
- Geen telemetrie: EULA artikel 6 en geen netwerkcode buiten de licentiecontrole van JetBrains (`pro/Licentie.kt` gebruikt `LicensingFacade`).

**Niet beloofd** (zit niet in 1.0): haakjes paren, echte C/C++-hulp in acties (alleen kleuren), uitleg van shift/reduce-conflicten, Bison draaien, Flex-naamdefinities als `{DIGIT}`, meldingen voor tokens bij `%define api.token.prefix` of `api.token.constructor` (bewust stil).

### Change notes voor 1.0 (`<change-notes>`)
```html
<p>First release. Bison/Yacc and Flex/Lex file types, highlighting, syntax errors,
folding, Structure view, and go to definition, find usages and rename within a file.
Pro: navigation, find usages and rename of tokens across grammar and scanner,
and warnings for undefined and unused names, with a quick fix to remove unused ones.</p>
```

## 2. Bij het uploaden (Thijs, met Jet zijn stappen op lijst-thijs)
Velden uit het uploadformulier (DERDEN, [uploading-a-new-plugin](https://plugins.jetbrains.com/docs/marketplace/uploading-a-new-plugin.html)):

| Veld | Invullen | Waarom |
|---|---|---|
| License | `https://dortus.com/bison-flex/eula.html` | Eigen EULA is verplicht. Pas na "EULA ok" van Thijs. Kies geen open-bronlicentie: dan vraagt het formulier een link naar de broncode. |
| Tags | `Programming Language`, `Navigation`, `Inspection` | Tags zijn zoekfilters; verkeerde tags schaden de vindbaarheid (DERDEN, zelfde pagina). Alle drie bestaan (GEZIEN, 81 tags via `/api/tags`). `Programming Language` gebruikt ook de bestaande Bison-plugin (GEZIEN 7 nov). Een maximum aantal vond ik niet; lukt drie niet, dan alleen de eerste. |
| Channel | Stable (standaard) | Geen bèta. |
| Hidden | aan bij de eerste upload | Zo kan Thijs Sales Info invullen en de pagina bekijken voordat iemand de plugin ziet (Jet zijn plan). |
| Website (op de pluginpagina, na het uploaden) | `https://dortus.com/bison-flex/` | Productpagina met support, privacy en EULA. |
| Source code | leeg laten | Geen open bron. |

## 3. Invulblad Sales Info (Thijs, na de upload)
Plek: pluginpagina, tab **Sales Info**, knop **Add to Marketplace**. Zie je die knop niet, dan ontbreken de bankgegevens bij Trader Details (DERDEN, [release-plugin](https://plugins.jetbrains.com/docs/marketplace/release-plugin.html)). Velden zoals op de schermafbeelding van JetBrains (DERDEN, `images/sales_details.png` op die pagina; die afbeelding is van 2021, dus het echte formulier kan iets afwijken):

| Veld in het formulier | Invullen | Waarom |
|---|---|---|
| Licensing Type | `Plugin licensing` | De standaardkeuze; onze plugin heeft een eigen productcode (PBISONFLEX). |
| Available Billing Method | **Annual** en **Monthly** allebei aanvinken | Annual is verplicht voor de programma's voor studenten en open bron (DERDEN, zelfde pagina). Monthly verlaagt de drempel na de proef (GOK). |
| Individual Customer Annual Price | `19` | In USD ("Prices must be given in USD", DERDEN, sales_details.png). Voorstel `prijs.md`. |
| Businesses and Organizations Annual Price | `49` | Idem. |
| Allow sales via resellers | aanvinken | Bedrijven kopen software vaak via een vaste wederverkoper; zonder dit vinkje kan dat niet (GOK). De commissie van de wederverkoper gaat van het deel van JetBrains af, niet van het onze; ook dan houdt de maker 85% (DERDEN, [revenue-sharing-and-fees](https://plugins.jetbrains.com/docs/marketplace/revenue-sharing-and-fees.html)). Past bij EULA artikel 4. |

**Maandprijs:** die vul je niet apart in. Met Monthly aan rekent JetBrains: jaarprijs is maandprijs maal 10 (DERDEN, tekst naast de velden op de schermafbeelding). Dus $1,90 en $4,90 per maand, precies het voorstel.

**Discount Community Programs** (onder het formulier). Aanvinken:
- For students and teachers (Free)
- For classroom assistance (Free)
- For training courses, coding schools, and bootcamps (Free)
- For universities and educational organizations (50% Off)
- For former student license holders (40% Off)
- For Open Source projects (Free)
- For non-profit organizations (50% Off)
- For Developer Recognition Program (Free)
- For user groups (Free)

**Niet** aanvinken: For startups (50% Off). Waarom: Bison en Flex worden veel in compilervakken en open-bronprojecten gebruikt (GOK), dus onderwijs en open bron gratis kost weinig en levert reviews en latere zakelijke gebruikers op (`prijs.md`). Startups zijn juist de zakelijke kopers waar het geld vandaan moet komen; $49 per jaar is voor een bedrijf al laag. Klassen en cursussen worden voor plugins nog niet ondersteund, maar aanvinken bewaart de keuze voor later (DERDEN, `images/community_prog.png`). Lijst van de programma's: GEZIEN op die schermafbeelding. Staan de programma's niet in het formulier, mail dan marketplace@jetbrains.com; dat vraagt JetBrains ook om ze aan te zetten (DERDEN, release-plugin).

**Trial Period:** 30 dagen laten staan (standaard; kan ook 7, 10, 14 of uit, en later nog aangepast worden; wie al een proef had, houdt zijn dagen, DERDEN, zelfde pagina). De Pro-balloon (`pro/ProMelding.kt` regel 190 tot 200) en de vier beschrijvingen in `inspectionDescriptions/` zeggen "free to try for 30 days" (GEZIEN), dus niet korter zetten zonder die teksten aan te passen.

**Fallback-licentie:** voorstel was abonnement met fallback (`prijs.md`), en EULA artikel 3 belooft een Fallback Version na 12 maanden betalen. Op de schermafbeelding staat geen keuze hiervoor, en de docs zeggen dat fallback werkt via `release-date` en `release-version` (DERDEN, add-required-parameters). Vraagt het echte formulier wél een keuze, kies dan "with a fallback license", anders klopt de EULA niet.

**Na Submit:** JetBrains beoordeelt binnen twee werkdagen (DERDEN). Velden later wijzigen kan alleen via marketplace@jetbrains.com (DERDEN), dus de bedragen eerst zeker weten. Een kortingsactie kan niet binnen 30 dagen na een prijsverhoging (DERDEN, [special offers](https://plugins.jetbrains.com/docs/marketplace/special-offers.html)); daarom niet laag beginnen om daarna te verhogen.

## 3b. Vooraf nodig en na de goedkeuring
- **Vooraf (Thijs, staat al op lijst-thijs, punt verkoper worden):** Developer Agreement accepteren, Vendor profile met trader status, Trader Details met bankgegevens, uitbetaalvaluta USD of EUR kiezen. Zonder bankgegevens geen knop Add to Marketplace.
- **Links op de pluginpagina (Technical Information):** documentatie `https://dortus.com/bison-flex/`; issue tracker: `mailto:thijs@dortus.com` tot er een openbare plek is. JetBrains raadt deze links aan, ze zijn ook in de IDE te zien (DERDEN, best practices for listing).
- **Na de goedkeuring (Jet, in 2026.1.1):** `pro/Proef.kt` regel 30 heeft als terugval `KOOPPAGINA = "https://plugins.jetbrains.com/"`; dat moet de echte pluginpagina worden zodra de URL bekend is (controleur; stond al als kan-punt bij Jet).

## 4. Plaatjes (Daan en Jet)
Volgorde (zie `winkeltekst.md`, bijwerking run 4): 1. poster, 2. `calc.y` met kleuren en structuur (licht), 3. `calc.l` (donker), 4. hernoemen in beide bestanden, 5. melding ongebruikte regel met de snelle oplossing (nu kan dat: eis 7 zit erin; scherm `meldingen`, of `meldingen-oplossing` als Jet het zwarte menu repareert). Alle plaatjes in één verhouding (advies 9, nog open), minimaal 1200 bij 760 aanbevolen, standaardthema's van de IDE (DERDEN, best practices for listing).

## 5. Nulmeting op de dag van indienen
Bison Language Support: 13.020 downloads (GEZIEN 8 nov via `/api/searchPlugins?search=bison`, gelijk aan 7 nov). Eigen plugin: 0 installs, 0 reviews, 0 verkopen. Dag 7 en dag 30 komen in `cijfers.md`.
