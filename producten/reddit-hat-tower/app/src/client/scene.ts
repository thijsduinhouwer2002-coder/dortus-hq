// Het speelveld: grot, gezamenlijke toren, Gloop, de vallende held en de hoedentoren.
// De spelregels komen uit shared/spel.ts; hier zit alleen hoe het eruitziet en beweegt.
// Eenheden: de breedte is altijd 454 (zoals op het horloge), de hoogte volgt het scherm.
import {
  inVangzone,
  isGoud,
  type Potje,
  Toestand,
  WEG_MS,
} from '../shared/spel.ts'
import {Deeltjes, klem, Schok, Veer, veerUit} from './effecten.ts'
import {tekenGrot, tekenSamen, tekst} from './grot.ts'
import type {GloopStand, Kunst} from './kunst.ts'

export const B = 454
const CX = B / 2

type Vlucht = {
  hoed: number
  vanX: number
  vanY: number
  start: number
  duur: number
  plek: number
}

/** Alles wat het beeld onthoudt tussen frames (veren, timers, deeltjes). */
export type Beeld = {
  zoom: number
  voetPlek: number
  opzij: number
  gloopVeer: Veer
  torenVeer: Veer
  deeltjes: Deeltjes
  schok: Schok
  vluchten: Vlucht[]
  /** Hoeden die echt op de toren staan (de rest vliegt nog). */
  toren: number
  landMs: number
  slokSinds: number
  misSinds: number
  luchtSinds: number
  blijTot: number
  knipperTot: number
  volgendeKnipper: number
  kreet: string
  kreetSub: string
  kreetSinds: number
  /** Hoeden van de subreddit vandaag (zonder deze ronde). */
  samen: number
  sub: string
  /** Bordje bij de gezamenlijke toren (uit achter het start- en uitslagscherm). */
  bordje: boolean
}

export function nieuwBeeld(): Beeld {
  return {
    zoom: 1,
    voetPlek: 1,
    opzij: 0,
    gloopVeer: new Veer(0.0011, 0.011),
    torenVeer: new Veer(0.0006, 0.004),
    deeltjes: new Deeltjes(),
    schok: new Schok(),
    vluchten: [],
    toren: 0,
    landMs: -9999,
    slokSinds: -9999,
    misSinds: -9999,
    luchtSinds: -9999,
    blijTot: 0,
    knipperTot: 0,
    volgendeKnipper: 2500,
    kreet: '',
    kreetSub: '',
    kreetSinds: -9999,
    samen: 0,
    sub: '',
    bordje: true,
  }
}

export class Scene {
  readonly ctx: CanvasRenderingContext2D
  h = 800
  schaal = 1

  readonly canvas: HTMLCanvasElement
  readonly k: Kunst

  constructor(canvas: HTMLCanvasElement, k: Kunst) {
    this.canvas = canvas
    this.k = k
    const ctx = canvas.getContext('2d')
    if (!ctx) throw new Error('geen canvas')
    this.ctx = ctx
  }

  pasAan(): void {
    const r = this.canvas.getBoundingClientRect()
    const dpr = Math.min(window.devicePixelRatio || 1, 3)
    this.canvas.width = Math.round(r.width * dpr)
    this.canvas.height = Math.round(r.height * dpr)
    this.schaal = this.canvas.width / B
    this.h = this.canvas.height / this.schaal
  }

  get voet(): number {
    return this.h - 46
  }

  /** Waar de mond van Gloop staat (midden), in spel-eenheden. */
  mond(): {x: number; y: number} {
    const g = this.k.maten.gloop
    return {x: CX - g.b / 2 + g.mond[0], y: this.voet - g.h + g.mond[1]}
  }

  /** De plek van hoed i in de toren (onderkant), vanaf de kruin. */
  hoedPlekken(n: number, volgorde: readonly number[]): number[] {
    const g = this.k.maten.gloop
    let y = this.voet - g.h + g.kruin[1] + 8
    const uit: number[] = []
    for (let i = 0; i < n; i++) {
      const m = this.k.maten.hoed[volgorde[i % 10] as number] as {h: number}
      uit.push(y)
      y -= m.h * 0.56
    }
    uit.push(y)
    return uit
  }

