# Klaarzetblad: Studio wordt "Studio / Seller" op Gumroad (Bram, 24 nov 2026)

Opdracht: Afkijker 24 nov 03:40 (HueForge, `platformen/ideeen/afkijken-2-2026-11-21/doorlopend/2026-11-24-hueforge.md`). Daan keurt de tekst, daarna plakt de hoofdchat hem op Gumroad. Geen prijs, code of variant erbij of eraf: alleen naam en omschrijving van de bestaande $59-variant en één zin in de productbeschrijving.

**Waarom (geld):** "team tot 5" spreekt een kleine Etsy- of MakerWorld-verkoper van flexi-figuren niet aan, terwijl juist die aan zijn prints verdient. HueForge noemt zijn dure trede naar wat je met je prints doet en geeft beta's alleen aan die trede (GEZIEN, https://shop.thehueforge.com/products.json). Effect GOK: als 1 op 5 kopers Seller kiest in plaats van Personal, gaat de opbrengst per 10 kopers van ±$190 naar ±$270. Kost $0.

## Wat er nu op Gumroad staat (GEZIEN 24 nov met curl, https://duinhouwer8.gumroad.com/l/click-joints-pro)
- Variant "Personal": "License for one person." ($19)
- Variant "Supporter": "Same download as Personal, for one person. Helps us keep building." (+$5, dus $24)
- Variant "Studio (up to 5 people)": "License for a team or studio of up to 5 people." (+$40, dus $59)
- Beschrijving, kopje Versions: "Personal is for one person. Supporter is the same download and helps us keep building. Studio is for a team of up to 5 people."

## Nieuwe tekst (Engels, om te plakken)

**Variantnaam** (was "Studio (up to 5 people)"):
```
Studio / Seller
```

**Variantomschrijving** (was "License for a team or studio of up to 5 people."):
```
For a team of up to 5 people, or for sellers of printed figures who want to support the work. Same add-on as Personal. You get new versions first as a beta, and your questions are answered first.
```

**Kopje Versions in de beschrijving** (vervangt de hele zin eronder):
```
Personal is for one person. Supporter is the same download and helps us keep building. Studio / Seller is for a team of up to 5 people, or for sellers of printed figures who want to support the work: you get new versions first as a beta and your questions are answered first. You may sell your prints with any version; Studio / Seller is how sellers support the work.
```

## Waarom zo (eerlijk onder de GPL)
- Click Joints Pro is GPL-3.0-or-later. Daarom staat er nergens dat Personal niet mag verkopen. De laatste zin zegt het juist andersom: met elke versie mag je verkopen.
- De twee echte extra's zijn dingen die wij zelf kiezen en die de GPL niet raakt: wie wij een beta-zip sturen (vaste regel in `platformen/blender/uitgavelijst-pro.md`) en wiens vraag wij eerst beantwoorden (punt 6 in skill `triage`: vraag van een Studio / Seller-koper bovenaan).
- **De factuur op bedrijfsnaam laat ik bewust weg.** Gumroad geeft volgens mij elke koper een factuur waarop hij zelf een bedrijfsnaam zet (GOK, niet nagekeken). Dan is het geen extra van deze trede en zou de tekst meer beloven dan er is. Wil de hoofdchat hem toch: eerst nakijken of Gumroad dat alleen bij sommige kopers doet.
- Geen nieuwe prijzen: $19 / $24 / $59 blijft (besluit 19 nov). Superhive pas na 2 dec en dan apart (daar heet hij Studio, $45).
- CYBER25 (25%, GEZIEN in het scorebord) geldt op alle varianten, dus ook op Studio / Seller; niets aan te passen.

## Na plakken (hoofdchat)
1. Curl de pagina en zoek "Studio / Seller" en "sellers of printed figures"; zet GEZIEN met tijd onderaan dit blad.
2. Variant-id blijft gelijk (alleen hernoemen, geen nieuwe variant), zodat oude Studio-kopers in dezelfde groep blijven voor de beta-post.
3. Zet de nieuwe zin ook in `commercie/blender-click-joints/winkeltekst.md` (FAQ "What is the Studio licence?") of laat Bram dat doen.

## Open voor de hoofdchat (alleen nakijken, niets wijzigen)
- Kan een Gumroad-post (e-mail aan kopers) gefilterd worden op één variant? Ik denk ja (GOK). **Zo niet: haal "You get new versions first as a beta" uit beide teksten vóór plakken.** Een mail-terugval is er niet: wij versturen geen mail (Gmail alleen lezen).

## Keuring
- Daan 24 nov ±04:40: ja na M1 en M2 (`ontwerp/keuringen/2026-11-24-studio-seller-daan.md`). Verwerkt 24 nov ±05:20 door Bram: M1 omschrijving als keus (letterlijk de zin van Daan, ook in de beschrijving); M2 regel 6 in skill `triage`, mail-terugval weg; K1 GPL-zin. Klaar voor de hoofdchat.
