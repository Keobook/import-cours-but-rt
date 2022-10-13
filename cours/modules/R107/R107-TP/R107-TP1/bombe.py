#!/usr/bin/python3

## Désamorcer une bombe
def desamorcer(nbr_serie):
    x = str(nbr_serie)
    u, n = int(x[:3]), int(x[3:])
    for i in range(0, n):
        print(f"{u} -> ", end="")
        y = str(u*13)
        u = int(y[len(y)-3:])
        print(f"{y} -> {u}")
    
    return u

print("\nLe fil à couper est le:", desamorcer(123456))