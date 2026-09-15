def fonction(tab, val):
    debut = 0
    fin = len(tab) - 1
    while  debut <= fin:
        milieu = (debut + fin) //2
        val_milieu = tab[milieu]
        
        if val == val_milieu:
            return True
        if val < val_milieu:
            fin = milieu - 1
            
        if val > val_milieu:
            debut = milieu + 1
        return False

tab = [n for n in range (0, 1000)]