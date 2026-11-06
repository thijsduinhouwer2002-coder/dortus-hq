"use strict";
var __defProp = Object.defineProperty;
var __getOwnPropDesc = Object.getOwnPropertyDescriptor;
var __getOwnPropNames = Object.getOwnPropertyNames;
var __hasOwnProp = Object.prototype.hasOwnProperty;
var __export = (target, all) => {
  for (var name in all)
    __defProp(target, name, { get: all[name], enumerable: true });
};
var __copyProps = (to, from, except, desc) => {
  if (from && typeof from === "object" || typeof from === "function") {
    for (let key of __getOwnPropNames(from))
      if (!__hasOwnProp.call(to, key) && key !== except)
        __defProp(to, key, { get: () => from[key], enumerable: !(desc = __getOwnPropDesc(from, key)) || desc.enumerable });
  }
  return to;
};
var __toCommonJS = (mod) => __copyProps(__defProp({}, "__esModule", { value: true }), mod);

// src/main.ts
var main_exports = {};
__export(main_exports, {
  KEPT_RESULTS_LIMIT: () => KEPT_RESULTS_LIMIT,
  default: () => RollwrightPlugin
});
module.exports = __toCommonJS(main_exports);
var import_obsidian8 = require("obsidian");

// src/import/dice-roller-data.ts
var NAME_KEYS = ["alias", "name", "title", "label"];
var FORMULA_KEYS = ["formula", "dice", "value"];
function firstString(entry, keys) {
  for (const key of keys) {
    const value = entry[key];
    if (typeof value === "string" && value.trim() !== "") return value.trim();
  }
  return null;
}
function extractSavedFormulas(jsonText) {
  let data;
  try {
    data = JSON.parse(jsonText);
  } catch (e) {
    return [];
  }
  if (typeof data !== "object" || data === null) return [];
  const found = [];
  for (const [key, value] of Object.entries(data)) {
    if (!key.toLowerCase().includes("formula")) continue;
    if (Array.isArray(value)) {
      for (const entry of value) {
        if (typeof entry !== "object" || entry === null) continue;
        const name = firstString(entry, NAME_KEYS);
        const formula = firstString(entry, FORMULA_KEYS);
        if (name && formula) found.push({ name, formula });
      }
    } else if (typeof value === "object" && value !== null) {
      for (const [name, formula] of Object.entries(value)) {
        if (typeof formula === "string" && formula.trim() !== "") found.push({ name, formula: formula.trim() });
      }
    }
  }
  return found;
}
function mergeFormulas(current, incoming) {
  const names = new Set(current.map((f) => f.name));
  const merged = [...current];
  for (const formula of incoming) {
    if (names.has(formula.name)) continue;
    names.add(formula.name);
    merged.push(formula);
  }
  return { merged, added: merged.length - current.length };
}

// src/pro/license.ts
var KEY_SHAPE = /^RW1-[A-Z2-9]{5}-[A-Z2-9]{5}-[0-9A-F]{6}$/;
function licenseChecksum(body) {
  let hash = 2166136261;
  for (let i = 0; i < body.length; i++) {
    hash ^= body.charCodeAt(i);
    hash = Math.imul(hash, 16777619) >>> 0;
  }
  return (hash >>> 8).toString(16).toUpperCase().padStart(6, "0");
}
function isValidLicenseKey(key) {
  const clean = key.trim().toUpperCase();
  if (!KEY_SHAPE.test(clean)) return false;
  return licenseChecksum(clean.slice(0, clean.lastIndexOf("-"))) === clean.slice(clean.lastIndexOf("-") + 1);
}
var BUY_URL = "";
function shouldShowBuyButton(url = BUY_URL) {
  return url.trim() !== "";
}

// src/pro/skins.ts
var SKINS = [
  { id: "classic", name: "Classic", paid: false, cssClass: "rollwright-skin-classic" },
  { id: "parchment", name: "Parchment", paid: true, cssClass: "rollwright-skin-parchment" },
  { id: "arcane", name: "Arcane", paid: true, cssClass: "rollwright-skin-arcane" }
];
var FREE_SKIN = SKINS[0];
function availableSkins(licensed) {
  return SKINS.filter((skin) => licensed || !skin.paid);
}
function resolveSkin(id, licensed) {
  var _a;
  return (_a = availableSkins(licensed).find((skin) => skin.id === id)) != null ? _a : FREE_SKIN;
}

// src/engine/types.ts
var DiceError = class extends Error {
  constructor(message) {
    super(message);
    this.name = "DiceError";
  }
};
var LIMITS = {
  formulaLength: 1e3,
  parseDepth: 64,
  diceInGroup: 1e3,
  sides: 1e6,
  rollsPerFormula: 1e4,
  /** Upper bound for the repeat count of ! and r, and the meaning of "i". */
  repeats: 100,
  aliasDepth: 8,
  /** Calculation steps per roll, so chains of named formulas cannot run for ages. */
  stepsPerRoll: 1e5,
  /** Picks from tables, lists and notes per roll, nesting included. */
  picksPerRoll: 1e4
};
function newBudget() {
  return { rolls: 0, steps: 0, picks: 0 };
}

// src/engine/tokenizer.ts
var COMPARATORS = [">=", "<=", "=<", "=>", "=!", "=-", "-=", ">", "<", "="];
function isDigit(ch) {
  return ch >= "0" && ch <= "9";
}
function isLetter(ch) {
  return ch >= "a" && ch <= "z" || ch >= "A" && ch <= "Z" || ch === "_";
}
function tokenize(input) {
  const tokens = [];
  let i = 0;
  while (i < input.length) {
    const ch = input.charAt(i);
    if (ch === " " || ch === "	" || ch === "\n" || ch === "{" || ch === "}") {
      i++;
      continue;
    }
    if (isDigit(ch) || ch === "." && isDigit(input.charAt(i + 1))) {
      const start = i;
      while (isDigit(input.charAt(i))) i++;
      if (input.charAt(i) === "." && isDigit(input.charAt(i + 1))) {
        i++;
        while (isDigit(input.charAt(i))) i++;
      }
      tokens.push({ type: "num", value: input.slice(start, i), pos: start });
      continue;
    }
    if (isLetter(ch)) {
      const start = i;
      const afterValue = isAfterValue(tokens);
      while (isLetter(input.charAt(i)) || i > start && isDigit(input.charAt(i)) && !isDiceBoundary(input, start, i, afterValue)) i++;
      tokens.push({ type: "word", value: input.slice(start, i), pos: start });
      continue;
    }
    const comparator = COMPARATORS.find((c) => input.startsWith(c, i));
    if (comparator) {
      tokens.push({ type: "cmp", value: comparator, pos: i });
      i += comparator.length;
      continue;
    }
    if (ch === "!") {
      const double = input.charAt(i + 1) === "!";
      tokens.push({ type: "bang", value: double ? "!!" : "!", pos: i });
      i += double ? 2 : 1;
      continue;
    }
    if ("+-*/^()[],%".includes(ch)) {
      tokens.push({ type: "sym", value: ch, pos: i });
      i++;
      continue;
    }
    throw new DiceError(`Unexpected character "${ch}" at position ${i + 1}`);
  }
  return tokens;
}
function isAfterValue(tokens) {
  const last = tokens[tokens.length - 1];
  if (!last) return false;
  return last.type === "num" || last.type === "word" || last.type === "bang" || last.type === "sym" && (last.value === ")" || last.value === "]" || last.value === "%");
}
function isDiceBoundary(input, start, i, afterValue) {
  const word = input.slice(start, i);
  if (/^[dD]?[fF]?(kh|kl|dh|dl|k|sa|sd|s|u|r|i)*$/.test(word)) return true;
  return afterValue && /^d?f?(kh|kl|dh|dl|k|sa|sd|s|u|r|i)*$/i.test(word);
}

