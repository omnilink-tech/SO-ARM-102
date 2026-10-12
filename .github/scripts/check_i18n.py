"""Check document-guide coverage, local links and reviewed source versions."""

import argparse
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "docs/i18n"
MANIFEST = BASE / "manifest.json"


def source_hash(path):
    content = path.read_bytes()
    if path.suffix.lower() != ".pdf":
        content = content.replace(b"\r\n", b"\n")
    return hashlib.sha256(content).hexdigest()


def documents():
    return {
        path.relative_to(ROOT).as_posix()
        for path in ROOT.rglob("*")
        if path.is_file()
        and ".git" not in path.relative_to(ROOT).parts
        and not path.is_relative_to(BASE)
        and (path.suffix.lower() in {".md", ".pdf", ".txt"}
             or path.name in {"NOTICE", "REUSE.toml"})
    }


def check(manifest):
    errors = []
    sources = set(manifest["sources"])
    actual = documents()
    for path in sorted(actual - sources):
        errors.append(f"Document not described in manifest: {path}")
    for path in sorted(sources - actual):
        errors.append(f"Source document missing: {path}")
    for path in sorted(sources & actual):
        if source_hash(ROOT / path) != manifest["sources"][path]:
            errors.append(f"Review all language descriptions after source change: {path}")

    guides = [BASE / locale / "README.md" for locale in manifest["locales"]]
    navigation_targets = {guide.resolve() for guide in guides}
    for guide in [ROOT / "README.md", BASE / "README.md", *guides]:
        if not guide.is_file():
            errors.append(f"Missing guide: {guide.relative_to(ROOT)}")
            continue
        text = guide.read_text(encoding="utf-8")
        targets = set()
        for match in re.finditer(r"!?\[[^\]\n]*\]\(([^\s)]+)\)", text):
            url = urlsplit(match.group(1))
            if url.scheme or url.netloc or not url.path:
                continue
            target = (guide.parent / unquote(url.path)).resolve()
            if not target.is_relative_to(ROOT):
                errors.append(f"Link leaves repository in {guide.relative_to(ROOT)}: {url.path}")
            elif not target.exists():
                errors.append(f"Broken link in {guide.relative_to(ROOT)}: {url.path}")
            targets.add(target)
        if not navigation_targets.issubset(targets):
            errors.append(f"Incomplete language navigation: {guide.relative_to(ROOT)}")
        if guide in guides:
            if not {(ROOT / path).resolve() for path in sources}.issubset(targets):
                errors.append(f"Incomplete document coverage: {guide.relative_to(ROOT)}")
            # One table row per source: a linked filename and a non-empty description.
            rows = re.findall(r"^\| \[`([^`]+)`\]\([^)]+\) \| (.+) \|$", text, re.M)
            if len(rows) != len(sources) or {row[0] for row in rows} != sources:
                errors.append(f"Missing or duplicate descriptions: {guide.relative_to(ROOT)}")
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--refresh-source-hashes", action="store_true",
                        help="Record source versions after reviewing every affected language description")
    args = parser.parse_args()
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    if args.refresh_source_hashes:
        # New sources require descriptions in every guide before this command is run.
        manifest["sources"] = {path: source_hash(ROOT / path) for path in sorted(documents())}
        MANIFEST.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
                            encoding="utf-8", newline="\n")
    errors = check(manifest)
    if errors:
        print("\n".join(errors))
        return 1
    print(f"OK: {len(manifest['sources'])} documents, {len(manifest['locales'])} language guides; "
          "source hashes, coverage and local links passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
