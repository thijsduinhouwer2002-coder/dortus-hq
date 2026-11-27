# Eigen pagina's: de salelink in plaats van de gewone link, en "applied at checkout" eruit (Verspreider, run 39, vr 27 nov 2026, C)

**Status:** keuring Daan gevraagd. Na zijn ja: deel 1 doet Bram (repo dortus), deel 2 de hoofdchat (repo click-joints). Deel 3 (terugzetten) op wo 2 dec, samen met Brams weghaalklus.

## Waarom (geld en eerlijkheid)
Wie ons al kent (gratis gebruikers, kijkers van YouTube Shorts, lezers van de gidsen) komt in de saleweek via onze eigen pagina's bij Pro. Die pagina's linken nu allemaal naar de gewone Gumroad-pagina, en daar staat de korting niet vanzelf aan:

- `bash platformen/blender/sale-controle.sh` om ±02:55 NL (GEZIEN): de salelink `/CYBER25` geeft 25%, $19 wordt $14.25; de gewone pagina geeft `"discount_code":null`. "Automatically apply" staat dus nog uit (zelfde als de hoofdmanager om 00:40 zag).
- dortus.com/click-joints/ zegt nu letterlijk: "From November 27 to December 1, Pro is 25% off on Gumroad, applied at checkout." (GEZIEN, `dortus/click-joints/index.html` regel 223). Dat klopt nu niet: wie op de knop drukt en de code niet typt, betaalt $19. Dat is een belofte die we niet waarmaken, en een koper die het merkt voelt zich bedrogen.
- Geen van onze eigen pagina's gebruikt de salelink (GEZIEN, curl ±02:55 NL): dortus.com/, dortus.com/click-joints/, dortus.com/yt, dortus.com/tt en de README van click-joints linken naar `https://duinhouwer8.gumroad.com/l/click-joints-pro` zonder code, en noemen CYBER25 nergens.

De salelink werkt in beide gevallen: staat "Automatically apply" uit, dan geeft de link toch de korting; zet Thijs het aan, dan doet de link niets mis. Dus dit is goed ongeacht wat er in het dashboard gebeurt.

Effect op verkoop: GOK. Elke koper via onze eigen pagina's betaalt $14.25 in plaats van af te haken bij $19, en niemand voelt zich misleid. Kost: ±10 minuten voor Bram, ±2 minuten voor de hoofdchat. Geen geld, niets onder de naam van Thijs.

## Deel 1: dortus.com (Bram, repo dortus, commit 9e3d0d4 als basis)

**1a. `click-joints/index.html` regel 223:** vervang
```
From November 27 to December 1, Pro is 25% off on Gumroad, applied at checkout.
```
door
```
From November 27 to December 1, Pro is 25% off on Gumroad with code CYBER25: the button below applies it.
```

**1b. `click-joints/index.html` regel 229:** in de knop alleen de href:
```
https://duinhouwer8.gumroad.com/l/click-joints-pro
```
wordt
```
https://duinhouwer8.gumroad.com/l/click-joints-pro/CYBER25
```
(Knoptekst blijft "Get Click Joints Pro on Gumroad". Regel 36, de Offer in de gestructureerde gegevens, blijft zoals hij is: die is voor zoekmachines en moet de vaste prijs houden.)

**1c. `index.html` regel 179** (knop "Pro on Gumroad"): zelfde href-wissel naar `.../click-joints-pro/CYBER25`.

**1d. `yt/index.html` en `tt/index.html`, regel 37 en 63:** zelfde href-wissel naar `.../click-joints-pro/CYBER25`. Op regel 37 ook de knoptekst:
```
Get Click Joints Pro, $19
```
wordt
```
Get Click Joints Pro, $14.25 until Dec 1
```
(25% van $19 is $14.25, GEZIEN in de salecontrole; de code loopt af op `2026-12-01T22:59:00Z` = di 1 dec 23:59 NL, GEZIEN in de Gumroad-pagina.) Regel 63 houdt zijn knoptekst.

Controle na live (Bram): `curl -sL https://dortus.com/click-joints/ | grep -c "applied at checkout"` moet 0 geven, en `grep -c "click-joints-pro/CYBER25"` op de vier pagina's minstens 1.

## Deel 2: README click-joints (hoofdchat, repo click-joints)

Bram zet de nieuwe regel in `producten/blender-gewrichten/repo-click-joints/README.md`; de hoofdchat pusht. Na regel 32 (`On Gumroad: personal license $19, ...`) één regel erbij:
```
Until December 1: 25% off on Gumroad with code CYBER25, or use this link, which applies it: https://duinhouwer8.gumroad.com/l/click-joints-pro/CYBER25
```

## Deel 3: terugzetten op wo 2 dec (Bram en hoofdchat)
Na het aflopen van de code geeft de salelink geen korting meer en hoort de saletekst weg:
- `click-joints/index.html` regel 223: de hele zin "From November 27 to December 1, ..." weg; regel 229 en `index.html` 179 terug naar de gewone link.
- `yt/` en `tt/` regel 37: terug naar "Get Click Joints Pro, $19" en de gewone link; regel 63 de gewone link.
- README click-joints: de regel "Until December 1: ..." weg.
