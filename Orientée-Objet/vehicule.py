from abc import ABC, abstractmethod #importation d'une bibliotheque de l'abstraction

#Notion sur l'abstraction tres essentiels a maitriser
class Vehicule(ABC):
    @abstractmethod
    def __init__(self, marque, numeroSerie):
        self.marque = marque
        self.numeroSerie = numeroSerie

    @abstractmethod
    def demarrer(self):
        pass
    @abstractmethod
    def arreter(self):
        pass