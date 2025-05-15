# Busqueda semántica con spaCy y FAISS

Este proyecto es una aplicación de búsqueda semántica que utiliza el modelo de lenguaje [spaCy](https://spacy.io/) para el procesamiento del texto y el índice de [FAISS](https://github.com/facebookresearch/faiss) para la búsqueda. La aplicación también utiliza [SentenceTransformers](https://www.sbert.net/) para generar vectores de embeddings de las categorías.

## Requisitos

- Python 3.10
- spaCy
- SentenceTransformers
- FAISS
- Numpy

## Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/pablomarin/semantic_search.git
```

2. Crea un entorno virtual:

```bash
python -m venv myenv
```

3. Activa el entorno virtual:

```bash
myenv\Scripts\activate
```

4. Instala las dependencias:

```bash
pip install -r requirements.txt
```

5. Descarga el modelo de spacy:

```bash
python -m spacy download es_core_news_md
```

6. Ejecuta el script de sincronización de embeddings:

```bash
python sync.py
```

7. Ejecuta el script principal:

```bash
python main.py
```

## Ejemplo de uso

```python
>>> from main import suggest_categories
>>> suggest_categories("Hacemos platillos deliciosos")
Categorías sugeridas:
 - Restaurantes y comida (similitud: 0.50)
 - Salud y bienestar (similitud: 0.20)
 - Tecnología y software (similitud: 0.20)
 - Ropa y moda (similitud: 0.10)
 - Hogar y jardín (similitud: 0.10)
 ```

## Licencia

Este proyecto está bajo la licencia MIT.

## Autor

[Mr.Jack] (https://github.com/ikarius6)