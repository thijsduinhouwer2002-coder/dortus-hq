# Keuring blender-gewrichten winkelschermbeelden Pro 1.2.7, 24-11-2026, automatische keurder
Wat ik keurde: commit 0a3e3d477, bestand producten/blender-gewrichten/e2e/scherm_winkel.py (alleen tekst, geen beelden gezien)
Akkoord: ja

## Deel A: doet het wat beloofd is?
De opdracht uit de hoofdchat (16:40) heb ik niet gezien. Ik toets tegen de commitregel en de docstring.

| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | Het script maakt drie beelden (w1-figuur, w2-uitelkaar, w3-testkaart) van 1920x1080 en logt per beeld een regel en aan het eind "WINKEL OK". | Feit (uit de code) | hoog | Een groene run van workflow pro-schermbeelden met drie PNG's. |
| 2 | Het script leent de bouw en de camera van `scherm_mens.py` door de bron in te lezen en één regel te vervangen. Dat is breekbaar, maar er staat een assert die luid faalt als die regel verandert. | Feit | hoog | Een run die de assert haalt. |
| 3 | Het script gebruikt `S["kijk"]`, `S["bouw"]`, `S["rustig"]`, `S["staat"]` en acht hulpfuncties uit `scherm_basis`. Die zitten niet in deze wijziging. | Vermoeden | midden | Een run zonder KeyError of ImportError. |
| 4 | "WINKEL OK" betekent alleen dat de bestanden bestaan. Een fout in een `zet`-stap wordt gelogd maar telt niet mee. `breder()` en `labels_alle()` falen stil. Een beeld zonder labels of met een smalle zijbalk kan dus toch "OK" krijgen. | Feit (uit de code) | hoog | Zelf de drie PNG's bekijken en in het log zoeken naar "zet ... fout" en `zijbalk=`. |
| 5 | Het script logt de versie van de betaalde zip niet. "Pro 1.2.7" is dus niet in het log te controleren. Ook is er geen versieverhoging in deze wijziging, en het laatste akkoord in ontwerp.md is voor 1.2.6. | Vermoeden | midden | Een logregel met de versie uit `blender_manifest.toml` van de geïnstalleerde zip. |

## Deel B: houdt het zich aan onze regels?

| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Het bestand is 168 regels. Het is een nieuw script en er is geen test aangepast om te slagen. | Feit | hoog | Bestanden onder ±400 regels, tests niet aangepast. |
| 2 | Het figuur is MakeHuman (CC0), dus geen AI-beeld. De beelden zijn voor Superhive, waar betaalde functies mogen. Op extensions.blender.org mogen ze niet, want daar alleen gratis functies (ToS 6.2). | Feit uit de docstring, gebruik is vermoeden | midden | Beschrijving en plaatjes op extensions.blender.org tonen alleen gratis functies. |
| 3 | Er staan geen persoonsgegevens of sleutels in de wijziging. | Feit | hoog | Geen persoonsgegevens. |
| 4 | De commitregel noemt de workflow `pro-schermbeelden`, maar die zit niet in de gewijzigde bestanden. `architectuur.md` is niet bijgewerkt. Voor een proefscript is dat waarschijnlijk niet nodig. | Vermoeden | laag | Controleren of de workflow al bestond. |

## Deel C: zou een gebruiker het leuk en fijn vinden?
Ik zie geen beelden, dus ik kan hier niets over het resultaat zeggen. Dit zijn alleen aandachtspunten uit de code.

| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | Het figuur wordt 60 eenheden naar links geschoven en de zijbalk 260 px breder getrokken. Of het figuur daarna goed in beeld staat en niet achter de zijbalk verdwijnt, kan ik niet zien. | Daan bekijkt de drie beelden voor ze op Superhive komen. | klein |
| 2 | In w3 staat de testkaart op een hoek van 50° en -20° met alle andere objecten verborgen. Of de vijf nummers leesbaar zijn, is niet uit tekst te halen. | Een beeld van boven of een iets dichterbij gezoomd beeld als de cijfers klein zijn. | klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** niets.

**Kan:**
- Laat "WINKEL OK" alleen verschijnen als er geen "zet fout" was, het label-attribuut bestond en `breder()` slaagde.
- Log de versie van de geïnstalleerde betaalde add-on, zodat 1.2.7 in het log te controleren is.
- Daan (uiterlijk) en Thijs keuren de drie PNG's voor ze op Superhive komen. Ze mogen niet op extensions.blender.org.
- Controleer dat `scherm_basis` en `scherm_mens` de gebruikte namen leveren. De run moet dat bevestigen.

---
Automatische keurder, model `claude-sonnet-5-5`, 20420 tokens in, 3487 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
