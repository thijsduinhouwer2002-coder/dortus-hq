# Keuring blender-gewrichten, betrouwbaarheid en drempel 4.2, 23-11-2026, automatische keurder
Wat ik keurde: commits 183fae2..5aa27a8 (5aa27a88d): `e2e/meet_drempel.json` en `proeven/betrouwbaar-rig-2026-11-23/uitslag.md`
Akkoord: ja

## Deel A: doet het wat beloofd is?
De add-on zelf is niet veranderd, alleen een testdrempel en een meetverslag. Ik toets dus of het verslag klopt en past bij de opdracht.

| # | Bevinding | Feit of vermoeden | Zekerheid (hoog/midden/laag) | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De tellingen in de tabellen kloppen onderling: 4.2.23 geeft 6+6+7+8+9+7+8 = 51 van 60, en 5.2.3 geeft 60 van 60. De 9 gemiste gewrichten in "Wat nog niet lukt" (2 robots × 3, robot-fijn 2, kleding 1) komen daar ook op uit. | Feit | Hoog | Alleen uit de tekst gerekend. De logs van de runs zelf heb ik niet gezien. |
| 2 | De 5.x-cijfers komen uit run 45273407326 (commit 0eb3510), de 4.2-cijfers uit run 45275271607 (commit 183fae2). Of "60 van 60" in 5.x ook geldt voor de huidige code (5aa27a8) is niet bewezen. | Vermoeden | Midden | Een 5.x-run op 5aa27a8 met dezelfde uitkomst. Zonder dat is het een aanname dat `herstel.opschonen` in 5.x niets veranderde. |
| 3 | Het verslag zegt dat het linkerscharnier in 4.2 een bereik van 0 tot 150 geeft in plaats van 120, bij een snede die "niet goed" is. Het blijft onduidelijk of een koper dat verkeerde getal te zien krijgt of dat het gewricht geweigerd wordt. | Vermoeden | Midden | Het log of de paneeltekst van de 4.2-run voor robot, linkerschouder en linkerheup. Staat daar "no room" en geen graden, dan is er geen probleem. |
| 4 | De bron van het wisselen in 5.x is netjes onderbouwd. In de nulstand waren 186 van 558 sneden "los" en precies die waren slecht. Op de tak is het 0 van 430, en het "parallel rekenwerk" is expliciet als GOK gemarkeerd. | Feit en vermoeden, gescheiden | Hoog | Meer herhalingen op de tak. De 0 van 430 is sterk bewijs voor de oorzaak "volgorde van rekenwerk", maar niet voor de precieze reden. |

## Deel B: houdt het zich aan onze regels?

| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | De ondergrens in 4.2 gaat omlaag voor robot-a en robot-b (7 naar 6), en robot-fijn krijgt een eigen 4.2-grens van 7. Dat is een testdrempel die zakt. De reden staat open in het bestand en in het verslag: andere robot (studio-3), gemeten stand als bodem, doel blijft 9. | Feit | Hoog | Tests niet aanpassen om te slagen. Ik beoordeel dit als geen overtreding, omdat het een gedocumenteerde ondergrens tegen terugval is. De figuurwissel en de verlaging staan wel in één commit. |
| 2 | Het verslag zegt "5 keer per figuur", maar rigify in 4.2 heeft 4 uitkomsten en robot-fijn in 5.3.0 maar 3, zonder uitleg bij de nieuwe tabel. Alleen de nulstand-tabel noemt "afgebroken". | Feit | Hoog | Cijfers eerlijk (GEZIEN/DERDEN/GOK). Het is klein, want de conclusie "gelijk" blijft staan. |
| 3 | De commit noemt "berichten bijgewerkt", maar er staat geen berichtenbestand in de gewijzigde lijst. | Vermoeden | Laag | Controle of dat in een andere commit of repo zit. Geen regelschending. |
| 4 | Geen persoonsgegevens of sleutels gezien. De add-on is niet gewijzigd, dus `architectuur.md` hoeft niet mee. | Feit | Hoog | Geen persoonsgegevens, architectuur bijwerken. |
| 5 | Of `uitslag.md` onder de ±400 regels blijft kan ik uit de diff niet zien. Het bestand is wel al meer dan 130 regels lang en groeit. | Vermoeden | Laag | `wc -l` op het bestand. De regel gaat over code en is voor een verslag niet streng. |

## Deel C: zou een gebruiker het leuk en fijn vinden?
Er is niets te zien of te spelen in deze wijziging. Hieronder staat wat de cijfers voor een koper betekenen.

| # | Bevinding | Wat het beter maakt | Moeite (klein/midden/groot) |
|---|---|---|---|
| 1 | Een koper op Blender 4.2 (de laagste ondersteunde versie) krijgt op de robot 6 van 9 gewrichten en 8 op het aangeklede figuur. In 5.x krijgt hij ze allemaal. Dat voelt als een tweederangs versie. | De 4.2-melding duidelijk maken ("fully supported from Blender 5.2"). Of de scharniersnede in 4.2 zelf oplossen, zoals het verslag al als eigen spoor noemt. | Midden tot groot |
| 2 | In 4.2 duurt een figuur 2 tot 5 minuten. Dat voelt traag als er geen voortgang te zien is. | Een voortgangsbalk of melding per gewricht, zodat de gebruiker niet denkt dat Blender vastzit. | Klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Draai één 5.x-run op de huidige commit 5aa27a8 om te bevestigen dat "60 van 60" nog geldt (A2).
- Controleer in het 4.2-log of een koper het bereik 0 tot 150 bij het linkerscharnier te zien krijgt. Zo ja, dan is dat een echt probleem voor de belofte "see how far it bends" (A3).
- Vermeld in het verslag bij rigify (4.2) en robot-fijn (5.3.0) waarom het er 4 en 3 zijn in plaats van 5 (B2).
- Zet de figuurwissel (studio-2 naar studio-3) en de drempelverlaging voortaan in aparte commits, zodat een echte terugval niet verdwijnt achter een nieuwe testfiguur (B1).
- Maak de 4.2-ervaring voor kopers beter, met een duidelijke melding en voortgang (C1, C2).

---
Automatische keurder, model `claude-sonnet-5-5`, 21167 tokens in, 6072 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
