from personne import Personne
#classe etudiant herite la classe personne pour reutiliser le meme objet
class Etudiant(Personne):
    def __init__(self, nom, prenom, age, bac):
        super().__init__(nom, prenom, age)#appele des element de personne
        # la je reouvre un nouvelle attribut qui ne meme pas dans la classe personne
        # C'est ce qu'on appelle polymorphisme
        self.bac = bac
    def voir(self):
        print(" je suis un Etudiant :")
        print("Nom : ", self.nom)
        print("Prenom : ",self.prenom)
        print("Age : ",self.age)
        print("dans un niveau Bac : ",self.bac)
