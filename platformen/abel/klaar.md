# Klaar: volgorde voor de hoofdchat (Abel)

Versie 7 (definitief), 10 nov 2026 07:50 NL. De run van 08:19 schaaft alleen nog bij.

## Stand in één zin
De hele merkkit staat en is door Daan goedgekeurd: avatar v2, Steam-kop v2, Steam-logo v2b, Steam-achtergrond v3, og en social v2b (met een onderregel die vandaag klopt). Overal hetzelfde uniform: de scharnieren van de deur-D zijn in elk beeld gelijk (keuring 5, 10 nov 04:45). Elk plan noemt de definitieve bestanden en is getoetst op de echte pagina van dat platform. Grootste open punt: **dortusgames is vrijwel zeker een beperkt Steam-account**; dan kan Thijs geen groep en dus geen ontwikkelaarspagina maken. €5 op de Steam-portemonnee lost het op (zijn keuze, staat op zijn lijst). Nieuw sinds 07:45: een plan voor de **Superhive-winkel** (Blender-winkel van Click Joints Pro), want Hans vraagt Thijs vanochtend dat account te maken; avatar en banner liggen klaar, alleen de banner wacht nog op Daans ja.

## Controle als Thijs (10 nov 06:30)
Alle zeven plannen van boven naar onder gelezen alsof ik Thijs ben met de zip open. Wat ik rechtzette:
- Elk plan noemt nu het bestand uit `upload/` (de naam die Thijs in de zip ziet), niet meer een bestand in `merk/` met v-nummers. Kop van elk plan zegt in één regel welke map.
- Steam: kop van het plan zei nog "beelden v2"; nu v2b voor het logo. Knopnamen ook in het Engels (View my profile > Edit Profile), want Steam staat misschien in het Engels.
- GitHub: de bio beloofde nog "A tiny dungeon game is on its way to Steam". Mijn logboek van run 4 zei dat dat eruit was, maar het stond er nog. Nu `Small games on the way`, gelijk aan og en social (Daan, kan 5).
- Polar: oude zin over "spikkels" weg; met avatar v2 zijn het inkepingen.
- Obsidian: bovenaan gezet dat eerst "Hide my public profile" uit moet, anders ziet niemand de rest.
- Nagemeten met `cmp` dat de Steam- en GitHub-avatar in `upload/` dezelfde zijn als de goedgekeurde v2.
Bewuste uitzondering: op Steam (profiel en groep) noemen we Hats of the Fallen wel, want daar komt het spel; we zeggen nergens dat het al uit is.

## Alle beelden in één keer
`platformen/abel/upload/` (per account een map, bestandsnamen zeggen waar ze heen gaan, met `LEESMIJ.md`) en hetzelfde als één zip: `platformen/abel/dortus-beelden.zip` (0,8 MB). Thijs hoeft dus niet in `merk/` te zoeken tussen v1, v1b, v2 en v3. Opnieuw maken: `sh merk/bron/maak_upload.sh` (maakt v2b, de goedgekeurde versie). Alle tien bestanden samen bekeken op 10 nov 05:25.

## Zo ziet het eruit (proeven op echte pagina's, alleen in onze browser vervangen)
**Alles op één blad: `merk/proef/overzicht-alle-accounts.png`** (Steam pagina en profiel, Polar, GitHub, Blender, Obsidian, de nieuwe hoofdpagina van dortus.com en de Superhive-winkel onder elkaar; goed om Thijs als eerste te laten zien). Opnieuw maken: `python3 merk/bron/abel_overzicht.py` vanuit `merk/`.
- Steam-ontwikkelaarspagina, definitief (avatar v2, kop v2, logo v2b, achtergrond v3, paginakleur Nacht): `merk/proef/steam-pagina-definitief-1920.png` en `-1280.png` (opnieuw gemaakt 10 nov 05:23 met logo v2b; de spellen in de proef zijn van Klei, de pagina die ik als mal gebruikte). Breed scherm: `steam-pagina-v3-nacht-op-steam-2560.png`.
- Steam-profiel: `merk/proef/steam-profiel-kort-op-steam.png`
- Polar-afrekenpagina: `merk/proef/polar-afrekenen-uitsnede.png` (nu staat daar een grijze letter D)
- Blender Extensions: `merk/proef/blender-avatar-uitsnede.png` (nu een leeg poppetje)
- Obsidian-forum: `merk/proef/obsidian-draad-dark.png` (nu een letter "t")
- GitHub: `merk/proef/github-repo-light.png` en `-dark.png` (sinds 10 nov 06:45 met het vak About gevuld zoals na stap 2: beschrijving, website, topics)
- dortus.com nieuw: `dortus-com/voorbeeld-desktop.png` en `voorbeeld-telefoon.png`
- Superhive-winkel (nieuw 10 nov 07:45): `merk/proef/superhive-winkel-1920.png`, `-1280.png` en `-telefoon.png` (mal: de openbare winkel van Blender Guru; de producten onder de kop zijn van hen)
- Avatar v1 en v2 klein en rond naast elkaar: `merk/proef/avatar-v1-v2-klein-rond.png`
(Proeven van Polar, Blender, Obsidian en GitHub opnieuw gemaakt met avatar v2 op 10 nov 03:40; ook de Steam-profielproef. De achtergrondkleur van die proef komt van het profiel dat ik als mal gebruikte; ons profiel krijgt de gewone Steam-kleur.)

