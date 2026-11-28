# Ontwerpblad Hol 2.0 (Sanne, 28 nov, issue #371)

Voor de wens van Thijs (28 nov 10:37 tot 11:01): alles kleiner zodat het hol veel groter kan, Gloop zelf besturen, 2 verdiepingen, een tuin, "een soort Fallout Shelter", iets meer retro, en minder lag. Bronnen: `organisatie/lat/hats.md` kopje "Hol 2.0 (28 nov)" (Afkijker, #373) en het beeld van Rusty dat Thijs stuurde (`organisatie/lat/beelden/hats/rusty-bureaublad-van-thijs-28nov.png`).

Beelden (maak opnieuw met `python3 maak_schets.py`):
- `hol2-ontwerpblad.jpg`: Rusty, Hats nu op 200 en 96 px, de maatschets van Hol 2.0 op ware maat en vier keer vergroot.
- `hol2-maatschets-120-1x.png`: alleen de strook van Hol 2.0, 1920 x 120, ware maat.
- `hol2-op-scherm-1080.png`: die strook op een scherm van 1920 x 1080 boven de taakbalk.

De maatschets is GEEN nieuwe kunst: het zijn bestaande renders en stukken van een spelbeeld, verkleind en op 6 tot 10 kleuren per ding gezet. Hij laat alleen de maat en de dichtheid zien. Fakkels en goud hebben nog een blokje achtergrond; dat is de schets, niet het plan.

## 1. Maat (gemeten)

| | strook tegenover scherm | figuur tegenover strook | rijen | bron |
|---|---|---|---|---|
| Rusty's Retirement | ±27% (±156 van ±570 px in het beeld van Thijs) | robotje ±8 tot 12% | ±5 rijen dingen boven elkaar | GEZIEN, eigen meting op het beeld van Thijs; Afkijker kwam op 27% en 12% |
| Hats nu, 200 px | 18,5% van 1080 | Gloop ±100 px = ±50% | 1 gang | GEZIEN, `bewijs-strook-hoger/minuut1-std-200-ware-maat.png` |
| Hats nu, 96 px (standaard sinds #372) | 9% | Gloop ±48 px = ±50% | 1 gang | GEZIEN, `bewijs-fps-12/` |
| **Hol 2.0 voorstel, 120 px** | 11% | Gloop 20 px = 17%, helden 16 px = 13% | tuin + 2 verdiepingen | schets in deze map |

Wat het beeld zegt: bij ons is de strook al niet groot (96 px is 9%), maar ALLES erin is groot. Kleiner zetten (96 px) maakt het hol niet groter, alleen alles kleiner. Hol 2.0 houdt de strook laag en maakt de dingen erin 2,5 keer kleiner, zodat er 4 keer zoveel hol in past: 9 kamers en 10 helden in beeld (was 1 gang met 2 tot 3 helden).

Indeling van de strook op 120 spelpx (ook de vaste kunstmaat; op andere hoogtes vergroot met hele getallen, nearest):

| laag | hoogte | wat |
|---|---|---|
| tuin | 22 px | gras, struiken, bloemen; helden komen hier binnen; later groente of paddenstoelen die Gloop eet |
| maaiveld | 4 px | rand met ladders naar beneden |
| verdieping 1 | 44 px | kamers met vallen, helden lopen, ladder naar 2 |
| balk | 4 px | vloer en plafond |
| verdieping 2 | 44 px | troon van Gloop met de schat, de diepste vallen |
| rand | 2 px | |

Gloop 20 px, helden 16 px, hoeden 4 tot 6 px, vallen en luiken ±12 px breed. Bord rechts wordt één regel: goud en doel (geen grote tekst meer in de strook, zoals Rusty: twee getallen).

## 2. Schuiven: JA, maar alleen omhoog en omlaag, en pas als er een derde verdieping is

Advies: **ja**, met het muiswiel boven het hol, verticaal, en alleen als het hol dieper is dan de strook laat zien. Niet horizontaal: de strook is al het hele scherm breed.

Waarom:
- Fallout Shelter en Project Highrise verslaven door "getting taller and taller" (DERDEN, reviews in de lat). Bij 2 verdiepingen is het hol op; groeien kan alleen in de diepte, dus moet je kunnen schuiven.
- Rusty biedt zoomen als keuze omdat klachten beide kanten op gaan ("too big on the screen" en "larger window mode", GEZIEN in de lat). Schuiven met het wiel is onze versie: de strook blijft laag, het hol mag groot worden.
- Het muiswiel werkt zonder focus (klikken komen nu al aan, toetsen nooit; lat punt 2). Er wordt dus nooit een toets van het werk gepakt.
- De Height-instelling (96 tot 240) gaat niet meer alles vergroten maar laat meer verdiepingen zien: op 240 zie je tuin en 4 verdiepingen. Wie meer ruimte geeft, krijgt meer hol, geen grotere Gloop. Dat is precies wat Thijs vroeg.

Regels: een nieuwe verdieping komt vrij bij een aantal hoeden op de toren (onze "bewoners", zoals Fallout Shelter met bewoners). Na 10 s zonder muis schuift het beeld zacht terug naar de verdieping waar het meest gebeurt. In de proef: 2 verdiepingen plus een derde om het schuiven te voelen.

## 3. Gloop zelf laten lopen: klikken om te lopen, plus een besturen-stand

Keuze: **klikken om te lopen is de standaard**: klik ergens in het hol en Gloop loopt erheen (via de ladders), klik op een ding en hij doet het (val zetten, held opeten, oogsten in de tuin). WASD alleen in een **besturen-stand**: klik op Gloop zelf, dan pakt het spel de focus en krijgt de strook een gouden rand van 1 spelpx; WASD of pijltjes lopen, W of S op een ladder klimt. Stopt vanzelf bij Esc, bij een klik buiten het hol, of na 10 s zonder toets; dan valt de focus terug.

Waarom: het spel mag nooit toetsen van het werk pakken (het venster heeft nu WS_EX_NOACTIVATE en no_focus, lat punt 2). Bij 61 bureaubladspellen doet niemand WASD (GEZIEN, Afkijker); klikken past bij het genre en werkt zonder focus. Thijs vroeg wel om WASD, dus die krijgt hij, maar alleen als hij er zelf om klikt, met een zichtbaar teken, en met een vaste uitweg.

## 4. Gloop scharrelt zelf (tabel per plek, issue #374, les Shimeji)

Als je hem niet bestuurt, kiest Gloop elke keer als een gedraging klaar is één nieuwe uit de tabel van de plek waar hij staat, met één gewogen loting. Past niets (bijvoorbeeld een ladder weg), dan loopt hij terug naar de troon (vangnet). Na de besturen-stand pakt hij de tabel weer op op de plek waar hij staat. Bewegen op ±4 beelden per seconde, alleen op hele spelpx.

| plek | gedraging | gewicht | duur | daarna mag |
|---|---|---|---|---|
| troon | zitten en ademen | 4 | 6 tot 12 s | alles van troon |
| troon | munten tellen (goud wipt) | 2 | 3 s | troon, vloer |
| troon | slapen (zzz) | 2 | 10 tot 20 s | troon |
| troon | opstaan en wandelen | 2 | 0 s | vloer |
| vloer | wandelen naar een willekeurige plek op de verdieping | 4 | tot hij er is | vloer, ladder, rand |
| vloer | snuffelen aan een val (kijkt of hij scherp is) | 2 | 3 s | vloer |
| vloer | spugen (zoals nu) | 1 | 2 s | vloer |
| vloer | terug naar de troon | 2 | tot hij er is | troon |
| ladder | klimmen naar de andere verdieping | 5 | tot boven of onder | vloer, tuin |
| ladder | halverwege rondkijken | 1 | 2 s | ladder |
| rand (bij een balk) | over de rand gluren naar beneden | 2 | 2 s | vloer |
| rand | naar beneden laten ploppen (alleen boven een gat of ladder) | 1 | 1 s | vloer |
| tuin | zonnen (wordt plat en breed) | 3 | 5 tot 10 s | tuin |
| tuin | iets uit de tuin eten | 2 | 3 s | tuin |
| tuin | een held aanstaren die binnenkomt (alleen als er een is) | 4 | 2 s | tuin, ladder |
| tuin | terug naar beneden | 3 | tot bij de ladder | ladder |

Regel: een held op dezelfde verdieping binnen 40 spelpx gaat altijd voor (Gloop draait zich om en kijkt; eten doet hij alleen als hij die stap gekocht heeft, zoals nu). Gewicht en duur zijn een eerste GOK; Iris keurt het gevoel in de proef.

## 5. Retro en lag

Licht retro, zoals Thijs zei ("niet groots, hooguit een beetje"): niet alles opnieuw tekenen, maar de 3D-renders van Mila direct op de doelmaat in spelpx renderen (Gloop 20, held 16), zonder anti-aliasing, met 2 of 3 tinten per materiaal en een vast palet van ±32 kleuren (lat punt 4, les Dead Cells). Figuren bewegen alleen op hele spelpx, tegen flikkeren.

Lag: het spel tekent op 1920 x 120 en vergroot met een heel getal (Godot rekstand viewport). Olaf meet binnen één run tegen een placebo, zoals bij het palet, en schrijft de procent CPU op voor 120 px oud tegen 120 px Hol 2.0. Eis: Hol 2.0 kost niet meer CPU dan het hol nu op 96 px, terwijl er 4 keer zoveel in beeld is.

## 6. Wat dit doet met de planning (eerlijk)

Hol 2.0 is geen kleine wijziging: alle kunst opnieuw op kleine maat, een tweede verdieping met ladders, een tuin, lopen met klikken, schuiven, en Gloop met een tabel. Inschatting (GOK):
- **Speelbare proef** op een eigen tak (`hol2-proef`), met de huidige kunst verkleind en 2 nieuwe kleine figuren van Mila: ±2 tot 3 dagen. Main blijft zoals hij is.
- **Echt Hol 2.0** na een ja van Thijs op de proef: ±1,5 tot 2 weken (alle kunst, balans van goud en prijzen opnieuw voor 2 verdiepingen, eerste minuut opnieuw, keuringen).
- **Demo 18 dec:** haalbaar als Thijs vóór ±2 dec ja zegt op de proef. Zegt hij later ja, dan gaat de demo uit met het hol van nu (96 px) en komt Hol 2.0 vóór het fest (14 tot 18 jan). Er gaat dus niets verloren door de proef: main blijft uitbrengbaar.

## 7. Wie doet wat

- Olaf (issue "Hol 2.0 proef"): de proeftak met 2 verdiepingen en een derde om te schuiven, tuin, klikken om te lopen, besturen-stand, schuiven, Gloop met de tabel, meting CPU, en een .exe voor Thijs.
- Mila (issue "Hol 2.0 kleine figuren"): Gloop op 20 px en 3 helden op 16 px, direct klein gerenderd in retro (zie punt 5), plus een tegel voor tuin, wand en ladder.
- Iris speelt de proef en keurt het gevoel; Daan keurt dit blad.
