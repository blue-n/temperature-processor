import os
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS

url = os.getenv("INFLUXDB_URL", "http://localhost:8086")
token = os.getenv("INFLUXDB_TOKEN", "initadmintoken")
org = os.getenv("INFLUXDB_ORG", "admin")
myBucket = os.getenv("INFLUXDB_BUCKET", "sensor")

print("InfluxDB Bucket: ", myBucket)
print("InfluxDB Org: ", org)
print("InfluxDB Token: ", token)
print("InfluxDB URL: ", url)

influxClient = InfluxDBClient(url=url, token=token, org=org)
influxWrite = influxClient.write_api(write_options=SYNCHRONOUS)
influxRead = influxClient.query_api()
