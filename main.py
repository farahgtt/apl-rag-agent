from read_pdf import lire_pdf
from chunks import decouper_en_chunks
from embeddings import embedder_chunks

# 1. Lire le PDF
texte = lire_pdf("Fiche_APL.pdf")

# 2. Découper en chunks
chunks = decouper_en_chunks(texte)

# 3. Générer un vecteur pour chaque chunk
vecteurs_chunks = embedder_chunks(chunks)

print(f"{len(chunks)} chunks transformés en vecteurs")
print(f"Chaque vecteur fait {len(vecteurs_chunks[0])} nombres de long")