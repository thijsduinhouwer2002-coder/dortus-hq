# Ontwerp support.html (16 nov 2026, run 38)

**Wat en voor wie:** de pagina dortus.com/support.html, waar de link "Support" bovenaan en onderaan de voorpagina naartoe gaat. Voor gebruikers van Click Joints (gratis en Pro), Ebb, Rollwright en Bison & Flex. Nu gaat hij alleen over de gestopte Atlassian-apps met support@dortus.com.

**Af als:** per huidig product staat er wat je in je mail zet en waar je terecht kunt (GitHub, privacy, terugbetalen waar we dat weten); overal thijs@dortus.com; de Atlassian-apps alleen als één regel onderaan; Amami, meta-CSP, referrer en meta description erin; geen horizontaal scrollen op 390 en 1280; Daan zegt ja.

**Open vragen, zelf beantwoord:**
- Antwoordtijd? "binnen 5 werkdagen", net als Ebb (staat al live); geen nieuwe belofte.
- Terugbetalen bij Pro (Gumroad)? Geen beleid vastgelegd, dus niets beloven; wel waar de downloadlink staat (de Gumroad-mail).
- Bison & Flex is nog niet in de winkel: kaart blijft, met "Coming soon", zoals op de productpagina.
- privacy.html en terms.html gaan over Atlassian: niet als hoofdknop, wel per product de eigen privacy-plek.
- De 81 oude pagina's die naar support.html linken: geen ankers, dus niets breekt.

**Aanpakken:**
1. Alleen adres en Atlassian-tekst vervangen. Snel, maar de pagina blijft over de verkeerde producten gaan.
2. Pagina opnieuw opbouwen met de bouwstenen van styles.css (page-head, band, cards, checks), kop en voet zoals de productpagina's. Middenweg: past bij de rest, geen nieuwe CSS.
3. Nieuwe opmaak in de stijl van de voorpagina (eigen inline-CSS). Mooier aan elkaar, maar meer werk en meer kans op fouten.

**Keuze: 2.** Productpagina's en ebb/support.html gebruiken dezelfde styles.css, dus de bezoeker die van een product komt ziet hetzelfde. Geen nieuwe CSS nodig.
