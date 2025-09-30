# AGENT – ALAS Core

## Propósito
Motor abierto para traducción entre español colombiano y glosas de LSC, compartido bajo MPL-2.0.

## Estado actual
- Estructura de paquete Python (`src/alas_core`) con pipelines simulados.
- CLI (`src/alas_core/cli.py`) y tests básicos (`tests/test_pipeline.py`).
- Documentación en `docs/` describe roadmap, arquitectura, API y glosario.

## Próximos pasos sugeridos
1. Implementar prototipo real de `translate_text_to_gloss` usando reglas iniciales.
2. Definir set de pruebas con frases/ glosas reales y añadir fixtures.
3. Elaborar guía de modelos (`docs/models.md`) con fechas estimadas y dependencias.
4. Coordinar con `alas-data-gov` para acceso a corpus y registrar en roadmap.

## Referencias
- `README.md`: visión general y guía de participación.
- `docs/roadmap.md`: hitos técnicos.
- `docs/api.md`: contratos preliminares para `alas-platform`.
