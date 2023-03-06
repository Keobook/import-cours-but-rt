from math import sqrt

_u = [0]

for n in range(1,4):
  u = (_u[n-1] + 3**n-1)  / (_u[n-1] - 3**(n+1))
  _u.append(u)
  print(f"u{n} = {u}")


## u[n+1] = u[n-1] + 2j u[n]
## Sortir les résultats sous la forme: un = x + j(y)
##
## u0 = 1
## u1 = 1
## u2 = u0 + 2j u1 = 1 + 2j1
## u3 = u1 + 2j u2 = 1 + 2j(1+ 2j) = 1 + 2j1 + 2j² = 1 + 2j -4 = -3 + j(2)
## u4 = u2 + 2j u3 = (1 + 2j1) + 2j(-3 + 2j) = 1 + 2j -6j - 4j² = 1-4 + 2j-6j = -3 - 4j = -3 + j(-4)
## u5 = u3 + 2j u4 = (-3 + 2j) + 2j(-3 - 4j) = -3 + 2j -6j - 8j² = -3-8j² + 2j-6j = -3+8 -4j = 5 - 4j

## u[n] = n-1 + 10j * u[n-1]
## u0 = 2
## u1 = 0 + 10j2 = 10j2 = 20j
## u2 = 1 + 10j(20j) = 1 + 200j² = 1 - 200 = -199
## u3 = 2 + 10j(-199) = 2 - 1990j 

## log(1+Un) - log(1-Un) = n
## 
