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
var import_obsidian10 = require("obsidian");

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
var import_obsidian = require("obsidian");
var POLAR_ORG_ID = "5f4a360c-7552-4269-a44a-4311f7f672d6";
var POLAR_BENEFIT_ID = "344f6030-66ec-437a-8fbb-186b80a98c65";
var BUY_URL = "https://buy.polar.sh/polar_cl_kJQ6H0U8GSNV0qMQkejM6SY4BYkU9k3SxfApH07ipIP";
var PRICE_TEXT = "$6";
var VALIDATE_URL = "https://api.polar.sh/v1/customer-portal/license-keys/validate";
var RECHECK_INTERVAL_MS = 30 * 24 * 60 * 60 * 1e3;
var obsidianRequest = async (request) => {
  const response = await (0, import_obsidian.requestUrl)(request);
  let json = null;
  try {
    json = response.json;
  } catch (e) {
    json = null;
  }
  return { status: response.status, json };
};
var LICENSE_MESSAGES = {
  invalid: "This key is not valid. If you rotated it, paste the new key from your Polar purchases.",
  "no-connection": "Could not reach Polar, try again.",
  "our-error": "Something is wrong on our side, please contact thijs@dortus.com."
};
var POLAR_IDS = { organizationId: POLAR_ORG_ID, benefitId: POLAR_BENEFIT_ID, buyUrl: BUY_URL };
function paymentReady(ids = POLAR_IDS) {
  return ids.organizationId.trim() !== "" && ids.benefitId.trim() !== "" && ids.buyUrl.trim() !== "";
}
async function validateLicense(key, request, ids = POLAR_IDS) {
  let response;
  try {
    response = await request({
      url: VALIDATE_URL,
      method: "POST",
      contentType: "application/json",
      body: JSON.stringify({ key: key.trim(), organization_id: ids.organizationId, benefit_id: ids.benefitId }),
      throw: false
    });
  } catch (e) {
    return "no-connection";
  }
  if (response.status === 200) {
    const answer = typeof response.json === "object" && response.json !== null ? response.json : {};
    const ours = answer.organization_id === ids.organizationId && answer.benefit_id === ids.benefitId && answer.status === "granted";
    return ours ? "valid" : "invalid";
  }
  if (response.status === 404) return "invalid";
  if (response.status === 422) return "our-error";
  return "no-connection";
}
function recheckDue(checkedAt, now) {
  return checkedAt > 0 && now >= checkedAt && now - checkedAt >= RECHECK_INTERVAL_MS;
}
function isLicenseActive(state) {
  return typeof state.licenseKey === "string" && state.licenseKey.trim() !== "" && typeof state.licenseCheckedAt === "number" && state.licenseCheckedAt > 0;
}
async function activateLicense(state, key, request, now, ids = POLAR_IDS) {
  const outcome = await validateLicense(key, request, ids);
  if (outcome === "valid") {
    state.licenseKey = key.trim();
    state.licenseCheckedAt = now;
  }
  return outcome;
}
async function recheckLicense(state, request, now, ids = POLAR_IDS) {
  if (!paymentReady(ids) || !isLicenseActive(state)) return false;
  if (state.licenseCheckedAt > now) {
    state.licenseCheckedAt = now;
    return true;
  }
  if (!recheckDue(state.licenseCheckedAt, now)) return false;
  const outcome = await validateLicense(state.licenseKey, request, ids);
  if (outcome === "valid") state.licenseCheckedAt = now;
  else if (outcome === "invalid") state.licenseCheckedAt = 0;
  else return false;
  return true;
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
function tooManyDiceMessage(count) {
  return `At most ${LIMITS.diceInGroup} dice can be rolled at once, not ${count}. Use a smaller number, like 100d6.`;
}
var TOO_MANY_ROLLS_MESSAGE = `This formula rolls more than ${LIMITS.rollsPerFormula} dice. Roll fewer dice, or limit exploding and rerolling, like 10d6!3.`;
var TOO_LARGE_MESSAGE = "The result is too large to show. Use smaller numbers or fewer dice, like 10d6 * 100.";
function newBudget() {
  return { rolls: 0, steps: 0, picks: 0 };
}

// src/engine/stunt.ts
var STUNT_SPREAD = { mean: 10.5, min: 3, max: 18, whole: true };
function isStuntWord(word) {
  return word.startsWith("dS");
}
function stuntNode(count, word) {
  if (word.value !== "dS") throw new DiceError(`The stunt die takes no modifiers: write 1dS, not ${word.value}`);
  if (count !== null && !(count.type === "number" && count.value === 1)) {
    const shown = count.type === "number" ? String(count.value) : "X";
    throw new DiceError(`Only one stunt die can be rolled: write 1dS, not ${shown}dS`);
  }
  return { type: "stunt" };
}
function rollStunt(rollD6) {
  const first = rollD6();
  const second = rollD6();
  const stunt = rollD6();
  const double = first === second || first === stunt || second === stunt;
  const points = double ? ` (${stunt} stunt ${stunt === 1 ? "point" : "points"})` : "";
  return { value: first + second + stunt, text: `[${first}, ${second}, S:${stunt}]${points}` };
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
    throw new DiceError(`Unexpected character "${ch}" at position ${i + 1}. Remove it and use only numbers, dice and + - * / ( ), like 2d6 + 1.`);
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
function unexpected(token, previous) {
  const afterValue = previous !== void 0 && previous.type !== "cmp" && !(previous.type === "sym" && "+-*/^(".includes(previous.value));
  let fix = "Remove it, like 2d6 + 3.";
  if (token.value === ")") fix = "Remove it or add the ( it closes, like (2d6 + 1) * 2.";
  else if (afterValue) fix = "Remove it or put + - * / before it, like 2d6 + 3.";
  return new DiceError(`Unexpected "${token.value}" at position ${token.pos + 1}. ${fix}`);
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
    if (this.tokens.length === 0) throw new DiceError("The formula is empty. Write a formula after dice:, like 2d6 + 1.");
    const node = this.additive();
    const left = this.peek();
    if (left) throw unexpected(left, this.tokens[this.index - 1]);
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
    if (++this.depth > LIMITS.parseDepth) throw new DiceError("The formula is nested too deeply. Use fewer brackets, like (2d6 + 1) * 2.");
  }
  /** Names the last token, so the message shows where the formula stops. */
  endsTooEarly() {
    var _a, _b;
    const last = (_b = (_a = this.tokens[this.tokens.length - 1]) == null ? void 0 : _a.value) != null ? _b : "";
    if (last === "") return new DiceError("The formula ends too early. Add a number or a die at the end, like 2d6 + 1.");
    return new DiceError(`The formula ends too early: it ends with ${last}. Add a number or a die after it, like 2d6 + 1.`);
  }
  primary() {
    const token = this.peek();
    if (!token) throw this.endsTooEarly();
    if (token.type === "num") {
      this.index++;
      const value = Number(token.value);
      if (!Number.isSafeInteger(Math.trunc(value))) throw new DiceError(`The number ${token.value} is too large. Use a number with at most 15 digits, like 1000000.`);
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
      if (!this.isSym(")")) throw new DiceError("A closing bracket is missing. Add ) after the group, like (2d6 + 1) * 2.");
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
    throw unexpected(token, this.tokens[this.index - 1]);
  }
  dice(count) {
    const word = this.peek();
    if (isStuntWord(word.value)) {
      this.index++;
      return stuntNode(count, word);
    }
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
        if (digits.includes(0)) throw new DiceError(`d${token.value}% has a die with zero sides. Use the digits 1 to 9, like d66%.`);
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
    if (first === void 0 || second === void 0) throw new DiceError("Custom dice need at least two numbers. Write d[min, max] or d[a, b, c], like d[1, 4].");
    if (values.length === 2) return { kind: "range", min: Math.min(first, second), max: Math.max(first, second) };
    return { kind: "faces", faces: values };
  }
  wholeNumber(token, what) {
    const value = Number(token.value);
    if (!Number.isInteger(value)) throw new DiceError(`${what} must be a whole number, not ${token.value}. Leave out the decimals, like 2d6 or 4d6kh3.`);
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
        modifiers.push({ kind: "explode", combine: token.value === "!!", times, conditions: this.conditions("1d6!>=5") });
      } else if (token.type === "cmp") {
        modifiers.push(this.countModifier());
      } else if (token.type === "word") {
        const lower = token.value.toLowerCase();
        const match = MODIFIER_WORDS.find((m) => lower.startsWith(m));
        if (!match) throw new DiceError(`Unknown modifier "${token.value}" at position ${token.pos + 1}. Use kh, kl, dh, dl, r, u, s or !, like 4d6kh3.`);
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
        return { kind: "reroll", times, conditions: this.conditions("1d6r<2") };
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
    if (count > LIMITS.repeats) throw new DiceError(`A die can repeat at most ${LIMITS.repeats} times. Use a smaller number, like 1d6!10.`);
    return count;
  }
  /** Conditions right after ! or r belong to that modifier. */
  conditions(example) {
    const conditions = [];
    for (; ; ) {
      const token = this.peek();
      if ((token == null ? void 0 : token.type) !== "cmp") return conditions;
      const { op, score } = mapComparator(token.value);
      if (score === -1) throw new DiceError(`"${token.value}" only works for counting, not on ! or r. Use it for counting, like 5d10>=8-=1.`);
      this.index++;
      const value = this.peek();
      if ((value == null ? void 0 : value.type) !== "num") throw new DiceError(`A number is missing after "${token.value}". Add one, like ${example}.`);
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
    throw new DiceError(`A number is missing after "${comparator}". Add one, like 5d10>=8.`);
  }
};
function parseFormula(formula, names = []) {
  if (formula.length > LIMITS.formulaLength) {
    throw new DiceError(`The formula is longer than ${LIMITS.formulaLength} characters. Save parts of it as named formulas and use their names, like 1d20 + atk.`);
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
function roundNumber(raw, mode) {
  if (mode === void 0 || !Number.isFinite(raw)) return raw;
  const value = Number(raw.toFixed(10));
  if (mode === "ceil") return Math.ceil(value);
  if (mode === "floor") return Math.floor(value);
  return Math.sign(value) * Math.round(Math.abs(value));
}
function formatResult(value, style = {}) {
  const shown = formatNumber(roundNumber(value, style.round));
  const signed = style.signed && !shown.startsWith("-") ? `+${shown}` : shown;
  return style.paren ? `(${signed})` : signed;
}

// src/engine/compare.ts
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

// src/engine/faces.ts
var TOO_MANY_SIDES = `A die can have at most ${LIMITS.sides} sides. Use a smaller die, like 1d100.`;
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
      if (faces.length > LIMITS.diceInGroup) throw new DiceError(`A custom die has too many faces. Use at most ${LIMITS.diceInGroup}, or a range, like d[1, 5000].`);
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
  if (!Number.isInteger(sides) || sides < 1) throw new DiceError(`A die needs at least 1 side, not ${sides}. Use 1 or more, like 1d6.`);
  if (sides > LIMITS.sides) throw new DiceError(TOO_MANY_SIDES);
  return range(1, sides);
}
function checkedSpan(min, max) {
  if (max - min + 1 > LIMITS.sides) throw new DiceError(TOO_MANY_SIDES);
  return range(min, max);
}

// src/engine/random.ts
var defaultRandom = (min, max) => min + Math.floor(Math.random() * (max - min + 1));

// src/engine/state.ts
function spend(state) {
  if (++state.budget.rolls > LIMITS.rollsPerFormula) {
    throw new DiceError(TOO_MANY_ROLLS_MESSAGE);
  }
}
function rollDie(faces, state) {
  spend(state);
  return faces.roll(state.random);
}
function spendStep(budget) {
  if (++budget.steps > LIMITS.stepsPerRoll) throw new DiceError("This formula is too complex to work out. Make it simpler, with fewer dice and fewer named formulas, like 4d6kh3 + 2.");
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

// src/engine/modifiers.ts
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
    throw new DiceError(`${active.length} dice cannot all differ: there are only ${faces.size} results. Roll fewer dice or a bigger die, like 3d6u.`);
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

// src/engine/evaluate.ts
function evaluateDice(node, state) {
  const count = node.count ? evaluate(node.count, state).value : state.defaultCount;
  if (!Number.isInteger(count)) throw new DiceError(`The number of dice must be whole, not ${formatNumber(count)}. Use a whole number before the d, like 2d6.`);
  if (count < 0) throw new DiceError(`The number of dice cannot be negative (${count}). Use 0 or more, like 2d6.`);
  if (count > LIMITS.diceInGroup) throw new DiceError(tooManyDiceMessage(count));
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
    if (!Number.isFinite(value)) throw new DiceError(TOO_LARGE_MESSAGE);
  }
  return { value, text: `[${dice.map(showDie).join(", ")}]` };
}
function lookupName(names, name) {
  return names && Object.prototype.hasOwnProperty.call(names, name) ? names[name] : void 0;
}
function insideName(name, state, work) {
  const formula = lookupName(state.names, name);
  if (formula === void 0) throw new DiceError(`Unknown name "${name}". Check the spelling, or add ${name} to the frontmatter or the saved formulas, like ${name}: 2.`);
  if (state.aliasStack.includes(name) || state.aliasStack.length >= LIMITS.aliasDepth) {
    throw new DiceError(`The named formula "${name}" refers to itself. Change that saved formula so it does not use "${name}", like 1d20 + 5.`);
  }
  state.aliasStack.push(name);
  const result = work(parseFormula(formula, Object.keys(state.names)));
  state.aliasStack.pop();
  return result;
}
function evaluateName(name, state) {
  return insideName(name, state, (node) => evaluate(node, state));
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
    case "stunt":
      return rollStunt(() => rollDie(range(1, 6), state).value);
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
      if (b === 0) throw new DiceError("Cannot divide by zero. Check the number after /, like 10 / 2.");
      value = a / b;
      break;
    default:
      value = Math.pow(a, b);
  }
  if (!Number.isFinite(value)) throw new DiceError(TOO_LARGE_MESSAGE);
  return value;
}
function roll(formula, options = {}) {
  var _a;
  const node = parseFormula(formula, Object.keys((_a = options.names) != null ? _a : {}));
  const { value, text } = evaluate(node, makeState(options));
  return { formula: formula.trim(), total: value, breakdown: text };
}

// src/engine/average.ts
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
    case "stunt":
      return STUNT_SPREAD;
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

// src/engine/narrative.ts
var NAMES = {
  ability: "Ability",
  proficiency: "Proficiency",
  difficulty: "Difficulty",
  challenge: "Challenge",
  boost: "Boost",
  setback: "Setback",
  force: "Force"
};
var FACES = {
  boost: ["", "", "S", "S A", "A A", "A"],
  setback: ["", "", "F", "F", "T", "T"],
  ability: ["", "S", "S", "S S", "A", "A", "S A", "A A"],
  difficulty: ["", "F", "F F", "T", "T", "T", "T T", "F T"],
  proficiency: ["", "S", "S", "S S", "S S", "A", "S A", "S A", "S A", "A A", "A A", "Tr"],
  challenge: ["", "F", "F", "F F", "F F", "T", "T", "F T", "F T", "T T", "T T", "De"],
  force: ["D", "D", "D", "D", "D", "D", "D D", "L", "L", "L L", "L L", "L L"]
};
var LETTERS = {
  g: "ability",
  a: "ability",
  y: "proficiency",
  pro: "proficiency",
  d: "difficulty",
  diff: "difficulty",
  r: "challenge",
  c: "challenge",
  b: "boost",
  boo: "boost",
  s: "setback",
  sb: "setback",
  blk: "setback",
  w: "force",
  f: "force"
};
var WORDS = [...Object.keys(LETTERS), "p"].sort((a, b) => b.length - a.length);
var SWITCHES = /* @__PURE__ */ new Set(["a", "c", "d", "diff"]);
function splitLetters(run, from = 0, dead = /* @__PURE__ */ new Set()) {
  if (from === run.length) return [];
  if (dead.has(from)) return null;
  for (const word of WORDS) {
    if (!run.startsWith(word, from)) continue;
    const rest = splitLetters(run, from + word.length, dead);
    if (rest) return [word, ...rest];
  }
  dead.add(from);
  return null;
}
function isOrdinaryPiece(piece) {
  try {
    const node = parseFormula(piece, []);
    return !(node.type === "name" || node.type === "dice" && node.sides.kind === "default" && node.modifiers.length === 0);
  } catch (e) {
    return false;
  }
}
function parseNarrative(formula) {
  if (formula.length > LIMITS.formulaLength) return null;
  const pieces = formula.trim().split(/\s+/);
  const words = [];
  for (const piece of pieces) {
    const text = piece.toLowerCase();
    if (!/^[0-9a-z]*[a-z]$/.test(text) || isOrdinaryPiece(piece)) return null;
    const groups = /(\d*)([a-z]+)/g;
    for (let match = groups.exec(text); match; match = groups.exec(text)) {
      const split = splitLetters(match[2]);
      if (!split) return null;
      split.forEach((word, i) => words.push({ count: i === 0 && match[1] !== "" ? Number(match[1]) : 1, word }));
    }
  }
  const switched = words.some((w) => SWITCHES.has(w.word));
  return words.map(({ count, word }) => {
    if (word !== "p") return { count, kind: LETTERS[word] };
    if (!switched) throw new DiceError("P is ambiguous here: write Y for Proficiency or D for Difficulty");
    return { count, kind: "proficiency" };
  });
}
function isNarrative(formula) {
  try {
    return parseNarrative(formula) !== null;
  } catch (error) {
    return error instanceof DiceError;
  }
}
function showFace(face) {
  return face === "" ? "blank" : face;
}
function summarize(counts) {
  const parts = [];
  const net = counts.S + counts.Tr - counts.F - counts.De;
  if (net > 0) parts.push(`${net} Success`);
  else if (net < 0) parts.push(`${-net} Failure`);
  const edge = counts.A - counts.T;
  if (edge > 0) parts.push(`${edge} Advantage`);
  else if (edge < 0) parts.push(`${-edge} Threat`);
  if (counts.Tr > 0) parts.push(`${counts.Tr} Triumph`);
  if (counts.De > 0) parts.push(`${counts.De} Despair`);
  if (counts.L > 0) parts.push(`${counts.L} Light`);
  if (counts.D > 0) parts.push(`${counts.D} Dark`);
  return parts.length > 0 ? parts.join(", ") : "No result";
}
function rollNarrative(formula, random = defaultRandom, budget = newBudget()) {
  var _a;
  const groups = parseNarrative(formula);
  if (!groups) throw new DiceError(`"${formula.trim()}" is not narrative dice. Write a number and a letter for each kind, like 3g2d.`);
  const total = groups.reduce((sum, g) => sum + g.count, 0);
  if (total > LIMITS.diceInGroup) throw new DiceError(tooManyDiceMessage(total));
  const counts = { S: 0, F: 0, A: 0, T: 0, Tr: 0, De: 0, L: 0, D: 0 };
  const shown = /* @__PURE__ */ new Map();
  for (const { count, kind } of groups) {
    const faces = FACES[kind];
    const list = (_a = shown.get(kind)) != null ? _a : [];
    shown.set(kind, list);
    for (let i = 0; i < count; i++) {
      if (++budget.rolls > LIMITS.rollsPerFormula) throw new DiceError(TOO_MANY_ROLLS_MESSAGE);
      const face = faces[random(1, faces.length) - 1];
      for (const symbol of face.split(" ")) if (symbol !== "") counts[symbol]++;
      list.push(showFace(face));
    }
  }
  const breakdown = [...shown].filter(([, list]) => list.length > 0).map(([kind, list]) => `${NAMES[kind]} [${list.join(", ")}]`).join("; ");
  return { summary: summarize(counts), breakdown: breakdown === "" ? "No dice" : breakdown, counts };
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
function changeFor(lineText, code, formula, replacement) {
  if (!code || !code.modify || code.formula !== formula) return null;
  return { from: code.from, to: code.to, insert: fitReplacement(lineText, code.from, code.to, replacement) };
}
function replacementInLine(lineText, index, formula, replacement) {
  return changeFor(lineText, findInlineDice(lineText)[index], formula, replacement);
}
function replaceCodeInLine(lineText, index, formula, replacement) {
  const change = replacementInLine(lineText, index, formula, replacement);
  return change === null ? null : lineText.slice(0, change.from) + change.insert + lineText.slice(change.to);
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

// src/result-listeners.ts
var ResultListeners = class {
  constructor() {
    this.byKey = /* @__PURE__ */ new Map();
  }
  /** Returns the function that stops listening; call it when the widget goes away. */
  on(key, listener) {
    let set = this.byKey.get(key);
    if (!set) {
      set = /* @__PURE__ */ new Set();
      this.byKey.set(key, set);
    }
    set.add(listener);
    return () => {
      const current = this.byKey.get(key);
      if (!current) return;
      current.delete(listener);
      if (current.size === 0) this.byKey.delete(key);
    };
  }
  emit(key, outcome) {
    var _a;
    for (const listener of [...(_a = this.byKey.get(key)) != null ? _a : []]) listener(outcome);
  }
  /** How many keys have a listener; for tests. */
  get size() {
    return this.byKey.size;
  }
};

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
var THEMATIC_BREAK = /^ {0,3}([-*_])(?:[ \t]*\1){2,}[ \t]*$/;
function noteLines(markdown) {
  var _a;
  const lines = markdown.replace(/\r\n/g, "\n").split("\n");
  let start = 0;
  if (((_a = lines[0]) == null ? void 0 : _a.trim()) === "---") {
    const end = lines.findIndex((line, index) => index > 0 && line.trim() === "---");
    if (end > 0) start = end + 1;
  }
  return lines.slice(start).filter((line) => line.trim() !== "" && !THEMATIC_BREAK.test(line));
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
  if (args.length > 0) throw new DiceError(`Unknown flag "${args[0]}". Check the spelling after |, like 1d20|avg or 1d20|text(Attack).`);
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
    throw new DiceError(`This roll picks more than ${LIMITS.picksPerRoll} results. Pick fewer, or nest fewer tables, like 2[[Names^first]].`);
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
  if (!Number.isInteger(count) || count < 0) throw new DiceError(`Cannot pick ${formatNumber(count)} results. Put a whole number of 0 or more before the link, like 2[[Names^first]].`);
  if (count > MAX_PICKS) throw new DiceError(`At most ${MAX_PICKS} results can be picked at once. Use a smaller number before the link, like 10[[Names^first]].`);
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
  var _a, _b, _c, _d, _e;
  const random = (_a = context.random) != null ? _a : defaultRandom;
  spendPick(context);
  if (table.rows.length === 0) throw new DiceError("The table has no rows. Add a row under the header, like | Goblin |.");
  const formula = lookupFormula(table);
  let columnIndex = -1;
  if (column !== void 0) {
    columnIndex = findColumn(table, column);
    if (columnIndex === -1 && column.toLowerCase() !== "xy") {
      throw new DiceError(`The table has no column "${column}". It has: ${table.headers.join(", ")}. Write one of these after |, like |${(_b = table.headers[0]) != null ? _b : ""}.`);
    }
  }
  if (formula !== null) {
    const rolled = roll(formula, diceOptions(context));
    const row2 = findLookupRow(table, rolled.total);
    const shown = formatNumber(rolled.total);
    if (!row2) throw new DiceError(`The lookup table has no row for ${shown}. Add a row that covers it, like | ${shown} | Goblin |.`);
    const cells = columnIndex > 0 ? [(_c = row2[columnIndex]) != null ? _c : ""] : row2.slice(1);
    return { text: await resolveCells(cells, context, depth), detail: `${formula} = ${shown}` };
  }
  const row = pick(table.rows, random);
  if (columnIndex >= 0) return { text: await resolveNested((_d = row[columnIndex]) != null ? _d : "", context, depth), detail: column != null ? column : "" };
  if (column !== void 0) {
    const from = row.length > 1 ? 1 : 0;
    return { text: await resolveNested((_e = row[random(from, row.length - 1)]) != null ? _e : "", context, depth), detail: "xy" };
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
    if (!BLOCK_TYPES.has(type) && !/^heading-[1-6]$/.test(type)) throw new DiceError(`Unknown block type "${type}". Use a type such as paragraph, list, table or heading-2, like [[Note]]|list.`);
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
  if (!note) throw new DiceError(`Note "${target.note}" was not found. Check the name in the link, or add the folder, like [[Folder/Note]].`);
  const count = pickCount(target.prefix, context);
  const blocks = parseBlocks(note.markdown);
  if (target.blockId !== void 0) {
    const block = blocks.find((b) => b.id === target.blockId);
    if (!block) throw new DiceError(`Block ^${target.blockId} was not found in "${target.note}". Check the id, or add ^${target.blockId} on its own line right after that table or list.`);
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
      const picks2 = pickMany(listItems(block.text), count, random, "The list is empty. Add items to it, like - Goblin.", context);
      const texts = [];
      for (const item of picks2) texts.push(await resolveNested(item, context, depth));
      return { kind: "list", text: texts.join(", "), details: "", source: note.path };
    }
    return { kind: "section", text: block.text, details: "", source: note.path };
  }
  if (spec.args.some((arg) => arg.toLowerCase() === "line")) {
    const picks2 = pickMany(noteLines(note.markdown), count, random, `"${target.note}" has no lines. Add some text to it, or link another note, like [[Names]]|line.`, context);
    return { kind: "line", text: picks2.join("\n"), details: "", source: note.path };
  }
  const types = blockTypes(spec.args);
  const empty = types.length === 0 ? `"${target.note}" has no text to pick from. Add some text to it, like - Goblin.` : `"${target.note}" has no matching blocks. Check the block types after |, like [[${target.note}]]|paragraph.`;
  const picks = pickMany(selectBlocks(blocks, types), count, random, empty, context);
  return { kind: "section", text: picks.join("\n\n"), details: "", source: note.path };
}
async function rollTag(spec, context) {
  var _a, _b;
  if (spec.target.kind !== "tag") throw new DiceError("Not a tag");
  const target = spec.target;
  const random = (_a = context.random) != null ? _a : defaultRandom;
  const notes = await context.notesWithTag(target.tag);
  if (notes.length === 0) throw new DiceError(`No notes have the tag #${target.tag}. Check the spelling, or add #${target.tag} to a note, like tags: ${target.tag}.`);
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
  if (parts.length === 0 && count > 0) throw new DiceError(`No matching blocks in notes with #${target.tag}. Check the block types after |, like #${target.tag}|paragraph.`);
  return { kind: "tag", text: parts.join("\n\n"), details: `#${target.tag}: ${chosen.length} note(s)`, source: chosen.length === 1 ? (_b = chosen[0]) == null ? void 0 : _b.path : void 0 };
}
async function rollSpecAt(raw, context, depth, firstRoll = false, average = false) {
  var _a;
  if (depth > MAX_NESTING) throw new DiceError("Rollers are nested too deeply, or a table points at itself. Check that no cell has a dice: code that points back at its own table.");
  const spec = parseSpec(raw, context.aliases);
  const formula = raw.trim();
  if (spec.target.kind === "dice") {
    const dice = spec.target.formula;
    try {
      if (firstRoll && spec.flags.avg || average) {
        const average2 = averageOf(dice, diceOptions(context));
        return { kind: "dice", text: formatResult(average2.value, spec.flags), total: average2.value, estimated: !average2.exact, average: true, formula: dice, details: average2.exact ? "Average" : "Estimated average", flags: spec.flags };
      }
      const result = roll(dice, diceOptions(context));
      return { kind: "dice", text: formatResult(result.total, spec.flags), total: result.total, formula: dice, details: result.breakdown, flags: spec.flags };
    } catch (error) {
      if (!(error instanceof DiceError) || !isNarrative(dice)) throw error;
      if (firstRoll && spec.flags.avg || average) throw new DiceError("Narrative dice have no average");
      const result = rollNarrative(dice, (_a = context.random) != null ? _a : defaultRandom, context.budget);
      return { kind: "dice", text: result.summary, formula: dice, details: result.breakdown, flags: spec.flags };
    }
  }
  const outcome = spec.target.kind === "note" ? await rollNote(spec, context, depth) : await rollTag(spec, context);
  return { flags: spec.flags, ...outcome, formula };
}
function rollSpec(raw, context, options = {}) {
  var _a, _b;
  return rollSpecAt(raw, { ...context, budget: newBudget() }, 0, (_a = options.firstRoll) != null ? _a : false, (_b = options.average) != null ? _b : false);
}

// src/ui/dice-mod.ts
var import_obsidian2 = require("obsidian");
var CHANGED_NOTICE = "The dice-mod code has changed, so nothing was replaced.";
var EMBED_NOTICE = "A dice-mod code in an embedded note cannot be replaced here. Open that note to replace it.";
var RESULT_NOTICE = "A dice-mod code inside a rolled result cannot be replaced.";
var NOT_MARKDOWN_NOTICE = "Only a dice-mod code in a markdown note can be replaced.";
var UNPLACED_NOTICE = "This dice-mod code cannot be replaced here, because its line in the note is unknown.";
var ReplaceCodeModal = class extends import_obsidian2.Modal {
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
    new import_obsidian2.Setting(this.contentEl).addButton((button) => button.setButtonText("Cancel").onClick(() => this.reply(false))).addButton((button) => button.setButtonText("Replace").setCta().onClick(() => this.reply(true)));
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
      new import_obsidian2.Notice(RESULT_NOTICE);
      return;
    }
    if (target.closest(".markdown-embed, .internal-embed")) {
      new import_obsidian2.Notice(EMBED_NOTICE);
      return;
    }
    if (!position) {
      new import_obsidian2.Notice(UNPLACED_NOTICE);
      return;
    }
    const text = modifiedText(outcome, plugin.settings.diceModFormula);
    void plugin.confirmReplace(text).then((replace) => replace ? plugin.replaceInNote(sourcePath, position.line, position.index, formula, text) : false);
  };
}
function editorModifier(plugin, view, target, formula, line, index) {
  return (outcome) => {
    const text = modifiedText(outcome, plugin.settings.diceModFormula);
    void plugin.confirmReplace(text).then((replace) => {
      if (replace) replaceInEditor(view, target, formula, line, index, text);
    });
  };
}
function replaceInEditor(view, target, formula, lineNumber, index, text) {
  if (!target.isConnected || !view.contentDOM.contains(target)) {
    new import_obsidian2.Notice(CHANGED_NOTICE);
    return;
  }
  const doc = view.state.doc;
  const line = lineNumber >= 0 && lineNumber < doc.lines ? doc.line(lineNumber + 1) : null;
  const change = line ? replacementInLine(line.text, index, formula, text) : null;
  if (!line || !change) {
    new import_obsidian2.Notice(CHANGED_NOTICE);
    return;
  }
  view.dispatch({ changes: { from: line.from + change.from, to: line.from + change.to, insert: change.insert }, userEvent: "input" });
}

// src/ui/history-view.ts
var import_obsidian3 = require("obsidian");

// src/ui/history-label.ts
function fileName(path) {
  var _a;
  const last = (_a = path.split("/").pop()) != null ? _a : path;
  return last.replace(/\.md$/i, "").trim();
}
function aliasOf(raw) {
  var _a, _b;
  const head = (_a = splitPipes(raw)[0]) != null ? _a : "";
  const wiki = /\[\[[^\]]*?\|([^\]]*)\]\]\s*$/.exec(head);
  return ((_b = wiki == null ? void 0 : wiki[1]) != null ? _b : "").trim();
}
function countText(prefix) {
  return prefix === "" ? "" : `${prefix}\xD7 `;
}
function targetText(target, raw) {
  var _a;
  if (target.kind === "dice") return target.formula.trim();
  if (target.kind === "tag") return `${countText(target.prefix)}#${target.tag}`;
  const [note = "", ...headings] = target.note.split("#");
  const alias = aliasOf(raw);
  const place = [(_a = target.blockId) != null ? _a : "", ...headings].map((part) => part.trim()).filter((part) => part !== "");
  const name = alias !== "" ? alias : [fileName(note), ...place].filter((part) => part !== "").join(", ");
  return name === "" ? "" : `${countText(target.prefix)}${name}`;
}
function historyLabel(formula) {
  var _a;
  const raw = typeof formula === "string" ? formula : String(formula != null ? formula : "");
  try {
    const spec = parseSpec(raw);
    const shown = targetText(spec.target, raw);
    if (shown === "") return { name: "", formula: raw };
    return { name: ((_a = spec.flags.text) != null ? _a : "").trim(), formula: shown };
  } catch (e) {
    return { name: "", formula: raw };
  }
}

// src/ui/history-view.ts
var HISTORY_VIEW = "rollwright-history";
var RollHistoryView = class extends import_obsidian3.ItemView {
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
      new import_obsidian3.Notice(`${formula}: ${outcome.text}`);
    } catch (error) {
      new import_obsidian3.Notice(error instanceof Error ? error.message : String(error));
    }
  }
  refresh() {
    const root = this.contentEl;
    root.empty();
    root.addClass("rollwright-history");
    const form = root.createEl("form", { cls: "rollwright-history-form" });
    const input = form.createEl("input", { type: "text", placeholder: "1d20 + 5" });
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
      const label = historyLabel(entry.formula);
      if (label.name !== "") item.createDiv({ cls: "rollwright-history-name", text: label.name });
      const formula = item.createDiv({ cls: "rollwright-history-formula", text: label.formula });
      formula.setAttribute("title", entry.formula);
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
      (0, import_obsidian3.setIcon)(again, "refresh-cw");
      again.addEventListener("click", () => void this.rollAndNotify(entry.formula));
    }
  }
};

