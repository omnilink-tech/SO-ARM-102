"""Check complete translations against their English source documents."""

import argparse
import hashlib
import json
import re
from collections import Counter
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "docs/i18n"
MANIFEST = BASE / "manifest.json"
LINK = re.compile(r"\]\(([^\s)]+)\)")


def source_body(path):
    text = path.read_text(encoding="utf-8")
    text = re.sub(r"\n?<!-- documentation-languages -->.*?<!-- /documentation-languages -->\n?",
                  "", text, flags=re.S)
    return text.strip() + "\n"


def digest(path):
    return hashlib.sha256(source_body(path).encode("utf-8")).hexdigest()


def translated_body(text):
    match = re.search(r"<!-- translated-content -->\n(.*?)\n<!-- /translated-content -->", text, re.S)
    if not match:
        raise ValueError("Missing translated-content boundaries")
    return re.sub(r'<a id="[^"]+"></a>\n', "", match[1])


def structural_counts(text):
    return Counter({
        "headings": len(re.findall(r"^#{1,6} ", text, re.M)),
        "table_rows": len(re.findall(r"^\|", text, re.M)),
        "fences": len(re.findall(r"^```", text, re.M)),
        "links_and_images": len(LINK.findall(text)),
        "numbered_steps": len(re.findall(r"^\d+\. ", text, re.M)),
    })


def technical_values(text):
    # Ignore paths and URLs: localized paths differ, but their destinations are checked.
    text = LINK.sub("](LINK)", text)
    text = re.sub(r"(?<=\d)\s*[-\u2212\u2013]\s*(?=\d)", " to ", text)
    text = text.replace("+", " ")
    return Counter(re.findall(r"[-−±+]?(?:\$|€)?\d+(?:[.,]\d+)*", text))


def identifiers(text):
    text = LINK.sub("](LINK)", text)
    return Counter(re.findall(r"(?:SO102[.][0-9.*-]+|RB9[.][0-9.*-]+|STS[0-9]+|ST-[0-9]+)", text))


def check(manifest):
    errors = []
    listed = set(manifest["documents"])
    actual = {path.relative_to(ROOT).as_posix() for path in ROOT.rglob("*.md")
              if path.is_file() and not path.is_relative_to(BASE)
              and ".git" not in path.relative_to(ROOT).parts}
    if actual - listed:
        errors.append(f"Source Markdown documents not translated: {sorted(actual - listed)}")
    for source, record in manifest["documents"].items():
        original = ROOT / source
        if not original.is_file():
            errors.append(f"Missing source: {source}")
            continue
        current_hash = digest(original)
        source_text = source_body(original)
        shape = structural_counts(source_text)
        numbers = technical_values(source_text)
        parts = identifiers(source_text)
        external = Counter(url for url in LINK.findall(source_text) if urlsplit(url).scheme)
        if set(record["translations"]) != set(manifest["locales"]):
            errors.append(f"Incomplete language coverage: {source}")
        for locale, translation in record["translations"].items():
            path = ROOT / translation["path"]
            if not path.is_file():
                errors.append(f"Missing translation: {translation['path']}")
                continue
            if translation["source_sha256"] != current_hash:
                errors.append(f"Outdated translation: {locale} {source}")
            text = path.read_text(encoding="utf-8")
            try:
                body = translated_body(text)
            except ValueError as error:
                errors.append(f"{translation['path']}: {error}")
                continue
            if structural_counts(body) != shape:
                errors.append(f"Missing or altered sections/tables/steps/links: {locale} {source}; "
                              f"expected {dict(shape)}, got {dict(structural_counts(body))}")
            missing = numbers - technical_values(body)
            if missing:
                errors.append(f"Missing numerical values: {locale} {source}: {dict(missing)}")
            if identifiers(body) != parts:
                errors.append(f"Changed part identifiers: {locale} {source}")
            translated_external = Counter(url for url in LINK.findall(body) if urlsplit(url).scheme)
            if translated_external != external:
                errors.append(f"Changed external URLs: {locale} {source}")
            if re.search(r"\{\d+\}",body):
                errors.append(f"Unresolved translation token: {locale} {source}")
            expected_navigation = {(ROOT / item["path"]).resolve()
                                   for item in record["translations"].values()}
            destinations = set()
            for href in LINK.findall(text):
                url = urlsplit(href)
                if url.scheme or url.netloc:
                    continue
                dest = (path.parent / unquote(url.path)).resolve() if url.path else path.resolve()
                destinations.add(dest)
                if not dest.is_relative_to(ROOT) or not dest.exists():
                    errors.append(f"Broken local link: {translation['path']}: {href}")
                    continue
                if dest.suffix == ".md" and url.fragment:
                    target_text = dest.read_text(encoding="utf-8")
                    if f'id="{unquote(url.fragment)}"' not in target_text:
                        errors.append(f"Missing explicit anchor: {translation['path']}: {href}")
            if not expected_navigation.issubset(destinations):
                errors.append(f"Incomplete equivalent-page language navigation: {locale} {source}")
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--record-reviewed", action="store_true")
    parser.add_argument("--locale")
    parser.add_argument("--source")
    args = parser.parse_args()
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    if args.record_reviewed:
        if not args.locale or not args.source:
            parser.error("--record-reviewed requires --locale and --source after reviewing that translation")
        record = manifest["documents"][args.source]
        record["translations"][args.locale]["source_sha256"] = digest(ROOT / args.source)
        MANIFEST.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
                            encoding="utf-8", newline="\n")
    errors = check(manifest)
    if errors:
        print("\n".join(errors))
        return 1
    count = sum(len(item["translations"]) for item in manifest["documents"].values())
    print(f"OK: {count} complete documents, {len(manifest['locales'])} languages; "
          "source versions, structure, technical values, identifiers, links and anchors passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