  torenTop(n: number, volgorde: readonly number[]): number {
    const p = this.hoedPlekken(n, volgorde)
    return (p[p.length - 1] as number) - 30
  }

  /** De spelregels melden iets: start de bijpassende beweging. */
  gebeurtenis(
    soort: string,
    p: Potje,
    beeld: Beeld,
    volgorde: readonly number[],
    nu: number,
  ): void {
    const m = this.mond()
    if (soort === 'raak' || soort === 'hap') {
      const goud = p.uitslagen[p.uitslagen.length - 1] === 'gold'
      beeld.slokSinds = nu
      beeld.gloopVeer.stoot(goud ? 0.0055 : soort === 'raak' ? 0.0045 : 0.003)
      beeld.schok.geef(goud ? 9 : soort === 'raak' ? 6 : 3, nu)
      beeld.deeltjes.strooi('slijm', m.x, m.y, soort === 'raak' ? 10 : 6)
      if (soort === 'raak') beeld.deeltjes.strooi('vonk', m.x, m.y - 10, 8)
      if (goud) beeld.deeltjes.strooi('goud', m.x, m.y - 10, 16, 1.4)
      if (soort === 'raak' || goud) beeld.blijTot = nu + 650
      // De hoeden die deze slok oplevert, vliegen een voor een van het hoofd van de held naar de toren.
      const al = beeld.toren + beeld.vluchten.length
      for (let i = 0; i < p.winst; i++) {
        beeld.vluchten.push({
          hoed: volgorde[(al + i) % 10] as number,
          vanX: m.x - 10,
          vanY: m.y - 30,
          start: nu + i * 90,
          duur: 430,
          plek: al + i,
        })
      }
      beeld.kreet = goud ? 'GOLDEN!' : soort === 'raak' ? 'PERFECT!' : 'GULP!'
      beeld.kreetSub =
        p.winst > 1
          ? `+${p.winst} hats${p.reeks > 1 ? `, streak ${p.reeks}` : ''}`
          : '+1 hat'
      beeld.kreetSinds = nu
    } else if (soort === 'mis') {
      beeld.misSinds = nu
    } else if (soort === 'lucht') {
      beeld.luchtSinds = nu
      beeld.gloopVeer.stoot(-0.0018)
    }
  }

  teken(
    p: Potje,
    beeld: Beeld,
    volgorde: readonly number[],
    dt: number,
    nu: number,
  ): void {
    const {ctx} = this
    ctx.setTransform(this.schaal, 0, 0, this.schaal, 0, 0)
    ctx.imageSmoothingQuality = 'high'
    const s = beeld.schok.verschuiving(nu)
    ctx.translate(s.x, s.y)
    tekenGrot(ctx, this.h, this.voet, this.mond())

    // Gezamenlijke toren achterin: de hoeden van de hele subreddit vandaag, plus die van deze ronde.
    if (beeld.sub)
      tekenSamen(
        ctx,
        this.k,
        this.voet,
        beeld.samen + beeld.toren,
        beeld.sub,
        volgorde,
        beeld.bordje,
      )

    const voet = this.voet
    const doelVoet = beeld.voetPlek * this.h - (beeld.voetPlek < 1 ? 0 : 46)
    ctx.save()
    ctx.translate(CX + beeld.opzij, doelVoet)
    ctx.scale(beeld.zoom, beeld.zoom)
    ctx.translate(-CX, -voet)

    this.landHoeden(beeld, nu)
    const squash = beeld.gloopVeer.stap(dt)
    const sway = beeld.torenVeer.stap(dt)
    const adem = Math.sin(nu / 420) * 0.018
    const wacht =
      p.toestand === Toestand.Valt && p.y > 520 && p.hapDicht === 0
        ? klem((p.y - 520) / 300, 0, 1)
        : 0
    const sy = 1 - squash + adem + wacht * 0.05
    const sx = 1 + squash * 0.9 - adem * 0.6 - wacht * 0.02
    const kanteling =
      nu - beeld.misSinds < 520
        ? Math.sin((nu - beeld.misSinds) / 40) *
          0.07 *
          (1 - (nu - beeld.misSinds) / 520)
        : 0
    this.tekenHeldAchter(p, beeld, nu)
    const kruin = this.tekenGloop(p, beeld, nu, sx, sy, kanteling)
    this.tekenToren(beeld, volgorde, kruin, sway, nu)
    this.tekenHeld(p, beeld, nu, volgorde)
    this.tekenVluchten(beeld, kruin, volgorde, nu)
    beeld.deeltjes.teken(ctx, dt)
    ctx.restore()

    if (p.toestand !== Toestand.Klaar && p.toestand !== Toestand.Einde) {
      this.tekenTijd(p)
      this.tekenTeller(p)
      this.tekenKreet(beeld, nu)
      if (p.toestand === Toestand.Weg)
        tekst(ctx, 'bye!', 30, voet - 190, 30, 'left', '#fff6e6')
    }
  }

