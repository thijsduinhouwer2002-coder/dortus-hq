# Hol 2.0 proef (Olaf, #388): Gloop scharrelt zelf, loopt waar je klikt, en laat zich besturen.
# Scharrelen volgt de tabel in ontwerp-hol2/LEESMIJ.md punt 4: als een gedraging klaar is, kiest hij één nieuwe uit
# de tabel van de plek waar hij staat (één gewogen loting). Past niets, dan terug naar de troon (vangnet).
# Een held op dezelfde verdieping binnen 40 spelpx gaat altijd voor: Gloop draait zich om en kijkt.
extends "res://hol2/loper.gd"

const F_RUST := 0
const F_PLAT := 1
const F_KNIPPER := 2
const F_BLIJ := 3
const F_HAP := 4
const F_KNEEP := 5
const F_SPUUG := 6

# plek -> [[gedraging, gewicht, min s, max s]]
const TABEL := {
	"troon": [["zitten", 4, 6.0, 12.0], ["tellen", 2, 3.0, 3.0], ["slapen", 2, 10.0, 20.0], ["opstaan", 2, 0.0, 0.0]],
	"vloer": [["wandelen", 4, 0.0, 0.0], ["snuffelen", 2, 3.0, 3.0], ["spugen", 1, 2.0, 2.0], ["naar_troon", 2, 0.0, 0.0]],
	"ladder": [["klimmen", 5, 0.0, 0.0], ["rondkijken", 1, 2.0, 2.0]],
	"rand": [["gluren", 2, 2.0, 2.0], ["ploppen", 1, 1.0, 1.0], ["wandelen", 2, 0.0, 0.0]],
	"tuin": [["zonnen", 3, 5.0, 10.0], ["eten", 2, 3.0, 3.0], ["aanstaren", 4, 2.0, 2.0], ["naar_beneden", 3, 0.0, 0.0]],
}

var rng: RandomNumberGenerator
var doet := ""            # huidige gedraging
var rest := 0.0           # seconden over (voor gedragingen met een duur)
var frame := F_RUST
var t := 0.0
var bestuurd := false     # besturen-stand (WASD), gezet door hol2.gd
var stuur_dx := 0
var helden_ref: Array = []
var log_f: Callable       # log_regel van hol2.gd
var na_pad := ""          # wat te doen als het pad af is ("snuffelen", "eten", ...)
var kijk_held = null
var gekozen := ""         # de laatst gelote gedraging (voor de log en de toets)

func _init() -> void:
	snel = 26.0
	klim_snel = 18.0

func plek() -> String:
	if klimt:
		return "ladder"
	if niveau == 0:
		return "tuin"
	var tx: float = kaart.troon_x + 6
	if niveau == kaart.troon_niveau and absf(x - tx) < 14:
		return "troon"
	for l in kaart.ladders:
		var lx: float = l.x + kaart.LAD_B / 2.0
		if absf(lx - x) <= 6.0 and (l.boven == niveau or l.onder == niveau):
			return "rand" if l.boven == niveau and niveau > 0 and rng.randf() < 0.4 else "ladder"
	return "vloer"

# Klikken om te lopen (ook als hij bestuurd wordt niet: dan gaan de toetsen voor).
func klik_naar(n: int, px: float) -> void:
	if ga_naar(n, px):
		doet = "op_weg"
		na_pad = ""
		log_f.call("HOL2 gloop loopt naar niveau %d x %d (klik)" % [n, int(px)])

func kies() -> void:
	var p := plek()
	var lijst: Array = TABEL.get(p, [])
	var som := 0
	for g in lijst:
		som += g[1]
	if som == 0:
		_begin("naar_troon", 0.0)
		return
	var r := rng.randi_range(1, som)
	for g in lijst:
		r -= g[1]
		if r <= 0:
			_begin(g[0], rng.randf_range(g[2], g[3]))
			log_f.call("HOL2 gloop %s (plek %s)" % [g[0], p])
			return

func _begin(wat: String, duur: float) -> void:
	doet = wat
	rest = duur
	na_pad = ""
	match wat:
		"opstaan":
			ga_naar(niveau, x - rng.randf_range(20.0, 40.0))   # van de troon af, daarna de tabel van de vloer
		"wandelen":
			# soms naar een ladder op deze verdieping, zodat de plekken ladder en rand (en zo de tuin) ook voorkomen
			var doel_x := rng.randf_range(20.0, kaart.breed - 20.0)
			var hier: Array = kaart.ladders.filter(func(l): return l.boven == niveau or l.onder == niveau)
			if not hier.is_empty() and rng.randf() < 0.4:
				doel_x = hier[rng.randi_range(0, hier.size() - 1)].x + kaart.LAD_B / 2.0
			if not ga_naar(niveau, doel_x):
				_vangnet()
		"naar_troon":
			_vangnet()
		"snuffelen":
			var v = _dichtste_val()
			if v != null and absf(v.x + 6 - x) > 2.0 and ga_naar(niveau, v.x + 6):
				na_pad = "snuffelen"
				doet = "op_weg"
		"eten":
			var k = _dichtste("kool")
			if k != null and absf(k.x + 3 - x) > 2.0 and ga_naar(0, k.x + 3):
				na_pad = "eten"
				doet = "op_weg"
		"klimmen", "ploppen":
			var naar := niveau + 1
			if kaart.ladder_tussen(niveau, naar, x).is_empty() or ladder_hier(naar).is_empty():
				naar = niveau - 1
			if ladder_hier(naar).is_empty() or naar < 0:
				_vangnet()
			else:
				klim_snel = 40.0 if wat == "ploppen" else 18.0
				ga_naar(naar, x + rng.randf_range(-60.0, 60.0))
				log_f.call("HOL2 gloop klimt van %d naar %d" % [niveau, naar])
		"naar_beneden":
			ga_naar(1, x + rng.randf_range(-80.0, 80.0))
	gekozen = wat
	if wat in ["opstaan", "klimmen", "ploppen", "wandelen", "naar_troon", "naar_beneden"]:
		doet = "op_weg" if loopt() else doet

