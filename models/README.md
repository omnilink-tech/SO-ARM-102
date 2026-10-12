# 3D models

<!-- documentation-languages -->
[English](../docs/i18n/en/models/README.md) · [Русский](../docs/i18n/ru/models/README.md) · [Español](../docs/i18n/es/models/README.md) · [Français](../docs/i18n/fr/models/README.md) · [Deutsch](../docs/i18n/de/models/README.md) · [Português (Brasil)](../docs/i18n/pt-BR/models/README.md) · [简体中文](../docs/i18n/zh-CN/models/README.md) · [日本語](../docs/i18n/ja/models/README.md) · [हिन्दी](../docs/i18n/hi/models/README.md) · [العربية](../docs/i18n/ar/models/README.md)
<!-- /documentation-languages -->

| Folder | Content |
|---|---|
| `3mf/` | Bambu Studio projects with saved plate layouts, orientation and support settings |
| `stl/` | Print-ready meshes, binary STL, millimetres |
| `step/` | CAD sources, one solid per file |

The `stl/` and `step/` folders use the same split:

- `common/` holds the parts both arms use. The quantities in the print table cover the whole kit.
- `follower/` holds the parallel gripper, the camera mount and the follower board case.
- `leader/` holds the handle, trigger, wrist roll and the leader board case.

## 3MF slicer projects

| Project | Contents | Saved filament profile |
|---|---|---|
| [SO102_leader.3mf](3mf/SO102_leader.3mf) | One leader: arm parts, handle, trigger, wrist roll and board case | Bambu PETG-CF |
| [SO102_follower.3mf](3mf/SO102_follower.3mf) | One follower's arm parts | Fiberon PET-CF17 |
| [SO102_follower_gripper_box.3mf](3mf/SO102_follower_gripper_box.3mf) | Follower gripper, camera holder and spacer, and board case | Bambu PETG-CF |

Open these files as projects in **Bambu Studio** to retain the saved settings.
All three use the **Bambu Lab A1, 0.4 mm nozzle** profile and one **256 × 256 mm** plate each.
Select your printer, nozzle and filament before slicing. For a smaller bed, split the parts
across additional plates while preserving their orientations and support settings.

For one leader + one follower, print all three projects once. The arm projects each include
the common parts for one arm; there is no need to print a separate common set.

Saved settings and layout previews are in [docs/printing.md](../docs/printing.md#3mf-slicer-projects).

Part numbers, quantities and print settings are in [docs/printing.md](../docs/printing.md).
