#!/usr/bin/python3

#-------------------------------------------------------------------------------------
## 1.
#-------------------------------------------------------------------------------------

## Boucle1.py
def boucle1():
	x=0
	while x<= 20:
		print(x)
		x += 2

## Boucle2.py
def boucle2():
	for i in range(30, 9, -3):
		print(i)


## Boucle3.py
def boucle3():
	x = 0
	while x<3:
		for i in range(0,2):
			print(x, i)
		x += 1
## Boucle4.py
def boucle4():
	x = 0
	while x < 6:
		for i in range(0,x):
			print(i, end=" ")
		print("\n")
		x+= 1


#------------------------------------------------------------------------------------
## 2.
#------------------------------------------------------------------------------------
r = [5,9,7,3,15,8]
## 1
def ScdShowValues(liste):

	for i in range(0, len(liste)):
		print(liste[i])
## 2
def ScdSum(liste):
	r = 0
	for i in range(0, len(liste)):
		r += liste[i]

	return r

## 3
def ScdAddLast(list):
	l = list.copy()
	l.append(4)
	return l

## 4
def ScdAddLastThenVerify(liste):
	l = liste.copy()
	l.append(4)
	if len(liste) != len(l):
		print("Bien ajouté")
	else:
		print("Non Ajouté")

## 5
def ScdNullifyMultiples(liste, nbr):
	l = liste.copy()
	for i in range(0, len(l)):
		if l[i]%nbr == 0:
			l[i] = 0
	return l


#------------------------------------------------------------------------------------
## 3.
#------------------------------------------------------------------------------------
s = "message secret"
s1 = "sésame ouvre-toi"
s2 = "LNLRNBCDWVNBBJPNLQROOAN"

## 1
def ThrdJump2(s):
	print(s[0:-1:2])

## 2
def Thrdreverse(s):
	print(s[-1:0:-1])
## 3
def ThrdASCII(s):
	r = ""
	for char in s:
		r += char
	return r

## 4
def ThrdDecode(s, spacing):
	alph = "abcdefghijklmnopqrstuvwxyz"
	r = ""
	for char in s:
		i = alph.index(char.lower())-spacing
		r += alph[i]
	return r

def ThrdDecodeASCII(s, spacing):
	r = ""
	for i in s:
		code=ord(i)-9
		if code<ord("A"):
			code += 26
		r += chr(code)
	return r

print(ThrdDecode(s2, 9))
print(ThrdDecodeASCII(s2, 9))
