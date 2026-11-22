# Keuring blender-gewrichten, 22-11-2026, automatische keurder
Wat ik keurde: commit becfa9715 (f1a171e..becfa97): `rig.py`, `een_lid_diep.py` en `architectuur.md`, alleen als tekst gelezen
Akkoord: ja

## Deel A: doet het wat beloofd is?
De opdracht in `ontwerp.md` is akkoord voor Click Joints 0.1.1 en Pro 1.0.2. Deze wijziging hoort bij "Figure from rig" (Pro 1.1) en valt daar niet onder. Ik toets daarom tegen de eigen belofte van de commit: elleboog alleen naar voren, met omhulsel H.

| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|-----------|-------------------|-----------|--------------------------------------|
| 1 | De stand naar achteren is uit `rig.py` gehaald: de lijst met kandidaten bevat alleen de eigen plekken en de naar voren gedraaide plekken. | Feit (uit de diff) | Hoog | Een run op een T-houding rig waarbij de elleboog niet meer naar achteren buigt. |
| 2 | `ALTIJD_H` staat aan voor de gedraaide plekken (`i >= eigen_n`) en wordt altijd teruggezet in `finally`. Een rig die al lukte merkt er dus niets van. | Feit voor de code, vermoeden voor het gedrag | Midden | Een run op een rig die al lukte (bijvoorbeeld de MakeHuman-mens) met een gelijk resultaat voor en na. |
| 3 | De diff toont niet hoe `i` en `kandidaten` in de lus lopen, ook niet bij `poging_kk == 1`. Als `i` daar niet tegen dezelfde lijst telt, staat H aan of uit op de verkeerde plek. | Vermoeden | Laag | De hele lus lezen, of een log met per poging de waarde van `ALTIJD_H`. |
| 4 | Met één lus en H aan loopt `bereid_diep` verder in code die we niet zien. Die kan twee lussen verwachten. | Vermoeden | Laag | De rest van `bereid_diep`, of de Yeti-run (lokaal gezien, zie Deel B). |
| 5 | De bewering "Yeti en Orc 4 gewrichten, ellebogen naar voren" is niet te controleren in de diff. `architectuur.md` noemt alleen Yeti. | Vermoeden | Midden | Een uitslag per figuur (Yeti, Orc, Alien) uit de echte Blender, bij voorkeur in Actions. |
| 6 | Rigs waar alleen de stand naar achteren lukte, krijgen nu geen elleboog. Het ontwerp noemt dat alleen als eerlijke overslag bij knie en enkel. | Vermoeden | Midden | De uitslag op Alien en andere rigs: is er een gewricht minder, en meldt de add-on dat netjes? |

## Deel B: houdt het zich aan onze regels?

| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|-----------|-------------------|-----------|-------|
| 1 | Er is geen test aangepast en er is geen test bijgekomen. Wel veranderde het gedrag: de stand naar achteren is weg en `ALTIJD_H` is nieuw. Niets in de repo houdt vast dat een elleboog niet meer naar achteren buigt. | Feit | Hoog | Toetsbaar in de echte Blender. Geen test aangepast om te slagen: voldaan. |
| 2 | `architectuur.md` is bijgewerkt met `ALTIJD_H`, "alleen naar voren" en de reden. De regel over Orc en Alien (eerst 2 naar 4 of 6) is verdwenen. Alleen Yeti staat er nog met 4 gewrichten, terwijl de commit ook Orc noemt. | Feit | Hoog | architectuur.md bijgewerkt: grotendeels voldaan. |
| 3 | De bron is "GEZIEN Blender 5.3.0 lokaal" en "keuring Daan". Er is geen log, geen beeld en geen keuringsbestand bij de wijziging. | Feit | Hoog | Cijfers met GEZIEN, DERDEN of GOK: label staat er, maar het bewijs is niet te controleren. |
| 4 | `rig.py` is veel groter dan ±400 regels (de diff begint al op regel 671). Dit commit voegt er netto een paar regels aan toe. | Feit | Hoog | Bestanden onder ±400 regels. Het probleem was er al. |
| 5 | Geen persoonsgegevens, sleutels of wachtwoorden in de wijziging. | Feit | Hoog | Geen persoonsgegevens: voldaan. |

## Deel C: zou een gebruiker het leuk en fijn vinden?
Ik kan niets zien of spelen. Dit zijn dus vermoedens uit de tekst.

| # | Bevinding | Wat het beter maakt | Moeite |
|---|-----------|---------------------|--------|
| 1 | Alle ellebogen buigen nu naar voren. Dat is meestal wat een figuur nodig heeft, maar elke gedraaide elleboog buigt dan hetzelfde. | Op de winkelplaatjes een figuur met ellebogen in een natuurlijke pose laten zien, zodat de koper de richting ziet. | Klein |
| 2 | Knieën en enkels worden bij zijwaarts buigen overgeslagen. Een figuur kan dus 4 gewrichten krijgen waar je er 6 verwacht. | In het paneel per overgeslagen gewricht de reden tonen, bijvoorbeeld "knee skipped: would bend sideways". | Klein |
| 3 | Een kopersbeeld van Yeti en Orc met buigende ellebogen zou verkopen. Daan en Iris keuren het beeld. | Een schermafbeelding of beweegproef van Yeti na de wijziging naast de oude toestand zetten. | Klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** niets.

**Kan:**
- Voeg een toets toe in de echte Blender (Actions) voor Yeti, Orc en Alien: het aantal gewrichten, geen verloren stuk boven 6%, en de elleboog buigt niet naar achteren. Nu staat het alleen als lokaal gezien in tekst.
- Zet in `architectuur.md` wat er met Orc, Alien en Ninja is (4 of 6 gewrichten, of overgeslagen), zodat de lijst bij de commit past.
- Controleer in de lus van `rig.py` dat `i >= eigen_n` ook klopt bij `poging_kk == 1`, en dat `bereid_diep` met één lus en H aan niet vastloopt.
- Splits `rig.py` op, want het bestand is ver boven de ±400 regels.
- Leg de keuring van Daan vast in een bestand (de commit verwijst ernaar, maar het staat niet in de wijziging).

---
Automatische keurder, model `claude-sonnet-5-5`, 23993 tokens in, 5502 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
