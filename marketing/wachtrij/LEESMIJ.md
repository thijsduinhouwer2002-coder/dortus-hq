# Wachtrij van Roep: zo ziet een concept eruit

Eén concept is één bestand in deze map. Maker, Keurder, Chris en de hoofdchat gebruiken allemaal dit formaat. Regels: `marketing/REGELS.md`.

## Bestandsnaam
`JJJJ-MM-DD-<kanaal>-<korte-naam>.md`, met de datum waarop het uit moet. Kanaal is `tiktok`, `yt-lang` of `yt-short`.
Voorbeeld: `2026-11-21-yt-lang-pro-hinge.md`, `2026-11-22-tiktok-ball-joint-fit.md`.
Eén kanaal per bestand. Hetzelfde filmpje op TikTok en YouTube = twee bestanden (de teksten verschillen toch).

## Wie schrijft wat
| Deel | Schrijft | Anderen |
|---|---|---|
| Kop, Titel, Tekst, Eerste reactie, Bronnen | de maker van het concept (Maker of Chris) | niet aanraken |
| `## Keuring`, en `status` op groen, oranje of rood | de Keurder | niet aanraken |
| `status` op ingepland, geplaatst, mislukt, en rood na 24 uur oranje zonder besluit | de Maker | niet aanraken |
| `## Oranje-besluit` | de hoofdchat-ronde | niet aanraken |
| `## Na plaatsen` | de Maker | niet aanraken |

Nooit een concept weghalen, ook niet als het rood is. Een verbeterde versie is een nieuw bestand met `-v2` achter de naam en `vorige:` in de kop.

## Status (de regel `status:` in de kop)
`open` (wacht op de Keurder) → `groen`, `oranje` of `rood` (Keurder) → bij oranje: `groen` of `rood` (hoofdchat) → `ingepland` (Maker zette het in Metricool) → `geplaatst` (adres teruggelezen) of `mislukt` (ERROR of geen adres binnen 2 uur).

## Sjabloon (kopieer vanaf de streep)

---
```
# <korte naam van de post>

- status: vervallen (hoofdchat 27 nov 16:20, Thijs koos "1": marketing weer aan alleen voor nieuw gekeurd werk; oud werk gaat niet meer uit)
- kanaal: tiktok | yt-lang | yt-short
- soort: video | diashow
- product: click-joints-pro
- bestand: <openbare URL van de ...-geluid.mp4, of de dia's (png/jpg) onder elkaar>
- geluid_check: GOED (<dB>), <datum en tijd> | n.v.t. bij diashow
- lengte: <mm:ss>, <liggend 1920x1080 | staand 1080x1920>
- tijd: <JJJJ-MM-DDTUU:MM:00+01:00>   (voorgesteld moment, Europe/Amsterdam)
- doel: <meetadres: https://dortus.com/yt/ (lange YouTube) of dortus.com/tt (TikTok, over te typen)>
- gemaakt_door: Roep-Maker | Chris | <naam>
- vorige: <bestandsnaam als dit een verbeterde versie is, anders leeg>

## Titel
<YouTube: hoogstens 100 tekens, geen < of >. TikTok: korte titel voor tiktokData.title, mag leeg>

## Tekst
<YouTube lang: eerste regel https://dortus.com/yt/ (nooit een Gumroad-link).
TikTok: geen klikbare link, geen "link in bio"; wel het over te typen dortus.com/tt. 5 tot 7 hashtags.
Short (REGELS 21 nov): geen klikbare link, wel het over te typen dortus.com/yt in de beschrijving; niet meer vanzelf oranje.
Altijd: schrijf als Dortus ("we"), nooit in de ik-vorm.>

## Eerste reactie
<YouTube lang: https://dortus.com/yt/ met één zin erbij. TikTok: LEEG laten (persoonlijk account, kan niet). Short: leeg laten.>

## Bronnen
- <waar elke bewering vandaan komt: changelog, winkelpagina, meting, met pad of link>

## Keuring
(leeg tot de Keurder komt)

## Oranje-besluit
(alleen de hoofdchat, alleen bij oranje)

## Na plaatsen
(alleen de Maker)
```
---

## Zo vult de Keurder `## Keuring` in
```
## Keuring
- keurder: Roep-Keurder, <datum en tijd NL>
- 1 bron klopt: ja | nee, <waarom>
- 2 geen AI-zin, geen AI-melding: ja
- 3 geen medische claim: ja
- 4 geen Hats-spelerstekst: ja
- 5 echt beeld zelf bekeken, -geluid.mp4 en geluid_check GOED: ja (<welke beelden bekeken>)
- 6 geen persoonsgegevens: ja
- 7 past bij het kanaal: ja
- 8 niet gelijk aan een post van de laatste 14 dagen: ja
- 9 geen AI-beeld, AI-stem of AI-persoon: ja
- 10 schrijft als Dortus, niet als Thijs: ja
- techniek-check: <per regel uit REGELS.md: goed, of oranje/rood met welke regel>
- uitkomst: groen | oranje | rood
- reden: <één zin>
```
En zet dan bovenin `status:` op dezelfde uitkomst. Commitkop van de Keurder begint met `Roep-Keurder:`; zo kan de Maker met `git log` zien dat groen van de Keurder kwam.

## Zo vult de hoofdchat `## Oranje-besluit` in
```
## Oranje-besluit
- hoofdchat, <datum en tijd NL>: groen | rood, <één zin waarom>
```
En zet `status:` op groen of rood. Geen besluit binnen 24 uur na de keuring: de Maker zet het op rood met reden "24 uur geen besluit".

## Zo vult de Maker `## Na plaatsen` in
```
## Na plaatsen
- ingepland: <datum en tijd NL>, Metricool-nummer <id>, moment <tijd>
- gelezen: <datum en tijd NL>, status PUBLISHED | ERROR
- adres: <https://www.tiktok.com/@dortusstudio/video/... of https://www.youtube.com/watch?v=...>
- handle klopt: ja (@dortusstudio | @Dortusapps)
- cijfers: <weergaven (bron: videopagina of RSS), kijktijd (Metricool), likes, reacties>, GEZIEN <tijd>
```
