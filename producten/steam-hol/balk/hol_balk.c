/* hol-balk.exe: hulp naast Het Hol (Olaf, 25 nov 2026, issue #24).
 *
 * Wat het doet, voor het venster van het spel (HWND als argument):
 * 1. App-balk: houdt met een eigen onzichtbaar venster een strook onderaan het scherm vrij bij Windows
 *    (SHAppBarMessage ABM_NEW, ABM_QUERYPOS, ABM_SETPOS), zodat gemaximaliseerde vensters boven het spel eindigen.
 *    Daarna zet het het venster van het spel precies in die strook. Bij stoppen ABM_REMOVE.
 *    Naar WpfAppBar (MIT, https://github.com/mgaffigan/WpfAppBar), AppBarWindow.cs r. 144 tot 230 en 286 tot 306.
 * 2. Doorklikken: WS_EX_LAYERED en WS_EX_TRANSPARENT aan als de muis niet op het hol staat, uit als hij erop staat.
 *    Naar godot-native-click-through (MIT, https://github.com/KhangQuachUnique/godot-native-click-through),
 *    src/native_click_through.cpp r. 253 tot 321. Bij twijfel of fout gaat de muis door het spel heen.
 * 3. Geen taakbalkknop (WS_EX_TOOLWINDOW, WS_EX_NOACTIVATE) en verstoppen als een ander programma het scherm vult.
 *    Naar idle.exe (MIT, https://github.com/XYMYX/idle.exe), tools/sysinfo/sysinfo.cpp r. 150 tot 200.
 *
 * Waarom een los programma en geen GDExtension: als het spel hard wordt afgesloten, merkt dit programma dat (de
 * pijp naar het spel breekt, het venster bestaat niet meer) en geeft het de strook netjes terug. Het onzichtbare
 * venster van de app-balk is van dit programma zelf, dus ABM_REMOVE gaat altijd over een levend venster.
 *
 * Gebruik: hol-balk.exe <hwnd> <hoogte> [logbestand]
 * Regels op stdin (van het spel):
 *   h <hoogte>                   nieuwe hoogte van de strook
 *   v <x0> <x1> <top> ...         vlak dat de muis vangt, in venster-pixels: per stuk van x0 tot x1 vanaf top tot onder
 *   q                            stoppen
 * Stdin dicht of het venster weg: strook teruggeven en stoppen.
 */
#define WIN32_LEAN_AND_MEAN
#define _WIN32_WINNT 0x0A00
#include <windows.h>
#include <shellapi.h>
#include <shlobj.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define WM_BALK (WM_APP + 1)
#define MAX_STUK 4096

static HWND spel = NULL;      /* venster van het spel */
static HWND balk = NULL;      /* ons onzichtbare venster dat de app-balk is */
static DWORD spel_pid = 0;
static int hoogte = 120;
static int geregistreerd = 0;
static int doorzicht = -1;    /* -1 onbekend, 1 muis gaat door het spel heen, 0 het spel vangt de muis */
static int verstopt = 0;
static int vlak_n = 0;        /* 0 = nog geen vlak: alles gaat door (veilig) */
static int vlak[MAX_STUK][3];
static FILE *logf = NULL;
static RECT laatste = {0, 0, 0, 0};

static void logr(const char *fmt, ...) {
	if (!logf) return;
	SYSTEMTIME t;
	GetLocalTime(&t);
	fprintf(logf, "%02d:%02d:%02d ", t.wHour, t.wMinute, t.wSecond);
	va_list a;
	va_start(a, fmt);
	vfprintf(logf, fmt, a);
	va_end(a);
	fputc('\n', logf);
	fflush(logf);
}

static void dpi_bewust(void) {
	HMODULE u = GetModuleHandleW(L"user32.dll");
	typedef BOOL(WINAPI * ctx_t)(HANDLE);
	ctx_t f = u ? (ctx_t)(void *)GetProcAddress(u, "SetProcessDpiAwarenessContext") : NULL;
	if (!f || !f((HANDLE)-4 /* PER_MONITOR_AWARE_V2 */)) SetProcessDPIAware();
}

