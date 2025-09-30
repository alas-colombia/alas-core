"""Pipelines simulados para traducción.

Estos métodos funcionan como placeholders y deberán ser reemplazados
por implementaciones reales conforme avance el proyecto.
"""
from typing import Dict


def translate_text_to_gloss(text: str, contexto: str | None = None) -> Dict[str, object]:
    """Convierte texto en glosas de LSC (simulado).

    Args:
        text: cadena en español.
        contexto: etiqueta opcional que describe el dominio del mensaje.

    Returns:
        Diccionario con glosa y puntajes de confianza ficticios.
    """
    gloss = text.upper().replace("¿", "").replace("?", "")
    gloss = gloss.replace(",", "").replace("  ", " ")
    tokens = gloss.split()
    simulated_gloss = " ".join(tokens[:3]) if tokens else ""
    return {
        "gloss": simulated_gloss or "SIN-DATO",
        "confianza": 0.1,
        "contexto": contexto or "general",
        "notas": "Implementación temporal sin reglas lingüísticas.",
    }


def translate_gloss_to_text(gloss: str, contexto: str | None = None) -> Dict[str, object]:
    """Convierte glosas en texto español (simulado)."""
    texto = gloss.capitalize().replace("-", " ")
    return {
        "texto": texto,
        "confianza": 0.1,
        "contexto": contexto or "general",
        "notas": "Implementación temporal sin procesamiento lingüístico.",
    }
