# JetBrains: taken (belangrijkste bovenaan)

- [ ] Kies de bestandssoort voor D en neem het bouwbesluit. Werk de stap "Volgende meting" uit `marktmeting-2026-11-06.md` af (Marketplace via WebFetch, niet via curl). Ook het grootste gratis alternatief naast Bash en Nginx meten.
- [ ] Wacht op vrijgave van de bouwdomeinen (`lijst-thijs.md`). Test bij elke run eerst met één curl-verzoek of `plugins.gradle.org` werkt. Weigering: niet herhalen, geen omweg, één regel in het logboek.
- [ ] Herhaal de Gradle-build van een lege plugin zodra de domeinen open zijn. Eerste poging (6 nov) faalde op het downloaden van de plugin `org.jetbrains.intellij.platform`.
- [ ] Bouw een eerste versie in `producten/jetbrains-<naam>/`, met tests en meteen met proefperiode en betaalde functies.
- [ ] Zet de betaalde versie op via JetBrains Marketplace (vraagt Thijs: account en sleutel).
- [ ] Lanceren en meten op dag 7 en dag 30.
- [x] Controle uit `kandidaten.md` met echte Marketplace-cijfers, nagekeken (6 nov), zie `marktmeting-2026-11-06.md`.
- [x] Eerste ronde onderzoek zonder Marketplace-cijfers: 3 kandidaten en voorlopige keuze (6 nov), zie `kandidaten.md`.
