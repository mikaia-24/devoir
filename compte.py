class Compte:
    def __init__(self, fornisseur, solde):
        self.fournisseur = fornisseur
        self.solde = solde
        
    def se_presenter(self):
        print(f"Je suis {self.fournisseur} et mon solde est:{self.solde} Ar.")

class CompteBancaire(Compte):
    def __init__(self, fornisseur, solde, banque):
        super().__init__(fornisseur, solde)
        self.banque = banque
    def se_presenter(self):
        super().se_presenter()
        print(f"Ma banque est {self.banque}.")
        
compte1 = CompteBancaire("DOLLY", 1250000, "BFV")
compte1.se_presenter()