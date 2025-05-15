import spacy
import faiss
import numpy as np
from categories import categories, embed_model

# -----------------------------
# Configuración y carga de modelos
# -----------------------------
# 1) Cargar modelo de spaCy para lematización (por ejemplo, en inglés: en_core_web_sm)
nlp = spacy.load("es_core_news_md")

# Cargar embeddings precomputados
category_embeddings = np.load("category_embeddings.npy")

d = category_embeddings.shape[1]  # dimensión de los embeddings
n_categories = category_embeddings.shape[0]

# -----------------------------
# Indexación con FAISS
# -----------------------------
# Usamos un índice plano L2; para muchos miles de vectores, considera IVFFlat
index = faiss.IndexFlatIP(d)  # Inner Product = coseno si vectores normalizados
# Normalizamos embeddings para usar similitud coseno
faiss.normalize_L2(category_embeddings)
index.add(category_embeddings)

# -----------------------------
# Función principal: sugerir categorías
# -----------------------------
def suggest_categories(text, top_k=5, threshold=0.3):
    """
    Dado un texto libre, retorna las top_k categorías más similares
    y revisa si la similitud máxima supera el umbral.
    """
    # 1) Preprocesamiento: limpieza y lematización
    doc = nlp(text.lower())
    tokens = [token.lemma_ for token in doc if not token.is_stop and not token.is_punct]
    cleaned = " ".join(tokens)

    # 2) Generar embedding y normalizar
    q_emb = embed_model.encode([cleaned], convert_to_numpy=True)
    faiss.normalize_L2(q_emb)

    # 3) Buscar en índice
    scores, indices = index.search(q_emb, top_k)
    scores = scores[0]
    indices = indices[0]

    # 4) Mapear resultados
    results = [(categories[i], float(scores[idx])) for idx, i in enumerate(indices)]

    # 5) Validar similitud
    if results[0][1] < threshold:
        print(f"La categoría sugerida ('{results[0][0]}') tiene baja similitud ({results[0][1]:.2f}).")
        print("Considera pedir al proveedor que ajuste o aclare la descripción.")
    else:
        print("Categorías sugeridas:")
        for cat, score in results:
            print(f" - {cat} (similitud: {score:.2f})")

    return results

# -----------------------------
# Ejemplo de uso
# -----------------------------
if __name__ == "__main__":
    ejemplo = "Hacemos platillos deliciosos"
    sugerencias = suggest_categories(ejemplo)