// src/ui/live-preview.ts
var import_language = require("@codemirror/language");
var import_state4 = require("@codemirror/state");
var import_view = require("@codemirror/view");
var import_obsidian5 = require("obsidian");

// src/ui/widget.ts
var import_obsidian4 = require("obsidian");
var NO_SOURCE_NOTICE = "This result comes from more than one note, so there is no single note to open.";
var SOURCE_GONE_NOTICE = "The note this result came from is no longer there.";
var BLOCK_CLASS = "rollwright-roll-block";
function renderedParts(el) {
  const parts = [];
  for (let i = 0; i < el.childElementCount; i++) {
    const child = el.children.item(i);
    if (child === null) continue;
    if (child.tagName === "DIV" && child.childElementCount > 0) parts.push(...renderedParts(child));
    else parts.push(child);
  }
  return parts;
}
function isBlockValue(value) {
  const parts = renderedParts(value);
  if (parts.length > 1) return true;
  const [only] = parts;
  if (only === void 0) return false;
  return only.tagName !== "P" || only.querySelector("br") !== null;
}
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
  target.removeClass(BLOCK_CLASS);
  (0, import_obsidian4.setIcon)(target.createSpan({ cls: "rollwright-icon" }), "dices");
  (0, import_obsidian4.setTooltip)(target, formula);
}
function showError(target, formula, error) {
  target.empty();
  target.removeClass(BLOCK_CLASS);
  target.addClass("rollwright-error");
  const message = errorMessage(error);
  target.createSpan({ text: `dice: ${formula}` });
  (0, import_obsidian4.setTooltip)(target, message);
  target.setAttribute("data-rollwright-error", message);
}
async function showOutcome(plugin, target, outcome, sourcePath, component) {
  target.empty();
  target.removeClass("rollwright-error");
  target.removeClass(BLOCK_CLASS);
  const { flags } = outcome;
  if (!flags.nodice) {
    (0, import_obsidian4.setIcon)(target.createSpan({ cls: "rollwright-icon" }), "dices");
  }
  if (flags.text !== void 0) target.createSpan({ cls: "rollwright-label", text: `${flags.text}: ` });
  else if (flags.form) target.createSpan({ cls: "rollwright-label", text: `${outcome.formula} -> ` });
  const value = target.createSpan({ cls: "rollwright-value" });
  if (outcome.kind === "dice") {
    value.setText(`${outcome.estimated ? "~" : ""}${outcome.total === void 0 ? outcome.text : formatResult(outcome.total, flags)}`);
  } else {
    await import_obsidian4.MarkdownRenderer.render(plugin.app, defuseRolls(outcome.text), value, sourcePath, component);
    if (value.parentElement !== target) return;
    if (isBlockValue(value)) target.addClass(BLOCK_CLASS);
  }
  (0, import_obsidian4.setTooltip)(target, tooltipFor(outcome));
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
    if (outcome === shown) return;
    shown = outcome;
    await showOutcome(plugin, target, outcome, sourcePath, component);
  };
  const showIfNewest = async (outcome) => {
    const newest = plugin.latestResult(key);
    if (newest !== void 0 && newest !== outcome) return;
    await show(outcome);
  };
  const fail = (error) => {
    shown = null;
    showError(target, formula, error);
  };
  const rerollNow = async () => {
    try {
      if (!modify) {
        await showIfNewest(await plugin.freshResult(key, formula, sourcePath, keep));
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
      await showIfNewest(await plugin.averageResult(key, formula, sourcePath, keep));
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
      new import_obsidian4.Notice(NO_SOURCE_NOTICE);
      return;
    }
    const file = plugin.app.vault.getAbstractFileByPath(shown.source);
    if (!(file instanceof import_obsidian4.TFile)) {
      new import_obsidian4.Notice(SOURCE_GONE_NOTICE);
      return;
    }
    await plugin.app.workspace.getLeaf(pane === true ? "tab" : pane).openFile(file);
  };
  target.setAttribute("tabindex", "0");
  target.addEventListener("keydown", (event) => {
    if (event.key !== "Enter") return;
    event.preventDefault();
    void rerollNow();
  });
  target.addEventListener("click", (event) => {
    if (event.target.instanceOf(Element) && event.target.closest("a")) return;
    event.preventDefault();
    event.stopPropagation();
    const pane = import_obsidian4.Keymap.isModEvent(event);
    if (pane) void modClick(pane);
    else if (event.altKey && !modify) void averageNow();
    else void rerollNow();
  });
  target.addEventListener("mousedown", (event) => event.preventDefault());
  component.register(plugin.resultListeners.on(key, (outcome) => void show(outcome)));
  if (hideFirst && !plugin.hasResult(key, keep)) {
    showBlank(target, formula);
    return;
  }
  plugin.firstResult(key, formula, sourcePath, keep).then(show, fail).catch(fail);
}

