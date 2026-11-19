// Het scherm: de grot, Gloop, de vallende held en de toren. Overgezet uit SpelView.mc (Garmin),
// met dezelfde plaatjes van Mila (kit 454) en dezelfde ankers. Eenheden: de breedte is altijd
// 454 (zoals de kit), de hoogte volgt het scherm, zodat de toren op een telefoon hoger mag worden.
import {
  inVangzone,
  isGoud,
  type Potje,
  SLOK_MS,
  Toestand,
  WEG_MS,
} from '../shared/spel.ts'

export const B = 454
const CX = B / 2
// Maten uit Maten.mc voor 454: Gloop breed 154, rust hoog 112, hap 119, slok 119, held 119x124,
// helm 101x100, voet van de toren op (82, 15) in de rustsprite.
const GLOOP_B = 154
const RUST_H = 112
const HAP_H = 119
const HELD_B = 119
const HELD_H = 124
const HELM_B = 101
const HELM_H = 100
const TOREN_DX = 82
const TOREN_DY = 15
const HOED_BESTAND = [
  'hoed_00_helm',
  'hoed_01_puntmuts',
  'hoed_02_kap',
  'hoed_03_pet',
  'hoed_04_kroon',
  'hoed_05_koksmuts',
  'hoed_06_emmer',
  'hoed_07_hoge_hoed',
  'hoed_08_pan',
  'hoed_09_veermuts',
]

const KLEUR = {
  grotDiep: '#24110a',
  grotWarm: '#a85a2a',
  grotGloed: '#d98a45',
  licht: 'rgba(255, 200, 130, 0.30)',
  vloer: '#3b170c',
  goud: '#ffc93c',
  rood: '#ff4b3a',
  wit: '#fff6e6',
  rand: '#2b1206',
}

type Plaatjes = Record<string, HTMLImageElement>

export async function laadPlaatjes(): Promise<Plaatjes> {
  const namen = [
    'gloop_rust',
    'gloop_hap',
    'gloop_blij',
    'gloop_slok',
    'held_val',
    'helm_vlieg',
    ...HOED_BESTAND,
  ]
  const uit: Plaatjes = {}
  await Promise.all(
    namen.map(
      n =>
        new Promise<void>((klaar, fout) => {
          const img = new Image()
          img.onload = () => klaar()
          img.onerror = () => fout(new Error(`plaatje ${n} ontbreekt`))
          img.src = `kit/${n}.png`
          uit[n] = img
        }),
    ),
  )
  return uit
}

type Vonk = {
  x: number
  y: number
  vx: number
  vy: number
  leven: number
  goud: boolean
}

export type Beeld = {
  /** Hoeveel ms de kreet al staat (voor het opveren). */
  kreetMs: number
  kreet: string
  kreetSub: string
  /** Camera: 1 tijdens het spel, kleiner aan het eind zodat de hele toren in beeld komt. */
  zoom: number
  /** Waar de voet van Gloop op het scherm staat (0..1 van de hoogte). */
  voetPlek: number
  vonken: Vonk[]
  /** Schuif Gloop opzij (eenheden), voor de post in de feed waar links de tekst staat. */
  opzij: number
}

export function nieuwBeeld(): Beeld {
  return {
    kreetMs: 9999,
    kreet: '',
    kreetSub: '',
    zoom: 1,
    voetPlek: 1,
    vonken: [],
    opzij: 0,
  }
}

export class Tekenaar {
  readonly canvas: HTMLCanvasElement
  readonly ctx: CanvasRenderingContext2D
  readonly pl: Plaatjes
  /** Hoogte in spel-eenheden. */
  h = 800
  schaal = 1

  constructor(canvas: HTMLCanvasElement, pl: Plaatjes) {
    this.canvas = canvas
    const ctx = canvas.getContext('2d')
    if (!ctx) throw new Error('geen canvas')
    this.ctx = ctx
    this.pl = pl
  }

  /** Past de canvas aan het scherm aan. Breedte is altijd 454 eenheden. */
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

