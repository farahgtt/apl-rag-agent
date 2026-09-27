from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

def embedder_chunks(chunks):
    """Prend une liste de textes (chunks), retourne une liste de vecteurs correspondants."""
    vecteurs = model.encode(chunks)
    return vecteurs

def embedder_texte(texte):
    """Transforme un seul texte (ex: la question posée) en vecteur."""
    return model.encode(texte)