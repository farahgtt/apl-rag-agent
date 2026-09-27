from sklearn.metrics.pairwise import cosine_similarity
from embeddings import embedder_texte

def trouver_chunk_pertinent(question, chunks, vecteurs_chunks):
    """Trouve le chunk le plus proche (en sens) de la question posée."""
    
    # 1. Transformer la question en vecteur
    vecteur_question = embedder_texte(question)
    
    # 2. Comparer ce vecteur à chaque vecteur de chunk
    similarites = cosine_similarity([vecteur_question], vecteurs_chunks)[0]
    
    # 3. Trouver l'index du chunk le plus proche (score le plus haut)
    index_meilleur = similarites.argmax()
    
    return chunks[index_meilleur]

def debug_scores(question, chunks, vecteurs_chunks):
    """Affiche les scores de similarité entre la question et chaque chunk."""
    vecteur_question = embedder_texte(question)
    similarites = cosine_similarity([vecteur_question], vecteurs_chunks)[0]
    
    for i, (chunk, score) in enumerate(zip(chunks, similarites)):
        print(f"\n--- Chunk {i} (score: {score:.3f}) ---")
        print(chunk[:150])