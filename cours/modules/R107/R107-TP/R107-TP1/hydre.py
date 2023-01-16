#!/usr/bin/python3

def combatHercule(tetes):
    nbr_tetes = tetes
    x = 0
    while nbr_tetes != 1:
        x += 1
        nbr_tetes /= 2
        print(f"Coup {x}: {int(nbr_tetes)} têtes coupées, ", end="")
        if nbr_tetes%2 != 0:
            if nbr_tetes != 1:
                nbr_tetes = (nbr_tetes*3)+1
            print(f"Il reste {int(nbr_tetes)} têtes après qu'elles aient pu repousser")
        else:
            print("Rien ne repousse")
    print(f"Coup {x+1}: Hercule achève l'Hydre")


combatHercule(8542)