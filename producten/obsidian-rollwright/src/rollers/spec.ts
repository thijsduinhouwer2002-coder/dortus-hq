import { DiceError } from "../engine";

export interface Flags {
	nodice: boolean;
	form: boolean;
	avg: boolean;
	none: boolean;
	text?: string;
}

export type Target =
	| { kind: "dice"; formula: string }
	| { kind: "note"; prefix: string; note: string; blockId?: string }
	| { kind: "tag"; prefix: string; tag: string };

export interface Spec {
	raw: string;
	target: Target;
	flags: Flags;
	/** Everything after "|" that is not a display flag: column names, block types, "line", "-" and so on. */
	args: string[];
}

/** Flags from the notation that we accept and that change nothing in this version. */
const IGNORED_FLAGS = new Set(["dice", "render", "norender", "noform", "paren", "noparen", "round", "noround", "ceil", "floor", "signed"]);

/** Splits on "|", but not inside (), [] or [[]]. */
export function splitPipes(raw: string): string[] {
	const parts: string[] = [];
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

function decodeLink(link: string): string {
	try {
		return decodeURI(link);
	} catch {
		return link;
	}
}

function parseLink(head: string): { prefix: string; note: string; blockId?: string } | null {
	let prefix: string;
	let link: string;
	const wiki = /^(.*?)\[\[(.+?)\]\]$/.exec(head);
	const markdown = /^(.*?)\[[^\][]*\]\(([^()]+)\)$/.exec(head);
	if (wiki) {
		prefix = wiki[1] as string;
		link = (wiki[2] as string).split("|")[0] as string;
	} else if (markdown) {
		prefix = markdown[1] as string;
		link = decodeLink(markdown[2] as string);
	} else {
		return null;
	}
	const caret = link.indexOf("^");
	if (caret === -1) return { prefix: prefix.trim(), note: link.trim() };
	const note = link.slice(0, caret).replace(/#$/, "").trim();
	return { prefix: prefix.trim(), note, blockId: link.slice(caret + 1).trim() };
}

export function parseSpec(raw: string, aliases: Record<string, string> = {}): Spec {
	const [first = "", ...rest] = splitPipes(raw);
	const alias = Object.prototype.hasOwnProperty.call(aliases, first) ? aliases[first] : undefined;
	const pipes = splitPipes(alias !== undefined && !alias.includes(first) ? alias : first);
	const body = pipes[0] ?? "";

	const flags: Flags = { nodice: false, form: false, avg: false, none: false };
	const args: string[] = [];
	for (const part of [...pipes.slice(1), ...rest]) {
		const lower = part.toLowerCase();
		if (lower === "nodice" || lower === "form" || lower === "avg" || lower === "none") {
			flags[lower] = true;
		} else if (lower.startsWith("text(") && part.endsWith(")")) {
			flags.text = part.slice(5, -1);
		} else if (!IGNORED_FLAGS.has(lower) && part !== "") {
			args.push(part);
		}
	}

	const link = parseLink(body);
	if (link) return { raw, flags, args, target: { kind: "note", ...link } };
	const tag = /^(.*?)#([^\s#]+)$/.exec(body);
	if (tag) return { raw, flags, args, target: { kind: "tag", prefix: (tag[1] as string).trim(), tag: tag[2] as string } };
	if (args.length > 0) throw new DiceError(`Unknown flag "${args[0] as string}"`);
	return { raw, flags, args, target: { kind: "dice", formula: body } };
}
