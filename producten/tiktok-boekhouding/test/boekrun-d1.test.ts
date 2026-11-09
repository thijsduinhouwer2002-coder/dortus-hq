// Toets (a), ontwerp-d1-worker.md: alle toetsen uit boekrun.test.ts nog eens, nu met D1Opslag op node:sqlite.
import { describe } from "node:test";
import { D1ToetsOpslag } from "./d1-toets-opslag.ts";

(globalThis as any).maakToetsOpslag = () => new D1ToetsOpslag();
describe("(a) met D1Opslag", async () => { await import("./boekrun.test.ts"); });
