#l'utilisateur entre son prénom
prenom = input('Entrez un prénom')

#création de la liste qui va stocker les lettres du prénom
lettres = []
#la variable caractère va prendre la valeur de chaque lettre
caractère= 0
#création de la liste où la traduction sera transposée
traduction = []
#dictionnaire qui associe chaque lettre classique à sa version cyrillique
dic={"a":"a","b":"б","c":"ц","d":"д","e":"е","f":"ф","g":"г","h":"х","i":"и","j":"й","k":"к","l":"л","m":"м","n":"н",
     "o":"о","p":"п","q":"q","r":"р","s":"с","t":"т","u":"у","v":"в","w":"w","x":"х","y":"ы","z":"з"}

#stockage des lettres du prénom dans la liste
for i in range(len(prenom)):
    lettres.append(prenom[i])

for i in range(len(lettres)):
    caractère = lettres[i]
    traduction.append(dic[caractère])

print(traduction)









