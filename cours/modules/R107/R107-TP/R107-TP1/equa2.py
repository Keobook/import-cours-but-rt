#!/usr/bin/python3

from math import sqrt

## Déterminer les racines d'une
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


a = int(input("Entrez le facteur 'a' de votre expression du 2nd degré: "))
b = int(input("Entrez le facteur 'b' de votre expression du 2nd degré: "))
c = int(input("Entrez le terme constant 'c' de votre expression du 2nd degré: "))
degree2(a, b, c)