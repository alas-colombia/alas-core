from alas_core.pipeline import translate_text_to_gloss, translate_gloss_to_text


def test_translate_text_to_gloss_returns_dict() -> None:
    resultado = translate_text_to_gloss("Hola mundo")
    assert "gloss" in resultado
    assert resultado["contexto"] == "general"


def test_translate_gloss_to_text_returns_dict() -> None:
    resultado = translate_gloss_to_text("HOLA MUNDO")
    assert "texto" in resultado
    assert resultado["confianza"] == 0.1
