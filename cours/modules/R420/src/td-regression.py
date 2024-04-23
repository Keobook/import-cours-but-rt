import numpy as np
import matplotlib.pyplot as plt

n = 10
age = np.array([31, 30, 26, 25, 21, 31, 27, 21, 25, 32 ])
salaire = np.array([40297, 39989, 38259, 35610, 35190, 37635, 37598, 33969, 37472, 38782 ])

# Afficher les premières lignes des données
print("Age:", age[:10])
print("Salaire :", salaire[:10])

# salaire = a1*age+a0 calcul de a0 et a1
xm = np.mean(age)
ym = np.mean(salaire)

a1=np.sum((np.sum(age))*(-xm)) / np.sum((np.sum(salaire)-ym)**2)
a0=np.sum(salaire)-xm

print(f"a1: {a1}, a0: {a0}")

x_values = np.array([age.min() - 1, age.max() + 1])
y_values = a0 + a1 * x_values
plt.plot(x_values, y_values, color='red', label="Estimateur")

# Tracer les points des données
plt.scatter(age, salaire)
plt.xlabel("Age")
plt.ylabel("Salaire")
plt.legend()
plt.title("Régression linéaire entre salaire et age")
plt.show()