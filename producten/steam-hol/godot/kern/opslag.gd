extends RefCounted
# Deel van kern/strook.gd (Olaf), losgehaald bij het opruimen van 10 nov (strook.gd was 650 regels).
# Statische functies; `s` is de strook. Gedrag gelijk aan voor het splitsen (film.log gelijk).
const VOORTGANG := preload("res://systemen/voortgang.gd")
const AFLOOP := preload("res://kern/afloop.gd")   # faam_erbij (hol-niveau)
const HOL_NIVEAU := preload("res://systemen/hol_niveau.gd")   # weg_regel en optocht (Sanne 16 nov 14:50)
const OPSLAG_VERSIE := 3   # 3: hol groeit naar links, schat rechts (oudere saves: vers begin, er zijn nog geen spelers)
const OPSLAG := "user://hol.json"
# voortgang.gd belooft dat de bewaarde tijd nooit achteruit gaat (nieuwe_laatst). Stond de klok terug, dan blijft de
# hoogste tijd bewaard; anders telt het gat nog een keer als de klok weer goed staat (controleur 13 nov, kan-punt).
static var tijd_vloer := 0

static func bewaar(s) -> void:
	var data := {"versie": OPSLAG_VERSIE, "tijd": maxi(int(Time.get_unix_time_from_system()), tijd_vloer), "gang": s.hol.gang, "boven": s.hol.boven,
		"eerste_held_gedaan": s.eerste_held_gedaan, "vallen": s.hol.vallen, "ingang_kol": s.hol.ingang_kol, "gevallen_namen": s.gevallen_namen,
		"schat_kol": s.hol.schat_kol, "goud": s.hol.goud, "terugkomers": s.terugkomers, "kroniek": s._kroniek_bewaar(),
		"begin_gedaan": s.begin_gedaan, "begin_vlucht": s.begin_vlucht, "helden_nr": s.helden_nr, "lied_helden": s.lied_helden,
		"pensioen_namen": s.pensioen_namen, "speeltijd_s": s.speeltijd_s, "faam": s.faam, "rij": s.rij, "rij_t": s.rij_t, "gegraven": s.zelf_gegraven,
		"uitleg": int(s.uitleg.stap) if s.uitleg != null else 4,
		"slijm": s.slijm.naar_dict() if s.slijm.has_method("naar_dict") else {},
		"upgrades": s.hol.upgrades.naar_dict() if s.hol.upgrades != null else {},
		"boek": s.boek.naar_dict() if s.boek != null else {}}
	var f := FileAccess.open(OPSLAG, FileAccess.WRITE)
	if f:
		f.store_string(JSON.stringify(data))
		f.close()

