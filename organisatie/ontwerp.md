# Ontwerp: de organisatie van Dortus

Versie 1, 6 november 2026. Status: **aan sinds 6 nov 2026** (vaste geplande taken, aangemaakt vanuit de projectchat).

## Het idee in één zin

Een vaste ploeg van Claudes die de hele dag werkt, elk uur een run van ±45 minuten: per platform een manager met 1 of 2 agents, daarboven een hoofdmanager, en die stuurt Thijs aan het eind van de dag één kort rapport.

## Wie is wie

```
                 Thijs (eigenaar)
                       |
                 Hoofdmanager
        _______________|____________
       |          |                 |
   Obsidian   JetBrains         Verkenner
   manager    manager           (nieuwe platformen)
    |   |      |   |              |   |
  bouwer check bouwer check  onderzoeker check
```

### Thijs (eigenaar)
- Wil onderbouwde keuzes, enthousiasme en hard werken.
- Wil zelf zo min mogelijk doen. De managers werken zelfstandig en beslissen zelf, naar eigen inzicht. Elke beslissing krijgt een korte onderbouwing in het logboek, zodat Thijs achteraf kan zien waarom.
- Wordt alleen gevraagd in nood (zie "Wanneer Thijs vragen").
- Indienen, publiceren en nieuwe versies uitbrengen mag, via de officiële weg van het platform.
- Leest elke avond het rapport (±3 minuten).

### Hoofdmanager
- Draait aan het eind van de dag (20:44), nadat alle platformmanagers klaar zijn.
- Leest de status van elk platform en schrijft het dagrapport.
- Houdt het bord bij: één lijst met wat er per platform loopt.
- Bewaakt de regels. Ziet hij dat een manager steeds hetzelfde doet zonder resultaat, dan meldt hij dat.
- Bepaalt de koers: welke platformen erbij komen, welke stoppen, waar de meeste tijd heen gaat. Altijd met onderbouwing in het rapport.
- Bouwt zelf niets.

### Platformmanager (één per platform)
- Draait elk uur van 08:00 tot 20:00. Werkt per run ±45 minuten door, taak na taak, en slaat na elke taak op.
- Leest zijn eigen map: status, takenlijst, logboek.
- Pakt de belangrijkste taak, zet daar 1 of 2 agents op en controleert hun werk voordat het telt.
- Schrijft na afloop: wat er gedaan is, wat er nu staat, en wat Thijs moet doen.
- Werkt alleen in zijn eigen map en de code van zijn eigen product.

### Agents (maximaal 2 per manager)
- **Bouwer:** schrijft code, tests, teksten voor de winkelpagina.
- **Controleur:** kijkt het werk van de bouwer na, zonder het zelf gemaakt te hebben. Draait de tests, checkt feiten tegen de bron.
- **Onderzoeker/meter:** haalt cijfers op (installs, reviews, concurrenten).

## De platformen bij de start

| Manager | Wat hij doet | Hoe vaak |
|---|---|---|
| Obsidian | Eerste plugin bouwen, lanceren, meten. Bijzaak: max ±1 week bouwen. | elk uur, 08:13 tot 19:13 |
| JetBrains | Uitzoeken wat we bouwen, daarna bouwen. Hier moet het geld vandaan komen. | elk uur, 08:52 tot 19:52 |
| Verkenner | Nieuwe platformen onderzoeken als gokje. Stelt per keer één platform voor, met cijfers. | 2x per week |

**Zo groeit de organisatie:**
1. De verkenner onderzoekt een platform en schrijft een voorstel met cijfers.
2. Vindt de hoofdmanager het goed onderbouwd, dan komt er een **nieuwe manager voor dat platform**, met 1 of 2 agents eronder, een eigen map en een eigen vaste tijd overdag. Kost het geld, dan vraagt hij Thijs eerst.
3. De verkenner gaat gewoon door met het volgende platform. Hij stopt nooit met zoeken.

Zo komt er steeds een manager bij zolang er goede platformen gevonden worden. Werkt een platform niet (stopregel), dan stopt die manager weer.

## Wanneer het draait (Nederlandse tijd)

| Tijd | Wie |
|---|---|
| elk uur om :13, 08:13 tot 19:13 | Obsidian-manager |
| elk uur om :52, 08:52 tot 19:52 | JetBrains-manager |
| 10:31, elke dag | Verkenner |
| 20:44 | Hoofdmanager: dagrapport voor Thijs |

