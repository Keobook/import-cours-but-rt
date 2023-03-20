import subprocess
from subprocess import STDOUT
import jc.parsers.ss as ss_parse
import json
import rich

## 1.2 - JSON + SS

cmd_output = open("./ss-tun.log", "rt", encoding="utf-8").read()

state_list = ["ESTAB","LISTENING","FIN-WAIT-1","FIN-WAIT-2","TIME-WAIT","CLOSED","CLOSE-WAIT","SYNC-SENT","SYNC-RECV","LAST-ACK","CLOSING"]


# cmd_output = subprocess.check_output(['ss', '-tun'], stderr=STDOUT)
data = ss_parse.parse(cmd_output)

count = 0

for state in state_list:
  count = 0
  for element in data:
    if state == element["state"]:
      count += 1

  print(f"état: {state}, nombre d'entrées dans cet état: {count}")

## 2.1 + RIS

ris_record = []

with open('./src/materiel/ris.json', 'r') as fin:
  for json_obj in fin:
    record = json.loads(json_obj)
    ris_record.append(record)

for record in ris_record[:3]:
  print(record['data']['peer_asn'])

# 2.2 + médianes