// src/engine/parser.ts
var MODIFIER_WORDS = ["kh", "kl", "dh", "dl", "k", "sa", "sd", "s", "u", "r"];
function isDiceWord(word) {
  if (word.charAt(0) !== "d" && word.charAt(0) !== "D") return false;
  let rest = word.slice(1).toLowerCase();
  if (rest.charAt(0) === "f") rest = rest.slice(1);
  while (rest.length > 0) {
    const match = MODIFIER_WORDS.find((m) => rest.startsWith(m));
    if (!match) return false;
    rest = rest.slice(match.length);
    if (match === "r" && rest.charAt(0) === "i") rest = rest.slice(1);
  }
  return true;
}
function mapComparator(value) {
  switch (value) {
    case "=<":
      return { op: "<=", score: 1 };
    case "=>":
      return { op: ">=", score: 1 };
    case "=!":
      return { op: "!=", score: 1 };
    case "=-":
    case "-=":
      return { op: "=", score: -1 };
    default:
      return { op: value, score: 1 };
  }
}
var Parser = class {
  constructor(tokens, names) {
    this.tokens = tokens;
    this.names = names;
    this.index = 0;
    this.depth = 0;
  }
  parse() {
    if (this.tokens.length === 0) throw new DiceError("The formula is empty");
    const node = this.additive();
    const left = this.peek();
    if (left) throw new DiceError(`Unexpected "${left.value}" at position ${left.pos + 1}`);
    return node;
  }
  peek() {
    return this.tokens[this.index];
  }
  isSym(value) {
    const token = this.peek();
    return (token == null ? void 0 : token.type) === "sym" && token.value === value;
  }
  additive() {
    var _a;
    let left = this.multiplicative();
    while (this.isSym("+") || this.isSym("-")) {
      const op = (_a = this.tokens[this.index++]) == null ? void 0 : _a.value;
      left = { type: "binary", op, left, right: this.multiplicative() };
    }
    return left;
  }
  multiplicative() {
    var _a;
    let left = this.unary();
    while (this.isSym("*") || this.isSym("/")) {
      const op = (_a = this.tokens[this.index++]) == null ? void 0 : _a.value;
      left = { type: "binary", op, left, right: this.unary() };
    }
    return left;
  }
  unary() {
    this.enter();
    let node;
    if (this.isSym("-")) {
      this.index++;
      node = { type: "negate", inner: this.unary() };
    } else if (this.isSym("+")) {
      this.index++;
      node = this.unary();
    } else {
      node = this.power();
    }
    this.depth--;
    return node;
  }
  /** "^" binds tighter than a leading minus and groups from the right. */
  power() {
    const base = this.primary();
    if (this.isSym("^")) {
      this.index++;
      return { type: "binary", op: "^", left: base, right: this.unary() };
    }
    return base;
  }
  enter() {
    if (++this.depth > LIMITS.parseDepth) throw new DiceError("The formula is nested too deeply");
  }
  primary() {
    const token = this.peek();
    if (!token) throw new DiceError("The formula ends too early");
    if (token.type === "num") {
      this.index++;
      const value = Number(token.value);
      if (!Number.isSafeInteger(Math.trunc(value))) throw new DiceError(`The number ${token.value} is too large`);
      const next = this.peek();
      if ((next == null ? void 0 : next.type) === "word" && (next.value.charAt(0) === "d" || next.value.charAt(0) === "D") && isDiceWord(next.value)) {
        return this.dice({ type: "number", value });
      }
      return { type: "number", value };
    }
    if (token.type === "sym" && token.value === "(") {
      this.index++;
      this.enter();
      const inner = this.additive();
      this.depth--;
      if (!this.isSym(")")) throw new DiceError("A closing bracket is missing");
      this.index++;
      const next = this.peek();
      if ((next == null ? void 0 : next.type) === "word" && isDiceWord(next.value)) return this.dice(inner);
      return { type: "group", inner };
    }
    if (token.type === "word") {
      if (this.names.has(token.value)) {
        this.index++;
        return { type: "name", name: token.value };
      }
      if (isDiceWord(token.value)) return this.dice(null);
      this.index++;
      return { type: "name", name: token.value };
    }
    throw new DiceError(`Unexpected "${token.value}" at position ${token.pos + 1}`);
  }
  dice(count) {
    const word = this.peek();
    let rest = word.value.slice(1);
    let sides = { kind: "default" };
    if (rest.charAt(0) === "F" || rest.charAt(0) === "f") {
      sides = { kind: "fudge" };
      rest = rest.slice(1);
    }
    if (rest.length > 0) {
      word.value = rest;
    } else {
      this.index++;
      if (sides.kind === "default") sides = this.sides();
    }
    return { type: "dice", count, sides, modifiers: this.modifiers() };
  }
  sides() {
    const token = this.peek();
    if ((token == null ? void 0 : token.type) === "num") {
      this.index++;
      if (this.isSym("%")) {
        this.index++;
        if (!/^[0-9]+$/.test(token.value)) throw new DiceError("Digit dice need a whole number, such as d66%");
        const digits = token.value.split("").map(Number);
        if (digits.includes(0)) throw new DiceError(`d${token.value}% has a die with zero sides`);
        return { kind: "digits", digits };
      }
      return { kind: "number", sides: this.wholeNumber(token, "The number of sides") };
    }
    if (this.isSym("%")) {
      this.index++;
      return { kind: "percent" };
    }
    if (this.isSym("[")) {
      this.index++;
      return this.bracketSides();
    }
    return { kind: "default" };
  }
  /** Two numbers are a range, both ends included. Three or more are the faces themselves. */
  bracketSides() {
    var _a;
    const values = [];
    for (; ; ) {
      let sign = 1;
      if (this.isSym("-")) {
        sign = -1;
        this.index++;
      }
      const token = this.peek();
      if ((token == null ? void 0 : token.type) !== "num") throw new DiceError("Write custom dice as d[min, max] or d[a, b, c]");
      this.index++;
      values.push(sign * this.wholeNumber(token, "A face"));
      if (this.isSym("]")) {
        this.index++;
        break;
      }
      if (this.isSym(",") || this.isSym("-")) {
        if (this.isSym(",")) this.index++;
        else if (((_a = this.tokens[this.index + 1]) == null ? void 0 : _a.type) === "num") this.index++;
        continue;
      }
      throw new DiceError("Write custom dice as d[min, max] or d[a, b, c]");
    }
    const [first, second] = values;
    if (first === void 0 || second === void 0) throw new DiceError("Custom dice need at least two numbers");
    if (values.length === 2) return { kind: "range", min: Math.min(first, second), max: Math.max(first, second) };
    return { kind: "faces", faces: values };
  }
  wholeNumber(token, what) {
    const value = Number(token.value);
    if (!Number.isInteger(value)) throw new DiceError(`${what} must be a whole number, not ${token.value}`);
    return value;
  }
  modifiers() {
    const modifiers = [];
    for (; ; ) {
      const token = this.peek();
      if (!token) return modifiers;
      if (token.type === "bang") {
        this.index++;
        const times = this.repeatCount();
        modifiers.push({ kind: "explode", combine: token.value === "!!", times, conditions: this.conditions() });
      } else if (token.type === "cmp") {
        modifiers.push(this.countModifier());
      } else if (token.type === "word") {
        const lower = token.value.toLowerCase();
        const match = MODIFIER_WORDS.find((m) => lower.startsWith(m));
        if (!match) throw new DiceError(`Unknown modifier "${token.value}" at position ${token.pos + 1}`);
        this.consumeWordPart(token, match.length);
        modifiers.push(this.wordModifier(match));
      } else {
        return modifiers;
      }
    }
  }
  consumeWordPart(token, length) {
    token.value = token.value.slice(length);
    token.pos += length;
    if (token.value.length === 0) this.index++;
  }
  wordModifier(word) {
    switch (word) {
      case "k":
      case "kh":
        return { kind: "keep", which: "high", count: this.optionalCount() };
      case "kl":
        return { kind: "keep", which: "low", count: this.optionalCount() };
      case "dh":
        return { kind: "drop", which: "high", count: this.optionalCount() };
      case "dl":
        return { kind: "drop", which: "low", count: this.optionalCount() };
      case "s":
      case "sa":
        return { kind: "sort", direction: "asc" };
      case "sd":
        return { kind: "sort", direction: "desc" };
      case "u":
        return { kind: "unique" };
      default: {
        const times = this.repeatCount();
        return { kind: "reroll", times, conditions: this.conditions() };
      }
    }
  }
  optionalCount() {
    const token = this.peek();
    if ((token == null ? void 0 : token.type) !== "num") return 1;
    this.index++;
    return this.wholeNumber(token, "The modifier count");
  }
  /** The number after ! or r, or "i" for the highest allowed. */
  repeatCount() {
    const token = this.peek();
    if ((token == null ? void 0 : token.type) === "word" && token.value.charAt(0).toLowerCase() === "i") {
      this.consumeWordPart(token, 1);
      return LIMITS.repeats;
    }
    const count = this.optionalCount();
    if (count > LIMITS.repeats) throw new DiceError(`A die can repeat at most ${LIMITS.repeats} times`);
    return count;
  }
  /** Conditions right after ! or r belong to that modifier. */
  conditions() {
    const conditions = [];
    for (; ; ) {
      const token = this.peek();
      if ((token == null ? void 0 : token.type) !== "cmp") return conditions;
      const { op, score } = mapComparator(token.value);
      if (score === -1) throw new DiceError(`"${token.value}" only works for counting, not on ! or r`);
      this.index++;
      const value = this.peek();
      if ((value == null ? void 0 : value.type) !== "num") throw new DiceError(`A number is missing after "${token.value}"`);
      this.index++;
      conditions.push({ op, value: Number(value.value) });
    }
  }
  countModifier() {
    const token = this.peek();
    this.index++;
    const { op, score } = mapComparator(token.value);
    return { kind: "count", op, score, threshold: this.threshold(token.value) };
  }
  /** A number or plain dice. Modifiers after it belong to the outer dice. */
  threshold(comparator) {
    const token = this.peek();
    if ((token == null ? void 0 : token.type) === "num") {
      this.index++;
      const value = Number(token.value);
      const next = this.peek();
      if ((next == null ? void 0 : next.type) === "word" && next.value.toLowerCase() === "d") {
        this.index++;
        return { type: "dice", count: { type: "number", value }, sides: this.sides(), modifiers: [] };
      }
      return { type: "number", value };
    }
    if ((token == null ? void 0 : token.type) === "word" && token.value.toLowerCase() === "d") {
      this.index++;
      return { type: "dice", count: null, sides: this.sides(), modifiers: [] };
    }
    throw new DiceError(`A number is missing after "${comparator}"`);
  }
};
function parseFormula(formula, names = []) {
  if (formula.length > LIMITS.formulaLength) {
    throw new DiceError(`The formula is longer than ${LIMITS.formulaLength} characters`);
  }
  return new Parser(tokenize(formula), new Set(names)).parse();
}

// src/engine/format.ts
function formatNumber(value) {
  if (value === Infinity) return "\u221E";
  if (value === -Infinity) return "-\u221E";
  const rounded = Math.round(value * 100) / 100;
  if (!Number.isFinite(rounded)) return String(value);
  return String(rounded === 0 ? 0 : rounded);
}
function roundNumber(value, mode) {
  if (mode === void 0 || !Number.isFinite(value)) return value;
  if (mode === "ceil") return Math.ceil(value);
  if (mode === "floor") return Math.floor(value);
  return Math.sign(value) * Math.round(Math.abs(value));
}
function formatResult(value, style = {}) {
  const shown = formatNumber(roundNumber(value, style.round));
  const signed = style.signed && !shown.startsWith("-") ? `+${shown}` : shown;
  return style.paren ? `(${signed})` : signed;
}

// src/engine/random.ts
var defaultRandom = (min, max) => min + Math.floor(Math.random() * (max - min + 1));

