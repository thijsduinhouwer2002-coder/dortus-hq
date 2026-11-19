// De held: valt in een boog en tuimelt met de hoed die hij straks kwijt is, gaat de mond in, of landt
// naast Gloop en hupt weg.
import {
  inVangzone,
  isGoud,
  type Potje,
  Toestand,
  WEG_MS,
} from '../shared/spel.ts'
import {B, Basis, type Beeld} from './basis.ts'
import {klem} from './effecten.ts'
import {tekst} from './grot.ts'

export class MetHeld extends Basis {
  /** De held valt in een boog en tuimelt, met de hoed die hij straks kwijt is op zijn hoofd. */
  heldPlek(p: Potje): {x: number; y: number; hoek: number; t: number} {
    const m = this.mond()
    return this.boog(p.y / 815, m)
  }

  /** De valboog: eerst vooral omlaag langs de lichtbaan, op het laatst opzij de mond in (niet door de toren). */
  boog(
    t: number,
    m: {x: number; y: number},
  ): {x: number; y: number; hoek: number; t: number} {
    const sx = 30
    const sy = 40
    const tx = Math.max(0, t) ** 2.1
    const x = sx + (m.x - 6 - sx) * tx
    const y = sy + (m.y - sy) * (0.55 * t + 0.45 * t * t)
    return {x, y, hoek: Math.PI * (0.15 + 0.88 * t), t}
  }

  tekenHeld(
    p: Potje,
    beeld: Beeld,
    nu: number,
    volgorde: readonly number[],
  ): void {
    const {ctx} = this
    const mh = this.k.maten.held
    const hoedNr = volgorde[
      (beeld.toren + beeld.vluchten.length) % 10
    ] as number
    if (p.toestand === Toestand.Valt) {
      const {x, y, hoek, t} = this.heldPlek(p)
      if (isGoud(p)) {
        const g = ctx.createRadialGradient(x, y, 6, x, y, 95)
        g.addColorStop(0, 'rgba(255, 220, 90, 0.8)')
        g.addColorStop(1, 'rgba(255, 200, 60, 0)')
        ctx.fillStyle = g
        ctx.fillRect(x - 95, y - 95, 190, 190)
      }
      const rek = 0.06 * t
      ctx.save()
      ctx.translate(x, y)
      ctx.rotate(hoek + Math.sin(nu / 110) * 0.06)
      ctx.scale(1 - rek, 1 + rek)
      // Draaipunt is de kruin van het hoofd: daar zit de hoed, en daarmee gaat hij de mond in.
      this.tekenHeldMetHoed('schrik', hoedNr, 0, 0)
      ctx.restore()
      if (inVangzone(p) && p.hapDicht === 0)
        tekst(ctx, '!', x - 52, y - 70, 50, 'center', '#ffe94a')
    } else if (
      p.toestand === Toestand.Slok ||
      (nu - beeld.slokSinds < 260 && p.toestand === Toestand.Wacht)
    ) {
      this.tekenSlok(beeld, nu)
    } else if (p.toestand === Toestand.Weg) {
      // Gemist: hij landt naast Gloop (squash), en hupt dan weg naar links.
      const f = p.fase / WEG_MS
      const s = mh.schrik
      const landX = this.mond().x - 120
      if (f < 0.16) {
        // Eerst valt hij verder, langs de mond, naar de vloer; hij draait weer rechtop.
        const k = f / 0.16
        const van = this.boog(900 / 815, this.mond())
        const x = van.x + (landX - van.x) * k
        const y = van.y + (this.voet - s.h * 0.5 - van.y) * k * k
        ctx.save()
        ctx.translate(x, y)
        ctx.rotate(van.hoek + (Math.PI * 2 - van.hoek) * k)
        ctx.drawImage(this.k.held.schrik, -s.b / 2, -s.h / 2, s.b, s.h)
        ctx.restore()
      } else if (f < 0.32) {
        const k = (f - 0.16) / 0.16
        const squash = Math.sin(k * Math.PI) * 0.28
        ctx.save()
        ctx.translate(landX, this.voet)
        ctx.scale(1 + squash, 1 - squash)
        ctx.drawImage(this.k.held.schrik, -s.b / 2, -s.h, s.b, s.h)
        ctx.restore()
        if (k < 0.2) beeld.deeltjes.strooi('stof', landX, this.voet - 4, 2)
      } else {
        const k = (f - 0.32) / 0.68
        const x = landX - (landX + s.b) * k
        const hup = Math.abs(Math.sin(k * Math.PI * 4)) * 18
        const img =
          Math.floor(k * 8) % 2 === 0 ? this.k.held.stap1 : this.k.held.stap2
        const st = Math.floor(k * 8) % 2 === 0 ? mh.stap1 : mh.stap2
        ctx.save()
        ctx.translate(x, this.voet - hup)
        ctx.scale(-1, 1)
        ctx.drawImage(img, -st.b / 2, -st.h, st.b, st.h)
        ctx.restore()
      }
    }
  }

  /** De held zonder hoed, met de hoed van de toren op zijn hoofd; (x, y) is de kruin. */
  tekenHeldMetHoed(
    stand: 'schrik',
    hoedNr: number | null,
    x: number,
    y: number,
  ): void {
    const s = this.k.maten.held[stand]
    this.ctx.drawImage(
      this.k.held[stand],
      x - s.kruin[0],
      y - s.kruin[1],
      s.b,
      s.h,
    )
    if (hoedNr === null) return
    const m = this.k.maten.hoed[hoedNr] as {b: number; h: number}
    const hb = m.b * 0.62
    const hh = m.h * 0.62
    this.ctx.drawImage(
      this.k.hoed[hoedNr] as HTMLImageElement,
      x - hb / 2,
      y - hh * 0.8,
      hb,
      hh,
    )
  }

  /** Slok: de held gaat ondersteboven de mond in en verdwijnt; alleen wat boven of in de mond is, is te zien. */
  tekenSlok(beeld: Beeld, nu: number): void {
    const {ctx} = this
    const m = this.mond()
    const g = this.k.maten.gloop
    const f = klem((nu - beeld.slokSinds) / 240, 0, 1)
    if (f >= 1) return
    const s = this.k.maten.held.schrik
    ctx.save()
    ctx.beginPath()
    ctx.rect(-200, -2000, B + 400, m.y + 2000)
    ctx.ellipse(m.x, m.y, g.mond[2] * 1.15, g.mond[3] * 1.3, 0, 0, Math.PI * 2)
    ctx.clip()
    const zak = f * s.h * 1.05
    const k = 1 - 0.25 * f
    ctx.translate(m.x, m.y + zak)
    ctx.rotate(Math.PI + Math.sin(f * 9) * 0.08)
    ctx.scale(k * (1 + 0.15 * f), k)
    this.tekenHeldMetHoed('schrik', null, 0, 0)
    ctx.restore()
  }

  /** Gouden gloed achter Gloop als er een gouden held aankomt. */
  tekenHeldAchter(p: Potje, _beeld: Beeld, nu: number): void {
    if (p.toestand !== Toestand.Valt || !isGoud(p)) return
    const m = this.mond()
    const a = 0.12 + 0.06 * Math.sin(nu / 120)
    this.ctx.fillStyle = `rgba(255, 210, 80, ${a})`
    this.ctx.beginPath()
    this.ctx.ellipse(m.x + 20, m.y, 130, 90, 0, 0, Math.PI * 2)
    this.ctx.fill()
  }
}
