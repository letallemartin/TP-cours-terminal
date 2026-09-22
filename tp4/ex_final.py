def compte_votes(votes):
    dico = {}
    for v in votes:
        if v in dico.keys():
            dico[v] += 1
        else:
            dico[v] = 1
    return (dico)

def best(votes):
    dico = compte_votes(votes)
    max = 0
    for val in dico.values():
        if val > max:
            max = val
    return max
        