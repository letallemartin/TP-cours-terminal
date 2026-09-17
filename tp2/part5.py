def celsius_to_fahrenheit(temp_c):
    while True:
        try:
            F = temp_c * 9/5 + 32
        except ValueError:
            print("error")
        else: 
            break

def fahrenheit_to_celsius(temp_f):
    while True:
        try:
            C = (temp_f - 32) * 5/9
        except ValueError:
            print("error")
        else :
            break

def demander_temperature():
    # Tant qu'on a rien retourné ou qu'il n'y a pas eu d'erreur
    while True:
        try:
            temp = float(input("Entrez une température : "))
            return temp
        # Si l'utilisateur rentre un mot, float(mot) posera problème
        except TypeError :
            print("❌ Tu dois entrer un nombre (ex : 23.5) !")

def euros_vers_wons(montant):
    while True:
        try:
            total = montant * 1623
            return total
        except ValueError:
            print("error") 

def wons_vers_euros(montant):
    while True:
            try:
                total = montant * 0.00062
                return total
            except ValueError:
                print("error") 

def demander_devise():
    # Tant qu'on a rien retourné ou qu'il n'y a pas eu d'erreur
    while True:
        try:
            montant = float(input("Entrez un montant : "))
            return montant
        # Si l'utilisateur rentre un mot, float(mot) posera problème
        except ValueError :
            print("❌ Tu dois entrer un nombre !")

def demander_choix(message, choix_valides):
    while True:
        try:
            # on demande à l'utilisateur de saisir la valeur
            reponse = str(input("valeur:{choix_valide}"))
            if reponse in choix_valides:
                return reponse
            else:
                print(f"❌ Choix invalide. Réponses possibles : {','.join(choix_valides)}")
        except ValueError:
            print("error1")
        # si la réponse est dans les choix valides

def application():
    print("Bienvenue dans le convertisseur !")
    type_conversion = str(input("Tapez 't' pour température, ou 'd' pour devise : ",['t', 'd']))
    # Si l'utilisateur veut des températures
    if type_conversion == 't':
        sens_conversion = str(input("Tapez 'c' pour °C → °F, ou 'f' pour °F → °C : ",['c', 'f']))
        temp = ...
        # °C -> °F
    if sens_conversion == 'c':
        resultat = ...
        print(f"{temp} °C = {resultat:.2f} °F")
    else:
        resultat = ...
        print(f"{temp} °F = {resultat:.2f} °C")
    # Si l'utilisateur veut des devises
    else:
        sens_conversion = str(input("Tapez 'e' pour euros → wons, ou 'w' pour wons →euros : ", ['e', 'w'])
        montant = ...
                    

            