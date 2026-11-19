// Alleen voor het inzendfilmpje (?film=1): een eigen klok, zodat dev/film.py het spel beeld voor beeld
// kan laten lopen en elk beeld op ware grootte (1080x1920) kan vastleggen. In het echte spel doet dit niets.
if (new URLSearchParams(location.search).has('film')) {
  let virt = 0
  let wachtrij: FrameRequestCallback[] = []
  const timers: {t: number; fn: () => void}[] = []
  performance.now = () => virt
  window.requestAnimationFrame = cb => {
    wachtrij.push(cb)
    return wachtrij.length
  }
  window.setTimeout = ((fn: () => void, ms?: number) => {
    timers.push({t: virt + (ms ?? 0), fn})
    return 0
  }) as unknown as typeof setTimeout
  const stap = (ms: number): void => {
    virt += ms
    for (const t of timers.filter(x => x.t <= virt)) {
      timers.splice(timers.indexOf(t), 1)
      t.fn()
    }
    const nu = wachtrij
    wachtrij = []
    for (const cb of nu) cb(virt)
  }
  Object.assign(window, {
    /** Laat de klok `ms` lopen in `delen` stapjes (de speler en het spel kijken bij elk stapje). */
    gloopFilmStap: (ms: number, delen = 1): void => {
      for (let i = 0; i < delen; i++) stap(ms / delen)
    },
  })
}
