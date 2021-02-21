from pigpio_dht import DHT22
from datetime import datetime
import time, sys
from plants import Plant
from LED import LED
from moisture_sensor import MoistureSensor

def main(plant: Plant):
    while True:
        try:
            result = plant.temperature_sensor.read()
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            f_data = f"Current Time: {current_time} - Temp: {result['temp_c']} - Humidity: {result['humidity']}\n"
            if result['valid'] == True:
                print(f_data)
                with import RPi.GPIO as GPIO

class MoistureSensor():

    def __init__(self, gpio):
        self.gpio = gpio

        # Initialse the GPIO pins and LEDs
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

        GPIO.setup(self.gpio, GPIO.IN)

    def get_moisture_state(self):

        """ Returns True if the plant needs water and False if not """

        if GPIO.input(self.gpio):
            return True
        else:
            return Falseopen("data.txt", "a") as f:
                    f.write(f_data)
                plant.check_temperature(result['temp_c'])
                plant.check_moisture()
                time.sleep(10)
        
        except KeyboardInterrupt:
            LED.turn_off_all_leds()
            sys.exit(0)

if __name__ == '__main__':
    
    schefflera = Plant("schefflera", 
                        humidity=(50, 90), 
                        temperature=(12, 22), 
                        moisture_sensor=MoistureSensor(26), 
                        temperature_sensor=DHT22(4), 
                        green=LED(18, "green"), 
                        blue=LED(24, "green"), 
                        red=LED(23, "red"))

    main(schefflera)
