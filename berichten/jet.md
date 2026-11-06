# Berichten van Thijs aan Jet (JetBrains-manager)

Thijs zet hier (via de projectchat) opdrachten en wensen neer. Lees dit bestand als eerste bij elke run.
- Nieuwste bovenaan. Een open bericht gaat voor op je takenlijst, tenzij het de regels breekt.
- Klaar of verwerkt? Zet er "(verwerkt <datum>: wat je deed)" achter. Verwijder niets.

- **6 nov 16:56:** Het netwerk staat nu echt open (Any website). Gecontroleerd vanuit de projectchat: plugins.jetbrains.com, plugins.gradle.org en Maven zijn bereikbaar. Je blokkade is weg: doe je kandidaten-controle met echte Marketplace-cijfers en probeer de build van de lege plugin opnieuw. Maven gaf één keer 429 (te veel verzoeken), probeer dan even later opnieuw. (verwerkt 6 nov 16:12 UTC: controle met echte Marketplace-cijfers gedaan, zie `platformen/jetbrains/marktmeting-2026-11-06.md`; lege plugin gebouwd, 2 tests groen, zie `bouwsjabloon.md`. Maven gaf weer 429, opgelost met de JetBrains-spiegel.)

- **6 nov 17:08:** In je taken staat "Marketplace via WebFetch, niet via curl". Dat klopt niet meer: curl werkt nu (gecontroleerd, 200), en WebFetch laat Thijs steeds op een knop drukken. Gebruik vanaf nu curl, ook in de opdrachten aan je agents, en pas die regel in je `taken.md` aan. Volgorde voor je volgende run: eerst de lege plugin bouwen met Gradle (bewijst dat bouwen kan), dan de bestandssoort voor D kiezen en het bouwbesluit nemen. De tussenstap van 6 december is krap. (verwerkt 6 nov 16:55 UTC: curl stond al in `taken.md`, de WebFetch-zin uit `status.md` gehaald; lege plugin opnieuw gebouwd in een verse omgeving, werkt.)

- **6 nov 17:18, correctie op het bericht van 17:08:** Neem de tijd voor je keuze. Thijs wil uitdrukkelijk niet dat je haast maakt: een goed gekozen product gaat voor de datum van 6 december. Doe het onderzoek naar de bestandssoort grondig, en neem het bouwbesluit pas als je het kunt onderbouwen. De rest van het bericht van 17:08 blijft staan: curl in plaats van WebFetch, en de proefbuild met Gradle mag je meteen doen, want die kost weinig en bewijst dat bouwen kan. (verwerkt 6 nov 17:15 UTC: geen bouwbesluit genomen, onderzoek naar de bestandssoort verdiept, zie `platformen/jetbrains/marktmeting-2026-11-06.md` deel 6.)

- **6 nov 21:53:** De regel van Hans "bouwbesluit binnen 2 runs" vervalt: die botst met het besluit van Thijs om keuzes nooit te haasten (zie `organisatie/besluiten.md`). Wat wel blijft: begin geen nieuwe zijpaden meer. Werk de kandidaten die je nu hebt (Yacc/Bison met Flex, en Tcl) grondig af, en neem het bouwbesluit als het onderbouwd is.

- **6 nov 23:45:** Nieuwe vaste regel: elk product wordt getest in de echte app, op GitHub Actions (zie "Testen in de echte app" in `organisatie/regels.md`, voorbeeld Rollwright). Zodra je een bouwbesluit hebt, zet je een IDE-test op dezelfde manier op. Ook bouwen kan daar, als het in onze cloud niet lukt.
