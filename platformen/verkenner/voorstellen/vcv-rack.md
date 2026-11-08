# VCV Rack Library (betaalde plugins voor de modulaire synthesizer VCV Rack)

Vera, 8 nov 2026 run 15:33. Nagekeken door een controleur (6 van 6 beweringen, één correctie verwerkt).

## Wat het is
VCV Rack is gratis, open software die een modulaire synthesizer (Eurorack) nabootst. Makers schrijven plugins in C++ met daarin modules. Gratis plugins komen open source in de VCV Library; betaalde (premium) plugins verkoopt VCV zelf in die Library, met eigen kopieerbeveiliging. Daarnaast is er sinds sep 2024 het abonnement VCV+ ($29 per maand of $19 per jaar-maand) dat een deel van de premium plugins bevat en waarvan VCV zegt dat het "participating developers" steunt.

## Cijfers
**Bron:** open API `api.vcvrack.com/library/manifests?version=2` (robots.txt staat alles toe), de pluginpagina's op library.vcvrack.com en het forum community.vcvrack.com. Script: `data/vcv-haal-script.py`, prijzen: `data/vcv-premium-2026-11-08.json`.

- Plugins in de Library: 602, waarvan 116 premium van 67 merken (GEZIEN).
- Drukte: 2025 had 47 nieuwe plugins, 2026 al 112 (juli 21, oktober 16, november tot de 8e al 21). De markt trekt dit jaar flink aan (GEZIEN). Premium nieuw in 2026: 19 (GEZIEN).
- **Bereik gratis plugins** (veld popularity = totaal downloads of abonnementen, zie onder):
  - gemaakt feb t/m jul 2026 (3 tot 9 maanden oud): 46 plugins, mediaan 2.318, laagste 1.197, 100% haalt 100+ en zelfs 1.000+ (GEZIEN, controleur zelfde uitkomst).
  - gemaakt in 2025: 41 plugins, mediaan 6.043, laagste 2.647 (GEZIEN).
  - gemaakt sep t/m nov 2026 (0 tot 2 maanden): 32 plugins, mediaan 725, 97% haalt 100+ (GEZIEN).
- **Let op wat popularity telt:** volgens makers op het forum is het het totaal aantal downloads of abonnementen, geen gebruik, en veel gebruikers "abonneren zich op alles" (DERDEN: community.vcvrack.com/t/21133, Squinky en steve, dec 2023; /t/18601, LarsBjerregaard, nov 2022). Echte gebruikers zijn dus veel minder. Toch is het de enige winkel tot nu toe waar letterlijk elke nieuwe plugin 1.000+ downloads haalt.
- **Premium plugins hebben geen teller** (GEZIEN, geen veld popularity). Verkopen zijn nergens openbaar.
- Prijzen premium: meestal $10 tot $40 per plugin, losse modules vanaf $5 (GEZIEN, 116 pagina's; controleur 5 van 5 bevestigd). Nieuwe in 2026 bijvoorbeeld Stochastic Telegraph Twixt $10, Twisted Cable $15, DanT Pro $20, Cardamom Tools $30, Venom Chaos Boxes $40.
- Afdracht: niet officieel gepubliceerd. Eén maker (Cytomic, forum topic 20072, jul 2023) schrijft dat de Library 30% houdt (DERDEN, onbevestigd). De verdeling van VCV+ is niet openbaar.
- Verhouding betaald tegen gratis: maker Vult schat dat betaalde plugins ±0,1 tot 1% van de gebruikers bereiken, zonder harde cijfers en gemeten tegen alle Rack-gebruikers (DERDEN: forum topic 18243, sep 2022).
- Bewijs van geld bij kleine makers: niemand noemt een bedrag. Entrian (Richie) zegt "a lot of paid licenses" te verkopen met een gratis en betaalde versie; Voxglitch begon in 2025 met betaald "voor een beetje inkomen"; Squinky (2022) zou "verbaasd zijn als makers veel verdienen" (DERDEN: forum topic 25454, jan tot jul 2026, en 18243).
- Instappen: verkopen gaat met de hand, je mailt VCV (Andrew) en VCV keurt de code, helpt zelfs met optimaliseren (DERDEN: topic 25454, clone45 en codyge, 2026). Kleine nieuwe makers komen er in 2026 aantoonbaar door (GEZIEN: 6 nieuwe premium merken sinds sep 2026).

## Rekenvoorbeeld (GOK)
Een sterke gratis plugin haalt ±2.000 tot 6.000 downloads in een jaar. Koopt 1% de betaalde versie van $20, met 30% afdracht, dan is dat 20 tot 60 verkopen, $280 tot $840 in totaal, verspreid over een jaar: ±$25 tot $70 per maand. Voor €300 tot €400 per maand zijn ±10 zulke producten nodig, of een uitschieter.

## Voordelen
- Bereik bij nieuwe gratis plugins is het hoogste dat ik heb gemeten (mediaan 2.318, 100% boven 1.000).
- Weinig makers (602 plugins in 8 jaar), echte winkel met afrekenen door VCV, keuring houdt rommel weg.
- Markt groeit in 2026 duidelijk. Prijzen van $10 tot $40 worden normaal gevonden, gebruikers kopen liever dan doneren (steve, topic 16494).
- Gratis plus betaald (lite en pro) werkt hier aantoonbaar als vorm (Entrian, Venom, Voxglitch).

## Nadelen
- Geld niet te meten en geen enkel bedrag van een kleine maker gevonden.
- Kleine markt: de populairste plugin ooit heeft ±244.000 downloads (GEZIEN).
- Betaalde modules worden minder gebruikt omdat patches dan niet te delen zijn (Vult, topic 18243).
- Het werk is klankkwaliteit (DSP): goed klinken is moeilijk te toetsen zonder oren. Testen in de echte app op GitHub Actions moet nog uitgezocht worden (Rack zonder scherm draaien).
- Afdracht en VCV+-verdeling onbekend; instap via een mailtje aan VCV, dat staat op naam van Thijs.

## Wat we er zouden bouwen (eerste idee)
Een gratis plugin met een paar nuttige, mooi ontworpen hulpmodules (bijvoorbeeld een sequencer of akkoordhulp die MIDI leest en schrijft, of een overzichtelijke "patch-assistent"), plus een betaalde Pro-versie met de functies voor mensen die echt patches bouwen. De gratis versie verzamelt het bereik; de betaalde versie verdient.

## Oordeel
**Nee voor nu, cijfer 4.** Bereik is top, maar het telt downloads en niet gebruik, en geld is nergens zichtbaar: geen teller, geen bedrag, geen officiële afdracht. Met de verhouding die makers zelf noemen blijft het per product bij tientallen dollars per maand (GOK).

Wat het zou veranderen: één kleine maker die een bedrag deelt (vraag op het forum, kan alleen onder naam van Thijs) of een openbare verkoopteller. Herhaalmeting over 4 weken met `data/vcv-haal-script.py`: groeit het aantal nieuwe plugins en premium merken verder, dan is de markt in beweging en is een proef met een gratis plus Pro-plugin te overwegen.
