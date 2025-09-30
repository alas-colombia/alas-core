# Ingesta del Diccionario INSOR

## Situación
- El portal histórico del diccionario (`https://www.insor.gov.co/diccionario-lsc/`) devuelve HTTP 404 (consultado el 30 de septiembre de 2025).
- No se publica licencia abierta; es necesario un acuerdo formal con el INSOR para obtener y reutilizar datos (videos, imágenes, definiciones).

## Plan propuesto
1. **Gestión institucional**: solicitar autorización escrita y dataset en formato abierto (CSV/Excel) mediante la línea de “Publicaciones” o canales de asesoría del INSOR.
2. **Conversión a JSON**: usar `scripts/convert_insor_dictionary.py` para transformar el CSV autorizado en un JSON estructurado que alimente `alas-core`.
3. **Metadatos sugeridos**: `glosa`, `descripcion`, `url_video`, `url_imagen`, `categoria`, `etiquetas`, `fuente`, `fecha_actualizacion`.
4. **Integración**: cargar el JSON generado en la signoteca (`alas-platform`) y alimentar el lexicón/base de reglas de `alas-core`.
5. **Versionamiento**: almacenar los archivos en `alas-data-gov` bajo control de acceso, documentando consentimientos y licencias.

## Ejecución del script
```bash
python scripts/convert_insor_dictionary.py \
  --input data/insor_dictionary.csv \
  --output data/insor_dictionary.json \
  --fields glosa,descripcion,url_video,url_imagen,categoria,etiquetas
```

El script valida que existan las columnas declaradas y genera un JSON con metadata básica (`fuente`, `entradas`).

## Próximos pasos
- Confirmar contacto con INSOR (ver `alas-playbook/docs/05-financiacion-y-alianzas.md`).
- Definir formato final acordado y pipeline de actualizaciones.
- Evaluar métodos para extraer etimología/variaciones regionales cuando se cuente con datos oficiales.
