import { parseFormula } from "./parser";
import { formatNumber } from "./format";
import { defaultRandom } from "./random";
import { compare, matchesAny } from "./compare";
import { rollStunt, STUNT_SPREAD } from "./stunt";
import { DiceError, LIMITS, newBudget, type Budget, type Condition, type Modifier, type Node, type RandomInt, type RollOptions, type RollResult, type Sides } from "./types";

interface Die {
	value: number;
	label?: string;
	dropped?: boolean;
	exploded?: boolean;
	rerolled?: boolean;
	score?: number;
}

interface Faces {
	min: number;
	max: number;
	/** How many different results exist. */
	size: number;
	mean: number;
	roll(random: RandomInt): { value: number; label?: string };
}

interface Evaluated {
	value: number;
	text: string;
}

interface State {
	random: RandomInt;
	defaultSides: number;
	defaultCount: number;
	names: Record<string, string>;
	budget: Budget;
	aliasStack: string[];
}

function range(min: number, max: number): Faces {
	return { min, max, size: max - min + 1, mean: (min + max) / 2, roll: (random) => ({ value: random(min, max) }) };
}

function resolveFaces(sides: Sides, state: State): Faces {
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
				},
			};
		case "faces": {
			const faces = sides.faces;
			if (faces.length > LIMITS.diceInGroup) throw new DiceError("A custom die has too many faces");
			return {
				min: Math.min(...faces),
				max: Math.max(...faces),
				size: new Set(faces).size,
				mean: faces.reduce((a, b) => a + b, 0) / faces.length,
				roll: (random) => ({ value: faces[random(0, faces.length - 1)] as number }),
			};
		}
		case "digits": {
			const digits = sides.digits;
			const join = (values: number[]) => Number(values.join(""));
			return {
				min: join(digits.map(() => 1)),
				max: join(digits),
				size: digits.reduce((a, b) => a * b, 1),
				mean: digits.reduce((sum, d) => sum * 10 + (d + 1) / 2, 0),
				roll: (random) => {
					const values = digits.map((d) => random(1, d));
					return { value: join(values), label: values.join(",") };
				},
			};
		}
	}
}

function checkedSides(sides: number): Faces {
	if (!Number.isInteger(sides) || sides < 1) throw new DiceError(`A die needs at least 1 side, not ${sides}`);
	if (sides > LIMITS.sides) throw new DiceError(`A die can have at most ${LIMITS.sides} sides`);
	return range(1, sides);
}

function checkedSpan(min: number, max: number): Faces {
	if (max - min + 1 > LIMITS.sides) throw new DiceError(`A die can have at most ${LIMITS.sides} sides`);
	return range(min, max);
}

function spend(state: State): void {
	if (++state.budget.rolls > LIMITS.rollsPerFormula) {
		throw new DiceError(`This formula rolls more than ${LIMITS.rollsPerFormula} dice`);
	}
}

function rollDie(faces: Faces, state: State): Die {
	spend(state);
	return faces.roll(state.random);
}

function applyKeepDrop(dice: Die[], mod: Extract<Modifier, { kind: "keep" | "drop" }>): void {
	const active = dice.filter((d) => !d.dropped).sort((a, b) => a.value - b.value);
	const wanted = Math.min(mod.count, active.length);
	let toDrop: Die[];
	if (mod.kind === "keep") {
		toDrop = mod.which === "high" ? active.slice(0, active.length - wanted) : active.slice(wanted);
	} else {
		toDrop = mod.which === "low" ? active.slice(0, wanted) : active.slice(active.length - wanted);
	}
	for (const die of toDrop) die.dropped = true;
}

