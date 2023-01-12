from lxml import etree
from io import StringIO, BytesIO
import requests
import time
import json
import os

def checkDirIsPresent(directory: str, if_not_create: bool = False):
  if os.path.exists(os.path.abspath("./")+directory[1:]) == False:
    if if_not_create:
      if os.name == "nt":
        _dir = directory.replace('/', '\\')
      elif os.name == "posix":
        _dir = directory
      os.system(f"mkdir {_dir}")
      if checkDirIsPresent(directory):
       print(f"checkDirIsPresent: The directory '{directory}' has been successfully created")
  else:
    pass

  return True


def requestThenPrint(request: str):
  response = requests.get(request)
  print(response.text)


def requestThenReturn(request: str):
  response = requests.get(request)
  return response.text


def requestThenReturnAsFileObject(request: str):
  response = requests.get(request)
  response_text = response.text
  _file = BytesIO(bytes(response_text, encoding="utf-8"))
  return _file


def requestThenWrite(request: str, _dir: str = None):
  if _dir == None:
    if os.name == "nt":
      _dir = "./in/stats"

  response = requests.get(request)
  filename = response.url.strip().split("/")[-1]

  if checkDirIsPresent(_dir, if_not_create=True):

    with open(f"{_dir}/{filename}", "xt", encoding="utf-8") as fout:
      fout.write(response.text)

def parseXMLData(parking: str):
  state = ""
  opened = False  # valeur "globale" dans le namespace de la fonction
  free_places = 0  # valeur "globale" dans le namespace de la fonction
  # On supprime l'extension du fichier afin d'avoir juste le nom - Utilisation future probablement
  # Création d'un fichier temporaire
  with open("temp-file.log", "wt", encoding="utf-8") as f_temp:
    f_temp.write(parking)
  tree = etree.parse("temp-file.log")
  # Condition tertiaire afin d'avoir une valeur boulléenne
  date = tree.xpath("DateTime")[0].text
  opened = True if tree.xpath("Status")[0].text.lower() == "open" else False
  free_places = int(tree.xpath("Free")[0].text)
  places = int(tree.xpath("Total")[0].text)
  name = tree.xpath("Name")[0].text

  state = f"{name},{date},{opened},{free_places},{places}"

  # On nettoie notre fichier temporaire - Garbage Collector
  os.remove("temp-file.log")

  return state

def parseJSONData(response_data: str, type: str):
  ### type: "status" / "info" / "agenda"
  json_loaded = json.loads(response_data)
  returned_data = ""
  if type == "info":
    data = json_loaded["data"]
    for item in data["stations"]:
      ### id,name,places,lat,lon
      temp_data = f"{item['station_id']},{item['name']},{item['capacity']},{item['lat']},{item['lon']}"
      returned_data += temp_data + "\n"
  if type == "status":
    data = json_loaded["data"]
    for item in data["stations"]:
      ### id,date,nbr_availble,nbr_disabled,docks_avilable,is_installed,is_renting,is_returning
      temp_data = f"{item['station_id']},{item['last_reported']},{item['num_bikes_available']},{item['num_bikes_disabled']},{item['num_docks_available']},{item['is_installed']},{item['is_renting']},{item['is_returning']}"
      returned_data += temp_data + "\n"

  return returned_data

def isCSVHeaderPresentIfNotWrite(filename : str, csv_header: str):
  is_required_to_write = False
  entire_file = csv_header+"\n"

  if os.path.exists(filename):
    with open(filename, "rt", encoding="utf-8") as fin:
      content = fin.readlines()
      if len(content) >= 1:
        # print(content, csv_header, True if content[0].replace("\n", "") == csv_header else False)
        if content[0].replace("\n", "") == csv_header:
          is_required_to_write = False

        else:
          is_required_to_write = True
          # On ajoute donc l'en-tête CSV au fichier que l'on va réecrire
          content.insert(0, csv_header+"\n")
          entire_file = content

  if is_required_to_write:
    with open(filename, "wt", encoding="utf-8") as fout:
      fout.write("".join(entire_file))


