
import sys #bibliotheque qui accompagne pathlib
from pathlib import Path #cette bibliotheque  importee permette de chercher un fichier sil exist dans le disque
from personne import Personne
from etudiant import Etudiant
from voiture import voiture


if __name__ == '__main__':
# appel a la classe etudiant et ses methodes
    print("------------Information sur l'etudiant---------------------\n")
    personne = Personne("Blaise ", "Bangwa", 23)
    personne.voir()
    etudiant = Etudiant("Raphael ", "Kulimushi", 30, 3)
    etudiant.voir()

#appel a l'abstraction voiture
    voiture = voiture("Holland","4535","TX2","20000$")
    voiture.demarrer()
    voiture.arreter()


#appel et ala reutilisation de cette bibiotheque en soi
    print("--------------Fin abstation voiture----------------------\n")
    if Path("Vision.txt").exists():
        print(" le fichier Vision.txt est recent")
    else:
        sys.exit("le fichier Vision.txt n'existe du tout pas ")


