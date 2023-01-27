import socket
import time
import sys
ip_pc = '192.168.10.2'
port = 9000
adresse_pc = (ip_pc,port)
adresse_tello = ('192.168.10.1',8889)
# on crée un point de branchement pour pouvoir communiquer
prise = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
try:
    prise.bind((ip_pc,port))
except socket.error:
    print('la connexion a échoué')
    sys.exit()
print('la connexion a réussi')
#on envoie le message 'command' pour pouvir entrer en mode programmation dans le done
prise.sendto('command'.encode(encoding='utf-8'),adresse_tello)
reponse = prise.recv(1024).decode(encoding='utf-8')
print("Entrer dans le mode programmation",reponse)
time.sleep(2)
# on envoie le message 'battery'
prise.sendto('battery?'.encode(encoding='utf-8'),adresse_tello)
reponse= prise.recv(1024).decode(encoding='utf-8')
print("le niveau de charge de la batterie est de ",reponse,"%")

def lecture_commande(liste_commande):
    liste = liste_commande
    time.sleep(2)
    for i in range(len(liste)):
        prise.sendto(liste[i].encode(encoding='utf-8'),adresse_tello)
        reponse= prise.recv(1024).decode(encoding='utf-8')
        #création des phrases pour vérifier le bon déroulement
        ok = 'La commande {} sest bien déroulée'
        non = 'La commande {} ne sest pas bien déroulée'
        if reponse == 'ok':
            print(ok.format(liste[i]))
        else: print(non.format(liste[i]))


    commande = input('Quelle commande voulez vous exécuter ?')
    
    liste = []
    liste.append(commande)
    lecture_commande(liste)

if int(reponse) < 20 :
    prise.close()
    print("fin connexion, le niveau de charge est trop faible ")
else:
    #demander la commande à l'utilisateur
    commande = input('Quelle commande voulez vous exécuter ?')
    liste_commande = []
    #ajouter la commande à la liste
    liste_commande.append(commande)
    #activer la caméra
    prise.sendto('streamon'.encode(encoding='utf-8'),adresse_tello)
    reponse= prise.recv(1024).decode(encoding='utf-8')
    #appeler la fonction
    lecture_commande(liste_commande)


