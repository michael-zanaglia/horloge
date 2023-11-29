import time

def times(m) :
    tmp = "{:02d}:{:02d}:{:02d}".format(m[0],m[1],m[2])
    print(tmp)
    time.sleep(1)
    m = (m[0],m[1],m[2] + 1)
    if m[2] == 60 :
        m = (m[0],m[1] + 1, 0)
        if m[1] == 60 :
            m = (m[0] +1, 0, 0)
            if m[0] == 24 :
                m = (0, 0, 0)
                
    return m
    
def afficher_heure() :
    while True :
        n = input("Souhaitez vous modifier l'heure ?(y/n)").lower()
        if n == "y" :
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
        elif n == "n" :
            break
        else :
            print("Entrez un caractere valide.")
            continue
    print(new)
    return new

def alarm(t) :
    if t == (7, 30, 30) :
        print("DEBOUT !!!!!!!!! Il est 7h30 !!!!!!")
        time.sleep(10)
        t = (7, 30, 41)
    return t
    
        
    
    

modif = afficher_heure()

while True :    
    modif = times(modif)
    modif = alarm(modif)