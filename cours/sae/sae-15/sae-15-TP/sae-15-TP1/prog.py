import requests
import os

def checkDirIsPresent(directory: str, if_not_create: bool = False):
  if os.path.exists(os.path.abspath("./")+directory) == False:
    if if_not_create:
      windir = directory.replace('/', '\\')
      os.system(f"mkdir -p {windir}")
      if checkDirIsPresent(directory):
       print(f"checkDirIsPresent: The directory '{directory}' has been successfully created")

  return True

def requestThenPrint(request: str):
  response = requests.get(request)
  print(response.text)

def requestThenWrite(request: str, _dir: str = None):
  if _dir == None:
    _dir = "./in/stats"

  response = requests.get(request)
  filename = response.url.strip().split("/")[-1]

  if checkDirIsPresent(_dir, if_not_create=True):

    with open(f"{_dir}/{filename}", "xt", encoding="utf-8") as fout:
      fout.write(response.text)

### Question 1
print("Question 1:")
requestThenWrite("https://data.montpellier3m.fr/sites/default/files/ressources/FR_MTP_COME.xml")



## Question 2
print("\n\nQuestion 2:")
parkings = ['FR_MTP_ANTI.xml','FR_MTP_COME.xml','FR_MTP_CORU.xml','FR_MTP_EURO.xml','FR_MTP_FOCH.xml','FR_MTP_GAMB.xml','FR_MTP_GARE.xml','FR_MTP_TRIA.xml','FR_MTP_ARCT.xml','FR_MTP_PITO.xml','FR_MTP_CIRC.xml','FR_MTP_SABI.xml','FR_MTP_GARC.xml','FR_CAS_SABL.xml','FR_MTP_MOSS.xml','FR_STJ_SJLC.xml','FR_MTP_MEDC.xml','FR_MTP_OCCI.xml','FR_CAS_VICA.xml','FR_MTP_GA109.xml','FR_MTP_GA250.xml','FR_CAS_CDGA.xml','FR_MTP_ARCE.xml','FR_MTP_POLY.xml']

for parking in parkings :
  requestThenPrint(f"https://data.montpellier3m.fr/sites/default/files/ressources/{parking}")
