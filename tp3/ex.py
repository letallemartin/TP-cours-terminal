import random
def nb_moi():
    liste = []
    for i in range (5):
        while True:
            try:
                x = int(input("1-49"))
            except ValueError:
                print("type inccorect")
            if x < 1 or x > 49 or x in liste:
                print("hors limites")
            else:
                liste.append(x)
                break
    return (liste)

def nb_loterie():
    liste_tir = []
    for i in range (5):
        x = random.randint(1, 49)
        liste_tir.append(x)
    return (liste_tir)

def tirage(liste1, liste2):
    nb = 0
    for i in range(len(liste1)):
        for j in range(len(liste2)):
            if liste1[i] == liste2[j]:
                print(liste1[i])
                nb += 1
    return nb

def test():
    liste1 = [2, 4, 30, 20, 1]
    liste2 = [3, 23, 7, 8, 25]
    assert tirage(liste1, liste2) == 0, "gagnant"
    liste1 = [2, 4, 30, 20, 1]
    liste2 = [3, 23, 7, 20, 9]
    assert tirage(liste1, liste2) > 0, "perdant"
   
# l1 = nb_moi()
# l2 = nb_loterie()
# tirage(l1, l2)

test()