// src/ui/live-preview.ts
var components = /* @__PURE__ */ new WeakMap();
var RollWidget = class extends import_view.WidgetType {
  constructor(plugin, formula, key, sourcePath, keep, modify, line, index) {
    super();
    this.plugin = plugin;
    this.formula = formula;
    this.key = key;
    this.sourcePath = sourcePath;
    this.keep = keep;
    this.modify = modify;
    this.line = line;
    this.index = index;
  }
  // The key holds line and index, so a code on another line or place gets a new widget with the right line and index.
  eq(other) {
    return other.key === this.key && other.keep === this.keep && other.modify === this.modify;
  }
  toDOM(view) {
    const span = activeDocument.createElement("span");
    const component = new import_obsidian5.Component();
    component.load();
    components.set(span, component);
    const modify = this.modify ? editorModifier(this.plugin, view, span, this.formula, this.line, this.index) : void 0;
    mountRoll(this.plugin, span, this.formula, this.key, this.sourcePath, component, this.keep, modify);
    return span;
  }
  destroy(dom) {
    var _a;
    (_a = components.get(dom)) == null ? void 0 : _a.unload();
    components.delete(dom);
  }
  ignoreEvent() {
    return true;
  }
};
function build(plugin, view) {
  var _a, _b, _c;
  const builder = new import_state4.RangeSetBuilder();
  const state = view.state;
  if (!state.field(import_obsidian5.editorLivePreviewField, false)) return builder.finish();
  const sourcePath = (_c = (_b = (_a = state.field(import_obsidian5.editorInfoField, false)) == null ? void 0 : _a.file) == null ? void 0 : _b.path) != null ? _c : "";
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
        builder.add(start, end, import_view.Decoration.replace({ widget: new RollWidget(plugin, found.formula, key, sourcePath, found.keep, found.modify, line.number - 1, index) }));
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
        const modeChanged = update.startState.field(import_obsidian5.editorLivePreviewField, false) !== update.state.field(import_obsidian5.editorLivePreviewField, false);
        if (update.docChanged || update.viewportChanged || update.selectionSet || modeChanged) {
          this.decorations = build(plugin, update.view);
        }
      }
    },
    { decorations: (value) => value.decorations }
  );
}

