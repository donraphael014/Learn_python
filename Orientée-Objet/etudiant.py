from personne import Personne

class Etudiant(Personne):
    def __init__(self, nom, prenom, age, bac):
        super().__init__(nom, prenom, age)
        self.bac = bac
    def voir(self):
        print(" je suis un L'Etudiant :")
        print("Nom : ", self.nom)
        print("Prenom : ",self.prenom)
        print("Age : ",self.age)
        print("dans un niveau Bac : ",self.bac)