# Steam: kant-en-klaar plan (Abel)

Versie 2, 10 nov 2026 01:40 NL. Status: beelden van Mila staan er, teksten aangepast op keuring 1 van Daan (moet-punten 1 en 2, kan-punt 3). Wacht op: Daans akkoord op dit plan en op de twee v1b-beelden (`merk/voor-mila.md`).

## In één zin
Op Steam ziet een speler straks overal hetzelfde Dortus: het profiel dortusgames, de groep en de ontwikkelaarspagina dragen dezelfde deur-D en dezelfde korte tekst, en de winkelpagina van Hats of the Fallen linkt naar die ontwikkelaarspagina, zodat iemand op "Follow" kan klikken.

## Hoe het eruit gaat zien (proef op een echte Steam-pagina)
- Kop van de ontwikkelaarspagina: `merk/proef/steam-kop-v1b-op-steam-1280.png` en `-1024.png`.
- Hele ontwikkelaarspagina met logo en achtergrond: `merk/proef/steam-pagina-v1b-op-steam-1920.png` en `-1280.png`. (De spellen in de proef zijn van Klei, wiens pagina ik als mal gebruikte; bij ons staat daar Hats of the Fallen.)

## Waarom dit telt
Wie de ontwikkelaarspagina volgt, krijgt van Steam bericht als we iets uitbrengen, en Steam toont onze nieuwe spellen eerder aan volgers. DERDEN: https://partner.steamgames.com/doc/store/creator_homepage ("What customers see"). Elke volger is dus een gratis lanceringsbericht. Voor het fest van 14 januari willen we de pagina live hebben zodra Hats of the Fallen "binnenkort" staat.

## Wat er nu staat (GEZIEN 10 nov 00:40)
- steamcommunity.com/id/dortus, /groups/dortus en /groups/dortusgames: "Error", dus vrij.
- store.steampowered.com/developer/dortus: bestaat niet. Vrij.

## Stap 1. Profiel dortusgames (Thijs, ±5 min, kan nu)
Waar: Steam (app of steamcommunity.com), ingelogd als dortusgames > je naam rechtsboven > **Profiel bekijken** > **Profiel bewerken**.

| Veld | Invullen |
|---|---|
| Profielnaam | `Dortus` |
| Echte naam | leeg laten |
| Eigen URL | `dortus` (wordt steamcommunity.com/id/dortus) |
| Land | Netherlands |
| Samenvatting | zie hieronder |
| Avatar (tab Avatar) | `platformen/abel/merk/avatar-184.png` |
| Privacy (tab Privacy) | Mijn profiel: Openbaar. Spellendetails: Privé. Opmerkingen: Alleen vrienden (geen spam onder ons profiel). |

Samenvatting om te plakken:
```
Dortus makes small games and focused tools.
Our first game, Hats of the Fallen, is a tiny dungeon on your taskbar: heroes come for the slime's treasure, and he keeps their hats.
Made by Thijs in the Netherlands. Questions or bugs: thijs@dortus.com
```

Niet doen: achtergrond, kader of badges kopen in de Puntenwinkel. Een kaal maar verzorgd profiel straalt meer vertrouwen uit dan een bont gekocht thema, en het kost geld.

## Stap 2. Communitygroep "Dortus" (Thijs, ±5 min)
De ontwikkelaarspagina wordt op een communitygroep gebouwd; de naam van de groep komt bovenaan de pagina. DERDEN: https://partner.steamgames.com/doc/store/creator_homepage

**Eerst controleren:** is dortusgames een "beperkt account"? Steam beperkt accounts die minder dan $5 in de Steam-winkel uitgaven; die kunnen geen groep maken. Of de Steam Direct-fee meetelt, weet ik niet (GOK: niet, want die betaal je in Steamworks, niet in de winkel). Proef: lukt stap 2 niet, dan staat er een melding over een beperkt account. Oplossing is $5 op de Steam-portemonnee of een spel kopen: dat is geld, dus Thijs beslist.

Waar: steamcommunity.com > je profiel > **Groepen** > **Groep aanmaken**.

| Veld | Invullen |
|---|---|
| Groepsnaam | `Dortus` |
| Afkorting | `DORTUS` |
| Groeps-URL | `dortus` |
| Openbaar | Ja, iedereen mag lid worden |
| Avatar | `avatar-184.png` (zelfde als het profiel) |
| Kop (headline) | `Small games and focused tools from the Netherlands` |
| Samenvatting | zelfde tekst als het profiel |
| Website | `https://dortus.com`, pas als de hoofdpagina niet meer over Confluence gaat (zie `dortus-com.md`). Tot dan leeg. |

