books = []

def ajouter_livre(titre, auteur):
    livre = {
        "titre": titre,
        "auteur": auteur,
        "disponible": True
    }
    books.append(livre)
    return livre

def lister_livres():
    return books

def rechercher_livre(titre):
    for livre in books:
        if livre["titre"].lower() == titre.lower():
            return livre
    return None
