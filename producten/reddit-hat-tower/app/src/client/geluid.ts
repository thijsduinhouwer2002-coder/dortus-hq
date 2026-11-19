// Geluid zonder bestanden: korte klanken uit de Web Audio API. Start pas na de eerste tik (regel van browsers).
// Voor het inzendfilmpje (?film=1) onthoudt het elke klank met zijn tijd, zodat dezelfde klanken
// achteraf in een OfflineAudioContext tot een WAV gerenderd kunnen worden (dev/film.py).
let ctx: AudioContext | undefined
let aan = localStorage.getItem('gloop-geluid') !== 'uit'
const FILM = new URLSearchParams(location.search).has('film')
const logboek: {t: number; naam: Klank; arg: number[]}[] = []

type Klank =
  | 'gulp'
  | 'goud'
  | 'lucht'
  | 'mis'
  | 'einde'
  | 'land'
  | 'start'
  | 'boing'
  | 'wie'

export function geluidAan(): boolean {
  return aan
}

export function zetGeluid(waarde: boolean): void {
  aan = waarde
  localStorage.setItem('gloop-geluid', waarde ? 'aan' : 'uit')
}

export function wekGeluid(): void {
  if (!ctx) {
    try {
      ctx = new AudioContext()
    } catch {
      return
    }
  }
  if (ctx.state === 'suspended') void ctx.resume()
}

type Doel = BaseAudioContext

function toon(
  c: Doel,
  begin: number,
  van: number,
  naar: number,
  duur: number,
  soort: OscillatorType,
  sterkte: number,
  wacht = 0,
): void {
  const t = begin + wacht
  const osc = c.createOscillator()
  const gain = c.createGain()
  const filter = c.createBiquadFilter()
  filter.type = 'lowpass'
  filter.frequency.value = 1800
  osc.type = soort
  osc.frequency.setValueAtTime(van, t)
  osc.frequency.exponentialRampToValueAtTime(naar, t + duur)
  gain.gain.setValueAtTime(0.0001, t)
  gain.gain.exponentialRampToValueAtTime(sterkte, t + 0.012)
  gain.gain.exponentialRampToValueAtTime(0.0001, t + duur)
  osc.connect(filter).connect(gain).connect(c.destination)
  osc.start(t)
  osc.stop(t + duur + 0.02)
}

/** Alle klanken: (doel, starttijd, argumenten). */
const KLANKEN: Record<Klank, (c: Doel, t: number, arg: number[]) => void> = {
  // De slok: een zakkende, ronde klank. Hoger bij een langere reeks; met een tinkel bij een voltreffer.
  gulp: (c, t, [raak = 0, reeks = 0, kleur = 1]) => {
    const op = Math.min(reeks, 8) * 18
    // Elke slok net iets anders: toonhoogte en lengte wisselen een beetje.
    toon(
      c,
      t,
      (260 + op) * kleur,
      70 * kleur,
      0.2 + 0.05 * (kleur - 0.9) * 5,
      'sine',
      0.5,
    )
    if (raak)
      toon(c, t, 880 + op * 3, 1320 + op * 3, 0.12, 'triangle', 0.18, 0.05)
  },
  goud: (c, t) => {
    toon(c, t, 660, 990, 0.1, 'triangle', 0.22)
    toon(c, t, 990, 1480, 0.14, 'triangle', 0.2, 0.08)
    toon(c, t, 260, 70, 0.22, 'sine', 0.5)
  },
  lucht: (c, t) => toon(c, t, 180, 140, 0.06, 'square', 0.06),
  mis: (c, t) => toon(c, t, 320, 240, 0.16, 'sine', 0.12),
  // Tegen de wand: een korte boing.
  boing: (c, t) => {
    toon(c, t, 150, 420, 0.09, 'triangle', 0.2)
    toon(c, t, 420, 260, 0.14, 'sine', 0.12, 0.08)
  },
  // Een held komt binnen: een klein "wie!" omhoog, per soort held een eigen hoogte.
  wie: (c, t, [soort = 0]) => {
    const f = 520 + soort * 70
    toon(c, t, f, f * 1.6, 0.16, 'sine', 0.05)
  },
  land: (c, t) => toon(c, t, 520, 780, 0.08, 'triangle', 0.08),
  // Begin van de ronde: een korte, opgewekte "boing" omhoog.
  start: (c, t) => {
    toon(c, t, 220, 660, 0.18, 'triangle', 0.22)
    toon(c, t, 440, 880, 0.12, 'sine', 0.12, 0.12)
  },
  einde: (c, t) => {
    toon(c, t, 523, 523, 0.12, 'triangle', 0.2)
    toon(c, t, 659, 659, 0.12, 'triangle', 0.2, 0.12)
    toon(c, t, 784, 784, 0.3, 'triangle', 0.22, 0.24)
  },
}

