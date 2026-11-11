# Ebb blad v8 (stand v8.1): dieren v8 en sea log (Mila, 11 nov run 28 en 29)

**Opdracht:** "Voor Mila" in `ebb-bouw-1-keuring-drie.md` (dieren v8, sea log, verhaallijn, data voor Gijs).
**Dieren:** `ebb-dieren-v8.png` (alle 25 in het vak 40 x 32 van de sea log op 260; boven gevonden op 0000AA, onder niet gevonden op zwart), vergroot `dieren8/overzicht-v8-3x.png`, maten `dieren8/maten-v8.txt`.
**Blad:** `ebb-blad-v8.png` (6 schermen, links 454, rechts 260 op ware grootte), losse beelden en meting in `blad8/`.
**Data voor Gijs:** `ebb-dieren-v8-data.json` (zelfde formaat als v7, 6270 bytes, controle `blad8/data-v8.txt`).
**Bron:** `bron/ebb_dieren_v8.py`, `bron/ebb_blad_v8.py`, `bron/exporteer_dieren_v8.py`, `bron/overzicht_dieren_v8.py` (bouwen op v7).

## Afvinklijst (keuring bouw 1, voor Mila)
- [ja] 1. Eén eigen kenmerk per dier, ook als omtrek. Nieuw: kenmerkrollen (`licht_k`, `donker_k`) die als silhouet in de randkleur 00AAFF verschijnen, dus als uitsparing. Orka: hoge rechte rugvin plus witte oogvlek (uitsparing). Haai: rechte hoge rugvin, lange bovenste staartlob, drie kieuwen (uitsparing). Dolfijn: snuit en gebogen rug (hij springt). Zwaardvis: zwaard en sikkelstaart. Narwal: rechte, dikkere tand met draai (uitsparing). Zeehond: banaanhouding, kop omhoog, achterflippers omhoog, voorflipper omlaag. Clownvis: banden als uitsparing. Manta: twee kopvinnen naar voren. Rog: ronde schijf met staart.
- [ja] 2. Opnieuw en compact in 40 x 32 op 260: zeeotter (opgekruld, schelp op de buik), zeekomkommer (mint, zonder Zzz, met glimlach en voelers), kreeft (bovenaanzicht, scharen open), maanvis (korte vinnen schuin naar achteren).
- [ja] 3. Silhouet alleen buitenomtrek: gaten worden gevuld, de krul van de garnaal wordt gevuld met een deel dat alleen in het silhouet meedoet (rol 9), bij de krab gaan smalle spleten dicht; armen van octopus, kwal en reuzeninktvis blijven los. Eén oogvorm voor alle dieren (wit met pupil, glans vanaf maat 30; het halfdichte oog is weg). Zeepaardje op de volle vakhoogte, net als kwal, krab en zeester (37 px met rand). Orka-lijf donkergrijs 555555, zadel AAAAAA.
- [ja] 4. Sea log: keuzestip vast 3 px onder de onderkant van het gekozen dier (gemeten aan het dier, niet aan het vak); niet-actieve bladstippen 00AAFF; blad 3 raster om hetzelfde midden als blad 1 en 2 (lager dan v7). Namen in het dierenoverzicht heel (geen "Jellyfis" meer).
- [ja] 5. Eén verhaal, van links naar rechts op het blad, met het schema en "hoogstens één nieuw dier per sessie, laagste nummer eerst":
  - A. 6c, dag 3 avond: sessie 11, reeks 3, geen nieuw dier: "next: Starfish, 1 more day", 3 days in a row. Daan L2: de zin "1 rest day is fine" staat alleen als je gisteren rustte, hier dus niet; onderaan nog twee regels plus stippen.
  - B. 6b, dag 4 ochtend: sessie 12, reeks 4. Starfish (4d) en Octopus (12x) halen allebei hun drempel; Starfish (nr. 7) gaat voor: "new friend: Starfish".
  - C. Sea log daarna: "8 of 24"; blad 1 Pufferfish "1 more day in a row", blad 2 Octopus "next session", blad 3 Whale "at 50 sessions".
  - D. 6d, dag 4 avond: Calm telt als sessie 13: "new friend: Octopus", 4 days in a row.

## Gemeten (260 MIP)
Vorm x op alle zes schermen binnen 0,4 px van het midden; 0 pixels buiten de 64 MIP-kleuren; tekst binnen 0,83 R (`blad8/meting-v8.txt`). Stickerrand en silhouetkleuren zijn gelijk aan v7 (wit 12:1 op 0000AA, 00AAFF 8:1 op zwart), dus het contrast van v7 geldt; de kenmerken in het silhouet zijn 00AAFF op 000055 (zelfde paar als de rand).

