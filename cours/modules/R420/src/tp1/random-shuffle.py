from os import (chdir, path, mkdir, listdir, devnull)
from typing import Union
import matplotlib.pyplot as plt ### pip install matplotlib
import numpy as np ### pip install numpy
import ffmpeg ### pip install ffmpeg-python
import json
import time
import cv2 ### pip install opencv-python

def linear_regression(seed: int = 42, samples_size: int = 10, mode: str = "cs", show: bool=True, computed_values: list = []) -> Union[list[list, list, list, list], None]:
  """Simple linear regression function.

  Args:
      seed (int, optional): The seed used to generate the data before the linear regression. Defaults to 42.
      samples_size (int, optional): The size of the sample used. Defaults to 10. 
      mode (str, optional): The working mode of this function. Defaults to "cs".  
          Are accepted as values:  
          - `c`: Computing values of the linear regression and returing a double array such as: [[array of values], [mean quadratic error, R2score], [min(y), max(y)], [min(x), min(y)]]  
          - `s`: Creating the Pyplot plot, the `computed_values` parameter is required, defaults `show` to true.  
          - `cs` Computing values of the linear regression and creating the Pyplot plot, uses the `show` parameter to know if the plot should be shown or not.
          - `p`: Works the same as if you were going to show the plot but defaults `show` to false and gives you the opportunity to print however your plot.
      show (bool, optional): Defines if the function should show the plot. Defaults to True. 
      computed_values (list, optional): Already computed values used only if `mode` == `s`. Defaults to [].

  Returns:
      Union[list[list, list, list, list], None]: Either the computed values or nothing (Depends on the mode)
  """

  plt.clf()

  if mode == "c" or mode == "cs":

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
    x_values = np.array([age.min() - 1, age.max() + 1])
    y_values = a0 + a1 * x_values


    #///////////////////////////////////////
    #
    # Error indexes Computing Section
    #
    #////////////////////////////////////////

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

  #///////////////////////////////////////
  #
  # Pyplot plot Section
  #
  #////////////////////////////////////////

  if mode == "s" or mode == "cs" or mode == "p":

    if mode == "s" or mode == "p":
      ### If we're in the `s` or `p` mode, only showing pre-computed data
      ### we need to unpack the parameter to set the required variables
      ### for the Pyplot plot.
      x_values, y_values, age_tds, salaire_tds, age_test, salaire_test = computed_values

      ### If we're showing the plot then defaults the show variable to True
      ### Otherwise, we're in the printing mode which defaults the show variable to False
      if mode == "s":
        show = True
      else:
        show = False


    # Affichage de la droite du prédicteur
    plt.plot(x_values, y_values, color='red', label="Estimateur")
    plt.scatter(age_tds, salaire_tds,color="blue",label="Apprentissage") # Tracer les points des données d'apprentissage
    plt.scatter(age_test, salaire_test,color="green",label="Test") # Tracer les points des données de test
    plt.xlabel("Age")
    plt.ylabel("Salaire")
    plt.title("Régression linéaire entre salaire et age")
    plt.legend()

    if show:
      plt.show()

    if mode == "p":
      return plt.ylim(), plt.xlim()
    

  if mode == "c" or mode == "cs":
    return [[x_values, y_values, age_tds, salaire_tds, age_test, salaire_test], [a1, a0, rmse_tds, rmse_test, scoreR2], plt.ylim(), plt.xlim()]



