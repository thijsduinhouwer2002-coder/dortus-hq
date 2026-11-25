# Saleweek Click Joints Pro: saleregels, salelink en controle (Bram, 25 nov 2026, issue #61)

**Waarom (geld):** de sale van vr 27 nov is de grootste geldkans van de week. Wij hebben 7.504 YouTube-weergaven en 1 verkoop (GEZIEN, `organisatie/meten/stand.md`). Wie in de saleweek komt, moet de korting meteen zien en ook echt krijgen. Effect op verkoop: GOK.

## 1. Hoe CYBER25 werkt (nagekeken 25 nov ±10:15 NL met curl, zonder inloggen)
- **De code bestaat en hoort bij Pro.** De pagina `.../l/click-joints-pro/CYBER25` geeft nu `"discount_code":{"valid":false,"error_code":"inactive"}`; een verzonnen code (`/NEPCODE99`) geeft `"error_code":"invalid_offer"` (GEZIEN). "inactive" betekent: bekend, maar loopt nu nog niet. Klopt met de inplanning 27 nov 00:00 tot 1 dec 23:59 NL (hoofdchat 19 nov, `organisatie/archief/besluiten-t-m-2026-11-24.md` regel 171).
- **Het scorebord ziet hem ook:** CYBER25, 25%, alleen voor Click Joints Pro, 0 keer gebruikt, geen maximum (GEZIEN, Gumroad API `/v2/products/:id/offer_codes`, `organisatie/scorebord.md`).
- **De link met de code erin werkt**, ook met utm erachter: `/CYBER25?utm_source=yt&utm_medium=video` geeft dezelfde uitslag als zonder utm (GEZIEN). `?offer_code=CYBER25` werkt ook (GEZIEN). Gumroad: "Once you click on the discounted link, you will see that the original price is crossed out, and the discounted price is displayed next to it." (DERDEN, https://gumroad.com/help/article/128-discount-codes)
- **Vanzelf toepassen bestaat bij Gumroad:** "turn on Automatically apply discount code ... every customer gets the discount without doing anything", en de pagina toont dan de doorgestreepte prijs met "applied at checkout" (DERDEN, zelfde hulpartikel). De hoofdchat schreef op 19 nov dat CYBER25 "automatisch toegepast" is ingesteld. Van buiten is dat nu niet te zien: de gewone pagina geeft `"discount_code":null` (GEZIEN), wat ook zo is als de code nog niet loopt. **Dus: zeker weten pas op 27 nov**, met de controle in deel 4.
- **Typen:** het invulvak op de afrekenpagina verschijnt alleen als de maker dat aanzette ("Only if a discount is available"); anders kan een code alleen via de link (DERDEN, zelfde hulpartikel). Of dat vak bij ons aan staat, is van buiten niet te zien (GOK).
- **Conclusie:** de salelink werkt in elk geval. Staat vanzelf toepassen aan, dan krijgt ook wie zonder link komt de korting; komt iemand met de link en staat vanzelf ook aan, dan telt er één korting ("Discounts never stack", DERDEN). Daarom gebruiken alle kanalen die week de salelink.

## 2. De ene salelink voor alle kanalen (vr 27 nov t/m di 1 dec)
```
https://duinhouwer8.gumroad.com/l/click-joints-pro/CYBER25
```
Een kanaal mag er zijn eigen utm achter zetten (`?utm_source=yt&utm_medium=video`, zie `organisatie/meten/korte-links.md`); de korting blijft dan werken (GEZIEN). Per verkoop ziet het scorebord dan de code CYBER25 en de utm.
Superhive heeft geen code: daar is de link gewoon `https://superhivemarket.com/products/click-joints-pro`.

## 3. Saleregels (bovenaan de beschrijving, boven "Rig in. Joints out.")

**Gumroad, regel A** (gebruik deze als de controle zegt dat vanzelf toepassen UIT staat):
```
Cyber Week sale: 25% off with code CYBER25, Friday November 27 to Tuesday December 1 (until 23:59 CET). Personal is $14.25 instead of $19.
```
**Gumroad, regel B** (alleen als de controle zegt dat vanzelf toepassen AAN staat):
```
Cyber Week sale: 25% off, applied at checkout, Friday November 27 to Tuesday December 1 (until 23:59 CET). Personal is $14.25 instead of $19.
```
**Superhive:**
```
Cyber Sale: 35% off on Superhive, Friday November 27 to Wednesday December 2. No code needed. Personal is $7.80 instead of $12.
```

Feiten achter de regels:
- Data Gumroad 27 nov t/m 1 dec en Superhive 35% 27 nov t/m 2 dec: `organisatie/besluiten.md` regel 28 (GEZIEN door de hoofdchat in beide dashboards, 19 nov).
- $19 min 25% = $14.25; $12 min 35% = $7.80 (gerekend). Prijzen nu $19/$24/$59 Gumroad en $12/$45/$3 Superhive (GEZIEN, curl 25 nov). Andere varianten noem ik niet; dat de procentkorting ook op Supporter en Studio geldt is GOK.
- "No code needed" op Superhive: zo werkt een sitewide sale daar (GOK tot de controle op 27 nov de saleprijs op de pagina laat zien). Ziet de controle geen $7.80, dan gaat de Superhive-regel niet online.
- Geen "applied at checkout" op Gumroad zonder dat iemand het zag: zelfde moet als Daan op 20 nov gaf (`platformen/blender/keuring/2026-11-20-blackfriday-teksten-daan.md`, moet 1).

**Weghalen:** de Gumroad-regel op wo 2 dec, de Superhive-regel op do 3 dec. Een regel met een verlopen datum maakt een koper wantrouwig.

## 4. Controle voor de hoofdchat, vr 27 nov ochtend (vóór het plakken)
```
bash platformen/blender/sale-controle.sh
```
Het script leest met curl de gewone Gumroad-pagina, de salelink en de Superhive-pagina, en zegt per stap GOED of FOUT:
1. Salelink: `"valid":true` = goed. Nog `inactive` of `invalid_offer` na 27 nov 00:00 NL = de code staat niet aan: niet plakken, melden.
2. Gewone pagina: `"valid":true` = vanzelf toepassen staat aan, gebruik regel B. Anders regel A.
3. Superhive: $7.80 bij Personal = goed, plak de Superhive-regel. Geen $7.80 = Superhive-regel niet plakken, kijk in het dashboard.

Het script geeft uitgang 0 als alles goed is en 1 bij iets fouts. Proef op 25 nov 10:20 NL: stap 1 "inactive", stap 2 `null`, stap 3 $12 en $45, uitgang 1 (GEZIEN; zo hoort het twee dagen voor de sale).
Met de hand kan het ook: `curl -sL https://duinhouwer8.gumroad.com/l/click-joints-pro/CYBER25 | sed 's/&quot;/"/g' | grep -o '"discount_code":{[^}]*}' | head -1` (GEZIEN, geeft nu `{"valid":false,"error_code":"inactive"}`).
