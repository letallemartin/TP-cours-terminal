#------------------------------------------#
# Programme 1 :
notes = [15, 12, 18, 9]
for i in range(len(notes) + 1) :
    print("Note" + str(notes[i]))

#------------------------------------------#
# Programme 2 : 
age = 18
if age > 18 : #age est un str pas un int
    print("Vous etes majeur !")
    
#------------------------------------------#
# Programme 3 : 
note = 16
if note > 16 :
    mention = "Très bien"
elif note <= 16 :
    mention = "Mention bien" #oublie <=
    
#------------------------------------------#
# Programme 4 : 
print(0.1 + 0.2 == 0.3) # resultat de booleen aproximatif (arrondi binaire)

#------------------------------------------#
# Programme 5 : 
somme = 0
i = 1
while somme < 100 :
    somme = somme + i # i = 0

#------------------------------------------#
# Programme 6 : 
x = 0
if x == 0 : # x pas declaré
    print("Variable nul")
elif x < 0 :
    print("Nombre négatif")
else :
    print("Nombre positif")

#------------------------------------------#
# Programme 7 : 
original = [1, 2, 3]
copie = original

copie[0] = 999
print(original) # lien créer entre copie et original (copi n'est pas reelement une copie mais un lien direct avec l'original)

#------------------------------------------#
# Programme 8 : 
authentifie = False
mot_de_passe = input("Mot de passe : ")

if mot_de_passe == "nsi2025":
    print("Mot de passe correct.")
    authentifie = True
else:
    print("Mot de passe incorrect.")
    authentifie = False
if authentifie == True:
	print("Accès autorisé.") #mauvaise indentation et oublie de if

#------------------------------------------#