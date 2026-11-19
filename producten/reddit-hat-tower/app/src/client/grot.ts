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

let grotCache: {sleutel: string; doek: HTMLCanvasElement} | undefined

export function tekenGrot(
  ctx: CanvasRenderingContext2D,
  h: number,
  voet: number,
  mond: {x: number; y: number},
): void {
  // Wand, druipstenen en vloer veranderen niet: één keer tekenen, daarna alleen kopiëren.
  const px = ctx.getTransform().a
  const sleutel = `${h}|${px}`
  if (grotCache?.sleutel !== sleutel) {
    const doek = document.createElement('canvas')
    doek.width = Math.ceil((B + 40) * px)
    doek.height = Math.ceil((h + 40) * px)
    const c = doek.getContext('2d') as CanvasRenderingContext2D
    c.scale(px, px)
    c.translate(20, 20)
    tekenWand(c, h, voet)
    grotCache = {sleutel, doek}
  }
  ctx.drawImage(grotCache.doek, -20, -20, B + 40, h + 40)
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
}

function tekenWand(
  ctx: CanvasRenderingContext2D,
  h: number,
  voet: number,
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
/** Waar de gezamenlijke toren staat (midden), binnen beeld ook op een telefoon. */
export const SAMEN_X = 392

/** De bovenkant van de gezamenlijke toren zoals hij nu getekend is. */
export function samenTop(): number {
  return samenCache?.top ?? 200
}

let samenCache:
  | {sleutel: string; doek: HTMLCanvasElement; top: number}
  | undefined

export function tekenSamen(
  ctx: CanvasRenderingContext2D,
  k: Kunst,
  voet: number,
  aantal: number,
  sub: string,
  volgorde: readonly number[],
  bordje: boolean,
): void {
  // Eén keer tekenen in een los doek en dat hergebruiken: 100+ hoeden met een filter elke frame is te zwaar.
  const px = ctx.getTransform().a
  const sleutel = `${aantal}|${voet}|${px}|${volgorde.join('')}`
  if (samenCache?.sleutel !== sleutel)
    samenCache = {sleutel, ...bouwSamen(k, voet, aantal, volgorde, px)}
  const nu = performance.now()
  ctx.save()
  // De hele toren wiegt heel langzaam, alsof hij net niet omvalt.
  ctx.translate(SAMEN_X, voet)
  ctx.rotate(Math.sin(nu / 1400) * 0.012)
  ctx.globalAlpha = bordje ? 0.55 : 0.3
  ctx.drawImage(samenCache.doek, -60, -voet - 40, 120, voet + 40)
  ctx.restore()
  if (!bordje) return
  // Bordje bovenop (of bovenin als de toren hoger is dan de grot).
  const bordY = Math.max(22, samenCache.top - 40)
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

function bouwSamen(
  k: Kunst,
  voet: number,
  aantal: number,
  volgorde: readonly number[],
  px: number,
): {doek: HTMLCanvasElement; top: number} {
  const doek = document.createElement('canvas')
  doek.width = Math.ceil(120 * px)
  doek.height = Math.ceil((voet + 40) * px)
  const c = doek.getContext('2d') as CanvasRenderingContext2D
  c.scale(px, px)
  c.translate(60, voet + 40)
  c.filter = 'brightness(0.72) saturate(0.8)'
  const schaal = 0.42
  // De voet staat op de vloer (de vloer loopt hier al iets omhoog).
  let y = -2
  for (let i = 0; i < Math.min(aantal, 160) && y > -voet - 40; i++) {
    const nr = volgorde[(i * 3) % 10] as number
    const m = k.maten.hoed[nr] as {b: number; h: number}
    // Een wankele toren: hij buigt langzaam heen en weer.
    const x = Math.sin(i * 0.11) * 14 + (((i * 5) % 7) - 3) * 0.6
    c.drawImage(
      k.hoed[nr] as HTMLImageElement,
      x - (m.b * schaal) / 2,
      y - m.h * schaal * 0.8,
      m.b * schaal,
      m.h * schaal,
    )
    y -= m.h * schaal * 0.56
  }
  return {doek, top: voet + y}
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
