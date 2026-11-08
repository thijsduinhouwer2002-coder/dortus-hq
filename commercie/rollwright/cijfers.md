# Rollwright: cijfers

Door Chris. Meetmomenten: dag 0 (nu), dag 7 en dag 30 na de aanmelding in Community plugins, daarna elke week. Nieuwste meting bovenaan.

Hoe meten (curl, geen inlog):
- Downloads: `https://raw.githubusercontent.com/obsidianmd/obsidian-releases/master/community-plugin-stats.json`, sleutel `rollwright`.
- Release-downloads: `https://api.github.com/repos/thijsduinhouwer2002-coder/rollwright/releases`.
- Sterren en issues: `https://api.github.com/repos/thijsduinhouwer2002-coder/rollwright`.
- Verkopen: Polar (alleen Thijs kan inloggen; nog geen weg voor de ploeg).

## Meting 8 nov 2026, ±08:00 UTC (0.3.0 uit, nog niet aangemeld)
| Wat | Waarde | Label |
|---|---|---|
| Rollwright in community-plugin-stats.json | nog niet aanwezig | GEZIEN |
| Aantal plugins in community-plugins.json | 10.095 (01:45: 10.083) | GEZIEN |
| Release 0.3.0 (8 nov 06:23 UTC) | main.js 1, manifest.json 2, styles.css 1 download | GEZIEN |
| Sterren, open issues op GitHub | 0, 0 | GEZIEN |
| Verkopen skins | 0 (niet te koop via de lijst) | GOK |

Concurrenten: alle downloadtellers in community-plugin-stats.json zijn gelijk aan de meting van 01:45 (Dice Roller 289.111, Dice Rolls 366, Dice Tray 100, GEZIEN). Het bestand is dus in die ±6 uur niet bijgewerkt; geen nieuwe groeicijfers.

Nieuw in de lijst sinds de vorige meting, wel dobbel-gerelateerd maar smal (GEZIEN, community-plugins.json en stats): `vtmvfive-dice-roller` (alleen Vampire the Masquerade 5, 170 downloads), `power-roll-detector` (alleen Draw Steel, 92), `roll-initiative` (initiatieftracker, 42). Geen directe concurrent. Hun beschrijving eindigt op "This plugin has not been manually reviewed by Obsidian staff." Die zin staat bij 7.511 van de 10.095 plugins, ook bij Dice Rolls en Dice Tray, niet bij Dice Roller (GEZIEN, community-plugins.json 8 nov, nagemeten door de controleur). Rollwright krijgt hem waarschijnlijk ook (GOK); niets aan te doen.

## Meting 8 nov 2026, 01:45 UTC (nog niet aangemeld, wacht op 0.3.0)
| Wat | Waarde | Label |
|---|---|---|
| Rollwright in community-plugin-stats.json | nog niet aanwezig | GEZIEN |
| Aantal plugins in community-plugins.json | 10.083 (7 nov: 10.075) | GEZIEN |
| Verkopen skins | 0 (niet te koop via de lijst) | GOK |

Concurrenten (GEZIEN, community-plugin-stats.json 8 nov 01:45; tussen haakjes 7 nov ±22:00, dus ±4 uur ertussen, of 6 nov bij de laatste kolom):
| Plugin | Downloads | Groei | Opmerking |
|---|---|---|---|
| obsidian-dice-roller | 289.111 (289.005) | +106 | vanaf 6 nov (288.884): +227 in ±1,5 dag, ±150 per dag |
| simple-dice-roller | 8.755 (8.753) | +2 | |
| atlas-physical-dice | 1.188 (1.160) | +28 | ander doel (3D voor Atlas VTT) |
| rpg-detect-dice-roll | 1.039 (1.038) | +1 | |
| dice-table-calculator | 759 (758) | +1 | |
| dice-table | 613 (613) | 0 | |
| rpg-dice-roller | 587 (583) | +4 | |
| dice-rolls | 366 (343) | +23 | vanaf 6 nov (314): +52 in ±1,5 dag, ±35 per dag |
| dice-tray | 100 (97) | +3 | |

Let op: de stats-file wordt niet elk uur bijgewerkt, dus "±4 uur" kan meer zijn (GOK). De groei per dag is daarom grof.

Nieuw in beeld, naast ons (GEZIEN in community-plugins.json en hun README, 8 nov). Geen van drieën is dezelfde soort plugin, maar ze vissen in dezelfde vijver:
| Plugin | Downloads | Wat het doet | Wat wij ervan leren |
|---|---|---|---|
| perhaps (Perhaps, Script Wizards) | 913 | Willekeurige tabellen in eigen Perchance-notatie, in een codeblok; klikken op een deel rolt dat deel opnieuw | Tabellen zonder dobbelnotatie trekken ook publiek. Niet onze notatie, geen directe concurrent |
| solo-oracle (Solo Oracle) | 83 | Oracle en GM-emulator voor solo-spel in een codeblok, rolt ook op eigen tabellen | Heeft een **demo in de browser** met de echte plugincode op een voorbeeldnotitie. Dat hebben wij niet; advies 10 |
| lonelog | 6.196 | Notatie en sjablonen voor een solo-logboek | Solo-spelers houden een logboek bij; ons Roll log past daar (GOK) |

Lezing: Dice Roller groeit nog ±150 per dag zonder nieuwe release sinds maart 2025 (GEZIEN, grof). Dice Rolls, de nieuwkomer van dezelfde soort, haalt ±30 per dag. Mijn verwachting van gisteren (±900 downloads in de eerste maand als we dat tempo halen, GOK) blijft staan.

## Meting 7 nov 2026, ±22:00 (dag 0, nog niet aangemeld)
| Wat | Waarde | Label |
|---|---|---|
| Rollwright in community-plugin-stats.json | nog niet aanwezig | GEZIEN |
| Release 0.2.0 (7 nov 20:44 UTC) | main.js 1, manifest.json 1, styles.css 1 download | GEZIEN |
| Sterren, open issues op GitHub | 0, 0 | GEZIEN |
| Verkopen skins | 0 (niemand kan nog kopen via de lijst) | GOK |
| dortus.com/rollwright/ | gebouwd deze run, live na publicatie | GEZIEN |

Concurrenten (GEZIEN, community-plugin-stats.json 7 nov; tussen haakjes de stand van 6 nov uit `platformen/obsidian/status.md`):
| Plugin | Downloads | Opmerking |
|---|---|---|
| obsidian-dice-roller | 289.005 (288.884) | laatste release 24 mrt 2025 |
| simple-dice-roller | 8.753 (8.750) | stil sinds 2022 |
| rpg-detect-dice-roll | 1.038 | nieuw in onze lijst |
| atlas-physical-dice | 1.160 | 3D-dobbelstenen voor Atlas VTT, ander doel |
| dice-table-calculator | 758 | nieuw in onze lijst, vult tabelbereiken in |
| dice-table | 613 | nieuw in onze lijst, rolt op dobbeltabellen |
| rpg-dice-roller | 583 (580) | |
| dice-rolls | 343 (314) | +29 op één dag, zelfde soort plugin als wij |
| dice-tray | 97 (95) | zelfde soort plugin als wij |

Lezing: Dice Roller groeit nog met ±120 downloads per dag (GEZIEN, verschil tussen 6 en 7 nov; één dag, dus grof). Dat is de vraag die er nog is. Dice Rolls haalt ±29 per dag als nieuwkomer (één dag, GOK als gemiddelde). Als Rollwright een vergelijkbaar tempo haalt: ±900 downloads in de eerste maand (GOK).

## Meting 8 nov 2026, ±13:30 UTC (run 7, nog niet aangemeld)
| Wat | Stand | Bron |
|---|---|---|
| Rollwright in community-plugin-stats.json | nog niet aanwezig | GEZIEN |
| Release 0.3.0 | main.js 1, manifest.json 2, styles.css 1 download | GEZIEN |
| Release 0.3.1 | nog niet uitgebracht | GEZIEN |
| Sterren, open issues | 0, 0 | GEZIEN |
| Verkopen skins | 0 (geen gebruikers) | GOK |

Concurrenten (GEZIEN, community-plugin-stats.json; tussen haakjes 7 nov): obsidian-dice-roller 289.111 (289.005), dice-rolls 366 (343), dice-tray 100 (97). Dice Roller groeit nog ±100 per dag, de twee nieuwkomers samen ±25 per dag (afgeleid uit twee metingen een dag uit elkaar, grof). Geen nieuwe concurrent bekeken deze run. Volgende meting: dag 1 en dag 7 na de aanmelding.

## Meting 8 nov 2026, ±14:30 UTC (run 8, dag 0: live sinds 13:04)
| Wat | Stand | Bron |
|---|---|---|
| Downloads op de listing community.obsidian.md | 4 | GEZIEN |
| Versie op de listing | 0.3.0 | GEZIEN |
| Rollwright in community-plugin-stats.json en community-plugins.json | niet aanwezig (oude bestanden, de nieuwe directory telt apart) | GEZIEN |
| Lanceerberichten geplaatst | nog geen | GEZIEN (lijst-thijs) |
| Verkopen skins | onbekend, Polar alleen met inlog | GOK: 0 |

Let op voor volgende metingen: de downloads staan nu op de listing, niet meer in `community-plugin-stats.json`. Meet daar (curl op de listing, zoek "downloads"). Concurrenten blijven in de oude stats staan zolang ze daar staan.

## Meting 8 nov 2026, ±13:45 UTC (run 10, dag 0: forumbericht net zichtbaar)
| Wat | Stand | Bron |
|---|---|---|
| Downloads op de listing community.obsidian.md | 4 (gelijk aan run 8) | GEZIEN |
| Versie op de listing | 0.3.0 | GEZIEN |
| Release 0.3.0 op GitHub | main.js 3, manifest.json 3, styles.css 2 | GEZIEN (GitHub API) |
| Sterren, open issues | 0, 0 | GEZIEN |
| Forumbericht | zichtbaar, 7 keer bekeken, 0 reacties, 0 likes | GEZIEN (https://forum.obsidian.md/t/rollwright-roll-dice-and-random-tables-in-your-notes-where-a-natural-20-lands-in-gold/121721) |

Nulpunt voor het forumbericht: 4 downloads. Volgende meting: 9 nov rond 13:45 UTC (dag 1 na het forum, vlak voor r/ObsidianMD), zodat het effect van elk bericht los te zien is.
