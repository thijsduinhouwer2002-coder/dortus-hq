# Click Joints

![Click Joints: place a ball joint on a wooden figure, bend the arm, and see the fit ring and the exploded parts](media/click-joints.gif)

**Click where it should bend, and Click Joints cuts a printable ball joint that fits, and shows how far it bends before you print.**

Free on the [Blender Extensions platform](https://extensions.blender.org/add-ons/click-joints/). Blender 4.2 LTS, 5.2 LTS and 5.3.

Want a whole figure that moves? **[Click Joints Pro](https://duinhouwer8.gumroad.com/l/click-joints-pro)** reads your rig and puts a hinge with an end stop at every elbow and knee, and a ball joint at shoulders, hips and neck. $19 once, [details below](#pro-in-addition-to-everything-above).

## Free

- Ball and socket, or pin and hole, cut into two watertight parts
- Measured bend range of every ball joint, in degrees; past the limit it turns red
- Fit ring on the cut: green good, yellow tight, red too thin
- Auto size: the largest ball with a good fit, or a clear message when none fits
- Clearance in mm (0.1 to 0.3 mm is typical)
- Exploded view, and "Make watertight" for messy meshes (on a copy)
- Export as STL or 3MF, one file per part, in millimetres

## Pro, in addition to everything above

- Figure from rig: one button reads your armature. Elbows and knees become hinges with an end stop, shoulders, hips and neck become ball joints.
- The end stop comes from Limit Rotation in your rig (30° to 150°). A side without a limit takes the other side; no limit at all gives a preset per body part.
- A degree arc and number at every joint, and a joint list with where each range came from.
- Recognises Rigify, Mixamo, Auto-Rig Pro, Unreal, Character Creator, VRoid, Biped and Daz bone names.
- No rig? Six body-part presets: place the 3D cursor and click Shoulder, Hip, Neck, Elbow, Knee or Ankle.
- Hinge with end stop and pose slider, red where parts hit past the stop, and spacing checks between joints.

Measured in Blender, not print tested by us yet: print a test joint first. Works best on figures of about 200 mm or taller with separate arms and legs, in Blender 4.5 or newer. A joint that does not fit is skipped, and the list says why. The free Click Joints and Pro can not be enabled at the same time: disable the free one first.

On Gumroad: personal license $19, studio license (up to 5 people) $59, all Pro 1.x updates included: https://duinhouwer8.gumroad.com/l/click-joints-pro

Also sold on [Superhive](https://superhivemarket.com/products/click-joints-pro), with its own price and update terms.

The free Click Joints stays free and keeps getting fixes. What changed in each version: [CHANGELOG.md](CHANGELOG.md).

## Install

Edit > Preferences > Get Extensions, search "Click Joints". Or download the zip from the releases and use Install from Disk.

Using Click Joints? A short review on [Blender Extensions](https://extensions.blender.org/add-ons/click-joints/reviews/) helps other people find it.

## Report a problem

Open an issue here: https://github.com/thijsduinhouwer2002-coder/click-joints/issues

Please include your Blender version, what you clicked, and the message the panel showed. A small .blend file helps a lot.

Email: thijs@dortus.com

## License

GPL-3.0-or-later. See [LICENSE](LICENSE).
