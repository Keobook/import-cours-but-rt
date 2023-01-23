import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS
import datetime

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


a = int("1674119306")
print (a,datetime.datetime.fromtimestamp(a))

timestamp_to_date_time = datetime.datetime.fromtimestamp(a/1000000000).strftime('%Y-%m-%d %H:%M:%S,%f')
print(timestamp_to_date_time)





# velib_infos = info[f"{i}"]
#p.field()....
# p.field("name", velib_infos[0])
# p.filed("position", (velib_infos[2], velib_infos[3]))


info[f"{i}"]


info = {
  "1": ("Rue Jules Ferry - Gare Saint-Roch","12","43.605366","3.881346")
}

idexe = ("rue","nombre","latittude","longitude")
id001 = ("Rue Jules Ferry - Gare Saint-Roch","12","43.605366","3.881346")
id002 = ("Comédie","24","43.608148","3.878778")
id003 = ("Esplanade","32","43.609478","3.881293")
id004 = ("Hôtel de Ville","16","43.599088","3.894866")
id005 = ("Corum","12","43.613989","3.8816")
id006 = ("Place Albert 1er - St Charles","27","43.616768","3.873375")
id007 = ("Foch","8","43.610989","3.873345")
id008 = ("Halles Castellane","12","43.609935","3.877208")
id009 = ("Observatoire","8","43.606081","3.876931")
id010 = ("Rondelet","16","43.603038","3.875796")
id011 = ("Plan Cabanes","12","43.608491","3.868389")
id012 = ("Boutonnet","12","43.622629","3.868375")
id013 = ("Emile Combes","8","43.616742","3.87998")
id014 = ("Beaux-Arts","28","43.616698","3.884981")
id015 = ("Les Aubes","8","43.618692","3.893844")
id016 = ("Antigone centre","16","43.607942","3.890634")
id017 = ("Médiathèque Emile Zola","16","43.608218","3.89314")
id018 = ("Nombre d'Or","16","43.607859","3.886644")
id019 = ("Louis Blanc","16","43.614642","3.877648")
id020 = ("Gambetta","8","43.607106","3.870693")
id021 = ("Port Marianne","16","43.60032","3.89851")
id022 = ("Clemenceau","12","43.603539","3.872394")
id023 = ("Les Arceaux","16","43.611991","3.867157")
id024 = ("Cité Mion","8","43.601143","3.884373")
id025 = ("Nouveau Saint-Roch","8","43.599817","3.875757")
id026 = ("Renouvier","8","43.603553","3.867884")
id027 = ("Odysseum","8","43.603727","3.918979")
id028 = ("Saint-Denis","8","43.605021","3.875065")
id029 = ("Richter","16","43.603424","3.899263")
id030 = ("Charles Flahault","8","43.618762","3.865971")
id031 = ("Voltaire","8","43.603767","3.888659")
id032 = ("Prés d'Arènes","8","43.59048","3.884611")
id033 = ("Garcia Lorca","8","43.590757","3.890616")
id034 = ("Vert Bois","0","43.63458","3.86823")
id035 = ("Malbosc","8","43.633679","3.832861")
id036 = ("Occitanie","32","43.634242","3.849128")
id037 = ("FacdesSciences","24","43.631018","3.860697")
id038 = ("Fac de Lettres","16","43.630665","3.87023")
id039 = ("Aiguelongue","8","43.626163","3.882492")
id040 = ("Jeu de Mail des Abbés","8","43.619701","3.883831")
id041 = ("Euromédecine","8","43.639119","3.828199")
id042 = ("Marie Caizergues","8","43.619871","3.873812")
id043 = ("Sabines","8","43.584211","3.860031")
id044 = ("Celleneuve","8","43.61467","3.832624")
id045 = ("Jardin de la Lironde","8","43.60585","3.911576")
id046 = ("Père Soulas","8","43.621983","3.855603")
id047 = ("Place Viala","8","43.616812","3.855075")
id048 = ("Hôtel du Département","8","43.621682","3.83477")
id049 = ("Tonnelles","8","43.615155","3.839466")
id050 = ("Parvis Jules Ferry - Gare Saint-Roch","8","43.603889","3.879362")
id051 = ("Pont de Lattes - Gare Saint-Roch","12","43.606036","3.882393")
id053 = ("Deux Ponts - Gare Saint-Roch","8","43.604319","3.880916")
id054 = ("Providence - Ovalie","8","43.588239","3.853421")
id055 = ("Pérols Etang de l'Or","68","43.558351","3.963412")
id056 = ("Albert 1er - Cathédrale","12","43.614005","3.873218")
id057 = ("Saint-Guilhem - Courreau","8","43.608996","3.872752")
id059 = ("Sud De France","8","43.59562","3.9235")