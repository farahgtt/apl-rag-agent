from pypdf import PdfReader

def lire_pdf(chemin_fichier):
    reader = PdfReader(chemin_fichier)
    texte_complet = ""
    for page in reader.pages:
        texte_complet += page.extract_text()
    return texte_complet