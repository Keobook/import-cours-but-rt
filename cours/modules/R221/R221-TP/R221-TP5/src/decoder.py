#! /bin/env python3
# *-* encoding: utf-8 *-*

import requests as r
from datetime import datetime

def ax25ToIntTable(ax25Packet: str) -> list:

  decodedPacket = []

  with open(ax25Packet, "rt") as fin:
    content = fin.read()

    ### language: French
    ### On transforme l'Hexadécimal en entiers
    ### puis en caractère ASCII

    for i in range(0, len(content), 3):
      character = int(content[i:i+2], 16)
      decodedPacket.append(character)

  return decodedPacket

def decodeAx25Header(decodedAx25Packet: list | tuple) -> list:

  ### AX25 Header
  ### Address :
  ###   6 Bytes -> Destination
  ###   1 Byte -> Destination SSID (0x60)
  ###   6 Bytes -> Source
  ###   1 Byte -> Source SSID (0x61)
  ###
  ### Control :
  ###   1 Byte -> For control Purposes (0x03)
  ###
  ### PID :
  ###   1 Byte -> PID of Packet (0xF0)
  ###
  ### AX25 Info :
  ###   N * Bytes -> ROB-1C Application Layer

  current_trame = []
  header = []

  ### On récupère l'addresse de Destination
  for char in decodedAx25Packet[0:6]:
    nchar = char >> 1
    current_trame.append(chr(nchar))

  header.append(current_trame)
  current_trame = []

  ### On récupère le Destination SSID

  ### Destination SSID -> CRRSSID0
  ### where C = command bit
  ### RR = 2 bits at 1
  ### SSID = 4 bits
  ### 1 bit at 0

  DSSID = int("".join([str(char) for char in decodedAx25Packet[6:7]]))
  header.append((DSSID >> 1)&0x0F)

  ### On récupère l'adresse Source
  for char in decodedAx25Packet[7:13]:
    nchar = char >> 1
    current_trame.append(chr(nchar))

  header.append(current_trame)
  current_trame = []

  ### On récupère le Source SSID

  ### Source SSID -> cRRSSID1
  ### where c = response bit
  ### RR = 2 bits at 1
  ## SSID = 4 bits
  ## 1 bit at 1

  SSSID = int("".join([str(char) for char in decodedAx25Packet[14:15]]))
  header.append((SSSID >> 1)&0x0F)

  ### On récupère l'octet de Control
  header.append(decodedAx25Packet[16:17][0])
  ### On récupère l'octet de PID
  header.append(decodedAx25Packet[17:18][0])

  return header, decodedAx25Packet[18:]

def getHeaderFromAX25Packet(ax25File: str) -> str:
  ax25IntReadableData = ax25ToIntTable(ax25File)
  toFormatHeader, body = decodeAx25Header(ax25IntReadableData)

  formattedOutput = formatHeaderData(toFormatHeader)

  print(decodeTelemetry(body))

  return formattedOutput


def formatHeaderData(headerData: list | tuple):
  controlEscapeCharsFromHeaderData(headerData)
  return f"Destination: {''.join(headerData[0])}\n D-SSID: {headerData[1]}\n Source: {''.join(headerData[2])}\t\t \n S-SSID: {headerData[3]}\n Control: {headerData[4]}\n PID: {headerData[5]}\n"

def decodeTelemetry(ax25Body: list | tuple):
  ts = datetime.fromtimestamp(int.from_bytes(ax25Body[1:5], byteorder='little'))
  temp = int.from_bytes(ax25Body[120:122],byteorder="little",signed=True)*0.25
  mtemp = int.from_bytes(ax25Body[121:122], byteorder="little", signed=True)*0.25
  return f"{ts}, {temp}, {mtemp}"

###########################################################
###
### API-related functions
###
############################################################

def ax25FrameToIntTable(ax25Packet: str) -> list:

  decodedPacket = []

  ### language: French
  ### On transforme l'Hexadécimal en entiers
  ### puis en caractère ASCII

  for i in range(0, len(ax25Packet), 3):
    character = int(ax25Packet[i:i+2], 16)
    decodedPacket.append(character)

  return decodedPacket

def getHeaderFromAPIAX25Packet(ax25Frame: str) -> str:
  ax25IntReadableData = ax25FrameToIntTable(ax25Frame)
  toFormatHeader, body = decodeAx25Header(ax25IntReadableData)

  formattedOutput = formatHeaderData(toFormatHeader)
  body = decodeTelemetry(body)

  return formattedOutput, body

def APITest(url: str):
  global APIToken


  try:

    returnData = r.get(url, headers={"accept": "application/json", "Authorization": f"Token {APIToken}"})

    if returnData.status_code == 200:

      dataJSON = returnData.json()
      frameToDecode = dataJSON["frame"]

      header, body = getHeaderFromAPIAX25Packet(frameToDecode)

      return [header, body]
  except r.exceptions.ConnectionError:
    return None

def getAPIJSONData(url: str) -> dict:
  global APIToken

  try:
    returnData = r.get(url, headers={"accept": "application/json", "Authorization": f"Token {APIToken}"})

    if returnData.status_code == 200:
      dataJSON = returnData.json()
      return dataJSON

  except r.exceptions.ConnectionError:
    return None

def getDataFromAPI(NoradID: int) -> str:
  content = APITest(f"https://db.satnogs.org/api/telemetry/{NoradID}/?format=json")
  if content != None:
    header, body = content
    satelliteInformations = getAPIJSONData(f"https://db.satnogs.org/api/satellites/{NoradID}/?format=json")
    if satelliteInformations != None:
      print(f"Retrieved {satelliteInformations['name']}'s data from SatNoGS API")

    return body + "\n" + header
  else:
    return f"Couldn't retrieve any information for {NoradID}, check your network."

##############################################################
###
### Formatting related functions
###
##############################################################

def controlEscapeCharsFromHeaderData(headerData: list | tuple) -> None:

  global asciiEscChars

  for element in headerData:
    if isinstance(element, list):
      for i in range(0, len(element)):
        if element[i] in asciiEscChars:
          element[i] = "\x20"

### Global variables
APIToken = "9eebacd25e1a47808ee574883be66eff92d329aa"

asciiEscChars = ["\x1b"]


### Scripting

for file in ["./trames/cirbe-9-5-2023.txt", "./trames/uvsq-dat-8-5-2023.txt", "./trames/tausat-1-4-5-2023.txt", "./trames/robusta1B-7-5-2023.txt"]:
  print("Header from:", file)
  print(getHeaderFromAX25Packet(file))

print(getDataFromAPI(47438))
print(getDataFromAPI(56188))
print(getDataFromAPI(42792))
