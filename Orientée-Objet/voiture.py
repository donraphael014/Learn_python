from vehicule import *

class voiture(Vehicule):
    def __init__(self, marque,numeroSerie,nom,prix):
        super().__init__(marque, numeroSerie)
        self.nom = nom
        self.prix = prix
        print("-----------------LA VOITURE------------------\n")
        print(f"le nom d'objet est : {self.nom} \n le prix  est : {self.prix} \n la marque est : {self.marque} \n")
        print(f"le numero serie est : {self.numeroSerie}")
    def demarrer(self):
        print(f"ma voiture : {self.nom} demarre ")
        print(f"le prix de ma voiture  est : {self.prix}")

    def arreter(self):
        print(f"ma voiture : {self.nom} arrete ")
        print(f"le prix de ma voiture  est toujours au : {self.prix}")


