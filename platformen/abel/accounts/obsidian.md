# Obsidian: kant-en-klaar plan (Abel)

Versie 3, 10 nov 2026 06:30 NL. Status: klaar. Avatar v2 van Mila, akkoord Daan (keuring 4), proef op de echte forumdraad bekeken. **Bestand: `platformen/abel/upload/5-obsidian/forum-profielfoto-512.png`.** Doe eerst het vinkje "Hide my public profile" uit (zie onder), anders ziet niemand de rest.

## Wat er nu staat (GEZIEN 10 nov 00:55)
- Rollwright in de pluginlijst: auteur **Dortus**, authorUrl https://dortus.com (manifest.json 0.3.5). Goed, maar die link landt op de Confluence-hoofdpagina (zie `dortus-com.md`).
- In de pluginlijst linkt de plugin naar de GitHub-repo; daar zie je het GitHub-account met de standaardavatar (zie `github.md`).
- Forum: gebruiker **Thijs.Dortus**, avatar is de automatische letter "t" (letter_avatar). Eén draad: "Rollwright: roll dice and random tables in your notes..." (8 nov, 1 bericht). Naam, bio en website niet openbaar te lezen.

## Stap 1. Forumprofiel (Thijs, ±3 min)
Inloggen op https://forum.obsidian.md > avatar rechtsboven > **Preferences**.
- Account > **Profile picture** > uploaden: `upload/5-obsidian/forum-profielfoto-512.png` (Discourse knipt hem rond; Mila houdt de vorm binnen de middelste 70%).
- Account > Name: `Thijs`.
- Profile > **About me**:
```
Thijs from the Netherlands. I make Rollwright (dice in your notes) under the name Dortus. The code is written by AI agents; I direct and test the work. Happy to help with dice, tables and TTRPG setups in Obsidian.
```
- Profile > Website: `https://dortus.com/rollwright/` (niet de hoofdpagina zolang die over Confluence gaat).

Waarom de AI-zin hier wel: de Obsidian-community is er gevoelig voor (r/ObsidianMD bant AI-projecten, 9 nov), en de gedragscode van Obsidian verbiedt misleiding. Wie het vooraf in het profiel leest, kan niet later roepen dat het verzwegen is. Thijs mag de zin schrappen, maar dan ook nergens iets anders beweren.

- Vondst (GEZIEN, forum.obsidian.md/u/Thijs.Dortus.json, 10 nov 02:30): het profiel staat op **verborgen** (`profile_hidden: true`). Dan ziet niemand About me of website, en dan heeft de stap hierboven geen zin. In Preferences > **Profile**, bovenaan, het vinkje **"Hide my public profile"** uitzetten en onderaan op Save changes. (Plek nagezocht in de openbare broncode van Discourse, `frontend/discourse/app/templates/preferences/profile.gjs`, en de Engelse tekst in `config/locales/client.en.yml`: GEZIEN 10 nov 03:40. Obsidian kan een eigen vertaling hebben, maar het vinkje staat op de pagina Profile.)

Waarom de About me nu dezelfde woorden gebruikt als de draad: in de draad van 8 nov schreef Thijs al "The code is written by AI agents that my small studio, Dortus, runs. I direct and test the work". Het profiel zegt nu precies hetzelfde, korter. Twee verschillende versies ("built with the help of AI tools" tegenover "written by AI agents") zouden lezen als afzwakken.

Zo ziet het eruit: `merk/proef/obsidian-draad-dark.png` en `obsidian-draad-light.png` (de echte draad, alleen in mijn browser de letter "t" vervangen). De D leest op 45 px rond, op licht en donker.

## Stap 2. Wat het plan voor GitHub en dortus.com hier oplost
Avatar en bio op GitHub (`github.md`) en een nieuwe hoofdpagina (`dortus-com.md`) maken de pluginlijst vanzelf verzorgder. Hier hoeft verder niets.

## Klaar als
Avatar, naam en "About me" staan, Daan zette `Akkoord: ja`.
