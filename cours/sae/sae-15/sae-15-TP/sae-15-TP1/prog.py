## question 1

import requests

responce1=requests.get("https://data.montpellier3m.fr/sites/default/files/ressources/FR_MTP_COME.xml")

print(responce1.text)


## question 2 

import requests

parkings = ['FR_MTP_ANTI.xml','FR_MTP_COME.xml','FR_MTP_CORU.xml','FR_MTP_EURO.xml','FR_MTP_FOCH.xml','FR_MTP_GAMB.xml','FR_MTP_GARE.xml','FR_MTP_TRIA.xml','FR_MTP_ARCT.xml','FR_MTP_PITO.xml','FR_MTP_CIRC.xml','FR_MTP_SABI.xml','FR_MTP_GARC.xml','FR_CAS_SABL.xml','FR_MTP_MOSS.xml','FR_STJ_SJLC.xml','FR_MTP_MEDC.xml','FR_MTP_OCCI.xml','FR_CAS_VICA.xml','FR_MTP_GA109.xml','FR_MTP_GA250.xml','FR_CAS_CDGA.xml','FR_MTP_ARCE.xml','FR_MTP_POLY.xml']

for Parkings in parkings : 
  responce2=requests.get("https://data.montpellier3m.fr/sites/default/files/ressources/",Parkings)

  print (responce2.text)
