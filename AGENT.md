# AGENT – ALAS Core

## Propósito
Motor abierto para traducción entre español colombiano y glosas de LSC, compartido bajo MPL-2.0.

## Estado actual
- Estructura de paquete Python (`src/alas_core`) con pipeline texto → gloss basado en reglas iniciales y diccionario configurable (`lexicon.py`).
- CLI (`src/alas_core/cli.py`) y pruebas unitarias que cubren el prototipo (`tests/test_pipeline.py`).
- Documentación en `docs/` actualizada (roadmap, arquitectura, modelos).

## Próximos pasos sugeridos
1. Ampliar el lexicón y cubrir frases frecuentes (segmentos salud, educación, trámites).
2. Diseñar métrica de evaluación rápida (ejemplos esperados en `tests/fixtures`) y ampliar test suite.
3. Elaborar guía de modelos (`docs/models.md`) con hitos para incorporar modelos neuronales.
4. Coordinar con `alas-data-gov` para acceso a corpus y alimentar iteraciones futuras.

## Referencias
- `README.md`: visión general y guía de participación.
- `docs/roadmap.md`: hitos técnicos.
- `docs/api.md`: contratos preliminares para `alas-platform`.
