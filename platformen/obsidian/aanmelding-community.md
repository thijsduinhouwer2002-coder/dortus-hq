# Aanmelding Rollwright bij community.obsidian.md (klaargezet voor Thijs)

Staat sinds 7 nov 21:45 op `organisatie/lijst-thijs.md`; aanmelden mag sinds 8 nov 08:40 (Thijs). Bijgewerkt voor 0.3.0 op 8 nov.

Bron (GEZIEN 7 nov, gelezen met curl): docs "Submit your plugin" en "Manage your plugin or theme" in github.com/obsidianmd/obsidian-developer-docs (map `en/Plugins/Releasing` en `en/Community directory`).

## Wat Thijs doet (eenmalig, ±10 minuten). Bijgewerkt 8 nov 08:30 UTC voor 0.3.0
Stand: release 0.3.0 staat in https://github.com/thijsduinhouwer2002-coder/rollwright (workflow groen), de README daar is de winkelpagina (poster, GIF, logboek, geen skins-plaatje meer). Thijs zei op 8 nov 08:40: aanmelden mag met het gratis deel.

1. Ga naar https://community.obsidian.md en log in met je Obsidian-account (Sign in).
2. Koppel je GitHub-account (thijsduinhouwer2002-coder) aan je profiel. Zo ziet de site dat de repo van jou is.
3. Voeg een plugin toe (Add plugin) met als repository: `https://github.com/thijsduinhouwer2002-coder/rollwright`. De site leest `manifest.json` van main (id `rollwright`, versie 0.3.0) en de release 0.3.0.
4. Kies bij Edit listing:
   - **Payment type: Optional payment** (alle worpen gratis, de skins betaald; zo noemt Obsidian dat).
   - **Short description** (komt uit manifest.json van 0.3.0; Chris' nieuwe tekst komt met 0.3.1): Roll dice inside your notes with a full formula notation, draw from tables, lists, sections and tags, and keep a history of every roll.
   - **Long description** (volledige winkeltekst van Chris voor 0.3.0, met zijn bijwerkingen van run 5 en 6; tussen de stippellijnen kopiëren):
     ```
     Roll dice and random tables right inside your notes. Write a formula, read the result, click to roll again. Made for game masters and solo players who keep their sessions in Obsidian.

     Every roll is a small game piece. Click it and it tumbles and lands in about half a second. The highest possible roll lights up gold, with a NAT 20 stamp on a natural 20; the lowest turns red. Every roll you click goes into a Roll log, grouped by note and session, so a session reads back like a story.

     New to it? Open the empty Roll log and press Try it: create an example note: a tavern scene where every roll is live.

     - Uses the `dice:` notation known from the Dice Roller plugin, so most of your existing notes should keep working.
     - Roll on your own tables, lists, sections, lines and tagged notes. Lookup tables pick the matching row.
     - Keep a result after a restart with `dice+:`, or write it into the note with `dice-mod:`.
     - Use numbers from your frontmatter: `dice: 1d20 + str`.
     - Keep highest, exploding, rerolls, success counting, Fudge and Genesys narrative dice.
     - Reading view and Live Preview look the same, in light, dark and popular themes. Roll animations are off when your system asks for reduced motion.

     All rolling is free. Optional extra skins are a one-time purchase. No account, no telemetry.
     ```
   - **Categories:** TTRPG als eerste, Editing als tweede als er twee mogen (advies 1 van Chris: daar staat Dice Roller en daar zoeken spelers).
   - **Screenshots (1200 bij 800):** twee plaatjes, in deze volgorde: `winkel-1-poster-1200.png` en `winkel-2-logboek-1200.png`, te downloaden via https://github.com/thijsduinhouwer2002-coder/dortus-hq/tree/main/platformen/obsidian/lijst-plaatjes . Geen skins-plaatje (jouw "skins nee"). De oude vijf `lijst-*.png` daar niet meer gebruiken. Daan maakt het logboek-plaatje opnieuw met verschillende tijden; komt dat later, dan kun je het via Edit listing vervangen (Olaf zet het dan op je lijst). Keuze: nu aanmelden met het huidige logboek-plaatje, omdat je dat plaatje al goedkeurde en bereik wachten ook kost; vervangen kan later zonder nieuwe keuring door Obsidian.
5. Kies Publish. De site keurt automatisch; staat er een fout, zeg het in de projectchat, dan repareert Olaf het met een nieuwe release.

Teksten volgen `commercie/rollwright/winkeltekst.md` (Chris, run 6, advies 16).

Daarna doet Olaf de rest: nakijken met "Review branch", lanceerberichten klaarzetten (forum Share & showcase, Discord #updates, r/ObsidianMD), meten op dag 7 en dag 30.
