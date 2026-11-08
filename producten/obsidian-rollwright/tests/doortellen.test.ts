import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";
import type { RandomInt } from "../src/engine";
import RollwrightPlugin from "../src/main";
import { mountRoll, startTicking, TICK_ATTR, TICK_STEPS } from "../src/ui/widget";

// Ontwerp-v2 klus 4: het getal telt na een klik ±300 ms door en landt op de echte uitkomst.

/** A value element that remembers its attribute, and every number it showed. */
function fakeValue() {
	const seen: string[] = [];
	const attrs = new Map<string, string>();
	return {
		seen,
		attrs,
		setAttribute: (name: string, value: string) => {
			attrs.set(name, value);
			if (name === TICK_ATTR) seen.push(value);
		},
		removeAttribute: (name: string) => attrs.delete(name),
	};
}

/** A roll element whose created value span is a fakeValue, with text. */
function fakeRoll() {
	const classes = new Set<string>();
	const listeners: Record<string, (event: unknown) => void> = {};
	const values: (ReturnType<typeof fakeValue> & { text: string })[] = [];
	const el = {
		classes,
		listeners,
		values,
		empty() {},
		addClass: (cls: string) => classes.add(cls),
		removeClass: (cls: string) => classes.delete(cls),
		setAttribute() {},
		removeAttribute() {},
		setText() {},
		createSpan: (options?: { cls?: string }) => {
			if (options?.cls !== "rollwright-value") return el;
			const value = Object.assign(fakeValue(), { text: "", setText: (text: string) => (value.text = text), parentElement: el });
			values.push(value);
			return value;
		},
		addEventListener: (name: string, listener: (event: unknown) => void) => (listeners[name] = listener),
		closest: () => null,
	};
	return el;
}

let reduce = false;
beforeEach(() => {
	reduce = false;
	vi.useFakeTimers();
	vi.stubGlobal("Element", class {});
	vi.stubGlobal("activeDocument", { body: { toggleClass() {}, removeClass() {} } });
	vi.stubGlobal("activeWindow", {
		matchMedia: () => ({ matches: reduce }),
		setTimeout: (fn: () => void, ms: number) => setTimeout(fn, ms),
		clearTimeout: (id: number) => clearTimeout(id),
	});
});
afterEach(() => {
	vi.useRealTimers();
	vi.unstubAllGlobals();
});

describe("startTicking", () => {
	it("shows 6 numbers within the range, slower each time, ±300 ms, then takes the attribute away", () => {
		const value = fakeValue();
		const stop = startTicking(value as never, { min: 1, max: 20 });
		expect(stop).not.toBeNull();
		expect(TICK_STEPS).toHaveLength(6);
		expect(TICK_STEPS.reduce((a, b) => a + b, 0)).toBe(300);
		for (let i = 1; i < TICK_STEPS.length; i++) expect(TICK_STEPS[i]).toBeGreaterThan(TICK_STEPS[i - 1] as number);
		vi.advanceTimersByTime(299);
		expect(value.attrs.has(TICK_ATTR)).toBe(true);
		vi.advanceTimersByTime(1);
		expect(value.attrs.has(TICK_ATTR)).toBe(false);
		expect(value.seen).toHaveLength(6);
		for (const n of value.seen) expect(Number(n)).toBeGreaterThanOrEqual(1);
		for (const n of value.seen) expect(Number(n)).toBeLessThanOrEqual(20);
		expect(vi.getTimerCount()).toBe(0);
	});

	it("does nothing without a known range, for a fixed result, or with reduced motion", () => {
		expect(startTicking(fakeValue() as never, null)).toBeNull();
		expect(startTicking(fakeValue() as never, { min: 7, max: 7 })).toBeNull();
		reduce = true;
		const value = fakeValue();
		expect(startTicking(value as never, { min: 1, max: 20 })).toBeNull();
		expect(value.seen).toEqual([]);
		expect(vi.getTimerCount()).toBe(0);
	});

	it("stops at once: no timer keeps running", () => {
		const value = fakeValue();
		const stop = startTicking(value as never, { min: 2, max: 12 });
		vi.advanceTimersByTime(50);
		stop?.();
		expect(vi.getTimerCount()).toBe(0);
		expect(value.attrs.has(TICK_ATTR)).toBe(false);
	});
});

