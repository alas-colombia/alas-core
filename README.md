# ALAS Core

ALAS Core es el motor abierto del proyecto **ALAS (Accesibilidad Lingüística Asistida con Señales)**. Incluye los componentes necesarios para traducir entre español colombiano y glosas de Lengua de Señas Colombiana (LSC), así como utilidades de integración con interfaces accesibles.

## Objetivos
- Proporcionar una base transparente y auditada por la comunidad sorda.
- Permitir contribuciones colaborativas en modelos lingüísticos, diccionarios y herramientas de validación.
- Servir como núcleo reutilizable para aplicaciones web, móviles y servicios públicos.

## Características iniciales
- Pipeline texto → gloss con reglas básicas y diccionario configurable.
- Diccionario de glosas con metadatos para sincronizar videos/avatars.
- API REST y CLI de referencia para integraciones con `alas-platform`.

## Datos externos
El diccionario oficial del INSOR requiere autorización. Consulta `docs/ingestion.md` y coordina con `alas-playbook` antes de incorporar información o recursos multimedia.

## Estado del proyecto
> **Alpha** – En fase de diseño y prototipado. El roadmap se gestiona en `docs/roadmap.md` y en el repositorio `alas-playbook`.

## Cómo participar
1. Lea el [Código de Conducta](CODE_OF_CONDUCT.md).
2. Consulte la guía de [Contribución](CONTRIBUTING.md).
3. Revise las tareas previstas en `docs/roadmap.md` y coordine con el equipo.

## Licencia
Este proyecto se distribuye bajo la licencia [MPL-2.0](LICENSE).

## Continuidad
- Consulte `AGENT.md` para conocer estado actual y próximos pasos antes de trabajar en nuevas tareas.
