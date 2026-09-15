#------------------------------------------#
# Programme 1 :
notes = [15, 12, 18, 9]
for i in range(len(notes) + 1) :
    print("Note" + str(notes[i]))

#------------------------------------------#
# Programme 2 : 
age = "18"
if age > 18 :
    print("Vous etes majeur !")
    
#------------------------------------------#
# Programme 3 : 
note = 16
if note > 16 :
    mention = "Très bien"
elif note < 16 :
    mention = "Mention bien"
    
#------------------------------------------#
# Programme 4 : 
print(0.1 + 0.2 == 0.3)

#------------------------------------------#
# Programme 5 : 
somme = 0
i = 0
while somme < 100 :
    somme = somme + i

#------------------------------------------#
# Programme 6 : 
if x == 0 :
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
print(original)

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

    print("Accès autorisé.")

#------------------------------------------#