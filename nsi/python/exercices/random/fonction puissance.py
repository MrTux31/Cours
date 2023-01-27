#! /usr/bin/python3
somme = 0
n = int(input("Entrer un entier"))

def puissance(t):
	return t**2



for i in range(n):
    somme = puissance(i)+ somme
print(puissance(i))


print(somme)