## Voor Gijs
- `ebb-dieren-v8-data.json`, formaat als v7 (int8 in 1/90, op het zwaartepunt, hoogstens 42 punten). Nieuw: **rol 7 = licht_k, rol 8 = donker_k**. Gevonden: teken ze als rol 1 en 2. Silhouet: eerst de buitenvorm (alle delen in 00AAFF, 2 px verschoven, dan alle delen in 000055), daarna alleen rol 7 en 8 in 00AAFF erover. Rol 6 (`zz`) komt niet meer voor.
- **v8.1: rol 10 = muts_k** (schelp van de zeeotter: gevonden in MUTS 5555FF, als silhouet in 00AAFF). Rol 9 `sil` komt in v8.1 niet meer voor (de garnaal is nu een open C zonder krul naar binnen). Gaten ontstaan op het horloge niet, omdat je volle veelhoeken tekent.
- Halfdicht oog (`slaperig`) weg: elk dier hetzelfde oog. Komkom heeft nu een glimlach (rol 3).

## Bekeken met Read
Alle 25 dieren op 260, 4 keer vergroot, gevonden en silhouet; het blad op ware grootte. Gezien: orka, haai en dolfijn zijn als omtrek nu uit elkaar te houden (vlek, kieuwen, boog); de reuzeninktvis verloor eerst zijn armen door het dichtmaken, nu alleen bij de krab; de garnaal krijgt een vuldeel (rol 9). Zwakste nog: de zeeotter als omtrek (een blok met voeten) en de maanvis die hoog blijft (30 x 37).

## v8.1: omtrektoets op 260 zonder naam (run 29, opdracht nachtronde 02:58)
Onderaan het blad en in `dieren8/omtrek-260.png` (ware grootte) en `omtrek-4x.png`: alle 25 als omtrek, zonder naam, in geschudde volgorde (sleutel `dieren8/omtrek-sleutel.txt`, script `bron/omtrek_toets_v8.py`).
Eerlijke toets, eerst benoemd en daarna met de sleutel nagekeken:
- **Eerste ronde (v8): 22 van 25.** Mis: garnaal (werd een bol door het vullen van de krul), zeeotter (blok), zeekomkommer (bol met balletje).
- Opnieuw getekend: **garnaal** als open C met waaierstaart buiten de krul en dikke sprieten; **zeeotter** met gezicht en schelp als uitsparing en grotere oren; **zeekomkommer** met bulten boven de rug, vijf voetjes eronder en drie voelers schuin omhoog (geen staart meer, eerst las hij als vis).
- **Tweede ronde (v8.1): 24 van 25 zonder twijfel.** Twijfel blijft: zeeotter (je ziet een liggend dier met gezicht en voeten, "otter" zeg je pas na even kijken). De rog leest als een lolly met staart, maar niet als iets anders.

## v8.2: punten "Voor Mila" uit keuring bouw 2 (run 30, 11 nov)
Bron `bron/ebb_dieren_v82.py` (bouwt op v8, alleen wat verandert), alles opnieuw gemaakt met `bron/maak_v82.py`. Blad `ebb-blad-v82.png`, schermen `blad82/`, overzicht en omtrektoets `dieren82/`, data `ebb-dieren-v82-data.json` (6372 bytes). De v8-bestanden staan er nog naast.
- [ja] 1. **Zeeotter:** drijft op de rug als een bootje. Kop in profiel omhoog links (rond, met oor, roomkleurige snuit als uitsparing en zwarte neus), pootjes houden de schelp boven de buik, twee voeten omhoog rechts, korte platte staart. Bruin (AA5500) met room (FFFFAA), niet meer dezelfde oranje als de vis. 45 x 29 px (was 45 x 24, een blok met vlekken).
- [ja] 2. **Narwal:** lijf, buik, vlekken en vinnen 1,3 keer hoger, tand gelijk. 45 x 24 px (was 45 x 19): 5 px hoger.
- [ja] 3. **Eigen tint:** dolfijn hemelsblauw 55AAFF met lichte buik (blijft), zwaardvis indigo 5555FF met witte buik en lila zeil, zwaard en staart AAAAFF (3,0:1 op het lijf; paars AA55FF haalde maar 1,3:1), haai staalgroen 55AAAA met witte buik (was AAAAFF, gelijk aan de maanvis). Orka blijft grijs 555555. Alle vier nu in één blik uit elkaar.
- [ja] 4. **Zeepaardje voller:** dikke buik met ringen, lange snuit, grote rugvin, staart krult naar buiten. 32 x 37 px (was 25 x 37).
- [ja] 5. **Rog:** ruit met spitse snuit en puntige vleugels, achterkant rond met twee bekkenvinnen, dunne staart met stekel, lichte middenrug. Zandkleur AAAA55, zodat hij ook gevonden niet op de grijze manta lijkt. Als omtrek: vlieger met staart, de manta heeft hoorns. 45 x 36 px.

