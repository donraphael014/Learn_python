"""PARTIE POUR BLAISE"""
#***********************************************************************************************************************
#Déclaration et affectation des variables
nom = "blaise"
age ="24 ans"
salaire = 300
duree_de_travail ="20 ans"

print(nom, age, salaire,"dollars"+ duree_de_travail ,"ans")

#condition et boucle

age=input("inserer age")
if salaire > 20:
    print(nom ,"a votre age"+ age ,"ans tu peux etre riche")
else:
    print("si tu te debrouille bien tu peut aumoin en devenir un")

#Boucles
# for
for x in  range(10):
    print(x)
#while
x = 0
while x < 10:
    print(x)
    x += 1

#Fonctions
#sans retour et sans parametre
def indentite():
    print("indentite:\n"+nom,"age : \n"+age, "salaire" +salaire,"duree_de_travail : "+duree_de_travail)

    indentite()
    print(indentite())
#avec parametre
def somme( a,b):
    print("somme",a+b)


#avec retour

def somme(a , b):
 return a+b
somme (3,4)
somme (5,6)
print(somme(3,4))

#LES COLLECTION
#liste
fruits = ["pomme", "banane", "orange"]
print(fruits)
#pour selement afficher element ya kwanza

print(fruits[0])
print(fruits[1])
#etc........

#pour modofier

fruits[2] ="mangue"
print(fruits)

#pour ajouter un autre elements

fruits.append("avocat")
print(fruits)

#effacer
fruits.remove("banane")
print(fruits)


#trier le lise
nombres = [4, 2, 9, 1]
nombres.sort()         # Trie croissant
print(nombres)         # [1, 2, 4, 9]

nombres.reverse()
print(nombres)         # [9, 4, 2, 1]


#TUPLES
couleurs = ("rouge", "bleu", "vert")
print(couleurs)


etudiant = {
    "nom :" "Blaise "
    "prenom :" "Bangwa "
    "age :" "23"

}
print(etudiant)
#modifier
print(etudiant)
print("Apres l'ajout de donnnees")
#ajouter une paire
etudiant.add("ville :" "Bujumbura")
etudiant.remove("ville :" "Bujumbura")

print(etudiant)

#FIN procedural blaise
#===================================================================================================================