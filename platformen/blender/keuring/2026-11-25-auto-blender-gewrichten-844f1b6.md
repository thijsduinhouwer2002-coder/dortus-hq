# Keuring Pro 1.2.8: los stuk na scharniersnede (issue #14), 25-11-2026, automatische keurder
Wat ik keurde: commit 844f1b65b (ef154fe..844f1b6), alleen de tekst van de wijziging
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | `los_stuk` telt na de snede de stukken van A en B. Bij 1+1 gaat het door. Anders ruimt het eerst dunne kruimels op. Daarna mag het totaal hooguit één hoger zijn dan in de bron. Anders volgt een nieuwe poging of de weigering "loose piece" met de mesh ongewijzigd. Dat past bij wat het issue beschrijft (voet los in deel B). | Feit (uit de code) | Hoog | Een groene 4.2.23-run in CI op army_man. |
| 2 | Of het probleem op army_man echt verdwijnt, volgt niet uit de tekst. `toetsen_los` bootst de fout na met een extra blok in B, en niet met de echte wisselende Exact-boolean. | Vermoeden | Midden | De e2e op 4.2.23 met army_man, meerdere keren gedraaid. |
| 3 | `rig.py` neemt bij "loose piece" de volgende plek, en `redenen.leesbaar` geeft een leesbare tekst. De trefwoorden komen overeen met de nieuwe melding ("loose piece", "pieces)"). | Feit | Hoog | Toets `toetsen_los` of een rig-run met zo'n weigering. |
| 4 | De regel "totaal hooguit bron + 1" laat een bron met een los oog door. Verliest de snede dan ook een echt stuk (voet) maar blijft het totaal gelijk, dan wordt dat niet gezien. Dat is een kleine, zeldzame lacune. | Vermoeden | Laag | Een testfiguur met los oog én een voet die loslaat. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | De nieuwe toets staat los in `toetsen_los.py` (93 regels) en wordt alleen aan `toetsen_scharnier.py` toegevoegd. Er is geen bestaande toets aangepast om te slagen. | Feit | Hoog | Tests niet aangepast om te slagen |
| 2 | `architectuur.md` en `KAART.md` zijn bijgewerkt, met toets, melding en werking. | Feit | Hoog | architectuur.md bijgewerkt |
| 3 | De titel en KAART noemen een "geheugenwachter in de 4.2-e2e". In de gewijzigde bestanden staat geen workflow of e2e-code daarvoor (alleen `toetsen_los` en `toetsen_scharnier`). Hij kan in een bestand zitten dat niet is meegestuurd. | Vermoeden | Midden | Beweringen moeten met de wijziging kloppen |
| 4 | `los_stuk` gebruikt `snippers` en `zwaai`. De imports staan niet in de diff. Ze staan er vermoedelijk al, want KAART meldt de toets lokaal groen. Die uitslag kan ik niet zien. | Vermoeden | Midden | Tests moeten echt slagen |
| 5 | De regelaantallen van `scharnier.py` en `rig.py` zijn niet te zien, dus ±400 regels is niet te toetsen. Beide bestanden zijn waarschijnlijk al groot. | Vermoeden | Laag | Bestanden onder ±400 regels |
| 6 | Er staan geen persoonsgegevens of sleutels in de wijziging. Er zijn geen cijfers of spelerstekst om te labelen en geen AI-beeld of -geluid. | Feit | Hoog | Persoonsgegevens, GEZIEN/DERDEN/GOK, Steam |

## Deel C: zou een gebruiker het leuk en fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | Dit is een betrouwbaarheidsfix zonder nieuw beeld. De gebruiker merkt alleen een nette weigering of een ander plekvoorstel in Figure from rig. De tekst "place it by hand a few mm along the bone" is duidelijk. | Niets nodig. Een korte regel in de changelog van Pro helpt wel ("no more half-cut hinges"). | Klein |

## Deel C: is het goed genoeg?
Er is geen beeld of klantzichtbaar plaatje in deze wijziging, dus een cijfer en een blinde test zijn niet van toepassing. Daan en Iris keuren het uiterlijk apart. KAART zegt zelf dat de code nog bij Daan ligt (issue #11).

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
1. Toon in de e2e-run op 4.2.23 met army_man dat de fout niet terugkomt (liefst meerdere keren). De huidige toets bootst alleen na.
2. Meld welk bestand de geheugenwachter bevat, of stuur het mee. De titel noemt hem, maar in de diff is hij niet te vinden.
3. Controleer of `snippers` en `zwaai` bovenaan `scharnier.py` zijn geïmporteerd (de groene toets zou dat al bevestigen).
4. Overweeg een toets voor een bron met een los oog én een echt losgelaten voet, want de regel "bron + 1" ziet die niet.
5. Houd de grootte van `scharnier.py` en `rig.py` in de gaten tegen de ±400 regels.

---
Automatische keurder, model `claude-sonnet-5-5`, 27362 tokens in, 4255 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
