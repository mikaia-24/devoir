class CompteBancaire:
    def __init__(self, titulaire, solde):
        self.titulaire = titulaire
        self.solde = solde
        
    def se_presenter(self):
        print(f" Je m'applle {self.titulaire}.")
        print(f"Ma solde {self.solde} Ar.")
        
class CompteEpargne(CompteBancaire):
    
    def __init__(self, titulaire, solde, interet):
        super().__init__(titulaire, solde)
        self.interet= interet
    
    def calculer_interet(self):
        interet = self.solde * self.interet /100
        print(f"Interet {interet}Ar")
    
    def afficher_solde(self):
        super().se_presenter()
        
        print(f"Interet est de {self.interet}%.")
        
compte1 = CompteEpargne("DOLLY", 1500000, 5)
compte1.afficher_solde()
compte1.calculer_interet()

        