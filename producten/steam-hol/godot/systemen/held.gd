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
# Terug in info (voor strook.gd en kroniek.gd): "wat" (korte Engelse zin), "laatst_geraakt", "hoard_toucher",
# "trek", "gezien_vijand". Uitkomst: "gevallen" of "ontsnapt".

signal klaar(held, uitkomst: String, info: Dictionary)

# Kunst van Daan (kunst/LEESMIJ.md, Karakter-laag 19:45): lijf in 5 vaste kleuren, littekens als losse laag,
# hoed met een hap als Gloop hem beet, tekens (8 x 8) boven het hoofd. Nooit schalen (halve pixels).
const LIJF := preload("res://kunst/held_lijf_kleuren.png")   # 4 loopframes x 5 rijen (rood, groen, paars, oker, zeegroen)
const HOEDEN := preload("res://kunst/held_hoeden.png")
const HOEDEN_HAP := preload("res://kunst/held_hoeden_hap.png")
const LITTEKENS := preload("res://kunst/held_littekens.png")  # pleister, ooglap, schram, verband
const WAPENS := preload("res://kunst/held_wapens.png")
const TEKENS := preload("res://kunst/tekens.png")            # boos, uitroep, zweet, zzz, ster
const TEKEN := {"boos": 0, "uitroep": 1, "zweet": 2, "zzz": 3, "ster": 4}
const HOED_SOORTEN := 10        # Mila 21:55: 10 hoeden in held_hoeden.png en held_hoeden_hap.png
const HOED_TOP := [0, 0, 2, 3, 2, 0, 0, 0, 2, 0]   # Mila 23:00 en 23:10: helm met kam vanaf rij 0, kroon 2 (hoed erboven zakt tussen de punten); bovenste pixel per hoed (helm, puntmuts, kap, pet, kroon, koksmuts, emmer, hoge hoed, pan, veermuts)
const OOGLAP := 1
const SCHRAM := 2                # ooglap en schram nooit samen (zelfde oog, Daan)

const SNEL := 11.0           # spelpixels per seconde
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
const VAL_S := 1.1           # hele val, daarna klaar()
const VAL_SCHRIK := 0.2      # hop omhoog voordat hij zakt
const VAL_WEG := 1.0         # op dit moment is hij helemaal onder de vloer
const VAL_TEKEN_S := 0.4     # zo lang staat het uitroepteken of de poef erboven

var hol
var info := {}
var trek := "hebzuchtig"
var staat := "afdalen"       # afdalen, lopen, vluchten, klimmen, vallen
var doel_kol := 0
var vijand_kol := -1         # kolom van zijn vijand, -1 als hij er geen (meer) heeft
var klappen := 0
var t := 0.0
var geraakt_tot := 0.0
var val_t := 0.0
var val_teken := ""          # het teken op het moment dat hij viel ("boos" wordt een poef)
var gezien := {}             # kolommen waar hij al gegooid heeft
var rng := RandomNumberGenerator.new()
var verdedigingen := 0       # hoeveel keer hij al gooide (voor moet_vallen)
var vloer := 36.0            # voeten op de vloer van de gang: uit hol.cel_naar_pos (Olaf 19:40: nu 38)
var kleur_nr := 0            # rij in held_lijf_kleuren.png, vast per naam
var hoed_nr := 0
var littekens: Array[int] = []

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
	var p: Vector2 = hol.cel_naar_pos(hol.ingang())
	vloer = p.y
	position = Vector2(p.x, 2)
	_kies_uiterlijk(naam)
	_kies_doel()

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
	delta *= clampf(float(info.get("snelheid", 1.0)), 0.25, 4.0)   # alleen lopen en klimmen; t en het wegzakken blijven gewoon
	match staat:
		"afdalen":
			position.y = move_toward(position.y, vloer, SNEL * delta)
			if position.y >= vloer:
				staat = "lopen"
		"lopen":
			if vijand_kol < 0:
				doel_kol = hol.schat().x   # de schat schuift mee als je graaft
			var doel: Vector2 = hol.cel_naar_pos(Vector2i(doel_kol, 0))
			position.x = move_toward(position.x, doel.x, SNEL * (1.25 if trek == "hebzuchtig" else 1.0) * delta)
			_onderweg()
			if staat == "lopen" and absf(position.x - doel.x) < 0.5:
				_aangekomen()
		"vluchten":
			var terug: Vector2 = hol.cel_naar_pos(hol.ingang())
			position.x = move_toward(position.x, terug.x, SNEL * 1.5 * delta)
			if absf(position.x - terug.x) < 0.5:
				staat = "klimmen"
		"klimmen":
			position.y = move_toward(position.y, -4, SNEL * delta)
			if position.y <= -4:
				staat = "weg"
				klaar.emit(self, "ontsnapt", info)
				queue_free()
		"vallen":
			val_t += echt
			if val_t >= VAL_S:
				staat = "weg"
				klaar.emit(self, "gevallen", info)
				queue_free()
	queue_redraw()

