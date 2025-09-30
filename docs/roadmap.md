# Roadmap Técnico ALAS Core

## Etapa Alpha (0-3 meses)
- Definir contrato de datos de entrada (tokenización, normalización). ✅ Implementado en el prototipo de reglas.
- Implementar prototipo texto → gloss con reglas y transformer DistilBERT fine-tuned. ✅ Primera versión rule-based lista (septiembre 2025).
- Diseñar API REST minimal (`/translate/text-to-gloss`).
- Preparar set de pruebas unitarias con frases comunes.

## Etapa Beta (3-9 meses)
- Añadir pipeline gloss → texto con post-procesamiento gramatical.
- Integrar módulo de selección de videos/avatars basado en glosa.
- Incluir soporte de retroalimentación del usuario en la API.
- Publicar documentación de despliegue (Docker, ONNX/TF Lite).

## Etapa Release (9+ meses)
- Versionado semántico y paquetes oficiales.
- Instrumentación de métricas de calidad (BLEU adaptado, evaluaciones humanas).
- Compatibilidad con SDK (`alas-platform`).
