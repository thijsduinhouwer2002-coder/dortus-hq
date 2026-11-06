# Rollwright: wat nog open staat

Stand: 6 nov 2026, versie 0.1.0. Geschreven door de bouwer.

## Niet in Obsidian getest

Hier draait geen Obsidian. De rekenkern, de rollers, de licentiecontrole en de import hebben tests. Van de pluginlaag is `src/main.ts` getest met een zelfgeschreven nep-Obsidian (`tests/obsidian-stub.ts`): dat bewijst de samenhang, niet dat het in de echte app werkt. De schermcode in `src/ui/` (widget, Live Preview, lezen, zijpaneel, instellingen, venster) is alleen door `tsc`, de build en lint gegaan en is nooit uitgevoerd. Iemand moet dit met de hand nalopen op de laatste Obsidian, op desktop en op telefoon:

1. De plugin laadt zonder fout in de console en is uit te zetten zonder restanten.
2. `` `dice: 2d6` `` in lezen en in Live Preview: uitkomst, tooltip, klik rolt opnieuw.
3. Live Preview: de cursor op de code toont de bron, de cursor eraf toont de uitkomst. Typen elders en scrollen laten de uitkomst staan. Geen uitkomst in een codeblok. De controle op codeblokken zoekt op de naam "codeblock" in de syntaxboom: dat is een aanname.
4. Dezelfde uitkomst in lezen en Live Preview op dezelfde plek. Regels toevoegen boven een worp geeft een nieuwe worp: dat is bekend gedrag van de sleutel met regelnummer.
5. Vlaggen `|nodice`, `|form`, `|avg`, `|none`, `|text(x)`.
6. Kapotte formule: rood onderstreept, reden in de tooltip.
7. Tabel, lookup, geneste cel, lijst, sectie, regel, tag op echte notities. Vooral kijken of een uitkomst met meerdere alinea's er goed uitziet in de regel.
8. Tags uit frontmatter en uit de tekst, ook geneste tags.
9. Zijpaneel: opent, toont bronnotitie, klik op bron opent de notitie, opnieuw rollen, wissen. Bewaard na herstart.
10. Instellingen: alles opslaan, formule met naam gebruiken in een worp.
11. Import met een echte `data.json` van Dice Roller.
12. Skins: de betaalde zijn niet kiesbaar zonder sleutel, wel met sleutel. Ook in een los venster. Kleuren in licht en donker thema.
13. Op iOS laden, in verband met reguliere expressies en de API.

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

Bevindingen van de controleur, nog niet opgelost:

- L2: `dice: x` zonder backticks in een tabelrij met meer kolommen geeft "Unknown flag" (`src/rollers/run.ts`, `resolveNested` krijgt de samengevoegde cellen).
- L3: kolommen met een vlagnaam, zoals Round, worden als vlag opgegeten (`src/rollers/spec.ts`).
- L4: `|avg` meldt exact maar is fout bij niet-lineaire formules, zoals `(1d4)^2`, en is traag op grote groepen (`src/engine/evaluate.ts`, `averageOf`).
- L5: gelijke sleutel `el:0` voor dobbelcodes in tabelcellen (`src/ui/reading-view.ts`). De README-zin "Results stay as they are until you click" klopt niet na een regel erboven of na een herstart (`src/ui/live-preview.ts`).
- L6, klein: weergave van Infinity (`src/engine/format.ts`, `evaluate.ts`), een leeg instelveld wordt 0 (`src/ui/settings.ts`), al open vensters zonder skin (`src/main.ts`), traag op tabelregels met 50.000 spaties (`src/rollers/markdown.ts`), `1D6KH1` wordt geweigerd.
- Voor verkoop: sleutels met een handtekening in plaats van de controlesom.

Herhaald renderen is opgelost in `src/rollers/defuse.ts` plus een controle in `src/ui/reading-view.ts`. Alleen in Obsidian te bewijzen, dus handmatig testen: `dice: [[Zichzelf]]` en `dice: #npc` in een notitie met die tag, ook met `![[Zichzelf]]` in de notitie. Let op: een andere plugin die notities in een uitkomst invoegt (zoals Dataview) is niet gedekt, en of `el.closest` werkt hangt ervan af of Obsidian het element al heeft ingehangen tijdens de post-processor.

## Niet vastgesteld

- De indeling van `data.json` van Dice Roller. Broncode lezen mocht niet, dus de import herkent eenvoudige vormen onder elke sleutel met "formula" in de naam. Tests draaien op een eigen model, niet op een echt bestand. De map `obsidian-dice-roller` komt uit het id in deel 3 van het onderzoek.
- Of de notatie in randgevallen gelijk is aan Dice Roller: niet naast de echte plugin gedraaid.
- Het kleurcontrast van de betaalde skins: niet bekeken.

## Na de herkeuring (6 nov), voor uitgave
- Omzeilen van `defuseRolls` kan nog met html-vormen zoals `dice&#58;` en `d<b>ice</b>:`. Dan hangt het aan `el.closest`, in Obsidian te bewijzen.

## Na herkeuring L7 en L8 (6 nov), voor uitgave
- L9: `src/rollers/defuse.ts:18`, de code-regex loopt over blokgrenzen. Een losse backtick eerder (`it`s`) maakt echte code onherkenbaar, en die blijft rollen. Per blok of regel werken, met test. Hoe erg dit is hangt af van het tweede slot in Obsidian.
