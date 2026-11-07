# Rollwright: lanceerberichten (concepten)

Door Chris, 7 nov 2026. Posten onder de naam van Thijs doet Thijs zelf. Deze berichten gaan pas naar `organisatie/lijst-thijs.md` als Rollwright echt in Community plugins staat (anders kan niemand het met één klik installeren). Daarvoor moet Thijs eerst de aanmelding doen (lijst-thijs, 7 nov 21:45).

## Volgorde en waarom
1. **Obsidian-forum, categorie Share & showcase** (forum.obsidian.md). Daar kondigen makers nieuwe plugins aan; mensen die Obsidian goed kennen lezen het.
2. **r/ObsidianMD** (Reddit). Groot publiek van Obsidian-gebruikers.
3. **r/Solo_Roleplaying**, één of twee dagen later. Solo-spelers houden vaak een logboek bij in notities en rollen veel op tabellen; dat is onze kerngebruiker (GOK).
4. **Obsidian Discord, kanaal #updates** (alleen als de regels van dat kanaal een nieuwe plugin toestaan).

Niet tegelijk overal posten: dan kan Thijs niet op vragen reageren. Eén plek per dag.

Let op (GOK, niet kunnen lezen): de regels van de subreddits over eigen werk en over plugins die met AI gemaakt zijn. Reddit gaf geen antwoord op curl. Thijs: lees de regels in de zijbalk voor je post. Is er een regel over AI, zet dan de zin "Built with the help of AI tools, tested in the real Obsidian app before every release." onderaan. Eerlijk zijn gaat voor bereik.

## 1. Forum, Share & showcase

**Titel:** Rollwright: roll dice and random tables inside your notes

**Tekst:**
Hi all,

I made Rollwright, a dice roller for people who run or play tabletop games in Obsidian. You write a formula in a note, read the result, and click it to roll again.

It uses the same `dice:` notation as the Dice Roller plugin, so notes you already have should keep working. On top of that:

- Roll on your own tables, lists, sections, single lines and tagged notes. A lookup table picks the row that matches a roll.
- `dice+:` keeps a result after a restart, `dice-mod:` writes the result into the note after you confirm.
- Numbers from your frontmatter work in a roll: with `str: 3`, `dice: 1d20 + str` adds 3.
- Keep highest, exploding dice, rerolls, success counting, Fudge dice and Genesys narrative dice.
- A roll history panel. Reading view and Live Preview look the same.

All rolling is free. Two extra looks are a one-time $6 purchase, which is how I hope to keep working on it. No account and no telemetry.

Install: Settings, Community plugins, search "Rollwright".
Full reference and source: https://github.com/thijsduinhouwer2002-coder/rollwright
Page: https://dortus.com/rollwright/

I'd love to hear what you roll on and what is missing. Bugs and ideas are welcome here or on GitHub.

[plaatje: lijst-2-live-preview.png uit `platformen/obsidian/lijst-plaatjes/`]

## 2. r/ObsidianMD

**Titel:** I made a dice roller plugin that rolls on your own tables and uses your frontmatter

**Tekst:** zelfde als het forumbericht, zonder de eerste regel "Hi all". Voeg toe als eerste zin na de titel: "Rollwright is now in Community plugins." Plaatje: lijst-2-live-preview.png en lijst-3-geschiedenis.png.

## 3. r/Solo_Roleplaying

**Titel:** For solo players who journal in Obsidian: a plugin to roll dice and oracle tables inside your notes

**Tekst:**
I play and keep my session logs in Obsidian, so I made a plugin for it: Rollwright.

You keep your oracles and random tables as normal notes. Then, in your journal, `dice: [[Oracles^yesno]]` picks a row, and a click rolls again. A lookup table can have a formula in its header (`dice: 1d20`) and Rollwright finds the matching row. You can roll a random line from a list, a block from a note, or a note with a tag. The roll history shows what you rolled and where it came from.

It is free (two optional skins cost $6 once) and needs no account. It is in Obsidian's Community plugins as "Rollwright".

More: https://dortus.com/rollwright/

[plaatje: lijst-1-lezen.png]

Let op Thijs: de eerste zin "I play and keep my session logs in Obsidian" alleen gebruiken als dat klopt. Zo niet, begin met: "Many solo players keep their session logs in Obsidian, so I made a plugin for it: Rollwright."

## 4. Discord #updates (kort)
Rollwright 0.2.0 is in Community plugins: roll dice and random tables inside your notes. Uses the `dice:` notation, rolls on your tables, lists, sections and tags, reads numbers from frontmatter, keeps a roll history. Free, two optional $6 skins. https://github.com/thijsduinhouwer2002-coder/rollwright

## Na het posten
- Reageer binnen een dag op vragen; een bug gaat als issue naar de repo, Olaf pakt hem op.
- Chris telt op dag 7 de downloads per bericht-dag (sprongen in community-plugin-stats.json) in `cijfers.md`.
