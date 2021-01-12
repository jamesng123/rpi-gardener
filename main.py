# NOTE: The import has a _ not - in the module name.
from pigpio_dht import DHT22
from datetime import datetime
import time
import plants
import LED
import sys


gpio = 4 # BCM Numbering

sensor = DHT22(gpio)

def main(plant: plants.Plant):
    while True:
        try:
            result = sensor.read()
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            f_data = f"Current Time: {current_time} - Temp: {result['temp_c']} - Humidity: {result['humidity']}\n"
            if result['valid'] == True:
                print(f_data)
                with open("data.txt", "a") as f:
                    f.write(f_data)            
                plant.check_temperature(result['temp_c'])
                time.sleep(10)
        except KeyboardInterrupt:
            LED.LED.turn_off_all_leds()
            sys.exit(0)

if __name__ == '__main__':
    
    basil = plants.Plant("Basil", humidity=(15, 25), temperature=(15, 26.5), moisture=(0, 100))

    main(basil)


# while True:
#     try:
#         result = sensor.read()
#         now = datetime.now()
#         current_time = now.strftime("%H:%M:%S")
#         f_data = f"Current Time: {current_time} - Temp: {result['temp_c']} - Humidity: {result['humidity']}\n"
#         if result['valid'] == True:
#             print(f_data)
#             with open("data.txt", "a") as f:
#                 f.write(f_data)            
#             basil.check_temperature(result['temp_c'])
#             time.sleep(10)
#     except KeyboardInterrupt:
#         LED.LED.turn_off_all_leds()
#         sys.exit(0)

# When something has gone wrong - flash the LED
# When it's fine, don't flash
