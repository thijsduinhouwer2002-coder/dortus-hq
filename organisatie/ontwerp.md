# Ontwerp: de organisatie van Dortus

Versie 1, 6 november 2026. Status: **voorstel, nog niet aan.** Thijs keurt goed, daarna zetten we het aan.

## Het idee in één zin

Een vaste ploeg van Claudes die elke nacht werkt: per platform een manager met 1 of 2 agents, daarboven een hoofdmanager, en die stuurt Thijs elke ochtend één kort rapport.

## Wie is wie

```
                 Thijs (eigenaar)
                       |
                 Hoofdmanager
        _______________|_______________________
       |          |           |                |
   Obsidian   JetBrains   Atlassian        Verkenner
   manager    manager     manager          (nieuwe platformen)
    |   |      |   |        |                |   |
  bouwer check bouwer check meter       onderzoeker check
```

### Thijs (eigenaar)
- Wil onderbouwde keuzes, enthousiasme en hard werken.
- Wil zelf zo min mogelijk doen. De managers werken zelfstandig en beslissen zelf, naar eigen inzicht. Elke beslissing krijgt een korte onderbouwing in het logboek, zodat Thijs achteraf kan zien waarom.
- Wordt alleen gevraagd in nood (zie "Wanneer Thijs vragen").
- Indienen, publiceren en nieuwe versies uitbrengen mag, via de officiële weg van het platform.
- Leest elke ochtend het rapport (±3 minuten).

### Hoofdmanager
- Draait elke ochtend, nadat alle platformmanagers klaar zijn.
- Leest de status van elk platform en schrijft het dagrapport.
- Houdt het bord bij: één lijst met wat er per platform loopt.
- Bewaakt de regels. Ziet hij dat een manager steeds hetzelfde doet zonder resultaat, dan meldt hij dat.
- Bepaalt de koers: welke platformen erbij komen, welke stoppen, waar de meeste tijd heen gaat. Altijd met onderbouwing in het rapport.
- Bouwt zelf niets.

### Platformmanager (één per platform)
- Draait één keer per nacht.
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
| Obsidian | Eerste plugin bouwen, lanceren, meten. Bijzaak: max ±1 week bouwen. | elke nacht |
| JetBrains | Uitzoeken wat we bouwen, daarna bouwen. Hier moet het geld vandaan komen. | elke nacht |
| Atlassian | Alleen meten: installs, reviews, vragen van klanten. De code blijft in Sprintbrief. | 1x per week |
| Verkenner | Nieuwe platformen onderzoeken als gokje. Stelt per keer één platform voor, met cijfers. | 2x per week |

**Zo groeit de organisatie:**
1. De verkenner onderzoekt een platform en schrijft een voorstel met cijfers.
2. Vindt de hoofdmanager het goed onderbouwd, dan komt er een **nieuwe manager voor dat platform**, met 1 of 2 agents eronder, een eigen map en een eigen vaste tijd in de nacht. Kost het geld, dan vraagt hij Thijs eerst.
3. De verkenner gaat gewoon door met het volgende platform. Hij stopt nooit met zoeken.

Zo komt er steeds een manager bij zolang er goede platformen gevonden worden. Werkt een platform niet (stopregel), dan stopt die manager weer.

## Wanneer het draait (Nederlandse tijd)

| Tijd | Wie |
|---|---|
| 02:13 | Obsidian-manager |
| 02:52 | JetBrains-manager |
| 03:31 | Verkenner (maandag en donderdag) |
| 04:07 | Atlassian-manager (maandag) |
| 06:44 | Hoofdmanager: rapport klaar voor Thijs wakker is |

De tijden liggen bewust uit elkaar, zodat de managers elkaar niet in de weg zitten bij het opslaan van hun werk.

## Wanneer Thijs vragen (alleen in nood)

- Er moet geld uitgegeven worden.
- Iets is niet terug te draaien: iets definitief verwijderen, een live product stoppen of uit een winkel halen.
- Er is een risico voor zijn accounts of juridisch (bijvoorbeeld een waarschuwing van een platform).
- Een taak lukt twee nachten op rij niet.
- Een handeling die alleen Thijs kan doen.

Al het andere beslissen de managers zelf.

## Regels voor het werk

1. **Bewijs bij elke bewering.** Elk cijfer krijgt een label: GEZIEN (zelf gemeten), DERDEN (uit een bron, met link) of GOK.
2. **Nakijken voor het telt.** Geen werk is klaar zonder controleur. Code is pas klaar als de tests groen zijn.
3. **Eén taak tegelijk per manager.** Liever één ding af dan drie half.
4. **Stopregel per product.** Op dag 30 na lancering: onder de 30 gebruikers stopt of verandert de manager, met onderbouwing. Een product uit een winkel halen is wel een vraag aan Thijs.
5. **Geen herhaling zonder resultaat.** Lukt een taak twee nachten niet, dan stopt de manager ermee en vraagt hij Thijs wat te doen.
6. **Open blik.** We bouwen wat op een platform ontbreekt, niet wat we toevallig al hebben. Wat Dortus eerder voor Atlassian maakte, is geen reden om het elders ook te bouwen.
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
    logboek.md         per nacht: wat er gebeurd is
  jetbrains/ ...
  atlassian/ ...
  verkenner/ ...
rapporten/
  2026-11-07.md        het dagrapport
producten/
  <naam>/              de code per product
```

## Het rapport aan Thijs

Elke ochtend, kort. Altijd dezelfde vorm:

1. **Cijfers:** per platform installs, nieuwe reviews, verkopen.
2. **Wat er vannacht gebeurd is:** per platform één of twee zinnen.
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
