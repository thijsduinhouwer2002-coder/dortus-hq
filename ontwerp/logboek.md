# Logboek van Daan (ontwerper)

Alleen aanvullen. Per run: datum, wat bekeken (met run-nummer), wat gevonden, wat besloten.

## 7 nov 2026, run 1 (±08:23 tot 09:05)

- **Bekeken:** Rollwright 0.2.0 (main afc189a). Eerst de bestaande plaatjes in `schermen/rollwright/main` (run 42355012628). Daarna een eigen ontwerptest geschreven: `producten/obsidian-rollwright/e2e/ontwerp/ontwerp.e2e.mjs`, met eigen kluis `e2e/vaults/ontwerp`, eigen config `wdio.ontwerp.conf.mjs` en eigen workflow `.github/workflows/rollwright-ontwerp.yml` (start bij push naar `ontwerp/**`, plaatjes in `schermen/rollwright/ontwerp-<tak>`). Zo raakt mijn test de tests van Olaf niet.
- **Runs:** 42355482509 (rood: thema Blue Topaz heeft een versienummer dat de launcher niet leest, vervangen door Border), 42355788539, 42356165675, 42356482046 (groen, 35 plaatjes).
- **Gevonden:** de worp in de tekst is netjes en past in alle geteste thema's (standaard, Minimal, AnuPpuccin, Things, Border, licht en donker). Rommelig: worpen op secties en koppen, foutmelding zonder oplossing, betaalde skins niet te zien voor het kopen, koopknop zonder prijs, Parchment te fel in donker, ruwe codes in de geschiedenis.
- **Besloten:** `Akkoord: nee` in `producten/obsidian-rollwright/ontwerp.md` met 10 punten op volgorde. Waarom: een eerste indruk met rommelige sectieworpen en een koopknop zonder voorbeeld kost installs en verkopen; de rest is al goed genoeg. Controleur (agent) keek de plaatjes en het oordeel na: eens, vier punten toegevoegd.
- **Lukt nog niet:** het instellingenvenster komt niet in beeld in de test (drie manieren geprobeerd), zweven toont geen tooltip, en het venster laat zich niet kleiner maken. Volgende run: vlak voor de schermafbeelding loggen welke `.modal-container` er zijn, en kijken of iets het venster meteen sluit. Lukt het twee runs niet, dan beoordeel ik de instellingen uit de tekst plus de code en zeg ik dat erbij.
- **Stijl:** eerste versie van `ontwerp/stijl.md` geschreven.

## 7 nov 2026, run 2 (±09:23 tot 10:05)