// src/ui/modal.ts
var import_obsidian6 = require("obsidian");
var RollFormulaModal = class extends import_obsidian6.Modal {
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
        new import_obsidian6.Notice(`${formula.trim()}: ${outcome.text}`);
        this.close();
      } catch (error) {
        new import_obsidian6.Notice(error instanceof Error ? error.message : String(error));
      }
    };
    new import_obsidian6.Setting(this.contentEl).setName("Formula").addText((text) => {
      text.setPlaceholder("1d20 + 5").onChange((value) => {
        formula = value;
      });
      text.inputEl.addEventListener("keydown", (event) => {
        if (event.key === "Enter") void submit();
      });
    });
    new import_obsidian6.Setting(this.contentEl).addButton((button) => button.setButtonText("Roll").setCta().onClick(() => void submit()));
  }
  onClose() {
    this.contentEl.empty();
  }
};

// src/ui/reading-view.ts
var import_obsidian7 = require("obsidian");
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
    const child = new import_obsidian7.MarkdownRenderChild(span);
    ctx.addChild(child);
    const modify = dice.modify ? readingModifier(plugin, span, ctx.sourcePath, counted ? position : void 0, formula) : void 0;
    mountRoll(plugin, span, formula, `${ctx.sourcePath}|${place}|${formula}`, ctx.sourcePath, child, keep, modify);
  }
}

