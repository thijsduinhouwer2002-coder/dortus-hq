# Keuring e2e Bison & Flex, bekendePlatformfout (fdbdab4), Chris, 24 nov 2026 ±00:44 NL
**Akkoord: ja**
- Filter is smal: beide stukjes tekst moeten erin staan ("node is not a child" en "OccurenceNavigatorSupport"), en nooit als er com.dortus in de melding staat (Gedeeld.kt regel 39 tot 43). Elke overslag komt in het log met DORTUS-E2E.
- Run 45278286189 op fdbdab4 groen in beide thema's (GEZIEN, Actions-API). Zoals Olaf zelf zegt: de fout trad niet op, dus dit bewijst alleen dat de test niet stuk is.
- Kan: kleine unittest met drie gevallen (bekende fout, dezelfde met com.dortus, andere fout), zoals de automatische keurder ook zegt. Kan: haal de filter weg zodra IntelliJ het oplost.