  gloopStand(p: Potje, beeld: Beeld, nu: number): GloopStand {
    if (p.toestand === Toestand.Slok || nu - beeld.slokSinds < 200) return 'hap'
    if (nu - beeld.luchtSinds < 150 || nu - beeld.misSinds < 450) return 'kneep'
    if (p.toestand === Toestand.Valt && inVangzone(p) && p.hapDicht === 0)
      return 'hap'
    if (p.toestand === Toestand.Einde || nu < beeld.blijTot) return 'blij'
    if (nu > beeld.volgendeKnipper) {
      beeld.knipperTot = nu + 120
      beeld.volgendeKnipper = nu + 2200 + Math.random() * 2600
    }
    return nu < beeld.knipperTot ? 'knipper' : 'rust'
  }

  /** Tekent Gloop met squash en stretch rond zijn voet; geeft de plek van zijn kruin terug. */
  tekenGloop(
    p: Potje,
    beeld: Beeld,
    nu: number,
    sx: number,
    sy: number,
    kanteling: number,
  ): {x: number; y: number} {
    const {ctx} = this
    const g = this.k.maten.gloop
    const img = this.k.gloop[this.gloopStand(p, beeld, nu)]
    ctx.save()
    ctx.translate(CX, this.voet)
    ctx.rotate(kanteling)
    ctx.scale(sx, sy)
    // Zachte schaduw onder Gloop.
    ctx.fillStyle = 'rgba(20, 8, 4, 0.35)'
    ctx.beginPath()
    ctx.ellipse(0, -4, g.b * 0.46, 10, 0, 0, Math.PI * 2)
    ctx.fill()
    ctx.drawImage(img, -g.b / 2, -g.h, g.b, g.h)
    ctx.restore()
    return {
      x: CX + (-g.b / 2 + g.kruin[0]) * sx + kanteling * g.h * 0.6,
      y: this.voet - (g.h - g.kruin[1] - 8) * sy,
    }
  }

  tekenToren(
    beeld: Beeld,
    volgorde: readonly number[],
    kruin: {x: number; y: number},
    sway: number,
    nu: number,
  ): void {
    const plekken = this.hoedPlekken(beeld.toren, volgorde)
    const basis = plekken[0] as number
    const land = nu - beeld.landMs
    for (let i = 0; i < beeld.toren; i++) {
      const nr = volgorde[i % 10] as number
      const m = this.k.maten.hoed[nr] as {b: number; h: number}
      const hoogte = i / Math.max(1, beeld.toren)
      const dx =
        ((i * 7) % 5) -
        2 +
        sway * (i + 1) ** 1.25 * 0.6 +
        Math.sin(nu / 700 + i * 0.6) * 0.6 * hoogte
      const y = kruin.y + ((plekken[i] as number) - basis)
      // De bovenste hoed is net geland: hij veert in.
      const boven = i === beeld.toren - 1 && land < 260
      const ky = boven ? 1 - 0.25 * Math.sin((land / 260) * Math.PI) : 1
      const kx = boven ? 1 + 0.18 * Math.sin((land / 260) * Math.PI) : 1
      this.ctx.drawImage(
        this.k.hoed[nr] as HTMLImageElement,
        kruin.x + dx - (m.b * kx) / 2,
        y - m.h * 0.8 * ky,
        m.b * kx,
        m.h * ky,
      )
    }
  }