func _vangnet() -> void:
	ga_naar(kaart.troon_niveau, kaart.troon_x + 6)
	doet = "op_weg"
	na_pad = "zitten"

func _dichtste_val():
	var beste = null
	var d := 220.0
	for v in kaart.vallen:
		if v.niveau == niveau and absf(v.x + 6 - x) < d:
			d = absf(v.x + 6 - x)
			beste = v
	return beste

func _dichtste(soort: String):
	var beste = null
	var d := INF
	for b in kaart.bloemen:
		if b.soort == soort and absf(b.x - x) < d:
			d = absf(b.x - x)
			beste = b
	return beste

func werk(delta: float) -> void:
	t += delta
	if bestuurd:
		_bestuur(delta)
		return
	# een held dichtbij gaat voor
	kijk_held = null
	if not klimt:
		for h in helden_ref:
			if h.leeft and h.niveau == niveau and absf(h.x - x) < 40.0 and not h.klimt:
				kijk_held = h
				break
	if kijk_held != null and doet != "op_weg":
		naar_rechts = kijk_held.x > x
		frame = F_BLIJ if fmod(t, 1.0) < 0.5 else F_RUST
		return
	if doet == "op_weg" or loopt():
		var klaar := stap(delta)
		frame = F_KNEEP if (int(t * 4.0) % 2 == 0 and not klimt) else F_RUST
		if not loopt():
			klim_snel = 18.0
			if na_pad != "":
				var wat := na_pad
				_begin(wat, 3.0 if wat != "zitten" else rng.randf_range(6.0, 12.0))
				return
			doet = ""
		if klaar == "klim":
			log_f.call("HOL2 gloop is op niveau %d" % niveau)
		return
	rest -= delta
	match doet:
		"zitten":
			frame = F_KNIPPER if fmod(t, 3.5) < 0.25 else F_RUST
		"tellen":
			frame = F_BLIJ
		"slapen":
			frame = F_PLAT if rest > 0.5 else F_RUST
		"snuffelen":
			frame = F_KNEEP if fmod(t, 0.5) < 0.25 else F_RUST
		"spugen":
			frame = F_SPUUG
		"rondkijken", "gluren":
			naar_rechts = fmod(t, 1.0) < 0.5
			frame = F_RUST
		"zonnen":
			frame = F_PLAT
		"eten":
			frame = F_HAP if fmod(t, 0.5) < 0.25 else F_RUST
		"aanstaren":
			frame = F_BLIJ
			for h in helden_ref:
				if h.leeft and h.niveau == 0:
					naar_rechts = h.x > x
					break
		_:
			frame = F_RUST
	if rest <= 0.0:
		kies()

func _bestuur(delta: float) -> void:
	if loopt():
		stap(delta)   # een klim of klikpad maakt hij af
		frame = F_KNEEP if int(t * 4.0) % 2 == 0 else F_RUST
		return
	if stuur_dx != 0:
		naar_rechts = stuur_dx > 0
		x = clampf(x + stuur_dx * snel * 1.4 * delta, 4.0, kaart.breed - 4.0)
		frame = F_KNEEP if int(t * 4.0) % 2 == 0 else F_RUST
	else:
		frame = F_KNIPPER if fmod(t, 3.5) < 0.25 else F_RUST

# W/S in de besturen-stand: klimmen als er hier een ladder is.
func klim_toets(omhoog: bool) -> bool:
	var naar := niveau - 1 if omhoog else niveau + 1
	var l := ladder_hier(naar)
	if l.is_empty() or naar < 0:
		return false
	pad = [{"soort": "klim", "naar": naar, "x": l.x + kaart.LAD_B / 2.0}]
	log_f.call("HOL2 gloop klimt van %d naar %d (toets)" % [niveau, naar])
	return true

func teken(laag: CanvasItem, tex: Texture2D, info: Dictionary, tegels: Texture2D, munt_r: Rect2) -> void:
	var w: int = info.w
	var h: int = info.h
	var p := pos()
	var wip := -1.0 if (loopt() and not klimt and int(t * 4.0) % 2 == 1) else 0.0
	var dst := Rect2(p.x - info.anker_x, p.y - h + wip, w, h)
	var src := Rect2(frame * w, 0, w, h)
	if not naar_rechts:
		laag.draw_set_transform(Vector2(2.0 * p.x, 0), 0.0, Vector2(-1, 1))
	laag.draw_texture_rect_region(tex, dst, src)
	laag.draw_set_transform(Vector2.ZERO)
	if doet == "slapen" and not loopt():
		var z := int(t * 2.0) % 3
		laag.draw_rect(Rect2(p.x + 4 + z, p.y - h - 2 - z * 2, 3, 1), Color8(230, 230, 240))
		laag.draw_rect(Rect2(p.x + 5 + z, p.y - h - 1 - z * 2, 1, 1), Color8(230, 230, 240))
		laag.draw_rect(Rect2(p.x + 4 + z, p.y - h - z * 2, 3, 1), Color8(230, 230, 240))
	if doet == "tellen" and not loopt():
		var hop := absi(int(t * 6.0) % 6 - 3)
		laag.draw_texture_rect_region(tegels, Rect2(p.x + 2, p.y - h - 2 - hop, 2, 2), munt_r)
