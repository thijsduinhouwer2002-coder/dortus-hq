extends Node2D
# Held (Bram). Vervangt de stand-in van Olaf; de kern pakt dit bestand vanzelf als het bestaat.
# Afspraak (platformen/steam/taken.md): start(hol, info) en signaal klaar(held, uitkomst, info).
# Gebruikt van het hol alleen: cel_naar_pos, pos_naar_cel, ingang, schat, val_op (en bewoners onder Hol/Wezens).
#
# Wat hij doet (features.md van Sanne, balans.md):
# - komt binnen bij de ingang en loopt naar zijn doel. Een held met een wrok loopt EERST naar zijn vijand
#   (de val of de bewoner bij naam), niet naar de schat.
# - bij elke verdediging op zijn pad (een val of een bewoner) gooit hij één keer: valt hij, dan laat hij goud achter.
#   Kans: slijm 45%, stekelput 35% (sim/, zie sim/UITKOMST.md). Tegen zijn eigen vijand is hij roekeloos: +10 procentpunt.
# - valt hij niet, dan is hij geraakt: hij krijgt een wrok tegen wat hem raakte. Een bewoner die verliest gaat niet dood,
#   die is even plat (plat()).
# - karakter: "hebzuchtig" loopt door tot de schat (vlucht pas na twee klappen); "schijterig" draait na een klap de helft van de keren om.
# - haalt hij de schat, dan pakt hij NIETS (geen straf): hij raakt hem aan, krijgt de bijnaam Hoard-Toucher en rent weg.
#   Een Hoard-Toucher komt brutaler terug: iets vaker vluchten, nooit iets van jou kwijt.
# - info["snelheid"]: factor op al zijn bewegingen (standaard 1.0); de demo zet hem hoger zodat de Hoard-Toucher
#   rond 35 tot 40 s bij de schat is (Olaf 22:35).
# - info["moet_vallen"] = true: hij valt bij de eerste verdediging (de eerste held van een nieuw spel, balans.md).
# - info["moet_vluchten"]: overleeft de eerste verdediging en rent dan weg (krijgt zijn wrok).
# - info["moet_doorlopen"]: overleeft alles, rent nergens voor weg en raakt de schat aan (Hoard-Toucher).
# - info["moet_opgegeten"]: de eerste bewoner op zijn pad eet hem (vallen overleeft hij); zijn hoed gaat op de toren.
# - info["moet_afgerekend"]: een terugkomer met een wrok overleeft alles tot zijn vijand en valt precies daar
#   (Sanne toets 6 punt 1: in de demo-minuut moet de grap af zijn, "Bram came back. The Spike Pit won.").
#   Staat zijn vijand er niet (meer), dan loopt hij door naar de schat zoals altijd.
# - valt hij door een bewoner, dan gaat zijn hoed naar diens hoedentoren: info "hoed_naar" ("bewoner", of "wand"
#   voor een aartsvijand zodra WAND_ER waar is) en "hoeden_bewoner" (hoeveel hoeden die bewoner nu heeft, voor kroniek.hoed()).
#
# - info["soort_held"]: "ridder", "dief", "magier" of "bard" (systemen/heldensoort.gd, versie 1); leeg = zoals hierboven.
#   info["trek"] mag ook "slaapkop", "wraakzuchtig" of "opschepper" zijn (heldensoort.kies_trek); slaapkop zet info "dutje".
#   Een bard die vlucht (ook als Hoard-Toucher) zet info["lied"] = 2; strook.gd moet dan 2 helden extra laten komen
#   (nog aan te sluiten door Olaf, taken.md 10 nov). Zonder soort_held verandert er niets.
#
# Terug in info (voor strook.gd en kroniek.gd): "wat" (korte Engelse zin), "laatst_geraakt", "hoard_toucher",
# "trek", "gezien_vijand". Uitkomst: "gevallen" of "ontsnapt".

signal klaar(held, uitkomst: String, info: Dictionary)

