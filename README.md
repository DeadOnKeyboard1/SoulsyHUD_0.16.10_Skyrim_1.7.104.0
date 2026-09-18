# SoulsyHUD - Skyrim 1.7.104.0 Compatibility Patch

An unofficial compatibility update and native SKSE plugin port of **SoulsyHUD** for **The Elder Scrolls V: Skyrim Special Edition / Anniversary Edition runtime 1.7.104.0** (SKSE 2.3.1).

This repository contains the source code and build files for the Skyrim 1.7.104.0 compatibility patch. All original mod content, design, and implementation belong to the original author, **[ceejbot](https://github.com/ceejbot)**.

- **Original Mod on NexusMods:** [SoulsyHUD by ceejbot](https://www.nexusmods.com/skyrimspecialedition/mods/96210/)
- **Upstream Repository:** [ceejbot/soulsy](https://github.com/ceejbot/soulsy)
- **Original License:** GNU General Public License v3.0 ([LICENSE](./LICENSE))

---

## What This Patch Does

1. **Skyrim 1.7.104.0 Runtime Support (SKSE 2.3.1):**
   - Recompiled native plugin DLL with CommonLibSSE-NG (`alandtse/CommonLibVR`, branch `ng`, commit `1504349dddfc622d4d25704bba19e2ade669dc5a`).
   - Verified Address Library ID relocations and hook call-sites for runtime 1.7.104.0.
   - Preserves backward compatibility with previously supported game versions (1.5.97, 1.6.640, 1.6.1130, 1.6.1170) via CommonLibSSE-NG dynamic runtime dispatch.

2. **MCM Keybinding Improvements:**
   - Added `ignoreConflicts: true` to all 13 keymap controls in `config.json`. This allows binding any desired keys (including standard vanilla action keys, number keys 1–8, mouse buttons, and modifier keys like Shift, Ctrl, Alt) without SkyUI conflict blocking.

3. **Settings Parser Enhancements:**
   - Improved `FromIniStr` parser in Rust to support unmapped/cleared keys (`-1` -> unassigned) and hex codes, preventing unassigned hotkeys from silently reverting to defaults.
   - Robust configuration fallback loading: loads base defaults from `Config/SoulsyHUD/settings.ini` and overlays user customizations from `Settings/SoulsyHUD.ini`.

4. **Modern Toolchain Compatibility:**
   - Updated Rust `time` dependency to 0.3.44.
   - Updated C++23 / MSVC compiler compatibility (DirectX buffer casts, sound handle API modernization, and `__cdecl` SKSEAPI trampolines).

---

## Installation

This patch is an overwrite patch for the original mod:

1. Install the main **[SoulsyHUD](https://www.nexusmods.com/skyrimspecialedition/mods/96210/)** mod via your mod manager (Vortex or Mod Organizer 2).
2. Install the **[Skyrim 1.7.104.0 Compatibility Patch](https://github.com/DeadOnKeyboard1/SoulsyHUD_0.16.10_Skyrim_1.7.104.0/releases)**.
3. Ensure the patch loads **after / overwrites** the original mod files (`SoulsyHUD.dll`, `SoulsyHUD.pdb`, and `config.json`).

---

## Building from Source

### Prerequisites
- [Rust](https://rustup.rs) (MSVC toolchain for Windows)
- [Visual Studio 2022](https://visualstudio.microsoft.com) with Desktop development with C++ (v143 toolset)
- [CMake](https://cmake.org) (3.22+)
- [vcpkg](https://github.com/microsoft/vcpkg) with `VCPKG_ROOT` set in your environment

### Dependencies
- `spdlog`, `imgui` (installed via vcpkg automatically)
- `CommonLibSSE-NG` (pulled as a git submodule in `extern/CommonLibSSE-NG`)

### Build Steps
```powershell
# Clone the repository with submodules
git clone --recursive https://github.com/DeadOnKeyboard1/SoulsyHUD_0.16.10_Skyrim_1.7.104.0.git
cd SoulsyHUD_0.16.10_Skyrim_1.7.104.0

# Configure using the CMake preset
cmake --preset vs2022-windows

# Build Release DLL and PDB
cmake --build --preset vs2022-windows --config Release
```

The compiled `SoulsyHUD.dll` and `SoulsyHUD.pdb` will be placed in `build/Release/`.

---

## Credits & Attribution

All credit for the original SoulsyHUD mod belongs to **ceejbot** and the upstream contributors:
- **[ceejbot](https://github.com/ceejbot)** – Creator and lead developer of SoulsyHUD.
- **[mlthelama](https://github.com/mlthelama)** – Author of [LamasTinyHUD](https://www.nexusmods.com/skyrimspecialedition/mods/82545), from which Soulsy originally diverged.
- **[MinhazMurks](https://www.nexusmods.com/skyrimspecialedition/users/26341279)** – Untarnished UI skin inspiration.
- **psychosteve** – SkyUI icons.
- **Maxicons** – Role Playing Game collection icons (Noun Project).
- **THICC Team** – Icons from the [THICC icon mod](https://www.nexusmods.com/skyrimspecialedition/mods/90508).
- **Rasmus Andersson** – [Inter](https://rsms.me/inter/) font.
- **CharmedBaryon / alandtse** – CommonLibSSE / CommonLibSSE-NG.

---

## License

This project is licensed under the **GNU General Public License v3.0** ([LICENSE](./LICENSE)), preserving the original licensing of SoulsyHUD.  
For third-party component licenses, see [THIRD_PARTY_NOTICES.md](./THIRD_PARTY_NOTICES.md).
