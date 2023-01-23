# SAE-15 Traiter les données

## Les statistiques

- Acquisition
  - capteurs
  - webscrapping
- Analyse / Interprétation
  - Indicateurs
  - Graphs

### Exemple de série chifrée

|                                      |       Notes A1       |       Notes A2        |
| :----------------------------------: | :------------------: | :-------------------: |
|                                      |          10          |          18           |
|                                      |          11          |          16           |
|                                      |          9           |           2           |
|                                      |          10          |           4           |
|                                      |          12          |          11           |
|                                      |          8           |          12           |
|                                      |          10          |           7           |
|        $\frac{1}{n} \sum x_i$        |          10          |          10           |
| $\frac{1}{n} \sum (x_i - \bar{x})^2$ |         1,42         |         30,57         |
|               $\sigma$               | $\sqrt{1.42} = 1.19$ | $\sqrt{30.57} = 5.52$ |

| x <br> Maths | y <br> Reseau |
| :----------: | :-----------: |
|      12      |       8       |
|      6       |       7       |
|      13      |       8       |
|      9       |      17       |
|      2       |      20       |
|      14      |      17       |

$(x_i - \bar{x} ) (y_i - \bar{x})$

| Nom            | Formule                                                  | Définition                                                                                                         |
| -------------- | -------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| La moyenne     | $\bar{x} = \frac{1}{n} \sum x_i$                         | La moyenne est la somme des valeurs divisée par le nombre de valeurs.                                              |
| La variance    | ${1 \over n} \sum (x_i - \bar{x})^2$                     | La variance est la moyenne des écarts à la moyenne.                                                                |
| L'écart-type   | $\sigma = \sqrt{var(x)}$                                 | L'écart-type est la racine de la variance.                                                                         |
| La covarience  | $cov(x,y) = {1 \over n} \sum (x - \bar{x})(y - \bar{y})$ | Avec deux valeurs, le produit $(x - \bar{x})(y - \bar{y})$.                                                        |
| La correlation | $r(x,y) = \frac{cov(x,y)}{\sigma x \sigma y}$            | La correlation n'est pas la causalité.<br> Cela veut aussi dire qu'il y a susceptiblement une raison sous-jacente. |

## Un module Python

Un $\underbar{module}$ est un fichier python contenant un ensemble
de fonctions et de variables prédéfinies que l'on peut utiliser
dans différents projets.  
Le but est de $\underbar{simplifier l'écriture}$ des programmes,
$\underbar{d'améliorer leur lisibilité}$ et de $\underbar{structurer un projet}$.

### Template d'un module Python

Un module nommé `geometrie.py`

```python
# Module: geometrie
# Copyright: <nom/prénom>
# Version: <version>
# Date: <date de dernière MAJ>

# Variables
pi = 3.14159265

# Fonctions

# Fonction qui calcule la surface
# d'un carré de côté <a>
def surfaceCarre(a):
  return a**2

# ...
def surfaceRectangle(a,b):
  return a*b

# ...
def surfaceDisque(r):
  return pi*(r**2)

```

## Miniprojet

Pour avoir les données de ce miniprojet, il faut prendre le dépôt GitHub:

```HTTPS
https://github.com/alexis-opolka/SAE-15-DATA.git
```
