#!/usr/bin/python3

## Déterminer l'IMC d'une personne avec en entrée son poids (kg) et sa taille (m)
t = float(input("Entrez la taille (en m): "))
m = int(input('Entrez la masse (en kg): '))
imc = m/t**2

if imc < 25:
    print("Vous n'êtes pas en surpoids")
else:
    print("Vous êtes en surpoids")
