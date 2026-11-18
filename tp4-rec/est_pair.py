def est_pair(n):
    while n > 0:
        n = n - 2
    return n == 0

def est_pair_rec(n):
    if n <= 0:
        return n == 0
    return est_pair_rec(n - 2)



def inverse(liste1):
    if len(liste1) == 0 or len(liste1) == 1:
        return ""
    return   inverse(liste1[1:]) + liste1[0]

def inverse_acc(txt, inv):
    if len(txt) == 0:
        return txt + inv
    return   inverse_acc(txt[1:], txt[0] + inv)
print(inverse_acc("ab", ""))
def secondes_en_minutes(nb, n = 0):
    if nb < 60:
        return (n, nb)
    return secondes_en_minutes(nb - 60, n + 1)

def seconde_iter(nb, n = 0):
	if nb >= 60:
		nb = nb - 1
		n += 1
	return (n, nb)
def inverse_iter(txt):
    inv = ""
    for i in txt:
        inv = i + inv
    return inv

def rendu_monnaie(montant_a_rendre, billets):
    
    if len(billets) == 0:
        return []
    
    if montant_a_rendre  < billets[0]:
        return rendu_monnaie(montant_a_rendre, billets[1:])
    
    return [billets[0]] + rendu_monnaie(montant_a_rendre - billets[0], billets)

print(rendu_monnaie(6, [4, 3, 1]))

def rendu_rec(montant_a_rendre, billets):
    liste1 = []
    for i in range(len(billets)):
        while montant_a_rendre < billets[i]:
            liste1.append(billets[i])
            montant_a_rendre -= billets[i]
    return liste1
            
            
            
VALEUR_ROMAIN = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
def romain(chaine):
    total = 0
    n = len(chaine)

    for i in range(n):
        valeur = VALEUR_ROMAIN[chaine[i]]
        if i + 1 < n and valeur < VALEUR_ROMAIN[chaine[i + 1]]:
            total -= valeur
        else:
            total += valeur

    return total
def rec_romain(chaine):
    if len(chaine) == 0:
        return 0
    elif len(chaine) == 1:
        return VALEUR_ROMAIN[chaine[0]]
    else:
        prem = VALEUR_ROMAIN[chaine[0]]
        sec = VALEUR_ROMAIN[chaine[1]]
        if prem < sec:
            return(sec - prem) + rec_romain(chaine[2:])
        else:
            return prem + rec_romain(chaine[1:])

print(rec_romain("X"))
        
assert romain("XIX") == 19
assert romain("XIV") == 14
assert romain("XXI") == 21
assert romain("MCMXC") == 1990
assert romain("IV") == 4
assert romain('X') == 10
assert romain('XCI') == 91
assert romain('MMXIX') == 2019

def est_liste(liste, x):
    if len(liste) == 0:
        return est_liste(liste[1:])
    if liste[0] == x:
        return True
    return False

def est_liste(liste, x, i = 0):
    if i < len(liste):
        if liste[i] == x:
                return True
        return est_liste(liste,x,  i + 1)
    return False

print(est_liste([1, 2, 3], 3))

def rech_dico(tab, x, gauche, droite):
    if gauche > droite:
        return False
    millieu = (droite + gauche ) // 2
    if tab[millieu] == x:
        return True
    elif x < tab[millieu]:
        return rech_dico(tab, x, gauche, millieu - 1)
    return rech_dico(tab, x, millieu + 1, droite)

def dec2bin(x):
    if x < 2:
        return [x]
    return dec2bin(x // 2) + [x % 2]

print(dec2bin(3))