  /** Hoogste punt van de toren in spel-eenheden bij n hoeden (zelfde stapel als tekenToren). */
  torenTop(n: number, volgorde: readonly number[]): number {
    let y = this.voet - RUST_H + TOREN_DY
    for (let i = 0; i < n; i++) {
      const img = this.pl[
        HOED_BESTAND[volgorde[i % 10] as number] as string
      ] as HTMLImageElement
      y = y - img.height * 0.78 + img.height * 0.22
    }
    return y
  }

  teken(
    p: Potje,
    beeld: Beeld,
    volgorde: readonly number[],
    dtMs: number,
  ): void {
    const {ctx} = this
    ctx.setTransform(this.schaal, 0, 0, this.schaal, 0, 0)
    ctx.imageSmoothingQuality = 'high'
    this.tekenGrot()

    // Camera: schaal rond de voet van Gloop, en schuif de voet naar voetPlek.
    const voet = this.voet
    const doelVoet = beeld.voetPlek * this.h - (beeld.voetPlek < 1 ? 0 : 46)
    ctx.save()
    ctx.translate(CX + beeld.opzij, doelVoet)
    ctx.scale(beeld.zoom, beeld.zoom)
    ctx.translate(-CX, -voet)

    const torenX = CX - GLOOP_B / 2 + TOREN_DX
    const kruinY = voet - RUST_H + TOREN_DY
    let n = p.hoeden
    if (p.toestand === Toestand.Slok) n -= isGoud(p) ? 3 : 1
    if (beeld.zoom < 1) this.tekenVloer(voet)
    this.tekenGloop(p, voet)
    const top = this.tekenToren(torenX, kruinY, Math.max(0, n), volgorde)
    this.tekenHeld(p, voet)
    this.tekenVliegendeHelm(p, voet, torenX, top)
    this.tekenVonken(beeld, dtMs)
    ctx.restore()

    if (p.toestand !== Toestand.Klaar && p.toestand !== Toestand.Einde) {
      this.tekenTijd(p)
      this.tekenTeller(p, top)
      this.tekenKreet(beeld, torenX, dtMs)
      if (p.toestand === Toestand.Weg)
        this.tekst('bye!', 34, voet - 170, 30, 'left', KLEUR.wit)
    }
  }

  tekenGrot(): void {
    const {ctx, h} = this
    const voet = this.voet
    const g = ctx.createRadialGradient(
      CX,
      voet - 120,
      30,
      CX,
      voet - 120,
      Math.max(h, B) * 0.85,
    )
    g.addColorStop(0, KLEUR.grotGloed)
    g.addColorStop(0.35, KLEUR.grotWarm)
    g.addColorStop(1, KLEUR.grotDiep)
    ctx.fillStyle = g
    ctx.fillRect(0, 0, B, h)
    // De lichtbaan van linksboven naar de bek, zoals op het horloge.
    const mondY = voet - 82
    const d = 50
    const ax = -14
    const bx = 0.38 * B
    const lg = ctx.createLinearGradient(0, 0, bx, mondY)
    lg.addColorStop(0, 'rgba(255, 214, 150, 0.42)')
    lg.addColorStop(1, 'rgba(255, 190, 120, 0.10)')
    ctx.fillStyle = lg
    ctx.beginPath()
    ctx.moveTo(ax - d, -40)
    ctx.lineTo(ax + d, -40)
    ctx.lineTo(bx + d, mondY + 9)
    ctx.lineTo(bx - d, mondY + 9)
    ctx.closePath()
    ctx.fill()
    this.tekenVloer(voet)
  }

  tekenVloer(voet: number): void {
    const {ctx} = this
    ctx.fillStyle = KLEUR.vloer
    ctx.beginPath()
    ctx.ellipse(CX, voet + 46 + 10, B * 0.62, 70, 0, Math.PI, 0)
    ctx.lineTo(B * 2, this.h * 3)
    ctx.lineTo(-B, this.h * 3)
    ctx.closePath()
    ctx.fill()
  }

