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

def secondes_en_minutes(nb, n = 0):
    if nb < 60:
        return (n, nb)
    return secondes_en_minutes(nb - 60, n + 1)

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

print(rendu_monnaie(152, [100, 50, 20, 10, 5, 2, 1]))

