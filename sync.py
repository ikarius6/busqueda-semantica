import numpy as np
from categories import categories, embed_model

def compute_category_embeddings(cat_list):
    """
    Computa y retorna un array de embeddings para la lista de categorías.
    """
    cat_embeddings = embed_model.encode(cat_list, convert_to_numpy=True)
    return cat_embeddings

if __name__ == "__main__":
    embeddings = compute_category_embeddings(categories)
    np.save("category_embeddings.npy", embeddings)
    print("Embeddings guardados en category_embeddings.npy")
