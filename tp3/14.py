def nb_minimal(a:list)-> int :
    """ Cette fonction retourne le minimum d'une liste
    entrée : une liste
    sortie : une valeur minimum
    """
    min = a[0]
    longueur = len(a)
    for i in range(longueur):
        if a[i] < min :
            min = a[i]
    return min

nombre_note = 3
sommeNotes = 0
âge = 15