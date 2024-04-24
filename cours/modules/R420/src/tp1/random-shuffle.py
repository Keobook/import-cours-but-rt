import numpy as np
import matplotlib.pyplot as plt
import json

def ai(seed: int, samples_size: int = 10):
  # Les données mesurées
  data= np.array([[31, 30, 26, 25, 21, 31, 27, 21, 25, 32 ],[40297, 39989, 38259, 35610, 35190, 37635, 37598, 33969, 37472, 38782 ]])
  N=samples_size

  # On les mélange aléatoirement
  rng=np.random.default_rng(seed)   # fixer la graine pour tester votre programme avec les mêmes données
  rng.shuffle(data,axis=1)
  age=rng.integers(low=20, high=40, size=N)
  salaire = 35000 + 250*age + rng.normal(0, 1000, size=N)

  # données d'entrainement (1ère moitié du dataset)
  age_tds=age[:int(N/2)]
  salaire_tds=salaire[:int(N/2)]

  # données de test (2nd moitié du dataset)
  age_test=age[int(N/2):]
  salaire_test=salaire[int(N/2):]

  # Modèle  salaire_prédit = a1*age+a0 
  # On cherche les paramètre a0 et a1 qui minimise l'erreur de prédiction quadratique moyenne sur les données d'apprentissage (training dataset)
  # Utiliser la formule de stat pour calculer a0 et a1, les paramètres de la droite de régression

  x_moyen = age.mean()
  y_moyen = salaire.mean()

  cov = np.sum((age - x_moyen) * (salaire - y_moyen))
  variance = np.sum((age - x_moyen)**2)

  a1 = cov / variance
  a0 = y_moyen - a1 * x_moyen

  print(variance, cov, a1)

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

  # Tracer les points des données d'apprentissage
  plt.scatter(age_tds, salaire_tds,color="blue",label="Apprentissage")
  # Tracer les points des données de test
  plt.scatter(age_test, salaire_test,color="green",label="Test")
  plt.xlabel("Age")
  plt.ylabel("Salaire")
  plt.legend()
  plt.title("Régression linéaire entre salaire et age")

  return [a1, a0, rmse_tds, rmse_test, scoreR2]


def shuffle(seed_range: tuple[int, int, int], samples_size_range: tuple[int, int, int]):

  data = {
    "title": "random-shuffle",
    "description": "Randomly shuffles a seed in order to test acurracy of the linear regression.",
    "data": []
  }
  x = 0

  for seed in range(seed_range[0], seed_range[1], seed_range[2]):
    seed_data = {
      "seed": seed,
      "samples": []
    }

    for samples_size in range(samples_size_range[0], samples_size_range[1], samples_size_range[2]):

      print(f"Linear regression with seed: {seed} & sample's size: {samples_size}")

      ai_result = ai(seed, samples_size)

      sample_data = {
        "size": samples_size,
        "a1": ai_result[0],
        "a0": ai_result[1],
        "rmse": {
          "learning": ai_result[2],
          "test": ai_result[3]
        },
        "r2-score": ai_result[4]
      }

      seed_data["samples"].append(sample_data)


      ### PNG figure
      plt.savefig(f"./out/linear-regression-{seed:03}-{samples_size:04}.png")
      plt.clf()

    data["data"].append(seed_data)

    x += 1

  ### JSON report of the seed shuffle
  json.dump(data, open("./out/random-data-shuffle.json", "wt", encoding="utf-8"))

  print(f"We generated {x} samples!")

shuffle([10, 500, 8], [10, 4000, 16])