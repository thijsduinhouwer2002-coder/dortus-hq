# Keuring blender-gewrichten winkelschermbeelden ronde 6, 24-11-2026, automatische keurder
Wat ik keurde: commit cd52767c3, bestand producten/blender-gewrichten/e2e/scherm_winkel.py (45bba0d..cd52767)
Akkoord: ja

## Deel A: doet het wat beloofd is?
De opdracht noemt geen eigen eis voor dit script. Het hoort bij de winkelplaatjes (poster, uit elkaar, testkaart), dus ik toets het aan wat de commit zegt: schaal in een eigen stap, zodat de klik op de kop raak is.

| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De schaal staat nu in eigen stappen ("-schaal-w2", "-schaal-w3") vóór het beeld. De stapmachine tekent na zo'n stap opnieuw (zet, ververs, schiet) voordat de volgende begint. Dat is de bedoelde oplossing. | Feit (diff) | hoog | Niet nodig. |
| 2 | Of de klik op de kop nu echt raak is, kan ik uit de tekst niet halen. | Vermoeden | midden | Een groene run van de beeldjob met het log "WINKEL OK" en een winkelbeeld w2 waarop de kop is uitgeklapt of aangeklikt. |
| 3 | De stappen met "-" slaan `schiet` over en tellen niet mee in de eindcontrole `alles`. De controle op de drie echte beelden blijft dus gelijk. | Feit (diff) | hoog | Niet nodig. |
| 4 | De rest van `stap()` is niet meegestuurd. Als die elders `p[2]` leest, zoals `zijbalk_omlaag` bij w2, kunnen de nieuwe tweedelige regels een fout geven. | Vermoeden | laag | De run van de beeldjob: geen IndexError in het log. |

## Deel B: houdt het zich aan onze regels?

| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Alleen een script voor winkelbeelden is gewijzigd, geen add-on-code en geen test die een eis toetst. De eindcontrole is niet versoepeld: alle echte beelden moeten er nog steeds zijn. | Feit | hoog | Tests niet aangepast om te slagen |
| 2 | Er staan geen persoonsgegevens, sleutels of wachtwoorden in de diff. | Feit | hoog | Geen persoonsgegevens |
| 3 | De bestandslengte is niet te zien (de diff is klein). | Vermoeden | laag | Bestanden onder ±400 regels: `wc -l` op het bestand |
| 4 | `architectuur.md` hoeft niet bij te werken, want de add-on is niet veranderd. | Feit | midden | architectuur.md bijgewerkt |
| 5 | De beelden zelf kon ik niet bekijken. Dat zijn gerenderde beelden uit Blender, dus geen AI-beeld. | Vermoeden | midden | Steam-regel: de oorsprong van de beelden |

## Deel C: zou een gebruiker het leuk en fijn vinden?
Ik zie geen beelden en kan dus niets over plezier of uiterlijk zeggen. Daan keurt de winkelbeelden zelf.

| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | Geen beeld ontvangen, dus geen oordeel. | Daan kijkt naar w1, w2 en w3: is de kop te zien en is de schaal leesbaar? | klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** niets.

**Kan:**
- Controleer in de run van de beeldjob dat het log "WINKEL OK" toont en dat er geen fout staat bij de nieuwe stappen met "-".
- Gebruik liever een benoemd veld (bijvoorbeeld `toon=False`) dan het voorvoegsel "-" in de naam. Dat is minder foutgevoelig, maar smaak.

---
Automatische keurder, model `claude-sonnet-5-5`, 17931 tokens in, 2079 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
