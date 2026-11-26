extends Node2D
# Laag met de gouden stenen van stap 4 tot 6 (#162, systemen/stap_teken.gd). Een eigen laag, zodat Gloop en het hol
# (die vaak opnieuw tekenen: ademen, flakkeren) de stenen niet elk beeld opnieuw tekenen: deze laag tekent alleen als
# het aantal of de plek verandert. hol.gd en slijm.gd roepen zet() aan vanuit hun _draw; dat is alleen een vergelijking.
const STAP_TEKEN := preload("res://systemen/stap_teken.gd")

var plekken: Array = []   # middens van de rijen (Vector2, spelpixels in de ouder)
var n := 0

func zet(nieuw_plekken: Array, nieuw_n: int) -> void:
	if nieuw_n == n and nieuw_plekken == plekken:
		return
	plekken = nieuw_plekken
	n = nieuw_n
	queue_redraw()

func _draw() -> void:
	for p in plekken:
		STAP_TEKEN.teken(self, p, n)

# Maak de laag als eerste kind van de ouder: boven de ouder zelf, onder de andere lagen (helden, licht).
static func maak(ouder: Node) -> Node2D:
	var l: Node2D = load("res://systemen/stap_stenen.gd").new()
	l.name = "StapStenen"
	ouder.add_child(l)
	ouder.move_child(l, 0)
	return l
