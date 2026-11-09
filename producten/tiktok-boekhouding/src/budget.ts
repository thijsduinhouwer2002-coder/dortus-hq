// Budget per Worker-aanroep (ontwerp-productlaag.md, kop "Budget"). Eén teller voor beide clients, als omhulsel om
// fetch: elke pagina, bestelling, Moneybird-verzoek en herhaling telt. Gratis plan: 50 uitgaande verzoeken per aanroep.

export const START_BUDGET = 45; // 5 over voor tokens verversen en onvoorzien
/** Slechtste geval van één boeking: GET bekendId 3x, zoeken 3x, schrijven 3x bij 429, plus DELETE en POST als terugval. */
export const RESERVE_BOEKING = 12;

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
  private readonly totaal: number;
  constructor(totaal = START_BUDGET) {
    this.totaal = totaal;
  }

  get over(): number {
    return this.totaal - this.gebruikt;
  }

  /** Telt één verzoek, of gooit BudgetOp als er niets meer over is. */
  neem(): void {
    if (this.over <= 0) throw new BudgetOp();
    this.gebruikt++;
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
