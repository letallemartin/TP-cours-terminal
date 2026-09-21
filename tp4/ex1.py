dico_hermionne = {"Nom" : "granger", "Prénom" : "Hermione", "Age" : 16}
dico_hermionne ={"Prénom" : "Hermione","Nom" : "granger","Age" : 16}
x = 0
for cle in dico_hermionne:
    x+=1
    
print(x)

print(dico_hermionne["Nom"])
print(dico_hermionne["Age"])
for cle,val in dico_hermionne.items():
    print(cle, val)
    
# if "Prénom" in dico_hermionne.keys():
#     print("ok")

# if 16 in dico_hermionne.values():
#     print("ok")

# if ("Nom", "Weasley") in dico_hermionne.items():
#     print("ok")

dico_hermionne["animal"] = "Pattenrond"
dico_hermionne.pop("animal")
dico_hermionne["Age"] = 16
print(dico_hermionne.values())
