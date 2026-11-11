# Ebb blad v8: dieren v8 en sea log (Mila, 11 nov run 28)

**Opdracht:** "Voor Mila" in `ebb-bouw-1-keuring-drie.md` (dieren v8, sea log, verhaallijn, data voor Gijs).
**Dieren:** `ebb-dieren-v8.png` (alle 25 in het vak 40 x 32 van de sea log op 260; boven gevonden op 0000AA, onder niet gevonden op zwart), vergroot `dieren8/overzicht-v8-3x.png`, maten `dieren8/maten-v8.txt`.
**Blad:** `ebb-blad-v8.png` (6 schermen, links 454, rechts 260 op ware grootte), losse beelden en meting in `blad8/`.
**Data voor Gijs:** `ebb-dieren-v8-data.json` (zelfde formaat als v7, 6280 bytes, controle `blad8/data-v8.txt`).
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
- **Rol 9 = sil**: alleen in het silhouet (vult de krul van de garnaal, zodat de omtrek geen binnenlijnen heeft); gevonden sla je hem over. Alleen de garnaal heeft er een. Andere gaten ontstaan op het horloge niet, omdat je volle veelhoeken tekent.
- Halfdicht oog (`slaperig`) weg: elk dier hetzelfde oog. Komkom heeft nu een glimlach (rol 3).

## Bekeken met Read
Alle 25 dieren op 260, 4 keer vergroot, gevonden en silhouet; het blad op ware grootte. Gezien: orka, haai en dolfijn zijn als omtrek nu uit elkaar te houden (vlek, kieuwen, boog); de reuzeninktvis verloor eerst zijn armen door het dichtmaken, nu alleen bij de krab; de garnaal krijgt een vuldeel (rol 9). Zwakste nog: de zeeotter als omtrek (een blok met voeten) en de maanvis die hoog blijft (30 x 37).
