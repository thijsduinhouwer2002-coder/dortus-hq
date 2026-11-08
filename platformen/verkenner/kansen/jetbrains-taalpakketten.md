# Productkans JetBrains: taalpakketten (de IDE in het Frans, Italiaans, Tsjechisch enzovoort)

Vera, 8 nov 2026 run 22:31 (Amsterdam). Productkans-run. Labels: GEZIEN (zelf gemeten op 8 nov met de open API van de Marketplace of YouTrack), DERDEN, GOK.

## Hoe ik hierop kwam
Eerst een brede zoektocht naar een zwakke nummer één bij de ±500 betaalde en freemium plugins die Jet in zijn betaalbereidheid-scan niet bekeek (geen taal, bestandssoort, thema of AI; data uit `platformen/jetbrains/data/betaalbereidheid-scan-2026-11-08.tsv`). Uitkomst: bijna overal een sterke, goed beoordeelde leider die regelmatig bijwerkt (Bitbucket Integration Pro 4,76 uit 491 stemmen, JetLab 4,83, Fast Request 4,94, Symfony Plugin, GitToolBox). Verlaten betaalde plugins (Redis Manager, Kafka Client, OpenAPI Editor) zijn al vervangen door wat JetBrains zelf inbouwt. De enige groep met **betaalde producten, veel gebruik en slechte beoordelingen** waren de taalpakketten. Die zijn hieronder uitgezocht.

