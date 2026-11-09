# Steam: kant-en-klaar plan (Abel)

Versie 1, 10 nov 2026 00:45 NL. Status: wacht op de beelden van Mila (uniform) en het akkoord van Daan. Teksten zijn klaar.

## In één zin
Op Steam ziet een speler straks overal hetzelfde Dortus: het profiel dortusgames, de groep en de ontwikkelaarspagina dragen hetzelfde beeldmerk en dezelfde korte tekst, en de winkelpagina van Het Hol (van Mila) linkt naar die ontwikkelaarspagina, zodat iemand op "Volgen" kan klikken.

## Waarom dit telt
Wie de ontwikkelaarspagina volgt, krijgt van Steam een mail als we uitbrengen, en Steam mengt onze nieuwe spellen in zijn voorpagina en tagpagina's. DERDEN: https://partner.steamgames.com/doc/store/creator_homepage ("What customers see"). Elke volger is dus een gratis lanceringsbericht. Voor het fest van 14 januari willen we de pagina live hebben zodra Het Hol "binnenkort" staat.

## Wat er nu staat (GEZIEN 10 nov 00:40)
- steamcommunity.com/id/dortusgames, /id/dortus, /groups/dortus en /groups/dortusgames: geven allemaal "Error", dus die namen zijn vrij (of het profiel heeft geen eigen URL).
- store.steampowered.com/developer/dortus: bestaat niet (toont de zoekpagina). Vrij.

## Stap 1. Profiel dortusgames (Thijs, ±5 min, nu al te doen)
Waar: Steam (app of steamcommunity.com), ingelogd als dortusgames > profiel > **Profiel bewerken**.

| Veld | Invullen |
|---|---|
| Profielnaam | `Dortus` |
| Echte naam | leeg laten |
| Eigen URL | `dortus` (wordt steamcommunity.com/id/dortus) |
| Land | Netherlands |
| Samenvatting | zie hieronder |
| Avatar | `platformen/abel/merk/avatar-184.png` (komt van Mila) |
| Privacy (tab Privacy) | Mijn profiel: Openbaar. Spellendetails mogen privé. Opmerkingen: Alleen vrienden (geen spam onder ons profiel). |

Samenvatting om te plakken:
```
Dortus makes small games and focused tools.
Our first game, Hats of the Fallen, is a little lair that lives at the bottom of your desktop.
Made by Thijs in the Netherlands. Questions or bugs: thijs@dortus.com
```
(De naam van het spel volgt het besluit van Mila en Daan vóór 11 nov. Wordt het Hat Hoard, dan alleen die naam wisselen.)

Niet doen: profielachtergrond of kader kopen in de Puntenwinkel. Kost geld en een kaal maar verzorgd profiel straalt meer vertrouwen uit dan een bont gekocht thema.

## Stap 2. Communitygroep "Dortus" (Thijs, ±5 min)
De ontwikkelaarspagina wordt op een communitygroep gebouwd, en de naam van de groep komt bovenaan de pagina. DERDEN: https://partner.steamgames.com/doc/store/creator_homepage

**Eerst controleren:** is dortusgames een "beperkt account"? Steam beperkt accounts die minder dan $5 in de Steam-winkel uitgaven; die kunnen geen groep maken. Of de Steam Direct-fee meetelt, weet ik niet (GOK: waarschijnlijk niet, want die betaal je in Steamworks, niet in de winkel). Proef: lukt stap 2 niet, dan staat er een melding over een beperkt account. Oplossing is $5 op de Steam-portemonnee zetten of een spel kopen: dat is geld, dus Thijs beslist.

Waar: steamcommunity.com > je profiel > Groepen > **Groep aanmaken**.

| Veld | Invullen |
|---|---|
| Groepsnaam | `Dortus` |
| Afkorting | `DORTUS` |
| Groeps-URL | `dortus` (wordt steamcommunity.com/groups/dortus; deze URL gebruikt de ontwikkelaarspagina niet, maar netjes is netjes) |
| Openbaar | Ja, iedereen mag lid worden |
| Avatar | `avatar-184.png` (zelfde als het profiel) |
| Kop (headline) | `Small games and focused tools from the Netherlands` |
| Samenvatting | zelfde tekst als het profiel |
| Website | `https://dortus.com` (pas als de hoofdpagina niet meer over Confluence gaat, zie plan dortus.com) |