func _aangekomen() -> void:
	if doel_kol == vijand_kol:
		# zijn vijand stond er niet meer (weggehaald) of hij overleefde het duel: door naar de schat
		vijand_kol = -1
		doel_kol = hol.schat().x
		return
	# bij de schat: aanraken, niets pakken, wegrennen
	info["hoard_toucher"] = true
	info["wat"] = "touched your hoard, took nothing and ran"
	staat = "vluchten"

# De upgrades (systemen/upgrades.gd) hangen aan het hol als dat een eigenschap "upgrades" heeft; anders null.
func _upgrades():
	if hol != null and "upgrades" in hol:
		return hol.get("upgrades")
	return null

func _onderweg() -> void:
	var cel: Vector2i = hol.pos_naar_cel(position)
	if gezien.has(cel.x):
		return
	var soort: String = hol.val_op(cel)
	var b = _bewoner_op(cel.x)
	if soort == "" and b == null:
		return
	gezien[cel.x] = true
	if soort != "":
		b = null   # val en bewoner in dezelfde kolom: hij vecht tegen de val
	var naam_vijand: String = NAAM_PUT if soort != "" else b.naam()
	var soort_vd: String = soort if soort != "" else String(b.get("soort") if "soort" in b else "slijm")
	var kans: float = KANS.get(soort_vd, KANS_ANDERS)
	var upg = _upgrades()
	if upg != null:
		kans += upg.kans_erbij(soort_vd)   # systemen/upgrades.gd: +7 procentpunt per gekochte stap (balans.md)
	var is_vijand := vijand_kol >= 0 and cel.x == vijand_kol
	if is_vijand:
		info["gezien_vijand"] = true
		kans += ROEKELOOS
	if bool(info.get("hoard_toucher", false)):
		kans *= BRUTAAL
	verdedigingen += 1
	var valt := rng.randf() < kans
	# vaste uitkomsten voor de eerste tien minuten (Olaf 20:25 en 20:45, Sanne features.md); strook.gd zet ze alleen bij een vers spel
	if bool(info.get("moet_vallen", false)) and verdedigingen == 1:
		valt = true
	if bool(info.get("moet_vluchten", false)) and verdedigingen == 1:
		valt = false           # één klap en hij rent (hieronder)
	if bool(info.get("moet_doorlopen", false)):
		valt = false           # overleeft alles en raakt de schat aan: Hoard-Toucher
	if bool(info.get("moet_opgegeten", false)):
		valt = b != null       # een bewoner krijgt hem (held 5: eerste hoed op Gloop); een val overleeft hij
	if bool(info.get("moet_afgerekend", false)):
		valt = is_vijand       # alles onderweg overleeft hij, zijn eigen vijand krijgt hem
	if valt:
		info["laatst_geraakt"] = naam_vijand
		info["wat"] = ("finally fell to " if is_vijand else "fell to ") + naam_vijand
		val_teken = teken_nu()
		staat = "vallen"
		if b != null and b.has_method("raak"):
			# hoedentoren: zijn hoed gaat naar de bewoner; een aartsvijand pas naar de wand als die te zien is (WAND_ER)
			var naar_wand := WAND_ER and is_aartsvijand()
			var n = null
			if b.has_method("hoeden_op_hoofd"):   # slijm.gd met hoedentoren
				n = b.raak(-1 if naar_wand else hoed_nr)
			else:
				b.raak()          # stand-in van Olaf (kern/standin_slijm.gd) kent geen hoeden
			if b.has_method("hoeden_op_hoofd") or naar_wand:
				info["hoed_naar"] = "wand" if naar_wand else "bewoner"   # stand-in zonder toren: hoed blijft op zijn hoofd
			info["hoeden_bewoner"] = 0 if naar_wand or n == null else int(n)   # voor kroniek.hoed(naam, bewoner, aantal)
		return
	# overleefd: geraakt, wrok tegen dit ding; een bewoner die verliest is even plat
	klappen += 1
	geraakt_tot = t + 0.5
	info["laatst_geraakt"] = naam_vijand
	if b != null and b.has_method("plat"):
		b.plat()
	if b != null and String(b.get("soort")) == "slijm":
		info["gebeten"] = true   # door Gloop gebeten: vanaf nu (ook bij terugkomst) een hoed met een hap eruit
	if is_vijand:
		vijand_kol = -1
		doel_kol = hol.schat().x
	# schijterig draait na een klap de helft van de keren om, hebzuchtig pas na twee klappen
	var rent := (trek == "schijterig" and rng.randf() < 0.5) or klappen >= 2
	if soort == "stekelput" and upg != null and upg.put_houdt_vast() and klappen < 2:
		rent = false           # Deep Pit: een schijterige held keert na zijn eerste klap (van de put) niet om
	if bool(info.get("moet_vluchten", false)):
		rent = true
	if bool(info.get("moet_doorlopen", false)) or bool(info.get("moet_opgegeten", false)) or bool(info.get("moet_afgerekend", false)):
		rent = false
	if rent:
		info["wat"] = "got hurt by %s and ran" % naam_vijand
		staat = "vluchten"

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

