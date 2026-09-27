from read_pdf import lire_pdf
from chunks import decouper_en_chunks
from embeddings import embedder_chunks
from recherche import trouver_chunk_pertinent
from llm import demander_au_llm
from recherche import debug_scores

# --- Préparation (fait une seule fois au démarrage) ---
texte = lire_pdf("Fiche_APL.pdf")
chunks = decouper_en_chunks(texte)
vecteurs_chunks = embedder_chunks(chunks)

print(f"Document chargé : {len(chunks)} chunks prêts.\n")

# --- Boucle de questions (comme ton shell en C !) ---
while True:
    question = input("Pose ta question (ou 'exit' pour quitter) : ")
    
    if question.lower() == "exit":
        break

    # 1. Trouver le chunk le plus pertinent
    chunk_trouve = trouver_chunk_pertinent(question, chunks, vecteurs_chunks)
    
    print(f"\n[Chunk utilisé : {chunk_trouve[:80]}...]\n")
    
    # 2. Demander au LLM de répondre en se basant dessus
    reponse = demander_au_llm(question, chunk_trouve)
    
    print(f"Réponse : {reponse}\n")