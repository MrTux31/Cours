#! /usr/bin/python3
valeur = 0
somme = 0
entier = int(input("Entrer un entier"))

for i in range(entier):
    somme = i + 1

if entier == somme:
    print('la somme est à', somme)
    print('L addition est :')
    for x in range(somme):
        print("+1")