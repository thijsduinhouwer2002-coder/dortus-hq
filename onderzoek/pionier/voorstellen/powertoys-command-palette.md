# PowerToys Command Palette (extensies en Extension Gallery)

Noor, pionier, 8 nov 2026. Meting zelf (Gallery-feed en Store-API) plus één onderzoeker (agent) voor groei, Raycast en vraag; kerncijfers van de agent zelf nagekeken (sterren, downloads, Raycast-API).

## Wat het is
Command Palette (CmdPal) is de snelstarter van Microsoft PowerToys, de opvolger van PowerToys Run (Alt+Spatie op Windows). Makers bouwen extensies in .NET en verspreiden die via de Microsoft Store of WinGet. Sinds PowerToys 0.100 (juni 2026) zit er een Extension Gallery in de instellingen: een gecureerde lijst waaruit je met één klik installeert (GEZIEN, https://devblogs.microsoft.com/commandline/powertoys-0-100-is-here-new-shortcut-guide-command-palette-improvements-and-much-more/ en https://learn.microsoft.com/en-us/windows/powertoys/command-palette/extension-gallery). Aanmelden gaat met een pull request in github.com/microsoft/CmdPal-Extensions.

## 1. Groeit het platform hard? Nee, groot maar vlakker
- PowerToys: 140.714 sterren op GitHub (GEZIEN, https://api.ossinsight.io/gh/repo/microsoft/PowerToys), 144 miljoen downloads van GitHub-releases in totaal (GEZIEN, https://img.shields.io/github/downloads/microsoft/PowerToys/total.json). Store en WinGet tellen daar niet in mee.
- Groei van de sterren (ossinsight, telt iets lager): nov 2024 117.795, nov 2025 129.771, nov 2026 135.584. Dat is +12.000 en daarna +5.800 per jaar: de groei is ongeveer gehalveerd (DERDEN, https://api.ossinsight.io/q/analyze-stars-history?repoId=184456251).
- Microsoft noemt geen aantal gebruikers. De Store-pagina van PowerToys heeft 3.608 beoordelingen in de VS (GEZIEN, Store-API, product XP89DCGQ3K6VLD).
- De mogelijke motor: de nieuwe Run-dialoog (Win+R) in Windows 11 draait op dezelfde code als CmdPal, nu alleen opt-in in het Insider-kanaal Experimental; Microsoft schrijft dat CmdPal ooit "part of the OS itself" kan worden (DERDEN, https://devblogs.microsoft.com/commandline/the-new-run-dialog-faster-cleaner-and-more-capable/, 1 mei 2026). Extensies in Windows zelf zijn niet aangekondigd, ook niet op Build 2026 (DERDEN, https://thewincentral.com/developer-optimized-windows-11-experience-build-2026/). Dat zou het publiek wel enorm maken, maar het is een GOK.

## 2. Is de winkel jong? Ja
- Gallery-feed van 3 nov 2026: 97 extensies van 61 makers (GEZIEN, https://raw.githubusercontent.com/microsoft/CmdPal-Extensions/main/extensions.json).
- Toegevoegd per maand: april 49 (startvulling), daarna 7, 7, 11, 6, 9, 5 en 3 (tot 3 nov). Dus ±7 per maand, en niet stijgend (GEZIEN).
- Bronnen: 60 alleen Store, 25 Store en WinGet, 12 alleen WinGet (GEZIEN).
- Categorieën: hulpmiddelen 76, productiviteit 67, ontwikkelaars 29, de rest bijna leeg (GEZIEN; een extensie kan in meer categorieën staan).
- Buiten de Gallery vond de onderzoeker 28 CmdPal-extensies in de Store via zoeken, allemaal gratis (DERDEN via agent, https://apps.microsoft.com/api/products/search?query=command%20palette). Het aantal in WinGet kon niet geteld worden.

## 3. Kan er betaald worden? Technisch ja, in de praktijk niemand
- Extensies in de Store zijn gewone MSIX-apps; de Store kent betaalde apps en aankopen in de app. Registreren als individuele maker is gratis (GEZIEN, https://learn.microsoft.com/en-us/windows/powertoys/command-palette/publish-extension-store).
- Maar van de 85 Store-extensies in de Gallery kost er 0 iets (GEZIEN, Store-API per product). Geen betaalde CmdPal-extensie gevonden op Gumroad of eigen sites (DERDEN via agent).
- Microsoft zelf zegt niets over geld voor CmdPal-makers. De Gallery is gratis en gecureerd; of een betaalde extensie erin mag, staat nergens (GOK: niet verboden, niet aangemoedigd).
- Raycast, de grote concurrent, staat geen betaalde extensies toe (MIT-licentie verplicht), dus betalen zou hier juist een verschil zijn (GEZIEN door de agent, https://developers.raycast.com/basics/prepare-an-extension-for-store).

## 4. Is er vraag? Zwak bewijs
- Beoordelingen in de Store (VS) voor alle 85 Gallery-extensies samen: 24. De beste: Weather 7, Media Controls 6, Godot Engine 6, EverythingCmdPal 5 (GEZIEN, script `data/cmdpal-meet.py`, uitkomst `data/cmdpal-2026-11-08.json`). Installs zelf zijn nergens zichtbaar.
- Ter vergelijking: Raycast-extensies die op Windows werken, 1.000 van 3.538, samen 9,3 miljoen downloads (DERDEN via agent, telling van https://www.raycast.com/api/v1/store_listings; macOS-downloads tellen daar ook in mee).
- Verzoeken op GitHub die nog niemand bouwde: Remote Desktop (https://github.com/microsoft/PowerToys/issues/38305), OneNote zoeken (/issues/39444), timer (/issues/38547), rekenen met datums (/issues/38749), Copilot vragen (/issues/40930), spelling (/issues/45433). Outlook, agenda, Jira en Notion staan niet in de Gallery (DERDEN, titels via zoeken; stemmen konden we niet lezen omdat GitHub voor Microsoft-repo's hier dicht is).

## 5. Is de eerste plek te pakken? Ja, maar de prijs is klein
- Categorie met kans: Microsoft 365 voor werkende mensen (Outlook-mail en agenda, OneNote, To Do, Teams), want zakelijke Windows-gebruikers zijn het publiek van PowerToys en Microsoft bouwde zelf alleen GitHub en Azure DevOps (GEZIEN in de feed). Er is nu geen enkele M365-extensie behalve Teams Meeting Control en Todo.
- Huidige beste: niemand. Wel bouwt de maker van Change Case en negen andere (Jiri Polasek, tevens bouwer van de Gallery in PowerToys) snel en goed; die kan elk gat in een paar weken vullen.
- Waarom wij beter kunnen: een M365-koppeling vraagt inloggen met Microsoft Graph en nette formulieren, meer werk dan de typische hobby-extensie.

## Risico en waaraan je het ziet
- Grootste risico: het publiek blijft klein. 24 beoordelingen voor alle extensies samen na zeven maanden wijst op weinig installs. Raycast is sinds 25 aug 2026 algemeen beschikbaar op Windows (DERDEN, https://www.raycast.com/changelog/windows) en heeft al 1.000 extensies; zakelijke snelstart-gebruikers kunnen daarheen gaan.
- Teken dat het stokt: Gallery blijft onder 10 nieuwe extensies per maand en beoordelingen van de top blijven onder de 20.
- Teken dat het doorbreekt: Microsoft zet CmdPal of de extensies in Windows zelf (niet alleen de Run-dialoog), of de Gallery krijgt installtellers en de top haalt duizenden.

## Eerste productidee (als het ooit ja wordt)
"Outlook in je palet": mail zoeken, agenda van vandaag, snel een afspraak of taak aanmaken, OneNote doorzoeken, met Microsoft Graph. Gratis basis, betaald voor meerdere accounts en gedeelde agenda's via de Store.

## Cijfer en advies
**Cijfer 4. Nee voor nu, wachtlijst.**
Waarom: de winkel is jong en de categorieën zijn leeg, en betalen kan technisch via de Store, maar het platform groeit niet hard (sterrengroei gehalveerd), er is geen enkel teken van geld en de vraag is nauwelijks meetbaar en lijkt klein. Vraag 1 weegt het zwaarst en daar zakt het. Alleen als Microsoft CmdPal-extensies in Windows zelf opneemt, wordt dit een echte pionierskans; dan opnieuw wegen.

Herhaalmeting: `python3 data/cmdpal-meet.py data/cmdpal-<datum>.json` rond 8 feb 2027, en bij elk nieuws over CmdPal in Windows 11.
Geen controleur ingezet: het advies is geen ja, en de kerncijfers (feed, Store-API, sterren, downloads) heb ik zelf gezien.
