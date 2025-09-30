from alas_core.pipeline import translate_text_to_gloss, translate_gloss_to_text


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
