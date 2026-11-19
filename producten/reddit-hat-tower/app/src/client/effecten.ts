// Kleine bewegingen die het spel levend maken: veren (squash en stretch, wiebelen), deeltjes en schermschok.
// Alles loopt op de klok van het beeld (ms), los van de spelregels.

/** Een gedempte veer: duw hem met `stoot`, hij schiet door en komt tot rust. */
export class Veer {
  x = 0
  v = 0
  readonly stijf: number
  readonly demp: number
  constructor(stijf = 0.0009, demp = 0.012) {
    this.stijf = stijf
    this.demp = demp
  }
  stoot(snelheid: number): void {
    this.v += snelheid
  }
  stap(dtMs: number): number {
    // In kleine stukjes, zodat een trage frame de veer niet laat ontploffen.
    let rest = dtMs
    while (rest > 0) {
      const d = Math.min(rest, 8)
      const a = -this.stijf * this.x - this.demp * this.v
      this.v += a * d
      this.x += this.v * d
      rest -= d
    }
    return this.x
  }
}

export type Soort = 'slijm' | 'vonk' | 'goud' | 'stof'

type Deeltje = {
  soort: Soort
  x: number
  y: number
  vx: number
  vy: number
  leven: number
  duur: number
  r: number
}

export class Deeltjes {
  lijst: Deeltje[] = []

  strooi(soort: Soort, x: number, y: number, aantal: number, kracht = 1): void {
    for (let i = 0; i < aantal; i++) {
      const hoek =
        soort === 'stof'
          ? Math.PI *
            (Math.random() < 0.5
              ? 0.95 + Math.random() * 0.2
              : -0.15 + Math.random() * 0.2)
          : -Math.PI * (0.08 + 0.84 * Math.random())
      const v =
        (soort === 'stof' ? 0.05 : 0.18) +
        Math.random() * (soort === 'stof' ? 0.08 : 0.32) * kracht
      const duur = soort === 'stof' ? 420 : 520 + Math.random() * 260
      this.lijst.push({
        soort,
        x,
        y,
        vx: Math.cos(hoek) * v,
        vy: Math.sin(hoek) * v,
        leven: duur,
        duur,
        r:
          soort === 'slijm'
            ? 4 + Math.random() * 6
            : soort === 'stof'
              ? 8 + Math.random() * 8
              : 3 + Math.random() * 4,
      })
    }
  }

  teken(ctx: CanvasRenderingContext2D, dtMs: number): void {
    this.lijst = this.lijst.filter(d => d.leven > 0)
    for (const d of this.lijst) {
      d.leven -= dtMs
      d.x += d.vx * dtMs
      d.y += d.vy * dtMs
      if (d.soort !== 'stof') d.vy += 0.0011 * dtMs
      const a = Math.max(0, d.leven / d.duur)
      if (d.soort === 'slijm') {
        ctx.fillStyle = `rgba(120, 232, 184, ${0.9 * a})`
        ctx.beginPath()
        ctx.ellipse(
          d.x,
          d.y,
          d.r * (0.6 + 0.4 * a),
          d.r * (0.8 + 0.5 * (1 - a)),
          0,
          0,
          Math.PI * 2,
        )
        ctx.fill()
        ctx.fillStyle = `rgba(255, 255, 255, ${0.6 * a})`
        ctx.beginPath()
        ctx.arc(d.x - d.r * 0.3, d.y - d.r * 0.3, d.r * 0.25, 0, Math.PI * 2)
        ctx.fill()
      } else if (d.soort === 'stof') {
        ctx.fillStyle = `rgba(120, 72, 44, ${0.5 * a})`
        ctx.beginPath()
        ctx.arc(d.x, d.y, d.r * (1.6 - 0.6 * a), 0, Math.PI * 2)
        ctx.fill()
      } else {
        ctx.fillStyle =
          d.soort === 'goud'
            ? `rgba(255, 206, 64, ${a})`
            : `rgba(255, 250, 220, ${a})`
        const r = d.r * (0.5 + a)
        ctx.beginPath()
        ctx.moveTo(d.x, d.y - r * 1.7)
        ctx.lineTo(d.x + r * 0.5, d.y)
        ctx.lineTo(d.x, d.y + r * 1.7)
        ctx.lineTo(d.x - r * 0.5, d.y)
        ctx.closePath()
        ctx.fill()
      }
    }
  }
}

/** Korte schermschok bij een hap. Respecteert "minder beweging" van het systeem. */
export class Schok {
  #tot = 0
  #sterkte = 0
  readonly rustig =
    window.matchMedia?.('(prefers-reduced-motion: reduce)').matches ?? false

  geef(sterkte: number, nu: number): void {
    if (this.rustig) return
    this.#sterkte = sterkte
    this.#tot = nu + 160
  }

  verschuiving(nu: number): {x: number; y: number} {
    const rest = this.#tot - nu
    if (rest <= 0) return {x: 0, y: 0}
    const s = (this.#sterkte * rest) / 160
    return {x: (Math.random() * 2 - 1) * s, y: (Math.random() * 2 - 1) * s}
  }
}

export const veerUit = (t: number): number => 1 - (1 - t) ** 3
export const klem = (v: number, a: number, b: number): number =>
  Math.min(b, Math.max(a, v))
