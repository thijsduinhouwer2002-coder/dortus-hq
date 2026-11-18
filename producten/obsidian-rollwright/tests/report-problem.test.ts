import { describe, expect, it } from "vitest";
import { reportBody, reportUrl, reportUrlHere, systemName } from "../src/ui/report-problem";

function fields(url: string): Record<string, string> {
	return Object.fromEntries(new URL(url).searchParams.entries());
}

describe("Report a problem (roestronde R5)", () => {
	it("fills version, Obsidian and system in the issue link", () => {
		const url = reportUrl("0.3.6", "1.9.14", "Windows (desktop)");
		expect(url.startsWith("https://github.com/thijsduinhouwer2002-coder/rollwright/issues/new?")).toBe(true);
		expect(url).not.toContain("template=");
		const f = fields(url);
		expect(f.version).toBe("0.3.6");
		expect(f.obsidian).toBe("1.9.14");
		expect(f.os).toBe("Windows (desktop)");
		expect(f.body).toBe(reportBody("0.3.6", "1.9.14", "Windows (desktop)"));
		expect(f.body).toContain("Rollwright: 0.3.6\nObsidian: 1.9.14\nSystem: Windows (desktop)");
		expect(url.length).toBeLessThan(2000);
	});

	it("names the system without anything personal", () => {
		expect(systemName({ isMacOS: true })).toBe("macOS (desktop)");
		expect(systemName({ isLinux: true })).toBe("Linux (desktop)");
		expect(systemName({ isIosApp: true, isMacOS: true, isMobile: true })).toBe("iOS (mobile)");
		expect(systemName({ isAndroidApp: true, isLinux: true, isMobile: true })).toBe("Android (mobile)");
		expect(systemName({})).toBe("unknown (desktop)");
	});

	it("uses the Platform of Obsidian", () => {
		const f = fields(reportUrlHere("0.3.6"));
		expect(f.os).toBe("Linux (desktop)");
		expect(f.obsidian).toBe("1.7.2");
		expect(f.version).toBe("0.3.6");
	});
});
