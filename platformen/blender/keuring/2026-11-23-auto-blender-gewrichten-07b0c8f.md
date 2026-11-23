# Keuring blender-gewrichten kantel-herkansing, 23-11-2026, automatische keurder
Wat ik keurde: commit 07b0c8f86 (8402114..07b0c8f), bestanden `betaald/rig.py` en `e2e/toetsen_mens.py`
Akkoord: ja

## Deel A: doet het wat beloofd is?
De opdracht in `ontwerp.md` (ja van 16 nov) gaat over de gratis 0.1.1 en Pro 1.0.2. Deze wijziging raakt de betaalde `rig.py`, dus dat ja dekt haar niet. De commit zegt zelf "niet voor main", dus ik toets of de proef doet wat het commitbericht belooft.

| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | Bij "blocked" of "no watertight parts" komt direct na die plek één kandidaat bij: dezelfde plek, as 0,5° gekanteld (`gekanteld`, `kantel_in`). Alleen kogels, en elke plek maar één keer. | Feit | Hoog | Staat zo in de diff. |
| 2 | De plek zelf verschuift niet: de vertaling wordt letterlijk overgenomen en alleen de rotatie om X verandert. | Feit | Hoog | Een test die de kogelpositie voor en na vergelijkt. |
| 3 | De toets simuleert de AMD-uitkomst door elke ongekantelde snede op DOEL2 te weigeren. Dat bewijst dat de herkansing loopt, niet dat een gekantelde snede op de echte CI-processor wel slaagt. | Feit (simulatie) | Hoog | Een groene run met CJ_HERKANS=4 op CI, plus een run zonder nep-weigering op de AMD-runner. |
| 4 | Het commentaar in de toets belooft "beweegt minstens 15 graden, delen gesloten". De check zelf telt alleen dat `kogel_vast` niet weigert. | Feit | Midden | De volledige `kogel_vast` lezen. Als die de buighoek en gesloten delen meet, klopt het commentaar. |
| 5 | De herkansing werkt alleen als `kandidaten.insert(i + 1, ...)` tijdens de lus gezien wordt. De lus is niet in de diff te zien. Draait hij over `enumerate(kandidaten)` of `while`, dan werkt het. Bij `range(len(...))` blijft de kantelplek ongezien. | Vermoeden | Midden | De lus lezen, of de CI-run met CJ_HERKANS=4. |
| 6 | `Matrix` wordt in `gekanteld` gebruikt, maar de import staat niet in de diff. `gedraaid` direct eronder gebruikt waarschijnlijk dezelfde import. | Vermoeden | Midden | Een run die `gekanteld` aanroept. |

## Deel B: houdt het zich aan onze regels?

| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Er is niets aan bestaande toetsen verzwakt: de toets is alleen uitgebreid, achter CJ_HERKANS=4. | Feit | Hoog | Tests niet aangepast om te slagen: voldaan. |
| 2 | `rig.py` is veel langer dan 400 regels (de hunks staan al rond regel 700 tot 790) en groeit met ruim 30 regels. Dat was al zo. | Feit | Hoog | Bestanden onder ±400 regels: niet gehaald, al eerder. |
| 3 | `architectuur.md` is niet bijgewerkt voor de nieuwe herkansing, de constante `KANTEL_GRADEN` of de toets CJ_HERKANS=4. | Feit | Hoog | architectuur.md bijgewerkt: nog niet. Voor een proefwijziging "niet voor main" is dat geen blokkade. |
| 4 | Het commentaar noemt "CI AMD, lokaal Intel" als oorzaak, zonder GEZIEN, DERDEN of GOK. Het is een verklaring van Olaf. | Vermoeden | Midden | Cijfers met GEZIEN/DERDEN/GOK. |
| 5 | `KANTEL_GRADEN = 0.5` staat standaard aan. Op deze tak verandert het gedrag van de betaalde knop dus voor alle kogels zodra een snede mislukt, ook zonder de toetsvariabele. | Feit | Hoog | Geen regelbreuk zolang het niet naar main gaat. |
| 6 | Persoonsgegevens, sleutels, AI-beeld of -geluid en spelerstekst van Hats komen in deze wijziging niet voor. | Feit | Hoog | Voldaan. |

## Deel C: zou een gebruiker het leuk en fijn vinden?
Er is niets te zien of te spelen in deze wijziging.

| # | Bevinding | Wat het beter maakt | Moeite (klein/midden/groot) |
|---|---|---|---|
| 1 | Een gebruiker merkt van 0,5° kantelen niets, behalve dat er vaker een gewricht komt in plaats van "blocked". Dat is winst, als het op echte figuren slaagt. | Telling "N gewrichten op de tweede kans" in het eindbericht van de knop, zodat Chris of Thijs de winst ziet. | Klein |
| 2 | Een gewricht dat 0,5° scheef staat, geeft geen zichtbaar verschil. Het buigbereik kan een halve graad afwijken. | Controleer na de proef of "Bends ±N°" nog klopt op de gekantelde snede, bijvoorbeeld op de MakeHuman-heup. | Klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Draai CJ_HERKANS=4 op CI en leg de groene run vast voor je dit naar main wilt (A3, A5, A6).
- Test ook zonder nep-weigering op de AMD-runner dat de kantelsnede echt slaagt. De simulatie bewijst alleen de route (A3).
- Laat de check in de toets ook de buighoek van minstens 15° en gesloten delen meten, of pas het commentaar aan (A4).
- Werk `architectuur.md` bij en splits `rig.py` voor samenvoegen naar main (B2, B3).
- Zet GEZIEN of GOK bij de bewering over AMD en Intel (B4).
- Dit dekt geen release: een nieuwe keuring is nodig voor Pro 1.1 of hoger.

---
Automatische keurder, model `claude-sonnet-5-5`, 20249 tokens in, 5628 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
