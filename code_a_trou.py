def recherche_dichotomique(tab, val):
    borne_min = 0
    borne_max = len(tab)
    n = 0

    while borne_min <= borne_max:
        indice_milieu = ( borne_max + borne_min) // 2
        if tab[indice_milieu] == val:
            return indice_milieu, n
        elif val < tab[indice_milieu]:
            borne_max = indice_milieu - 1
        else:
            borne_min = indice_milieu + 1
        n += 1
    return -1, n
liste = [n for n in range (0, 1000)]
print(recherche_dichotomique(liste, 1))