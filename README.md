# temperature-processor

## Optional Environment Variables

- INFLUXDB_URL: http(s)://influxdbhost:8086
- INFLUXDB_TOKEN: InfluxDB token
- INFLUXDB_ORG: InfluxDB organization
- INFLUXDB_BUCKET: InfluxDB bucket
- TEMPERATURE_PORT: Port Temperature-Sensor to listen on

## Testing

1. `pip install -r requirements.txt`
1. `docker-compose up -d`
1. Be in the root directory of the project
1. `pytest`

## Deploying

1. `docker run -it -e INFLUXDB_URL=http://foo -e INFLUXDB_TOKEN=bar -e INFLUXDB_ORG=somewhere -e TEMPERATURE_PORT=1111 -p 8080:1111 temperature-processor`

## Building

1. `docker build -t temperature-processor . -f build/Dockerfile`
