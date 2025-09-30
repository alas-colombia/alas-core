from __future__ import annotations

import json
from pathlib import Path

from alas_core.pipeline import translate_gloss_to_text, translate_text_to_gloss


def test_translate_text_to_gloss_maps_known_words() -> None:
    resultado = translate_text_to_gloss("Hola, ¿cómo estás tú?")
    assert resultado["gloss"] == "TU HOLA COMO ESTAR"
    assert resultado["confianza"] > 0.2
    assert resultado["contexto"] == "general"


def test_translate_text_to_gloss_marks_unknown_words() -> None:
    resultado = translate_text_to_gloss("Hola planeta desconocido")
    assert "PLANETA" in resultado["gloss"]
    assert "desconocido" in resultado["notas"]
    assert resultado["confianza"] < 0.9


def test_translate_gloss_to_text_returns_dict() -> None:
    resultado = translate_gloss_to_text("HOLA MUNDO")
    assert "texto" in resultado
    assert resultado["confianza"] == 0.1


def test_translate_text_to_gloss_from_fixtures() -> None:
    fixture_path = Path(__file__).parent / "fixtures" / "text_to_gloss.json"
    payloads = json.loads(fixture_path.read_text(encoding="utf-8"))
    for case in payloads:
        resultado = translate_text_to_gloss(case["input"])
        assert resultado["gloss"] == case["expected_gloss"], case["notes"]
        assert resultado["confianza"] >= 0.2
        assert resultado["gloss"].strip() != ""


def test_fixture_file_present() -> None:
    fixture_path = Path(__file__).parent / "fixtures" / "text_to_gloss.json"
    assert fixture_path.exists()
