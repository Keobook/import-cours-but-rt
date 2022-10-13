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

### Utilise la méthode d'Ératosthène
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

###////////////////////////////////////////////////////////////////////////////////////
###
### Zone d'afichage
###
###////////////////////////////////////////////////////////////////////////////////////


print("Fonctions données dans l'énoncé:")
print("F0():", end=" ")
f0()
print("F1(5):", f1(5))
print(f"F2(5,2): {f2(5,2)}, F2(5): {f2(5)}", end="\n\n")

print("Exercice sur la TVA/TTC/HT")

### TVA: 20%
print(f"HT 124€ + TVA 20% ->", calcTTCPrice(124, 20))
print(f"HT 622€ + TVA 20% ->", calcTTCPrice(622, 20))
print(f"HT 3254.8€ + TVA 20% ->", calcTTCPrice(3254.8, 20), end="\n\n")

### TVA: 10%
print(f"HT 124€ + TVA 10% ->", calcTTCPrice(124, 10))
print(f"HT 622€ + TVA 10% ->", calcTTCPrice(622, 10))
print(f"HT 3254.8€ + TVA 10% ->", calcTTCPrice(3254.8, 10), end="\n\n")

## TVA: 5.5%
print(f"HT 124€ + TVA 5.5% ->", calcTTCPrice(124, 5.5))
print(f"HT 622€ + TVA 5.5% ->", calcTTCPrice(622, 5.5))
print(f"HT 3254.8€ + TVA 5.5% ->", calcTTCPrice(3254.8, 5.5), end="\n\n")

print("La valeur maximum d'une séquence:")
## Get Max
l3 = [5,6,7,45,22,32.5,622,32,4.8]
print(getMax(l3), end="\n\n")

print("La position de la plus petite valeur:")
## Get Position of Minimum
print(positionMin([2,5,1,4,3,10], 3))
print(positionMin([2,5,1,4,3,10], 1))
print(positionMin([2,5,1,4,3,10]), end="\n\n")

print("Échanger les éléments d'une séquence avec les indices i et j:")
## Exchange the elems of i and j index
print(echangeIndice([4,1,7,11,8], 1, 4), end="\n\n")

## Tri par sélection
print("Trier par sélection une séquence donnée:")
print("Séquence triée:", triSelection([4,6,1,1,2,8,6,7,24,12,11,-90,53,0,6]))
print("Séquence triée avec la bonne méthode:", triSelectionCorrected([4,6,1,1,2,8,6,7,24,12,11,-90,53,0,6]), end="\n\n")

# 3/ Calcul des résistances et la R totale avec des résistances différentes

## Calcul des résistances du montage avec résistance constante
print("Les résistances où rx=100:")
r1, r2, r3, r4, r5, r6, r7 = 100, 100, 100, 100, 100, 100, 100
print(r1, r2, r3, r4, r5, r6, r7)
r23 = resistanceSerie(r1, r2)
r123 = resistanceParallele(r1, r23)
r1234 = resistanceSerie(r123, r4)
r56 = resistanceParallele(r5, r6)
r123456 = resistanceSerie(r1234, r56)
r_montage = resistanceParallele(r123456, r7)
print(f"La résistance R du montage est de {r_montage} Ω", end="\n\n")

## Calcul des résistances du montage avec résistance incrémentée (100,200,300, etc.)
print("Les résistances où rx=100*x:")
r1, r2, r3, r4, r5, r6, r7 = 100, 200, 300, 400, 500, 600, 700
print(r1, r2, r3, r4, r5, r6, r7)
r23 = resistanceSerie(r1, r2)
r123 = resistanceParallele(r1, r23)
r56 = resistanceParallele(r5, r6)
r1234 = resistanceSerie(r123, r4)
r123456 = resistanceSerie(r1234, r56)
r_montage = resistanceParallele(r123456, r7)
print(f"La résistance R du montage est de {r_montage} Ω")

## Méthode Ératosthène
asked_seq = getNonNullNbrs(methEratosthene(createListToMax(2, 5000), False))
test_seq = getNonNullNbrs(methEratosthene(createListToMax(2, 20), False))
print("liste de test (2-20):", test_seq)
print("taille de la liste demandée (1-5000):", len(asked_seq), "chiffres premiers", end="\n\n")

## On trouve les diviseurs d'un nombre donné
print("Les diviseurs premiers du nombre 4030, sont:", trouveDiviseurNbrPremiers(4030))
print("Les diviseurs premiers et leur puissances du nombres 4030, sont:", trouveDiviseurNbrPremiersPuissances(4030))
print("Les diviseurs premiers et leur puissances du nombres 4032, sont:", trouveDiviseurNbrPremiersPuissances(4032))

print("Les diviseurs premiers et leur puissances du nombres 541204020, sont:", trouveDiviseurNbrPremiersPuissances(541204020))
print("Les diviseurs premiers et leur puissances du nombres 541204180, sont:", trouveDiviseurNbrPremiersPuissances(541204180))
print("Les diviseurs premiers et leur puissances du nombres 146669667139293303318642251838158394533529602659455, sont:", trouveDiviseurNbrPremiersPuissances(146669667139293303318642251838158394533529602659455))
print("Les diviseurs premiers et leur puissances du nombres 57191917829970203366904687080421927585621410177728758804240866015859751025476977064161324049412097812553348506582041789545712378495079387086022458464258720081718619718596587749133967250809910621760510205719832815068546540921397989526355238291011876456118755238882366831037649848449076383547435571679385599334795966330175131054152929807966925969524364438783789101847733060120973714061089127351200212033277439358733722879685611031421713026571419034952139825726497586591109499648075243998439963933636254358620565337806862706679435322863163574526086660870463620842147280194411421632657273898463803549539198930379254376059732815806091527108509098224942301779781488757867562131041507272679635190986910134983840499252832503597546973156117876902152928604743292911201119261552281204112020920481155734554449956771346970944529016099778787456709978478042346841439501861362012422887435962429399199467612419387305454345445373580524923411837001598580996235307619771083407652630271772377123672049879465798881173710964418886591999466780776334461168904032693016290175280004897355349174, sont:", trouveDiviseurNbrPremiersPuissances(57191917829970203366904687080421927585621410177728758804240866015859751025476977064161324049412097812553348506582041789545712378495079387086022458464258720081718619718596587749133967250809910621760510205719832815068546540921397989526355238291011876456118755238882366831037649848449076383547435571679385599334795966330175131054152929807966925969524364438783789101847733060120973714061089127351200212033277439358733722879685611031421713026571419034952139825726497586591109499648075243998439963933636254358620565337806862706679435322863163574526086660870463620842147280194411421632657273898463803549539198930379254376059732815806091527108509098224942301779781488757867562131041507272679635190986910134983840499252832503597546973156117876902152928604743292911201119261552281204112020920481155734554449956771346970944529016099778787456709978478042346841439501861362012422887435962429399199467612419387305454345445373580524923411837001598580996235307619771083407652630271772377123672049879465798881173710964418886591999466780776334461168904032693016290175280004897355349174))
