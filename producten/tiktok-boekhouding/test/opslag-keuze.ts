// Welke opslag de bestaande verwerk-toetsen krijgen: standaard GeheugenOpslag; de *-d1.test.ts-bestanden zetten
// vóór het laden een maker voor D1Opslag (ontwerp-d1-worker.md, toets a: dezelfde toetsen ook met D1Opslag).
import { GeheugenOpslag } from "../src/opslag.ts";

export function maakOpslag(): GeheugenOpslag {
  const maker = (globalThis as { maakToetsOpslag?: () => GeheugenOpslag }).maakToetsOpslag;
  return maker ? maker() : new GeheugenOpslag();
}
