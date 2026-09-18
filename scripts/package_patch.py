#!/usr/bin/env python3
"""
SoulsyHUD Compatibility Patch Packager for Skyrim 1.7.104.0
Packages ONLY the compatibility patch payload into a Vortex-ready ZIP archive:
  - SKSE/plugins/SoulsyHUD.dll
  - SKSE/plugins/SoulsyHUD.pdb
  - MCM/Config/SoulsyHUD/config.json
  - licenses/...
"""

import argparse
import os
import sys
import zipfile


def find_build_artifacts(build_dir, repo_root):
    candidate_dirs = []
    if build_dir:
        candidate_dirs.append(os.path.abspath(build_dir))
    candidate_dirs.extend([
        os.path.join(repo_root, "build", "Release"),
        os.path.join(repo_root, "build", "RelWithDebInfo"),
        os.path.join(repo_root, "build"),
    ])

    dll_path = None
    pdb_path = None

    for d in candidate_dirs:
        candidate_dll = os.path.join(d, "SoulsyHUD.dll")
        candidate_pdb = os.path.join(d, "SoulsyHUD.pdb")
        if os.path.isfile(candidate_dll) and not dll_path:
            dll_path = candidate_dll
        if os.path.isfile(candidate_pdb) and not pdb_path:
            pdb_path = candidate_pdb
        if dll_path and pdb_path:
            break

    return dll_path, pdb_path


def main():
    parser = argparse.ArgumentParser(description="Package SoulsyHUD compatibility patch archive.")
    parser.add_argument("--build-dir", default=None, help="Directory containing SoulsyHUD.dll and SoulsyHUD.pdb")
    parser.add_argument("--output-dir", default="releases", help="Output directory for the ZIP archive")
    parser.add_argument("--archive-name", default="SoulsyHUD_0.16.10_Skyrim_1.7.104.0.zip", help="Filename of the ZIP archive")
    args = parser.parse_args()

    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    
    dll_path, pdb_path = find_build_artifacts(args.build_dir, repo_root)

    if not dll_path or not os.path.isfile(dll_path):
        print(f"Error: SoulsyHUD.dll not found. Looked in provided --build-dir and default build locations.", file=sys.stderr)
        sys.exit(1)

    if not pdb_path or not os.path.isfile(pdb_path):
        print(f"Warning: SoulsyHUD.pdb not found. Debugging symbols will be omitted.", file=sys.stderr)

    config_path = os.path.join(repo_root, "installer", "core", "mcm", "config", "SoulsyHUD", "config.json")
    if not os.path.isfile(config_path):
        print(f"Error: MCM config file not found at {config_path}", file=sys.stderr)
        sys.exit(1)

    licenses_dir = os.path.join(repo_root, "packaging", "licenses")
    if not os.path.isdir(licenses_dir):
        print(f"Error: Licenses directory not found at {licenses_dir}", file=sys.stderr)
        sys.exit(1)

    out_dir = os.path.abspath(os.path.join(repo_root, args.output_dir))
    os.makedirs(out_dir, exist_ok=True)
    zip_path = os.path.join(out_dir, args.archive_name)

    print(f"Creating compatibility patch archive: {zip_path}")
    entries = []

    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        # 1. DLL
        zf.write(dll_path, "SKSE/plugins/SoulsyHUD.dll")
        entries.append("SKSE/plugins/SoulsyHUD.dll")

        # 2. PDB
        if pdb_path and os.path.isfile(pdb_path):
            zf.write(pdb_path, "SKSE/plugins/SoulsyHUD.pdb")
            entries.append("SKSE/plugins/SoulsyHUD.pdb")

        # 3. MCM Config
        zf.write(config_path, "MCM/Config/SoulsyHUD/config.json")
        entries.append("MCM/Config/SoulsyHUD/config.json")

        # 4. Licenses
        for root, dirs, files in os.walk(licenses_dir):
            dirs.sort()
            for file in sorted(files):
                full_file_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_file_path, licenses_dir)
                archive_dest = f"licenses/{rel_path}".replace("\\", "/")
                zf.write(full_file_path, archive_dest)
                entries.append(archive_dest)

    print(f"Successfully packaged {len(entries)} items into {zip_path}:")
    for entry in sorted(entries):
        print(f"  + {entry}")


if __name__ == "__main__":
    main()