## Stap 3. Ontwikkelaarspagina (Thijs, ±15 min, kan pas als Het Hol een app-ID heeft in Steamworks)
1. Steamworks > app van Het Hol > Winkelpagina bewerken > tab **Basisinformatie**: ontwikkelaar `Dortus`, uitgever `Dortus`. Opslaan, dan op **link** naast elk veld klikken en de groep Dortus kiezen.
2. Steamworks > menu Apps & pakketten > **Creator Homepage Custom URL Setup**: `dortus`. Dan werkt store.steampowered.com/developer/dortus. Let op: Valve ziet dit als "Company Mark", het moet van ons zijn. Dortus is van ons (dortus.com).
3. Naar de ontwikkelaarspagina > tab **admin**:
   - Logo (links in de kop, 184 x 184): `avatar-184.png`.
   - Achtergrond van de kop (1500 x 220, donker, rustig, randen vervagen vanzelf): `steam-kop-1500x220.png`.
4. Admin > **Creator Home v2** > Create New. Houd de standaardsecties (Populair, Op je verlanglijst, Aanbevolen, Binnenkort, Alles bekijken); Valve raadt aan "Op je verlanglijst" en "Aanbevolen" te houden. Voeg bovenaan één **tekstblok** toe (tekst hieronder) en zet de paginalogo `steam-logo-1200x460.png` en de achtergrond `steam-achtergrond-1920.png`.
5. Tab **publish** > publiceren. Terug naar admin > Creator Home v2 > bij "Inactive" op **Set as Active** (ster).

Tekstblok "About Dortus" om te plakken:
```
Hi, we're Dortus.

We make small games that keep you company while you work, and tools that fill a real gap.
Our first game, Hats of the Fallen, lives in a strip at the bottom of your desktop: a slime in a cave, heroes who come for his treasure, and a growing tower of the hats they leave behind.

Follow us to get one email when it comes out. No spam, nothing else.
Questions, bugs or ideas: thijs@dortus.com
```
Waarom zo: kort, zegt meteen wat je krijgt als je volgt (één mail), en noemt alleen wat echt in het spel zit (hoedentoren, schat, helden: GEZIEN in `platformen/steam/features.md` en de builds van Mila). De naam pas definitief na het besluit van 11 nov.

## Stap 4. Rond de winkelpagina (afstemming met Mila)
- De winkelpagina zelf is van Mila. Ik zorg dat ontwikkelaar en uitgever "Dortus" heten en gelinkt zijn (stap 3.1), zodat de knop "Volgen" onder de winkelpagina naar onze pagina gaat.
- Website-link op de winkelpagina: `https://dortus.com/<spelnaam>/` zodra die pagina er is (map voor het spel op dortus.com, mag volgens de regels). Tot dan geen website-link: een link naar de huidige Confluence-hoofdpagina wekt wantrouwen.
- **Eerlijkheid AI:** in de Content Survey (verplicht bij het indienen) vraagt Valve of er inhoud in het spel zit die "met hulp van AI-tools" is gemaakt en door spelers wordt gezien: kunst, geluid, tekst, vertaling. Dat heet "Pre-Generated" en moet je in detail beschrijven; Valve toont het op de winkelpagina. DERDEN: https://partner.steamgames.com/doc/gettingstarted/contentsurvey. Onze pixelkunst, teksten en het spel zelf zijn door Claudes gemaakt. Dat moet eerlijk ingevuld worden; verzwijgen breekt de belofte aan Valve en riskeert het account dat Thijs net betaalde. Voorstel voor de tekst in de survey (Thijs keurt): "The pixel art, text and code were made with the help of AI tools (Anthropic's Claude) and reviewed by the developer. No AI runs while you play." (Alleen invullen wat waar is: past het niet meer bij hoe het spel gemaakt is, dan aanpassen.) Staat ook op `organisatie/lijst-thijs.md`.

## Beelden die hier nodig zijn (van Mila)
`avatar-184.png`, `steam-kop-1500x220.png`, `steam-logo-1200x460.png`, `steam-achtergrond-1920.png`. Maten: `platformen/abel/merk/maten.md`.

## Klaar als
Mila's beelden staan in `merk/`, Daan zette `Akkoord: ja` onder dit plan, en de naam van het spel is besloten (11 nov).
