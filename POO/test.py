class Client:
    def __init__(self, nom):
        self.nom = nom
        

client1 = Client("jean")

class ComptBancaire:
    def __init__(self, numero, solde = 0):
        self.numero = numero
        self.solde = solde
    
    def deposer(self, montant):
        self.solde += montant
        print(f"{montant}$ déposé sur le compt de {self.numero}")
    
    def retrait(self, montant):
        self.solde -= montant
        print(f"{montant}$ retiré sur le compt de {self.numero}")
        
    def consulter_solde(self):
        print(f"numero: {self.numero} -> {self.solde}$")
        
    def virement(self, compt_destinataire, montant):
        if montant < self.solde:
            self.solde -= montant
            compt_destinataire.solde += montant
        else: print("pas assez")
        
    def __str__(self):
        return f"numero: {self.numero} -> {self.solde}$"   

compt2 = ComptBancaire(500)
compt1 = ComptBancaire(300)
print(compt2)

class Client:
    def __init__(self, nom, prenom, comptes):
        self.nom = nom 
        self.prenom = prenom
        self.comptes = comptes
        
    def ajouter_compte(self,compt):
        self.comptes.append(compt)
        
    def afficher(self):
        print(f"Client : {self.prenom} {self.nom}")
        for compt in self.comptes:
            compt.afficher()
            
    def __str__(self):
        list = []
        for compt in self.comptes:
            list.append(str(compt))
        return f"{self.nom} {self.prenom} {list}"

client = Client("Dupont","Paul",[compt2,compt1])
while True:
    print(client)
    choix_compt = int(input("compt"))
    choix_montant = int(input("montant: "))
    if choix_compt == 1: