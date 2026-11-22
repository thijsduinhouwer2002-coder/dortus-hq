# Onderzoek: wat YouTube ons leert over onze werkwijze

15 nov 2026, hoofdchat, op vraag van Thijs. Status: voorstellen, Thijs kiest.

## Hoe onderzocht
Gezocht op 10 onderwerpen (ploegen van agents, Claude Code-koppelingen, Blender en Godot met Claude, spellen maken met AI, Steam-marketing, Blender-hulpmiddelen verkopen, waarom AI-agents mislukken). Van 9 video's de volledige ondertiteling gelezen (lijst onderaan). Twee video's hadden geen ondertiteling ("100 uur een game met Claude", "Agent teams beter dan 99%"); die zijn NIET bekeken. Cijfers uit video's zijn niet door ons nagecontroleerd, tenzij erbij staat GEZIEN.

## Wat we al goed doen (bevestigd)
- Geen AI-beeld of AI-geluid in het Steam-spel. Volgens een video kan de verplichte AI-melding de verkoop sterk drukken (genoemd: tot 53%, NIET NAGEKEKEN).
- Testen met eigen ogen voordat iets uitgaat (echte Blender, 28 horloges). "Breng niets uit wat je niet zelf kunt controleren" komt in bijna elke video terug.
- Kleine stappen per agent in plaats van "bouw het hele spel". Wie het hele ontwerp in één keer vraagt, krijgt kapotte menu's.
- Godot (tekstbestanden, Claude kan alles lezen) en Blender via code.

## Waar we afwijken van wat werkt
1. **Mooi voor leuk.** Elke spelvideo zegt: eerst het spel met blokjes testen ("graybox"), pas als het dan leuk is mooie beelden. AI kan niet zien of iets leuk is, alleen echte spelers. Wij poetsen nu winkelbeelden en Thijs speelt pas op 4 dec.
2. **Geen contact met echte gebruikers.** De oprichter van Gumloop: "50 AI-agents die mijn bedrijf runnen" is een slop-machine; waarde komt van AI toepassen op iets wat je snapt, en praten met gebruikers. Ben Awad liet Opus 5 negen dagen een bedrijf runnen: slechte producten, bedelen om berichten te plaatsen, de omzet ging van $55 naar $88. Het enige wat goed werkte was een spelletje. Wij hebben veel agents, €0 omzet en nog geen enkele reactie van een gebruiker.
3. **Steam: pagina en demo vroeg.** Een solo-maker kreeg 60% van zijn 3.099 verlanglijstjes in 16 dagen: Next Fest (met demo) en de persoonlijke kalender van Steam vlak voor de release. Verkeer van buiten Steam was minder dan 3%. Zijn les: winkelpagina zo vroeg mogelijk, demo en speeltest veel eerder, YouTubers laten spelen.
4. **Laten zien in plaats van vertellen.** Bij Blender-spullen: mensen kopen omdat ze het in een filmpje zien. Wij hebben voor Click Joints Pro nog geen demofilmpje.

## Gereedschap dat genoemd werd, met ons oordeel
| Tool | Wat | Oordeel voor ons |
|---|---|---|
| Hooks en controles bij elke commit (zoals in "Claude Code Game Studios") | automatisch tegenhouden wat niet mag | **Ja.** Een controle in GitHub die commits met persoonsgegevens (IBAN, telefoonnummer, privé-mail) of gedachtestreepjes tegenhoudt. De repo is openbaar; nu hangt het af van elke agent die het onthoudt. |
| "Klaar"-eisen per taak met screenshot als bewijs | taak pas af als het gezien is | **Deels al zo.** Strakker maken voor het spel: elke taak die je ziet, heeft een schermafbeelding uit de echte build. |
| Uitwaaieren met tegenspraak (Claude Code-team) | meerdere agents zoeken, anderen controleren of het klopt | **Ja, voor keuringen.** Doen we al bij Ebb (drie frisse keurders). Ook voor winkelbeelden en de speeltest. |
| Blender MCP | Claude bestuurt Blender met de muis | **Nee.** Wij draaien Blender als Python-pakket in de cloud, dat is sneller en werkt zonder scherm. |
| Godot MCP | Claude start het spel en kijkt mee | **Misschien.** Onze agents hebben geen scherm. Eerst proberen of Godot in de cloud een schermafbeelding kan maken (GOK dat het met een virtueel scherm kan). |
| Caveman (teksten inkorten) | CLAUDE.md en rolinstructies korter, minder verbruik | **Ja, voorzichtig.** Onze opdrachten zijn lang en worden elk uur door elke agent gelezen. Inkorten en daarna testen of het werk even goed blijft. |
| CLI's in plaats van koppelingen | minder verbruik | Klein voordeel, niet nu. |
| Firecrawl | websites lezen die curl niet haalt (zoals Reddit) | Kost geld en een account (moet Thijs doen). Niet nu. |
| Higgsfield, PixelLab, Tripo | AI-beelden en 3D-modellen | **Nee** voor Steam (AI-melding). |
| Vercel | HTML snel online | Niet nodig, we hebben GitHub Pages en artifacts. |
| Bouwen in het openbaar op X | volgers en spelers vóór de lancering | Werkt volgens twee video's. Vraagt een account van Thijs. Kandidaat. |

## Voorstellen, op volgorde van mijn advies
1. **Ruwe speeltest eerder** (rond za 21 nov), vóór nog meer poetswerk. Thijs speelt, en als het kan twee of drie andere mensen.
2. **Controle in GitHub voor de openbare repo** (persoonsgegevens en gedachtestreepjes). Klein werk, groot risico weg.
3. **Demofilmpje Click Joints Pro** (20 tot 30 seconden, echte Blender-beelden) voor de lancering op BlenderNation en Superhive.
4. **Opdrachten van de agents inkorten** om verbruik te sparen, met een test erna.
5. **Echte gebruikers zoeken**: speeltesters voor Hats of the Fallen, reacties uit de Blender-community, later een X-account om in het openbaar te bouwen.

## Bronnen
- [The 3 Levels of Vibe Coding AI Apps with Claude Code](https://www.youtube.com/watch?v=PySsRphFaHA), Zinho Automates
- [How the Claude Code team uses Claude Code](https://www.youtube.com/watch?v=S-sYlFiGFv8), Claude
- ["50 AI Agents Running My Company" Is a Lie](https://www.youtube.com/watch?v=CxFQykWiJqY), EO, Max Brodeur-Urbas
- [I Let Claude Opus 5 Run a Business Alone for 9 Days](https://www.youtube.com/watch?v=vOK0Cdbk-Ps), Ben Awad
- [How to Make a Game With Claude Code and Publish It on Steam](https://www.youtube.com/watch?v=r2z01arn2aE), Mr omi
- [Build a Solo Game with Claude Code Game Studios](https://www.youtube.com/watch?v=cDQ9yQk23qw), Deep Vector
- [How I Got 3,099 Steam Wishlists With Zero Ads](https://www.youtube.com/watch?v=cxPfpYsXNWE), Brian Is Making Games
- [The Real Way to Make Money With Blender in 2026](https://www.youtube.com/watch?v=hDYGeRcbnKA), BlenderVitals
- [12 Claude Plugins, Skills & MCP's I Can't Live Without](https://www.youtube.com/watch?v=je95KXv1QlA), Ben AI
