# Arquitectura Inicial

```
+-----------------+      +----------------------+      +------------------+
| Input Processor | ---> | Linguistic Pipeline  | ---> | Output Generator |
+-----------------+      +----------------------+      +------------------+
        |                        |                             |
        v                        v                             v
  Normalizador           Reglas + Modelo             API/CLI + Render
```

## Componentes
- **Input Processor:** limpieza de texto español (expansión de abreviaturas, análisis morfológico).
- **Linguistic Pipeline:**
  - Capa de reglas (orden tópico-comentario, marcadores no manuales).
    - La heurística de tópico prioriza pronombres explícitos pero evita mover el artículo «el»
      cuando funciona como determinante ambiguo, reduciendo el ruido en preguntas simples.
  - Modelo neuronal ligero para resolver ambigüedades léxicas.
  - Generación de gloss intermedio estándar.
- **Output Generator:**
  - Selección de recursos multimedia.
  - Generación de notación SiGML para avatar.
  - Post-procesamiento para español escrito/voz.

## Integraciones
- `alas-platform`: orquesta servicios web/móviles.
- `alas-data-gov`: provee corpus versionados y políticas de acceso.