// src/ui/settings.ts
var import_obsidian9 = require("obsidian");

// src/ui/skin-preview.ts
var import_obsidian8 = require("obsidian");
var PREVIEW_RESULT = "17";
function renderSkinPreview(parent) {
  const preview = parent.createDiv({ cls: "rollwright-skin-preview" });
  for (const skin of SKINS) {
    const tile = preview.createDiv({ cls: ["rollwright-skin-preview-tile", skin.cssClass] });
    const roll2 = tile.createSpan({ cls: ["rollwright-roll", "rollwright-skin-preview-roll"] });
    (0, import_obsidian8.setIcon)(roll2.createSpan({ cls: "rollwright-icon" }), "dices");
    roll2.createSpan({ cls: "rollwright-value", text: PREVIEW_RESULT });
    tile.createDiv({ cls: "rollwright-skin-preview-name", text: skin.name });
  }
}

// src/ui/settings.ts
function parseWholeNumber(value, min) {
  const text = value.trim();
  if (!/^\d+$/.test(text)) return null;
  const number = Number(text);
  return Number.isSafeInteger(number) && number >= min ? number : null;
}
var COMING_SOON = "Paid skins are coming soon.";
var CHECK_NOTE = "It is checked online at most once every 30 days.";
function licenseStatus(active, checkedAt, error) {
  if (error !== null) return LICENSE_MESSAGES[error];
  if (active) return `Active, checked on ${new Date(checkedAt).toLocaleDateString()}.`;
  return "Paste the key from your purchase email and press Activate.";
}
function renderRow(setting, row) {
  var _a;
  if (row.name !== "") setting.setName(row.name);
  if (row.desc !== void 0) setting.setDesc(row.desc);
  (_a = row.build) == null ? void 0 : _a.call(row, setting);
}
function toDefinition(row) {
  return {
    name: row.name,
    desc: row.desc,
    searchable: row.name !== "",
    render: (setting) => renderRow(setting, row)
  };
}
var RollwrightSettingTab = class extends import_obsidian9.PluginSettingTab {
  constructor(app, plugin) {
    super(app, plugin);
    this.plugin = plugin;
    /** The outcome of the last Activate that failed, shown until the next try. */
    this.lastError = null;
  }
  /** The tab for Obsidian before 1.13. From 1.13 on, Obsidian draws getSettingDefinitions() instead. */
  display() {
    const { containerEl } = this;
    containerEl.empty();
    for (const section of this.sections()) {
      if (section.heading !== void 0) new import_obsidian9.Setting(containerEl).setName(section.heading).setHeading();
      for (const row of section.rows) renderRow(new import_obsidian9.Setting(containerEl), row);
    }
  }
  /** The same rows as display(), so they show up in the settings search of Obsidian 1.13 and later. */
  getSettingDefinitions() {
    return this.sections().flatMap(
      (section) => section.heading === void 0 ? section.rows.map(toDefinition) : [{ type: "group", heading: section.heading, items: section.rows.map(toDefinition) }]
    );
  }
  /** Draw the tab again after a row was added, removed or changed. */
  redraw() {
    if ((0, import_obsidian9.requireApiVersion)("1.13.0")) this.update();
    else this.display();
  }
  /** Every row of the tab, built from the current settings. The one source for both ways of drawing. */
  sections() {
    const settings = this.plugin.settings;
    const save = () => this.plugin.saveSettings();
    const general = [
      {
        name: "Default die",
        desc: "The number of sides when a formula leaves it out, as in 3d.",
        build: (setting) => setting.addText(
          (text) => text.setValue(String(settings.defaultSides)).onChange(async (value) => {
            const sides = parseWholeNumber(value, 1);
            if (sides === null) return;
            settings.defaultSides = sides;
            await save();
          })
        )
      },
      {
        name: "Default number of dice",
        desc: "The number of dice when a formula leaves it out, as in d6.",
        build: (setting) => setting.addText(
          (text) => text.setValue(String(settings.defaultCount)).onChange(async (value) => {
            const count = parseWholeNumber(value, 0);
            if (count === null) return;
            settings.defaultCount = count;
            await save();
          })
        )
      },
      {
        name: "Keep the formula when a dice-mod code is replaced",
        desc: "On: 3d6 -> [2, 5, 4] -> 11. Off: [2, 5, 4] -> 11. Results of tables, lists and notes never show a formula.",
        build: (setting) => setting.addToggle(
          (toggle) => toggle.setValue(settings.diceModFormula).onChange(async (value) => {
            settings.diceModFormula = value;
            await save();
          })
        )
      }
    ];
    const formulas = settings.formulas.map((formula, index) => ({
      name: "",
      build: (setting) => setting.addText(
        (text) => text.setPlaceholder("Name").setValue(formula.name).onChange(async (value) => {
          formula.name = value.trim();
          await save();
        })
      ).addText(
        (text) => text.setPlaceholder("Formula").setValue(formula.formula).onChange(async (value) => {
          formula.formula = value.trim();
          await save();
        })
      ).addExtraButton(
        (button) => button.setIcon("trash").setTooltip("Remove").onClick(async () => {
          settings.formulas.splice(index, 1);
          await save();
          this.redraw();
        })
      )
    }));
    formulas.push(
      {
        name: "Add a formula",
        desc: "Use its name in any roll, such as dice: attack.",
        build: (setting) => setting.addButton(
          (button) => button.setButtonText("Add").onClick(async () => {
            settings.formulas.push({ name: `formula${settings.formulas.length + 1}`, formula: "1d20" });
            await save();
            this.redraw();
          })
        )
      },
      {
        name: "Import saved formulas",
        desc: "Copies named formulas from the data file of the Dice Roller plugin, if you have it. That file is only read, and existing names stay as they are.",
        build: (setting) => setting.addButton(
          (button) => button.setButtonText("Import").onClick(async () => {
            await this.plugin.importSavedFormulas();
            this.redraw();
          })
        )
      }
    );
    return [
      { rows: general },
      { heading: "Saved formulas", rows: formulas },
      { heading: "Skins", rows: this.skinRows() }
    ];
  }
  /** The skin choice with a preview of every skin, then Buy and the key field with Activate only when payment is ready. */
  skinRows() {
    const settings = this.plugin.settings;
    const ready = paymentReady(this.plugin.polarIds);
    const paidNames = SKINS.filter((skin) => skin.paid).map((skin) => skin.name).join(" and ");
    const rows = [
      {
        name: "Skin",
        desc: `All rolling is free. ${paidNames} are paid skins and need a license key.${ready ? "" : ` ${COMING_SOON}`}`,
        build: (setting) => setting.addDropdown((dropdown) => {
          for (const skin of availableSkins(this.plugin.isLicensed)) dropdown.addOption(skin.id, skin.name);
          dropdown.setValue(settings.skin).onChange(async (value) => {
            settings.skin = value;
            await this.plugin.saveSettings();
            this.plugin.applySkin();
          });
        })
      },
      { name: "", build: (setting) => renderSkinPreview(setting.infoEl) }
    ];
    if (!ready) {
      rows.push({ name: "License key", desc: COMING_SOON });
      return rows;
    }
    const status = licenseStatus(this.plugin.isLicensed, settings.licenseCheckedAt, this.lastError);
    rows.push(
      {
        name: "Get the paid skins",
        desc: `${paidNames}. One payment, yours to keep.`,
        build: (setting) => setting.addButton(
          (button) => button.setButtonText(`Buy for ${PRICE_TEXT}`).onClick(() => {
            activeWindow.open(this.plugin.polarIds.buyUrl);
          })
        )
      },
      {
        name: "License key",
        desc: `${status} ${CHECK_NOTE}`,
        build: (setting) => {
          let draft = settings.licenseKey;
          setting.addText(
            (text) => text.setPlaceholder("Your license key").setValue(draft).onChange((value) => {
              draft = value.trim();
            })
          ).addButton(
            (button) => button.setButtonText("Activate").onClick(async () => {
              button.setDisabled(true);
              const outcome = await this.plugin.activateLicense(draft);
              this.lastError = outcome === "valid" ? null : outcome;
              this.redraw();
            })
          );
        }
      }
    );
    return rows;
  }
};

