// Het speelveld: grot, gezamenlijke toren, Gloop, de vallende held en de hoedentoren.
// De spelregels komen uit shared/spel.ts; hier zit alleen hoe het eruitziet en beweegt.
// Eenheden: de breedte is altijd 454 (zoals op het horloge), de hoogte volgt het scherm.
import {inVangzone, type Potje, Toestand} from '../shared/spel.ts'
import {B, type Beeld, CX, type Vlucht} from './basis.ts'
import {klem, veerUit} from './effecten.ts'
import {tekenGrot, tekenSamen, tekst} from './grot.ts'
import {MetHeld} from './held.ts'
import type {GloopStand} from './kunst.ts'

export {B, type Beeld, nieuwBeeld} from './basis.ts'

export class Scene extends MetHeld {
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
          vanX: m.x - 14,
          vanY: m.y - 70,
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
      this.tekenTeller(p, this.torenTop(beeld.toren, volgorde))
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
      // Klein uit de mond, groeit tot hij landt.
      const groei = 0.55 + 0.45 * f
      ctx.scale(groei, groei)
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

  tekenTijd(p: Potje): void {
    const {ctx} = this
    ctx.fillStyle = 'rgba(0, 0, 0, 0.35)'
    ctx.fillRect(0, 0, B, 9)
    ctx.fillStyle = p.tijdOver < 5000 ? '#ff4b3a' : '#ffc93c'
    ctx.fillRect(0, 0, (B * p.tijdOver) / 30000, 9)
  }

  /** Teller bovenaan; komt de toren zo hoog, dan wijkt hij uit naar links (zoals op het horloge). */
  tekenTeller(p: Potje, top: number): void {
    const kroon = this.k.hoed[4] as HTMLImageElement
    const km = this.k.maten.hoed[4] as {b: number; h: number}
    const s = String(p.hoeden)
    this.ctx.font = '44px "Lilita One", sans-serif'
    const tb = this.ctx.measureText(s).width
    const kb = km.b * 0.7
    const midden = top < 100 ? 92 : CX
    const x0 = midden - (tb + kb + 8) / 2
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
