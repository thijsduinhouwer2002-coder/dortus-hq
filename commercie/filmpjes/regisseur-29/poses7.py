"""Kandidaat-poses voor v7b (keuring Daan #217 M3: één open pose die laat zien dat knie en elleboog echt buigen,
zonder botsing, gelijk in de weergave en de Cycles-film). Kogels: lijst van (as in wereld, graden), in volgorde
toegepast om het kogelmidden; schouders en heupen binnen het bereik van Pro, draaien om de lengteas mag altijd.
Scharnieren: graden buigen. De robot kijkt naar -Y; zijn links is +X."""

BENEN_STAP = {
    "Left hip": [((1, 0, 0), -16.0), ((0, 1, 0), -6.0)], "Left knee": 34.0,
    "Right hip": [((1, 0, 0), 8.0), ((0, 1, 0), 8.0)], "Right knee": 8.0,
}
BENEN_BREED = {
    "Left hip": [((0, 1, 0), -10.0)], "Left knee": 22.0,
    "Right hip": [((0, 1, 0), 10.0)], "Right knee": 6.0,
}

LOOP = {   # midden in een stap: voorste been recht, achterste knie duidelijk gebogen (hiel los)
    "Left hip": [((1, 0, 0), -14.0), ((0, 1, 0), -4.0)], "Left knee": 6.0,
    "Right hip": [((1, 0, 0), 18.0), ((0, 1, 0), 5.0)], "Right knee": 48.0,
}
LOOP_L = {   # zelfde, linkerknie achter
    "Right hip": [((1, 0, 0), -14.0), ((0, 1, 0), 4.0)], "Right knee": 6.0,
    "Left hip": [((1, 0, 0), 18.0), ((0, 1, 0), -5.0)], "Left knee": 48.0,
}
ZWAAI_R = {"Right shoulder": [((0, 0, 1), -90.0), ((0, 1, 0), 30.0)], "Right elbow": 135.0}
ZIJ_L = {"Left shoulder": [((0, 0, 1), -90.0), ((0, 1, 0), -30.0)], "Left elbow": 100.0}
LOS_L = {"Left shoulder": [((0, 1, 0), -14.0), ((1, 0, 0), 10.0)], "Left elbow": 25.0}
VOOR_L = {"Left shoulder": [((0, 1, 0), -16.0), ((1, 0, 0), -22.0)], "Left elbow": 60.0}   # onderarm naar voren, opzij van het lijf
ACHTER_L = {"Left shoulder": [((0, 1, 0), -12.0), ((1, 0, 0), 24.0)], "Left elbow": 40.0}  # zwaait mee naar achter
HOOFD = {"Neck": [((0, 0, 1), -18.0), ((0, 1, 0), 8.0)]}

POSES = {
    "a_zwaai_zij_loop": {**LOOP, **ZWAAI_R, **ZIJ_L, **HOOFD},
    "b_zwaai_zij_loopL": {**LOOP_L, **ZWAAI_R, **ZIJ_L, **HOOFD},
    "c_zwaai_los_loop": {**LOOP, **ZWAAI_R, **LOS_L, **HOOFD},
    "d_zwaai_zij_breed": {**BENEN_BREED, **ZWAAI_R, **ZIJ_L, **HOOFD},
    # proef 26 nov: 0 botsingen, maar in de weergave (camera aan de +X-kant) wijst de vuist naar de camera, voor de buik
    "e_zwaai_voor_loop": {**LOOP, **ZWAAI_R, **VOOR_L, "Neck": [((0, 0, 1), 12.0), ((0, 1, 0), 8.0)]},
    "f_zwaai_achter_loop": {**LOOP, **ZWAAI_R, **ACHTER_L, **HOOFD},
    # gekozen voor v7b: linkerarm zwaait mee naar achter (niets voor het lijf), hoofd iets naar de camera (+X-kant)
    "g_zwaai_achter_loop": {**LOOP, **ZWAAI_R, "Left shoulder": [((0, 1, 0), -14.0), ((1, 0, 0), 26.0)],
                            "Left elbow": 55.0, "Neck": [((0, 0, 1), 12.0), ((0, 1, 0), 8.0)]},
}
