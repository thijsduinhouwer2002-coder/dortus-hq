/* Olaf, 28 nov 2026 (issue #401, Daan #394 moet 2). Klein hulpje voor de besturen-stand van Hol 2.0.
 * Het hol pakt de focus alleen in de besturen-stand. Gaat die stand uit (Esc, klik buiten, 10 s geen toets), dan moet
 * de focus terug naar het venster waar je mee werkte, anders typ je in het hol.
 *
 *   focus.exe neem             schrijft het venster dat nu vooraan staat (getal), vóór het hol de focus pakt
 *   focus.exe terug <vorig> <ons>
 *                              zet <vorig> weer vooraan; is dat weg of ons eigen venster, dan het bovenste gewone
 *                              venster onder het hol (zoals Alt+Tab doet). Schrijft wat het deed.
 *
 * Mag het venster naar voren? Windows staat dat toe als het proces gestart is door het proces dat vooraan staat; het hol
 * start dit hulpje terwijl het zelf vooraan staat. Lukt het toch niet, dan nog één keer na een losse Alt-tik.
 * Bouwen: x86_64-w64-mingw32-gcc-win32 -O2 -s -Wall -mwindows -Wl,--no-insert-timestamp focus.c -o focus.exe -luser32 -ldwmapi
 */
#include <windows.h>
#include <dwmapi.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static HWND ons = NULL;
static HWND gevonden = NULL;

static int gewoon(HWND h) {
	char klas[64];
	int verborgen = 0;
	if (h == ons || !IsWindowVisible(h) || IsIconic(h)) return 0;
	if (GetWindow(h, GW_OWNER) != NULL) return 0;
	if (GetWindowLongPtrA(h, GWL_EXSTYLE) & WS_EX_TOOLWINDOW) return 0;
	if (SUCCEEDED(DwmGetWindowAttribute(h, DWMWA_CLOAKED, &verborgen, sizeof(verborgen))) && verborgen) return 0;
	GetClassNameA(h, klas, sizeof(klas));
	if (!strcmp(klas, "Shell_TrayWnd") || !strcmp(klas, "Shell_SecondaryTrayWnd") || !strcmp(klas, "Progman") ||
		!strcmp(klas, "WorkerW")) return 0;
	return 1;
}

static BOOL CALLBACK zoek(HWND h, LPARAM l) {
	(void)l;
	if (gewoon(h)) { gevonden = h; return FALSE; }
	return TRUE;
}

static int naar_voren(HWND h) {
	if (SetForegroundWindow(h) && GetForegroundWindow() == h) return 1;
	/* een losse Alt-tik geeft dit proces het recht om een venster naar voren te halen */
	keybd_event(VK_MENU, 0, 0, 0);
	keybd_event(VK_MENU, 0, KEYEVENTF_KEYUP, 0);
	SetForegroundWindow(h);
	return GetForegroundWindow() == h ? 2 : 0;
}

static void schrijf(const char *s) {
	DWORD n;
	HANDLE uit = GetStdHandle(STD_OUTPUT_HANDLE);
	if (uit && uit != INVALID_HANDLE_VALUE) WriteFile(uit, s, (DWORD)strlen(s), &n, NULL);
}

int main(int argc, char **argv) {
	char r[256], naam[96] = "";
	HWND vorig, doel;
	int ok;
	if (argc >= 2 && !strcmp(argv[1], "neem")) {
		snprintf(r, sizeof(r), "%llu\n", (unsigned long long)(ULONG_PTR)GetForegroundWindow());
		schrijf(r);
		return 0;
	}
	if (argc < 4 || strcmp(argv[1], "terug")) {
		schrijf("gebruik: focus.exe neem | focus.exe terug <vorig> <ons>\n");
		return 2;
	}
	vorig = (HWND)(ULONG_PTR)_strtoui64(argv[2], NULL, 10);
	ons = (HWND)(ULONG_PTR)_strtoui64(argv[3], NULL, 10);
	doel = (vorig && vorig != ons && IsWindow(vorig) && IsWindowVisible(vorig)) ? vorig : NULL;
	if (!doel) {
		EnumWindows(zoek, 0);
		doel = gevonden;
	}
	if (!doel) {
		schrijf("geen venster gevonden\n");
		return 1;
	}
	ok = naar_voren(doel);
	GetClassNameA(doel, naam, sizeof(naam));
	snprintf(r, sizeof(r), "%s %llu (%s, %s)\n", ok ? "terug naar" : "MISLUKT", (unsigned long long)(ULONG_PTR)doel, naam,
		doel == vorig ? "vorig venster" : "bovenste gewone venster");
	schrijf(r);
	return ok ? 0 : 1;
}
