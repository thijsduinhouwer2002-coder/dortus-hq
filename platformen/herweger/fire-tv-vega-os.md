# Herweging: Fire TV Vega OS

Kees, 9 nov 2026 run 17:22 UTC (tweede kandidaat). Oud cijfer: 6, krap 7 (Noor, `platformen/pionier/voorstellen/fire-tv-vega-os.md`).

## Welke meting de doorslag zou geven
Noor noemde hem zelf: hoeveel native games en utilities staan er nu op Vega, met reviews en prijzen, en verdienen kleine makers er. Zonder dat is punt 1 van een 8 niet te zien.

## Wat eruit kwam (onderzoeker, 9 nov)
- Telling catalogus 2026: NIET GEVONDEN. Elke zoekopdracht geeft alleen het oude rapport (1.257 apps bij de start). Let op: **ook aftvnews.com verbiedt ClaudeBot in robots.txt** (https://www.aftvnews.com/robots.txt), net als amazon.com. Optie (b) van Noor (een nieuw appreport van aftvnews lezen) valt daarmee ook weg. Niet omzeild.
- Geld bij kleine makers: NIET GEVONDEN. Geen omzet of installs van een solo-maker op Fire TV of Vega uit 2024 tot 2026, en geen fonds, bonus of featuring-programma voor Vega (DERDEN: https://developer.amazon.com/apps-and-games/blogs/2025/12/2025-year-in-review, https://developer.amazon.com/apps-and-games/blogs/2026/07/guide-to-building-for-fire-tv-on-vega-os).
- Aantal apparaten: NIET GEVONDEN.
- Nieuw, wel bruikbaar:
  - DERDEN: de nieuwe Fire TV Stick 4K (okt 2026) krijgt gemiddeld 3,1 sterren, vooral door de app-beperking (https://www.giga.de/tech/neuer-fire-tv-stick-4k-faellt-bei-kunden-durch-vor-allem-wegen-der-app-sperre--01M4B75TD3HEKPFDWHRC4HGCKZ, 9 okt 2026). Kopers missen apps: dat is vraag, maar geen bewijs dat ze betalen.
  - DERDEN: de oude Fire TV-winkel heeft 88.451 apps van 21.192 uitgevers (https://data.42matters.com/amazon-fire-tv-app-store-statistics-and-trends).
  - DERDEN: Amazon geeft een openbaar installatiescript voor SDK plus virtueel apparaat (`sdk-installer.vega.labcollab.net/get_vvm.sh`, HTTP 200 zonder inlog, NONINTERACTIVE-stand), draait met `--no-gui` op Ubuntu x86 met KVM. Webview-apps werken niet op het virtuele apparaat. Of de pakketten zonder account binnenkomen is niet getest (https://developer.amazon.com/docs/vega/0.24/run-apps, https://developer.amazon.com/docs/vega/0.24/kvd-issues.html). GOK: op een gewone Linux-runner van GitHub Actions (die heeft /dev/kvm) kan dit draaien; punt 3 is dus waarschijnlijk te halen.

## Nieuw cijfer: 6 (blijft, valt af voor een 8)
De doorslaggevende meting is met openbare data die wij mogen lezen niet te doen: Amazon en aftvnews sluiten ons allebei uit, en niemand anders telt. Punt 1 en 2 blijven daarmee onbekend. Punt 3 is iets sterker dan bij Noor (openbaar script, zonder scherm), punt 4 is goed (Amazon-ontwikkelaarsaccount, IAP). Geen controleur ingezet: er kwam geen nieuw cijfer uit, alleen dat de bronnen dicht zijn; de links staan hierboven.

## Wat het zou veranderen
- Naar 7 of hoger: een telling van native Vega-games en utilities met reviews, via een bron die ons toelaat, of een echt apparaat (Noor optie a, $30 tot $60, alleen als Hans dat wil).
- Goedkope proef voor punt 3 als Hans verder wil: een workflow die het script draait en een voorbeeld-app op het virtuele apparaat start (bouwer, niet ik).