function speel(naam: Klank, arg: number[] = []): void {
  if (FILM) logboek.push({t: performance.now(), naam, arg})
  if (!aan || !ctx) return
  KLANKEN[naam](ctx, ctx.currentTime, arg)
}

export const gulp = (raak: boolean, reeks: number): void =>
  speel('gulp', [raak ? 1 : 0, reeks, 0.92 + Math.random() * 0.16])
export const goud = (): void => speel('goud')
export const lucht = (): void => speel('lucht')
export const mis = (): void => speel('mis')
export const einde = (): void => speel('einde')
export const land = (): void => speel('land')
export const start = (): void => speel('start')
export const boing = (): void => speel('boing')
export const wie = (soort: number): void => speel('wie', [soort])

/** Alleen voor het filmpje: rendert alle gespeelde klanken vanaf `vanaf` (performance.now) tot een WAV (base64). */
async function filmGeluid(vanaf: number, seconden: number): Promise<string> {
  const rate = 48000
  const c = new OfflineAudioContext(2, Math.ceil(seconden * rate), rate)
  for (const e of logboek) {
    const t = (e.t - vanaf) / 1000
    if (t >= 0 && t < seconden) KLANKEN[e.naam](c, t, e.arg)
  }
  const buf = await c.startRendering()
  return wavBase64(buf)
}

function wavBase64(buf: AudioBuffer): string {
  const n = buf.length
  const kanalen = buf.numberOfChannels
  const data = new DataView(new ArrayBuffer(44 + n * kanalen * 2))
  const schrijf = (o: number, s: string) => {
    for (let i = 0; i < s.length; i++) data.setUint8(o + i, s.charCodeAt(i))
  }
  schrijf(0, 'RIFF')
  data.setUint32(4, 36 + n * kanalen * 2, true)
  schrijf(8, 'WAVEfmt ')
  data.setUint32(16, 16, true)
  data.setUint16(20, 1, true)
  data.setUint16(22, kanalen, true)
  data.setUint32(24, buf.sampleRate, true)
  data.setUint32(28, buf.sampleRate * kanalen * 2, true)
  data.setUint16(32, kanalen * 2, true)
  data.setUint16(34, 16, true)
  schrijf(36, 'data')
  data.setUint32(40, n * kanalen * 2, true)
  let o = 44
  for (let i = 0; i < n; i++) {
    for (let k = 0; k < kanalen; k++) {
      const v = Math.max(-1, Math.min(1, buf.getChannelData(k)[i] ?? 0))
      data.setInt16(o, v * 0x7fff, true)
      o += 2
    }
  }
  const bytes = new Uint8Array(data.buffer)
  let s = ''
  for (let i = 0; i < bytes.length; i += 0x8000)
    s += String.fromCharCode(...bytes.subarray(i, i + 0x8000))
  return btoa(s)
}

if (FILM) Object.assign(window, {gloopFilmGeluid: filmGeluid})
