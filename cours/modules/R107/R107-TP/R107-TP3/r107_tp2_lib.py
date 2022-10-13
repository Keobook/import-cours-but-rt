#!/usr/bin/env python3
# -*- code: utf-8 -*-

###////////////////////////////////////////////////////////////////////////////////////
###
### Zone d'initialisation (fonctions, classes)
###
###////////////////////////////////////////////////////////////////////////////////////

## 1. Introduction

### 1/

#### Functions already present
def f0(): # Prints "Hello"
  print("Hello")

def f1(x): # Returns x^2
  return x**2

def f2(x, y=5): # Returns the sum of x & y
  return x+y

#### 1. TVA/TTC
def calcTTCPrice(prix, tva): # Returns the price with the tax
  return float(prix*(1+tva/100))

#### 2. Fct complémentaire
def CalcAmountTax(prix, tva): # Returns the amount of tax knowing the price and the tax added to
  return prix/(1+tva/100)

#### 3. Donne la valeur la plus élevée d'une séquence
def getMax(seq): # Returns the maximum value of a sequence (list, tuple, range)
  max = seq[0]
  for i in seq:
    if i > max:
      max = i

  return max

#### 4. Trouve la position du minimum d'une séquence
def positionMin(seq, offset=0): # Returns the position of the minimum value of a sequence (list, tuple)
  min = (seq[offset], offset)
  for i in range(offset, len(seq)):
    print(seq[i], min[0], True if seq[i] < min[0] else False)
    if seq[i] < min[0]:
      min = (seq[i], i)

  return min

#### 5. Echange les éléments d'indice i et j dans une liste
def echangeIndice(seq, to_place: int, to_deplace: int): # Returns a new sequence (list) object with permuted elements using the given indexes i & j
  new_seq = seq
  new_seq[to_place], new_seq[to_deplace] = new_seq[to_deplace], new_seq[to_place]
  return new_seq

#### 6. Tri par sélection une séquence
def triSelection(seq): # Returns a new sequence (list, tuple) sorted by selection
  if isinstance(seq, list):
    new_seq = seq.copy()
  else:
    new_seq = list(seq)

  print("Séquence Depart:", seq)

  for i in range(0, len(new_seq)):
    min = i
    for j in range(i+1, len(new_seq)):
      if new_seq[min] > new_seq[j]:
        min = j
    tmp = new_seq[i]
    new_seq[i] = new_seq[min]
    new_seq[min] = tmp

  if isinstance(seq, tuple):
    return tuple(new_seq)
  return new_seq

def triSelectionCorrected(seq):
  p = None
  t = None
  for i in range(0, len(seq)-1):
    p = positionMin(seq, i)
    t = echangeIndice(seq, p[1], 0+i)

  return t

### 2/

#### Résistance en série
def resistanceSerie(r1, r2): #
  return r1+r2

#### Résistance en parallèle
def resistanceParallele(r1, r2):
  return (r1*r2)/(r1+r2)

### 3/ Voir dans la zone d'affichage



## 2. Crible d'ÉRATOSTHÈNE
### Crée par compréhension une liste de nombres
def createListToMax(start, end):
  if end > 5000:
    end = 5000
  return [i for i in range(start, end+1)]

### Utilise la méthode d'Ératosthène afin de trouver
### des nombres premiers dans une liste
def methEratosthene(seq, show=True):
  for i in range(0, len(seq)):
    if seq[i] == 0 or seq[i] == 1:
      continue

    for j in range(i+1, len(seq)):
      if seq[j] == 0:
        continue

      if i+1 < len(seq):
        if seq[j]%seq[i] == 0:
          seq[j] = 0
  if show == True:
    print(seq)
  return seq

### Néttoie l'affichage en enlevant les 0 d'une liste
def getNonNullNbrs(seq):
  r = []
  for nbr in seq:
    if nbr != 0:
      r.append(nbr)
  return r

## 3. Décomposition en fatceurs premiers
def trouveDiviseurNbrPremiers(nbr):
  resultat = []
  seq_premiers = getNonNullNbrs(methEratosthene(createListToMax(1, nbr), False))
  for i in seq_premiers[1:]:
    if nbr%i == 0:
      resultat.append(i)
  return resultat

def trouveDiviseurNbrPremiersPuissances(nbr, debug=False):
  resultat = []
  seq_premiers = getNonNullNbrs(methEratosthene(createListToMax(1, nbr), False))
  for i in seq_premiers[1:]:
    x = 0
    while nbr%i == 0:
      x += 1
      nbr = nbr//i
    if x != 0:
      resultat.append((i, x))
  return resultat
