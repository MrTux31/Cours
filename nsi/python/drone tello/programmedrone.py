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
        time.sleep(5)
    prise.sendto('streamoff'.encode(encoding='utf-8'),adresse_tello)
    reponse= prise.recv(1024).decode(encoding='utf-8')    
    prise.close()
    print("fin connexion ")

if int(reponse) < 20 :
    prise.close()
    print("fin connexion, le niveau de charge est trop faible ")
else:
    # chemin du fichier
    objet_fichier = open("/media/sdb1/nsi/cours/plan_vol.txt", mode = 'r',encoding='utf-8')
    #liste qui stocke les commandes
    liste_commande = []
    # ajouter chaque élément du fichier à la liste
    for ligne in objet_fichier:
        liste_commande.append(ligne.strip('\n'))
    objet_fichier.close()
    prise.sendto('streamon'.encode(encoding='utf-8'),adresse_tello)
    reponse= prise.recv(1024).decode(encoding='utf-8')    
    #appeler la fonction
    lecture_commande(liste_commande)






