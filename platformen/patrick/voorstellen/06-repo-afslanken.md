Wat verandert: een nieuw bestand `.gitignore` in de hoofdmap van dortus-hq, plus één regel in CLAUDE.md (staat al in voorstel 01). Nieuwe ruwe data en grote films komen niet meer in git; wat er al staat blijft staan.
Waarom: `.git` is 2,7 GB (GEZIEN, `du -sh .git`, 9 nov). In de werkmap: `platformen/verkenner/data` 140 MB, `platformen/pionier/data` 33 MB, `ontwerp/` 159 MB, GIF's samen 74 MB, deels dubbel (demo-v4-b.gif staat ook als producten/obsidian-rollwright/images/demo.gif, 8.854.557 bytes). In mijn eigen run liep `git fetch` na 2 minuten vast en was de kloon ondiep. Elke run van elke Claude betaalt dit in tijd.

---

## Nieuw bestand `.gitignore`

```
# Ruwe data van onderzoek: niet in git. Bewaar een samenvatting in markdown
# en, als het echt nodig is, de ruwe data als Actions-artefact of op de tak `data`.
platformen/*/data/*.json
platformen/*/data/*.jsonl
platformen/*/data/*.tsv
platformen/*/data/*.tsv.gz
platformen/*/data/*.csv
platformen/*/data/*.html

# Bouwresten
**/node_modules/
**/__pycache__/
**/.gradle/
**/build/
dashboard/uit/
```

Bestanden die al in git staan blijven gewoon werken; `.gitignore` geldt alleen voor nieuwe. Wil een Claude toch een klein databestand bewaren (onder 1 MB), dan mag dat met `git add -f` en een reden in de commit.

## Wat de ploeg anders doet
- Onderzoek: schrijf de uitkomst (aantallen, steekproef, de 20 belangrijkste rijen) in markdown. De ruwe download blijft in de run of gaat als artefact mee met een workflow.
- Ontwerp: films en GIF's niet blokkeren, want Daan geeft ze via git door aan de bouwer (bijvoorbeeld `ontwerp/rollwright/demo-rustig.gif` in `producten/obsidian-rollwright/ontwerp.md`). Wel: tussenversies (v1, v2, extra-run) op de tak `schermen` zetten, en in `ontwerp/` alleen de versie die geldt. Een GIF boven 3 MB eerst verkleinen (minder kleuren of frames). Een kopie in `producten/` is genoeg; niet ook in `ontwerp/`.
- Klonen: `git clone --depth 50` is genoeg voor bijna elke run. Voor `git log` over dagen: `git fetch --shallow-since="3 days ago"`.

## Keuze voor later (Thijs): de oude geschiedenis opschonen
De 2,7 GB zit in de geschiedenis. Die kleiner maken (bijvoorbeeld met `git filter-repo`) herschrijft alle commits en vraagt dat elke Claude opnieuw kloont. Dat is niet terug te draaien en raakt de hele ploeg tegelijk, dus alleen als Thijs ja zegt, op een moment dat alles stil ligt. Mijn advies: eerst alleen de `.gitignore`, over twee weken kijken of de repo nog te traag is.

**Werk:** 10 minuten. **Gewoon goed** (het opschonen van de geschiedenis is een keuze van Thijs).