def shuffle(seed_range: tuple[int, int, int], samples_size_range: tuple[int, int, int]):

  def updateLimits(y_limits: list[int, int], x_limits: list[int, int], init: bool = False):

    if not init:
      xmin, xmax, ymin, ymax = all_predictions_max

      ymin = y_limits[0] if y_limits[0] < ymin else ymin
      ymax = y_limits[1] if y_limits[1] > ymax else ymax
      xmin = x_limits[0] if x_limits[0] < xmin else xmin
      xmax = x_limits[1] if x_limits[1] > xmax else xmax
    else:
      [ymin, ymax], [xmin, xmax] = y_limits, x_limits

    return xmin, xmax, ymin, ymax
  
  def addNewTimeEntry(task: str, start: float, end: float) -> None:
    time_data["data"].append({
      "task": task,
      "start": start,
      "end": end,
      "time": end - start
    })


  ### How works the shuffle function:
  ###
  ### We're computing the min and max values of each repetition (while also pre-computing the linear regression values)
  ### We're then creating every plot using the pre-computed data
  ### We're creating the video from the available plots

  data = {
    "title": "random-shuffle-data",
    "description": "Data from randomly shuffling a seed in order to test acurracy of the linear regression.",
    "data": []
  }
  time_data = {
    "title": "random-shuffle-time",
    "description": "Time taken to execute steps during the process of `random-shuffle.py`",
    "data": []
  }
  x, y = 0, 0
  data_values = []
  data_files = []
  all_predictions_max = [0, 0, 0, 0]

  total_start_time = time.time()
  start_time = time.time()
  end_time = None
  out_folder = "test"

  ###///////////////////////////////////////////////////////////////////////
  ###
  ### First Process - Linear regression values computing
  ###
  ###///////////////////////////////////////////////////////////////////////

  for seed in range(seed_range[0], seed_range[1], seed_range[2]):
    seed_data = {
      "seed": seed,
      "samples": []
    }

    for samples_size in range(samples_size_range[0], samples_size_range[1], samples_size_range[2]):
      print(f"Linear regression with seed: {seed} & sample's size: {samples_size}")

      values, predictions, y_limits, x_limits = linear_regression(seed, samples_size, "cs", False)
      

      if y == 0:
        all_predictions_max = updateLimits(y_limits, x_limits, True)
      else:
        all_predictions_max = updateLimits(y_limits, x_limits)

      sample_data = {
        "size": samples_size,
        "a1": predictions[0],
        "a0": predictions[1],
        "rmse": {
          "learning": predictions[2],
          "test": predictions[3]
        },
        "r2-score": predictions[4]
      }

      seed_data["samples"].append(sample_data)
      data_values.append(values)
      data_files.append(f"linear-regression-{seed:03}-{samples_size:04}.png")
      y += 1

    data["data"].append(seed_data)
    x += 1

  end_time = time.time()
  addNewTimeEntry("step-1", start_time, end_time)

  ### Checking if the path exists
  if not path.exists(f"./{out_folder}/"):
    ### If not, creating the directory
    mkdir(f"./{out_folder}/")

  ### JSON report of the seed shuffle
  json.dump(data, open(f"./{out_folder}/random-data-shuffle.json", "wt", encoding="utf-8"))

  print(f"Step 1 Completed - We generated {y} predictions for {x} seeds in {end_time - start_time:.4f} seconds !")

  ###///////////////////////////////////////////////////////////////////////
  ###
  ### Second Process - Graphs creation
  ###
  ###///////////////////////////////////////////////////////////////////////

  start_time = time.time()

  print("Creating graphs...")
  for i in range(0, len(data_values)):

    linear_regression(computed_values=data_values[i], mode="p")

    plt.ylim(all_predictions_max[2:])
    plt.xlim(all_predictions_max[:2])

    plt.savefig(f"./{out_folder}/{data_files[i]}")

  end_time = time.time()
  addNewTimeEntry("step-2", start_time, end_time)

  print("graphs created!")
  print(f"Step 2 completed in {end_time - start_time:.4f} seconds !")


  ###///////////////////////////////////////////////////////////////////////
  ###
  ### Third Process - Video Compilation
  ###
  ###///////////////////////////////////////////////////////////////////////

  start_time = time.time()

  print("Compiling the video...")

  create_video(out_folder, 30)

  end_time = time.time()

  addNewTimeEntry("step-3", start_time, end_time)

  print(f"Step 3 completed in {end_time - start_time:.4f} seconds!")

  ###///////////////////////////////////////////////////////////////////////
  ###
  ### Fourth Process - Video Compression
  ###
  ###///////////////////////////////////////////////////////////////////////

  start_time = time.time()

  print("Compressing the video... Please Wait")
  compress_video(f'{out_folder}/linear-regression.avi', 'linear-regression.mp4', 50 * 1000)
  
  end_time = time.time()
  addNewTimeEntry("step-4", start_time, end_time)
  
  print(f"Step 4 completed in {end_time - start_time:.4f} seconds!")


  total_end_time = time.time()
  print(f"Completed all processes in {total_end_time - total_start_time}")

  json.dump(time_data, open(f"./{out_folder}/random-data-shuffle-time.json", "wt", encoding="utf-8"))


def create_video(folder: str, fps: int = 10):
  image_folder = folder
  video_name = f'linear-regression-{fps}.avi'

  images = [img for img in listdir(image_folder) if img.endswith(".png")]

  if images != []:

    frame = cv2.imread(path.join(image_folder, images[0]))
    height, width, layers = frame.shape

    video = cv2.VideoWriter(video_name, 0, fps, (width,height))

    for image in images:
      print(f"Adding image '{image}' into the video...")
      video.write(cv2.imread(path.join(image_folder, image)))

    cv2.destroyAllWindows()
    chdir(image_folder)
    video.release()
    print("Video compiled")
  else:
    raise Exception("No image found!")


### @credits: https://stackoverflow.com/a/64439347/13025136
def compress_video(video_full_path, output_file_name, target_size):
    # Reference: https://en.wikipedia.org/wiki/Bit_rate#Encoding_bit_rate
    min_audio_bitrate = 32000
    max_audio_bitrate = 256000

    probe = ffmpeg.probe(video_full_path)
    # Video duration, in s.
    duration = float(probe['format']['duration'])
    # Audio bitrate, in bps.
    audio_bitrate = float(next((s for s in probe['streams'] if s['codec_type'] == 'audio'), None)['bit_rate'])
    # Target total bitrate, in bps.
    target_total_bitrate = (target_size * 1024 * 8) / (1.073741824 * duration)

    # Target audio bitrate, in bps
    if 10 * audio_bitrate > target_total_bitrate:
        audio_bitrate = target_total_bitrate / 10
        if audio_bitrate < min_audio_bitrate < target_total_bitrate:
            audio_bitrate = min_audio_bitrate
        elif audio_bitrate > max_audio_bitrate:
            audio_bitrate = max_audio_bitrate
    # Target video bitrate, in bps.
    video_bitrate = target_total_bitrate - audio_bitrate

    i = ffmpeg.input(video_full_path)
    ffmpeg.output(i, devnull, **{'c:v': 'libx264', 'b:v': video_bitrate, 'pass': 1, 'f': 'mp4'}).overwrite_output().run()
    ffmpeg.output(i, output_file_name, **{'c:v': 'libx264', 'b:v': video_bitrate, 'pass': 2, 'c:a': 'aac', 'b:a': audio_bitrate}).overwrite_output().run()

shuffle([10, 500, 8], [10, 4000, 16])