  tekenGloop(p: Potje, voet: number): void {
    const t = p.toestand
    const x = CX - GLOOP_B / 2
    let img = this.pl.gloop_rust as HTMLImageElement
    let hoog = RUST_H
    if (t === Toestand.Slok) {
      img = this.pl.gloop_slok as HTMLImageElement
      hoog = HAP_H
    } else if (t === Toestand.Valt && inVangzone(p) && p.hapDicht === 0) {
      img = this.pl.gloop_hap as HTMLImageElement
      hoog = HAP_H
    } else if (t === Toestand.Einde || (t === Toestand.Wacht && p.reeks > 0)) {
      img = this.pl.gloop_blij as HTMLImageElement
    }
    this.ctx.drawImage(img, x, voet - hoog)
  }

  tekenToren(
    torenX: number,
    kruinY: number,
    n: number,
    volgorde: readonly number[],
  ): number {
    let y = kruinY
    for (let i = 0; i < n; i++) {
      const img = this.pl[
        HOED_BESTAND[volgorde[i % 10] as number] as string
      ] as HTMLImageElement
      const boven = y - img.height * 0.78
      // De toren wiebelt een beetje: elke hoed een paar pixels opzij (zoals op het horloge).
      const dx = ((i * 7) % 5) - 2
      this.ctx.drawImage(img, torenX - img.width / 2 + dx, boven)
      y = boven + img.height * 0.22
    }
    return y
  }

  heldPlek(p: Potje, voet: number): {x: number; y: number} {
    const t = p.y / 815
    const startY = 64
    const mondY = voet - 82
    return {x: B * (0.04 + 0.34 * t), y: startY + (mondY - startY) * t}
  }

  tekenHeld(p: Potje, voet: number): void {
    const {ctx} = this
    const held = this.pl.held_val as HTMLImageElement
    if (p.toestand === Toestand.Valt) {
      const {x, y} = this.heldPlek(p, voet)
      if (isGoud(p)) {
        const g = ctx.createRadialGradient(x, y, 10, x, y, 90)
        g.addColorStop(0, 'rgba(255, 220, 90, 0.85)')
        g.addColorStop(1, 'rgba(255, 200, 60, 0)')
        ctx.fillStyle = g
        ctx.fillRect(x - 90, y - 90, 180, 180)
      }
      ctx.drawImage(held, x - HELD_B / 2, y - HELD_H / 2)
      if (isGoud(p))
        this.tekst(
          'x3',
          x + HELD_B / 2 - 6,
          y - HELD_H / 2 + 6,
          30,
          'left',
          KLEUR.goud,
        )
      if (inVangzone(p) && p.hapDicht === 0) {
        this.tekst(
          '!',
          x - HELD_B / 2 + 4,
          y - HELD_H / 2 + 4,
          46,
          'right',
          '#ffe94a',
        )
      }
    } else if (p.toestand === Toestand.Weg) {
      // Gemist: hij glijdt langs Gloop naar links het beeld uit.
      const x = B * 0.3 - ((B * 0.3 + HELD_B) * p.fase) / WEG_MS
      ctx.drawImage(held, x, voet - HELD_H)
    }
  }

  tekenVliegendeHelm(
    p: Potje,
    voet: number,
    torenX: number,
    top: number,
  ): void {
    if (p.toestand !== Toestand.Slok) return
    const f = Math.min(1, p.fase / SLOK_MS)
    const begin = voet - RUST_H - HELM_H / 2
    const eind = top - HELM_H / 2
    const x = CX + (torenX - CX) * f + B * 0.22 * 4 * f * (1 - f)
    const y = begin + (eind - begin) * f
    this.ctx.drawImage(
      this.pl.helm_vlieg as HTMLImageElement,
      x - HELM_B / 2,
      y - HELM_H / 2,
    )
  }