Gemeten op 260 (`blad82/meting-v82.txt`): vorm x binnen 0,4 px van het midden op alle zes schermen, 0 pixels buiten MIP, tekst tot 0,84 R (sea log 1, gelijk aan v8). Kader x op sea log 3 is -2,5 px (was -0,5): de rog is breder; het kader is het raster, de vorm zelf staat op 0,0. Data opnieuw getekend en vergeleken: 1,6 tot 5,5% randpixels verschil, zoals v8.

Bekeken met Read: de vijf dieren oud en nieuw naast elkaar op 260, 3 en 6 keer vergroot, gevonden en als omtrek; alle 25 in het overzicht; het blad. Eerste otter (lang en plat met lange staart) las als een witte vlek, want het oog was groter dan de kop; kop groter en staart korter gemaakt. Zwakste nu: de voeten van de otter zijn donkerbruin op bruin en vallen op 260 een beetje weg; de vorm leest wel.

Let op: de teksten op dit blad ("next: Starfish", "3 days in a row") volgen nog v8. Besluit hoofdchat 11 nov 04:30 (weken op rij, geen "next") gaat voor en staat bij Gijs punt 4 en 5; dit blad gaat alleen over de dieren.

Omtrektoets v8.2 (`dieren82/omtrek-4x.png`, sleutel `dieren82/omtrek-sleutel.txt`): eerst alle 25 benoemd, daarna met de sleutel nagekeken: **25 van 25** (v8.1: 24 van 25, otter twijfel). Eerlijk: ik tekende ze zelf, dus een frisse beoordelaar telt zwaarder. De otter leest nu door kop met oor, schelp en voeten omhoog; hij blijft de minst strakke vorm van de 25.

## v8.3: punten "Voor Mila" uit keuring bouw 3 (run 31, 11 nov)
Bron `bron/ebb_dieren_v83.py` (bouwt op v8.2), json `ebb-dieren-v83-data.json` (6112 bytes, zelfde formaat en rollen als v8.2), blad `ebb-blad-v83.png`, beelden in `dieren83/`. Nieuw: `bron/horloge_sim.py`, een nabootsing van Gijs' `DierenData.mc` regel voor regel (gehele getallen zoals Monkey C, fillPolygon, fillCircle, stickerrand in 4 schuine richtingen). Gelegd naast het echte FR255-beeld (scène 4, bouw 3): zelfde plusjes-ogen, zelfde harige kogelvis, zelfde stand per pixel op het oog af. Alles hieronder is dus bekeken zoals het horloge het tekent, niet zoals mijn eigen tekenaar.
- [ja] 1. **Ogen.** Oorzaak van de plusjes: `fillCircle` met straal 2 (wit) en 1 (pupil) tekent op het horloge een plus, geen rondje. Nieuw: tot maat 60 alleen een **zwart vierkantje**, zijde `max(2, (8 * maat + 50) / 100)`: 2 x 2 px op 260 (sea log en inhouden), 3 x 3 op 454; geen wit. Vanaf maat 60 (eindscherm op 454) een rond zwart oog, straal `max(3, maat / 20)`, met 1 wit pixel als glimp linksboven. Met zwart op zwart vielen acht ogen weg; die kregen een ander punt in de data: krab van de dunne steeltjes naar het schild, orka in de witte oogvlek, haai, clownvis, kreeft, garnaal, zwaardvis en aal een paar 1/90 naar de dichtstbijzijnde lichte plek. Gemeten met `bron/meet_ogen_v83.py` op alle maten van de app (20, 24, 35, 39, 43, 68): de ring van 1 px rond elk oog haalt bij alle 25 voor minstens 75% 3:1 tegen zwart.
- [ja] 2. **Kogelvis.** 14 dunne stekels werden met de rand van 2 px een harige ring. Nu een bolle vis die naar links kijkt: 6 korte dikke stekels alleen boven en onder, een grote waaierstaart, een vinnetje, getuite lippen als kenmerk. Als silhouet: bol met stekels, staart en tuitmond, een vis en geen zon of zee-egel.
- [ja] 3. **Alle 25 op 260 nagelopen** (maat 20, nagebootst en op het echte beeld). Gevonden en verbeterd: de **narwal**: de drie schuine streepjes op de tand lazen als "zzz", een slapend dier; tand nu glad (de lange tand is zelf het kenmerk, ook als omtrek). Verder niets wat wegvalt of iets anders leest. Zwakste blijven: de zeeotter (voeten donkerbruin op bruin) en het zwaard van de zwaardvis (op 260 een dubbel wit lijntje met lila ertussen).
- Voor Gijs, niet van mij maar wel gezien op het echte beeld: in de sea log op 260 raken de rijen elkaar (zeepaardje tegen kwal en kogelvis, schildpad tegen zeester); dat is zijn punt 9 (3 px tussen rijen).

