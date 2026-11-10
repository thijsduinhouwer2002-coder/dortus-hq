extends RefCounted
# Deel van kern/strook.gd (Olaf), losgehaald bij het opruimen van 10 nov (strook.gd was 650 regels).
# Statische functies; `s` is de strook. Gedrag gelijk aan voor het splitsen (film.log gelijk).

# De kroniek loopt gelijk met het beeld (Sanne toets 5, punt 1). Elke regel gaat eerst in een wachtrij; _toon() kiest:
# - een regel over wat er gebeurt (val, vlucht, schat, hoed) gaat altijd voor en verdringt een binnenkom-regel na 1 s;
# - een binnenkom-regel komt alleen als er niets anders wacht en vervalt na 3 s wachten (dan komt hij nooit in de kroniek);
#   "Gloop is flat" en "up again" zijn net zo laag: een toestand, geen gebeurtenis (film run 42720059959: anders liep de
#   kroniek in een drukke minuut 6 s achter door plat en op);
# - een getoonde regel blijft minstens 2,5 s staan (een binnenkom-regel 1 s als er een gebeurtenis wacht); wacht er niets,
#   dan blijft hij staan tot er iets nieuws is (een leeg vak zegt niets).
# Alleen getoonde regels komen in `kroniek` (hover en opslag), zodat je nooit een regel terugleest die niemand zag.
const REGEL_MIN := 2.5
const BINNEN_WACHT := 3.0
const BINNEN_WIJK := 1.0
# Lage regels die toch nooit vervallen (Sanne toets 9, besluit 2c): "Gloop is flat" zolang hij plat ligt, want wat je
# ziet gaat altijd voor. Ze wachten wel achter gebeurtenissen; staat hij weer op voor de regel kwam, dan valt "plat"
# weg in strook.gd (samen met "op"). De lied-regel is een sfeerregel: laag (besluit 2a), maar hij vervalt ook niet
# (afwijking, besluit Olaf 10 nov): in de film van fe3411e verviel hij en kwam daarna "Lotte hums the song" zonder dat
# je ooit van een lied hoorde. Laag betekent dat hij nooit een gebeurtenis ophoudt, dus de kroniek loopt niet achter.
const NOOIT_WEG := ["plat", "lied"]
# "Gloop is flat" drukt net als een gebeurtenis een getoonde lage regel (lied, binnenkomst) na 1 s weg (Sanne toets 10,
# punt 3: hij kwam 1,3 s te laat omdat de lied-regel er nog stond).
const DRINGEND := ["plat"]
# Weggedrukt voor hij 2,5 s stond (Sanne toets 11, punt 1: "Bram's song got popular. Uh oh." stond 1 s, plat drukte hem
# weg): de lied-regel (TERUG) komt direct na de regel die hem wegdrukte nog één keer terug, zonder die op te houden, en gaat
# daarna pas weg. Alleen lage sfeerregels (besluit Olaf 10 nov): een binnenkom-regel mag na 1 s wijken voor een gebeurtenis
# (toets 5) en terugkomen zou de kroniek weer laten achterlopen. Gebeurtenissen gaan nog steeds voor de terugkomer.
# Hij komt maar één keer terug (`terug`), en in de kroniek staat hij daarna één keer, op zijn nieuwe plek.
# Alleen "lied", niet "plat" (controleur 10 nov 06:30): een plat die terugkomt terwijl Gloop al op is zegt iets anders
# dan je ziet, en strook.gd haalt een wachtende plat weg als hij opstaat (dan zou "op" ontbreken).
const TERUG := ["lied"]

static func toon(s) -> void:
	# binnenkom-regels die te lang wachten vervallen
	for i in range(s.wachtrij.size() - 1, -1, -1):
		if bool(s.wachtrij[i].binnen) and not bool(s.wachtrij[i].get("terug", false)) and not NOOIT_WEG.has(String(s.wachtrij[i].get("soort", ""))) and s.t - float(s.wachtrij[i].sinds) > BINNEN_WACHT:
			s.log_regel("HOL kroniek vervallen %.1f: %s" % [s.t, s.wachtrij[i].r])
			s.wachtrij.remove_at(i)
	if s.wachtrij.is_empty():
		return
	# eerst een gebeurtenis, dan "plat" (wat je ziet), dan de oudste lage regel
	var k := -1
	for i in s.wachtrij.size():
		if not bool(s.wachtrij[i].binnen):
			k = i
			break
	if k < 0:
		k = 0
		var dringend := -1
		var terug := -1
		for i in s.wachtrij.size():
			if dringend < 0 and DRINGEND.has(String(s.wachtrij[i].get("soort", ""))):
				dringend = i
			if terug < 0 and bool(s.wachtrij[i].get("terug", false)):
				terug = i
		if dringend >= 0:
			k = dringend
		elif terug >= 0:
			k = terug
	var volgende: Dictionary = s.wachtrij[k]
	var staat: float = s.t - s.regel_sinds
	var mag := staat >= REGEL_MIN
	var drukt: bool = not bool(volgende.binnen) or DRINGEND.has(String(volgende.get("soort", "")))
	if s.regel_binnen and drukt and staat >= BINNEN_WIJK:
		mag = true
	if not mag:
		return
	s.wachtrij.remove_at(k)
	# de getoonde regel stond te kort: één keer terug, vooraan bij de lage regels
	var oud: Dictionary = s.regel_nu
	if not oud.is_empty() and staat < REGEL_MIN and TERUG.has(String(oud.get("soort", ""))) and not bool(oud.get("terug", false)):
		var weer := oud.duplicate()
		weer["terug"] = true
		weer["sinds"] = s.t
		s.wachtrij.insert(0, weer)
		s.log_regel("HOL kroniek weggedrukt na %.1f s, komt terug: %s" % [staat, oud.r])
	s.regel_sinds = s.t
	s.regel_binnen = bool(volgende.binnen)
	s.regel_nu = volgende
	if bool(volgende.get("terug", false)):
		var oude_plek: int = s.kroniek.rfind(String(volgende.r))
		if oude_plek >= 0:
			s.kroniek.remove_at(oude_plek)
	s.kroniek.append(String(volgende.r))
	while s.kroniek.size() > 40:
		s.kroniek.remove_at(0)
	s.tekst.zet(s.kroniek, s.hol.goud)
	s.log_regel("HOL kroniek %.1f (wacht %.1f): %s" % [s.t, s.t - float(volgende.sinds), volgende.r])

# wat bewaard wordt: de getoonde regels plus wachtende gebeurtenissen (geen lage), zodat bij afsluiten niets wegvalt
# (controleur 23:30: de regels "terwijl je weg was" stonden bij het eerste bewaren nog in de wachtrij)
static func kroniek_bewaar(s) -> Array[String]:
	var k: Array[String] = []
	k.assign(s.kroniek)
	for w in s.wachtrij:
		if not bool(w.binnen):
			k.append(String(w.r))
	while k.size() > 40:
		k.remove_at(0)
	return k
