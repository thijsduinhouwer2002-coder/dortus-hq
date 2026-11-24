# Keuring blender-gewrichten Pro 1.2.7, 24-11-2026, automatische keurder
Wat ik keurde: commits c65d228..b89472e (8b7385f31 en b89472e85), vijf bestanden, alleen als tekst gelezen
Akkoord: ja

## Deel A: doet het wat beloofd is?
De opdracht is de beschrijving in de commit en in `architectuur.md`: een scharnier na Shift + rechtsklik moet werken. `ontwerp.md` bevat nog geen eis voor 1.2.7.

| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De logica klopt op de rechte staaf. Bij cursor-Z naar de kijker (hoek 0 of 180 graden) schat `lid_uit_vorm` de lidas uit de smalste breedte. `naar_midden` zet het punt dan terug naar het midden, en dat levert x-as en z=0 op. | Feit uit de code, uitkomst nagerekend op papier | midden | Een groene run van `toetsen_shift` in 4.2.23, 5.2.3 en 5.3.0. Er staat geen run-id in de wijziging. |
| 2 | De toets geeft kijkrichting en cursorassen zelf mee aan `plaats_scharnier`. Hij speelt dus niet een echte Shift + rechtsklik in een echte 3D-weergave na. Of Blender de cursor echt met orientation VIEW plaatst en de `region_3d` goed doorgeeft, zie ik niet. | Vermoeden | midden | Een Xvfb-run met een echte klik in de viewport (zoals `schermen.py`) of een schermafbeelding van clip 3. |
| 3 | `op_huid` eist een afstand tot de huid van hoogstens 0,5 mm. Op een groot figuur of met weinig diepteprecisie kan de cursor verder van de huid landen. Dan valt het gedrag terug op de oude meldingen "Too thin" of "Look at the joint from the side". | Vermoeden | laag | Een proef op een echt figuur (bijvoorbeeld de Yeti of de robot) met een klik in de viewport. |
| 4 | De richting van de lidas komt uit `k.cross(d)`. Het teken hangt af van welke richting `d` uit de lus als smalste wint. Dat kan de delen A en B omwisselen of de buigkant omdraaien. De toets gebruikt `abs(lid.x)` en ziet dat niet. | Vermoeden | laag | Een toets die de buigrichting en welk deel boven zit controleert, of een bewuste keuze van het teken (bijvoorbeeld naar scherm-omhoog). |
| 5 | Een cursor binnen het figuur blijft zoals hij was, en de weigering blijft. Dat is getoetst in (c) en past bij `toetsen_kijk`. | Feit uit de code | hoog | n.v.t. |

## Deel B: houdt het zich aan onze regels?

| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | `toetsen_scharnier.py` kreeg alleen een extra aanroep. Bestaande toetsen zijn niet aangepast om te slagen. | Feit | hoog | Tests niet aanpassen om te slagen |
| 2 | `architectuur.md` is bijgewerkt: `cursor_lid.py`, de zeven waarden van `assen`, `cj_bijgesteld`, de toets en de bekende beperking. | Feit | hoog | architectuur.md bijgewerkt |
| 3 | `cursor_lid.py` is 132 regels en `toetsen_shift.py` 71. De regelaantallen van `scharnier.py` zie ik niet. | Vermoeden | laag | Bestanden onder ±400 regels (`wc -l`) |
| 4 | Er staan geen persoonsgegevens of sleutels in de wijziging. | Feit | hoog | Geen persoonsgegevens |
| 5 | Het commitbericht zegt dat de uitgave-workflow op 1.2.7 staat. Het manifest en de workflow staan niet in de lijst met gewijzigde bestanden. | Vermoeden | midden | Een `git show --stat b89472e` of de versieregel in `blender_manifest.toml` |
| 6 | De grens `KIJK_MIN` staat dubbel (hier en als getal in `scharnier_vorm`). Dat is eerlijk in de tekst vermeld, maar het kan later uit elkaar lopen. | Feit | hoog | Eén bron voor een grens |
| 7 | Alle nieuwe zichtbare tekst is Engels. Er is geen AI-beeld of -geluid en geen spelerstekst. | Feit | hoog | Tekst voor kopers in het Engels |

## Deel C: zou een gebruiker het leuk en fijn vinden?
Ik kan niets zien of spelen, dus dit zijn aanbevelingen op basis van de tekst.

| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | De add-on stelt zelf de lidas en het midden bij. De gebruiker ziet dat alleen in een melding onderin. | Toon kort de geschatte as en het punt in de viewport, of laat een undo en "gebruik mijn cursor" duidelijk zien. | midden |
| 2 | De melding "Cursor on the surface: limb axis from the mesh and centred in the limb." is technisch. | Korter en menselijker: "Hinge placed in the middle of the limb." | klein |
| 3 | De aanpak is alleen getoetst op een rechte staaf. Bij een gebogen lid of twee dicht bij elkaar staande benen kan het misgaan. | Een proef op de Yeti of de robot met Shift + rechtsklik, en een schermafbeelding in het log. | midden |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
1. Voor het uitbrengen is een groene e2e-run in 4.2.23, 5.2.3 en 5.3.0 voor deze commit nodig, met het run-id in het bericht. Ook ontbreekt nog een akkoord in `ontwerp.md` voor 1.2.7 (Daan of Iris).
2. Controleer dat het manifest en de uitgave-workflow echt op 1.2.7 staan (deel B, punt 5).
3. Kies het teken van de lidas bewust en toets de buigrichting (deel A, punt 4).
4. Overweeg een ruimere of slimmere `RAND_MM`, of meld duidelijk als de cursor te ver van de huid ligt (deel A, punt 3).
5. Eén bron voor `KIJK_MIN`.
6. Meld de bijstelling kort en in gewone woorden.

---
Automatische keurder, model `claude-sonnet-5-5`, 30022 tokens in, 7221 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
