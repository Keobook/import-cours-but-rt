---
Author: Alexis Opolka
Subject: Cloud - Automatisation de la récupération des prix d'AWS
Company: IUT de Béziers
Copyright: All Rights Reserved
---

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

          2. Récupérez les prix des instances t1 et t2.micro de la region eu-west-1 sauvegardez les dans un fichier medium.json.

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

          3. à quoi correspondent les données extraites ?

              Les données extraites correspondent aux différentes informations
              utiles ou nécessaires afin d'estimer le coûts d'utilisation de telles machines
              dans le cloud.

          4. Quel est la différence de prix au mois entre une m6a.48xlarge et une t1.micro ?

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

            ou

            ```sh
            jq -r '.Prices' ./out/tiny-jq.json
            ```

            Ce qui nous donne:

            ```json
              {
                "InstanceType": "m6id.8xlarge",
                "Memory": "128 GiB",
                "VCPUS": 32,
                "Storage": "1 x 1900 SSD",
                "Network": "12500 Megabit",
                "Cost": 2.1168,
                "MonthlyPrice": 1545.2640000000001,
                "SpotPrice": "NA"
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

            ou

            ```sh
            jq -r '.Prices[] |keys|@csv' out/tiny-jq.json | head -n 1
            ```

            Ce qui nous donne:

            ```sh
            "Cost","InstanceType","Memory","MonthlyPrice","Network","SpotPrice","Storage","VCPUS"
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

            ou

            ```sh
            jq -r '.Prices[] |keys|@csv' out/tiny-jq.json | head -n 1
            ```

            Ce qui nous donne:

            ```sh
            "Cost","InstanceType","Memory","MonthlyPrice","Network","SpotPrice","Storage","VCPUS"
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

            ou

            ```sh
            jq -r '.Prices[] | join(",")' out/tiny-jq.json
            ```

            ce qui nous donne:

            ```sh
            m5a.8xlarge,128 GiB,32,EBS only,Up to 10 Gigabit,1.376,1004.4799999999999,NA
            m5dn.24xlarge,384 GiB,96,4 x 900 NVMe SSD,100 Gigabit,6.528,4765.44,NA
            m5d.4xlarge,64 GiB,16,2 x 300 NVMe SSD,Up to 10 Gigabit,0.904,659.9200000000001,NA
            m5ad.8xlarge,128 GiB,32,2 x 600 NVMe SSD,Up to 10 Gigabit,1.648,1203.04,NA
            m5d.xlarge,16 GiB,4,1 x 150 NVMe SSD,Up to 10 Gigabit,0.226,164.98000000000002,NA
            m5.xlarge,16 GiB,4,EBS only,Up to 10 Gigabit,0.192,140.16,NA
            m5d.large,8 GiB,2,1 x 75 NVMe SSD,Up to 10 Gigabit,0.113,82.49000000000001,NA
            m5n.metal,384 GiB,96,EBS only,100 Gigabit,5.712,4169.76,NA
            m5n.large,8 GiB,2,EBS only,Up to 25 Gigabit,0.119,86.86999999999999,NA
            m5zn.12xlarge,192 GiB,48,EBS only,100 Gigabit,3.9641,2893.793,NA
            m5a.24xlarge,384 GiB,96,EBS only,20 Gigabit,4.128,3013.44,NA
            m5.16xlarge,256 GiB,64,EBS only,20 Gigabit,3.072,2242.56,NA
            m5dn.metal,384 GiB,96,4 x 900 NVMe SSD,100 Gigabit,6.528,4765.44,NA
            m5ad.24xlarge,384 GiB,96,4 x 900 NVMe SSD,20 Gigabit,4.944,3609.12,NA
            m5d.24xlarge,384 GiB,96,4 x 900 NVMe SSD,25 Gigabit,5.424,3959.5200000000004,NA
            m5.large,8 GiB,2,EBS only,Up to 10 Gigabit,0.096,70.08,NA
            m5a.4xlarge,64 GiB,16,EBS only,Up to 10 Gigabit,0.688,502.23999999999995,NA
            m5a.12xlarge,192 GiB,48,EBS only,10 Gigabit,2.064,1506.72,NA
            m5a.large,8 GiB,2,EBS only,Up to 10 Gigabit,0.086,62.779999999999994,NA
            m5.4xlarge,64 GiB,16,EBS only,Up to 10 Gigabit,0.768,560.64,NA
            m5zn.metal,192 GiB,48,EBS only,100 Gigabit,3.9641,2893.793,NA
            m5dn.4xlarge,64 GiB,16,2 x 300 NVMe SSD,Up to 25 Gigabit,1.088,794.24,NA
            m5d.12xlarge,192 GiB,48,2 x 900 NVMe SSD,10 Gigabit,2.712,1979.7600000000002,NA
            m5zn.6xlarge,96 GiB,24,EBS only,50 Gigabit,1.982,1446.86,NA
            m5n.2xlarge,32 GiB,8,EBS only,Up to 25 Gigabit,0.476,347.47999999999996,NA
            m5zn.large,8 GiB,2,EBS only,Up to 25 Gigabit,0.1652,120.596,NA
            m5ad.16xlarge,256 GiB,64,4 x 600 NVMe SSD,12 Gigabit,3.296,2406.08,NA
            m5n.16xlarge,256 GiB,64,EBS only,75 Gigabit,3.808,2779.8399999999997,NA
            m5zn.2xlarge,32 GiB,8,EBS only,Up to 25 Gigabit,0.6607,482.311,NA
            m5dn.8xlarge,128 GiB,32,2 x 600 NVMe SSD,25 Gigabit,2.176,1588.48,NA
            m5ad.4xlarge,64 GiB,16,2 x 300 NVMe SSD,Up to 10 Gigabit,0.824,601.52,NA
            m5d.2xlarge,32 GiB,8,1 x 300 NVMe SSD,Up to 10 Gigabit,0.452,329.96000000000004,NA
            m5ad.xlarge,16 GiB,4,1 x 150 NVMe SSD,Up to 10 Gigabit,0.206,150.38,NA
            m5.24xlarge,384 GiB,96,EBS only,25 Gigabit,4.608,3363.8399999999997,NA
            m5.metal,384 GiB,96,EBS only,25 Gigabit,4.608,3363.8399999999997,NA
            m5n.12xlarge,192 GiB,48,EBS only,50 Gigabit,2.856,2084.88,NA
            m5n.24xlarge,384 GiB,96,EBS only,100 Gigabit,5.712,4169.76,NA
            m5.12xlarge,192 GiB,48,EBS only,10 Gigabit,2.304,1681.9199999999998,NA
            m5zn.3xlarge,48 GiB,12,EBS only,Up to 25 Gigabit,0.991,723.43,NA
            m5dn.xlarge,16 GiB,4,1 x 150 NVMe SSD,Up to 25 Gigabit,0.272,198.56,NA
            m5a.xlarge,16 GiB,4,EBS only,Up to 10 Gigabit,0.172,125.55999999999999,NA
            m5d.8xlarge,128 GiB,32,2 x 600 NVMe SSD,10 Gigabit,1.808,1319.8400000000001,NA
            m5zn.xlarge,16 GiB,4,EBS only,Up to 25 Gigabit,0.3303,241.119,NA
            m5n.xlarge,16 GiB,4,EBS only,Up to 25 Gigabit,0.238,173.73999999999998,NA
            m5d.metal,384 GiB,96,4 x 900 NVMe SSD,25 Gigabit,5.424,3959.5200000000004,NA
            m5ad.2xlarge,32 GiB,8,1 x 300 NVMe SSD,Up to 10 Gigabit,0.412,300.76,NA
            m5a.2xlarge,32 GiB,8,EBS only,Up to 10 Gigabit,0.344,251.11999999999998,NA
            m5dn.16xlarge,256 GiB,64,4 x 600 NVMe SSD,75 Gigabit,4.352,3176.96,NA
            m5.8xlarge,128 GiB,32,EBS only,10 Gigabit,1.536,1121.28,NA
            m5dn.large,8 GiB,2,1 x 75 NVMe SSD,Up to 25 Gigabit,0.136,99.28,NA
            m5n.8xlarge,128 GiB,32,EBS only,25 Gigabit,1.904,1389.9199999999998,NA
            m5ad.large,8 GiB,2,1 x 75 NVMe SSD,Up to 10 Gigabit,0.103,75.19,NA
            m5n.4xlarge,64 GiB,16,EBS only,Up to 25 Gigabit,0.952,694.9599999999999,NA
            m5dn.2xlarge,32 GiB,8,1 x 300 NVMe SSD,Up to 25 Gigabit,0.544,397.12,NA
            m5ad.12xlarge,192 GiB,48,2 x 900 NVMe SSD,10 Gigabit,2.472,1804.56,NA
            m5d.16xlarge,256 GiB,64,4 x 600 NVMe SSD,20 Gigabit,3.616,2639.6800000000003,NA
            m5.2xlarge,32 GiB,8,EBS only,Up to 10 Gigabit,0.384,280.32,NA
            m5dn.12xlarge,192 GiB,48,2 x 900 GB NVMe SSD,50 Gigabit,3.264,2382.72,NA
            m5a.16xlarge,256 GiB,64,EBS only,12 Gigabit,2.752,2008.9599999999998,NA
            m5zn.metal,192 GiB,48,EBS only,100 Gigabit,3.9641,2893.793,0.8106
            m5dn.metal,384 GiB,96,4 x 900 NVMe SSD,100 Gigabit,6.528,4765.44,1.3387
            m5d.24xlarge,384 GiB,96,4 x 900 NVMe SSD,25 Gigabit,5.424,3959.5200000000004,1.9158
            m5ad.large,8 GiB,2,1 x 75 NVMe SSD,Up to 10 Gigabit,0.103,75.19,0.0374
            m5a.12xlarge,192 GiB,48,EBS only,10 Gigabit,2.064,1506.72,0.7086
            m5dn.24xlarge,384 GiB,96,4 x 900 NVMe SSD,100 Gigabit,6.528,4765.44,1.2423
            m5n.16xlarge,256 GiB,64,EBS only,75 Gigabit,3.808,2779.8399999999997,1.4118
            m5.xlarge,16 GiB,4,EBS only,Up to 10 Gigabit,0.192,140.16,0.0708
            m5a.16xlarge,256 GiB,64,EBS only,12 Gigabit,2.752,2008.9599999999998,0.9955
            m5zn.12xlarge,192 GiB,48,EBS only,100 Gigabit,3.9641,2893.793,1.0491
            m5dn.xlarge,16 GiB,4,1 x 150 NVMe SSD,Up to 25 Gigabit,0.272,198.56,0.0745
            m5n.large,8 GiB,2,EBS only,Up to 25 Gigabit,0.119,86.86999999999999,0.0373
            m5.8xlarge,128 GiB,32,EBS only,10 Gigabit,1.536,1121.28,0.5526
            m5dn.12xlarge,192 GiB,48,2 x 900 GB NVMe SSD,50 Gigabit,3.264,2382.72,0.8796
            m5a.xlarge,16 GiB,4,EBS only,Up to 10 Gigabit,0.172,125.55999999999999,0.0730
            m5ad.12xlarge,192 GiB,48,2 x 900 NVMe SSD,10 Gigabit,2.472,1804.56,0.7322
            m5.metal,384 GiB,96,EBS only,25 Gigabit,4.608,3363.8399999999997,1.3858
            m5ad.4xlarge,64 GiB,16,2 x 300 NVMe SSD,Up to 10 Gigabit,0.824,601.52,0.4272
            m5d.8xlarge,128 GiB,32,2 x 600 NVMe SSD,10 Gigabit,1.808,1319.8400000000001,0.5966
            m5a.2xlarge,32 GiB,8,EBS only,Up to 10 Gigabit,0.344,251.11999999999998,0.1519
            m5n.12xlarge,192 GiB,48,EBS only,50 Gigabit,2.856,2084.88,1.0148
            m5d.xlarge,16 GiB,4,1 x 150 NVMe SSD,Up to 10 Gigabit,0.226,164.98000000000002,0.0810
            m5n.xlarge,16 GiB,4,EBS only,Up to 25 Gigabit,0.238,173.73999999999998,0.0739
            m5zn.large,8 GiB,2,EBS only,Up to 25 Gigabit,0.1652,120.596,0.0377
            m5dn.large,8 GiB,2,1 x 75 NVMe SSD,Up to 25 Gigabit,0.136,99.28,0.0427
            m5ad.16xlarge,256 GiB,64,4 x 600 NVMe SSD,12 Gigabit,3.296,2406.08,1.1993
            m5n.2xlarge,32 GiB,8,EBS only,Up to 25 Gigabit,0.476,347.47999999999996,0.1631
            m5dn.2xlarge,32 GiB,8,1 x 300 NVMe SSD,Up to 25 Gigabit,0.544,397.12,0.1533
            m5n.8xlarge,128 GiB,32,EBS only,25 Gigabit,1.904,1389.9199999999998,0.6611
            m5n.metal,384 GiB,96,EBS only,100 Gigabit,5.712,4169.76,1.6827
            m5a.4xlarge,64 GiB,16,EBS only,Up to 10 Gigabit,0.688,502.23999999999995,0.3107
            m5d.16xlarge,256 GiB,64,4 x 600 NVMe SSD,20 Gigabit,3.616,2639.6800000000003,1.3031
            m5zn.6xlarge,96 GiB,24,EBS only,50 Gigabit,1.982,1446.86,0.4905
            m5dn.4xlarge,64 GiB,16,2 x 300 NVMe SSD,Up to 25 Gigabit,1.088,794.24,0.3269
            m5ad.xlarge,16 GiB,4,1 x 150 NVMe SSD,Up to 10 Gigabit,0.206,150.38,0.0754
            m5ad.8xlarge,128 GiB,32,2 x 600 NVMe SSD,Up to 10 Gigabit,1.648,1203.04,0.3549
            m5d.metal,384 GiB,96,4 x 900 NVMe SSD,25 Gigabit,5.424,3959.5200000000004,1.3287
            m5.16xlarge,256 GiB,64,EBS only,20 Gigabit,3.072,2242.56,1.2008
            m5a.24xlarge,384 GiB,96,EBS only,20 Gigabit,4.128,3013.44,1.2162
            m5d.4xlarge,64 GiB,16,2 x 300 NVMe SSD,Up to 10 Gigabit,0.904,659.9200000000001,0.3012
            m5zn.2xlarge,32 GiB,8,EBS only,Up to 25 Gigabit,0.6607,482.311,0.1967
            m5zn.xlarge,16 GiB,4,EBS only,Up to 25 Gigabit,0.3303,241.119,0.0750
            m5a.8xlarge,128 GiB,32,EBS only,Up to 10 Gigabit,1.376,1004.4799999999999,0.4471
            m5d.large,8 GiB,2,1 x 75 NVMe SSD,Up to 10 Gigabit,0.113,82.49000000000001,0.0386
            m5dn.8xlarge,128 GiB,32,2 x 600 NVMe SSD,25 Gigabit,2.176,1588.48,0.6130
            m5.24xlarge,384 GiB,96,EBS only,25 Gigabit,4.608,3363.8399999999997,1.6118
            m5a.large,8 GiB,2,EBS only,Up to 10 Gigabit,0.086,62.779999999999994,0.0377
            m5ad.2xlarge,32 GiB,8,1 x 300 NVMe SSD,Up to 10 Gigabit,0.412,300.76,0.1500
            m5.12xlarge,192 GiB,48,EBS only,10 Gigabit,2.304,1681.9199999999998,0.8243
            m5d.2xlarge,32 GiB,8,1 x 300 NVMe SSD,Up to 10 Gigabit,0.452,329.96000000000004,0.1509
            m5.large,8 GiB,2,EBS only,Up to 10 Gigabit,0.096,70.08,0.0337
            m5zn.3xlarge,48 GiB,12,EBS only,Up to 25 Gigabit,0.991,723.43,0.2305
            m5ad.24xlarge,384 GiB,96,4 x 900 NVMe SSD,20 Gigabit,4.944,3609.12,1.4826
            m5n.24xlarge,384 GiB,96,EBS only,100 Gigabit,5.712,4169.76,1.8205
            m5d.12xlarge,192 GiB,48,2 x 900 NVMe SSD,10 Gigabit,2.712,1979.7600000000002,0.8946
            m5n.4xlarge,64 GiB,16,EBS only,Up to 25 Gigabit,0.952,694.9599999999999,0.4124
            m5.4xlarge,64 GiB,16,EBS only,Up to 10 Gigabit,0.768,560.64,0.3203
            m5.2xlarge,32 GiB,8,EBS only,Up to 10 Gigabit,0.384,280.32,0.1284
            m5dn.16xlarge,256 GiB,64,4 x 600 NVMe SSD,75 Gigabit,4.352,3176.96,1.1696
            m5ad.12xlarge,192 GiB,48,2 x 900 NVMe SSD,10 Gigabit,2.76,2014.8,NA
            m5.4xlarge,64 GiB,16,EBS only,Up to 10 Gigabit,0.856,624.88,NA
            m5n.metal,384 GiB,96,EBS only,100 Gigabit,6.384,4660.320000000001,NA
            m5n.xlarge,16 GiB,4,EBS only,Up to 25 Gigabit,0.266,194.18,NA
            m5a.large,8 GiB,2,EBS only,Up to 10 Gigabit,0.096,70.08,NA
            m5zn.2xlarge,32 GiB,8,EBS only,Up to 25 Gigabit,0.7364,537.572,NA
            m5.24xlarge,384 GiB,96,EBS only,25 Gigabit,5.136,3749.28,NA
            m5d.12xlarge,192 GiB,48,2 x 900 NVMe SSD,10 Gigabit,3.024,2207.52,NA
            m5n.2xlarge,32 GiB,8,EBS only,Up to 25 Gigabit,0.532,388.36,NA
            m5ad.16xlarge,256 GiB,64,4 x 600 NVMe SSD,12 Gigabit,3.68,2686.4,NA
            m5d.24xlarge,384 GiB,96,4 x 900 NVMe SSD,25 Gigabit,6.048,4415.04,NA
            m5ad.4xlarge,64 GiB,16,2 x 300 NVMe SSD,Up to 10 Gigabit,0.92,671.6,NA
            m5zn.12xlarge,192 GiB,48,EBS only,100 Gigabit,4.4184,3225.4320000000002,NA
            m5.16xlarge,256 GiB,64,EBS only,20 Gigabit,3.424,2499.52,NA
            m5n.8xlarge,128 GiB,32,EBS only,25 Gigabit,2.128,1553.44,NA
            m5.12xlarge,192 GiB,48,EBS only,10 Gigabit,2.568,1874.64,NA
            m5n.4xlarge,64 GiB,16,EBS only,Up to 25 Gigabit,1.064,776.72,NA
            m5d.16xlarge,256 GiB,64,4 x 600 NVMe SSD,20 Gigabit,4.032,2943.36,NA
            m5a.16xlarge,256 GiB,64,EBS only,12 Gigabit,3.072,2242.56,NA
            m5zn.xlarge,16 GiB,4,EBS only,Up to 25 Gigabit,0.3682,268.786,NA
            m5dn.xlarge,16 GiB,4,1 x 150 NVMe SSD,Up to 25 Gigabit,0.304,221.92,NA
            m5dn.metal,384 GiB,96,4 x 900 NVMe SSD,100 Gigabit,7.296,5326.08,NA
            m5n.16xlarge,256 GiB,64,EBS only,75 Gigabit,4.256,3106.88,NA
            m5a.8xlarge,128 GiB,32,EBS only,Up to 10 Gigabit,1.536,1121.28,NA
            m5dn.16xlarge,256 GiB,64,4 x 600 NVMe SSD,75 Gigabit,4.864,3550.72,NA
            m5dn.4xlarge,64 GiB,16,2 x 300 NVMe SSD,Up to 25 Gigabit,1.216,887.68,NA
            m5.8xlarge,128 GiB,32,EBS only,10 Gigabit,1.712,1249.76,NA
            m5.xlarge,16 GiB,4,EBS only,Up to 10 Gigabit,0.214,156.22,NA
            m5a.2xlarge,32 GiB,8,EBS only,Up to 10 Gigabit,0.384,280.32,NA
            m5zn.6xlarge,96 GiB,24,EBS only,50 Gigabit,2.2092,1612.7160000000001,NA
            m5.metal,384 GiB,96,EBS only,25 Gigabit,5.136,3749.28,NA
            m5ad.large,8 GiB,2,1 x 75 NVMe SSD,Up to 10 Gigabit,0.115,83.95,NA
            m5dn.large,8 GiB,2,1 x 75 NVMe SSD,Up to 25 Gigabit,0.152,110.96,NA
            m5dn.12xlarge,192 GiB,48,2 x 900 GB NVMe SSD,50 Gigabit,3.648,2663.04,NA
            m5zn.large,8 GiB,2,EBS only,Up to 25 Gigabit,0.1841,134.393,NA
            m5dn.2xlarge,32 GiB,8,1 x 300 NVMe SSD,Up to 25 Gigabit,0.608,443.84,NA
            m5.2xlarge,32 GiB,8,EBS only,Up to 10 Gigabit,0.428,312.44,NA
            m5ad.24xlarge,384 GiB,96,4 x 900 NVMe SSD,20 Gigabit,5.52,4029.6,NA
            m5d.large,8 GiB,2,1 x 75 NVMe SSD,Up to 10 Gigabit,0.126,91.98,NA
            m5ad.8xlarge,128 GiB,32,2 x 600 NVMe SSD,Up to 10 Gigabit,1.84,1343.2,NA
            m5dn.24xlarge,384 GiB,96,4 x 900 NVMe SSD,100 Gigabit,7.296,5326.08,NA
            m5d.4xlarge,64 GiB,16,2 x 300 NVMe SSD,Up to 10 Gigabit,1.008,735.84,NA
            m5ad.xlarge,16 GiB,4,1 x 150 NVMe SSD,Up to 10 Gigabit,0.23,167.9,NA
            m5d.metal,384 GiB,96,4 x 900 NVMe SSD,25 Gigabit,6.048,4415.04,NA
            m5d.2xlarge,32 GiB,8,1 x 300 NVMe SSD,Up to 10 Gigabit,0.504,367.92,NA
            m5a.xlarge,16 GiB,4,EBS only,Up to 10 Gigabit,0.192,140.16,NA
            m5dn.8xlarge,128 GiB,32,2 x 600 NVMe SSD,25 Gigabit,2.432,1775.36,NA
            m5n.12xlarge,192 GiB,48,EBS only,50 Gigabit,3.192,2330.1600000000003,NA
            m5d.8xlarge,128 GiB,32,2 x 600 NVMe SSD,10 Gigabit,2.016,1471.68,NA
            m5d.xlarge,16 GiB,4,1 x 150 NVMe SSD,Up to 10 Gigabit,0.252,183.96,NA
            m5zn.metal,192 GiB,48,EBS only,100 Gigabit,4.4184,3225.4320000000002,NA
            m5.large,8 GiB,2,EBS only,Up to 10 Gigabit,0.107,78.11,NA
            m5a.24xlarge,384 GiB,96,EBS only,20 Gigabit,4.608,3363.8399999999997,NA
            m5zn.3xlarge,48 GiB,12,EBS only,Up to 25 Gigabit,1.1046,806.3580000000001,NA
            m5n.24xlarge,384 GiB,96,EBS only,100 Gigabit,6.384,4660.320000000001,NA
            m5ad.2xlarge,32 GiB,8,1 x 300 NVMe SSD,Up to 10 Gigabit,0.46,335.8,NA
            m5a.4xlarge,64 GiB,16,EBS only,Up to 10 Gigabit,0.768,560.64,NA
            m5a.12xlarge,192 GiB,48,EBS only,10 Gigabit,2.304,1681.9199999999998,NA
            m5n.large,8 GiB,2,EBS only,Up to 25 Gigabit,0.133,97.09,NA
            m6i.2xlarge,32 GiB,8,EBS only,Up to 12500 Megabit,0.384,280.32,NA
            m6g.large,8 GiB,2,EBS only,Up to 10 Gigabit,0.077,56.21,NA
            m6gd.xlarge,16 GiB,4,1 x 237 NVMe SSD,Up to 10 Gigabit,0.1808,131.98399999999998,NA
            m6gd.12xlarge,192 GiB,48,2 x 1425 NVMe SSD,20 Gigabit,2.1696,1583.808,NA
            m6id.32xlarge,512 GiB,128,4 x 1900 SSD,50000 Megabit,7.5936,5543.328,NA
            m6g.4xlarge,64 GiB,16,EBS only,Up to 10 Gigabit,0.616,449.68,NA
            m6i.large,8 GiB,2,EBS only,Up to 12500 Megabit,0.096,70.08,NA
            m6id.4xlarge,64 GiB,16,1 x 950 SSD,Up to 12500 Megabit,0.9492,692.916,NA
            m6id.large,8 GiB,2,1 x 118 SSD,Up to 12500 Megabit,0.11865,86.6145,NA
            m6g.medium,4 GiB,1,EBS only,Up to 10 Gigabit,0.0385,28.105,NA
            m6i.xlarge,16 GiB,4,EBS only,Up to 12500 Megabit,0.192,140.16,NA
            m6id.metal,512 GiB,128,4 x 1900 SSD,50000 Megabit,7.5936,5543.328,NA
            m6a.xlarge,16 GiB,4,EBS only,Up to 12500 Megabit,0.1728,126.144,NA
            m6a.32xlarge,512 GiB,128,EBS only,50000 Megabit,5.5296,4036.608,NA
            m6g.8xlarge,128 GiB,32,EBS only,10 Gigabit,1.232,899.36,NA
            m6a.16xlarge,256 GiB,64,EBS only,25000 Megabit,2.7648,2018.304,NA
            m6i.24xlarge,384 GiB,96,EBS only,37500 Megabit,4.608,3363.8399999999997,NA
            m6g.metal,256 GiB,64,EBS only,25 Gigabit,2.464,1798.72,NA
            m6i.12xlarge,192 GiB,48,EBS only,18750 Megabit,2.304,1681.9199999999998,NA
            m6a.8xlarge,128 GiB,32,EBS only,12500 Megabit,1.3824,1009.152,NA
            m6g.16xlarge,256 GiB,64,EBS only,25 Gigabit,2.464,1798.72,NA
            m6i.8xlarge,128 GiB,32,EBS only,12500 Megabit,1.536,1121.28,NA
            m6gd.8xlarge,128 GiB,32,1 x 1900 NVMe SSD,10 Gigabit,1.4464,1055.8719999999998,NA
            m6gd.16xlarge,256 GiB,64,2 x 1900 NVMe SSD,25 Gigabit,2.8928,2111.7439999999997,NA
            m6i.16xlarge,256 GiB,64,EBS only,25000 Megabit,3.072,2242.56,NA
            m6id.12xlarge,192 GiB,48,2 x 1425 SSD,18750 Megabit,2.8476,2078.748,NA
            m6gd.large,8 GiB,2,1 x 118 NVMe SSD,Up to 10 Gigabit,0.0904,65.99199999999999,NA
            m6a.large,8 GiB,2,EBS only,Up to 12500 Megabit,0.0864,63.072,NA
            m6i.4xlarge,64 GiB,16,EBS only,Up to 12500 Megabit,0.768,560.64,NA
            m6g.12xlarge,192 GiB,48,EBS only,12 Gigabit,1.848,1349.04,NA
            m6id.16xlarge,256 GiB,64,2 x 1900 SSD,25000 Megabit,3.7968,2771.664,NA
            m6id.2xlarge,32 GiB,8,1 x 474 SSD,Up to 12500 Megabit,0.4746,346.458,NA
            m6a.2xlarge,32 GiB,8,EBS only,Up to 12500 Megabit,0.3456,252.288,NA
            m6id.8xlarge,128 GiB,32,1 x 1900 SSD,12500 Megabit,1.8984,1385.832,NA
            m6g.xlarge,16 GiB,4,EBS only,Up to 10 Gigabit,0.154,112.42,NA
            m6gd.2xlarge,32 GiB,8,1 x 475 NVMe SSD,Up to 10 Gigabit,0.3616,263.96799999999996,NA
            m6a.24xlarge,384 GiB,96,EBS only,37500 Megabit,4.1472,3027.4559999999997,NA
            m6a.metal,768 GiB,192,EBS only,50000 Megabit,8.2944,6054.911999999999,NA
            m6g.2xlarge,32 GiB,8,EBS only,Up to 10 Gigabit,0.308,224.84,NA
            m6i.metal,512 GiB,128,EBS only,50000 Megabit,6.144,4485.12,NA
            m6id.24xlarge,384 GiB,96,4 x 1425 SSD,37500 Megabit,5.6952,4157.496,NA
            m6gd.medium,4 GiB,1,1 x 59 NVMe SSD,Up to 10 Gigabit,0.0452,32.995999999999995,NA
            m6gd.4xlarge,64 GiB,16,1 x 950 NVMe SSD,Up to 10 Gigabit,0.7232,527.9359999999999,NA
            m6id.xlarge,16 GiB,4,1 x 237 SSD,Up to 12500 Megabit,0.2373,173.229,NA
            m6a.4xlarge,64 GiB,16,EBS only,Up to 12500 Megabit,0.6912,504.576,NA
            m6i.32xlarge,512 GiB,128,EBS only,50000 Megabit,6.144,4485.12,NA
            m6gd.metal,256 GiB,64,2 x 1900 NVMe SSD,25 Gigabit,2.8928,2111.7439999999997,NA
            m6a.12xlarge,192 GiB,48,EBS only,18750 Megabit,2.0736,1513.7279999999998,NA
            m6a.48xlarge,768 GiB,192,EBS only,50000 Megabit,8.2944,6054.911999999999,NA
            m6i.16xlarge,256 GiB,64,EBS only,25000 Megabit,3.072,2242.56,1.1719
            m6a.4xlarge,64 GiB,16,EBS only,Up to 12500 Megabit,0.6912,504.576,0.2984
            m6g.2xlarge,32 GiB,8,EBS only,Up to 10 Gigabit,0.308,224.84,0.1188
            m6a.32xlarge,512 GiB,128,EBS only,50000 Megabit,5.5296,4036.608,1.4943
            m6g.xlarge,16 GiB,4,EBS only,Up to 10 Gigabit,0.154,112.42,0.0552
            m6id.16xlarge,256 GiB,64,2 x 1900 SSD,25000 Megabit,3.7968,2771.664,0.9235
            m6a.8xlarge,128 GiB,32,EBS only,12500 Megabit,1.3824,1009.152,0.6002
            m6i.large,8 GiB,2,EBS only,Up to 12500 Megabit,0.096,70.08,0.0321
            m6gd.large,8 GiB,2,1 x 118 NVMe SSD,Up to 10 Gigabit,0.0904,65.99199999999999,0.0339
            m6i.12xlarge,192 GiB,48,EBS only,18750 Megabit,2.304,1681.9199999999998,0.8751
            m6a.12xlarge,192 GiB,48,EBS only,18750 Megabit,2.0736,1513.7279999999998,0.7225
            m6a.metal,768 GiB,192,EBS only,50000 Megabit,8.2944,6054.911999999999,2.0751
            m6g.8xlarge,128 GiB,32,EBS only,10 Gigabit,1.232,899.36,0.4282
            m6gd.metal,256 GiB,64,2 x 1900 NVMe SSD,25 Gigabit,2.8928,2111.7439999999997,1.1769
            m6g.16xlarge,256 GiB,64,EBS only,25 Gigabit,2.464,1798.72,0.7917
            m6id.24xlarge,384 GiB,96,4 x 1425 SSD,37500 Megabit,5.6952,4157.496,1.4859
            m6id.large,8 GiB,2,1 x 118 SSD,Up to 12500 Megabit,0.11865,86.6145,0.0409
            m6a.48xlarge,768 GiB,192,EBS only,50000 Megabit,8.2944,6054.911999999999,2.3006
            m6i.xlarge,16 GiB,4,EBS only,Up to 12500 Megabit,0.192,140.16,0.0652
            m6i.metal,512 GiB,128,EBS only,50000 Megabit,6.144,4485.12,2.0047
            m6i.32xlarge,512 GiB,128,EBS only,50000 Megabit,6.144,4485.12,1.9571
            m6g.medium,4 GiB,1,EBS only,Up to 10 Gigabit,0.0385,28.105,0.0145
            m6i.2xlarge,32 GiB,8,EBS only,Up to 12500 Megabit,0.384,280.32,0.1637
            m6id.4xlarge,64 GiB,16,1 x 950 SSD,Up to 12500 Megabit,0.9492,692.916,0.3222
            m6g.metal,256 GiB,64,EBS only,25 Gigabit,2.464,1798.72,0.7003
            m6id.2xlarge,32 GiB,8,1 x 474 SSD,Up to 12500 Megabit,0.4746,346.458,0.1467
            m6i.8xlarge,128 GiB,32,EBS only,12500 Megabit,1.536,1121.28,0.5605
            m6a.large,8 GiB,2,EBS only,Up to 12500 Megabit,0.0864,63.072,0.0357
            m6gd.medium,4 GiB,1,1 x 59 NVMe SSD,Up to 10 Gigabit,0.0452,32.995999999999995,0.0113
            m6gd.2xlarge,32 GiB,8,1 x 475 NVMe SSD,Up to 10 Gigabit,0.3616,263.96799999999996,0.1172
            m6g.4xlarge,64 GiB,16,EBS only,Up to 10 Gigabit,0.616,449.68,0.2471
            m6a.16xlarge,256 GiB,64,EBS only,25000 Megabit,2.7648,2018.304,1.0082
            m6id.32xlarge,512 GiB,128,4 x 1900 SSD,50000 Megabit,7.5936,5543.328,1.4723
            m6id.12xlarge,192 GiB,48,2 x 1425 SSD,18750 Megabit,2.8476,2078.748,0.6228
            m6id.xlarge,16 GiB,4,1 x 237 SSD,Up to 12500 Megabit,0.2373,173.229,0.0763
            m6a.xlarge,16 GiB,4,EBS only,Up to 12500 Megabit,0.1728,126.144,0.0586
            m6i.4xlarge,64 GiB,16,EBS only,Up to 12500 Megabit,0.768,560.64,0.2965
            m6i.24xlarge,384 GiB,96,EBS only,37500 Megabit,4.608,3363.8399999999997,1.8259
            m6gd.12xlarge,192 GiB,48,2 x 1425 NVMe SSD,20 Gigabit,2.1696,1583.808,0.8093
            m6gd.xlarge,16 GiB,4,1 x 237 NVMe SSD,Up to 10 Gigabit,0.1808,131.98399999999998,0.0649
            m6a.24xlarge,384 GiB,96,EBS only,37500 Megabit,4.1472,3027.4559999999997,1.1381
            m6id.8xlarge,128 GiB,32,1 x 1900 SSD,12500 Megabit,1.8984,1385.832,0.5822
            m6a.2xlarge,32 GiB,8,EBS only,Up to 12500 Megabit,0.3456,252.288,0.1443
            m6gd.8xlarge,128 GiB,32,1 x 1900 NVMe SSD,10 Gigabit,1.4464,1055.8719999999998,0.4124
            m6id.metal,512 GiB,128,4 x 1900 SSD,50000 Megabit,7.5936,5543.328,1.4192
            m6gd.4xlarge,64 GiB,16,1 x 950 NVMe SSD,Up to 10 Gigabit,0.7232,527.9359999999999,0.2494
            m6g.large,8 GiB,2,EBS only,Up to 10 Gigabit,0.077,56.21,0.0244
            m6gd.16xlarge,256 GiB,64,2 x 1900 NVMe SSD,25 Gigabit,2.8928,2111.7439999999997,0.8882
            m6g.12xlarge,192 GiB,48,EBS only,12 Gigabit,1.848,1349.04,0.6275
            m6a.2xlarge,32 GiB,8,EBS only,Up to 12500 Megabit,0.3852,281.19599999999997,NA
            m6id.xlarge,16 GiB,4,1 x 237 SSD,Up to 12500 Megabit,0.2646,193.15800000000002,NA
            m6id.24xlarge,384 GiB,96,4 x 1425 SSD,37500 Megabit,6.3504,4635.7919999999995,NA
            m6i.large,8 GiB,2,EBS only,Up to 12500 Megabit,0.107,78.11,NA
            m6gd.2xlarge,32 GiB,8,1 x 475 NVMe SSD,Up to 10 Gigabit,0.4032,294.336,NA
            m6g.2xlarge,32 GiB,8,EBS only,Up to 10 Gigabit,0.344,251.11999999999998,NA
            m6id.12xlarge,192 GiB,48,2 x 1425 SSD,18750 Megabit,3.1752,2317.8959999999997,NA
            m6i.4xlarge,64 GiB,16,EBS only,Up to 12500 Megabit,0.856,624.88,NA
            m6i.32xlarge,512 GiB,128,EBS only,50000 Megabit,6.848,4999.04,NA
            m6i.24xlarge,384 GiB,96,EBS only,37500 Megabit,5.136,3749.28,NA
            m6gd.medium,4 GiB,1,1 x 59 NVMe SSD,Up to 10 Gigabit,0.0504,36.792,NA
            m6id.large,8 GiB,2,1 x 118 SSD,Up to 12500 Megabit,0.1323,96.57900000000001,NA
            m6g.16xlarge,256 GiB,64,EBS only,25 Gigabit,2.752,2008.9599999999998,NA
            m6gd.16xlarge,256 GiB,64,2 x 1900 NVMe SSD,25 Gigabit,3.2256,2354.688,NA
            m6a.32xlarge,512 GiB,128,EBS only,50000 Megabit,6.1632,4499.1359999999995,NA
            m6a.large,8 GiB,2,EBS only,Up to 12500 Megabit,0.0963,70.29899999999999,NA
            m6g.4xlarge,64 GiB,16,EBS only,Up to 10 Gigabit,0.688,502.23999999999995,NA
            m6gd.12xlarge,192 GiB,48,2 x 1425 NVMe SSD,20 Gigabit,2.4192,1766.016,NA
            m6i.8xlarge,128 GiB,32,EBS only,12500 Megabit,1.712,1249.76,NA
            m6g.12xlarge,192 GiB,48,EBS only,12 Gigabit,2.064,1506.72,NA
            m6g.large,8 GiB,2,EBS only,Up to 10 Gigabit,0.086,62.779999999999994,NA
            m6a.24xlarge,384 GiB,96,EBS only,37500 Megabit,4.6224,3374.352,NA
            m6a.4xlarge,64 GiB,16,EBS only,Up to 12500 Megabit,0.7704,562.3919999999999,NA
            m6g.xlarge,16 GiB,4,EBS only,Up to 10 Gigabit,0.172,125.55999999999999,NA
            m6gd.metal,256 GiB,64,2 x 1900 NVMe SSD,25 Gigabit,3.2256,2354.688,NA
            m6gd.8xlarge,128 GiB,32,1 x 1900 NVMe SSD,10 Gigabit,1.6128,1177.344,NA
            m6a.8xlarge,128 GiB,32,EBS only,12500 Megabit,1.5408,1124.7839999999999,NA
            m6i.16xlarge,256 GiB,64,EBS only,25000 Megabit,3.424,2499.52,NA
            m6g.medium,4 GiB,1,EBS only,Up to 10 Gigabit,0.043,31.389999999999997,NA
            m6g.8xlarge,128 GiB,32,EBS only,10 Gigabit,1.376,1004.4799999999999,NA
            m6id.4xlarge,64 GiB,16,1 x 950 SSD,Up to 12500 Megabit,1.0584,772.6320000000001,NA
            m6gd.large,8 GiB,2,1 x 118 NVMe SSD,Up to 10 Gigabit,0.1008,73.584,NA
            m6id.metal,512 GiB,128,4 x 1900 SSD,50000 Megabit,8.4672,6181.0560000000005,NA
            m6a.12xlarge,192 GiB,48,EBS only,18750 Megabit,2.3112,1687.176,NA
            m6gd.xlarge,16 GiB,4,1 x 237 NVMe SSD,Up to 10 Gigabit,0.2016,147.168,NA
            m6id.2xlarge,32 GiB,8,1 x 474 SSD,Up to 12500 Megabit,0.5292,386.31600000000003,NA
            m6a.16xlarge,256 GiB,64,EBS only,25000 Megabit,3.0816,2249.5679999999998,NA
            m6i.metal,512 GiB,128,EBS only,50000 Megabit,6.848,4999.04,NA
            m6id.32xlarge,512 GiB,128,4 x 1900 SSD,50000 Megabit,8.4672,6181.0560000000005,NA
            m6i.12xlarge,192 GiB,48,EBS only,18750 Megabit,2.568,1874.64,NA
            m6a.metal,768 GiB,192,EBS only,50000 Megabit,9.2448,6748.704,NA
            m6i.xlarge,16 GiB,4,EBS only,Up to 12500 Megabit,0.214,156.22,NA
            m6g.metal,256 GiB,64,EBS only,25 Gigabit,2.752,2008.9599999999998,NA
            m6a.48xlarge,768 GiB,192,EBS only,50000 Megabit,9.2448,6748.704,NA
            m6i.2xlarge,32 GiB,8,EBS only,Up to 12500 Megabit,0.428,312.44,NA
            m6a.xlarge,16 GiB,4,EBS only,Up to 12500 Megabit,0.1926,140.59799999999998,NA
            m6gd.4xlarge,64 GiB,16,1 x 950 NVMe SSD,Up to 10 Gigabit,0.8064,588.672,NA
            m6id.16xlarge,256 GiB,64,2 x 1900 SSD,25000 Megabit,4.2336,3090.5280000000002,NA
            m6id.8xlarge,128 GiB,32,1 x 1900 SSD,12500 Megabit,2.1168,1545.2640000000001,NA

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

            ou

            ```sh
            jq -r '.Prices[] |keys | join(",")' out/tiny-jq.json | head -n 1 > ./out/tiny-jq.csv && jq -r '.Prices[] | join(",")' out/tiny-jq.json >> ./out/tiny-jq.csv
            ```

            On peut voir que le fichier s'ouvre donc bien sur LibreOffice Calc:

            ![cloud-td1-excel](./src/TD1/cloud-td1-excel.png)