async function load() {
	const plugin = new (RollwrightPlugin as unknown as new (app: unknown) => RollwrightPlugin)({
		workspace: { on: vi.fn(), getLeavesOfType: () => [], getActiveViewOfType: () => null, onLayoutReady: (callback: () => void) => callback(), iterateAllLeaves: () => {} },
		metadataCache: { getFirstLinkpathDest: () => null, getFileCache: () => ({}) },
		vault: { configDir: ".obsidian", cachedRead: async () => "", getMarkdownFiles: () => [], getAbstractFileByPath: () => null },
	});
	(plugin as unknown as { stored: unknown }).stored = null;
	await plugin.onload();
	const random: RandomInt = (_min, max) => max;
	const original = plugin.rollContext.bind(plugin);
	plugin.rollContext = (sourcePath) => ({ ...original(sourcePath), random });
	return plugin;
}

const press = () => ({ target: { instanceOf: () => false }, preventDefault() {}, stopPropagation() {} });
const settle = async () => {
	for (let i = 0; i < 20; i++) await Promise.resolve();
};

describe("counting on the roll", () => {
	it("never on opening; after a click it counts while the real text is there all the time, and is gone after 300 ms", async () => {
		const plugin = await load();
		const roll = fakeRoll();
		const cleanups: (() => void)[] = [];
		mountRoll(plugin, roll as never, "1d20+4", "k", "A.md", { register: (fn: () => void) => cleanups.push(fn) } as never);
		await settle();
		expect(roll.values[0]?.seen).toEqual([]);

		roll.listeners.click?.(press());
		await settle();
		const value = roll.values[roll.values.length - 1];
		expect(value?.text).toBe("24");
		expect(value?.attrs.has(TICK_ATTR)).toBe(true);
		vi.advanceTimersByTime(300);
		expect(value?.attrs.has(TICK_ATTR)).toBe(false);
		expect(value?.seen.length).toBe(6);
		expect(value?.text).toBe("24");
		// 24 is a crit: its gold comes with a timer of its own at 460 ms (klus 2d), then nothing runs.
		vi.advanceTimersByTime(160);
		expect(vi.getTimerCount()).toBe(0);
	});

	it("a new click stops the old counting, and so does the roll going away", async () => {
		const plugin = await load();
		const roll = fakeRoll();
		const cleanups: (() => void)[] = [];
		mountRoll(plugin, roll as never, "2d6", "k2", "A.md", { register: (fn: () => void) => cleanups.push(fn) } as never);
		await settle();
		roll.listeners.click?.(press());
		await settle();
		const first = roll.values[roll.values.length - 1];
		vi.advanceTimersByTime(60);
		roll.listeners.click?.(press());
		await settle();
		expect(first?.attrs.has(TICK_ATTR)).toBe(false);
		// The new counting, and the landing of its gold (12 is a crit, klus 2d); the old ones are gone.
		expect(vi.getTimerCount()).toBe(2);
		for (const fn of cleanups) fn();
		expect(vi.getTimerCount()).toBe(0);
	});

	it("does not count a table or list result", async () => {
		const plugin = await load();
		plugin.firstResult = async () => ({ kind: "list", text: "Goblin", formula: "[[M]]", details: "", flags: {} as never });
		plugin.freshResult = async () => ({ kind: "list", text: "Orc", formula: "[[M]]", details: "", flags: {} as never });
		const roll = fakeRoll();
		mountRoll(plugin, roll as never, "[[M]]", "k3", "A.md", { register() {} } as never);
		await settle();
		roll.listeners.click?.(press());
		await settle();
		expect(roll.values.every((v) => v.seen.length === 0)).toBe(true);
		expect(vi.getTimerCount()).toBe(0);
	});
});
