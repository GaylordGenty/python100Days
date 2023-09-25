# Go to https://replit.com/@appbrewery/rock-paper-scissors-start?v=1
import random

ppc = ["Pierre", "Papier","Ciseaux"]
victoire = 0
égalité = 0
défaite  = 0

while True :
    randInt = random.randint(0,2)
    choix_adv = ppc[randInt]

    def msgDef() :
        print("Vous avez perdu...")
        
    def msgVic() :
        print("Vous avez gagné !")

    for i in ppc :
        print(f"{ppc.index(i)+1}] {i}")
        
    choix = input("Faite votre choix !\n")

    if choix == "1" :
        choix = "Pierre"
    elif choix == "2" :
        choix = "Papier"
    elif choix == "3" :
        choix = "Ciseaux"

    print(f"Vous {choix} VS {choix_adv}")

    if ppc[randInt].upper() == choix.upper() :
        print("Égalité")
        égalité +=1
    elif choix == "Pierre" :
        if choix_adv == "Papier" :
            msgDef()
            défaite +=1
        elif choix_adv == "Ciseaux" :
            msgVic()
            victoire +=1
    elif choix == "Papier" :
        if choix_adv == "Ciseaux" :
            msgDef()
            défaite +=1
        elif choix_adv == "Pierre" :
            msgVic()
            victoire +=1
    elif choix == "Ciseaux" :
        if choix_adv == "Pierre" :
            msgDef()
            défaite +=1
        elif choix_adv == "Papier" :
            msgVic()
            victoire +=1

    print("**********")
    print(f"Victoire   : {victoire}")
    print(f"Matche Nul : {égalité}")
    print(f"Défaite    : {défaite}")
    print("**********")
    