static void monitor_van_spel(RECT *uit) {
	HMONITOR m = MonitorFromWindow(spel, MONITOR_DEFAULTTOPRIMARY);
	MONITORINFO mi;
	mi.cbSize = sizeof(mi);
	GetMonitorInfoW(m, &mi);
	*uit = mi.rcMonitor;
}

/* AppBarWindow.cs r. 183 tot 230: rechthoek = scherm, QUERYPOS, onderkant vast, SETPOS, dan het venster plaatsen. */
static void plaats(void) {
	if (!geregistreerd) return;
	APPBARDATA ab;
	memset(&ab, 0, sizeof(ab));
	ab.cbSize = sizeof(ab);
	ab.hWnd = balk;
	ab.uEdge = ABE_BOTTOM;
	monitor_van_spel(&ab.rc);
	SHAppBarMessage(ABM_QUERYPOS, &ab);
	ab.rc.top = ab.rc.bottom - hoogte;
	SHAppBarMessage(ABM_SETPOS, &ab);
	RECT r = ab.rc;
	if (memcmp(&r, &laatste, sizeof(r)) != 0) {
		logr("BALK plek %ld,%ld tot %ld,%ld (hoogte %d)", r.left, r.top, r.right, r.bottom, hoogte);
		laatste = r;
	}
	SetWindowPos(balk, NULL, r.left, r.top, r.right - r.left, r.bottom - r.top, SWP_NOZORDER | SWP_NOACTIVATE);
	SetWindowPos(spel, HWND_TOPMOST, r.left, r.top, r.right - r.left, r.bottom - r.top, SWP_NOACTIVATE);
}

/* Elke seconde: staat het spel nog in de strook? (Godot of de gebruiker kan het verplaatst hebben.) Geen ABM_SETPOS hier,
 * want dat laat Windows elke keer de werkruimte opnieuw rekenen. */
static void bewaak(void) {
	if (!geregistreerd || verstopt) return;
	RECT r;
	if (GetWindowRect(spel, &r) && memcmp(&r, &laatste, sizeof(r)) != 0) {
		logr("BALK spel stond op %ld,%ld tot %ld,%ld, terug in de strook", r.left, r.top, r.right, r.bottom);
		SetWindowPos(spel, HWND_TOPMOST, laatste.left, laatste.top, laatste.right - laatste.left,
		             laatste.bottom - laatste.top, SWP_NOACTIVATE);
	}
}

static void registreer(void) {
	APPBARDATA ab;
	memset(&ab, 0, sizeof(ab));
	ab.cbSize = sizeof(ab);
	ab.hWnd = balk;
	ab.uCallbackMessage = WM_BALK;
	geregistreerd = SHAppBarMessage(ABM_NEW, &ab) ? 1 : 0;
	logr("BALK ABM_NEW %s", geregistreerd ? "ok" : "MISLUKT");
	plaats();
}

static void geef_terug(void) {
	if (!geregistreerd) return;
	APPBARDATA ab;
	memset(&ab, 0, sizeof(ab));
	ab.cbSize = sizeof(ab);
	ab.hWnd = balk;
	SHAppBarMessage(ABM_REMOVE, &ab);
	geregistreerd = 0;
	RECT w;
	SystemParametersInfoW(SPI_GETWORKAREA, 0, &w, 0);
	logr("BALK ABM_REMOVE, werkruimte nu %ld,%ld tot %ld,%ld", w.left, w.top, w.right, w.bottom);
}

/* idle.exe sysinfo.cpp: geen knop in de taakbalk; de taakbalk ziet de stijl pas na verbergen en weer tonen. */
static void geen_taakbalkknop(void) {
	LONG_PTR ex = GetWindowLongPtrW(spel, GWL_EXSTYLE);
	LONG_PTR nieuw = (ex | WS_EX_TOOLWINDOW | WS_EX_NOACTIVATE | WS_EX_LAYERED) & ~(LONG_PTR)WS_EX_APPWINDOW;
	if (nieuw == ex) return;
	ShowWindow(spel, SW_HIDE);
	SetWindowLongPtrW(spel, GWL_EXSTYLE, nieuw);
	ShowWindow(spel, SW_SHOWNOACTIVATE);
	logr("BALK stijl 0x%llx -> 0x%llx", (unsigned long long)ex, (unsigned long long)nieuw);
}

