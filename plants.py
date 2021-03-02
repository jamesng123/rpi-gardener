import time
import RPi.GPIO as GPIO
from LED import LED
from water_pump import WaterPump
from pigpio_dht import DHT22
from moisture_sensor import MoistureSensor


class Plant():

    def __init__(self, name: str, humidity: tuple, temperature: tuple, moisture_sensor: MoistureSensor, temperature_sensor: DHT22, green: LED, blue: LED, red: LED):
        self.name = name
        self.humidity = humidity
        self.temperature = temperature
        self.moisture_sensor = moisture_sensor
        self.temperature_sensor = temperature_sensor
        self.green = green
        self.red = red
        self.blue = blue

        assert temperature[0] < temperature[1], "The lower temperature threshold comes first"

        assert humidity[0] < humidity[1], "The lower humidity threshold comes first"

    def check_temperature(self, current_temp: float):
        """ Checks the temperature of the plant. Performs actions to bring the temperature within a specified range """

        if self.temperature[0] <= current_temp <= self.temperature[1]:

            # This is the desired state
            print("this is desired")

            # LED.turn_off_all_leds()
            # self.green.turn_on()

        elif current_temp < self.temperature[0]:

            print("this is too cold, the range is: ", self.temperature)
            self.heat_up(current_temp)
            LED.turn_off_all_leds()
            self.blue.turn_on()

        else:
            print("this is too hot, the range is: ", self.temperature)
            self.cool_down(current_temp)
            LED.turn_off_all_leds()
            self.red.turn_on()

    def check_humidity(self, current_humidity: float):
        """ Checks the humidity of the plant. Performs actions to bring the humidity within a specified range """

        if self.humidity[0] <= current_humidity <= self.humidity[1]:
            pass  # This is the desired state
        elif current_humidity < self.humidity[0]:
            # TODO Implement logic for increasing the humidity
            pass
        else:
            # TODO Implement logic for decreasing the humidity
            pass

    def check_moisture(self):
        """ Checks the moisture of the plant. Performs actions to bring the moisture within a specified range """

        if not self.moisture_sensor.get_moisture_state():
            print("No water needed, got plenty")
            LED.turn_off_all_leds()
            self.green.turn_on()
        else:
            self.water()

    def heat_up(self, current_temperature: float):
        """ Increases the temperature for the plant """

        # TODO Implement logic for heating up
        print("heating up....")
        # while current_temperature < self.temperature[0]:
        #     current_temperature += 1
        #     print(current_temperature)
        #     time.sleep(1)
        #
        # print("warmed!")

    def cool_down(self, current_temperature: float):
        """ Decreases the temperature for the plant """

        # TODO Implement logic for cooling down
        print("cooling down....")
        # while current_temperature > self.temperature[1]:
        #     current_temperature -= 1
        #     print(current_temperature)
        #     time.sleep(1)
        # print("cooled!")

    def water(self):
        """ Releases water for the plant """
        print("Water")
        # TODO Implement logic for controlling the water pump
        pass
