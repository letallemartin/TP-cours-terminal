
def conversion_chaine(string):
    dico = {}
    for i in range(len(string)):
        if string[i] in dico.keys():
            dico[string[i]] += 1
        else:
            dico[string[i]] = 1
    return dico

dico = {2 : 10, "Orange" : 15, "Fraise" : 3}
# print(dico.items())

def echanger(dico):
    dico2 = {}
    for cle,val in dico.items():
        dico2[val] = cle
        
    print(dico2.items())

# echanger(dico)

def somme_dico(dico):
    x = 0
    for val in dico.values():
        x += val
    print(x)

# somme_dico(dico)

def alphabet():
    dico = {}
    list = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(list)):
        dico[list[i]] = i + 1
    print(dico.items())
    
# alphabet()

def test_str(dico):
    for cle in dico.keys():
        if isinstance(cle, int):
            return False
    return True


def conversion_tab(liste1,liste2):
    dico = {}
    for i,j in (liste1,liste2):
        dico[i] = j

magasin_A = {"Pomme" : 10, "Orange" : 15, "Fraise" : 3}
magasin_B = {"Pomme" : 7, "Orange" : 4, "Fraise" : 8}

def patate(dico1, dico2):
    dico3 = dico2
    for cle in (dico2.keys()):
        if dico1[cle] > dico2[cle]:
            dico3[cle] = dico1[cle]
    print(dico3.items())
patate(magasin_A, magasin_B)
        