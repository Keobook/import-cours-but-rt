#!/usr/bin/python3

## Conversion de F° en C°
def FarhenheitToCelsius(temp):
    return (temp-32)*5/9


x = int(input("Entrez votre température en F°: "))

print(f"Votre température en C°: {FarhenheitToCelsius(x)}")