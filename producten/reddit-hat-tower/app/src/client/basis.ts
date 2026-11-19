// Basis van het speelveld: maten, het geheugen van het beeld (Beeld) en de plek van mond en toren.
import {Deeltjes, Schok, Veer} from './effecten.ts'
import type {Kunst} from './kunst.ts'

export const B = 454
export const CX = B / 2

export type Vlucht = {
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

export class Basis {
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
}
