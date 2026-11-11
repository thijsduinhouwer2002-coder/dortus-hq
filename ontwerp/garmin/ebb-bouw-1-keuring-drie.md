# Keuring echte bouw 1 (schermen zonder dieren) en dieren v7, drie frisse beoordelaars (11 nov 02:55)

Cijfers: visueel bouw 4, dieren v7 6; product bouw 4; veiligheid en code 6. Dit is een tussenstand: 13 van de 22 schermen staan in geen testbeeld.

## Voor Gijs (bouw 2), volgorde van belang
1. FOUT: na FASE_KLAAR opent BACK het pauzemenu en "Save" slaat de sessie dubbel op (today, 8 weeks, sessieDagen, dierenteller). In FASE_KLAAR: BACK sluit of gaat naar het menu, nooit pauzemenu. Test erbij.
2. Uitlegzin "then hold while the sea gets dark" weg; wordt "then hold only while it feels easy". Zelfde in de winkeltekst. Belletjes verdwijnen niet als laatste-stand-signaal.
3. Letter: de smalle letter van het ontwerp (Barlow Condensed, OFL) als eigen lettertype in een paar maten (kop, tekst, groot cijfer) per schermmaat 454, 416, 390, 260. Nu oogt het als standaard Garmin.
4. AMOLED (fenix 8, fr265, venu, vivoactive 5, epix): zee met verloop en lichte kam (tekenen of afbeelding per maat), volle kleuren; palet van 64 alleen op MIP (fr255, fenix 7, fr955/965 MIP-versies).
5. Ademen: blauwe zee zoals het blad, cijfer altijd boven de hoogste golfstand. Rustig: zoals blad 5 (zwart, zee onderaan, groot cijfer met s, "Calm 4-7-8"), geen teal vlak met wit (2,86:1).
6. Menu: het eigen dier zwemt mee (niet de rode vis); schuimgolf zoals het blad.
7. Bouw het eindscherm 6c (en 6b als Mila's dieren er zijn): rondes done, tijden, next, stippen met label; past bij 1 tot 6 rondes, ook op 260; daarna pas today.
8. Bouw de sea log als raster 3 x 3 over drie bladen met dieren als data (ebb-dieren-v7-data.json, later v8); weg met de lijst van 4.
9. Settings in Ebb-stijl (zwart, gekozen regel als blauwe pil), op knop- en aanraakhorloges; woorden van blad v7 ("Buzz every 30 s", "Buzz on last 3 breaths", "Ebb makes no sound"); geen "touch lock" in de winkeltekst als het geen instelling is.
10. Testbeelden met vaste namen per scherm: veilig 1/2/3, start, uitleg, ademen in en uit, inhouden 0:30/1:45/2:30/3:04, herstel, rustig, einde, today (ook 6 rondes en 3 sessies), 8 weeks, sea log 1/2/3, sea log dier, settings 1/2; op 454, 416, 390 en 260; demo-a repareren; beelden ook op venu2, venu3, epix2pro, fr965.
11. Winkeltekst in drie talen gelijk aan de app: Box en Calm 5.5 eruit (titel, tags, tekst), geen "one V per round", "Sit or lie down", veiligheidszinnen letterlijk van de drie bladen, geen dier-beloften die nog niet gebouwd zijn, nagekeken-lijst opschonen.
12. Dode code weg (EbbStart.menu, StartDelegate, vPunten, diepste, getijPunten, gemiddeldeLijn, Box in PATROON_NAMEN). status.md bijwerken.

## Voor Mila (dieren v8)
1. Elk dier één eigen kenmerk dat ook als omtrek (niet-gevonden) overeind blijft: orka hoge rugvin plus witte vlek als uitsparing; haai rechte hoge rugvin en kieuwen; dolfijn snuit en gebogen rug; zwaardvis zwaard en sikkelstaart; narwal rechte gedraaide tand; zeehond kop omhoog en flippers; clownvis strepen als uitsparing; manta kopvinnen; rog ronde schijf.
2. Opnieuw en binnen ongeveer 40 x 32 px op 260: zeeotter, zeekomkommer (zonder Zzz, niet rood), kreeft, maanvis.
3. Tekenregel: niet-gevonden alleen buitenomtrek (garnaal zonder binnenlijnen); per houding één oogvorm; zeepaardje even hoog als de rest; orka-lijf donkergrijs (85,85,85).
4. Sea log: keuzestip vast 3 px onder het gekozen dier of een ring; niet-actieve paginastippen (0,170,255); pagina 3 raster iets lager; labels niet afgekapt.
5. Verhaallijn op het blad in één volgorde (8 of 24, 6b, 6c).
Lever als data (json) voor Gijs.

## Open voor Thijs (08:00)
Reeksregel (dagen of weken op rij); Box (weg uit de winkel, of terug in de app).
