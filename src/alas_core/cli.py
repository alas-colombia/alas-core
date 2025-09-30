"""CLI de referencia para utilizar ALAS Core."""
import json
import typer

from .pipeline import translate_gloss_to_text, translate_text_to_gloss

app = typer.Typer(help="Herramientas de traducción ALAS Core")


@app.command()
def texto_a_gloss(texto: str, contexto: str = "general") -> None:
    """Convierte `texto` en glosa de LSC (salida JSON)."""
    resultado = translate_text_to_gloss(texto, contexto=contexto)
    typer.echo(json.dumps(resultado, ensure_ascii=False, indent=2))


@app.command()
def gloss_a_texto(gloss: str, contexto: str = "general") -> None:
    """Convierte `gloss` en texto español (salida JSON)."""
    resultado = translate_gloss_to_text(gloss, contexto=contexto)
    typer.echo(json.dumps(resultado, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    app()
