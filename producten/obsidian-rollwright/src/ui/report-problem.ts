import { apiVersion, Platform } from "obsidian";

/**
 * Command "Report a problem" (roestronde R5): opens a new GitHub issue with the Rollwright version, the Obsidian
 * version and the system already filled in. Only a link the user opens; nothing is sent by itself (Obsidian bans
 * client-side telemetry). No `template=` in the link, so it works with or without an issue form in the repository.
 */
export const ISSUES_URL = "https://github.com/thijsduinhouwer2002-coder/rollwright/issues/new";

/** The parts of Platform we read; tests pass their own. */
export interface PlatformFlags {
	isMacOS?: boolean;
	isWin?: boolean;
	isLinux?: boolean;
	isIosApp?: boolean;
	isAndroidApp?: boolean;
	isMobile?: boolean;
}

/** "Windows (desktop)", "iOS (mobile)", ...: no user name, no paths. */
export function systemName(p: PlatformFlags): string {
	const os = p.isIosApp ? "iOS" : p.isAndroidApp ? "Android" : p.isMacOS ? "macOS" : p.isWin ? "Windows" : p.isLinux ? "Linux" : "unknown";
	return `${os} (${p.isMobile ? "mobile" : "desktop"})`;
}

export function reportBody(version: string, obsidian: string, system: string): string {
	return [
		"**What happened?**",
		"",
		"",
		"**What did you expect?**",
		"",
		"",
		"**Steps to reproduce** (the dice code from your note helps a lot)",
		"",
		"",
		"---",
		`Rollwright: ${version}`,
		`Obsidian: ${obsidian}`,
		`System: ${system}`,
	].join("\n");
}

export function reportUrl(version: string, obsidian: string, system: string): string {
	const fields: [string, string][] = [
		["version", version],
		["obsidian", obsidian],
		["os", system],
		["body", reportBody(version, obsidian, system)],
	];
	return `${ISSUES_URL}?${fields.map(([k, v]) => `${k}=${encodeURIComponent(v)}`).join("&")}`;
}

/** The link for this Obsidian. */
export function reportUrlHere(version: string): string {
	return reportUrl(version, apiVersion, systemName(Platform));
}
