from read_pdf import lire_pdf

def decouper_en_chunks(texte, taille_paquet=3):
    texte_propre = texte.replace("\n", " ")
    phrases = texte_propre.split(". ")
    phrases = [p.strip() for p in phrases if len(p.strip()) > 10]

    chunks = []
    for i in range(0, len(phrases), taille_paquet):
        paquet = phrases[i:i + taille_paquet]
        chunks.append(". ".join(paquet))
    return chunks