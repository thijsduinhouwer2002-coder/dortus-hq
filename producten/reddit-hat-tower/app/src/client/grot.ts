// De grot achter het spel, de gezamenlijke toren van de subreddit en tekst met een rand.
import type {Kunst} from './kunst.ts'

const B = 454
const CX = B / 2

/** Stofjes in de lichtbaan: vaste plekken, ze zweven langzaam. */
const STOF = Array.from({length: 18}, (_, i) => ({
  t: (i * 0.618) % 1,
  d: ((i * 37) % 23) / 23 - 0.5,
  r: 1 + ((i * 13) % 5) / 3,
  v: 0.00002 + ((i * 7) % 5) * 0.000006,
}))

export function tekenGrot(
  ctx: CanvasRenderingContext2D,
  h: number,
  voet: number,
  mond: {x: number; y: number},
): void {
  const g = ctx.createRadialGradient(
    CX,
    voet - 120,
    30,
    CX,
    voet - 160,
    Math.max(h, B) * 0.9,
  )
  g.addColorStop(0, '#dc8d48')
  g.addColorStop(0.32, '#a85a2a')
  g.addColorStop(0.75, '#4a2212')
  g.addColorStop(1, '#24110a')
  ctx.fillStyle = g
  ctx.fillRect(-20, -20, B + 40, h + 40)

  // Druipstenen langs het plafond, donker tegen de gloed.
  ctx.fillStyle = 'rgba(30, 12, 6, 0.55)'
  ctx.beginPath()
  ctx.moveTo(-20, -20)
  const punten = [
    0, 22, 40, 70, 96, 130, 170, 214, 250, 290, 322, 356, 392, 420, 454,
  ]
  for (let i = 0; i < punten.length; i++) {
    const x = punten[i] as number
    const diep = 14 + ((i * 29) % 7) * 7 + (i % 3 === 0 ? 22 : 0)
    ctx.lineTo(x, i % 2 === 0 ? 8 : diep)
  }
  ctx.lineTo(B + 20, -20)
  ctx.closePath()
  ctx.fill()

  // De lichtbaan van linksboven naar de bek, zoals op het horloge.
  const lg = ctx.createLinearGradient(0, 0, mond.x, mond.y)
  lg.addColorStop(0, 'rgba(255, 214, 150, 0.40)')
  lg.addColorStop(1, 'rgba(255, 190, 120, 0.08)')
  ctx.fillStyle = lg
  ctx.beginPath()
  ctx.moveTo(-60, -40)
  ctx.lineTo(50, -40)
  ctx.lineTo(mond.x + 50, mond.y + 10)
  ctx.lineTo(mond.x - 50, mond.y + 10)
  ctx.closePath()
  ctx.fill()
  const nu = performance.now()
  for (const s of STOF) {
    const t = (s.t + nu * s.v) % 1
    const x = -5 + (mond.x + 5) * t + s.d * 70
    const y = -40 + (mond.y + 40) * t
    ctx.fillStyle = `rgba(255, 236, 200, ${0.5 * Math.sin(t * Math.PI)})`
    ctx.beginPath()
    ctx.arc(x, y, s.r, 0, Math.PI * 2)
    ctx.fill()
  }

  // Vloer.
  ctx.fillStyle = '#3b170c'
  ctx.beginPath()
  ctx.ellipse(CX, voet + 56, B * 0.64, 72, 0, Math.PI, 0)
  ctx.lineTo(B + 40, h + 40)
  ctx.lineTo(-40, h + 40)
  ctx.closePath()
  ctx.fill()
}

/**
 * De gezamenlijke toren van de subreddit, achterin rechts en verder weg (kleiner, doffer).
 * Een hoed per hoed van vandaag, tot hij boven de grot uitkomt; het bordje noemt het echte aantal.
 */
export function tekenSamen(
  ctx: CanvasRenderingContext2D,
  k: Kunst,
  voet: number,
  aantal: number,
  sub: string,
  volgorde: readonly number[],
  bordje: boolean,
): void {
  const schaal = 0.42
  let y = voet - 34
  const zichtbaar = Math.min(aantal, 160)
  const nu = performance.now()
  ctx.save()
  ctx.globalAlpha = 0.5
  ctx.filter = 'brightness(0.72) saturate(0.8)'
  let x = 404
  for (let i = 0; i < zichtbaar && y > -40; i++) {
    const nr = volgorde[(i * 3) % 10] as number
    const m = k.maten.hoed[nr] as {b: number; h: number}
    // Een wankele toren: hij buigt langzaam heen en weer, en wiebelt een beetje.
    x = 404 + Math.sin(i * 0.11) * 14 + Math.sin(nu / 900 + i * 0.05) * i * 0.04
    ctx.drawImage(
      k.hoed[nr] as HTMLImageElement,
      x - (m.b * schaal) / 2,
      y - m.h * schaal * 0.8,
      m.b * schaal,
      m.h * schaal,
    )
    y -= m.h * schaal * 0.56
  }
  ctx.restore()
  if (!bordje) return
  // Bordje bovenop (of bovenin als de toren hoger is dan de grot).
  const bordY = Math.max(22, y - 40)
  tekst(ctx, `r/${sub}`, B - 8, bordY, 16, 'right', '#fff6e6')
  tekst(
    ctx,
    `${aantal.toLocaleString('en-US')} hats today`,
    B - 8,
    bordY + 18,
    13,
    'right',
    '#ffe08a',
  )
}

/** Tekst met een donkere rand, zoals "GULP!" op het horloge. y is de bovenkant. */
export function tekst(
  ctx: CanvasRenderingContext2D,
  s: string,
  x: number,
  y: number,
  grootte: number,
  uitlijn: CanvasTextAlign,
  kleur: string,
): void {
  ctx.font = `${grootte}px "Lilita One", sans-serif`
  ctx.textAlign = uitlijn
  ctx.textBaseline = 'top'
  ctx.lineJoin = 'round'
  ctx.lineWidth = Math.max(4, grootte * 0.18)
  ctx.strokeStyle = '#2b1206'
  ctx.strokeText(s, x, y)
  ctx.fillStyle = kleur
  ctx.fillText(s, x, y)
}
