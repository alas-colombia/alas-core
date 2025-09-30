# API de Referencia (Borrador)

## `POST /v1/translate/text-to-gloss`
- **body**
  ```json
  {
    "text": "Hola, ¿cómo estás?",
    "dialecto": "es-CO",
    "contexto": "informal"
  }
  ```
- **respuesta**
  ```json
  {
    "gloss": "HOLA COMO-ESTAR",
    "confianza": 0.82,
    "recomendaciones": ["Agregar gesto de saludo con sonrisa"]
  }
  ```

## `POST /v1/translate/gloss-to-text`
- Similar estructura; devuelve texto legible y notas culturales.

## `GET /v1/dictionary/{gloss}`
- Retorna metadatos, video/avatar y ejemplos de uso.

> Los endpoints definitivos se publicarán cuando se consolide la arquitectura de `alas-platform`.
