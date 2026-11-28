# Click Joints Pro 1.2.10: releasenote (Bram, 28 nov 2026) CONCEPT

**Uitbrengen niet vóór 1.2.9 live staat (ma 30 nov) en de tak `claude/blender-306` op main zit.** Tak `claude/blender-410`.

## Releasenote 1.2.10 (Engels, Gumroad en Superhive), concept
```
Click Joints Pro 1.2.10
- Shoulder, Hip and Neck now work right after Shift + right click on the surface: the ball joint moves to the middle of the limb and turns along the limb, so the arm or leg comes off as its own part. Before, this said "Too thin here for a ball joint".
- Tested on Blender 4.2 LTS, 5.2 LTS and 5.3.
```
Bewijs: toets `e2e/toetsen_kogel_huid.py`; kopersreis van Iris nagedaan (issue 410). Regels over gratis 0.1.3 (tenen, #306) komen erbij bij het samenvoegen.