def requestThenWriteDataHistory(request: str, type: str, data: str, _dir: str = None):
  if _dir == None:
    _dir = "./in/stats/csv"

  response = requests.get(request)

  _file = response.url.strip().split("/")[-1]

  if type == "XML":
    filename = response.url.strip().split("/")[-1].replace(".xml", ".csv")
  elif type == "JSON":
    filename = response.url.strip().split("/")[-1].replace(".json", ".csv")
  else:
    filename = response.url.strip().split("/")[-1]

  filename = filename.upper()

  if checkDirIsPresent(_dir, if_not_create=True):

    if data == "parking":
      isCSVHeaderPresentIfNotWrite(f"{_dir}/{filename}", "name,date,opened,free_places,places")
      with open(f"{_dir}/{filename}", "at", encoding="utf-8") as fout:
        fout.write(parseXMLData(response.text) + "\n")

    elif data == "velib_status":
      isCSVHeaderPresentIfNotWrite(f"{_dir}/{filename}", "id,date,nbr_available,nbr_disabled,docks_available,is_installed,is_renting,is_returning")
      with open(f"{_dir}/{filename}", "at", encoding="utf-8") as fout:
        fout.write(parseJSONData(response.text, type="status") + "\n")

    elif data == "velib_info":
      isCSVHeaderPresentIfNotWrite(f"{_dir}/{filename}", "id,name,places,lat,lon")
      with open(f"{_dir}/{filename}", "at", encoding="utf-8") as fout:
        fout.write(parseJSONData(response.text, type="info") + "\n")

    print("GET: ", _file, " - ", response.status_code, " - ", response.reason, " - ", "parsed successfully")


database = [
  #### Parkings voitures - Parser Done - To parse every minute
  [
    'FR_MTP_ANTI.xml', 'FR_MTP_COME.xml', 'FR_MTP_CORU.xml', 'FR_MTP_EURO.xml', 'FR_MTP_FOCH.xml',
    'FR_MTP_GAMB.xml', 'FR_MTP_GARE.xml', 'FR_MTP_TRIA.xml', 'FR_MTP_ARCT.xml', 'FR_MTP_PITO.xml',
    'FR_MTP_CIRC.xml', 'FR_MTP_SABI.xml', 'FR_MTP_GARC.xml', 'FR_MTP_SABL.xml', 'FR_MTP_MOSS.xml',
    'FR_STJ_SJLC.xml', 'FR_MTP_MEDC.xml', 'FR_MTP_OCCI.xml', 'FR_CAS_VICA.xml', 'FR_MTP_GA109.xml',
    'FR_MTP_GA250.xml', 'FR_CAS_CDGA.xml', 'FR_MTP_ARCE.xml', 'FR_MTP_POLY.xml'
  ],
  ### Parkings vélos - Parser done - To parse every minute
  [
   'station_information.json',
   'station_status.json'
  ],
  ### Utilisation Trams - Parser not done - To parse every minute
  [
    "TAM_MMM_TpsReel.csv",
  ],
  ### Comptage vélos + piétons - Parser not done - To parse every day
  [
    "MMM_MMM_GeolocCompteurs.csv"
  ],
  ### Agenda de la journée - Parser not done - To parse every day
  [
    "opendata-export-agenda-json"
  ]
]

start_timestamp = int(time.time())
jump = 0
time_to_run = 60
last_time_parsed = {
  "parking": 0, ### Every minute
  "velib_status": 0, ### Every minute
  "velib_info": 0, ### Every 12 hours
  "tram": 0, ### Every minute
  "comptage": 0, ### Every day
  "agenda": 0 ### Every 12 hours
}
print("Timestamp as of start:", start_timestamp)

while int(time.time()) <= start_timestamp+time_to_run-10:
  while int(time.time()) == start_timestamp+jump:
    for i in range(0, len(database)):
      ### TODO: Add a condition to check the last time parsed
      if i == 0:
        for j in range(0, len(database[i])):
          print(f"Request: {i}:{j}, {database[i][j]}", end=" ")
          requestThenWriteDataHistory(f"https://data.montpellier3m.fr/sites/default/files/ressources/{database[i][j]}", "XML", "parking")
      elif i == 1:
        for j in range(0, len(database[i])):
          print(f"Request: {i}:{j}, {database[i][j]}", end=" ")
          if j == 0:
            _type = "info"
          elif j == 1:
            _type = "status"
          requestThenWriteDataHistory(f"https://montpellier-fr-smoove.klervi.net/gbfs/en/{database[i][j]}", "JSON", f"velib_{_type}")

      elif i == 2:
        for j in range(0, len(database[i])):
          print(f"Request: {i}:{j}, {database[i][j]}", end=" ")
          requestThenWriteDataHistory(f"https://data.montpellier3m.fr/sites/default/files/ressources/{database[i][j]}", "CSV", "tram")

      elif i == 3:
        for j in range(0, len(database[i])):
          print(f"Request: {i}:{j}, {database[i][j]}", end=" ")
          requestThenWriteDataHistory(f"https://data.montpellier3m.fr/sites/default/files/ressources/{database[i][j]}", "CSV", "comptage")

      elif i == 4:
        for j in range(0, len(database[i])):
          print(f"Request: {i}:{j}, {database[i][j]}", end=" ")
          requestThenWriteDataHistory(f"https://www.montpellier3m.fr/{database[i][j]}", "JSON", "agenda")

    jump += 10
    print(f"\nOur current jump: {jump}, our limit jump: {time_to_run}")
print("Timestamp as of end:", int(time.time()), " - ", "Our scheme has been respected" if int(time.time())-start_timestamp == time_to_run else "Our scheme hasn't been respected")
