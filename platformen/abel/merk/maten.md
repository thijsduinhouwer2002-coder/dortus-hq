# Maten en eisen per account (voor Mila)

Door Abel, 10 nov 2026 00:30 NL. Mila maakt de beelden, Abel zet ze per account klaar. Elke maat heeft een label: DERDEN (uit de docs van het platform, met link), GEZIEN (zelf gemeten op de live pagina) of GOK (uit het hoofd, nog niet bevestigd).

## Kort: wat Mila moet maken

Eén **beeldmerk** (vierkant, werkt op 32 px en 16 px) en één **sfeerbeeld** (breed, rustig, donker) in de stijl van het uniform. Daaruit snijden we alles:

| Bestand (zet in `platformen/abel/merk/`) | Maat | Voor |
|---|---|---|
| `avatar-1024.png` | 1024 x 1024, vierkant, geen transparantie aan de rand nodig | bron voor alle avatars |
| `avatar-512.png` | 512 x 512 | GitHub, Polar, Blender ID, forum.obsidian.md, JetBrains |
| `avatar-184.png` | 184 x 184 | Steam (profiel dortusgames, groep, ontwikkelaarspagina) |
| `avatar-32.png` en `avatar-16.png` | 32 en 16 | toets: leest het nog? (Steam toont avatars op 32 en 64 px in lijsten) |
| `steam-kop-1500x220.png` | 1500 x 220 | achtergrond kop ontwikkelaarspagina Steam |
| `steam-achtergrond-1920.png` | 1920 breed (hoogte vrij, ±1080 tot 2000) | achtergrond ontwikkelaarspagina (v2-editor) |
| `steam-logo-1200x460.png` | 1200 x 460, transparant | logo bovenaan ontwikkelaarspagina (v2-editor), mag ook 940 x 460 |
| `social-1280x640.png` | 1280 x 640 | GitHub social preview per repo (Dortus-rand plus productbeeld) |
| `og-1200x630.png` | 1200 x 630 | dortus.com deelplaatje (vervangt het oude Confluence-plaatje) |
| `merkteken.svg` | vector | favicon dortus.com, alles wat scherp moet blijven |

## Per platform, met bron

### Steam (eerst)
- **Ontwikkelaarspagina (Creator Homepage), kop:** links een vierkant logo **184 x 184**, "het ene beeld dat je bedrijf door heel Steam vertegenwoordigt, naast aanbevolen spellen". Erachter een achtergrond **1500 x 220**; de linker- en rechterrand vervagen vanzelf op brede schermen. Valve: "liefst donker en zonder harde contrasten, zeker achter de tekst". De naam naast het logo is de naam van de communitygroep. DERDEN: https://partner.steamgames.com/doc/store/creator_homepage/example
- **Ontwikkelaarspagina v2-editor (secties):** eigen achtergrond voor de hele pagina of per sectie; logo bovenaan **1200 x 460 (of 940 x 460), transparante achtergrond**, beweging alleen heel subtiel. Geen prijzen of valuta in beeld, niet wegsturen van Steam. DERDEN: https://partner.steamgames.com/doc/marketing/event_tools/sales/tools en https://partner.steamgames.com/doc/marketing/event_tools/creatorhome/tools
- **Communitygroep "Dortus"** (de pagina is op een groep gebouwd): groepsavatar = hetzelfde vierkante logo. DERDEN: https://partner.steamgames.com/doc/store/creator_homepage ("You'll probably also want to upload an avatar image to the group for your company logo"). Maat: 184 x 184 (GOK, de standaard Steam-avatarmaat).
- **Profiel dortusgames:** avatar 184 x 184 (GOK, standaard). Profielachtergronden en kaders koop je in de Puntenwinkel: niet nodig, niet doen.
- **Eventuele aankondigingen (nieuws op de pagina):** omslag **800 x 450**, kop **1920 x 622**. DERDEN: sales/tools hierboven. Pas nodig bij de eerste aankondiging.
- Winkelpagina Het Hol: van Mila zelf (`ontwerp/steam/winkelpagina/plan.md`).

### JetBrains Marketplace
- Verkopersprofiel "Dortus" (vendor/dortus): heeft een logo-veld. Maat niet in openbare docs te lezen (de docs-pagina laadt niet met curl). Lever **512 x 512 PNG**, vierkant; dat schaalt overal goed. GOK.
- Pluginicoon Bison & Flex blijft van Daan (`pluginIcon.svg`, 40 x 40). Het uniform zit in de verkopersavatar, niet in het pluginicoon.

### Blender (extensions.blender.org)
- Het profiel is je Blender ID. Avatar: vierkant, **512 x 512** is ruim genoeg. GOK.
- Per extensie (Click Joints, van Daan): icoon **256 x 256 PNG**; uitgelicht beeld **minstens 1920 x 1080, 16:9** (png, jpg of webp). DERDEN: broncode van de site, https://projects.blender.org/infrastructure/extensions-website/raw/branch/main/extensions/models.py en constants/base.py.

### Obsidian
- Geen eigen profielpagina: de plugin hangt aan het GitHub-account. Het forum (forum.obsidian.md, Discourse) heeft een avatar: vierkant, **512 x 512**. GOK.

### GitHub (thijsduinhouwer2002-coder)
- Profielfoto: vierkant, rond **500 x 500**, PNG/JPG/GIF, onder 1 MB. GOK (uit het hoofd; de docs-pagina laadt niet met curl). We leveren 512 x 512.
- Social preview per repo: **1280 x 640** voor de beste weergave, minimaal 640 x 320, onder 1 MB. DERDEN: https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/customizing-your-repositorys-social-media-preview
- Nu: de standaard grijs-gele blokjes (GEZIEN, avatar 295318200). Geen naam, geen bio.

### Polar (organisatie dortus)
- Organisatie-avatar: vierkant, **512 x 512**. GOK. Verschijnt op de afrekenpagina, dus het moet vertrouwen wekken naast het betaalformulier.

### dortus.com
- Favicon: SVG (nu `assets/dortus-mark.svg`, een paarse D). Deelplaatje **1200 x 630** (GEZIEN: het huidige `og-home.png` is 1200 x 630 en toont nog de Confluence-editors).

## Eisen voor het beeldmerk (mijn toets, naast Mila's vier vragen)
1. Leest op **32 px** (Steam-lijst, GitHub-commits) en op **16 px** (favicon). Weinig details, één vorm.
2. Werkt in een **cirkel** (GitHub en Discourse knippen rond) en in een vierkant (Steam). Belangrijkste vorm binnen de middelste 70%.
3. Werkt op **licht en donker** (Steam is donker, GitHub en JetBrains vaak licht).
4. Past bij **alles wat we maken**: een spel (Het Hol), plugins voor programmeurs, Blender, Obsidian. Dus het merk Dortus is de maker, geen spelfiguur. Gloop hoort bij Het Hol, niet in het Dortus-logo (anders lijkt Bison & Flex een spel).
5. Eén vaste set kleuren en één letter, overal gelijk.
