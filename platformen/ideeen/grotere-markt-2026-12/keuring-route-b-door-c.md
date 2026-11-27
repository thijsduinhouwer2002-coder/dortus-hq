# Keuring route B (printers zonder Blender), 27 nov 2026 ±23:00 NL, Afkijker C
Wat ik keurde: `platformen/ideeen/grotere-markt-2026-12/route-b.md`, commit 55a4fbf (Afkijker B). Ik heb route B niet gemaakt en niets aan het bestand veranderd. Alles hieronder heb ik zelf met curl nagekeken op 27 nov 2026 tussen ±22:20 en 23:00 NL, tenzij er iets anders staat.
Akkoord: **nee** (vier moet-punten, alle vier klein tekstwerk; de eindconclusie "route B niet kiezen als grotere markt" steun ik wel)

## Zelf nagekeken (minstens 2 cijfers per kans)
| Cijfer uit route B | Wat ik zag | Klopt? |
|---|---|---|
| Split3r: 2.501 backers, 114.405, afgesloten 9 okt 2025 | `stats.json`: `"state":"successful","backers_count":2501,"pledged":"114405.0"`, `state_changed_at` 1759994380 = 9 okt 2025 07:19 UTC | ja |
| TrestleFDM: 268 verkopen, vanaf $12, 8 beoordelingen gemiddeld 5,0 | Gumroad-pagina, data in `data-page`: `sales_count` 268, `price_cents` 1200 (betaal wat je wilt, voorgesteld $12), `ratings` count 8, average 5.0 | ja |
| Flexi Factory 7.377 betalend van 45.738 | Patreon-API vanity `flexifactory`: `paid_member_count` 7377, `patron_count` 45738 | ja |
| Cinderwing3D 6.306 van 48.145 | Patreon-API: 6306 en 48145 | ja |
| NunnBreakable 7 van 311; Painted4Combat 1.334 | Patreon-API: 7 en 311; 1334 | ja |
| JointLab 1.537 accounts | https://jointlab3d.com/api/stats: `{"ok":true,"registeredUsers":1537}` | ja |
| OrcaSlicer 2.5.0 op 7 nov 2026 | newreleases.io: 2026-11-07T07:13:09; release notes 2.5.0 zeggen letterlijk "You can now add features with Python plugins" en "lots of plugins on the Orca Cloud plugin hub". In de wiki staat nu ook al V2.5.2 | ja |
| "orca.host ... read-only ... nothing here mutates the model" | letterlijk zo op `developer_reference/plugin_development/api_reference/host.html` | ja |
| Orca Cloud: alleen donatielinks, geen prijs per plugin | Orca Cloud-wiki: "Donation Links ... Ko-fi, PayPal, Patreon"; geen woord over prijs, verkopen of licenties. FAQ: "Core Orca Cloud features for individual OrcaSlicer users will remain free" | ja |
| r/OrcaSlicer 7.703 leden | Arctic Shift `subreddits/search`: `"subscribers":7703` | ja |
| Holes Fixer 186 punten, Pluginator 84 | Arctic Shift, de 100 nieuwste posts in r/OrcaSlicer sinds 1 nov: 1y545ri score 186, 1y5z56n score 84 | ja |
| Bambu-forum "sadly, no fully automatic no", 177 keer bekeken | https://forum.bambulab.com/t/236266.json: zo geschreven op 23 feb 2026, views 177 | ja |
| Meshy splitst alleen eigen modellen | Meshy-docs: "Uploaded and remeshed models can't be split" | ja |
| MakerWorld 53,09 mln bezoeken | Semrush: "makerworld.com is ranked #798 in US with 53.09M Traffic" [October 2026] | ja |
| 3D Splitter gratis | site geeft in de schema-data `"price": "0"` (de zin "100% free" vond ik niet in de html, die is grotendeels JavaScript) | ja, in de kern |

Rekensommen nagerekend: 53,09 / 1,69 = 31 ("30 keer", klopt); 217.767 / 7.703 = 28 (klopt); 114.405 / 2.501 = 45,7 (klopt); 18 per dag x 30 = 540 per maand (klopt); Jopek 122 / 386.448 = 0,03% (klopt). **Eén som klopt niet**, zie A1.

