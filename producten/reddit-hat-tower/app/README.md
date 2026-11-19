# Gloop's Hat Tower

A one-button daily stacking game for Reddit. A hero drops into the cave. Tap when he reaches
Gloop's mouth: GULP, his hat flies onto the tower on Gloop's head. You have 30 seconds.

Every day there is one new tower for everyone, and every subreddit stacks one shared tower together.

## How to play

- Tap anywhere (or press Space) when the hero is at Gloop's mouth. A yellow `!` shows the moment.
- Hit the middle of the mouth for a perfect GULP and build a streak.
- Every catch makes the next hero fall a little faster.
- Missing never costs a hat. The hero walks off ("bye!") and the next one falls a bit slower.
- Tapping too early makes Gloop snap at the air and close his mouth for a moment.
- Golden heroes carry three hats.

## Every day

- **One tower per day, the same for everyone.** Every player gets the same heroes in the same rhythm,
  with the same golden heroes. Your first run of the day counts. Practice as much as you like.
- **A daily rule** changes how the tower plays: Classic, Rush Hour, Heavy Heroes, Golden Hour or Big Mouth.
- **Today's tallest towers**: a leaderboard per subreddit, per day.
- **Days in a row**: come back tomorrow to keep your streak.
- **The community tower**: every hat anyone stacks today goes on one shared tower for the subreddit.
- **Share your run** as a comment: one square per hero, so others can compare without spoiling the score.

```
Gloop's Hat Tower #1 (Classic)
🎩 16 hats, best streak 5
🟩⬛🟩🌟🟩🟩🟩🟨🟨🟩
🟩🟨🟩🟨🟩
```

## Fair scores

The server never trusts a score from the browser. The game runs in fixed steps of 4 ms, so the
browser only sends the moments you tapped, and the server replays the whole run to get the score.

## For developers

Built on the official `devvit-template-bare` (Devvit Web, plain TypeScript and canvas, no framework).

- `src/shared/spel.ts`: game rules, shared by client and server.
- `src/client/`: the post in the feed (`splash.ts`) and the game (`game.ts`, `teken.ts`).
- `src/server/`: Devvit server; `logica.ts` holds the logic with a small storage interface, backed by Redis.
- `dev/local.ts`: runs the game locally without Reddit, with in-memory storage.

```
npm install
npm test             # types, lint, unit tests, build
npm run local        # http://localhost:5173/splash.html (PROEF=1 adds practice bots to the leaderboard)
npm run playtest     # on Reddit, after devvit login
```
