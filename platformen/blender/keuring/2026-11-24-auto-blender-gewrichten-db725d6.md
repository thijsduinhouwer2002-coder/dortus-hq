# Keuring blender-gewrichten winkelschermbeelden ronde 4, 24-11-2026, automatische keurder
Wat ik keurde: commit db725d69f (94ff933..db725d6), alleen `producten/blender-gewrichten/e2e/scherm_winkel.py`
Akkoord: ja

## Deel A: doet het wat beloofd is?
De belofte staat in de commitregel: bij plaatje w2 moet Export STL/3MF in beeld staan. Er zit geen add-on-code in de wijziging.

| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De nieuwe functie `zijbalk_omlaag` scrolt de zijbalk met 25 muiswielklikken boven het midden van de zijbalk en daarna met `view2d.scroll_down` als vangnet. De aanpak is logisch. | Feit (uit de code) | Hoog | Dat het ook werkt, blijft een vermoeden: zie rij 2. |
| 2 | Het script controleert niet of Export STL/3MF na het scrollen echt zichtbaar is. Het schrijft alleen de view2d-positie in het log, en `WINKEL OK` hangt daar niet van af. Of de knop in beeld staat, blijkt dus alleen uit het plaatje zelf. | Vermoeden | Midden | Het plaatje w2 van de run met de Read-tool bekijken. Daar moeten Export STL en Export 3MF volledig zichtbaar zijn. |
| 3 | De Python-opbouw van `PLAN` klopt. De lambda blijft één tupel, `zijbalk_omlaag` is het derde element, en `PLAN[i][:2]` met `na` werkt ook voor w1 en w3 met twee elementen. | Feit (uit de diff) | Hoog | Een groene run van het script. |
| 4 | De wachttijd na het tekenen gaat van 1,0 naar 1,5 s voor alle plaatjes. Dat is onschadelijk, het kost alleen een paar seconden. | Feit | Hoog | n.v.t. |

## Deel B: houdt het zich aan onze regels?

| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Er is geen test aangepast om te slagen. De eis voor `alles` en de OK/FOUT-regel zijn niet gewijzigd. | Feit | Hoog | Tests niet aangepast om te slagen |
| 2 | De wijziging is klein (±30 regels erbij). Of het bestand onder ±400 regels blijft, kan ik niet zien, maar het is waarschijnlijk. | Vermoeden | Midden | Bestanden onder ±400 regels |
| 3 | `architectuur.md` hoeft niet bij te werken: er verandert niets aan de add-on of aan het gedrag voor de gebruiker. | Feit | Midden | architectuur.md bijgewerkt |
| 4 | Er staan geen persoonsgegevens, sleutels of cijfers zonder bron in de wijziging. | Feit | Hoog | Geen persoonsgegevens, GEZIEN/DERDEN/GOK |
| 5 | De hulpfuncties `xdo`, `zijbalk`, `time` en `os` komen niet in de diff voor. Ze bestaan waarschijnlijk al in het bestand, want `ververs` gebruikt `zijbalk` al. | Vermoeden | Midden | Een groene run van het script |
| 6 | De zijbalk blijft na w2 omlaag gescrold staan. Plaatje w3 (testkaart) wordt daarna genomen en kan een andere uitsnede van het paneel krijgen dan bedoeld. | Vermoeden | Laag | Plaatje w3 naast het vorige plaatje leggen. |

## Deel C: zou een gebruiker het leuk en fijn vinden?
Ik kan geen beelden zien, dus dit zijn alleen aandachtspunten voor Daan en Iris.

| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | Als stap 3 in beeld komt, scrolt stap 1 (Place) mogelijk uit beeld. Op een winkelplaatje wil je liefst het hele paneel van 1 tot 3 laten zien. | De viewport hoger maken, of het paneel compacter of kleiner opnemen, in plaats van scrollen. | Klein |
| 2 | Plaatjes voor extensions.blender.org mogen alleen gratis functies tonen. Het script maakt niet kenbaar of w2 en w3 uit de gratis of de betaalde build komen. | Bij de plaatjes vastleggen welke build ze toont (w3, de testkaart, is betaald en hoort dus alleen op Superhive). | Klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Laat het script falen of waarschuwen als na het scrollen de Export-knoppen niet binnen de zijbalk vallen. Nu bewijst alleen het plaatje dat het gelukt is.
- Bekijk w2 met de Read-tool voordat het plaatje in een winkel gaat. Daan keurt het uiterlijk.
- Zet de zijbalk voor w3 terug naar boven, of controleer dat w3 niet door de scrollstand verandert.
- Zet in het log of de naam van het plaatje welke build (gratis of Pro) het is.

---
Automatische keurder, model `claude-sonnet-5-5`, 18361 tokens in, 3586 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