// src/engine/evaluate.ts
function range(min, max) {
  return { min, max, size: max - min + 1, mean: (min + max) / 2, roll: (random) => ({ value: random(min, max) }) };
}
function resolveFaces(sides, state) {
  switch (sides.kind) {
    case "default":
      return checkedSides(state.defaultSides);
    case "number":
      return checkedSides(sides.sides);
    case "percent":
      return range(1, 100);
    case "range":
      return checkedSpan(sides.min, sides.max);
    case "fudge":
      return {
        min: -1,
        max: 1,
        size: 3,
        mean: 0,
        roll: (random) => {
          const value = random(-1, 1);
          return { value, label: value > 0 ? "+" : value < 0 ? "-" : "0" };
        }
      };
    case "faces": {
      const faces = sides.faces;
      if (faces.length > LIMITS.diceInGroup) throw new DiceError("A custom die has too many faces");
      return {
        min: Math.min(...faces),
        max: Math.max(...faces),
        size: new Set(faces).size,
        mean: faces.reduce((a, b) => a + b, 0) / faces.length,
        roll: (random) => ({ value: faces[random(0, faces.length - 1)] })
      };
    }
    case "digits": {
      const digits = sides.digits;
      const join = (values) => Number(values.join(""));
      return {
        min: join(digits.map(() => 1)),
        max: join(digits),
        size: digits.reduce((a, b) => a * b, 1),
        mean: digits.reduce((sum, d) => sum * 10 + (d + 1) / 2, 0),
        roll: (random) => {
          const values = digits.map((d) => random(1, d));
          return { value: join(values), label: values.join(",") };
        }
      };
    }
  }
}
function checkedSides(sides) {
  if (!Number.isInteger(sides) || sides < 1) throw new DiceError(`A die needs at least 1 side, not ${sides}`);
  if (sides > LIMITS.sides) throw new DiceError(`A die can have at most ${LIMITS.sides} sides`);
  return range(1, sides);
}
function checkedSpan(min, max) {
  if (max - min + 1 > LIMITS.sides) throw new DiceError(`A die can have at most ${LIMITS.sides} sides`);
  return range(min, max);
}
function compare(value, op, target) {
  switch (op) {
    case "=":
      return value === target;
    case "!=":
      return value !== target;
    case ">":
      return value > target;
    case "<":
      return value < target;
    case ">=":
      return value >= target;
    case "<=":
      return value <= target;
  }
}
function matchesAny(value, conditions) {
  return conditions.some((c) => compare(value, c.op, c.value));
}
function spend(state) {
  if (++state.budget.rolls > LIMITS.rollsPerFormula) {
    throw new DiceError(`This formula rolls more than ${LIMITS.rollsPerFormula} dice`);
  }
}
function rollDie(faces, state) {
  spend(state);
  return faces.roll(state.random);
}
function applyKeepDrop(dice, mod) {
  const active = dice.filter((d) => !d.dropped).sort((a, b) => a.value - b.value);
  const wanted = Math.min(mod.count, active.length);
  let toDrop;
  if (mod.kind === "keep") {
    toDrop = mod.which === "high" ? active.slice(0, active.length - wanted) : active.slice(wanted);
  } else {
    toDrop = mod.which === "low" ? active.slice(0, wanted) : active.slice(active.length - wanted);
  }
  for (const die of toDrop) die.dropped = true;
}
function applyExplode(dice, mod, faces, state) {
  const conditions = mod.conditions.length > 0 ? mod.conditions : [{ op: "=", value: faces.max }];
  const output = [];
  for (const die of dice) {
    output.push(die);
    if (die.dropped) continue;
    let current = die;
    for (let i = 0; i < mod.times && matchesAny(current.value, conditions); i++) {
      current.exploded = true;
      const extra = rollDie(faces, state);
      if (mod.combine) {
        die.value += extra.value;
        die.label = void 0;
      } else {
        output.push(extra);
      }
      current = mod.combine ? { value: extra.value } : extra;
    }
  }
  return output;
}
function applyReroll(dice, mod, faces, state) {
  const conditions = mod.conditions.length > 0 ? mod.conditions : [{ op: "=", value: faces.min }];
  for (const die of dice) {
    if (die.dropped) continue;
    for (let i = 0; i < mod.times && matchesAny(die.value, conditions); i++) {
      const next = rollDie(faces, state);
      die.value = next.value;
      die.label = next.label;
      die.rerolled = true;
    }
  }
}
function applyUnique(dice, faces, state) {
  const active = dice.filter((d) => !d.dropped);
  if (active.length > faces.size) {
    throw new DiceError(`${active.length} dice cannot all differ: there are only ${faces.size} results`);
  }
  const seen = /* @__PURE__ */ new Set();
  for (const die of active) {
    while (seen.has(die.value)) {
      const next = rollDie(faces, state);
      die.value = next.value;
      die.label = next.label;
      die.rerolled = true;
    }
    seen.add(die.value);
  }
}
function showDie(die) {
  var _a;
  let text = (_a = die.label) != null ? _a : formatNumber(die.value);
  if (die.dropped) text += "d";
  if (die.exploded) text += "!";
  if (die.rerolled) text += "r";
  if (die.score === 1) text += "*";
  if (die.score === -1) text += "-";
  return text;
}
function evaluateDice(node, state) {
  const count = node.count ? evaluate(node.count, state).value : state.defaultCount;
  if (!Number.isInteger(count)) throw new DiceError(`The number of dice must be whole, not ${formatNumber(count)}`);
  if (count < 0) throw new DiceError(`The number of dice cannot be negative (${count})`);
  if (count > LIMITS.diceInGroup) throw new DiceError(`At most ${LIMITS.diceInGroup} dice can be rolled at once, not ${count}`);
  const faces = resolveFaces(node.sides, state);
  let dice = [];
  for (let i = 0; i < count; i++) dice.push(rollDie(faces, state));
  const counting = [];
  for (const mod of node.modifiers) {
    switch (mod.kind) {
      case "keep":
      case "drop":
        applyKeepDrop(dice, mod);
        break;
      case "explode":
        dice = applyExplode(dice, mod, faces, state);
        break;
      case "reroll":
        applyReroll(dice, mod, faces, state);
        break;
      case "unique":
        applyUnique(dice, faces, state);
        break;
      case "sort":
        dice = [...dice].sort((a, b) => mod.direction === "asc" ? a.value - b.value : b.value - a.value);
        break;
      case "count":
        counting.push(mod);
        break;
    }
  }
  const active = dice.filter((d) => !d.dropped);
  let value;
  if (counting.length > 0) {
    const targets = counting.map((c) => ({ c, target: evaluate(c.threshold, state).value }));
    for (const die of active) {
      const hit = targets.find(({ c, target }) => compare(die.value, c.op, target));
      die.score = hit ? hit.c.score : 0;
    }
    value = active.reduce((sum, d) => {
      var _a;
      return sum + ((_a = d.score) != null ? _a : 0);
    }, 0);
  } else {
    value = active.reduce((sum, d) => sum + d.value, 0);
    if (!Number.isFinite(value)) throw new DiceError("The result is too large to show");
  }
  return { value, text: `[${dice.map(showDie).join(", ")}]` };
}
function lookupName(names, name) {
  return names && Object.prototype.hasOwnProperty.call(names, name) ? names[name] : void 0;
}
function insideName(name, state, work) {
  const formula = lookupName(state.names, name);
  if (formula === void 0) throw new DiceError(`Unknown name "${name}"`);
  if (state.aliasStack.includes(name) || state.aliasStack.length >= LIMITS.aliasDepth) {
    throw new DiceError(`The named formula "${name}" refers to itself`);
  }
  state.aliasStack.push(name);
  const result = work(parseFormula(formula, Object.keys(state.names)));
  state.aliasStack.pop();
  return result;
}
function evaluateName(name, state) {
  return insideName(name, state, (node) => evaluate(node, state));
}
function spendStep(budget) {
  if (++budget.steps > LIMITS.stepsPerRoll) throw new DiceError("This formula is too complex to work out");
}
function evaluate(node, state) {
  spendStep(state.budget);
  switch (node.type) {
    case "number":
      return { value: node.value, text: formatNumber(node.value) };
    case "name":
      return evaluateName(node.name, state);
    case "negate": {
      const inner = evaluate(node.inner, state);
      return { value: -inner.value, text: `-${inner.text}` };
    }
    case "group": {
      const inner = evaluate(node.inner, state);
      return { value: inner.value, text: `(${inner.text})` };
    }
    case "dice":
      return evaluateDice(node, state);
    case "binary": {
      const left = evaluate(node.left, state);
      const right = evaluate(node.right, state);
      return { value: calculate(node.op, left.value, right.value), text: `${left.text} ${node.op} ${right.text}` };
    }
  }
}
function calculate(op, a, b) {
  let value;
  switch (op) {
    case "+":
      value = a + b;
      break;
    case "-":
      value = a - b;
      break;
    case "*":
      value = a * b;
      break;
    case "/":
      if (b === 0) throw new DiceError("Cannot divide by zero");
      value = a / b;
      break;
    default:
      value = Math.pow(a, b);
  }
  if (!Number.isFinite(value)) throw new DiceError("The result is too large to show");
  return value;
}
function makeState(options) {
  var _a, _b, _c, _d, _e;
  return {
    random: (_a = options.random) != null ? _a : defaultRandom,
    defaultSides: (_b = options.defaultSides) != null ? _b : 100,
    defaultCount: (_c = options.defaultCount) != null ? _c : 1,
    names: (_d = options.names) != null ? _d : {},
    budget: (_e = options.budget) != null ? _e : newBudget(),
    aliasStack: []
  };
}
function roll(formula, options = {}) {
  var _a;
  const node = parseFormula(formula, Object.keys((_a = options.names) != null ? _a : {}));
  const { value, text } = evaluate(node, makeState(options));
  return { formula: formula.trim(), total: value, breakdown: text };
}
function constant(value) {
  return { mean: value, min: value, max: value, whole: Number.isInteger(value) };
}
function isConstant(spread) {
  return spread.min === spread.max;
}
function corners(a, b) {
  const products = [a.min * b.min, a.min * b.max, a.max * b.min, a.max * b.max];
  return { min: Math.min(...products), max: Math.max(...products) };
}
function exactSpread(node, state) {
  spendStep(state.budget);
  switch (node.type) {
    case "number":
      return constant(node.value);
    case "name":
      return insideName(node.name, state, (inner) => exactSpread(inner, state));
    case "group":
      return exactSpread(node.inner, state);
    case "negate": {
      const inner = exactSpread(node.inner, state);
      return inner && { mean: -inner.mean, min: -inner.max, max: -inner.min, whole: inner.whole };
    }
    case "dice":
      return exactDice(node, state);
    case "binary": {
      const left = exactSpread(node.left, state);
      if (!left) return null;
      const right = exactSpread(node.right, state);
      if (!right) return null;
      switch (node.op) {
        case "+":
          return { mean: calculate("+", left.mean, right.mean), min: left.min + right.min, max: left.max + right.max, whole: left.whole && right.whole };
        case "-":
          return { mean: calculate("-", left.mean, right.mean), min: left.min - right.max, max: left.max - right.min, whole: left.whole && right.whole };
        case "*":
          return { mean: calculate("*", left.mean, right.mean), ...corners(left, right), whole: left.whole && right.whole };
        case "/": {
          if (!isConstant(right)) return null;
          const mean = calculate("/", left.mean, right.mean);
          const ends = [left.min / right.mean, left.max / right.mean];
          return { mean, min: Math.min(...ends), max: Math.max(...ends), whole: isConstant(left) && Number.isInteger(mean) };
        }
        case "^":
          return isConstant(left) && isConstant(right) ? constant(calculate("^", left.mean, right.mean)) : null;
      }
    }
  }
}
function exactDice(node, state) {
  if (node.modifiers.length > 0) return null;
  const count = node.count ? exactSpread(node.count, state) : constant(state.defaultCount);
  if (!count || !count.whole || count.min < 0 || count.max > LIMITS.diceInGroup) return null;
  const faces = resolveFaces(node.sides, state);
  const facesSpread = { mean: faces.mean, min: faces.min, max: faces.max, whole: true };
  return { mean: calculate("*", count.mean, faces.mean), ...corners(count, facesSpread), whole: true };
}
var AVERAGE_SAMPLES = 2e3;
function averageOf(formula, options = {}) {
  var _a;
  const node = parseFormula(formula, Object.keys((_a = options.names) != null ? _a : {}));
  const exact = exactSpread(node, makeState({ ...options, budget: void 0 }));
  if (exact) return { value: exact.mean, exact: true };
  let mean = 0;
  let samples = 0;
  const budget = newBudget();
  for (; samples < AVERAGE_SAMPLES; samples++) {
    try {
      mean += (evaluate(node, makeState({ ...options, budget })).value - mean) / (samples + 1);
    } catch (error) {
      const spent = budget.rolls > LIMITS.rollsPerFormula || budget.steps > LIMITS.stepsPerRoll;
      if (!spent || samples === 0) throw error;
      break;
    }
  }
  return { value: mean, exact: false };
}

// src/rollers/fields.ts
var NOTATION_WORD = /^d?f?(kh|kl|dh|dl|k|sa|sd|s|u|r|i)*$/i;
var NUMBER_TEXT = /^-?\d+(\.\d+)?$/;
function usableName(name) {
  var _a;
  if (NOTATION_WORD.test(name)) return false;
  try {
    const tokens = tokenize(name);
    return tokens.length === 1 && ((_a = tokens[0]) == null ? void 0 : _a.type) === "word" && tokens[0].value === name;
  } catch (e) {
    return false;
  }
}
function numberText(value) {
  if (typeof value !== "number" && typeof value !== "string") return void 0;
  const text = typeof value === "number" ? String(value) : value.trim();
  return NUMBER_TEXT.test(text) && Number.isFinite(Number(text)) ? text : void 0;
}
function fieldNames(frontmatter) {
  const names = {};
  if (typeof frontmatter !== "object" || frontmatter === null || Array.isArray(frontmatter)) return names;
  for (const [name, value] of Object.entries(frontmatter)) {
    const text = numberText(value);
    if (text !== void 0 && name !== "__proto__" && usableName(name)) names[name] = text;
  }
  return names;
}

