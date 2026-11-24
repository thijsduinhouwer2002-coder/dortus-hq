# Speelscherm op een licht bureaublad (Mila, 24 nov 2026, issue 6)

Waarom: de nulmeting (`organisatie/blindtest/uitslag/hats-scherm-2026-11-24-2253.md`, GEZIEN) zette de huidige winkelschermen 1 en 4 op plek 3 tot 4 bij beide rechters. Hun reden, vier keer: "het laat niet zien dat het op je bureaublad onderaan het scherm leeft" en "lijkt een gewoon mobiel spel". Dat is precies punt 10 van de etalage-audit: licht bureaublad, werkvenster, hogere strook, zoals Rusty's scherm 1.

- `maak_speelscherm.py <strook> <uit>`: lucht, wolken en heuvels met Pillow, een teksteditor, pictogrammen en een neutrale taakbalk (geen merken), en de strook op ware grootte (1920 x 320, geen opschaling).
- `strook-fel-1920x320.png`: Blender-render van `producten/steam-hol/modellen/hol.py` met `HOL_FEL=1` (aarde een trede donkerder in dezelfde warme kleur, vloer en gras lichter, look Medium High Contrast). `strook-nu-1920x320.png`: dezelfde render zoals de tegels nu zijn.
- C = fel, D = nu. Zo meet de blinde test los wat het bureaublad doet en wat het felle licht doet.

**Let op, eerlijk:** de strook is een render van de hol-scène uit de spelmodellen, geen opname uit het spel. Voor Steam moet het winnende beeld opnieuw uit het spel komen (zelfde opstelling, strook zo hoog als het spel toelaat). Dit is een richtingsproef, niet om te uploaden.
