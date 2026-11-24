# Keuring blender-gewrichten Pro 1.2.3 (Betrouwbaarheid Figure from rig), 24-11-2026, automatische keurder
Wat ik keurde: commit 14e6e42 (bereik 212df3c..14e6e42), alleen de tekst van de wijziging
Akkoord: ja

## Deel A: doet het wat beloofd is?
De opdracht is de commitboodschap en `uitslag.md`: elk haalbaar gewricht in Figure from rig, op een vaste testset in Blender 4.2, 5.2 en 5.3.

| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | Volgens `uitslag.md` halen 5.2.3 en 5.3.0 elk 60 van 60 gewrichten met 0 slechte sneden. De code past bij de verklaring: H wordt een voxelvorm, en een mislukte vereniging valt terug op de oude weg. | Feit voor de tekst en de code, vermoeden voor de cijfers zelf | midden | De JSON-uitslagen op tak `betrouwbaar-uitslag` bij de genoemde runs, of een groene run op de uiteindelijke main. |
| 2 | Blender 4.2 haalt maar 51 van 60, tegen een doel van 9 per figuur. `uitslag.md` zegt dat eerlijk en geeft de reden, een eigen spoor voor de Exact-snede van het scharnier. | Feit | hoog | Geen actie nodig. De koper krijgt in `redenen.py` een zin met wat hij kan doen. |
| 3 | De commitboodschap noemt "PRO_VERSIE 1.2.3", maar geen versiebestand (manifest, `PRO_VERSIE`, Pro-releasenote) staat in de lijst gewijzigde bestanden. | Vermoeden | midden | Een diff van het versiebestand, of `toets_zips.py` groen op de Pro-zip met versie 1.2.3. |
| 4 | De cijfers komen uit runs op verschillende tak-commits (0eb3510, 183fae2, 1945f46, 6dc00b2). Geen enkele run staat letterlijk op de squash-commit 14e6e42. | Vermoeden | laag | Eén groene run van `betrouwbaar-rig.yml` op 14e6e42, of een bewijs dat de inhoud gelijk is aan de laatste takstand. |

## Deel B: houdt het zich aan onze regels?

| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | `architectuur.md` is bijgewerkt voor `omhulsel`, `herstel`, `redenen`, de testset en de nieuwe toets `CJ_HERKANS=3`. | Feit | hoog | architectuur.md bijgewerkt |
| 2 | Alle bestanden blijven onder ±400 regels (`meet_diag.py` is het langst met ±280). | Feit | hoog | bestanden onder ±400 regels |
| 3 | `meet_drempel.json` zet de ondergrens voor 4.2 op de gemeten stand (robot 6 in plaats van 9). Dat is een nieuwe test die eerlijk is uitgelegd, geen bestaande test die is verlaagd. Het is wel een vangnet tegen terugval, geen bewijs dat het goed is. | Feit | hoog | tests niet aangepast om te slagen |
| 4 | De cijfers in `uitslag.md` en `architectuur.md` zijn gemarkeerd met GEZIEN of GOK. De verklaring "volgorde van het parallelle rekenwerk" staat terecht als GOK. | Feit | hoog | cijfers met GEZIEN/DERDEN/GOK |
| 5 | De commit zegt "releasenote gekeurd (Claude)", terwijl `uitslag.md` zegt "Keuring: nog niet gedaan". De releasenote zelf staat niet in deze wijziging. Een keuring door de bouwer telt niet. | Feit voor de tegenstrijdigheid, vermoeden voor de releasenote | midden | keurder is niet de bouwer |
| 6 | `bouw_meshy` in `meet_rig.py` gebruikt een Meshy-figuur waarvan de licentie niet is nagelezen. Het zit bewust niet in de testset. In `uitslag.md` staat de Meshy knight wel in de gewone e2e. | Feit | midden | eigen of vrije figuren |
| 7 | Geen persoonsgegevens, sleutels of wachtwoorden gezien. | Feit | midden | geen persoonsgegevens |

## Deel C: zou een gebruiker het leuk en fijn vinden?

| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | In 4.2 is Figure from rig 2 tot 3,6 keer trager op lichte figuren (rigify 64 naar 230 s, mens 84 naar 165 s). Het is niet te zien of de knop voortgang toont. | Een voortgangsregel of een melding vooraf ("kan enkele minuten duren in Blender 4.2"). | klein |
| 2 | De nieuwe redenen in de lijst "Skipped" zeggen wat de koper kan doen ("place it by hand a few mm along the bone"). Dat is een duidelijke verbetering, maar de tekst is nooit getoond. | Laat Daan of Iris de zinnen in het paneel bekijken. | klein |
| 3 | In 4.2 raken nog steeds gewrichten overgeslagen (robot 6 van 9). De tip om een nieuwere Blender te gebruiken helpt alleen wie kan wisselen. | Zet in de Superhive-beschrijving dat Figure from rig het best werkt in Blender 5.2 of nieuwer. | klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Bevestig dat het versiebestand en de Pro-releasenote van 1.2.3 echt in de uitgebrachte zip zitten (A3, B5). De lijst gewijzigde bestanden laat ze niet zien.
- Laat één groene run draaien op 14e6e42 zelf en zet die in `uitslag.md` (A4).
- Corrigeer de zin "releasenote gekeurd (Claude)" of laat een andere keurder de releasenote lezen (B5).
- Voeg een melding of voortgang toe voor de lange tijd in 4.2 (C1).
- Laat Daan of Iris de nieuwe tekst in het paneel bekijken (C2).
- De Meshy-licentie nalezen voordat die figuur ergens in een testset komt (B6).

---
Automatische keurder, model `claude-sonnet-5-5`, 58226 tokens in, 6629 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
