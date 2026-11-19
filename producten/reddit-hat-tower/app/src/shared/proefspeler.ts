// Een nep-speler die het spel echt speelt (voor de toetsen en de lokale ranglijst). Niet in het spel zelf.
import {
  begin,
  druk,
  inVangzone,
  nieuwPotje,
  type Potje,
  stap,
  Toestand,
} from './spel.ts'

/** Speelt een potje: drukt rond `mikpunt` (y), met `ruis` spreiding, en mist een deel met `kansMis`. */
export function speelProef(
  dag: number,
  mikpunt = 815,
  ruis = 30,
  kansMis = 0.1,
  zaad = 1,
): Potje {
  let z = zaad
  const toeval = (): number => {
    z = (z * 1103515245 + 12345) & 0x7fffffff
    return z / 0x7fffffff
  }
  const p = nieuwPotje(dag)
  begin(p)
  let doel = mikpunt + (toeval() * 2 - 1) * ruis
  let laat = toeval() < kansMis
  let held = p.held
  while (p.toestand !== Toestand.Einde) {
    if (p.held !== held) {
      held = p.held
      doel = mikpunt + (toeval() * 2 - 1) * ruis
      laat = toeval() < kansMis
    }
    if (p.toestand === Toestand.Valt && !laat && p.y >= doel && inVangzone(p))
      druk(p)
    stap(p)
  }
  return p
}
