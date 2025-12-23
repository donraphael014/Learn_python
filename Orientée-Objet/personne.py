class Personne:
    #classe personne pour bien apprendre l'hritage et polymorphisme qui sera instancier dans main.py
    def __init__(self,nom,prenom,age):
        self.nom = nom
        self.prenom = prenom
        self.age = age

    def voir(self):
        print(" Je m'appelle :")
        print("Nom : ", self.nom)
        print("Prenom : ",self.prenom)
        print("Age : ", self.age)