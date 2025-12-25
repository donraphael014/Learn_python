list = [3, 67, 8.5,"Blaise","Carmel"]
print(list)
a = input("inserer un nombre ")
list.append(a)
print(list)
try:
    b = input("veuillez entrez un element a supprimer sur la liste : ")
    conversion = float(b)

    list.remove(conversion)
    print(list)
except ValueError:
    print("La valeur n'est pas valide")