## Het product
Een plugin die de hele IDE (menu's, meldingen, instellingen, foutteksten) vertaalt. De IDE heeft er sinds 2024 een vaste plek voor: Settings > Appearance & Behavior > System Settings > Language and Region (GEZIEN in de beschrijving van de pakketten). Technisch is het vooral data (vertaalde tekstbestanden per onderdeel), die bij elke IDE-versie bijgewerkt moet worden.

## Bewijs van vraag en betalen
- **JetBrains zelf doet alleen Chinees (vereenvoudigd), Japans en Koreaans** (ids 13710, 13964, 13711; GEZIEN, controleur vond geen andere). Geen aankondiging van meer talen in 2025 of 2026 gevonden (controleur, blog via de WordPress-API).
- **Betaalde pakketten bestaan en worden gebruikt.** De maker "Code" (klein bedrijf, aiDevTool, Jeruzalem) verkoopt 11 talen voor $39 persoonlijk en $79 zakelijk per jaar (Italiaans $29/$59) en een All Languages-pakket voor $79/$199 (GEZIEN, prijs-API). Downloads van de meest gedownloade versie van de laatste 90 dagen (versie 2026.2.x van 16 aug; elke installatie die bijwerkt telt één keer, dus een benadering van actieve installaties, inclusief proefgebruikers):

| Taal (id) | Actief, benadering | Gemiddeld sterren (stemmen) |
|---|---|---|
| Chinees traditioneel (25810) | ±10.700 | 5,0 (2) |
| Spaans (24541) | ±7.900 | 4,33 (3) |
| Portugees (24542) | ±5.300 | 4,5 (2) |
| Frans (24539) | ±2.200 | **1,75 (4)** |
| Duits (24543) | ±2.100 | 4,2 (5) |
| Russisch (24544) | ±1.100 | **2,5 (4)** |
| Italiaans (24494) | ±970 | **2,0 (1)** |
| Turks, Pools, Tsjechisch, Hongaars | ±900, ±800, ±190, ±120 (dl90) | Tsjechisch **1,0 (1)** |

(GEZIEN, alle getallen nagekeken door de controleur.) Code houdt 11 talen al twee jaar bij, elke IDE-versie opnieuw, en bracht in maart 2026 nog een All Languages-pakket uit. Dat wijst op verkoop, maar **hoeveel er betaald wordt is niet te zien** (GOK).
- **Tweede betaalde maker:** Anton Shuvaev, eeuwigdurende licentie $29/$39 (controleur). Russisch (26495) 3,86 uit 7 stemmen, "Finally, a real plugin with human translation, not MTL". Zijn Frans (26734) staat op 1,0 uit 3 en kreeg sinds 1 mrt 2026 geen versie meer (GEZIEN).
- **Wat gebruikers zeggen (letterlijk, GEZIEN in de comments):**
  - Frans (Code): "Too many missing texts, not updated quickly even though the plugin is paid" (apr 2025), "The price definitely not worth it. Bad quality and missing text" (jul 2026), "Vous auriez gagné plus a partager votre plugin ... que vendre un outil bancale" (aug 2025).
  - Russisch (Code): "Machine translation" en "Still the same machine translation without any adequacy" (2025).
  - Spaans en Portugees: vooral klachten over de prijs ("seria melhor ainda se fosse de graça", "injusto que toque pagar"), vragen om een studentenversie, en over late updates bij een nieuwe IDE-versie.
  - Wie het fijn vindt, zijn vaak beginners: "Для меня, как начинающего ... огромное подспорье" (gratis Russisch pakket, jan 2026).
- **Verzoeken bij JetBrains (YouTrack, GEZIEN, alle open):** Russisch 81 stemmen (IJPL-43691, sinds 2020), Spaans 15 (IJPL-83063), Frans 6 (IJPL-162754). Bescheiden.
- **Talen zonder enig pakket:** Nederlands, Oekraïens, Vietnamees, Arabisch, Hindi (GEZIEN, controleur). Het enige Indonesische pakket (freemium) haalde 974 downloads in een jaar, dus kleine talen trekken weinig (GEZIEN).

## Top 3 en hoe sterk (harde regel)
1. **Code**: de enige die alle grote talen dekt en elke versie bijwerkt. Zwak in kwaliteit (machinevertaling, ontbrekende teksten), sterk in volhouden. Klein bedrijf, geen merk. In Frans, Russisch, Italiaans en Tsjechisch duidelijk slecht beoordeeld; in Spaans, Duits, Portugees en Chinees redelijk tot goed (maar met 2 tot 5 stemmen zegt dat weinig).
2. **Anton Shuvaev**: betere vertaling (Russisch), maar loopt achter met versies; Frans slecht.
3. **Gratis makers**: Code zelf geeft gratis varianten die een versie achterlopen; Alex Ivanov (Russisch, 86.609 downloads, sinds nov 2025 geen versie, Ctrl+Tab stuk); sinds 2026 nieuwe gratis makers (DevCairn Labs, Patrick Cornelissen Duits, igalexor Russisch).

Dus: de top is **zwak in Frans, Italiaans en Tsjechisch**, middelmatig in de andere grote talen, en er komen gratis makers bij. Geen groot bedrijf, geen duizenden reviews. Het mag volgens de harde regel.

## Het gat in één zin
Wie de IDE in het Frans (of Italiaans, Tsjechisch) wil, kan nu alleen kiezen uit slecht beoordeelde, half vertaalde pakketten; een goede, volledige en op tijd bijgewerkte vertaling bestaat niet.

## Wie betaalt, hoeveel, hoe vaak
Vooral beginners, studenten en mensen die liever niet in het Engels werken, persoonlijk, met een kleine jaarprijs ($19 tot $39) of eenmalig ($29 tot $39). Geen zakelijke inkoop nodig.
Rekensom (GOK): Frans heeft nu ±2.200 actief op het betaalde pakket en ±1.000 op het gratis pakket van Code. Halen wij de helft van ±3.200 en betaalt 10% daarvan $25 per jaar, dan is dat ±$4.000 per jaar, ±€300 per maand. Met Italiaans, Tsjechisch en Pools erbij misschien €500 per maand. Dat is de onderkant van de niche die de rol noemt.
Russisch valt af als geldbron: vanuit Rusland kan niemand op de Marketplace betalen (JetBrains schortte de verkoop in maart 2022 op, DERDEN via de controleur; kopers klagen erover in de comments van 26495).

## Eerste productidee
"Français pour JetBrains": één pakket voor alle IDE's, vertaald met een vaste woordenlijst (de termen die JetBrains zelf in zijn Chinese, Japanse en Koreaanse pakketten consequent gebruikt, als voorbeeld van wat er vertaald moet worden), elke tekst gecontroleerd op ontbrekende stukken en op sneltoetsen die stukgaan (de klacht over Ctrl+Tab), en binnen een week na elke IDE-versie bijgewerkt. Gratis proef van 30 dagen, daarna $19 per jaar of $39 eenmalig. Later dezelfde machine voor Italiaans, Tsjechisch, Pools.
Eerlijk over de AI: de vertaling maken wij met AI. Gebruikers haten juist "machine translation". Dat werkt alleen als de kwaliteit merkbaar beter is dan die van Code; zonder iemand die Frans als moedertaal spreekt om steekproeven te keuren, kunnen we dat niet beloven.

## Cijfer en advies
**Cijfer 4. Nog niet bouwen, wel een kleine proef waard als Jet ruimte heeft.**
- Voor: de nummer één is aantoonbaar zwak (cijfers en letterlijke klachten), er wordt een betaald product voor gebruikt door duizenden, het past bij onze bestaande JetBrains-account en betaalroute, en het is vooral data, dus snel te maken.
- Tegen: wat er echt betaald wordt is nergens te zien; de Franse markt is klein (±3.200 actief); vertalen met AI is precies waar gebruikers over klagen; elke IDE-versie (3 per jaar plus tussenversies) vraagt nieuw werk; er komen gratis makers bij; en JetBrains kan altijd zelf een taal toevoegen.
- Wat het cijfer naar 5 of 6 brengt: (1) een echt verkoopcijfer van een taalpakket (bijvoorbeeld als Code of Shuvaev het deelt, of het verkooprapport van ons eigen Bison & Flex laat zien hoeveel proeven omzetten op dit platform); (2) een goedkope kwaliteitsproef: 200 willekeurige teksten uit het Franse pakket van Code naast een eigen vertaling, gekeurd door een Franstalige.

Bericht aan Jet gezet (berichten/jet.md), Hans beslist.

## Bronnen en data
- Pakketten en comments: `data/jetbrains-taalpakketten-2026-11-08.json`, script `data/jetbrains-taalpakketten-script.py`; zoeklijst tag Localization: `data/jetbrains-localization-zoek-2026-11-08.jsonl`.
- API: `https://plugins.jetbrains.com/api/plugins/<id>`, `/updates`, `/rating`, `/comments`, `/api/marketplace/plugin/<id>/prices?countryCode=US`. YouTrack: `https://youtrack.jetbrains.com/api/issues/<id>`.

Nagekeken door de controleur (8 nov ±22:45): alle 8 beweringen kloppen; correcties verwerkt (25810 heeft al 2026.3.1, All Languages loopt twee versies achter, laatste Russische versie Shuvaev 7 jul 2026, meer gratis concurrenten dan eerst genoemd, Rusland kan niet betalen).
