// Geluid zonder bestanden: korte klanken uit de Web Audio API. Start pas na de eerste tik (regel van browsers).
let ctx: AudioContext | undefined
let aan = localStorage.getItem('gloop-geluid') !== 'uit'

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

function toon(
  van: number,
  naar: number,
  duur: number,
  soort: OscillatorType,
  sterkte: number,
  wacht = 0,
): void {
  if (!aan || !ctx) return
  const t = ctx.currentTime + wacht
  const osc = ctx.createOscillator()
  const gain = ctx.createGain()
  const filter = ctx.createBiquadFilter()
  filter.type = 'lowpass'
  filter.frequency.value = 1800
  osc.type = soort
  osc.frequency.setValueAtTime(van, t)
  osc.frequency.exponentialRampToValueAtTime(naar, t + duur)
  gain.gain.setValueAtTime(0.0001, t)
  gain.gain.exponentialRampToValueAtTime(sterkte, t + 0.012)
  gain.gain.exponentialRampToValueAtTime(0.0001, t + duur)
  osc.connect(filter).connect(gain).connect(ctx.destination)
  osc.start(t)
  osc.stop(t + duur + 0.02)
}

/** De slok: een zakkende, ronde klank. Hoger bij een langere reeks. */
export function gulp(raak: boolean, reeks: number): void {
  const op = Math.min(reeks, 8) * 18
  toon(260 + op, 70, 0.22, 'sine', 0.5)
  if (raak) toon(880 + op * 3, 1320 + op * 3, 0.12, 'triangle', 0.18, 0.05)
}

export function goud(): void {
  toon(660, 990, 0.1, 'triangle', 0.22)
  toon(990, 1480, 0.14, 'triangle', 0.2, 0.08)
  toon(260, 70, 0.22, 'sine', 0.5)
}

export function lucht(): void {
  toon(180, 140, 0.06, 'square', 0.06)
}

export function mis(): void {
  toon(320, 240, 0.16, 'sine', 0.12)
}

export function einde(): void {
  toon(523, 523, 0.12, 'triangle', 0.2)
  toon(659, 659, 0.12, 'triangle', 0.2, 0.12)
  toon(784, 784, 0.3, 'triangle', 0.22, 0.24)
}
