// Toets (a) voor betalen-run.test.ts: dezelfde toetsen met D1Opslag op node:sqlite.
import { describe } from "node:test";
import { D1ToetsOpslag } from "./d1-toets-opslag.ts";

(globalThis as any).maakToetsOpslag = () => new D1ToetsOpslag();
describe("(a) met D1Opslag", async () => { await import("./betalen-run.test.ts"); });
