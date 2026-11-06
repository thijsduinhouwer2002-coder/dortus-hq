# Rollwright: wat nog open staat

Stand: 6 nov 2026, versie 0.1.0. Geschreven door de bouwer. Bijgewerkt na de reparaties L2 tot L6 en L9.

## Niet in Obsidian getest

Hier draait geen Obsidian. De rekenkern, de rollers, de licentiecontrole en de import hebben tests. Van de pluginlaag is `src/main.ts` getest met een zelfgeschreven nep-Obsidian (`tests/obsidian-stub.ts`): dat bewijst de samenhang, niet dat het in de echte app werkt. De schermcode in `src/ui/` (widget, Live Preview, lezen, zijpaneel, instellingen, venster) is alleen door `tsc`, de build en lint gegaan en is nooit uitgevoerd. Iemand moet dit met de hand nalopen op de laatste Obsidian, op desktop en op telefoon:

1. De plugin laadt zonder fout in de console en is uit te zetten zonder restanten.
2. `` `dice: 2d6` `` in lezen en in Live Preview: uitkomst, tooltip, klik rolt opnieuw.
3. Live Preview: de cursor op de code toont de bron, de cursor eraf toont de uitkomst. Typen elders en scrollen laten de uitkomst staan. Geen uitkomst in een codeblok. De controle op codeblokken zoekt op de naam "codeblock" in de syntaxboom: dat is een aanname.
4. Dezelfde uitkomst in lezen en Live Preview op dezelfde plek. Regels toevoegen boven een worp geeft een nieuwe worp: dat is bekend gedrag van de sleutel met regelnummer.
5. Vlaggen `|nodice`, `|form`, `|avg`, `|none`, `|text(x)`.
6. Kapotte formule: rood onderstreept, reden in de tooltip.
7. Tabel, lookup, geneste cel, lijst, sectie, regel, tag op echte notities. Vooral kijken of een uitkomst met meerdere alinea's er goed uitziet in de regel. Ook: een dobbelcode in een tabelcel van de notitie zelf (krijgt die een eigen uitkomst per cel), en een kolom met een vlagnaam zoals Round.
8. Tags uit frontmatter en uit de tekst, ook geneste tags.
9. Zijpaneel: opent, toont bronnotitie, klik op bron opent de notitie, opnieuw rollen, wissen. Bewaard na herstart.
10. Instellingen: alles opslaan, formule met naam gebruiken in een worp.
11. Import met een echte `data.json` van Dice Roller.
12. Skins: de betaalde zijn niet kiesbaar zonder sleutel, wel met sleutel. Ook in een los venster. Kleuren in licht en donker thema.
13. Op iOS laden, in verband met reguliere expressies en de API.

Lint geeft 0 fouten en 1 waarschuwing: `RollwrightSettingTab` heeft geen `getSettingDefinitions()`, dus de instellingen staan niet in de zoekfunctie van Obsidian 1.13 en later. Dat is een nieuwe functie en valt buiten deze reparaties.

Lint draait met de `recommended`-instelling van `eslint-plugin-obsidianmd`, niet met de aparte scannerinstelling: die staat in de docs van de GitHub-repo van de plugin en die repo mocht ik niet ophalen. De map `tests` valt buiten lint.

Voor uitgave ook: **Review branch** in het dashboard van Obsidian draaien (Run preview scan). Dat kan alleen met het account.

## Betaling (eis van de eigenaar: klaarzetten, niet aanzetten)

- `BUY_URL` in `src/pro/license.ts` is leeg. Daardoor is de koopknop verborgen. Betaling is nog niet geregeld. Dat is een stap voor Thijs (geld en account).
- **De licentiecontrole beschermt niets.** Het is een controlesom in openbare code. Iedereen die de code leest kan een geldige sleutel maken. Dat past bij "eenvoudig en zonder druk", maar voor echte verkoop is het te zwak. Advies: voor de start van de verkoop vervangen door sleutels met een digitale handtekening (alleen de publieke sleutel in de plugin). De geheime sleutel mag niet in de repo. Daarom is dat nu niet gedaan.
- Er bestaat nu geen enkele verkochte of uitgegeven sleutel, en geen hulpmiddel om ze uit te geven. Alleen de test maakt er een.
- In het dashboard moet de plugin het label **Optional payments** krijgen, volgens deel 5.2 van het onderzoek. Dat kan alleen met het account.

## Keuzes die ik zelf maakte

De bronnen gaven hier geen uitsluitsel of ze zijn bewust niet gelezen. Het is eigen ontwerp en wijkt misschien af van Dice Roller.

