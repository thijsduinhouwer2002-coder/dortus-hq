# Oude bestanden staan in een release

De ruwe onderzoeksdata uit deze map staan sinds 22 nov 2026 niet meer op main, maar in de release `archief-beelden-2026-11-22`, bestand `onderzoek-data.zip`:
https://github.com/thijsduinhouwer2002-coder/dortus-hq/releases/tag/archief-beelden-2026-11-22

In de zip staan ze met hun oude pad. De lijst van paden staat in `organisatie/opruimen/archief-beelden/onderzoek-data.txt`. In de geschiedenis van git staan ze ook nog (`git log --all -- <pad>`). Reden: opruimen fase 2, besluit Thijs 19 nov 17:31 (repo kleiner, snellere kloon).

**Bijgewerkt 22 nov 2026 (keuring fase 2):** bestanden met mailadressen van anderen (ruwe winkeldumps) zitten niet meer in de zip; welke staat in `organisatie/opruimen/archief-beelden/onderzoek-data.weglaten`. Ze staan alleen nog in de git-geschiedenis.

`steam-desktop-kaart-2026-11-16.csv` staat weer hier (22 nov), want `platformen/steam/marketing/data/demo-spelers.py` leest hem.
