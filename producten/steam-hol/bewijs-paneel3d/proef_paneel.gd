extends SceneTree
# Olaf: proefbeeld van het paneel (kaartje en kroniek) op 160 px, oud en nieuw
var stap := 0
var t
func _initialize():
	t = SubViewport.new(); t.size = Vector2i(1024, 340); t.render_target_update_mode = SubViewport.UPDATE_ALWAYS; root.add_child(t)
	var bg := ColorRect.new(); bg.color = Color("#5a3a4a"); bg.size = Vector2(1024, 340); t.add_child(bg)
	var T = load("res://kern/tekst.gd")
	for i in 2:
		T.met_3d = i == 1
		var n = Node2D.new(); n.set_script(T)
		n.breedte = 1024.0; n.hoogte = 160.0; n.schaal = 4; n.goud = 27
		n.position = Vector2(0, i * 170)
		if i == 0:
			var rg: Array[String] = ["Bram fell in the Spike Pit. +9", "Ties tried to lift it.", "Gloop ate Joost. A crown!"]
			n.regels = rg; n.hover = true
		else:
			n.kaart = {"titel": "Big Gloop", "uitleg": "Bought.", "kost": 45, "kan": true, "tekort": 0, "terug": 45, "weg": false}
		t.add_child(n)
		n.texture_filter = CanvasItem.TEXTURE_FILTER_LINEAR if i == 1 else CanvasItem.TEXTURE_FILTER_NEAREST
	T.met_3d = true
func _process(_d):
	stap += 1
	if stap == 2:
		# met_3d is static: zet oud paneel opnieuw tekenen kan niet tegelijk; daarom twee keer draaien
		pass
	if stap == 5:
		t.get_texture().get_image().save_png(OS.get_environment("UIT"))
		return true
	return false