- `d[a,b]` is een bereik met beide grenzen erbij. Drie of meer getallen zijn de vlakken zelf. Het onderzoek waarschuwt dat het grensgedrag in Dice Roller niet is vastgesteld.
- `!` en `r` zonder getal gelden één keer per steen, zoals tabel 4.4 zegt (`{n}` standaard 1).
- Bij meerdere dobbelcondities telt de eerste die klopt.
- Conditie direct na `!` of `r` hoort bij die modifier. Wil je daarna tellen, zet er iets tussen: `1d20r<3s>=15`.
- `#tag` zonder `|+` of `|-` werkt als `|+`.
- `|xy` slaat de eerste kolom over, omdat daar meestal de rijnamen staan.
- Meerdere trekkingen uit een tabel, lijst of sectie kunnen dezelfde uitkomst geven.
- `|text(x)` toont `x: uitkomst`. `|nodice` verbergt het dobbelicoon. De precieze betekenis in Dice Roller heb ik niet vastgesteld.
- Alleen geklikte en getypte worpen komen in de geschiedenis. Anders vult het openen van een notitie de lijst.
- `minAppVersion` is 1.7.2, de hoogste `@since` onder de gebruikte API's in `obsidian.d.ts` (`Workspace.revealLeaf` met belofte). Nagekeken in de typebestanden, niet in een oude Obsidian.

## Niet gebouwd in deze versie

Bewust weggelaten om binnen de tijd een werkend geheel te hebben: `dice+:`, `dice-:`, `dice-mod:`, narratieve dobbelstenen (Genesys), `1dS`, notitievelden als getal, Dataview `dv(...)`, codeblok `dice`, dobbelpaneel met knoppen, 3D-stenen, Ctrl-klik naar de bron, Alt-klik voor het gemiddelde, en de vlaggen `|round`, `|ceil`, `|floor`, `|signed`, `|paren` (die worden geaccepteerd maar doen nog niets). `[[Note#Kop]]` zoekt nog niet op kop en geeft een melding. In secties herkent het eigen blokmodel alleen blokken, geen inline soorten zoals `strong` of `link`: die namen geven "no matching blocks".

## Voor uitgave

Bevindingen van de controleur. Opgelost op tak `claude/obsidian-2026-11-06-c` (6 nov), elk met een eigen test die zonder de reparatie faalde. Nog na te kijken door de controleur.

- L2 (opgelost): `dice: x` zonder backticks in een tabelrij met meer kolommen gaf "Unknown flag" (`src/rollers/run.ts`, `resolveNested` kreeg de samengevoegde cellen). Nu wordt elke cel apart gerold. Test: `tests/l2-cells.test.ts`.
- L3 (opgelost): kolommen met een vlagnaam, zoals Round, werden als vlag opgegeten (`src/rollers/spec.ts`). Nu gaat een kolom van de tabel voor: `|Round` of `|Form` kiest die kolom, en de vlag met die naam geldt dan niet voor die worp. Zonder zo'n kolom blijft het een vlag. Test: `tests/l3-columns.test.ts`. Rest: bij een kolom met de naam "None" toont de widget de eerste keer toch alleen het icoon, omdat de widget de tabel niet leest voor de eerste worp.
- L4 (opgelost): `|avg` meldde exact maar was fout bij niet-lineaire formules, zoals `(1d4)^2` (`src/engine/evaluate.ts`, `averageOf`). Nu is het gemiddelde alleen exact bij optellen, aftrekken, vermenigvuldigen, delen door een vast getal en stenen zonder modifiers met een telling die altijd lukt. Delen door stenen en machten van stenen gaan door de simulatie en krijgen `~`. Tellingen die in een echte worp kunnen mislukken (zoals `1.5d6`) geven nu een melding in plaats van een verzonnen gemiddelde. De traagheid op grote groepen was al weg door het gedeelde budget van L7: gemeten 2 tot 9 ms voor onder meer `1000d6k1` en `1000d1000000u` (GEZIEN, hier in de testomgeving). Wel krijgt zo'n formule weinig steekproeven (bij `1000d6!` maar een paar), dus de schatting is ruw, maar gemarkeerd. Test: `tests/l4-average.test.ts`.
- L5 (opgelost): gelijke sleutel `el:0` voor dobbelcodes in tabelcellen (`src/ui/reading-view.ts`). Nu krijgt elke code zonder bekende regel een eigen nummer. Gevolg: zo'n code rolt opnieuw als de notitie opnieuw getekend wordt, en deelt zijn uitkomst niet met Live Preview. De README-zin "Results stay as they are until you click" is vervangen door wat echt gebeurt: opnieuw rollen bij klik, herstart, regels erboven erbij of eraf, en in tabelcellen bij opnieuw tekenen. Een kleine reparatie die de oude zin waar maakt bestaat niet: de sleutel hangt aan het regelnummer en het geheugen is niet bewaard. Test: `tests/l5-keys.test.ts`. Niet bewezen: dat `getSectionInfo` in Obsidian echt leeg is bij tabelcellen; dat zei de controleur.
- L6 (opgelost), klein:
  - weergave van Infinity (`src/engine/format.ts`, `evaluate.ts`): een groot eindig getal werd bij afronden Infinity; een som van stenen kon overlopen; de som van steekproeven van het gemiddelde ook. Test: `tests/l6-numbers.test.ts`.
  - een leeg instelveld werd 0 (`src/ui/settings.ts`): nu alleen hele getallen vanaf het minimum, via `parseWholeNumber`. Test: `tests/l6-settings.test.ts`. Niet bewezen: het instelscherm zelf, alleen de functie.
  - al open vensters zonder skin (`src/main.ts`): na `onLayoutReady` worden alle vensters met een tabblad meegenomen via `iterateAllLeaves`. Test: in `tests/plugin.test.ts`, met de nep-Obsidian. Niet bewezen in de echte app.
  - traag op tabelregels met 50.000 spaties (`src/rollers/markdown.ts`): de reguliere expressie voor de regel onder de kop is vervangen door een controle per cel. Was ongeveer 0,9 s, nu ruim onder 150 ms. Test: `tests/l6-table-rule.test.ts`.
  - `1D6KH1` werd geweigerd: nu tellen hoofdletters mee in modifiers na een getal of steen. Opgeslagen formules met hoofdletters en cijfers, zoals `K2`, blijven werken. Test: `tests/l6-capitals.test.ts`.
