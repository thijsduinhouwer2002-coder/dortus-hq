# Keuring blender-gewrichten Pro 1.2.7 (Shift + rechtsklik), 24-11-2026 16:22 NL, automatische keurder
Wat ik keurde: commit b1053327d (11fd4d4..b105332), bestanden `betaald/cursor_lid.py`, `betaald/scharnier.py`, `e2e/toetsen_scharnier.py`, `e2e/toetsen_shift.py`
Akkoord: nee

## Deel A: doet het wat beloofd is?
Ik toets tegen de commitbeschrijving en `ontwerp.md`. Ik heb niets gedraaid, dus alles hier komt uit de tekst.

| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | Bij een cursor op de huid met Z naar de kijker schat de code de lidas uit de smalste breedte in het schermvlak. Daarna schuift het punt naar het midden van de doorsnede. Bij het lezen klopt de logica. | Vermoeden | midden | Een groene e2e-run met `toetsen_shift` in 4.2, 5.2 en 5.3. In de commit staat geen run. |
| 2 | De test gebruikt alleen een rechte staaf, waar de smalste richting vanzelf het lid aangeeft. Een gebogen been, een elleboog of twee benen dicht bij elkaar zijn niet getoetst. | Vermoeden | midden | Een toets op een echt figuur (knie van voren en van opzij) die binnen enkele graden van de echte lidas uitkomt. |
| 3 | De richting van de lidas komt uit `kijk × smalste richting` zonder vaste kant. Daardoor kan de buigkant of de plek van deel A en B anders uitvallen dan voorheen. | Vermoeden | laag | Dezelfde knie met cursor Z naar de kijker en met een rechte cursor geplaatst: buigt hij dezelfde kant op? |
| 4 | `assen` geeft nu 7 waarden terug in plaats van 6, maar alleen de aanroep in `plaats_scharnier` is aangepast. Een andere aanroeper, zoals een toets of script, zou dan breken. | Vermoeden | laag | Een zoektocht op `assen(` in de hele map, en een groene volledige e2e. |
| 5 | Een cursor binnen het figuur wordt niet bijgesteld, dus de weigering "Look at the joint from the side" blijft. Dat volgt uit `op_huid` (grens 0,5 mm) en wordt in toets (c) gecontroleerd. | Vermoeden | hoog | Toets (c) groen in de echte run. |
| 6 | `ontwerp.md` heeft geen akkoord voor 1.2.7. Het laatste ja is voor 1.2.6, en Shift + rechtsklik komt in het gelezen deel niet voor. | Feit | hoog | Een regel in `ontwerp.md` met de eis en het akkoord van Daan voor 1.2.7. |

## Deel B: houdt het zich aan onze regels?

| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | `architectuur.md` staat niet in de wijziging. De nieuwe module `cursor_lid.py` en het veranderde gedrag van `assen` (nieuwe parameters, extra teruggegeven waarde, `cj_bijgesteld`) staan er dus niet in. | Feit | hoog | architectuur.md bijgewerkt |
| 2 | Er is geen bestaande test aangepast. Er is alleen een aanroep en een import toegevoegd, plus een nieuw testbestand. | Feit | hoog | Tests niet aangepast om te slagen |
| 3 | `cursor_lid.py` is 132 regels en `toetsen_shift.py` 71. De totale lengte van `scharnier.py` zie ik niet, maar de wijziging is ongeveer 20 regels netto. | Vermoeden | laag | Bestanden onder ±400 regels (`wc -l scharnier.py` bevestigt het) |
| 4 | Ik zie geen persoonsgegevens, sleutels of wachtwoorden in de wijziging. | Feit | hoog | Geen persoonsgegevens |
| 5 | De commit heet "Pro 1.2.7", maar manifest en changelog van Pro staan niet in de wijziging. Een versienummer en uitleg voor de koper ontbreken dus nog. | Feit | midden | Alleen een kan-punt, zie hieronder |
| 6 | `KIJK_MIN = 30.0` wordt in `cursor_lid.py` herhaald, met de opmerking "zelfde grens als scharnier_assen". Als een van beide verandert, lopen ze uit elkaar. | Feit | hoog | Geen harde regel, een kan-punt |

## Deel C: zou een gebruiker het leuk en fijn vinden?

| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | Het scharnier komt in het midden van het lid, maar de cursor blijft op de huid staan. De speler ziet het gewricht dus op een andere plek dan waar hij klikte, en alleen een korte melding in de statusbalk legt dat uit. | De cursor mee verplaatsen naar het gecorrigeerde punt, of de melding duidelijker maken, bijvoorbeeld "Moved to the middle of the limb". | klein |
| 2 | De geschatte lidas kan bij een schuin of gebogen lid fout zijn, en de speler ziet dat pas na het snijden. | Na het plaatsen kort de lidas als lijn tonen, of de as in het Redo-paneel laten aanpassen. | midden |
| 3 | De bijstelling gebeurt stil bij as-bron "View direction". Wie met opzet op de huid klikt, krijgt een verschoven punt zonder dat de optie dat uitlegt. | Eén regel hulptekst bij de as-bron in het paneel. | klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet**
1. Werk `architectuur.md` bij met de nieuwe module `betaald/cursor_lid.py`, de nieuwe parameters en teruggegeven waarde van `assen`, en `cj_bijgesteld`. (B1)

**Kan**
1. Laat de e2e-run in 4.2, 5.2 en 5.3 groen zien voor deze commit. (A1, A5)
2. Voeg een toets toe op een echt figuur met een knie en een elleboog, van voren en van opzij, en controleer of de buigkant gelijk blijft. (A2, A3)
3. Zoek alle aanroepers van `assen` na, nu de teruggegeven waarde is veranderd. (A4)
4. Zet de eis en het akkoord van Daan voor 1.2.7 in `ontwerp.md` voor het uitbrengen. (A6)
5. Werk manifest en changelog van Pro bij voor 1.2.7. (B5)
6. Haal `KIJK_MIN` uit één gedeelde plek in plaats van hem te herhalen. (B6)
7. Verbeter wat de speler ziet: de cursor meeverplaatsen, de lidas tonen en een regel hulptekst in het paneel. (C1 tot C3)
8. Controleer de bestandslengte van `scharnier.py`. (B3)

---
Automatische keurder, model `claude-sonnet-5-5`, 25504 tokens in, 10075 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