// src/rollers/defuse.ts
var IMAGE = /\.(avif|bmp|gif|jpe?g|png|svg|webp)$/i;
function isImage(target) {
  var _a, _b;
  const path = (_b = ((_a = target.split("|")[0]) != null ? _a : "").split("#")[0]) != null ? _b : "";
  return IMAGE.test(path.trim());
}
var CODE = /\\[\s\S]|`+[\s>]*dice\s*(?:[+-]|-\s*mod)?\s*:|<code\b[^>]*>[\s\S]*?(?:<\/code>|$)/gi;
function defuseRolls(markdown) {
  return markdown.replace(/!\[\[([^\]]+)\]\]/g, (whole, target) => isImage(target) ? whole : `[[${target}]]`).replace(
    /!\[([^\]]*)\]\(([^()]*)\)/g,
    (whole, label, target) => isImage(target) || /^https?:/i.test(target) ? whole : `[${label}](${target})`
  ).replace(CODE, (whole) => whole.replace(/(dice\s*(?:[+-]|-\s*mod)?)(\s*:)/gi, "$1\u200B$2"));
}

// src/rollers/inline.ts
function findInlineDice(line) {
  const found = [];
  const pattern = /\\[\s\S]|(`+)([^`]*)\1/g;
  for (let match = pattern.exec(line); match; match = pattern.exec(line)) {
    if (match[1] === void 0) continue;
    const code = readDiceCode(match[2]);
    if (match[1].length === 1 && code !== null) {
      found.push({ from: match.index, to: match.index + match[0].length, formula: code.formula, keep: code.keep, modify: code.modify === true });
    }
  }
  return found;
}
function readDiceCode(text) {
  var _a;
  const match = /^dice(-mod|[+-])?:\s*(.*\S)\s*$/i.exec(text.trim());
  if (!match) return null;
  const prefix = ((_a = match[1]) != null ? _a : "").toLowerCase();
  const code = { formula: match[2], keep: prefix === "+" };
  if (prefix === "-mod") code.modify = true;
  return code;
}

// src/rollers/modify.ts
function oneLine(text) {
  return text.replace(/\s*[\r\n]\s*/g, " ").trim();
}
function modifiedText(outcome, showFormula) {
  if (outcome.kind !== "dice") return oneLine(defuseRolls(outcome.text));
  const total = `${outcome.estimated ? "~" : ""}${outcome.total === void 0 ? outcome.text : formatResult(outcome.total, outcome.flags)}`;
  const parts = [];
  if (showFormula) parts.push(outcome.formula.trim());
  const breakdown = outcome.average ? "" : outcome.details.trim();
  if (breakdown !== "") parts.push(breakdown);
  parts.push(total);
  return oneLine(defuseRolls(parts.join(" -> ")));
}
function escapeAll(text, char) {
  const pattern = char === "`" ? /(\\*)`/g : /(\\*)\|/g;
  return text.replace(pattern, (whole, slashes) => slashes.length % 2 === 0 ? `${slashes}\\${char}` : whole);
}
function hasBarePipe(text) {
  return /(^|[^\\])(\\\\)*\|/.test(text);
}
var BLOCK_START = /^(?:[#>\-+*=_~|<]|\[[^\]]*\]:)/;
function fitReplacement(line, from, to, text) {
  let safe = escapeAll(text, "`");
  const rest = line.slice(0, from) + line.slice(to);
  if (rest.replace(/^[\s>]*/, "").startsWith("|") || hasBarePipe(rest)) safe = escapeAll(safe, "|");
  if (/^(?:\s|>|[-+*](?=\s)|\d+[.)](?=\s))*$/.test(line.slice(0, from))) {
    if (BLOCK_START.test(safe)) safe = `\\${safe}`;
    else safe = safe.replace(/^(\d+)([.)])/, "$1\\$2");
  }
  return safe;
}
function replaceCodeInLine(lineText, index, formula, replacement) {
  const code = findInlineDice(lineText)[index];
  if (!code || !code.modify || code.formula !== formula) return null;
  return lineText.slice(0, code.from) + fitReplacement(lineText, code.from, code.to, replacement) + lineText.slice(code.to);
}
function replacementAt(lineText, column, formula, replacement) {
  const code = findInlineDice(lineText).find((found) => found.from === column);
  if (!code || !code.modify || code.formula !== formula) return null;
  return { from: code.from, to: code.to, insert: fitReplacement(lineText, code.from, code.to, replacement) };
}
function replaceCodeInNote(markdown, line, index, formula, replacement) {
  const lines = markdown.split("\n");
  const text = lines[line];
  if (text === void 0) return null;
  const replaced = replaceCodeInLine(text, index, formula, replacement);
  if (replaced === null) return null;
  lines[line] = replaced;
  return lines.join("\n");
}

// src/rollers/markdown.ts
var TRAILING_ID = /\s\^([A-Za-z0-9-]+)\s*$/;
var ID_ONLY = /^\^([A-Za-z0-9-]+)\s*$/;
var HEADING = /^(#{1,6})\s/;
var THEMATIC = /^ {0,3}(\*{3,}|-{3,}|_{3,})\s*$/;
var LIST_ITEM = /^(\s*)([-*+]|\d+[.)])\s/;
var FENCE = /^ {0,3}(`{3,}|~{3,})/;
var HTML = /^<[a-zA-Z/!]/;
var FOOTNOTE = /^\[\^[^\]]+\]:/;
var DEFINITION = /^\[[^\]]+\]:/;
var RULE_CELL = /^:?-+:?$/;
function isTableRule(line) {
  let text = line.trim();
  if (text.startsWith("|")) text = text.slice(1);
  if (text.endsWith("|")) text = text.slice(0, -1);
  return text.split("|").every((cell) => RULE_CELL.test(cell.trim()));
}
function startsBlock(line, next) {
  return HEADING.test(line) || THEMATIC.test(line) || LIST_ITEM.test(line) || FENCE.test(line) || line.startsWith(">") || line.includes("|") && next !== void 0 && next.includes("-") && isTableRule(next);
}
function finish(type, lines, level) {
  var _a;
  const block = { type, text: lines.join("\n") };
  if (level !== void 0) block.level = level;
  const last = (_a = lines[lines.length - 1]) != null ? _a : "";
  const match = type === "code" ? null : TRAILING_ID.exec(last);
  if (match) {
    block.id = match[1];
    block.text = block.text.replace(TRAILING_ID, "");
  }
  return block;
}
function parseBlocks(markdown) {
  var _a;
  const lines = markdown.replace(/\r\n/g, "\n").split("\n");
  const blocks = [];
  let i = 0;
  if (((_a = lines[0]) == null ? void 0 : _a.trim()) === "---") {
    const end = lines.findIndex((line, index) => index > 0 && line.trim() === "---");
    if (end > 0) {
      blocks.push({ type: "yaml", text: lines.slice(1, end).join("\n") });
      i = end + 1;
    }
  }
  while (i < lines.length) {
    const line = lines[i];
    const next = lines[i + 1];
    if (line.trim() === "") {
      i++;
      continue;
    }
    const idOnly = ID_ONLY.exec(line);
    const previous = blocks[blocks.length - 1];
    if (idOnly && previous) {
      previous.id = idOnly[1];
      i++;
      continue;
    }
    const heading = HEADING.exec(line);
    const fence = FENCE.exec(line);
    if (heading) {
      blocks.push(finish("heading", [line], heading[1].length));
      i++;
    } else if (fence) {
      const marker = fence[1];
      const body = [line];
      i++;
      while (i < lines.length) {
        const current = lines[i];
        body.push(current);
        i++;
        if (current.trim().startsWith(marker)) break;
      }
      blocks.push(finish("code", body));
    } else if (THEMATIC.test(line)) {
      blocks.push({ type: "thematicBreak", text: line });
      i++;
    } else if (line.includes("|") && next !== void 0 && next.includes("-") && isTableRule(next)) {
      const body = [line, next];
      i += 2;
      while (i < lines.length && lines[i].includes("|") && !ID_ONLY.test(lines[i])) {
        body.push(lines[i]);
        i++;
      }
      blocks.push(finish("table", body));
    } else if (line.startsWith(">")) {
      const body = [];
      while (i < lines.length && lines[i].startsWith(">")) {
        body.push(lines[i]);
        i++;
      }
      blocks.push(finish(/^>\s*\[!/.test(line) ? "callout" : "blockquote", body));
    } else if (LIST_ITEM.test(line)) {
      const body = [];
      while (i < lines.length) {
        const current = lines[i];
        if (current.trim() === "" || ID_ONLY.test(current)) break;
        if (!LIST_ITEM.test(current) && !/^\s/.test(current)) break;
        body.push(current);
        i++;
      }
      blocks.push(finish("list", body));
    } else if (FOOTNOTE.test(line)) {
      blocks.push(finish("footnoteDefinition", [line]));
      i++;
    } else if (DEFINITION.test(line)) {
      blocks.push(finish("definition", [line]));
      i++;
    } else if (HTML.test(line)) {
      const body = [];
      while (i < lines.length && lines[i].trim() !== "") {
        body.push(lines[i]);
        i++;
      }
      blocks.push(finish("html", body));
    } else {
      const body = [line];
      i++;
      while (i < lines.length) {
        const current = lines[i];
        if (current.trim() === "" || ID_ONLY.test(current) || startsBlock(current, lines[i + 1])) break;
        body.push(current);
        i++;
      }
      blocks.push(finish("paragraph", body));
    }
  }
  return blocks;
}
function listItems(listText) {
  var _a, _b, _c, _d, _e;
  const lines = listText.split("\n");
  const indent = (_d = (_c = (_b = LIST_ITEM.exec((_a = lines[0]) != null ? _a : "")) == null ? void 0 : _b[1]) == null ? void 0 : _c.length) != null ? _d : 0;
  const items = [];
  for (const line of lines) {
    const match = LIST_ITEM.exec(line);
    if (match && match[1].length <= indent) items.push([line]);
    else (_e = items[items.length - 1]) == null ? void 0 : _e.push(line);
  }
  return items.map((item) => item.join("\n").replace(LIST_ITEM, "").trim());
}
function noteLines(markdown) {
  var _a;
  const lines = markdown.replace(/\r\n/g, "\n").split("\n");
  let start = 0;
  if (((_a = lines[0]) == null ? void 0 : _a.trim()) === "---") {
    const end = lines.findIndex((line, index) => index > 0 && line.trim() === "---");
    if (end > 0) start = end + 1;
  }
  return lines.slice(start).filter((line) => line.trim() !== "");
}

// src/rollers/spec.ts
var IGNORED_FLAGS = /* @__PURE__ */ new Set(["dice", "render", "norender", "noform"]);
function applyNumberFlag(flags, lower) {
  if (lower === "round" || lower === "ceil" || lower === "floor") flags.round = lower;
  else if (lower === "noround") delete flags.round;
  else if (lower === "signed") flags.signed = true;
  else if (lower === "paren") flags.paren = true;
  else if (lower === "noparen") delete flags.paren;
  else return false;
  return true;
}
function splitPipes(raw) {
  const parts = [];
  let depth = 0;
  let current = "";
  for (const ch of raw) {
    if (ch === "(" || ch === "[") depth++;
    if ((ch === ")" || ch === "]") && depth > 0) depth--;
    if (ch === "|" && depth === 0) {
      parts.push(current);
      current = "";
    } else {
      current += ch;
    }
  }
  parts.push(current);
  return parts.map((part) => part.trim());
}
function decodeLink(link) {
  try {
    return decodeURI(link);
  } catch (e) {
    return link;
  }
}
function parseLink(head) {
  let prefix;
  let link;
  const wiki = /^(.*?)\[\[(.+?)\]\]$/.exec(head);
  const markdown = /^(.*?)\[[^\][]*\]\(([^()]+)\)$/.exec(head);
  if (wiki) {
    prefix = wiki[1];
    link = wiki[2].split("|")[0];
  } else if (markdown) {
    prefix = markdown[1];
    link = decodeLink(markdown[2]);
  } else {
    return null;
  }
  const caret = link.indexOf("^");
  if (caret === -1) return { prefix: prefix.trim(), note: link.trim() };
  const note = link.slice(0, caret).replace(/#$/, "").trim();
  return { prefix: prefix.trim(), note, blockId: link.slice(caret + 1).trim() };
}
function withoutFlag(flags, word) {
  const lower = word.toLowerCase();
  const output = { ...flags };
  if (lower === "nodice" || lower === "form" || lower === "avg" || lower === "none") output[lower] = false;
  else if (lower.startsWith("text(")) delete output.text;
  else if (lower === "round" || lower === "ceil" || lower === "floor") delete output.round;
  else if (lower === "signed") delete output.signed;
  else if (lower === "paren") delete output.paren;
  return output;
}
function parseSpec(raw, aliases = {}) {
  var _a;
  const [first = "", ...rest] = splitPipes(raw);
  const alias = Object.prototype.hasOwnProperty.call(aliases, first) ? aliases[first] : void 0;
  const pipes = splitPipes(alias !== void 0 && !alias.includes(first) ? alias : first);
  const body = (_a = pipes[0]) != null ? _a : "";
  const flags = { nodice: false, form: false, avg: false, none: false };
  const args = [];
  const parts = [...pipes.slice(1), ...rest].filter((part) => part !== "");
  for (const part of parts) {
    const lower = part.toLowerCase();
    if (lower === "nodice" || lower === "form" || lower === "avg" || lower === "none") {
      flags[lower] = true;
    } else if (lower.startsWith("text(") && part.endsWith(")")) {
      flags.text = part.slice(5, -1);
    } else if (!applyNumberFlag(flags, lower) && !IGNORED_FLAGS.has(lower)) {
      args.push(part);
    }
  }
  const link = parseLink(body);
  if (link) return { raw, flags, args, parts, target: { kind: "note", ...link } };
  const tag = /^(.*?)#([^\s#]+)$/.exec(body);
  if (tag) return { raw, flags, args, parts, target: { kind: "tag", prefix: tag[1].trim(), tag: tag[2] } };
  if (args.length > 0) throw new DiceError(`Unknown flag "${args[0]}"`);
  return { raw, flags, args, parts, target: { kind: "dice", formula: body } };
}

// src/rollers/table.ts
function splitRow(line) {
  let text = line.trim();
  if (text.startsWith("|")) text = text.slice(1);
  if (text.endsWith("|") && !text.endsWith("\\|")) text = text.slice(0, -1);
  const cells = [];
  let current = "";
  for (let i = 0; i < text.length; i++) {
    const ch = text.charAt(i);
    if (ch === "\\" && text.charAt(i + 1) === "|") {
      current += "|";
      i++;
    } else if (ch === "|") {
      cells.push(current.trim());
      current = "";
    } else {
      current += ch;
    }
  }
  cells.push(current.trim());
  return cells;
}
function parseTable(markdown) {
  const lines = markdown.split("\n").filter((line) => line.trim() !== "");
  const [head, , ...body] = lines;
  return { headers: splitRow(head != null ? head : ""), rows: body.map(splitRow) };
}
function lookupFormula(table) {
  var _a;
  const first = ((_a = table.headers[0]) != null ? _a : "").replace(/`/g, "").trim();
  const match = /^dice[+-]?:\s*(.+)$/i.exec(first);
  return match ? match[1].trim() : null;
}
function parseRowRanges(label) {
  const ranges = [];
  for (const raw of label.split(",")) {
    const part = raw.trim();
    const match = /^(-?\d+)(?:\s*[-–—]\s*(-?\d+))?$/.exec(part);
    if (!match) return null;
    const low = Number(match[1]);
    const high = match[2] === void 0 ? low : Number(match[2]);
    ranges.push([Math.min(low, high), Math.max(low, high)]);
  }
  return ranges;
}
function findLookupRow(table, value) {
  return table.rows.find((row) => {
    var _a, _b;
    const ranges = parseRowRanges((_a = row[0]) != null ? _a : "");
    return (_b = ranges == null ? void 0 : ranges.some(([low, high]) => value >= low && value <= high)) != null ? _b : false;
  });
}
function findColumn(table, name) {
  const wanted = name.trim().toLowerCase();
  return table.headers.findIndex((header) => header.trim().toLowerCase() === wanted);
}

