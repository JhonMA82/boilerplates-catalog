#!/usr/bin/env python3
from __future__ import annotations
import json
import re
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "catalog.json"

ALLOWED = {
    "selected",
    "recommended",
    "recommended_pilot",
    "specialized_candidate",
    "internal_planned",
    "infrastructure_pack",
}

def fail(msg: str) -> None:
    raise SystemExit(f"ERROR: {msg}")

def markdown_links(text: str):
    return re.findall(r"\[[^\]]+\]\(([^)]+)\)", text)

def main() -> None:
    data = json.loads(CATALOG.read_text(encoding="utf-8"))
    entries = data.get("entries")
    if not entries:
        fail("catalog.json no contiene entries")

    ids = set()
    details = set()
    for entry in entries:
        for field in ("id", "name", "kind", "origin", "status", "category", "default_for", "details", "summary"):
            if field not in entry:
                fail(f"{entry.get('id', '?')}: falta {field}")
        if entry["id"] in ids:
            fail(f"id duplicado: {entry['id']}")
        ids.add(entry["id"])
        if entry["status"] not in ALLOWED:
            fail(f"{entry['id']}: estado inválido")
        if entry["details"] in details:
            fail(f"detalle duplicado: {entry['details']}")
        details.add(entry["details"])
        if not (ROOT / entry["details"]).exists():
            fail(f"{entry['id']}: falta {entry['details']}")
        repo = entry.get("repository")
        if repo:
            parsed = urlparse(repo)
            if parsed.scheme != "https" or not parsed.netloc:
                fail(f"{entry['id']}: URL inválida")
        elif entry["status"] != "internal_planned":
            fail(f"{entry['id']}: solo starters internos pueden omitir repository")

    # Verify relative Markdown links throughout repository.
    for md in ROOT.rglob("*.md"):
        text = md.read_text(encoding="utf-8")
        for target in markdown_links(text):
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            clean = target.split("#", 1)[0]
            if not clean:
                continue
            resolved = (md.parent / clean).resolve()
            try:
                resolved.relative_to(ROOT.resolve())
            except ValueError:
                fail(f"{md.relative_to(ROOT)}: enlace fuera del repo: {target}")
            if not resolved.exists():
                fail(f"{md.relative_to(ROOT)}: enlace roto: {target}")

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    for entry in entries:
        if entry["details"] not in readme:
            fail(f"README no enlaza {entry['id']}")

    coverage = (ROOT / "docs/strategy/coverage-map.md").read_text(encoding="utf-8")
    required_terms = [
        "TanStack", "Next", "SpeedPy", "FastAPI", "Open SaaS",
        "GoShip", "Institutional Operations", "AI Assistant",
        "Self-hosted", "forks", "AI-friendly",
    ]
    for term in required_terms:
        if term not in coverage:
            fail(f"coverage-map no menciona: {term}")

    print(f"OK: {len(entries)} entradas, enlaces relativos válidos y cobertura mínima completa.")

if __name__ == "__main__":
    main()
