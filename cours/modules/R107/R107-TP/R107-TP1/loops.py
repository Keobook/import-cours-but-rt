#!/usr/bin/python3

## Boucle des étoiles en horizontal
def StarLoop(_list):
    for i in _list:
        print("*"*i)

    print("\n", end="")

## Boucle des étoiles en vertical
def VerticalStarLoop(_list):
    x = max(_list)
    t = [[[" "]*(x-_list[i])+["*"]*_list[i]] for i in range(0, len(_list))]
    for i in range(0, x):
        for j in t:
            print(j[0][i], end="")
        print()

StarLoop([5,8,3,7,11,2])
print("-"*20, "\n")
VerticalStarLoop([5,8,3,7,11,2])
