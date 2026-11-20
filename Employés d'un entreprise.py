class Employe:
    def __init__(self, nom, salaire):
        self.nom = nom
        self.salaire = salaire
    
    def afficher_info_personnelles(self):
        print("Nom:",{self.nom})
        print(f"Salaire:,{self.salaire}Ar")
        
class Developpeur(Employe):
    def __init__(self, nom, salaire, specialite):
        super().__init__(nom, salaire)
        self.specialite = specialite
    
    def  afficher_info(self):
        print(f"Votre nom: {self.nom}")
        print(f"Salaire: {self.salaire}AR")
        print(f"specialité: {self.specialite}")
        
employe1 = Developpeur("DOLLY", 100000, "python")
employe1.afficher_info()