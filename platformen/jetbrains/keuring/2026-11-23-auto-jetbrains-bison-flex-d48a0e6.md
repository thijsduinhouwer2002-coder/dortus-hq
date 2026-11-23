# Keuring e2e CLion-build en structuurweergave 263, 23-11-2026, automatische keurder
Wat ik keurde: commit d48a0e60f (ee8117f..d48a0e6), `ClionTest.kt` en `StructuurEnZweven.kt` in `producten/jetbrains-bison-flex/e2e/`
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid (hoog/midden/laag) | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De wijziging raakt alleen e2e-testcode. De belofte van het product (plugin.xml, winkeltekst) en de plugincode zelf zijn niet veranderd. | Feit | hoog | De lijst met gewijzigde bestanden. |
| 2 | De structuurweergave wordt nu op twee plekken gezocht: eerst de eigen plugin van 263 en daarna de kern tot 262. De code leest logisch en vangt de fouten van beide plekken netjes op. | Feit | midden | Een groene e2e-run op 263 en op 262, met in het log de regel "DORTUS-E2E structuurweergave via ...". |
| 3 | Het is niet te zien of dit op 263 echt werkt. In de tekst staat geen uitslag van een run. De eerste aanroep (`StructureViewFactoryEx`) kan op 263 ook verhuisd zijn. | Vermoeden | midden | Een run op 263 waarin `structuurBestand()` een bestandsnaam geeft in plaats van "fout ...". |
| 4 | De EAP-lijst wordt gelezen met een regex op JSON (datum tot het eerstvolgende "build"). Heeft een release geen "build", dan koppelt de regex een datum aan de build van een andere release. De 29 dagen geldigheid is een aanname uit één foutmelding. | Vermoeden | laag | Een proef met de echte respons van de API, plus een build net voor en net na de grens van 30 dagen. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Er staat een nieuwe `Assumptions.assumeTrue`: de CLion-test slaat zichzelf over als er geen geldige EAP is. Een overgeslagen test geeft geen bewijs voor CLion, terwijl het ontwerp zegt "zonder CLion-bewijs niet indienen". De reden komt wel in het log. Dit is geen aangepaste test om te slagen, want de controles zelf zijn niet versoepeld. | Feit | hoog | Tests niet aanpassen om te slagen. Een overslag mag niet als bewijs tellen. |
| 2 | `CLION_BUILD` is nu `String?`. Elk ander gebruik van die waarde (andere testbestanden, Gradle, het log) moet daarbij aansluiten. In de diff zie ik dat niet. | Vermoeden | midden | Compileren. Een zoekopdracht naar `CLION_BUILD`. |
| 3 | De bestandslengtes zijn niet te zien. `ClionTest.kt` en `StructuurEnZweven.kt` zijn gegroeid, en ik weet niet of ze onder de ±400 regels blijven. | Vermoeden | laag | `wc -l` op beide bestanden. |
| 4 | `architectuur.md` is niet aangepast. Dat is verdedigbaar voor testcode, maar ik kan niet zien of de e2e-opzet daar beschreven staat. | Vermoeden | laag | Zoeken in `architectuur.md` naar "e2e" of "CLion-EAP". |
| 5 | Ik zie geen persoonsgegevens, sleutels of wachtwoorden en geen AI-beeld of -geluid in de diff. | Feit | hoog | Geen regel geschonden. |

## Deel C: zou een gebruiker het leuk en fijn vinden? (alles wat je kunt zien of spelen)
| # | Bevinding | Wat het beter maakt | Moeite (klein/midden/groot) |
|---|---|---|---|
| 1 | Geen zichtbare verandering voor gebruikers: het is testcode. Ik kan hier niets zien of spelen. | Niet van toepassing. | klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Laat de overslag van de CLion-test in de workflow zichtbaar zijn, bijvoorbeeld als gele waarschuwing of aparte status. Reken een overgeslagen run bij de indienlijst (punt 3 van "Moet in 1.0") niet als CLion-bewijs.
- Zet een timeout (verbinding en lezen) op het ophalen van de EAP-lijst, zodat een trage server de CI niet laat hangen.
- Maak de regex van de EAP-lijst sterker, of lees de JSON echt, zodat een release zonder "build" geen verkeerde koppeling geeft.
- Draai de week-test op 263 en op 262 en zet in het bericht wat het log zegt over de gekozen plek voor de structuurweergave.
- Controleer dat `CLION_BUILD` als `String?` nergens anders de build breekt, en dat de bestanden onder ±400 regels blijven.

---
Automatische keurder, model `claude-sonnet-5-5`, 22836 tokens in, 3952 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
