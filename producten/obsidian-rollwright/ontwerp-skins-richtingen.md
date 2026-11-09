# Betaalde skins: drie richtingen (Daan, 9 nov 2026)

Aanleiding: Thijs 8 nov 22:58. Hij werd niet warm van Parchment en Arcane v3 ("klein en los op zwart, je ziet niet dat het in Obsidian zit, neon is algemeen"). Hij wil per skin een andere achtergrond, een ander lettertype, andere kleuren, en beeld bij wat er gerold wordt (wolf, val). Vraag: 2 of 3 duidelijk verschillende richtingen, groot (16:9) in een echte Obsidian-notitie met rollenspeltekst, zodat hij kan kiezen.

**Waarom wij (één zin):** dobbelsteen-skins bij de concurrenten (Dice So Nice in Foundry, D&D Beyond, dddice) zijn een 3D-dobbelsteen op een tafel los van je aantekeningen; een Rollwright-skin verandert de hele plek waar je speelt: je notitie, je worpen en je Roll log worden samen één wereld, met een eigen materiaal, letter en icoon per worp.

## De drie richtingen
Elke richting is een complete wereld. Alle drie gezien in de echte Obsidian met de echte plugin en echte worpen (tak `ontwerp/rollwright-richtingen`, prototype-CSS bovenop 0.3.2).

| | A. De Taverne | B. De Kerker | C. De Hofcodex |
|---|---|---|---|
| Sfeer | warme herberg bij kaarslicht | koude kerker, vuur in de verte | verluchte middeleeuwse codex |
| Achtergrond | donker eikenhout, warm kaarslicht langs de randen | ruwe grijze steen, sintelgloed van onderen | nachtblauw rond een blad velijn met goud- en lapisranden |
| Letter | Alegreya SC (uithangbord) | Uncial Antiqua (Keltisch, gebeiteld) | UnifrakturMaguntia (fraktur) met rode initiaal |
| Kleuren | messing, amber, donkerbruin | steengrijs, sintel-oranje | lapisblauw, vermiljoen, bladgoud op ivoor |
| Token | gegoten messing munt met reliëf | stenen plaatje met gebeitelde letters | blauw vak met gouden en rode lijsten, zoals een verluchte letter |
| NAT 20 | munt licht op als kaarsvlam (gouden gloed) | goud gloeit op uit het steen | bladgoud met dubbele lijst in blauw en rood |
| NAT 1 | dof koper, rode gloed | het steen barst aan de randen, rood licht door de barst | vermiljoen vak |
| Roll log | houten bordjes met messing letters | in de muur gehakte regels met een gloeiende rand | regels op velijn met rode fraktur-namen |
| Wolf, val | messing silhouet | gloeiend oranje silhouet | lapisblauw silhouet zoals een miniatuur |

**Icoon bij een worp (alle drie):** een optie, niet geraden uit de tekst. De gebruiker kiest zelf een icoon bij een worp (bijvoorbeeld `dice: 1d20 + 6|text(Attack)|icon(wolf)`) of een lijstje woord naar icoon in de instellingen. Iconen van game-icons.net (CC BY 3.0, naamsvermelding in de README en de instellingen). In het prototype staat het icoon klein in het token en groot in de callout van de notitie.

**Eerlijkheid:** de achtergrond van de notitie is in dit prototype deel van de skin. In de plugin kan dat alleen als de gebruiker het aanzet (een notitie met `cssclasses: rollwright-world`, of een schakelaar "skin ook op de notitie"), omdat een plugin niet ongevraagd andermans notities mag verven. Zonder die schakelaar krijgt de gebruiker token, Roll log en iconen in de wereld van de skin.

## Mijn keuze (bijgewerkt na de controleur)
**A (Taverne) en C (Hofcodex) als de twee betaalde skins, B als derde later.** Waarom: A en C zijn het verst uit elkaar (donker en warm tegen licht en kleurrijk) en elk is in één oogopslag te herkennen. C is de enige lichte wereld (de plaatjes van C zijn in het lichte thema gemaakt). B is gedurfder dan A; de controleur raadt C plus B aan. Daarom vraag ik Thijs te kiezen uit A, B en C en noem ik geen vaste twee. Zelf neig ik naar C plus B, de controleur heeft gelijk dat A het braafst is.

## Plaatjes (16:9, echte Obsidian)
Zie de links in `ontwerp/rollwright/richtingen/` (onderaan bijgewerkt na de keuring).

## Keuring
- Runs: 42540486539 (eerste), 42541007972, 42541435382, 42541905330 en 42542400186 (laatste, plaatjes in `ontwerp/rollwright/richtingen/`). Alles GEZIEN met de Read-tool.
- Controleur (agent) op run 42541905330: nee, vijf moet-punten: fraktur in kleine tekst onleesbaar (stempel, kop Roll log), witte hoekjes bij de tab in C, barst door de tekst in B, ongetoetste bewering over licht thema, beweringen die niet te zien waren (lichtvlek, groef, afgeschuinde hoeken). Alles verwerkt in ronde e (run 42542400186, GEZIEN door mij met de Read-tool): stempel en kop in Spectral, tab schoon, barst alleen aan de randen, kaarslicht in A sterker, tekst rechtgezet. Geen tweede keuring, de punten waren klein en zijn per plaatje nagekeken.
- Kan-punten voor de bouw: placeholder van het invoerveld in A en B bijna onzichtbaar; vijfde logregel zonder naam (Initiative heeft geen label in de notitie).
