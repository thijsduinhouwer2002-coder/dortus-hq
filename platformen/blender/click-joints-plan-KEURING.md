# Keuring plan Click Joints Pro, 19 nov 2026, keurder (agent, niet de maker)
Wat ik keurde: `platformen/blender/click-joints-plan-2026-11-19.md` (commit 6b79c632), naast de code op main in `producten/blender-gewrichten/click_joints/` en de besluiten van 16, 17 en 19 nov.
Akkoord: nee (drie moet-punten, alle drie tekstwerk van minder dan een uur; daarna is het plan bruikbaar)

Alles hieronder met curl gelezen op 19 nov 2026 tussen ±14:15 en 14:45 UTC, tenzij anders vermeld.

## Kort
- De marktcijfers kloppen: 13 van de 14 nagelopen claims staan precies zo op de bron. Fout of scheef: de saleprijs (25% in plaats van 35%), de twee Reddit-draden die "het probleem van figuurmakers" moeten bewijzen (een telefoonhouder en een kart), "254 downloads in 9 dagen" (het zijn 11 dagen) en "nog van niemand" (Cleave heeft "socket slits" bij zijn kogel).
- Wat het plan zegt over wat Pro kan, klopt met de code, maar "Figure from rig" staat alleen op main: de verkochte Pro op Gumroad is nog 1.0.2 (alleen scharnier). Het plan zet de prijs "nu" op $19 voor die versie, en dat botst met het besluit van 16 nov.
- De volgorde (prijs, print, pagina, testkaartje, grip en ratel) is verdedigbaar. Wat mist: Pro 1.1.0 uitbrengen en de Superhive-keuring vóór 27 nov rond krijgen. Zonder dat levert de Cyber Sale niets op.
- Prijs $19 / $24 / $59 is redelijk tegen de markt. Gecorrigeerd voor 35%: in de sale houden we $7,83 per Personal-verkoop, niet $9,08.

