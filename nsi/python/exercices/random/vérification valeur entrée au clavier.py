#! /usr/bin/python3

#entrer une valeur au clavier

valeur = int(input("entrer un entier"))
L = [2,7,2,5,10,4,2]
valeurliste = False
compteur = 0

#scan de la liste
for i in range(len(L)):
	if L[i] == valeur:
		valeurliste = True
		compteur = compteur + 1

if valeurliste == True:
	print("La valeur est", compteur, " fois dans la liste")

else: print("La valeur n'est pas dans la liste")
	
	 