function applyExplode(dice: Die[], mod: Extract<Modifier, { kind: "explode" }>, faces: Faces, state: State): Die[] {
	const conditions: Condition[] = mod.conditions.length > 0 ? mod.conditions : [{ op: "=", value: faces.max }];
	const output: Die[] = [];
	for (const die of dice) {
		output.push(die);
		if (die.dropped) continue;
		let current = die;
		for (let i = 0; i < mod.times && matchesAny(current.value, conditions); i++) {
			current.exploded = true;
			const extra = rollDie(faces, state);
			if (mod.combine) {
				die.value += extra.value;
				die.label = undefined;
			} else {
				output.push(extra);
			}
			current = mod.combine ? { value: extra.value } : extra;
		}
	}
	return output;
}

function applyReroll(dice: Die[], mod: Extract<Modifier, { kind: "reroll" }>, faces: Faces, state: State): void {
	const conditions: Condition[] = mod.conditions.length > 0 ? mod.conditions : [{ op: "=", value: faces.min }];
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

function applyUnique(dice: Die[], faces: Faces, state: State): void {
	const active = dice.filter((d) => !d.dropped);
	if (active.length > faces.size) {
		throw new DiceError(`${active.length} dice cannot all differ: there are only ${faces.size} results`);
	}
	const seen = new Set<number>();
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

function showDie(die: Die): string {
	let text = die.label ?? formatNumber(die.value);
	if (die.dropped) text += "d";
	if (die.exploded) text += "!";
	if (die.rerolled) text += "r";
	if (die.score === 1) text += "*";
	if (die.score === -1) text += "-";
	return text;
}

function evaluateDice(node: Extract<Node, { type: "dice" }>, state: State): Evaluated {
	const count = node.count ? evaluate(node.count, state).value : state.defaultCount;
	if (!Number.isInteger(count)) throw new DiceError(`The number of dice must be whole, not ${formatNumber(count)}`);
	if (count < 0) throw new DiceError(`The number of dice cannot be negative (${count})`);
	if (count > LIMITS.diceInGroup) throw new DiceError(`At most ${LIMITS.diceInGroup} dice can be rolled at once, not ${count}`);
	const faces = resolveFaces(node.sides, state);

	let dice: Die[] = [];
	for (let i = 0; i < count; i++) dice.push(rollDie(faces, state));

	const counting: Extract<Modifier, { kind: "count" }>[] = [];
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
				dice = [...dice].sort((a, b) => (mod.direction === "asc" ? a.value - b.value : b.value - a.value));
				break;
			case "count":
				counting.push(mod);
				break;
		}
	}

	const active = dice.filter((d) => !d.dropped);
	let value: number;
	if (counting.length > 0) {
		const targets = counting.map((c) => ({ c, target: evaluate(c.threshold, state).value }));
		for (const die of active) {
			const hit = targets.find(({ c, target }) => compare(die.value, c.op, target));
			die.score = hit ? hit.c.score : 0;
		}
		value = active.reduce((sum, d) => sum + (d.score ?? 0), 0);
	} else {
		value = active.reduce((sum, d) => sum + d.value, 0);
		if (!Number.isFinite(value)) throw new DiceError("The result is too large to show");
	}
	return { value, text: `[${dice.map(showDie).join(", ")}]` };
}

/** Own keys only, so a name like "constructor" is simply unknown. */
function lookupName(names: Record<string, string> | undefined, name: string): string | undefined {
	return names && Object.prototype.hasOwnProperty.call(names, name) ? names[name] : undefined;
}

/** Runs work on the formula behind a name, and guards against names that refer to themselves. */
function insideName<T>(name: string, state: State, work: (node: Node) => T): T {
	const formula = lookupName(state.names, name);
	if (formula === undefined) throw new DiceError(`Unknown name "${name}"`);
	if (state.aliasStack.includes(name) || state.aliasStack.length >= LIMITS.aliasDepth) {
		throw new DiceError(`The named formula "${name}" refers to itself`);
	}
	state.aliasStack.push(name);
	const result = work(parseFormula(formula, Object.keys(state.names)));
	state.aliasStack.pop();
	return result;
}