## Gecorrigeerde saleprijzen (Cyber Sale 35%, vr 27 nov t/m wo 2 dec)
Afdracht Superhive op het gratis plan: (prijs min 5,5% min $0,49) maal 70% (GEZIEN, https://support.superhivemarket.com/article/185-how-merchant-and-transaction-fees-are-calculated). Korting gaat van de prijs af, de afdracht wordt over de lagere prijs gerekend (GEZIEN, https://support.superhivemarket.com/article/184-how-coupons-affect-your-commission-earnings). Gumroad 10% plus $0,50 bij directe verkoop, 30% via Discover (GEZIEN, https://gumroad.com/pricing). Bedragen zijn eigen rekensom (GOK alleen in die zin dat btw en wisselkoers buiten beeld blijven).

| Variant | Volle prijs | Wij houden (Superhive) | Saleprijs (35%) | Wij houden in de sale | Plan zei (25%) |
|---|---|---|---|---|---|
| Huidig Personal | $12 | $7,59 | $7,80 | **$4,82** | $9 / $5,61 |
| Personal | $19 | $12,23 | **$12,35** | **$7,83** | $14,25 / $9,08 |
| Supporter | $24 | $15,53 | **$15,60** | **$9,98** | niet berekend |
| Studio (tot 5) | $59 | $38,69 | **$38,35** | **$25,03** | niet berekend |
| Huidig Studio | $45 | $29,42 | $29,25 | $19,01 | niet berekend |

Gumroad als we daar dezelfde week 35% geven (kan-punt 3): $19 wordt $12,35 en we houden $10,62; zonder korting $16,60.

Wat het betekent: in de sale levert $19 nog maar $0,24 meer op dan $12 nu bij volle prijs ($7,83 tegen $7,59). De zin in het plan "meer dan nu bij de volle prijs" klopt nog net. Het echte voordeel van $19 in de sale: we houden $7,83 in plaats van $4,82 als we op $12 blijven.

## Deel A: doet het wat beloofd is?
(toets tegen de opdracht van de hoofdchat: onderzoek naar Cleave en anderen, top 5 op opbrengst per moeite, prijsadvies, binnen de besluiten)

### A1. Nagelopen claims (curl, 19 nov)
| # | Claim in het plan | Wat ik zag | Feit of vermoeden | Zekerheid |
|---|---|---|---|---|
| 1 | Cleave $23, Support $28 met dezelfde download | "Support the developer Same download as Standard ... $28", Standard $23 (https://superhivemarket.com/products/cleave) | feit, klopt | hoog |
| 2 | Cleave derde in "Top Selling Items this Week" na Auto-Rig Pro en Human Generator | precies zo, Cleave $23.00-$28.00 op plek 3 (https://superhivemarket.com/popular) | feit, klopt | hoog |
| 3 | Teller 200+, 3 ratings op Superhive | "Sales 200+ Rating 3 ratings Published about 2 months ago Blender Version 4.2 - 5.2" | feit, klopt | hoog |
| 4 | Functies: pennen, deuvel, staaf, magneet, kogel, geen; 120+ printers; geen scharnier | "Pegs, dowels, rods, magnets, ball joints", "a plain seam", "Over 120 models built in"; het woord "hinge" komt 0 keer voor | feit, klopt | hoog |
| 5 | 11 versies in 8 weken, kogel in 1.6.0 (28 okt), 1.7.0 (17 nov) met Seam from Points, spleet en rood | 1.0.0 (23 sep) t/m 1.7.0 (17 nov) zijn 11 versies; 1.7.0 tekst zoals in het plan (https://superhivemarket.com/products/cleave/versions) | feit, klopt | hoog |
| 6 | "Dat rood is ons idee van de passingkleur; hij neemt over wat werkt" (als GEZIEN) | het rood staat er; dat het van ons komt is een uitleg | vermoeden, label moet GOK zijn | hoog |
| 7 | Gumroad Cleave $21,99, 4 reviews 5,0 | ld+json: price 21.99, ratingValue 5.0, reviewCount 4 (https://v4ss3ur.gumroad.com/l/cleave) | feit, klopt | hoog |
| 8 | Quotes van kopers, ook "Price" bij "The good" | alle zeven zinnen staan letterlijk op https://superhivemarket.com/products/cleave/ratings | feit, klopt | hoog |
| 9 | CatPin $24 (normaal $30), steun $36, studio $80, 400+ | klopt; steun en studio zijn ook afgeprijsd (normaal $45 en $100) (https://superhivemarket.com/products/catpin) | feit, klopt | hoog |
| 10 | Split-3DPrint $0 / $22 / $28 / $59, 400+ | klopt ($22 normaal $28, steun $28 normaal $34, 5 plekken $59 normaal $65) (https://superhivemarket.com/products/split-3dprint) | feit, klopt | hoog |
| 11 | Reddit "harder to move?" 512 punten, 258 reacties, 4 sep 2026 | cijfers kloppen (Arctic Shift), **maar het gaat om een joystick die een telefoon van 200 gram moet dragen, in PETG**, geen figuur | feit, cijfer klopt, gebruik is scheef | hoog |
| 12 | Reddit fuzzy skin 467 punten, reactie 836 "ridges are going to wear", 188 en 136 | cijfers en zinnen kloppen, **maar het is een kogel voor een kart** ("add a ball joint to my kart"); de draad heeft 63 reacties | feit, cijfer klopt, gebruik is scheef | hoog |
| 13 | Uncle Jessy "The Ultimate Guide to Fixing Loose Joints" 40.212 weergaven | "40,212 views, 2y ago", titel "... - 3D Prints" (YouTube-zoekpagina) | feit, klopt | hoog |
| 14 | Formlabs-forum: "will not hold its pose", Revoltech, 0,0 tot 0,2 mm blijft staan, boven 0,3 los | klopt (https://forum.formlabs.com/t/action-figures-methods-to-stop-rag-doll-effect/28524), maar de draad is van aug 2020, 5 berichten, en het witboek gaat over hars (Formlabs Durable), niet FDM | feit, klopt, ouder en smaller dan het lijkt | hoog |
| 15 | Gratis versie 254 downloads "in 9 dagen" | 254 klopt, maar de pagina zegt "Published Nov. 8th, 2026": 11 dagen (https://extensions.blender.org/add-ons/click-joints/) | feit, klein foutje | hoog |
| 16 | Click Joints Pro $12 op Gumroad | price 12.0 (https://duinhouwer8.gumroad.com/l/click-joints-pro) | feit, klopt | hoog |
| 17 | Rekensom afdracht $12 → $7,60, $19 → $12,23, $24 → $15,53; Gumroad $16,60 en $10,30 | formule en uitkomsten kloppen (artikel 185, Gumroad pricing) | feit, klopt | hoog |
| 18 | ZeroDotCMD 48.794, 3D Zip Guy "New Ratchet Joints!" 16.213 | klopt (YouTube-zoekpagina) | feit, klopt | hoog |

Ook gezien en niet in het plan: Cleave's kogel heeft op de pagina de varianten "ONE SIDE · BALL ON ROD", "DOUBLE SIDE · DOUBLE-BALL PIN" en "SOCKET SLITS". Sleuven in de kom zijn juist een bekende manier om een kom te laten klemmen en klikken. Dus "een grip-instelling is nog van niemand" klopt niet helemaal (feit, hoog: het label staat op de pagina; wat zijn sleuven precies doen, staat er niet bij).

Tijden: het plan zegt "gelezen tussen ±13:30 en 14:30 UTC", maar de commit is van 12:45 UTC. Waarschijnlijk Nederlandse tijd als UTC geschreven (vermoeden, midden). De commit kwam 3 minuten na het besluit over 35% (07dc01ca, 12:42 UTC), dus het missen van 35% is begrijpelijk, maar het moet nu goed.

### A2. Wat Pro nu echt kan (code op main, `producten/blender-gewrichten/click_joints/`)
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | Scharnier met eindstop 90/115/135 en een vrij getal 30 tot 150 (`betaald/scharnier.py` GRADEN_MIN/MAX), gradenboog (`scharnier_boog.py`), pose en rood (`scharnier_beweeg.py`, `scharnier_kleur.py`), afstandscontrole (`afstand.py`): klopt met het plan | feit | hoog | |
| 2 | Figure from rig leest Rigify, Mixamo, Unreal, Character Creator, VRoid, Biped, Daz en Auto-Rig Pro (`betaald/rig.py` regels 3 tot 41): klopt | feit | hoog | |
| 3 | **Maar Figure from rig is nog niet te koop.** Gumroad noemt alleen scharnier, pose, passing en afstand (versie 1.0.2); Superhive heeft 1.0.1 in de keuring; 1.1.0 wacht op Daan (`berichten/hoofdchat.md` regel 319, `organisatie/bord.md`). Het plan schrijft "Wij zijn de enige die er een poseerbare figuur van maakt" en bouwt blok D1 erop, alsof het al verkocht wordt | feit | hoog | Gumroad-pagina na uitgave van 1.1.0 |
| 4 | Gratis en Pro tegelijk aan wordt geweigerd (`weiger_dubbel` in `betaald/__init__.py`): klopt | feit | hoog | |
| 5 | "Niets tegen loszitten, alleen speling in mm" klopt voor de kogel. Het scharnier heeft wel klikneuzen (`scharnier_neus.py`, klikdiepte 0,25 mm), maar die houden de delen bij elkaar, ze geven geen standen: de top van de neus ligt precies op de draaias | feit | hoog | |
| 6 | "Geen pennen" bij de zwakke punten is verwarrend: de gratis versie heeft een pen ("Pin and hole, turns around one axis", `eigenschappen.py`). Bedoeld zijn vaste verbindingspennen zoals bij Cleave; zo opschrijven | feit | hoog | |
| 7 | Testkaartje, printerprofielen, magneetgaten en wrijvingsribbels stonden in het oude ontwerp (`ontwerp.md` regel 37) maar zijn niet gebouwd; het plan noemt ze terecht nieuw. De speling geldt nu al voor de hele scene (`scene.click_joints.speling`), dus "my printer: 0.15 mm geldt voor de hele figuur" is al zo; nieuw is alleen een naam per printer | feit | hoog | |

### A3. Zijn de voorgestelde functies realistisch met de bestaande code?
| # | Functie | Oordeel | Feit of vermoeden | Zekerheid |
|---|---|---|---|---|
| 1 | **Testkaartje (C1), 1 tot 2 runs** | Haalbaar: de kogel en het scharnier zijn al losse operators, en `commercie/blender-click-joints/testprint/maak.py` maakt al staafjes met Pro-gewrichten in bpy. Nieuw: vijf gewrichten op één strook en getallen in reliëf. Tekst naar mesh plus Boolean moet gesloten blijven (export eist dat), en er komt een eigen e2e-toets en een keuring door Daan bij. Reken 2 tot 3 runs | vermoeden | midden |
| 2 | **Grip met klemribbels in de kom (C2 stap 1)** | Kan technisch: Pro vervangt al een functie van de gratis kern bij register (`uit_elkaar.afstand`), zo kan de komvorm ook. `beweeg.py` laat kogel en kom buiten de botsproef, dus het bereik blijft gelijk. Wel geraakt: `passing.py` meet de speling van kogel naar kom, en de toets "speling 0,1/0,2/0,3 over 500+ punten" gaat met ribbels anders uitkomen; nieuwe toets nodig. Groter punt: de eigen bron van het plan zegt dat ribbels slijten (reactie 836). Een gefacetteerde kogel of sleuven in de kom (zoals Cleave) is de betere eerste proef | feit (code), vermoeden (slijten) | hoog / midden |
| 3 | **Ratelscharnier (C2 stap 2), 3 tot 6 runs** | Bouwstenen zijn er: `_draailichaam`, `_kap`, de zaagsnede en de rek-eis in `scharnier_neus.py`, de streepjes op `scharnier_boog.py`. Maar een ratel vraagt een nokje buiten de as en een rij kuiltjes per 15° in de wang, en de wang moet bij elke stand opzij veren. Het plan noemt tanden van 0,4 tot 0,6 mm; de bestaande code houdt de klikdiepte op 0,25 mm en verkleint hem verder als de rek boven 3% komt (`H_MM`, `REK_MAX`). Tanden van 0,4 tot 0,6 mm zouden die eis breken. Start vanaf 0,25 mm en de rek-eis. Plus de eis "printbaar zonder steun onder 45°" voor elk kuiltje. Reken eerder 5 tot 8 runs | feit (code), vermoeden (runs) | hoog / laag |
| 4 | **Elastiekkanaal (C3), 2 tot 3 runs** | Simpel als vorm (een cilinder door A en B, met een trechter aan de komkant omdat de kogel kantelt). Maar de nek is 0,48 keer de kogel (`gewricht.py`): bij een kogel van 4,5 mm is de nek 2,2 mm, een kanaal van 1 mm laat dan 0,6 mm wand over. Alleen haalbaar bij grote kogels (GOK: vanaf ±10 mm). De vraag rust op één r/BJD-draad met 34 punten (feit, Arctic Shift); BJD-makers werken vooral met hars | feit (maten), vermoeden (vraag) | hoog / midden |
| 5 | Swivel en magneetgat (C4, C5) | Dichtbij wat er is (pen en cilinders in `vormen.py`); C5 terecht klein gehouden vanwege het besluit "geen splits-add-on" | vermoeden | midden |

### A4. Volgorde op opbrengst per moeite
- **Verdedigbaar:** eerst wat niets kost om te bouwen (prijs, pagina), dan bewijs (print), dan het testkaartje (hergebruik), dan de grote unieke functie. Dat past bij de hoofdzaak "geld binnen weken" (feit: het enige geldmoment binnen 2 weken is de Cyber Sale van 27 nov t/m 2 dec, besluit 19 nov 13:45).
- **Mist 1: Pro 1.1.0 uitbrengen.** Het besluit van 16 nov koppelt de prijs van $15 tot $19 aan 1.1 ("alleen als Daan of kopers het indrukwekkend vinden"). De pagina-blokken van D1 en het uitgelichte beeld van Bram (`superhive/README.md`, beeld 1 "From rig to poseable print in one click") gaan ook over 1.1. Dit hoort vóór punt 1 (feit, hoog).
- **Mist 2: de Superhive-keuring vóór 27 nov.** Pending sinds 15 nov; zonder goedkeuring doet Pro niet mee met de sale (besluit 19 nov 13:45). Het plan noemt Pending maar zet geen actie: navragen bij Superhive (via de hoofdchat, tekst onder de naam van Thijs alleen na zijn ja) en uitzoeken of 1.1.0 al in de lopende aanvraag kan. Dit is de grootste hefboom voor geld in de komende twee weken (vermoeden, midden: hoeveel de sale oplevert voor een nieuw product weten we niet).
- **Mist 3: een nulmeting van de verkopen.** Hoeveel Pro op Gumroad verkocht, ziet alleen Thijs. Zonder dat getal kan de stopregel "14 dagen geen verkoop op $19" niets zeggen over de prijs, want ook op $12 kan het nul zijn (vermoeden, midden).
- **De print (B) haalt de sale niet** bij Craftcloud (doorlooptijd ±1 week, het plan zegt het zelf). Toch nu starten, maar niet rekenen op "clicks" in de sale-week (vermoeden, midden).

### A5. Prijsadvies
- **Redelijk:** $19 zit onder Cleave ($23), CatPin ($24) en Split-3DPrint ($22) en boven de nieuwkomers. De drie-variantenopzet staat echt bij alle drie (feit, hoog, zie A1).
- **Risico 1, besluit:** "Gumroad meteen" op $19 terwijl Gumroad 1.0.2 levert botst met het besluit van 16 nov (feit, hoog). Oplossing: $19 tegelijk met 1.1.0 en het akkoord van Daan, of eerst een nieuw besluit van de hoofdchat.
- **Risico 2, nepkorting:** de prijs gaat 8 dagen vóór de sale van $12 naar $19, en de saleprijs ($12,35) is vrijwel de oude prijs. Wie de Reddit-post met de Gumroad-link van $12 zag, ziet dan een "korting" die er geen is. Dortus is een Nederlands bedrijf: bij een prijsverlaging naar EU-consumenten moet de "van"-prijs de laagste prijs van de 30 dagen ervoor zijn (Prijsaanduidingsbesluit, Omnibus). Superhive zet de doorgestreepte prijs, niet wij; of die regel dan voor ons geldt, weet ik niet (vermoeden, zekerheid laag; niet nagelezen bij een jurist of in de regels van Superhive). Op Superhive was Pro nooit te koop, dus daar is het risico kleiner dan op Gumroad.
- **Risico 3, Supporter:** kost niets, maar op Superhive staat de keuze bij "Seats" naast een tweede variant; bij weinig verkeer kiest bijna niemand hem (GOK). Geen schade, wel geen echte opbrengst.
- **Risico 4, de broncode van Pro staat in deze openbare repo** (`producten/blender-gewrichten/click_joints/betaald/`, feit, hoog; ook gemeld in `berichten/hoofdchat.md` regel 398). Onder de GPL mag dat, maar het maakt "betaal $19" zwakker en het besluit van 18 nov (betaalde code privé) is nog niet uitgevoerd. Dit staat niet in het plan.
- **Na de print, C2 en 3 reviews naar $24:** redelijk als volgende stap; de omgooiregel (14 dagen, dan eerst pagina en bewijs) is goed opgezet, mits er een nulmeting is (A4 mist 3).

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Cyber Sale op 25% gerekend en de datums "niet na te lezen", terwijl het besluit van 19 nov 13:45 (35%, 27 nov t/m 2 dec, GEZIEN in het dashboard) al bestond | feit | hoog | besluiten gaan voor |
| 2 | Prijs "nu" op $19 op Gumroad zonder 1.1 en zonder oordeel van Daan of kopers | feit | hoog | besluit 16 nov |
| 3 | Labels: "ons idee van de passingkleur" staat als GEZIEN, is GOK; "254 in 9 dagen" is 11 dagen | feit | hoog | regel 5 eerlijk |
| 4 | De Reddit-draden staan als bewijs voor figuurmakers, maar gaan over een telefoonhouder en een kart. Het label DERDEN klopt, de uitleg niet | feit | hoog | regel 5 eerlijk |
| 5 | Geen persoonsgegevens van Thijs, geen gedachtestreepjes, Nederlands | feit | hoog | regels 2 en 8 |
| 6 | Uitgave van geld (print) netjes via de hoofdchat; plaatsen van filmpjes netjes via de Maker van Roep na keuring; concurrent niet bij naam op onze pagina | feit | hoog | regels 1 en 4 |
| 7 | 151 regels, onder de grens | feit | hoog | bestanden onder ±400 regels |

## Deel C: zou een koper het fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | Elke nieuwe instelling (grip, ratel, elastiek, swivel) komt in een paneel dat al drie stappen heeft. De enige klacht over Cleave is precies "te veel menu's" (feit, Maurice) | Nieuwe opties standaard dicht onder een kop "Hold the pose", met een goede standaardkeuze; het testkaartje als eerste knop voor een nieuwe koper ("Print this first") | klein |
| 2 | De Gumroad-pagina zegt nu al "so your figure holds a pose instead of flopping". Dat ligt dicht tegen een belofte die pas na een print mag (besluit 17 nov). Een koper die een losse knie krijgt, voelt zich bedrogen | Zin vervangen door wat we meten: "stops at 115° instead of bending backwards" | klein |
| 3 | Een koper van de gratis versie moet die eerst uitzetten voor Pro werkt; dat is een stroef eerste moment | In de eerste regel van "Good to know" en in de zip een korte LEESMIJ met één zin; staat er al, maar onderaan | klein |
| 4 | Het sterkste beeld voor een koper is een echte geprinte knie die bij 115° stopt; zonder print blijft elk beeld een render | Print starten (B), en het testkaartje zelf mooi maken: het wordt de foto die verkoopt (zei Daan al, `ontwerp.md` regel 67) | midden |
| 5 | "Split with anything. Make it move with Click Joints." is een sterke, eerlijke zin voor kopers van Cleave | Houden, bovenaan de pagina naast het rig-blok | klein |

## Moet (blokkeert akkoord)
1. **Saleprijzen en marges op 35% zetten**, met de datums 27 nov t/m 2 dec uit het besluit van 19 nov 13:45: Personal $12,35 ($7,83 voor ons), Supporter $15,60 ($9,98), Studio $38,35 ($25,03). "Wat ik niet kon nalezen" over de datums weghalen.
2. **Prijs koppelen aan Pro 1.1.0 en het besluit van 16 nov**: niet "Gumroad nu", maar $19 tegelijk met het uitbrengen van 1.1.0 na het akkoord van Daan (of de hoofdchat legt een nieuw besluit vast). Zet "Pro 1.1.0 uitbrengen" en "Superhive-keuring vóór 27 nov navragen" als eerste punten in de top 5, en schrijf overal dat Figure from rig op main staat en nog niet verkocht wordt.
3. **Het bewijs voor "probleem nummer één" eerlijk maken**: zeg dat de Reddit-draden van 512 en 467 punten over een telefoonhouder en een kart gaan (het loszitten van kogels is breder dan figuren, dat is ook een punt), noem de Formlabs-draad met jaartal (2020) en materiaal (hars), en haal "nog van niemand" weg of verzwak het: Cleave's kogel heeft "socket slits". Verbeter ook de twee labels (passingkleur als GOK, 11 dagen).

## Kan (mag later)
1. Ratel: uitgaan van de klikdiepte 0,25 mm en de rek-eis in `scharnier_neus.py`, niet van tanden van 0,4 tot 0,6 mm; moeite eerder 5 tot 8 runs.
2. Grip: eerst een gefacetteerde kogel of sleuven in de kom proberen in plaats van klemribbels (die slijten volgens de eigen bron); een nieuwe speltoets voor `passing.py` plannen.
3. Gumroad dezelfde week 35% korting geven (code), zodat "Gumroad gelijk aan Superhive" ook in de sale geldt; wij houden dan $10,62.
4. Nulmeting: de hoofdchat vraagt Thijs één keer het aantal Pro-verkopen op Gumroad, zodat de prijsproef iets kan zeggen.
5. Risico nepkorting (prijs omhoog 8 dagen voor de sale) en de openbare Pro-broncode noemen in het prijsadvies.
6. Elastiekkanaal alleen bij kogels vanaf een minimummaat (GOK ±10 mm) en lager zetten dan swivel; de vraag is dun.
7. Testkaartje op 2 tot 3 runs schatten in plaats van 1 tot 2.
