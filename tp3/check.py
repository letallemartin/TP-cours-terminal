def check_val_negatives(liste) :
    for i in range (len(liste)):
        if liste[i] < 0:
            return False
    return True
# code à faire

liste_test = [1,2,3,-4,6]
print(check_val_negatives(liste_test)) # doit afficher Faux
liste_test2 = [1,2,3,4,6]
print(check_val_negatives(liste_test2)) # doit afficher True