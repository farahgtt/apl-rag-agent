from pypdf import PdfReader

# 1. Ouvrir le fichier PDF
reader = PdfReader("Fiche_APL.pdf")

# 2. Parcourir chaque page et extraire le texte
texte_complet = ""
for page in reader.pages:
    texte_complet += page.extract_text()

# 3. Afficher le résultat pour vérifier
print(texte_complet)