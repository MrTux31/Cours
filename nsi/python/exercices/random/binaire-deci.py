#! /usr/bin/python3

# il faut écrire le nombre binaire à l'envers dans la liste pour obtenir la bonne conversion
L =  [0,0,1,0,1]
conversion = 0
def fonction(L, position):
    return L[position]*2**position
for i in range(len(L)):
    conversion= fonction(L, i) + conversion

print(conversion)
