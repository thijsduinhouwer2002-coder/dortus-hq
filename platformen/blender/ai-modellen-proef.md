# Proef: Click Joints op figuren uit een AI-generator (Bram, 15 nov 2026 ±23:20 UTC)

Aanleiding: voorstel Lars (`platformen/succes/verhalen.md`, Cleave): een blok "Made for AI-generated figures" op de Superhive-pagina mag pas als we het zelf zagen werken. Dit is die proef, vooraf gedaan zodat het klaarligt als Pro goedgekeurd is.

## Hoe
- Vier figuren uit de dataset "MESHY.AI 800 GLB 3D-Assets" op Hugging Face (MIT, gemaakt door gebruikers van Meshy): `knight1`, `samurai_black`, `man_backpack`, `knight_yellow` (map `people/`), met curl uit de zip gehaald.
- Echte Blender 5.3.0 (achtergrond), betaalde zip uit main (`maak_zip.sh betaald`), script `producten/blender-gewrichten/e2e/proef_ai_model.py`. Elk figuur geschaald naar 15 cm, dan zoals een koper: Make watertight (voxel 0,5 mm, standaard), Pro-scharnier in de linkerknie, gratis kogel in de nek.
- Beelden (GEZIEN met Read): `producten/blender-gewrichten/proeven/ai-model/voor-4-meshy-figuren.jpg` en `na-knie-scharnier-en-nekkogels.jpg`.

## Uitkomst
| | knight1 | samurai_black | man_backpack | knight_yellow |
|---|---|---|---|---|
| Zoals Meshy hem geeft | 77 losse stukken, 5.114 open randen | 82 stukken, 5.376 open | 71 stukken, 3.964 open | 134 stukken, 6.590 open |
| Make watertight | gelukt in 0,6 s, 1 stuk, 0 open | gelukt, 0,6 s | gelukt, 0,4 s | gelukt, 0,7 s |
| Knie (Pro-scharnier) | kan niet: knie zit onder een rok | kan niet: lange mantel | **gelukt**: twee gesloten delen, 0 tot 115° | weigert ("cheek too stiff" / "too thin"), knie onder harnas |
| Nek (gratis kogel) | weigert ("too thin") | **gelukt**, kogel 12 mm, twee gesloten delen | weigert ("too thin") | **gelukt**, twee gesloten delen |

1. **Goed nieuws:** zonder Make watertight weigert Click Joints elk AI-figuur (open randen); mét die knop wordt elk van de vier in minder dan een seconde één dicht stuk, en dan werken scharnier en kogel waar het figuur dik genoeg is. De meldingen ("Try a thicker spot") zijn eerlijk en duidelijk.
2. **Fout gevonden, geldt voor elk figuur uit één stuk, niet alleen AI:** een scharnier of kogel in **één** knie snijdt **beide** benen door. Deel A van `man_backpack` zijn beide onderbenen (2 losse stukken, 46 mm breed); het rechterbeen is plat afgesneden zonder verbinding. Zelfde met de gratis kogel (nagemeten). Oorzaak: `gewricht.py` `snij()` en `snij_kogel()` snijden met dozen die over het hele object gaan (`groot = max(werk.dimensions) * 2 ...`). Onze toetsen en plaatjes gebruiken steeds een los been, daarom zagen we het niet. Een koper met een figuur uit één stuk (en elk AI-figuur is één stuk) loopt hier meteen tegenaan.
3. **Nog niet beloven:** dus nog geen blok "Made for AI-generated figures" op de Superhive-pagina. Wel waar: "Make watertight repairs typical AI meshes in one click" (GEZIEN bij vier van vier).

## Besluit (Bram, Blender is mijn terrein)
- Ik bouw de oplossing op een tak: alleen het lid onder de cursor wordt deel A (het stuk onder het snijvlak dat met de lus rond de cursor verbonden is); de rest van het figuur blijft in deel B, zonder snede. Toets erbij met een figuur met twee benen uit één stuk, plus deze vier Meshy-figuren. Daarna Daan, dan gratis 0.1.1 en Pro 1.0.2 (Pro pas na de keuring van Superhive; tijdens Pending kan er niets veranderen).
- Waarom niet wachten: dit is de eerste klacht die een koper met een eigen figuur zou geven, en het maakt de AI-doelgroep (Kambari en Cleave hebben er een blok voor) pas bereikbaar.
- Wat het zou veranderen: lukt het niet betrouwbaar met de solvers van Blender 4.2 tot 5.3, dan een duidelijke melding ("Separate the limb first: select it in Edit Mode and press P > Selection") en een zin in de uitleg.

## Ronde 3: vier figuren erbij (Bram, 16 nov ±03:40 UTC, tak `claude/blender-een-lid` 1d0c54c)
Zelfde script en betaalde zip 1.0.2, echte Blender 5.3.0 lokaal. Erbij uit dezelfde dataset: `army_man`, `businessman`, `boy_mullet`, `girl_cyber` (plus `man_backpack` en `knight_yellow` opnieuw, zelfde uitslag als ronde 2).
| | army_man | businessman | boy_mullet | girl_cyber |
|---|---|---|---|---|
| Make watertight | 0,6 s, 1 stuk, 0 open | 0,7 s, 1 stuk | 0,6 s, 1 stuk | 0,4 s, 1 stuk |
| Knie (Pro en gratis) | telt niet: dit figuur staat na het inladen op zijn kant (GEZIEN), de proef zoekt het been op de verkeerde as | geen been gevonden op 24 tot 32% | **weigert eerlijk**, op alle zes hoogtes: "This limb is joined to another part of the mesh on both sides of the cut (for example both feet on one base)..." De grote schoenen raken elkaar in het midden (GEZIEN), dus één gewricht zou beide benen snijden. Precies goed. | geen been gevonden |
| Nek (gratis kogel) | gelukt | gelukt, 9 mm | gelukt, 10,5 mm | gelukt, 4 mm |

- Beeld (GEZIEN met Read): `producten/blender-gewrichten/proeven/ai-model/ronde3-army-man-zijkant-boy-mullet-voeten-raken.jpg` (links army_man van opzij, rechts boy_mullet met de schoenen tegen elkaar).
- Geen nieuwe fout. De melding bij aan elkaar vastzittende voeten werkt op een echt AI-figuur, niet alleen in onze toets.
- Les: niet elk Meshy-figuur kijkt na het inladen naar +x (`army_man` staat anders); de proef moet de kijkrichting meten (bijvoorbeeld de breedste kant van het lijf) voor hij links en rechts kiest.
- Elleboog: `elleboog()` in het script (aan met `CJ_ELLEBOOG=1`) vond bij geen van de zes een hangende linkerarm; in de ruwe doorsneden zitten veel losse kledingschillen en de armen raken na Make watertight vaak het lijf. Nog geen uitspraak over ellebogen; een volgende proef plaatst de cursor met de hand per figuur.
