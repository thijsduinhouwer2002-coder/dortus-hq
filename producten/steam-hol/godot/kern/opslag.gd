extends RefCounted
# Deel van kern/strook.gd (Olaf), losgehaald bij het opruimen van 10 nov (strook.gd was 650 regels).
# Statische functies; `s` is de strook. Gedrag gelijk aan voor het splitsen (film.log gelijk).
const VOORTGANG := preload("res://systemen/voortgang.gd")
const OPSLAG_VERSIE := 3   # 3: hol groeit naar links, schat rechts (oudere saves: vers begin, er zijn nog geen spelers)
const OPSLAG := "user://hol.json"

static func bewaar(s) -> void:
	var data := {"versie": OPSLAG_VERSIE, "tijd": Time.get_unix_time_from_system(), "gang": s.hol.gang, "boven": s.hol.boven,
		"eerste_held_gedaan": s.eerste_held_gedaan, "vallen": s.hol.vallen, "ingang_kol": s.hol.ingang_kol, "gevallen_namen": s.gevallen_namen,
		"schat_kol": s.hol.schat_kol, "goud": s.hol.goud, "terugkomers": s.terugkomers, "kroniek": s._kroniek_bewaar(),
		"begin_gedaan": s.begin_gedaan, "begin_vlucht": s.begin_vlucht, "helden_nr": s.helden_nr, "lied_helden": s.lied_helden,
		"slijm": s.slijm.naar_dict() if s.slijm.has_method("naar_dict") else {},
		"upgrades": s.hol.upgrades.naar_dict() if s.hol.upgrades != null else {}}
	var f := FileAccess.open(OPSLAG, FileAccess.WRITE)
	if f:
		f.store_string(JSON.stringify(data))
		f.close()

static func laad(s, begin) -> void:
	if not FileAccess.file_exists(OPSLAG):
		return
	var data = JSON.parse_string(FileAccess.get_file_as_string(OPSLAG))
	if typeof(data) != TYPE_DICTIONARY:
		s.log_regel("HOL opslag onleesbaar, vers begin")
		return
	if int(data.get("versie", 0)) < OPSLAG_VERSIE:
		s.log_regel("HOL opslag van een oudere versie, vers begin")
		return
	var g: Array = data.get("gang", [])
	for i in mini(g.size(), s.hol.kolommen):
		s.hol.gang[i] = bool(g[i])
	s.hol.vallen.clear()
	for k in data.get("vallen", {}):
		s.hol.vallen[int(k)] = String(data.vallen[k])
	var b: Array = data.get("boven", [])
	for i in mini(b.size(), s.hol.kolommen):
		s.hol.boven[i] = bool(b[i])
	s.hol.schat_kol = clampi(int(data.get("schat_kol", s.hol.schat_kol)), 0, mini(s.hol.max_kol, s.hol.kolommen - 1))
	s.hol.ingang_kol = clampi(int(data.get("ingang_kol", s.hol.ingang_kol)), 1, s.hol.schat_kol - 1)
	s.hol.gang[0] = false   # oude save met de ingang op kolom 0: die kolom hoort niet meer bij de gang (controleur 22:30)
	var gn = data.get("gevallen_namen", {})
	for n in gn:
		s.gevallen_namen[String(n)] = int(gn[n])
	s.slijm.position = s.hol.cel_naar_pos(Vector2i(s.hol.schat_kol - 2, 0))
	s.hol._schatkamer()
	s.eerste_held_gedaan = bool(data.get("eerste_held_gedaan", true))
	# een save van voor de eerste tien minuten: dat begin is voorbij
	s.begin_gedaan = data.get("begin_gedaan", begin.duplicate() if s.eerste_held_gedaan else [])
	s.begin_vlucht = String(data.get("begin_vlucht", ""))
	s.helden_nr = int(data.get("helden_nr", 0))
	s.lied_helden = int(data.get("lied_helden", 0))
	if s.slijm.has_method("van_dict"):
		s.slijm.van_dict(data.get("slijm", {}))
	s.hol.goud = int(data.get("goud", 0))
	s.terugkomers = data.get("terugkomers", [])
	# de held die moest vluchten liep nog in het hol toen het spel dichtging: hij komt nooit meer terug, dus "terug" telt
	# als gedaan, anders wacht het begin voor altijd (controleur 9 nov 22:30)
	if s.begin_gedaan.has("vluchten") and not s.begin_gedaan.has("terug") and s._terugkomer_i(s.begin_vlucht) < 0:
		s.begin_gedaan.append("terug")
	for r in data.get("kroniek", []):
		s.kroniek.append(String(r))
	# terwijl je weg was (Bram, voortgang.gd): alleen winst, plafond 12 uur, 2 tot 3 regels met namen
	if s.hol.upgrades != null and data.get("upgrades") is Dictionary:
		s.hol.upgrades.van_dict(data.get("upgrades"))
		if s.slijm != null and s.slijm.has_method("upgrade_veranderd"):
			s.slijm.upgrade_veranderd()   # het lijf van zijn gekochte stap meteen bij openen (Bram 03:25)
	# gekochte stappen tellen ook terwijl je weg was (Bram, voortgang.gd); gangen en faam zoals voorheen (6 en 0)
	var weg := VOORTGANG.reken(int(data.get("tijd", 0)), int(Time.get_unix_time_from_system()), s.hol.vallen.size(), 1, 7, 6, 0, s.hol.upgrades)
	if int(weg.helden) > 0:
		s.hol.goud += int(weg.goud)
		var helden_d := {}
		for h in s.terugkomers:
			helden_d[String(h.naam)] = {"gevlucht": int(h.bezoeken), "wrok": String(h.get("wrok", ""))}
		var namen := [s.slijm.naam()]
		if not s.hol.vallen.is_empty():
			namen.append("the Spike Pit")
		# via de wachtrij, zodat je ze bij openen een voor een ziet (controleur punt 4)
		for r in VOORTGANG.verhaal(weg, helden_d, namen, 7):
			s._kroniek(String(r))
	s.hol.queue_redraw()
	s.tekst.zet(s.kroniek, s.hol.goud)
	s.log_regel("HOL opslag geladen: %d terugkomers, %d goud" % [s.terugkomers.size(), s.hol.goud])
