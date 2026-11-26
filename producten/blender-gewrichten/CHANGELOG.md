# Changelog

Click Joints (free) for Blender. The newest version is on top.
This file feeds the GitHub release and the release notes on extensions.blender.org
(`click-joints-uitgave.yml` takes the section of the version it ships, max 1024 characters).
Write each line from the user's side, at most 5 lines per version.

## 0.1.2 (2026-11-26)

### Added
- "Report a problem" at the bottom of the Click Joints tab opens a bug report on GitHub with your Click Joints, Blender and system versions already filled in. Nothing is sent until you submit it yourself.
- After a Good fit and an export, one small line at the bottom of the panel links to the reviews on Blender Extensions. Click the link or the X and it does not ask again. No popups.

### Fixed
- On some figures, a knee joint could leave the sole of the foot as a loose piece. The foot now stays with the leg.

## 0.1.1 (2026-11-16)

### Fixed
- On a one-piece figure, a joint in one knee no longer cuts through the other leg. Only the limb at the 3D cursor is cut; the rest stays whole.
- If another part touches that limb (for example two feet joined on one base), Click Joints now refuses with a clear message instead of making a broken cut.

## 0.1.0 (2026-11-10)

First release.

### New
- Set the 3D cursor, click Place joint, and the mesh is cut into two watertight parts with a ball and socket or a pin, sized with your clearance in millimetres.
- Range of motion: every ball joint shows its measured bend in degrees before you print, and turns red where the parts would collide.
- A ring on the cut shows the fit (green good, yellow tight, red too thin), and the panel says why.
- Export as STL or 3MF, one file per part, in millimetres.
