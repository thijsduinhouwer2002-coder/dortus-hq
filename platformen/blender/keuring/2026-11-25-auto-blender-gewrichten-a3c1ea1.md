# Keuring blender-gewrichten, paneelvolgorde en beoordelingsregel (Pro 1.2.9, issue 70), 25-11-2026, automatische keurder
Wat ik keurde: commit a3c1ea1c9 (ae91289..a3c1ea1), alleen de tekst van de wijziging. Ik zag geen e2e-uitslag, geen schermen en geen bestand buiten de diff.
Akkoord: nee

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | Figure from rig staat nu bovenaan het hoofdpaneel, alleen als het actieve mesh een rig heeft (`teken_boven` met `rig.zoek_armature`). | Feit | hoog | Staat in de diff. De test `paneel met rig: Figure from rig vóór stap 1` toetst het. |
| 2 | Proefstrip staat in stap 2 onder Clearance, scharnier onder Place joint, scharnierbereik in stap 3. Dat past bij Daans regel "per stap alleen wat je dan nodig hebt". | Feit | hoog | Diff van `paneel.py` en de volgorde in `toetsen_paneel.py`. |
| 3 | De regel "Happy with it? Leave a rating:" verschijnt zodra een object in de scène `cj_passing == "groen"` heeft. Of de echte code die eigenschap zo zet, zie ik niet. De test zet hem zelf met de hand. | Vermoeden | midden | `gewricht.py`/`passing.py` tonen dat `cj_passing` op het deel of op het object staat, en een e2e-stap die na een echte Place joint de regel toont. |
| 4 | Het versienummer 1.2.9 staat in de commit, maar `blender_manifest.toml` of het bouwscript staat niet in de gewijzigde bestanden. | Vermoeden | midden | Een diff of build die laat zien dat de zip `click_joints_pro-1.2.9.zip` heet. |
| 5 | Ik zag geen uitslag van de e2e-run met `toetsen_paneel.py`. De test hangt af van de exacte knopteksten (zoals "Export") en van `bl_idname` van de rig-operator. | Vermoeden | midden | Groene run in 4.2, 5.2 en 5.3. |
| 6 | De links (extensions.blender.org/.../reviews/ en Gumroad) zijn volgens de commentaar met curl nagekeken (200). Dat kon ik niet zelf zien. Of de Extensions-pagina al bestaat, weet ik ook niet. | Vermoeden | laag | `curl -I` op beide links door de keurder. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | `meld.py` staat in de kern en dus in de gratis zip. Daar staan nu "Pro", Superhive, Gumroad en een link naar `click-joints-pro` in als code (`BEOORDEEL_PRO`, `"Pro" in naam`). De gratis build toont ze niet, maar het bestand verwijst wel naar de betaalde versie. Architectuur.md zegt dat de kern de betaalde naam niet mag noemen en dat `toets_zips` dat bewaakt. | Feit dat de strings in de kern staan; vermoeden dat `toets_zips` er rood van wordt | midden | Gratis versie zonder verwijzing naar betaald (ontwerp, regels 3.3 en 3.10 van extensions.blender.org); `toets_zips` groen. |
| 2 | `architectuur.md` is niet aangepast. Er is een nieuw plekkenmechanisme in `paneel.py` (BOVEN, STAP2, STAP2_KEUS, STAP3, `teken`), een beoordelingsregel in `meld.py` en een andere plek voor het Pro-deel. De bestandenlijst is volledig ("niets niet meegestuurd"). | Feit | hoog | architectuur.md bijgewerkt. |
| 3 | De nieuwe test is een extra bestand en past geen bestaande test aan. De wijziging in `test_betaald.py` is een toevoeging. | Feit | hoog | Tests niet aangepast om te slagen: in orde. |
| 4 | De CHANGELOG (gratis) noemt de beoordelingsregel niet, terwijl de gratis build hem toont. | Feit | hoog | CHANGELOG voedt de release notes, regel per gebruikerskant. |
| 5 | Bestandslengte onder 400 regels kan ik niet zien, want de regeltotalen ontbreken. | Vermoeden | laag | `wc -l` op `figuur.py`, `paneel.py` en `test_betaald.py`. |
| 6 | Geen persoonsgegevens of sleutels gezien. Wel twee openbare winkel-URL's in `meld.py`. | Feit | hoog | Geen persoonsgegevens. |

