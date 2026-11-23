# Keuring blender-gewrichten, proef AI-figuren tak-rig, 24-11-2026, automatische keurder
Wat ik keurde: commits 23fd6bb..061e138 (061e13862), drie bestanden in `producten/blender-gewrichten/proeven/ai-figuren-tak-rig-2026-11-24/`
Akkoord: ja

## Deel A: doet het wat beloofd is?
De opdracht is hier geen release maar een proef: "tak betrouwbaar-rig doet op 3 AI-figuren niet slechter dan main". De add-on zelf is niet veranderd.

| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | `log-main.txt` en `log-tak.txt` zijn byte voor byte gelijk (zelfde blob c9acf9348). De tabel in `uitslag.md` klopt met het log: 1 gewricht en 6 overgeslagen, 2 gewrichten en 3 overgeslagen, en geen rig bij businessman. | Feit | Hoog | Dit is de basis voor "geen achteruitgang". |
| 2 | Het log noemt nergens welke zip (PRO_VERSIE 1.2.3 of 1.2.0), welke Blender of welke commit is gebruikt. Of de twee runs echt uit verschillende builds komen, volgt dus alleen uit de tekst van `uitslag.md`. | Vermoeden | Midden | Een regel met versie en commit bovenaan elk log, of de gebruikte zips met hun sha256. |
| 3 | Bij businessman vond de proefrig bij beide builds geen benen. Die figuur toetst de tak dus niet, en de vergelijking gaat feitelijk over twee figuren. | Feit | Hoog | Een derde figuur waar de rig wel werkt. |
| 4 | De conclusie "winst zit in armen en benen dicht tegen het lijf (testset)" wordt hier niet getoond en heeft geen label (GEZIEN, DERDEN of GOK). | Vermoeden | Midden | Een verwijzing naar de testsetuitslag van Betrouwbaarheid. |

## Deel B: houdt het zich aan onze regels?

| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Er is geen test aangepast en er is geen code veranderd. Alleen proefuitslagen zijn toegevoegd, en alle bestanden zijn kort. | Feit | Hoog | Tests niet aangepast om te slagen, bestanden onder ±400 regels. |
| 2 | `architectuur.md` hoeft niet bij, want de add-on is niet veranderd. | Feit | Hoog | architectuur.md bijgewerkt. |
| 3 | In de logs staan geen persoonsgegevens, paden of sleutels. | Feit | Hoog | Geen persoonsgegevens. |
| 4 | `uitslag.md` gebruikt GEZIEN en GOK, en de releasenote-aanbeveling is voorzichtig ("on our test figures"). | Feit | Hoog | Cijfers met GEZIEN/DERDEN/GOK. |
| 5 | De figuren zijn Meshy-meshes (AI-gemaakt). De ontwerpeis is "zelf gemaakt of CC0". De bestanden staan niet in deze commit, maar de licentie van de Meshy-uitvoer (plan, naamsvermelding) is niet genoemd. | Vermoeden | Laag | Ontwerp.md, eis testfiguren. Bevestiging: de licentie van de gebruikte Meshy-plan, of een notitie in de proefmap. |

## Deel C: zou een gebruiker het leuk en fijn vinden?
Er is niets te zien of te spelen. Dit zijn alleen aanwijzingen uit het log.

| # | Bevinding | Wat het beter maakt | Moeite (klein/midden/groot) |
|---|---|---|---|
| 1 | Op beide figuren met een rig komen maar 1 of 2 gewrichten uit de knop "Figure from rig", terwijl er 3 tot 6 worden overgeslagen. Wie "full figure" verwacht, is na 30 seconden teleurgesteld. | Een duidelijke samenvatting in het paneel: "2 of 5 placed, 3 need a manual spot", met een knop naar de eerste overgeslagen plek. | Midden |
| 2 | De melding "Tight: too little limb past this joint" bij de knieën van spacetrooper1 klopt volgens Olaf waarschijnlijk niet (het onderbeen is lang genoeg). Een misleidende tip voelt stroef. | De tekst of de meting voor een latere versie aanpassen. | Midden |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Zet bovenaan elk proeflog een regel met zipversie, commit en Blender-versie, zodat het verschil tussen main en tak uit het bewijs zelf blijkt (A2).
- Voeg een figuur toe waar de rig wel werkt, want businessman toetst niets (A3).
- Zet een label bij de bewering over de testset of verwijs naar de uitslag (A4).
- Noteer de licentie van de Meshy-figuren in de proefmap (B5).
- Maak voor een latere versie de samenvatting bij overgeslagen gewrichten en de kniemelding beter (C1, C2).

---
Automatische keurder, model `claude-sonnet-5-5`, 20796 tokens in, 3513 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
