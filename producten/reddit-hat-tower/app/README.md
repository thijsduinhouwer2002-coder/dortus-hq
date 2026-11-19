# Gloop's Hat Tower

A one-button daily stacking game for Reddit. A hero drops into the cave. Tap when he reaches
Gloop's mouth: GULP, his hat flies onto the tower on Gloop's head. You have 30 seconds.

Every day there is one new tower for everyone, and every subreddit stacks one shared tower together.

## How to play

- Tap anywhere (or press Space) when the hero is at Gloop's mouth. A yellow `!` shows the moment.
- A normal gulp stacks 1 hat. Hit the middle of the mouth for a **perfect** gulp: 2 hats, and a
  streak of perfects stacks more (3, then 4 per gulp).
- Every catch makes the next hero fall a little faster.
- Missing never costs a hat. The hero lands, walks off ("bye!") and the next one falls a bit slower.
- Tapping too early makes Gloop snap at the air: his mouth stays shut for a moment and your streak
  ends. Tapping blindly never pays off.
- Golden heroes give 2 extra hats.

## Every day

- **One tower per day, the same for everyone.** Every player gets the same heroes in the same rhythm,
  with the same golden heroes. Your first run of the day counts from the moment you press Play;
  reloading does not give a new run. Practice as much as you like.
- **A daily rule** changes how the tower plays: Classic, Rush Hour, Heavy Heroes, Golden Hour or Big Mouth.
- **Today's tallest towers**: a leaderboard per subreddit, per day.
- **Days in a row**: come back tomorrow to keep your streak.
- **The community tower**: every hat anyone stacks today goes on one shared tower for the subreddit.
  It stands at the back of the cave while you play, and your hats join it live.
- **Share your run** as a comment: one square per hero, so others can compare. You see the comment
  before it is posted.
- **Join the subreddit** from the result screen to get tomorrow's tower.

```
Gloop's Hat Tower #1 (Classic)
🎩 16 hats, best streak 5
🟩⬛🟩🌟🟩🟩🟩🟨🟨🟩
🟩🟨🟩🟨🟩
```

## For moderators

- **Install** the app on your subreddit from its app page. On install it posts today's tower.
- **A new tower every day:** the app posts "Gloop's Hat Tower #N: rule" at 00:00 UTC by itself.
- **Post a tower by hand:** subreddit menu, "Gloop's Hat Tower: new daily post".
- **What it stores** (Redis, per subreddit): today's leaderboard and community tower (kept 40 days),
  and per player their best tower and days in a row. Nothing leaves Reddit.
- **On behalf of players**, and only after they tap the button: posting their result as a comment,
  and joining the subreddit.

## Fair scores

The server never trusts a score from the browser. The game runs in fixed steps of 4 ms, so the
browser only sends the moments you tapped, and the server replays the whole run to get the score.
A run is claimed at the start, and a second submission of the same run never counts twice.

## For developers

Built on the official `devvit-template-bare` (Devvit Web, plain TypeScript and canvas, no framework).

- `src/shared/spel.ts`: game rules, shared by client and server.
- `src/client/`: the post in the feed (`splash.ts`), the game (`game.ts`), drawing and motion
  (`scene.ts`, `held.ts`, `grot.ts`, `effecten.ts`) and the result screen (`uitslag.ts`).
- `public/kunst/`: renders of Gloop, the hero and the ten hats.
- `src/server/`: Devvit server; `logica.ts` holds the logic with a small storage interface, backed by Redis.
- `dev/local.ts`: runs the game locally without Reddit, with in-memory storage.

```
npm install
npm test             # types, lint, unit tests, build
npm run local        # http://localhost:5173/splash.html (PROEF=1 adds practice bots to the leaderboard)
npm run playtest     # on Reddit, after devvit login
```
