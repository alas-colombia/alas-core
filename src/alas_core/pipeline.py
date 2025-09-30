"""Pipelines de traducción inicial para ALAS Core."""
from __future__ import annotations

import re
import unicodedata
from typing import Dict, Iterable, List

from .lexicon import LEXICON, PRONOUNS

WORD_PATTERN = re.compile(r"[\wÁÉÍÓÚÜÑáéíóúüñ']+", re.UNICODE)


def translate_text_to_gloss(text: str, contexto: str | None = None) -> Dict[str, object]:
    """Convierte texto español en glosas LSC usando reglas básicas."""

    tokens = _tokenize(text)
    if not tokens:
        return {
            "gloss": "SIN-DATO",
            "confianza": 0.0,
            "contexto": contexto or "general",
            "notas": "Sin contenido interpretable.",
        }

    mapped, desconocidas = _map_tokens(tokens)
    glosses = _apply_topic_comment(mapped, tokens)
    gloss = " ".join(glosses)
    confianza = _estimate_confidence(tokens, desconocidas)
    notas = (
        "Glosas generadas mediante reglas iniciales." if not desconocidas
        else "Palabras sin glosa: " + ", ".join(sorted(set(desconocidas)))
    )

    return {
        "gloss": gloss or "SIN-DATO",
        "confianza": confianza,
        "contexto": contexto or "general",
        "notas": notas,
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


def _tokenize(text: str) -> List[str]:
    lowered = text.lower()
    lowered = lowered.replace("¿", "").replace("¡", "")
    return WORD_PATTERN.findall(lowered)


def _normalize(token: str) -> str:
    return "".join(
        ch for ch in unicodedata.normalize("NFKD", token) if not unicodedata.combining(ch)
    )


def _map_tokens(tokens: Iterable[str]) -> tuple[List[str], List[str]]:
    glosses: List[str] = []
    desconocidas: List[str] = []

    for token in tokens:
        normalized = _normalize(token)
        normalized = normalized.lower()
        gloss = LEXICON.get(normalized)
        if gloss is None:
            gloss = token.upper()
            desconocidas.append(token)
        glosses.append(gloss)
    return glosses, desconocidas


def _is_topic_pronoun(token: str, normalized: str) -> bool:
    if normalized not in PRONOUNS:
        return False
    if normalized == token and normalized == "el":
        return False
    return True


def _apply_topic_comment(glosses: List[str], tokens: List[str]) -> List[str]:
    result = list(glosses)
    for idx, token in enumerate(tokens):
        normalized = _normalize(token).lower()
        if idx < len(result) and _is_topic_pronoun(token, normalized):
            if idx != 0:
                pronoun_gloss = result.pop(idx)
                result.insert(0, pronoun_gloss)
            break
    return result


def _estimate_confidence(tokens: List[str], desconocidas: List[str]) -> float:
    if not tokens:
        return 0.0
    ratio = len(desconocidas) / len(tokens)
    confidence = 0.9 - 0.5 * ratio
    return round(max(0.2, confidence), 2)
