#!/usr/bin/env python3
"""Regenera únicamente la tabla de catálogo dentro de README.md."""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
START = "<!-- CATALOG_TABLE_START -->"
END = "<!-- CATALOG_TABLE_END -->"

def status_label(s):
    return {
        "selected": "Seleccionado",
        "recommended": "Recomendado",
        "recommended_pilot": "Piloto recomendado",
        "specialized_candidate": "Candidato especializado",
        "internal_planned": "Starter interno",
        "infrastructure_pack": "Infraestructura/POC",
    }[s]

def main():
    data = json.loads((ROOT / "catalog.json").read_text(encoding="utf-8"))
    rows = [
        "| Estado | Opción | Uso principal | Upstream | Ficha |",
        "|---|---|---|---|---|",
    ]
    for e in data["entries"]:
        repo = f"[Repositorio]({e['repository']})" if e.get("repository") else "Por crear"
        rows.append(
            f"| {status_label(e['status'])} | "
            f"**{e['name']}** | {e['default_for']} | {repo} | [Detalle]({e['details']}) |"
        )
    readme_path = ROOT / "README.md"
    text = readme_path.read_text(encoding="utf-8")
    if START not in text or END not in text:
        raise SystemExit("README no contiene marcadores de tabla")
    before, rest = text.split(START, 1)
    _, after = rest.split(END, 1)
    readme_path.write_text(before + START + "\n" + "\n".join(rows) + "\n" + END + after, encoding="utf-8")

if __name__ == "__main__":
    main()
