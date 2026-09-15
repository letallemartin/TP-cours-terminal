def caisse(liste):
    """
    entré: liste(int): nombre - et + int
    sortie: liste(int)

    """
    for i in range(len(liste)):#parcour les indice de la liste 
        if liste[i] < 0:#si la valeur a l'indice i est négative
            liste.pop(i) #enleve la valeur 
    return liste

print(caisse([2 , -6]))