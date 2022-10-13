#!/usr/bin/env python3

### Ce module est créé afin de répondre au 2. du TD3 de R107
### Il copie les fonctions présentes dans le fichier père (r107-td3.py)

## 1
def CalcTTCPrice(prix, tva):
    return float(prix*(1+tva/100),)
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
### On verra ce que le prof fera