## Stap 3. Ontwikkelaarspagina (Thijs, ±15 min, kan pas als Hats of the Fallen een app-ID heeft in Steamworks)
1. Steamworks > app van Hats of the Fallen > Winkelpagina bewerken > tab **Basisinformatie**: ontwikkelaar `Dortus`, uitgever `Dortus`. Opslaan, dan op **link** naast elk veld klikken en de groep Dortus kiezen.
2. Steamworks > Apps & pakketten > **Creator Homepage Custom URL Setup**: `dortus`. Dan werkt store.steampowered.com/developer/dortus. Valve ziet dit als handelsnaam; Dortus is van ons (dortus.com).
3. Ontwikkelaarspagina > tab **admin**:
   - Logo links in de kop (184 x 184): `merk/avatar-184.png`.
   - Achtergrond van de kop (1500 x 220): `merk/steam-kop-1500x220-v1b.png` (niet v1: daarin valt de deur op kleinere schermen weg, zie proef).
4. Admin > **Creator Home v2** > Create New. Houd de standaardsecties; Valve raadt aan "On your wishlist" en "Recommended" te houden. Zet als paginalogo `merk/steam-logo-1200x460.png` en als achtergrond `merk/steam-achtergrond-1920-v1b.png` (niet v1: daarin staat een tweede grote D naast het logo). Voeg bovenaan één **tekstblok** toe (tekst hieronder).
5. Kijk in de voorvertoning of de lichtbundel van de achtergrond onder de D van het logo begint. Zo niet: zeg het, dan schuift Mila hem een paar pixels.
6. Tab **publish** > publiceren. Terug naar admin > Creator Home v2 > bij "Inactive" op **Set as Active** (ster).

Tekstblok "About Dortus" om te plakken:
```
Hi, we're Dortus.

We make small games that keep you company while you work, and tools that fill a real gap.
Our first game, Hats of the Fallen, is a tiny dungeon on your taskbar: heroes come for the slime's treasure, and he keeps their hats.

Follow us and Steam will let you know when it comes out.
Questions, bugs or ideas: thijs@dortus.com
```
Waarom zo: kort, één vaste zin voor het spel (keuring Daan), en we beloven niets wat Steam bepaalt.

## Stap 4. Rond de winkelpagina (afstemming met Mila en Sanne)
- De winkelpagina zelf is van Mila en Sanne. Ik zorg dat ontwikkelaar en uitgever "Dortus" heten en gelinkt zijn (stap 3.1), zodat "Follow" onder de winkelpagina naar onze pagina gaat.
- Website-link op de winkelpagina: `https://dortus.com/hats-of-the-fallen/` zodra die pagina er is. Tot dan geen website-link: de huidige hoofdpagina gaat over Confluence en wekt wantrouwen.
- **Eerlijkheid AI:** in de Content Survey (verplicht bij het indienen) vraagt Valve of er inhoud in het spel zit die met hulp van AI-tools gemaakt is en die spelers zien. Dat moet je beschrijven; Valve toont het op de winkelpagina. DERDEN: https://partner.steamgames.com/doc/gettingstarted/contentsurvey. Voorstel (Thijs keurt): "The pixel art, text and code were made with the help of AI tools (Anthropic's Claude) and reviewed by the developer. No AI runs while you play." Alleen invullen wat waar is. Staat ter info op `organisatie/lijst-thijs.md`.

## Beelden (allemaal van Mila, v1b is mijn verschuiving met haar eigen code)
| Waar | Bestand | Maat |
|---|---|---|
| Profiel, groep, logo in de kop | `merk/avatar-184.png` | 184 x 184 |
| Kop ontwikkelaarspagina | `merk/steam-kop-1500x220-v1b.png` | 1500 x 220 |
| Paginalogo (v2) | `merk/steam-logo-1200x460.png` | 1200 x 460, doorzichtig |
| Achtergrond (v2) | `merk/steam-achtergrond-1920-v1b.png` | 1920 x 1200 |

## Klaar als
Daan zette `Akkoord: ja` onder dit plan (of in `ontwerp/keuring-abel.md`), en Mila nam v1b over of verving het door iets beters.

## Keuring Daan
(Daan: ja of nee met moet-punten.)
