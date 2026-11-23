# Keuring concurrentie Splitser, 23 nov 2026, keurder concurrentie (opdracht hoofdchat)
Wat ik keurde: `producten/blender-splitser/concurrentie.md` (commit b97e78f45, stand op main 720770555). Alles met curl nagelezen op 23 nov 2026 ±18:30 tot 19:30 NL; geen account, niets gekocht.
Akkoord: **nee** (3 moet-punten over het verkoopverhaal, 2 kleine moet-punten over regels en geld)

Kort: de cijfers en citaten kloppen bijna allemaal en zijn netjes gelabeld. Maar twee van de vier "zo worden we beter"-punten zijn als "niemand doet dit" geschreven, en dat klopt niet. Tegen de grote vier (CatPin, Cleave, Split 3D Print, Dovetail Key) houdt het verhaal stand; tegen de hele markt niet. Het verkoopverhaal valt niet om, maar moet smaller en eerlijker.

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| A1 | CatPin `sales_count` **2042** klopt (GEZIEN, [catpin.json](https://alexsokol.gumroad.com/l/catpin.json)), aangemaakt 20 jul, 85 beoordelingen, 4,8. Gumroad-prijs $21 (was $30); tiers daar heten "CatPin + Thanks" $31,50 en "ProMax" $70 (de $36 en $80 in de tabel zijn de Superhive-prijzen; staat niet fout, wel door elkaar). | feit | hoog | |
| A2 | Superhive-tellers kloppen: CatPin 400+ (3 maanden), Cleave 300+ (2 maanden, $23, Support $28), Split 3D Print 400+ (4 maanden, $22, gratis $0, Support $28, 5 pl. $59), Dovetail Key 800+ (5 maanden, $18, 13 beoordelingen, gemiddeld 4, 62/24/16%). | feit | hoog | |
| A3 | Split toont op Superhive **twee** tellers: "Sales 400+" en "Downloads 400+". Dat de 400+ de gratis variant meetelt is dus een GOK, geen GEZIEN. | feit | hoog | |
| A4 | "±$50K tot $70K" als GOK is eerlijk gelabeld en de som klopt (2.450 x $21 en x $30). De ondergrens is wel aan de hoge kant: CatPin had een coupon van 30% en een actieprijs, en Superhive houdt op het gratis plan ±35% in (welk plan CatPin heeft is onbekend). Netto voor de maker eerder ±$35K tot $55K (GOK). | feit (som), vermoeden (ondergrens) | midden | Gumroad-tiers en coupongebruik zijn niet openbaar |
| A5 | Omzetverwachting $600 tot $1.400 per maand (30 tot 60 verkopen) is alleen het goede scenario. De eigen tabel 2c laat zien dat bijna alle nieuwkomers op 0 tot 40+ verkopen in 1 tot 8 maanden blijven (SPLIT IT 20+, SnapSplit 30+ in 8 maanden, North Slice, Bed Fit Splitter, Print Ready Kit zonder teller). Alleen makers met dagelijkse Shorts en wekelijkse updates halen 100+ per maand. Er staat geen laag scenario en geen netto (Superhive ±65%, Gumroad eigen link ±84%, Gumroad Discover 70%, zie `commercie/blender-click-joints/prijs.md` en `platformen/succes/verhalen.md` verhaal 16). | vermoeden | midden | eerste 4 weken verkopen van de Splitser zelf |
| A6 | **Passingproef: "Niemand in Blender doet dit" klopt niet.** PrintForge ($8,99, Superhive, ±2 maanden oud) heeft "Create Fit Test Coupon" die "two small test parts" maakt ([docs](https://superhivemarket.com/products/print-forge/docs)). Fit & Tolerance Test Generator ($7) maakt een plaat met gaten en pennen op 2 tot 12 spelingen, "The clearance is engraved next to every hole" ([pagina](https://superhivemarket.com/products/fit-tolerance-test-generator)). Die laatste staat al in onze eigen repo (`commercie/blender-click-joints/winkeltekst.md` regel 103, `platformen/succes/verhalen-groei.md` regel 706). CatPin raadt een proef zelf aan maar heeft geen knop: "A small test print is recommended" ([FAQ](https://superhivemarket.com/products/catpin/faq)). Wat wél klopt: geen van de grote vier heeft het (GEZIEN: winkelpagina, versiegeschiedenis, FAQ, docs en Gumroad-tekst van alle vier). Cleave heeft alleen Reassemble in Blender. Ons echte verschil: de proef met **jouw eigen verbinder** op 4 spelingen, onthouden per printer en materiaal, binnen de splitser. | feit | hoog | |
| A7 | **Nummers op de snijvlakken: "Niemand heeft dit (GEZIEN, geen van de pagina's)" klopt niet.** Split3MF (gratis web, staat zelf in tabel 2c en in de eigen Reddit-bron 1xsdh9i) heeft de optie "Number both cut faces" en schrijft: "Each cut face is engraved 'piece number-joint number'" ([split3mf.com/fit-to-printer](https://split3mf.com/fit-to-printer)). PrintForge heeft "numbered identifiers", een uitgeklapt beeld en een **bouwplaatje** (`Assembly Guide.html` en `parts.svg`, "a numbered visual index"), maar zegt zelf dat versie 1.0 geen "engraved labels" heeft. Luban nummert delen volgens een forumgebruiker (DERDEN, [Bambu-forum](https://forum.bambulab.com/t/cutting-big-models-like-luban3d/250540)). Wat wél klopt: geen Blender-add-on die ik vond graveert nummers in de snijvlakken; geen van de grote vier nummert iets (Cleave nummert alleen bestandsnamen bij export, versie 1.2.0). Het bouwplaatje is dus geen voorsprong. | feit | hoog | |
| A8 | Wandcheck (punt 3): PrintForge heeft ook een wandcheck ("Sampled thin walls", rood), maar niet per verbinder en niet in mm per verbinder. Cleave kleurt het stuk verbinder dat buiten het model steekt rood (1.7.0). "Per verbinder in mm met reden" blijft een verschil, maar PrintForge hoort in tabel 2c en tabel 2a-regel "Wandcheck" moet de bron noemen. | feit | hoog | |
| A9 | Citaten: ik controleerde er **17** bij de bron, allemaal echt en woordelijk: Cleave "six hour print" en "minor bugs that made my blender crash" en "many menu's"; Dovetail Key "vibe coded tools ... preview glitching"; CatPin Gumroad (51 met tekst, 44x5, 6x4, 1x1) "throws an error", "i have an error", "too fast", "proper documentation", Spaans tutorial, "flat side", "discount"; CatPin SH "2 holes and a pin"; Split "gouged a small surface chunk" (model was echt "very high-poly") en "thanks Google!"; Reddit SideSplitter, CadSplit, obloid, Bambu-tip (51 punten, van BambuLabSupport); Meshy; Easy-Print "infinite plane"; EasySlice "eyes, buttons". "3 van 6 vier-sterren over uitleg" klopt. De conclusies volgen eruit. | feit | hoog | |
| A10 | Klacht 1 leunt op de winkeltekst van Cleave ("six hour print"), dat is reclame van een concurrent, geen klacht van een koper. Het obloid-citaat is wel een maker-stem. Echte kopersklachten over speling vond de analist niet; de proef is dus een GOK op vraag, net als de nummers (punt 12 zegt dat eerlijk, punt 1 niet). | feit | midden | YouTube-reacties of Reddit-zoeken op "tolerance" en "doesn't fit" |
| A11 | YouTube-cijfers kloppen (GEZIEN nu: 564.171, 483.117, 258.637, 118.890, MeshyAI 3.155.024, "4mo ago"). Het MeshyAI-filmpje staat op het bedrijfskanaal van Meshy en is waarschijnlijk betaald gepromoot; als bewijs van "vraag naar uitleg" is het zwak. | feit (cijfers), vermoeden (promotie) | midden | YouTube-statistieken zijn niet openbaar |
| A12 | Kleine fouten: Cleave 1.0 kwam op **23 sep** volgens de [versiepagina](https://superhivemarket.com/products/cleave/versions), niet 17 sep. Superhive toont 11 versies (Cleave zegt zelf "12 free updates since launch"), dus "13 versies" is net te hoog. Dovetail Key "Mesh repareren: meerdere solvers" is een terugval tussen boolean-solvers, geen reparatie. | feit | hoog | |
| A13 | Prijsadvies $24, start $19, Supporter $34, Studio $79 past bij de markt ($18 tot $24 bij de vier die verkopen, GEZIEN). De bundel $35 met Click Joints Pro is logisch (CatPin zegt zelf geen beweegbare gewrichten). | feit | hoog | |
| A14 | Gratis variant op dezelfde Gumroad-pagina: de onderbouwing (Split staat 2e op Gumroad-zoeken "daardoor") is een GOK op oorzaak, niet zo gelabeld. Risico voor geld: Gumroad geeft de pagina dan als prijs **"$0"** (zo staat het in [Split json](https://auerblender.gumroad.com/l/kxxyq.json): `price_formatted "$0"`), gratis downloads tellen niet mee voor de $100 die Discover vraagt, en "één rechte snede plus ronde pen" doet hetzelfde als de gratis slicers en Easy-Print (7.855). Voordeel: Gumroad laat je alle kopers mailen, ook gratis, dus een lijst voor de betaalde versie. | vermoeden | midden | A/B: 2 weken alleen betaald, daarna gratis erbij, verkopen per dag vergelijken |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| B1 | Vier citaten zijn langer dan 15 woorden: SideSplitter (±22), CadSplit (17), de eerste zin van Dovetail Key in 2b (±28), Meshy (17). | feit | hoog | citaten kort |
| B2 | Geen persoonsgegevens: alleen openbare makersnamen en winkellinks; reviewers en Reddit-schrijvers zonder naam. `check.py` geeft OK. | feit | hoog | harde regel 2 |
| B3 | Geen gedachtestreepjes gevonden. | feit | hoog | harde regel 8 |
| B4 | Labels bijna overal goed. Uitzonderingen: "Niemand heeft dit (GEZIEN)" bij punt 4 is fout (zie A7); de Meshy-zin staat als DERDEN maar is zelf gelezen (mag GEZIEN, het is wel hun eigen bewering); Split "inclusief gratis" is GOK (A3). | feit | hoog | harde regel 5 |
| B5 | Onderaan staat "Keuring: nog niet gedaan". Na deze keuring en de fixes bijwerken. | feit | hoog | werk is af na keuring |

## Deel C: zou een koper het willen? (het verkoopverhaal, als koper bekeken)
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| C1 | "Past de eerste keer" blijft de sterkste belofte, ook als hij niet uniek is: de grote vier hebben hem niet, en de twee die een proef hebben zijn kleine, losse tools zonder teller. Een koper gelooft het pas als hij een echte print ziet passen. | In de Short: proefblokje van de printer, vier pennen, één klikt. Geen "niemand doet dit" in de winkeltekst, wel "in één knop, met je eigen verbinder". | klein |
| C2 | Nummers in het snijvlak zie je in één beeld, en in Blender heeft niemand het. Maar Split3MF doet het gratis in de browser. | Zeg "gegraveerd in het verborgen snijvlak, in Blender" en laat het bouwplaatje als voorsprong vallen. | klein |
| C3 | Cleave brengt ±wekelijks een versie uit; een passingproef of nummers kan hij in een week namaken. De voorsprong zit in snelheid en in betrouwbaarheid op lelijke meshes (punt 2), niet in één functie. | Zet punt 2 (nooit vastlopen, e2e met 10 AI-modellen) hoger in het verhaal; dat is moeilijker na te doen. | klein |
| C4 | Een koper die "$0" ziet op de Gumroad-pagina kiest vaak de gratis versie en komt niet terug. | Begin alleen betaald met $19, gratis variant pas na 2 weken of op een eigen pagina, en meet. | klein |

## Moet (blokkeert akkoord)
1. **Passingproef (punt 1, tabel 2a, klacht 1):** "Niemand in Blender doet dit" vervangen door wat klopt: geen van de grote vier heeft het; PrintForge ($8,99) en Fit & Tolerance Test Generator ($7) hebben een losse proef. Ons verschil is de proef met je eigen verbinder op 4 spelingen, onthouden per printer en materiaal. Bronnen erbij.
2. **Nummers (punt 4, tabel 2a "Labels", must have 8):** "Niemand heeft dit (GEZIEN)" vervangen: Split3MF graveert "piece number-joint number" in elk snijvlak (gratis web); PrintForge heeft genummerde delen en een bouwplaatje zonder gravure. Wel uniek: gegraveerd in Blender. Bouwplaatje niet als voorsprong noemen.
3. **PrintForge en Fit & Tolerance Test Generator** in tabel 2c zetten (prijs, wat, geen teller, link), en wandcheck (punt 3) afzetten tegen PrintForge.
4. **Omzet (sectie 1 en 5):** naast 30 tot 60 per maand een laag scenario zetten op basis van de nieuwkomers in tabel 2c (GOK, bijv. 5 tot 15 per maand), en netto per verkoop noemen (Superhive ±65%, Gumroad eigen link ±84%, Discover 70%).
5. **Vier citaten** onder 15 woorden brengen (SideSplitter, CadSplit, Dovetail Key-zin in 2b, Meshy).

## Kan (mag later)
- Ondergrens CatPin-omzet iets lager (coupon 30%, actieprijs, Superhive-afdracht), bijv. ±$35K tot $70K bruto.
- Cleave 1.0 op 23 sep; "11 versies op Superhive, 12 updates volgens Cleave"; Dovetail Key "solvers" niet als mesh-reparatie.
- Split "inclusief gratis" als GOK labelen; "staat 2e door de gratis variant" als GOK labelen.
- Gratis variant: advies uit C4 overwegen; het is een afweging, geen fout.
- MeshyAI-filmpje noemen als bedrijfskanaal; vraag beter onderbouwen met de onafhankelijke tutorials (564K, 483K, 258K).
- Klacht 1 eerlijk maken: de "six hour print"-zin is Cleave-reclame; vraag naar een proef is een GOK zoals bij punt 12.
- Gumroad-tiers van CatPin ($31,50, $70) apart van de Superhive-tiers noemen.

## Herkeuring, 23 nov 2026 ±20:15 NL, keurder concurrentie
Wat ik keurde: `producten/blender-splitser/concurrentie.md` op commit d51daa6c9, alleen de 5 moet-punten plus een blik op nieuwe fouten. Bronnen opnieuw met curl.
Akkoord: **ja**

| # | Moet-punt | Verwerkt? | Feit of vermoeden | Zekerheid |
|---|---|---|---|---|
| 1 | Passingproef niet "niemand" | ja. Punt 1, tabel 2a (met CatPin-FAQ), klacht 1 en must have 4 zeggen nu: geen van de grote vier, wel losse proeftools; ons verschil is de eigen verbinder op 4 spelingen, onthouden per printer. Vraag staat eerlijk als GOK, Cleave-zin als reclame. | feit | hoog |
| 2 | Nummers niet "niemand" | ja. Punt 6 (zakt van 4 naar 6), klacht 12, must have 8 en tabel 2a: Split3MF graveert, PrintForge nummert zonder gravure, uniek alleen gegraveerd in Blender. Bouwplaatje niet meer als voorsprong. Citaat "Every cut face is numbered" staat zo op [split3mf.com](https://split3mf.com/fit-to-printer). | feit | hoog |
| 3 | PrintForge en testgenerator in 2c, wandcheck ertegen | ja. Beide rijen kloppen met de pagina's ($8,99; $7 nu $5,25; 29 dagen; geen teller; "engraved labels" niet in 1.0). Punt 3 zet de wandcheck af tegen PrintForge en Cleave. | feit | hoog |
| 4 | Laag scenario en netto | ja. Laag 5 tot 15, hoog 30 tot 60, beide GOK. Netto narekend: Superhive (24 min 5,5% min $0,49) x 70% = $15,53; Gumroad eigen link ±$19,60; Discover $16,80. Laag ±$80 tot $300, hoog ±$500 tot $1.200: klopt. CatPin-omzet nu ±$35K tot $70K. | feit | hoog |
| 5 | Vier citaten onder 15 woorden | ja. SideSplitter, CadSplit, Dovetail Key en Meshy zijn ingekort en kloppen nog met de bron. | feit | hoog |

Ook verwerkt uit de kan-lijst: Split-teller als GOK, gratis variant pas na 2 weken, MeshyAI als bedrijfskanaal, Dovetail "solvers", CatPin Gumroad-tiers, Cleave-versies. Mijn eigen kan-punt over Cleave 1.0 was half fout: de Cleave-pagina zelf zegt "1.0 17 Sep", de versiepagina 23 sep; de analist noemt nu beide, dat is juist.

Nieuw ingeslopen, niets dat blokkeert:
- Kan: de Split3MF-rij zegt "downloaden vraagt Pro". Dat zag ik niet bevestigd: de eigen Reddit-post van Split3MF (1xsdh9i) noemt alleen tools met een kroon als Pro, en "Fit to printer" staat daar niet bij. Label als GOK of naar "gratis web" terugzetten. Ons verhaal verandert er niet door.
- Kan: de Cleave-titel in tabel 2b is 17 woorden, maar het is een producttitel, geen citaat van een persoon. Mag blijven.
- Geen nieuwe gedachtestreepjes, `check.py` OK, nieuwe cijfers hebben allemaal een label.
- Onderaan concurrentie.md staat nu "wacht op herkeuring": de analist kan dat bijwerken naar akkoord ja.
