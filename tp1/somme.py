def somme(n):
    """entré: n(int)
       sortie: n(int)
       calcule la somme des nb de 1 a n"""
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

print(somme(3))