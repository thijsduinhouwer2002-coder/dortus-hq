extends Node2D
# Laag met de gouden stenen van stap 4 tot 6 (#162, systemen/stap_teken.gd). Een eigen laag, zodat Gloop en het hol
# (die vaak opnieuw tekenen: ademen, flakkeren) de stenen niet elk beeld opnieuw tekenen: deze laag tekent alleen als
# het aantal, de plek of de schaal verandert, en dan één klaar plaatje per rij. hol.gd en slijm.gd roepen zet() aan
# vanuit hun _draw; dat is alleen een vergelijking.
# Meten (#162): startargument wissel=stenen zet de stenen elke WISSEL_S seconden aan en uit, met een regel
# "HOL wissel stenen aan|uit unix=<s> t=<speltijd>" in de uitvoer. Zo meet je de CPU binnen één run (balans.md: alleen dat telt).
const STAP_TEKEN := preload("res://systemen/stap_teken.gd")
const WISSEL_S := 20.0

var plekken: Array = []   # middens van de rijen (Vector2, spelpixels in de ouder)
var n := 0
var _wissel := false
var _nep := false   # wissel=nep: zelfde regels, stenen blijven aan (placebo voor de ruis)
var _was := true

func _ready() -> void:
	set_notify_transform(true)   # andere hoogte (schaal): plaatje op de nieuwe schaal
	_wissel = "wissel=stenen" in OS.get_cmdline_user_args()
	_nep = "wissel=nep" in OS.get_cmdline_user_args()
	_wissel = _wissel or _nep
	for a in OS.get_cmdline_user_args():
		if a.begins_with("stenen_keer="):
			_keer = clampi(int(a.split("=")[1]), 1, 1000)
	set_process(_wissel)

func _notification(what: int) -> void:
	if what == NOTIFICATION_TRANSFORM_CHANGED:
		queue_redraw()

func _process(_delta: float) -> void:
	# op de klok, zodat de laag van Gloop en die van het hol samen aan en uit gaan (oneven halve minuten uit)
	var aan := int(Time.get_unix_time_from_system() / WISSEL_S) % 2 == 0
	if aan != _was:
		_was = aan
		visible = aan or _nep
		var sc := get_tree().current_scene
		var t: float = float(sc.get("t")) if sc != null and sc.get("t") != null else -1.0
		print("HOL wissel stenen %s unix=%.2f t=%.2f pad=%s" % ["aan" if aan else "uit", Time.get_unix_time_from_system(), t, get_parent().name])

func zet(nieuw_plekken: Array, nieuw_n: int) -> void:
	if nieuw_n == n and nieuw_plekken == plekken:
		return
	plekken = nieuw_plekken
	n = nieuw_n
	queue_redraw()

func _draw() -> void:
	for i in _keer:
		for p in plekken:
			STAP_TEKEN.teken(self, p + Vector2(0.0, -0.01 * i), n)

# stenen_keer=<n> (alleen meten): elke rij n keer over elkaar, zodat de kost van één rij n keer zo groot en meetbaar wordt
var _keer := 1

# Maak de laag als eerste kind van de ouder: boven de ouder zelf, onder de andere lagen (helden, licht).
static func maak(ouder: Node) -> Node2D:
	var l: Node2D = load("res://systemen/stap_stenen.gd").new()
	l.name = "StapStenen"
	ouder.add_child(l)
	ouder.move_child(l, 0)
	return l
