# Voorstel: Sylius Addons Marketplace

Vera, verkenner. Run 14 nov 2026, 16:31 (Amsterdam). Eigen meting van alle 568 productpagina's uit de sitemap (`data/sylius-addons-2026-11-14.jsonl`), plus één hulpagent voor voorwaarden, grootte en geld. De kern (verkopen mag niet) heb ik zelf in de voorwaarden nagelezen.

## Wat het is
Sylius is open-source webwinkelsoftware op Symfony (PHP), uit Polen. In maart 2026 opende Sylius een eigen winkel voor plugins, addons.sylius.com, met de plugins van GitHub en de oude Sylius Store erin (DERDEN, https://sylius.com/blog/implementing-the-sylius-addons-marketplace/, 3 mrt 2026).

## De doorslag: makers mogen er niets verkopen
- GEZIEN, Vendor Terms (https://addons.sylius.com/terms-and-conditions.pdf), artikel 6: "Vendor Products are made available through the Marketplace as free of charge plugins distributed through public repositories and installable via Composer. The Marketplace does not provide integrated payment processing for Vendor Products." Alleen Sylius zelf mag betaalde producten aanbieden.
- GEZIEN, https://addons.sylius.com/en_US/become-a-vendor: betalen voor makers is "planned", zonder datum. De wervingstekst noemt al abonnementen en snelle uitbetaling, maar de voorwaarden zeggen het tegendeel.
- GEZIEN, eigen meting: van de 568 producten hebben er 2 een prijs, en die zijn allebei van Sylius zelf (certificering € 250, cursus € 599). Alle 566 andere staan op € 0. De Sylius Plus-modules staan er met "Contact Sales" (gezien door de hulpagent).

## Bereik (GEZIEN, eigen meting)
- 568 producten van 211 makers. Grootste: Setono 44, Sylius 31, BitBag 27, Monsieur Biz 26, tmonier 22, 3BRS 20. Bijna allemaal bureaus; BitBag hoort bij hetzelfde concern als Sylius.
- Downloads staan in vakjes (Packagist, telt ook CI): 301 onder 1K, 126 1K+, 81 10K+, 20 50K+, 32 100K+, 1 500K+, 4 1M+.
- Drukte: eerste uitgave in 2024 65, in 2025 51, in 2026 tot nu 44 plugins. Dus ±4 per maand.
- Nieuwe plugins van jan t/m jun 2026 (21): 14 onder 1K downloads, 6 boven 1K, 1 boven 10K. Mei t/m okt 2025 (28): 18 onder 1K, 3 1K+, 5 10K+, 2 100K+.
- Reviews: 4 van de 568 producten hebben er een. De winkel speelt geen rol bij kiezen; gebruikers zijn ontwikkelaars die via Composer installeren.

## Grootte van Sylius
- Sylius zegt "10 000+ online stores" (DERDEN, https://sylius.com/). Wappalyzer ziet er maar 350, 60% in Frankrijk (DERDEN, https://www.wappalyzer.com/technologies/ecommerce/sylius/).
- Downloads van sylius/sylius per dag: 2.564 (2023), 2.882 (2024), 2.263 (2025), 3.859 (2026, in okt en nov ±6.000) (GEZIEN door de hulpagent, Packagist).
- Het bedrijf groeit: in feb 2026 kocht cyber_Folks samen met Sylius en BitBag PrestaShop (DERDEN, https://www.ecommerce-nation.fr/?p=125797).

## Geld
- In de winkel: nul, verboden voor makers (zie boven).
- Buiten de winkel: het enige voorbeeld van een derde die verkoopt is Odiseo, Marketplace Plugin vanaf $1.690 met bureaulicentie, eigen site (DERDEN, https://odiseo.io/en/products/sylius-marketplace-plugin). Geen omzetcijfers van makers gevonden.
- Kopers zijn bureaus en middelgrote bedrijven, niet losse winkeliers (afleiding uit bureaulicenties en "Contact Sales", GOK). Dat lijkt op Atlassian, waar we bewust weg zijn gegaan.

## Past het bij ons
Bouwen kan (PHP/Symfony), maar zonder kassa moeten we zelf verkopen aan bureaus. Dat is precies wat we niet kunnen zonder naam en verkoopwerk.

## Cijfer en advies
**Cijfer 1. Nee.** Bereik klein (±4 nieuwe plugins per maand, nieuwe plugins meest onder 1.000 downloads) en geld onmogelijk: de voorwaarden staan alleen gratis plugins toe. Opnieuw kijken alleen als Sylius de betaalde verkoop voor makers echt opent (nieuwe Vendor Terms); dan eerst tellen hoeveel betaalde plugins van derden er na 3 maanden staan.

Niet apart nagekeken door een controleur: de uitkomst is nee en hangt aan één zin uit de voorwaarden, die ik zelf in het PDF las.
