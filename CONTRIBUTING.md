# Guía de Contribución

¡Gracias por tu interés en ALAS Core! Este documento resume el flujo para proponer cambios y colaborar con el equipo.

## 1. Principios clave
- Prioriza la inclusión de la comunidad sorda y sigue las recomendaciones del Consejo Lingüístico.
- Mantén el código accesible, documentado y libre de sesgos culturales o lingüísticos.
- Respeta el [Código de Conducta](CODE_OF_CONDUCT.md).

## 2. Flujo general
1. Revisa los issues abiertos o crea uno nuevo describiendo el problema/propuesta.
2. Espera la confirmación del equipo antes de iniciar desarrollo considerable.
3. Trabaja en una rama descriptiva (`feature/gloss-normalizer`, `fix/api-typo`).
4. Asegura que las pruebas y linters locales se ejecuten correctamente.
5. Envía pull request y solicita revisión.

## 3. Estándares de código
- Python 3.11+, tipado opcional pero recomendado.
- Linters: `ruff` y `mypy` (ver `pyproject.toml`).
- Añade docstrings y comentarios breves cuando la lógica no sea evidente.

## 4. Pruebas
- Incluye pruebas unitarias cuando agregues funcionalidad nueva.
- Para conjuntos de datos o reglas lingüísticas, adjunta ejemplos de entrada/salida.
- Documenta cualquier requisito adicional (modelos, pesos) en `docs/models.md`.

## 5. Documentación
- Actualiza `docs/` con notas de diseño, API o decisiones relevantes.
- Añade entradas al changelog futuro (pendiente) siguiendo el formato Keep a Changelog.

## 6. Reporte de vulnerabilidades
Envía un correo a `seguridad@alas.org.co` (placeholder) o abre un issue privado si encuentras problemas de seguridad.

## 7. Reconocimiento
Todas las contribuciones se listarán en `docs/colaboradores.md`. Agradecemos especialmente a quienes aporten validaciones realizadas por personas sordas.
