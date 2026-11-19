// De held: valt in een boog en tuimelt met de hoed die hij straks kwijt is, gaat de mond in, of landt
// naast Gloop en hupt weg. Elke held komt anders binnen (kant, boog, draaiing, soort), vast per dag en
// heldnummer via heldStijl, dus iedereen ziet dezelfde toren.
import {
  type HeldStijl,
  heldStijl,
  inVangzone,
  isGoud,
  type Potje,
  Toestand,
  WEG_MS,
} from '../shared/spel.ts'
import {B, Basis, type Beeld} from './basis.ts'
import {klem} from './effecten.ts'
import * as geluid from './geluid.ts'
import {tekst} from './grot.ts'
import type {HeldBeelden, HeldMaten} from './kunst.ts'

type Plek = {x: number; y: number; hoek: number; t: number}

/** Waar de stuiterende held de wand raakt (deel van de val). */
const STUIT = 0.42

export class MetHeld extends Basis {
  stijl(p: Potje): HeldStijl {
    return heldStijl(p.dag, p.held)
  }

  heldPlek(p: Potje): Plek {
    return this.boog(p.y / 815, this.mond(), this.stijl(p))
  }

  /** Startplek van een held (voor de lichtbaan). */
  beginX(stijl: HeldStijl): number {
    return this.boog(0, this.mond(), stijl).x
  }

  /**
   * De valboog. Alle bogen eindigen op t = 1 precies in de mond, zodat de hap altijd op hetzelfde
   * moment valt; alleen de weg ernaartoe verschilt. Ze komen op het laatst van opzij de mond in,
   * nooit dwars door de toren.
   */
  boog(t: number, m: {x: number; y: number}, stijl: HeldStijl): Plek {
    // Voorbij de mond (laat in de vangzone, of gemist) gaat hij rustig door in dezelfde richting.
    if (t > 1) {
      const p1 = this.boog(1, m, stijl)
      const p0 = this.boog(0.97, m, stijl)
      const k = ((t - 1) / 0.03) * 0.5
      return {
        x: p1.x + (p1.x - p0.x) * k,
        y: p1.y + (p1.y - p0.y) * k,
        hoek: p1.hoek,
        t,
      }
    }
    const tt = Math.max(0, t)
    const eind = Math.PI * 1.03
    // Draaiing: rond t = 1 hangt hij met zijn hoofd naar de mond; ervoor tuimelt hij `draai` keer.
    const hoek =
      eind -
      stijl.draai * Math.PI * 2 * (1 - tt) * (stijl.kant === 'boven' ? 1.5 : 1)
    const omlaag = (y0: number, k = 0.55) =>
      y0 + (m.y - y0) * (k * tt + (1 - k) * tt * tt)
    switch (stijl.kant) {
      case 'rechts': {
        const x = B - 30 + (m.x + 6 - (B - 30)) * tt ** 2.1
        return {x, y: omlaag(40), hoek: -hoek, t}
      }
      case 'boven': {
        // Valt van bovenin bijna recht omlaag langs de linkerkant van de toren en haakt dan de mond in.
        const x = 70 + (m.x - 6 - 70) * tt ** 5
        return {x, y: -70 + (m.y + 70) * tt ** 1.45, hoek, t}
      }
      case 'stuiterL':
      case 'stuiterR': {
        // Vliegt eerst schuin naar de andere wand, stuitert ertegen en komt dan van die kant de mond in.
        const links = stijl.kant === 'stuiterL'
        const van = links ? 24 : B - 24
        const wand = links ? B - 18 : 18
        const yWand = 70 + (m.y - 70) * 0.38
        if (tt < STUIT) {
          const u = tt / STUIT
          return {
            x: van + (wand - van) * u,
            y: 50 + (yWand - 50) * u ** 1.3,
            hoek: links ? hoek : -hoek,
            t,
          }
        }
        const u = (tt - STUIT) / (1 - STUIT)
        const doel = m.x + (links ? 6 : -6)
        const x = wand + (doel - wand) * u ** 1.7
        const y =
          yWand +
          (m.y - yWand) * (0.35 * u + 0.65 * u * u) -
          60 * Math.sin(u * Math.PI) * (1 - u)
        return {x, y, hoek: links ? -hoek : hoek, t}
      }
      default: {
        const x = 30 + (m.x - 6 - 30) * tt ** 2.1
        return {x, y: omlaag(40), hoek, t}
      }
    }
  }

  beelden(p: Potje): {img: HeldBeelden; maat: HeldMaten} {
    const s = this.stijl(p).soort
    return {
      img: this.k.helden[s] ?? (this.k.helden[0] as HeldBeelden),
      maat: this.k.maten.helden[s] ?? (this.k.maten.helden[0] as HeldMaten),
    }
  }