- Voor verkoop: sleutels met een handtekening in plaats van de controlesom.

Herhaald renderen is opgelost in `src/rollers/defuse.ts` plus een controle in `src/ui/reading-view.ts`. Alleen in Obsidian te bewijzen, dus handmatig testen: `dice: [[Zichzelf]]` en `dice: #npc` in een notitie met die tag, ook met `![[Zichzelf]]` in de notitie. Let op: een andere plugin die notities in een uitkomst invoegt (zoals Dataview) is niet gedekt, en of `el.closest` werkt hangt ervan af of Obsidian het element al heeft ingehangen tijdens de post-processor.

## Niet vastgesteld

- De indeling van `data.json` van Dice Roller. Broncode lezen mocht niet, dus de import herkent eenvoudige vormen onder elke sleutel met "formula" in de naam. Tests draaien op een eigen model, niet op een echt bestand. De map `obsidian-dice-roller` komt uit het id in deel 3 van het onderzoek.
- Of de notatie in randgevallen gelijk is aan Dice Roller: niet naast de echte plugin gedraaid.
- Het kleurcontrast van de betaalde skins: niet bekeken.

## Na de herkeuring (6 nov), voor uitgave
- Omzeilen van `defuseRolls` kan nog met html-vormen zoals `dice&#58;` en `d<b>ice</b>:`. Dan hangt het aan `el.closest`, in Obsidian te bewijzen.

## Na herkeuring L7 en L8 (6 nov), voor uitgave
- L9 (opgelost, 6 nov): `src/rollers/defuse.ts:18`, de code-regex liep over blokgrenzen. Een losse backtick eerder (`it`s`) maakte echte code onherkenbaar, en die bleef rollen. Gekozen is niet per blok of regel te paren, maar backticks helemaal niet te paren: een rolbare code begint altijd met `dice:` direct na de backticks (zie `formulaFromCode`), dus elke `dice:` direct na een reeks backticks krijgt het onzichtbare teken. Dat werkt ook bij lijstitems, tabelrijen en koppen, waar een indeling per blok zou falen. Bijwerking: gewone tekst die direct na een sluitende backtick met `dice:` begint, krijgt ook het onzichtbare teken; dat zie je niet. Test: `tests/l9-defuse.test.ts`.

## Na de herkeuring van L2 tot L9 (6 nov, 15:30)
- De controleur vond een nieuw lek in de L9-reparatie: een code over twee regels in een citaat of callout (`> \`` en op de volgende regel `> dice: 1d6\``) werd niet meer onschadelijk gemaakt. Opgelost door ook `>` over te slaan tussen backticks en `dice`, met vijf tests in `tests/l9-defuse.test.ts`.
- Bekend en niet blokkerend: bij een telling die zelden mislukt, zoals `(1d1000-2)d6`, hangt het van de steekproef af of `|avg` een melding of een schatting geeft. `(-8)^(1/3)` geeft de melding "too large to show" (was er al).
