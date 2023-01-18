import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS

bucket = "parking"
org = "iut-students"
token = "C-y-3-UfAZCL6oqxq5vCorwdbI2_XKv7BkMjTRURe_dXGcALUOCrzVqrt0aHpONaPJ6UlGYUBsFJInMIJ5n1NA=="
# Store the URL of your InfluxDB instance
url = "http://188.166.151.235/"

client = influxdb_client.InfluxDBClient(
    url=url,
    token=token,
    org=org
)

write_api = client.write_api(write_options=SYNCHRONOUS)

with open("./in/stats/csv/FR_MTP_GARE.CSV") as fin:
  fin = fin.readlines()
  

p = influxdb_client.Point("").tag("location", "Prague").field("temperature", 25.3)
write_api.write(bucket=bucket, org=org, record=p)
