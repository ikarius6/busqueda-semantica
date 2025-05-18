from sentence_transformers import SentenceTransformer

# Lista de categorías
categories = [
    "Restaurantes y comida",
    "Salud y bienestar",
    "Tecnología y software",
    "Ropa y moda",
    "Hogar y jardín",
    "Belleza y cuidado personal",
    "Deportes y actividades al aire libre",
    "Automóviles y vehículos",
    "Arte y entretenimiento",
    "Educación y formación",
    # ... más categorías
]

#  Puedes cambiar a "all-MiniLM-L6-v2" u otro según tus necesidades
#  distiluse-base-multilingual-cased-v2
#  hiiamsid/sentence_similarity_spanish_es
#  sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2
embed_model = SentenceTransformer('sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2') # all-MiniLM-L6-v2 por velocidad