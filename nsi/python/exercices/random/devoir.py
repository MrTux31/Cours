#! /usr/bin/python3

k = int(input("Entrer un nombre à partir duquel les premières puissances sont calculées"))
n = int(input("Indiquez combien de puissances sont calculées"))
t = 0
def puissance(x, exposant):
	return x**exposant

	
for i in range(k, n+k):	
	print(puissance(i , 2))
	t =t + puissance(i, 2)

	
print("le total est" ,t)
