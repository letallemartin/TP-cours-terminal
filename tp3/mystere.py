def mystere(liste, b) :
    """""
    créer une liste et y ajoute tt
    les valeur b presente dans 
    la liste en parametre
    """""
    resultat = []
    for i in range(0, len(liste)) :
        if liste[i] == b :
            resultat.append(liste[i])
    return resultat