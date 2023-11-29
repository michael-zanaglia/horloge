# J'importe la bibliotheque de time pour utiliser le time.sleep() principalement
import time

# Cette fonction sert a calculer le temps en fonction d'un tuple 'm'.
def times(m,ampm) :
    # Reponse obtenu suite a une question d'une autre fonction
    if ampm == "y" :
        # ap devient AM si h est inferieur a 12 sinon il deviendra PM
         ap = "AM" if m[0] < 12 else "PM"
         # Je definis un format pour l'affichage '{:02d} definis un affichage de deux valeurs qui
         #seront convertis en str. Le '%' permet ici d'aller de 0 a 12 en BOUCLE et le
         #'or 12' signifie que si je tombe a zero, 0 devient 12.
         tmp = "{:02d}:{:02d}:{:02d} {}".format(m[0] % 12 or 12,m[1],m[2], ap)
    else :
        tmp = "{:02d}:{:02d}:{:02d}".format(m[0],m[1],m[2])
        if m[0] == 24 :
                # h = 0 dans le cas de figure ou je n'ai pas besoin de AM/PM
                m = (0, m[1],m[2]) 
    print(tmp)
    # Pause de 1seconde
    time.sleep(1)
    # j'incremente ma seconde de 1
    m = (m[0],m[1],m[2] + 1)
    # si seconde = à 60 :
    if m[2] == 60 :
        # +1 en minute et mes secondes retournent à 0
        m = (m[0],m[1] + 1, 0)
        # si mes minutes = 60
        if m[1] == 60 :
            # +1 pour mes heures
            m = (m[0] +1, 0, 0)
            # Et si mes heures sont = à 24
            if m[0] == 24 :
                # h = 0 dans le cas de figure ou je n'ai pas besoin de AM/PM
                m = (0, 0, 0) 
     # Je retourne le tuple mis a jour à ma variable appelant la fonction afin de rafraichir les valeurs           
    return m

# Cette fonction sert a definir les besoin de l'utilisateur.    
def afficher_heure() :
    while True :
        n = input("Souhaitez vous modifier l'heure ?(y/n)").lower()
        if n == "y" :
            while True :
                ampm = input("Souhaitez vous un format 12h ?(y/n)").lower()
                if ampm == "y" or ampm == "n" :
                    break
                else : 
                    print("Entrez un caractere valide.")
                    continue
            while True :
                h = int(input("Entrz une heure : "))
                if h < 1 or h > 24 :
                    print("Un chiffre entre 1 et 24")
                else :
                    break
            while True :
                m = int(input("Entrz des minutes : "))
                if m < 0 or m > 60 :
                    print("Un chiffre entre 0 et 60")
                else :
                    break
            while True :
                s = int(input("Entrz des secondes : "))
                if s < 0 or s > 60 :
                    print("Un chiffre entre 0 et 60")
                else :
                    break
            new = (h, m, s)
            break
        # Si je n'ai pas besoin de parametrer mon horloge : 
        elif n == "n" :
            # Boucle infini afin d'afficher l'heure universel
            while True :
                print(time.strftime("%H:%M:%S"))
                time.sleep(1)
        else :
            print("Entrez un caractere valide.")
            continue
    print(new)
    
    # Je retourne le tuple new dans modif et ampm pour la fonction plus au dessus
    return new, ampm

# Fonction pour une alarme : S'il est 7h30, BIP BIP 
def alarm(t) :
    if t == (7, 30, 30) :
        print("DEBOUT !!!!!!!!! Il est 7h30 !!!!!!")
        time.sleep(10)
        #Puisque je fais une pause de 10 sec je reprends la je me suis arreter + 10 ! pour ne pas avoir une heure erronée
        t = (7, 30, 41)
    # Je retourne t dans ma variable modif pour ne pas pertuber le fonctionnement:
    return t
    
        
    
    

modif, ampm = afficher_heure()

while True :    
    modif = times(modif, ampm)
    modif = alarm(modif)