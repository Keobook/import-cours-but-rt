import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS

bucket = "sae-12"
token = "e3I0e6my88_8RrWfzgdwYKFGUduSm7jSqxxqYl7Wl58b6uGeoAfrXFMjnb1T48iTl3Q-m4cqmvt6oh9fY57DHA=="
org = "iut-students"
url = "188.166.151.235:8086"

client = influxdb_client.InfluxDBClient(
   url=url,
   token=token,
   org=org
)
write_api = client.write_api(write_options=SYNCHRONOUS)
##name,date,export_date,opened,free_places,places##
liste=["CDGA","2023-01-12T09:34:52",None,True,224,260]

import requests

def requestThenPrint(request: str):
  response = requests.get(request)
  print(response.text)


parkings = [
  'FR_MTP_ANTI.CSV','FR_MTP_COME.CSV','FR_MTP_CORU.CSV','FR_MTP_EURO.CSV','FR_MTP_FOCH.CSV',
  'FR_MTP_GAMB.CSV','FR_MTP_GARE.CSV','FR_MTP_TRIA.CSV','FR_MTP_ARCT.CSV','FR_MTP_PITO.CSV',
  'FR_MTP_CIRC.CSV','FR_MTP_SABI.CSV','FR_MTP_GARC.CSV','FR_CAS_SABL.CSV','FR_MTP_MOSS.CSV',
  'FR_STJ_SJLC.CSV','FR_MTP_MEDC.CSV','FR_MTP_OCCI.CSV','FR_CAS_VICA.CSV','FR_MTP_GA109.CSV',
  'FR_MTP_GA250.CSV','FR_CAS_CDGA.CSV','FR_MTP_ARCE.CSV','FR_MTP_POLY.CSV'
]

for parking in parkings :
  print("Reading:", parking, end=";")
  with open(f"in/stats/csv/{parking}", "rt", encoding="utf-8") as fin:
    fin = fin.readlines()
    if fin[1].strip().replace("\n", "") == "name,date,opened,free_places,places":
      print("File has old header", end=";")
      fin.pop(1)
    else:
      print("File hasn't old header")
    for line in fin[1:]:
      curr_data = line.strip().split(",")
      p = influxdb_client.Point("parkings")
      if curr_data[2] == "":
        curr_data[2] = None

      p.field("name", curr_data[0])
      p.field("export_date", curr_data[1])
      p.field("real_date", curr_data[2])
      p.field("is_opened", curr_data[3])
      p.field("availability", int(curr_data[4]))
      p.field("total_places", int(curr_data[5]))
      if curr_data[2] == None:
        p.time(curr_data[1])
      else:
        p.time(curr_data[2])
      write_api.write(bucket=bucket, org=org, record=p)
