import { parseFormula } from "./parser";
import { formatNumber } from "./format";
import { defaultRandom } from "./random";
import { DiceError, LIMITS, type CompareOp, type Condition, type Modifier, type Node, type RandomInt, type RollOptions, type RollResult, type Sides } from "./types";

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
	rolls: number;
	aliasStack: string[];
	/** Replace each die by its mean instead of rolling. */
	useMean: boolean;
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

function compare(value: number, op: CompareOp, target: number): boolean {
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

function matchesAny(value: number, conditions: Condition[]): boolean {
	return conditions.some((c) => compare(value, c.op, c.value));
}

function spend(state: State): void {
	if (++state.rolls > LIMITS.rollsPerFormula) {
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
	if (!state.useMean && !Number.isInteger(count)) throw new DiceError(`The number of dice must be whole, not ${formatNumber(count)}`);
	if (count < 0) throw new DiceError(`The number of dice cannot be negative (${count})`);
	if (count > LIMITS.diceInGroup) throw new DiceError(`At most ${LIMITS.diceInGroup} dice can be rolled at once, not ${count}`);
	const faces = resolveFaces(node.sides, state);

	if (state.useMean) {
		const value = count * faces.mean;
		return { value, text: formatNumber(value) };
	}

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
	}
	return { value, text: `[${dice.map(showDie).join(", ")}]` };
}

/** Own keys only, so a name like "constructor" is simply unknown. */
function lookupName(names: Record<string, string> | undefined, name: string): string | undefined {
	return names && Object.prototype.hasOwnProperty.call(names, name) ? names[name] : undefined;
}

function evaluateName(name: string, state: State): Evaluated {
	const formula = lookupName(state.names, name);
	if (formula === undefined) throw new DiceError(`Unknown name "${name}"`);
	if (state.aliasStack.includes(name) || state.aliasStack.length >= LIMITS.aliasDepth) {
		throw new DiceError(`The named formula "${name}" refers to itself`);
	}
	state.aliasStack.push(name);
	const result = evaluate(parseFormula(formula, Object.keys(state.names)), state);
	state.aliasStack.pop();
	return result;
}

function evaluate(node: Node, state: State): Evaluated {
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

function makeState(options: RollOptions, useMean = false, random?: RandomInt): State {
	return {
		random: random ?? options.random ?? defaultRandom,
		defaultSides: options.defaultSides ?? 100,
		defaultCount: options.defaultCount ?? 1,
		names: options.names ?? {},
		rolls: 0,
		aliasStack: [],
		useMean,
	};
}

/** Rolls a formula. Throws DiceError with a readable message when it is broken. */
export function roll(formula: string, options: RollOptions = {}): RollResult {
	const node = parseFormula(formula, Object.keys(options.names ?? {}));
	const { value, text } = evaluate(node, makeState(options));
	return { formula: formula.trim(), total: value, breakdown: text };
}

function hasModifiers(node: Node, options: RollOptions, seen: string[] = []): boolean {
	switch (node.type) {
		case "number":
			return false;
		case "name": {
			const formula = lookupName(options.names, node.name);
			if (formula === undefined || seen.includes(node.name)) return false;
			return hasModifiers(parseFormula(formula, Object.keys(options.names ?? {})), options, [...seen, node.name]);
		}
		case "negate":
		case "group":
			return hasModifiers(node.inner, options, seen);
		case "binary":
			return hasModifiers(node.left, options, seen) || hasModifiers(node.right, options, seen);
		case "dice":
			return node.modifiers.length > 0 || (node.count !== null && node.count.type !== "number" && hasModifiers(node.count, options, seen));
	}
}

const AVERAGE_SAMPLES = 2000;

/**
 * The expected result. Exact without modifiers (dice replaced by their mean),
 * otherwise an estimate from simulated rolls.
 */
export function averageOf(formula: string, options: RollOptions = {}): { value: number; exact: boolean } {
	const node = parseFormula(formula, Object.keys(options.names ?? {}));
	if (!hasModifiers(node, options)) {
		return { value: evaluate(node, makeState(options, true)).value, exact: true };
	}
	let sum = 0;
	for (let i = 0; i < AVERAGE_SAMPLES; i++) sum += evaluate(node, makeState(options)).value;
	return { value: sum / AVERAGE_SAMPLES, exact: false };
}
