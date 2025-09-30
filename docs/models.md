# Modelos Planeados

| Nombre | Propósito | Estado | Notas |
|--------|-----------|--------|-------|
| `alas-text2gloss` | Traducción español → gloss LSC | MVP reglas | Transformador planeado; actualmente heurísticas y diccionario base.
| `alas-gloss2text` | Traducción gloss → español | Diseño | Seq2seq con atención.
| `alas-gesture-classifier` | Reconocimiento de señas desde video | Investigación | Basado en MediaPipe/pose estimación.

## Requisitos de entrenamiento
- Scripts y notebooks irán en `research/` (pendiente).
- Versionar datasets a través de `alas-data-gov`.
- Registrar experimentos (MLflow o similar) y publicar métricas en esta tabla.