# Kunst van Daan (kunst/LEESMIJ.md, Karakter-laag 19:45): lijf in 5 vaste kleuren, littekens als losse laag,
# hoed met een hap als Gloop hem beet, tekens (8 x 8) boven het hoofd. Nooit schalen (halve pixels).
const SOORT := preload("res://systemen/heldensoort.gd")      # ridder, dief, magiër, bard (versie 1); "" = zoals altijd
const HELD_BEELD := preload("res://systemen/held_beeld.gd")   # lijf, littekens, hoed, wapen, teken en de val
const HELD_LOOP := preload("res://systemen/held_loop.gd")   # lopen: beeld volgt de afgelegde weg, kijken, draaien, springen (#25)
const HELD_VAL := preload("res://systemen/held_val.gd")     # bij een val of bewoner: vallen of zichtbaar overspringen
const HELD_OPSLAG := preload("res://systemen/held_opslag.gd")   # naar_dict en herstel (bewaren midden in een loop)
const HOED_SOORTEN := 10        # Mila 21:55: 10 hoeden in held_hoeden.png en held_hoeden_hap.png
const HOED_TOP := [0, 0, 2, 3, 2, 0, 0, 0, 2, 0]   # Mila 23:00 en 23:10: helm met kam vanaf rij 0, kroon 2 (hoed erboven zakt tussen de punten); bovenste pixel per hoed (helm, puntmuts, kap, pet, kroon, koksmuts, emmer, hoge hoed, pan, veermuts)
const OOGLAP := 1
const SCHRAM := 2                # ooglap en schram nooit samen (zelfde oog, Daan)

const SNEL := 10.0           # afdalen en klimmen, spelpixels per seconde (lopen en vluchten: systemen/held_loop.gd, #25)
# Afdalen en klimmen in gelijke stappen (Daan 13 nov 17:35): op een vaste klok van PAS s, altijd hele spelpixels.
const PAS := 0.1
const KANS := {"slijm": 0.45, "stekelput": 0.35}   # uit sim/ (Bram 9 nov), balans.md had 0,30 en 0,22
const KANS_ANDERS := 0.25
const ROEKELOOS := 0.10      # extra kans om te vallen tegen zijn eigen vijand
const BRUTAAL := 0.8         # Hoard-Toucher: kans om te vallen x 0,8
const NAAM_PUT := "the Spike Pit"
# Sanne 22:55: zolang de wand niet te zien is gaat ook de hoed van een aartsvijand op de bewoner die hem at
# (een trofee, en een hoed verdwijnt nooit zonder dat je ziet waarheen). Wand er (versie 1): op true.
const WAND_ER := false
# De val zelf (Sanne toets 7 punt 2: "duurt één beeld"): schrik (hop van 2 pixels), dan zakt hij in hele pixels
# weg onder de vloerlijn (bijgesneden, niet vervaagd en niet geschaald), het boze wolkje knapt als een poef.
# klaar() komt pas als hij helemaal weg is, dus muntjes en regel vallen samen met het verdwijnen.
# Iris (#7, #25): hij stond ±1 s op de pinnen; nu valt hij meteen: 0,2 s schrik, in 0,4 s weg (was 0,8).
const VAL_S := 0.7           # hele val, daarna klaar()
const VAL_SCHRIK := 0.2      # hop omhoog voordat hij zakt
const VAL_WEG := 0.6         # op dit moment is hij helemaal onder de vloer
const VAL_TEKEN_S := 0.4     # zo lang staat het uitroepteken of de poef erboven

var hol
var info := {}
var trek := "hebzuchtig"
var soort_held := ""         # systemen/heldensoort.gd, uit info["soort_held"]; "" = gewone held
var dut_kol := -1            # slaapkop: kolom waar hij een dutje doet (-1 = geen of al gedaan)
var dut_tot := 0.0
var staat := "afdalen"       # afdalen, lopen, vluchten, klimmen, vallen
var doel_kol := 0
var vijand_kol := -1         # kolom van zijn vijand, -1 als hij er geen (meer) heeft
var klappen := 0
var t := 0.0
var geraakt_tot := 0.0
var val_t := 0.0
var val_x := -1.0            # in een val: midden van de putkolom, daar schuift hij heen voor hij zakt (moet Daan 15 nov 17:50)
var pas_klok := PAS / 4.0    # tijd sinds de laatste stap; start een kwart stap voor de beeldgrens, zodat beelden die
                             # een paar ms te vroeg of te laat komen niet afwisselend 0 en 2 pixels geven (controleur 13 nov)
