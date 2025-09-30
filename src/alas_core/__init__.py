"""Paquete principal de ALAS Core.

Este módulo expone las interfaces para traducir entre español y glosas de LSC.
Actualmente se incluye una implementación simulada para facilitar pruebas.
"""

from .pipeline import translate_text_to_gloss, translate_gloss_to_text  # noqa: F401
