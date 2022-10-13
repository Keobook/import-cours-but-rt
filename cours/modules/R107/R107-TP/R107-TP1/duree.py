#!/usr/bin/python3

## Convertir Jour,Heures,Minutes en Secondes
def Quest15(j, h, m, s):
    x = (j*24)*3600
    y = h*3600
    z = m*60
    r = x+y+z+s
    return r

## Convertir Secondes en Jour,Heures,Minutes
def Quest16(t):
    j = int(t/(24*3600))
    h = int((t-j*24*3600)/3600)
    m = int((t-j*24*3600-h*3600)/60)
    s = t-j*24*3600 - h*3600 - m*60
    return (j, h, m, s)


print(Quest15(1, 3, 26, 5))
print(Quest16(654321))