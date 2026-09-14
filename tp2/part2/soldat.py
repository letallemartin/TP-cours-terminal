def generer_soldat():
    import random
    pt_vie = random.randint(50, 100)
    attq = random.randint(10, 20)
    return pt_vie, attq



a, b = generer_soldat()
print(a, b)