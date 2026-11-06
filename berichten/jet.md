# Berichten van Thijs aan Jet (JetBrains-manager)

Thijs zet hier (via de projectchat) opdrachten en wensen neer. Lees dit bestand als eerste bij elke run.
- Nieuwste bovenaan. Een open bericht gaat voor op je takenlijst, tenzij het de regels breekt.
- Klaar of verwerkt? Zet er "(verwerkt <datum>: wat je deed)" achter. Verwijder niets.

- **6 nov 16:56:** Het netwerk staat nu echt open (Any website). Gecontroleerd vanuit de projectchat: plugins.jetbrains.com, plugins.gradle.org en Maven zijn bereikbaar. Je blokkade is weg: doe je kandidaten-controle met echte Marketplace-cijfers en probeer de build van de lege plugin opnieuw. Maven gaf één keer 429 (te veel verzoeken), probeer dan even later opnieuw. (verwerkt 6 nov 16:15 UTC: controle met echte Marketplace-cijfers gedaan, zie `platformen/jetbrains/marktmeting-2026-11-06.md`; lege plugin gebouwd, 2 tests groen, zie `bouwsjabloon.md`. Maven gaf weer 429, opgelost met de JetBrains-spiegel.)

- **6 nov 17:08:** In je taken staat "Marketplace via WebFetch, niet via curl". Dat klopt niet meer: curl werkt nu (gecontroleerd, 200), en WebFetch laat Thijs steeds op een knop drukken. Gebruik vanaf nu curl, ook in de opdrachten aan je agents, en pas die regel in je `taken.md` aan. Volgorde voor je volgende run: eerst de lege plugin bouwen met Gradle (bewijst dat bouwen kan), dan de bestandssoort voor D kiezen en het bouwbesluit nemen. De tussenstap van 6 december is krap.
