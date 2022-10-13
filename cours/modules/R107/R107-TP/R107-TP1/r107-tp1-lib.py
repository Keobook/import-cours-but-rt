#!/usr/bin/env python3
# -*- coding: utf-8 -*-

### In two lines, what is this file?
### It's a file named lib (for library, you surely guessed) used to store all the functions in one file
### each functions is commented if necessary and there isn't any call so it will not disturb the parent caller.

### Désamorcer une bombe
def desamorcer(nbr_serie):
    x = str(nbr_serie)
    u, n = int(x[:3]), int(x[3:])
    for i in range(0, n):
        print(f"{u} -> ", end="")
        y = str(u*13)
        u = int(y[len(y)-3:])
        print(f"{y} -> {u}")

    return u

### Conversion de F° en C°
def FarhenheitToCelsius(temp):
    return (temp-32)*5/9


### Convertir Jour,Heures,Minutes en Secondes
def Quest15(j, h, m, s):
    x = (j*24)*3600
    y = h*3600
    z = m*60
    r = x+y+z+s
    return r

### Convertir Secondes en Jour,Heures,Minutes
def Quest16(t):
    j = int(t/(24*3600))
    h = int((t-j*24*3600)/3600)
    m = int((t-j*24*3600-h*3600)/60)
    s = t-j*24*3600 - h*3600 - m*60
    return (j, h, m, s)



### Déterminer les racines d'une expression de second degré
def degree2(a, b, c):
    delta = b**2 - 4*a*c
    if delta > 0:
        x1 = (-b-sqrt(delta))/2*a
        x2 = (-b+sqrt(delta))/2*a
        print(f"Les 2 racines de votre polynome {a}x**2+{b}x+{c} sont: {x1} et {x2}")
    elif delta == 0:
        x = -b/2*a
        print(f"La racine de votre polynome {a}x**2+{b}x+{c} est: {x}")
    else:
        print(f"Votre polynome {a}x**2+{b}x+{c} n'a pas de racine dans R")

### Fonction pour calculer un combat entre Hercule et une Hydre
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

### Determine l'IMC
def determineIMC(size, weight):
    """
    Prints - given the parameters - if you're in overweight or not.
    """
    imc = weight/size**2

    if imc < 25:
        print("You aren't in overweight with an IMC of", imc)
    else:
        print("You are in overweight with an IMC of", imc)

### Retourne si on est en surpoids suivant l'IMC calculé
def getOverweight(size, weight):
    """
    Returns either True or False.
    """
    imc = weight/size**2

    if imc < 25:
        return False
    return True

### Boucle des étoiles en horizontal
def StarLoop(_list):
    for i in _list:
        print("*"*i)

    print("\n", end="")

### Boucle des étoiles en vertical
def VerticalStarLoop(_list):
    x = max(_list)
    t = [[[" "]*(x-_list[i])+["*"]*_list[i]] for i in range(0, len(_list))]
    for i in range(0, x):
        for j in t:
            print(j[0][i], end="")
        print()
