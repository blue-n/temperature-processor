from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS

myBucket = "sensor"
influxClient = InfluxDBClient(url="http://localhost:8086", token="initadmintoken", org="admin")
influxWrite = influxClient.write_api(write_options=SYNCHRONOUS)
influxRead = influxClient.query_api()