class Telephone:
    def __init__(self, marque, couleur, memoire, batterie):
        self.marque = marque
        self.couleur = couleur
        self.memoire = memoire
        self.batterie = batterie
        
    def appeler(self, numero):
        print(f"Le téléphone {self.marque} appelle le numéro {numero}.")

    def envoyer_message(self, numero, message):
        print(f"Message envoyé au {numero} : {message}")
        
    def ecouter_musique(self):
        print(f"Le telephone {self.marque} joue bien la musique (mp3).")    
    
    def charger(self):
        print(f"Le telephone {self.batterie} Batterie chargée à 100%")
        
            

    def afficher_information(self):
        print(f"Marque : {self.marque}")
        print(f"Couleur : {self.couleur}")
        print(f"Mémoire : {self.memoire} Go")
        print(f"Batterie : {self.batterie} %")


telephone1 = Telephone("IPAD", "Noir", 251, 100)

telephone2 = Telephone("MOTOROLA", "rouge", 128, "Bien")



telephone1.afficher_information()
telephone1.appeler("0341234567")
telephone1.envoyer_message("032345678", "salut_python!")

telephone2.afficher_information()
telephone2.appeler("0334567890")
telephone2.envoyer_message("0334567890", "Bienvenue sur le python!")
telephone2.charger()
telephone2.ecouter_musique()