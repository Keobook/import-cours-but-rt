import json
import rich
from os import system as sys
from collections import Counter


### Let's Set-up what we need

records = []

with open("./src/eve.json", "rt") as fin:
  for json_obj in fin:
    enreg = json.loads(json_obj)
    records.append(enreg)

def quest_1():
  for elem in records[:3]:
    rich.print_json(data=elem)

def quest_2():
  ### Comment fonctionne la commande 2
  ### ...

  alertes = []
  for ligne in records:
    try:
      alerte = ligne['alert']['signature']
      alertes.append(alerte)
    except KeyError:
      pass

  ### uniq -c
  alertCounter = Counter(alertes)

  for alerte, nbr in alertCounter.most_common():
    print(f'{nbr} "{alerte}"')
