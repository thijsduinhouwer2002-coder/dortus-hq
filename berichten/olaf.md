# Berichten van Thijs aan Olaf (Obsidian-manager)

Thijs zet hier (via de projectchat) opdrachten en wensen neer. Lees dit bestand als eerste bij elke run.
- Nieuwste bovenaan. Een open bericht gaat voor op je takenlijst, tenzij het de regels breekt.
- Klaar of verwerkt? Zet er "(verwerkt <datum>: wat je deed)" achter. Verwijder niets.


- **6 nov 22:26:** Polar staat klaar, behalve de uitbetaling (die doet Thijs later). Vul de constanten in Rollwright in: organisatie-id `5f4a360c-7552-4269-a44a-4311f7f672d6`, benefit-id `344f6030-66ec-437a-8fbb-186b80a98c65` (License Keys, geen vervaldatum, geen activatielimiet), afrekenpagina `https://buy.polar.sh/polar_cl_kJQ6H0U8GSNV0qMQkejM6SY4BYkU9k3SxfApH07ipIP`. Product-id ter info: `ecb63981-66ab-4aef-9679-7d74b6f0683f`. Laat je controleur nagaan dat de koopknop en het sleutelveld nu verschijnen. Geen haast.

- **6 nov 22:33:** Probeer Rollwright te testen in de echte Obsidian, in je eigen cloudomgeving, zodat Thijs dat niet hoeft te doen. Idee (niet getest, kan mislukken): download de Obsidian-AppImage van GitHub (obsidianmd/obsidian-releases), pak hem uit met `--appimage-extract`, start hem zonder scherm onder Xvfb (`xvfb-run`, installeer zo nodig de ontbrekende systeembibliotheken), maak een testkluis met `.obsidian/plugins/rollwright/` en zet de plugin aan via `.obsidian/community-plugins.json`. Bewijs met screenshots dat een dobbelcode rolt, een tabel werkt en de koopknop met sleutelveld verschijnt. Lukt het na een redelijke poging niet, schrijf in je logboek precies waar het vastliep en laat de test op de lijst voor Thijs staan. Geen haast, en niets aan de bestaande tests veranderen.
