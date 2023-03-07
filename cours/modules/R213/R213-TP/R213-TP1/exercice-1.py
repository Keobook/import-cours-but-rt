u = 6
a = 6
b = 7

for n in range(1, 11):
    u = u + (a+b)
    print(f"u{n} = {u}")

print("\n---", end="\n\n")
u = 6

for n in range(1, 6):
    u = u * (a+b)
    print(f"v{n} = {u}")

print(f"\n v5 = {6*(6+7)**5}")