// src/main.ts
var DEFAULT_SETTINGS = {
  defaultSides: 100,
  defaultCount: 1,
  formulas: [],
  history: [],
  licenseKey: "",
  licenseCheckedAt: 0,
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
var RollwrightPlugin = class extends import_obsidian10.Plugin {
  constructor() {
    super(...arguments);
    this.settings = { ...DEFAULT_SETTINGS };
    this.results = /* @__PURE__ */ new Map();
    /** First rolls still on their way (a table reads a note first), so a second view of the same code waits for it. */
    this.pending = /* @__PURE__ */ new Map();
    /** Widgets per key, told about every new result so all views of a place show the same. */
    this.resultListeners = new ResultListeners();
    /** Results of `dice+:`, written to disk with the settings. */
    this.kept = /* @__PURE__ */ new Map();
    this.skinnedDocuments = /* @__PURE__ */ new Set();
    /** The network call, the clock and our Polar ids; tests put in their own. */
    this.licenseRequest = obsidianRequest;
    this.now = () => Date.now();
    this.polarIds = POLAR_IDS;
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
      void this.recheckLicense();
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
  /** The only question the rest of the code asks. A key without a check date is not active. */
  get isLicensed() {
    return paymentReady(this.polarIds) && isLicenseActive(this.settings);
  }
  /** Activate in the settings. Only a valid answer stores the key and unlocks the skins. */
  async activateLicense(key) {
    const outcome = await activateLicense(this.settings, key, this.licenseRequest, this.now(), this.polarIds);
    if (outcome === "valid") await this.saveSettings();
    this.applySkin();
    return outcome;
  }
  /** Quiet check of an active key, at most once per 30 days. Only a clear "not valid" locks. */
  async recheckLicense() {
    if (await recheckLicense(this.settings, this.licenseRequest, this.now(), this.polarIds)) {
      await this.saveSettings();
      this.applySkin();
    }
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
      if (!(file instanceof import_obsidian10.TFile)) return {};
      return fieldNames((_a = this.app.metadataCache.getFileCache(file)) == null ? void 0 : _a.frontmatter);
    } catch (e) {
      return {};
    }
  }
  async readNote(link, sourcePath) {
    const file = this.app.metadataCache.getFirstLinkpathDest(link, sourcePath);
    if (!(file instanceof import_obsidian10.TFile)) return null;
    return { path: file.path, markdown: await this.app.vault.cachedRead(file) };
  }
  async notesWithTag(tag) {
    const wanted = `#${tag}`.toLowerCase();
    const notes = [];
    for (const file of this.app.vault.getMarkdownFiles()) {
      const cache = this.app.metadataCache.getFileCache(file);
      const tags = cache ? (0, import_obsidian10.getAllTags)(cache) : null;
      if (tags == null ? void 0 : tags.some((t) => t.toLowerCase() === wanted || t.toLowerCase().startsWith(`${wanted}/`))) {
        notes.push({ path: file.path, markdown: await this.app.vault.cachedRead(file) });
      }
    }
    return notes;
  }
  /** The newest result remembered for a place, if any. */
  latestResult(key) {
    return this.results.get(key);
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
    const running = this.pending.get(key);
    if (running) return running;
    let roll2 = void 0;
    roll2 = (async () => {
      try {
        const outcome = await rollSpec(formula, this.rollContext(sourcePath), { firstRoll: true });
        if (this.pending.get(key) !== roll2) return outcome;
        const newer = this.results.get(key);
        if (newer) return newer;
        this.remember(key, outcome);
        if (keep) await this.keep(key, outcome);
        return outcome;
      } finally {
        if (this.pending.get(key) === roll2) this.pending.delete(key);
      }
    })();
    this.pending.set(key, roll2);
    return roll2;
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
    this.pending.delete(key);
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
    this.resultListeners.emit(key, outcome);
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
    if (!(file instanceof import_obsidian10.TFile)) {
      new import_obsidian10.Notice(CHANGED_NOTICE);
      return false;
    }
    if (file.extension !== "md") {
      new import_obsidian10.Notice(NOT_MARKDOWN_NOTICE);
      return false;
    }
    let done = false;
    await this.app.vault.process(file, (data) => {
      const next = replaceCodeInNote(data, line, index, formula, replacement);
      done = next !== null;
      return next != null ? next : data;
    });
    if (!done) new import_obsidian10.Notice(CHANGED_NOTICE);
    return done;
  }
  currentNotePath() {
    var _a, _b, _c;
    return (_c = (_b = (_a = this.app.workspace.getActiveViewOfType(import_obsidian10.MarkdownView)) == null ? void 0 : _a.file) == null ? void 0 : _b.path) != null ? _c : "";
  }
  /** Reads the named formulas of the other plugin. Reads only; its file stays as it is. */
  async importSavedFormulas() {
    const path = `${this.app.vault.configDir}/plugins/obsidian-dice-roller/data.json`;
    const adapter = this.app.vault.adapter;
    if (!await adapter.exists(path)) {
      new import_obsidian10.Notice("No saved formulas found to import.");
      return;
    }
    const found = extractSavedFormulas(await adapter.read(path));
    const { merged, added } = mergeFormulas(this.settings.formulas, found);
    this.settings.formulas = merged;
    await this.saveSettings();
    new import_obsidian10.Notice(`Imported ${added} of ${found.length} saved formulas.`);
  }
};