## Deel C: zou een gebruiker het leuk en fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | Het paneel volgt nu de flow en Figure from rig is de eerste knop bij een rig. Dat is een duidelijke verbetering ten opzichte van een tweede paneel onder ±880 px. Of het er mooi uitziet, kan ik niet zien (vermoeden). | Daan bekijkt het e2e-scherm van het paneel met een rig. | klein |
| 2 | Stap 2 wordt langer: schuif, proefstrip met twee knoppen, Place joint, scharnier met drie standen en Flip bend. De "grote knop per stap" van Daan zit nu tussen veel kleine knoppen. De knoppen "Fit test: ball" en "Fit test: hinge" naast elkaar kunnen in een smalle zijbalk afkappen (vermoeden). | Bekijk het in een smal paneel; zet eventueel de proefstrip in een inklapbaar subpaneeltje. | klein |
| 3 | De beoordelingsregel staat er zolang er ergens een groen gewricht in de scène is, bij elke sessie, zonder weg te klikken. Dat wordt snel een zeurende regel. | Eén keer per sessie, of na de eerste export, of met een "Don't show again". | klein |
| 4 | `goed_resultaat` loopt bij elke herteken over alle objecten van de scène. In een scène met honderden objecten en geen groen gewricht kost dat elke keer tijd (vermoeden). | Alleen controleren na Place joint en het resultaat in een scene-eigenschap bewaren. | klein |

## Deel C: is het goed genoeg?
Deze wijziging bevat geen beeld, hoofdplaatje of thumbnail, dus de blinde test geldt niet. Ik kan het paneel niet zien en geef daarom geen cijfers. Dat is geen oordeel dat het goed is.
| Vraag | Cijfer 1 tot 10 | Waarom, en waarmee vergeleken |
|---|---|---|
| Ziet het er top uit, op het niveau van de beste in de winkel? | niet te geven | Alleen tekst gezien. Daan moet het e2e-scherm naast de panelen van Cleave en Split 3D Print leggen. |
| Zou ik het zelf kopen of bekijken op basis van dit? | niet te geven | Zelfde reden. |
| Zou Thijs er trots op zijn? | niet te geven | Zelfde reden. |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet**
1. Haal de Pro-, Superhive- en Gumroad-gegevens uit `meld.py` (kern, gratis zip). Zet `BEOORDEEL_PRO` en de Pro-keuze in de betaalde map en laat de kern alleen de gratis link kennen, bijvoorbeeld met een lijst die het betaalde deel erbij zet. Of toon met een groene `toets_zips` en de run dat de gratis zip geen Pro-verwijzing bevat. Dit is deel B 1.
2. Werk `architectuur.md` bij: de paneelplekken, de beoordelingsregel en de plek van het Pro-deel. Dit is deel B 2.

**Kan**
- Voeg de beoordelingsregel toe aan de CHANGELOG (Unreleased, gratis), en controleer dat de zip echt 1.2.9 heet (A4).
- Toon de beoordelingsregel niet permanent (C3) en bewaar het resultaat in plaats van elke herteken te scannen (C4).
- Wacht op een groene e2e-run met `toetsen_paneel.py` in drie Blender-versies (A5) en vraag Daan de panelen met en zonder rig te bekijken (C1, C2). Voor Pro 1.2.9 uitkomt is een nieuw akkoord nodig, want het ja in `ontwerp.md` geldt voor 1.2.8.
- Controleer de twee beoordelingslinks zelf met `curl` (A6).

---
Automatische keurder, model `claude-sonnet-5-5`, 27866 tokens in, 8765 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
