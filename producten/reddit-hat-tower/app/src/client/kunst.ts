// De plaatjes: renders uit de 3D-modellen van Gloop, de held en de tien hoeden (kunst/render.sh en
// kunst/knip.py). Maten en ankers in spel-eenheden staan in public/kunst/kunst.json.

export type Maat = {b: number; h: number}
export type KunstMaten = {
  px: number
  gloop: Maat & {
    kruin: [number, number]
    mond: [number, number, number, number]
  }
  held: Record<
    'schrik' | 'vallen' | 'stap1' | 'stap2',
    Maat & {kruin: [number, number]}
  >
  hoed: Maat[]
}

export type GloopStand = 'rust' | 'hap' | 'blij' | 'knipper' | 'kneep'

export type Kunst = {
  maten: KunstMaten
  gloop: Record<GloopStand, HTMLImageElement>
  held: Record<'schrik' | 'vallen' | 'stap1' | 'stap2', HTMLImageElement>
  hoed: HTMLImageElement[]
}

function laad(src: string): Promise<HTMLImageElement> {
  return new Promise((klaar, fout) => {
    const img = new Image()
    img.onload = () => klaar(img)
    img.onerror = () => fout(new Error(`plaatje ${src} ontbreekt`))
    img.src = src
  })
}

export async function laadKunst(): Promise<Kunst> {
  const maten = (await (await fetch('kunst/kunst.json')).json()) as KunstMaten
  const standen: GloopStand[] = ['rust', 'hap', 'blij', 'knipper', 'kneep']
  const helden = ['schrik', 'vallen', 'stap1', 'stap2'] as const
  const [gl, hd, hoed] = await Promise.all([
    Promise.all(standen.map(s => laad(`kunst/gloop-${s}.png`))),
    Promise.all(helden.map(s => laad(`kunst/held-${s}.png`))),
    Promise.all(
      Array.from({length: 10}, (_, i) => laad(`kunst/hoed-${i}.png`)),
    ),
  ])
  return {
    maten,
    gloop: Object.fromEntries(
      standen.map((s, i) => [s, gl[i]]),
    ) as Kunst['gloop'],
    held: Object.fromEntries(helden.map((s, i) => [s, hd[i]])) as Kunst['held'],
    hoed,
  }
}
