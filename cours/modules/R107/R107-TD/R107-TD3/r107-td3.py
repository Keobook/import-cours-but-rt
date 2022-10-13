#!/usr/bin/env python3

#------------------------------------------------------------------------------------
## 1. Fonctions:
#------------------------------------------------------------------------------------

## 1
def CalcTTCPrice(prix, tva):
    return float(prix*(1+tva/100))
## 2
def CalcAmountTax(prix, tva):
    return prix/(1+tva/100)
## 3
def getMax(seq):
    max = seq[0]
    for i in seq:
        if i > max:
            max = i

    return max

## 4
def positionMin(seq, offset=0):
    min = (seq[offset], 0)
    for i in range(offset, len(seq)):
        if seq[i] < min[0]:
            min = (seq[i], i)

    return min[1]

## 5
def echange(seq, i, j):
    seq[i], seq[j] = seq[j], seq[i]
    return seq

## 6



### TVA: 20%

#print(f"HT 124€ + TVA 20% ->", CalcTTCPrice(124, 20))
#print(f"HT 622€ + TVA 20% ->", CalcTTCPrice(622, 20))
#print(f"HT 3254.8€ + TVA 20% ->", CalcTTCPrice(3254.8, 20))

### TVA: 10%
#print(f"HT 124€ + TVA 10% ->", CalcTTCPrice(124, 10))
#print(f"HT 622€ + TVA 10% ->", CalcTTCPrice(622, 10))
#print(f"HT 3254.8€ + TVA 10% ->", CalcTTCPrice(3254.8, 10))

## TVA: 5.5%
#print(f"HT 124€ + TVA 5.5% ->", CalcTTCPrice(124, 5.5))
#print(f"HT 622€ + TVA 5.5% ->", CalcTTCPrice(622, 5.5))
#print(f"HT 3254.8€ + TVA 5.5% ->", CalcTTCPrice(3254.8, 5.5))

## Get Max
#l3 = [5,6,7,45,22,32.5,622,32,4.8]
#print(getMax(l3))

## Get Position of Minimum
#print(positionMin([2,5,1,4,3,10], 3))
#print(positionMin([2,5,1,4,3,10], 1))
#print(positionMin([2,5,1,4,3,10]))

## Exchange the elems of i and j index
#print(echange([4,1,7,11,8], 1, 4))

#------------------------------------------------------------------------------------
## 2. Modules Python
#------------------------------------------------------------------------------------