# ---- tekenen: Daans lijf + litteken + hoed + wapen (16 x 16, anker midden onder), teken erboven ----
# Eén laag van 16 x 16 tekenen, onder de vloerlijn (y 0) afgesneden: zo zakt hij weg zonder te schalen.
func _laag(tex: Texture2D, bron_x: int, bron_y: int, y: int, zak: int, kleur: Color) -> void:
	var h := 16 - zak
	if h <= 0:
		return
	draw_texture_rect_region(tex, Rect2(-8, y, 16, h), Rect2(bron_x, bron_y, 16, h), kleur)

func _draw() -> void:
	if staat == "weg":
		return
	var frame := 0
	if staat in ["lopen", "vluchten"]:
		frame = int(t * 8) % 4
	var omlaag := 1 if frame in [1, 3] else 0
	var links := staat == "vluchten"
	var wapen := 2 if trek == "schijterig" else 0       # schijterig neemt een fakkel mee, hebzuchtig een zwaard
	var kleur := Color.WHITE
	if t < geraakt_tot and int(t * 10) % 2 == 0:
		kleur = Color(1, 0.55, 0.55)
	var vb := {}
	var zak := 0
	var hop := 0
	if staat == "vallen":
		vb = val_beeld(val_t)
		zak = int(vb.zak)
		hop = int(vb.hop)
	if links:
		draw_set_transform(Vector2.ZERO, 0, Vector2(-1, 1))   # spiegelen, geen halve pixels
	var y := -16 + zak + hop
	# bij een hop staat hij boven de vloer: niets afsnijden; bij zakken alles onder y 0 weg
	_laag(LIJF, frame * 16, kleur_nr * 16, y, zak, kleur)
	for l in littekens:
		_laag(LITTEKENS, l * 16, 0, y + omlaag, zak, kleur)
	if vb.is_empty() or bool(vb.hoed):
		_laag(HOEDEN_HAP if is_gebeten() else HOEDEN, hoed_nr * 16, 0, y + omlaag, zak, kleur)
	if staat != "vallen":
		_laag(WAPENS, wapen * 16, 0, y + omlaag, 0, kleur)
	draw_set_transform(Vector2.ZERO, 0, Vector2.ONE)
	# teken: één lege rij boven de bovenkant van de hoed (Sanne toets 2: 1 tot 2 spelpixels boven het hoofd)
	var tk: String = teken_nu() if staat != "vallen" else String(vb.teken)
	if tk == "":
		return
	var onder: int = y + int(HOED_TOP[hoed_nr]) + omlaag - 1
	if tk == "poef":
		_poef(onder - 4, float(vb.poef_fase))
		return
	draw_texture_rect_region(TEKENS, Rect2(-4, onder - 8, 8, 8), Rect2(int(TEKEN[tk]) * 8, 0, 8, 8))

# Het boze wolkje knapt: eerst nog even het wolkje, dan vier plukjes die naar buiten schieten en vervagen.
# Hele pixels, geen schalen. Mila mag dit vervangen door een getekende poef (zelfde plek, zelfde tijd).
func _poef(midden_y: int, fase: float) -> void:
	if fase < 0.25:
		draw_texture_rect_region(TEKENS, Rect2(-4, midden_y - 4, 8, 8), Rect2(int(TEKEN["boos"]) * 8, 0, 8, 8))
		return
	var p := (fase - 0.25) / 0.75
	var d := 1 + int(p * 4.0)
	var c := Color(0.85, 0.85, 0.9, 1.0 - p)
	for r in [Vector2i(-1, -1), Vector2i(1, -1), Vector2i(-1, 1), Vector2i(1, 1)]:
		draw_rect(Rect2(r.x * d - 1, midden_y + r.y * d - 1, 2, 2), c)
	if p < 0.4:
		draw_rect(Rect2(-1, midden_y - 1, 2, 2), Color(1, 1, 1, 1.0 - p * 2.0))