// src/rollers/run.ts
var MAX_NESTING = 8;
var MAX_PICKS = 100;
var BLOCK_TYPES = /* @__PURE__ */ new Set([
  "blockquote",
  "break",
  "callout",
  "code",
  "delete",
  "emphasis",
  "footnoteReference",
  "footnote",
  "heading",
  "html",
  "imageReference",
  "image",
  "inlineCode",
  "linkReference",
  "link",
  "listItem",
  "list",
  "paragraph",
  "root",
  "strong",
  "table",
  "text",
  "thematicBreak",
  "toml",
  "yaml",
  "definition",
  "footnoteDefinition"
]);
function spendPick(context) {
  if (context.budget && ++context.budget.picks > LIMITS.picksPerRoll) {
    throw new DiceError(`This roll picks more than ${LIMITS.picksPerRoll} results`);
  }
}
function pick(items, random) {
  return items[random(0, items.length - 1)];
}
function diceOptions(context) {
  var _a;
  return {
    random: (_a = context.random) != null ? _a : defaultRandom,
    defaultSides: context.defaultSides,
    defaultCount: context.defaultCount,
    names: context.aliases,
    budget: context.budget
  };
}
function pickCount(prefix, context) {
  const plain = /^(\d*)d?$/.exec(prefix);
  const count = plain ? Number(plain[1] || 1) : roll(prefix, diceOptions(context)).total;
  if (!Number.isInteger(count) || count < 0) throw new DiceError(`Cannot pick ${formatNumber(count)} results`);
  if (count > MAX_PICKS) throw new DiceError(`At most ${MAX_PICKS} results can be picked at once`);
  return count;
}
async function resolveNested(text, context, depth) {
  const whole = /^dice[+-]?:\s*(.+)$/i.exec(text.trim());
  if (whole) return (await rollSpecAt(whole[1], context, depth + 1)).text;
  const pattern = /`dice[+-]?:\s*([^`]+)`/gi;
  let output = "";
  let last = 0;
  for (let match = pattern.exec(text); match; match = pattern.exec(text)) {
    output += text.slice(last, match.index);
    output += (await rollSpecAt(match[1], context, depth + 1)).text;
    last = match.index + match[0].length;
  }
  return output + text.slice(last);
}
async function resolveCells(cells, context, depth) {
  const texts = [];
  for (const cell of cells) texts.push(await resolveNested(cell, context, depth));
  return texts.join(" | ");
}
async function pickFromTable(table, column, context, depth) {
  var _a, _b, _c, _d;
  const random = (_a = context.random) != null ? _a : defaultRandom;
  spendPick(context);
  if (table.rows.length === 0) throw new DiceError("The table has no rows");
  const formula = lookupFormula(table);
  let columnIndex = -1;
  if (column !== void 0) {
    columnIndex = findColumn(table, column);
    if (columnIndex === -1 && column.toLowerCase() !== "xy") {
      throw new DiceError(`The table has no column "${column}". It has: ${table.headers.join(", ")}`);
    }
  }
  if (formula !== null) {
    const rolled = roll(formula, diceOptions(context));
    const row2 = findLookupRow(table, rolled.total);
    const shown = formatNumber(rolled.total);
    if (!row2) throw new DiceError(`The lookup table has no row for ${shown}`);
    const cells = columnIndex > 0 ? [(_b = row2[columnIndex]) != null ? _b : ""] : row2.slice(1);
    return { text: await resolveCells(cells, context, depth), detail: `${formula} = ${shown}` };
  }
  const row = pick(table.rows, random);
  if (columnIndex >= 0) return { text: await resolveNested((_c = row[columnIndex]) != null ? _c : "", context, depth), detail: column != null ? column : "" };
  if (column !== void 0) {
    const from = row.length > 1 ? 1 : 0;
    return { text: await resolveNested((_d = row[random(from, row.length - 1)]) != null ? _d : "", context, depth), detail: "xy" };
  }
  return { text: await resolveCells(row, context, depth), detail: "" };
}
function matchesType(block, type) {
  const heading = /^heading-([1-6])$/.exec(type);
  if (heading) return block.type === "heading" && block.level === Number(heading[1]);
  return block.type === type;
}
function selectBlocks(blocks, types) {
  for (const type of types) {
    if (!BLOCK_TYPES.has(type) && !/^heading-[1-6]$/.test(type)) throw new DiceError(`Unknown block type "${type}"`);
  }
  if (types.length === 0) {
    return blocks.filter((b) => b.type !== "thematicBreak" && b.type !== "yaml").map((b) => b.text);
  }
  const output = [];
  for (const block of blocks) {
    if (types.includes("listItem") && block.type === "list") output.push(...listItems(block.text));
    else if (types.some((type) => matchesType(block, type))) output.push(block.text);
  }
  return output;
}
function blockTypes(args) {
  return args.flatMap((arg) => arg.split(",")).map((type) => type.trim()).filter((type) => type !== "");
}
function pickMany(options, count, random, emptyMessage, context) {
  if (count === 0) return [];
  if (options.length === 0) throw new DiceError(emptyMessage);
  const picks = [];
  for (let i = 0; i < count; i++) {
    spendPick(context);
    picks.push(pick(options, random));
  }
  return picks;
}
async function rollNote(spec, context, depth) {
  var _a;
  if (spec.target.kind !== "note") throw new DiceError("Not a note");
  const target = spec.target;
  const random = (_a = context.random) != null ? _a : defaultRandom;
  const note = await context.readNote(target.note, context.sourcePath);
  if (!note) throw new DiceError(`Note "${target.note}" was not found`);
  const count = pickCount(target.prefix, context);
  const blocks = parseBlocks(note.markdown);
  if (target.blockId !== void 0) {
    const block = blocks.find((b) => b.id === target.blockId);
    if (!block) throw new DiceError(`Block ^${target.blockId} was not found in "${target.note}"`);
    if (block.type === "table") {
      const table = parseTable(block.text);
      const column = spec.parts.find((part) => spec.args.includes(part) || findColumn(table, part) !== -1);
      const flags = column === void 0 ? spec.flags : withoutFlag(spec.flags, column);
      const results = [];
      for (let i = 0; i < count; i++) results.push(await pickFromTable(table, column, context, depth));
      const detail = results.map((r) => r.detail).filter((d) => d !== "").join("; ");
      return { kind: "table", text: results.map((r) => r.text).join(", "), details: detail, source: note.path, flags };
    }
    if (block.type === "list") {
      const picks2 = pickMany(listItems(block.text), count, random, "The list is empty", context);
      const texts = [];
      for (const item of picks2) texts.push(await resolveNested(item, context, depth));
      return { kind: "list", text: texts.join(", "), details: "", source: note.path };
    }
    return { kind: "section", text: block.text, details: "", source: note.path };
  }
  if (spec.args.some((arg) => arg.toLowerCase() === "line")) {
    const picks2 = pickMany(noteLines(note.markdown), count, random, `"${target.note}" has no lines`, context);
    return { kind: "line", text: picks2.join("\n"), details: "", source: note.path };
  }
  const options = selectBlocks(blocks, blockTypes(spec.args));
  const picks = pickMany(options, count, random, `"${target.note}" has no matching blocks`, context);
  return { kind: "section", text: picks.join("\n\n"), details: "", source: note.path };
}
async function rollTag(spec, context) {
  var _a, _b;
  if (spec.target.kind !== "tag") throw new DiceError("Not a tag");
  const target = spec.target;
  const random = (_a = context.random) != null ? _a : defaultRandom;
  const notes = await context.notesWithTag(target.tag);
  if (notes.length === 0) throw new DiceError(`No notes have the tag #${target.tag}`);
  const modes = spec.args.map((arg) => arg.toLowerCase());
  if (modes.includes("link")) {
    const note = pick(notes, random);
    return { kind: "tag", text: `[[${note.path.replace(/\.md$/, "")}]]`, details: `#${target.tag}`, source: note.path };
  }
  const chosen = modes.includes("-") ? [pick(notes, random)] : notes;
  const types = blockTypes(spec.args.filter((arg) => arg !== "-" && arg !== "+"));
  const count = pickCount(target.prefix, context);
  const parts = [];
  for (const note of chosen) {
    const options = selectBlocks(parseBlocks(note.markdown), types);
    if (options.length > 0) parts.push(...pickMany(options, count, random, "", context));
  }
  if (parts.length === 0 && count > 0) throw new DiceError(`No matching blocks in notes with #${target.tag}`);
  return { kind: "tag", text: parts.join("\n\n"), details: `#${target.tag}: ${chosen.length} note(s)`, source: chosen.length === 1 ? (_b = chosen[0]) == null ? void 0 : _b.path : void 0 };
}
async function rollSpecAt(raw, context, depth, firstRoll = false, average = false) {
  if (depth > MAX_NESTING) throw new DiceError("Rollers are nested too deeply, or a table points at itself");
  const spec = parseSpec(raw, context.aliases);
  const formula = raw.trim();
  if (spec.target.kind === "dice") {
    const dice = spec.target.formula;
    if (firstRoll && spec.flags.avg || average) {
      const average2 = averageOf(dice, diceOptions(context));
      return { kind: "dice", text: formatResult(average2.value, spec.flags), total: average2.value, estimated: !average2.exact, average: true, formula: dice, details: average2.exact ? "Average" : "Estimated average", flags: spec.flags };
    }
    const result = roll(dice, diceOptions(context));
    return { kind: "dice", text: formatResult(result.total, spec.flags), total: result.total, formula: dice, details: result.breakdown, flags: spec.flags };
  }
  const outcome = spec.target.kind === "note" ? await rollNote(spec, context, depth) : await rollTag(spec, context);
  return { flags: spec.flags, ...outcome, formula };
}
function rollSpec(raw, context, options = {}) {
  var _a, _b;
  return rollSpecAt(raw, { ...context, budget: newBudget() }, 0, (_a = options.firstRoll) != null ? _a : false, (_b = options.average) != null ? _b : false);
}

