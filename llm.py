import ollama

def demander_au_llm(question, contexte):
    prompt = f"""Réponds à la question en te basant UNIQUEMENT sur le texte suivant.
Si le texte ne contient pas la réponse, dis-le clairement.

Texte : {contexte}

Question : {question}"""

    reponse = ollama.chat(
        model="llama3.2:1b",
        messages=[{"role": "user", "content": prompt}]
    )
    return reponse["message"]["content"]