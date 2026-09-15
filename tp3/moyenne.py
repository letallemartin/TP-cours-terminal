def moyenne(liste):
    """entré: liste(int)
        sortie: int or float
        renvoie la moyenne des nb de la liste"""
    total = 0
    for i in range(len(liste)):
        total += liste[i]
    return total / len(liste) #total diviser par le nb d'élément