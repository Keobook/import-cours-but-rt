#!/usr/bin/python3

# Sujet : classement de smartphones
modele=['Samsoun','Appeul','Wawé','Motorolus','Ellegée']
batterie=[5200,4000,3000,5000,4500] # capacité en mAh (milliampères/heure)
vitesse=[3200,2800,4300,4000,2900] # en MHz
nbPixels=[786432,1920000,3360000,1296000,2400000] # nombre total de pixels

# 1)-Nombre de smartphones à étudier
n = len(modele)
print("Nombre de smartphones à étudier:", n)
# 2)-Capacité moyenne des batteries
somme = 0
for i in range(0, n):
  somme += batterie[i]
moyenne_batterie = somme/n
print("La capacité moyenne des batteries est", moyenne_batterie, "mAh")
# 3)-Nom du smartphone le plus rapide
plus_rapide = (0, 0)
for i in range(0, n):
  if vitesse[i] > plus_rapide[0]:
    plus_rapide = (vitesse[i], i)

print("Le smartphone le plus rapide est", modele[plus_rapide[1]], "avec une vitesse de", plus_rapide[0], "MHz")

# 4)-nous allons maintenant utiliser des fonctions pour faciliter le traitement des données
# refaire la question précédente en définissant une fonction pour la recherche de la position du max.
# but : rappeler le mécanisme de définition et d'utilisation des fonctions
def recherche_pos_max(seq):
  max = (0, 0)
  for i in range(len(seq)):
    if seq[i] > max[0]:
      max = (seq[i], i)

  return max

# 5)-Réutilisation de la fonction précédente pour déterminer celui qui a la plus grande batterie
plus_batterie = recherche_pos_max(batterie)
print("Le smartphone ayant la plus grande batterie est", modele[plus_batterie[1]], "avec une batterie de", plus_batterie[0], "mAh", end="\n\n")

# 6)-On souhaite évaluer le score des smartphones avec un nombre unique !
# nous utiliserons la formule suivante : score=10*vitesse + 7*batterie +0.5*nbPixels
# écrire une fonction qui donne le score d'un smartphone connaissant son indice
def getScore(indice):
  score = int(10*vitesse[indice] + 7*batterie[indice] + 0.5*nbPixels[indice])
  return score

# 7)-écrire une boucle pour afficher la performance de chaque smartphone
for i in range(0, n):
  print(f"Le téléphone {modele[i]} a un score de {getScore(i)}")

# 8)-créer un nouveau tableau contenant les scores des smartphones
score = [getScore(i) for i in range(0, n)]

# 9)-réutiliser alors la fonction posMaximum pour donner le nom du smartphone le plus performant
plus_perform = recherche_pos_max(score)
print("Le plus performant est", modele[plus_perform[1]])

# 10)-créer la fonction posMaximum2 pour donner le nom des 2 smartphones les plus performants.


# si on a le temps, on peut classer les smartphones du plus performant au moins performant.