# Pure rekensom (toets in systemen/toetsen/toets_systemen.gd): schuif gang, kamers en vallen zo dat de schat op
# de laatste kolom voor het tekstvak staat (min(max_kol, kolommen - 1)). Wat links van kolom 1 valt is weg; de ingang
# blijft minstens op kolom 1 en de gang loopt van de ingang tot de schat. Een val komt alleen tussen ingang en schat.
static func schuif_naar_vak(g: Array, b: Array, v: Dictionary, schat: int, ingang: int, max_kol: int, kolommen: int) -> Dictionary:
	var doel := clampi(mini(max_kol, kolommen - 1), 3, maxi(3, kolommen - 1))
	var d := doel - schat
	var ng: Array = []
	var nb: Array = []
	ng.resize(kolommen)
	nb.resize(kolommen)
	ng.fill(false)
	nb.fill(false)
	for i in g.size():
		var j := i + d
		if j >= 1 and j <= doel:
			ng[j] = bool(g[i])
	for i in b.size():
		var j := i + d
		if j >= 1 and j <= doel:   # geen zwevende kamer op kolom 0 zonder gang eronder (controleur kan 1)
			nb[j] = bool(b[i])
	var ni := clampi(ingang + d, 1, doel - 1)
	for k in range(ni, doel + 1):
		ng[k] = true
	var nv := {}
	for k in v:
		var j := int(k) + d
		if j > ni and j < doel:
			nv[j] = String(v[k])
	# alle vallen geschoven uit beeld: één terug zoals leg_aan (controleur kan 2), anders geen koopmuntje voor de put
	if nv.is_empty() and not v.is_empty():
		nv[maxi(ni + 1, mini(ni + 5, doel - 3))] = "stekelput"
	return {"gang": ng, "boven": nb, "vallen": nv, "schat_kol": doel, "ingang_kol": ni, "schuif": d}

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
	# Olaf 14 nov (kan Daan 22:40): de save kan van een breder scherm of een lagere strook komen (week-save op 1920,
	# opname op 1280; of de hoogte via rechtsklik naar 160). Dan schuift het hele hol zo dat de schat weer rechts
	# tegen het tekstvak staat; anders lagen putten en kamers onder het paneel.
	var a := schuif_naar_vak(data.get("gang", []), data.get("boven", []), data.get("vallen", {}),
		int(data.get("schat_kol", s.hol.schat_kol)), int(data.get("ingang_kol", s.hol.ingang_kol)), s.hol.max_kol, s.hol.kolommen)
	for i in s.hol.kolommen:
		s.hol.gang[i] = a.gang[i]
		s.hol.boven[i] = a.boven[i]
	s.hol.vallen = a.vallen
	s.hol.schat_kol = a.schat_kol
	s.hol.ingang_kol = a.ingang_kol
	if int(a.schuif) != 0:
		s.log_regel("HOL save geschoven %d kolommen: schat %d, ingang %d, vallen %s" % [int(a.schuif), int(a.schat_kol), int(a.ingang_kol), str(a.vallen.keys())])
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
	s.faam = maxi(0, int(data.get("faam", 0)))
	s.zelf_gegraven = maxi(0, int(data.get("gegraven", 0)))   # graafbonus (Sanne 16 nov 21:00); oude saves 0
	s.uitleg_stap = clampi(int(data.get("uitleg", 4)), 0, 4)   # eerste minuut (kern/eerste_minuut.gd); oude saves: klaar
	s.rij = maxi(0, int(data.get("rij", 0)))   # rij bij de ingang (Sanne 16 nov 16:00); oude saves 0
	s.rij_t = float(data.get("rij_t", 0.0))   # oude saves vanaf 0 (hol-niveau 1); versie blijft gelijk
	s.speeltijd_s = float(data.get("speeltijd_s", 0))   # demo-einde; oude saves vanaf 0, versie blijft 3
	s.pensioen_namen = []
	var pn = data.get("pensioen_namen", [])
	if pn is Array:
		for n in pn:
			s.pensioen_namen.append(String(n))
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
	if s.boek != null and data.get("boek") is Dictionary:
		s.boek.van_dict(data.get("boek"))
	if s.hol.upgrades != null and data.get("upgrades") is Dictionary:
		s.hol.upgrades.van_dict(data.get("upgrades"))
		if s.slijm != null and s.slijm.has_method("upgrade_veranderd"):
			s.slijm.upgrade_veranderd()   # het lijf van zijn gekochte stap meteen bij openen (Bram 03:25)
	# gekochte stappen tellen ook terwijl je weg was (Bram, voortgang.gd); gangen en faam zoals voorheen (6 en 0)
	var weg := VOORTGANG.reken(int(data.get("tijd", 0)), int(Time.get_unix_time_from_system()), s.hol.vallen.size(), 1, 7, 6, 0, s.hol.upgrades, s.zelf_gegraven)
	tijd_vloer = int(weg.get("nieuwe_laatst", 0))
	# stond de klok per ongeluk ver vooruit (meer dan 3 dagen), dan niet tot die datum zonder weg-winst blijven (controleur kan-punt)
	if tijd_vloer > int(Time.get_unix_time_from_system()) + 3 * 86400:
		tijd_vloer = 0
	# demolijst 4 (bewijs op Windows, steam-hol.yml stap "Weg geweest"): goud voor en wat erbij kwam
	s.log_regel("HOL weg geweest %d s (klok terug: %s): goud voor %d, helden %d, erbij %d, hoeden %d" % [int(weg.weg_s), str(weg.teruggezet),
		s.hol.goud, int(weg.helden), int(weg.goud) if int(weg.helden) > 0 else 0, int(weg.opgegeten)])
	var faam_voor: int = s.faam
	if int(weg.helden) > 0:
		s.hol.goud += int(weg.goud)
		# faam ook als je weg was, op weg-snelheid, maar hooguit 2 hol-niveaus per keer weg (Sanne 16 nov 22:00)
		var wf: int = HOL_NIVEAU.weg_faam(s.faam, int(weg.get("faam", 0)))
		if wf < int(weg.get("faam", 0)):
			s.log_regel("HOL weg faam afgekapt %d van %d (hooguit %d niveaus)" % [wf, int(weg.get("faam", 0)), HOL_NIVEAU.WEG_NIVEAUS])
		AFLOOP.faam_erbij(s, wf)
		# hoeden ook terwijl je weg was, op hetzelfde kwart tempo (Sanne 16 nov 14:05); geef_hoeden zet hoeden_gegeven,
		# zodat het verhaal ze pas noemt als ze echt op Gloop staan
		# Hoeden van de nacht (Sanne 17 nov, features.md): niet meteen op de toren, maar in een rij die na de wip
		# een voor een op de top valt, zodat je de toren ziet groeien. Save blijft gelijk (naar_dict telt de rij mee).
		if s.slijm != null:
			var hn: Array[int] = VOORTGANG.geef_hoeden([s.slijm], weg, 7, true)
			if s.slijm.has_method("start_nacht") and hn[0] > 0:
				s.slijm.start_nacht()
				s.log_regel("HOL hoeden van de nacht %d (vallen vanaf %.1f s, toren nu %d)" % [hn[0], s.slijm.NACHT_WACHT_S, s.slijm.hoeden.size()])
				if s.slijm.has_method("berg_zichtbaar"):   # Iris' keurregel (Sanne 17 nov 07:00): groeit de berg zichtbaar?
					s.log_regel("HOL berg zichtbaar %d -> %d" % [s.slijm.berg_zichtbaar(s.slijm.hoeden.size()), s.slijm.berg_zichtbaar(s.slijm.hoeden.size() + s.slijm.nacht_hoeden.size())])
		var helden_d := {}
		for h in s.terugkomers:
			helden_d[String(h.naam)] = {"gevlucht": int(h.bezoeken), "wrok": String(h.get("wrok", ""))}
		var namen := [s.slijm.naam()]
		if not s.hol.vallen.is_empty():
			namen.append("the Spike Pit")
		# via de wachtrij, zodat je ze bij openen een voor een ziet (controleur punt 4)
		var vh: Array[String] = VOORTGANG.verhaal(weg, helden_d, namen, 7)
		for r in vh:
			s._kroniek(String(r))
		# de telling ("115 came, 82 fell ...") blijft bovenaan het kaartje tot de eerste nieuwe held binnen is (moet Daan 16 nov 23:30 a)
		if not vh.is_empty():
			s.tekst.vast = String(vh[vh.size() - 1])
			s.tekst.weg_regels = vh.duplicate()   # Iris keuring 16 punt 2: oude regels niet meer op het kaartje
			s.tekst.weg_tel = s.tekst.vast
		for hn in helden_d:
			s.namen_recent.append(String(hn))
		var tr := VOORTGANG.tempo_regel(weg)
		if tr != "":
			s._kroniek(tr)
		# optocht van de niveaus van weg (Sanne 16 nov 14:50): één kroniekregel na de kwart-regel, en het plan
		# (wip, poef per ding, nieuwe heldensoorten als eerstvolgende bezoekers). Tekenen volgt met het bordje (Mila).
		# rij bij de ingang (Sanne 16 nov 16:00): hooguit 4 niveaus meteen, de rest wacht
		var wg: Dictionary = HOL_NIVEAU.weg(faam_voor, s.faam, s.rij)
		s.rij = int(wg.rij)
		if s.rij > 0:
			s.log_regel("HOL rij bij de ingang %d (meteen %s)" % [s.rij, str(wg.meteen)])
		for wr in wg.regels:
			if HOL_NIVEAU.REGELS_AAN:
				s._kroniek(String(wr))
			else:
				s.log_regel("HOL weg-regel uit tot het bordje: %s" % wr)   # moet Daan 16 nov 15:33
		s.optocht = wg.optocht
		if bool(s.optocht.wip):
			var stukken: Array[String] = []
			for po in s.optocht.poef:
				stukken.append("%.1f poef %d%s" % [float(po.t), int(po.niveau), " munt" if bool(po.munt) else ""])
			s.log_regel("HOL optocht wip, %s; helden %s; duur %.1f s" % [", ".join(stukken) if not stukken.is_empty() else "geen poef",
				str(s.optocht.helden), float(s.optocht.duur)])
	# met pensioen (Bram 04:35, Sanne kroniek-regels.md): na minstens 30 min weg hooguit één held die nooit terugkwam
	var p: Dictionary = VOORTGANG.pensioen(s.pensioen_namen, weg, s.regels)
	if not p.is_empty():
		s._kroniek(String(p.regel))
		s.namen_recent.append(String(p.naam))
		s.pensioen_namen.erase(p.naam)
	s.hol.queue_redraw()
	s.tekst.zet(s.kroniek, s.hol.goud)
	s.log_regel("HOL opslag geladen: %d terugkomers, %d goud, faam %d" % [s.terugkomers.size(), s.hol.goud, s.faam])