- **Bekeken:** Rollwright 0.2.0, de instellingen. Eigen spec `e2e/ontwerp/instellingen.e2e.mjs` op tak `ontwerp/rollwright`. Run 42359692659: vier manieren om te openen (tandwiel klikken, Ctrl+komma, `app.setting.open()`, `openTabById`), geen enkel venster in de app, maar na de klik verloor het hoofdvenster de focus. Daaruit: Obsidian 1.15 opent de instellingen in een eigen venster. Run 42359976567: de test wisselt naar dat venster, plaatjes licht, donker, onder en met Tab-focus.
- **Gevonden:** instellingen netjes en echt Obsidian. Rommelig: volgorde in Skins (sleutel voor kopen), "Polar" in de tekst, geen stand van de sleutel, lange naam van de schakelaar, onverklaarde 100.
- **Besloten:** blijft `Akkoord: nee`; punten 11 tot en met 16 erbij, 11 en 12 voor akkoord. Waarom: de koopflow moet lopen in de volgorde waarin je hem gebruikt, anders kost het verkopen; de rest is tekst en klein. Controleur keek na, voegde drie punten toe.
- **Bison & Flex (JetBrains):** eerste oordeel op het skelet (IDE-run 42358929005, vier plaatjes). Iconen goed. `Akkoord: nee` tot er kleuring via de standaardkleuren, een kleurenpagina, de Pro-melding en winkelplaatjes in beeld zijn. Regel in `platformen/jetbrains/taken.md`. Waarom nu al: Jet bouwt het nu, dus nu sturen is goedkoper dan later overdoen.
- **Stijl:** versie 2, hoofdletterregel per platform (JetBrains: Title Case op knoppen en menu's, sentence case in meldingen en links, nagekeken in de richtlijnen van JetBrains).
- **Gezien bij Olaf:** tak `claude/obsidian-2026-11-07-e` werkt aan foutmeldingen en de prijs op de koopknop (mijn punten 2 en 4). Beoordeel ik zodra het op main staat.
- **Daarna (09:55):** Olafs foutmeldingen en koopknop staan op main; ontwerprun 42360408238 op mijn tak (met main erin) toont "Buy for $6". Punten 2 en 4 afgevinkt in `ontwerp.md`. Open voor akkoord: 1, 3, 10, 11, 12.

## 7 nov 2026, run 3 (±10:23 tot 10:50)

- **Bekeken:** Olafs punten 3, 11 en 12 (op main) en punt 1 (tak `claude/obsidian-2026-11-07-h`, nog niet op main). Main en tak h samengevoegd in `ontwerp/rollwright`, ontwerprun 42363837554. Ook Olafs plaatjes van run 42363600604 (blokken, licht en donker).
- **Gevonden:** instellingen goed (voorbeeld van de skins, volgorde, tekst zonder Polar). Blokken goed in lezen, maar in Live Preview lege regels in en onder het blok, door `pre-wrap` van de editor en `display: flex`.
- **Gedaan:** zelf twee CSS-regels (mag volgens mijn rol, alleen uiterlijk): `white-space: normal` en `inline-flex`. Run 42364116651: Live Preview nu bijna gelijk aan lezen. Voor Olaf op tak `ontwerp/blok-css` gezet (tak h plus cc0fb33), run 42364540237.
- **Besloten:** blijft `Akkoord: nee` alleen omdat de oplossing nog niet op main staat; alle eisen zijn in beeld goedgekeurd. Waarom niet nu al ja: akkoord geldt voor de versie die wordt ingediend, en die heb ik nog niet samengevoegd gezien. Punten 17 tot 20 voor na de eerste versie. Koopknop blijft grijs (betaald deel duwt niet). Controleur keek na: eens, voegde 17, 19 en 20 toe.
- **Bison & Flex:** plaatjes van run 42363613266 gezien (calc.y licht, calc.l donker): kleuren via de IDE, rustig en goed leesbaar, ook C in de acties. Richting goed. Nog niet in beeld: kleurenpagina, Pro-melding, winkelplaatjes. Oordeel blijft nee tot die er zijn.
- **10:50:** run 42364540237 op tak `ontwerp/blok-css` (precies tak h plus mijn CSS, cc0fb33) groen; Live Preview van de secties netjes, zonder lege regels. Dit is de versie die op main moet komen.

## 7 nov 2026, run 4 (±11:23 tot 11:50)

- **Bekeken:** Rollwright op main. Olaf voegde tak h samen met een eigen Live Preview-reparatie (zelfde idee als mijn cc0fb33, alleen binnen `.cm-line`). Mijn tak `ontwerp/rollwright` bijgewerkt met main, `styles.css` gelijk aan main gezet zodat ik de echte versie zie, en de geschiedenisstap laat klikken in de leesweergave (tip Olaf). Ontwerprun 42368056384, groen, RUN.txt klopt.
- **Gevonden:** alle eisen voor akkoord goed in beeld (secties, instellingen, geschiedenis). Nog rommelig maar niet nodig voor de eerste versie: Parchment in donker, ruwe code in de geschiedenis, smal paneel.
- **Besloten:** `Akkoord: ja` voor 0.2.0 (main 92b8b23; na 61d44a0 alleen `|line`-logica, geen uiterlijk). Waarom: de gratis ervaring is rustig en past in elk thema, de koopflow is eerlijk; verder wachten levert geen betere eerste indruk op. Controleur eens; hij wees op Parchment in donker als enige wat een koper raakt, dat staat nu als eerste voor 0.2.1. Regel in `platformen/obsidian/taken.md`.
- **Bison & Flex:** beoordeling 2 (IDE-run 42367431455): pluginicoon en kleuren goed, winkelplaatjes nog niet (paneel met `/tmp`-pad, geel lampje). Blijft nee tot kleurenpagina, Pro-melding en winkelplaatjes in beeld zijn. Regel in `platformen/jetbrains/taken.md`.
- **Eigen test slordig:** tooltip bij de foutmelding en scrollen naar onder in de instellingen werken niet in mijn test. Volgende run oplossen.

## 7 nov 2026, run 5 (±12:24 tot 12:50)

- **Lokale kopie:** de oude lokale `main` liep uiteen met GitHub (oude geschiedenis). Niet weggegooid maar bewaard als lokale tak `oud-lokaal-main`, gewerkt op een verse kopie van origin/main.
- **Bekeken Rollwright:** main 38ef6eb (punt 5, 6, 8, 9 van Olaf erin), ontwerprun 42372473217 op `ontwerp/rollwright`. Parchment donker en de fout in gewone letter goed, geschiedenis met nette namen goed. Punt 7 (smal) nog open.
- **Besloten:** `Akkoord: ja` opnieuw gegeven, nu voor main 38ef6eb. Waarom: het uiterlijk veranderde na mijn eerste akkoord, en een akkoord geldt voor wat er echt ingediend wordt.
- **Winkelplaatjes (Olaf, tak p, run 42372342605):** nog geen akkoord. Vooral: je ziet niet wat je typt (W1) en de onderste helft is leeg (W2). Punten W1 tot W8, regel in `platformen/obsidian/taken.md`. Controleur keek alles na: eens, voegde drie dingen toe.
- **Mijn test:** scrollen in de instellingen was nooit kapot (de lijst past in twee schermen). De tooltip komt ook met een echte muis niet in beeld, tweede run op rij: gestopt, tekst staat in het log en is goed.
- **Bison & Flex:** beoordeling 3 (IDE-run 42371684895): structuurweergave goed. Nog nee tot kleurenpagina, Pro-melding en bijgesneden Engelse winkelplaatjes in beeld zijn. Regel in `platformen/jetbrains/taken.md`.

## 7 nov 2026, run 6 (±13:24 tot 13:50)

- **Lokale kopie:** weer uiteengelopen `main`; niets weggegooid, gewerkt op een nieuwe lokale tak `werk` vanaf origin/main en daarvandaan naar main gepusht.
- **Bison & Flex:** beoordeling 4 (main 9d53d64, IDE-run 42376440919). Kleurenpagina goed (punt 2 af), winkelplaatjes `*-calc-y-structuur.png` goed (punt 5 af): Engels, alleen het IDE-venster, factor 2. Klein: geheugenmeter uit (Jet doet dat al op tak g), `calc.l` niet los in de winkel (onderste helft leeg). Besloten: blijft `nee`, nu alleen om de Pro-melding. Waarom: dat is de enige eis die een koper raakt en die ik nog niet zag.
- **Rollwright winkelplaatjes:** tak r (408bf69) had geen run, dus zelf gestart met workflow_dispatch: run 42376919846, groen, RUN.txt klopt. W1 tot W5 goed. Besloten: nog `nee`, alleen om de paarse focusrand rond de buit (winkel-1 en winkel-3) en de placeholder `2d20kh1 + 3` (W8). Waarom: het eerste plaatje beslist over de install, en een rand die op een fout lijkt hoort er niet in; beide zijn één regel. Controleur keek alle plaatjes na: eens, voegde toe dat de rand ook in winkel-3 zit, de buit naast het paneel over twee regels loopt en buit en tolwachter niet in de geschiedenis staan. Regel in `platformen/obsidian/taken.md`.
- **Stijl:** versie 4, twee regels voor winkelplaatjes (geen losse meters, gelijke uitkomsten, focus weg voor de opname).

## 7 nov 2026, run 7 (±14:23 tot 14:45)

- **Lokale kopie:** stond los van een tak; lokale `main` gelijk gezet aan origin/main (niets lokaals verloren, werkboom was schoon).
- **Bison & Flex, beoordeling 5:** Pro-melding in beeld (main d141ce6, IDE-run 42380794961, `licht-` en `donker-pro-melding.png`, RUN.txt klopt). Balloon zelf goed: gewone melding, sentence case, één keer per sessie. Rommelig: de IDE-hint "Cannot find declaration to go to" staat ernaast (leest als fout plus verkooppraatje), en de tekst zegt "across grammar and scanner" terwijl ook springen binnen één bestand Pro is (gezien in `GaNaar.kt`).
- **Besloten:** blijft `Akkoord: nee`, alleen om die twee. Advies aan Jet: springen binnen één bestand gratis, tussen `.l` en `.y` Pro. Waarom: dit is het enige moment waarop een gratis gebruiker over Pro hoort, en een fout of een upsell bij iets basaals kost de goede eerste indruk. Controleur (agent) keek plaatjes en code na: eens, voegde toe dat de hint code afdekt en dat latere klikken alleen een kale foutmelding geven. Regel in `platformen/jetbrains/taken.md`.
- **Rollwright:** main liep door tot 6755a48; na mijn akkoord (38ef6eb) alleen logica van de eerste worp in `src/main.ts`, geen `styles.css` of `src/ui/`. Akkoord bijgewerkt naar main 6755a48 zonder nieuwe ontwerprun. Waarom: een ontwerprun op een logicawijziging laat niets nieuws zien. Winkelplaatjes: W6a en W8 nog niet gedaan door Olaf, niets nieuws te keuren.
- **Stijl:** versie 5, twee regels bij het betaalde deel (geen foutmelding bij een betaalde functie, tekst over Pro zegt precies wat Pro is).
- **Daarna (14:30 tot 14:45):** W6a en W8 zelf gedaan op tak `ontwerp/winkel` (mag: alleen uiterlijk), runs 42381793178 (geschiedenis wiebelde, herhaald groen) en 42382211717 (groen). Tegelijk deed Olaf hetzelfde op main; mijn tak is overbodig, niet samenvoegen. Les: eerst `git log origin/main` kijken vlak voor ik iets van een manager overneem.
- **Rollwright winkelplaatjes, beoordeling 7:** main f1de9de, run 42382269076: geen rand, placeholder goed, buit op één regel, geschiedenis netjes. Besloten: `Akkoord: ja` voor de winkelplaatjes, plugin `ja` voor f1de9de. Waarom: beloofd zonder nieuwe eisen, en het eerste plaatje is nu rustig en duidelijk. Gezien: lezen en Live Preview tonen soms andere buit (de fout op Olafs lijst); dat eerst voor indienen.
- **Bison & Flex, aanvulling:** IDE-run 42381761183 (main 75e5856): hint weg bij de eerste klik, goed. Nog open: latere klikken en de tekst. Blijft nee.
- **Controleur winkelplaatjes (14:50):** eens met de punten; noemde factor 2, leeg onderste derde, ongelijke buit en een cursor in winkel-2 donker. Akkoord blijft ja (README toont ±880 breed; cursor hoort bij W1); factor 2 en gelijke buit voor de volgende ronde plaatjes. Fout van mij: in de opdracht gaf ik de controleur eerst een verkeerde schermen-commit (ab33758); hij vond zelf de goede (25fe62a).

## 7 nov 2026, run 8 (±15:24 tot 15:55)

- **Lokale kopie:** weer los van een tak en uiteengelopen `main`; niets weggegooid, gewerkt vanaf origin/main.
- **README Rollwright (bericht Thijs 15:40):** Olaf had hem al herschreven (main 6a55179). Zelf bijgeschaafd op tak `ontwerp/readme` (f597fe1): Live Preview als eerste plaatje (dit typ je, dit krijg je), plaatjes bijgesneden, "Made by Thijs at Dortus" bovenaan, kopjes in de naslag. Waarom zelf: alleen uiterlijk, en zo hoeft Olaf niet een uur te wachten. Controleur eens. Op main als 5fdd7d1.
- **Besloten:** README en plugin `Akkoord: ja` voor main 5fdd7d1. Waarom: de pagina leest als een winkelpagina en volgt de stijl op alles wat een bezoeker ziet; factor 2 en gelijke uitkomsten zijn voor 0.2.1.
- **Lijstplaatjes 1200x800 van Olaf** (run 42386024452): bekeken, goed genoeg.
- **Stijl versie 6:** supportadres thijs@dortus.com (bericht Thijs 15:45), de regel "Made by Thijs at Dortus", opbouw van een README als winkelpagina.
- **Gezien:** e2e op main c76d271 (run 42385842375) was rood, de run erna op tak z groen. Voor Olaf, niet van mij (alleen README en plaatjes veranderd).

## 7 nov 2026, run 9 (±16:24 tot 17:00)

- **Lokale kopie:** de oude map liep weer uiteen (los van een tak, andere geschiedenis); niets weggegooid, verse kopie van GitHub in een nieuwe map gebruikt.
- **Bison & Flex, beoordeling 6:** schermen van IDE-run 42390272274 (tak `-l` 8be8190, in main 61d663a). Alleen de balloon bij de eerste klik, daarna een korte hint zonder fout, tekst klopt nu met het gedrag (binnen één bestand gratis), structuur toont calc.l. Uiterlijk goedgekeurd zonder nieuwe eisen.
- **Besloten:** totaal blijft `Akkoord: nee`, alleen om Ctrl+zweven (verkoopmelding zonder actie, Jets eigen fout) en de link van "Start free trial". Waarom: allebei raken wat een gebruiker meemaakt bij het betaalde deel, en dat mag niet duwen. Controleur (agent) eens, voegde toe dat ook de hint niet bij zweven mag komen. Regel in `platformen/jetbrains/taken.md`.
- **Rollwright:** na mijn akkoord (5fdd7d1) alleen `showIfNewest` (logica) en e2e. Akkoord bijgewerkt naar main 61388d1 zonder ontwerprun. Waarom: niets aan uiterlijk veranderd. Olaf zit op de wiebelende geschiedenistest (tak zc, alleen e2e), niets voor mij.
- **Stijl:** versie 7, twee regels bij het betaalde deel (melding alleen na een bewuste actie; een trial-knop gaat in één stap naar de proef). Waarom: beide kwamen uit Bison & Flex en gelden ook voor latere producten.
- **Gezien 16:35:** Bison & Flex IDE-run 42391151643 op main 61d663a groen, schermen gelijk aan tak `-l`. Rollwright e2e op main de68a79 (run 42391376336) rood en op dd0975f groen; ik veranderde alleen md-bestanden, dus dit is de wiebelende geschiedenistest op Olafs lijst.

## 7 nov 2026, run 10 (±17:24 tot 17:45)

- **Lokale kopie:** weer los van een tak; lokale `main` opnieuw gezet op origin/main (werkboom schoon, niets verloren).
- **Bison & Flex, beoordeling 7:** schermen van IDE-run 42394756687 (tak `-m` 0f28fc4, in main 7732165). Ctrl+zweven geeft geen balloon en geen hint meer, vóór en na de eerste Ctrl+B (GEZIEN in het log, licht en donker). "Start free trial" opent Help > Register met PBISONFLEX. Uiterlijk gelijk aan beoordeling 6.
- **Besloten:** `Akkoord: ja` voor main 7732165. Waarom: dit waren de laatste twee punten en ik beloofde in beoordeling 6 akkoord zonder nieuwe eisen. Wat nog gebouwd wordt (eis 7 meldingen, hernoemen) bekijk ik voor indienen. Controleur (agent) eens, geen moet-punten. Regel in `platformen/jetbrains/taken.md`.
- **Rollwright:** na 61388d1 alleen e2e-tests (klikWorp-hulp, geschiedenistest), niets aan `styles.css`, `src/` of README. Akkoord blijft staan voor de plugin; geen ontwerprun nodig. Olaf wacht op Thijs voor uitbrengen (veiligheidscontrole), niets voor mij.
- **Gezien 17:32:** Bison & Flex IDE-run 42395989193 op main 7732165 groen, schermen gelijk aan tak `-m`. Rollwright akkoord bijgewerkt naar main d200717 (alleen e2e veranderd). Verder niets te keuren; run afgesloten (regel 0c).

## 7 nov 2026, run 11 (±18:24 tot 18:52)

- **Lokale kopie:** weer los van een tak; lokale `main` opnieuw gezet op origin/main (werkboom schoon, niets verloren).
- **Bison & Flex, beoordeling 8 (vooruitblik):** Jet bouwt hernoemen en alle plekken vinden op tak `-n` (25c7c8f), nog zonder schermen. Code gelezen: de eerste geblokkeerde Shift+F6 toont een balloon over "Go to declaration", de hint zegt niet waarom er niets hernoemd is, en vanuit de structuurweergave gebeurt de tweede keer niets. Besloten: nu al opschrijven in plaats van wachten op schermen. Waarom: Jet kan het dan meenemen voor hij de IDE-test schrijft, dat scheelt een ronde. Akkoord voor main 7732165 blijft staan (dit zit nog niet op main).
- **Controleur (agent):** eens, vond drie moet-punten erbij (onterechte melding tijdens indexeren, zelf nagezien in `Koppeling.kt` regel 100; gedeelde vlag met ga-naar; mogelijk IDE-fout bij Shift+F6 in calc.l, GOK) en een fout van mij: er is geen hernoemen in de editor zelf, alleen het venster. Verwerkt in beoordeling 8 en de regel in `platformen/jetbrains/taken.md`.
- **Rollwright:** main be257c3 heeft na mijn akkoord alleen een lekreparatie in `live-preview.ts` (geen verschil in beeld) en tests. Akkoord bijgewerkt naar be257c3 zonder ontwerprun. Olafs tak `zh` (zoeken in de instellingen, Obsidian 1.13) is nog rood (run 42401067049, zoekveld niet gevonden), `zoek-5-tab.png` toont nog geen instellingen. Niets te keuren; bekijk ik als hij groen is.

## 7 nov 2026, run 12 (±22:23 tot 23:00)

- **Bericht Thijs 22:10 (belangrijk):** de lat is omhoog, "netjes" is niet genoeg. Rol en regels opnieuw gelezen.
- **Besloten:** Rollwright `Akkoord: nee` voor aanmelden en 0.3.0. Waarom: het heeft geen eigen gezicht en geen gevoel bij een klik; mijn eerdere `ja` mat de ondergrens. 0.2.0 blijft uit staan (werkt, geen fouten).
- **Gemaakt:** `producten/obsidian-rollwright/ontwerp-v2.md` (token met d20, rollen, crit goud, fumble rood, logboek, skins, voorbeeldnotitie, lijstplaatjes en GIF, klussen voor Olaf). CSS-proef, voorbeeldnotitie "The Rusty Flagon" en ontwerptest `e2e/ontwerp/v2.e2e.mjs` op tak `ontwerp/rollwright-v2` (da3b9bd). Waarom zelf bouwen: alleen uiterlijk, en met echte plaatjes is het voorstel te keuren in plaats van te geloven.
- **Bekeken:** runs 42420718712 (geen map voor schermen), 42420964772 (crit niet gezet: de verborgen Live Preview-kopie werd gemarkeerd), 42421335321 (zelfde), 42421672346 (goed). In de laatste: token, crit, fumble, tuimelen in 8 keer vertraging, logboek, vier thema's en twee skins GEZIEN. Instellingen kwamen niet in beeld.
- **Controleur (agent):** eens met de richting, "nog een gekleurde pil". Overgenomen: stempel NAT 20 / NAT 1, vonk pas na het landen (zelf gerepareerd), Arcane licht en olijfgoud in donker zijn mijn werk voor de volgende ronde, tabeluitkomsten lichter, klussen scherper. Fout van mij: ik schreef "overal leesbaar" terwijl Arcane licht dat niet was.
- **Stijl versie 8:** nieuw gevoel in één zin, deel "Eigen gezicht" (themakleuren met color-mix, eigen teken mag, korte bewegingen alleen na een klik), eerste lijstplaatje is een poster, GIF in de README, nieuwe voorbeelden.
- **Volgende run:** proef opnieuw draaien (vonk, ring, Arcane licht, goud in donker, instellingen in beeld), daarna wachten op Olafs bouw voor lijstplaatjes en GIF.

## 8 nov 2026, run 13 (±00:23 tot 00:55; klok van de omgeving 23:23 tot 23:55 UTC 7 nov)

- **Lokale kopie:** de oude map was ondiep en liep uiteen; verse kopie in een nieuwe map, niets weggegooid.
- **Olafs bouw gezien:** klus 1, 2, 2b, 3, 3b op tak `claude/obsidian-2026-11-08-a` (run 42425105889 groen), inmiddels op main.
- **Gemaakt:** tak `ontwerp/rollwright-v2b` boven op Olafs bouw: ontwerptest met echte crit en fumble (Math.random in de test vastgezet), instellingen in hun eigen venster in beeld, CSS ronde 2 tot 4. Waarom op zijn bouw: nu de klassen echt zijn, keur ik wat de gebruiker straks krijgt in plaats van een nabootsing.
- **Bekeken:** runs 42425319203, 42425823375, 42426336351 (alle groen). Goud warm in donker, Arcane licht leest, klap en golf bij een crit, dreun bij een fumble, stempel zonder lege plek, logboekkaarten in goud en rood, tabeluitkomsten als tekst. Skin-tegels kaal.
- **Controleur (agent):** vond dat mijn grijze fase in ronde 3 de crit juist verklapte en uitgeschakeld leek (klopt, weggehaald), dat de gewone worp niet in beeld kwam (test rolde "Initiative", maar dat woord staat buiten het token; nu "Hit"), dat het landen een echte klap nodig had (gebouwd), khaki goud in donker (rijker gemaakt), paarse namen op gouden kaarten (aangepast), tabeluitkomsten nog als pil (pil weg), tooltip over een token (muis weg). Overgenomen: alles.
- **Besloten:** akkoord blijft `nee`. Waarom: het token haalt nu de lat, maar logboek, skin-tegels, voorbeeldnotitie en doortellen nog niet. Nieuwe klussen 0, 2c, 2d en een scherpere 7 bij Olaf (taken.md en ontwerp-v2.md).
- **Stijl versie 9:** een bijzonder moment komt pas als de uitkomst er is, nooit eerder; tekstuitkomsten rustiger dan getallen; de meeste toppers op Obsidian hebben een kale README met één schermafbeelding, dus een poster en een GIF vallen op.

## 8 nov 2026, run 14 (klok van de omgeving 00:25 tot ±00:50 UTC)

- **Lokale kopie:** weer ondiep en uiteengelopen; gewerkt op een eigen lokale tak vanaf origin/main, niets weggegooid.
- **Bison & Flex, beoordeling 9:** schermen van IDE-run 42427906937 (tak `-o` f1a1f06, op main c0562da). Hernoemen goed (balloon, hint, scanner, vensters). Klein: balloon in de structuurweergave onder de knoop. Antwoord op Jets vraag over de nieuwe lat: het eigen gezicht zit in icoon, poster en meldingsicoon, niet in de editorkleuren. Waarom: een programmeur kiest zijn eigen kleurschema.
- **Besloten:** Bison & Flex `Akkoord: nee` voor indienen tot poster, nieuw icoon, eigen balloonicoon en een kortere balloontekst er zijn. Waarom: de nieuwe lat; zonder eigen gezicht verdwijnt het tussen de andere plugins. Poster en icoon zelf gemaakt (`ontwerp/bison-flex/`), zodat Jet alleen hoeft te kopiëren.
- **Controleur (agent):** vond dat de poster vooral Pro toont terwijl Pro alleen klein onderaan stond, dat "checks free" niet klopte, dat de Pro-balloon wordt afgekapt bij "Try it free..." (had ik gemist), en dat het 13px-icoon niet leest. Alles overgenomen: PRO-label, voetregel groter en juist, 16px-icoon met pijl, Mac-stippen weg, punt 5 bij Jet.
- **Rollwright ronde 5:** tak `ontwerp/rollwright-v2c` = main ba2fcd5 plus mijn CSS van ronde 2 tot 4; run 42430360190 groen, plaatjes gelijk aan ronde 4, dus klus 0 ligt klaar voor Olaf. Doortellen gemeten met een tijdlijn in het log: de eerste vier getallen vallen in de tijd dat het vakje nog onzichtbaar is, het echte getal staat er 200 ms voor het landen. Nieuwe klus 4b (tellen van ±140 tot ±500 ms). Goud verschijnt bij een crit op 30 ms, dus klus 2d eerst. Controleur eens, twee aanvullingen overgenomen. Fout van mij: de plaatjesreeks ving een verborgen kopie; volgende keer volle schermen.
- **Stijl versie 10:** gezicht van een programmeertool, icoon toetsen op ware grootte, Pro zichtbaar op de poster, poster van echte schermen.
- **Volgende run:** Olafs klussen 0, 2d, 4b bekijken als ze er zijn (volle schermen, ook Live Preview); Jets icoon en balloon; daarna lijstplaatjes en GIF voor Rollwright.

## 8 nov 2026, run 15 (klok van de omgeving 01:23 tot ±02:00 UTC)

- **Lokale kopie:** lokale `main` liep weer uiteen (andere geschiedenis); gewerkt op eigen lokale takken vanaf origin/main, niets weggegooid.
- **Rollwright ronde 6:** tak `ontwerp/rollwright-v2d` (main 5fc217d met Olafs 2c, 2d, 4b, plus alleen mijn test). `klik()` bootst niets meer na; nieuwe stap meet een tijdlijn op gewone snelheid met volle schermen in lezen en Live Preview. Run 42434318370 groen. GEZIEN: goud en rood pas op 463 ms, tellen van 143 tot 509 ms, bewegingen herstarten. Gevonden: ±46 ms een gouden token met een verkeerd getal (`v2-40`, goud met "1"), nieuwe klus 4c bij Olaf. Eerste run (42434225006, op d1f6809 zonder 4b) laat ik liggen.
- **Controleur (agent):** eens; 4c moet in één tik (setTimeouts lopen uit), en de regel springt bij het landen omdat de stempel het token breder maakt (zelf nagezien, `v2-47` tegen `v2-48`). Besloten: stempel in de tekst wordt een sticker op de hoek, alleen CSS, bouw ik zelf volgende run. Waarom zelf: mijn CSS, en Olaf zit op 4c en 5.
- **Bison & Flex, beoordeling 10:** schermen van IDE-run 42432516728 (tak `-a` 0cd70b8). Icoon (gelijk aan mijn bestand), eigen Pro-icoon, Pro-tekst op twee regels, hint onder de knoop: af. Besloten: `Akkoord: ja` voor wat zichtbaar is; indienen pas na de schermen van eis 7. Waarom: dat is het laatste zichtbare stuk van 1.0. Controleur eens.
- **Blender-gewrichten:** eerste reactie op Brams ontwerp v1 (geen oordeel, nog niets te zien). Cut Flex heeft al 15 gewrichtsvormen voor figuren (DERDEN, hun pagina), dus het onderscheid moet "zie voor het printen of het klikt en hoe ver het buigt" worden: passingkleur als hart, beweegproef onderzoeken, paneel in drie stappen.
- **Volgende run:** stempel als sticker en klap vanuit links (CSS, eigen tak), spellingscontrole uit in de ontwerpkluis; daarna Olafs 4c en 5 bekijken.

## 8 nov 2026, run 16 (klok van de omgeving 02:24 tot ±02:55 UTC)

- **Lokale kopie:** lokale `main` liep weer uiteen; gewerkt op eigen lokale takken vanaf origin/main, niets weggegooid.
- **Bison & Flex, beoordeling 11:** schermen `meldingen` en `meldingen-oplossing` van IDE-run 42437187439 (tak `-b` 8c0efc0, op main d9973fa), licht en donker. Ongedefinieerd als gewone waarschuwing, ongebruikt grijs, verder geen markering in calc.y; teksten in de code kort en in de woorden van de IDE. Het Alt+Enter-menu is een zwart vlak op het scherm (GOK: foto te vroeg), tekst daarom op de code en `OplossingenTest` gekeurd.
- **Besloten:** Bison & Flex `Akkoord: ja` voor indienen van 1.0. Waarom: dit was het laatste zichtbare stuk dat ik in beoordeling 10 noemde, en ik beloofde daarna geen nieuwe eisen. Controleur (agent) eens, geen moet-punten; kan-punten (calc.l in beeld met Pro, schuifbalk, menu niet zwart) bij Jet.
- **Fout van mij:** ik schreef eerst 02:45 als tijd terwijl de klok 02:27 zei; verbeterd in 3c70964.
- **Rollwright ronde 7:** tak `ontwerp/rollwright-v2e` (main d9973fa plus alleen CSS en mijn test). Stempel als sticker op de rechterbovenhoek, vonk naar links, klap vanuit links, spellingscontrole uit. Runs 42438770074 en 42439336973 groen. GEZIEN: regel springt niet meer (breedte en bovenkant voor en na gelijk in het log), "Saving throw" niet meer afgedekt. Waarom zelf: alleen CSS, en Olaf zat op klus 6.
- **Controleur (agent):** eens dat het mooi en eigen is; twee moet-punten: sticker raakte in donkere thema's de bovenkant van de 20, en "NAT 20" leest op ware grootte maar net. Beide verwerkt in ronde 7c (9098cde, 0.6em, hoger). Kan-punten: token aan het eind van een regel en tegen de rechterrand testen; MIN in Arcane donker valt weinig op.
- **Klus 8 bij Olaf:** blok "Ronde 7" overnemen.
- **Gezien 02:55:** ronde 7c (run 42439969019): getal vrij in Border donker en licht, NAT 20 leest op ware grootte.
- **Volgende run:** token aan de rechterrand testen; als Olaf klus 8 heeft gedaan, de lijstplaatjes (poster) en de GIF maken op main.

## 8 nov 2026, run 17 (klok van de omgeving 03:24 tot ±03:55 UTC)

- **Lokale kopie:** lokale `main` liep weer uiteen; gewerkt op een eigen lokale tak vanaf origin/main, niets weggegooid.
- **Olaf klaar met klus 0 tot 8** (main 39653f2). Mijn eerste tak `ontwerp/rollwright-v2f` lag op de oude main; overgestapt naar `ontwerp/rollwright-v2g` op zijn bouw. Waarom: keuren wat de gebruiker krijgt.
- **Rollwright ronde 8:** nieuwe ontwerptest `ronde8.e2e.mjs` (leeg logboek, knop, voorbeeldnotitie, logboek met kopjes, skin-tegels). Runs 42442820040, 42443312533, 42443792945 groen. Voorbeeldnotitie en kopjes goed. Gevonden: tabelzin in het logboek groot en vet met een formule van één letter breed (kapot), kaal leeg logboek, skin-tegels die alle drie dezelfde gouden crit tonen. Alle drie met CSS opgelost en gezien; klus 9 bij Olaf (klasse voor tekstuitkomsten, CSS overnemen). Smal venster lukte niet: `setWindowSize` werkt niet in deze Obsidian.
- **Lijstplaatje en GIF versie 1** in `ontwerp/rollwright/`: poster van echte schermen (notitie in donker, NAT 20 op zoom 3 uitvergroot) en een GIF van drie klikken op echte snelheid (opnametest `reclame.e2e.mjs`, runs 42442883775 tot 42443739902). Fout van mij: na de opname op zoom 3 stond de notitie verschoven, waardoor één GIF-opname mislukte; nu begint de GIF bovenaan. Handig gevonden: de tak `schermen` bewaart elke run in zijn geschiedenis, dus met `git archive <commit>` haal ik ook een overschreven run terug.
- **Controleur (agent):** poster haalt de lat; voorbeeldnotitie ja; leeg logboek, skin-tegels en GIF nog niet. Overgenomen: voetregel noemt de $6, "popular themes" in plaats van "every theme", sticker in de tegel hoger, tabeluitkomst getest. Niet overgenomen: poster recht zetten (zie stijl versie 12).
- **Besloten:** akkoord blijft `nee`. Waarom: klus 9 en mijn open punten (tegels groter, GIF met muispijl en langer op de NAT 20, statusbalk uit de plaatjes) moeten eerst; daarna gaan poster, GIF en README naar de lijst van Thijs.
- **Volgende run:** skin-tegels groter, GIF versie 2, de overige lijstplaatjes (dit typ je, logboek ernaast, drie skins), README-voorstel; dan lijst Thijs.
- **Gezien 03:55:** ronde 8c (run 42444319338): skin-tegels in drie kolommen en groter, sticker vrij. GIF versie 2 met muispijl en 3,2 s rust op de NAT 20 staat in `ontwerp/rollwright/demo.gif`.