// src/ui/dice-mod.ts
var import_obsidian = require("obsidian");
var CHANGED_NOTICE = "The dice-mod code has changed, so nothing was replaced.";
var EMBED_NOTICE = "A dice-mod code in an embedded note cannot be replaced here. Open that note to replace it.";
var RESULT_NOTICE = "A dice-mod code inside a rolled result cannot be replaced.";
var NOT_MARKDOWN_NOTICE = "Only a dice-mod code in a markdown note can be replaced.";
var UNPLACED_NOTICE = "This dice-mod code cannot be replaced here, because its line in the note is unknown.";
var ReplaceCodeModal = class extends import_obsidian.Modal {
  constructor(app, text, answer) {
    super(app);
    this.text = text;
    this.answer = answer;
    this.answered = false;
  }
  onOpen() {
    this.setTitle("Replace the dice code?");
    this.contentEl.createEl("p", { text: "The code in the note becomes:" });
    this.contentEl.createEl("pre").createEl("code", { text: this.text });
    new import_obsidian.Setting(this.contentEl).addButton((button) => button.setButtonText("Cancel").onClick(() => this.reply(false))).addButton((button) => button.setButtonText("Replace").setCta().onClick(() => this.reply(true)));
  }
  reply(replace) {
    this.answered = true;
    this.answer(replace);
    this.close();
  }
  onClose() {
    this.contentEl.empty();
    if (!this.answered) this.answer(false);
  }
};
function readingModifier(plugin, target, sourcePath, position, formula) {
  return (outcome) => {
    if (target.closest(".rollwright-value")) {
      new import_obsidian.Notice(RESULT_NOTICE);
      return;
    }
    if (target.closest(".markdown-embed, .internal-embed")) {
      new import_obsidian.Notice(EMBED_NOTICE);
      return;
    }
    if (!position) {
      new import_obsidian.Notice(UNPLACED_NOTICE);
      return;
    }
    const text = modifiedText(outcome, plugin.settings.diceModFormula);
    void plugin.confirmReplace(text).then((replace) => replace ? plugin.replaceInNote(sourcePath, position.line, position.index, formula, text) : false);
  };
}
function editorModifier(plugin, view, target, formula) {
  return (outcome) => {
    const text = modifiedText(outcome, plugin.settings.diceModFormula);
    void plugin.confirmReplace(text).then((replace) => {
      if (replace) replaceInEditor(view, target, formula, text);
    });
  };
}
function replaceInEditor(view, target, formula, text) {
  if (!target.isConnected || !view.contentDOM.contains(target)) {
    new import_obsidian.Notice(CHANGED_NOTICE);
    return;
  }
  let at = -1;
  try {
    at = view.posAtDOM(target);
  } catch (e) {
    at = -1;
  }
  const line = at >= 0 && at <= view.state.doc.length ? view.state.doc.lineAt(at) : null;
  const change = line ? replacementAt(line.text, at - line.from, formula, text) : null;
  if (!line || !change) {
    new import_obsidian.Notice(CHANGED_NOTICE);
    return;
  }
  view.dispatch({ changes: { from: line.from + change.from, to: line.from + change.to, insert: change.insert }, userEvent: "input" });
}

// src/ui/history-view.ts
var import_obsidian2 = require("obsidian");
var HISTORY_VIEW = "rollwright-history";
var RollHistoryView = class extends import_obsidian2.ItemView {
  constructor(leaf, plugin) {
    super(leaf);
    this.plugin = plugin;
    this.icon = "dices";
  }
  getViewType() {
    return HISTORY_VIEW;
  }
  getDisplayText() {
    return "Roll history";
  }
  async onOpen() {
    this.refresh();
    await Promise.resolve();
  }
  async rollAndNotify(formula) {
    try {
      const source = this.plugin.currentNotePath();
      const outcome = await this.plugin.freshResult(null, formula, source);
      new import_obsidian2.Notice(`${formula}: ${outcome.text}`);
    } catch (error) {
      new import_obsidian2.Notice(error instanceof Error ? error.message : String(error));
    }
  }
  refresh() {
    const root = this.contentEl;
    root.empty();
    root.addClass("rollwright-history");
    const form = root.createEl("form", { cls: "rollwright-history-form" });
    const input = form.createEl("input", { type: "text", placeholder: "2d20kh1 + 3" });
    input.setAttribute("aria-label", "Formula");
    form.createEl("button", { text: "Roll", type: "submit" });
    form.addEventListener("submit", (event) => {
      event.preventDefault();
      if (input.value.trim() !== "") void this.rollAndNotify(input.value.trim());
    });
    const saved = this.plugin.settings.formulas;
    if (saved.length > 0) {
      const row = root.createDiv({ cls: "rollwright-history-saved" });
      for (const formula of saved) {
        const button = row.createEl("button", { text: formula.name });
        button.setAttribute("aria-label", formula.formula);
        button.addEventListener("click", () => void this.rollAndNotify(formula.formula));
      }
    }
    const history = this.plugin.settings.history;
    if (history.length === 0) {
      root.createDiv({ cls: "rollwright-history-empty", text: "Click a roll in a note to see it here." });
      return;
    }
    const clear = root.createEl("button", { cls: "rollwright-history-clear", text: "Clear history" });
    clear.addEventListener("click", () => void this.plugin.clearHistory());
    const list = root.createDiv({ cls: "rollwright-history-list" });
    for (const entry of history) {
      const item = list.createDiv({ cls: "rollwright-history-item" });
      item.createDiv({ cls: "rollwright-history-result", text: entry.result });
      item.createDiv({ cls: "rollwright-history-formula", text: entry.formula });
      if (entry.details !== "") item.createDiv({ cls: "rollwright-history-details", text: entry.details });
      const meta = item.createDiv({ cls: "rollwright-history-meta" });
      meta.createSpan({ text: new Date(entry.time).toLocaleTimeString() });
      if (entry.source !== "") {
        const link = meta.createEl("a", { text: entry.source });
        link.addEventListener("click", (event) => {
          event.preventDefault();
          void this.app.workspace.openLinkText(entry.source, "");
        });
      }
      const again = meta.createEl("button", { cls: "clickable-icon" });
      again.setAttribute("aria-label", "Roll again");
      (0, import_obsidian2.setIcon)(again, "refresh-cw");
      again.addEventListener("click", () => void this.rollAndNotify(entry.formula));
    }
  }
};

// src/ui/live-preview.ts
var import_language = require("@codemirror/language");
var import_state = require("@codemirror/state");
var import_view = require("@codemirror/view");
var import_obsidian4 = require("obsidian");

// src/ui/widget.ts
var import_obsidian3 = require("obsidian");
var NO_SOURCE_NOTICE = "This result comes from more than one note, so there is no single note to open.";
var SOURCE_GONE_NOTICE = "The note this result came from is no longer there.";
function errorMessage(error) {
  return error instanceof Error ? error.message : String(error);
}
function tooltipFor(outcome) {
  return outcome.details === "" ? outcome.formula : `${outcome.formula}
${outcome.details}`;
}
function showBlank(target, formula) {
  target.empty();
  target.removeClass("rollwright-error");
  (0, import_obsidian3.setIcon)(target.createSpan({ cls: "rollwright-icon" }), "dices");
  (0, import_obsidian3.setTooltip)(target, formula);
}
function showError(target, formula, error) {
  target.empty();
  target.addClass("rollwright-error");
  const message = errorMessage(error);
  target.createSpan({ text: `dice: ${formula}` });
  (0, import_obsidian3.setTooltip)(target, message);
  target.setAttribute("data-rollwright-error", message);
}
async function showOutcome(plugin, target, outcome, sourcePath, component) {
  target.empty();
  target.removeClass("rollwright-error");
  const { flags } = outcome;
  if (!flags.nodice) {
    (0, import_obsidian3.setIcon)(target.createSpan({ cls: "rollwright-icon" }), "dices");
  }
  if (flags.text !== void 0) target.createSpan({ cls: "rollwright-label", text: `${flags.text}: ` });
  else if (flags.form) target.createSpan({ cls: "rollwright-label", text: `${outcome.formula} -> ` });
  const value = target.createSpan({ cls: "rollwright-value" });
  if (outcome.kind === "dice") {
    value.setText(`${outcome.estimated ? "~" : ""}${outcome.total === void 0 ? outcome.text : formatResult(outcome.total, flags)}`);
  } else {
    await import_obsidian3.MarkdownRenderer.render(plugin.app, defuseRolls(outcome.text), value, sourcePath, component);
  }
  (0, import_obsidian3.setTooltip)(target, tooltipFor(outcome));
}
function mountRoll(plugin, target, formula, key, sourcePath, component, keep = false, modify) {
  target.addClass("rollwright-roll");
  target.setAttribute("role", "button");
  let hideFirst = false;
  try {
    hideFirst = parseSpec(formula, plugin.rollContext(sourcePath).aliases).flags.none;
  } catch (e) {
    hideFirst = false;
  }
  let shown = null;
  const show = async (outcome) => {
    shown = outcome;
    await showOutcome(plugin, target, outcome, sourcePath, component);
  };
  const fail = (error) => {
    shown = null;
    showError(target, formula, error);
  };
  const rerollNow = async () => {
    try {
      if (!modify) {
        await show(await plugin.freshResult(key, formula, sourcePath, keep));
        return;
      }
      if (shown === null) await show(await plugin.firstResult(key, formula, sourcePath));
      if (shown !== null) modify(shown);
    } catch (error) {
      fail(error);
    }
  };
  const averageNow = async () => {
    try {
      await show(await plugin.averageResult(key, formula, sourcePath, keep));
    } catch (error) {
      fail(error);
    }
  };
  const modClick = async (pane) => {
    if (hideFirst) {
      shown = null;
      await plugin.forgetResult(key);
      showBlank(target, formula);
      return;
    }
    if (shown === null || shown.kind === "dice") {
      await rerollNow();
      return;
    }
    if (shown.source === void 0) {
      new import_obsidian3.Notice(NO_SOURCE_NOTICE);
      return;
    }
    const file = plugin.app.vault.getAbstractFileByPath(shown.source);
    if (!(file instanceof import_obsidian3.TFile)) {
      new import_obsidian3.Notice(SOURCE_GONE_NOTICE);
      return;
    }
    await plugin.app.workspace.getLeaf(pane === true ? "tab" : pane).openFile(file);
  };
  target.setAttribute("tabindex", "0");
  target.addEventListener("keydown", (event) => {
    if (event.key === "Enter") void rerollNow();
  });
  target.addEventListener("click", (event) => {
    if (event.target.instanceOf(Element) && event.target.closest("a")) return;
    event.preventDefault();
    event.stopPropagation();
    const pane = import_obsidian3.Keymap.isModEvent(event);
    if (pane) void modClick(pane);
    else if (event.altKey && !modify) void averageNow();
    else void rerollNow();
  });
  target.addEventListener("mousedown", (event) => event.preventDefault());
  if (hideFirst && !plugin.hasResult(key, keep)) {
    showBlank(target, formula);
    return;
  }
  plugin.firstResult(key, formula, sourcePath, keep).then(show, fail).catch(fail);
}

