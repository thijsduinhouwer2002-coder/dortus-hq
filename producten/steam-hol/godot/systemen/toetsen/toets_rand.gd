extends SceneTree
# Toetsen voor rand en schaduw om elke held (Olaf 27 nov, issue #242, keuze Sanne: rand 1 spelpx #1a1008 dekking 0,85
# om lijf en hoed, schaduwvlek 10 x 3 spelpx dekking 0,35, weg zodra de held valt).
# Draaien: godot --headless --path <godot-map> -s systemen/toetsen/toets_rand.gd
const RAND := preload("res://systemen/held_rand.gd")
const HB := preload("res://systemen/held_beeld.gd")
var fout := 0

func ok(voorwaarde: bool, wat: String) -> void:
	if voorwaarde:
		print("[rand-toets] OK ", wat)
	else:
		fout += 1
		print("[rand-toets] FOUT ", wat)

func _init() -> void:
	kleur()
	silhouetten()
	schaduw()
	print("[rand-toets] klaar: %d FOUT" % fout)
	quit(1 if fout > 0 else 0)

func kleur() -> void:
	var c := RAND.RAND_KLEUR
	ok(c.r8 == 0x1a and c.g8 == 0x10 and c.b8 == 0x08, "rand warm bijna zwart #1a1008, niet puur zwart")
	ok(absf(c.a - 0.85) < 0.001, "rand dekking 0,85")
	ok(RAND.RAND_PX == 1.0 and RAND.RICHTING.size() == 4, "rand 1 spelpx naar 4 kanten")
	ok(RAND.SCHADUW_B == 10.0 and RAND.SCHADUW_H == 3.0 and absf(RAND.SCHADUW_A - 0.35) < 0.001, "schaduw 10 x 3 spelpx, dekking 0,35")

# Voor elk heldenblad en de hoeden: het silhouet is even groot, wit, vol waar het blad vol is, leeg in de waas (alfa <= 96).
func silhouetten() -> void:
	HB._laad_3d()
	var namen := ["ridder", "heks", "dief", "bard", "held0", "held1", "held2", "held3", "held4", HB.HOEDEN3D, HB.HOEDEN3D_HAP]
	for naam in namen:
		if not HB.held3d.has(naam):
			ok(false, "blad %s geladen" % naam)
			continue
		var ct: CanvasTexture = HB.held3d[naam][0]
		var t0 := Time.get_ticks_usec()
		var s: CanvasTexture = RAND.silhouet(ct)
		var ms := (Time.get_ticks_usec() - t0) / 1000.0
		if s == null:
			ok(false, "silhouet %s gemaakt" % naam)
			continue
		var a := ct.diffuse_texture.get_image()
		a.decompress()
		a.clear_mipmaps()
		a.convert(Image.FORMAT_RGBA8)
		var b := s.diffuse_texture.get_image()
		b.clear_mipmaps()
		var mis := 0
		var niet_wit := 0
		var vol := 0
		for y in range(0, a.get_height(), 2):
			for x in range(0, a.get_width(), 2):
				var ca := a.get_pixel(x, y)
				var cb := b.get_pixel(x, y)
				var a8 := ca.a8
				if (a8 >= RAND.SIL_TOT and cb.a8 != 255) or (a8 <= RAND.SIL_VAN and cb.a8 != 0):
					mis += 1
				if cb.a > 0.0:
					vol += 1
					if cb.r < 0.99 or cb.g < 0.99 or cb.b < 0.99:
						niet_wit += 1
		ok(a.get_size() == b.get_size() and mis == 0 and niet_wit == 0 and vol > 0,
			"silhouet %s: %s, %d punten vol, %d mis, %d niet wit, %.1f ms" % [naam, str(b.get_size()), vol, mis, niet_wit, ms])
		ok(RAND.silhouet(ct) == s, "silhouet %s één keer gemaakt (tweede keer uit de bak)" % naam)

func schaduw() -> void:
	var st := RAND.schaduw_stand("lopen", 0.0, 0.0)
	ok(st.x == 1.0 and st.y == 1.0, "lopend: volle schaduw, volle breedte")
	st = RAND.schaduw_stand("vallen", 0.1, 0.0)
	ok(st.x > 0.0 and st.x < 1.0, "net gevallen (0,1 s): schaduw vervaagt (%.2f)" % st.x)
	st = RAND.schaduw_stand("vallen", 0.2, 0.0)
	ok(st.x == 0.0, "na 0,2 s vallen: schaduw weg")
	st = RAND.schaduw_stand("lopen", 0.0, -6.0)
	ok(absf(st.x - 0.5) < 0.01 and absf(st.y - 0.7) < 0.01, "sprong 6 spelpx hoog: schaduw half zo donker, 70 procent breed")
	ok(RAND.schaduw_stand("weg", 0.0, 0.0).x == 0.0, "weg: geen schaduw")
	var img := RAND.schaduw_beeld().diffuse_texture.get_image()
	var midden := img.get_pixel(img.get_width() / 2, img.get_height() / 2).a
	var hoek := img.get_pixel(0, 0).a
	ok(midden > 0.9 and hoek == 0.0, "vlek: midden vol (%.2f), hoek leeg (%.2f): ovaal met zachte rand" % [midden, hoek])
