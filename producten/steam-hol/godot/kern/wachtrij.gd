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
# punt 3: hij kwam 1,3 s te laat omdat de lied-regel er nog stond). De weggedrukte lage regel was al getoond en komt niet terug.
const DRINGEND := ["plat"]

static func toon(s) -> void:
	# binnenkom-regels die te lang wachten vervallen
	for i in range(s.wachtrij.size() - 1, -1, -1):
		if bool(s.wachtrij[i].binnen) and not NOOIT_WEG.has(String(s.wachtrij[i].get("soort", ""))) and s.t - float(s.wachtrij[i].sinds) > BINNEN_WACHT:
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
		for i in s.wachtrij.size():
			if DRINGEND.has(String(s.wachtrij[i].get("soort", ""))):
				k = i
				break
	var volgende: Dictionary = s.wachtrij[k]
	var staat: float = s.t - s.regel_sinds
	var mag := staat >= REGEL_MIN
	var drukt: bool = not bool(volgende.binnen) or DRINGEND.has(String(volgende.get("soort", "")))
	if s.regel_binnen and drukt and staat >= BINNEN_WIJK:
		mag = true
	if not mag:
		return
	s.wachtrij.remove_at(k)
	s.regel_sinds = s.t
	s.regel_binnen = bool(volgende.binnen)
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
