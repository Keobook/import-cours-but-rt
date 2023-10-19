# BUT-RT2 - Cloud - TD1 - Automatisation de la récupération des prix d'AWS

1. ## Obtention des prix au format json des instances "COMPUTE" d'aws via curl

    1. ### Installation d'un container de prix

          On fait:

          ```sh
          git clone git@github.com:yeo/ec2.shop.git; cd ec2.shop; docker pull golang:1.17-bullseye; docker compose build; docker compose up
          ```

          1. Récupérez les prix des instances m5 et m6 de la region us-east puis eu-west-1 et sauvegardez les dans un fichier tiny.json.

              ```py
              import os
              import json
              from typing import Dict, Union
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
                if not os.path.exists(f"./out/"):
                  os.mkdir("./out/")

                with open(f"./out/{filename}", "wt", encoding="utf-8") as fout:
                  fout.write(json.dumps(data))

              ### Question 1
              regions = ["us-east-1", "us-east-2", "eu-west-1"]
              filters = ["m5", "m6"]
              data = {}

              filename = "tiny.json"

              get_data("1.1.1", filters, regions, data)
              write_data_to_file(filename, data)
              ```

          1. Récupérez les prix des instances t1 et t2.micro de la region eu-west-1 sauvegardez les dans un fichier medium.json.

              ```py
              import os
              import json
              from typing import Dict, Union
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
                if not os.path.exists(f"./out/"):
                  os.mkdir("./out/")

                with open(f"./out/{filename}", "wt", encoding="utf-8") as fout:
                  fout.write(json.dumps(data))

              ### Question 2
              regions = ["eu-west-1"]
              filters = ["t1", "t2.micro"]
              data = {}

              filename = "medium.json"

              get_data("1.1.2", filters, regions, data)
              write_data_to_file(filename, data)
              ```

          1. à quoi correspondent les données extraites ?

              Les données extraites correspondent aux différentes informations
              utiles ou nécessaires afin d'estimer le coûts d'utilisation de telles machines
              dans le cloud.

          1. Quel est la différence de prix au mois entre une m6a.48xlarge et une t1.micro ?

              ```py
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
              ```

              La sortie est:

              ```sh
              1.1.4 prices --> {'t1.micro': 14.6, 'm6a.48xlarge': 6748.704}
              ```

    1. ### Transformation des fichiers json en csv

        1. A quoi sert l'option `-r` ?

            Elle sert à l'avoir en "raw", c'est à dire sans
            avoir été formatté par jq.

        1. éliminez la clef `Prices` de la sortie json ?

            ```py
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
            ```

            ce qui nous donne:

            ```json
            {
              "t2.micro": {
                "eu-west-1": [
                  {
                    "InstanceType": "t2.micro",
                    "Memory": "1 GiB",
                    "VCPUS": 1,
                    "Storage": "EBS only",
                    "Network": "Low to Moderate",
                    "Cost": 0.0126,
                    "MonthlyPrice": 9.198,
                    "SpotPrice": "NA"
                  }
                ]
              }
            }
            ```

        1. Quelles sont les clefs des entrées (utilisez `|keys|@csv`) ?

            ```py
            ### Question 3
            regions = ["us-east-1", "us-east-2", "eu-west-1"]
            filters = ["m5", "m6"]
            data = {}

            get_data("2.3", filters, regions, data)
            print("2.3 Keys -->", [key for key in data[filters[0]][regions[0]]["Prices"][0].keys()])
            ```

            Ce qui nous donne:

            ```sh
            2.3 Keys --> ['InstanceType', 'Memory', 'VCPUS', 'Storage', 'Network', 'Cost', 'MonthlyPrice', 'SpotPrice']
            ```

        1. N'affichez qu'une seule ligne pour les clefs qui constituera les en-têtes de votre fichier csv.

            ```py
            ### Question 4
            regions = ["us-east-1", "us-east-2", "eu-west-1"]
            filters = ["m5", "m6"]
            data = {}

            get_data("2.4", filters, regions, data)
            print("2.4 Keys -->", ",".join([key for key in data[filters[0]][regions[0]]["Prices"][0].keys()]))
            ```

            Ce qui nous donne:

            ```sh
            2.4 Keys --> InstanceType,Memory,VCPUS,Storage,Network,Cost,MonthlyPrice,SpotPrice
            ```

        1. Utilisez l'ordre `join` pour produire les lignes du fichier csv.

            ```py
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
            ```

            Ce qui nous donne:

            ```sh
            2.5 Items --> m5a.8xlarge,128 GiB,32,EBS only,Up to 10 Gigabit,1.376,1004.4799999999999,NA
            2.5 Items --> m5dn.24xlarge,384 GiB,96,4 x 900 NVMe SSD,100 Gigabit,6.528,4765.44,NA
            2.5 Items --> m5d.4xlarge,64 GiB,16,2 x 300 NVMe SSD,Up to 10 Gigabit,0.904,659.9200000000001,NA
            2.5 Items --> m5ad.8xlarge,128 GiB,32,2 x 600 NVMe SSD,Up to 10 Gigabit,1.648,1203.04,NA
            2.5 Items --> m5d.xlarge,16 GiB,4,1 x 150 NVMe SSD,Up to 10 Gigabit,0.226,164.98000000000002,NA
            2.5 Items --> m5.xlarge,16 GiB,4,EBS only,Up to 10 Gigabit,0.192,140.16,NA
            2.5 Items --> m5d.large,8 GiB,2,1 x 75 NVMe SSD,Up to 10 Gigabit,0.113,82.49000000000001,NA
            2.5 Items --> m5n.metal,384 GiB,96,EBS only,100 Gigabit,5.712,4169.76,NA
            2.5 Items --> m5zn.metal,192 GiB,48,EBS only,100 Gigabit,3.9641,2893.793,0.8388
            2.5 Items --> m5dn.metal,384 GiB,96,4 x 900 NVMe SSD,100 Gigabit,6.528,4765.44,1.3545
            2.5 Items --> m5d.24xlarge,384 GiB,96,4 x 900 NVMe SSD,25 Gigabit,5.424,3959.5200000000004,1.9209
            2.5 Items --> m5ad.large,8 GiB,2,1 x 75 NVMe SSD,Up to 10 Gigabit,0.103,75.19,0.0375
            2.5 Items --> m5a.12xlarge,192 GiB,48,EBS only,10 Gigabit,2.064,1506.72,0.7131
            2.5 Items --> m5dn.24xlarge,384 GiB,96,4 x 900 NVMe SSD,100 Gigabit,6.528,4765.44,1.2826
            2.5 Items --> m5n.16xlarge,256 GiB,64,EBS only,75 Gigabit,3.808,2779.8399999999997,1.4122
            2.5 Items --> m5.xlarge,16 GiB,4,EBS only,Up to 10 Gigabit,0.192,140.16,0.0712
            2.5 Items --> m5ad.12xlarge,192 GiB,48,2 x 900 NVMe SSD,10 Gigabit,2.76,2014.8,NA
            2.5 Items --> m5.4xlarge,64 GiB,16,EBS only,Up to 10 Gigabit,0.856,624.88,NA
            2.5 Items --> m5n.metal,384 GiB,96,EBS only,100 Gigabit,6.384,4660.320000000001,NA
            2.5 Items --> m5n.xlarge,16 GiB,4,EBS only,Up to 25 Gigabit,0.266,194.18,NA
            2.5 Items --> m5a.large,8 GiB,2,EBS only,Up to 10 Gigabit,0.096,70.08,NA
            2.5 Items --> m5zn.2xlarge,32 GiB,8,EBS only,Up to 25 Gigabit,0.7364,537.572,NA
            2.5 Items --> m5.24xlarge,384 GiB,96,EBS only,25 Gigabit,5.136,3749.28,NA
            2.5 Items --> m5d.12xlarge,192 GiB,48,2 x 900 NVMe SSD,10 Gigabit,3.024,2207.52,NA
            2.5 Items --> m6i.2xlarge,32 GiB,8,EBS only,Up to 12500 Megabit,0.384,280.32,NA
            2.5 Items --> m6g.large,8 GiB,2,EBS only,Up to 10 Gigabit,0.077,56.21,NA
            2.5 Items --> m6gd.xlarge,16 GiB,4,1 x 237 NVMe SSD,Up to 10 Gigabit,0.1808,131.98399999999998,NA
            2.5 Items --> m6gd.12xlarge,192 GiB,48,2 x 1425 NVMe SSD,20 Gigabit,2.1696,1583.808,NA
            2.5 Items --> m6id.32xlarge,512 GiB,128,4 x 1900 SSD,50000 Megabit,7.5936,5543.328,NA
            2.5 Items --> m6g.4xlarge,64 GiB,16,EBS only,Up to 10 Gigabit,0.616,449.68,NA
            2.5 Items --> m6i.large,8 GiB,2,EBS only,Up to 12500 Megabit,0.096,70.08,NA
            2.5 Items --> m6id.4xlarge,64 GiB,16,1 x 950 SSD,Up to 12500 Megabit,0.9492,692.916,NA
            2.5 Items --> m6i.16xlarge,256 GiB,64,EBS only,25000 Megabit,3.072,2242.56,1.1742
            2.5 Items --> m6a.4xlarge,64 GiB,16,EBS only,Up to 12500 Megabit,0.6912,504.576,0.2977
            2.5 Items --> m6g.2xlarge,32 GiB,8,EBS only,Up to 10 Gigabit,0.308,224.84,0.1192
            2.5 Items --> m6a.32xlarge,512 GiB,128,EBS only,50000 Megabit,5.5296,4036.608,1.5273
            2.5 Items --> m6g.xlarge,16 GiB,4,EBS only,Up to 10 Gigabit,0.154,112.42,0.0564
            2.5 Items --> m6id.16xlarge,256 GiB,64,2 x 1900 SSD,25000 Megabit,3.7968,2771.664,0.9542
            2.5 Items --> m6a.8xlarge,128 GiB,32,EBS only,12500 Megabit,1.3824,1009.152,0.6020
            2.5 Items --> m6i.large,8 GiB,2,EBS only,Up to 12500 Megabit,0.096,70.08,0.0322
            2.5 Items --> m6a.2xlarge,32 GiB,8,EBS only,Up to 12500 Megabit,0.3852,281.19599999999997,NA
            2.5 Items --> m6id.xlarge,16 GiB,4,1 x 237 SSD,Up to 12500 Megabit,0.2646,193.15800000000002,NA
            2.5 Items --> m6id.24xlarge,384 GiB,96,4 x 1425 SSD,37500 Megabit,6.3504,4635.7919999999995,NA
            2.5 Items --> m6i.large,8 GiB,2,EBS only,Up to 12500 Megabit,0.107,78.11,NA
            2.5 Items --> m6gd.2xlarge,32 GiB,8,1 x 475 NVMe SSD,Up to 10 Gigabit,0.4032,294.336,NA
            2.5 Items --> m6g.2xlarge,32 GiB,8,EBS only,Up to 10 Gigabit,0.344,251.11999999999998,NA
            2.5 Items --> m6id.12xlarge,192 GiB,48,2 x 1425 SSD,18750 Megabit,3.1752,2317.8959999999997,NA
            2.5 Items --> m6i.4xlarge,64 GiB,16,EBS only,Up to 12500 Megabit,0.856,624.88,NA
            ```

        1. A l'aide de bash assemblez le header et les lignes pour créer le csv. Vérifiez que le fichier csv produit est importable dans libre office.

            ```py
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
            ```

            Ce qui nous donne:

            ```csv
            InstanceType,Memory,VCPUS,Storage,Network,Cost,MonthlyPrice,SpotPrice
            m5a.8xlarge,128 GiB,32,EBS only,Up to 10 Gigabit,1.376,1004.4799999999999,NA
            m5dn.24xlarge,384 GiB,96,4 x 900 NVMe SSD,100 Gigabit,6.528,4765.44,NA
            m5d.4xlarge,64 GiB,16,2 x 300 NVMe SSD,Up to 10 Gigabit,0.904,659.9200000000001,NA
            m5ad.8xlarge,128 GiB,32,2 x 600 NVMe SSD,Up to 10 Gigabit,1.648,1203.04,NA
            m5d.xlarge,16 GiB,4,1 x 150 NVMe SSD,Up to 10 Gigabit,0.226,164.98000000000002,NA
            m5.xlarge,16 GiB,4,EBS only,Up to 10 Gigabit,0.192,140.16,NA
            m5d.large,8 GiB,2,1 x 75 NVMe SSD,Up to 10 Gigabit,0.113,82.49000000000001,NA
            m5n.metal,384 GiB,96,EBS only,100 Gigabit,5.712,4169.76,NA
            m5zn.metal,192 GiB,48,EBS only,100 Gigabit,3.9641,2893.793,0.8388
            m5dn.metal,384 GiB,96,4 x 900 NVMe SSD,100 Gigabit,6.528,4765.44,1.3545
            m5d.24xlarge,384 GiB,96,4 x 900 NVMe SSD,25 Gigabit,5.424,3959.5200000000004,1.9209
            m5ad.large,8 GiB,2,1 x 75 NVMe SSD,Up to 10 Gigabit,0.103,75.19,0.0375
            m5a.12xlarge,192 GiB,48,EBS only,10 Gigabit,2.064,1506.72,0.7131
            m5dn.24xlarge,384 GiB,96,4 x 900 NVMe SSD,100 Gigabit,6.528,4765.44,1.2826
            m5n.16xlarge,256 GiB,64,EBS only,75 Gigabit,3.808,2779.8399999999997,1.4122
            m5.xlarge,16 GiB,4,EBS only,Up to 10 Gigabit,0.192,140.16,0.0712
            m5ad.12xlarge,192 GiB,48,2 x 900 NVMe SSD,10 Gigabit,2.76,2014.8,NA
            m5.4xlarge,64 GiB,16,EBS only,Up to 10 Gigabit,0.856,624.88,NA
            m5n.metal,384 GiB,96,EBS only,100 Gigabit,6.384,4660.320000000001,NA
            m5n.xlarge,16 GiB,4,EBS only,Up to 25 Gigabit,0.266,194.18,NA
            m5a.large,8 GiB,2,EBS only,Up to 10 Gigabit,0.096,70.08,NA
            m5zn.2xlarge,32 GiB,8,EBS only,Up to 25 Gigabit,0.7364,537.572,NA
            m5.24xlarge,384 GiB,96,EBS only,25 Gigabit,5.136,3749.28,NA
            m5d.12xlarge,192 GiB,48,2 x 900 NVMe SSD,10 Gigabit,3.024,2207.52,NA
            m6i.2xlarge,32 GiB,8,EBS only,Up to 12500 Megabit,0.384,280.32,NA
            m6g.large,8 GiB,2,EBS only,Up to 10 Gigabit,0.077,56.21,NA
            m6gd.xlarge,16 GiB,4,1 x 237 NVMe SSD,Up to 10 Gigabit,0.1808,131.98399999999998,NA
            m6gd.12xlarge,192 GiB,48,2 x 1425 NVMe SSD,20 Gigabit,2.1696,1583.808,NA
            m6id.32xlarge,512 GiB,128,4 x 1900 SSD,50000 Megabit,7.5936,5543.328,NA
            m6g.4xlarge,64 GiB,16,EBS only,Up to 10 Gigabit,0.616,449.68,NA
            m6i.large,8 GiB,2,EBS only,Up to 12500 Megabit,0.096,70.08,NA
            m6id.4xlarge,64 GiB,16,1 x 950 SSD,Up to 12500 Megabit,0.9492,692.916,NA
            m6i.16xlarge,256 GiB,64,EBS only,25000 Megabit,3.072,2242.56,1.1742
            m6a.4xlarge,64 GiB,16,EBS only,Up to 12500 Megabit,0.6912,504.576,0.2977
            m6g.2xlarge,32 GiB,8,EBS only,Up to 10 Gigabit,0.308,224.84,0.1192
            m6a.32xlarge,512 GiB,128,EBS only,50000 Megabit,5.5296,4036.608,1.5273
            m6g.xlarge,16 GiB,4,EBS only,Up to 10 Gigabit,0.154,112.42,0.0564
            m6id.16xlarge,256 GiB,64,2 x 1900 SSD,25000 Megabit,3.7968,2771.664,0.9542
            m6a.8xlarge,128 GiB,32,EBS only,12500 Megabit,1.3824,1009.152,0.6020
            m6i.large,8 GiB,2,EBS only,Up to 12500 Megabit,0.096,70.08,0.0322
            m6a.2xlarge,32 GiB,8,EBS only,Up to 12500 Megabit,0.3852,281.19599999999997,NA
            m6id.xlarge,16 GiB,4,1 x 237 SSD,Up to 12500 Megabit,0.2646,193.15800000000002,NA
            m6id.24xlarge,384 GiB,96,4 x 1425 SSD,37500 Megabit,6.3504,4635.7919999999995,NA
            m6i.large,8 GiB,2,EBS only,Up to 12500 Megabit,0.107,78.11,NA
            m6gd.2xlarge,32 GiB,8,1 x 475 NVMe SSD,Up to 10 Gigabit,0.4032,294.336,NA
            m6g.2xlarge,32 GiB,8,EBS only,Up to 10 Gigabit,0.344,251.11999999999998,NA
            m6id.12xlarge,192 GiB,48,2 x 1425 SSD,18750 Megabit,3.1752,2317.8959999999997,NA
            m6i.4xlarge,64 GiB,16,EBS only,Up to 12500 Megabit,0.856,624.88,NA
            ```

## Copyright &copy; 2023 Alexis Opolka - All Rights Reserved