static void zet_doorzicht(int aan) {
	if (aan == doorzicht) return;
	doorzicht = aan;
	LONG_PTR ex = GetWindowLongPtrW(spel, GWL_EXSTYLE);
	ex |= WS_EX_LAYERED;
	if (aan) ex |= WS_EX_TRANSPARENT;
	else ex &= ~(LONG_PTR)WS_EX_TRANSPARENT;
	SetWindowLongPtrW(spel, GWL_EXSTYLE, ex);
}

static int muis_op_hol(void) {
	if (vlak_n == 0 || verstopt) return 0;
	POINT p;
	if (!GetCursorPos(&p) || !ScreenToClient(spel, &p)) return 0;
	RECT c;
	GetClientRect(spel, &c);
	if (p.x < 0 || p.y < 0 || p.x >= c.right || p.y >= c.bottom) return 0;
	for (int i = 0; i < vlak_n; i++)
		if (p.x >= vlak[i][0] && p.x < vlak[i][1] && p.y >= vlak[i][2]) return 1;
	return 0;
}

static int is_schil(HWND h) {
	wchar_t k[64];
	GetClassNameW(h, k, 64);
	return !wcscmp(k, L"Progman") || !wcscmp(k, L"WorkerW") || !wcscmp(k, L"Shell_TrayWnd") ||
	       !wcscmp(k, L"Shell_SecondaryTrayWnd");
}

/* idle.exe sysinfo.cpp r. 155 tot 185: volledig scherm (spel, film, presentatie) op ons scherm. */
static int volledig_scherm(void) {
	QUERY_USER_NOTIFICATION_STATE st;
	if (SUCCEEDED(SHQueryUserNotificationState(&st)) &&
	    (st == QUNS_RUNNING_D3D_FULL_SCREEN || st == QUNS_PRESENTATION_MODE))
		return 1;
	HWND fg = GetForegroundWindow();
	if (!fg || fg == spel || fg == balk || is_schil(fg)) return 0;
	DWORD pid = 0;
	GetWindowThreadProcessId(fg, &pid);
	if (pid == spel_pid || pid == GetCurrentProcessId()) return 0;
	HMONITOR m = MonitorFromWindow(fg, MONITOR_DEFAULTTONULL);
	if (!m || m != MonitorFromWindow(spel, MONITOR_DEFAULTTONEAREST)) return 0;
	MONITORINFO mi;
	mi.cbSize = sizeof(mi);
	RECT r;
	if (!GetMonitorInfoW(m, &mi) || !GetWindowRect(fg, &r)) return 0;
	return r.left <= mi.rcMonitor.left && r.top <= mi.rcMonitor.top && r.right >= mi.rcMonitor.right &&
	       r.bottom >= mi.rcMonitor.bottom;
}

static void zet_verstopt(int ja, const char *waarom) {
	if (ja == verstopt) return;
	verstopt = ja;
	ShowWindow(spel, ja ? SW_HIDE : SW_SHOWNOACTIVATE);
	if (!ja) plaats();
	logr("BALK %s (%s)", ja ? "verstopt" : "weer zichtbaar", waarom);
}

static LRESULT CALLBACK balk_proc(HWND h, UINT m, WPARAM w, LPARAM l) {
	if (m == WM_BALK) {
		if (w == ABN_POSCHANGED) plaats();
		else if (w == ABN_FULLSCREENAPP) logr("BALK melding volledig scherm %d", (int)l);
		return 0;
	}
	if (m == WM_DISPLAYCHANGE || m == WM_DPICHANGED) {
		plaats();
		return 0;
	}
	return DefWindowProcW(h, m, w, l);
}

