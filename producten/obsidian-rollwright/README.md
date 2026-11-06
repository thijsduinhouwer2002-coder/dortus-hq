# Rollwright

Roll dice inside your notes. Write a formula in inline code, read the result, click to roll again. Rollwright also draws from tables, lists, sections, lines and tags, and it keeps a history that shows which note each roll came from.

Rollwright is at version 0.1.0 and has not been tested in a running app yet. Expect rough edges.

## Rolling dice

Write `` `dice: 2d6 + 3` `` in a note. It works in reading view and Live Preview. Hover to see the formula and the dice. Click to roll again. A result stays while you scroll or type elsewhere in the note. It is rolled again when you click, after a restart, and when lines above it are added or removed, because a result is tied to its line. A roll in a table cell can also roll again when the note is drawn again.

| You write | What it does |
|---|---|
| `2d6 + 3 * (1d4 - 1) ^ 2` | Arithmetic with `+ - * / ^` and brackets |
| `d20`, `3d`, `d` | Leave out the count (1) or the sides (100). Both can be changed in the settings |
| `2d[3,5]` | Dice from 3 to 5, both included |
| `1d[1,3,5]` | Dice with exactly these faces |
| `d%` | A hundred-sided die |
| `1d66%` | One die per digit, read together: 6 and 3 give 63 |
| `4dF` | Fudge dice |
| `(1d4)d6` | Roll for the number of dice first |

### Modifiers

Modifiers run from left to right. A number is optional and defaults to 1.

| Modifier | Meaning | Shown as |
|---|---|---|
| `k2`, `kh2` | Keep the highest 2 | `3d` for a dropped 3 |
| `kl2` | Keep the lowest 2 | `3d` |
| `dl2`, `dh2` | Drop the lowest or highest 2 | `3d` |
| `!2`, `!i` | Explode up to 2 times per die. `i` means up to 100 | `6!` |
| `!!2`, `!!i` | The same, added into a single die | `28!` |
| `r2`, `ri` | Reroll up to 2 times and replace. `i` means up to 100 | `4r` |
| `s`, `sa`, `sd` | Sort low to high, or high to low | |
| `u` | Reroll until all dice differ | `4r` |

`!` explodes on the highest face and `r` rerolls the lowest, unless you add conditions: `1d4!=3`, `1d4!i=!3`, `1d4r<3`, `1d4r<2>3`. Conditions right after `!` or `r` belong to that modifier.

### Counting successes

A condition on dice turns each die into a score: 1 if it matches, otherwise 0. The result is the sum.

`=`, `=!` (not equal), `>`, `<`, `>=`, `<=`, and `-=` or `=-` to score -1. Example: `5d10>=8-=1`. The first matching condition counts. The threshold can be dice too: `3d6>1d6`.

### Flags

Add flags after `|`, as in `1d20 + 2|nodice|text(Dexterity +2)`.

| Flag | Effect |
|---|---|
| `\|nodice` | Hide the die icon |
| `\|form` | Show the formula before the result |
| `\|avg` | Show the average first; a click rolls. With modifiers, or when a formula divides by dice or raises dice to a power, the average is an estimate, marked with `~` |
| `\|none` | Show only an icon until the first click |
| `\|text(label)` | Show your label before the result |

## Rolling on your notes

| You write | What it does |
|---|---|
| `[[Note^id]]` | A random row of that table, or a random item of that list |
| `3[[Note^id]]`, `3d[[Note^id]]`, `1d4+1[[Note^id]]` | Several picks. Picks can repeat |
| `[[Note^id]]\|Column` | A random cell from that column |
| `[[Note^id]]\|xy` | A random cell, outside the first column. A column named xy wins |
| `[[Note]]` | A random block of the note, without frontmatter and horizontal rules |
| `[[Note]]\|paragraph,heading-2` | Only these block types |
| `[[Note]]\|line` | A random non-empty line |
| `#tag`, `#tag\|+` | A random block from each note with the tag |
| `#tag\|-` | A random block from one random note with the tag |
| `#tag\|link` | A link to one random note with the tag |
| `2d#tag`, `#tag\|-\|paragraph,yaml` | Several picks, and block types |

The forms `[[Note#^id]]` and `[text](Note#^id)` also work.

A roll inside a block or section you draw is not rolled again: it shows as plain code. An embedded note in such a result becomes a link. Embedded images stay.

### Lookup tables

If the first header is a formula, Rollwright rolls it and finds the matching row. Rows can be written as `1-2`, `11`, `13,14` or `51–60`. A cell may hold another roll, such as `` `dice: 2d6` `` or `dice: [[Note^id]]`.

```markdown
| dice: 1d20 | Weather |
|---|---|
| 1-5 | Rain |
| 6,7 | Fog |
| 8–20 | `dice: [[Skies^clear]]` |
^weather
```

## Side panel, commands and settings

- **Roll history** shows rolls you clicked or typed, with the source note, and lets you roll again. Rolls that happen by themselves when a note opens are not listed. The history is stored in the plugin's data file.
- **Commands:** "Open roll history" and "Roll a formula".
- **Settings:** default die, default number of dice, and saved formulas. A saved formula works by name in any roll, such as `` `dice: attack` `` or `1d6 + bonus`.
- **Import:** a button copies named formulas from the data file of the Dice Roller plugin, if you have it. That file is only read. Existing names are kept. The layout of that file was not verified, so an import may find nothing.

## Paid skins

**All rolling features are free. Two visual skins, Parchment and Arcane, are paid and need a license key.** The Classic skin is free.

License keys are not on sale yet. Payment has not been arranged, and there is no buy button until it has. The key is checked on your device.

## Privacy

Rollwright makes no network connections, has no telemetry and needs no account. It reads your notes to roll on them. Your notes are not changed. Outside the vault it touches nothing.

## Limits

Up to 1000 dice per group, 10000 dice per formula, 1000000 sides, and 100 repeats per die for `!` and `r`. One roll, nesting included, can use up to 10000 picks from notes. Beyond that you get a message. A broken formula is underlined and the tooltip gives the reason.

## Development

`npm install`, then `npm test`, `npm run build` and `npm run lint`.

## License

MIT, see [LICENSE](LICENSE).
