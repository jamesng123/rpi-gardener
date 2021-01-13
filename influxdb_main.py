from pigpio_dht import DHT22
from datetime import datetime
import time, sys
import plants
from LED import LED
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
# You can generate a Token from the "Tokens Tab" in the UI
token = "9xgguPB02fOZksxpN0opaQbQmPdiQ_-vHwIO-RGQaPeHjewTmCmg1Yup6IfBpr_dtFjxAllLXiwLarD_9AQNkA=="
org = "rpi-garden"
bucket = "garden"
client = InfluxDBClient(url="http://192.168.1.197:8086", token=token)
write_api = client.write_api(write_options=SYNCHRONOUS)


def main(plant: plants.Plant, dht_sensor: DHT22):
    while True:
        try:
            result = dht_sensor.read()
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            f_data = f"Current Time: {current_time} - Temp: {result['temp_c']} - Humidity: {result['humidity']}\n"
            if result['valid'] == True:
                print(f_data)
                temp_data = f"temperature,plant={plant.name} used_percent={result['temp_c']}"
                write_api.write(bucket, org, temp_data)
                humidity_data = f"humidity,plant={plant.name} used_percent={result['humidity']}"
                write_api.write(bucket, org, humidity_data)
                plant.check_temperature(result['temp_c'])

        except KeyboardInterrupt:
            LED.turn_off_all_leds()
            sys.exit(0)

if __name__ == '__main__':
    
    basil = plants.Plant("Basil", humidity=(15, 25), temperature=(15, 25), moisture=(0, 100))
    sensor = DHT22(gpio=4) # Uses BCM numbering

    main(basil, sensor)