/* Een regel van het spel verwerken. Geeft 0 terug bij "q". */
static int regel(char *s) {
	if (s[0] == 'q') return 0;
	if (s[0] == 'h') {
		int n = atoi(s + 1);
		if (n >= 48 && n <= 400 && n != hoogte) {
			hoogte = n;
			plaats();
		}
	} else if (s[0] == 'v') {
		int n = 0;
		char *p = s + 1;
		while (n < MAX_STUK) {
			char *e;
			long a = strtol(p, &e, 10);
			if (e == p) break;
			p = e;
			long b = strtol(p, &e, 10);
			if (e == p) break;
			p = e;
			long c = strtol(p, &e, 10);
			if (e == p) break;
			p = e;
			vlak[n][0] = (int)a;
			vlak[n][1] = (int)b;
			vlak[n][2] = (int)c;
			n++;
		}
		if (vlak_n == 0 && n > 0) logr("BALK eerste vlak, %d stukken", n);
		vlak_n = n;
	}
	return 1;
}

/* Lees zonder te wachten wat er op stdin staat. Geeft 0 als de pijp dicht is (het spel is weg). */
static char buf[65536];
static int buf_n = 0;
static int lees_stdin(HANDLE in) {
	DWORD er = 0;
	if (!PeekNamedPipe(in, NULL, 0, NULL, &er, NULL)) return 0;
	while (er > 0) {
		DWORD ruimte = (DWORD)(sizeof(buf) - 1 - buf_n), n = 0;
		if (ruimte == 0) buf_n = 0, ruimte = sizeof(buf) - 1;   /* te lange regel: weggooien */
		if (!ReadFile(in, buf + buf_n, er < ruimte ? er : ruimte, &n, NULL) || n == 0) return 0;
		buf_n += (int)n;
		er -= n;
		buf[buf_n] = 0;
		char *start = buf, *nl;
		while ((nl = strchr(start, '\n')) != NULL) {
			*nl = 0;
			if (!regel(start)) return 0;
			start = nl + 1;
		}
		buf_n = (int)(buf + buf_n - start);
		memmove(buf, start, buf_n);
	}
	return 1;
}

int WINAPI WinMain(HINSTANCE inst, HINSTANCE vorige, LPSTR cmd, int toon) {
	(void)vorige; (void)cmd; (void)toon;
	int argc = __argc;
	char **argv = __argv;
	if (argc < 3) return 2;
	spel = (HWND)(intptr_t)_strtoi64(argv[1], NULL, 10);
	hoogte = atoi(argv[2]);
	if (argc >= 4) logf = fopen(argv[3], "a");
	dpi_bewust();
	if (!IsWindow(spel)) {
		logr("BALK geen venster %s", argv[1]);
		return 3;
	}
	GetWindowThreadProcessId(spel, &spel_pid);

	WNDCLASSW wc;
	memset(&wc, 0, sizeof(wc));
	wc.lpfnWndProc = balk_proc;
	wc.hInstance = inst;
	wc.lpszClassName = L"HetHolBalk";
	RegisterClassW(&wc);
	/* onzichtbaar en zonder knop: alleen om de app-balk bij Windows op naam te hebben */
	balk = CreateWindowExW(WS_EX_TOOLWINDOW | WS_EX_NOACTIVATE, wc.lpszClassName, L"Het Hol balk", WS_POPUP, 0, 0, 0, 0,
	                       NULL, NULL, inst, NULL);

	zet_doorzicht(1);   /* veilig beginnen: de muis gaat door het spel heen tot het vlak er is */
	geen_taakbalkknop();
	registreer();

	HANDLE in = GetStdHandle(STD_INPUT_HANDLE);
	int tik = 0;
	for (;;) {
		MSG msg;
		while (PeekMessageW(&msg, NULL, 0, 0, PM_REMOVE)) {
			TranslateMessage(&msg);
			DispatchMessageW(&msg);
		}
		if (!lees_stdin(in)) {
			logr("BALK spel stopt (stdin dicht of q)");
			break;
		}
		if (!IsWindow(spel)) {
			logr("BALK venster van het spel is weg");
			break;
		}
		zet_doorzicht(!muis_op_hol());
		if (++tik % 20 == 0) {   /* elke seconde */
			zet_verstopt(volledig_scherm(), "volledig scherm");
			bewaak();
		}
		MsgWaitForMultipleObjects(0, NULL, FALSE, 50, QS_ALLINPUT);
	}
	zet_doorzicht(1);
	geef_terug();
	if (balk) DestroyWindow(balk);
	if (logf) fclose(logf);
	return 0;
}