Bekeken met Read: het echte FR255-beeld 4x, de nabootsing van v8.2 en v8.3 naast elkaar (3x), alle 25 op 260 (3x) en op 454, kogelvis in drie versies (de eerste nieuwe met 9 stekels was nog een zon, de tweede met 8 dunne te rommelig in de witte rand). Eerlijk: de omtrektoets heb ik niet opnieuw zelf gedaan; zie hieronder de frisse toets.

**Frisse toets v8.3** (een agent zonder sleutel, eerst silhouetten, dan kleur; plaatjes `dieren83/toets-sil-3x.png` en `toets-gev-3x.png`, sleutel `toets-sleutel.txt`):
- Silhouet: **20 van 25 goed** (8 daarvan met twijfel). Mis: narwal ("vis met lange snuit"), schildpad, zeekomkommer ("vlek"), garnaal, zeeotter ("vlek").
- Kleur: **22 van 25 zeker of goed met twijfel**, mis: narwal ("witte vis met lange snuit, steur?"). Twijfel: zeekomkommer, zeeotter, manta (gezicht leest als kat), maanvis.
- Kogelvis: silhouet goed met twijfel ("ook zon"), kleur zeker. Dat is de winst van deze run; v8.2 was als silhouet een harige ring.
- Meteen gedaan: **narwal** kreeg een gevlekte grijsblauwe rug (5555AA, vlekken AAAAFF) en witte buik; wit lijf met witte tand smolt samen tot een snuit, nu staat de witte tand los van de donkere kop. Zelf bekeken op 260: leest als kleine walvis met hoorn.
- Open voor de volgende run, eerlijk: **zeeotter** en **zeekomkommer** zijn de zwakste van de 25 (frisse blik en mijn eigen blik zijn het eens). Silhouetten van schildpad en garnaal lezen niet zonder kleur; in kleur wel.
- Daarna in dezelfde run: **zeeotter** voeten en staart in de lijfkleur (donkerbruin viel weg), schelp 1,6 keer zo groot zonder ribbels (die werden een donkere V), pootjes erop. **Zeekomkommer** als lange worst (1,3 keer), puntige bulten, voelers als bloemetje vooruit aan de kop (omhoog lazen ze als een walvisfontein).

**Frisse toets 2 v8.3** (nieuwe agent, nieuwe volgorde; `dieren83/toets2-*.png`, sleutel `toets2-sleutel.txt`):
- Silhouet: **24 van 25 goed** (12 met twijfel). Mis alleen de zeeotter ("vlek met een gat").
- Kleur: **25 van 25 goed**, twijfel bij zeeotter ("bruine klont"), zeekomkommer ("rups met stekels", wat een zeekomkommer ook is), manta (gezicht als kat) en narwal (tand leest als losse stok).
- Open voor de volgende run: zeeotter blijft de zwakste; daarna manta-gezicht en narwaltand (dunner, puntig, uit de bovenlip).
- Nachtronde 05:35 (zelfde opdracht, stond al): de twee open punten uit toets 2 meteen gedaan. **Manta:** geen mond meer, ogen opzij aan de hoorns, vleugels met spitse punten naar achteren (het "kattengezicht" kwam van hoorns plus ogen plus mond ertussen). **Narwal:** tand dunner en puntig, groeit uit de bovenlip (las als losse stok). Ogen opnieuw gemeten: alle 25 goed. Bekeken op 260 (6x): manta leest als vleugeldier met hoorns, narwal als kleine walvis met hoorn. Zeeotter blijft als silhouet de zwakste; dat is het enige open punt.
