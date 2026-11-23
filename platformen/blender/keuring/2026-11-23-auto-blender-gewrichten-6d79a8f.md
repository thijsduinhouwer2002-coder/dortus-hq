# Keuring kantel-herkansing blender-gewrichten, 23-11-2026, automatische keurder
Wat ik keurde: commits 17123dd..6d79a8f (6d79a8ff4), alleen het bestand `producten/blender-gewrichten/proeven/kantel-2026-11-23/uitslag.md`
Akkoord: ja

Het akkoord geldt alleen voor dit proefverslag. De code waar het over gaat (`rig.py`, `toetsen_mens.py`, tak `claude/olaf-kantel` 07b0c8f) zit niet in deze wijziging en heb ik niet gezien.

## Deel A: doet het wat beloofd is?
De opdracht in `ontwerp.md` (Akkoord ja voor Click Joints 0.1.1 en Pro 1.0.2) wordt niet geraakt: er is geen add-on-bestand veranderd.

| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De wijziging bevat alleen een proefverslag en verandert niets aan de add-on of de releases 0.1.1 en 1.0.2. | Feit (diff) | hoog | n.v.t. |
| 2 | Het verslag is eerlijk over de grens: het bewijst niet dat de gekantelde snede op de AMD-processor van CI heel is. | Feit (tekst) | hoog | Een CI-run met de kantel aan en 9 gewrichten. |
| 3 | De uitkomst "kantel werkt als tweede kans" is alleen lokaal getoond, op één figuur (MakeHuman) en één Blender-versie (5.3.0). | Feit (tekst) | hoog | CI-run op 4.2.23 en 5.2.3 met het studio-figuur. |
| 4 | De commitboodschap noemt ook `apt-snel.sh` en berichten aan Bram en de Regisseur, maar die staan niet in de meegestuurde bestanden. | Vermoeden: ze zitten buiten de lijst of zijn niet meegestuurd | midden | De volledige bestandslijst van 6d79a8ff4. |

## Deel B: houdt het zich aan onze regels?

| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Het bestand is 28 regels en bevat geen persoonsgegevens of sleutels. | Feit | hoog | Bestandsgrootte en geen persoonsgegevens |
| 2 | De tabel met uitslagen is gemarkeerd als GEZIEN. De zin over AMD tegenover Intel en de duur "±6 min" hebben geen label. | Feit | hoog | Cijfers met GEZIEN, DERDEN of GOK |
| 3 | De nieuwe toetsmodus `CJ_HERKANS=4` laat ongekantelde sneden bewust weigeren. Dat is een proefopzet, geen aangepaste test om te slagen, maar ik zie de code niet. | Vermoeden | midden | Tests niet aangepast om te slagen |
| 4 | `architectuur.md` is in deze wijziging niet bijgewerkt. De kantelregel zit pas op een aparte tak, dus dat hoort bij het samenvoegen. | Feit voor deze diff, vermoeden voor de tak | midden | architectuur.md bijgewerkt |
| 5 | In het verslag staat niet welke latere eis de gekantelde sneden bij de schouders liet afvallen ("welke heb ik niet gelogd"). | Feit | hoog | Bewijs moet na te gaan zijn |

## Deel C: zou een gebruiker het leuk en fijn vinden?
Er is niets te zien of te spelen, dus dit is alleen een vermoeden uit de tekst.

| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | Bij de linkerheup valt het bereik terug van ±25° naar ±20° als de gekantelde snede gebruikt wordt. De koper ziet dan een kleiner bereik zonder te weten waarom. | Een korte melding in het paneel als een kantel-herkansing is gebruikt. | klein |
| 2 | Elke run duurt ±6 min op 2 kernen. Bij een weigering zonder terugval voelt dat lang. | Voortgang tonen bij Figure from rig. | midden |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Log bij de proef welke eis de gekantelde sneden bij de schouders afwees, zodat de oorzaak na te gaan is.
- Geef de zinnen over AMD tegenover Intel en over de duur een label (GEZIEN, DERDEN of GOK).
- Werk `architectuur.md` bij met de kantelregel en `KANTEL_GRADEN` zodra de tak naar main gaat.
- Keur de code op `claude/olaf-kantel` zelf apart, met de CI-run van studio-2 als bewijs, voordat het in een release komt.
- Zet de bestanden uit de commitboodschap (`apt-snel.sh`, berichten) in de volgende keuring, of meld waarom ze ontbreken.

---
Automatische keurder, model `claude-sonnet-5-5`, 18298 tokens in, 2858 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