var pas_rest := 0.0          # niet meer gebruikt sinds keus b van Daan (13 nov 19:45, altijd hele pixels per stap); blijft voor oude saves
var passen := 0              # stappen in deze aanroep van stap()
var val_teken := ""          # het teken op het moment dat hij viel ("boos" wordt een poef)
var gezien := {}             # kolommen waar hij al gegooid heeft
var rng := RandomNumberGenerator.new()
var verdedigingen := 0       # hoeveel keer hij al gooide (voor moet_vallen)
var vloer := 36.0            # voeten op de vloer van de gang: uit hol.cel_naar_pos (Olaf 19:40: nu 38)
var kleur_nr := 0            # rij in held_lijf_kleuren.png, vast per naam
var hoed_nr := 0
var littekens: Array[int] = []
# lopen (systemen/held_loop.gd, issue #25)
var loop_stap := 1.0         # spelpixels per beeldwissel (stap_px uit sprites.json)
var loop_fps := 10.0
var loop_n := 4              # loopbeelden in een kring (6 bij een 3D-blad)
var loop_klok := 0.25        # start een kwart beeld voor de grens, zodat haperende beelden niet afwisselend 0 en 2 wissels geven
var afgelegd := 0.0          # spelpixels gelopen sinds hij begon te lopen of te vluchten: daaruit volgt het loopbeeld
var kijk_tot := 0.0
var volgende_kijk := 0.0
var draai_tot := 0.0
var spring_t := -1.0         # >= 0: in de sprong over een val
var spring_van := 0.0
var spring_naar := 0.0
var spring_teken := ""
var na_sprong := ""          # "vluchten": na de landing omdraaien
var terug_gesprongen := {}   # kolommen met een val waar hij bij het vluchten al overheen terugsprong
var rng_loop := RandomNumberGenerator.new()   # eigen dobbelsteen voor rondkijken, zodat de val-uitkomsten gelijk blijven

func is_held() -> bool:
	return true

func start(h, i: Dictionary) -> void:
	hol = h
	info = i
	texture_filter = CanvasItem.TEXTURE_FILTER_NEAREST
	var naam: String = String(info.get("naam", "Hero"))
	rng.seed = int(info.get("zaad", hash([naam, int(info.get("bezoeken", 0)), Time.get_ticks_usec()])))
	trek = String(info.get("trek", ""))
	if trek == "":
		trek = "schijterig" if (hash(naam) & 1) == 1 else "hebzuchtig"
		info["trek"] = trek
	soort_held = String(info.get("soort_held", ""))
	if not SOORT.geldig(soort_held):
		soort_held = ""
	dut_kol = -1
	if trek == "slaapkop":
		dut_kol = int(round(lerpf(float(hol.ingang().x), float(hol.schat().x), 0.5)))   # halverwege het hol
	var p: Vector2 = hol.cel_naar_pos(hol.ingang())
	vloer = p.y
	position = Vector2(p.x, 2)
	_kies_uiterlijk(naam)
	_kies_doel()
	rng_loop.seed = hash(naam + "#loop")
	HELD_LOOP.kies(self)

# Bewaren van een held die nog in het hol loopt (Olaf, kan-punt 00:40: bij wisselen van hoogte of afsluiten
# verdween hij). naar_dict() geeft alleen JSON-veilige waarden (kleuren als tekst, rng.state als tekst want
# JSON rekent met doubles); herstel(hol, d) zet hem precies terug, ook midden in een val. Roep herstel aan na
# add_child (anders vindt hij de bewoners niet). Een held die al "weg" is geeft {}: niet bewaren.
# Alleen de velden hieronder worden weer een Color of een heel getal; een nieuw kleurveld hier bijzetten.
func naar_dict() -> Dictionary:
	return HELD_OPSLAG.naar_dict(self)

func herstel(h, d: Dictionary) -> void:
	HELD_OPSLAG.herstel(self, h, d)

# Vast per naam (zaad = naam), zodat je Kees herkent als hij terugkomt.
func _kies_uiterlijk(naam: String) -> void:
	kleur_nr = int(info.get("kleur_nr", absi(hash(naam + "#lijf")) % 5))
	hoed_nr = absi(int(info.get("hoed_nr", absi(hash(naam))))) % HOED_SOORTEN
	# littekens: bezoek 2 een, bezoek 3 twee, aartsvijand (drie keer gevlucht) drie
	var n := clampi(int(info.get("bezoeken", 0)), 0, 3)
	var r := RandomNumberGenerator.new()
	r.seed = hash(naam + "#litteken")
	var volgorde := [0, 1, 2, 3]
	for i in range(3, 0, -1):
		var j := r.randi_range(0, i)
		var tmp = volgorde[i]
		volgorde[i] = volgorde[j]
		volgorde[j] = tmp
	littekens.clear()
	for l in volgorde:
		if littekens.size() >= n:
			break
		if (l == OOGLAP and SCHRAM in littekens) or (l == SCHRAM and OOGLAP in littekens):
			continue
		littekens.append(l)