## Deel A: doet het wat beloofd is?
Opdracht (issue #323, route B): 3 kansen met kopers, prijs, 3 concurrenten met zwakke plek, bouwweken, euro per maand na 3 maanden met rekensom, toets aan de ideeëntest, ranglijst en één advies. Dat staat er allemaal. De bronnen zijn goed na te lopen.

| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| A1 | **Rekenfout bij kans 1.** "2.000 installaties x 3% koopt Pro x $15 = 90 kopers in 3 maanden, ±$1.350". Maar 2.000 x 3% = **60** kopers, en 60 x $15 = **$900**. Daarna "in maand 3 ±40 kopers" past daar niet bij: 40 van de 60 in één maand is onwaarschijnlijk. Met 60 kopers gelijk over 3 maanden is het ±20 per maand, ±$300 bruto, na de kosten van Gumroad (10% plus $0,50 per verkoop, GOK uit mijn hoofd, niet nagekeken) ±$260, **±€240 per maand**. De middenschatting van ±€480 is dus ongeveer twee keer te hoog. | feit (rekensom) | hoog | B rekent het zelf opnieuw na |
| A2 | **Terugzetten op de plaat staat niet in de API, en het bestaande voorbeeld is een omweg.** B schrijft dat het "niet gedocumenteerd" is (GOK: via een bestand). Ik heb de code van OrcaCAD gelezen (`git clone https://github.com/yazdannl/orcad-plugin`, `orcad.py` r. 678 tot 730): "Send to plate" schrijft een STL naar schijf en geeft die aan Orca via een Windows-bericht (`WM_COPYDATA`), of start Orca opnieuw met het bestand; zijn eigen melding zegt "the plate import itself cannot be confirmed ... drag the saved STL from exports if missing". In zijn test staat zelfs `assert not hasattr(fake_orca.host.plater(), "load_files")`. Holes Fixer maakt "a copy" van het project (GEZIEN, Reddit 1y545ri). Voor een splitser is dit het hart van het product: de delen moeten op de plaat komen. Dat werkt per besturingssysteem anders, vraagt de toestemming "start other programs", en wij kunnen alleen Linux testen. Dat maakt kans 1 moeilijker en trager dan "3 tot 4 weken". | feit (code en docs gelezen) | hoog | een plugin die op Windows en Mac betrouwbaar delen op de plaat zet zonder omweg, of een nieuwe API-functie in 2.5.x |
| A3 | **Betalen met een Gumroad-sleutel werkt slecht, omdat de code openbaar is.** Volgens de Orca Cloud-wiki upload je `.py` of `.whl`, en "the uploaded files and release notes follow the plugin's visibility on Orca Cloud": een openbare plugin is dus openbare Python-code. Een sleutelcontrole haal je er met één regel uit, en de hub zit vol makers die alles gratis delen (B zegt dat zelf). Meshy verdient wel, maar daar zit het werk op hun server (B noemt dat). B moet dit verschil benoemen in "Geld" en in de rekensom. Eerlijke opties: (a) gratis plugin plus donatielink, (b) het zware werk op een eigen server (kost geld en een server: Thijs), (c) de betaalde versie buiten de hub verkopen als bestand (kan, Pluginator laat zien dat lokaal installeren werkt; ook die code is te delen). | feit (wiki) en vermoeden (gevolg) | hoog voor de openbare code, midden voor het gevolg | een plugin in de hub die aantoonbaar geld verdient met een sleutel |
| A4 | **"Er staat nog geen splitser in de hub" is een vermoeden, geen feit.** B keek naar Reddit-posts, niet in de hub zelf (terecht, de hub vraagt een login: `api.orcaslicer.com/api/v1/plugins` gaf mij `401 missing_authorization`). De schermafdruk in de eigen wiki van Orca (`OrcaCloud-plugins-assets/20-plugin-hub-home.png`, gemaakt na 20 nov want "Blender Studio" staat erop) toont **227 plugins** in de hub. Ik zie er 16; een splitser zit daar niet tussen, maar wel **"Embedder: puts magnets and NFC stickers inside your prints"** (192 abonnees), van een maker die er minstens 8 heeft (Heitor Ramon Ribeiro, ook Organizer, Spooler, Print Calculator, UI Control). Dat raakt onze magneetgaten en laat zien hoe snel één maker een gat vult. B moet de zin als GOK of ONBEKEND labelen en Embedder noemen. | feit (schermafdruk) en vermoeden (geen splitser in de 211 die ik niet zie) | midden | iemand met een Orca Cloud-account zoekt in de hub op "split", "cut", "connector" (hoofdchat, 2 minuten) |
| A5 | **Bereik kan beter onderbouwd worden, en valt mee.** Dezelfde schermafdruk toont "Trending now, Subscribers 7d": BumpMesh Textures +2.283, ModelFinder +1.946, OrcaCAD +1.326, Support Fins +1.236, Print Calculator +1.226 in 7 dagen; gewone plugins 100 tot 420 abonnees totaal. B's GOK van 1.000 tot 3.000 installaties in 3 maanden is dus haalbaar voor een goede plugin. Dat maakt het bereik beter dan B dacht, maar niet het geld (A3). | feit (schermafdruk) | midden (datum precies onbekend) | aantal abonnees na 4 weken van onze eigen gratis plugin |
| A6 | Kans 2 en 3 en de ranglijst kloppen met de cijfers; de rekensom van kans 2 ($200 per maand bij 20 abonnees van $9,99) klopt. De eindconclusie ("printers betalen voor modellen en licenties, niet voor gereedschap") volgt uit de Patreon-cijfers (7.377 en 6.306 tegen 7). Het advies "pas Pro bouwen bij 500 installaties" is verstandig, maar de drempel ($225 per maand) heeft dezelfde aanname van 3% als A1, en die is volgens B's eigen getal (375 gratis downloads, 1 verkoop = 0,3%) waarschijnlijk 10 keer te hoog. | feit | hoog | |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| B1 | Elk cijfer heeft GEZIEN, DERDEN of GOK, met link of pad. Wat niet te lezen was (403, GitHub, hub) staat eerlijk in "Wat ik niet kon meten". | feit | hoog | regel 5 |
| B2 | Geen persoonsgegevens van Thijs; "Thijs heeft geen printer" verwijst naar een besluit en is geen persoonsgegeven. | feit | hoog | regel 2 |
| B3 | Geen gedachtestreepjes gevonden (grep op lange en halve streepjes gaf niets); Nederlands, gewone woorden. | feit | hoog | regel 8 |
| B4 | Niets geplaatst, niemand benaderd, geen account (regel 3 van het bestand); de interne hub-API is terecht niet aangeroepen. Geen AI in een product voorgesteld (Meshy alleen als concurrent). | feit | hoog | regels 4, 5, 7 |
| B5 | De zin "Daar staat nog geen splitser" staat in het Kort antwoord en in kans 1 als feit, zonder label (zie A4). | feit | hoog | regel 5 (elk feit een label) |
| B6 | Ruwe pagina's staan niet in de repo ("werkmap van deze run"). Na te doen met de adressen, dus geen moet; wel makkelijker keuren als de JSON-uitslagen erbij staan. | feit | hoog | ideeëntest (bron per antwoord) |

## Deel C
Niet van toepassing: dit is intern onderzoek, niets wat een klant ziet.

## Moet (blokkeert akkoord)
1. **A1:** rekensom kans 1 rechtzetten (2.000 x 3% = 60 kopers, niet 90) en de middenschatting en de bandbreedte daarop aanpassen, ook in de ranglijst (nu ±€480).
2. **A2:** in kans 1 opschrijven dat de API alleen leest, dat "op de plaat zetten" nu een omweg per besturingssysteem is (OrcaCAD, met bron), dat wij Windows en Mac niet kunnen testen, en de bouwweken en het risico daarop aanpassen.
3. **A3:** bij "Geld" en in de rekensom opschrijven dat de plugincode in de hub openbaar is, dus dat een Gumroad-sleutel makkelijk te omzeilen is; de echte opties noemen (donatie, server bij Thijs, los bestand buiten de hub).
4. **A4 en B5:** "nog geen splitser in de hub" labelen als GOK of ONBEKEND (hub niet doorzocht, 227 plugins), en Embedder (magneten in prints, 192 abonnees) bij de concurrenten van kans 1 zetten.

## Kan (mag later)
- A5: de trending-cijfers uit de wiki-schermafdruk als bron voor bereik gebruiken (+1.200 tot +2.300 abonnees per week voor de top 5).
- A6: de 3% omlaag naar iets wat bij ons eigen getal past (0,3% tot 1%), of beide laten zien.
- Vraag aan de hoofdchat: met een Orca Cloud-account in 2 minuten in de hub zoeken op "split", "cut", "connector", "dowel". Dat beslist A4.
- B6: de JSON-uitslagen (Patreon, Kickstarter, Arctic Shift) in de map zetten.

## Mijn oordeel over het advies
Het advies van B blijft overeind, ook na de correcties, en past bij wat ik in route C vond: geen van beide routes geeft een nieuwkomer binnen 3 maanden meer dan de nummer 1 in onze eigen hoek (±€2.000 per maand, GOK). Na A1 tot A3 zakt kans 1 (Orca-plugin) eerder naar **±€100 tot €300 per maand**, met als echte winst bereik en naamsbekendheid, niet geld. Als proef blijft hij redelijk (gratis, ±2 weken, installaties meten), maar alleen als we vooraf weten hoe we delen op de plaat krijgen en hoe we er ooit geld voor vragen.