  /** Vonken bij een voltreffer of gouden held. */
  strooiVonken(beeld: Beeld, goud: boolean): void {
    const mondX = CX - 20
    const mondY = this.voet - 70
    for (let i = 0; i < (goud ? 16 : 9); i++) {
      const hoek = -Math.PI * (0.1 + 0.8 * Math.random())
      const v = 0.25 + Math.random() * 0.35
      beeld.vonken.push({
        x: mondX,
        y: mondY,
        vx: Math.cos(hoek) * v,
        vy: Math.sin(hoek) * v,
        leven: 520,
        goud,
      })
    }
  }

  tekenVonken(beeld: Beeld, dtMs: number): void {
    const {ctx} = this
    beeld.vonken = beeld.vonken.filter(v => v.leven > 0)
    for (const v of beeld.vonken) {
      v.leven -= dtMs
      v.x += v.vx * dtMs
      v.y += v.vy * dtMs
      v.vy += 0.0009 * dtMs
      const a = Math.max(0, v.leven / 520)
      ctx.fillStyle = v.goud
        ? `rgba(255, 210, 70, ${a})`
        : `rgba(255, 250, 220, ${a})`
      const r = 3 + 3 * a
      ctx.beginPath()
      ctx.moveTo(v.x, v.y - r * 1.6)
      ctx.lineTo(v.x + r * 0.5, v.y)
      ctx.lineTo(v.x, v.y + r * 1.6)
      ctx.lineTo(v.x - r * 0.5, v.y)
      ctx.closePath()
      ctx.fill()
    }
  }

  tekenTijd(p: Potje): void {
    const {ctx} = this
    const deel = p.tijdOver / 30000
    ctx.fillStyle = 'rgba(0, 0, 0, 0.35)'
    ctx.fillRect(0, 0, B, 9)
    ctx.fillStyle = p.tijdOver < 5000 ? KLEUR.rood : KLEUR.goud
    ctx.fillRect(0, 0, B * deel, 9)
  }

  tekenTeller(p: Potje, top: number): void {
    const kroon = this.pl.hoed_04_kroon as HTMLImageElement
    const s = String(p.hoeden)
    this.ctx.font = '44px "Lilita One", sans-serif'
    const tb = this.ctx.measureText(s).width
    // Komt de toren tot bovenin, dan wijkt de teller uit naar rechts (zoals op het horloge).
    const hoog = top < 110
    const midden = hoog ? B * 0.8 : CX
    const x0 = midden - (tb + kroon.width + 8) / 2
    const y = 48
    this.ctx.drawImage(kroon, x0, y - kroon.height / 2)
    this.tekst(s, x0 + kroon.width + 8, y - 24, 44, 'left', '#ffe066')
  }

  tekenKreet(beeld: Beeld, torenX: number, dtMs: number): void {
    beeld.kreetMs += dtMs
    if (!beeld.kreet || beeld.kreetMs > 520) return
    const veer = beeld.kreetMs < 120 ? 1.35 - (0.35 * beeld.kreetMs) / 120 : 1
    const rechts = torenX - 60
    const y = this.voet - 250
    this.ctx.save()
    this.ctx.translate(rechts, y)
    this.ctx.scale(veer, veer)
    this.tekst(beeld.kreet, 0, -24, 52, 'right', KLEUR.wit)
    if (beeld.kreetSub)
      this.tekst(beeld.kreetSub, 0, 30, 36, 'right', KLEUR.goud)
    this.ctx.restore()
  }

  /** Tekst met een donkere rand, zoals "GULP!" op het horloge. y is de bovenkant. */
  tekst(
    s: string,
    x: number,
    y: number,
    grootte: number,
    uitlijn: CanvasTextAlign,
    kleur: string,
  ): void {
    const {ctx} = this
    ctx.font = `${grootte}px "Lilita One", sans-serif`
    ctx.textAlign = uitlijn
    ctx.textBaseline = 'top'
    ctx.lineJoin = 'round'
    ctx.lineWidth = Math.max(4, grootte * 0.16)
    ctx.strokeStyle = KLEUR.rand
    ctx.strokeText(s, x, y)
    ctx.fillStyle = kleur
    ctx.fillText(s, x, y)
  }
}
