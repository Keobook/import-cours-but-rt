import os
import subprocess
import importlib
from io import StringIO, BytesIO
import time

try:
  importlib.import_module("lxml")
except:
  print("lxml is not installed, installing it now...")
  if subprocess.check_output("whereis pip", shell=True, text=True).strip().split(":")[-1].replace("\n", "") == "":
    os.system("sudo apt install -y pip")

  os.system("pip install lxml")

try:
  importlib.import_module("requests")
except:
  print("requests is not installed, installing it now...")
  os.system("pip install requests")

try:
  importlib.import_module("json")
except:
  print("json is not installed, installing it now...")
  os.system("pip install json")

from lxml import etree
import requests
import json


def getCurrentDateTime():
  return int(time.time())


def getCurrentFormattedDateTime():
  return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

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

def renderInLine(text):
  text = text.replace("\n", "\t")
  return text

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
  try:
    json_loaded = json.loads(response_data)
  except json.decoder.JSONDecodeError:
    print("Error while parsing JSON data", response_data)
    return None
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

  if type == "agenda":
    data = json_loaded["agenda"]
    for i in range(0, len(data)):
      curr_data = json_loaded["agenda"][i]["event"]
      ### event_id,titre,vignette_src,field_date,description,field_communes,field_lieu,field_access,field_thematique,x,y,url
      temp_data = f"{curr_data['nid']},{curr_data['titre'],{curr_data['field_vignette']['src']}},{curr_data['field_date']},'{renderInLine(curr_data['description'])}',{curr_data['field_communes']},{curr_data['field_lieu']},{curr_data['field_acces']},{curr_data['field_thematique']},{curr_data['x']},{curr_data['y']},{curr_data['url']}"
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
    filename = response.url.strip().split("/")[-1]
    if ".json" in filename:
      filename = filename.replace(".json", ".csv")
    else:
      filename += ".csv"
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

    elif data == "tram":
      isCSVHeaderPresentIfNotWrite(f"{_dir}/{filename}", "course,stop_code,stop_id,stop_name,route_short_name,trip_headsign,direction_id,departure_time,is_theorical,delay_sec,dest_ar_code,course_sae")
      with open(f"{_dir}/{filename}", "at", encoding="utf-8") as fout:
        fout.write(response.text + "\n")

    elif data == "agenda":
      isCSVHeaderPresentIfNotWrite(f"{_dir}/{filename}", "event_id,titre,vignette_src,field_date,description,field_communes,field_lieu,field_access,field_thematique,x,y,url")
      with open(f"{_dir}/{filename}", "at", encoding="utf-8") as fout:
        fout.write(parseJSONData(response.text, type="agenda") + "\n")

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
  ### Agenda de la journée - Parser not done - To parse every day
  [
    "opendata-export-agenda-json"
  ]
]

start_timestamp = int(time.time())
jump = 0
second = 1
minute = 60
hour = 3600
day = 86400
time_to_run = 604800
last_time_parsed = {
  "parking": 0, ### Every minute
  "velib_status": 0, ### Every minute
  "velib_info": 0, ### Every 12 hours
  "tram": 0, ### Every minute
  "comptage": 0, ### Every day
  "agenda": 0 ### Every 12 hours
}
try:
  print("Timestamp as of start:", start_timestamp, "Time to run:", time_to_run)

  while getCurrentDateTime() <= start_timestamp+time_to_run:
    for i in range(0, len(database)):
      ### TODO: Add a condition to check the last time parsed
      if i == 0: ### Parkings Voitures
        if last_time_parsed["parking"] == 0 or last_time_parsed["parking"]+minute <= getCurrentDateTime():
          for j in range(0, len(database[i])):
            _link = f"https://data.montpellier3m.fr/sites/default/files/ressources/{database[i][j]}"
            print(f"Request: {i}:{j}, {database[i][j]} - [{getCurrentFormattedDateTime()}/{getCurrentDateTime()}] - {_link}", end=" ")
            requestThenWriteDataHistory(_link, "XML", "parking")

          last_time_parsed["parking"] = getCurrentDateTime()

      elif i == 1: ### Vélos status / Vélos infos
          for j in range(0, len(database[i])):
            _link = f"https://montpellier-fr-smoove.klervi.net/gbfs/en/{database[i][j]}"
            print(f"Request: {i}:{j}, {database[i][j]} - [{getCurrentFormattedDateTime()}/{getCurrentDateTime()}] - {_link}", end=" ")

            if j == 0: ### Vélos infos
              _type = "info"
              if last_time_parsed["velib_status"] == 0 or last_time_parsed["velib_status"]+minute <= getCurrentDateTime():
                requestThenWriteDataHistory(_link, "JSON", f"velib_{_type}")
                last_time_parsed["velib_status"] = getCurrentDateTime()

            elif j == 1: ### Vélos status
              _type = "status"
              if last_time_parsed["velib_info"] == 0 or last_time_parsed["velib_info"]+(12*hour) <= getCurrentDateTime():
                requestThenWriteDataHistory(_link, "JSON", f"velib_{_type}")
                last_time_parsed["velib_info"] = getCurrentDateTime()

      elif i == 2: ### Vélos tram
        if last_time_parsed["tram"] == 0 or last_time_parsed["tram"]+minute <= getCurrentDateTime():
          for j in range(0, len(database[i])):
            _link = f"https://data.montpellier3m.fr/sites/default/files/ressources/{database[i][j]}"
            print(f"Request: {i}:{j}, {database[i][j]} - [{getCurrentFormattedDateTime()}/{getCurrentDateTime()}] - {_link}", end=" ")
            requestThenWriteDataHistory(_link, "CSV", "tram")

        last_time_parsed["tram"] = getCurrentDateTime()

      elif i == 3: ### Agenda de la journée
        if last_time_parsed["agenda"] == 0 or last_time_parsed["agenda"]+(12*hour) <= getCurrentDateTime():
          for j in range(0, len(database[i])):
            _link = f"https://www.montpellier3m.fr/{database[i][j]}"
            print(f"Request: {i}:{j}, {database[i][j]} - [{getCurrentFormattedDateTime()}/{getCurrentDateTime()}] - {_link}", end=" ")
            requestThenWriteDataHistory(_link, "JSON", "agenda")

          last_time_parsed["agenda"] = getCurrentDateTime()

    jump += minute
    print(f"\nOur current jump: {jump}, our limit jump: {time_to_run}")
    time.sleep(120)
  print("Timestamp as of end:", int(time.time()), " - ", "Our scheme has been respected" if int(time.time())-start_timestamp == time_to_run else "Our scheme hasn't been respected")

except KeyboardInterrupt:
  print("\n\x1b[31m KeyboardInterrupted - Exiting \x1b[0m \n")
