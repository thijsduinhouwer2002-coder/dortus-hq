# Keuring blender-gewrichten testkaartplaatjes, 19-11-2026, automatische keurder
Wat ik keurde: commits 7c8ae22..3ff874a (3ff874a7d), bestand `producten/blender-gewrichten/e2e/scherm_testkaart.py`
Akkoord: ja

## Deel A: doet het wat beloofd is?
De opdracht in `ontwerp.md` gaat over de gratis add-on 0.1.1 en Pro 1.0.2. Deze wijziging raakt de add-on niet, alleen het script dat de winkelplaatjes van de testkaart maakt. Ik toets daarom tegen het commitbericht en de kopregel van het script.

| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | Plaatje 20 zet nu de scharnierset rechts naast de kogelset in plaats van 30 mm naar achteren, zoals het commit zegt. De code schuift de scharnierset in x en y naar rechts van de kogelset, met 25 mm lucht ertussen. | Feit (uit de code) | hoog | Het plaatje zelf bekijken. |
| 2 | Nieuw plaatje 20h toont de hele scharnierset van dichtbij (`camera(mh, 2.3*maat_h.x, 42, 8)`), met alleen die set zichtbaar. | Feit (uit de code) | hoog | Het plaatje bekijken: staan vork en bovendeel samen in beeld? |
| 3 | De tekst "Shown pulled apart" hangt als tekstobject aan de camera, links onderin, en komt dus op alle drie de plaatjes. `hide_render` raakt dat object niet. | Feit (uit de code) | hoog | Alle drie de plaatjes bekijken. |
| 4 | De plek en maat van de tekst gaan uit van een beeld van 1920×1080 en een vaste afstand van 50 mm voor de camera. Is de rendergrootte anders, dan kan de tekst verschuiven of afgesneden worden. | Vermoeden | midden | De renderinstelling in `render()` (niet in deze diff) en het plaatje. |
| 5 | Of de tekst leesbaar is en niet over een deel heen valt, is uit tekst niet te zien. De kleur hangt af van objectkleur in Workbench, wat de bestaande code al gebruikt. | Vermoeden | midden | De drie PNG's op tak `schermen` bekijken. |
| 6 | `KAART BEELD OK` telt de render van 20h mee, want `ok` wordt per plaatje bijgewerkt. | Feit (uit de code) | hoog | Het log van de volgende run. |

## Deel B: houdt het zich aan onze regels?

| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Er is geen test aangepast om te slagen. De eis van 10 + 10 delen en vijf getallen per set staat nog. | Feit | hoog | Tests niet aangepast |
| 2 | Het bestand is ruim onder de 400 regels. | Feit | hoog | Bestandsgrootte |
| 3 | Het bijschrift maakt eerlijk duidelijk dat de kaart opgetild is getoond. Er is geen AI-beeld of -geluid; het zijn Workbench-renders. | Feit | hoog | Geen AI-beeld op Steam, eerlijk beeld |
| 4 | Plaatje 20h toont de betaalde scharnierset. Het mag dus alleen op Superhive en niet op extensions.blender.org (ToS 6.2). Het script zelf zegt daar niets over. | Feit | hoog | ToS 6.2, alleen gratis functies op extensions.blender.org |
| 5 | Het script heeft geen persoonsgegevens, sleutels of cijfers zonder bron. `architectuur.md` is niet bijgewerkt, wat bij een hulpscript voor plaatjes geen bezwaar is. | Feit | midden | Persoonsgegevens, architectuur.md |

## Deel C: zou een gebruiker het leuk en fijn vinden?
Dit kan ik niet zien, ik lees alleen tekst. Wat hieronder staat is een vermoeden dat Daan en Iris op de plaatjes moeten bevestigen.

| # | Bevinding | Wat het beter maakt | Moeite (klein/midden/groot) |
|---|---|---|---|
| 1 | Beide sets naast elkaar zijn in één blik te vergelijken, en het bijschrift voorkomt een verkeerde verwachting. Dat is waarschijnlijk een verbetering. | Controleren dat de kogelset niet te klein wordt nu alles op één plaatje staat. | klein |
| 2 | De tekst is ongeveer 4% van de beeldhoogte. Op een kleine winkelthumbnail is hij daardoor mogelijk niet te lezen. | Tekst iets groter, of het bijschrift in de winkelbeschrijving herhalen. | klein |
| 3 | Alle drie de plaatjes hebben hetzelfde bijschrift op dezelfde plek. Dat is rustig, maar bij 20d, het close-up op de getallen, kan het de blik afleiden. | Bij 20d het bijschrift weglaten, als het storend blijkt. | klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Daan keurt de drie plaatjes (20, 20d, 20h) op beeld. Let op de leesbaarheid van het bijschrift en of 20h vork en bovendeel samen toont.
- Controleer in `.github/workflows` dat 20h ook mee naar tak `schermen` gaat. Dat bestand zat niet in de wijziging, dus ik kon het niet zien (vermoeden, zekerheid laag).
- Pas de kopregel van het script aan: "beide plaatjes bestaan" moet "alle drie".
- Zet 20h alleen op Superhive en niet op de pagina van extensions.blender.org (ToS 6.2).

---
Automatische keurder, model `claude-sonnet-5-5`, 20159 tokens in, 4825 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