  landHoeden(beeld: Beeld, nu: number): void {
    while (
      beeld.vluchten.length > 0 &&
      nu >=
        (beeld.vluchten[0] as Vlucht).start + (beeld.vluchten[0] as Vlucht).duur
    ) {
      beeld.vluchten.shift()
      beeld.toren += 1
      beeld.landMs = nu
      beeld.torenVeer.stoot((Math.random() < 0.5 ? -1 : 1) * 0.012)
    }
  }

  tekenVluchten(
    beeld: Beeld,
    kruin: {x: number; y: number},
    volgorde: readonly number[],
    nu: number,
  ): void {
    const plekken = this.hoedPlekken(
      beeld.toren + beeld.vluchten.length + 1,
      volgorde,
    )
    const basis = plekken[0] as number
    for (const v of beeld.vluchten) {
      if (nu < v.start) continue
      const f = klem((nu - v.start) / v.duur, 0, 1)
      const m = this.k.maten.hoed[v.hoed] as {b: number; h: number}
      const doelY = kruin.y + ((plekken[v.plek] as number) - basis) - m.h * 0.8
      const x = v.vanX + (kruin.x - v.vanX) * f - 90 * 4 * f * (1 - f)
      const y = v.vanY + (doelY - v.vanY) * veerUit(f) - 140 * 4 * f * (1 - f)
      const {ctx} = this
      ctx.save()
      ctx.translate(x, y + m.h / 2)
      ctx.rotate((1 - f) * 2.4)
      ctx.drawImage(
        this.k.hoed[v.hoed] as HTMLImageElement,
        -m.b / 2,
        -m.h / 2,
        m.b,
        m.h,
      )
      ctx.restore()
    }
  }

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

  tekenTijd(p: Potje): void {
    const {ctx} = this
    ctx.fillStyle = 'rgba(0, 0, 0, 0.35)'
    ctx.fillRect(0, 0, B, 9)
    ctx.fillStyle = p.tijdOver < 5000 ? '#ff4b3a' : '#ffc93c'
    ctx.fillRect(0, 0, (B * p.tijdOver) / 30000, 9)
  }

  tekenTeller(p: Potje): void {
    const kroon = this.k.hoed[4] as HTMLImageElement
    const km = this.k.maten.hoed[4] as {b: number; h: number}
    const s = String(p.hoeden)
    this.ctx.font = '44px "Lilita One", sans-serif'
    const tb = this.ctx.measureText(s).width
    const kb = km.b * 0.7
    const x0 = CX - (tb + kb + 8) / 2
    this.ctx.drawImage(kroon, x0, 48 - (km.h * 0.7) / 2, kb, km.h * 0.7)
    tekst(this.ctx, s, x0 + kb + 8, 24, 44, 'left', '#ffe066')
  }

  tekenKreet(beeld: Beeld, nu: number): void {
    const t = nu - beeld.kreetSinds
    if (!beeld.kreet || t > 700) return
    const veer = t < 140 ? 1.4 - (0.4 * t) / 140 : 1
    const op = t > 450 ? (t - 450) / 250 : 0
    const {ctx} = this
    ctx.save()
    ctx.globalAlpha = 1 - op
    ctx.translate(28, this.voet - 300 - op * 30)
    ctx.scale(veer, veer)
    const kleur =
      beeld.kreet === 'GOLDEN!'
        ? '#ffc93c'
        : beeld.kreet === 'PERFECT!'
          ? '#8ff0c4'
          : '#fff6e6'
    tekst(ctx, beeld.kreet, 0, 0, 48, 'left', kleur)
    tekst(ctx, beeld.kreetSub, 2, 52, 26, 'left', '#ffe066')
    ctx.restore()
  }
}
