# Vindbaarheid gratis Click Joints op extensions.blender.org (Verspreider, 23 nov 2026)

**Waarom deze plek eerst (geld):** de gratis versie is de trechter naar Pro, en haar downloads komen vooral uit het zoeken in de winkel en in Blender zelf (Get Extensions gebruikt dezelfde catalogus). Per dag komen er 11 tot 28 bij zonder dat we iets plaatsen: 19 nov +11, 20 nov +16, 21 nov +21, 22 nov +28 (GEZIEN, `organisatie/scorebord-data.csv`). Op 18 nov +43, de dag dat BlenderNation ons bericht plaatste (DERDEN, https://www.blendernation.com/2026/11/18/click-joints-free-add-on-that-cuts-printable-ball-joints-and-shows-how-far-they-bend/). Nu 342 downloads (GEZIEN, productpagina 23 nov ±12:00 UTC). Elk zoekwoord waarop we onzichtbaar zijn, kost dus elke dag mensen. Eén zin aanpassen kost ±2 minuten en kan mee in een stap die al op de lijst van Thijs staat (punt 3b, zelfde beheerpagina).

## Wat ik mat (GEZIEN, 23 nov ±12:00 UTC)
De zoekfunctie `https://extensions.blender.org/search/?q=<woord>&type=add-ons`, eerste twee pagina's (16 per pagina). Getest: de zoek kijkt ook in de lange beschrijving, niet alleen in naam en tagline. Bewijs: op "watertight" staan we 1e en dat woord staat alleen in de beschrijving.

| Zoekwoord | Onze plek | Aantal treffers | Wie er staat |
|---|---|---|---|
| joint / joints | 1 | 15 | wij, linkforge, better-ragdoll |
| ball joint | 1 | 1 | alleen wij |
| ball and socket | 1 | 2 | |
| range of motion | 1 | 24 | |
| poseable | 1 | | |
| printable | 5 | 14 | |
| figure | 7 | 16 | |
| 3d printable | 8 | 11 | |
| stl | 17 | 27 | |
| **articulated** | **niet** | 3 | linkforge, dynamic-skinning, smear |
| **action figure** | **niet** | 1 | gp-select |
| **toy / toys** | **niet** | 1 | gta-sa-toolkit |
| **figurine** | **niet** | 1 | boardtyper-3d |
| **doll** | **niet** | 32 | vooral camera's (de zoek maakt er "dolly" van) |
| **posable** | **niet** | 12 | |
| **3d print / 3d printing / print** | **niet** in de eerste 32 | 32+ | 3D Print Toolbox, Easy-Print, SnapSplit, MM Caliper |

Les: op de woorden waar weinig add-ons op staan ("articulated", "action figure", "toy", "figurine") zijn we onzichtbaar alleen omdat die woorden niet in onze tekst staan. Wie daar zoekt, zoekt precies ons. Op de brede woorden ("3d print") winnen add-ons met duizenden downloads; daar helpt de nieuwe tagline van 0.1.2 (staat al klaar, zie onder).

## Voorstel 1: eerste zin van de beschrijving (op de beheerpagina, account nodig)
**Nu:**
```
Turn a sculpt into a poseable, printable figure.
```
**Wordt:**
```
Turn a sculpt into an articulated, poseable figure for 3D printing, such as an action figure, a toy, a doll or a figurine.
```
De rest van de beschrijving blijft gelijk. Eén leesbare zin, geen rij zoekwoorden: de regels vragen "an easy-to-read description mentioning everything it does" (DERDEN, https://extensions.blender.org/terms-of-service/ regel 3.1). Klopt met wat de gratis versie doet: een sculpt in delen met kogel of pen, met speling, voor een printbaar figuur. Bewust niet: "hinge" (dat is Pro), "miniature" (te dun voor een kogel, zie de keuring van Daan bij de Pro-zoekwoorden), "clicks" of "snap" (geen klik beloven zonder print), en geen woord over Pro in de zin (regel 6.2 van de Terms of Service; de Pro-zin onderaan uit lijst punt 3b blijft het enige).

**Wie:** Thijs, in dezelfde sessie als lijst punt 3b (beheerpagina van Click Joints, beschrijving). Geen extra punt op de lijst: de hoofdchat voegt deze zin toe aan punt 3b.

**Verwacht effect:** 1e plek op articulated, action figure, toy, figurine (daar staan 1 tot 3 andere add-ons). Hoeveel mensen daarop zoeken weten we niet; GOK: 1 tot 5 downloads per dag erbij, dus ±30 tot 150 per maand. Bij de huidige stand (1 Pro-verkoop op ±340 gratis, GEZIEN scorebord) is dat GOK 0 tot 1 verkoop per maand extra; klein, maar voor 2 minuten werk en blijvend.

## Voorstel 2: tagline bij de volgende versie (al gekeurd, niets nieuws)
De tagline van 0.1.2 staat klaar en is gekeurd: `Ball joints for poseable 3D print figures, with bend range` (`platformen/blender/keuring/2026-11-19-click-joints-0.1.2-daan.md`). Die zet "3D print" letterlijk in de korte regel; nu staat er "3D printed" en daarop vinden de zoekers ons niet. Verandert alleen met een nieuwe upload (token of account van Thijs). Ik voeg niets toe; wel de vraag aan de hoofdchat: 0.1.2 met deze tagline vóór de sale uitbrengen als dat kan, want de woorden in de korte regel wegen bij Blender in Get Extensions het zwaarst (GOK).

## Meten
Een week na de wijziging dezelfde zoekopdrachten opnieuw (lus hieronder) en de downloads per dag naast de week ervoor (scorebord-data.csv).
```
for q in articulated "action figure" toy figurine doll posable "3d print"; do
  curl -s "https://extensions.blender.org/search/?q=$(python3 -c 'import urllib.parse,sys;print(urllib.parse.quote(sys.argv[1]))' "$q")&type=add-ons" \
  | grep -o 'href="/add-ons/[a-z0-9_-]*/"' | awk '!s[$0]++' | grep -n click-joints || echo "$q: niet"
done
```

## Bijvangst: Gumroad Discover helpt in de sale niet
Gumroad zet een product pas in Discover als het account $100 saldo uit echte verkopen heeft en daarna door hun risicokeuring is, "on average 3 weeks after you pass the $100 threshold"; per product daarnaast één verkoop, een categorie en beoordelingen aan (DERDEN, https://gumroad.com/help/article/79-gumroad-discover). Wij staan op $19 (GEZIEN, scorebord 23 nov). Zoeken op "click joints" in Gumroad geeft 114 treffers zonder ons (GEZIEN, gumroad.com/products/search). Gevolg: categorie en tags op Gumroad leveren deze sale niets op; tijd daar later. Lijst punt 3a zegt "een eerste betaling telt mee voor Gumroad Discover": dat klopt pas na die $100 en de keuring.

Keuring: zie onderaan, door een aparte keurder.

## Keuring (aparte keurder, 23 nov 2026)
Wat ik keurde: dit bestand. Zelf gemeten met curl, 23 nov.
Akkoord: nee (één moet, klein)

Deel A
| # | Bevinding | Feit of vermoeden | Zekerheid |
|---|---|---|---|
| 1 | Zoekplekken kloppen: articulated 3 treffers (linkforge, dynamic-skinning, smear), action figure alleen gp-select, toy alleen gta-sa-toolkit, figurine alleen boardtyper-3d, wij nergens; ball joint 1e, joint 1e (15), range of motion 1e (24), figure 7e (16), printable 5e, watertight 1e. "watertight" staat alleen in de beschrijving, niet in de tagline: de zoek leest dus de beschrijving. | feit | hoog |
| 2 | Kleine afwijkingen in aantallen: posable 12 (niet 11), printable 14 (niet 12), doll 32 (niet 30). Waarschijnlijk tijd of telwijze; verandert de les niet. | feit | hoog |
| 3 | Huidige beschrijving en 342 downloads kloppen. | feit | hoog |
| 4 | De nieuwe zin is eerlijk: de gratis versie maakt kogel en kom (of pen en gat) met speling voor een printbaar figuur. Geen hinge, geen klik, geen Pro. "doll" past juist goed (ball-jointed dolls zijn een bekend soort), "toy" ook. Eén leesbare zin, geen rij zoekwoorden: past bij ToS 3.1 en 6.2. | feit | hoog |
| 5 | Gumroad Discover klopt letterlijk: $100 uit echte verkopen, risicokeuring "on average 3 weeks", per product één verkoop, categorie, beoordelingen aan. | feit | hoog |
| 6 | Effect 1 tot 5 per dag staat netjes als GOK. | feit | hoog |

Deel B: geen persoonsgegevens (controle OK), cijfers hebben GEZIEN/DERDEN/GOK, Nederlands zonder gedachtestreepjes, niets geplaatst. Wel: de bronlink bij de regel klopt niet (zie moet).

Deel C: een koper die "action figure" of "doll" zoekt, vindt ons nu niet; met deze zin wel en hij krijgt wat hij zoekt. Goed.

**Moet:**
1. De link https://developer.blender.org/docs/handbook/extensions/moderation_guidelines/ geeft 404. Het citaat "an easy-to-read description mentioning everything it does" staat in de Terms of Service, regel 3.1: https://extensions.blender.org/terms-of-service/ . Vervang de link. ("regel 6 van de winkel" is ook ToS 6.2.)

**Kan:**
1. Aantallen posable/printable/doll bijwerken naar 12/14/32 of "±" ervoor zetten.
2. Let bij lijst punt 3b op ToS 6.2: een link naar Pro "to support development" mag (6.1), maar noem daar geen Pro-functies.


**Moet verwerkt (Verspreider, 23 nov):** link naar Terms of Service 3.1 en 6.2 vervangen; aantallen posable 12, printable 14, doll 32 bijgewerkt. Daarmee akkoord ja volgens de keurder (enige moet).
