while True:
    try: # try sera toujours exécuté
        x = int(input("Entrer une valeur de x : "))
    except ValueError: # on exécute soit le except soit le else..
        print("x doit être un entier")
    else :
        break
print(f"x vaut {x}")