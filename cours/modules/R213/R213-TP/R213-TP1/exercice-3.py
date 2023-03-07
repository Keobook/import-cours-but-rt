def puissance(x,n, i=1):
    if n>0:
        r = x * puissance(x, n-1, i+1)
        print(f"Appel {i}: puissance({x}, {n}) = {r}")
        return r
    else:
        return 1


def getRecursiveSequence(n: int, u: float | int = 0, a: float | int = 0, b: float | int = 0, debug: bool = False) -> tuple[int, int]:
    ### u[n+1] = a*u[n] + (a + b)
    ### With u[0] = 0
    if debug:
        print(f"Appel {n}: u = {u}, a = {a}, b = {b}")
    while n > 0:
        n, u = getRecursiveSequence(n-1, u, a, b)
    u = a*u + (a + b)
    return n, u

def showResults(results: tuple[int, int], n: int) -> str:
    _, u = results
    return f"u{n} = {u}"

a, b = 6, 7

print(showResults(getRecursiveSequence(4, a=a, b=b), 5))
print(showResults(getRecursiveSequence(9, a=a, b=b), 10))
