// Het eindmoment: de camera laat je hele toren zien (bij een hoge toren van de top naar Gloop, nooit
// zo ver uitgezoomd dat het een streep wordt), daarna vliegen je hoeden naar de gezamenlijke toren van
// de subreddit, die meegroeit, met een mijlpaal als je er een passeert.
import type {Potje} from '../shared/spel.ts'
import {type Beeld, CX} from './basis.ts'
import {klem} from './effecten.ts'
import * as geluid from './geluid.ts'
import {SAMEN_X, samenTop, tekst} from './grot.ts'
import type {Scene} from './scene.ts'

const MIN_ZOOM = 0.5
const BOVEN = 70

export type Slot = {
  start: number
  hoeden: number
  zoom: number
  vStart: number
  vEind: number
  pan: boolean
  camKlaar: number
  vluchten: {start: number; duur: number; hoed: number; i: number}[]
  samenVan: number
  samenTot: number
  mijlpaal: string
  mijlpaalVanaf: number
  mijlpaalGeklonken: boolean
  klaarOp: number
}

/** Mooie ronde getallen voor "r/... passed N hats today". */
export function mijlpaal(van: number, tot: number): number | null {
  const reeks = [25, 50, 100, 150, 200, 250, 300, 400, 500, 750]
  for (let tien = 1; tien <= 1e6; tien *= 10)
    reeks.push(
      1000 * tien,
      1500 * tien,
      2000 * tien,
      2500 * tien,
      5000 * tien,
      7500 * tien,
    )
  let beste: number | null = null
  for (const m of reeks) if (m > van && m <= tot) beste = m
  return beste
}

export function maakSlot(
  scene: Scene,
  p: Potje,
  beeld: Beeld,
  volgorde: readonly number[],
  nu: number,
  naarSamen: boolean,
): Slot {
  const h = scene.h
  const voet = scene.voet
  const top = scene.torenTop(p.hoeden, volgorde)
  const vEind = h * 0.44
  const nodig = voet - top + 20
  const past = (vEind - 30) / nodig
  const zoom = klem(past, MIN_ZOOM, 1)
  const pan = past < MIN_ZOOM
  // Bij een te hoge toren begint de camera bij de top en zakt hij naar Gloop.
  const vStart = pan ? BOVEN - (top - voet) * zoom : vEind
  const camKlaar = nu + (pan ? 600 + 1500 : 900)
  const n = naarSamen && beeld.sub ? Math.min(p.hoeden, 10) : 0
  const vluchten = Array.from({length: n}, (_, i) => ({
    start: camKlaar + 150 + i * 90,
    duur: 900,
    hoed: volgorde[(p.hoeden - 1 - i + 100) % 10] as number,
    // Van onderin je toren (vlak boven Gloop, goed in beeld), niet van de top die buiten beeld kan staan.
    i: Math.min(i, p.hoeden - 1),
  }))
  const laatste = n > 0 ? camKlaar + 150 + (n - 1) * 90 + 900 : camKlaar
  const samenVan = beeld.samen
  const samenTot = n > 0 ? beeld.samen + p.hoeden : beeld.samen
  const m = n > 0 ? mijlpaal(samenVan, samenTot) : null
  return {
    start: nu,
    hoeden: p.hoeden,
    zoom,
    vStart,
    vEind,
    pan,
    camKlaar,
    vluchten,
    samenVan,
    samenTot,
    mijlpaal: m
      ? `r/${beeld.sub}\npassed ${m.toLocaleString('en-US')}\nhats today!`
      : '',
    mijlpaalVanaf: laatste,
    mijlpaalGeklonken: false,
    klaarOp: laatste + (m ? 1100 : 300),
  }
}

/** Zet de camera voor dit moment. */
export function zetCamera(
  slot: Slot,
  beeld: Beeld,
  voet: number,
  nu: number,
): void {
  const t = nu - slot.start
  const glad = (x: number) => x * x * (3 - 2 * x)
  if (!slot.pan) {
    const e = 1 - (1 - klem(t / 900, 0, 1)) ** 3
    beeld.zoom = 1 + (slot.zoom - 1) * e
    beeld.voetY = voet + (slot.vEind - voet) * e
    return
  }
  if (t < 600) {
    const e = 1 - (1 - t / 600) ** 3
    beeld.zoom = 1 + (slot.zoom - 1) * e
    beeld.voetY = voet + (slot.vStart - voet) * e
  } else {
    const e = glad(klem((t - 600) / 1500, 0, 1))
    beeld.zoom = slot.zoom
    beeld.voetY = slot.vStart + (slot.vEind - slot.vStart) * e
  }
}