function evaluateName(name: string, state: State): Evaluated {
	return insideName(name, state, (node) => evaluate(node, state));
}

function spendStep(budget: Budget): void {
	if (++budget.steps > LIMITS.stepsPerRoll) throw new DiceError("This formula is too complex to work out");
}

function evaluate(node: Node, state: State): Evaluated {
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

function calculate(op: string, a: number, b: number): number {
	let value: number;
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

function makeState(options: RollOptions): State {
	return {
		random: options.random ?? defaultRandom,
		defaultSides: options.defaultSides ?? 100,
		defaultCount: options.defaultCount ?? 1,
		names: options.names ?? {},
		budget: options.budget ?? newBudget(),
		aliasStack: [],
	};
}

/** Rolls a formula. Throws DiceError with a readable message when it is broken. */
export function roll(formula: string, options: RollOptions = {}): RollResult {
	const node = parseFormula(formula, Object.keys(options.names ?? {}));
	const { value, text } = evaluate(node, makeState(options));
	return { formula: formula.trim(), total: value, breakdown: text };
}

/** What is known for sure about a part of a formula that has no modifiers. */
interface Spread {
	mean: number;
	min: number;
	max: number;
	whole: boolean;
}

function constant(value: number): Spread {
	return { mean: value, min: value, max: value, whole: Number.isInteger(value) };
}

function isConstant(spread: Spread): boolean {
	return spread.min === spread.max;
}

function corners(a: Spread, b: Spread): { min: number; max: number } {
	const products = [a.min * b.min, a.min * b.max, a.max * b.min, a.max * b.max];
	return { min: Math.min(...products), max: Math.max(...products) };
}

/**
 * Works out the exact mean, or returns null when only a simulation can tell.
 * Every part of a formula rolls its own dice, so parts are independent: a sum and a
 * product of means are exact. Dividing by a die or a power of a die is not linear
 * ((1d4)^2 is 7.5, while (mean 2.5)^2 is 6.25), so those give null. Neither do counts
 * that could fail in a real roll get a mean.
 */
function exactSpread(node: Node, state: State): Spread | null {
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

function exactDice(node: Extract<Node, { type: "dice" }>, state: State): Spread | null {
	if (node.modifiers.length > 0) return null;
	const count = node.count ? exactSpread(node.count, state) : constant(state.defaultCount);
	// Only a count that always works in a real roll: whole, not negative, within the limit.
	if (!count || !count.whole || count.min < 0 || count.max > LIMITS.diceInGroup) return null;
	const faces = resolveFaces(node.sides, state);
	const facesSpread = { mean: faces.mean, min: faces.min, max: faces.max, whole: true };
	return { mean: calculate("*", count.mean, faces.mean), ...corners(count, facesSpread), whole: true };
}

const AVERAGE_SAMPLES = 2000;

/**
 * The expected result. Exact where the rules of means allow it (see exactSpread),
 * otherwise an estimate from at most 2000 simulated rolls, as far as the budget of one roll reaches.
 */
export function averageOf(formula: string, options: RollOptions = {}): { value: number; exact: boolean } {
	const node = parseFormula(formula, Object.keys(options.names ?? {}));
	const exact = exactSpread(node, makeState({ ...options, budget: undefined }));
	if (exact) return { value: exact.mean, exact: true };
	let mean = 0;
	let samples = 0;
	// One budget for all samples: a heavy formula gets fewer samples, not more time.
	const budget = newBudget();
	for (; samples < AVERAGE_SAMPLES; samples++) {
		try {
			// A running mean, because a sum of very large results could overflow.
			mean += (evaluate(node, makeState({ ...options, budget })).value - mean) / (samples + 1);
		} catch (error) {
			const spent = budget.rolls > LIMITS.rollsPerFormula || budget.steps > LIMITS.stepsPerRoll;
			if (!spent || samples === 0) throw error;
			break;
		}
	}
	return { value: mean, exact: false };
}
