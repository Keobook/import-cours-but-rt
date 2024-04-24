import numpy as np
import matplotlib.pyplot as plt

# Les données mesurées
data= np.array([[31, 30, 26, 25, 21, 31, 27, 21, 25, 32 ],[40297, 39989, 38259, 35610, 35190, 37635, 37598, 33969, 37472, 38782 ]])
N=10
# On les mélange aléatoirement
rng=np.random.default_rng(42)   # fixer la graine pour tester votre programme avec les mêmes données
rng.shuffle(data,axis=1)
age=data[0]
salaire=data[1]

# données d'entrainement (1ère moitié du dataset)
age_tds=age[:int(N/2)]
salaire_tds=salaire[:int(N/2)]

# données de test (2nd moitié du dataset)
age_test=age[int(N/2):]
salaire_test=salaire[int(N/2):]

# Modèle  salaire_prédit = a1*age+a0 
# On cherche les paramètre a0 et a1 qui minimise l'erreur de prédiction quadratique moyenne sur les données d'apprentissage (training dataset)
# Utiliser la formule de stat pour calculer a0 et a1, les paramètres de la droite de régression

#a1 = covariance / variance
#a0 = y_moyen - a1 * x_moyen

# Affichage de la droite du prédicteur
x_values = np.array([age.min() - 1, age.max() + 1])
y_values = a0 + a1 * x_values
plt.plot(x_values, y_values, color='red', label="Estimateur")


# Calculer l'erreur d'apprentissage (erreur quadratique moyenne)
y_pred_tds  = a0+a1*age_tds
rmse_tds = np.sqrt(np.mean((y_pred_tds - salaire_tds)**2))
# Calculer l'erreur d'apprentissage (erreur quadratique moyenne)
y_pred_test = a0+a1*age_test
rmse_test = np.sqrt(np.mean((y_pred_test - salaire_test)**2))
# Calculer le score R2 = 1-SSR/SST
SSR=np.mean((y_pred_test - salaire_test)**2)
SST=np.mean((salaire_test-np.mean(salaire_test))**2)
scoreR2=1-SSR/SST

print("Le prédicteur du salaire est : salaire = ",a1, " * age + ",a0)
print("Erreur quadratique moyenne d'apprentissage ",rmse_tds)
print("Erreur quadratique moyenne de test ",rmse_test)
print("Coefficient de détermination (score R2) : ",scoreR2)


# Tracer les points des données d'apprentissage
plt.scatter(age_tds, salaire_tds,color="blue",label="Apprentissage")
# Tracer les points des données de test
plt.scatter(age_test, salaire_test,color="green",label="Test")
plt.xlabel("Age")
plt.ylabel("Salaire")
plt.legend()
plt.title("Régression linéaire entre salaire et age")
plt.show()
