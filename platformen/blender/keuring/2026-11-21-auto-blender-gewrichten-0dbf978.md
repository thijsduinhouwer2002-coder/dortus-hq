# Keuring Direct-zip met Pro-knoppen op slot (blender-gewrichten), 21-11-2026, automatische keurder
Wat ik keurde: commits 45fadb84d en c368201fa (0827e42..0dbf978), zeven bestanden onder producten/blender-gewrichten/
Akkoord: ja

## Deel A: doet het wat beloofd is?
De opdracht in ontwerp.md gaat over de gratis Click Joints 0.1.1 en Pro 1.0.2. De direct-zip staat daar niet in. Ik toets daarom tegen de eigen belofte in architectuur.md: de extensions-zip blijft gelijk, de direct-zip is gratis plus Pro-knoppen op slot.

| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | `maak_zip.sh` laat de gratis en betaalde tak ongemoeid en voegt alleen een tak `direct` toe. De extensions-zip kan dus niet veranderen. | Feit (uit de diff) | hoog | Een run van `toets_zips.py` die groen blijft. |
| 2 | `toets_direct_zip.py` controleert dat de extensions-zip "Pro" nergens noemt en geen `direct.py` heeft. Hij controleert ook dat de direct-zip precies de gratis zip plus `direct.py` is, met `__init__.py` gelijk aan het origineel plus het fragment. Zo is de regel "geen verwijzing naar betaald op extensions.blender.org" afgedekt. | Feit | hoog | Een groene run van deze toets. |
| 3 | `direct.py` heeft drie slotknoppen, een venstertje en "Upgrade to Pro". Alles gaat via `wm.url_open` naar dortus.com/click-joints/ en er staat geen prijs in. Dat past bij de beschrijving. | Feit (uit de code) | hoog | Zie #5. |
| 4 | De nieuwe knoppen staan volgens de beschrijving boven "Report a problem" en niet erboven of ertussen. Dat volgt uit hoe Blender subpanelen tekent. | Vermoeden | midden | Het scherm `d1-slot-paneel` uit `scherm_direct.py`. |
| 5 | De opdracht noemt de direct-zip niet. Daan keurt het uiterlijk van de nieuwe Pro-knoppen nog niet, en een ja van Thijs voor een Pro-aanbieding in de gratis download staat niet in de tekst. | Feit (afwezigheid in de tekst) | midden | Een regel in `ontwerp.md` of een bericht met Thijs' ja en Daans blik op `d1-slot`. |

## Deel B: houdt het zich aan onze regels?

| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Alle nieuwe bestanden zijn kort (onder 100 regels). Er zijn geen bestaande tests aangepast, alleen nieuwe toevoegd. | Feit | hoog | Bestanden onder ±400 regels en tests niet aangepast om te slagen |
| 2 | `architectuur.md` is bijgewerkt met de nieuwe sectie "Direct-zip". | Feit | hoog | architectuur.md bijgewerkt |
| 3 | Er staan geen persoonsgegevens, sleutels of cijfers zonder bron in de wijziging. | Feit | hoog | Geen persoonsgegevens, GEZIEN/DERDEN/GOK |
| 4 | De sectie noemt een workflowstap "Direct-zip" in drie Blender-versies, een artefact en een grep op de extensions-zip. Er is geen workflowbestand meegestuurd. Misschien filtert de lijst alleen op deze productmap, misschien ontbreekt de wijziging. Zonder die stap draaien `test_direct.py` en `scherm_direct.py` niet in CI en is er geen groene run. | Vermoeden | midden | architectuur.md moet kloppen met de werkelijkheid |
| 5 | Geen AI-beeld of -geluid en geen spelerstekst van Hats. Niet van toepassing. | Feit | hoog | Overige regels |

## Deel C: zou een gebruiker het leuk en fijn vinden?
Ik kan het scherm niet zien. Dit zijn vermoedens uit de code.

| # | Bevinding | Wat het beter maakt | Moeite (klein/midden/groot) |
|---|---|---|---|
| 1 | Drie knoppen met slot plus nog een "Upgrade to Pro" onder één klein vak kan opdringerig voelen. Dat zijn vier plekken voor dezelfde boodschap. | Alleen de drie slotknoppen houden, of alleen de upgradeknop. | klein |
| 2 | Een klik op een slot geeft een venstertje met één knop. Daar kan een gebruiker geen functie uitproberen. | Een korte regel per functie wat het doet, bijvoorbeeld bij "Hinge with end stop" dat het voor knie en elleboog is. | klein |
| 3 | Het venster hangt bij de muis. Onder Xvfb lukt dat niet altijd, zegt de scherm-test zelf. | Kijk het na op een echt scherm. | klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Bevestig dat de workflow `Direct-zip` en de grep echt in de repo staan (zie B4). Zonder die stap bewijst alleen `toets_direct_zip.py` iets als je hem zelf draait. Groen vinkje van de volledige run met `test_direct.py` en `scherm_direct.py` afwachten.
- Leg de direct-zip kort vast in `ontwerp.md`, met Thijs' ja. Laat Daan `d1-slot` bekijken voordat de zip ergens live gaat (A5).
- Zorg dat de directe download en de extensions-zip niet door elkaar kunnen komen bij het uploaden. De toets bewaakt de inhoud van de zip, maar niet welk bestand je uploadt. Een duidelijke bestandsnaam of releasechecklist helpt.
- Een paar operatornamen in `test_direct.py` (bijvoorbeeld `figuur_uit_rig`, `controleer`) zijn uit de diff niet te controleren. Een verkeerde naam in de lijst "geen betaalde operator" zou die controle leeg maken.

---
Automatische keurder, model `claude-sonnet-5-5`, 27038 tokens in, 5371 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
