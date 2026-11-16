# LG webOS Content Store en Samsung Smart TV-apps (Tizen)

Vera, 16 nov 2026, run 03:31 (Amsterdam). Vervolg op de Roku-meting van 13 nov (cijfer 2). Snelle schifting met bronnen, geen eigen lichting: de twee harde drempels hieronder maken een telling overbodig.

## Uitkomst
**Nee, cijfer 1.** Bij LG kun je niet meer via de winkel laten betalen, bij Samsung kom je buiten de VS alleen binnen met een contract met Samsung. Het verdienmodel van veel kleine tv-apps (proxy-SDK's) wordt in 2026 juist verboden.

## Wat ik zag
- **LG betalen: weg.** "The LG Billing Service for In-App Purchase is no longer provided." LG raadt Paymentwall aan en kan een apart contract vragen bij een andere betaalpartij (GEZIEN, zelf nagelezen 16 nov, https://webostv.developer.lge.com/develop/guides/in-app-purchase).
- **LG publiceren: mag als particulier** ("Individual Seller ... under a personal name"), in 36 landen (GEZIEN door de onderzoeker, https://webostv.developer.lge.com/distribute/app-ecosystem). Keuring duurt lang: na 31 dagen nog "QA Processing", een maker wachtte meer dan 6 maanden (GEZIEN door de onderzoeker, forum.webostv.developer.lge.com/t/1941 en /t/10482).
- **Samsung publiceren: alleen in de VS zonder contract.** Een Public Seller "can launch TV application services only in the United States"; buiten de VS eerst een "offline contract with Samsung HQ or a local subsidiary" (GEZIEN, zelf nagelezen 16 nov, https://developer.samsung.com/tv-seller-office/guides/membership/becoming-seller-office-member.html). Samsung Checkout bestaat wel (ook Nederland), maar de documentatie spreekt steeds van partners (GEZIEN door de onderzoeker, https://developer.samsung.com/tv/develop/guides/samsung-checkout). Afdracht niet gevonden.
- **Omvang:** 413+ miljoen verkochte Tizen-toestellen tot en met 2025 (DERDEN, samsungtizenos.com). Beide winkels samen een paar duizend apps: Spur pakte 6.038 webOS- en Tizen-pakketten uit (DERDEN, ppc.land). Nieuwe apps per maand: niet gevonden.
- **Geld van kleine makers:** geen enkel bedrag of downloadcijfer van een indie-maker gevonden. Ruim 42% van de LG-apps en ruim een kwart van de Tizen-apps verdiende via proxy-SDK's (vooral Bright Data); LG en Samsung schorsen die apps nu (DERDEN, krebsonsecurity.com, juli 2026).
- **Vindbaarheid:** zoeken op naam en een rij "most popular". De webwinkel van LG (us.lgappstv.com) draait alleen met JavaScript en toont geen tellers; Samsung heeft geen openbare webwinkel. Zelf meten kan dus niet met open pagina's.
- **Bouwen en testen:** de webOS TV 26 Simulator draait op Ubuntu 24 (webapps); de Tizen-emulator draait op QEMU. Bouwen zou dus kunnen, maar dat helpt niet zonder betaalroute.

## Voor- en nadelen
- Voor: heel veel tv's, weinig apps, LG laat particulieren toe, testen op Linux kan.
- Tegen: geen betalen via de winkel bij LG, contract nodig bij Samsung buiten de VS, keuring weken tot maanden, geen tellers, geen bewijs dat kleine makers verdienen.

## Advies
Nee. Niet opnieuw meten, tenzij LG weer een eigen betaalsysteem invoert of Samsung de Public Seller buiten de VS opent. Samen met Roku (2) is de tv-hoek voor kleine betaalde apps dicht; alleen Fire TV Vega OS (pionier, 6) heeft daar een echte betaalroute.
