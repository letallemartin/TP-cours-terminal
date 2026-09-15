def super_fonction(a:list)-> int :
    """ Cette fonction retourne le minimum d'une liste
    entrée : une liste
    sortie : une valeur minimum
    """
    m = a[0]
    n = len(a)
    for i in range(n): # on parcourt tous les indices de la liste
        if a[i] < m :# si l'élément courant est plus petit que m
            m = a[i]# on initialise m avec le premier élément de la liste
    return m