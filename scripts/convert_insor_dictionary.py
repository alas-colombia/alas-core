"""Herramienta auxiliar para convertir el diccionario de INSOR a JSON estructurado.

Uso esperado:
    python scripts/convert_insor_dictionary.py \
        --input data/insor_dictionary.csv \
        --output data/insor_dictionary.json

El script asume un CSV con cabeceras al menos: glosa, descripcion, url_video,
url_imagen, categoria, etiquetas. Los campos disponibles pueden adaptarse
mediante opciones en línea de comandos.

No incluye datos reales; requiere contar con el archivo proporcionado por INSOR
bajo autorización explícita.
"""
from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Iterable

DEFAULT_FIELDS = [
    "glosa",
    "descripcion",
    "url_video",
    "url_imagen",
    "categoria",
    "etiquetas",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Convierte diccionario INSOR a JSON")
    parser.add_argument("--input", required=True, help="Ruta del CSV original")
    parser.add_argument("--output", required=True, help="Ruta del archivo JSON destino")
    parser.add_argument(
        "--fields",
        default=",
".join(DEFAULT_FIELDS),
        help="Lista de columnas a incluir separadas por coma",
    )
    parser.add_argument(
        "--encoding",
        default="utf-8",
        help="Codificación del archivo CSV (por defecto utf-8)",
    )
    return parser.parse_args()


def load_csv(path: Path, encoding: str, fields: Iterable[str]) -> list[dict[str, str]]:
    with path.open("r", encoding=encoding, newline="") as handle:
        reader = csv.DictReader(handle)
        missing = [f for f in fields if f not in reader.fieldnames]
        if missing:
            raise ValueError(f"Columnas faltantes en CSV: {missing}")

        rows: list[dict[str, str]] = []
        for row in reader:
            cleaned = {field: (row.get(field, "") or "").strip() for field in fields}
            if cleaned[fields[0]]:
                rows.append(cleaned)
        return rows


def main() -> None:
    args = parse_args()
    input_path = Path(args.input)
    output_path = Path(args.output)
    fields = [f.strip() for f in args.fields.split(",") if f.strip()]

    if not input_path.exists():
        raise FileNotFoundError(f"Archivo CSV no encontrado: {input_path}")

    entries = load_csv(input_path, args.encoding, fields)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        json.dumps({"metadata": {"fuente": "INSOR", "entradas": len(entries)}, "items": entries},
                   ensure_ascii=False,
                   indent=2),
        encoding="utf-8",
    )
    print(f"Archivo JSON generado: {output_path} ({len(entries)} entradas)")


if __name__ == "__main__":
    main()
