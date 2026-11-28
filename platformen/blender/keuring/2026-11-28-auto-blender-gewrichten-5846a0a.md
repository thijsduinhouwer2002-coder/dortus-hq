# Keuring blender-gewrichten plakkaart gratis 0.1.3, 28-11-2026, automatische keurder
Wat ik keurde: commit 5846a0a97 (bestanden `producten/blender-gewrichten/KAART.md` en `producten/blender-gewrichten/winkel/plak-gratis-0.1.3.md`)
Akkoord: ja

## Deel A: doet het wat beloofd is?
Toetsmaat: Daan M1 (#340), dus Superhive Lite krijgt de extensions-zip in plaats van de direct-zip, omdat de Lite-zin dezelfde code als extensions.blender.org belooft.

| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De wijziging doet wat M1 vraagt. In de zipstabel gaat de extensions-zip nu naar extensions.blender.org en Superhive Lite, de direct-zip naar dortus.com, Gumroad en Printables. | Feit (uit de tekst) | hoog | Niets nodig. |
| 2 | De plakkaart is intern consistent: volgorde (stap 3 Lite, stap 4 de rest), tabelrij "Waar naartoe", nieuw blok in deel 3 en de verplaatste Lite-regel kloppen met elkaar. De ontbrekende regel "Superhive Lite" in de oude stap 3 is weg. | Feit | hoog | Niets nodig. |
| 3 | De regel dat 0.1.2 "in geen winkel behalve Printables" staat, klopt met KAART.md en de tabel. | Feit (uit de tekst) | midden | De claim over Printables (direct-zip 0.1.2, 27 nov) komt uit `commercie/geplaatst.md`, dat ik niet zag. |
| 4 | Dat Superhive voor Lite een nieuwe versie 0.1.3 toelaat naast Pro 1.2.9, staat er als gewoonte ("zoals bij Pro"). Ik kan niet zien of dat voor deze licentievariant echt zo werkt. | Vermoeden | laag | Eén keer in het Superhive-formulier kijken voor Lite, of een eerdere Lite-update in `commercie/geplaatst.md`. |
| 5 | De Lite-zin wordt "same code as the free Click Joints 0.1.3 on extensions.blender.org". De controle-stap erkent zelf dat 0.1.3 daar dagen op `WACHT` kan staan. Tot die tijd noemt Lite een versie die daar nog niet staat. | Feit (uit de tekst) | hoog | Zin zonder versienummer, of Lite pas bijwerken na goedkeuring door de moderator. |

## Deel B: houdt het zich aan onze regels?

| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Er is alleen markdown gewijzigd. Er is geen code en geen test aangepast. | Feit | hoog | Tests niet aangepast om te slagen: niet van toepassing. |
| 2 | Er staan geen persoonsgegevens, sleutels of wachtwoorden in de wijziging. De sha256's zijn bestandshashes. | Feit | hoog | Geen persoonsgegevens. |
| 3 | De nieuwe beweringen dragen een label (GEZIEN met curl, tijd en bron). Ik kon ze zelf niet narekenen. | Feit dat het label er staat | midden | Cijfers met GEZIEN/DERDEN/GOK. |
| 4 | Het controlescript `controle-gratis-0.1.3.sh` zit niet in deze wijziging. De plakkaart eist nog steeds `ALLES GOED`. Controleert het script Lite op de direct-zip, dan geeft het na deze wijziging ten onrechte FOUT. | Vermoeden | laag | Script lezen op de Lite-regel (zip en versie). Niet te zien in de tekst. |
| 5 | Er is geen bestand boven ±400 regels en geen wijziging in `architectuur.md`. Er is geen beeld of geluid toegevoegd. | Feit | midden | Bestandsgrootte, architectuur, AI-beeld: geen aanleiding. |

## Deel C: zou een gebruiker het leuk en fijn vinden?
Niet te zien: dit is een interne plakkaart zonder beeld of spel. Voor de koper is wel belangrijk dat Lite-kopers geen slotjes en "Upgrade to Pro" zien, en dat lost de wijziging op.

| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | Een Lite-koper krijgt straks dezelfde zip als de gratis versie op Blender Extensions, zonder verkooppraat. Dat past bij de belofte in de Lite-zin. | Niets nodig. | klein |

## Deel C: is het goed genoeg?
Niet van toepassing. De wijziging bevat niets dat een klant als eerste ziet (geen hoofdbeeld, omslag of thumbnail). Er is dus geen blinde test en geen cijferlijst nodig.

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
1. Haal het versienummer uit de Lite-zin, of plak Lite pas nadat extensions.blender.org 0.1.3 heeft goedgekeurd. Tot die tijd klopt "0.1.3 on extensions.blender.org" niet (deel A, punt 5).
2. Controleer of `controle-gratis-0.1.3.sh` Lite op de extensions-zip toetst (deel B, punt 4). Anders blokkeert stap 5 straks onterecht.
3. Bevestig in het Superhive-formulier dat Lite een eigen versie 0.1.3 kan krijgen naast Pro 1.2.9 (deel A, punt 4).

---
Automatische keurder, model `claude-sonnet-5-5`, 22561 tokens in, 3754 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
