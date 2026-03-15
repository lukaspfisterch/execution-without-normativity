from __future__ import annotations

from datetime import datetime
from pathlib import Path
import shutil
import zipfile


ROOT = Path(__file__).resolve().parents[1]
PAPER = ROOT / "paper"
DIST = ROOT / "dist" / "arxiv"
SECTIONS = PAPER / "sections"

REQUIRED_FILES = [
    PAPER / "main.tex",
    PAPER / "refs.bib",
]

OPTIONAL_FILES = [
    PAPER / "main.bbl",
]


def _assert_inputs() -> None:
    missing = [path for path in REQUIRED_FILES if not path.exists()]
    if missing:
        names = ", ".join(path.relative_to(ROOT).as_posix() for path in missing)
        raise SystemExit(f"Missing required arXiv source files: {names}")
    if not SECTIONS.exists():
        raise SystemExit("Missing required directory: paper/sections")


def _copy_tree(src: Path, dst: Path) -> None:
    dst.mkdir(parents=True, exist_ok=True)
    for path in sorted(src.rglob("*")):
        if path.is_dir():
            continue
        rel = path.relative_to(src)
        target = dst / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, target)


def build_bundle() -> Path:
    _assert_inputs()

    timestamp = datetime.now().strftime("%Y%m%d")
    stage_dir = DIST / f"execution-without-normativity-arxiv-{timestamp}"
    zip_path = DIST / f"{stage_dir.name}.zip"

    if stage_dir.exists():
        shutil.rmtree(stage_dir)
    if zip_path.exists():
        zip_path.unlink()

    stage_dir.mkdir(parents=True, exist_ok=True)

    shutil.copy2(PAPER / "main.tex", stage_dir / "main.tex")
    shutil.copy2(PAPER / "refs.bib", stage_dir / "refs.bib")

    for optional in OPTIONAL_FILES:
        if optional.exists():
            shutil.copy2(optional, stage_dir / optional.name)

    _copy_tree(SECTIONS, stage_dir / "sections")

    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for path in sorted(stage_dir.rglob("*")):
            if path.is_dir():
                continue
            zf.write(path, path.relative_to(stage_dir).as_posix())

    return zip_path


def main() -> None:
    zip_path = build_bundle()
    print(f"Wrote {zip_path}")


if __name__ == "__main__":
    main()