## Volgorde
| # | Account | Plan | Thijs-tijd | Hangt af van | Stand |
|---|---|---|---|---|---|
| 0 | Steam: beperkt account? €5 op portemonnee | `accounts/steam.md` stap 0, lijst-thijs | ±3 min, €5 | keuze Thijs | klaar om te vragen |
| 1 | Steam: profiel dortusgames | `accounts/steam.md` stap 1 | ±5 min | stap 0 (anders alleen voor vrienden zichtbaar) | klaar, akkoord Daan |
| 2 | Steam: groep Dortus | `accounts/steam.md` stap 2 | ±5 min | stap 0 | klaar, akkoord Daan |
| 3 | dortus.com: ja op nieuwe hoofdpagina | `accounts/dortus-com.md` | ±1 min (ja/nee) | niets | pagina in het uniform, deur v2, og met ware onderregel |
| 4 | Polar: logo op de afrekenpagina | `accounts/polar.md` | ±2 min | niets | klaar |
| 5 | GitHub: profiel, repo's, pins, social preview | `accounts/github.md` | ±10 min | niets | klaar, akkoord Daan |
| 6 | Blender ID: avatar | `accounts/blender.md` | ±3 min | niets | klaar |
| 7 | Obsidian-forum: profiel zichtbaar maken, avatar, About me | `accounts/obsidian.md` | ±3 min | niets | klaar; profiel staat nu verborgen |
| 8 | JetBrains: beschrijving (één woord) | `accounts/jetbrains.md` | ±2 min | niets | klaar; er bestaat geen logoveld |
| 9 | Superhive: avatar, banner, naam en zin van de winkel | `accounts/superhive.md` | ±5 min | het verkopersaccount (lijst-thijs, Hans 06:45) | klaar; avatar akkoord, banner (uitsnede van achtergrond v3) wacht op Daans ja |
| later | Steam: ontwikkelaarspagina | `accounts/steam.md` stap 3 | ±15 min | stap 0 en app-ID van Hats of the Fallen | beelden en teksten klaar, paginakleur `#1d1426` niet vergeten |

Samen: ±34 min Thijs-tijd voor 0 tot en met 8 (plus €5 als stap 0 nodig is), plus ±5 min Superhive zodra dat account er is; de ontwikkelaarspagina later ±15 min.

Waarom deze volgorde: Steam eerst (opdracht Thijs), en stap 0 vóór alles omdat stap 1 tot 3 er anders op vastlopen. Polar naar voren: dat is waar iemand betaalt, en daar staat nu een grijze letter. Blender ID omdat de moderatoren nu naar Click Joints kijken. JetBrains als laatste van de bestaande accounts: alleen een tekstje, geen beeld mogelijk. Superhive staat los onderaan omdat het account nog gemaakt moet worden; doe het meteen erna, dan staat de winkel verzorgd voordat Click Joints Pro erin komt.

## Community-bijdrages (elk apart een ja van Thijs)
| Bijdrage | Plek | Thijs-tijd |
|---|---|---|
| `bijdrages/2026-11-10-obsidian-open-with.md` | forum.obsidian.md, vraag zonder antwoord sinds 2 nov | ±2 min lezen en ja/nee |

Niet op Blender Artists, het Godot-forum en r/ObsidianMD: daar zijn door AI geschreven antwoorden verboden (`communities.md`).

## Wat nog ontbreekt
- Mila: social per repo (rollwright, click-joints); tot dan `social-1280x640-v2b-nu.png` (één plaatje voor beide, goedgekeurd).
- ~~Kan-punt Daan (scharnieren gelijk met avatar v2)~~ klaar: Daan zei ja (keuring 5); `upload/`, de zip en alle plannen gebruiken nu v2b.
- ~~Obsidian: plek van het vinkje~~ opgelost: Preferences > Profile, bovenaan (broncode Discourse).
- Steam: paginakleur instellen is door Valve beschreven en aangeraden (docs); alleen de exacte knopnaam heb ik niet gezien.
- Superhive: Daans ja op de banner (gevraagd 10 nov 07:45). Bij nee alleen de avatar zetten en de banner leeg laten; het plan zegt hoe. Ook niet gezien: het instellingenscherm zelf (alleen na inloggen); veldnamen komen uit Superhive's eigen hulppagina's.

## Geplaatst door de hoofdchat (10 nov 11:40, op Thijs' ja)
- GitHub: profielfoto, plus social preview bij rollwright en click-joints.
- Polar: logo.
- Blender ID: avatar.
- Obsidian-forum: profielfoto.
- Steam: profielavatar. De ontwikkelaarspagina en groep kunnen pas als het account niet meer beperkt is ($5 uitgeven).
- Nog open: Superhive-avatar (formulier vraagt eerst een land), Superhive-winkelbanner (pas na goedkeuring als maker), dortus.com (wacht op Thijs' ja).
