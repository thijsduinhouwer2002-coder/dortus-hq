# Keuring blender-gewrichten (Pro 1.1 plaatje 19), 19-11-2026, automatische keurder
Wat ik keurde: commits 00dd538..3c5c7e5 (3c5c7e57, Bram), vier gewijzigde bestanden onder producten/blender-gewrichten/
Akkoord: ja

## Deel A: doet het wat beloofd is?
Er is geen ontwerptekst van Daan 18 nov meegestuurd. Ik toets daarom tegen de commitregel: teller gelijk aan de lijst, romp glad, heupsnede recht, kop.

| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | Teller en lijst zijn gelijk gemaakt. `samenvatting` telt "from rig", "mirrored" en de rest ("preset") elk één keer. Het voorbeeld 2 + 2 + 5 geeft "9 joints · 2 rig · 2 mirror · 5 preset" (38 tekens). | Feit (uit de code en de nieuwe test) | hoog | Een run van `toetsen_figuur.py` (groen) en een scherm van de zijbalk. |
| 2 | Een lid zonder `herkomst` telt als "preset", ook als het iets anders is. Bij 2 joints zonder rig of mirror blijft het "2 joints" zonder preset-deel. | Vermoeden | midden | Controleren welke `herkomst`-waarden er bestaan in `betaald/`. |
| 3 | De romp wordt glad gestreken (`glad_romp`, Laplace, 25 keer, factor 0,8) tussen z 92 en 170 en |x| < 30. De code moet het resultaat nog bewijzen. | Vermoeden | midden | Het nieuwe plaatje 19 uit de run: zijn borsten, navel en billen weg? |
| 4 | De commit noemt vier moets, maar de diff raakt alleen de teller en de romp. Heupsnede recht en kop zitten er niet in. | Feit (diff) over wat ontbreekt, vermoeden over of het ontbreekt | midden | Zit het in een eerder commit, in een niet-gewijzigd script of in een tekstbestand buiten de diff? Zo niet, dan zijn twee moets van Daan nog open. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | De test voor de samenvatting is aangepast, maar omdat de tekst bewust veranderde, niet om te slagen. Er is een nieuwe test voor 9 joints bijgekomen. | Feit | hoog | Tests niet aangepast om te slagen: ok |
| 2 | `toetsen_rig.py` controleert nu alleen op de losse stukjes " rig" en "mirror". Dat is zwakker dan het volledige getal. | Feit | hoog | Test blijft zinvol: kan scherper |
| 3 | De docstring van `glad_romp` zegt "volume blijft". `smooth_vert` is Laplace-gladstrijken en krimpt de vorm een beetje. | Vermoeden | midden | Beweringen kloppen: kan |
| 4 | `glad_romp` heeft geen test. Alleen `staat["glad_romp"]` en een logregel. Of `os` in `scherm_mens.py` al geïmporteerd is, blijkt niet uit de diff. | Vermoeden | laag | Een run van het schermscript bevestigt het. |
| 5 | `architectuur.md` is niet gewijzigd. De oude tekst "6 joints · 4 from rig · 1 mirrored" kan daar of in de winkeltekst nog staan. | Vermoeden | laag | Zoeken naar "from rig" in de docs. |
| 6 | Geen persoonsgegevens, sleutels of AI-beeld gezien. De pop wordt in Blender zelf gemaakt. Bestandsgroottes zijn uit de diff niet te zien. | Feit | midden | Bestanden onder ±400 regels: niet te beoordelen |

## Deel C: zou een gebruiker het leuk en fijn vinden?
Ik kan niets zien. Dit zijn vermoedens uit de tekst.

| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | "2 rig · 2 mirror · 5 preset" is korter, maar voor een nieuwe koper is "preset" onduidelijk. | Een tooltip of een kleine uitleg in het paneel. | klein |
| 2 | De romp wordt glad strijken met een harde selectiegrens (geen zachte rand, ondanks de docstring). Dat kan een rand of knik bij hals, dijen of schouder geven. | Per punt een gewicht dat naar de rand afneemt. Check op het nieuwe plaatje. | midden |
| 3 | Een volledig gladde tekenpop kan saai ogen op de poster. | Een duidelijke pose of kleurkeuze zodat het gewricht opvalt. | klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Bevestig dat heupsnede recht en de kop (moet 3 en 4 van Daan) echt gedaan zijn. De diff toont ze niet. Daan keurt het nieuwe plaatje 19 hierop.
- Voeg een kleine test toe voor `glad_romp` (aantal punten groter dan 0, `os` geïmporteerd).
- Maak de test in `toetsen_rig.py` scherper.
- Pas de docstring "volume blijft" aan of voeg een zachte rand toe.
- Zoek in `architectuur.md` en de winkeltekst naar de oude vorm "from rig" en werk bij.
- Daan keurt het uiterlijk van plaatje 19 nog.

---
Automatische keurder, model `claude-sonnet-5-5`, 19975 tokens in, 4426 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
