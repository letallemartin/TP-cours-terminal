#e code de base sans try/except


while True:
    try :
        a = int(input("Entrez un premier nombre : "))
        b = int(input("Entrez un deuxième nombre : "))
        print("Résultat de a / b :", a / b)
    except ZeroDivisionError:
        print("error de division")
    except ValueError :
        print("valeur incorrect")
    else:
        break