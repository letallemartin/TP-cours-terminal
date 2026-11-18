class Client:
    def __init__(self, nom):
        self.nom = nom
        

client1 = Client("jean")

class ComptBancaire:
    def __init__(self, numero, solde = 1000):
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
            compt.consulter_solde()
            
    def __str__(self):
        list = []
        for compt in self.comptes:
            list.append(str(compt))
        return f"{self.nom} {self.prenom} {list}"

client = Client("Dupont","Paul",[compt2,compt1])
while True:
	print(client)
	choix_compt = int(input("compt"))
	for compt in range(len(client.comptes)):
		if (choix_compt - 1) == compt:
			choix_action = int(input("choix: consulter(1) ajouter(2) retirez(3) virement(4)"))
			if choix_action == 1:
				client.afficher()
			else:
				montant = int(input("montant: "))
			if choix_action == 2:
				client.comptes[compt].deposer(montant)
			elif choix_action == 3:
				client.comptes[compt].retrait(montant)
			elif choix_action == 4:
				choix_compt2 = int(input("compt dest"))
				for compt_dest in range(len(client.comptes)):
					if (choix_compt2 - 1) == compt_dest:
						client.comptes[compt].virement((client.comptes[compt_dest]), montant)