func is_aartsvijand() -> bool:
	return int(info.get("bezoeken", 0)) >= 3 or bool(info.get("aartsvijand", false))

func is_gebeten() -> bool:
	# alleen echt gebeten (strook.gd bewaart info.gebeten bij terugkomers). Niet uit de wrok afleiden:
	# Kees II heeft een wrok tegen Gloop omdat Gloop zijn vader at, maar zelf is hij nooit gebeten.
	return bool(info.get("gebeten", false))

# Welk teken boven zijn hoofd, "" voor geen. Eén tegelijk: boos > zweet > uitroep > ster.
func teken_nu() -> String:
	if spring_t >= 0.0:
		return spring_teken    # sprong over een val: waarom hij niet viel (held_loop.gd)
	if staat == "dutten":
		return "zzz"           # slaapkop doet een dutje in je hol
	if staat == "lopen" and vijand_kol >= 0:
		return "boos"          # wrok en op weg naar zijn vijand
	if staat in ["vluchten", "klimmen"]:
		return "zweet"
	if staat == "lopen" and absf(position.x - hol.cel_naar_pos(hol.schat()).x) < 40.0:
		return "uitroep"       # ziet de schat
	if is_aartsvijand():
		return "ster"          # aartsvijand, blijft staan
	return ""

# Waar loopt hij heen? Vijand eerst, anders de schat.
func _kies_doel() -> void:
	vijand_kol = _zoek_vijand(String(info.get("wrok", "")))
	doel_kol = vijand_kol if vijand_kol >= 0 else hol.schat().x
	info["gezien_vijand"] = false

func _zoek_vijand(wrok: String) -> int:
	if wrok == "" or wrok == "your Hoard":
		return -1
	var start_kol: int = hol.ingang().x
	var eind: int = hol.schat().x
	for k in range(start_kol, eind + 1):
		var cel := Vector2i(k, 0)
		if wrok == NAAM_PUT and hol.val_op(cel) != "":
			return k
		var b = _bewoner_op(k)
		if b != null and b.naam() == wrok:
			return k
	return -1

func _bewoner_op(k: int):
	if get_parent() == null:
		return null
	for w in get_parent().get_children():
		if w != self and w.has_method("is_bewoner") and hol.pos_naar_cel(w.position).x == k:
			if w.has_method("kan_vechten") and not w.kan_vechten():
				continue   # even plat: hij loopt er gewoon langs
			return w
	return null

func _process(delta: float) -> void:
	stap(delta)

# Los van _process zodat de toetsen hem met de hand kunnen laten lopen.
func stap(delta: float) -> void:
	t += delta
	var echt := delta
	delta *= clampf(float(info.get("snelheid", 1.0)) * SOORT.snel(soort_held), 0.25, 4.0)   # alleen lopen en klimmen; t en het wegzakken blijven gewoon
	pas_klok += echt
	passen = int(pas_klok / PAS + 0.0001)
	pas_klok = maxf(0.0, pas_klok - passen * PAS)
	var f := delta / echt if echt > 0.0 else 1.0   # snelheidsfactor van deze held
	if spring_t >= 0.0:
		HELD_LOOP.sprong_tik(self, echt)   # over een val heen (#25); daarna gewoon verder of omdraaien
		queue_redraw()
		return
	match staat:
		"afdalen":
			position.y = move_toward(position.y, vloer, _px(f))
			if position.y >= vloer:
				staat = "lopen"
		"lopen":
			if vijand_kol < 0:
				doel_kol = hol.schat().x   # de schat schuift mee als je graaft
			var doel: Vector2 = hol.cel_naar_pos(Vector2i(doel_kol, 0))
			if dut_kol >= 0 and hol.pos_naar_cel(position).x == dut_kol and (hol.val_op(Vector2i(dut_kol, 0)) != "" or _bewoner_op(dut_kol) != null):
				dut_kol = dut_kol + 1 if dut_kol + 1 < hol.schat().x else -1   # niet bovenop een val of bewoner slapen: een kolom verder
			if dut_kol >= 0 and hol.pos_naar_cel(position).x == dut_kol and vijand_kol < 0:
				dut_kol = -1
				dut_tot = t + SOORT.DUT_S
				staat = "dutten"
				info["dutje"] = true
				return
			# lopen (#25): het loopbeeld volgt de weg, elke 3 tot 6 s even rondkijken (held_loop.gd)
			if not HELD_LOOP.kijkt(self):
				HELD_LOOP.loop(self, HELD_LOOP.wissels(self, echt, false), doel.x, true)
			if staat == "lopen" and absf(position.x - doel.x) < 0.5:
				_aangekomen()
		"dutten":
			if t >= dut_tot:
				staat = "lopen"   # wakker, verder (dezelfde kolom gooit hij niet nog eens)
		"vluchten":
			var terug: Vector2 = hol.cel_naar_pos(hol.ingang())
			if t >= draai_tot - HELD_LOOP.EPS:   # eerst het draai-beeld
				HELD_LOOP.loop(self, HELD_LOOP.wissels(self, echt, true), terug.x, false)
			if absf(position.x - terug.x) < 0.5:
				staat = "klimmen"
		"klimmen":
			position.y = move_toward(position.y, -4, _px(f))
			if position.y <= -4:
				staat = "weg"
				klaar.emit(self, "ontsnapt", info)
				queue_free()
		"vallen":
			if val_x >= 0.0 and position.x != val_x:   # binnen de schrik (0,2 s) naar het midden van de put, hele spelpixels
				var deel := minf(echt / maxf(VAL_SCHRIK - val_t, echt), 1.0)
				position.x = move_toward(position.x, val_x, maxf(ceilf(absf(val_x - position.x) * deel), 1.0))
			val_t += echt
			if val_t >= VAL_S:
				staat = "weg"
				klaar.emit(self, "gevallen", info)
				queue_free()
	queue_redraw()

# Hele pixels voor deze aanroep (afdalen en klimmen): per stap van de klok (PAS) een heel aantal spelpixels, nooit een
# rest (Daan 13 nov 19:45, keus b). Lopen en vluchten gaan sinds 25 nov via systemen/held_loop.gd (stap_px per beeld).
func _px(factor: float) -> float:
	if passen == 0:
		return 0.0
	return float(passen * maxi(1, roundi(factor * SNEL * PAS)))

func _aangekomen() -> void:
	if doel_kol == vijand_kol:
		# zijn vijand stond er niet meer (weggehaald) of hij overleefde het duel: door naar de schat
		vijand_kol = -1
		doel_kol = hol.schat().x
		return
	# bij de schat: aanraken, niets pakken, wegrennen
	info["hoard_toucher"] = true
	info["wat"] = "touched your hoard, took nothing and ran"
	HELD_LOOP.draai(self)
	if SOORT.zingt(soort_held):
		info["lied"] = SOORT.LIED_HELDEN

# De upgrades (systemen/upgrades.gd) hangen aan het hol als dat een eigenschap "upgrades" heeft; anders null.
func _upgrades():
	if hol != null and "upgrades" in hol:
		return hol.get("upgrades")
	return null

func _onderweg() -> void:
	HELD_VAL.onderweg(self)   # val of bewoner: valt hij, of springt hij zichtbaar over (systemen/held_val.gd)

# Hoe de val eruitziet op tijd vt (los van _draw, zodat de toets het kan nakijken zonder te tekenen):
# hop (negatief = omhoog), zak (0 tot 16 pixels onder de vloer), teken erboven ("uitroep", "poef" of ""),
# poef_fase (0 tot 1) en of de hoed nog getekend wordt (niet als hij al op de toren van de bewoner staat).
func val_beeld(vt: float) -> Dictionary:
	var hop := 0
	if vt < VAL_SCHRIK:
		hop = -2 if vt < VAL_SCHRIK * 0.5 else -1
	var u := clampf((vt - VAL_SCHRIK) / (VAL_WEG - VAL_SCHRIK), 0.0, 1.0)
	var zak := int(round(16.0 * u * u))    # eerst langzaam, dan snel: hij wordt naar binnen getrokken
	var tk := ""
	if vt < VAL_TEKEN_S:
		tk = "poef" if val_teken == "boos" else "uitroep"
	return {"hop": hop, "zak": zak, "teken": tk, "poef_fase": clampf(vt / VAL_TEKEN_S, 0.0, 1.0),
		"hoed": String(info.get("hoed_naar", "")) == ""}

# ---- tekenen: in systemen/held_beeld.gd (opgesplitst 10 nov, held.gd bleef anders boven de 400 regels) ----
func _draw() -> void:
	HELD_BEELD.teken(self)
