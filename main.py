from pigpio_dht import DHT22
from datetime import datetime
import time, sys
from plants import Plant
from LED import LED

def main(plant: Plant):
    while True:
        try:
            result = plant.sensor.read()
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
            LED.turn_off_all_leds()
            sys.exit(0)

if __name__ == '__main__':
    
    basil = Plant("Basil", humidity=(15, 25), temperature=(15, 26.5), moisture=True, sensor=DHT22(4))

    main(basil)