// src/ui/live-preview.ts
var RollWidget = class extends import_view.WidgetType {
  constructor(plugin, formula, key, sourcePath, keep, modify) {
    super();
    this.plugin = plugin;
    this.formula = formula;
    this.key = key;
    this.sourcePath = sourcePath;
    this.keep = keep;
    this.modify = modify;
    this.component = null;
  }
  eq(other) {
    return other.key === this.key && other.keep === this.keep && other.modify === this.modify;
  }
  toDOM(view) {
    const span = activeDocument.createElement("span");
    this.component = new import_obsidian4.Component();
    this.component.load();
    const modify = this.modify ? editorModifier(this.plugin, view, span, this.formula) : void 0;
    mountRoll(this.plugin, span, this.formula, this.key, this.sourcePath, this.component, this.keep, modify);
    return span;
  }
  destroy() {
    var _a;
    (_a = this.component) == null ? void 0 : _a.unload();
    this.component = null;
  }
  ignoreEvent() {
    return true;
  }
};
function build(plugin, view) {
  var _a, _b, _c;
  const builder = new import_state.RangeSetBuilder();
  const state = view.state;
  if (!state.field(import_obsidian4.editorLivePreviewField, false)) return builder.finish();
  const sourcePath = (_c = (_b = (_a = state.field(import_obsidian4.editorInfoField, false)) == null ? void 0 : _a.file) == null ? void 0 : _b.path) != null ? _c : "";
  const selection = state.selection.ranges;
  const tree = (0, import_language.syntaxTree)(state);
  for (const { from, to } of view.visibleRanges) {
    let line = state.doc.lineAt(from);
    for (; ; ) {
      findInlineDice(line.text).forEach((found, index) => {
        const start = line.from + found.from;
        const end = line.from + found.to;
        if (selection.some((range2) => range2.from <= end && range2.to >= start)) return;
        if (tree.resolveInner(start + 1, 1).name.includes("codeblock")) return;
        const key = `${sourcePath}|${line.number - 1}:${index}|${found.formula}`;
        builder.add(start, end, import_view.Decoration.replace({ widget: new RollWidget(plugin, found.formula, key, sourcePath, found.keep, found.modify) }));
      });
      if (line.to >= to || line.number >= state.doc.lines) break;
      line = state.doc.line(line.number + 1);
    }
  }
  return builder.finish();
}
function rollwrightLivePreview(plugin) {
  return import_view.ViewPlugin.fromClass(
    class {
      constructor(view) {
        this.decorations = build(plugin, view);
      }
      update(update) {
        const modeChanged = update.startState.field(import_obsidian4.editorLivePreviewField, false) !== update.state.field(import_obsidian4.editorLivePreviewField, false);
        if (update.docChanged || update.viewportChanged || update.selectionSet || modeChanged) {
          this.decorations = build(plugin, update.view);
        }
      }
    },
    { decorations: (value) => value.decorations }
  );
}

// src/ui/modal.ts
var import_obsidian5 = require("obsidian");
var RollFormulaModal = class extends import_obsidian5.Modal {
  constructor(app, plugin) {
    super(app);
    this.plugin = plugin;
  }
  onOpen() {
    this.setTitle("Roll a formula");
    let formula = "";
    const submit = async () => {
      if (formula.trim() === "") return;
      try {
        const outcome = await this.plugin.freshResult(null, formula.trim(), this.plugin.currentNotePath());
        new import_obsidian5.Notice(`${formula.trim()}: ${outcome.text}`);
        this.close();
      } catch (error) {
        new import_obsidian5.Notice(error instanceof Error ? error.message : String(error));
      }
    };
    new import_obsidian5.Setting(this.contentEl).setName("Formula").addText((text) => {
      text.setPlaceholder("2d20kh1 + 3").onChange((value) => {
        formula = value;
      });
      text.inputEl.addEventListener("keydown", (event) => {
        if (event.key === "Enter") void submit();
      });
    });
    new import_obsidian5.Setting(this.contentEl).addButton((button) => button.setButtonText("Roll").setCta().onClick(() => void submit()));
  }
  onClose() {
    this.contentEl.empty();
  }
};

// src/ui/reading-view.ts
var import_obsidian6 = require("obsidian");
function codePositions(el, ctx) {
  var _a;
  const info = ctx.getSectionInfo(el);
  if (!info) return [];
  const positions = [];
  const lines = info.text.split("\n");
  for (let line = info.lineStart; line <= info.lineEnd; line++) {
    findInlineDice((_a = lines[line]) != null ? _a : "").forEach((_, index) => positions.push({ line, index }));
  }
  return positions;
}
var unplaced = 0;
function processReadingView(plugin, el, ctx) {
  var _a;
  if (el.closest(".rollwright-value")) return;
  const codes = Array.from(el.querySelectorAll("code")).filter((code) => {
    var _a2;
    return ((_a2 = code.parentElement) == null ? void 0 : _a2.tagName) !== "PRE";
  });
  const positions = codePositions(el, ctx);
  const counted = codes.filter((code) => {
    var _a2;
    return readDiceCode((_a2 = code.textContent) != null ? _a2 : "") !== null;
  }).length === positions.length;
  let nth = 0;
  for (const code of codes) {
    const dice = readDiceCode((_a = code.textContent) != null ? _a : "");
    if (dice === null) continue;
    const { formula } = dice;
    const position = positions[nth];
    const keep = dice.keep && position !== void 0;
    const place = position ? `${position.line}:${position.index}` : `el:${++unplaced}`;
    nth++;
    const span = activeDocument.createElement("span");
    code.replaceWith(span);
    const child = new import_obsidian6.MarkdownRenderChild(span);
    ctx.addChild(child);
    const modify = dice.modify ? readingModifier(plugin, span, ctx.sourcePath, counted ? position : void 0, formula) : void 0;
    mountRoll(plugin, span, formula, `${ctx.sourcePath}|${place}|${formula}`, ctx.sourcePath, child, keep, modify);
  }
}

// src/ui/settings.ts
var import_obsidian7 = require("obsidian");
function parseWholeNumber(value, min) {
  const text = value.trim();
  if (!/^\d+$/.test(text)) return null;
  const number = Number(text);
  return Number.isSafeInteger(number) && number >= min ? number : null;
}
var RollwrightSettingTab = class extends import_obsidian7.PluginSettingTab {
  constructor(app, plugin) {
    super(app, plugin);
    this.plugin = plugin;
  }
  display() {
    const { containerEl } = this;
    containerEl.empty();
    const settings = this.plugin.settings;
    new import_obsidian7.Setting(containerEl).setName("Default die").setDesc("The number of sides when a formula leaves it out, as in 3d.").addText(
      (text) => text.setValue(String(settings.defaultSides)).onChange(async (value) => {
        const sides = parseWholeNumber(value, 1);
        if (sides === null) return;
        settings.defaultSides = sides;
        await this.plugin.saveSettings();
      })
    );
    new import_obsidian7.Setting(containerEl).setName("Default number of dice").setDesc("The number of dice when a formula leaves it out, as in d6.").addText(
      (text) => text.setValue(String(settings.defaultCount)).onChange(async (value) => {
        const count = parseWholeNumber(value, 0);
        if (count === null) return;
        settings.defaultCount = count;
        await this.plugin.saveSettings();
      })
    );
    new import_obsidian7.Setting(containerEl).setName("Keep the formula when a dice-mod code is replaced").setDesc("On: 3d6 -> [2, 5, 4] -> 11. Off: [2, 5, 4] -> 11. Results of tables, lists and notes never show a formula.").addToggle(
      (toggle) => toggle.setValue(settings.diceModFormula).onChange(async (value) => {
        settings.diceModFormula = value;
        await this.plugin.saveSettings();
      })
    );
    new import_obsidian7.Setting(containerEl).setName("Saved formulas").setHeading();
    settings.formulas.forEach((formula, index) => {
      new import_obsidian7.Setting(containerEl).addText(
        (text) => text.setPlaceholder("Name").setValue(formula.name).onChange(async (value) => {
          formula.name = value.trim();
          await this.plugin.saveSettings();
        })
      ).addText(
        (text) => text.setPlaceholder("Formula").setValue(formula.formula).onChange(async (value) => {
          formula.formula = value.trim();
          await this.plugin.saveSettings();
        })
      ).addExtraButton(
        (button) => button.setIcon("trash").setTooltip("Remove").onClick(async () => {
          settings.formulas.splice(index, 1);
          await this.plugin.saveSettings();
          this.display();
        })
      );
    });
    new import_obsidian7.Setting(containerEl).setName("Add a formula").setDesc("Use its name in any roll, such as dice: attack.").addButton(
      (button) => button.setButtonText("Add").onClick(async () => {
        settings.formulas.push({ name: `formula${settings.formulas.length + 1}`, formula: "1d20" });
        await this.plugin.saveSettings();
        this.display();
      })
    );
    new import_obsidian7.Setting(containerEl).setName("Import saved formulas").setDesc("Copies named formulas from the data file of the Dice Roller plugin, if you have it. That file is only read, and existing names stay as they are.").addButton(
      (button) => button.setButtonText("Import").onClick(async () => {
        await this.plugin.importSavedFormulas();
        this.display();
      })
    );
    new import_obsidian7.Setting(containerEl).setName("Skins").setHeading();
    const paidNames = SKINS.filter((skin) => skin.paid).map((skin) => skin.name).join(" and ");
    new import_obsidian7.Setting(containerEl).setName("Skin").setDesc(`All rolling is free. ${paidNames} are paid skins and need a license key.`).addDropdown((dropdown) => {
      for (const skin of availableSkins(this.plugin.isLicensed)) dropdown.addOption(skin.id, skin.name);
      dropdown.setValue(settings.skin).onChange(async (value) => {
        settings.skin = value;
        await this.plugin.saveSettings();
        this.plugin.applySkin();
      });
    });
    new import_obsidian7.Setting(containerEl).setName("License key").setDesc("Checked on this device only. Nothing is sent anywhere.").addText(
      (text) => text.setValue(settings.licenseKey).onChange(async (value) => {
        settings.licenseKey = value.trim();
        await this.plugin.saveSettings();
        this.plugin.applySkin();
      })
    ).addButton(
      (button) => button.setButtonText("Check").onClick(() => {
        new import_obsidian7.Notice(isValidLicenseKey(settings.licenseKey) ? "The license key is valid." : "This license key is not valid.");
        this.display();
      })
    );
    if (shouldShowBuyButton()) {
      new import_obsidian7.Setting(containerEl).setName("Get the paid skins").addButton(
        (button) => button.setButtonText("Buy").onClick(() => {
          activeWindow.open(BUY_URL);
        })
      );
    }
  }
};

