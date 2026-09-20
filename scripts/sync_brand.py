#!/usr/bin/env python3
"""Vendor the organisation-facing brand assets from absolute-power-brand.

absolute-power-brand is the single source of truth for colour, type and marks,
and it is private. This repository has to be public — GitHub only honours a
profile page and default community health files from a public `.github` repo,
including for the private repositories that inherit them. So the brand cannot be
a dependency here; it is vendored, and vendoring is done by this script rather
than by hand so that what landed is always traceable to a commit.

This is deliberately the same mechanism absolute-game-servers uses, down to the
SOURCE.json format, rather than a third way of doing the same thing.

brand/SOURCE.json records the upstream commit and a SHA-256 for every vendored
file. `--check` re-hashes them, which is what CI runs: it cannot prove the
vendored copy is current (that needs the private repo), but it does prove nobody
edited the vendored copy locally, which is the drift that actually happens.

Usage:
    sync_brand.py                       vendor from the default branch
    sync_brand.py --ref <branch|sha>    vendor from a specific ref
    sync_brand.py --check               re-hash only; no network, no writes
"""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VENDOR = ROOT / "brand"
SOURCE = VENDOR / "SOURCE.json"
REPO = "https://github.com/abspwgm/absolute-power-brand.git"

# upstream path -> vendored path. Deliberately narrow: the marks that represent
# the organisation itself. docs/BRAND_GUIDELINES.md is *not* vendored — this
# repository is public and the guidelines are internal brand strategy, so they
# stay upstream and are cited by path.
FILES = {
    "logos/ap-org-avatar.svg": "logos/ap-org-avatar.svg",
    "logos/ap-social-preview.svg": "logos/ap-social-preview.svg",
    "logos/ap-tcgaming-lockup.svg": "logos/ap-tcgaming-lockup.svg",
    "logos/ap-gameservers-lockup.svg": "logos/ap-gameservers-lockup.svg",
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def check() -> int:
    if not SOURCE.exists():
        print(f"error: {SOURCE.relative_to(ROOT)} is missing; run sync_brand.py", file=sys.stderr)
        return 1
    recorded = json.loads(SOURCE.read_text(encoding="utf-8"))["files"]
    problems: list[str] = []
    for name, want in sorted(recorded.items()):
        path = VENDOR / name
        if not path.exists():
            problems.append(f"{name}: vendored file is missing")
        elif digest(path) != want:
            problems.append(f"{name}: edited in place (hash does not match SOURCE.json)")
    for path in sorted(p for p in VENDOR.rglob("*") if p.is_file()):
        name = path.relative_to(VENDOR).as_posix()
        if name not in recorded and name not in {"SOURCE.json", "README.md"}:
            problems.append(f"{name}: untracked file in brand/; add it to sync_brand.py or delete it")
    for problem in problems:
        print(f"brand drift: {problem}", file=sys.stderr)
    if problems:
        print(
            "\nbrand/ is vendored output. Change tokens in absolute-power-brand, then\n"
            "re-run: python3 scripts/sync_brand.py",
            file=sys.stderr,
        )
        return 1
    print(f"brand/ matches SOURCE.json ({len(recorded)} files, upstream "
          f"{json.loads(SOURCE.read_text(encoding='utf-8'))['commit'][:12]})")
    return 0


def sync(ref: str) -> int:
    with tempfile.TemporaryDirectory() as tmp:
        clone = Path(tmp) / "brand"
        print(f"cloning {REPO} @ {ref} ...")
        result = subprocess.run(
            ["git", "clone", "--quiet", "--depth", "1", "--branch", ref, REPO, str(clone)],
            capture_output=True,
            text=True,
        )
        if result.returncode:  # --branch rejects a bare sha; fall back to a full clone.
            subprocess.run(["git", "clone", "--quiet", REPO, str(clone)], check=True)
            subprocess.run(["git", "-C", str(clone), "checkout", "--quiet", ref], check=True)
        commit = subprocess.run(
            ["git", "-C", str(clone), "rev-parse", "HEAD"],
            check=True, capture_output=True, text=True,
        ).stdout.strip()

        files: dict[str, str] = {}
        for upstream, vendored in FILES.items():
            src = clone / upstream
            if not src.exists():
                sys.exit(f"error: {upstream} is not in absolute-power-brand @ {ref}")
            dest = VENDOR / vendored
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(src, dest)
            files[vendored] = digest(dest)
            print(f"  {upstream} -> brand/{vendored}")

    SOURCE.write_text(
        json.dumps(
            {
                "repo": REPO,
                "ref": ref,
                "commit": commit,
                "synced": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
                "files": dict(sorted(files.items())),
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    print(f"wrote {SOURCE.relative_to(ROOT)} at upstream {commit[:12]}")
    return 0


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--ref", default="main", help="branch, tag or commit in absolute-power-brand")
    parser.add_argument("--check", action="store_true", help="verify the vendored copy; no network")
    args = parser.parse_args()
    sys.exit(check() if args.check else sync(args.ref))


if __name__ == "__main__":
    main()