  tekenHeld(
    p: Potje,
    beeld: Beeld,
    nu: number,
    volgorde: readonly number[],
  ): void {
    const {ctx} = this
    const hoedNr = volgorde[
      (beeld.toren + beeld.vluchten.length) % 10
    ] as number
    const {img, maat} = this.beelden(p)
    const stijl = this.stijl(p)
    if (p.toestand === Toestand.Valt) {
      const {x, y, hoek, t} = this.heldPlek(p)
      // Stuiter tegen de wand: stof en een klank, één keer per held.
      if (
        (stijl.kant === 'stuiterL' || stijl.kant === 'stuiterR') &&
        t >= STUIT &&
        beeld.stuiterHeld !== p.held
      ) {
        beeld.stuiterHeld = p.held
        beeld.deeltjes.strooi('stof', x, y, 5)
        geluid.boing()
      }
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
      this.tekenHeldMetHoed(img.schrik, maat.schrik, hoedNr, 0, 0)
      ctx.restore()
      if (inVangzone(p) && p.hapDicht === 0) {
        const links = x < this.mond().x
        tekst(ctx, '!', x + (links ? -52 : 52), y - 70, 50, 'center', '#ffe94a')
      }
    } else if (
      p.toestand === Toestand.Slok ||
      (nu - beeld.slokSinds < 260 && p.toestand === Toestand.Wacht)
    ) {
      this.tekenSlok(img.schrik, maat.schrik, beeld, nu)
    } else if (p.toestand === Toestand.Weg) {
      this.tekenWeg(p, beeld, img, maat, stijl)
    }
  }

  /** Gemist: hij valt door, landt naast Gloop (squash en stof) en hupt weg naar de kant waar hij vandaan kwam. */
  tekenWeg(
    p: Potje,
    beeld: Beeld,
    img: HeldBeelden,
    maat: HeldMaten,
    stijl: HeldStijl,
  ): void {
    const {ctx} = this
    const f = p.fase / WEG_MS
    const s = maat.schrik
    const van = this.boog(900 / 815, this.mond(), stijl)
    const rechts = van.x > this.mond().x
    const landX = this.mond().x + (rechts ? 120 : -120)
    if (f < 0.16) {
      const k = f / 0.16
      const x = van.x + (landX - van.x) * k
      const y = van.y + (this.voet - s.h * 0.5 - van.y) * k * k
      ctx.save()
      ctx.translate(x, y)
      ctx.rotate(
        van.hoek + (Math.PI * 2 * Math.sign(van.hoek || 1) - van.hoek) * k,
      )
      ctx.drawImage(img.schrik, -s.b / 2, -s.h / 2, s.b, s.h)
      ctx.restore()
    } else if (f < 0.32) {
      const k = (f - 0.16) / 0.16
      const squash = Math.sin(k * Math.PI) * 0.28
      ctx.save()
      ctx.translate(landX, this.voet)
      ctx.scale(1 + squash, 1 - squash)
      ctx.drawImage(img.schrik, -s.b / 2, -s.h, s.b, s.h)
      ctx.restore()
      if (k < 0.2) beeld.deeltjes.strooi('stof', landX, this.voet - 4, 2)
    } else {
      const k = (f - 0.32) / 0.68
      const doel = rechts ? B + s.b : -s.b
      const x = landX + (doel - landX) * k
      const hup = Math.abs(Math.sin(k * Math.PI * 4)) * 18
      const even = Math.floor(k * 8) % 2 === 0
      const st = even ? maat.stap1 : maat.stap2
      ctx.save()
      ctx.translate(x, this.voet - hup)
      ctx.scale(rechts ? 1 : -1, 1)
      ctx.drawImage(even ? img.stap1 : img.stap2, -st.b / 2, -st.h, st.b, st.h)
      ctx.restore()
    }
  }

  /** De held zonder hoed, met de hoed van de toren op zijn hoofd; (x, y) is de kruin. */
  tekenHeldMetHoed(
    img: HTMLImageElement,
    s: {b: number; h: number; kruin: [number, number]},
    hoedNr: number | null,
    x: number,
    y: number,
  ): void {
    this.ctx.drawImage(img, x - s.kruin[0], y - s.kruin[1], s.b, s.h)
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
  tekenSlok(
    img: HTMLImageElement,
    s: {b: number; h: number; kruin: [number, number]},
    beeld: Beeld,
    nu: number,
  ): void {
    const {ctx} = this
    const m = this.mond()
    const g = this.k.maten.gloop
    const f = klem((nu - beeld.slokSinds) / 240, 0, 1)
    if (f >= 1) return
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
    this.tekenHeldMetHoed(img, s, null, 0, 0)
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