// src/main.ts
var DEFAULT_SETTINGS = {
  defaultSides: 100,
  defaultCount: 1,
  formulas: [],
  history: [],
  licenseKey: "",
  skin: "classic",
  keptResults: [],
  diceModFormula: true
};
var HISTORY_LIMIT = 200;
var RESULT_CACHE_LIMIT = 2e3;
var KEPT_RESULTS_LIMIT = 500;
var OUTCOME_KINDS = /* @__PURE__ */ new Set(["dice", "table", "list", "section", "line", "tag"]);
function isKeptOutcome(value) {
  if (typeof value !== "object" || value === null) return false;
  const o = value;
  return typeof o.kind === "string" && OUTCOME_KINDS.has(o.kind) && typeof o.text === "string" && typeof o.formula === "string" && typeof o.details === "string" && typeof o.flags === "object" && o.flags !== null && !Array.isArray(o.flags) && (o.total === void 0 || typeof o.total === "number");
}
var RollwrightPlugin = class extends import_obsidian8.Plugin {
  constructor() {
    super(...arguments);
    this.settings = { ...DEFAULT_SETTINGS };
    this.results = /* @__PURE__ */ new Map();
    /** Results of `dice+:`, written to disk with the settings. */
    this.kept = /* @__PURE__ */ new Map();
    this.skinnedDocuments = /* @__PURE__ */ new Set();
  }
  async onload() {
    await this.loadSettings();
    this.registerView(HISTORY_VIEW, (leaf) => new RollHistoryView(leaf, this));
    this.registerMarkdownPostProcessor((el, ctx) => processReadingView(this, el, ctx));
    this.registerEditorExtension(rollwrightLivePreview(this));
    this.addSettingTab(new RollwrightSettingTab(this.app, this));
    this.addCommand({
      id: "open-history",
      name: "Open roll history",
      callback: () => void this.openHistory()
    });
    this.addCommand({
      id: "roll-formula",
      name: "Roll a formula",
      callback: () => new RollFormulaModal(this.app, this).open()
    });
    this.applySkin(activeDocument);
    this.registerEvent(this.app.workspace.on("window-open", (win) => this.applySkin(win.doc)));
    this.app.workspace.onLayoutReady(() => {
      this.app.workspace.iterateAllLeaves((leaf) => {
        this.skinnedDocuments.add(leaf.view.containerEl.doc);
      });
      this.applySkin();
    });
  }
  onunload() {
    for (const doc of this.skinnedDocuments) {
      for (const skin of SKINS) doc.body.removeClass(skin.cssClass);
    }
  }
  async loadSettings() {
    const stored = await this.loadData();
    this.settings = { ...DEFAULT_SETTINGS, formulas: [], history: [], keptResults: [], ...stored };
    this.kept.clear();
    const kept = Array.isArray(this.settings.keptResults) ? this.settings.keptResults : [];
    for (const entry of kept) {
      if (Array.isArray(entry) && typeof entry[0] === "string" && isKeptOutcome(entry[1])) this.kept.set(entry[0], entry[1]);
    }
    this.trimKept();
  }
  async saveSettings() {
    this.settings.keptResults = [...this.kept.entries()];
    await this.saveData(this.settings);
  }
  get isLicensed() {
    return isValidLicenseKey(this.settings.licenseKey);
  }
  /** Sets the skin on this document and on every window that already has one. */
  applySkin(doc = activeDocument) {
    this.skinnedDocuments.add(doc);
    const active = resolveSkin(this.settings.skin, this.isLicensed);
    for (const known of this.skinnedDocuments) {
      for (const skin of SKINS) known.body.toggleClass(skin.cssClass, skin.id === active.id);
    }
  }
  /** Builds the bridge between the pure rollers and this vault. */
  rollContext(sourcePath) {
    const aliases = this.noteFields(sourcePath);
    for (const formula of this.settings.formulas) aliases[formula.name] = formula.formula;
    return {
      sourcePath,
      defaultSides: this.settings.defaultSides,
      defaultCount: this.settings.defaultCount,
      aliases,
      readNote: (link, from) => this.readNote(link, from),
      notesWithTag: (tag) => this.notesWithTag(tag)
    };
  }
  /** The number fields in the frontmatter of this note, as names. Nothing when it has none. */
  noteFields(sourcePath) {
    var _a;
    try {
      const file = this.app.vault.getAbstractFileByPath(sourcePath);
      if (!(file instanceof import_obsidian8.TFile)) return {};
      return fieldNames((_a = this.app.metadataCache.getFileCache(file)) == null ? void 0 : _a.frontmatter);
    } catch (e) {
      return {};
    }
  }
  async readNote(link, sourcePath) {
    const file = this.app.metadataCache.getFirstLinkpathDest(link, sourcePath);
    if (!(file instanceof import_obsidian8.TFile)) return null;
    return { path: file.path, markdown: await this.app.vault.cachedRead(file) };
  }
  async notesWithTag(tag) {
    const wanted = `#${tag}`.toLowerCase();
    const notes = [];
    for (const file of this.app.vault.getMarkdownFiles()) {
      const cache = this.app.metadataCache.getFileCache(file);
      const tags = cache ? (0, import_obsidian8.getAllTags)(cache) : null;
      if (tags == null ? void 0 : tags.some((t) => t.toLowerCase() === wanted || t.toLowerCase().startsWith(`${wanted}/`))) {
        notes.push({ path: file.path, markdown: await this.app.vault.cachedRead(file) });
      }
    }
    return notes;
  }
  hasResult(key, keep = false) {
    return this.results.has(key) || keep && this.kept.has(key);
  }
  /**
   * The result for this place in a note: remembered, or rolled for the first time.
   * With keep (`dice+:`) the result also comes from and goes to disk.
   */
  async firstResult(key, formula, sourcePath, keep = false) {
    var _a;
    const known = (_a = this.results.get(key)) != null ? _a : keep ? this.kept.get(key) : void 0;
    if (known) {
      if (keep && !this.kept.has(key)) await this.keep(key, known);
      return known;
    }
    const outcome = await rollSpec(formula, this.rollContext(sourcePath), { firstRoll: true });
    this.remember(key, outcome);
    if (keep) await this.keep(key, outcome);
    return outcome;
  }
  /** A roll someone asked for. Only these go into the history. With keep, the new result replaces the kept one. */
  async freshResult(key, formula, sourcePath, keep = false) {
    const outcome = await rollSpec(formula, this.rollContext(sourcePath));
    if (key !== null) this.remember(key, outcome);
    if (key !== null && keep) this.storeKept(key, outcome);
    await this.addToHistory(outcome, formula, sourcePath);
    return outcome;
  }
  /**
   * Alt-click: dice show their average, as |avg does. It is remembered (and kept with keep)
   * but not put in the history, because nothing was rolled. Anything else rolls as a click does.
   */
  async averageResult(key, formula, sourcePath, keep = false) {
    const outcome = await rollSpec(formula, this.rollContext(sourcePath), { average: true });
    this.remember(key, outcome);
    if (keep) this.storeKept(key, outcome);
    if (outcome.kind !== "dice") await this.addToHistory(outcome, formula, sourcePath);
    else if (keep) await this.saveSettings();
    return outcome;
  }
  /** Ctrl-click on a |none code: forgets its result, also the kept one, so it stays empty. */
  async forgetResult(key) {
    this.results.delete(key);
    if (this.kept.delete(key)) await this.saveSettings();
  }
  /** Puts a result at the newest end of the kept results, dropping the oldest over the limit. */
  storeKept(key, outcome) {
    this.kept.delete(key);
    this.kept.set(key, outcome);
    this.trimKept();
  }
  trimKept() {
    while (this.kept.size > KEPT_RESULTS_LIMIT) {
      const oldest = this.kept.keys().next().value;
      if (oldest === void 0) break;
      this.kept.delete(oldest);
    }
  }
  async keep(key, outcome) {
    this.storeKept(key, outcome);
    await this.saveSettings();
  }
  remember(key, outcome) {
    if (this.results.size >= RESULT_CACHE_LIMIT) {
      const oldest = this.results.keys().next().value;
      if (oldest !== void 0) this.results.delete(oldest);
    }
    this.results.set(key, outcome);
  }
  async addToHistory(outcome, formula, sourcePath) {
    this.settings.history.unshift({
      time: Date.now(),
      formula,
      result: outcome.text,
      details: outcome.details,
      source: sourcePath
    });
    this.settings.history.length = Math.min(this.settings.history.length, HISTORY_LIMIT);
    await this.saveSettings();
    this.refreshHistoryViews();
  }
  async clearHistory() {
    this.settings.history = [];
    await this.saveSettings();
    this.refreshHistoryViews();
  }
  refreshHistoryViews() {
    for (const leaf of this.app.workspace.getLeavesOfType(HISTORY_VIEW)) {
      if (leaf.view instanceof RollHistoryView) leaf.view.refresh();
    }
  }
  async openHistory() {
    var _a;
    const { workspace } = this.app;
    let leaf = workspace.getLeavesOfType(HISTORY_VIEW)[0];
    if (!leaf) {
      leaf = (_a = workspace.getRightLeaf(false)) != null ? _a : void 0;
      await (leaf == null ? void 0 : leaf.setViewState({ type: HISTORY_VIEW, active: true }));
    }
    if (leaf) await workspace.revealLeaf(leaf);
  }
  /** Asks before a dice-mod code is replaced. True for Replace; Cancel and closing give false. */
  confirmReplace(text) {
    return new Promise((resolve) => new ReplaceCodeModal(this.app, text, resolve).open());
  }
  /**
   * Replaces a dice-mod code in this one note, read fresh inside vault.process. Only when
   * the code with this number on this line is still dice-mod with this formula; otherwise
   * the note is given back as it was, with a notice. Never touches any other note.
   */
  async replaceInNote(path, line, index, formula, replacement) {
    const file = this.app.vault.getAbstractFileByPath(path);
    if (!(file instanceof import_obsidian8.TFile)) {
      new import_obsidian8.Notice(CHANGED_NOTICE);
      return false;
    }
    if (file.extension !== "md") {
      new import_obsidian8.Notice(NOT_MARKDOWN_NOTICE);
      return false;
    }
    let done = false;
    await this.app.vault.process(file, (data) => {
      const next = replaceCodeInNote(data, line, index, formula, replacement);
      done = next !== null;
      return next != null ? next : data;
    });
    if (!done) new import_obsidian8.Notice(CHANGED_NOTICE);
    return done;
  }
  currentNotePath() {
    var _a, _b, _c;
    return (_c = (_b = (_a = this.app.workspace.getActiveViewOfType(import_obsidian8.MarkdownView)) == null ? void 0 : _a.file) == null ? void 0 : _b.path) != null ? _c : "";
  }
  /** Reads the named formulas of the other plugin. Reads only; its file stays as it is. */
  async importSavedFormulas() {
    const path = `${this.app.vault.configDir}/plugins/obsidian-dice-roller/data.json`;
    const adapter = this.app.vault.adapter;
    if (!await adapter.exists(path)) {
      new import_obsidian8.Notice("No saved formulas found to import.");
      return;
    }
    const found = extractSavedFormulas(await adapter.read(path));
    const { merged, added } = mergeFormulas(this.settings.formulas, found);
    this.settings.formulas = merged;
    await this.saveSettings();
    new import_obsidian8.Notice(`Imported ${added} of ${found.length} saved formulas.`);
  }
};
