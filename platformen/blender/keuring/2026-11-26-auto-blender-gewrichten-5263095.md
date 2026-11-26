# Keuring blender-gewrichten: gevonden worden in de lat (#161), 26-11-2026, automatische keurder
Wat ik keurde: commit 52630959d (KAART.md, zoek_gumroad.py, zoek_superhive.py; uitslag-2026-11-26.json kreeg ik niet te zien, die is te groot)
Akkoord: nee

## Deel A: doet het wat beloofd is?
De opdracht is het commitbericht en de KAART-regel: plek per zoekterm op Superhive en Gumroad, tags en categorie van de top 3, markten, en een voorstel voor tags, categorie en titel.

| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | KAART verwijst naar `platformen/blender/vindbaar-voorstel-2026-11-26.md` en naar keuring Daan #167, met plakken vóór vr 27 nov 12:00. Dat voorstelbestand zit niet in deze wijziging. | Feit (niet in de lijst met gewijzigde bestanden) | Midden | Het bestand staat al op main, of komt in een volgende commit. Dan vervalt dit punt. |
| 2 | De scripts meten alleen de plek per zoekterm. Er is geen script of bestand dat tags en categorie van de top 3 of de markten ophaalt. Dat deel is dus niet te herhalen of na te kijken. | Feit (alleen deze twee scripts) | Midden | Een bestand of script met die gegevens, of een uitleg in de KAART over hoe ze zijn verzameld. |
| 3 | De claims "Superhive plek 32 op articulated" en "niet gevonden op action figure blender" staan als GEZIEN, maar ik kon de uitslag niet lezen. Het script kijkt maar 4 pagina's diep. "Niet gevonden" betekent dus alleen "niet in de eerste 4 pagina's". | Vermoeden | Midden | Het aantal `n` per term in uitslag-superhive.json. De KAART moet het "niet in de top N" noemen. |
| 4 | "Eis $100 omzet plus ±3 weken voor Gumroad Discover" staat als DERDEN zonder link naar de bron. | Feit (geen bron genoemd) | Hoog | Een link naar de Gumroad-pagina met die voorwaarde. |
| 5 | Het Superhive-script zoekt met `v in lijst`, dus een exacte slug. `"jointlab-"` (eindigt op een streepje) en het geraden `click-joints-lite` matchen dan mogelijk nooit. Het resultaat wordt dan "None", wat op "niet gevonden" lijkt. | Vermoeden | Laag | Een run waarin de eigen slug `click-joints-pro` en `jointlab-` wel een plek krijgen. |

## Deel B: houdt het zich aan onze regels?

| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Alle bestanden zijn ruim onder de 400 regels. De scripts zijn 19 en 24 regels. | Feit | Hoog | Bestandsgrootte |
| 2 | Er is geen testwijziging en geen productcode veranderd. `architectuur.md` bijwerken is hier niet nodig. | Feit | Hoog | Tests en architectuur |
| 3 | De cijfers in de KAART hebben een label (GEZIEN of DERDEN). Het DERDEN-cijfer mist de bron (zie A4). | Feit | Hoog | Cijfers met GEZIEN, DERDEN of GOK |
| 4 | De scripts doen zich voor als een Chrome-browser (`User-Agent`) en wachten niet tussen verzoeken. Dat kan tegen de gebruiksvoorwaarden van de winkels ingaan of tot blokkades leiden. | Vermoeden | Laag | Geen vaste regel, wel voorzichtigheid |
| 5 | Het Gumroad-script heeft geen foutafhandeling: `d["total"]` crasht bij een niet-JSON-antwoord, bijvoorbeeld bij een blokkade. De uitvoerbestanden komen in de huidige map terecht, niet in `vindbaar/`. De namen wijken af van het bestand `uitslag-2026-11-26.json`. | Feit (uit de code) | Midden | Herhaalbaarheid |
| 6 | Persoonsgegevens, sleutels of wachtwoorden zag ik in de gestuurde tekst niet. Het JSON-bestand kon ik niet nalezen. Daar kunnen verkopersnamen in staan. | Vermoeden | Laag | Geen persoonsgegevens |

## Deel C: zou een gebruiker het leuk en fijn vinden?
Niet van toepassing: dit is intern onderzoek, niets wat een koper of speler ziet. Het voorstel voor titel en tags is wel voor klanten bedoeld, maar ontbreekt in deze wijziging (zie A1). Daan keurt dat in #167.

## Deel C: is het goed genoeg?
Geen cijfers, omdat er geen beeld, video, winkeltekst of spel van de klant in deze wijziging zit. De blinde test is niet van toepassing. Voor de titel en tags uit het voorstel geldt de cijferlat alsnog, zodra die er zijn.

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet**
- Het voorstelbestand (`vindbaar-voorstel-2026-11-26.md`) hoort bij deze wijziging, want de KAART en de deadline vr 12:00 hangen eraan. Voeg het toe, of laat zien dat het al op main staat (A1).
- Leg vast waar de tags, categorieën en markten van de top 3 vandaan komen, als bestand of als zin in de KAART. Nu is dat deel van de belofte niet na te kijken (A2).

**Kan**
- Noem bij "niet gevonden" hoe diep gezocht is (4 pagina's Superhive, 90 resultaten Gumroad) (A3).
- Zet een bronlink bij de Gumroad-eis van $100 en ±3 weken (A4).
- Gebruik exacte slugs in `volg` en toets dat de eigen slug een plek geeft (A5).
- Voeg foutafhandeling, een korte pauze tussen verzoeken en een vaste uitvoermap toe (B4, B5).
- Controleer dat uitslag-2026-11-26.json geen persoonsgegevens bevat (B6).

---
Automatische keurder, model `claude-sonnet-5-5`, 20508 tokens in, 4530 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