Sinds 6 nov de hele dag in plaats van 's nachts, op verzoek van Thijs: dit is zijn fulltime werk, hij wil tempo en kan meekijken en meteen zijn klussen oppakken.

De tijden liggen bewust uit elkaar, zodat de managers elkaar niet in de weg zitten bij het opslaan van hun werk.

## Wanneer Thijs vragen (alleen in nood)

- Er moet geld uitgegeven worden.
- Iets is niet terug te draaien: iets definitief verwijderen, een live product stoppen of uit een winkel halen.
- Er is een risico voor zijn accounts of juridisch (bijvoorbeeld een waarschuwing van een platform).
- Een taak lukt twee runs op rij niet.
- Een handeling die alleen Thijs kan doen.

Al het andere beslissen de managers zelf.

## Regels voor het werk

1. **Bewijs bij elke bewering.** Elk cijfer krijgt een label: GEZIEN (zelf gemeten), DERDEN (uit een bron, met link) of GOK.
2. **Nakijken voor het telt.** Geen werk is klaar zonder controleur. Code is pas klaar als de tests groen zijn.
3. **Eén taak tegelijk per manager.** Liever één ding af dan drie half.
4. **Stopregel per product.** Op dag 30 na lancering: onder de 30 gebruikers stopt of verandert de manager, met onderbouwing. Een product uit een winkel halen is wel een vraag aan Thijs.
5. **Geen herhaling zonder resultaat.** Lukt een taak twee runs op rij niet, dan stopt de manager ermee en vraagt hij Thijs wat te doen.
6. **Open blik.** We bouwen wat op een platform ontbreekt, niet wat we toevallig al hebben.
7. **Opslaan:** werk gaat via een eigen tak (branch) en wordt pas in de hoofdversie gezet als het nagekeken is.

## Het geheugen

Elke run begint met een lege Claude. Het enige geheugen zijn de bestanden. Daarom:

```
organisatie/
  ontwerp.md           dit bestand
  regels.md            de regels hierboven, als vaste instructie
  bord.md              alles wat loopt, bijgehouden door de hoofdmanager
  lijst-thijs.md       wat Thijs moet doen, met links
platformen/
  obsidian/
    status.md          waar we staan, in 10 regels
    taken.md           de takenlijst, belangrijkste bovenaan
    logboek.md         per run: wat er gebeurd is
  jetbrains/ ...
  verkenner/ ...
rapporten/
  2026-11-07.md        het dagrapport
producten/
  <naam>/              de code per product
```

## Het rapport aan Thijs

Elke dag om 20:44, kort. Altijd dezelfde vorm:

1. **Cijfers:** per platform installs, nieuwe reviews, verkopen.
2. **Wat er vandaag gebeurd is:** per platform één of twee zinnen.
3. **Wat jij moet doen:** een genummerde lijst met links. Bovenaan wat het meest oplevert.
4. **Genomen beslissingen:** wat de managers besloten hebben en waarom, in één zin per beslissing.
5. **Vragen aan Thijs:** alleen in nood. Met opties, voor- en nadelen en het advies.
6. **Problemen:** wat vastloopt of fout ging.

Thijs krijgt een melding op zijn telefoon als het rapport klaar is.

## Het tegoed

Het tegoed speelt geen rol bij beslissingen: de managers werken zo hard als nodig is. Eén feit blijft: is het tegoed op, dan starten runs niet meer tot het weer aangevuld is. De hoofdmanager meldt dat in het rapport als het gebeurt.

## Wat ik nog niet zeker weet (eerst testen)

1. **Toegang in geplande runs.** Een geplande run start in een nieuwe sessie. Ik weet nog niet zeker of die meteen toegang heeft tot deze repo. Dat testen we met één proefrun.
2. **De browser 's nachts.** Sommig onderzoek ging vandaag alleen via de browser in de Claude-app op jouw computer. Staat die 's nachts uit, dan kan een manager dat niet. Werk dat de browser nodig heeft, plannen we overdag of het komt op jouw lijst.

## Hoe we het aanzetten

1. Thijs keurt dit ontwerp goed (of past het aan).
2. Ik maak de mappen, de vaste instructies voor elke rol en de eerste takenlijsten.
3. Proefrun: één manager en de hoofdmanager draaien één keer met de hand. We kijken samen naar het rapport.
4. Werkt dat, dan zetten we alle geplande taken aan.
5. Na een week kijken we terug: wat leverde het op, wat kostte het, wat moet anders.
