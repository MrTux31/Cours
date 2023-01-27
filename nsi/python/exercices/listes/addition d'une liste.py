#! /usr/bin/python3
L = [1,2,3,4]
somme = 0
#scan de la liste
for i in range(len(L)):
	# on ajoute à somme les valeurs de la liste
	somme = L[i] + somme
print("la somme est", somme) 
	