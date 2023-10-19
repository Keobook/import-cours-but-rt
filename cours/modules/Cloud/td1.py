import os
import json
import csv
from typing import Dict, Union, Tuple
import requests

ec2_headers = {
  "accept": "json"
}

def get_data(question: str, filters: Union[list, tuple], regions: Union[list, tuple], data: Dict):
  for filter in filters:
    if filter not in data.keys():
      data.update({
        filter: {
          region: {} for region in regions
        }
      })

    for region in regions:
      print(f"{question} --> {filter}:{region}")
      res = requests.get(f"http://localhost:6001/?region={region}&filter={filter}", headers=ec2_headers)
      data[filter][region] = res.json()

def write_data_to_file(filename: str, data: Dict):
  if not os.path.exists("./out/"):
    os.mkdir("./out/")

  with open(f"./out/{filename}", "wt", encoding="utf-8") as fout:
    fout.write(json.dumps(data, indent=4))

### Question 1
regions = ["us-east-1", "us-east-2", "eu-west-1"]
filters = ["m5", "m6"]
data = {}

filename = "tiny.json"

get_data("1.1.1", filters, regions, data)
write_data_to_file(filename, data)

### Question 2
regions = ["eu-west-1"]
filters = ["t1", "t2.micro"]
data = {}

filename = "medium.json"

get_data("1.1.2", filters, regions, data)
write_data_to_file(filename, data)

### Question 3
regions = ["eu-west-1"]
filters = ["t1.micro", "m6a.48xlarge"]
data = {}

def get_data_and_monthly_price_difference(question: str, filters: Union[list, tuple], regions: Union[list, tuple], data: Dict) -> Tuple[any, any]:
  return_data = {}

  for filter in filters:
    if filter not in data.keys():
      data.update({
        filter: {
          region: {} for region in regions
        }
      })

    for region in regions:
      print(f"{question} --> {filter}:{region}")
      res = requests.get(f"http://localhost:6001/?region={region}&filter={filter}", headers=ec2_headers)
      data[filter][region] = res.json()

      return_data[filter] = data[filter][region]["Prices"][0]["MonthlyPrice"]

  return return_data


print("1.1.4 prices -->", get_data_and_monthly_price_difference("1.1.4", filters, regions, data))

### 2 - Transformation ...
### Question 2
regions = ["eu-west-1"]
filters = ["t1", "t2.micro"]
data = {}
filename = "medium-modified.json"

def get_data_and_monthly_price_difference(question: str, filters: Union[list, tuple], regions: Union[list, tuple], data: Dict):

  for filter in filters:
    if filter not in data.keys():
      data.update({
        filter: {
          region: {} for region in regions
        }
      })

    for region in regions:
      print(f"{question} --> {filter}:{region}")
      res = requests.get(f"http://localhost:6001/?region={region}&filter={filter}", headers=ec2_headers)
      data[filter][region] = res.json()["Prices"]

get_data_and_monthly_price_difference("2.2", filters, regions, data)
write_data_to_file(filename, data)

### Question 3
regions = ["us-east-1", "us-east-2", "eu-west-1"]
filters = ["m5", "m6"]
data = {}

get_data("2.3", filters, regions, data)
print("2.3 Keys -->", [key for key in data[filters[0]][regions[0]]["Prices"][0].keys()])

### Question 4
regions = ["us-east-1", "us-east-2", "eu-west-1"]
filters = ["m5", "m6"]
data = {}

get_data("2.4", filters, regions, data)
print("2.4 Keys -->", ",".join([key for key in data[filters[0]][regions[0]]["Prices"][0].keys()]))
print("")

### Question 5
regions = ["us-east-1", "us-east-2", "eu-west-1"]
filters = ["m5", "m6"]
data = {}

get_data("2.5", filters, regions, data)
print("2.5 Keys -->", ",".join([key for key in data[filters[0]][regions[0]]["Prices"][0].keys()]))
for filter in filters:
  for region in regions:
    for i in range(0, len(data[filter][region]["Prices"][0])):
      print("2.5 Items -->", ",".join([value if isinstance(value, str) else str(value) for value in data[filter][region]["Prices"][i].values()]))
print("")

### Question 6
regions = ["us-east-1", "us-east-2", "eu-west-1"]
filters = ["m5", "m6"]
data = {}

filename = "tiny.csv"

def write_data_to_csv_file(filename: str, data: Dict):
  if not os.path.exists("./out/"):
    os.mkdir("./out/")

  csv_writer = csv.writer(open(f"./out/{filename}", "wt", encoding="utf-8"), dialect="excel")

  ### Let's write the header
  csv_writer.writerow([key for key in data[filters[0]][regions[0]]["Prices"][0].keys()])

  for filter in filters:
    for region in regions:
      for i in range(0, len(data[filter][region]["Prices"][0])):
        csv_writer.writerow(data[filter][region]["Prices"][i].values())

get_data("2.6", filters, regions, data)
write_data_to_csv_file(filename, data)
print("2.6 --> Written to file")