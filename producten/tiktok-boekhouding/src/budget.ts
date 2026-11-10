// Budget per Worker-aanroep (ontwerp-productlaag.md, kop "Budget"). Eén teller voor beide clients, als omhulsel om
// fetch: elke pagina, bestelling, Moneybird-verzoek en herhaling telt. Gratis plan: 50 uitgaande verzoeken per aanroep.

export const START_BUDGET = 45; // 5 over voor tokens verversen en onvoorzien
/** Slechtste geval van één boeking: GET bekendId 3x, zoeken 3x, schrijven 3x bij 429, plus DELETE en POST als terugval,
 * plus 1 voor het vastleggen van de telling (ontwerp-betalen.md, punt 2 stap 3). */
export const RESERVE_BOEKING = 13;

/** Gegooid vóórdat een verzoek vertrekt: er is niets verstuurd en niets geschreven. Volgende aanroep gaat verder. */
export class BudgetOp extends Error {
  readonly budgetOp = true;
  constructor() {
    super("budget van deze aanroep is op; volgende aanroep gaat verder");
    this.name = "BudgetOp";
  }
}

export function isBudgetOp(e: unknown): e is BudgetOp {
  return (e as { budgetOp?: unknown })?.budgetOp === true;
}

export class Budget {
  private gebruikt = 0;
  readonly totaal: number;
  constructor(totaal = START_BUDGET) {
    this.totaal = totaal;
  }

  get over(): number {
    return this.totaal - this.gebruikt;
  }

  /** Wat nieuw werk nog mag gebruiken (zonder de reserve voor afmaken). Gelijk aan `over` als reserve 0 is. */
  get overVoorNieuw(): number {
    return this.over - this.reserve;
  }

  /** Deel dat nieuw werk niet mag aanspreken (ontwerp-d1-worker.md: reserve van 6 voor afmaken). Standaard 0. */
  reserve = 0;

  /** Nieuw werk: telt één verzoek, of gooit BudgetOp als alleen de reserve nog over is. */
  neem(): void {
    if (this.over <= this.reserve) throw new BudgetOp();
    this.gebruikt++;
  }

  /** Afmaken (status, wachtrij, slot terug): mag de reserve gebruiken, weigert pas als er echt niets over is. */
  neemAfmaken(): void {
    if (this.over <= 0) throw new BudgetOp();
    this.gebruikt++;
  }

  /** Hoeveel van het gebruikte budget naar de opslag (D1) ging: telt niet mee voor "vers" in ophalen.ts. */
  opslag = 0;

  /** Teller voor D1Opslag: zelfde pot (ontwerp-d1-worker.md, "Eén pot van 50"), maar apart bijgehouden. */
  opslagTeller(): { neem(): void; neemAfmaken(): void } {
    return {
      neem: () => { this.neem(); this.opslag++; },
      neemAfmaken: () => { this.neemAfmaken(); this.opslag++; },
    };
  }

  /** fetch die eerst het budget telt; geef dit mee als `fetchFn` aan beide clients. */
  omhul(fetchFn: typeof fetch): typeof fetch {
    // async, zodat BudgetOp net als bij fetch als afgewezen belofte komt en nooit synchroon.
    return (async (input: any, init?: any) => {
      this.neem();
      return fetchFn(input, init);
    }) as typeof fetch;
  }
}
