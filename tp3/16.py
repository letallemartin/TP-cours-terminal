def calcul(X):
    """
    entré: int
    sortie: float
    
    """
    Copie_a = X #garde une copie de x
    X = X * 2
    X = X + 10
    X = X / 2
    X = X - Copie_a
    print(X)

calcul(3)
calcul(7)
calcul(-5)