/** Tekent de vliegende hoeden (in schermeenheden) en laat de gezamenlijke toren meetellen. */
export function tekenSlot(
  scene: Scene,
  slot: Slot,
  beeld: Beeld,
  volgorde: readonly number[],
  nu: number,
): void {
  const {ctx, k} = scene
  const g = k.maten.gloop
  const plekken = scene.hoedPlekken(slot.hoeden, volgorde)
  const naarX = SAMEN_X
  // De top van de gezamenlijke toren; staat die boven de grot uit, dan een plek op de toren die in beeld is.
  const naarY = Math.max(samenTop() + 10, scene.h * 0.28)
  let geland = 0
  for (const v of slot.vluchten) {
    const f = (nu - v.start) / v.duur
    if (f >= 1) {
      geland++
      continue
    }
    if (f < 0) continue
    const wx = CX - g.b / 2 + g.kruin[0]
    const wy = (plekken[v.i] as number) - 20
    const vanX = CX + beeld.opzij + (wx - CX) * beeld.zoom
    const vanY = (beeld.voetY ?? scene.voet) + (wy - scene.voet) * beeld.zoom
    const x = vanX + (naarX - vanX) * f
    const y = vanY + (naarY - vanY) * f - 120 * 4 * f * (1 - f)
    const m = k.maten.hoed[v.hoed] as {b: number; h: number}
    // Groot genoeg om te zien: begint op ware grootte, krimpt naar de maat van de verre toren.
    const s = 1.05 - 0.6 * f
    ctx.save()
    ctx.translate(x, y)
    ctx.rotate(Math.sin(f * Math.PI) * 0.8)
    ctx.drawImage(
      k.hoed[v.hoed] as HTMLImageElement,
      (-m.b * s) / 2,
      (-m.h * s) / 2,
      m.b * s,
      m.h * s,
    )
    ctx.restore()
  }
  const n = slot.vluchten.length
  beeld.samenTeller =
    n === 0
      ? slot.samenTot
      : Math.round(
          slot.samenVan + ((slot.samenTot - slot.samenVan) * geland) / n,
        )
  // "+N hats" stijgt op bij het bordje zodra je eerste hoed aankomt.
  if (geland > 0) {
    const t0 = (slot.vluchten[0]?.start ?? 0) + (slot.vluchten[0]?.duur ?? 0)
    const op = Math.min(1, (nu - t0) / 1200)
    tekst(
      ctx,
      `+${slot.samenTot - slot.samenVan} hats`,
      SAMEN_X + 52,
      naarY + 34 - op * 24,
      24,
      'right',
      '#8ff0c4',
    )
  }
  // Staat 1,9 s en vervaagt dan, zodat het uitslagvel en zijn teksten vrij blijven.
  if (
    slot.mijlpaal &&
    nu >= slot.mijlpaalVanaf &&
    nu < slot.mijlpaalVanaf + 2200
  ) {
    const t = nu - slot.mijlpaalVanaf
    const veer = t < 160 ? 1.35 - (0.35 * t) / 160 : 1
    ctx.save()
    ctx.globalAlpha = t > 1900 ? 1 - (t - 1900) / 300 : 1
    // Onder Gloop, in de lege grot: nooit over je eigen toren.
    ctx.translate(CX, scene.h * 0.56)
    ctx.scale(veer, veer)
    const [eerste, tweede, derde] = slot.mijlpaal.split('\n')
    tekst(ctx, eerste ?? '', 0, 0, 22, 'center', '#fff6e6')
    tekst(ctx, tweede ?? '', 0, 28, 36, 'center', '#ffc93c')
    tekst(ctx, derde ?? '', 0, 68, 36, 'center', '#ffc93c')
    ctx.restore()
    if (!slot.mijlpaalGeklonken) {
      slot.mijlpaalGeklonken = true
      beeld.schermDeeltjes.strooi('goud', naarX, naarY, 14, 1.2)
      geluid.goud()
    }
  }
}
